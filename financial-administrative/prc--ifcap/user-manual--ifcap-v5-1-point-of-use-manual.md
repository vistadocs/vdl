---
title: IFCAP Version 5.1 Point of Use Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Point of Use Manual
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
description: Integrated Funds Distribution,Control Point Activity, Accountingand Procurement(IFCAP)
audience: 
keywords: 
  - strong
  - station
  - inventory
  - supply
  - table
  - point
  - style
  - width
  - order
  - secondary
page_count: 0
word_count: 32300
section_count: 36
table_count: 5
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2025
revision_count: 3
revision_newest: 06/07/11
revision_oldest: 12/29/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1pou_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1pou_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

![](ifcap-version-5-1-point-of-use-manual/001.png)

Integrated Funds Distribution,Control Point Activity, Accountingand Procurement(IFCAP)

Generic Inventory Package (GIP)

######### POINT OF USE

######### MANUAL

November 2025

Office of Information and Technology (OI&T)

Management, Enrollment, and Financial Systems

Revision History

|              |                                                                                             |                 |                  |
|--------------|---------------------------------------------------------------------------------------------|-----------------|------------------|
| Date         | Description (Patch \# if applicable.)                                                       | Project Manager | Technical Writer |
| October 2025 | Patch PRC\*5.1\*244 Add ABC Classification code to Inventory Points                         | REDACTED        | REDACTED         |
| October 2011 | Patch PRC\*5.1\*158 Modification of title for IFCAP VA Form 1358. See page [99](#glossary). | REDACTED        | REDACTED         |
| 06/07/11     | Patch PRC\*5.1\*142 - Print Transaction Register – p. [47-49](#transaction-register-report) | REDACTED        | REDACTED         |
| 12/29/04     | Updated to comply with SOP 192-352 Displaying Sensitive Data.                               |                 | REDACTED         |
| 12/29/04     | Pdf file checked for accessibility to readers with disabilities.                            |                 | REDACTED         |
|              |                                                                                             |                 |                  |

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [# Overview](#overview)
  - [“What is Point of Use?”](#what-is-point-of-use)
  - [“What can Point of Use do for us?”](#what-can-point-of-use-do-for-us)
- [# The “Revised” GIP](#the-revised-gip)
  - [Item Deletion](#item-deletion)
  - [Vendor Data and Conversion Factors](#vendor-data-and-conversion-factors)
  - [Editing the Item Short Description](#editing-the-item-short-description)
    - [At the Primary:](#at-the-primary)
    - [At the Secondary:](#at-the-secondary)
  - [Standard Reorder Point](#standard-reorder-point)
  - [Multiple Sources for a Secondary Inventory Point](#multiple-sources-for-a-secondary-inventory-point)
  - [Usage Demand Item Report](#usage-demand-item-report)
  - [Order Form](#order-form)
  - [Scheduling the Autogeneration of Distribution Orders](#scheduling-the-autogeneration-of-distribution-orders)
- [# # The ‘Interface-able’ GIP](#the-interface-able-gip)
  - [The Interface – Real time, but Queued](#the-interface-real-time-but-queued)
  - [Information Sent to the Supply Station from GIP](#information-sent-to-the-supply-station-from-gip)
    - [Regular Distribution Orders.](#regular-distribution-orders)
    - [Item Information (Short description, Normal, Standard Reorder, and Emergency Levels, Unit of Issue, Conversion Factor, and Last Cost).](#item-information-short-description-normal-standard-reorder-and-emergency-levels-unit-of-issue-conversion-factor-and-last-cost)
    - [Quantity on Hand (QOH) Query.](#quantity-on-hand-qoh-query)
  - [Information Sent to GIP from the Supply Station](#information-sent-to-gip-from-the-supply-station)
    - [Restocking.](#restocking)
    - [Item Activity.](#item-activity)
    - [Quantity on Hand (QOH) Response.](#quantity-on-hand-qoh-response)
  - [“Rules”](#rules)
    - [Linking a secondary inventory point with an automated supply cabinet](#linking-a-secondary-inventory-point-with-an-automated-supply-cabinet)
    - [Identifying the secondary inventory point items as items stored in the supply station](#identifying-the-secondary-inventory-point-items-as-items-stored-in-the-supply-station)
    - [Creating distribution orders for the supply station](#creating-distribution-orders-for-the-supply-station)
    - [Processing distribution orders for the supply station](#processing-distribution-orders-for-the-supply-station)
    - [Overriding the interface](#overriding-the-interface)
- [# New and Modified Functionality](#new-and-modified-functionality)
  - [Options for Inventory Points and Their Settings](#options-for-inventory-points-and-their-settings)
    - [Assigning a Supply Station Provider to a Secondary Inventory Point](#assigning-a-supply-station-provider-to-a-secondary-inventory-point)
    - [Item Description Default in the Secondary Inventory Point](#item-description-default-in-the-secondary-inventory-point)
    - [Editing the Item Description at the Primary Inventory Point](#editing-the-item-description-at-the-primary-inventory-point)
    - [Inventory Point Names](#inventory-point-names)
    - [Inactivating Inventory Points](#inactivating-inventory-points)
    - [Converting Secondary Inventory Points to Primary Inventory Points](#converting-secondary-inventory-points-to-primary-inventory-points)
    - [Adding Distribution Points to a Primary Inventory Point](#adding-distribution-points-to-a-primary-inventory-point)
    - [Removing Supply Station Secondary Distribution Points](#removing-supply-station-secondary-distribution-points)
    - [If you need to unlink a secondary inventory point from a supply station, or link it to a different supply station, you will first be required to delete or post all outstanding distribution orders for that secondary.](#if-you-need-to-unlink-a-secondary-inventory-point-from-a-supply-station-or-link-it-to-a-different-supply-station-you-will-first-be-required-to-delete-or-post-all-outstanding-distribution-orders-for-that-secondary)
    - [Processor for Supply Station Transactions (Task Manager Option)](#processor-for-supply-station-transactions-task-manager-option)
    - [Updating Items on the Supply Station](#updating-items-on-the-supply-station)
    - [Options Concerning Inventory Point Supplies](#options-concerning-inventory-point-supplies)
    - [Normal Stock Level](#normal-stock-level)
    - [Editing a Secondary Inventory Point Item’s Conversion Factor](#editing-a-secondary-inventory-point-items-conversion-factor)
    - [Item Deletion at the Primary and Secondary Inventory Points](#item-deletion-at-the-primary-and-secondary-inventory-points)
    - [Order Form](#order-form-1)
    - [Querying the Supply Station for its Quantity on Hand](#querying-the-supply-station-for-its-quantity-on-hand)
  - [Options Concerning Distribution Orders](#options-concerning-distribution-orders)
    - [Regular Orders and Editing Order Type in Orders for Supply Station Secondaries](#regular-orders-and-editing-order-type-in-orders-for-supply-station-secondaries)
    - [Sending an Order to the Supply Station](#sending-an-order-to-the-supply-station)
    - [Removing the Supply Station Flag](#removing-the-supply-station-flag)
  - [Reports](#reports)
    - [Supply Station Quantity Discrepancy](#supply-station-quantity-discrepancy)
    - [Inventory Sales Report](#inventory-sales-report)
    - [Quantity Distribution Report](#quantity-distribution-report)
    - [Usage Demand Item Report](#usage-demand-item-report-1)
    - [Transaction Register Report](#transaction-register-report)
  - [Bulletins](#bulletins)
    - [Notification of Ordered Items without a Refill Amount](#notification-of-ordered-items-without-a-refill-amount)
    - [Notification of trouble with an HL7 Refill Transaction](#notification-of-trouble-with-an-hl7-refill-transaction)
    - [Notification of Error in HL7 Supply Station Activity Transaction](#notification-of-error-in-hl7-supply-station-activity-transaction)
    - [Notification of Inventory Mismatches between Systems](#notification-of-inventory-mismatches-between-systems)
    - [Notification of Rejection of HL7 On-Hand Transaction](#notification-of-rejection-of-hl7-on-hand-transaction)
    - [List of Differences in Item Name between GIP and the Supply Station](#list-of-differences-in-item-name-between-gip-and-the-supply-station)
    - [Notification of On-Hand Discrepancies found by a QOH Response](#notification-of-on-hand-discrepancies-found-by-a-qoh-response)
    - [Notification of Items in a Supply Station not in GIP](#notification-of-items-in-a-supply-station-not-in-gip)
  - [Other messages](#other-messages)
    - [Quantity Discrepancies Exist With The Supply Station.](#quantity-discrepancies-exist-with-the-supply-station)
- [This page intentionally left blank.](#this-page-intentionally-left-blank)
- [Setting your system up to use the supply station interface](#setting-your-system-up-to-use-the-supply-station-interface)
  - [Checklist for Network Administrator and IRM](#checklist-for-network-administrator-and-irm)
    - [### Applications](#applications)
    - [Event Drivers](#event-drivers)
    - [Links](#links)
    - [Check the System Manager and start the filers if none are running](#check-the-system-manager-and-start-the-filers-if-none-are-running)
    - [Remaining Tasks](#remaining-tasks)
  - [Checklist for the Secondary Inventory Points](#checklist-for-the-secondary-inventory-points)
  - [Checklist for the Supply Station Settings](#checklist-for-the-supply-station-settings)
  - [Other Recommendations](#other-recommendations)
    - [Start the GIP Transaction Processing Queue](#start-the-gip-transaction-processing-queue)
    - [Test the Interface](#test-the-interface)
    - [Ask the vendor about accessing information related to communications](#ask-the-vendor-about-accessing-information-related-to-communications)
  - [Appendix 1: Resolutions to Issues Raised by the Test Sites](#appendix-1-resolutions-to-issues-raised-by-the-test-sites)
  - [Appendix 2: HL7 Implementation for Point of Use](#appendix-2-hl7-implementation-for-point-of-use)
  - [Appendix 3: Point of Use HL7 Message Details](#appendix-3-point-of-use-hl7-message-details)
- [#### ZIM](#zim)
  - [#### #### The following 3 segments repeat. Each segment appears once for each item ordered.](#the-following-3-segments-repeat-each-segment-appears-once-for-each-item-ordered)
  - [#### MSA](#msa)
  - [#### ERR (optional)](#err-optional)
  - [#### QRD](#qrd)
  - [#### ORC](#orc)
  - [#### RXR](#rxr)
  - [## ## ## ## ## #### #### PID (optional)](#pid-optional)
  - [#### RXR](#rxr-1)
  - [#### RXR](#rxr-2)
- [Glossary](#glossary)

#### Purpose of the Point of Use Manual

The Point of Use Manual summarizes the functional changes made to the existing Generic Inventory Package (GIP) module of the Integrated Funds Distribution, Control Point Accounting And Procurement Package (IFCAP). It is meant to supplement, not replace, any existing User Manuals on GIP and will be useful to programmers, site managers, and IRM technical staff setting up or maintaining the point of use interface, and to all Acquisition & Materiel Management (A&MM) personnel utilizing GIP.

#### #### Reference Numbering System

This document uses a numbering system to organize topics into sections that show the reader how the topics relate. For example, section 1.3 means this is the main topic for the third section of Chapter 1. If there were two subsections to this topic, they would be numbered 1.3.1 and 1.3.2. A section numbered 2.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third topic of Chapter 2. This numbering system tool allows the reader to more easily follow the logic of sections that contain several subsections.

# # Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## “What is Point of Use?”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Point of Use refers to the point in the inventory cycle where supplies actually get used. For us, this point is essentially the area from which medical staff retrieve items for use in patient care. Historically, these areas were usually a small room with several shelves or a closet. GIP usually represents these closets as the secondary inventory points.

Today, there are companies providing automated cabinets to use in place of the old closets. These cabinets enable items to be tracked by requiring information to be entered before a user can gain access. The computer on the cabinet keeps a ledger of all activity at the cabinet and a running total of the inventory for every item. It is even feasible to track supplies to a given patient.

## “What can Point of Use do for us?”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Automation provides the following benefits:

\- better control over who obtains supplies

\- better control over the quantity and type of supplies obtained each time

\- less need to frequently inventory the supplies manually

\- the ability to reference information centrally

The end result of these benefits is better efficiency at a reduced cost.

This page intentionally left blank.

# # The “Revised” GIP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The items in the following section affect all users of GIP whether or not they are using a point of use interface.

## Item Deletion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Items will not be eligible for deletion from a primary or secondary inventory point if they are on the active distribution orders for that inventory point. Active orders are those that are not yet posted or deleted. The restriction was added to maintain integrity within the due-in and due-out counts and to avoid problems created when trying to post an order containing an item in one of the affected inventory points.

Item deletion affects many parts of the GIP package. In addition to intentionally modifying items within an inventory point, the package allows background deletions such as the automatic purge of inactive items during the auto-generation process or the option to delete all items on a secondary inventory point prior to copying the items from another inventory point.

## Vendor Data and Conversion Factors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vendor Data on an item in the Secondary Inventory Point cannot be modified when a distribution order containing that item is on a released order. The restriction adds more integrity to the due-in and due-outs generated by releasing orders. The conversion factor, part of the vendor data, is used at order release to calculate the due-ins and due-outs using the following equation:

Due IN/OUT = Conversion Factor \* QTY Ordered from the Primary

If the conversion factor is edited after the order is released, the due-ins and due-outs are not updated properly when the order is posted or deleted because the system does not retain the old conversion factor value.

## Editing the Item Short Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### At the Primary:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After modifying the description of an item in the primary inventory point, you will be given the option to save this new value as the description in all the distribution points containing the item.

### At the Secondary:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When adding a new item to the inventory, the default for the items, short description will be the description of that item in the source primary inventory point.

## Standard Reorder Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The use of a zero standard reorder point to designate items as “order on demand” is no longer valid. Items to be ordered on demand must have nothing entered for a standard reorder point. Items having a standard reorder point, even of zero, will be considered by the autogeneration process in creating new distribution orders.

## Multiple Sources for a Secondary Inventory Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each Secondary inventory point may be stocked by one and only one primary inventory point. Part of the reason for this restriction is to allow the item description logic to function appropriately.

## Usage Demand Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The usage demand report may now be run for one or more selected items. In addition, the user will have the option to sort items by item number or alphabetically by item description.

## Order Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Order Form now allows the user more flexibility. The user may choose to exclude items that do not have a normal stock level greater than zero and may choose to exclude the blank lines.

## Scheduling the Autogeneration of Distribution Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new option have been added for selection in the TaskMan Schedule/Unschedule option \[XUTM SCHEDULE\]. The scheduler does not accommodate specification of individual inventory points or facilities. Each option will generate orders for all the secondary inventory points on your system as indicated below:

PRCP NON-SS ORDER BUILDER (For all secondary inventory points

not linked to supply stations)

PRCP SUPPLY STA ORDER BUILDER (For all secondary inventory points

linked to supply stations)

No reports will be generated as a result of these options and you will still need to release the orders through GIP.

Select Taskman Management Option: SCHEDule/Unschedule Options

Select OPTION to schedule or reschedule: PRCP SUPPLY STA ORDER BUILDER

PRCP SUPPLY STATION ORDER BUILDER

Are you adding 'PRCP SUPPLY STA ORDER BUILDER' as

a new OPTION SCHEDULING (the 52ND)? No// Y (Yes)

Edit Option Schedule

Option Name: PRCP SUPPLY STA ORDER BUILDER

Menu Text: PRCP SUPPLY STATION ORDER BUILDE TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME:

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY:

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Select OPTION to schedule or reschedule: PRCP NON-SS ORDER BULIDER

PRCP NON-SS ORDER BUILDER

Are you adding 'PRCP NON-SS ORDER BULIDER' as

a new OPTION SCHEDULING (the 53RD)? No// Y (Yes)

Edit Option Schedule

Option Name: PRCP NON-SS ORDER BULIDER

Menu Text: PRCP NON-SS ORDER BUILDER TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME:

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY:

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# # # The ‘Interface-able’ GIP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Interface-able GIP refers to the functionality of GIP when a secondary inventory point uses the POINT OF USE INTERFACE. This interface allows the communication of inventory information between the secondary inventory point and its associated automated supply cabinet.

## The Interface – Real time, but Queued

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The interface between GIP and the supply stations is real time. All transactions generated by GIP are sent immediately to the supply station for processing. Transactions are received real time from the supply stations but may not be immediately processed if the files affected in GIP are in use.

## Information Sent to the Supply Station from GIP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Regular Distribution Orders. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

GIP sends these orders at the time they are released. The information sent will list the

GIP order number, all items ordered, the quantity of each item in the primary's unit of

issue and the secondary's conversion factor.

### Item Information (Short description, Normal, Standard Reorder, and Emergency Levels, Unit of Issue, Conversion Factor, and Last Cost). 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This information is sent, dependent upon the specific supply station,

whenever updates occur in GIP.

### Quantity on Hand (QOH) Query. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A request to a specific supply station for a list of its current

inventory items and levels.

## Information Sent to GIP from the Supply Station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Restocking. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This information will update the distribution order created in GIP. Once all items are

received, GIP will receive a transaction from the supply station to automatically post the

order.

### Item Activity. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Items taken or returned or adjusted will be reported to GIP and stored in the

INVENTORY TRANSACTION FILE (#445.2). The names of patients receiving items

taken from the station will be converted to upper case for storage in GIP. Using case

sensitivity to distinguish between patients will NOT be honored by GIP.

### Quantity on Hand (QOH) Response. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message is received after a query from GIP was sent to the supply

station and its data will be stored in the GENERIC INVENTORY FILE (#445).

## “Rules”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

GIP supports inventory points that do and do not interface to automated supply cabinets. When used, the interface allows cabinets some control of GIP functionality. Rules were established to clarify how the systems will work together.

### Linking a secondary inventory point with an automated supply cabinet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Specify the Supply Station for each linked inventory point

> The value of this field must be the vendor providing the cabinet to which this inventory point is interfaced. Once this is done, GIP will treat the inventory point as a supply station secondary.

2.  Inventory Point Name and Supply Station Name must be the same

> This field ties the two different systems to each other and must be formatted as:

> \<Site number\> - \<String up to 10 characters\>

> e.g.: 000-MYSTATION

3.  No outstanding distribution orders may exist on the secondary inventory point being linked to a supply station. The secondary’s outstanding orders must be posted or deleted first.
4.  The secondary inventory point may be linked to one and only one primary

> You will not be allowed to create the supply station association while the secondary is stocked by multiple primaries.

### Identifying the secondary inventory point items as items stored in the supply station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Normal Stock Level must be greater than zero

> Items with no normal stock level or a normal stock level equal to zero on a supply station secondary will not be treated by GIP as items stocked in the supply station. Items with a non-zero normal stock level will be treated by GIP as items that are stocked in the supply station.

> \*\*\* NOTE: Items for case carts or instrument kits should NOT be stored in the supply station nor in the supply station secondary because the processing of distribution orders for these items will not be handled by the interface.

> This Normal Stock Level may not be edited to zero or from zero when the item is on a released order for a supply station secondary.

2.  Specific values associated with supply station items will be communicated to the supply station anytime the items are edited in the secondary.
3.  The Supply Station Quantity on Hand for an item is not transmitted to the supply station.

> This field is received with all transactions sent by the supply station and does not overwrite the GIP quantity on hand. It is instead kept in GIP along with the date and time it was received.

### Creating distribution orders for the supply station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  An order for a supply station secondary having a Regular Order Type will contain only supply station items. Consequently:

> A regular order type cannot be edited to a different order type if the order is on a supply station secondary.

> Emergency and Call-in Orders may contain all supply station items, no supply station items, or a mix of the both types of items.

> The Emergency or Call-in order type cannot be edited to a regular order type on a supply station secondary but Emergency can be edited to Call-in and Call-in edited to Emergency

2.  Orders automatically generated for a supply station secondary will include only supply station items because these are the only items with normal stock levels.
3.  Regular orders will be sent to the supply station when released on GIP unless the orders are for instrument kits or case carts.
4.  Case cart and instrument kit items should not be included in the supply station secondary inventory point because orders for these items cannot be accommodated by the interface.
5.  Send Order

> If the supply station does not receive an order, there is an option available to send the order to the supply station. Only regular orders that have already been released and were considered supply station orders at the time of release may be sent to the supply station.

### Processing distribution orders for the supply station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

a\. Editing released orders for a supply station secondary is prohibited.

> Edits may be completed when entering the amount received at the supply station.

2.  Editing of normal stock level and vendor information for items in the released orders is also restricted.
3.  Posting of supply station orders will be controlled by the supply station.

> This is done automatically after receipt of all items in the order.

4.  Deletions are allowed at any time but when a released regular order for a supply station secondary is deleted from GIP, it must also be deleted manually on the supply station.

### Overriding the interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

a\. Removing the supply station flag from orders.

> Only when the interface will be down for an extended period time, should you consider removing the supply station flag from an order. This allows you to process the order in GIP as though it were not for a supply station secondary. Once run, GIP will not accept any information about that order from the supply station and the supply station flag cannot be replaced.

This page intentionally left blank.

# # New and Modified Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Options for Inventory Points and Their Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Assigning a Supply Station Provider to a Secondary Inventory Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SUPPLY STATION (field \#22 of the GENERIC INVENTORY FILE (#445)) allows you to identify the vendor of the supply station for a secondary inventory point. After this field is entered, GIP will treat the secondary inventory point as a supply station secondary.

To enable effective communications, the inventory point name must be the same as the supply station name. All supply station items in the secondary inventory point must have a non-zero normal stock level and must be associated with a bin in the supply station.

The supply station field can only be populated when:

\- The secondary inventory point is stocked by only 1 primary

\- The inventory point is a secondary inventory point

\- The secondary inventory point has no outstanding distribution orders

\- The secondary inventory point's name is no more than 10 characters long

An example where the supply station field cannot be populated:

Select Manager For Secondary Point Menu Option: Enter/Edit Inventory And

Distribution Points

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: SAMPLE IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

+--------------------------------------------------+

\|You have the option to edit ALL \|

\|SECONDARY inventory points you have \|

\|access to. \|

+--------------------------------------------------+

Select a 'Secondary' Type Inventory Point: SAMPLE 999-SAMPLE SECONDARY

Edit Inventory Parameters Aug 15, 2000 10:57:58 Page: 1 of 2

INVENTORY POINT: 999-SAMPLE TOTAL NUMBER OF ITEMS: 1

Description

Type of Inventory Point : SECONDARY

Abbreviated Name : SMPL

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion:

(Supply Station Provider) : \<== NOTE PARENTHESIS

Flags

Print Emergency Stock Levels :

Automatic Purge :

Inventory Users

\+ Enter ?? for more actions

AF All Fields FC (Fund Control Points)FL Flags

DE Descriptive DP (Distribution Points)AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// SP Special Parameters

MOS INACTIVE BEFORE ITEM DEL.:

Change this secondary to be stocked by only 1 primary before adding a

supply station provider.

Edit Inventory Parameters Aug 15, 2000 10:58:20 Page: 1 of 2

INVENTORY POINT: 999-SAMPLE TOTAL NUMBER OF ITEMS: 1

Description

Type of Inventory Point : SECONDARY

Abbreviated Name : SMPL

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion:

(Supply Station Provider) :

Flags

Print Emergency Stock Levels :

Automatic Purge :

Inventory Users

\+ Enter ?? for more actions

AF All Fields FC (Fund Control Points)FL Flags

DE Descriptive DP (Distribution Points)AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen/SB Stocked By

CHECKING INVENTORY POINTS DISTRIBUTING TO '999-SAMPLE': \<== CANNOT HAVE

MULTIPLE

999-LYFE'S PRIMARY TYPE: PRIMARY PRIMARIES

999-HEIBY TEMP TYPE: PRIMARY

999-LYFE VOLUNTARY TYPE: PRIMARY

THIS SECONDARY INVENTORY POINT '999-SAMPLE' IS CURRENTLY DISTRIBUTED

TO BY THE PRIMARY INVENTORY POINT '999-LYFE'S PRIMARY'.

DO YOU WANT TO REMOVE IT AS A PRIMARY DISTRIBUTION POINT? NO// ^

Editing the inventory point to accommodate a supply station:

Select Manager For Secondary Point Menu Option: Enter/Edit Inventory And

Distribution Points

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: SAMPLE IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

+-------------------------------------+

\|You have the option to edit ALL \|

\|SECONDARY inventory points you have \|

\|access to. \|

+-------------------------------------+

Select a 'Secondary' Type Inventory Point: UNLINKED SECONDARY

999-UNLINKED SECONDARY SECONDARY

Edit Inventory Parameters Aug 15, 2000 10:58:24 Page: 1 of 2

INVENTORY POINT: 999-UNLINKED SECONDARY TOTAL NUMBER OF ITEMS: 0

Description

Type of Inventory Point : SECONDARY

Abbreviated Name : UNLSEC

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion:

(Supply Station Provider) : \<== NOTE PARENTHESIS

Flags

Print Emergency Stock Levels :

Automatic Purge :

Inventory Users

\+ Enter ?? for more actions

AF All Fields FC (Fund Control Points)FL Flags

DE Descriptive DP (Distribution Points)AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// SP Special Parameters

MOS INACTIVE BEFORE ITEM DEL.:

A supply station IP cannot have a name longer than 10 characters.

Edit the name before linking a supply station to this IP.

Edit Inventory Parameters Aug 15, 2000 10:58:40 Page: 1 of 2

INVENTORY POINT: 999-UNLINKED SECONDARY TOTAL NUMBER OF ITEMS: 0

Description

Type of Inventory Point : SECONDARY

Abbreviated Name : UNLSEC

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion:

(Supply Station Provider) :

Flags

Print Emergency Stock Levels :

Automatic Purge :

Inventory Users

\+ Enter ?? for more actions

AF All Fields FC (Fund Control Points)FL Flags

DE Descriptive DP (Distribution Points)AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// DE Descriptive

INVENTORY POINT: 999-UNLINKED SECONDARY Replace ED... With

Replace

999-UNLINK

ABBREVIATED NAME: UNLSEC//

KEEP PERPETUAL INVENTORY?: YES//

KEEP DETAILED TRX. HISTORY?: YES//

Edit Inventory Parameters Aug 15, 2000 10:59:06 Page: 1 of 2

INVENTORY POINT: 999-UNLINKED SECONDARY TOTAL NUMBER OF ITEMS: 0

Description

Type of Inventory Point : SECONDARY

Abbreviated Name : UNLSEC

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion:

Supply Station Provider :

Flags

Print Emergency Stock Levels :

Automatic Purge :

Inventory Users

\+ Enter ?? for more actions

AF All Fields FC (Fund Control Points)FL Flags

DE Descriptive DP (Distribution Points)AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// SP Special Parameters

MOS INACTIVE BEFORE ITEM DEL.:

SS PROVIDER: OMNICELL

Description

Type of Inventory Point : SECONDARY

Abbreviated Name : UNLSEC

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion:

Supply Station Provider : OMNICELL

Flags

Print Emergency Stock Levels :

Automatic Purge :

Inventory Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// NEXT SCREEN

### Item Description Default in the Secondary Inventory Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If not yet entered, the ITEM DESCRIPTION (Sub field \#6 of INVENTORY ITEM (Field \#1) of the GENERIC INVENTORY FILE (#445)) for an item in the secondary inventory point will default in the Enter/Edit Inventory Item Data \[PRCP EDIT INVENTORY ITEMS\] to the primary’s description of the item.

NOTE

Secondaries are recommended to have one and only one primary. If there are multiple primaries, the default is the item description in the first primary the system identifies. If the item does not exist in this primary, the default will be blank.

Select Inventory File Maintenance Menu Option: ENter/Edit Inventory Item Data

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY SUPPLY STATION IP IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

Select MY SUPPLY STATION IP ITEM: 706 RAZOR-SAFETY DISPOSABLE SINGLE EDGE

...OK? Yes// (Yes)

RAZOR-SAFETY DISPOSA NSN: 8530-01-347-9577

Edit Inventory Item Data Aug 14, 2000 11:06:42 Page: 1 of 3

INVENTORY POINT: 999-MY SUPPLY STATION IP \* \* \* IM#: 706 \* \* \*

Descriptive-445:

Description-441: RAZOR-SAFETY DISPOSABLE SINGLE EDGE

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: ? per ?? Norm Stock Level:

Emer Stock Level:

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt :

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From Inv

Select Item(s): Next Screen// DE Descriptive

...item description set to short description in primary.

ITEM DESCRIPTION: RAZOR-1 EDGE, DISP//

GROUP CATEGORY:

MAIN STORAGE LOCATION:

Select ADDITIONAL STORAGE LOCATION:

### Editing the Item Description at the Primary Inventory Point 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After editing an item description in the primary, you will be given the option to automatically replace the description for that item in all the primary’s dependent inventory points with the description just entered.

NOTE

Allowing different primaries to share a secondary is NOT recommended. If a primary's item description is updated to affect all items in that primary's distribution points and then the description for the same item is edited on a different primary distributing to this secondary, the second edit will overwrite the description specified by the first primary.

Select Inventory File Maintenance Menu Option: ENter/Edit Inventory Item Data

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Primary Inventory Point: MY PRIMARY IP IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> DISTRIBUTION HISTORY NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

Select LYFE'S PRIMARY ITEM: SOAP ANTISEP BAR 5C 31 SOAP ANTISEP BAR 5C

...OK? Yes// (Yes)

SOAP ANTISEP BAR 5C NSN: 6508-01-027-2103

Edit Inventory Item Data Aug 14, 2000 11:07:51 Page: 1 of 3

INVENTORY POINT: 999-MY PRIMARY IP \* \* \* IM#: 31 \* \* \*

Descriptive-445: SOAP, ANTISEPTIC BAR

Description-441: SOAP ANTISEP BAR 5C

Group Category : 1001

ABC Classification: B - next highest 10% of AUDs

Main Storage Lo: A,2,4,1

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 10 per BX Norm Stock Level: 250

Issue Multiple: 10 Emer Stock Level: 10

Min Issue Qty : 10 Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 50

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI Secondary Items RI Remove Item From Inv

Select Item(s): Next Screen// DE Descriptive

ITEM DESCRIPTION: SOAP, ANTISEPTIC BAR // SOAP ANTISEP BAR 5C

Do you want to update the DESCRIPTION for ALL distribution

points stocked by 999-MY PRIMARY IP? YES \<= NOTE QUESTION

updating DESCRIPTION for distribution points.....

999-IFCAPTWO SECONDARY DESCRIPTION updated

999-IFCAPTHREE'S SECONDARY DESCRIPTION updated

999-IFCAPFOUR TEST DESCRIPTION updated

999-IFCAPONE'S SECONDARY DESCRIPTION updated

999-SAMPLE DESCRIPTION updated

999-UNLINKED SECONDARY DESCRIPTION updated

999-EXAMPLER In use, could not update. \<= NOTE!!!

999-PYXIS DESCRIPTION updated

Building HL7 EDIT Transaction on item#31 for PYXIS

station 999-PYXIS

999-MY SUPPLY STATION IP DESCRIPTION updated

Building HL7 EDIT Transaction on item#31 for OMNICELL

station 999-MY SUPPLY STATION IP

NOTE!!!

If the 'In use, could not update' MESSAGE DISPLAYS, you will need to

manually update the item description in that inventory point later.

### Inventory Point Names

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will not be allowed to edit the name of your secondary INVENTORY POINT (Field \#.01 of the GENERIC INVENTORY FILE (#445)) using the option, Enter/Edit Inventory And Distribution Points \[PRCP INVPT PARAM

ENTER/EDIT\], if it is attached to a supply station. The restriction supports the fact that Inventory Point Name is used to identify the linked inventory point to its associated supply station.

IF THE GIP NAME DIFFERS FROM THE SUPPLY STATION NAME, GIP WILL BE

UNABLE TO PROCESS INFORMATION FROM THE SUPPLY STATION AND THE SUPPLY STATION WILL NOT PROCESS INFORMATION SENT BY GIP.

Select a 'Secondary' Type Inventory Point: MY SUPPLY STATION IP 999-MY

SUPPLY STATION IP SECONDARY

Edit Inventory Parameters Aug 14, 2000 12:53:33 Page: 1 of 2

INVENTORY POINT: 999-MY SUPPLY STATION IP TOTAL NUMBER OF ITEMS: 9

Description

Type of Inventory Point : SECONDARY

Abbreviated Name : OMNI

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion:

(Supply Station Provider) : OMNICELL

Flags

Print Emergency Stock Levels :

Automatic Purge :

Inventory Users

\+ Enter ?? for more actions

AF All Fields FC (Fund Control Points)FL Flags

DE Descriptive DP (Distribution Points)AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// DE Descriptive

The inventory point name cannot be edited on a supply station secondary.

ABBREVIATED NAME: MSSIP//

> **WARNING:** A 'NO' RESPONSE MAY CAUSE INTEGRITY PROBLEMS \<= NOTE!!!

WITH THE SUPPLY STATION INTERFACE.

KEEP PERPETUAL INVENTORY?: YES// YES

> **WARNING:** A 'NO' RESPONSE CAUSES GIP TO IGNORE INFORMATION \<= NOTE!!!

FROM THE SUPPLY STATION.

KEEP DETAILED TRX. HISTORY?: YES// YES

NOTE!!!

When editing 'KEEP PERPETUAL INVENTORY?' and 'KEEP DETAILED TRX.

HISTORY?' on supply station secondaries, it is recommended both questions are

answered 'YES'

### Inactivating Inventory Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will not be allowed to inactivate inventory points if they:

1.  are supply station secondaries or
2.  have any outstanding (unposted and undeleted) distribution orders.

Select Manager For Primary Inventory Point Menu Option: ENter/Edit Inventory And Distribution Points

Select STATION NUMBER ('^' TO EXIT): 999// Anytown, USA

I N V E N T O R Y version 5.1

\(999\) Primary Inventory Point: ONE PRIMARY IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> DISTRIBUTION HISTORY NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

+-------------------------------------+

\|You have the option to edit ALL \|

\|PRIMARY inventory points you have \|

\|access to. \|

+-------------------------------------+

Select a 'Primary' Type Inventory Point: ON

1 ONE PRIMARY 999-ONE PRIMARY PRIMARY

2 ONLY PRIMARY 999-ONLY PRIMARY PRIMARY

CHOOSE 1-2: 2 999-ONLY PRIMARY PRIMARY

Edit Inventory Parameters Aug 14, 2000 16:30:28 Page: 1 of 5

INVENTORY POINT: 999-ONLY PRIMARY TOTAL NUMBER OF ITEMS: 15

Description

Type of Inventory Point : PRIMARY

Abbreviated Name : ONLY

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion: 6

Primary Updated By Warehouse : YES

Special Inventory Point Type :

Department Number : 333

Issue Book Sort : NSN SORT

Regular Whse Issues Schedule : OTHER

Flags

\+ Enter ?? for more actions

AF All Fields FC Fund Control Points FL Flags

DE Descriptive DP Distribution Points AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// DE Descriptive

INVENTORY POINT: 999-ONLY PRIMARY// @

You cannot delete inventory points after they are created.

This action removes all the items, distribution points, users,

etc., for the inventory point and changes the name to

STATIONNUMBER-'\*\*\*INACTIVE\_#\*\*\*' where \# is the internal entry number.

ARE YOU SURE YOU WANT TO PROCEED? NO// Y (YES)

You must first post or delete outstanding orders for this inventory point.

?? Required

INVENTORY POINT: 999-ONLY PRIMARY//

### Converting Secondary Inventory Points to Primary Inventory Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Secondary inventory points linked to a supply station CANNOT be converted to primaries. The supply station may only be linked to a secondary inventory point because the interface functionality is inappropriate to the primary inventory point.

Select Inventory File Maintenance Menu Option: convert Secondary to Primary

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Primary Inventory Point: EXAMPLE PRIMARY IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> DISTRIBUTION HISTORY NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

+----------------------------------------------------------+

\|Select the SECONDARY inventory point to CONVERT. It must \|

\|be one of the DISTRIBUTION POINTS for 999-EXAMPLE PRIMARY. \|

+----------------------------------------------------------+

Select DISTRIBUTION POINT: SAMPLE 999-SAMPLE SECONDARY KEEP

PERPETUAL INV

+------------------------------------------------------------------ +

\|This inventory point is linked to a supply station and cannot be \|

\|converted. \|

+-------------------------------------------------------------------+

### Adding Distribution Points to a Primary Inventory Point 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you attempt to make a secondary inventory point a distribution point of a primary and that secondary is already a distribution point to a different primary, you will get the message, DUPLICATE ENTRY or 'This secondary is already stocked by (another primary)'.

A secondary inventory point cannot be linked to a supply station if that secondary is a distribution point for multiple primaries.

Select Manager For Primary Inventory Point Menu Option: ENter/Edit

Inventory And Distribution Points

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Primary Inventory Point: SINGLE PRIMARY IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> DISTRIBUTION HISTORY NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

+-------------------------------------+

\|You have the option to edit ALL \|

\|PRIMARY inventory points you have \|

\|access to. \|

+-------------------------------------+

Select a 'Primary' Type Inventory Point: CANTEEN INVENTORY 999-CANTEEN

INVENTORY PRIMARY

Edit Inventory Parameters Aug 15, 2000 16:23:51 Page: 1 of 3

INVENTORY POINT: 999-CANTEEN INVENTORY TOTAL NUMBER OF ITEMS: 1

Description

Type of Inventory Point : PRIMARY

Abbreviated Name : CANT

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion: 12

Primary Updated By Warehouse : YES

Special Inventory Point Type :

Department Number : 060

Issue Book Sort : NSN SORT

Regular Whse Issues Schedule : OTHER

Flags

\+ Enter ?? for more actions

AF All Fields FC Fund Control Points FL Flags

DE Descriptive DP Distribution Points AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// DP Distribution Points

Select a 'Secondary' Type Inventory Point: SAMPLE 999-SAMPLE SECONDARY

This secondary is already stocked by 999-BUSYIP.

### Removing Supply Station Secondary Distribution Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### If you need to unlink a secondary inventory point from a supply station, or link it to a different supply station, you will first be required to delete or post all outstanding distribution orders for that secondary.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Manager For Primary Inventory Point Menu Option: ENter/Edit

Inventory And Distribution Points

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Primary Inventory Point: ONE PRIMARY IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> DISTRIBUTION HISTORY NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

+-------------------------------------+

\|You have the option to edit ALL \|

\|PRIMARY inventory points you have \|

\|access to. \|

+-------------------------------------+

Select a 'Primary' Type Inventory Point: ON

1 ONE PRIMARY 999-ONE PRIMARY PRIMARY

2 ONLY PRIMARY 999-ONLY PRIMARY PRIMARY

CHOOSE 1-2: 2 999-ONLY PRIMARY PRIMARY

Edit Inventory Parameters Aug 15, 2000 10:34:25 Page: 1 of 5

INVENTORY POINT: 999-ONLY PRIMARY TOTAL NUMBER OF ITEMS: 15

Description

Type of Inventory Point : PRIMARY

Abbreviated Name : ONLY

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion: 6

Primary Updated By Warehouse : YES

Special Inventory Point Type :

Department Number : 333

Issue Book Sort : NSN SORT

Regular Whse Issues Schedule : OTHER

Flags

\+ Enter ?? for more actions

AF All Fields FC Fund Control Points FL Flags

DE Descriptive DP Distribution Points AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// DP Distribution Points

Select a 'Secondary' Type Inventory Point: SAMPLE 999-SAMPLE

SECONDARY

Edit Inventory Parameters Aug 15, 2000 10:34:30 Page: 1 of 2

INVENTORY POINT: 999-SAMPLE TOTAL NUMBER OF ITEMS: 9

Description

Type of Inventory Point : SECONDARY

Abbreviated Name : SMPL

Keep Perpetual Inventory : YES

Keep Transaction Register : YES

Special Parameters

Months Inactive Before Item Deletion:

(Supply Station Provider) :

Flags

Print Emergency Stock Levels :

Automatic Purge :

Inventory Users

\+ Enter ?? for more actions

AF All Fields FC (Fund Control Points)FL Flags

DE Descriptive DP (Distribution Points)AU Authorized Users

SP Special Parameters SB Stocked By MC MIS Costing

Select Item(s): Next Screen// SB Stocked By

CHECKING INVENTORY POINTS DISTRIBUTING TO '999-SAMPLE':

999-ONLY PRIMARY TYPE: PRIMARY

THIS SECONDARY INVENTORY POINT '999-SAMPLE' STOCKED BY THE PRIMARY

INVENTORY POINT '999-ONLY PRIMARY' HAS OUTSTANDING REGULAR ORDERS.

You must post or delete these orders before removing the primary

distribution point.

Press RETURN to continue, '^' to exit:^

### Processor for Supply Station Transactions (Task Manager Option)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may not be accessed through the menus but can be selected from

the Task Manager Schedule/Unschedule \[XUTM SCHEDULE\] option. This task

should only be scheduled if your site will be using the supply station

interface. An example is found under the instructions for setting your

system up for this interface.

Schedule the HL7 processing job, \[PRCP2 SUPPLY STATION TXN RUN\], to run

via the Schedule/Unschedule Options \[XUTM SCHEDULE\] option.

Edit Option Schedule

Option Name: PRCP2 SUPPLY STATION TXN RUN

Menu Text: PROCESSOR FOR SUPPLY STATION TXN TASK ID: 238541

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: SEP 11,2000@14:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 300S \<== Suggested interval of 3-5 minutes

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Updating Items on the Supply Station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When setting up the interface for the first time, you may use this option to update the item names in the supply station to correspond to what is appropriate for your inventory point. This option cannot correct problems due to the name’s length in GIP exceeding the number of characters allowed by the vendor.

This option automatically generates a transaction for all supply station items in your secondary inventory point.

Select IFCAP MENU Option: primary Inventory Point Main Menu

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

Select Primary Inventory Point: MY PRIMARY 999-MY PRIMARY PRIMARY

Select Primary Inventory Point Main Menu Option: manager For Primary Inventory P

oint Menu

Select Manager For Primary Inventory Point Menu Option: supply Station Item Update

I N V E N T O R Y version 5.1

\(999\) Primary Inventory Point: MY PRIMARY IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> DISTRIBUTION HISTORY NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> OPENING MONTHLY INVENTORY BALANCES NEED TO BE SET.

Select a 'Secondary' Type Inventory Point: pyxiS 999-PYXIS SECONDARY

This option sends information about ALL items with a normal stock

level greater than zero to the linked supply station.

You must flag the transactions as 'ADD' or 'EDIT'.

Select 'Add' OR 'Edit' transactions: (A/E): a ADD

Building HL7 EDIT Transaction on item#8 for PYXIS

station 999-PYXIS

Building HL7 EDIT Transaction on item#31 for PYXIS

station 999-PYXIS

Building HL7 EDIT Transaction on item#47 for PYXIS

station 999-PYXIS

Building HL7 EDIT Transaction on item#101 for PYXIS

station 999-PYXIS

Building HL7 EDIT Transaction on item#104 for PYXIS

station 999-PYXIS

Building HL7 EDIT Transaction on item#12002 for PYXIS

station 999-PYXIS

Building HL7 EDIT Transaction on item#12013 for PYXIS

station 999-PYXIS

### Options Concerning Inventory Point Supplies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Normal Stock Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All items in a secondary inventory point linked to a supply station, with a NORMAL STOCK LEVEL (Sub field \#9 of INVENTORY ITEM (Field \#1) of the GENERIC INVENTORY FILE (#445)) greater than zero are considered supply station items.

Normal Stock Levels may be edited using the following options:

Enter/Edit Inventory Item Data \[PRCP EDIT INVENTORY ITEMS\]

Enter/Edit Items On Distribution Point \[PRCP EDIT DISTR PT ITEMS\] (when

the perpetual inventory flag is set to NO)

If the supply station item being edited is on outstanding orders, you will not be allowed to change its normal stock level to zero because this action deletes the item from the supply station.

> **NOTE:** Items representing case carts or instrument kits should not be stored in the supply station or in its associated secondary inventory point because the interface will not support the processing of distribution orders for these items.

1\. Editing the Normal Stock Level on a Supply Station Item to a non-zero value

Select Inventory File Maintenance Menu Option: ENter/Edit Inventory Item Data

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

Select MY STATION ITEM: WOOZLES 12013 WOOZLES

...OK? Yes// (Yes)

WOOZLES NSN: 7510-19-229-2298

Edit Inventory Item Data Aug 14, 2000 14:19:43 Page: 1 of 3

INVENTORY POINT: 999-MY STATION \* \* \* IM#: 12013 \* \* \*

Description-445: WOOZLES

Description-441: WOOZLES

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 1 per EA Norm Stock Level: 90

Emer Stock Level: 20

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 30

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From Inv

Select Item(s): Next Screen// LE Levels

There are outstanding regular orders for this item.

You cannot delete the normal level or make it 0

NORMAL STOCK LEVEL (1 per EA): (1-999999): 90// 45

EMERGENCY STOCK LEVEL (1 per EA): 20//

TEMPORARY STOCK LEVEL (1 per EA):

STANDARD REORDER POINT (1 per EA): 30//

OPTIONAL REORDER POINT (1 per EA):

Edit Inventory Item Data Aug 14, 2000 14:19:58 Page: 1 of 3

INVENTORY POINT: 999-MY STATION \* \* \* IM#: 12013 \* \* \*

Descriptive-445:

Description-441: WOOZLES

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 1 per EA Norm Stock Level: 45

Emer Stock Level: 20

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 30

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From Inv

Select Item(s): Next Screen//

2\. Editing the Normal Stock Level on a Supply Station Item to a zero value:

NOTE

Editing the normal level to zero will remove an item from the supply station.

Select Inventory File Maintenance Menu Option: ENter/Edit Inventory Item Data

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IP

IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

Select MY STATION IP ITEM: WOOZLES 12013 WOOZLES

...OK? Yes// (Yes)

WOOZLES NSN: 7510-19-229-2298

Edit Inventory Item Data Aug 14, 2000 13:56:49 Page: 1 of 3

INVENTORY POINT: 999-MY STATION \* \* \* IM#: 12013 \* \* \*

Descriptive-445: WOOZLES

Descriptive-441:

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 1 per EA Norm Stock Level: 90

Emer Stock Level: 20

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 30

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From Inv

Select Item(s): Next Screen// LE Levels

Changing the level to zero will delete the item from the supply station.

NORMAL STOCK LEVEL (U OF I): 90// 0

Building HL7 DELETE Transaction on item#12013 for PYXIS

station 999-MY STATION

EMERGENCY STOCK LEVEL (1 per EA): 20//

TEMPORARY STOCK LEVEL (1 per EA):

STANDARD REORDER POINT (1 per EA): 30//

OPTIONAL REORDER POINT (1 per EA):

Edit Inventory Item Data Aug 14, 2000 13:56:49 Page: 1 of 3

INVENTORY POINT: 999-MY STATION IP \* \* \* IM#: 12013 \* \* \*

Descriptive-445:

Description-441: WOOZLES

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 1 per EA Norm Stock Level: 0

Emer Stock Level: 20

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 30

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From Inv

Select Item(s): Next Screen// LE Levels

3\. Editing the Normal Level of a non-supply station number to a non-zero value:

NOTE

Editing the normal level from zero to non-zero will add items to the supply station.

Select Inventory File Maintenance Menu Option: ENter/Edit Inventory Item Data

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IP IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

Select MY STATION IP ITEM: WOOZLES 12013 WOOZLES

...OK? Yes// (Yes)

WOOZLES NSN: 7510-19-229-2298

Edit Inventory Item Data Aug 14, 2000 13:56:49 Page: 1 of 3

INVENTORY POINT: 999-MY STATION IP \* \* \* IM#: 12013 \* \* \*

Descriptive-445:

Description-441: WOOZLES

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 1 per EA Norm Stock Level: 0

Emer Stock Level: 20

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 30

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From Inv

Select Item(s): Next Screen// LE Levels

Changing the level from zero will add the item to the supply station.

NORMAL STOCK LEVEL (U OF I): 0// 90

Building HL7 ADD Transaction on item#12013 for PYXIS

station 999-MY STATION

EMERGENCY STOCK LEVEL (1 per EA): 20//

TEMPORARY STOCK LEVEL (1 per EA):

STANDARD REORDER POINT (1 per EA): 30//

OPTIONAL REORDER POINT (1 per EA):

Edit Inventory Item Data Aug 14, 2000 13:56:49 Page: 1 of 3

INVENTORY POINT: 999-MY STATION IP \* \* \* IM#: 12013 \* \* \*

Descriptive-445:

Description-441: WOOZLES

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 1 per EA Norm Stock Level: 90

Emer Stock Level: 20

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 30

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From Inv

Select Item(s): Next Screen//

### Editing a Secondary Inventory Point Item’s Conversion Factor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DISPENSING UNIT CONVERSION FACTOR (sub field \#5 of the INVENTORY ITEM (field \#1) of the GENERIC INVENTORY FILE (#445)) cannot be edited for

items on released orders. GIP uses this field to calculate due-ins and due-outs when orders are released. The supply stations receive the conversion factor at the time of order release and use it to translate the order quantities into supply station amounts. If the value is edited after order release, the amount received at the supply station will differ

from what GIP posts to the secondary and the due-ins and due-outs will be wrong.

Select Inventory File Maintenance Menu Option: ENter/Edit Inventory Item Data

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

Select MY STATION ITEM: WOOZLES 12013 WOOZLES

...OK? Yes// (Yes)

WOOZLES NSN: 7510-19-229-2298

Edit Inventory Item Data Aug 15, 2000 10:10:30 Page: 1 of 3

INVENTORY POINT: 999-MY STATION \* \* \* IM#: 12013 \* \* \*

Descriptive-445: WOOZLES

Description-441: WOOZLES

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 4 per SF Norm Stock Level: 50

Emer Stock Level: 1

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 5

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From

Inv

Select Item(s): Next Screen// VN Vendors

...adding inventory points as procurement sources

...checking currently stored procurement sources

999-ONE PRIMARY

UNIT per PURCHASE: 1 per EA

UNIT per RECEIPT: 1 per EA

CONVERSION FACTOR: 1

...checking mandatory source in the inventory point

Checking the released orders for this item...

To edit these values, you must first post or delete the following

order(s):

91

Press RETURN to continue, '^' to exit:

### Item Deletion at the Primary and Secondary Inventory Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system will check unposted distribution orders prior to deleting an item from a primary or secondary inventory point. If the item is found on any outstanding orders, the deletion process will be stopped and a message will display indicating the orders that must first be deleted or posted. Options affected by this include:

Auto-generate Orders \[PRCP AUTOGENERATE PRIM/WHSE\]

Auto-generate Orders \[PRCP2 AUTOGENERATE SECONDARY\]

Copy Primary To Secondary \[PRCP COPY PRIMARY TO SECONDARY\]

Copy Secondary To Secondary \[PRCP COPY SECOND TO SECOND\]

Distribution Order Processing \[PRCP DIST ORDER PROCESSING\]

Enter/Edit Inventory Item Data \[PRCP EDIT INVENTORY ITEMS\]

Select Inventory File Maintenance Menu Option: ENter/Edit Inventory Item Data

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

Select MY STATION ITEM: WOOZLES 12013 WOOZLES

...OK? Yes// (Yes)

WOOZLES NSN: 7510-19-229-2298

Edit Inventory Item Data Aug 15, 2000 09:13:54 Page: 1 of 3

INVENTORY POINT: 999-MY STATION \* \* \* IM#: 12013 \* \* \*

Descriptive-445:

Description-441: WOOZLES

Group Category :

ABC Classification:

Main Storage Lo:

Add Storage Loc:

Type Of Item : PURCHASABLE

Issue Units Levels

Unit per Issue: 1 per EA Norm Stock Level: 45

Emer Stock Level: 20

Temp Stock Level:

Delete Temp SL :

Stand Reord Pt : 30

Option Reord Pt :

\+ Enter ?? for more actions

AF All Fields QT Quantities SP Special Parameters

DE Descriptive CD Costing Data DA (Drug Accountability)

IU Issue Units DI Due Ins VN Vendors

LE Levels SI (Secondary Items) RI Remove Item From Inv

Select Item(s): Next Screen// RI Remove Item From Inv

Checking to see if this item is on an outstanding order....

This item cannot be deleted. You must first post, delete, or

remove the item from the following order(s):

92

\<Press RETURN to continue\>

### Order Form 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Order Form \[PRCP CATALOG/ORDER FORM PRINT\] option allows you to generate a printout of all or some of the items in a specified inventory point. The printout can optionally include:

1.  All items or just those with a non-zero normal stock level
2.  Blanks for entering values

Select Stock Replenishment Menu Option: ORder Form

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

+--------------------------------------+

\|The Order Form prints the current or \|

\|selected inventory point's items \|

\|sorted by main storage location and \|

\|description. Blanks for daily \|

\|ordering may be included. \|

+--------------------------------------+

+-------------------------------------+

\|Select the month-year of the order \|

\|form for 999-MY STATION. \|

+-------------------------------------+

Print Catalog/Order Form for DATE: TODAY// (AUG 15, 2000)

Print only items with a non-zero normal level? YES// (YES)

Include blanks on printout? YES// N (NO)

DEVICE: HOME// UCX/TELNET

\<\*\> please wait \<\*\>

ORDER FORM FOR: 999-MY STATION AUG 15, 2000@12:47:46 PAGE 1

FOR THE MONTH-YEAR: AUG 2000 STAND NORM

UNIT

DESCRIPTION MI# NSN UNIT/IS REOPT STLVL

COST

--------------------------------------------------------------------------

MAIN STORAGE LOCATION: ?

KIT SHAVING-SURG PREP 104 6515001036659 1/KT 100 120

3.00

SOAP ANTISEP BAR 5C 31 6508010272103 1/BR 50 250

0.09

STERI PEEL 6 IN X 10 IN 47 6530012580953 1/EA 1000 1200

0.09

TOSYLATE SYRINGE 50MG/10ML 101 650501A991234A 1/EA 12 50

2.25

\[END OF REPORT\]------------------------------------------------\[USER:IFUSER,ONE\]

\<Press RETURN to continue\>

### Querying the Supply Station for its Quantity on Hand

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Supply Station Quantity Discrepancy \[PRCP SS QTYDISCREPANCIES\] will display the date and time of the last query to the supply station and allow you to create a new query.

Select Secondary Inventory Point Main Menu Option: REPorts Menu

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

Select Reports Menu Option: SUPPly Station Quantity Discrepancy

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

+--------------------------------------+

\|This report displays items whose \|

\|on-hand quantity in 999-OMNICELL \|

\|differs from the supply station's \|

\|on-hand amount \|

+--------------------------------------+

+-------------------------------------+

\|The Last QOH update was received on \|

\|AUG 7,2000 at 12:56:02. If this date \|

\|is too old, you may now request an \|

\|update. \|

+-------------------------------------+

Do you want to request a refresh of the supply station QOH? NO// Y (YES)

Sending request...

Please give GIP time to get the information before printing the report.

## Options Concerning Distribution Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All orders autogenerated on supply station secondaries will contain only items considered by GIP to be items stocked in the supply station.

### Regular Orders and Editing Order Type in Orders for Supply Station Secondaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a regular order has been created for a supply station, its TYPE (field \#3.5 of the INTERNAL ORDER/ADJ FILE (#445.3)) cannot be edited. Regular orders for a supply station secondary will contain only supply station items. No non-supply station items may be added to a regular order. Once released, you may delete but not edit the order. Orders deleted in GIP must also be manually deleted from the supply station.

NOTE

Items representing case carts or instrument kits should not be stored in the supply station or in its associated secondary inventory point because the interface will not support the processing of distribution orders for these items.

Select Stock Replenishment Menu Option: DISTribution Order Processing

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

\*\* Distribution from inventory point: 999-ONE PRIMARY \*\*

Select DISTRIBUTION ORDER: 94 999-MY STATION 08-14-00 REGULAR ORDER

This is a regular order on a supply station secondary.

Its 'TYPE OF ORDER' cannot be edited to CALL_IN or EMERGENCY.

REMARKS:

Distribution Order Processing Aug 14, 2000 14:58:54 Page: 1 of 1

POST ITEMS TO SECONDARY: 999-MY STATION

999-ONE PRIM DISTRIBUTION ORDER: 94 STATUS: \<\< NOT RELEASED \>\>

ITEM DESCRIPTION UI ORDERED CONVFACT QTY

ONHAND

CATS (#12002) EA 3 1 655

Enter ?? for more actions

EI Edit Items On Order DI Delete Item On Order SO (Send Order)

CO Check Order/Items DO Delete Order PT (Picking Ticket Print)

EE E/E Inventory Items RO Release Order PO (Post Order)

Select Item(s): Quit// QUIT

Select Stock Replenishment Menu Option: DISTribution Order Processing

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

Emergency and Call-in distribution orders may be a mix of both supply station and non-supply station items. The order type of these orders cannot be edited to Regular after the order is created.

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

\*\* Distribution from inventory point: 999-ONE PRIMARY \*\*

Select DISTRIBUTION ORDER: 85 999-MY STATION 08-04-00

EMERGENCY

RELEASED TO FILL

This order is for a supply station secondary.

The order type cannot be changed to regular.

TYPE OF ORDER: (C/E): EMERGENCY// R

Enter a code from the list.

Select one of the following:

C CALL-IN

E EMERGENCY

This order is for a supply station secondary.

The order type cannot be changed to regular.

TYPE OF ORDER: (C/E): EMERGENCY// CALL-IN

REMARKS:

Distribution Order Processing Aug 14, 2000 14:59:07 Page: 1 of 1

POST ITEMS TO SECONDARY: 999-MY STATION

999-ONE PRIM DISTRIBUTION ORDER: 85 STATUS: RELEASED TO FILL

ITEM DESCRIPTION UI ORDERED CONVFACT QTY ONHAND

ARM BOARD 9 INCH LONG (#7) RO 2 1 200

SOAP ANTISEP BAR 5C (#31) BX 1 10 7374

Enter ?? for more actions

EI (Edit Items On Order)DI (Delete Item On Order)SO(Send Order)

CO Check Order/Items DO (Delete Order) PT Picking Ticket Print

EE E/E Inventory Items RO (Release Order) PO (Post Order)

Select Item(s): Quit//

### Sending an Order to the Supply Station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only regular orders for a supply station secondary may be sent to the supply station. This will be done automatically when the order is released. If for some reason, the station does not receive the order, you may re-transmit it using the option, SO - Send Order on the Distribution Order Processing screen.

NOTE

Items representing case carts or instrument kits should not be stored in the supply station or in its associated secondary inventory point because the interface will not support the processing of distribution orders for these items.

This option may only be used on orders that have been released but are not yet posted. Orders whose supply station flag has been removed cannot be re-sent to the supply station and must be completed in GIP.

Distribution Order Processing Aug 11, 2000 15:16:45 Page: 1 of 1

POST ITEMS TO SECONDARY: 999-SUPPLY CAB

999-THE BEST PRIM DISTRIBUTION ORDER: 91 STATUS: RELEASED TO FILL

ITEM DESCRIPTION UI ORDERED CONVFACT QTY ONHAND

CATS (#12002) EA 3 1 655

WOOZLES (#12013) EA 10 1 55

Enter ?? for more actions

EI (Edit Items On Order)DI (Delete Item On Order)SO Send Order

CO Check Order/Items DO (Delete Order) PT Picking Ticket Print

EE E/E Inventory Items RO (Release Order) PO (Post Order)

Select Item(s): Quit// so Send Order

ORDER INFORMATION WILL BE TRANSMITTED TO THE SUPPLY STATION.

### Removing the Supply Station Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The supply station flag is automatically added to the distribution order record when a regular order for a supply station secondary is released. This flag maintains the integrity of the GIP/SUPPLY STATION interface by insuring that all order processing will be driven by activity at the supply station.

If the interface will be down for extended periods of time, it may be necessary to disable this flag and allow the order to be processed manually in GIP using Remove Supply Station From Dist Order \[PRCP2 REMOVE SS FROM DIST ORD\]. Once run, the flag cannot be replaced into the order record.

Select Stock Replenishment Menu Option: REMOve Supply Station From Dist Order

Select DISTRIBUTION ORDER: 91 999-SUPPLY CAB 08-11-00

REGULAR ORDER

RELEASED TO FILL

> **WARNING:** RESTRICTIONS MAY COMPROMISE THE INTEGRITY OF INVENTORY DATA !!!

Restrict processing ONLY when a supply station or its interface is

down for extended periods of time.

Restrict all processing of this order to GIP? NO// YES

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Supply Station Quantity Discrepancy 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Supply Station Quantity Discrepancy \[PRCP SS QTYDISCREPANCIES\] report is a new report that will list the latest quantity on hand for both the inventory point and the supply station. The quantity on-hand last reported by the supply station displays with the date reported for each item. Items not in GIP but in the supply station will not appear on the report.

The report option also facilitates a mechanism for querying the supply station to refresh all supply station quantities on hand within GIP.

Select Reports Menu Option: SUPply Station Quantity Discrepancy

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

+--------------------------------------+

\|This report displays items whose \|

\|on-hand quantity in 999-MY STATION \|

\| differs from the supply station's }

\|on-hand amount \|

+--------------------------------------+

+-------------------------------------+

\|The Last QOH update was received on \|

\|AUG 1,2000 at 10:38:28. If this date \|

\|is too old, you may now request an \|

\|update. \|

+-------------------------------------+

Do you want to request a refresh of the supply station QOH? NO// (NO)

DEVICE: HOME// UCX/TELNET

\<\*\> please wait \<\*\>

SUPPLY STATION QUANTITY DISCREPANCY REPORT AUG 11, 2000@16:05:02 PAGE 1

FOR: 999-MY STATION

GIP SUPPLY STATION

QTY NOW QTY (AS OF DATE and TIME) ITEM NUMBER AND DESCRIPTION

--------------------------------------------------------------------------

191 48 (AUG 7,2000@16:28:45) 31 SOAP ANTISEP BAR 5C

60 1110 (AUG 7,2000@16:28:46) 47 STERI PEEL 6 IN X 10 IN

-21 34 (AUG 7,2000@16:28:47) 101 TOSYLATE SYRINGE 50MG/10ML

-15 103 (AUG 7,2000@16:28:48) 104 KIT SHAVING-SURG PREP

\[END OF

REPORT\]------------------------------------------------\[USER:IFUSER,ONE\]

### Inventory Sales Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INVENTORY SALES REPORT \[PRCP INVENTORY SALES REPORT\] list all distribution activity for items stocked in an inventory point. Items stocked in the primary are distributed to secondary inventory points and items in a supply station secondary are distributed to patients.

Select Reports Menu Option: INVEntory Sales Report

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

+---------------------------------- ----+

\|The Inventory Sales Report will \|

\|display all sales from the Secondary \|

\|inventory point. This report is \|

\|sorted by description, the recipient \|

\|and the date issued. \|

+---------------------------------- ----+

+-------------------------------------+

\|Select the RECIPIENTS to display \|

+-------------------------------------+

Do you want ALL recipients? YES// (YES)

+--------------------------------------------------------------------+

\| Currently selected recipients: \|

\| \<\< ALL RECIPIENTS \>\> \|

\| You can DE-select one of the above recipients: by reselecting it. \|

+--------------------------------------------------------------------+

RECIPIENT:

+-------------------------------------+

\|Select the range of ISSUE DATES to \|

\|display \|

+-------------------------------------+

Start with Issue Date: AUG 01, 2000// (AUG 01, 2000)

End with Issue Date: AUG 15, 2000// (AUG 15, 2000)

\*\*\* Selected date range from AUG 01, 2000 to AUG 15, 2000 \*\*\*

+-------------------------------------+

\|Display Summary or ALL Data. \|

+-------------------------------------+

Do you want to print a summary only? YES// N (NO)

DEVICE: HOME// UCX/TELNET

\<\*\> please wait \<\*\>

INVENTORY SALES FOR: MY STATION AUG 15, 2000@12:45:56 PAGE 1

INVENTORY SALES DATE RANGE: AUG 01, 2000 TO AUG 15, 2000

DESCRIPTION DATE ISSUED QUANTITY SELL COST TOTAL

VALUE

--------------------------------------------------------------------------

KIT SHAVING-SURG PREP \[104\]

IFPATIENT,ONE 08/04/00 10 0.000

0.00

08/04/00 -3 0.000

0.00

08/08/00 10 0.000

0.00

08/08/00 -3 0.000

0.00

TOTALS BY RECIPIENT: 14

0.00

TOTALS BY ITEM: 14

0.00

SOAP ANTISEP BAR 5C \[31\]

IFPATIENT,ONE 08/04/00 11 0.010

0.11

08/04/00 -4 0.010

-0.04

08/08/00 11 0.010

0.11

08/08/00 -4 0.010

-0.04

TOTALS BY RECIPIENT: 14

0.14

TOTALS BY ITEM: 14

0.14

STERI PEEL 6 IN X 10 IN \[47\]

IFPATIENT,ONE 08/04/00 10 0.087

0.87

Press RETURN to continue, '^' to exit:

INVENTORY SALES FOR: MY STATION AUG 15, 2000@12:45:56 PAGE 2

INVENTORY SALES DATE RANGE: AUG 01, 2000 TO AUG 15, 2000

DESCRIPTION DATE ISSUED QUANTITY SELL COST TOTAL

VALUE

--------------------------------------------------------------------------

08/04/00 -10 0.087

-0.87

08/08/00 10 0.087

0.87

08/08/00 -10 0.087

-0.87

TOTALS BY RECIPIENT: 0

0.00

TOTALS BY ITEM: 0

0.00

TOSYLATE SYRINGE 50MG/10ML \[101\]

IFPATIENT,ONE 08/04/00 11 0.000

0.00

08/04/00 -1 0.000

0.00

08/08/00 11 0.000

0.00

08/08/00 -1 0.000

0.00

TOTALS BY RECIPIENT: 20

0.00

TOTALS BY ITEM: 20

0.00

TOTAL SALES TO RECIPIENTS:

IFPATIENT,ONE 0.14

TOTAL 0.14

\[END OF REPORT\]------------------------------------------------\[USER:IFUSER,ONE\]

\<Press RETURN to continue\>

### Quantity Distribution Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Quantity Distribution Report \[PRCP QUANTITY DISTRIBUTION\] summarizes the distributions each month from a specified inventory point.

Select Reports Menu Option: Quantity Distribution Report

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

+--------------------------------------+

\|The Quantity Distribution Report lists\|

\|all sales from a supply station to a \|

\|recipient. This report is sorted by \|

\|description and date issued. \|

+--------------------------------------+

+-------------------------------------+

\|Select the Items to display \|

+-------------------------------------+

To select ALL items, press RETURN.

Select PYXIS ITEM:

Do you want to select ALL items? YES// (YES)

DEVICE: HOME// UCX/TELNET

\<\*\> please wait \<\*\>

QUANTITY DISTRIBUTION REPORT FOR: MY STATION AUG 15, 2000@15:33 PAGE 1

QUANTITY DISTRIBUTION DATE RANGE: AUG 1999 TO AUG 15, 2000

STAND OPT TEMP EMER NORM

DESCRIPTION MI# UNIT/IS REOPT REOPT S.LVL S.LVL S.LVL

--------------------------------------------------------------------------

KIT SHAVING-SURG PREP 104 1/KT 100 5 120

AUG99 SEP99 OCT99 NOV99 DEC99 JAN00 ^

... ... ... ... ... ... \|

... ... ... ... ... ... v

FEB00 MAR00 APR00 MAY00 JUN00 JUL00 AUG00 AVG

... ... ... ... ... 13 ... 1

... ... ... ... ... 39.00 ... 3.25

SOAP ANTISEP BAR 5C 31 1/BR 50 10 250

AUG99 SEP99 OCT99 NOV99 DEC99 JAN00 ^

... ... ... ... ... ... \|

... ... ... ... ... ... v

FEB00 MAR00 APR00 MAY00 JUN00 JUL00 AUG00 AVG

... ... ... ... ... 15 ... 1

... ... ... ... ... 1.38 ... 0.12

STERI PEEL 6 IN X 10 IN 47 1/EA 1000 50 1200

AUG99 SEP99 OCT99 NOV99 DEC99 JAN00 ^

... ... ... ... ... ... \|

... ... ... ... ... ... v

FEB00 MAR00 APR00 MAY00 JUN00 JUL00 AUG00 AVG

... ... ... ... ... 20 ... 2

... ... ... ... ... 1.30 ... 0.11

TOSYLATE SYRINGE 50MG/10ML 101 1/EA 12 7 50

AUG99 SEP99 OCT99 NOV99 DEC99 JAN00 ^

... ... ... ... ... ... \|

... ... ... ... ... ... v

FEB00 MAR00 APR00 MAY00 JUN00 JUL00 AUG00 AVG

... ... ... ... ... 12 ... 1

... ... ... ... ... 27.01 ... 2.25

\[END OF REPORT\]------------------------------------------------\[USER:IFUSER,ONE\]

\<Press RETURN to continue\>

### Usage Demand Item Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Usage Demand Item Report \[PRCP USAGE DEMAND ITEM REPORT\] lists the quantity of items used monthly and the total used within a specified period for a specified inventory point.

Select Reports Menu Option: USAGE Demand Item Report

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

+--------------------------------------+

\|The Usage Demand Item Report will show\|

\|the quantity of items used within a \|

\|specified date period. \|

+--------------------------------------+

+-------------------------------------+

\|Select the date range which should be\|

\|used for displaying the usage. \|

+-------------------------------------+

Start with Date: MAY 2000// (MAY 2000)

End with Date: AUG 2000// (AUG 2000)

\*\*\* Selected date range from MAY 2000 to AUG 2000 \*\*\*

-- TOTAL NUMBER OF DAYS: 92

+-------------------------------------+

\|Select the items to display. \|

+-------------------------------------+

To select ALL items, press RETURN.

Select MY STATION ITEM:

Do you want to select ALL items? YES// (YES)

+-------------------------------------+

\|Select the Group Categories to \|

\|display \|

+-------------------------------------+

Do you want to select ALL group categories? YES// (YES)

------------------------------------------------------------------------

\| Currently selected group categories: \|

\| \<\< ALL GROUP CATEGORIES \>\> \|

\| You can DE-select one of the above group categories by reselecting it.

------------------------------------------------------------------------

Select GROUP CATEGORY:

+-------------------------------------+

\|Select the order in which you want \|

\|the item information to appear. \|

+-------------------------------------+

Select one of the following:

1 ITEM DESCRIPTION

2 ITEM NUMBER

Sort by: ITEM DESCRIPTION//

DEVICE: HOME// UCX/TELNET

\<\*\> please wait \<\*\>

USAGE DEMAND ITEM REPORT: MY STATION AUG 15, 2000@15:36:05 PAGE 1

USAGE DATE RANGE FROM MAY 2000 TO AUG 2000 (92 DAYS)

DESCRIPTION MI UNIT/IS LAST \$ AVG \$ ON-HAND

--------------------------------------------------------------------------

GROUP: \<\<NONE\>\>

ARM BOARD 9 INCH LONG 7 2/RO 0.000 0.000 0

MAY00 0 0.00 JUN00 0 0.00 JUL00 0 0.00

AUG00 0 0.00

---------------------------------------- CUMULATIVE TOTAL 0 0.00

CATS 12002 1/EA 35.715 0.000 0

MAY00

0 0.00 JUN00 0 0.00 JUL00 0 0.00

AUG00 0 0.00

---------------------------------------- CUMULATIVE TOTAL 0 0.00

COVER ARMBOARD 9 INCH 8 ?/?? 0.000 0.000 0

MAY00 0 0.00 JUN00 0 0.00 JUL00 0

0.00

AUG00 0 0.00

---------------------------------------- CUMULATIVE TOTAL 0 0.00

KIT SHAVING-SURG PREP 104 1/KT 3.000 0.000 -15

MAY00 0 0.00 JUN00 0 0.00 JUL00 -13

0.00

AUG00 -14 0.00

---------------------------------------- CUMULATIVE TOTAL -27 0.00

Press RETURN to continue, '^' to exit:

USAGE DEMAND ITEM REPORT: MY STATIOM AUG 15, 2000@15:36:05 PAGE 2

USAGE DATE RANGE FROM MAY 2000 TO AUG 2000 (92 DAYS)

DESCRIPTION MI UNIT/IS LAST \$ AVG \$

ON-HAND

--------------------------------------------------------------------------

------

SOAP ANTISEP BAR 5C 31 1/BR 0.092 0.010 191

MAY00 0 0.00 JUN00 0 0.00 JUL00 -15

0.00

AUG00 -14 -0.14

---------------------------------------- CUMULATIVE TOTAL -29 -0.14

STERI PEEL 6 IN X 10 IN 47 1/EA 0.065 0.087

60

MAY00 0 0.00 JUN00 0 0.00 JUL00 -20

0.00

AUG00 0 0.00

---------------------------------------- CUMULATIVE TOTAL -20 0.00

TOSYLATE SYRINGE 50MG/10ML 101 1/EA 2.251 0.000

-21

MAY00 0 0.00 JUN00 0 0.00 JUL00 -12

0.00

AUG00 -20 0.00

---------------------------------------- CUMULATIVE TOTAL -32 0.00

\[END OF REPORT\]------------------------------------------------\[USER:IFUSER,ONE\]

### Transaction Register Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transaction Register Report \[PRCP TRANSACTION REG REPORT\] list all activity in an inventory point within a specified period of time.

Select Reports Menu Option: TRANsaction Register Report

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, USA

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

+--------------------------------------+

\|The Transaction Register Report prints\|

\|all activity for specified items, \|

\|including the opening and closing \|

\|balances. The current month-year \|

\|balance on file appears under the \|

\|calculated closing balance if the two \|

\|values differ. \|

+--------------------------------------+

+-------------------------------------+

\|Enter the month-year range for \|

\|printing the transaction register \|

+-------------------------------------+

Print Transaction Register for beginning MONTH and YEAR: JUN 2009//AUG 2000 (AUG 2000)

Print Transaction Register for ending MONTH and YEAR: DEC 2008//FEB 2001 (FEB 2001)

+-------------------------------------+

\|You may now select to print only \|

\|items whose calculated closing \|

\|balance differs from the current \|

\|on-hand inventory. \|

+-------------------------------------+

Display only items out of balance? NO// (NO)

To select ALL items, press RETURN.

Select ITEM MASTER NUMBER:

Do you want to select ALL items? \<YES/NO\> Y (YES)

DEVICE: HOME// UCX/TELNET

\<\*\> please wait \<\*\>

TRANSACTION REGISTER REPORT FOR MY STATION AUG 15, 2001@15:34:38 PAGE 1

FOR THE MONTH OF AUG 2000

NSN DESCRIPTION \[#MI\]

TRANSID DT TRANS./P.O. U/I SELLUNIT SELL \$ QTY INV \$

--------------------------------------------------------------------------

6505-01-A99-1234A TOSYLATE SYRINGE 50MG/10ML \[#101\] U/I: 1/EA

DUE-IN: 0 DUE-OUT: 0

ISSUABLE + NONISSUABLE OPEN BALANCE: -11 24.76

U19 04 to: IFPATIENT,ONE 1/EA 0.000 0.00 -11 0.00

vend DECREASES INVENTORY

U23 04 to: IFPATIENT,ONE 1/EA 0.000 0.00 1 0.00

return INCREASES INVENTORY

U27 08 to: IFPATIENT,ONE 1/EA 0.000 0.00 -11 0.00

vend DECREASES INVENTORY

U31 08 to: IFPATIENT,ONE 1/EA 0.000 0.00 1 0.00

return INCREASES INVENTORY

CLOSING BALANCE: -31 24.76

\*\*\* CURRENT INVENTORY BALANCES: -21 24.76

6508-01-027-2103 SOAP ANTISEP BAR 5C \[#31\] U/I: 1/BR

DUE-IN: 0 DUE-OUT: 0

ISSUABLE + NONISSUABLE OPEN BALANCE: 198 1.95

Press RETURN to continue, '^' to exit:

TRANSACTION REGISTER REPORT FOR MY STATION AUG 15, 2001@15:34:38 PAGE 2

FOR THE MONTH OF AUG 2000

NSN DESCRIPTION \[#MI\]

TRANSID DT TRANS./P.O. U/I SELLUNIT SELL \$ QTY INV \$

--------------------------------------------------------------------------

U17 04 to: IFPATIENT,ONE 1/BR 0.010 -0.11 -11 -0.11

vend DECREASES INVENTORY

U21 04 to: IFPATIENT,ONE 1/BR 0.010 0.04 4 0.04

return INCREASES INVENTORY

U25 08 to: IFPATIENT,ONE 1/BR 0.010 -0.11 -11 -0.11

vend DECREASES INVENTORY

U29 08 to: IFPATIENT,ONE 1/BR 0.010 0.04 4 0.04

return INCREASES INVENTORY

CLOSING BALANCE: 184 1.81

\*\*\* CURRENT INVENTORY BALANCES: 191 1.88

6515-00-103-6659 KIT SHAVING-SURG PREP \[#104\] U/I: 1/KT

DUE-IN: 0 DUE-OUT: 0

ISSUABLE + NONISSUABLE OPEN BALANCE: -8 36.00

U20 04 to: IFPATIENT,ONE 1/KT 0.000 0.00 -10 0.00

vend DECREASES INVENTORY

Press RETURN to continue, '^' to exit:

TRANSACTION REGISTER REPORT FOR MY STATION AUG 15, 2001@15:34:38 PAGE 3

FOR THE MONTH OF AUG 2000

NSN DESCRIPTION \[#MI\]

TRANSID DT TRANS./P.O. U/I SELLUNIT SELL \$ QTY INV \$

--------------------------------------------------------------------------

U24 04 to: IFPATIENT,ONE 1/KT 0.000 0.00 3 0.00

return INCREASES INVENTORY

U28 08 to: IFPATIENT,ONE 1/KT 0.000 0.00 -10 0.00

vend DECREASES INVENTORY

U32 08 to: IFPATIENT,ONE 1/KT 0.000 0.00 3 0.00

return INCREASES INVENTORY

CLOSING BALANCE: -22 36.00

\*\*\* CURRENT INVENTORY BALANCES: -15 36.00

6515-00-241-3931 ARM BOARD 9 INCH LONG \[#7\] U/I: 2/RO

DUE-IN: 0 DUE-OUT: 0

ISSUABLE + NONISSUABLE OPEN BALANCE: 0 0.00

CLOSING BALANCE: 0 0.00

6515-00-799-8049 COVER ARMBOARD 9 INCH \[#8\] U/I: ?/??

DUE-IN: 0 DUE-OUT: 0

ISSUABLE + NONISSUABLE OPEN BALANCE: 0 0.00

Press RETURN to continue, '^' to exit:

TRANSACTION REGISTER REPORT FOR MY STATION AUG 15, 2001@15:34:38 PAGE 4

FOR THE MONTH OF AUG 2000

NSN DESCRIPTION \[#MI\]

TRANSID DT TRANS./P.O. U/I SELLUNIT SELL \$ QTY INV \$

--------------------------------------------------------------------------

CLOSING BALANCE: 0 0.00

6530-01-258-0953 STERI PEEL 6 IN X 10 IN \[#47\] U/I: 1/EA

DUE-IN: 0 DUE-OUT: 0

ISSUABLE + NONISSUABLE OPEN BALANCE: 60 5.20

U18 04 to: DOE,JOHN 1/EA 0.087 -0.87 -10 -0.87

vend DECREASES INVENTORY

U22 04 to: IFPATIENT,ONE 1/EA 0.087 0.87 10 0.87

return INCREASES INVENTORY

U26 08 to: IFPATIENT,ONE 1/EA 0.087 -0.87 -10 -0.87

vend DECREASES INVENTORY

U30 08 to: IFPATIENT,ONE 1/EA 0.087 0.87 10 0.87

return INCREASES INVENTORY

CLOSING BALANCE: 60 5.20

7510-C1-887-1287 CATS \[#12002\] U/I: 1/EA

DUE-IN: 0 DUE-OUT: 0

ISSUABLE + NONISSUABLE OPEN BALANCE: 0 0.00

Press RETURN to continue, '^' to exit:

TRANSACTION REGISTER REPORT FOR MY STATION AUG 15, 2001@15:34:38 PAGE 5

FOR THE MONTH OF AUG 2000

NSN DESCRIPTION \[#MI\]

TRANSID DT TRANS./P.O. U/I SELLUNIT SELL \$ QTY INV \$

--------------------------------------------------------------------------

CLOSING BALANCE: 0 0.00

TRANSACTION TYPE (TT) ABBREVIATIONS: U = USAGE

R = RECEIVING A = MANUAL ADJUSTMENT

D = DISTRIBUTION (REGULAR ISSUES) S = ASSEMBLE SETS

C = DISTRIBUTION (CALL-IN) P = PHYSICAL COUNT

E = DISTRIBUTION (EMERGENCY)

\[END OF REPORT\]------------------------------------------------\[USER:IFUSER,ONE\]

\<Press RETURN to continue\>

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These bulletins will be sent to the inventory point managers when there are problems with the HL7 transactions or information in the transactions. Reasons for rejection are varied. Some messages explain what needs to be done to correct the error. If the error is encountered while during the first phase off message processing, while validating the information in the HL7 transaction, the bulletin will contain the HL7 transaction. This transaction may be deciphered using appendix 3 of this manual.

The HL7 transaction number appearing in the message is a composite number representing the files in which the transaction is stored. The format for the HL7 transaction number is:

\<File 773 ien\> . \<File 772 ien\>. \<optional 447.1\>

The optional 447.1 suffix will appear only in cases where the error was found in the second phase of processing. This is the phase when information is being pulled from the AUTOMATED SUPPLY STATION PROCESSSING QUEUE (file 447.1) by the tasked PRCP2 SUPPLY STATION TXN RUN job.

Messages that will appear in these bulletins include:

HL7 transaction \#HLTXN has missing or unexpected segments.

HL7 transaction \#HLTXN has the wrong message type.

HL7 transaction \#HLTXN has a bad order control code in ORC.

HL7 transaction \#HLTXN has a bad order control code/activity.

HL7 transaction \#HLTXN has bad values in the QRD fields.

HL7 transaction \#HLTXN has an indication that the supply station could not

> respond.

HL7 transaction \#HLTXN has an order not in GIP or primary is unknown.

HL7 transaction \#HLTXN has Please remove this order from the supply station.

HL7 transaction \#HLTXN has activity on a posted order.

HL7 transaction \#HLTXN has order activity rejected by GIP.

All Posting activity for this order must be done on GIP.

HL7 transaction \#HLTXN has no order number.

HL7 transaction \#HLTXN has an inventory point not in GIP.

HL7 transaction \#HLTXN has an IP that is not a secondary.

HL7 transaction \#HLTXN has a secondary IP not in the order.

HL7 transaction \#HLTXN has an invalid site specified.

HL7 transaction \#HLTXN has no station specified.

HL7 transaction \#HLTXN has a non-supply station IP.

HL7 transaction \#HLTXN has an excessive quantity transacted.

HL7 transaction \#HLTXN has an excessive quantity remaining.

HL7 transaction \#HLTXN has an item not in the order.

HL7 transaction \#HLTXN has an item not in the primary.

HL7 transaction \#HLTXN has an item not in the secondary.

HL7 transaction \#HLTXN has a non-supply station item.

HL7 transaction \#HLTXN has an invalid item.

HL7 transaction \#HLTXN has no item information.

HL7 transaction \#HLTXN has a case cart or instrument kit item.

Message indicating receipt of all ordered items was not processed.

> Please adjust the GIP to show this information.

GIP can't create a new record for HL7 transaction# HLTXN

Contact your IRM if GIP continues to have trouble creating records.

QTY unit(s) of item# ITEM NAME was/were

> taken for RECIPENT/returned from RECIPIENT/disposed of/adjusted

> out of the inventory/adjusted into the inventory

by STAFF MEMBER

Please adjust the GIP to show this information.

### Notification of Ordered Items without a Refill Amount 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message will be seen whenever an order being posted has items for which GIP did not successfully receive a refill transaction.

PRCP_NO_REFILL

Subj: "Notification of ordered items without a refill amount" \[#295408\]

Sent: 08 Aug 00 12:30 6 lines

From: SUPPLY STATION INTERFACE

--------------------------------------------------------------------------

GIP did not get refill information on the following items in order 89

to update 999-ONE PRIMARY or 999-MY STATION.

Please determine the correct quantities received and enter an emergency

order to correct the counts in the primary and secondary inventory points.

TOSYLATE SYRINGE 50MG/10ML

Enter message action (in IN basket): Ignore//

### Notification of trouble with an HL7 Refill Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message will be sent when GIP is unable to process a refill transaction received from the supply station.

PRCP_BAD_ORDER

Subj: Notification of trouble with an HL7 refill transaction \[#295568\]

13 Aug 00 06:05 10 lines

From: SUPPLY STATION INTERFACE In 'IN' basket. Page 1 \*New\*

--------------------------------------------------------------------------

An HL7 item refill/post order transaction on order \# 85 for the secondary

inventory point, 999-MY STATION, rejected.

Please note the problem and make any corrections.

HL7 transaction \#3784.27647 has order activity rejected by GIP.

All Posting activity for this order must be done on GIP.

MSH\|~^\\\|PRCP_SSTATION\|\|PRCP_SS_VISTA\|\|20000813000131\|\|ORM~O01\|98\|D\|2.3\|98\|\|AL\|NE

ORC\|OF\|85\|\|~999-MYSTATION\|\|\|\|\|20000813000000\|\*MIDNIGHT\*

RQD\|\|\|\|7~ARM BOARD 9 INCH LONG\|0

NTE\|1\|O\|5

Enter message action (in IN basket): Ignore//

### Notification of Error in HL7 Supply Station Activity Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message is sent anytime GIP is unable to process a Usage, Return, or Adjustment transaction sent from the supply station.

PRCP_BAD_ACTIVITY

Subj: Notification of error in HL7 supply station activity transaction

\[#295456\] 09 Aug 00 10:16 8 lines

From: SUPPLY STATION INTERFACE In 'IN' basket. Page 1

--------------------------------------------------------------------------

An HL7 utilization transaction for 999-MY STATION rejected.

HL7 transaction \#3462.27325 has an item not in the secondary.

item# 31 SOAP ANTISEP BAR 5C

MSH\|^~\\\|PRCP_SSTATION\|...\|PRCP_SS_VISTA\|...\|20000809101609\|\|RAS^O01\|0475\|D\|2.3\|\|\|AL\|AL\|

ORC\|RP\|0\|\|^999-MY STATION\|\|\|\|\|20000809101609\|Guser^user, GEORGE\|

RXA\|0\|1\|20000809101609\|\|31^SOAP ANTISEP BAR 5C\|0\|\|\|\|IFUSER^FIVE,

\|\|\|\|\|\|\|\|ADJI^inventory\|55\|

RXR\|\|\|\|\|

Enter message action (in IN basket): Ignore//

### Notification of Inventory Mismatches between Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message is sent whenever an order or activity transaction is received which indicates the on-hand amount for an item within the supply station differs from the amount in the inventory point. Transactions causing this message to be sent will be processed as long as there are no other errors.

PRCP_QTY_MISMATCH

Subj: Notification of inventory mismatches between systems \[#295504\] 10 Aug 00 09:59

5 lines

From: SUPPLY STATION INTERFACE In 'IN' basket. Page 1

--------------------------------------------------------------------------

An on-hand discrepancy with 999-MY STATION exists for

item SOAP ANTISEP BAR 5C (31).

The quantity in 999-MY STATION is 140

The quantity on the supply station is 55

(Information acquired from HL7 txn# 563.2757.447.1 )

Enter message action (in IN basket): Ignore//

### Notification of Rejection of HL7 On-Hand Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message is sent whenever GIP is unable to successfully process the supply station’s response to a quantity on-hand request.

PRCP_BAD_QUERY

Subj: Notification of rejection of HL7 on-hand transaction. \[#295561\]

11 Aug 00 16:14 16 lines

From: SUPPLY STATION INTERFACE In 'IN' basket. Page 1 \*New\*

--------------------------------------------------------------------------

A query on hand response for 999-MY STATION could not be processed. Please

place the request again.

HL7 transaction \#3782.27645 has an item not in the secondary.

item# 9999 Huffalumps

MSH\|~^\\\|PRCP_SSTATION\|\|PRCP_SS_VISTA\|\|20000811161615\|\|OSR~Q06\|97\|D\|2.3\|97\|\|AL\|NE

MSA\|AA\|9993780\|MESSAGE ACCEPTED

QRD\|20000811161615\|R\|D\|QOH\|\|\|\|\|STA\|\|\|S

ORC\|OK\|\|\|~999-MY STATION\|\|\|\|\|20000811161615

NTE\|1\|O\|104~KIT SHAVING-SURG PREP~25

NTE\|2\|O\|12002~CATS~111

NTE\|3\|O\|12013~WOOZLES~43

NTE\|4\|O\|31~SOAP ANTISEP BAR 5C~150

NTE\|5\|O\|47~STERI PEEL 6 IN X 10 IN~1129

NTE\|6\|O\|7~ARM BOARD 9 INCH LONG~5

NTE\|7\|O\|9999~Huffalumps~10

### List of Differences in Item Name between GIP and the Supply Station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message may be seen whenever any transaction received from the supply station contains an item name different from the name kept in GIP. Transactions causing this error will be processed if other errors are not present.

PRCP_ITEM_NAME

Subj: List item name differences between GIP and the Supply Station

\[#295220\] 04 Aug 00 09:59 5 lines

From: SUPPLY STATION INTERFACE In 'IN' basket. Page 1

--------------------------------------------------------------------------

There is a name discrepancy in 999-MY STATION for item

31

ON GIP:

STATION: SOAP ANTISEP BAR 5C

(Information acquired from HL7 txn# 549.2743.447.1)

Enter message action (in IN basket): Ignore//

### Notification of On-Hand Discrepancies found by a QOH Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message displays when a response received to an on-hand query shows on-hand quantities that differ from what is in the inventory point. This message is informational and does not result from an error in processing.

PRCP_ALL_ITEMS_QTY_UPDATE

Subj: Notification of on-hand discrepancies found by a QOH response.

\[#286930\] 15 May 00 13:51 9 lines

From: SUPPLY STATION INTERFACE In 'IN' basket. Page 1

--------------------------------------------------------------------------

A supply station QOH response was received for 999-MY STATION.

Please investigate any discrepancies listed below.

Quantities

SuplSta GIP Item No Description (first 30 chars) \*\*comments

------- ------- ------- -----------------------------------------------

32 0 7 ARM BOARD 9 INCH LONG

12 0 31 SOAP ANTISEP BAR 5C \*\*Not in supply station

Enter message action (in IN basket): Ignore//

### Notification of Items in a Supply Station not in GIP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message appears whenever the response to a quantity on-hand query contains items that are not in GIP. This message does not prevent processing of the remaining response unless there are other errors.

PRCP_BAD_ITEM_QOH

Subj: Notification of Items in Supply Station not in GIP \[#295739\] 23 Aug 00 15:56

2 lines

From: SUPPLY STATION INTERFACE In 'IN' basket. Page 1 \*New\*

--------------------------------------------------------------------------

The supply station for 999-MY STATION contains an item not in IFCAP.

Item: 9999~huffalumps.

(Information acquired from HL7 txn# 558.2752)

Enter message action (in IN basket): Ignore//

## Other messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new messages may display when accessing a supply station inventory

Point. They are as follows:

### Quantity Discrepancies Exist With The Supply Station.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message indicates a discrepancy in the quantity on-hand between a supply station and its linked secondary inventory point. The details related to this message are available in the Supply Station Quantity Discrepancy \[PRCP SS QTY DISCREPANCIES\] report. Adjusting the on-hand quantity in the supply station will also update the secondary inventory point but on-hand adjustments to the secondary inventory point will not be transmitted to the supply station.

4.6.2 There Are Unprocessed Supply Station Transactions.

This message indicates that the secondary inventory point has HL7 transactions from the supply station waiting to be processed into GIP. Transactions will not process if:

1.  there is activity in the secondary inventory point, or
2.  an order needs to be posted and there is activity occurring in the primary.

The Task Manager starts the job to process these transactions according to the parameters entered via the Schedule/Unschedule option. See ‘Processor for Supply Station Transactions’ in chapter 4.

Below is a display of the two new messages:

I N V E N T O R Y version 5.1

\(999\) Secondary Inventory Point: MY STATION IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> QUANTITY DISCREPANCIES EXIST WITH THE SUPPLY STATION.

--\> THERE ARE UNPROCESSED SUPPLY STATION TRANSACTIONS.

# This page intentionally left blank.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Setting your system up to use the supply station interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contact your supply station provider prior to setting up the interface. Schedule a time to bring up the interface that is convenient for the vendor, OA&MM staff, your IRM staff and system or network administrators. You may find it beneficial to hold a conference call of all the above parties to discuss which stations will be interfaced and what each group will do and when. Discuss the vendor’s availability and how to contact him over the first few days after the interface is in place. If you are using the supply cabinet for items from different departments and your secondary has only supply items, ask the vendor to restrict the transactions you receive to the items in your secondary.

PYXIS: Verify PYXIS has your site number so they may store it in their system as your facility code. This information is entered at the PYXIS console in the option to set up site demographics.

OMNICELL: OMNICELL will use your site code in populating the OMNICELL supplier mapping table. Supply stations should be added to this table only when they will be interfaced to GIP.

## Checklist for Network Administrator and IRM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set up the TCP/IP according to MLLP requirements and the HL7 components as outlined in these instructions and the VISTA Health Level Seven (HL7) Site Manager & Developer Manual. Verify the HL7 Site Parameters have already been set up at your site and use the manual to determine how to set them up if they are not yet defined.

Serial connections are inappropriate for this interface.

Many vendors will require a modem to use in dialing onto the system to help them in providing support. Recent attention to security issues may require you to make special arrangements prior to setting up this interface that will allow them the access they need to assist you when problems arise.

If you are running multiple Task Managers concurrently, you may also need to make arrangements to run them in DCL context. This step is necessary to afford you control and prevent HL7 messages from being rejected. Instructions for running TaskMan in DCL context are available in the Kernel Systems Manual.

Although the Point of Use interface does not exactly match existing interfaces, IRM staff supporting the patient file or the Computerized Patient Record System (CPRS) will have some experience with concepts needed to set this interface up.

### ### Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Update the applications

PRCP_SS_VISTA and

PRCP_SSTATION

to be ACTIVE using the option, EA Application Edit \[HL EDIT APPL PARAM\].

The other application protocol settings should be:

(STATUS) ACTIVE

COUNTRY CODE US

HL7 FIELD SEPARATOR \|

HL7 ENCODING CHARACTERS ~^\\

MAIL GROUP \<the name of a mail group at your site to receive

alerts from the HL7 package\>

> **NOTE:** Setting up the mail group on the application is recommended because it serves as an early alert to potential problems within the interface.

### Event Drivers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For test accounts, update the Processing ID field for all the event protocols listed to "D" for debug. In the production accounts, the processing ID will be pulled from the HL7 site parameters. Verify you have the site parameters set up and refer to the HL7 Site Manager and Development Manual if you need to set them up. Edits to the event drivers should be made through the option, EP Protocol Edit \[HL EDIT INTERFACE\].

PRCP EV INV UPDATE

PRCP EV ITEM UPDATE

PRCP EV QOH REQ

PRCP EV REFILL/POST

PRCP EV REL ORDER

### Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each vendor system (PYXIS, OMNICELL) you will use:

1\) INCOMING LINKS (Listeners)

1)  Get the IP address (from where the task manager runs) and a port number to use in receiving messages from the vendor's system into GIP. The National registry has reserved port number REDACTED for receiving transmissions from PYXIS (via the PRCPFRPYXS link) and REDACTED for messages from OMNICELL (via the PRCPFROMNI link).

> USE A DIFFERENT PORT NUMBER FOR EACH VENDOR.

> The following ports are reserved nationally for this interface.

> PYXIS REDACTED

> OMNICELL REDACTED

> Tell your administrator not to set up a new com file for the port and not to assign REDACTED for this interface. Use of REDACTED will complicate the ability to trouble shoot the interface. <u>Also note that the RPC Broker should not be running on the port you plan to use.</u> The Broker is NOT needed to support this interface.

> If you are running multiple task managers, you will need to run them in DCL context as specified in the VISTA Health Level Seven (HL7) Site Manager & Developer Manual. The Kernel Systems Manual explains how to run TaskMan with DCL context.

2)  Plug each IP address and port number into the appropriate incoming link via the EL-EDIT LINK \[HL EDIT LOGICAL LINKS\] option:

Use link PRCPFRPYXS for PYXIS, and link PRCPFROMNI for OMNICELL)

Autostart "Enable"

LLP Type "TCP"

TCP/IP Service Type "SINGLE LISTENER"

TCP/IP Address \<Use the IP address where Task Man runs\>

TCP/IP Port \<recommend REDACTED or REDACTED, as stated above\>

Exceeded Attempts Action \<return\>

Startup Node \<return\>

Persistent "YES"

2\) OUTGOING LINKS (Client)

1)  Get all IP addresses needed to add the supply station to the network.
2)  Decide with the vendor what IP address and port number to use on the vendor system to receive GIP transactions. If the vendor system is already operating at your site, the IP address you need will be the one at which the vendor’s server resides.
3)  Add the supply station system IP address and port number to the outgoing link for the appropriate vendor via the EL- EDIT LINK \[HL EDIT LOGICAL LINKS\] option:

(Use link PRCPSSPYXS for PYXIS, and link PRCPSSOMNI for OMNICELL)

Autostart "Enable"

LLP Type "TCP"

TCP/IP Service Type "CLIENT(SENDER)"

TCP/IP Address \<Provided by your network administrator\>

TCP/IP Port \<Discuss with vendor\>

Exceeded Attempts Action \<return\>

Startup Node \<return\>

Persistent "YES"

3\) Start up the links

### Check the System Manager and start the filers if none are running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions are available in the VISTA Health Level Seven (HL7) Site Manager & Developer Manual.

### Remaining Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After completing these steps, and after OA&MM completes the steps in the following section 5.2 (Checklist for the Secondary Inventory Points), complete the remaining steps in section 5.4 (Other Recommendations)

## Checklist for the Secondary Inventory Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

THERE MUST BE A ONE TO ONE RELATIONSHIP OF SUPPLY STATION TO

SECONDARY INVENTORY POINT.

1.  A secondary inventory point linked to a supply station can also be linked to one and only one primary inventory point.
2.  The supply station name must be the Inventory Point Name (Field \# .01 of the GENERIC INVENTORY FILE (#445)) preceded with your site number. For example if your Inventory Point Name is GOODS, the supply station name is 969-GOODS.
3.  Use the SUPPLY STATION PROVIDER prompt under the SPECIAL PARAMETERS option on the Edit Inventory Parameters Screen to enter your supply station vendor (PYXIS or OMNICELL) for this secondary. This screen is found in the Manager option, Enter/Edit Inventory And Distribution Points \[PRCP INVPT PARAM ENTER/EDIT\]. The SUPPLY STATION PROVIDER value will be stored in SS PROVIDER (field \#22 of the GENERIC INVENTORY FILE (#445)).
4.  Set KEEP PERPUTAL INVENTORY? (Field \#.5 of the GENERIC INVENTORY FILE (#445)) to YES. This allows access to all the GIP options you need.
5.  Set KEEP DETAILED TRANSACTION HISTORY (Field \#.6 of the GENERIC INVENTORY FILE (#445)) to YES. If NO, your supply station and inventory point activities will not be saved.
6.  Set UNIT OF ISSUE (Sub field# 4 of INVENTORY ITEM (field \#1) of the GENERIC INVENTORY FILE (#445)) to the unit that is given to the patient (lowest level of issue).
7.  Set the NORMAL STOCK LEVEL (Sub field \# 9 of INVENTORY ITEM (field \#1) of the GENERIC INVENTORY FILE (#445)) on items stocked in the supply station secondary greater than zero. A zero or no value indicates the item is not on the supply station.
8.  The secondary inventory point should not include any case cart or instrument kit items.

## Checklist for the Supply Station Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The supply station name must match the name of its associated secondary inventory point.
2.  The items stocked in the supply station must be associated with a single bin or partition in that station. Until this step is completed, the supply station does not recognize the item.

Linking one item to multiple bins within a supply station is NOT recommended

because the secondary inventory point is item-focused not bin-focused. Integrity issues

may result if an item is assigned to multiple bins.

3.  Item names in the supply station should be the same as the names in the secondary inventory point if you are using OMNICELL. PYXIS station names must agree with the Item Short Description (field \#.05) in the Item Master File (File 441)
4.  Ask your vendor for the maximum length on item names. Verify the items description in your secondary inventory point do not exceed this length if you are using OMNICELL and that the item short description in the Item Master File does not exceed this length if you are using PYXIS.
5.  Verify your item names do not contain the following punctuation characters:

> \| (pipe)

> ~ (tilde)

> ^ (caret or up-arrow)

6.  If you are currently using a supply station, please note that the process for refilling the supply station will change after the interface is in place. Refills will be done against an order that displays for selection on the cabinet’s screen.
7.  Additional instructions for setting up the supply station are available from the vendor.
8.  Balance the quantity on hand values

> Adjust the values, if necessary, so they are the same in the supply station and the secondary inventory point. Adjustments at the supply station will be sent to GIP but adjustments in GIP will not be sent to the supply station.

## Other Recommendations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Start the GIP Transaction Processing Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Schedule the HL7 processing job, \[PRCP2 SUPPLY STATION TXN RUN\], to run

via the Schedule/Unschedule Options \[XUTM SCHEDULE\] option.

Edit Option Schedule

Option Name: PRCP2 SUPPLY STATION TXN RUN

Menu Text: PROCESSOR FOR SUPPLY STATION TXN TASK ID: 238541

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: SEP 11,2000@14:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 300S \<== Suggested interval of 3-5 minutes

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Test the Interface 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before setting up multiple supply stations, verify the interface is functioning properly.

1.  Verify the supply station receives item information from GIP.
2.  Request a quantity on-hand update and verify GIP receives the station’s response.
3.  Create a distribution order for one item. Both PYXIS and OMNICELL will allow the order to post even if you enter a zero for the ordered item. Verify GIP shows the order as posted.
4.  Perform an adjustment or utilization transaction. Verify it shows up in GIP.

Do not use the "PI Ping (TCP Only) \[HL PING\] option under the Filer and Link Management options menu to test connectivity. This option is proprietary and handles only VISTA to VISTA connections. It is inappropriate for the Point of Use connections with vendor systems.

NOTES

Refills for supply station secondaries will be completed at the supply station by selecting a GIP generated order. Because the supply station systems are not bound by GIP rules keep the following points in mind:

1.  Posted distribution orders for a supply station secondary may cause the primary inventory’s on-hand amount to become negative. This will occur when the technician restocking the secondary specifies a restock amount greater than the on-hand amount in the primary.
2.  The refill amount entered at the supply station may conflict with the primary's unit of issue package multiple. The distribution order, generated by GIP, respects the unit of issue package multiple but the supply stations do not accommodate the multiple and, consequently, will not restrict a technician's entry. You may get around this by making the unit of issue multiple 1 for all items stocked in the supply station.
3.  The reverse distribution order is supported by the supply station systems. Know how your supply cabinets handle this functionality.
4.  The interface does not support processing of distribution for case carts and instrument kits. It is recommended that these items not be stocked in your supply station nor in its associated secondary inventory point.

ORDERS CANCELLED IN GIP MUST BE REMOVED MANUALLY FROM THE SUPPLY STATION.

### Ask the vendor about accessing information related to communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Both PYXIS and OMNICELL have internal interfaces. Their server receives and sends information from/to GIP. They also send and receive information to/from their own cabinet. Sometimes problems can occur that are internal to the vendor’s system.

It is beneficial to have staff on site that can check the vendor’s system to determine if transactions to GIP have been successfully built and acknowledged and that transactions are being successfully received from GIP.

## Appendix 1: Resolutions to Issues Raised by the Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Summary of issues covered in this section:

“I am not receiving information from the supply station”

The vendor is not receiving acknowledgements from VistA

1\. Check to see if the IP and port at the listener is working properly.

2\. Verify the PRCPFROMNI or PRCPFRPYXS link is set up properly .

3\. Verify that the link’s status is appropriate.

4\. Verify that the correct processes are running by listing all system jobs

5\. Verify that if multiple Task managers are running they are in DCL context.

The vendor is receiving acknowledgements from VistA

1\. Check the acknowledgements to see if they contain error text.

2\. Verify that the background filer is running.

“The supply station is not receiving information from GIP”

“I am getting several messages on name mismatches”

“Refreshing the Quantity on-hand does not update GIP”

“I continue to get quantity on-hand mismatch messages”

“The interface is down and I need to post my orders”

“The background job PRCP2 SUPPLY STATION TXN RUN is using too much resource”

“The bulletin tells me that some items on an order were not filled”

“The order posted but GIP received no refill amount on any of the items”

> **NOTE:** Both PYXIS and OMNICELL have internal interfaces. Their server receives and sends information from/to GIP. They also send and receive information to/from their own cabinet. Sometimes problems can occur that are internal to the vendor’s system.

It is beneficial to have some staff on site that can check the vendor system to determine if the vendor has built and successfully transmitted transactions to GIP and received them from GIP.

Issue Detail:

“I am not receiving information from the supply station”

> Verify that the vendor is receiving an acknowledgement.

> <u>If the vendor is not receiving acknowledgements from VistA,</u> connectivity issues, improperly set up VistA components, or vendor software problems may be the cause.

1)  Check to see if the IP and port at the listener is working properly. Try pinging the

> port by entering the following text at the VMS prompt

> Telnet \<space\> \<IP address\> \<space\> \<Port#\>

> If the ping is successful, the system will display instructions to escape, (\<cntl\> \]).

> To check to see if the port is busy, type UCX at the VMS prompt, then type

> ‘show dev’. You will see a table similar to the one displayed below.

> (Note: type ‘exit’ at the ucx prompt to escape ucx)

> UCX\> show dev

> Port Remote

> Device_socket Type Local Remote Service Host

> bg3 STREAM REDACTED 0 LPD REDACTED

> bg4 STREAM REDACTED 0 REXEC REDACTED

> bg5 STREAM REDACTED 0 RSH REDACTED

> bg6 STREAM REDACTED 0 TELNET REDACTED

> bg7 STREAM REDACTED 0 XMINET2005 REDACTED

> bg8 STREAM REDACTED 0 XMINET2010 REDACTED

> bg9 STREAM REDACTED 0 XMINET2011 REDACTED

> bg10 STREAM REDACTED 0 XMINET2012 REDACTED

> bg18 DGRAM REDACTED 0 REDACTED

> bg21 DGRAM REDACTED 0 REDACTED

> bg26 STREAM REDACTED 0 XMINETMM REDACTED

> bg28 STREAM REDACTED 0 XMPOP REDACTED

> bg30 STREAM REDACTED 0 XWB REDACTED

> bg5167 STREAM REDACTED 5500 REDACTED

=\> bg5169 STREAM REDACTED 5500 REDACTED

=\> bg5174 STREAM REDACTED 0 REDACTED

=\> bg5175 STREAM REDACTED 4137 REDACTED

> bg6451 STREAM REDACTED 1098 TELNET REDACTED

> bg6732 STREAM REDACTED 1591 TELNET REDACTED

> bg6736 STREAM REDACTED 1101 TELNET REDACTED

> bg6754 STREAM REDACTED 1050 TELNET REDACTED

> UCX\>

> You should see 3 entries for each vendor associated with this interface. In this case, the entries are bg5174, bg5175, and bg5169:

> bg5174 has your local port REDACTED and a remote port of REDACTED with an IP address of REDACTED. This line represents the listener.

> bg5175 shows a local port of REDACTED, a remote port that is not zero and the IP address of your vendor system. This link represents your connection from the vendor to your system.

> bg5169 has a non-zero local port, the vendor’s remote port and the vendor’s IP address. This link represents a connection to the vendor.

If the IP addresses are all zero, it means there is no connection.

> The UCX-type table is usually displayed on PC systems after entering the following text at a DOS prompt:

> Netstat \<space\> -an \<return\>

2)  Verify that the PRCPFROMNI or PRCPFRPYXS link is connected to the correct IP address and port on VistA. This is the same address and port the vendor uses when sending transactions to VistA.
3)  Verify that the link’s status is reading or alternating between reading and idle. If on VMS, you may use the following function in VMS to verify the system link monitor is accurately displaying the link’s status:

To display all active HL7 listeners, type the following at the VMS prompt:

Show \<space\> sys/cluster/proc=HLS\* \<return\>

The response may look something like this:

OpenVMS V7.1-2 on node ISC2A1 24-JAN-2001 14:26:44.95 Uptime 43 03:10:08

Pid Process Name State Pri I/O CPU Page flts Pages

20264D07 HLSrv:170 HIB 5 8915 0 00:00:03.17 368 203

2025CF51 HLSrv:171 HIB 5 8877 0 00:00:02.97 337 187

> The number after HLSrv: is the ien of the link. You can find out the name of the link by viewing ^HLCS(870,ien,0).

4)  Verify that the correct processes are running by listing all system jobs

> Processes in DSM Environment DSMMANAG on NODE ISC2A1, 30-JAN-2001 09:16

> PID Process Name State Device UCI,VOL Routine Cmds Refs DIO Login

> 2026815F HLClnt:173 HIB DEV,FEY HLCSTCP2 362411 130820 261 14:39

> 2029991A HLClnt:172 HIB DEV,FEY HLCSTCP2 363338 130996 906 14:45

> 202662BA HLSrv:174 HIB DEV,FEY HLCSTCP1 457601 58384 770 15:10

> 20273300 CZEKAJ_9872 CUR TNA771 DEV,FEX %SY 511402 17601 1653 08:32

> 2024548A BTask 314307 HIB DEV,FEY HLCSIN 113609 973206 32049 07:50

> 2026815F HLClnt:173 HIB DEV,FEY HLCSTCP2 362411 130820 261 14:39

> 20244C99 BTask 314308 HIB DEV,FEY HLCSOUT 614295 177121 1427 07:52

> 20200292 BTask 293858 HIB MNT,DEM HLCSIN 794732 208292 77114 11:18

> 20200283 BTask 484829 HIB DEV,FEX HLCSMM1 319878 505071 10 11:18

> 20200276 HLmgr:484823 HIB DEV,FEX HLCSLM 123283 257545 87921 11:18

> 2026815F HLClnt:173 HIB DEV,FEY HLCSTCP2 362411 130820 261 14:39

> 20200276 HLmgr:484823 HIB DEV,FEX HLCSLM 123283 257545 87921 11:18

> 20200280 BTask 484828 HIB DEV,FEX HLCSOUT 149394 430506 1784 11:18

> 20272CD5 IFUSER

> LEF TNA770 MNT,VBB DIED 109586 117631 2886 08:18

> 2020025C BTask 484825 HIB DEV,FEX HLCSIN 196597 -19574 54195 11:17

> 2020025A BTask 293859 HIB MNT,DEM HLCSOUT 142826 411919 7433 11:17

> 2020023C DSM_DDP03_29 HIB 573 11:16

> 2020023B DSM_DDP02_29 HIB 17 11:16

> 2020023A DSM_DDP01_29 HIB 184 11:16

> 20200239 DSM_RECOVER_29 HIB 1220 11:16

> 20272E4F SU_8671 LEF TNA773 MNT,VBB XMJDIR 42680 5302 447 09:05

> 20200237 DSM_GARCOL_29 HIB 20363 11:16

> 20200236 DSM_DEMON_29 HIB 838265 11:16

> Process names starting:

> HLClnt:nnn where nnn is the ien of a link represents the job sending data to the vendor. In this interface, the link’s name in the HL7 application is PRCPSSOMNI or PRCPSSPYXS.

> HLSrvnnn: where nnn is the ien of a listening link represents the job associated with the link receiving data from the vendor. In this interface, this link’s name in the HL7 application is PRCPFROMNI or PRCPFRPYXS.

> BTask with a routine of HLCSIN or HLCSOUT represent inbound and outbound filer jobs.

> BTask with a routine of HLCSLM represent the Link Manager job

> BTask with a routine of HLCSMM1 represent the HL7 protocol job for MailMan

5)  If you are running multiple task managers concurrently and not in DCL context, verify the listener is running on the right node.

> To determine the correct node, first get the job number. Use the VMS statement ‘Show \<space\> sys/cluster/proc=HLS\*’ as in the above example to get the job number.

> Once you have the job number, use the option Number Base Changer from Kernel to convert the job number to hexadecimal. Within the routine enter at the Base prompt 10, then enter your task number. The number returned is in hexadecimal. In VMS enter the text ‘show process/ID=\<hexadecimal number\>’. The response indicates the node on which the process is running. If this node is not correct, both you and the vendor will need to update the link information in you systems to use the IP address corresponding to the correct node.

> NOTE: you can avoid this problem by running TaskMan in DCL context.

<u>If the vendor is receiving acknowledgements from VistA</u>, the problem could be that

the transactions are being rejected by VistA or that the Point of Use Filer is not

running.

> 1\) Verify the vendor is not receiving acknowledgements with error messages in

> them. These error messages will appear in the MSA segment. Two examples are

> shown:

> MSA\|CR\|1111\|Processing ID Mismatch with Event Driver

In this case, you need to verify all the event protocols for this interface are

populated with a processing ID only if the interface is being run from the test or

training system. If it is being run from the production system, the field in the

protocol should be blank and the site parameters should indicate the system is a

production system.

> MSA\|CR\|281\|Receiving Application is Inactive

> Indicates the HL7 applications (PRCP_SSTATION and PRCP_SS_VISTA) are

> inactive. In this case, transactions will be re-sent after the applications are

> activated. If there has been extensive traffic in the time the interface has been

> down, you may end up with an error, causing some transactions to be lost.

> 2\) Verify that the background filer is running

> You can do this by verifying the task PRCP2 SUPPLY STATION TXN RUN is scheduled to run in the Task Manager and that it reschedules according to its defined rescheduling frequency.

“The supply station is not receiving information from GIP”

1)  Verify that the PRCPSSOMNI (OMNICELL) or PRCPSSPYXS (PYXIS) link is up.
2)  Verify that the vendor is receiving transactions. It could be that the vendor system has been unable to process what it is receiving.

“I am getting several messages on name mismatches”

1)  Correct the name in the secondary inventory point if you are using OMNICELL and in file 441 if you are using PYXIS.
2)  If the names appear to be the same on the message, there may be trailing spaces in the GIP name. You can edit the name to remove these spaces.
3)  Verify the length of the names in GIP does not exceed the limit provided by your vendor.
4)  Verify the names in the vendor system are in upper case, just as in GIP and that they do not contain the following characters: (\|) pipe,(~) tilde, or (^) caret.

“Refreshing the Quantity on-hand does not update GIP”

1)  The Supply Station Quantity Discrepancy Report has an option to refresh the supply station quantity on-hand. The option does refresh the totals in GIP but not GIP’s quantity on-hand. The fields refreshed are 2 new fields introduced by patch PRC\*5.1\*1. These are the supply station quantity on-hand and the date and time the last message was received from the supply station.

“I continue to get quantity on-hand mismatch messages”

The quantity on-hand mismatch message results when the supply station value reported to VistA does not agree with GIP’s quantity on-hand for an item. If you are putting up the interface for the first time on a station, you often need to adjust the inventory in GIP. Because of timing considerations, you may need to adjust the quantity on some of the items more than once.

If the interface has been working well, new problems may be caused by the following:

- lost transactions
- errored transactions
- posting of emergency or call-in orders for supply station items

> (These orders update the quantity in the secondary but not the supply station)

- storing an item in more than one bin of the supply station

The best way to determine the problem is to print for the item a transaction register report in GIP and compare it to the transaction log generated off the supply station system.

“The interface is down and I need to post my orders”

If the orders are already refilled on the supply station, but the supply station activity is not being communicated to GIP, contact your IRM. When the problem cannot be resolved in a timely manner, use the Remove Supply Station Flag option in the Primary Manager’s Menu to allow posting to be done in GIP. Prior to posting the order in GIP, remember to edit the ordered quantities to be the quantities actually refilled in the supply station. Please also note that posting in GIP will restrict the quantity to not exceed the amount in the primary.

When the interface comes up, the supply station refill messages for this order will be rejected and you will get a MailMan message.

If the order did not reach the supply station, you may delete the regular order and post an emergency or call-in order. This step may result in mismatches even if you adjust the totals in the supply station. The reason for the mismatch is that all transactions occurring on the supply station, including adjustments, are transmitted to the secondary inventory point. Therefore, the secondary is updated by the order (due to the emergency or call-in order) and then again by the adjustment to the supply station. You can refill the items using a supply station generated order. Refills on supply station generated orders will be transmitted to GIP but will reject because the supply station order number does not exist in GIP.

“The background job PRCP2 SUPPLY STATION TXN RUN is using too much resource”

This has been a sign that there was an error incurred while processing a transaction. The symptoms included an incomplete record entry in file 447.1 and a job that appeared to be looping in routine PRCPHL70. One of the HL7 filers also had locked the problem record in file 447.1. The error was discovered by checking for a PRCPHL\* routine in the error monitor. Beyond repairing the bug in the PRCPHL\* routine, it was necessary to:

1.  Determine what caused the error to create an environment where the error would not recur before the code could be fixed. This may mean changing a feature of the inventory point or supply station, removing the flag indicating they are linked to one another, or taking down the interface.
2.  Determine what the transaction was trying to do and notify supply of the unprocessed transaction
3.  Remove the problem record from file 447.1 via a DIK call
4.  Stop and Restart the problem filer which has the bad record locked. This action will also serve to purge any variables set up by the defective process.

“The bulletin tells me that some items on an order were not filled”

This message indicates GIP either did not receive or could not process transactions on items in a GIP order from the supply station. Possible causes include items not assigned to bins in the supplier, items not being labeled by the supplier as supply items, and the rejection of item refill transactions due to bad information or changing the GIP item to be a non-supply station item. Users will get MailMan messages on these rejections. Transactions producing name and/or quantity mismatch messages will be processed unless there is some other error.

“The Order posted but GIP received no refill amount on any of the items”

If you are using OMNICELL, verify the system did not ‘age’ the order. You may set the aging period yourself. As an order reaches this length of time, OMNICELL will remove it from their system. If the order is for a station linked to an inventory point, they will also send GIP a transaction indicating the order is complete.

## Appendix 2: HL7 Implementation for Point of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix provides an overview of the HL7 transaction packets that are used by this interface.

#### Message

This is HL7’s unit of communication. It conveys a single activity and takes the following format:

Header Segment (MSH)

Segment Name \<delimiter\> \<field\> \<delimiter\> \<field\> \<delimiter\>…

Segment Name \<delimiter\> \<field\> \<delimiter\> \<field\> \<delimiter\>…

The Message Header (MSH)

Sequence Element Name Comments

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 44%" />
<col style="width: 41%" />
</colgroup>
<tbody>
<tr class="odd">
<td>1</td>
<td>Field Separator</td>
<td>| (the pipe character)</td>
</tr>
<tr class="even">
<td>2</td>
<td>Encoding Characters</td>
<td>~^\&amp;</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sending Application</td>
<td>PRCP_SS_VISTA or PRCP_SSTATION</td>
</tr>
<tr class="even">
<td>4</td>
<td>Sending Facility</td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Receiving Application</td>
<td>PRCP_SS_VISTA or PRCP_SSTATION</td>
</tr>
<tr class="even">
<td>6</td>
<td>Receiving Facility</td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Date/Time of Message</td>
<td>YYYYMMDDHHMMSS</td>
</tr>
<tr class="even">
<td>8</td>
<td>Security</td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>Message Type</td>
<td><p>Message ~Event</p>
<p>This denotes a type of activity or information contained in the message and implies the segments that will be included in the message</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>Message Control ID</td>
<td>System generated number, in VISTA this number is preceded with the site number</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Processing ID</td>
<td><p>P – Production Mode</p>
<p>T –Test Mode</p>
<p>D – Debug Mode</p>
<p>(In Vista, pulled from Site Parameters unless overrode in event protocol)</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>Version ID</td>
<td>HL7 version to use (2.3)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>Sequence Number</td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td>Continuation Pointer</td>
<td></td>
</tr>
<tr class="odd">
<td>15</td>
<td>Accept Acknowledgement Type</td>
<td><p>AL – Always</p>
<p>NE - Never</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>Application Acknowledgement Type</td>
<td><p>AL – Always</p>
<p>NE - Never</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>Country Code</td>
<td></td>
</tr>
<tr class="even">
<td>18</td>
<td>Character Set</td>
<td></td>
</tr>
<tr class="odd">
<td>19</td>
<td>Principal Language of Message</td>
<td></td>
</tr>
</tbody>
</table>

Each receiving system will respond to these messages with an acknowledgement. The acknowledgement transaction will always include an MSH segment and an MSA segment.

MSA

Sequence Element Name Comments

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>1</td>
<td>Acknowledgment Code</td>
<td><p>AA – Application Acknowledge</p>
<p>AE – Application Error</p>
<p>AR - Application Reject</p>
<p>CA – Commit Acknowledge</p>
<p>CE – Commit Error</p>
<p>CR – Commit Reject</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>Message Control ID</td>
<td>(of the message it is responding to)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Text Message</td>
<td>If an error occurred, there may be some text here</td>
</tr>
<tr class="even">
<td>4</td>
<td>Expected Sequence Number</td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Delayed Acknowledgement Type</td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>Error Condition</td>
<td></td>
</tr>
</tbody>
</table>

Within this interface, the following Message /Event Types are used:

#### Sent to the Supply Station

Message Event Activity

MFN Z01 Item Record Updates

ORM O01 Order Notifications

OSQ Q06 Quantity On Hand Query

#### Received from the Supply Station

Message Event Activity

ORM O01 Item Refill

ORM O01 Order Complete

OSR Q06 Quantity on Hand Response (Application

> acknowledgement to OSQ/QO6 message)

RAS O01 Inv. Activity (Adjustment, Disposal, Return, Usage)

Specific information may be obtained from the HL7 Manual (VISTA Health Level Seven Site Manager & Developer Manual) and through the data dictionaries.

HL7 messages used in this interface are kept in 2 separate files.

1.  File 773 (^HLMA) contains the MSH segment
2.  File 772 (^HL(772,) contains the remaining segments

File 773 (HL7 MESSAGE ADMINISTRATION) contains the MSH segment which is built by the VA HL7 package. A status of the transaction is stored at the P node. These statuses are outlined in the HL7 manual and include:

1 Pending transmission

1.5 Being transmitted

1.7 Awaiting response

2 Awaiting application acknowledgment

3 Successfully completed

4 Error

5 Error during generation

6 Error during processing

7 Application level error

8 Being generated

9 Awaiting processing

File 773 also contains the internal entry number to the File 772 record.

The file has the following cross-references:

“AC” (Set only while the transaction is in processing)

^HLMA(“AC”,”O” or “I”, Link#, ien)

where O denotes outbound transactions,

I denotes inbound transactions

Link# refers to the ien in file 870 for the link supporting the transaction

ien is the internal entry number to file 773 (^HLMA)

“AD” Date/Time File

^HLMA(“AD”,YYYMMDD.HHMMSS, ien)

where YYY is the FileMan year

ien is the internal entry number to file 773 (^HLMA)

^HLMA(“AH”, receiving application#, message control ID, ien)

where receiving application# is the ien in file 771 (^HL(771,)) for the receiving

> application (PRCP_SS_VISTA for GIP or PRCP_SSTATION for the

> supply station)

message control ID is a unique number to identify the transaction

ien is the internal entry number to file 773 (^HLMA)

^HLMA(“C”, message control ID, ien)

message control ID is a unique number to identify the transaction

ien is the internal entry number to file 773 (^HLMA)

HL(772 (HL7 MESSAGE TEXT)

Contains all but the MSH segment. These segments, unlike the MSH are built by GIP.

For ACK transactions, the MSA segment will contain the message processing ID of the originating message. If errors occur, the message of the error will also be displayed here.

## Appendix 3: Point of Use HL7 Message Details 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All transactions are transmitted within the MLLP specifications outlined in the (Health Level Seven) HL7 standard and are packaged as follows:

Starting block = ASCII 11

Data

Carriage return

Ending block = ASCII 28

Carriage return

#### Item Attribute Edit

Message Type: MFN Event Type: Z01

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SS_VISTA</p>
<p>PRCP_SSTATION</p>
<p>(date/time of transaction)</p>
<p>MFN~Z01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

#### MFI

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="sequence" class="unnumbered">Sequence</h4></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p></td>
<td><p>60</p>
<p>180</p>
<p>3</p>
<p>26</p>
<p>26</p>
<p>2</p></td>
<td><p>R</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>R</p></td>
<td><p>445~Generic Inventory</p>
<p>UPD</p>
<p>&lt;YYYYMMDDHHMMSS&gt;</p>
<p>NE</p></td>
<td><p>Master File Identifier</p>
<p>Master File Application Identifier</p>
<p>File-Level Event Code</p>
<p>Entered Date/Time</p>
<p>Effective Date Time</p>
<p>Response Level Code</p></td>
</tr>
</tbody>
</table>

#### MFE

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p></td>
<td><p>3</p>
<p>20</p>
<p>26</p>
<p>200</p></td>
<td><p>R</p>
<p>C</p>
<p>O</p>
<p>R</p></td>
<td><p>MAD &lt;if adding&gt;</p>
<p>MDL &lt;if deleting&gt;</p>
<p>MUP &lt;if editing&gt;</p>
<p>&lt;Item ID&gt; ~ &lt;Item Name&gt;</p></td>
<td><p>Record-Level Event Code</p>
<p>MFN Control ID</p>
<p>Effective Date/Time</p>
<p>Primary Key Value - MFE</p></td>
</tr>
</tbody>
</table>

# #### ZIM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 49%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p></td>
<td><p>70</p>
<p>40</p>
<p>7</p>
<p>7</p>
<p>7</p>
<p>35</p>
<p>7</p>
<p>11</p>
<p>??</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>&lt;Item Number&gt; ~ &lt;Item Name&gt;</p>
<p>&lt;Supply Station Code, not used&gt; ~ &lt;Supply Station Name, formatted as NNN-TEXT&gt;</p>
<p>&lt;numeric (patient units), if exists&gt;</p>
<p>&lt;numeric (patient units), if exists&gt;</p>
<p>&lt;numeric (patient units), if exists&gt;</p>
<p>&lt;2 character code&gt; ~ &lt;30 character Unit Name, not used&gt;</p>
<p>&lt;numeric, (conversion factor from restock to patient units)&gt;</p>
<p>&lt;decimal number, if exists&gt;</p></td>
<td><p>Entry being changed</p>
<p>Location affected by change</p>
<p>Normal Level</p>
<p>Standard Reorder Point</p>
<p>Emergency Level</p>
<p>Unit of Issue</p>
<p>Conversion Factor</p>
<p>Last Cost</p>
<p>UPN</p></td>
</tr>
</tbody>
</table>

#### Item Name Edit

Message Type: MFN Event Type:Z01

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SS_VISTA</p>
<p>PRCP_SSTATION</p>
<p>(date/time of transaction)</p>
<p>MFN~Z01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

#### MFI

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="sequence-1" class="unnumbered">Sequence</h4></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p></td>
<td><p>60</p>
<p>180</p>
<p>3</p>
<p>26</p>
<p>26</p>
<p>2</p></td>
<td><p>R</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>R</p></td>
<td><p>441~item Master</p>
<p>UPD</p>
<p>&lt;YYYYMMDDHHMMSS&gt;</p>
<p>NE</p></td>
<td><p>Master File Identifier</p>
<p>Master File Application Identifier</p>
<p>File-Level Event Code</p>
<p>Entered Date/Time</p>
<p>Effective Date Time</p>
<p>Response Level Code</p></td>
</tr>
</tbody>
</table>

#### MFE

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p></td>
<td><p>3</p>
<p>20</p>
<p>26</p>
<p>200</p></td>
<td><p>R</p>
<p>C</p>
<p>O</p>
<p>R</p></td>
<td><p>MAD &lt;if adding&gt;</p>
<p>MDL &lt;if deleting&gt;</p>
<p>MUP &lt;if editing&gt;</p>
<p>&lt;Item ID&gt; ~ &lt;Item Name&gt;</p></td>
<td><p>Record-Level Event Code</p>
<p>MFN Control ID</p>
<p>Effective Date/Time</p>
<p>Primary Key Value - MFE</p></td>
</tr>
</tbody>
</table>

#### Distribution Order Detail Notification

Message Type: ORM Event Type:O01

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SS_VISTA</p>
<p>PRCP_SSTATION</p>
<p>(date/time of transaction)</p>
<p>ORM~O01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

## #### #### The following 3 segments repeat. Each segment appears once for each item ordered.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ORC

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p></td>
<td><p>2</p>
<p>22</p>
<p>22</p>
<p>22</p>
<p>2</p>
<p>1</p>
<p>200</p>
<p>200</p>
<p>26</p>
<p>120</p>
<p>120</p>
<p>120</p>
<p>80</p>
<p>40</p>
<p>26</p>
<p>200</p>
<p>60</p>
<p>60</p>
<p>120</p>
<p>40</p>
<p>60</p>
<p>106</p>
<p>48</p>
<p>106</p></td>
<td><p>R</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>RF &lt;code for refill order request&gt;</p>
<p>&lt;GIP Order Number, 6 digit number&gt;</p>
<p>&lt;Supply Station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p>
<p>&lt;order release or resend, formatted YYYYMMDDHHMMSS&gt;</p>
<p>&lt;User ID, use 0&gt; ~&lt;User releasing or sending transaction in HL7 format e.g. Last~First~MI&gt;</p></td>
<td><p>Order Control</p>
<p>Placer Order Number</p>
<p>Filler Order Number</p>
<p>Placer Group Number</p>
<p>Order Status</p>
<p>Response Flag</p>
<p>Quantity/Timing</p>
<p>Parent</p>
<p>Date/Time of Transaction</p>
<p>Entered By</p>
<p>Verified By</p>
<p>Ordering Provider</p>
<p>Enterer’s Location</p>
<p>Call Back Phone Number</p>
<p>Order Effective Date/Time</p>
<p>Order Control Code Reason</p>
<p>Entering Organization</p>
<p>Entering Device</p>
<p>Action By</p>
<p>Advanced Beneficiary Notice Code</p>
<p>Ordering Facility Name</p>
<p>Ordering Facility Address</p>
<p>Ordering Facility Phone Number</p>
<p>Ordering Provider Address</p></td>
</tr>
</tbody>
</table>

#### RQD

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p></td>
<td><p>4</p>
<p>60</p>
<p>60</p>
<p>60</p>
<p>6</p>
<p>60</p>
<p>30</p>
<p>30</p>
<p>60</p>
<p>8</p></td>
<td><p>O</p>
<p>C</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>&lt;Item ID, numeric&gt; ~ &lt;Item Name&gt;</p>
<p>&lt;number ranging from –999999 to 999999 in restock units.&gt;</p>
<p>&lt;restock unit&gt;</p></td>
<td><p>Requisition Line Number</p>
<p>Item Code – Internal</p>
<p>Item Code – External</p>
<p>Hospital Item Code</p>
<p>Requisition Quantity</p>
<p>Requisition Unit of Measure</p>
<p>Department Cost Center</p>
<p>Item Natural Account Code</p>
<p>Deliver To ID<br />
Date Needed</p></td>
</tr>
</tbody>
</table>

#### NTE

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p></td>
<td><p>4</p>
<p>8</p>
<p>64k</p></td>
<td>O<br />
O<br />
O</td>
<td><p>1</p>
<p>RQD (implies addendum to RQD)</p>
<p>&lt;conversion factor&gt; ~ &lt;patient issue units&gt;</p></td>
<td><p>Set ID – NTE</p>
<p>Source of Comment</p>
<p>Comment</p></td>
</tr>
</tbody>
</table>

Note that the units of issue can change after an order was placed and before the time the refill is logged.

#### Refills

Message Type: ORM Event Type: 001 (ORS 001)

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SSTATION</p>
<p>PRCP_SS_VISTA</p>
<p>YYYYMMDDHHMMSS</p>
<p>ORM~O01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

#### ORC

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p></td>
<td><p>2</p>
<p>22</p>
<p>22</p>
<p>22</p>
<p>2</p>
<p>1</p>
<p>200</p>
<p>200</p>
<p>26</p>
<p>120</p>
<p>120</p>
<p>120</p>
<p>80</p>
<p>40</p>
<p>26</p>
<p>200</p>
<p>60</p>
<p>60</p>
<p>120</p>
<p>40</p>
<p>60</p>
<p>106</p>
<p>48</p>
<p>106</p></td>
<td><p>R</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>OF &lt;order refilled as requested&gt;</p>
<p>&lt;GIP Order Number, 6 digit number&gt;</p>
<p>&lt;Supply Station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p>
<p>&lt;refill time, formatted YYYYMMDDHHMMSS&gt;</p>
<p>&lt;User refilling the item in HL7 format e.g. Last~First~M.I.&gt;</p></td>
<td><p>Order Control</p>
<p>Placer Order Number</p>
<p>Filler Order Number</p>
<p>Placer Group Number</p>
<p>Order Status</p>
<p>Response Flag</p>
<p>Quantity/Timing</p>
<p>Parent</p>
<p>Date/Time of Transaction</p>
<p>Entered By</p>
<p>Verified By</p>
<p>Ordering Provider</p>
<p>Enterer’s Location</p>
<p>Call Back Phone Number</p>
<p>Order Effective Date/Time</p>
<p>Order Control Code Reason</p>
<p>Entering Organization</p>
<p>Entering Device</p>
<p>Action By</p>
<p>Advanced Beneficiary Notice Code</p>
<p>Ordering Facility Name</p>
<p>Ordering Facility Address</p>
<p>Ordering Facility Phone Number</p>
<p>Ordering Provider Address</p></td>
</tr>
</tbody>
</table>

#### #### #### RQD

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p></td>
<td><p>4</p>
<p>60</p>
<p>60</p>
<p>60</p>
<p>6</p>
<p>60</p>
<p>30</p>
<p>30</p>
<p>60</p>
<p>8</p></td>
<td><p>O</p>
<p>C</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>&lt;Item ID&gt; ~ &lt;Item Name, up to 60 char max&gt;</p>
<p>&lt;Quantity received, in restock units between the range of –999999 to 999999&gt;</p></td>
<td><p>Requisition Line Number</p>
<p>Item Code – Internal</p>
<p>Item Code – External</p>
<p>Hospital Item Code</p>
<p>Requisition Quantity</p>
<p>Requisition Unit of Measure</p>
<p>Department Cost Center</p>
<p>Item Natural Account Code</p>
<p>Deliver To ID<br />
Date Needed</p></td>
</tr>
</tbody>
</table>

#### NTE

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p></td>
<td><p>4</p>
<p>8</p>
<p>64k</p></td>
<td>O<br />
O<br />
O</td>
<td><p>1</p>
<p>O (letter O for other system)</p>
<p>&lt;Quantity on hand after, in patient units after refill was completed. Numbers range from –999999 to 999999&gt;</p></td>
<td><p>Set ID – NTE</p>
<p>Source of Comment</p>
<p>Comment</p></td>
</tr>
</tbody>
</table>

#### Order Completion

Message Type: ORM Event Type: 001 (^ORS 001)

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SSTATION</p>
<p>PRCP_SS_VISTA</p>
<p>YYYYMMDDHHMMSS</p>
<p>ORM~O01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

#### ORC

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p></td>
<td><p>2</p>
<p>22</p>
<p>22</p>
<p>22</p>
<p>2</p>
<p>1</p>
<p>200</p>
<p>200</p>
<p>26</p>
<p>120</p>
<p>120</p>
<p>120</p>
<p>80</p>
<p>40</p>
<p>26</p>
<p>200</p>
<p>60</p>
<p>60</p>
<p>120</p>
<p>40</p>
<p>60</p>
<p>106</p>
<p>48</p>
<p>106</p></td>
<td><p>R</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>FU &lt; for order refilled, unsolicited&gt;</p>
<p>&lt;GIP Order Number, 6 digit number&gt;</p>
<p>&lt;Supply Station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p>
<p>&lt; formatted YYYYMMDDHHMMSS&gt;</p>
<p>&lt;User completing the refill in HL7 format e.g. Last~First~M.I.&gt;</p></td>
<td><p>Order Control</p>
<p>Placer Order Number</p>
<p>Filler Order Number</p>
<p>Placer Group Number</p>
<p>Order Status</p>
<p>Response Flag</p>
<p>Quantity/Timing</p>
<p>Parent</p>
<p>Date/Time of Transaction</p>
<p>Entered By</p>
<p>Verified By</p>
<p>Ordering Provider</p>
<p>Enterer’s Location</p>
<p>Call Back Phone Number</p>
<p>Order Effective Date/Time</p>
<p>Order Control Code Reason</p>
<p>Entering Organization</p>
<p>Entering Device</p>
<p>Action By</p>
<p>Advanced Beneficiary Notice Code</p>
<p>Ordering Facility Name</p>
<p>Ordering Facility Address</p>
<p>Ordering Facility Phone Number</p>
<p>Ordering Provider Address</p></td>
</tr>
</tbody>
</table>

#### Quantity on Hand Query

Message Type: OSQ Event Type: Q06

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SS_VISTA</p>
<p>PRCP_SSTAION</p>
<p>(date/time of transaction - YYYYMMDDHHMMSS)</p>
<p>OSQ^Q06</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>AL</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

#### #### QRD

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p></td>
<td><p>26</p>
<p>1</p>
<p>1</p>
<p>10</p>
<p>1</p>
<p>26</p>
<p>10</p>
<p>60</p>
<p>60</p>
<p>60</p>
<p>20</p>
<p>1</p></td>
<td><p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p></td>
<td><p>&lt;formatted YYYYMMDDHHMMSS&gt;</p>
<p>R</p>
<p>D</p>
<p>QOH</p>
<p>STA</p>
<p>S</p></td>
<td><p>Query Date/Time</p>
<p>Query Format Code</p>
<p>Query Priority</p>
<p>Query ID</p>
<p>Deferred Response Type</p>
<p>Deferred Response Date/Time</p>
<p>Quantity Limited Request</p>
<p>Who Subject Filter</p>
<p>What Subject Filter</p>
<p>What Department Data Code</p>
<p>What Data Code Value Qual.</p>
<p>Query Results Level</p></td>
</tr>
</tbody>
</table>

#### QRF

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p></td>
<td><p>20</p>
<p>26</p>
<p>26</p>
<p>60</p>
<p>60</p>
<p>12</p>
<p>12</p>
<p>12</p>
<p>60</p></td>
<td><p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>Supply Station</p>
<p>&lt;Supply station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p></td>
<td><p>Where Subject Filter</p>
<p>When Data Start Date/Time</p>
<p>When Data End Date/Time</p>
<p>What User Qualifier</p>
<p>Other QRY Subject Filter</p>
<p>Which Date/Time Qualifier</p>
<p>Which Date/Time Status Qualifier</p>
<p>Date/Time Selection Qualifier</p>
<p>When Quantity/Timing Qualifier</p></td>
</tr>
</tbody>
</table>

#### Quantity On Hand Information

Message Type: OSR Event Type: Q06

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SSTATION</p>
<p>PRCP_SS_VISTA</p>
<p>(YYYYMMDDHHMMSS)</p>
<p>OSR^Q06</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

## #### MSA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p></td>
<td><p>2</p>
<p>20</p>
<p>80</p>
<p>15</p>
<p>1</p>
<p>100</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>B</p>
<p>O</p></td>
<td><p>AA, AE, or AR &lt;for Application accept, error or reject&gt;</p>
<p>&lt;&gt;</p>
<p>&lt;First line of reason for error&gt;</p>
<p>1</p></td>
<td><p>Acknowledgement Code</p>
<p>Message Control ID</p>
<p>Text Message</p>
<p>Expected Sequence Number</p>
<p>Delayed Acknowledgement type</p>
<p>Error Condition</p></td>
</tr>
</tbody>
</table>

## #### ERR (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>80</td>
<td>R</td>
<td>&lt;additional space for reason for error&gt;</td>
<td>Error Code and Location</td>
</tr>
</tbody>
</table>

## #### QRD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p></td>
<td><p>26</p>
<p>1</p>
<p>1</p>
<p>10</p>
<p>1</p>
<p>26</p>
<p>10</p>
<p>60</p>
<p>60</p>
<p>60</p>
<p>20</p>
<p>1</p></td>
<td><p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p></td>
<td><p>&lt;formatted YYYYMMDDHHMMSS&gt;</p>
<p>R &lt;for record oriented response&gt;</p>
<p>D &lt;for deferred&gt;</p>
<p>QOH</p>
<p>STA &lt;for Status&gt;</p>
<p>S &lt; for status only&gt;</p></td>
<td><p>Query Date/Time</p>
<p>Query Format Code</p>
<p>Query Priority</p>
<p>Query ID</p>
<p>Deferred Response Type</p>
<p>Deferred Response Date/Time</p>
<p>Quantity Limited Request</p>
<p>Who Subject Filter</p>
<p>What Subject Filter</p>
<p>What Department Data Code</p>
<p>What Data Code Value Qual.</p>
<p>Query Results Level</p></td>
</tr>
</tbody>
</table>

## #### ORC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p></td>
<td><p>2</p>
<p>22</p>
<p>22</p>
<p>22</p>
<p>2</p>
<p>1</p>
<p>200</p>
<p>200</p>
<p>26</p>
<p>120</p>
<p>120</p>
<p>120</p>
<p>80</p>
<p>40</p>
<p>26</p>
<p>200</p>
<p>60</p>
<p>60</p>
<p>120</p>
<p>40</p>
<p>60</p>
<p>106</p>
<p>48</p>
<p>106</p></td>
<td><p>R</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>OK &lt; for order accepted &amp; OK&gt;</p>
<p>&lt;Supply Station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p>
<p>&lt;QOH time, formatted YYYYMMDDHHMMSS&gt;</p></td>
<td><p>Order Control</p>
<p>Placer Order Number</p>
<p>Filler Order Number</p>
<p>Placer Group Number</p>
<p>Order Status</p>
<p>Response Flag</p>
<p>Quantity/Timing</p>
<p>Parent</p>
<p>Date/Time of Transaction</p>
<p>Entered By</p>
<p>Verified By</p>
<p>Ordering Provider</p>
<p>Enterer’s Location</p>
<p>Call Back Phone Number</p>
<p>Order Effective Date/Time</p>
<p>Order Control Code Reason</p>
<p>Entering Organization</p>
<p>Entering Device</p>
<p>Action By</p>
<p>Advanced Beneficiary Notice Code</p>
<p>Ordering Facility Name</p>
<p>Ordering Facility Address</p>
<p>Ordering Facility Phone Number</p>
<p>Ordering Provider Address</p></td>
</tr>
</tbody>
</table>

(The following segment occurs for each item in the supply station.)

#### NTE

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p></td>
<td><p>4</p>
<p>8</p>
<p>64k</p></td>
<td>O<br />
O<br />
O</td>
<td><p>(sequence number in item list)</p>
<p>O (letter O for other system)</p>
<p>&lt;Item ID&gt; ~ &lt;Item Name&gt; ~ &lt;Quantity on hand after, in patient units. Values range from –999999 to 999999&gt;</p></td>
<td><p>Set ID – NTE</p>
<p>Source of Comment</p>
<p>Comment</p></td>
</tr>
</tbody>
</table>

#### Adjustments

Message Type: RAS Event Type: 001

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SSTATION</p>
<p>PRCP_SS_VISTA</p>
<p>(YYYYMMDDHHMMSS)</p>
<p>RAS~O01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

#### PID (optional)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p>
<p>25</p>
<p>26</p>
<p>27</p>
<p>28</p>
<p>29</p>
<p>30</p></td>
<td><p>4</p>
<p>20</p>
<p>20</p>
<p>20</p>
<p>48</p>
<p>48</p>
<p>26</p>
<p>1</p>
<p>48</p>
<p>1</p>
<p>106</p>
<p>4</p>
<p>40</p>
<p>40</p>
<p>60</p>
<p>1</p>
<p>3</p>
<p>20</p>
<p>16</p>
<p>25</p>
<p>20</p>
<p>3</p>
<p>60</p>
<p>2</p>
<p>2</p>
<p>4</p>
<p>60</p>
<p>80</p>
<p>26</p>
<p>1</p></td>
<td><p>O</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>B</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>0</p>
<p>&lt;Patient name in Last~First~MI or other recipient of supplies as last name&gt;</p></td>
<td><p>Set ID – Patient ID</p>
<p>Patient Id (External ID)</p>
<p>Patient ID (Internal ID)</p>
<p>Alternate Patient ID – PID</p>
<p>Patient Name</p>
<p>Mother’s Maiden Name</p>
<p>Date/Time of Birth</p>
<p>Sex</p>
<p>Patient Alias</p>
<p>Race</p>
<p>Patient Address</p>
<p>County Code</p>
<p>Phone Number – Home</p>
<p>Phone Number – Business</p>
<p>Primary Language</p>
<p>Marital Status</p>
<p>Religion</p>
<p>Patient Account Number</p>
<p>SSN Number – Patient</p>
<p>Driver’s License Number - Patient</p>
<p>Mother’s Identifier</p>
<p>Ethnic Group</p>
<p>Birth Place</p>
<p>Multiple Birth Indicator</p>
<p>Birth Order</p>
<p>Citizenship</p>
<p>Veterans Military Status</p>
<p>Nationality</p>
<p>Patient Death Date and Time</p>
<p>Patient Death Indicator</p></td>
</tr>
</tbody>
</table>

#### #### ORC

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p></td>
<td><p>2</p>
<p>22</p>
<p>22</p>
<p>22</p>
<p>2</p>
<p>1</p>
<p>200</p>
<p>200</p>
<p>26</p>
<p>120</p>
<p>120</p>
<p>120</p>
<p>80</p>
<p>40</p>
<p>26</p>
<p>200</p>
<p>60</p>
<p>60</p>
<p>120</p>
<p>40</p>
<p>60</p>
<p>106</p>
<p>48</p>
<p>106</p></td>
<td><p>R</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>RP &lt;for order replace requested&gt;</p>
<p>0</p>
<p>&lt;Supply Station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p>
<p>&lt;time of adjustment, formatted YYYYMMDDHHMMSS&gt;</p></td>
<td><p>Order Control</p>
<p>Placer Order Number</p>
<p>Filler Order Number</p>
<p>Placer Group Number</p>
<p>Order Status</p>
<p>Response Flag</p>
<p>Quantity/Timing</p>
<p>Parent</p>
<p>Date/Time of Transaction</p>
<p>Entered By</p>
<p>Verified By</p>
<p>Ordering Provider</p>
<p>Enterer’s Location</p>
<p>Call Back Phone Number</p>
<p>Order Effective Date/Time</p>
<p>Order Control Code Reason</p>
<p>Entering Organization</p>
<p>Entering Device</p>
<p>Action By</p>
<p>Advanced Beneficiary Notice Code</p>
<p>Ordering Facility Name</p>
<p>Ordering Facility Address</p>
<p>Ordering Facility Phone Number</p>
<p>Ordering Provider Address</p></td>
</tr>
</tbody>
</table>

#### RXA

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p></td>
<td><p>4</p>
<p>4</p>
<p>26</p>
<p>26</p>
<p>100</p>
<p>20</p>
<p>60</p>
<p>60</p>
<p>200</p>
<p>200</p>
<p>200</p>
<p>20</p>
<p>20</p>
<p>60</p>
<p>20</p>
<p>26</p>
<p>60</p>
<p>200</p>
<p>200</p>
<p>2</p>
<p>2</p></td>
<td><p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>0</p>
<p>1</p>
<p>&lt;formatted YYYYMMDDHHMMSS&gt;</p>
<p>&lt;Item ID,&gt; ~ &lt;Item Name, up to 60 char max&gt;</p>
<p>&lt;Quantity transacted in patient units, absolute value&gt;</p>
<p>&lt;User Code, use 0&gt; ~&lt;Name of User doing the adjustment, formatted in HL7 e.g. LAST,FIRST,MI&gt;</p>
<p>&lt;Code&gt; ~ &lt;Reason for adjustment&gt;</p>
<p>Code = ADJ I for inventory increases, ADJD for decreases</p>
<p>&lt;Quantity remaining after adjustments were completed, number ranging from –999999 to 999999 in patient units)</p></td>
<td><p>Give Sub-ID Counter</p>
<p>Administration Sub-ID Counter</p>
<p>Date/Time Start of Administration</p>
<p>Date/Time End of Administration</p>
<p>Administered code</p>
<p>Administered Amount</p>
<p>Administered Unite</p>
<p>Administered Dosage</p>
<p>Administered Note</p>
<p>Administered Provider</p>
<p>Administered-at Location</p>
<p>Administered Per (Time Unit)</p>
<p>Administered Strength</p>
<p>Administered Strength Units</p>
<p>Substance Lot Number</p>
<p>Substance Expiration Date</p>
<p>Substance Manufacturer Name</p>
<p>Substance Refusal Reason</p>
<p>Indication</p>
<p>Completion Status</p>
<p>Action Code-RXA</p></td>
</tr>
</tbody>
</table>

## #### RXR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p></td>
<td><p>60</p>
<p>60</p>
<p>60</p>
<p>60</p>
<p>60</p></td>
<td><p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td>OTH</td>
<td><p>Route</p>
<p>Site</p>
<p>Administration Device</p>
<p>Administration Method</p>
<p>Routing Instruction</p></td>
</tr>
</tbody>
</table>

#### Discards

Message Type: RAS Event Type:O01

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SSTATION</p>
<p>PRCP_SS_VISTA</p>
<p>(YYYYMMDDHHMMSS)</p>
<p>RAS~O01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

## ## ## ## ## ## #### #### PID (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p>
<p>25</p>
<p>26</p>
<p>27</p>
<p>28</p>
<p>29</p>
<p>30</p></td>
<td><p>4</p>
<p>20</p>
<p>20</p>
<p>20</p>
<p>48</p>
<p>48</p>
<p>26</p>
<p>1</p>
<p>48</p>
<p>1</p>
<p>106</p>
<p>4</p>
<p>40</p>
<p>40</p>
<p>60</p>
<p>1</p>
<p>3</p>
<p>20</p>
<p>16</p>
<p>25</p>
<p>20</p>
<p>3</p>
<p>60</p>
<p>2</p>
<p>2</p>
<p>4</p>
<p>60</p>
<p>80</p>
<p>26</p>
<p>1</p></td>
<td><p>O</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>B</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>0</p>
<p>&lt;Patient name in Last~First~MI or other recipient of supplies as last name&gt;</p></td>
<td><p>Set ID – Patient ID</p>
<p>Patient Id (External ID)</p>
<p>Patient ID (Internal ID)</p>
<p>Alternate Patient ID – PID</p>
<p>Patient Name</p>
<p>Mother’s Maiden Name</p>
<p>Date/Time of Birth</p>
<p>Sex</p>
<p>Patient Alias</p>
<p>Race</p>
<p>Patient Address</p>
<p>County Code</p>
<p>Phone Number – Home</p>
<p>Phone Number – Business</p>
<p>Primary Language</p>
<p>Marital Status</p>
<p>Religion</p>
<p>Patient Account Number</p>
<p>SSN Number – Patient</p>
<p>Driver’s License Number - Patient</p>
<p>Mother’s Identifier</p>
<p>Ethnic Group</p>
<p>Birth Place</p>
<p>Multiple Birth Indicator</p>
<p>Birth Order</p>
<p>Citizenship</p>
<p>Veterans Military Status</p>
<p>Nationality</p>
<p>Patient Death Date and Time</p>
<p>Patient Death Indicator</p></td>
</tr>
</tbody>
</table>

#### ORC

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p></td>
<td><p>2</p>
<p>22</p>
<p>22</p>
<p>22</p>
<p>2</p>
<p>1</p>
<p>200</p>
<p>200</p>
<p>26</p>
<p>120</p>
<p>120</p>
<p>120</p>
<p>80</p>
<p>40</p>
<p>26</p>
<p>200</p>
<p>60</p>
<p>60</p>
<p>120</p>
<p>40</p>
<p>60</p>
<p>106</p>
<p>48</p>
<p>106</p></td>
<td><p>R</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>RP &lt;for order replace requested&gt;</p>
<p>0</p>
<p>&lt;Supply Station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p>
<p>&lt;time of adjustment, formatted YYYYMMDDHHMMSS&gt;</p></td>
<td><p>Order Control</p>
<p>Placer Order Number</p>
<p>Filler Order Number</p>
<p>Placer Group Number</p>
<p>Order Status</p>
<p>Response Flag</p>
<p>Quantity/Timing</p>
<p>Parent</p>
<p>Date/Time of Transaction</p>
<p>Entered By</p>
<p>Verified By</p>
<p>Ordering Provider</p>
<p>Enterer’s Location</p>
<p>Call Back Phone Number</p>
<p>Order Effective Date/Time</p>
<p>Order Control Code Reason</p>
<p>Entering Organization</p>
<p>Entering Device</p>
<p>Action By</p>
<p>Advanced Beneficiary Notice Code</p>
<p>Ordering Facility Name</p>
<p>Ordering Facility Address</p>
<p>Ordering Facility Phone Number</p>
<p>Ordering Provider Address</p></td>
</tr>
</tbody>
</table>

#### RXA

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p></td>
<td><p>4</p>
<p>4</p>
<p>26</p>
<p>26</p>
<p>100</p>
<p>20</p>
<p>60</p>
<p>60</p>
<p>200</p>
<p>200</p>
<p>200</p>
<p>20</p>
<p>20</p>
<p>60</p>
<p>20</p>
<p>26</p>
<p>60</p>
<p>200</p>
<p>200</p>
<p>2</p>
<p>2</p></td>
<td><p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>0</p>
<p>1</p>
<p>&lt;formatted YYYYMMDDHHMMSS&gt;</p>
<p>&lt;Item ID,&gt; ~ &lt;Item Name, up to 60 char max&gt;</p>
<p>&lt;Quantity transacted in patient units (absolute value)&gt;</p>
<p>&lt;User Code, use 0&gt; ~&lt;Name of User disposing of the supplies, formatted in HL7 e.g. LAST,FIRST,MI&gt;</p>
<p>DISP ~ &lt;Reason for adjustment&gt; ALWAYS DECREASES</p>
<p>INVENTORY</p>
<p>&lt;Quantity remaining after disposal, number ranging from –999999 to 999999 in patient units)</p></td>
<td><p>Give Sub-ID Counter</p>
<p>Administration Sub-ID Counter</p>
<p>Date/Time Start of Administration</p>
<p>Date/Time End of Administration</p>
<p>Administered code</p>
<p>Administered Amount</p>
<p>Administered Unite</p>
<p>Administered Dosage</p>
<p>Administered Note</p>
<p>Administered Provider</p>
<p>Administered-at Location</p>
<p>Administered Per (Time Unit)</p>
<p>Administered Strength</p>
<p>Administered Strength Units</p>
<p>Substance Lot Number</p>
<p>Substance Expiration Date</p>
<p>Substance Manufacturer Name</p>
<p>Substance Refusal Reason</p>
<p>Indication</p>
<p>Completion Status</p>
<p>Action Code-RXA</p></td>
</tr>
</tbody>
</table>

## #### RXR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p></td>
<td><p>60</p>
<p>60</p>
<p>60</p>
<p>60</p>
<p>60</p></td>
<td><p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td>OTH</td>
<td><p>Route</p>
<p>Site</p>
<p>Administration Device</p>
<p>Administration Method</p>
<p>Routing Instruction</p></td>
</tr>
</tbody>
</table>

#### #### #### #### #### #### #### #### Returns

Message Type: RAS Event Type: O01

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SSTATION</p>
<p>PRCP_SS_VISTA</p>
<p>(YYYYMMDDHHMMSS)</p>
<p>RAS~O01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

#### PID (optional)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p>
<p>25</p>
<p>26</p>
<p>27</p>
<p>28</p>
<p>29</p>
<p>30</p></td>
<td><p>4</p>
<p>20</p>
<p>20</p>
<p>20</p>
<p>48</p>
<p>48</p>
<p>26</p>
<p>1</p>
<p>48</p>
<p>1</p>
<p>106</p>
<p>4</p>
<p>40</p>
<p>40</p>
<p>60</p>
<p>1</p>
<p>3</p>
<p>20</p>
<p>16</p>
<p>25</p>
<p>20</p>
<p>3</p>
<p>60</p>
<p>2</p>
<p>2</p>
<p>4</p>
<p>60</p>
<p>80</p>
<p>26</p>
<p>1</p></td>
<td><p>O</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>B</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>0</p>
<p>&lt;Patient name in Last~First~MI or other recipient returning supplies as last name&gt;</p></td>
<td><p>Set ID – Patient ID</p>
<p>Patient Id (External ID)</p>
<p>Patient ID (Internal ID)</p>
<p>Alternate Patient ID – PID</p>
<p>Patient Name</p>
<p>Mother’s Maiden Name</p>
<p>Date/Time of Birth</p>
<p>Sex</p>
<p>Patient Alias</p>
<p>Race</p>
<p>Patient Address</p>
<p>County Code</p>
<p>Phone Number – Home</p>
<p>Phone Number – Business</p>
<p>Primary Language</p>
<p>Marital Status</p>
<p>Religion</p>
<p>Patient Account Number</p>
<p>SSN Number – Patient</p>
<p>Driver’s License Number - Patient</p>
<p>Mother’s Identifier</p>
<p>Ethnic Group</p>
<p>Birth Place</p>
<p>Multiple Birth Indicator</p>
<p>Birth Order</p>
<p>Citizenship</p>
<p>Veterans Military Status</p>
<p>Nationality</p>
<p>Patient Death Date and Time</p>
<p>Patient Death Indicator</p></td>
</tr>
</tbody>
</table>

#### #### ORC

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p></td>
<td><p>2</p>
<p>22</p>
<p>22</p>
<p>22</p>
<p>2</p>
<p>1</p>
<p>200</p>
<p>200</p>
<p>26</p>
<p>120</p>
<p>120</p>
<p>120</p>
<p>80</p>
<p>40</p>
<p>26</p>
<p>200</p>
<p>60</p>
<p>60</p>
<p>120</p>
<p>40</p>
<p>60</p>
<p>106</p>
<p>48</p>
<p>106</p></td>
<td><p>R</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>LI &lt; for link order to patient care&gt;</p>
<p>0</p>
<p>&lt;Supply Station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p>
<p>&lt;time of adjustment, formatted YYYYMMDDHHMMSS&gt;</p></td>
<td><p>Order Control</p>
<p>Placer Order Number</p>
<p>Filler Order Number</p>
<p>Placer Group Number</p>
<p>Order Status</p>
<p>Response Flag</p>
<p>Quantity/Timing</p>
<p>Parent</p>
<p>Date/Time of Transaction</p>
<p>Entered By</p>
<p>Verified By</p>
<p>Ordering Provider</p>
<p>Enterer’s Location</p>
<p>Call Back Phone Number</p>
<p>Order Effective Date/Time</p>
<p>Order Control Code Reason</p>
<p>Entering Organization</p>
<p>Entering Device</p>
<p>Action By</p>
<p>Advanced Beneficiary Notice Code</p>
<p>Ordering Facility Name</p>
<p>Ordering Facility Address</p>
<p>Ordering Facility Phone Number</p>
<p>Ordering Provider Address</p></td>
</tr>
</tbody>
</table>

#### RXA

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p></td>
<td><p>4</p>
<p>4</p>
<p>26</p>
<p>26</p>
<p>100</p>
<p>20</p>
<p>60</p>
<p>60</p>
<p>200</p>
<p>200</p>
<p>200</p>
<p>20</p>
<p>20</p>
<p>60</p>
<p>20</p>
<p>26</p>
<p>60</p>
<p>200</p>
<p>200</p>
<p>2</p>
<p>2</p></td>
<td><p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>0</p>
<p>1</p>
<p>&lt;formatted YYYYMMDDHHMMSS&gt;</p>
<p>&lt;Item ID,&gt; ~ &lt;Item Name, up to 60 char max&gt;</p>
<p>&lt;Quantity transacted in absolute value&gt;</p>
<p>&lt;User Code, use 0&gt; ~&lt;Name of User returning the supplies, formatted in HL7 e.g. LAST,FIRST,MI&gt;</p>
<p>RTRN ~ &lt;Reason for return&gt; INCREASES INVENTORY</p>
<p>&lt;Quantity remaining, number ranging from –999999 to 999999 in patient units)</p></td>
<td><p>Give Sub-ID Counter</p>
<p>Administration Sub-ID Counter</p>
<p>Date/Time Start of Administration</p>
<p>Date/Time End of Administration</p>
<p>Administered code</p>
<p>Administered Amount</p>
<p>Administered Unite</p>
<p>Administered Dosage</p>
<p>Administered Note</p>
<p>Administered Provider</p>
<p>Administered-at Location</p>
<p>Administered Per (Time Unit)</p>
<p>Administered Strength</p>
<p>Administered Strength Units</p>
<p>Substance Lot Number</p>
<p>Substance Expiration Date</p>
<p>Substance Manufacturer Name</p>
<p>Substance Refusal Reason</p>
<p>Indication</p>
<p>Completion Status</p>
<p>Action Code-RXA</p></td>
</tr>
</tbody>
</table>

## #### RXR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p></td>
<td><p>60</p>
<p>60</p>
<p>60</p>
<p>60</p>
<p>60</p></td>
<td><p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td>OTH</td>
<td><p>Route</p>
<p>Site</p>
<p>Administration Device</p>
<p>Administration Method</p>
<p>Routing Instruction</p></td>
</tr>
</tbody>
</table>

#### Usage

Message Type: RAS Event Type: O01

#### MSH

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p></td>
<td><p>1</p>
<p>4</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>180</p>
<p>26</p>
<p>40</p>
<p>7</p>
<p>20</p>
<p>3</p>
<p>8</p>
<p>15</p>
<p>180</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>6</p>
<p>60</p></td>
<td><p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>|</p>
<p>~^\&amp;</p>
<p>PRCP_SSTATION</p>
<p>PRCP_SS_VISTA</p>
<p>(YYYYMMDDHHMMSS)</p>
<p>RAS~O01</p>
<p>(number)</p>
<p>P (production) or D (debug)</p>
<p>2.3</p>
<p>AL</p>
<p>NE</p>
<p>US</p></td>
<td><p>Field Separator</p>
<p>Encoding Characters</p>
<p>Sending Application</p>
<p>Sending Facility</p>
<p>Receiving Application</p>
<p>Receiving Facility</p>
<p>Date/Time Of Message</p>
<p>Security</p>
<p>Message Type</p>
<p>Message Control ID</p>
<p>Processing ID</p>
<p>Version ID</p>
<p>Sequence Number</p>
<p>Continuation Pointer</p>
<p>Accept Acknowledgement Type</p>
<p>Application Acknowledgment Type</p>
<p>Country Code</p>
<p>Character Set</p>
<p>Principal Language Of Message</p></td>
</tr>
</tbody>
</table>

#### #### #### #### #### #### #### #### #### PID 

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p>
<p>25</p>
<p>26</p>
<p>27</p>
<p>28</p>
<p>29</p>
<p>30</p></td>
<td><p>4</p>
<p>20</p>
<p>20</p>
<p>20</p>
<p>48</p>
<p>48</p>
<p>26</p>
<p>1</p>
<p>48</p>
<p>1</p>
<p>106</p>
<p>4</p>
<p>40</p>
<p>40</p>
<p>60</p>
<p>1</p>
<p>3</p>
<p>20</p>
<p>16</p>
<p>25</p>
<p>20</p>
<p>3</p>
<p>60</p>
<p>2</p>
<p>2</p>
<p>4</p>
<p>60</p>
<p>80</p>
<p>26</p>
<p>1</p></td>
<td><p>O</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>B</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>0</p>
<p>&lt;Patient name in Last~First~MI or other recipient of supplies as last name&gt;</p></td>
<td><p>Set ID – Patient ID</p>
<p>Patient Id (External ID)</p>
<p>Patient ID (Internal ID)</p>
<p>Alternate Patient ID – PID</p>
<p>Patient Name</p>
<p>Mother’s Maiden Name</p>
<p>Date/Time of Birth</p>
<p>Sex</p>
<p>Patient Alias</p>
<p>Race</p>
<p>Patient Address</p>
<p>County Code</p>
<p>Phone Number – Home</p>
<p>Phone Number – Business</p>
<p>Primary Language</p>
<p>Marital Status</p>
<p>Religion</p>
<p>Patient Account Number</p>
<p>SSN Number – Patient</p>
<p>Driver’s License Number - Patient</p>
<p>Mother’s Identifier</p>
<p>Ethnic Group</p>
<p>Birth Place</p>
<p>Multiple Birth Indicator</p>
<p>Birth Order</p>
<p>Citizenship</p>
<p>Veterans Military Status</p>
<p>Nationality</p>
<p>Patient Death Date and Time</p>
<p>Patient Death Indicator</p></td>
</tr>
</tbody>
</table>

#### ORC

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p>
<p>22</p>
<p>23</p>
<p>24</p></td>
<td><p>2</p>
<p>22</p>
<p>22</p>
<p>22</p>
<p>2</p>
<p>1</p>
<p>200</p>
<p>200</p>
<p>26</p>
<p>120</p>
<p>120</p>
<p>120</p>
<p>80</p>
<p>40</p>
<p>26</p>
<p>200</p>
<p>60</p>
<p>60</p>
<p>120</p>
<p>40</p>
<p>60</p>
<p>106</p>
<p>48</p>
<p>106</p></td>
<td><p>R</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>LI &lt;for link order to patient care&gt;</p>
<p>0</p>
<p>&lt;Supply Station ID, not used&gt; ~ &lt;Supply Station Name, 30 char max, formatted as NNN-TEXT&gt;</p>
<p>&lt;time of adjustment, formatted YYYYMMDDHHMMSS&gt;</p></td>
<td><p>Order Control</p>
<p>Placer Order Number</p>
<p>Filler Order Number</p>
<p>Placer Group Number</p>
<p>Order Status</p>
<p>Response Flag</p>
<p>Quantity/Timing</p>
<p>Parent</p>
<p>Date/Time of Transaction</p>
<p>Entered By</p>
<p>Verified By</p>
<p>Ordering Provider</p>
<p>Enterer’s Location</p>
<p>Call Back Phone Number</p>
<p>Order Effective Date/Time</p>
<p>Order Control Code Reason</p>
<p>Entering Organization</p>
<p>Entering Device</p>
<p>Action By</p>
<p>Advanced Beneficiary Notice Code</p>
<p>Ordering Facility Name</p>
<p>Ordering Facility Address</p>
<p>Ordering Facility Phone Number</p>
<p>Ordering Provider Address</p></td>
</tr>
</tbody>
</table>

#### RXA

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p>
<p>10</p>
<p>11</p>
<p>12</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16</p>
<p>17</p>
<p>18</p>
<p>19</p>
<p>20</p>
<p>21</p></td>
<td><p>4</p>
<p>4</p>
<p>26</p>
<p>26</p>
<p>100</p>
<p>20</p>
<p>60</p>
<p>60</p>
<p>200</p>
<p>200</p>
<p>200</p>
<p>20</p>
<p>20</p>
<p>60</p>
<p>20</p>
<p>26</p>
<p>60</p>
<p>200</p>
<p>200</p>
<p>2</p>
<p>2</p></td>
<td><p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>R</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>C</p>
<p>C</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td><p>0</p>
<p>1</p>
<p>&lt;formatted YYYYMMDDHHMMSS&gt;</p>
<p>&lt;Item ID,&gt; ~ &lt;Item Name, up to 60 char max&gt;</p>
<p>&lt;Quantity transacted in patient units, absolute value&gt;</p>
<p>&lt;User Code, use 0&gt; ~&lt;Name of User obtaining the supplies, formatted in HL7 e.g. LAST,FIRST,MI&gt;</p>
<p>USGE ~ &lt;Reason for usage, if any&gt; DECREASES INVENTORY</p>
<p>&lt;Quantity remaining after items were obtained, number ranging from –999999 to 999999 in patient units)</p></td>
<td><p>Give Sub-ID Counter</p>
<p>Administration Sub-ID Counter</p>
<p>Date/Time Start of Administration</p>
<p>Date/Time End of Administration</p>
<p>Administered code</p>
<p>Administered Amount</p>
<p>Administered Unite</p>
<p>Administered Dosage</p>
<p>Administered Note</p>
<p>Administered Provider</p>
<p>Administered-at Location</p>
<p>Administered Per (Time Unit)</p>
<p>Administered Strength</p>
<p>Administered Strength Units</p>
<p>Substance Lot Number</p>
<p>Substance Expiration Date</p>
<p>Substance Manufacturer Name</p>
<p>Substance Refusal Reason</p>
<p>Indication</p>
<p>Completion Status</p>
<p>Action Code-RXA</p></td>
</tr>
</tbody>
</table>

#### RXR

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 46%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence</strong></td>
<td><p><strong>Maximum</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>OPT</strong></td>
<td><strong>Description/Format</strong></td>
<td><strong>Element Name</strong></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p></td>
<td><p>60</p>
<p>60</p>
<p>60</p>
<p>60</p>
<p>60</p></td>
<td><p>R</p>
<p>O</p>
<p>O</p>
<p>O</p>
<p>O</p></td>
<td>OTH</td>
<td><p>Route</p>
<p>Site</p>
<p>Administration Device</p>
<p>Administration Method</p>
<p>Routing Instruction</p></td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1358                                       | VA Form 1358, Obligation or Change in Obligation.                                                                                                                                                                                                                                                                                                                                                                              |
| 2138                                       | VA Form 90-2138, Order for Supplies or Services. First page of a VA Purchase Order.                                                                                                                                                                                                                                                                                                                                            |
| 2139                                       | VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.                                                                                                                                                                                                                                                                                                                |
| 2237                                       | VA Form 90-2237, Request, Turn-in and Receipt for Property or Services. Used to request goods and services.                                                                                                                                                                                                                                                                                                                    |
| A&MM                                       | Acquisition and Materiel Management Service.                                                                                                                                                                                                                                                                                                                                                                                   |
| AACS                                       | Automated Allotment Control System--Central computer system developed by VHA to disburse funding from VACO to field stations.                                                                                                                                                                                                                                                                                                  |
| Accounting Technician                      | Fiscal employee responsible for obligation and payment of received goods and services. Accounting Technicians process accounting transactions and transmit them to FMS.                                                                                                                                                                                                                                                        |
| Activity Code                              | The last two digits of the AACS number. It is defined by each station.                                                                                                                                                                                                                                                                                                                                                         |
| ADP Security Officer                       | The individual at your station who is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.                                                                                                                                                                                                                         |
| Agent Cashier                              | The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.                                                                                                                                                                                                                                                                              |
| Allowance table                            | Reference table in FMS that provides financial information at the level immediately above the AACS, or sub-allowance level.                                                                                                                                                                                                                                                                                                    |
| Amendment                                  | A document, which changes the information contained in a specified Purchase Order. Amendments are processed by the Purchasing & Contracting section of A&MM and obligated by Fiscal Service.                                                                                                                                                                                                                                   |
| AMIS                                       | Automated Management Information System.                                                                                                                                                                                                                                                                                                                                                                                       |
| Application Coordinator                    | The individuals responsible for the implementation, training and trouble-shooting of a software package within a service. IFCAP requires there be an Application Coordinator designated for Fiscal Service, Supply Service, and for the Control Points (Requesting Services).                                                                                                                                                  |
| Approve Requests                           | The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or other request form and transmit said request to Supply/Fiscal.                                                                                                                                                                                                                                                                       |
| Authorization                              | A charge to an obligated 1358. Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.                                                                                                                                                                                                         |
| Authorization Balance                      | The amount of money remaining that can be authorized against the 1358. The service balance minus total authorizations.                                                                                                                                                                                                                                                                                                         |
| Batch Number                               | A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.                                                                                                                                                                                                                                                                    |
| Breakout Code                              | A set of A&MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).                                                                                                                                                                                                                                                                    |
| Budget Analyst                             | Fiscal employee responsible for distributing and transferring funds.                                                                                                                                                                                                                                                                                                                                                           |
| Budget Object Code                         | Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes replace sub accounts in IFCAP 5.0. Budget object codes are listed in the left column of MP4 Part V, Appendix B-1.                                                                                                                                                                                                     |
| Budget Sort Category                       | Used by Fiscal Service to identify the allocation of funds throughout their facility.                                                                                                                                                                                                                                                                                                                                          |
| Ceiling Transactions                       | Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.                                                                                                                                                                                                                                                            |
| Classification of Request                  | An identifier a Control Point can assign to track requests that fall into a category, e.g., Memberships, Replacement Parts, Food Group III.                                                                                                                                                                                                                                                                                    |
| Common Numbering Series                    | This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering Series used by each facility.                                                    |
| Control Point                              | Financial element, existing ONLY in IFCAP that corresponds to the ACCS number in FMS. Also the division of monies to a specified service, activity or purpose from an appropriation.                                                                                                                                                                                                                                           |
| Control Point Clerk                        | The user within the service who is designated to input requests (2237s) and maintain the Control Point records for a Service.                                                                                                                                                                                                                                                                                                  |
| Control Point Official                     | The individual authorized to expend government funds for ordering of supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.                                                                                                                                                           |
| Control Point Official's Balance           | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                                  |
| Control Point Requestor                    | The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&MM.                                                                                                                                    |
| Cost Center                                | “Subsection” of a Fund Control Point. Cost centers allow fiscal staff to create total expense reports for a section or service, and allow requestors to assign requests to that section or service. Cost centers are listed in the left column of MP-4 Part V, Appendix B-1.                                                                                                                                                   |
| Cost Center                                | A subdivision of a Fund Control Point, which tells which service/section, is being charged for a request/order.                                                                                                                                                                                                                                                                                                                |
| Date Committed                             | The date that you want IFCAP to commit funds to the purchase.                                                                                                                                                                                                                                                                                                                                                                  |
| Default                                    | A suggested response that is provided by the system.                                                                                                                                                                                                                                                                                                                                                                           |
| Deficiency                                 | When a budget has obligated and expended more than it was funded (see MP-4, Part V, Section C).                                                                                                                                                                                                                                                                                                                                |
| Delinquent Delivery Listing                | A listing of all the Purchase Orders that have not had all the items received by the Warehouse in IFCAP. It is used to contact the vendor for updated delivery information.                                                                                                                                                                                                                                                    |
| Direct Delivery Patient                    | A patient who has been designated to have goods delivered directly to him/her from the vendor.                                                                                                                                                                                                                                                                                                                                 |
| Discount Item                              | This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.                                                                                                                                                                                                                                                                    |
| Distribution Order                         | A list of supplies and the quantity needed to restock an inventory point.                                                                                                                                                                                                                                                                                                                                                      |
| EDI Vendor                                 | A vendor with whom the VA has negotiated an arrangement to accept and fill orders electronically.                                                                                                                                                                                                                                                                                                                              |
| Electronic Data Interchange (EDI)          | Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.                                                                                                                                                                                                                                                                                            |
| Electronic Signature                       | The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off-station will require a written signature as well.                                                                                                                                                                                                                                           |
| Expenditure Request                        | A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).                                                                                                                                                                                                                                                                                                       |
| FCP                                        | Fund Control Point (see Control Point).                                                                                                                                                                                                                                                                                                                                                                                        |
| Federal Tax ID                             | A unique number that identifies your station to the Internal Revenue Service.                                                                                                                                                                                                                                                                                                                                                  |
| Fiscal Balance                             | The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidations submitted against the obligation.                                                                                                                                                                                                                                        |
| Fiscal Quarter                             | The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.                                                                                                                                                                                                                                                                                                                        |
| Fiscal Year                                | Twelve-month period from October 1 to September 30.                                                                                                                                                                                                                                                                                                                                                                            |
| FMS                                        | Financial Management System, which has replaced CALM as the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting. |
| FOB                                        | Freight on Board. An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means that shipping charges are due to the shipper, and must be paid when the shipper arrives at the warehouse with the item.                                                                          |
| FPDS                                       | Federal Procurement Data System.                                                                                                                                                                                                                                                                                                                                                                                               |
| FTEE                                       | Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned an FTEE of 0.5, as would a full-time employee that worked for half of a year.                                                                                                                                 |
| Fund Control Point                         | CALM accounting element that is not used by FMS.                                                                                                                                                                                                                                                                                                                                                                               |
| Funds Control                              | A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.                                                                                                                                                                                                                                                                                                     |
| Funds Distribution                         | A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.                                                                                                                                                                                                                                                                              |
| GBL                                        | Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of \$250.00.                                                                                                                                                                                                                                                                                                                   |
| GL                                         | General Ledger.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Identification Number                      | A computer-generated number assigned to a code sheet.                                                                                                                                                                                                                                                                                                                                                                          |
| Imprest Funds                              | Monies used for cash or 3rd party draft purchases at a VA facility.                                                                                                                                                                                                                                                                                                                                                            |
| Integrated Supply Management System (ISMS) | ISMS is the system that replaced LOG I for Expendable Inventory.                                                                                                                                                                                                                                                                                                                                                               |
| Item File                                  | A listing of items specified by A&MM as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.                                                                                                                                                                                                                          |
| Item History                               | Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.                                                                                                                                                                                                                                                                             |
| Item Master Number                         | A computer generated number used to identify an item in the Item File.                                                                                                                                                                                                                                                                                                                                                         |
| Inventory Point                            | An entity which identifies supplies stored in a common area                                                                                                                                                                                                                                                                                                                                                                    |
| Justification                              | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.                                                                                                                                                                                                                                         |
| Justification                              | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.                                                                                                                                                                                                                                         |
| Liquidation                                | The amount of money on the invoice from the vendor for the authorization. They are processed through payment/invoice tracking.                                                                                                                                                                                                                                                                                                 |
| LOG I                                      | LOG I is the name of the Logistics A&MM computer located at the Austin Data Processing Center. This system continues to support the Consolidated Memorandum of Receipt.                                                                                                                                                                                                                                                        |
| Mandatory Source                           | A Federal Agency that sells supplies and services to the VA. VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.                                                                                                                                                                                                                                                                      |
| MSC Confirmation Message                   | A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of CALM Code Sheets.                                                                                                                                                                                                                                                                                    |
| Obligation                                 | The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of a Purchase Order.                                                                                                                                                                                                                                                                                                                    |
| Obligation (Actual) Amount                 | The actual dollar figure obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document on IFCAP.                                                                                                                                                                                                                                 |
| Obligation Data                            | A Control Point option that allows the Control Point Clerk to enter data not recorded by IFCAP.                                                                                                                                                                                                                                                                                                                                |
| Obligation Number                          | The C prefix number that Fiscal Service assigns to the 1358.                                                                                                                                                                                                                                                                                                                                                                   |
| Organization Code                          | Accounting element functionally comparable to Cost Center, but used to organize purchases by the budget that funded them, not the purposes for spending the funds.                                                                                                                                                                                                                                                             |
| Outstanding 2237                           | A&MM report that lists all the IFCAP generated 2237s pending action in A&MM.                                                                                                                                                                                                                                                                                                                                                   |
| PAID                                       | Paid Accounting Integrated Data.                                                                                                                                                                                                                                                                                                                                                                                               |
| Partial                                    | A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.                                                                                                                                                                                                                                                                                                           |
| Partial Date                               | The date that a warehouse clerk created a receiving report for a shipment.                                                                                                                                                                                                                                                                                                                                                     |
| PAT Number                                 | Pending Accounting Transaction number - the primary FMS reference number.                                                                                                                                                                                                                                                                                                                                                      |
| Personal Property Management               | A section of A&MM Service responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process all requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.                                                            |
| PPM                                        | Personal Property Management.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Primary Inventory Point                    | An entity that dispenses supplies to the secondary inventory point. It may receive supplies from the warehouse or a vendor.                                                                                                                                                                                                                                                                                                    |
| Procurement Request Cards                  | VA Form 10-7142. Used to order items repetitively.                                                                                                                                                                                                                                                                                                                                                                             |
| Program Code                               | Accounting element that identifies the VA initiative or program that the purchase will support.                                                                                                                                                                                                                                                                                                                                |
| Prompt Payment Terms                       | The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).                                                                                                                                                                                                           |
| Purchase History Add (PHA)                 | Information about purchase orders which is automatically sent to Austin for archiving. This same transaction is also used to send a PO for EDI processing.                                                                                                                                                                                                                                                                     |
| Purchase Order                             | A government document authorizing the purchase of the goods or services at the terms indicated.                                                                                                                                                                                                                                                                                                                                |
| Purchase Order Acknowledgment              | Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).                                                                                                                                                                                                                                                                                                         |
| Purchase Order Status                      | The status of completion of a purchase order (e.g., Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).                                                                                                                                                                                                                                                                             |
| Purchasing Agents                          | A&MM employees legally empowered to create purchase orders to obtain goods and services from commercial vendors.                                                                                                                                                                                                                                                                                                               |
| Quarterly Report                           | A Control Point listing of all transactions (Ceilings, Obligations, Adjustments) made to a Control Point's Funds.                                                                                                                                                                                                                                                                                                              |
| Quotation for Bid                          | Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors.                                                                                                                                                                                                                                                                                                                                               |
| Receiving Report                           | Report that Warehouse Clerk creates to record that the warehouse has received an item.                                                                                                                                                                                                                                                                                                                                         |
| Receiving Report                           | The VA document used to indicate the quantity and dollar value of the goods being received.                                                                                                                                                                                                                                                                                                                                    |
| Reference Number                           | Also known as the Transaction Number. The computer generated number that identifies a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point - 4 digit Sequence Number.                                                                                                                                                                                                                           |
| Repetitive (PR Card) Number                | See Item Master Number.                                                                                                                                                                                                                                                                                                                                                                                                        |
| Repetitive Item List                       | A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate requests from the list.                                                                                                                                                                                                                              |
| Requestor                                  | See “Control Point Requestor.”                                                                                                                                                                                                                                                                                                                                                                                                 |
| Requisition                                | An order from a Government vendor.                                                                                                                                                                                                                                                                                                                                                                                             |
| Running Balance                            | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                                 |
| Secondary Inventory Point                  | The entity which receives supplies from the primary and stores them until they are used by patients                                                                                                                                                                                                                                                                                                                            |
| Section Request                            | A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.                                                                                                                                                                                                                                                       |
| Service Balance                            | The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.                                                                                                                                                                                                                |
| SF-18                                      | Request for Quotation.                                                                                                                                                                                                                                                                                                                                                                                                         |
| SF-30                                      | Amendment of Solicitation/Modification of Contract.                                                                                                                                                                                                                                                                                                                                                                            |
| Short Description                          | A phrase that describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).                                                                                                                                                                                                                       |
| Site Parameters                            | Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.                                                                                                                                                                                                                                                                |
| Sort Group                                 | An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.                                                                                                                                                                                                                                                                          |
| Sort Order                                 | The order in which the budget categories will appear on the budget distribution reports.                                                                                                                                                                                                                                                                                                                                       |
| Special Remarks                            | A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.                                                                                                                                                                                                                                                  |
| Stacked Documents                          | The POs, RRs & 1358s that are sent electronically to Fiscal and stored in a file rather than being printed immediately.                                                                                                                                                                                                                                                                                                        |
| Status of Funds                            | Fiscal's on-line status report of the monies available to a Control Point. FMS updates this information automatically.                                                                                                                                                                                                                                                                                                         |
| Sub-control Point                          | A specific budget within a Control Point, defined by a Control Point user.                                                                                                                                                                                                                                                                                                                                                     |
| Sub-cost Center                            | A subcategory of Cost Center. In IFCAP 5.0, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.                                                          |
| Supply Station                             | An automated machine which stores supplies and retains logs of interactions with staff to acquire or refill the contained supplies.                                                                                                                                                                                                                                                                                            |
| Supply Station Secondary                   | A secondary inventory point that is interfaced to an automated supply station.                                                                                                                                                                                                                                                                                                                                                 |
| Tasked Job                                 | A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.                                                                                                                                                                                                                                                                    |
| TDA                                        | See "Transfer of Disbursing Authority."                                                                                                                                                                                                                                                                                                                                                                                        |
| Total Authorizations                       | The total amount of the authorizations created for the 1358 obligation.                                                                                                                                                                                                                                                                                                                                                        |
| Total Liquidations                         | The total amount of the liquidation against the 1358 obligation.                                                                                                                                                                                                                                                                                                                                                               |
| Transaction Number                         | The number of the transaction that funded a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.                                                                                                                                                                                                                                      |
| Transmission Number                        | A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traffic.                                                                                                                                                                                                                                                                                                        |
| Type Code                                  | A set of A&MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.                                                                                                                                                                                                                                                                                                   |
| Vendor file                                | An IFCAP file of vendors solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. File 440 contains information about the vendors solicited by your station. The debtor's address may be drawn from this file, but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added.               |
| Vendor ID Number                           | The ID number assigned to a vendor by FMS.                                                                                                                                                                                                                                                                                                                                                                                     |
| VRQ                                        | FMS Vendor Request document. When users send vendor information to FMS, FMS sends a VRQ document to IFCAP with the vendor information, ensuring that the information in the IFCAP vendor file matches the information in the FMS vendor table.                                                                                                                                                                                 |
#
