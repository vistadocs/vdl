---
title: IFCAP Version 5.1 Control Point Requestor User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Control Point Requestor User's Guide
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
menu_options: 6
description: 
audience: 
keywords: 
  - request
  - strong
  - table
  - contents
  - number
  - vendor
  - prompt
  - control
  - point
  - class
page_count: 0
word_count: 19045
section_count: 24
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1cp_requestor.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1cp_requestor.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Control Point RequestorUser's Guide

![](ifcap-version-5-1-control-point-requestor-user-s-guide/001.png)

March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial Systems

Revision History

Initiated on 12/29/04

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 52%" />
<col style="width: 23%" />
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
<td>4.0</td>
<td><p>Updates based on patch PRC*5.1*257.</p>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p></td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="odd">
<td>October 2011</td>
<td>3.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See page <a href="#PRC_158_A">53</a>, <a href="#_Toc306433934">57</a>.</td>
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

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [INTRODUCTION](#introduction)
  - [The Role of the Control Point Requestor](#the-role-of-the-control-point-requestor)
  - [How to Use this Manual](#how-to-use-this-manual)
  - [Reference Numbering System](#reference-numbering-system)
  - [Package Management, Legal Requirements, and Security Measures](#package-management-legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
- [HOW TO BECOME A REQUESTOR](#how-to-become-a-requestor)
- [HOW TO CREATE REQUESTS](#how-to-create-requests)
  - [Introduction](#introduction-1)
  - [Which Request Form Should You Use?](#which-request-form-should-you-use)
  - [How to Consult the Item Master File](#how-to-consult-the-item-master-file)
    - [Introduction](#introduction-2)
    - [Menu Path](#menu-path)
    - [Setup Parameters](#setup-parameters)
    - [Vendor Information](#vendor-information)
    - [Order Type](#order-type)
  - [How to Create a Repetitive (PR Card) Order Request](#how-to-create-a-repetitive-pr-card-order-request)
    - [Introduction](#introduction-3)
    - [Setup Parameters](#setup-parameters-1)
    - [Create Transaction Number](#create-transaction-number)
    - [Classification and Sort Groups](#classification-and-sort-groups)
    - [Requestor and Priority](#requestor-and-priority)
    - [Special Remarks](#special-remarks)
    - [Vendor Information](#vendor-information-1)
    - [Item Selection](#item-selection)
    - [Item History and BOC](#item-history-and-boc)
    - [Delivery Schedules](#delivery-schedules)
  - [How to Create a Non-Repetitive Order Request](#how-to-create-a-non-repetitive-order-request)
    - [Introduction](#introduction-4)
    - [Setup Parameters](#setup-parameters-2)
    - [Create Transaction Number](#create-transaction-number-1)
    - [Classification and Sort Groups](#classification-and-sort-groups-1)
    - [Priority](#priority)
    - [Vendor Information](#vendor-information-2)
    - [Description](#description)
    - [Stock Number](#stock-number)
    - [Delivery Schedules](#delivery-schedules-1)
  - [How to Create a Repetitive and Non-Repetitive Order Request](#how-to-create-a-repetitive-and-non-repetitive-order-request)
    - [Introduction](#introduction-5)
    - [Setup Parameters](#setup-parameters-3)
    - [Create Transaction Number](#create-transaction-number-2)
    - [Classification and Sort Groups](#classification-and-sort-groups-2)
    - [Priority](#priority-1)
    - [Vendor Information](#vendor-information-3)
    - [Description](#description-1)
    - [Stock Number](#stock-number-1)
    - [Delivery Schedules](#delivery-schedules-2)
  - [How to Create an Issue Book/Interval Issue Request](#how-to-create-an-issue-bookinterval-issue-request)
    - [Introduction](#introduction-6)
    - [Setup Parameters](#setup-parameters-4)
    - [Create Transaction Number](#create-transaction-number-3)
    - [Classification and Sort Groups](#classification-and-sort-groups-3)
    - [Priority](#priority-2)
    - [Select Cost Center](#select-cost-center)
    - [Add Line Item](#add-line-item)
  - [How to Create a 1358 Order Request](#how-to-create-a-1358-order-request)
    - [Introduction](#introduction-7)
    - [Setup Parameters](#setup-parameters-5)
    - [Classification and Sort Groups](#classification-and-sort-groups-4)
    - [Requestor](#requestor)
    - [BOC](#boc)
    - [Select Vendor](#select-vendor)
    - [Vendor Information](#vendor-information-4)
  - [Notify the Control Point Clerk of Your Request](#notify-the-control-point-clerk-of-your-request)
- [HOW TO determine THE STATUS OF A REQUEST](#how-to-determine-the-status-of-a-request)
  - [Introduction](#introduction-8)
  - [Determine the Status of a Request (Request Status Report)](#determine-the-status-of-a-request-request-status-report)
    - [Select Temporary Transaction Number](#select-temporary-transaction-number)
    - [Display Transaction](#display-transaction)
    - [Status](#status)
- [OTHER ifcap FUNCTIONS](#other-ifcap-functions)
  - [Introduction](#introduction-9)
  - [Edit a Request (Section)](#edit-a-request-section)
    - [Introduction](#introduction-10)
    - [Select Transaction](#select-transaction)
    - [Classification and Sort Groups](#classification-and-sort-groups-5)
    - [Edit Line Item](#edit-line-item)
    - [Delivery Location](#delivery-location)
  - [Delete a Request (Section)](#delete-a-request-section)
    - [Introduction](#introduction-11)
    - [Select Transaction](#select-transaction-1)
    - [Delete Confirmation](#delete-confirmation)
  - [Print/Display Request Form (Section)](#printdisplay-request-form-section)
    - [Introduction](#introduction-12)
    - [Select Transaction](#select-transaction-2)
    - [Print Last Page of 2237](#print-last-page-of-2237)
    - [Interpreting the Request Form](#interpreting-the-request-form)
  - [Copy a Transaction (Section)](#copy-a-transaction-section)
    - [Introduction](#introduction-13)
    - [Menu Path](#menu-path-1)
    - [Select Transaction](#select-transaction-3)
    - [Review Request](#review-request)
    - [Setup Parameters](#setup-parameters-6)
  - [Item History](#item-history)
    - [Introduction](#introduction-14)
    - [Setup Parameters](#setup-parameters-7)
    - [Item History](#item-history-1)
  - [Edit 1358 Request (Section)](#edit-1358-request-section)
    - [Introduction](#introduction-15)
    - [Step 1](#step-1)
    - [Classification and Sort Groups](#classification-and-sort-groups-6)
    - [Review Request](#review-request-1)
- [Error Messages And THEIR Resolution](#error-messages-and-their-resolution)
- [GLOSSARY](#glossary)
- [INDEX](#index)
IFCAP stands for <u>I</u>ntegrated <u>F</u>unds Distribution, <u>C</u>ontrol Point Activity, <u>A</u>ccounting and <u>P</u>rocurement. The IFCAP design team created this manual to provide you, the IFCAP requestor, with the information necessary to create a supply or service request and check the status of your requests. IFCAP automates functions for Acquisition and Materiel Management Service (A&MM) employees and Fiscal Service employees. It also generates VA Form 90-2237, the VA request form for supplies and services. IFCAP allows all the VA employees who fund budgets, maintain budgets, order from vendors, stock items in the warehouse and pay vendors to work together and share information.
TABLE OF CONTENTS

# INTRODUCTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The Role of the Control Point Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a requestor, you will use IFCAP to create requests and track the status of your requests. Requestors are only one kind of IFCAP user. There are several others, some of whom you will contact as a user of IFCAP. This manual and other manuals, as well as IFCAP, will sometimes refer to requestors as Control Point Requestors. This is because IFCAP bills your requests under a special type of financial account called a Control Point.

## How to Use this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual explains how to perform the role of the Control Point Requestor by dividing that role into small, manageable tasks. The authors of this manual have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new Control Point Requestors to use this manual as a tutorial by following the instructions from beginning to end. Experienced Control Point Requestors can use this manual as a reference tool by using the index and table of contents.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1. All clear? Actually, all this means is that users who want to divide their reading into manageable lessons can concentrate on one section and all of its subsections. For example, section 1.3.5.4 and all of its subsections would make a coherent lesson.

## Package Management, Legal Requirements, and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use IFCAP to enter received goods and resolve shipping discrepancies, IFCAP users are given access to a set of IFCAP menu options designed for their use. Some of these menu options are additionally controlled by the use of access “keys.” These access keys are administered to individual users by the Information Resources Management Service at their facility.

As a Control Point Requestor, a Control Point Official will administer your access to IFCAP. The Control Point Official has the authority to give you access to the Control Point in order to create requests, and approve or reject the requests that you create.

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

As a requestor, you may create and edit requests assigned to a Control Point you are authorized to use. To use a Control Point, the Control Point Official for that Control Point has to give you access. If your user access is limited to the Control Point Requestor level, IFCAP will assign a temporary status to all requests that you create. This is because the Control Point Clerk and Official have to review and approve your request before they send it to Personal Property Management (2237 forms and Issue Book requests) or Accounting (1358 forms).

Different kinds of IFCAP users have different menus. If the menus in this manual include options that you do not see on your screen, do not panic! The instructions in this manual only use the options that you have as a Control Point Requestor. If you do not know what to enter at an IFCAP prompt, enter one, two or three question marks and IFCAP will list your available options or explain the prompt. The more question marks you enter at the prompt, the more information IFCAP will provide.

After you transmit a request for approval, you MUST notify the Control Point Clerk or Official.

Here are the principal IFCAP options you will use as a Control Point Requestor and their descriptions. These options will be explained in full in the following chapters.

| Options                                  | Descriptions                                                                                                                            |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Enter a Request (Section)            | Use this option to create a new request with a temporary number.                                                                        |
| Edit a Request (Section)             | Use this option to change a temporary request that you already created. Control Point Requestors can only edit temporary requests.      |
| Delete a Request (Section)           | Use this option to cancel the request and remove it from the IFCAP system. Control Point Requestors can only delete temporary requests. |
| New 1358 Request (Section)           | This option allows requestors to enter 1358 temporary requests.                                                                         |
| Edit 1358 Request (Section)          | This option allows requestors to edit 1358 temporary requests that they have entered.                                                   |
| Request Status Report (Section)      | Use this option to determine what status your request has reached.                                                                      |
| Print/Display Request Form (Section) | Use this option to print or display a request.                                                                                          |
| Copy a Transaction (Section)         | Use this option to copy a temporary request into a new temporary request, which may then be edited.                                     |
| Item History                         | This option prints/displays the history of an item in the Item file from the last five purchase orders on which the item appeared.      |

# HOW TO BECOME A REQUESTOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your ADP Coordinator will provide you with access and verify codes for access to VistA. Your Service Chief will contact the IFCAP Coordinator in Acquisition and Materiel Management for access to the menus you will need to create requests. You will also need access to a Control Point; your Service Chief will contact a Control Point Official for access to a Control Point.

# HOW TO CREATE REQUESTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To determine what type of request to make, follow the instructions in the section below. Turn to the section on the form they indicate, and create that form.

## Which Request Form Should You Use?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To choose the correct type of request form, you need to determine whether the item you want is on record in IFCAP as an item that someone has already purchased using IFCAP. If so, you are in luck, because that means that there is less information you will need to complete about the item to make your request. You determine whether there is a record for the item by consulting the Item Master File. If you are requesting a service for which an amount is set-aside over a specified time period, skip to the section on creating a 1358 order request.

## How to Consult the Item Master File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP has a file of most of the items that people at your facility have used IFCAP to purchase. This file is called the Item Master File. You need to consult this file to determine what kind of request to make. If you still do not know what vendor to select for your request after reading this section, contact the Acquisition section (Purchasing) in Acquisition and Materiel Management (A&MM).

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Item History from the Requestor’s Menu.

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: Item History

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Control Point. At the Select Item Master Number: prompt, enter the Item Master number for the item, the noun of the item, a stock number, or some other feature of the item that IFCAP can search. IFCAP will search the Item Master File for all item descriptions that have the information you enter at this prompt and ask you to choose one if there are several matches. You can also type three question marks at this prompt and read the entire item master list. If IFCAP does not find a match, you have to create either a Non-Repetitive Order or a Repetitive and Non-Repetitive Order. Skip to the sections on these two request types and create one of those requests instead.

Select CONTROL POINT: ??

Select CONTROL POINT: 60 1960 060 FISCAL SVC 0160A1 10 0100 010042100

OK? Yes// (Yes)

Select one of the following:

L Last 5 Purchase Orders

D Date Range

Select ITEM HISTORY Viewing Method: L// ast 5 Purchase Orders

Select ITEM MASTER NUMBER: ??

1 1 BANDAGE-CAST-6INX5YD

2 102-1309 2 CAP-SAFETY-BOTTLE-50S

3 111-6964 41 PETROLATUM-WHITE

4 116-1285 39 SPONGE-SURGICAL-STERILE-4X8

5 117-8741 91 AMPICILLIN

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 1 BANDAGE-CAST-6INX5YD

ITEM HISTORY

MAY 17, 2000@14:30 Site: 001 Control point: 046 SPD

Item Number: 1 Description: BANDAGE-CAST-6INX5YD

Quantity

Previously Unit of Quantity

Date Ordered PO Number Received Purchase Unit Cost Total Cost Ordered

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAY 05, 2000 001-P70096 0 EA 40.00 40.00 1

Vendor: RANDOM INTERNATIONAL

MAY 03, 2000 001-P70095 0 EA 1.00 1.00 1

Vendor: RANDOM INTERNATIONAL

Enter RETURN to continue or '^' to exit:

Would you like to look at another Item History? No// Y (Yes)

### Vendor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you select an item, IFCAP will display all the vendors for the item. Look at the VENDOR: field. Is "WAREHOUSE" one of the vendors listed for the item? If so, this means that this item is a "Posted Stock" item, or an item stocked at the warehouse for the control point. If one of the vendors is "WAREHOUSE," you have to create an Issue Book/Interval Issue Request for this item. Skip down to the section on Issue Book/Interval Issue Requests.

NUMBER: 37 SHORT DESCRIPTION: PEN

FSC: 7510 LAST VENDOR ORDERED: IFUSER,ONE

NSN: 7510-11-112-1111 MANDATORY SOURCE: SUPPLY IFVENDOR,THREE

DATE ITEM CREATED: JAN 27, 1994

BUDGET OBJECT CODE: 2660 Operating Supplies and Materials

CREATED BY: IFUSER,ONE INC: PEN

DESCRIPTION: BIC BALL POINT

VENDOR: IFVENDOR,TWO UNIT COST: 200

CONTRACT: 0501113 VENDOR STOCK \#: 12345

DATE OF UNIT PRICE: MAR 23, 1994 UNIT OF PURCHASE: BX

PACKAGING MULTIPLE: 10 UNIT CONVERSION FACTOR: 2

CONTRACT EXP. DATE (c): 03/23/95

VENDOR: IFVENDOR,THREE UNIT COST: 2.356

VENDOR STOCK \#: 444 DATE OF UNIT PRICE: JAN 27, 1994

UNIT OF PURCHASE: EA PACKAGING MULTIPLE: 1

UNIT CONVERSION FACTOR: 1 MINIMUM ORDER QTY: 1

VENDOR: IFUSER,ONE UNIT COST: 1

DATE OF UNIT PRICE: APR 13, 1994 UNIT OF PURCHASE: EA

PACKAGING MULTIPLE: 100 UNIT CONVERSION FACTOR: 100

VENDOR: IFVENDOR,SEVEN UNIT COST: 5

DATE OF UNIT PRICE: APR 5, 1994 UNIT OF PURCHASE: EA

PACKAGING MULTIPLE: 1 UNIT CONVERSION FACTOR: 1

NSN VERIFIED: JAN 27, 1994 SKU: BX

FCP: 001001

PURCHASE ORDER: 001-A40495

LONG NAME (c): SITE: 001 FCP: 001 Supply Special

FCP: 001101

PURCHASE ORDER: 001-A40467

PURCHASE ORDER: 001-A40999

LONG NAME (c): SITE: 001 FCP: 101 ISC2

FCP: 001111

PURCHASE ORDER: 001-A40482

PURCHASE ORDER: 001-A40460

PURCHASE ORDER: 001-P01235

PURCHASE ORDER: 001-A40365

LONG NAME (c): SITE: 001 FCP: 111 FMS TEST CONTROL POINT

### Order Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If IFCAP does not list "WAREHOUSE" as one of the vendors, you can create either a Repetitive order or a Repetitive and Non-Repetitive Order.

## How to Create a Repetitive (PR Card) Order Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If <u>EVERY</u> item in your request is in the Item Master File, you can create a Repetitive Order request. You can also create a Repetitive and Non-Repetitive Order request, even if you found matches for all of your items in the Item Master File.

### Setup Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Type Enter a Request (Section) at the Requestor’s Menu. Enter a Station Number, a fiscal year, and a fiscal quarter. Enter a Control Point.

Select Requestor's Menu Option: Enter a Request (Section)

Select STATION NUMBER: 001 ANYCITY,ANYSTATE

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: ???

CHOOSE FROM:

1 001 Supply Special

71 071 CANTEEN

101 101 ISC2

111 111 FMS TEST CONTROL POINT

222 222 FMS TEST CONTROL POINT

1037 1037 GENERAL POST FUND

1111 1111 FMS TEST CONTROL POINT

2222 2222 FMS TEST CON POINT

4537 4537 Supply Fund Special

7777 7777 IFVENDOR,THREE

9998 9998 FMS TEST CONTROL POINT

9999 9999 GRAND TOTAL

Select CONTROL POINT: 1

1 101 ISC2 A2222 10 0100 01AA20100

2 1037 GENERAL POST FUND 0160A1 10 1901 607001234

3 111 FMS TEST CONTROL POINT 0160A1 10 01AA 01AA60500

4 1111 FMS TEST CONTROL POINT 0160A1 10 01AA 01AA20100

CHOOSE 1-4: 1

### Create Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select Transaction: prompt, create a number for the transaction. At the Form Type: prompt, enter Repetitive (PR Card) Order.

Select TRANSACTION: SDF4312

Are you adding 'SDF4312' as a new CONTROL POINT ACTIVITY? No// Y (Yes)

The form types 1358 and NO FORM are no longer used for this option

This transaction is assigned temporary transaction number: SDF4312

FORM TYPE: ???

Choose from:

2 NON-REPETITIVE (2237) ORDER

3 REPETITIVE (PR CARD) ORDER

4 REPETITIVE AND NON-REP ORDER

5 ISSUE BOOK/INTERVAL ISSUE

FORM TYPE: 3 REPETITIVE (PR CARD) ORDER

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define.

Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Press the Enter key at the Date of Request: prompt if you want to accept the default of today's date.

> **NOTE:** The reports for Classification and Sort Group are only on the menus for the Clerk and Official.

CLASSIFICATION OF REQUEST: ???

This Classification of Request field allows you

to classify and/or categorize all transactions

(requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

This is the name used to identify the type of request. File \#410.2

is pointed to by the Classification of Request field (#8) of the

Control Point Activity file, \#410.

CLASSIFICATION OF REQUEST:

SORT GROUP: ???

This Sort Group field may be used to group together all

transactions (requests) that relate to a specific project,

work order, investigator, food group, doctor, etc.

This is the previous 'Project Number' field.

Enter one of the following:

S.EntryName to select a Sort Group

W.EntryName to select a Work Order

To see the entries in any particular file type \<Prefix.?\>

If you simply enter a name then the system will search each of

the above files for the name you have entered. If a match is

found the system will ask you if it is the entry that you desire.

However, if you know the file the entry should be in, then you can

speed processing by using the following syntax to select an entry:

\<Prefix\>.\<entry name\>

or

\<Message\>.\<entry name\>

or

\<File Name\>.\<entry name\>

Also, you do NOT need to enter the entire file name or message

to direct the look up. Using the first few characters will suffice.

SORT GROUP:

Date of REQUEST : TODAY// (May 18,2000)

### Requestor and Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter your name at the Requestor: prompt. At the Requesting Service: prompt, enter the name or the number of the service that will use the item. Enter the date required. Enter the priority of the request.

REQUESTOR: IFUSER,TWO

REQUESTING SERVICE: ???

This is the name of the service that submitted this request.

CHOOSE FROM:

A&MM 90

BLIND REHABILITATION 122

CANTEEN SERVICE 133

ENDOCRINOLOGY RESEARCH 151E

FISCAL 04

INFORMATION RESOURCE MGMT 10B/IRM

LABORATORY 113

REQUESTING SERVICE: LabORATORY 113

DATE REQUIRED: T+12 (APR 30, 1994)

PRIORITY OF REQUEST: ST// ???

This is the urgency or priority for this request.

CHOOSE FROM:

EM EMERGENCY

SP SPECIAL

ST STANDARD

PRIORITY OF REQUEST: ST// STANDARD

### Special Remarks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Special Remarks: prompt, enter any special handling information about the item, such as whether the item needs refrigeration, special handling, or if a VA employee has to go to the vendor to get the item. The Purchasing Agent can transfer these remarks to the purchase order that the vendor receives. Enter the cost center at the Cost Center: prompt if this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

SPECIAL REMARKS:

1\>These are special remarks.

2\>

EDIT Option:

COST CENTER: ??

Select the appropriate cost center for this request

ANSWER WITH COST CENTER

CHOOSE FROM:

805600 Office of Director for Operations

820111 LAB TEST CC 1

COST CENTER: 820111 LAB TEST CC 1

### Vendor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Vendor: prompt, enter the name of the vendor, or the first few letters of the name of the vendor's name. You can type three question marks (???) at the prompt to list all the vendors in the system. If you do not know which vendor has the item you want, follow the instructions in section 3.4, “How to Consult the Item Master File.” Press the Enter key at the vendor address prompts. Press the Enter key at the Line Item Number: prompt.

VENDOR ADDRESS1: 3900 BRANCH STREET//

VENDOR ADDRESS2: SUITE 200//

VENDOR ADDRESS3:

VENDOR CITY: ANYCITY//

VENDOR STATE: ANYSTATE//

VENDOR ZIP CODE: 99999//

VENDOR CONTACT: IFVENDOR,NINE//

VENDOR PHONE NO.: 999 555-5555//

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

### Item Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Repetitive (PR Card) No.: prompt, enter the number of the item you are requesting.

REPETITIVE (PR CARD) NO.: ???

ANSWER WITH ITEM MASTER NUMBER, OR SHORT DESCRIPTION, OR

VENDOR STOCK \#, OR NDC, OR NSN

DO YOU WANT THE ENTIRE ITEM MASTER LIST? y (YES)

CHOOSE FROM:

10 TEST ITEM \#10

11 ETHER U/P: 1/BT

211 METHANOL U/P: 1/BT

REPETITIVE (PR CARD) NO.: 11 ETHER U/P: 1/BT 210

### Item History and BOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Would you like to see the procurement history for this item? prompt, enter Y if you want to know the date, vendor, quantity ordered, item price or total purchase price of this item the last five times it was requested. Enter a budget object code (BOC). Budget Object Codes replace the use of sub accounts in IFCAP 5.0. Budget object codes are defined by Fiscal Service and describe what type of item or service you are requesting. Enter a quantity. This quantity represents numbers of units, so if you order one unit that has forty items per unit (say, syringes per box), then you are going to receive 40 syringes.

Would you like to see the procurement history for this item? No// Y (Yes)

ITEM HISTORY

MAY 18, 2000@14:29 Site: 001 Control point: 060 FISCAL SVC

Item Number: 14 Description: BATTERY AAA

Quantity

Previously Unit of Quantity

Date Ordered PO Number Received Purchase Unit Cost Total Cost Ordered

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NOV 09, 1999 001-P85011 0 EA 0.19 19.00 100

Vendor: RANDOM INTERNATIONAL INC

> **NOTE:** This item has a packaging multiple/unit of purchase of 12/EA

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

Answer with BOC

Do you want the entire 46-Entry BOC List? ?

BOC: 23

1 2330 Real Property Rentals

2 2341 Equipment Rental

3 2350 Motion-Picture Film Rentals

CHOOSE 1-3: 1 2330 Real Property Rentals

QUANTITY: 1

QTY BEG BAL: 1

### Delivery Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select Delivery Schedule: prompt, press the Enter key if you want all the items on your request delivered at once. If you select a delivery schedule, you are notifying the vendor that you want them to deliver different amounts of the items on different days. For example, if you want to order 100 cases of computer paper, but do not want all of it delivered at once, you can “stagger” the delivery by entering 1 at the Select Delivery Schedule: prompt. Enter a date ,the amount you would like delivered on that date and the delivery location. Enter 2 at the next Select Delivery Schedule: prompt and enter a date and the amount you would like delivered on that date and the delivery location, etc. Make sure that the total number of items among all the delivery dates and delivery locations equals the total number of items you are ordering.

At the Select Line Item Number: prompt, enter “2” if you want another item on this request. Otherwise, hit the Enter key. Enter the location you want the item to be delivered at the Deliver to/Location: prompt. At the Justification: prompt, enter your name and telephone number and information about how the item will be used. This will help the Personal Property Management (PPM) Accountable Officer and/or Purchasing Agent. The PPM Accountable Officer and/or Purchasing Agent will adjust your request to save money, solicit another vendor or purchase a similar item if there is a problem with the vendor or item you specified. Explaining how you plan to use the item will help the VA acquire the item faster and cheaper. Enter your name at the Originator of Request: prompt.

Add comments if you like. NOTE: The comments will not be seen by A&MM or FISCAL staff. Enter N at the Would You Like To Edit Another Request?: prompt to return to the Requestor's Menu.

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

DELIVER TO/LOCATION: Fiscal Office (02)

JUSTIFICATION:

1\>We're out of ether.

2\>

EDIT Option:

ORIGINATOR OF REQUEST: IFUSER,TWO

COMMENTS:

1\>

Would you like to edit another request? YES// n (NO)

## How to Create a Non-Repetitive Order Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If none of the items are in the Item Master File, you can use a Non-Repetitive Order request. You can also create a Repetitive and Non-Repetitive Order request, even if you did not find matches for any of your items on the Item Master File. This might keep A&MM staff from rejecting your request if you mistakenly listed an item as Non-Repetitive that in fact was in the Item Master File.

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Type Enter a Request (Section) at the Requestor’s Menu. Enter a Station Number, a fiscal year, and a fiscal quarter. Enter a Control Point.

Select Requestor's Menu Option: Enter a Request (Section)

Select STATION NUMBER: 001 ANYCITY,ANYSTATE

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: ???

CHOOSE FROM:

1 001 Supply Special

71 071 CANTEEN

101 101 ISC2

111 111 FMS TEST CONTROL POINT

222 222 FMS TEST CONTROL POINT

1037 1037 GENERAL POST FUND

1111 1111 FMS TEST CONTROL POINT

2222 2222 FMS TEST CON POINT

4537 4537 Supply Fund Special

7777 7777 IFVENDOR,THREE

9998 9998 FMS TEST CONTROL POINT

9999 9999 GRAND TOTAL

Select CONTROL POINT: 1

1 101 ISC2

2 1037 GENERAL POST FUND

3 111 FMS TEST CONTROL POINT

4 1111 FMS TEST CONTROL POINT

CHOOSE 1-4: 1

### Create Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select Transaction: prompt, create a number for the transaction. At the Form Type: prompt, enter Non-Repetitive Order. Assign a transaction number to this request at the Temporary Transaction Number: prompt.

> **NOTE:** Write this number down. You will need it to determine the status of your request.

Select TRANSACTION: SDF4312

Are you adding 'SDF4312' as a new CONTROL POINT ACTIVITY? No// Y (Yes)

The form types 1358 and NO FORM are no longer used for this option

This transaction is assigned temporary transaction number: SDF4312

FORM TYPE: ???

Choose from:

2 NON-REPETITIVE (2237) ORDER

3 REPETITIVE (PR CARD) ORDER

4 REPETITIVE AND NON-REP ORDER

5 ISSUE BOOK/INTERVAL ISSUE

FORM TYPE: 2 NON-REPETITIVE (2237) ORDER

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Press the Enter key at the Date of Request: prompt to select today's date. Enter your name at the Requestor: prompt. Enter the service that will use the item or service at the Requesting Service: prompt.

CLASSIFICATION OF REQUEST:

SORT GROUP:

DATE OF REQUEST: 2940418// (APR 18, 1994)

REQUESTOR: IFUSER,TWO

REQUESTING SERVICE: ???

This is the name of the service that submitted this request.

CHOOSE FROM:

A&MM 90

BLIND REHABILITATION 122

CHIEF OF STAFF 002

DENTAL 160

ENGINEERING 138

FISCAL 04

GERIATRICS AND EXTENDED CARE 180

INFORMATION SYSTEMS CENTER 162-2

LABORATORY 113

REQUESTING SERVICE: 113 LABORATORY 113

### Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date required and the priority of the request. Priorities are based on the days remaining before the delivery date requested for the item. The priority categories in IFCAP, ranging from shortest to longest delivery time remaining, are “Emergency,” “Special,” and “Standard.” Different stations assign different time durations to these categories. Check with your Fiscal or A&MM office to determine the durations at your station for these categories. At the Special Remarks: prompt, explain how the service will use the item, names of other items that would fulfill the same need, and any other information that would help the Purchasing Agent fulfill your request. Purchasing Agents sometimes change orders to fulfill the service’s need faster, find a better item or change the vendor for a better price. Explaining the use of the item will make these tasks easier to accomplish. Enter the cost center at the Cost Center: prompt if this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

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

820111 LAB TEST CC 1

COST CENTER: 805600 Office of Director for

### Vendor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Vendor: prompt, enter the name of the vendor that supplies the item you are requesting. If your vendor is not in the vendor file, IFCAP will ask you to confirm the vendor name. Enter the information for the new vendor. Enter 1 at the Line Item Number: prompt.

VENDOR: IFVENDOR,FOUR//

VENDOR ADDRESS1: 12605 GEE ST.

VENDOR ADDRESS2:

VENDOR CITY: ANYTOWN

VENDOR STATE: MD MARYLAND

VENDOR ZIP CODE: 99999-4102

VENDOR CONTACT: IFVENDOR,FIVE

VENDOR PHONE NO.: (111) 555-5555

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

### Description 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Description: prompt, define the item as thoroughly as you can. Since you are creating a non-repetitive order, the item you are requesting is not in the Item Master File. This means that the Purchasing Agent will have to make a “best guess” of exactly what kind of item you need, based on the information you provide in this field. Describe what the service plans to do with the item and any special features of the item (for example, does it have to be flexible or blue or heat-resistant or non-toxic). At the Unit of Purchase: prompt, enter the measuring standard for the item. For example, if you order one unit and select LB (pound) as unit of purchase, your request will list one pound of the item.

DESCRIPTION:

1\>Roofing Material

2\>

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

UNIT OF PURCHASE: LB POUND

> **NOTE:** Many users accidentally order too much or too little quantity by choosing the wrong unit of purchase. For example, a carboy of disinfectant is much greater than a gallon of disinfectant. Double-check the printout of your request to make sure that the quantity and the unit of purchase is correct.

### Stock Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the stock number for the item. Enter the estimated cost per unit. The cost per unit will depend on the item and how many items are in a unit. If the item is ordered at one unit per item, the cost per unit is the cost per item. If the vendor sells the item by the case, the cost per unit is the cost per case, etc. Enter a budget object code (BOC).

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

DO YOU WANT THE ENTIRE 81-ENTRY BUDGET OBJECT CODE LIST? y (YES)

CHOOSE FROM:

1081 Physicians-Full Time

1090 Administrative and Clerical Personnel Not Otherwise Classified

1091 Federal,Summer Employment Program for Youth-Summer Aids

1092 Stay-In-School Program Part-Time Employment of Needy Students

1093 Subsistence & Temp Exp, Real Estate Costs & Misc Exp-PL 89-516

1095 Employee Salary Continuation

1096 Computer Sys Analyst, Programmers, Keypunch & Computer Opr's

BOC: 1095 Employee Salary Continuation

QTY BEG BAL: 400

### Delivery Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select Delivery Schedule: prompt, press the Enter key if you want all the items on your request delivered at once. If you select a delivery schedule, you are notifying the vendor that you want them to deliver different amounts of the items on different days. For example, if you want to order 100 cases of computer paper, but do not want all of it delivered at once, you can “stagger” the delivery by entering 1 at the Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, enter 2 at the next Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, etc. Make sure that the total number of items among all the delivery dates equals the total number of items you are ordering.

Enter a 2 at the Select Line Number: prompt if you want to add another item to your request. Otherwise, press the Enter key.

Enter the estimated shipping and/or handling costs in dollars. Enter where you want the warehouse to deliver the item at the Deliver To/Location: prompt. At the Justification: prompt, explain why the service or item is needed by the service. Enter your name and telephone number. Enter your name at the Originator Of Request: prompt. Add comments if you like. Enter N at the Would You Like To Enter Another Request? prompt to return to the Requestor's Menu.

Select DELIVERY SCHEDULE: ???

This field is the Delivery Schedule of the Order file, \#442.8.

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

EST. SHIPPING AND/OR HANDLING: 40

DELIVER TO/LOCATION: Bldg.40

JUSTIFICATION:

1\>Roofing material for homeless veteran's shelter

2\>

EDIT Option:

ORIGINATOR OF REQUEST:

COMMENTS:

1\>

Would you like to enter another request? YES// n (NO)

## How to Create a Repetitive and Non-Repetitive Order Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If one or more, but not all the items on your request are on the Item Master File, you can create a Repetitive and Non-Repetitive Order Request. This is a versatile form type, because it allows other IFCAP users to "split" your request into multiple orders. Also, it is easier for Personal Property Management staff to correct a Repetitive and Non-Repetitive Order if you mistakenly list an item as non-repetitive that in fact is on the Item Master File, or if IFCAP fails to match an item to the Item Master File because you've misspelled or misnamed the item.

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a Station Number if prompted.
2.  Enter a fiscal year.
3.  Enter a fiscal quarter.
4.  Enter a Control Point.

Select Requestor's Menu Option: Enter a Request (Section)

Select STATION NUMBER: 001 ANYCITY,ANYSTATE

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: ???

CHOOSE FROM:

1 001 Supply Special

71 071 CANTEEN

101 101 ISC2

111 111 FMS TEST CONTROL POINT

222 222 FMS TEST CONTROL POINT

1037 1037 GENERAL POST FUND

1111 1111 FMS TEST CONTROL POINT

2222 2222 FMS TEST CON POINT

4537 4537 Supply Fund Special

7777 7777 IFVENDOR,THREE

9998 9998 FMS TEST CONTROL POINT

9999 9999 GRAND TOTAL

Select CONTROL POINT: 1

1 101 ISC2

2 1037 GENERAL POST FUND

3 111 FMS TEST CONTROL POINT

4 1111 FMS TEST CONTROL POINT

CHOOSE 1-4: 1

### Create Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select Transaction: prompt, create a number for the transaction. At the Form Type: prompt, enter Repetitive And Non-Rep Order. Press the Enter key at the Temporary Transaction Number: prompt.

Select TRANSACTION: SDF4312

Are you adding 'SDF4312' as a new CONTROL POINT ACTIVITY? No// Y (Yes)

The form types 1358 and NO FORM are no longer used for this option

This transaction is assigned temporary transaction number: SDF4312

FORM TYPE: ??

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

This is the previous Type of Request field.

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

REQUESTING SERVICE: ???

This is the name of the service that submitted this request.

CHOOSE FROM:

A&MM 90

AMBULATORY CARE 11C

ANESTHESIOLOGY 123

AUDIOLOGY AND SPEECH PATHOLOGY 126

REQUESTING SERVICE: 11C AMBULATORY CARE

### Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date required and the priority of the request. Priorities are based on the days remaining before the delivery date requested for the item. The priority categories in IFCAP, ranging from shortest to longest delivery time remaining, are “Emergency,” “Special,” and “Standard.” Different stations assign different time durations to these categories. Check with your Fiscal or A&MM office to determine the durations at your station for these categories. At the Special Remarks: prompt, explain how the service will use the item, names of other items that would fulfill the same need, and any other information that would help the Purchasing Agent fulfill your request. Purchasing Agents sometimes change orders to fulfill the service’s need faster, find a better item or change the vendor for a better price. Explaining the use of the item will make these tasks easier to accomplish. Enter the cost center at the Cost Center: prompt if this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

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

820111 LAB TEST CC 1

COST CENTER: 805600 Office of Director for

### Vendor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Vendor: prompt, enter the name of the vendor that supplies the item you are requesting. If your vendor is not in the vendor file, IFCAP will ask you to confirm the vendor name. Enter the information for the new vendor. Enter 1 at the Line Item Number: prompt.

VENDOR: IFVENDOR,FOUR//

VENDOR ADDRESS1: 12605 GEE ST.

VENDOR ADDRESS2:

VENDOR CITY: ANYTOWN

VENDOR STATE: MD MARYLAND

VENDOR ZIP CODE: 99999-4102

VENDOR CONTACT: IFVENDOR,FIVE

VENDOR PHONE NO.: (111) 555-5555

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

### Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Description: prompt, define the item as thoroughly as you can. If the item is not in the Item Master File, the Purchasing Agent is going to make a “best guess” of exactly what kind of item you need. This guesswork will be based on the information you provide in this field. Describe what the service plans to do with the item and any special features of the item (for example, does it have to be flexible or blue or heat-resistant or non-toxic). At the Unit of Purchase: prompt, enter the measuring standard for the item. For example, if you order one unit and select LB (pound) as unit of purchase, your request will list one pound of the item.

DESCRIPTION:

1\>Roofing Material

2\>

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

UNIT OF PURCHASE: LB POUND

> **NOTE:** Many users accidentally order too much or too little quantity by choosing the wrong unit of purchase. For example, a carboy of disinfectant is much greater than a gallon of disinfectant. Double-check the printout of your request to make sure that the quantity and the unit of purchase is correct.

### Stock Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the stock number for the item. Enter the estimated cost per unit. The cost per unit will depend on the item and how many items are in a unit. If the item is ordered at one unit per item, the cost per unit is the cost per item. If the vendor sells the item by the case, the cost per unit is the cost per case, etc. Enter a budget object code (BOC).

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

### Delivery Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select Delivery Schedule: prompt, press the Enter key if you want all the items on your request delivered at once. If you select a delivery schedule, you are notifying the vendor that you want them to deliver different amounts of the items on different days and/or different locations. For example, if you want to order 100 cases of computer paper, but do not want all of it delivered at once, you can “stagger” the delivery by entering 1 at the Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, and enter 2 at the next Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, etc. Make sure that the total number of items among all the delivery dates equals the total number of items you are ordering.

Enter a 2 at the Select Line Number: prompt if you want to add another item to your request. Otherwise, press the Enter key.

Enter the estimated shipping and/or handling costs in dollars. Enter where you want the warehouse to deliver the item at the Deliver To/Location: prompt. At the Justification: prompt, enter your name and telephone number and explain why the service or item is needed by the service. Enter your name at the Originator of Request: prompt. Add comments if you like. Enter N at the Would You Like To Enter Another Request? prompt to return to the Requestor's Menu.

Select DELIVERY SCHEDULE: ???

This field is the Delivery Schedule of the Order file, \#442.8.

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

EST. SHIPPING AND/OR HANDLING: 40

DELIVER TO/LOCATION: Bldg.40

JUSTIFICATION:

1\>Roofing material for homeless veteran's shelter

2\>

EDIT Option:

ORIGINATOR OF REQUEST:

COMMENTS:

1\>

Would you like to enter another request? YES// n (NO)

## How to Create an Issue Book/Interval Issue Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Issue Book/Interval Issue Request is for "posted stock" items, or items that the warehouse keeps in stock. You must use an Issue Book/Interval Issue request for posted stock items. You must not use an Issue Book/Interval Issue request for any items that are not posted stock. If you need some items that are posted stock and some items that are not posted stock, create an Issue Book/Interval Issue Request for the posted stock items. Use one of the other forms for the other items. The Government makes certain procurement guarantees to vendors in exchange for discounts on posted stock. Obtaining posted stock items from any source other than the warehouse is a potential violation of those guarantees. If you request a posted stock item on any request other than an Issue Book/Interval Issue request, the computer will reject your request.

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a Station Number if prompted.
1.  Enter the Fiscal Year.
2.  Enter the Fiscal Quarter.
3.  Enter the Control Point.

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: Enter a Request (Section)

Select STATION NUMBER: 001 ANYCITY,ANYSTATE

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: 101 ISC2 A2222 10 0100 01AA20100

### Create Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign a transaction number to this request at the Temporary Transaction Number: prompt.

> **NOTE:** Write this number down. You will need it to determine the status of your request.

At the Interval Issue?: prompt, enter “Y” if this is an item that you do not normally order. Enter “N” if this is an item you order on a regular basis. If you normally enter this item on an issue book order, but need the item before the next scheduled posted stock delivery, enter "Y." This prompt does NOT allow you to create a recurring order: it merely allows you to explain how you use the item.

For the transaction number, use an uppercase alpha as the first character,

and then 2-16 uppercase or numeric characters, as in ADP1.

Select TRANSACTION: TURK-182

ARE YOU ADDING 'TURK-182' AS A NEW CONTROL POINT ACTIVITY? Y (YES)

This transaction is assigned temporary transaction number: TURK-182

FORM TYPE: REPETITIVE AND NON-REP ORDER// Issue BOOK/INTERVAL ISSUE

Issue Book Requests will automatically be ordered from

SUPPLY IFVENDOR,THREE

INTERVAL ISSUE?: ???

This allows the user to specify (by entering Yes/No) whether the

request for items in the Warehouse is an Interval Issue.

i.e., Items requested between scheduled posted stock delivery, rather

than a regularly scheduled Issue Book order.

CHOOSE FROM:

1 YES

0 NO

INTERVAL ISSUE?: 1 YES

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define.

Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Press the Enter key at the Date of Request: prompt to accept the default date of today. Enter your name at the Requestor: prompt.

CLASSIFICATION OF REQUEST: ???

This Classification of Request field allows you

to classify and/or categorize all transactions

(requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

CHOOSE FROM:

TEST CLASS

CLASSIFICATION OF REQUEST:

SORT GROUP: ???

This Sort Group field may be used to group together all

transactions (requests) that relate to a specific project,

work order, investigator, food group, doctor, etc.

This is the previous 'Project Number' field.

Enter one of the following:

S.EntryName to select a Sort Group

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

DATE OF REQUEST: TODAY// (APR 18, 1994)

REQUESTOR: IFUSER,TWO

### Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Requesting Service: prompt, enter the name of the service that will use the item. Enter the date that the service will require the item. Enter the priority that you want to assign to the request. Enter any special remarks about the item that might help the Requirements Analyst fulfill your request or adjust inventory levels to accommodate the needs of your service (e.g., refrigeration required, must be picked up from vendor, etc.)

REQUESTING SERVICE: ???

This is the name of the service that submitted this request.

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

### Select Cost Center 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the cost center at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service. At the Select Line Item Number: prompt, Enter 1 for the first item on the request. Remember, you can only request issue items on an issue book request. At the Item Master File No.: prompt, enter the item name or number. You can also type three question marks (???) to see a list of the items you can request on an issue book request. Enter a budget object code (BOC).

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

REPETITIVE (PR CARD) NO.: 39 RULER U/P: 1/EA 39

> **NOTE:** This item has a minimum order quantity of 1

> **NOTE:** This item has a packaging multiple/unit of purchase of 1/EA

QUANTITY: 1

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

### Add Line Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter 2 at the Select Line Item Number: prompt if you want to add another item to your request. Otherwise, press the Enter key. Remember, you can only request issue items on an issue book request. Enter where you want the warehouse to deliver the item at the Deliver To/Location: prompt. At the Justification: prompt, enter your name and telephone number and explain why the service or item is needed. Enter your name at the Originator of Request: prompt. Add comments if you like. Enter N at the Would You Like To Enter Another Request? prompt to return to the Requestor's Menu.

Select LINE ITEM NUMBER: ???

Select DELIVERY SCHEDULE: ???

This field is the Delivery Schedule of the Order file, \#442.8.

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

EST. SHIPPING AND/OR HANDLING: 40

DELIVER TO/LOCATION: Bldg.40

JUSTIFICATION:

1\>Roofing material for homeless veteran's shelter

2\>

EDIT Option:

ORIGINATOR OF REQUEST:

COMMENTS:

1\>

Would you like to enter another request? YES// N (NO)

## How to Create a 1358 Order Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use a 1358 Order request to budget money for ongoing service expenses, such as the utility bill, copier repair, rent, or postage. A 1358 Order allows the Control Point to "obligate funds," or establish a budget for ongoing services, so there will be money to pay the vendor when the monthly or quarterly statement is due.

### Setup Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a station number if prompted.
2.  Enter a fiscal year.
3.  Enter a quarter.
4.  Enter a Control Point.
5.  Assign a transaction number to your request. Write this number down. You will need this number to determine the status of your request.

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: New 1358 Request

Select STATION NUMBER: 001 ANYCITY,ANYSTATE

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: 101

1 101 LAB TESTING 101

2 1011 BUDGET RETEST

3 1012 BUDGET RETEST

Enter a 2-16 digit number with a leading alpha, as in 'ABC123'

Select TRANSACTION: THX-1139

ARE YOU ADDING 'THX-1139' AS A NEW CONTROL POINT ACTIVITY? Y (YES)

This transaction is assigned temporary transaction number: THX-1139

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.

> **NOTE:** The Classification and Sort Group reports are found on the menus of the Official and the Clerk.

CLASSIFICATION OF REQUEST: ???

This Classification of Request field allows you

to classify and/or categorize all transactions

(requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

CHOOSE FROM:

This is the name used to identify the type of request. File \#410.2

is pointed to by the Classification of Request field (#8) of the

Control Point Activity file, \#410.

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

### Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter your name at the Requestor: prompt. Press the Enter key at the Date of Request: prompt to accept the default date of today. Enter the date that you want to commit funds to your request at the Date Committed: prompt, or press the Enter key to accept the default of the first date of the current month.

Enter the total cost in dollars for the item at the Committed (Estimated) Cost: prompt. Enter the cost center at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service.

REQUESTOR: IFUSER,TWO

DATE OF REQUEST: JUN 29,1994// (JUN 29, 1994)

DATE COMMITTED: 06/01/94// (JUN 01, 1994)

COMMITTED (ESTIMATED) COST: ???

This is the estimated amount of the committed cost of

the requested item(s).

COMMITTED (ESTIMATED) COST: 414 \$ 414.00

COST CENTER: ???

ANSWER WITH COST CENTER

CHOOSE FROM:

820100 LAB TEST CC

840200 LAB TEST BOC

COST CENTER: 800100 Office of Chief Medical

### BOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a budget object code (BOC) at the BOC1: prompt. Enter the amount of the item you want to attribute to the budget object code at the BOC1 Amount: prompt. You may also enter a Sub-control Point if you like.

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

BOC1: 2580 Miscellaneous Contractual Services by Individuals, Institu and Organi

BOC1 \$ AMOUNT: 40.00 \$ 40.00

Select SUB-CONTROL POINT:

### Select Vendor 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you if you want to enter a vendor for the request. You may or may not, depending on whether there is a single vendor or multiple vendors for the service. If there is only one vendor, enter the vendor name at the prompt. If there are multiple vendors, leave this field blank. You can assign a vendor that’s already in IFCAP, or create a new vendor for this order. Enter the contract number for the vendor.

Do you want to enter a vendor for this 1358 request? NO// Y (YES)

VENDOR: IFVENDOR,SIX 111-555-5555 NO. 7

SPECIAL FACTORS:

ORDERING ADDRESS: 4 PLAIN RD

ANYTOWN, AN 00001

OK? YES// (YES)

VENDOR CONTRACT NUMBER: ???

Select the appropriate contract number applicable to this request.

ANSWER WITH CONTRACT NUMBER

CHOOSE FROM:

D339347 -- EXP. DATE: 12-12-99

TK-987433-94 -- EXP. DATE: 01-31-98 10% 25 DAYS

VENDOR CONTRACT NUMBER: TK-987433-94 -- EXP. DATE: 01-31-98 10% 25 DAYS

### Vendor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the vendor address and contact information. At the Purpose: prompt, explain the purpose of the order, and enter your name and telephone number. Enter your name at the Originator Of Request: prompt. Add comments if you like. Enter N at the Would You Like To Enter Another Request? prompt to return to the Requestor's Menu.

VENDOR ADDRESS1: 4 PLAIN RD//

VENDOR ADDRESS2:

VENDOR CITY: AUSTIN//

VENDOR STATE: TEXAS//

VENDOR ZIP CODE: 00001//

VENDOR CONTACT: IFUSER,THREE//

VENDOR PHONE NO.: 111-555-5555//

PURPOSE:

1\>Audiovisual equipment rental

2\>

EDIT Option:

ORIGINATOR OF REQUEST: IFUSER,TWO

COMMENTS:

1\>

Would you like to enter another request? YES// n (NO)

## Notify the Control Point Clerk of Your Request 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The control point clerk will not be automatically advised that your temporary transaction is awaiting processing. The clerk will need to run the report Temporary Transaction Listing to see the temporary transactions that are awaiting action. You may wish to send the control point clerk a mail message advising them of the transaction you created if it is an emergency request.

# HOW TO determine THE STATUS OF A REQUEST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP requests pass through several stages; the processing stage, where requests are created and approved for spending, the accounting stage, where a deduction and an order are created and associated to the request, the inventory stage, where the order is filled, and the payment stage, where the funds are deducted and the vendor is paid. The IFCAP system will tell you what status your request has acquired.

## Determine the Status of a Request (Request Status Report)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Select Temporary Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You have to know the temporary transaction number to determine the status of a request. From the Requestor’s Menu, select Request Status Report (Section). At the Select Transaction Number: prompt, enter the temporary transaction number you assigned to the request when you created it in IFCAP. You may also enter the Vendor name to see a listing of transactions.

You cannot enter the PO number or permanent transaction number at the Select Transaction Number: prompt because requests can be split into multiple transactions of different types or some of your items can be rejected. IFCAP tracks the status of all the items on your request, regardless of how many transactions were created from it. Therefore, the only way to determine the status of your request AS YOU CREATED IT is to enter the temporary transaction number you created.

> **NOTE:** You can only display or print requests that you created.

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: Request Status Report (Section)

For the transaction number, use an uppercase alpha as the first character,

and then 2-16 uppercase or numeric characters, as in ADP1.

Select TRANSACTION NUMBER: THX-1138

1 THX-1138 001-94-2-101-0136 OBL IFVENDOR,SIX I40003 001-94-2-101-0134

Furry things with green hair

2 THX-1138 001-94-2-101-0134 OBL IFVENDOR,SIX

Furry things with green hair

CHOOSE 1-2: 1 001-94-2-101-0136

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Display Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the request. Look at the A&MM Status line.

Transaction Number: 001-94-2-101-0136 Transaction Type: OBLIGATION

A&MM Status: Order Not Completely Prepared

Temporary Trans. Number: THX-1138

Form Type: REPETITIVE AND NON-REP ORDER

Date of Request: MAR 28,1994 Date Required: APR 1,1994

Est. Delivery Date: Date Received:

Vendor: IFVENDOR,SIX P.O. Vendor: ANYONE'S BISCUIT BUNG

Committed (Estimated) Cost: \$94.00 Date Committed:

Obligated (Actual) Cost: \$0.00 Date Obligated:

Purchase Order/Obligation No.: I40003 Accounting Data: 3640151

FMS \$ Amount: \$0.00 FMS Date:

FMS Transaction Code:

Return to Service Comments:

Comments:

### Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Find the status on the table below. In the example above, the status is Order Not Completely Prepared. According to the table, the Purchasing Agent (node 19) has assigned a Purchase Order number to the request, but has not transmitted it to the Accounting Technician.

| Status of Request, Transaction, or Purchase Order | Description of Status                                                                                                                                                                      |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Assigned to PPM Clerk                             | PPM Clerk will create a requisition or purchase card order from a Government Vendor                                                                                                        |
| Assigned to Purchasing Agent                      | Purchase Order will be placed                                                                                                                                                              |
| Cancelled - 1358                                  | Cancelled request. Contact control point clerk or Accounting Technician for explanation.                                                                                                   |
| Cancelled Order                                   | Cancelled order. Contact control point clerk or purchaser for information.                                                                                                                 |
| Complete Order Received                           | Entire order was received.                                                                                                                                                                 |
| Complete Order Received (Amended)                 | Same as above, but the Purchaser made a change to the Purchase Order.                                                                                                                      |
| Complete Order Received But Not Obligated         | Entire order has been received by order has not been obligated. Contact Fiscal or Purchaser for information.                                                                               |
| Forward to Imprest Funds Agent                    | Purchaser will create order for payment by cash/check/draft.                                                                                                                               |
| Held for Review in Personal Prop.                 | Accountable Office is holding the 2237 for review.                                                                                                                                         |
| Held in P&C Pending Return of Quotations          | Purchasing Agent is awaiting quote(s) from Vendor(s).                                                                                                                                      |
| Issue Pending Delivery From Warehouse             | Request is being filled in the Warehouse.                                                                                                                                                  |
| Issue Request Pending Fiscal Action               | This status is not used. Currently, Fiscal Service does not process issue book orders.                                                                                                     |
| Obligated - 1358                                  | Fiscal has processed the 1358 transaction.                                                                                                                                                 |
| Obligated - Awaiting Invoice                      | Fiscal is awaiting certification of Invoice to make payment to Vendor                                                                                                                      |
| Order Not Completely Prepared                     | The Purchasing Agent has assigned a Purchase Order number to it, but has not electronically signed it yet.                                                                                 |
| Ordered (No Fiscal Action Required)               | This status means that Fiscal processing of the order is not required.                                                                                                                     |
| Ordered (No Fiscal Action) - Amended              | Order did not require action by Fiscal but the original order has been changed.                                                                                                            |
| Ordered and Obligated                             | Order has been placed with Vendor and obligated by Fiscal or Purchaser.                                                                                                                    |
| Ordered and Obligated (Amended)                   | Same as above, but the Purchaser made a change to the Purchase Order.                                                                                                                      |
| Paid (Complete Order Received)                    | A purchase card order that has been paid in full and the entire order has been received. Corrective action will be needed.                                                                 |
| Paid (Complete Order Received) - Amended          | A purchase card order that has been paid in full and the entire order has been received but the original order has been changed. Corrective action will be needed.                         |
| Paid - Not Received                               | A purchase card order that has been paid in full, but the shipment has not been received.                                                                                                  |
| Paid - Not Received - Amended                     | A purchase card order that has been paid in full, but the order has not been received and the original order has been changed.                                                             |
| Paid (Partial Receipt)                            | A purchase card order that has been paid in full and a partial shipment has been received.                                                                                                 |
| Paid (Partial Receipt) - Amended                  | A purchase card order that has been paid in full and a partial shipment has been received and the original order has been changed.                                                         |
| Partial Issue Delivered                           | Issue has been partially filled and delivered by Warehouse.                                                                                                                                |
| Partial Order Received                            | Part of the goods have been received by Warehouse or Purchaser.                                                                                                                            |
| Partial Order Received (Amended)                  | Same as above, but the Purchaser has changed the Purchase Order.                                                                                                                           |
| Partial Payment (Complete Rec)                    | A purchase card order has been partially paid ( and the entire order has been received.                                                                                                    |
| Partial Payment (Complete Rec) -Amended           | A purchase card order has been partially paid ( and the entire order has been received but the original order has been changed.                                                            |
| Partial Payment Not Received                      | A purchase card order has been partially paid but nothing has been received yet.                                                                                                           |
| Partial Payment Not Received - Amended            | A purchase card order has been partially paid but nothing has been received yet and the original order has been changed.                                                                   |
| Partial Payment (Partial Receipt)                 | A purchase card order has been partially paid and partial shipment has been received.                                                                                                      |
| Partial Payment (Partial Receipt) - Amended       | A purchase card order has been partially paid ( and partial shipment has been received. but the original order has been changed.                                                           |
| Partial Received (No Fiscal Action Req)           | Same as Partial Order Received but no fiscal action is required.                                                                                                                           |
| Partial Received But Not Obligated                | Same as Partial Order Received, but the funds have not been obligated yet.                                                                                                                 |
| Pending Accountable Officer Signature             | Request has not been signed in PPM.                                                                                                                                                        |
| Pending CP Official’s Signature                   | Request has not been signed by CP Official yet.                                                                                                                                            |
| Pending Completion by CP Clerk                    | Control Point Official has not marked the transaction as ready for approval by CP Official.                                                                                                |
| Pending Completion by Requestor                   | The Requestor has not completed the temporary request.                                                                                                                                     |
| Pending Contracting Officers Signature            | The Purchasing Agent has not electronically signed the purchase order yet.                                                                                                                 |
| Pending Fiscal Action                             | The Accounting Technician has not obligated the order or 1358, or processed the General Post Fund (GPF) transaction.                                                                       |
| Pending PPM Clerk Signature                       | The PPM Clerk has not electronically signed the requisition yet.                                                                                                                           |
| Reconciled                                        | The Purchase card order has been paid in full and the complete order has been received.                                                                                                    |
| Reconciled - Amended                              | The Purchase card order has been paid in full and completely received and the original order has been changed.                                                                             |
| Request Clarification by Service for P&C          | The Purchasing Agent is waiting for information from the CP Official or Clerk before completing the order.                                                                                 |
| Returned to Service by P&C                        | The 2237 request has been returned to the Service by the Purchasing Agent.                                                                                                                 |
| Returned to Service by Fiscal                     | The 1358 transaction or GPF transaction was returned to the Service by the Accounting Technician.                                                                                          |
| Returned to Service by PPM                        | The 2237 was returned to the Service by the PPM clerk.                                                                                                                                     |
| Returned to Supply (Pending Signature)            | The order or requisition was returned to the A&MM section by the Accounting Technician.                                                                                                    |
| Sent to Purchasing and Contracting                | The Accountable Officer has passed the 2237 to the Purchasing and Contracting section for placement of the order.                                                                          |
| Transaction Complete                              | All necessary processing has been completed on the order. (i.e. ordered, obligated, received) A 1358 or Certified Type purchase order will move to this status as soon as it is obligated. |
| Transaction Complete (Amended)                    | Same as above, but the Purchaser has changed the Purchase Order.                                                                                                                           |

# OTHER ifcap FUNCTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the options available to you in IFCAP that were not mentioned in the previous chapters. Each section of this chapter defines the purpose of the option, the menu path to reach the option in the menus, what information to enter at the prompts, and how to interpret the output that the option creates.

## Edit a Request (Section)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to change a temporary request that you already created. Control Point Requestors can only edit their own temporary requests that have not been turned into permanent transactions.

### Select Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Edit a Request (Section) from the Requestor’s Menu. Enter the temporary transaction number you assigned to your request at the Select Transaction: prompt. IFCAP will display a series of prompts that represent the categories of information about your request. If you have already entered information for a category, IFCAP will display the information you entered. If you have not entered information for the category, IFCAP will just display the category title. You can edit or add information to any of the categories that IFCAP displays during this routine, except the form type if the form type is "Repetitive," "Repetitive and Non-Repetitive," or "Issue Book.” If you want to change a request of one of these form types to another form type, you will have to delete this request and create another request from scratch. You may also enter one, two or three question marks at these prompts to read descriptions and explanations of the prompts, or read lists of acceptable responses to the prompts. If you want to go back to a prompt, type a caret (^) and the name of the prompt and IFCAP will return to that prompt. For example, if you wanted to return to the requestor prompt, type ^Requestor and IFCAP will return to the Requestor: prompt.

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: Edit a Request (Section)

For the transaction number, use an uppercase alpha as the first character,

and then 2-16 uppercase or numeric characters, as in ADP1.

Select TRANSACTION: WER1234 WER1234 OBL DEFENSE LOGISTIC AGE

FORM TYPE: REPETITIVE AND NON-REP ORDER//

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Enter a T for today’s date at the Date of Request: prompt. Enter your name at the Requestor: prompt. At the Requesting Service: prompt, enter the name or the number of the service that will use the item. Enter the date required. Enter the priority of the request. Enter any information about the item that the Purchasing Agent might need to know at the Special Remarks: prompt, such as whether the item needs refrigeration or other special handling. Enter the cost center at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service. At the Vendor: prompt, enter the name of the vendor that supplies the item you are requesting. If your vendor is not in the vendor file, IFCAP will ask you to confirm the vendor name. Enter the information for the new vendor. Enter the line item number of the item at the Select Line Item Number: prompt.

CLASSIFICATION OF REQUEST:

SORT GROUP:

DATE OF REQUEST: T (JUN 29, 1994)

REQUESTOR: IFUSER,TWO

REQUESTING SERVICE: FisCAL 04

DATE REQUIRED: JUL 20,1994// T+2 (JUL 01, 1994)

PRIORITY OF REQUEST: STANDARD// EM EMERGENCY

SPECIAL REMARKS:

1\>

COST CENTER: 802700 Surgical Service Replace

VENDOR: DEFENSE LOGISTIC AGENCY Replace

Select LINE ITEM NUMBER: 1//

### Edit Line Item 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can edit each of the items on your request by entering the line number of the item at the Select Line Item Number: prompt. Enter the item master file number of the item at the ITEM MASTER FILE NO.: prompt. You may edit the description of the item, its associated budget object code (BOC), the quantity, or the stock number. You can also edit the delivery schedule. Press the Enter key at the Select Delivery Schedule: prompt if you want all the items on your request delivered at once. If you select a delivery schedule, you are notifying the vendor that you want them to deliver different amounts of the items on different days. For example, if you want to order 100 cases of computer paper, but do not want all of it delivered at once, you can “stagger” the delivery by entering 1 at the Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date and enter 2 at the next Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, etc. Make sure that the total number of items among all the delivery dates equals the total number of items you are ordering. You may also add an item to your request by entering a new number at the Select Line Item Number: prompt.

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.:

DESCRIPTION:

1\>

BOC: 1007 Computer Systems Analyst,

QUANTITY: 1

UNIT OF PURCHASE: EA EACH

STOCK NUMBER: ???

This is the item Federal Supply Service (FSS) Number; or National Stock

Number (NSN); or any other stock number; or the manufacturer model

number.

STOCK NUMBER: BR-549

EST. ITEM (UNIT) COST: 449

QTY BEG BAL: 1

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

### Delivery Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter where you want the warehouse to deliver the item at the Deliver To/Location: prompt. At the Justification: prompt, enter your name and telephone number and explain why the service or item is needed by the service. Enter your name at the Originator Of Request: prompt. Add comments if you like. You may enter another request, or return to the Requestor’s Menu.

DELIVER TO/LOCATION: Bldg. 1

JUSTIFICATION:

1\>I need it!

2\>

3\>IFUSER,TWO, (111) 555-5555

4\>

EDIT Option:

ORIGINATOR OF REQUEST: IFUSER,TWO

COMMENTS:

1\>

Would you like to edit another request? YES// n (NO)

Select Requestor's Menu Option:

## Delete a Request (Section)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to delete the request and remove it from the IFCAP system. Control Point Requestors can delete their own requests if they have not been made into permanent transactions.

> **NOTE:** Once you delete a request from IFCAP using this option, you cannot retrieve it.

### Select Transaction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a transaction number.

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: Delete a Request (Section)

For the transaction number, use an uppercase alpha as the first character,

and then 2-16 uppercase or numeric characters, as in ADP1.

Select TRANSACTION NUMBER: ??

Please enter number using an alpha character

and 2-16 alphanumerics,as in 'A1234B'

Select TRANSACTION NUMBER: THX1138 THX1138 OBL

### Delete Confirmation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you to confirm that you want to delete the transaction, and ask you if you want to delete another transaction. If you do not want to delete another transaction, press the Enter key to return to the Requestor’s Menu.

Sure you want to delete this transaction? NO// Y (YES)

Okay It's deleted

Would you like to delete another transaction? NO// (NO)

Select Requestor's Menu Option:

## Print/Display Request Form (Section)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to print or display a request.

### Select Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the temporary transaction number you assigned to the request at the Select Transaction: prompt.

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: Print/Display Request Form (Section)

For the transaction number, use an uppercase alpha as the first character,

and then 2-16 uppercase or numeric characters, as in ADP1.

Select TRANSACTION: WER1234 WER1234 OBL DEFENSE LOGISTIC AGE

### Print Last Page of 2237

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter Yes at the Print Last Page of 2237? prompt if you want to see who has approved the request for purchase (the “Administrative Action” column) or who has certified receipt of the purchase (the “Receipt Action” column). Otherwise, enter No at this prompt.

Print last page of 2237? YES// (YES)

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Interpreting the Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The request form lists the information you provided in the Enter/Edit a Request options in a style that represents a manual VA 2237 form. The form lists each item with description and unit cost, and a total cost for the request. It also lists where the item(s) should be delivered. If you printed the last page of the 2237, the form will list signature and date columns for officers and clerks to sign at various stages of approval and receipt. Enter another transaction at the Select Transaction: number or press the Enter key to return to the Requestor’s Menu.

PRIORITY: \*\*\*EMERGENCY\*\*\*

JUN 29,1994@14:55:47 WER1234

--------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

--------------------------------------------------------------------------------

TO: A&MM Officer Requesting Office

SUPPLY (90)

----------------------- --------------------------------------------------------

Action Requested Date Prepared Date Required

Delivery JUN 29,1994 JUL 1,1994

----------------------- --------------------- ----------------------------------

ITEM NO. DESCRIPTION QUANTITY UNIT ESTIMATED

OR STOCK NO. UNIT COST

--------------------------------------------------------------------------------

BR-549 Food 1 449.0000

2 CELERY-FRESH-STALK LB 1.0000

TOTAL COST: \$449.00

--------------------------------------------------------------------------------

WER1234

--------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

--------------------------------------------------------------------------------

VENDOR INFORMATION:

VENDOR: DEFENSE LOGISTIC AGENCY CONTACT: IFVENDOR,EIGHT

123 MAIN STREET PHONE: 800-CALLME1

MYTOWN,PA 00001

--------------------------------------------------------------------------------

Ref. Voucher Number:

DELIVER TO: Bldg. 1, Office of the Bursar

--------------------------------------------------------------------------------

JUSTIFICATION OF NEED OR TURN-IN

I need it!

IFUSER,TWO, (111) 555-5555

--------------------------------------------------------------------------------

Originator of Request: IFUSER,TWO

Signature of Initiator Signature of Approving Official Date

IFUSER,TWO

------------------------------------ -------------------------------------------

WER1234

--------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

--------------------------------------------------------------------------------

Appropriation and Accounting Symbols

503-3640160.001.01-112-802700-0

--------------------------------------------------------------------------------

Select TRANSACTION:

Select Requestor's Menu Option:

## Copy a Transaction (Section)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to copy a temporary request into a new temporary request. IFCAP will allow you to edit the new temporary request.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: Copy a Transaction (Section)

### Select Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the temporary transaction name of the request you wish to copy. If you do not know the name of the transaction, enter the first few characters if you remember them, or enter three question marks to see a list of all the available transactions. Enter Y at the Would You Like To Review This Request? prompt to make sure that you have selected the right transaction. Print the last page of the 2237 if you want a copy of the 2237 for signatures.

Select transaction to be copied: WER

1 WER0123 WER0123 OBL

2 WER1234 WER1234 OBL IFVENDOR,SIX

3 WER1245 WER1245 OBL

4 WER2345 WER2345

5 WER246 WER246 OBL IFVENDOR,SIX

TYPE '^' TO STOP, OR

CHOOSE 1-5: 2 WER1234

Would you like to review this request? NO// Y (YES)

Print last page of 2237? YES// (YES)

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Review Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you decide to review the request, IFCAP will print the request, showing each item, the cost, and the vendor.

PRIORITY: \*\*\*EMERGENCY\*\*\*

OCT 7,1994@13:43:22 WER1234

--------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

--------------------------------------------------------------------------------

TO: A&MM Officer Requesting Office

FISCAL (04)

----------------------- --------------------------------------------------------

Action Requested Date Prepared Date Required

Delivery OCT 7,1994 OCT 9,1994

----------------------- --------------------- ----------------------------------

ITEM NO. DESCRIPTION QUANTITY UNIT ESTIMATED

OR STOCK NO. UNIT COST

--------------------------------------------------------------------------------

BR-549 \*\*\*NO DESCRIPTION\*\*\* 1 EA 449.0000

TOTAL COST: \$449.00

--------------------------------------------------------------------------------

VENDOR INFORMATION:

VENDOR: IFVENDOR,SIX CONTACT: IFUSER,THREE

4 PLAIN RD PHONE: 111-555-5555

ANYCITY,TX 00001

--------------------------------------------------------------------------------

Ref. Voucher Number:

If you print the last page of the 2237, you can use the printout to collect the authorizing signatures for the request.

WER1234

--------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

--------------------------------------------------------------------------------

DELIVER TO: Bldg. 1

--------------------------------------------------------------------------------

JUSTIFICATION OF NEED OR TURN-IN

I need it!

IFUSER,TWO, (111) 555-5555

--------------------------------------------------------------------------------

Originator of Request: IFUSER,TWO

Signature of Initiator Signature of Approving Official Date

IFUSER,TWO

Publications Analyst

------------------------------------ -------------------------------------------

Appropriation and Accounting Symbols

001-3650151.007-101-110100-1095 AA1118

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter the fiscal year.
2.  Enter the quarter.
3.  Enter the Control Point .
4.  Enter a new temporary transaction number. Write this number down. You will need it later to determine the status of your request.
5.  Enter the date that you require the item. IFCAP will give you one more chance to edit the transaction.
6.  Press the Enter key at the Would You Like To Edit This Entry? prompt to approve the transaction.
7.  Enter N at the Would You Like To Copy Another Request? prompt to return to the Requestor's Menu.

Select FISCAL YEAR: 95//

Select QUARTER: 1//

Select CONTROL POINT: 101 LAB TESTING 101

Please enter a new transaction in the format 'A1234'

Enter new temporary transaction number: GIT505

Transaction data is being copied.

DATE REQUIRED: OCT 9,1994//

Would you like to edit this entry? NO// (NO)

Would you like to copy another request? YES// N (NO)

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option:

## Item History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you want to use information from previous purchases to create a new purchase, you can use the Item History option to look at records of the last five purchases of the item. This is useful if you want to see how much the item cost in the past, compare vendor prices, or find a purchase order number.

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will display the available Control Points.
2.  Enter an item master number or name of the item at the Select Item Master Number: prompt.

Select Requestor's Menu Option: Item History

Select CONTROL POINT: 060 FISCAL SVC 0160A1 10 0100 010042100

Select one of the following:

L Last 5 Purchase Orders

D Date Range

Select ITEM HISTORY Viewing Method: Last 5 Purchase Orders

Select ITEM MASTER NUMBER:

### Item History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the last five purchase orders (if there are five purchase orders in the records) that included the item you selected. You may look at another Item History, or press the Enter key to return to the Requestor’s Menu.

ITEM HISTORY

Item Number: 112 Description: SYRINGES

Quantity

Previously Unit of Quantity

Date Ordered PO Number Received Purchase Unit Cost Total Cost Ordered

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

JUN 24,1994 001-A40908 EA 10.00 100.00 10

Vendor: IFVENDOR,SEVEN

JUN 10,1994 001-B40060 12 BX 12.50 187.50 15

Vendor: IFVENDOR,EIGHT

Would you like to look at another Item History? NO// (NO)

Select Requestor's Menu Option:

## Edit 1358 Request (Section)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option, like the Edit a Request (Section) option, allows you to change a temporary 1358 that you already created if it has not been turned into a permanent transaction. Control Point Requestors can only edit temporary requests.

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a transaction number. If you do not know the transaction number, enter the first few characters or three question marks at the prompt and IFCAP will list the available transactions.

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Select Requestor's Menu Option: Edit 1358 Request (Section)

Enter a 2-16 digit number with a leading alpha, as in 'ABC123'

Select TRANSACTION: WER246 WER246 OBL IF VENDOR,SIX

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.

Enter your name at the Requestor: prompt. Enter a T for today’s date at the Date of Request: prompt. Enter the date that you want to commit funds to your request at the Date Committed: prompt, or press the Enter key to accept the default of the first date of the current month. Enter the estimated cost of the request at the Committed (Estimated) Cost: prompt. Enter the cost center at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service.

Enter a budget object code (BOC) at the BOC1: prompt. Enter the amount of the item you want to attribute to the budget object code at the BOC1 Amount: prompt. Enter the name of the vendor at the Vendor: prompt. You may enter a new vendor if you like. Enter the contract number of the vendor. Enter the purpose of obtaining the item at the Purpose: prompt. Enter your name at the Originator Of Request: prompt. Enter comments if you like. You may review the request you just created.

CLASSIFICATION OF REQUEST:

SORT GROUP: ???

REQUESTOR: IFUSER,TWO//

DATE OF REQUEST: APR 19,1994// T

DATE COMMITTED: APR 1,1994//

COMMITTED (ESTIMATED) COST: 40//

COST CENTER: 800100 Office of Chief Medical Replace

BOC1: 2341 Equipment Rental Replace

BOC1 \$ AMOUNT: 40.00//

TRANSACTION BEG BAL: 40.00

VENDOR: IFVENDOR,SIX//

VENDOR CONTRACT NUMBER: TK-987433-94//

PURPOSE:

1\>Audiovisual equipment rental

EDIT Option:

ORIGINATOR OF REQUEST: IFUSER,TWO

COMMENTS:

1\>

Would you like to review this request? NO// Y (YES)

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Review Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you review the request, IFCAP will print or display the request as a form, with today's date in the header, your name, the vendor or vendors you assigned to your request, and signature blocks for approval. You may enter another request, or return to the Requestor's Menu.

MCG072611 JUL 26, 2011@13:36:14 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Originator of Request: CPUSER,ONE

Requestor: \|Date Requested: \|Obligation No.:

CPUSER,TWO \|JUL 26, 2011 \|

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

MCG072611 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

442-3610160-914-827200-2581 01AE27298 \| \|

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

# Error Messages And THEIR Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you use IFCAP to request goods and services, you will receive errors. Some errors are user errors. User errors mean that IFCAP has determined that the information you have entered in the system is either incomplete or inconsistent, and look like this:

Select TRANSACTION: 10195

Incorrect format - please re-enter number

Select TRANSACTION:

This guide and the online option descriptions should help you with these errors.

System errors occur when IFCAP fails to function properly. As with all programs, IFCAP is written in a programming language. IFCAP is written in a language called Digital Standard MUMPS. When these errors occur, IFCAP will display the error code. Record the error code and notify your ADPAC or IRM service.

RECORDING THAT AN ERROR OCCURRED ---

X2^PRCST212:1, %DSM-E-UNDEF, undefined variable PRCSTDT, -DSM-I-ECODE,

MUMPS error code: M6

Sorry 'bout that<span id="_Toc306433934" class="anchor"></span>

# GLOSSARY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary defines terms in this manual that users might find unfamiliar.
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
<td><strong>1358</strong></td>
<td>VA Form 1358, Estimated Obligation or Change in Obligation.</td>
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
<td>Appropriation Limitation Department. A set of Fiscal codes, which identifies the appropriation, used for funding.</td>
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
<td>A user that approves reconciliation’s to ensure that they are correct and complete.</td>
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
<td>Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes replaced sub accounts in IFCAP 5.0. Budget object codes are listed in VA Handbook 4671.2</td>
</tr>
<tr class="even">
<td><strong>Budget Sort Category</strong></td>
<td>Used by Fiscal Service to identify the allocation of funds throughout their facility.</td>
</tr>
<tr class="odd">
<td><strong>CCS</strong></td>
<td>The Credit Card System. This is the database in Austin that processes the credit card information from the external Credit Card Vendor system ,currently CitiDirect, and then passes information on to FMS and IFCAP.</td>
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
<td>A running record of all the transactions generated and approved for a Control Point from within IFCAP and also. effects changes to the control point that are initiated directly from within the FMS system. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.</td>
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
<td>The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidations submitted against the obligation.</td>
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
<td><strong>Freight on Board.</strong> An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means that shipping charges are due to the shipper, and must be paid when the shipper arrives at the warehouse with the item.</td>
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
<td>A Federal Agency that sells supplies and services to the VA. VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.</td>
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
<td>A unique number prefixed by an Alpha character assigned to a Purchase Order, Purchase Card Order, Delivery Order or 1358.</td>
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
<td><strong>PAID</strong></td>
<td>Paid Accounting Integrated Data. The VistA software used by stations to process timecard data to the PAID system in Austin.</td>
</tr>
<tr class="even">
<td><strong>Partial</strong></td>
<td>A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.</td>
</tr>
<tr class="odd">
<td><strong>Partial Date</strong></td>
<td>The date that a warehouse clerk created a receiving report for a shipment.</td>
</tr>
<tr class="even">
<td><strong>PAT Number</strong></td>
<td>Pending Accounting Transaction number - the primary FMS reference number. See also Obligation Number.</td>
</tr>
<tr class="odd">
<td><strong>Personal Property Management</strong></td>
<td>A section of A&amp;MM Service responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process all requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.</td>
</tr>
<tr class="even">
<td><strong>PPM</strong></td>
<td>Personal Property Management, now referred to at most sites as Acquisition and Materiel Management Service.</td>
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
<td>Report that Warehouse Clerk creates to record that the warehouse has received an item. The VA document used to indicate the quantity and dollar value of the goods being received</td>
</tr>
<tr class="even">
<td><strong>Reconciliation</strong></td>
<td>Comparing of two records to validate IFCAP Purchase Card orders. Purchase Card Users match the payment transactions(s) sent from the CCS system in Austin to an IFCAP Purchase Card Order.</td>
</tr>
<tr class="odd">
<td><strong>Reference Number</strong></td>
<td>Also known as the Transaction Number. The computer generated number that identifies a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point - 4 digit Sequence Number.</td>
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
<td>An order to a Government vendor.</td>
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
<td>See "Transfer of Disbursing Authority."</td>
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

# INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1358, 2, 4, 33, 55
2237, 2, 49, 52, 53
A&MM, 4, 14, 39
Budget Object Code, 12
Budget Object Code (BOC), 12, 19, 26, 31, 36, 46, 57
Control Point, 1, 2, 3, 5, 7, 15, 21, 27, 33, 37, 44, 47, 53, 54, 55
Control Point Clerk, 37
Control Point Official, 3
Control Point Requestor, 1, 2, 44, 47, 56
Copy a Transaction, 51
Copy a Transaction (Section), 51
Cost Center, 11, 17, 24, 31, 35, 45, 56
Date Committed, 35, 56
Delete a Request (Section), 47
Edit 1358 Request, 55
Edit 1358 Request (Section), 55
Edit a Request (Section), 44, 55
Enter a Request (Section), 7, 15
Fiscal Quarter, 27
Fiscal Year, 7, 15, 27
Item History, 4, 54, 55
Justification, 14, 20, 26, 32, 47
Purchasing Agents, 17, 24
Request Status Report (Section), 38
Requestor, 1, 2, 4, 7, 10, 14, 15, 16, 20, 23, 26, 29, 32, 35, 37, 38, 44, 45, 47, 50, 53, 55, 56, 57
Requirements Analyst, 30
Transaction Number, 15, 22, 28, 38
