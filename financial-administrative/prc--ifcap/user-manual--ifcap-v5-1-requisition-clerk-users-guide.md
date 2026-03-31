---
title: IFCAP Version 5.1 Requisition Clerk User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Requisition Clerk User's Guide
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
menu_options: 1
description: Requisitions are orders from a Government vendor. After the Accountable Officer approves a 2237 (Request, Turn-in and Receipt for Property or Services) for procurement from a Government vendor, Requisition Clerks turn the 2237 into a requisition. When you create a requisition, you assign it a requis
audience: 
keywords: 
  - requisition
  - number
  - table
  - contents
  - order
  - code
  - amendment
  - edit
  - adjustment
  - ifcap
page_count: 0
word_count: 6744
section_count: 44
table_count: 15
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2000
revision_count: 2
revision_newest: 12/29/04
revision_oldest: 12/29/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1requisition_clerk.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1requisition_clerk.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

![](ifcap-version-5-1-requisition-clerk-user-s-guide/001.png)

########### Integrated Funds Distribution,

########### Control Point Activity, Accounting

########### and Procurement

########### (IFCAP)

########### 

########### REQUISITION CLERK

########### USER'S GUIDE

########### Version 5.1

########### October 2000

########### Revised October 2011

Office of Information and Technology (OI&T)

Management, Enrollment, and Financial Systems

########### 

Revision History

Initiated on 12/29/04

|              |                                                                                             |                 |                  |
|--------------|---------------------------------------------------------------------------------------------|-----------------|------------------|
| Date         | Description (Patch \# if applic.)                                                           | Project Manager | Technical Writer |
| October 2011 | Patch PRC\*5.1\*158 Modification of title for IFCAP VA Form 1358. See page [20](#glossary). | REDACTED        | REDACTED         |
| 12/29/04     | Updated to comply with SOP 192-352 Displaying Sensitive Data.                               |                 | REDACTED         |
| 12/29/04     | Pdf file checked for accessibility to readers with disabilities.                            |                 | REDACTED         |
|              |                                                                                             |                 |                  |
|              |                                                                                             |                 |                  |
|              |                                                                                             |                 |                  |
|              |                                                                                             |                 |                  |
|              |                                                                                             |                 |                  |
|              |                                                                                             |                 |                  |
|              |                                                                                             |                 |                  |
|              |                                                                                             |                 |                  |

PREFACE

This document is for VA procurement personnel assigned the user category of Requisition Clerk in the Integrated Funds Distribution, Control Point Monitoring, Accounting and Procurement (IFCAP) system.

In IFCAP, VA employees request goods by creating electronic purchase orders, requisitions, issue book requests, delivery orders and Purchase Card orders. This manual explains how to use IFCAP as a tool to create and edit requisitions.

########### TABLE OF CONTENTS

CHAPTER 1 INTRODUCTION [iv](#_Toc290884598)

1.1 The Role of the Requisition Clerk [7](#the-role-of-the-requisition-clerk)

1.2 How to Use This Manual [7](#how-to-use-this-manual)

1.3 Reference Numbering System [7](#reference-numbering-system)

1.4 Package Management, Legal Requirements and Security Measures [7](#package-management-legal-requirements-and-security-measures)

1.5 Package Operation [7](#package-operation)

CHAPTER 2 HOW TO CREATE A REQUISITION [9](#_Toc290884604)

2.1 Introduction [9](#introduction)

2.2 Menu Path. [9](#menu-path)

2.3 Enter Requisition Number [9](#enter-requisition-number)

2.4 Order Data [9](#order-data)

2.5 Source Code 4 [10](#source-code-4)

2.6 Special Remarks [11](#special-remarks)

2.7 Delivery Location [12](#delivery-location)

2.8 Enter Item [12](#enter-item)

2.9 BOC [13](#boc)

2.10 Add Item [13](#add-item)

2.11 Log Code Sheets [14](#log-code-sheets)

CHAPTER 3 EDIT A REQUISITION [17](#chapter-3-edit-a-requisition)

3.1 Introduction [17](#introduction-1)

3.2 Edit a Requisition [17](#edit-a-requisition)

3.3 Select Requisition Number [17](#select-requisition-number)

3.4 Display Requisition [19](#display-requisition)

3.5 Log Code Sheets [20](#log-code-sheets-1)

CHAPTER 4 AMEND A REQUISITION [21](#chapter-4-amend-a-requisition)

4.1 Introduction [21](#introduction-2)

4.2 Amend Requisition [21](#_Toc497897139)

4.3 Menu Path [21](#menu-path-1)

4.4 Setup Parameters [21](#setup-parameters)

4.5 Delivery Schedules [22](#delivery-schedules)

4.6 Add Amendment Type [23](#add-amendment-type)

4.7 Display Amendment [23](#display-amendment)

4.8 Sign Amendment [24](#sign-amendment)

CHAPTER 5 ADJUST A REQUISITION RECEIVING REPORT [25](#chapter-5-adjust-a-requisition-receiving-report)

5.1 Introduction [25](#introduction-3)

5.2 Menu Path [25](#menu-path-2)

5.3 Setup Parameters [25](#setup-parameters-1)

5.4 Create Adjustment [26](#create-adjustment)

5.5 Select Partial Date [26](#select-partial-date)

5.6 Display Adjustment [26](#display-adjustment)

5.7 Review Adjustment [27](#review-adjustment)

5.8 Print Adjustment [27](#print-adjustment)

CHAPTER 6 REMOVE 2237 OR CANCEL A REQUISITION [29](#chapter-6-remove-2237-or-cancel-a-requisition)

6.1 Introduction [29](#introduction-4)

6.2 Remove 2237 [29](#remove-2237)

6.3 Select Requisition Number [29](#select-requisition-number-1)

6.4 Cancel Unobligated Requisition [30](#cancel-unobligated-requisition)

6.5 Menu Path [30](#menu-path-3)

6.6 Select Requisition [30](#select-requisition)

CHAPTER 7 CHANGING THE STAUS OF A REQUISITION [32](#chapter-7-changing-the-staus-of-a-requisition)

CHAPTER 8 ERROR MESSAGES AND THEIR RESOLUTION [35](#_Toc497897163)

GLOSSARY [40](#glossary)

INDEX [49](#index)

<span id="_Toc290884598" class="anchor"></span>

########### CHAPTER 1 INTRODUCTION

## The Role of the Requisition Clerk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Requisitions are orders from a Government vendor. After the Accountable Officer approves a 2237 (Request, Turn-in and Receipt for Property or Services) for procurement from a Government vendor, Requisition Clerks turn that 2237 into a requisition. Later, an Accounting Technician will obligate funds for the requisition (if necessary), the vendor will fulfill the requisition, and the Warehouse clerk will use IFCAP to report when the order is received. See the flow chart in this chapter for a complete representation of the IFCAP system and the Requisition Clerk’s relationship to the rest of the IFCAP user categories.

## How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual explains how to perform the role of the Requisition Clerk by dividing that role into small, manageable tasks. The authors of this manual have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new Requisition Clerks to use this manual as a tutorial by following the instructions from beginning to end.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third section of Chapter 1. All clear? Actually, all this means is that users that want to divide their reading into manageable lessons can concentrate on one section and all of its subsections, e.g., section 1.3.5.4 and all of its subsections would make a coherent lesson.

## Package Management, Legal Requirements and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use IFCAP to approve transactions, Requisition Clerks are given access to a set of IFCAP menu options designed for their use. Some of these menu options are additionally controlled by the use of access “keys”. These access keys are administered to individual Requisition Clerks by the Information Resources Management Service at their facility. Also, each Requisition Clerk will create a “signature code” that functions legally as their signature. Requisition Clerks must enter this signature to create any form in IFCAP that would require an authorizing signature if they created the form manually.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document explains how to use IFCAP to approve transactions. Novice users will be unfamiliar with the information that some of the IFCAP prompts require. IFCAP provides three levels of explanations for the prompts. Enter a question mark at the prompt to read a description of the kind of data the field will accept, two question marks to read a more complex explanation, and enter three question marks to read a complete description of the prompt and see a list of acceptable responses to the prompt.<span id="_Toc290884604" class="anchor"></span>

###########   CHAPTER 2 HOW TO CREATE A REQUISITION

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Requisitions are orders from a Government vendor. After the Accountable Officer approves a 2237 (Request, Turn-in and Receipt for Property or Services) for procurement from a Government vendor, Requisition Clerks turn the 2237 into a requisition. When you create a requisition, you assign it a requisition number, which you and other users will be able to use to refer to the requisition. The numbers are based on a numbering system in MP-4 Part V, Section 12-D.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Requisition Processing ...

LOG/GSA/DLA Code Sheets Menu ...

Display/Print Menu (PPM) ...

Select Requisition Clerk Menu Option: Requisition Processing

New Requisition

Edit an Incomplete Requisition

Amendment to Requisition

Cancel an Unobligated Requisition

Remove 2237 from Requisition

Display Purchase Order /Requisition

Change Delivery Date on Requisition

Enter DEPOT/GSA PUSH Order to PO Register

Change DEPOT/GSA PUSH Order on PO Register

Item File Edit

Requisition Register

Select Requisition Processing Option: New Requisition

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY,DC

## Enter Requisition Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Requisition Number.

ENTER A NEW REQUISITION NUMBER OR A COMMON NUMBERING SERIES

REQUISITION NUMBER: ???

CHOOSE FROM:

I0 999-I0 PERSONAL PROPERTY

I9 999-I9 PERSONAL PROPERTY

ENTER A NEW REQUISITION NUMBER OR A COMMON NUMBERING SERIES

REQUISITION NUMBER: ???

CHOOSE FROM:

I0 999-I0 PERSONAL PROPERTY

I9 999-I9 PERSONAL PROPERTY

ENTER A NEW REQUISITION NUMBER OR A COMMON NUMBERING SERIES

REQUISITION NUMBER: I0 999-I0 PERSONAL PROPERTY

## Order Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will use the requisition number you enter as a prefix for the entire requisition number, which it assigns. Answer “Y” at the “Are you adding 'XX-XXXXXX' as a new REQUISITION NUMBER?:” prompt.

The Method of Processing will default to Requisition, however the user may select Purchase Card instead.

At the ESTIMATED ORDER?: prompt, enter whether the cost of the order is an estimate or not.

The P.O. Date: prompt will default to TODAY. User may enter another date if appropriate.

Enter the vendor name at the Vendor: prompt. If Vendor name is not already in the Vendor file, the user will be prompted to fill in the required information for the Vendor record in IFCAP.

Enter the address where the payment should be sent if prompted for it.

Are you adding '999-B00002' as a new REQUISITION NUMBER? Y (YES)

METHOD OF PROCESSING: REQUISITION// ??

This is the method of payment.

Choose from:

8 REQUISITION

25 PURCHASE CARD

ESTIMATED ORDER?: Y// YES

P.O. DATE: TODAY// (APR 15, 1994)

VENDOR: ???

This is the name of the vendor.

Choose from:

4 IFVENDOR,ONE PH:555 222-8201 NO: 4

ORD ADD:11 FEDORA PLACE FMS:

ANYTOWN, NY 99999 CODE: FAX:555 789-4444

5 IFVENDOR,TWO PH:333 555-4444 NO: 5

ORD ADD:MAIN STREET FMS:

PHILADELPHIA, PA 19101 CODE: FAX: 123-4568

VENDOR: 4 IFVENDOR,ONE PH:555 222-8201 NO: 4

ORD ADD:11 FEDORA PLACE FMS:

ANYTOWN, NY 99999 CODE: FAX:555 789-4444

...OK? Yes// (Yes)

TAX ID/SSN: 000111111

SSN/TAX ID INDICATOR: TAX IDENTIFICATION NUMBER

// ?

Choose from:

S SOCIAL SECURITY NUMBER

T TAX IDENTIFICATION NUMBER

SSN/TAX ID INDICATOR: TAX IDENTIFICATION NUMBER

// t TAX IDENTIFICATION NUMBER

PAYMENT ADDRESS1: 11 FEDORA PLACE//

PAYMENT ADDRESS2: ATTN: 2FYI//

PAYMENT CITY: ANYTOWN//

PAYMENT STATE: ANYTOWN//

PAYMENT ZIP CODE: 99999//

## Source Code 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the source code for the vendor. IFCAP will offer a default value.

At the Select Request Worksheet 2237 Transaction Number: prompt, enter the 2237 you’re turning into a requisition. If you don’t remember the number, type three question marks (???) at the prompt and IFCAP will list all the outstanding 2237s. If there is no 2237 for this order, the user may press the Enter key and pass this field.

SOURCE CODE: 3// ???

This is the source code for this order.

Choose from:

0 Defense Supply Agency

1 VA Servicing Supply Depot

3 GSA Supply Depot

9 Marketing Center

SOURCE CODE: 3// IFVENDOR,ONE Supply Depot

Enter a 2237 reference number. The FCP,Cost Center,Service,Delivery

Location and Line Items will be transferred into this Purchase Order.

The 2237 Fiscal Year and Quarter must be earlier or same

as the P.O. Date Fiscal Year and Quarter.

Select REQUEST WORKSHEET 2237 TRANSACTION NUMBER

Enter a 2237 reference number. The FCP,Cost Center ,Service,Delivery

Location and Line Items will be transferred into this Purchase Order .

Select REQUEST WORKSHEET 2237 TRANSACTION NUMBER: ???

CHOOSE FROM:

999-94-2-120-0012 Assigned to PPM Clerk OBL SUPPLY WAREHOUSE PEN

999-94-2-120-0010 Assigned to PPM Clerk OBL SUPPLY WAREHOUSE ITEM \#8

999-94-2-120-0009 Assigned to PPM Clerk OBL SUPPLY WAREHOUSE PAINT

Select REQUEST WORKSHEET 2237 TRANSACTION NUMBER: 0009 999-94-2-120-0009 OBL

## Special Remarks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the 2237 contains information in the Special Remarks field, the user can move that information onto the Requisition by answering YES at the Transfer special remarks prompt.

Enter the line item on the 2237 you wish to order on the requisition. If you do not know the line item number, enter three question marks at the prompt and IFCAP will list the available line items. If you wish to select all the items on the 2237 you may enter A for ALL at the prompt.

Enter another transaction number to create a requisition from multiple transactions. The information on the 2237 will be “pulled” onto the Requisition automatically and the user will be able to change the data if necessary. If NO 2237 is attached to the Requisition, the user will be prompted to fill in the necessary FCP and item data.

Enter the cost center at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service.

Enter the service that requested the items. If you do not know the name of the service, enter three question marks at the prompt and IFCAP will list the available service names.

Line Items: ???

ENTER A LINE ITEM NUMBER IN THE FOLLOWING FORMAT: 1,2,3,4 OR 1:4

OR ENTER 'A' FOR ALL LINE ITEMS

1 112 SYRINGES

Line Items: 1

...HMMM, I'M WORKING AS FAST AS I CAN....

Select REQUEST WORKSHEET 2237 TRANSACTION NUMBER:

FCP: 110 LAB TESTING 110

COST CENTER: 800100//

REQUESTING SERVICE: 6// ???

This is the requesting Service.

CHOOSE FROM:

A&MM 90

BLIND REHABILITATION 122

CANTEEN SERVICE 133

DIETETICS 120

ENDOCRINOLOGY RESEARCH 151E

FISCAL 04

GERIATRICS AND EXTENDED CARE 180

INFORMATION RESOURCE MGMT 10B/IRM

LABORATORY 113

REQUESTING SERVICE: 6//

## Delivery Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the final destination of the purchase at the Delivery Location: prompt.

Enter where you want the VENDOR to deliver the purchase at the Ship To: prompt. The default value is the 1<sup>ST</sup> entry in the File 411, Receiving Location field.

Enter the delivery date.

Enter any estimated shipping and handling charges.

Enter the budget object code appropriate for the items the vendor will ship. If you do not know the budget object code, enter three question marks at the prompt and IFCAP will list the available budget object codes. Budget object code is a required field and the requisition will not process if this field is not populated.

Your name will appear as the default value at the PA/PPM /Authorized Buyer prompt. You may enter the name of another user.

DELIVERY LOCATION: WHSE

SHIP TO: WAREHOUSE//

DELIVERY DATE: TODAY+10// (AUG 14, 1994)

EST. SHIPPING AND/OR HANDLING: 40.00

EST. SHIPPING BOC : ???

ANSWER WITH BOC

DO YOU WANT THE ENTIRE 61-ENTRY BOC LIST? Y (YES)

CHOOSE FROM:

1081 Physicians-Full Time

1092 Stay-In-School Program Part-Time Employment of Needy Students

1095 Employee Salary Continuation

2101 Permanent Duty Travel

2103 Employee Training Travel

2122 Travel of Witnesses

2140 Commercial Transportation Charges

2220 Other Shipments

2230 Shipment of Household Goods & Personal Effects

2324 ADP Software Rental

2342 Office Automation/Word Processing, Rental

2350 Motion-Picture Film Rentals

EST. SHIPPING BOC : 2220 Other Shipments

PA/PPM/AUTHORIZED BUYER: IFBUYER,ONE// ??

Must be a PPM Clerk, Authorized Buyer or Manager for Requisitions, a

Purchasing Agent, Authorized Buyer or Manager for P.O.'s.

## Enter Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the line item number of the item you want to order on the requisition.

Enter its item master file number. If you do not know these numbers enter three question marks at the prompts and IFCAP will list the available line numbers and item master file numbers. Edit the item description if you like. You may also change the quantity, the unit of purchase (by the box, gallon, case, etc.), and the actual cost per unit you are ordering. You can change the packaging multiple (e.g., cans that only come in six-packs would have a packaging multiple of six). You can also change the unit conversion factor and the National Stock Number of the item. You must enter at least one item to be able to complete the order.

Enter a contract number if this requisition is made under the terms of a contract between the U.S. Government and the vendor.

Select LINE ITEM NUMBER: 1//

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.: 112// ..

DESCRIPTION:

1\> SYRINGES FOR FMS TESTING SCENARIOS

EDIT Option:

QUANTITY: 1//

UNIT OF PURCHASE: BX//

ACTUAL UNIT COST: \$12.5000//

PACKAGING MULTIPLE: 1//

SKU: BX//

UNIT CONVERSION FACTOR: 1//

NSN: 6640-87-112-3421//

CONTRACT/BOA \#:

## BOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the General Services Administration or Defense Logistics Agency serial number, if one applies.

Enter a backorder source indicator at the Backorder Control: prompt.

Enter a minus sign at the Substitute Control: prompt if substitution of items is not allowed.

Enter the budget object code classification for the item at the BOC: prompt. If you do not know the budget object code, enter three question marks at the prompt and IFCAP will display the available budget object codes.

You may enter or edit a delivery schedule for the item if the item will be delivered in multiple shipments.

SERIAL NO.(VEN/DLA):

BACKORDER CONTROL: ???

Enter '-' to set a backorder source for LOG code sheets.

Choose from:

\- ESTABLISH BACKORDER

BACKORDER CONTROL:

SUBSTITUTE CONTROL: ???

Enter '-' if substitution is not authorized for LOG code

sheets.

Choose from:

\- NO SUBSTITUTE

SUBSTITUTE CONTROL:

BOC: 2632 Other Medical and Dental Supplies Replace

Enter/Edit Delivery Schedule for this Item? NO//

Enter/Edit Delivery Schedule for this Item? NO// (NO)

## Add Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter another line item number if you wish to have multiple items on the Requisition.

Enter comments if you like.

IFCAP will display No FPDS Data to be Entered: because the federal sources have already entered FPDS data for the items they supply.

You may review the requisition.

Select LINE ITEM NUMBER:

COMMENTS:

1\>This is an order needed to open the new clinic.

EDIT Option:

No FPDS Data to be Entered:

Specifically excluded from reporting are grants,intragovernmental

procurements,procurements from imprest fund,nonappropriated

(general post,loan guarantee,etc.),SF44s,credit card

transactions,training authorizations,Government Bills of

Lading (GBL),and Government Transportation Requests (GTR).

Review Requisition ? YES// (YES)

REQUISITION: 999-B00010 STATUS: Pending PPM Clerk Signature

M.O.P.: REQUISITION LAST PARTIAL RECD.:

REQUESTING SERVICE: FISCAL

VENDOR: IFVENDOR,ONE SHIP TO: ANYCITY VAMC

11 FEDORA PLACE V.A. Medical Center

ATTN: 2FYI 50 ANYSTREET Street, NW

ANYTOWN, NY 99999 ANYCITY, DC 99999

555 222 8201

FMS Vendor Code: FED000000

DELIVERY LOCATION: BDL3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 842100 \| \|

TYPE: DELIVERY ORDER \| \|AGENT:

DELIVER ON/BEFORE 1/30/2000 \|CONTRACT: \| IFBUYER,TWO

DISCOUNT TERM: NET30 \| \|DATE: 1/20/2000

APP: 3600160-110 \| \|ESTIMATED

\| \|TOTAL: 16.85

--------------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

1 dolls 12 EA 1.20 14.40

NSN: 7510-98-989-9877

Items per EA: 1

BOC: 2660 FMS LINE: 001

2 EST. SHIPPING AND/OR HANDLING 2.45

This is for the waiting room in the clinic.

## Log Code Sheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may create LOG code sheets now if you like. Many users choose to create the LOG code sheets at this point and NOT affix their signature to the Requisition. Once the code sheets have processed and the user knows what is actually going to be delivered by the Vendor, they Edit the Requisition to reflect what will be delivered and then Affix their signature.

Answer Y at the Affix signature to Requisition and Print in Fiscal?: prompt.

Enter your electronic signature code.

Press the Enter key at the Requisition Number: prompt to return to the Requisition Processing menu.

Create LOG code sheets ? NO// (NO)

WARNING--LOG code sheets have NOT been created!!

Once processing is completed and code sheets have been sent the user will complete the requisition and affix their signature to the document.

Affix signature to Requisition and Print? NO// Yes

Enter ELECTRONIC SIGNATURE CODE: Thank you.

...please wait while I update the due-ins at the inventory points.

########### CHAPTER 3 EDIT A REQUISITION

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three ways to change a requisition. You can EDIT a requisition if you haven’t affixed your electronic signature to the Requisition yet.

After you’ve entered your electronic signature code, if the Requisition has been Obligated, you can AMEND the requisition (Chapter 4).

You can ADJUST the Requisition’s receiving report (Chapter 5) if you need to lower the quantity received.

## Edit a Requisition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit a requisition, select Edit an Incomplete Requisition from the Select Requisition Processing Option: prompt.

Enter a Station Number.

Select Requisition Clerk Menu Option: requisition Processing

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

Select Requisition Processing Option: EDIT an Incomplete Requisition

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

## Select Requisition Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the REQUISITION NUMBER: prompt, enter the number of the requisition you wish to edit. If you do not know the requisition number, enter three question marks (???) at the prompt and IFCAP will list all the requisitions that you can edit.

If you wish to add another 2237 to the Requisition enter the transaction number at the Select Request Worksheet 2237 Transaction Number: prompt. If you don’t remember the number, type three question marks (???) at the prompt and IFCAP will list all the outstanding 2237s. It must be from the same control point as the other 2237s already attached to the Requisition.

> **NOTE:** All previously entered information will be displayed as the default value. The user may change the existing information or add additional information to the requisition.

REQUISTION NUMBER: 999-B00013 01-26-00 RQ Pending PPM Clerk Signature

FCP: 110 \$ 112.56

METHOD OF PROCESSING: REQUISITION//

ESTIMATED ORDER?: YES//

P.O. DATE: JAN 26,2000//

VENDOR: IFVENDOR,ONE//

SOURCE CODE: 3//

Enter a 2237 reference number. The FCP,Cost Center,Service,Delivery

Location and Line Items will be transferred into this Purchase Order.

The 2237 Fiscal Year and Quarter must be earlier or same

as the P.O. Date Fiscal Year and Quarter.

This Purchase Order already contains: 999-00-2-110-0035

Select REQUEST WORKSHEET 2237 TRANSACTION NUMBER: 999-00-2-110-0036

Assigned to PPM Clerk OBL IFVENDOR,ONE

PENCILS

Line Items: A

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND....

Select REQUEST WORKSHEET 2237 TRANSACTION NUMBER:

FCP: 110 IFBUYER,ONE .01

COST CENTER: 842100//

REQUESTING SERVICE: FISCAL//

DELIVERY LOCATION: BDL2//

No FPDS Data to be Entered:

Specifically excluded from reporting are grants,intragovernmental

procurements,procurements from imprest fund,nonappropriated

(general post,loan guarantee,etc.),SF44s,credit card

transactions,training authorizations,Government Bills of

Lading (GBL),and Government Transportation Requests (GTR).

Review Requisition ? YES//

## Display Requisition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Requisition may be displayed to the screen

Review Requisition ? YES// (YES)

REQUISITION: 999-B00013 STATUS: Pending PPM Clerk Signature

M.O.P.: REQUISITION LAST PARTIAL RECD.:

REQUESTING SERVICE: FISCAL

VENDOR: IFVENDOR,ONE SHIP TO: ANYCITY VAMC

11 FEDORA PLACE V.A. Medical Center

ATTN: 2FYI 50 ANYSTREET Street, NW

ANYTOWN, NY 99999 ANYCITY, DC 99999

555 222 8201

FMS Vendor Code: FED000000

DELIVERY LOCATION: BDL2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 842100 \| \|

TYPE: DELIVERY ORDER \| \|AGENT:

DELIVER ON/BEFORE 2/5/2000 \|CONTRACT: \| IFBUYER,ONE

DISCOUNT TERM: NET30 \| \|DATE: 1/26/2000

APP: 3600160-110 \| \|ESTIMATED

\| \|TOTAL: 115.56

--------------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

1 BATTERY, NONRECHARGEABLE. 1.5 12 PG 9.38 112.56

VOLTS, CYLINDRICAL SHAPE, 1

TERMINAL. FLAT SURFACE TYPE,

1.344 INCHES NOMINAL, 2.406

INCHES LONG, SIZE D FOR

INDUSTRIAL FLASHLIGHT USE. 24S

NSN: 6135-01-999-9996

Items per PG: 24

BOC: 2660 FMS LINE: 001

2 PENCILS 12 EA 0.25 3.00

NSN: 7510-01-432-4333

Items per EA: 1

BOC: 2660 FMS LINE: 001

V.A. TRANSACTION NUMBERS:

999-00-2-110-0036

999-00-2-110-0035

END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:

## Log Code Sheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may create LOG code sheets if you like.

Answer Y at the Affix signature to Requisition and Print in Fiscal?: prompt.

Enter your electronic signature code.

Press the Enter key at the Requisition Number: prompt to return to the Requisition Processing menu.

Create LOG code sheets ? NO// y (YES)

P.O.(PAT) No.: 999-B00013

Document Identifier: B0013

Department No.: L01

Source Code: 3

Do you wish to pre-edit codesheet data ? NO// (NO)

Select LOG TRANSACTION TYPE: 700// 700 Unposted IFVENDOR,ONE Acquisition (Source 3)

Now creating LOG code sheets ...

1 2 3 4 5 6 7 8

12345678901234567890123456789012345678901234567890123456789012345678901234567890

----+----\|----+----\|----+----\|----+----\|----+----\|----+----\|----+----\|----+----\|

Line Item: 1

019999996 999700BATT 1,5VPG6135 L013B0013 G001125600012 2050 3

Line Item: 2

014324333 999700PENCILS EA7510 L013B0013 G000030000012 2050 3

Do you want to mark these code sheets for transmission? \<YES/NO\> y (YES)

TRANSMISSION DATE: TODAY// (JAN 26, 2000)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

CODE SHEETS MARKED FOR TRANSMISSION!

Affix signature to Requisition and Print ? NO// y (YES)

...please wait while I update the due-ins at the inventory points...

########### CHAPTER 4 AMEND A REQUISITION

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three ways to change a requisition. You can EDIT a requisition (Chapter 3) if you haven’t affixed your electronic signature to the Requisition yet.

After you’ve entered your electronic signature code, if the Requisition has been Obligated, you can AMEND the requisition (Chapter 4).

You can ADJUST the Requisition receiving report Chapter 5) if you need to lower the quantity received.

1)  Some amendments reconcile discrepancies between the units per unit of purchase (e.g., bottles per case) on the requisition and the units per unit of purchase supplied by the vendor.
2)  Some amendments decrease the amount due from a vendor if the vendor can't supply the amount you need.
3)  Some amendments increase the amount of units due on a requisition.
4)  Some amendments change the vendor on the requisition.
5)  Canceling an order is a specific type of amendment.
6)  Some amendments change the delivery date.
7)  Some amendments delete an item that's no longer available from the vendor after all the rest of the items are in. This is how you may update the status of a requisition. (i.e. Partial Order Received (Amended) to Complete Order Received (Amended)).

## Amend Requisition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IF the Requisition is not in a status of Transaction complete it may be amended using the option Amendment to Requisition.

> **NOTE:** If the Requisition has a Status of *Transaction Complete* you must use the option All Status Amendment to Requisition

## Menu Path 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Requisition Clerk Menu Option: REQuisition Processing

New Requisition

Edit an Incomplete Requisition

Amendment to Requisition

Adjustment Voucher to Requisition

Cancel an Unobligated Requisition

Remove 2237 from Requisition

Display Purchase Order/Requisition

Change Delivery Date on Requisition

Enter DEPOT/GSA PUSH Order to PO Register

Change DEPOT/GSA PUSH Order on PO Register

Item File Edit

Requisition Register

All Status Amendment to Req

Select Requisition Processing Option: AMEndment to Requisition

## Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Station Number

Select Requisition number. User may enter ?? to see a list of choices.

Software will assign an amendment number. The relevant Requisition data will be pulled onto the amendment work file.

User may accept the default date or enter a different date.

User must select the Authority type appropriate for this amendment. Authority E is to be used ONLY when you wish to cancel the Requisition. The necessary FMS documents will be sent to Austin to cancel the obligation. All other amendments are done using Authority D.

The PA/PPM/Authorized Buyer prompt will reflect the name of the person creating the amendment.

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

REQUISITION NO.: B00005 999-B00005 01-26-00 RQ Ordered and Obligated

FCP: 110 \$ 38.40

Amendment Number: 1

...copying Purchase Order into work file...

...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...

EFFECTIVE DATE: TODAY// (JAN 31, 2000)

AUTHORITY: D// ?

This is the AUTHORITY type.

CHOOSE A,B,C,D OR E

Answer with TYPE OF AMENDMENT NUMBER, or DESCRIPTION

Do you want the entire TYPE OF AMENDMENT List? Y (Yes)

Choose from:

A Not available for Requisition

B Not available for Requisition

C Not available for Requisition

D OTHER

E CANCEL REQUISITION

AUTHORITY: D//

PA/PPM/AUTHORIZED BUYER: IFBUYER,ONE// IBO

## Delivery Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select the type of Requisition amendment you wish to generate. The user will be prompted to fill in the appropriate fields for the amendment type selected.

A delivery schedule may be entered.

Select TYPE OF REQUISITION AMENDMENT NUMBER: ??

Choose from:

1 SHIP TO Edit

2 LINE ITEM Add

3 LINE ITEM Delete

4 LINE ITEM Edit

5 SOURCE CODE Edit

6 Edit MAIL INVOICE TO

7 ADMINISTRATIVE CERTIFICATION Add

8 ADMINISTRATIVE CERTIFICATION Delete

9 EST. SHIPPING Edit

10 F.C.P. Edit

11 Change FEDERAL VENDOR

12 REPLACE REQUISITION NUMBER

Select TYPE OF REQUISITION AMENDMENT NUMBER: 2 LINE ITEM Add

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

ADD LINE ITEM 2? NO// Y (YES)

ITEM MASTER FILE NO.: 12015 PURSES ..

DESCRIPTION:

1\> LEATHER,PURSE

EDIT Option:

QUANTITY: 12

UNIT OF PURCHASE: EA EACH

ACTUAL UNIT COST: 13.5

PACKAGING MULTIPLE: 1

SKU: EA//

UNIT CONVERSION FACTOR: 1

NSN: 7510-87-119-1010

SERIAL NO.(GSA/DLA): 3434

BACKORDER CONTROL:

SUBSTITUTE CONTROL: - NO SUBSTITUTE

BOC: 2341 Equipment Rental Replace

Enter/Edit Delivery Schedule for this Item? NO// (NO)

## Add Amendment Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another amendment type may be added.

Enter the correct delivery date.

The suggested status for the amended order will be displayed as a default value. If the user feels this status is not correct another may be entered.

Enter a Justification for the amendment.

Select TYPE OF REQUISITION AMENDMENT NUMBER:

DELIVERY DATE: FEB 5,2000//

AMENDMENT/ADJUSTMENT STATUS: Ordered and Obligated (Amended)

// 21

JUSTIFICATION: ADD ITEM

## Display Amendment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The newly created amendment may be displayed to the screen for review.

Review Amendment ? YES// (YES)

2\. MOD. NO.: \| 3. EFFECTIVE DATE: \| 4. REQUISITION/P.O. REQ. NO.:

1 \| 1/31/2000 \| B00005

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

8\. NAME AND ADDRESS OF CONTRACTOR \| 10A. MODIFICATION OF CONTRACT/ORDER

IFVENDOR,ONE \| NO. 999-B00005

OFFICE OF ITI \|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5555 MAIN ST \| 10B. DATED (See Item 13) 1/26/2000

SUITE 1111 \|

ANYCITY, VA 99999 \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

12\. ACCOUNTING AND APPROPRIATION DATA (If required)

Increase 3600160-110 \$ 162.00 TOTAL AMOUNT: \$ 200.40

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

D. OTHER

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **IMPORTANT:** Contractor is not required to sign this document and return

copies to the issuing office.

14\. DESCRIPTION OF MODIFICATION (organized by UCF section heading,

including contract subject matter where feasible.)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\*ADDED THROUGH AMENDMENT\*

Item No. 2 Item Master File No. 12015 BOC: 2341

LEATHER,PURSE

Items per EA: 1 NSN: 7510-87-119-1010

12 EA at \$ 13.5000 = \$ 162.00

\*ADDED THROUGH AMENDMENT\*

Authority Edit is OTHER

Except as provided herein, all terms and conditions of the document referenced in Item 10A, as heretofore changed, remains unchanged and in full force and effect.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

JUSTIFICATION: ADD ITEM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CONTRACTING OFFICER: IFBUYER,ONE

ENTER '^' TO HALT:

## Sign Amendment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If amendment is complete the user must indicate the amendment is ready for approval by entering Y at the Approve Amendment number prompt.

Enter electronic signature code.

Enter printer device name.

Review Amendment ? YES// N (NO)

Approve Amendment number 1: ? NO// Y (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

SEND TO SUPPLY

QUEUE ON DEVICE: SF SFCS6\$PRT-12/6/UP ANY CIOFO

Requested Start Time: NOW// (JAN 31,

# ########### CHAPTER 5 ADJUST A REQUISITION RECEIVING REPORT


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [The Role of the Requisition Clerk](#the-role-of-the-requisition-clerk)
  - [How to Use This Manual](#how-to-use-this-manual)
  - [Reference Numbering System](#reference-numbering-system)
  - [Package Management, Legal Requirements and Security Measures](#package-management-legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
  - [Introduction](#introduction)
  - [Menu Path](#menu-path)
  - [Enter Requisition Number](#enter-requisition-number)
  - [Order Data](#order-data)
  - [Source Code 4](#source-code-4)
  - [Special Remarks](#special-remarks)
  - [Delivery Location](#delivery-location)
  - [Enter Item](#enter-item)
  - [BOC](#boc)
  - [Add Item](#add-item)
  - [Log Code Sheets](#log-code-sheets)
  - [Introduction](#introduction-1)
  - [Edit a Requisition](#edit-a-requisition)
  - [Select Requisition Number](#select-requisition-number)
  - [Display Requisition](#display-requisition)
  - [Log Code Sheets](#log-code-sheets-1)
  - [Introduction](#introduction-2)
  - [Amend Requisition](#amend-requisition)
  - [Menu Path](#menu-path-1)
  - [Setup Parameters](#setup-parameters)
  - [Delivery Schedules](#delivery-schedules)
  - [Add Amendment Type](#add-amendment-type)
  - [Display Amendment](#display-amendment)
  - [Sign Amendment](#sign-amendment)
- [########### CHAPTER 5 ADJUST A REQUISITION RECEIVING REPORT](#chapter-5-adjust-a-requisition-receiving-report)
  - [Introduction](#introduction-3)
  - [Menu Path](#menu-path-2)
  - [Setup Parameters](#setup-parameters-1)
  - [Create Adjustment](#create-adjustment)
  - [Select Partial Date](#select-partial-date)
  - [Display Adjustment](#display-adjustment)
  - [Review Adjustment](#review-adjustment)
  - [Print Adjustment](#print-adjustment)
  - [Introduction](#introduction-4)
  - [Remove 2237](#remove-2237)
  - [Select Requisition Number](#select-requisition-number-1)
  - [Cancel Unobligated Requisition](#cancel-unobligated-requisition)
  - [Menu Path](#menu-path-3)
  - [Select Requisition](#select-requisition)
- [########### CHAPTER 7 CHANGING THE STAUS OF A REQUISITION](#chapter-7-changing-the-staus-of-a-requisition)
- [# ########### INDEX](#index)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three ways to change a requisition. You can EDIT a requisition (Chapter 3)if you haven’t affixed your electronic signature to the Requisition yet.

After you’ve entered your electronic signature code, if the Requisition has been Obligated, you can AMEND the requisition (Chapter 4).

You can ADJUST the Requisition receiving report (Chapter 5) if you need to lower the quantity received.

## Menu Path 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Requisition

Edit an Incomplete Requisition

Amendment to Requisition

Adjustment Voucher to Requisition

Cancel an Unobligated Requisition

Remove 2237 from Requisition

Display Purchase Order/Requisition

Change Delivery Date on Requisition

Enter DEPOT/GSA PUSH Order to PO Register

Change DEPOT/GSA PUSH Order on PO Register

Item File Edit

Requisition Register

All Status Amendment to Req

Select Requisition Processing Option: Adjustment Voucher to Requisition

## Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number.

Enter a requisition number. If you don’t know the requisition number, enter three question marks (???) at the Requisition No.: prompt and IFCAP will list the available requisitions.

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY,DC

REQUISITION NO.: B9

CHOOSE FROM:

1 B90001 999-B90001 12-23-98 RQ Pending Fiscal Action

FCP: 060 \$ 144.00

2 B90002 999-B90002 03-09-99 RQ Pending Fiscal Action

FCP: 060 \$ 1.00

3 B90003 999-B90003 03-16-99 RQ Pending Fiscal Action

FCP: 060 \$ 15.00

4 B90004 999-B90004 03-16-99 RQ Pending Fiscal Action

FCP: 060 \$ 15.00

5 B90005 999-B90005 03-16-99 RQ Pending PPM Clerk Signature

FCP: 060 \$ 10.00:

6 B90006 999-B90006 03-17-99 RQ Pending Fiscal Action

FCP: 060 \$ 10.00

7 B90007 999-B90007 03-17-99 RQ Pending PPM Clerk Signature

FCP: 060 \$ 5.00

8 B90008 999-B90008 03-22-99 RQ Ordered and Obligated

FCP: 060 \$ 27.60

9 B90009 999-B90009 06-16-99 RQ Partial Order Received

## Create Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the requisition number. The software will assign the correct adjustment number.

If you wish to continue with the adjustment voucher hit the Enter key.

Enter the effective date of the adjustment voucher.

Enter the name of the Requisition clerk responsible for the adjustment voucher.

Enter the appropriate status of the order after the adjustment voucher is completed. In this example the status will be Partial Received Amended because the Quantity Received is being reduced not deleted completely.

REQUISITION NO.: B90009 999-B90009 06-16-99 RQ Partial Order Received

FCP: 060 \$ 24.00

Adjustment number: 1

Do you wish to continue? YES// (YES)

EFFECTIVE DATE: T (JAN 31, 2000)

PA/PPM/AUTHORIZED BUYER: IFBUYER,ONE IBO

AMENDMENT/ADJUSTMENT STATUS: ??

This is a pointer to the Purchase Order Status File (442.3).

It indicates the status of the amendment/adjustment.

Choose from:

Complete Order Received (Amended) 31

Ordered (No Fiscal Action)-Amended 23

Ordered and Obligated (Amended) 21

Partial Order Received (Amended) 26

Transaction Complete (Amended) 41

AMENDMENT/ADJUSTMENT STATUS: Partial Order Received (Amended) 26

## Select Partial Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the partial date. If the partial date is more than thirty days old, check with Fiscal Service on the payment status.

Enter the number for the item you wish to adjust.

Decrease the amount listed at the Qty Being Received: prompt to the quantity that you actually received. IFCAP will prompt you to enter another item number. If you don’t want to enter another item number, press the enter key.

Select PARTIAL DATE: 1 6-16-1999

This partial receipt is more than 30 days old.

Please check payment status with Fiscal.

Would you like to continue? ? Y (YES)

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

Select ITEM: 1 SHAVING KIT, SURGICAL PREPARATION. DISPOSABLE. CONSISTS OF

QTY BEING RECEIVED: 6// 3

Select ITEM:

## Display Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the adjustment voucher you just created, and allow you to edit the description of the requisition if you want to explain the cause for the adjustment.

ADJUSTMENT VOUCHER 1/31/2000

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Adjustment Voucher for Purchase Order 999-B90009

Item No. 1 SHAVING KIT, SURGICAL PREPARATION. DISPOSABLE. CONSISTS OF

PLASTIC TRAY WITH SEPARATIONS FOR RINSE AND SOAP WATER, WATER REPELLENT

LINEN PROTECTOR, DOUBLE EDGE RAZOR WITH BLADE, ANTI-INFECTIVE SOAP OR

DETERGENT, CLEAN UP MATERIAL TO DRY SHAVEN AREA. FOR PREPARATION OF

SKIN PRIOR TO OPERATIONS. (WHS LOC B11)

Items per UN: 1 NSN: 6515-00-103-6659

12 UN at \$ 2.00 = \$ 24.00

ORIGINALLY QTY RECEIVED = 6 ,COST = \$ 12

will now read: QTY RECEIVED=3, COST=\$6

ENTER '^' TO HALT:

Vendor: IFVENDOR,ONE

APPROPRIATION: 3690160

This Receiving Report will now read:

CONTRACTING OFFICER: IFBUYER,ONE

ENTER '^' TO HALT:

Edit Description ? NO// (NO)

## Review Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the adjustment voucher to see that it is correct. IFCAP will ask you if the adjustment is ready to forward to Fiscal.

Approve and print (in FISCAL and SUPPLY) Adjustment no.: 1? NO// Y (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

...HMMM, I'M WORKING AS FAST AS I CAN...

...please wait while I update the due-ins at the inventory points...

SEND TO SUPPLY

QUEUE ON DEVICE: SF

1 SFCS6\$PRT-10/6/UP ANY CIOFO

2 SFCS6\$PRT-12/6/UP ANY CIOFO

3 SFCS6\$PRT-16/6/UP ANY CIOFO

Choose 1-3\> 2 SFCS6\$PRT-12/6/UP ANY CIOFO

Requested Start Time: NOW// (JAN 31, 2000@17:42:35)

SEND TO FISCAL

## Print Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will print the adjustment for you and the contracting officer to sign. If you want to adjust another receiving report, enter a requisition number at the Requisition No.: prompt. Otherwise, press the Enter key to return to the Requisition Processing Menu.

QUEUE ON DEVICE: LAT LAT_TERM LAT

SUBJECT: ADJUSTMENT VOUCHER

Adjustment Voucher for Purchase Order 999-B40016

Adjustment Partial 2

Vendor: GENERAL SERVICES ADMINISTRATION

APPROPRIATION: 3640151.001 3040/21-25

This adjustment will read:

Total Amount: 5.25

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Approve subject to final action on R/S on items indicated. \| DATE \|

P.O. NO.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\| \|

SIGNATURE OF CONTRACTING OFFICER \| \|

\| \|

/ES/REDACTED 4/27/94 \| 4/27/94 \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\|

SEND TO FISCAL

REQUISITION NO.:

Select Requisition Processing Option:

########### CHAPTER 6 REMOVE 2237 OR CANCEL A REQUISITION

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally, a clerk may attach a 2237 to a Requisition and then decide not to include that 2237 on the order. The 2237 can be separated from the Requisition. A clerk may decide that an order in progress is not going to be completed at all and should be cancelled.

## Remove 2237

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you determine that a 2237 should not be on an Unobligated Requisition you have to Remove the 2237 from the Requisition. This permits the 2237 to be placed on a different Requisition or it may be sent back to the service for cancellation. The Requisition Clerk may then assign another 2237(s) to the Requisition.

New Requisition

Edit an Incomplete Requisition

Amendment to Requisition

Cancel an Unobligated Requisition

Remove 2237 from Requisition

Display Purchase Order /Requisition

Change Delivery Date on Requisition

Enter DEPOT/GSA PUSH Order to PO Register

Change DEPOT/GSA PUSH Order on PO Register

Item File Edit

Requisition Register

Select Requisition Processing Option: Remove 2237 from Requisition

## Select Requisition Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the station number.

Enter the 2237 number at the Requisition No: prompt. If you don’t know the 2237 number, enter three question marks (???) at the prompt and IFCAP will display a list of the available requisitions.

IFCAP will ask you to confirm that you want to delete the 2237 from the Requisition. If you accept the default of NO the 2237 will remain on the Requisition. If you enter YES the 2237 will be removed from the Requisition and the user will be ~~and~~ returned to the Requisition Processing Menu.

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY,DC

Enter the Order number where the 2237 information resides.

REQUISITION NO.: ???

CHOOSE FROM:

B40001 06-10-94 RQ Order Not Completely Prepared FCP: 101 \$ 0.00

B40002 06-14-94 RQ Pending PPM Clerk Signature FCP: 101 \$100.00

B40003 11-29-93 RQ Order Not Completely Prepared FCP: \$ 0.00

B40004 11-29-93 RQ Order Not Completely Prepared FCP: \$ 0.00

REQUISITION NO.: B40002 999-B40002 06-14-94 RQ Pending PPM Clerk Signature

FCP: 101 \$ 100.00

Delete 999-B40002, are you sure? NO// Y (YES)

## Cancel Unobligated Requisition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is possible to simply cancel an Unobligated Requisition if it is not going to be processed to completion.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Requisition Processing ...

LOG/GSA/DLA Code Sheets Menu ...

Display/Print Menu (PPM) ...

Select Requisition Clerk Menu Option: Requisition Processing

New Requisition

Edit an Incomplete Requisition

Amendment to Requisition

Cancel an Unobligated Requisition

Remove 2237 from Requisition

Display Purchase Order /Requisition

Change Delivery Date on Requisition

Enter DEPOT/GSA PUSH Order to PO Register

Change DEPOT/GSA PUSH Order on PO Register

Item File Edit

Requisition Register

Select Requisition Processing Option: Cancel an Unobligated Requisition

## Select Requisition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number.

Enter the requisition you want to cancel. If you don’t remember the requisition number, type three question marks (???) and IFCAP will list the available requisitions. IFCAP will ask you to confirm that you want to cancel the requisition. IF you enter N the requisition will not be cancelled. If you enter Y the requisition is cancelled.

IFCAP will prompt you to enter another requisition to cancel. If you don’t want to cancel any more requisitions, enter three question marks (???) and IFCAP will return to the Requisition Processing menu.

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY,DC

REQUISITION NO.: ???

CHOOSE FROM:

B40009 01-12-94 RQ Order Not Completely Prepared FCP: 101 \$

B40010 01-12-94 RQ Order Not Completely Prepared FCP: 101 \$

B40011 01-12-94 RQ Pending PPM Clerk Signature FCP: 101 \$ 100

REQUISITION NO.: B40011 999-B40011 01-12-94 RQ Pending PPM Clerk Signature

FCP: 101 \$ 100

SURE YOU WANT TO CANCEL PURCHASE ORDER ? Y (YES)

REQUISITION NO.:

# ########### CHAPTER 7 CHANGING THE STAUS OF A REQUISITION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you process adjustments (Chapter 5), IFCAP will ask you if you want to change the status of the requisition. This chapter lists all the statuses you can assign to a requisition, and explains where that status is represented on a flowchart. The flowchart depicts every primary IFCAP function from funding control points to paying vendors.

|                                                   |                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Status of Request, Transaction, or Purchase Order | The request is pending action at node number                                                                             |
| Cancelled Order                                   | Requisition Clerk cancelled the request at 19.                                                                           |
| Complete Order Received (Amended)                 | 35 or 36.                                                                                                                |
| Ordered and Obligated (Amended)                   | 28 or 30. Talk to the vendor.                                                                                            |
| Partial Order Received (Amended)                  | Either 35, 36, 37, 38, 40, 41 or END. Talk to the Accounting Technician if you want to know if they’ve sent the payment. |
| Transaction Complete                              | Certified Purchase Orders: your request could be at 30, 33, 36, 38, 41 or END; All other requests: 40, 41, 42 or END.    |
| Transaction Complete (Amended)                    | Same as above, except that the Requisition Clerk amended the Requisition.                                                |

![](ifcap-version-5-1-requisition-clerk-user-s-guide/002.png)![](ifcap-version-5-1-requisition-clerk-user-s-guide/003.png)

########### CHAPTER 8 ERROR MESSAGES AND THEIR RESOLUTION

The following are errors that you may encounter when processing a requisition or purchase order. Each error is listed alphabetically by code. While some of the problems may be fixed by the user, many must be fixed by your Information Resources Management Service. If this is the case, record the error code and message and report the error immediately to your Information Resources Management Service.

|                |                                                                                                   |                                                                                                                                                             |
|----------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Error Code | Error Message                                                                                 | Reason                                                                                                                                                  |
| NAUC^\<LIN\>   | "No actual unit cost for this ITEM."                                                              | There is no Actual Unit Cost entry for the \<LIN\> Item in the Procurement & Accounting Transactions file.                                                  |
| NCNO^\<LIN\>   | "The type of order is not a P.O. and no contract number was entered for this ITEM in this P.O."   | The order is a Direct Order. There is no contract number entered for this \<LIN\> Item in the Procurement & Accounting Transactions file.                   |
| NDD            | "No delivery date for this P.O. in file 442."                                                     | There is no Delivery Date in the Procurement & Accounting Transactions file.                                                                                |
| NDP0           | "No entry in file 440.2 for direct delivery patient pointer."                                     | The Direct Delivery Patient entered in the Procurement & Accounting Transactions file for this purchase order cannot be found in file 440.2.                |
| NES            |                                                                                                   | There is no Electronic Signature entry in Procurement & Accounting Transactions file.                                                                       |
| NFT0^\<SITE\>  | "No entry in file 411.2 for facility type pointer from file 411."                                 | There is no entry in the Facility Type file (file 411.2) for the Facility Type field of the Admin. Activity Site Parameter file (file 411).                 |
| NFT^\<SITE\>   | "No facility type pointer for site in file 411."                                                  | The Admin. Activity Site Parameter file has no entry in it.                                                                                                 |
| NI2N^\<ITEM\>  | "No ITEM node 2 for this P.O."                                                                    | There are no ITEMS listed under the Item multiple in the Procurement & Accounting Transactions file (file 442).                                             |
| NMIC           | "No mail invoice city in file 411."                                                               | The city listed for No Mail Invoice could not be found in the Admin. Activity Site Parameter file.                                                          |
| NMIL           | "Node 4 in file 411 missing."                                                                     | No MAIL INVOICE LOCATION in Admin. Activity Site Parameter file (file 411).                                                                                 |
| NMIS           | "No state file pointer in file 411."                                                              | No Mail Invoice State pointer in Admin. Activity Site Parameter file.                                                                                       |
| NMIZ           | "No mail invoice ZIP CODE entry in file 411."                                                     | No Mail Invoice Zip in Admin. Activity Site Parameter file.                                                                                                 |
| NNET           | "No NET amount entry for this P.O."                                                               | There is no Net Amount entry in the Procurement & Accounting Transactions file.                                                                             |
| NOPR           | "No PROPOSAL entry in file 442 for this P.O."                                                     | There is no Proposal entry in Procurement & Accounting Transactions file.                                                                                   |
| NOPT           | "No patient file entry for direct delivery patient pointer."                                      | There is no entry in the Patient file (file 2) for the Direct Delivery Patient entered for this P.O. in file 442.                                           |
| NP12           | "No node 12 in file 442 for this P.O."                                                            | No electronic signature in Procurement & Accounting Transactions file (file 442).                                                                           |
| NP12           | "Node 12 missing in record."                                                                      | No invoice address in Procurement & Accounting Transactions file (file 442).                                                                                |
| NPH            | "No phone number for this PPM in the person file."                                                | The P&C user does not have a phone number entry in the Person File under his/her entry.                                                                     |
| NPH            | "No phone number for this PPM in the person file."                                                | The person file does not have a phone number listed for this PPM.                                                                                           |
| NPHN           | "No phone number node in the person file for this PPM."                                           | The P&C user does not have a phone number node in the Person File under his/her record entry.                                                               |
| NPIA           | "Invoice address missing."                                                                        | There is no Invoice Address in node 12 in the Procurement & Accounting Transactions file.                                                                   |
| NPO0           | "Zero node of record missing. Unable to check further."                                           | No Procurement & Accounting Transactions file (file 442) entry exists.                                                                                      |
| NPO1           | "Label is missing in record."                                                                     | No VENDOR, SHIP TO or ACCOUNTING information found for the Procurement & Accounting Transactions file record.                                               |
| NPOD           | "No purchase order date for this P.O."                                                            | There is no Purchase Order Date in the Procurement & Accounting Transactions file (file 442).                                                               |
| NPPM           | "No purchasing agent entry in file 442 for this P.O."                                             | There is no Purchasing Agent/PPM Agent entry in the Procurement & Accounting Transactions file.                                                             |
| NPPT           | "No prompt payment terms entered in P.O."                                                         | There are no Prompt Payment Terms entries in Procurement & Accounting Transactions file (file 442).                                                         |
| NQTY^\<LIN\>   | "No quantity listed for this ITEM."                                                               | There is no Quantity listed for the Line Item Number (\<LIN\>) in the Procurement & Accounting Transactions file.                                           |
| NRL            | "No receiving location node in file 411."                                                         | No Receiving Location node in Admin. Activity Site Parameter file.                                                                                          |
| NSC            | "No Source Code for type of order for this P.O."                                                  | No source code entry in the Procurement & Accounting Transactions file.                                                                                     |
| NSIT           | "No site entry in file 442."                                                                      | No Site entry in Procurement & Accounting Transactions file.                                                                                                |
| NSP0^\<SITE\>  | "No node zero in file 411."                                                                       | No FACILITY TYPE pointer in Admin. Activity Site Parameter file for SITE in Procurement & Accounting Transactions file.                                     |
| NST0           | "No state file node zero."                                                                        | No STATE entry in State file (file 5) for Vendor Address State pointer in Vendor file.                                                                      |
| NSTA           | "Abbreviation missing in state file entry."                                                       | No Abbreviation in State file.                                                                                                                              |
| NSTA           | "No Abbreviation in State file."                                                                  | There is no abbreviation in the state file for this state.                                                                                                  |
| NSTDP          | "No State file pointer in Direct Delivery Address in 440.2."                                      | No State file pointer in Direct Delivery Address field in Direct Delivery Patients file.                                                                    |
| NSTL           | "No Ship to pointer to entry in file 441."                                                        | No Ship To pointer to Admin. Activity Site Parameter file.                                                                                                  |
| NSTP           | "No pointer from the Vendor Address to the State file."                                           | No Vendor Address State file pointer in the Vendor file.                                                                                                    |
| NSTS           | "Within file 411 there is no Ship To suffix for the receiving location for this EDI P.O."         | The Ship To entry for this purchase order in file 442 cannot be found in file 411 (Ship To Suffix). An EDI purchase order requires the Ship To suffix.      |
| NSTT           | "No State file pointer in Receiving Location in file 411."                                        | No State File pointer in Receiving Location multiple in Admin. Activity Site Parameter file.                                                                |
| NUNI^\<LIN\>   | "No name entry in unit of purchase file for unit of purchase pointer in ITEM entry in P.O. file." | No Name entry in the Unit of Issue file (file 420.5) for the Unit of Purchase entry for the \<LIN\> Item in the Procurement & Accounting Transactions file. |
| NUOP^\<LIN\>   | "No unit of purchase pointer for this ITEM in this P.O."                                          | No Unit of Purchase pointer entered for the \<LIN\> Item in the Procurement & Accounting Transactions file.                                                 |
| NUPN^\<LIN\>   | "No entry in unit of issue file for unit of purchase pointer in ITEM entry in P.O. file."         | No entry in the Unit of Issue file (file 420.5) for the Unit of Purchase entry for the \<LIN\> Item in the Procurement & Accounting Transactions file.      |
| NV0            | "No node zero in vendor file."                                                                    | No Vendor file (file 440) entry for the Vendor pointer from Procurement & Accounting Transactions file (file 442).                                          |
| NVID           | "Missing a vendor ID number for an EDI vendor."                                                   | There is no Vendor ID Number for an EDI Vendor in the Vendor file.                                                                                          |

########### GLOSSARY

# |                                            |                                                                                                                                                                                                                                                                                                                                                                                                                  |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1358                                       | VA Form 1358, Estimated Obligation or Change in Obligation.                                                                                                                                                                                                                                                                                                                                                      |
| 2138                                       | VA Form 90-2138, Order for Supplies or Services. First page of a VA Purchase Order.                                                                                                                                                                                                                                                                                                                              |
| 2139                                       | VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.                                                                                                                                                                                                                                                                                                  |
| 2237                                       | VA Form 90-2237, Request, Turn-in and Receipt for Property or Services. Used to request goods and services.                                                                                                                                                                                                                                                                                                      |
| A&MM                                       | Acquisition and Materiel Management Service.                                                                                                                                                                                                                                                                                                                                                                     |
| Accounting Technician                      | Fiscal employee responsible for obligation of and payment for goods and services. Accounting Technicians process accounting transactions and transmit them to FMS.                                                                                                                                                                                                                                               |
| ADP Security Officer                       | The individual at your station who is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.                                                                                                                                                                                                           |
| Agent Cashier                              | The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.                                                                                                                                                                                                                                                                |
| Allowance table                            | Reference table in FMS that provides financial information at the level immediately above the sub-allowance level.                                                                                                                                                                                                                                                                                               |
| Amendment                                  | A document that changes the information contained in a specified Order.                                                                                                                                                                                                                                                                                                                                          |
| Approve Requests                           | The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or other request form and transmit said request to A&MM/Fiscal.                                                                                                                                                                                                                                                           |
| Authorization                              | A charge to an obligated 1358. Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.                                                                                                                                                                                           |
| Authorization Balance                      | The amount of money remaining that can be authorized against the 1358. The service balance minus total authorizations.                                                                                                                                                                                                                                                                                           |
| Batch Number                               | A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.                                                                                                                                                                                                                                                      |
| Breakout Code                              | A set of A&MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).                                                                                                                                                                                                                                                      |
| Budget Analyst                             | Fiscal employee responsible for distributing and transferring funds.                                                                                                                                                                                                                                                                                                                                             |
| Budget Object Code                         | Fiscal accounting element that tells what kind of item or service is being procured~~.~~ Budget object codes are listed in the VA Handbook 4671.2                                                                                                                                                                                                                                                                |
| Budget Sort Category                       | Used by Fiscal Service to identify the allocation of funds throughout their facility.                                                                                                                                                                                                                                                                                                                            |
| Ceiling Transactions                       | Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.                                                                                                                                                                                                                                              |
| Classification of Request                  | An identifier a Control Point can assign to track requests that fall into a category, e.g., Memberships, Replacement Parts, and Food Group III.                                                                                                                                                                                                                                                                  |
| Common Numbering Series                    | This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinator establishes the Common Numbering Series used by each facility.                                     |
| Control Point                              | Financial element, existing ONLY in IFCAP that corresponds to the ACC~~S~~ number in FMS. Also the division of monies to a specified service, activity or purpose from an appropriation.                                                                                                                                                                                                                         |
| Control Point Clerk                        | The user within the service who is designated to input requests and maintain the Control Point records for a Service.                                                                                                                                                                                                                                                                                            |
| Control Point Official                     | The individual authorized to expend government funds for ordering of supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.                                                                                                                                             |
| Control Point Official's Balance           | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                    |
| Control Point Requestor                    | The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&MM/Fiscal.                                                                                                               |
| Cost Center                                | “Subsection” of a Fund Control Point. Cost centers allow fiscal staff to create total expense reports for a section or service, and allow requestors to assign requests to that section or service. Cost centers are listed in the VA Handbook 4671.1.                                                                                                                                                           |
| Date Committed                             | The date that you want IFCAP to commit funds to the purchase.                                                                                                                                                                                                                                                                                                                                                    |
| Default                                    | A suggested response that is provided by the system.                                                                                                                                                                                                                                                                                                                                                             |
| Deficiency                                 | When a budget has obligated and expended more than it was funded (see MP-4, Part V, Section C).                                                                                                                                                                                                                                                                                                                  |
| Delinquent Delivery Listing                | A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information.                                                                                                                                                                                                                                      |
| Direct Delivery Patient                    | A patient who has been designated to have goods delivered directly to him/her from the vendor.                                                                                                                                                                                                                                                                                                                   |
| Discount Item                              | This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.                                                                                                                                                                                                                                                      |
| EDI Vendor                                 | A vendor with whom the VA has negotiated an arrangement to accept and fill orders electronically.                                                                                                                                                                                                                                                                                                                |
| Electronic Data Interchange (EDI)          | Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.                                                                                                                                                                                                                                                                              |
| Electronic Signature                       | The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off-station will require a written signature as well.                                                                                                                                                                                                                             |
| Expenditure Request                        | A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).                                                                                                                                                                                                                                                                                         |
| FCP                                        | Fund Control Point (see Control Point).                                                                                                                                                                                                                                                                                                                                                                          |
| Federal Tax ID                             | A unique number that identifies your station to the Internal Revenue Service.                                                                                                                                                                                                                                                                                                                                    |
| Fiscal Balance                             | The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidation submitted against the obligation.                                                                                                                                                                                                                           |
| Fiscal Quarter                             | The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.                                                                                                                                                                                                                                                                                                          |
| Fiscal Year                                | Twelve-month period from October 1 to September 30.                                                                                                                                                                                                                                                                                                                                                              |
| FMS                                        | Financial Management System, the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.              |
| FOB                                        | Freight on Board. An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means that shipping charges are due to the shipper, and must be paid when the shipper arrives at the warehouse with the item.                                                            |
| FPDS                                       | Federal Procurement Data System.                                                                                                                                                                                                                                                                                                                                                                                 |
| FTEE                                       | Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned an FTEE of 0.5, as would a full-time employee that worked for half of a year.                                                                                                                   |
| Fund Control Point                         | See Control Point                                                                                                                                                                                                                                                                                                                                                                                                |
| Funds Control                              | A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.                                                                                                                                                                                                                                                                                       |
| Funds Distribution                         | A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.                                                                                                                                                                                                                                                                |
| GBL                                        | Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of \$250.00.                                                                                                                                                                                                                                                                                                     |
| GL                                         | General Ledger.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Imprest Funds                              | Monies used for cash or 3rd party draft purchases at a VA facility.                                                                                                                                                                                                                                                                                                                                              |
| Integrated Supply Management System (ISMS) | ISMS is the system that replaced LOG I for Expendable Inventory. IFCAP sends PHA and PHM transactions to this system.                                                                                                                                                                                                                                                                                            |
| ISMS                                       | Integrated Supply Management System.                                                                                                                                                                                                                                                                                                                                                                             |
| Item File                                  | A listing of items specified by A&MMS as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.                                                                                                                                                                                                           |
| Item History                               | Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.                                                                                                                                                                                                                                                               |
| Item Master Number                         | A computer generated number used to identify an item in the Item File.                                                                                                                                                                                                                                                                                                                                           |
| Justification                              | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.                                                                                                                                                                                                                           |
| Liquidation                                | The amount of money to be paid a vendor. The payment will be posted on the 1358 document and will reduce the Fiscal Balance. They are processed through payment/invoice tracking.                                                                                                                                                                                                                                |
| LOG I                                      | LOG I is the name of the Logistics A&MM computer located at the Austin Data Processing Center. This system continues to support the Consolidated Memorandum of Receipt.                                                                                                                                                                                                                                          |
| Mandatory Source                           | A Federal Agency that sells supplies and services to the VA. VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.                                                                                                                                                                                                                                                        |
| MSC Confirmation Message                   | A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of documents.                                                                                                                                                                                                                                                                             |
| Obligation                                 | The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.                                                                                                                                                                                                                                                                                                              |
| Obligation (Actual) Amount                 | The actual dollar figure obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document in IFCAP.                                                                                                                                                                                                                   |
| Obligation Data                            | A Control Point option that allows the Control Point Clerk to enter data not recorded by IFCAP.                                                                                                                                                                                                                                                                                                                  |
| Organization Code                          | Accounting element functionally comparable to Cost Center, but used to organize purchases by the budget that funded them, not the purposes for spending the funds.                                                                                                                                                                                                                                               |
| Outstanding 2237                           | A&MM report that lists all the IFCAP generated 2237s pending action in A&MM.                                                                                                                                                                                                                                                                                                                                     |
| PAID                                       | Personnel Accounting Integrated Data.                                                                                                                                                                                                                                                                                                                                                                            |
| Partial                                    | A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.                                                                                                                                                                                                                                                                                             |
| Partial Date                               | The date that a warehouse clerk created a receiving report for a shipment.                                                                                                                                                                                                                                                                                                                                       |
| PAT Number                                 | Pending Accounting Transaction number - the primary FMS reference number.                                                                                                                                                                                                                                                                                                                                        |
| Personal Property Management               | A section of A&MM Service responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process all requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.                                              |
| PPM                                        | Personal Property Management.                                                                                                                                                                                                                                                                                                                                                                                    |
| Program Code                               | Accounting element that identifies the VA initiative or program that the purchase will support.                                                                                                                                                                                                                                                                                                                  |
| Prompt Payment Terms                       | The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).                                                                                                                                                                                             |
| Purchase History Add (PHA)                 | Procurement History Add transaction. This updates the Procurement History file in Austin when orders are obligated in IFCAP. This same transaction is also used to send a PO for EDI processing.                                                                                                                                                                                                                 |
| Purchase History Mod (PHM)                 | Procurement History Modification. This updates the Procurement History file in Austin when orders are amended                                                                                                                                                                                                                                                                                                    |
| Purchase Order                             | A government document authorizing the purchase of ~~the~~ goods or services at the terms indicated.                                                                                                                                                                                                                                                                                                              |
| Purchase Order Acknowledgment              | Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).                                                                                                                                                                                                                                                                                           |
| Purchase Order Status                      | The status of completion of a purchase order (e.g., Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).                                                                                                                                                                                                                                                               |
| Purchasing Agents                          | A&MM employees legally empowered to create purchase orders to obtain goods and services from commercial vendors.                                                                                                                                                                                                                                                                                                 |
| Quarterly Report                           | A Control Point listing of all transactions (Ceilings, Obligations, and Adjustments) made to a Control Point's Funds.                                                                                                                                                                                                                                                                                            |
| \Quotation for Bid                         | Standard Form 18. Used by Purchasing Agents to obtain written/electronic bids from vendors.                                                                                                                                                                                                                                                                                                                      |
| Receiving Report                           | Report that Warehouse Clerk creates to record that the warehouse has received an item. The VA document used to indicate the quantity and dollar value of the goods being received.                                                                                                                                                                                                                               |
| Reference Number                           | Also known as the Transaction Number. The computer generated number that identifies a request. It is comprised of the Station Number-Fiscal Year-Quarter -Control Point - 4-digit Sequence Number.                                                                                                                                                                                                               |
| Repetitive Item List                       | A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate requests from the list.                                                                                                                                                                                                                |
| Requestor                                  | See “Control Point Requestor.”                                                                                                                                                                                                                                                                                                                                                                                   |
| Requisition                                | The order form used to buy from a Government vendor.                                                                                                                                                                                                                                                                                                                                                             |
| Running Balance                            | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                   |
| Section Request                            | A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.                                                                                                                                                                                                                                         |
| Service Balance                            | The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.                                                                                                                                                                                                  |
| SF-18                                      | Request for Quotation.                                                                                                                                                                                                                                                                                                                                                                                           |
| SF-30                                      | Amendment of Solicitation/Modification of Contract.                                                                                                                                                                                                                                                                                                                                                              |
| Short Description                          | A phrase that describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).                                                                                                                                                                                                         |
| Site Parameters                            | Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.                                                                                                                                                                                                                                                  |
| Sort Group                                 | An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.                                                                                                                                                                                                                                                            |
| Sort Order                                 | The order in which the budget categories will appear on the budget distribution reports.                                                                                                                                                                                                                                                                                                                         |
| Special Remarks                            | A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.                                                                                                                                                                                                                                    |
| Stacked Documents                          | The POs, RRs & 1358s that are sent electronically to Fiscal and stored in a file rather than being printed immediately.                                                                                                                                                                                                                                                                                          |
| Status of Funds                            | Fiscal's on-line status report of the monies available to a Control Point. FMS updates this information automatically.                                                                                                                                                                                                                                                                                           |
| Sub-control Point                          | A specific budget within a Control Point, defined by a Control Point user.                                                                                                                                                                                                                                                                                                                                       |
| Sub-cost Center                            | A subcategory of Cost Center. In IFCAP 5.0, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.                                            |
| Tasked Job                                 | A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.                                                                                                                                                                                                                                                      |
| TDA                                        | See "Transfer of Disbursing Authority."                                                                                                                                                                                                                                                                                                                                                                          |
| Total Authorizations                       | The total amount of the authorizations created for the 1358 obligation.                                                                                                                                                                                                                                                                                                                                          |
| Total Liquidations                         | The total amount of the liquidation against the 1358 obligation.                                                                                                                                                                                                                                                                                                                                                 |
| Transaction Number                         | The number of the transaction that funded a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.                                                                                                                                                                                                                        |
| Transmission Number                        | A sequential number given to a data string when it is transmitted to the AAC; used for tracking message traffic.                                                                                                                                                                                                                                                                                                 |
| Type Code                                  | A set of A&MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.                                                                                                                                                                                                                                                                                     |
| Vendor file                                | An IFCAP file of vendors solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. File 440 contains information about the vendors solicited by your station. The debtor's address may be drawn from this file, but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added. |
| Vendor ID Number                           | The ID number assigned to a vendor by FMS.                                                                                                                                                                                                                                                                                                                                                                       |
| VRQ                                        | FMS Vendor Request document. When users send vendor information to FMS, FMS sends a VRQ document to IFCAP with the vendor information, ensuring that the information in the IFCAP vendor file matches the information in the FMS vendor table.                                                                                                                                                                   |

# # ########### INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Accounting Technician, 7

ADJUST the Requisition, 25

Amend Requisition, 21

Budget Object Code (BOC), 13

Cost Center, 11

Edit an Incomplete Requisition, 17

Numbering system, 7

Paragraph numbering, 7

Requisition Clerk, 7, 9

Requisition Processing, 14, 17, 20, 27, 29

Requisitions, 7, 9

Transaction Number, 10, 17