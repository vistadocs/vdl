---
title: IFCAP Version 5.1 Budget Analyst User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Budget Analyst User's Guide
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
  - blockquote
  - control
  - point
  - transaction
  - budget
  - funds
  - number
  - fund
  - strong
  - distribution
page_count: 0
word_count: 39073
section_count: 11
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1budget_analyst.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1budget_analyst.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

## Table of Contents

  - [Preface](#preface)
  - [Introduction](#introduction)
    - [The Role of the Budget Analyst](#the-role-of-the-budget-analyst)
    - [How to Use This Manual](#how-to-use-this-manual)
    - [Reference Numbering System](#reference-numbering-system)
    - [The Financial Management System (FMS)](#the-financial-management-system-fms)
    - [Automatic Fund Rollover](#automatic-fund-rollover)
    - [Allowance Level Fund Transfers](#allowance-level-fund-transfers)
    - [Sub-Cost Center Change](#sub-cost-center-change)
    - [EDI –Electronic Data Interchange](#edi-electronic-data-interchange)
    - [Monthly Credit Cards Accruals](#monthly-credit-cards-accruals)
    - [Carry Forward process](#carry-forward-process)
    - [Data Structures](#data-structures)
  - [How to Create, Edit, and Fund a Control Point](#how-to-create-edit-and-fund-a-control-point)
    - [Introduction](#introduction-1)
    - [How to Add/Edit a Control Point](#how-to-addedit-a-control-point)
    - [How to Create a Budget for a Control Point](#how-to-create-a-budget-for-a-control-point)
    - [How to Release Funds to a Control Point for Spending](#how-to-release-funds-to-a-control-point-for-spending)
    - [Report on the Release of Funds to FMS](#report-on-the-release-of-funds-to-fms)
    - [How to Edit Funding Transactions](#how-to-edit-funding-transactions)
  - [Control Point Management](#control-point-management)
    - [Introduction](#introduction-2)
    - [Creating a Reserve Fund Control Point](#creating-a-reserve-fund-control-point)
    - [How to Monitor FMS Status of Funds Reports for Deficits](#how-to-monitor-fms-status-of-funds-reports-for-deficits)
    - [How to Transfer Funds Among Control Points](#how-to-transfer-funds-among-control-points)
    - [How to Freeze the Spending of a Control Point](#how-to-freeze-the-spending-of-a-control-point)
  - [Supplementary Budget Analyst Menu Options](#supplementary-budget-analyst-menu-options)
    - [Introduction](#introduction-3)
    - [Options in the Transaction Menu](#options-in-the-transaction-menu)
    - [Options on the Multiple Transaction Menu](#options-on-the-multiple-transaction-menu)
    - [Quarterly Rollover Fund Control Point Balance](#quarterly-rollover-fund-control-point-balance)
    - [Accrual (Monthly)](#accrual-monthly)
    - [Carry Forward Quarterly](#carry-forward-quarterly)
    - [Options in the Print Menu](#options-in-the-print-menu)
    - [Options in the Audit Reports Menu](#options-in-the-audit-reports-menu)
    - [Supplementary Options on the FCP/BOC/SA Management Menu](#supplementary-options-on-the-fcpbocsa-management-menu)
    - [Options in the Cost Center Management Menu](#options-in-the-cost-center-management-menu)
    - [Options in the Fund Control Point Management Menu](#options-in-the-fund-control-point-management-menu)
    - [Options on Budget Utilities Menu](#options-on-budget-utilities-menu)
    - [Supplementary Options - FMS Documents Inquiry/Error Process Menu](#supplementary-options-fms-documents-inquiryerror-process-menu)
    - [Supplementary Options in the Dictionary Management Menu](#supplementary-options-in-the-dictionary-management-menu)
    - [Options on the Dictionary List Menu](#options-on-the-dictionary-list-menu)
    - [Fund/Appropriation List](#fundappropriation-list)
    - [Fund/Appropriation Enter/Edit](#fundappropriation-enteredit)
    - [Define Standard Dictionary](#define-standard-dictionary)
    - [Fund Enter/Edit](#fund-enteredit)
    - [Required Fields Edit](#required-fields-edit)
  - [Error Messages and their Resolutions](#error-messages-and-their-resolutions)
    - [FMS Error Processing](#fms-error-processing)
    - [Stack Status Report](#stack-status-report)
    - [Funds Distribution Error Processing](#funds-distribution-error-processing)
    - [How To Correct Errors Using the Accounting Technician's Menu](#how-to-correct-errors-using-the-accounting-technicians-menu)
    - [Payment Error Processing](#payment-error-processing)
    - [GIP Module](#gip-module)
    - [Error Listing](#error-listing)
  - [eCMS/IFCAP Message Events](#ecmsifcap-message-events)
  - [Menu Outline](#menu-outline)
  - [Glossary](#glossary)
  - [Index](#index)
Integrated Funds Distribution Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Budget AnalystUser’s Guide
![](ifcap-version-5-1-budget-analyst-user-s-guide/001.png)
March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial Systems
> THIS PAGE INTENTIONALLY LEFT BLANK
Revision History
Initiated on 12/29/04
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 52%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author(s)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>March 2026</p>
</blockquote></td>
<td><blockquote>
<p>6.0</p>
</blockquote></td>
<td><blockquote>
<p>Updates based on patch PRC*5.1*257.</p>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p>
</blockquote></td>
<td><blockquote>
<p>Technical Writer,</p>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>April 2022</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td><p>Patch PRC*5.1*225 (FMBT Purchase Card Order Accrual Extract):</p>
<ul>
<li><p>Added text about the Year-to-Date Accrual Extract in section 4.5.5 Generate/Rebuild FMS SV-Document Prompts, page 4-23</p></li>
<li><p>Added dialog from YTD Accrual Data Extract in Section 4.5.5's screen display, page 4-24</p></li>
<li><p>Added "Year to Date Accrual Extract" to Transaction menu option listing on pages: 2-13, 2-16, 2-17, 2-21, 2-23, 2-24, 2-27, 3-3, 3-5, 3-7, 3-9, 4-2, 4-4, 4-5, 4-9, 4-14, 4-15, 4-17, 4-20, 4-22, 4-24, 4-25, 7-1</p></li>
</ul></td>
<td><blockquote>
<p>Developer,</p>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>January 2014</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
<td><blockquote>
<p>Patch PRC*5.1*174 (IFCAP/eCMS Interface)</p>
</blockquote>
<ul>
<li><p>Preface –added “...and run Transaction Report - eCMS/IFCAP” to the end of bullet two sentence</p></li>
<li><p>Chapter 2 – added ‘Transaction Report - eCMS/IFCAP’ to the Budget Utilities Menu in section 2.2.1</p></li>
<li><p>Chapter 4 - added ‘Transaction Report - eCMS/IFCAP’ to the Budget Utilities Menu in sections 4.9.1, 4.10, 4.11, 4.12, 4.12.2.2, 4.14, 4.15</p></li>
<li><p>Chapter 6 – replaced “Chapter 6. Menu Outline” with “Chapter 6. eCMS/IFCAP Message Events” and Menu Outline is now Chapter 7</p></li>
<li><p>Chapter 7 – added new option: Transaction Report – eCMS/IFCAP to Menu Outline</p></li>
<li><p>Glossary – added eCMS to Glossary</p></li>
</ul></td>
<td><blockquote>
<p>Project Manager, Subject Matter Expert, Technical Writer,</p>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>October 2011</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
<td><blockquote>
<p>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358.</p>
</blockquote></td>
<td><blockquote>
<p>Technical Writer,</p>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>December 29, 2004</td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>Updated to comply with SOP 192-352 Displaying Sensitive Data.</p>
</blockquote></td>
<td><blockquote>
<p>Technical Writer,</p>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td>December 29, 2004</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Pdf file checked for accessibility to readers with disabilities.</p>
</blockquote></td>
<td><blockquote>
<p>Technical Writer,</p>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the IFCAP 5.1 Budget Analyst User's Guide. IFCAP stands for Integrated Funds Distribution, Control Point Activity, Accounting and Procurement. IFCAP is a subsystem of the Veterans Health Information Systems and Technology Architecture (VistA). There are several types of IFCAP users. The Budget Analyst User's Guide explains how to use IFCAP and the Funds Distribution Program Menu to perform two primary Budget Analyst goals: creating/funding Control Points and managing budgets. The Funds Distribution Program Menu is broken down into these areas of functionality.

- TRANSACTION MENU – To allocate funds and process related transactions
- BUDGET UTILITIES – To create or edit budgetary tables and run Transaction Report - eCMS/IFCAP
- PRINT MENU – To monitor the funding activities
- FMS Document Inquiry/Error Process – To process FMS/IFCAP errors

This guide divides these goals into small, manageable tasks. Each chapter represents a summary, or overall goal. Each major chapter section represents an essential task required to achieve that goal. These sections have subsections that explain how to perform the steps required to accomplish each task. The Budget Analyst User’s Guide was written in this format so that the information hierarchy would represent the structure of IFCAP formal training and on-the-job training.

Table of Contents

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The Role of the Budget Analyst

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One of the roles of the Budget Analyst (BA) is to set up, maintain and monitor funds. It is normally the Budget Analyst’s (BA’s) responsibility to set up the accounting elements including control points, cost centers, budget object codes, as well as the FMS interface tables.

Control Points (CPs) are used to divide funds into separate accounts. FMS uses Account Classification Codes (ACC) in the same manner. CPs and ACCs are used to easily monitor available funds and obligations on a daily, monthly, quarterly or yearly basis.

Cost Centers (CCs) are used to identify costs or expenses for a section or service (Ex. 842100 or 421 Fiscal Service). Several Cost Centers can be associated with one control point. It is a one-to-many relationship between the CP and CC. Cost Centers are standardized (VHA uses 8000 series) and the list can be found at [http://vaww.va.gov/PUBL/DIREC/FINANCE/v4671_1h.htm.](http://vaww.va.gov/PUBL/DIREC/FINANCE/v4671_1h.html)

BOCs are used to classify the type of personal service, supplies or service. The standardized listing can be found at [http://vaww.va.gov/PUBL/DIREC/FINANCE/v4671_2h.html.](%20http://vaww.va.gov/PUBL/DIREC/FINANCE/v4671_2h.html.) Any combination of BOCs can be associated with CCs, unless specified. Each CP is assigned to one or more BOCs. The Budget Analyst can budget and track control point spending by type of supplies or service using the BOC.

Budget Analysts can use the above combination of accounting elements with the available reporting functionality in IFCAP to make recommendations for future CP budgeting. They can provide budgetary assistance to Control Point Officials (CPOs) and prevent the budget of their facility from becoming deficient. Deficiency occurs when a service obligates and spends more money than it was funded for, which creates a negative balance at the end of the fiscal year.

### How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual explains how to manage control points and monitor funds control with IFCAP by dividing that role into small, manageable tasks. The authors have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. New Budget Analysts can use this manual as a tutorial by following the instructions from beginning to end, while experienced Budget Analysts can utilize it as a reference tool by using the index and table of contents.

It is not intended to educate the Budget Analyst on the budgetary cycle, but to allow the Budget Analyst to use the functionality in IFCAP to manage the controls points and monitor funding levels.

### Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third section of Chapter 1. Users that want to divide their reading into manageable lessons can concentrate on one section and all of its subsections, e.g., section 2.3 and all of its subsections would make a coherent lesson.

### The Financial Management System (FMS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FMS is the primary VA financial data management system.

### Automatic Fund Rollover

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP allows users to design their Control Points to automatically transfer unspent, or residual funds from before quarters to the current quarter. This transfer of funds is called a rollover. You can configure the rollover to transfer the funds to other Control Points or to the same Control Point. IFCAP does not literally transfer the funds but includes the rollover funds as part of the spending balance of the Control Point.

### Allowance Level Fund Transfers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Budget Analysts (BAs) can now transfer funds between two CPs that belong to different programs. Previous versions of IFCAP did not allow this kind of fund transfer.

### Sub-Cost Center Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In IFCAP the last two digits of the cost center, if anything other than “00”, is the “sub-cost center” that is sent to FMS. *IFCAP does not contain a “sub-cost center” field* but sends FMS the last two digits of the cost center as the FMS “sub-cost center,” unless the last two digits of the cost center are “00”.

### EDI –Electronic Data Interchange

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP includes capabilities to electronically exchange financial documents according to established user community standards. Through the Funds Distribution Menu options, the Budget Analyst can set up the abilities to bypass Fiscal for accounting review.

### Monthly Credit Cards Accruals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functionality allows fiscal users to compile and print a monthly credit card accrual report.

### Carry Forward process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functionality exists to enable the Budget Analyst to move forward both open transactions and balances from a closing quarter to the new open quarter. This facilitates the reconciliation between the FMS sub-allowance balance and the IFCAP control point balance.

### Data Structures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Budget Files

IFCAP contains files to store VHA budget structure elements. Special Control Points are maintained uniquely by FMS. FMS also maintains fund's ceiling information. For adjustments to Control Point balances not initiated by a process in IFCAP, FMS transmits an FMS Sub allowance Reconciliation document, which automatically updates the balance of the Control Point.

To fund a Control Point, you must set up required tables, create the Control Point, link the FMS ACC with the CP, reset the accounting elements, add new ceilings (funds) for the Control Point, and release funds to the Control Point for spending. The Budget Analyst must also coordinate the FMS set-up and release funds into the Financial Management System (FMS). FMS requires some additional fields for creating a Fund Control Point, and IFCAP maintains a required fields file that lists those fields.

Setting up Account Classification Codes (ACC) in FMS is not covered in this manual. See the FMS manual for FMS set up and processing.

#### Required Fields File

IFCAP also contains a Required Fields file. This file allows the system to determine, for a given fund and FMS document type, the budget fields that FMS requires. This enables the system to prompt the user only for the fields that are appropriate for a particular transaction.

#### Dictionary Management Menu

IFCAP contains a Dictionary Management menu to help users manage the new budget files, as well as the Required Fields file.

## How to Create, Edit, and Fund a Control Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Budget Analysts create budgets for Control Points and make funds from these budgets available for spending. Some funds are earmarked for certain kinds of spending, and budgets are often made available by funding the Control Point on a fixed schedule. To allow Budget Analysts to control the "when" and "how" of Control Point spending, creating a Control Point budget is a separate activity from releasing the funds to a Control Point for spending. IFCAP is more than a budgetary and procurement system. IFCAP also provides the spending and budgetary data that allows the Department of Veterans Affairs to manage its budget on a national scale. The Budget Analyst has a crucial role in reporting the budgeting and releasing of funds to the Financial Management System (FMS) in Austin.

In the process of defining a new Fund Control Point (FCP), all “station level” questions are prompted first, followed by the FCP level questions. The station level over-commit switch overrides the control point level settings. However, the individual control point level switches for EDI override the station level settings.

IFCAP uses different required fields for different funds by using the Allowance and Sub allowance budget Required Fields file settings. For example, if the new FCP will be spending from fund 0160A1 (Med Care), there will be no requirement to prompt for Object Class.

Because of the FMS interface, Budget Analysts must take care when defining FCPs. The budget elements defined in the IFCAP FCP file point to the FMS equivalent of an IFCAP Fund Control Point.

IFCAP developers want to retain the ability to “recycle” FCP numbers from year-to-year, rather than having Budget Analysts create a new set every year. IFCAP reuses FCPs from year-to-year as much as possible. With single-year and no-year funds, recycling FCP numbers is not an issue.

It becomes an issue when dealing with multi-year funds. Currently there are only a few multi-year funds, but there may be more in the future, which may have durations exceeding 2 years. Therefore, while Budget Analysts are responsible for establishing and numbering FCPs, IFCAP developers offer the following method for numbering FCPs.

Single-Year Funds

Simply reuse the FCP number from year to year, as illustrated below. BBFY is Beginning Budget Fiscal Year, and EBFY is Ending Budget fiscal Year.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 26%" />
<col style="width: 20%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SERVICE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FCP NUMBER</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BBFY</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>EBFY</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>125</p>
</blockquote></td>
<td><blockquote>
<p>92</p>
</blockquote></td>
<td><blockquote>
<p>92</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>125</p>
</blockquote></td>
<td><blockquote>
<p>93</p>
</blockquote></td>
<td><blockquote>
<p>93</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>125</p>
</blockquote></td>
<td><blockquote>
<p>94</p>
</blockquote></td>
<td><blockquote>
<p>94</p>
</blockquote></td>
</tr>
</tbody>
</table>

No-Year Funds

FCPs spending from no-year funds should always have the same FCP number, as illustrated below.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 27%" />
<col style="width: 25%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SERVICE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FCP NUMBER</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BBFY</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>EBFY</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SUPPLY</p>
</blockquote></td>
<td><blockquote>
<p>225</p>
</blockquote></td>
<td><blockquote>
<p>xx</p>
</blockquote></td>
<td><blockquote>
<p>xx</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SUPPLY</p>
</blockquote></td>
<td><blockquote>
<p>225</p>
</blockquote></td>
<td><blockquote>
<p>xx</p>
</blockquote></td>
<td><blockquote>
<p>xx</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SUPPLY</p>
</blockquote></td>
<td><blockquote>
<p>225</p>
</blockquote></td>
<td><blockquote>
<p>xx</p>
</blockquote></td>
<td><blockquote>
<p>xx</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 30%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ISC</p>
</blockquote></th>
<th><blockquote>
<p>103</p>
</blockquote></th>
<th><blockquote>
<p>01504B</p>
</blockquote></th>
<th><blockquote>
<p>92</p>
</blockquote></th>
<th><blockquote>
<p>95</p>
</blockquote></th>
<th><blockquote>
<p>92, 93, 94, 95</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>104</p>
</blockquote></td>
<td><blockquote>
<p>01504B</p>
</blockquote></td>
<td><blockquote>
<p>93</p>
</blockquote></td>
<td><blockquote>
<p>96</p>
</blockquote></td>
<td><blockquote>
<p>93, 94, 95, 96</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>101</p>
</blockquote></td>
<td><blockquote>
<p>01504B</p>
</blockquote></td>
<td><blockquote>
<p>94</p>
</blockquote></td>
<td><blockquote>
<p>97</p>
</blockquote></td>
<td><blockquote>
<p>94, 95, 96, 97</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>102</p>
</blockquote></td>
<td><blockquote>
<p>01504B</p>
</blockquote></td>
<td><blockquote>
<p>95</p>
</blockquote></td>
<td><blockquote>
<p>98</p>
</blockquote></td>
<td><blockquote>
<p>95, 96, 97, 98</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>103</p>
</blockquote></td>
<td><blockquote>
<p>01504B</p>
</blockquote></td>
<td><blockquote>
<p>96</p>
</blockquote></td>
<td><blockquote>
<p>99</p>
</blockquote></td>
<td><blockquote>
<p>96, 97, 98, 99</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>104</p>
</blockquote></td>
<td><blockquote>
<p>01504B</p>
</blockquote></td>
<td><blockquote>
<p>97</p>
</blockquote></td>
<td><blockquote>
<p>00</p>
</blockquote></td>
<td><blockquote>
<p>97, 98, 99, 00</p>
</blockquote></td>
</tr>
</tbody>
</table>

To help FCP users determine the correct FCP to enter on requests when dealing with multi-year funds, enter the valid years for using an FCP in the description field when establishing the FCP. For example, in the description field for FCP \#101 above, enter a description, including something to the effect that the FCP is valid in FYs 90, 94, 95 and 96. FCP \#102’s description would indicate that it is valid in FYs 91, 95, 96 and 97.

Multi-Year Funds

For multi-year funds, reuse the FCP number, but only after the duration of the fund has ended. When the initial four-year period is up, VACO may renew the fund for PERIOD, at which time the Budget Analyst would reuse the old FCP numbers for the fund. This process is illustrated below.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SERVICE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FCP NUMBER</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FUND</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BBFY</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>EBFY</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FY</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>101</p>
</blockquote></td>
<td><blockquote>
<p>01504B</p>
</blockquote></td>
<td><blockquote>
<p>90</p>
</blockquote></td>
<td><blockquote>
<p>93</p>
</blockquote></td>
<td><blockquote>
<p>90, 91, 92, 93</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>102</p>
</blockquote></td>
<td><blockquote>
<p>01504B</p>
</blockquote></td>
<td><blockquote>
<p>91</p>
</blockquote></td>
<td><blockquote>
<p>94</p>
</blockquote></td>
<td><blockquote>
<p>91, 92, 93, 94</p>
</blockquote></td>
</tr>
</tbody>
</table>

### How to Add/Edit a Control Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Navigation

From the Funds Distribution and Accounting Menu, select the following menu options in this order:

Funds Distribution Program Menu Budget Utilities Menu FCP/CC/BOC Management Menu

Fund Control Point Management Menu Add/Edit Control Point

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Budget Utilities Menu

Edit Budget Categories

FMS Exception Transaction Report

Repost FMS Exceptions

Clear FMS Exception File Entries

Clear Program Lock

Dictionary Management Menu...

Display Control Point Official's Balance

FCP/CC/BOC Management Menu...

Recalculate All Fund Control Point Balances

Transaction Report - eCMS/IFCAP

Select Budget Utilities Menu Option: FCP/CC/BOC Management Menu

BOC Management Menu...

Cost Center Management Menu...

Fund Control Point Management Menu...

Select FCP/CC/BOC Management Menu Option: Fund Control Point Management Menu

Add/Edit Control Point

Deactivate a Fund Control Point

Reactivate a Fund Control Point

Place Released Ceiling Transaction in CP File

Display Control Point Committed Transactions

Reset FCP Yearly Accounting Element & ACT Code

#### Station Level Setup

The initial setting up of a control point begins with a few prompts regarding the station level setup. The Budget Analyst may manage the funds for more than one station. The prompt defaults to the primary station setup in the IFCAP Coordinator’s Site Parameter File (PRIMARY STATION:// YES). Enter the station number that is related to the control point that needs to be set up or edited.

Select STATION NUMBER ('^' TO EXIT): 662// 688 WASHINGTON, DC

...OK? Yes// (Yes)

Enter the name of the person(s) responsible for releasing funds to the control point. Adding the user at this prompt does not control adding, editing or funding a control point, but only provides the ability to approve the release of funds to the control point. The release of funds is one of the steps in funding a control point.

> Select FUND RELEASING OFFICIAL: IFUSER1, A// IFUSER1, B ANALYST

The Station Over Commit Switch: prompt allows the Budget Analyst to determine the station level override authority for control point overspending. Normally, a control point must have adequate funds to approve spending transactions. If the control point wants to continue to approve spending transactions without additional funds, the control point must have “over commit” authority. The Budget Analyst may use this switch to override the CP OVERCOMMIT SWITCH: (See Section 2.2.3 Control Point Level Setup).

1.  OVERCOMMIT NOT ALLOWED FOR ALL FCP'S - Will not allow any control point to over commit funds, even if the CP OVERCOMMIT SWITCH is set to OVERCOMMIT ALLOWED in the control point level setup.
2.  CURRENT QUARTER OVERCOMMIT ALLOWED – Allows over commit authority for all control points in the current Fiscal Year and quarter. This is helpful at the beginning of a quarter, before any funds are distributed.
3.  FUTURE QUARTERS OVERCOMMIT ALLOWED – Allows over commit authority for all control points in the current Fiscal Year, future quarter. This is helpful at the end of quarter, when the control points want to start spending in the next quarter, and before the Budget Analyst has an opportunity to fund the upcoming quarter.
4.  CURRENT AND FUTURE QUARTERS OVERCOMMIT ALLOWED – Allows over commit authority for all control points for the current Fiscal Year -current and future quarters.
5.  INDIVIDUAL CP SWITCH USED – Allows the Budget Analyst to determine the over commit authority at the control point level CP OVERCOMMIT SWITCH.
6.  OVERCOMMIT ALLOWED – Allows over commit authority for all control points. Again, if the CP OVERCOMMIT SWITH is set to OVERCOMMIT NOT ALLOWED, using this switch will override the control point level. Use caution when using this option, it will allow all the control points to continue spending current, prior and future years and quarters without restrictions until further control is placed.

STATION OVERCOMMIT SWITCH: OVERCOMMIT ALLOWED// ?

Choose from:

0 OVERCOMMIT NOT ALLOWED FOR ALL FCP'S

1 CURRENT QUARTER OVERCOMMIT ALLOWED

2 FUTURE QUARTERS OVERCOMMIT ALLOWED

3 CURRENT AND FUTURE QUARTERS OVERCOMMIT ALLOWED

4 INDIVIDUAL CP SWITCH USED

5 OVERCOMMIT ALLOWED

The EDI Order Release: prompt is not required. It handles the flow of EDI (Electronic Document Interchange) through the Fiscal process. The CP level switch EDI AUTO RELEASE: can override this station level switch. (See Section 2.2.3 Control Point Level Setup).

Y YES – EDI orders are sent immediately to vendors without a review from Fiscal Service.

N NO or Blank – Fiscal review of orders is required before EDI orders are sent. These orders will have a status of Pending Fiscal Action, prior to Fiscal review.

EDI ORDER RELEASE: ?

Choose from:

Y YES

N NO

The Site All/Delivery Order Switch: prompt is not required. It handles which EDI (Electronic Document Interchange) documents flow through the Fiscal process. The CP level switch EDI AUTO RELEASE: can override this station level switch. (See Section 2.2.3 Control Point Level Setup).

SITE ALL/DELIVERY ORDER SWITCH: ALL ORDERS// ?

Choose from:

Y YES

N NO

The Station Rollover of EOQ Bal.: prompt handles the rollover of funds from one quarter into the next.

1.  ALL FCPs CAN SPEND PRIOR FUNDS – Choosing this option will not allow the ‘rollover’ of funds at the end of the quarter.
2.  INDIVIDUAL FCP ROLLOVER EOQ BALANCE IN EFFECT – This option will allow the ‘rollover’ of funds at the end of the quarter. The individual control point can be set to determine where the funds will be placed at the end of the quarter. This will allow the excess funds to be transferred into the next quarter or into another control point.

STATION ROLLOVER OF EOQ BAL.: ?

Choose from:

2 ALL FCPS CAN SPEND PRIOR FUND

3 INDIVIDUAL FCP ROLLOVER EOQ BALANCE IN EFFECTS

#### Control Point Level Setup

To add a new control point, begin with the 3 or 4 numeric identifiers, followed by a blank space and then enter the name of the control point at the Select Fund Control Point: prompt. This will add the new entry into the control point file. To edit a control point, just enter the control point number and press return. The Control Point Name will be displayed on the next line to confirm the spelling and format. Press “return” to accept the control point name but consider the format, all CAPS or the first letter only in CAPS. Example: 025 Radiology or 025 RADIOLOGY. For formatting purposes, you may want to enter all the control point names with similar formats.

> Select Fund Control Point:?

> Enter a new CONTROL POINT NAME, if you wish. Enter a 3 or 4-digit number, a space and the name of the control point. Answer must be 3 to 30 characters in length.

> Select Fund Control Point: 025 Radiology

> Are you adding ‘025 Radiology’ as a new CONTROL POINT NAME? No//

Enter the service that controls the funds of the Control Point. The controlling service must already exist in the Service/Section file.

> CONTROLLING SERVICE: RADIOLOGY// ?

Answer with SERVICE/SECTION NAME, or ABBREVIATION, or MAIL SYMBOL, or TYPE OF SERVICE, or MIS COSTING CODE

The FUND, ADMINISTRATIVE OFFICE, PROGRAM and FCP/PRJ fields store FMS elements, which must exist and be active in File Dictionaries before they are available for selection in this menu.

See section 4.4.7 – Supplementary Options in the Dictionary Management Menu – Dictionary Management Menu to add or update the FMS elements. Enter the FUND code The FUND code is the allowance element that identifies the appropriation used for the funding. Enter the beginning year of the fund at the Beginning Budget Fiscal Year: prompt. Enter the administrative office that provided the appropriation at the Administrative Office: prompt (almost always, this will be 10 (Veterans Health Administration)). Enter the code for the program that this fund supports (for example, All Other 0100) at the Program: prompt. Enter the FMS ACC (Account Classification Code) for this Fund Control Point.

> FUND: 0160A1//

> BEGINNING BUDGET FISCAL YEAR: 2000//

> ADMINISTRATIVE OFFICE: 10//

> PROGRAM: 0100//

> FCP/PRJ: 010022200//

The Automated?: prompt allows you to decide whether to activate the Control Point to transmit requests through IFCAP and FMS processing, and to have IFCAP update the Control Point records automatically. Enter “N” if you are creating a Control Point but do not want to activate it for use yet. If you do not want to activate the Control Point now, you can activate it later by using the Reactivate Control Point option.

> AUTOMATED: YES

Enter “Y” at the Allow Access by All Requestors: prompt if you want all Control Point Users to have at least “Requestor” access to the Control Point. Entering No will not allow all control point users to have access to this control point. Individual access and the level of access will be assigned in the next step: Select CONTROL POINT USER.

> ALLOW ACCESS BY ALL REQUESTORS: YES//

Enter the Control Point User’s name and press enter.

> Select CONTROL POINT USER: IFUSER1, THREE IUT

Enter the user's level of access. Users can be a Control Point Requestor, Control Point Clerk, or Control Point Official.

> LEVEL OF ACCESS: CONTROL POINT OFFICIAL// ?

> 1--CONTROL POINT OFFICIAL (Has authority to approve requests)

> 2--CONTROL POINT CLERK (Can enter permanent transactions)

> 3--REQUESTOR (Can initiate temporary requests to Control Point Clerk)

> Choose from:

> 1 CONTROL POINT OFFICIAL

> 2 CONTROL POINT CLERK

> 3 REQUESTOR

The Receive FMS Reconciliation: prompt is used to indicate which users will receive electronic mail messages whenever transactions in FMS affect the balance in their Fund Control Points.

Users with a Y in this field will receive the messages. If no user has a "y" value in this field, the messages will go to all Control Point Officials for that Fund Control Point.

RECEIVE FMS RECONCILIATION:

The Notification Designee prompt allows Control Point User to receive informational bulletins containing details of a ceiling transaction distributing funds to this Fund Control Point. NOTIFICATION DESIGNEE:

Enter another Control Point User to add additional users, or press the Enter key, if you have finished entering Control Point Users.

> Select CONTROL POINT USER:

At the Special Control Point: prompt, enter whether this Control Point is a General Post Fund, a Supply Fund, a Construction fund, or a Canteen fund. If not, leave this field blank.

> SPECIAL CONTROL POINT:

Enter the cost center at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service. The Cost Center must already exist and be “active” before it can be selected at this prompt. See section 4.4 Supplementary Options in the Budget Utilities Menu.

> Select COST CENTER:

Enter a description for the Control Point. You may use this field to input special notes. Notes regarding the reason for this Control Point, or any special circumstances regarding the funding may be helpful for future reference.

> DESCRIPTION:

> Edit? NO//YES

At the CP Over commit Switch: prompt, enter whether the Control Point is allowed to over commit funds. See section 2.2.2 Station Level Setup for further explanation of these options. These options are set for the control point level only and do not affect any other control point. The Control Point Level switch OVERRIDES the Station Level Switch.

STATION OVERCOMMIT SWITCH: OVERCOMMIT ALLOWED// ?

Choose from:

0 OVERCOMMIT NOT ALLOWED FOR ALL FCP'S

1 CURRENT QUARTER OVERCOMMIT ALLOWED

2 FUTURE QUARTERS OVERCOMMIT ALLOWED

3 CURRENT AND FUTURE QUARTERS OVERCOMMIT ALLOWED

4 INDIVIDUAL CP SWITCH USED

5 OVERCOMMIT ALLOWED

The EDI Order Release: prompt handles the flow of EDI (Electronic Document Interchange) through the Fiscal process. See section 2.2.2 Station Level Setup, for further explanation of these options.

Yes - Allows the release of EDI orders to vendors without fiscal review. No - Will send EDI orders through Fiscal for an accounting review.

EDI ORDER RELEASE: ?

Choose from:

Y YES

N NO

This Control Point Level prompt overrides the Station Level prompt. It determines which documents will not flow through the Fiscal process, either All Orders or just the Delivery Orders.

FCP ALL/DELIVERY ORDER SWITCH: ??

This is used to release orders directly without fiscal review.

Choose from:

A ALL ORDERS

D DELIVERY ORDERS ONLY

The Rollover of EOQ Balance prompt determines how to handle the remaining End of Quarter funding balance.

1.  Transfer funds to another FCP allows fund to be transferred into another FCP, like a “Reserve” FCP. Note: IFCAP will prompt for the other FCP.
2.  Spend Available Prior Funds allows the control point to access funds from a prior quarter that have not yet been carried forward.
3.  Restrict to Current Quarter allows the control point to spend funds in the current quarter only.

ROLLOVER OF EOQ BALANCE: ?

This is the rollover of the EOQ balance.

Choose from:

1 TRANSFER FUNDS TO ANOTHER FCP

2 SPEND AVAILABLE PRIOR FUNDS

3 RESTRICT TO CURRENT QUARTER (DEFAULT)

Enter another Fund Control Point at the Select Fund Control Point: prompt or press the Enter key to return to the Fund Control Point Management Menu.

### How to Create a Budget for a Control Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Navigation

From the Funds Distribution & Accounting Menu, select Funds Distribution Program Menu. From the Funds Distribution Program Menu, select Transaction Menu.

From the Transaction Menu, select Add New Transaction (Ceiling).

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Add New Transaction (Ceiling)

#### Transaction (Ceiling) Setup

Select a Station Number and a fiscal year. Record the transaction number that IFCAP assigns to the transaction. Approve the transaction number. Enter the Control Point number at the Control Point: prompt. Enter the TDA, or “Transfer of Disbursement Authority” number at the TDA Number: prompt. This number can be found on the AACS report from Austin. Enter the date of the TDA at the TDA Date: prompt. At the Recurring FTEE: prompt, enter the Full Time Employee Equivalent (FTEE) that you are appropriating into this CP from your budget. At the Non-Recur FTEE: prompt, enter the Full Time Employee Equivalent (FTEE) that you're appropriating into this CP from another budget. “Non-Recurring” means the funding is a one- time expense for a specific program, project, trip, purchase, etc. “Recurring” does not create a recurring appropriation: it merely describes the source of funds. This categorization allows IFCAP users to monitor expenses from different sources of funds. At the FTEE: prompt, enter the training FTEE that you are appropriating into this CP from your budget. If this Control Point is for medical care appropriation items, enter the appropriate Sort Category at the Budget Sort Category: prompt. Otherwise, press the Enter key. If you do not know the name or number of the category, enter three question marks at the prompt and IFCAP will list the available categories. Enter the transaction date, normally “T” for today, at the Transaction Date: prompt. Enter the amount of money you want to appropriate to the CP for each quarter. IFCAP will compute and display the total funding for the fiscal year.

*<u>NOTE:</u>* You can also use this option to withdraw funds from a Control Point by entering a minus sign before the dollar amount prompts.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 95//

I am going to create a new transaction with the number 688-95-0002

IS THIS OK ? YES// (YES)

CONTROL POINT: 101 LAB TESTING 101

...OK? Yes// (Yes)

TDA NUMBER: 4510

TDA DATE: 091994 (SEP 19, 1994)

RECURRING FTEE: 4 NON-RECUR FTEE: 0 TRNG FTEE: 0

BUDGET SORT CATEGORY:

TRANSACTION DATE: T (OCT 03, 1994)

1ST QTR: 45 \$ 45.00

2ND QTR: 45 \$ 45.00

3RD QTR: 60 \$ 60.00

4TH QTR: 45 \$ 45.00

TOTAL FUNDING= \$ 195.00

#### Recurring/Non-Recurring Funding Setup

At the Recurring/Non-Recurring: prompt, enter R if the funding for the Control Point is from your budget or NR if the funding is from another budget. “Non-Recurring” means the funding is a one-time expense for a specific program, project, trip, purchase, etc. “Recurring” does not create a recurring appropriation: it merely describes the source of funds. This categorization allows IFCAP users to monitor expenses from different sources of funds. Enter the station number at the Select Station Number: prompt to enter another transaction or enter a caret (^) to return to the Transaction Menu.

> RECURRING/NON-RECURRING: NON-RECURRING// NR NON-RECURRING

> DESCRIPTION:

> 1\>Graphics/Displays/Presentations Expenses

> 2\>

> EDIT Option: Select STATION NUMBER ('^' TO EXIT): 688// ^

> Add New Transaction (Ceiling)

> Release Transaction

> Monthly Budget Distribution

> Generate FMS Budget Documents

> Accrual (Monthly) Carry Forward Quarterly

> Enter FCP Adjustment Data

> Multiple Transaction Menu ...

> Quarterly Rollover Fund Control Point Balance

> Year to Date Accrual Extract

> Select Transaction Menu Option:

### How to Release Funds to a Control Point for Spending

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

This option creates a printout of the transaction numbers of each ceiling you create for a Control Point. After you create this printout, IFCAP sends a message to the Control Point Official that funds have been released to the Control Point.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Transaction Menu from the Funds Distribution Program Menu.

Select Release Transaction from the Transaction Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu ...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Release Transaction

#### Select Transaction

Enter the Station number, fiscal year and your electronic signature code. You may review a transaction if you like. Enter the sequence number of the transaction you wish to release. If you do not know the sequence number of the transaction, type three question marks at the Enter Sequence Number of Transaction(s) to be Released: prompt and IFCAP will list the available transactions.

> Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

> Select FISCAL YEAR ('^' to EXIT): 94//

> Enter ELECTRONIC SIGNATURE CODE: Thank you.

> Do you wish to review/edit any transactions? NO//

> Enter Sequence Number of Transaction(s) to be Released: ???

> Enter the Sequence Number or indicate a range of sequence numbers by separating the first and last numbers with a dash (-).

> Type "ALL" to release all unreleased transactions.

> Do you wish to see the list of all unreleased transactions? NO// YES

> Unreleased Sequence Numbers for Station 688, FY: 94

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEQ #</p>
<p>TOTAL</p></th>
<th>TRANS #</th>
<th>CP#</th>
<th>TOTAL</th>
<th>SEQ #</th>
<th>TRANS #</th>
<th>CP#</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>54</p>
<blockquote>
<p>$0.00</p>
</blockquote></td>
<td>688-94-0054</td>
<td>CP-19</td>
<td>$5.00</td>
<td>70</td>
<td>688-94-0070</td>
<td>CP-0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>71</p>
</blockquote>
<p>$-100.00</p></td>
<td>688-94-0071</td>
<td>CP-0</td>
<td>$0.00</td>
<td>76</td>
<td>688-94-0076</td>
<td>CP-201</td>
</tr>
<tr class="odd">
<td><p>77</p>
<p>$60000.00</p></td>
<td>688-94-0077</td>
<td>CP-202</td>
<td>$100.00</td>
<td>80</td>
<td>688-94-0080</td>
<td>CP-5101</td>
</tr>
<tr class="even">
<td><p>81</p>
<p>$10000000.00</p></td>
<td>688-94-0081</td>
<td>CP-5101</td>
<td>$23000000.00</td>
<td>82</td>
<td>688-94-0082</td>
<td>CP-5101</td>
</tr>
<tr class="odd">
<td><p>83</p>
<p>$123456.00</p></td>
<td>688-94-0083</td>
<td>CP-5102</td>
<td>$10533827.00</td>
<td>84</td>
<td>688-94-0084</td>
<td>CP-5102</td>
</tr>
<tr class="even">
<td><p>94</p>
<p>$30000.00</p></td>
<td>688-94-0094</td>
<td>CP-335</td>
<td>$96.00</td>
<td>95</td>
<td>688-94-0095</td>
<td>CP-5103</td>
</tr>
<tr class="odd">
<td><p>96</p>
<p>$0.00</p></td>
<td>688-94-0096</td>
<td>CP-101</td>
<td>$1101.00</td>
<td>97</td>
<td>688-94-0097</td>
<td>CP-0</td>
</tr>
<tr class="even">
<td><p>98</p>
<p>$100.00</p></td>
<td>688-94-0098</td>
<td>CP-101</td>
<td>$-100.00</td>
<td>99</td>
<td>688-94-0099</td>
<td>CP-105</td>
</tr>
<tr class="odd">
<td><p>100</p>
<p>$20.00</p></td>
<td>688-94-0100</td>
<td>CP-101</td>
<td>$-20.00</td>
<td>101</td>
<td>688-94-0101</td>
<td>CP-335</td>
</tr>
</tbody>
</table>

#### Remove Transaction

You may enter multiple sequence numbers if you like. If you decide not to release one of the transactions after you’ve already entered a long list of transactions, enter the last four digits of the transaction number and IFCAP will remove the transaction from the list. Enter a printer name at Device: prompt. You cannot enter LAT at this prompt.

> Enter Sequence Number of Transaction(s) to be Released: 96 OK

> Enter Sequence Number of Transaction(s) to be Released:

> To not release a transaction already selected to be released

> Enter the last 4 digits of the transaction for FY 94:

> QUEUE TO PRINT ON

> DEVICE: LAT \[YOU CAN NOT SELECT A VIRTUAL TERMINAL\]

> Previously, you had selected queueing.

> Do you STILL want your output QUEUED? YES//

> DEVICE: LAT

> You cannot select your home device.

> QUEUE TO PRINT ON

> DEVICE: LASERDP DEVELOPMENT

> \<Request Queued\>

#### Interpreting the Report

IFCAP will print a report on each transaction you released and list the funds released for that transaction for each fiscal quarter.

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="4">Trans #: 688-94-0096 FCP: 101 LAB TESTING QTR:</th>
<th>1ST</th>
<th><blockquote>
<p>AMT:</p>
</blockquote></th>
<th>333.00</th>
<th><blockquote>
<p>Released.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>2ND</th>
<th><blockquote>
<p>AMT:</p>
</blockquote></th>
<th>112.00</th>
<th><blockquote>
<p>Released.</p>
</blockquote></th>
</tr>
<tr class="header">
<th>3RD</th>
<th><blockquote>
<p>AMT:</p>
</blockquote></th>
<th>333.00</th>
<th><blockquote>
<p>Released.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>4TH</th>
<th><blockquote>
<p>AMT:</p>
</blockquote></th>
<th>333.00</th>
<th><blockquote>
<p>Released.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Report on the Release of Funds to FMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Use the Generate FMS Budget Documents option to notify FMS of funds released to each Control Point. IFCAP transmits the FMS documents automatically.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Transaction Menu from the Funds Distribution Program Menu.

Select Generate FMS Budget Documents from the Transaction Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Generate FMS Budget Documents

#### Select Transaction Date

Enter a station number, fiscal year and fiscal quarter. Press the Enter key at the Ok To Continue?: prompt. At the FMS Transaction Date: prompt, enter the date that you want the transaction to occur.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 95//

Select FISCAL QUARTER: 1//

This option will now create FMS documents for 1st Quarter, FY 95

released transactions which have not previously been coded.

FMS Transaction Date: OCT 3, 1994// (OCT 3, 1994)

Accounting Period (MM/YY): OCT 1994// (OCT 1994)

Ready to generate FMS documents? YES//

DEVICE: LAT Right Margin: 80//

#### Compile/Print Report

A hard copy printout of the transaction numbers released will print. Specify a Control Point for the distribution of funds. You must specify amounts for each quarter. You must also enter the various types of FTEE (Full Time Employee Equivalent) authorized by the TDA. This option only enters information from the TDA into the system for your internal use. You may edit or delete this information. A new transaction will need to be initiated to withdraw funds. After printing the report, IFCAP will return to the Transaction Menu.

FUND DISTRIBUTION STATISTICS OCT 03, 1994, 15:52

PAGE 1

TRANSACTION TRANSACTION

NUMBER CONTROL POINT DATE 1ST QTR

---------------------------------------------------------------------------------

688-00-0001 060 FISCAL SVC OCT 03,1994 10000.00

688-00-0002 060 FISCAL SVC DEC 22,1994 1000000.00

--------- ---------

SUBTOTAL

1010000.00

688-00-0003 076 BIO-MED EQUIPMENT DEC 22,1994 1000000.00

--------- ---------

SUBTOTAL

1000000.00

--------- ---------

TOTAL

2010000.00

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option:

### How to Edit Funding Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

You can edit any transactions that you have not released.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Transaction Menu from the Funds Distribution Program Menu.

Select Edit Existing, Unreleased Transaction from the Transaction Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Edit Existing, Unreleased Transaction

#### Select Transaction

Enter a station number and a fiscal year. At the Select Sequence Number for FY: prompt, enter the number of the transaction you want to edit.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

Select Sequence Number for FY 94: ???

Choose from:

0054 019 SPD

0070

0071

0080 5101 KATEY TEST

0081 5101 KATEY TEST

0082 5101 KATEY TEST

0083 5102 KATEY TESTING

0084 5102 KATEY TESTING

0086 5101 KATEY TEST

0089 101 LAB TESTING 101

Select Sequence Number for FY 94: 0089 101 LAB TESTING 101

#### Edit Transaction

You may change the Control Point, the TDA number, the record of the date on the TDA, and the Full Time Employee Equivalent (FTEE) associated with the transaction.

> CONTROL POINT: 101 LAB TESTING 101//

> TDA NUMBER: ???

> This is the Transfer of Disbursing Authority (TDA) 1-to-3-digit number from

> the ACCS report.

> TDA NUMBER: 460

> TDA DATE: ??

> Examples of Valid Dates:

> JAN 20, 1957, or 20 JAN 57 or 1/20/57 or 012057

> T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

> T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

> If the year is omitted, the computer uses the CURRENT YEAR. Two-digit year

> assumes no more than 20 years in the future, or 80 years in the past.

> TDA DATE: T (JUN 03, 1994)

> RECURRING FTEE: ??

> This is the number of recurring Full Time Employee Equivalent (FTEE).

> RECURRING FTEE: 120

> NON-RECUR FTEE: 10

> TRNG FTEE: 100

#### Edit Additional Parameters

Assign or change the budget sort category, if you like. You can also change the funding for the transaction for each quarter, and whether the funding comes from recurring or non-recurring funds. Specifying “recurring” at the Recurring/Non-Recurring: prompt does not create a recurring transaction: it only identifies the source of funds. You can enter another transaction to edit at the Select Next Sequence Number for FY: prompt or press the Enter key to return to the Transaction Menu.

BUDGET SORT CATEGORY: ??

This is the category for RD285 report for medical

care appropriation items only.

CHOOSE FROM:

1 ALL OTHER

2 RECURRING PERSONAL SERVICES

3 NR ALL OTHER

4 NR .23

5 19 REPL EQUIP

6 20 ADDITION EQUIPMENT

7 25 OUTREACH-OTHER R & NR

8 25 OUTR-OTH R&NR (FEE CP 853)

11 25B OUTREACH-PS R&NR

12 26 TRAINING

BUDGET SORT CATEGORY: 12 26 TRAINING

TRANSACTION DATE: MAY 27,1994//

1ST QTR: 10//

2ND QTR: 20//

3RD QTR: 30//

4TH QTR: 40//

TOTAL FUNDING= \$ 100.00

RECURRING/NON-RECURRING: NON-RECURRING//

DESCRIPTION:

1\>Training program

2\>

EDIT Option:

Select Next Sequence Number for FY 94:

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option:

## Control Point Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Budget Analysts prevent the facility they budget from becoming deficient and reconcile predicted spending with actual spending.

Deficiency is the overcommitment of an entire budget for a station. This happens when you allow Control Points to overcommit too many funds, so that the overall expenses are more than your overall budget. Deficient budgets are defined by the Anti-Deficiency Act. One way you can guard against deficiency is to prohibit nonessential Control Points from over committing.

You can also create a reserve Fund Control Point. As a final measure, you can solicit the Regional Budget Analyst for emergency funding.

The primary tools that Budget Analysts use to prevent deficiency are FMS Status of Funds Reports (which replace 826 reports) and Control Point fund transfers. FMS Status of Funds Reports (which replace 826 reports) provide Control Point balances, which Budget Analysts monitor to prevent budget deficits. If a Control Point budget is threatened with a deficit, the Budget Analyst can transfer funds to it from another Control Point or halt further purchases.

When a Control Point sets aside (or "commits") funds for a purchase, the amount of money they commit is often an estimate. Before the purchase is made, the accounting staff “obligates,” or withholds, money from the Control Point and earmarks it for the purchase. IFCAP updates the Control Point records of committed and obligated funds in the running balance records. Control Point users rely on the Budget Analyst, because the Budget Analyst funds a Control Point.

### Creating a Reserve Fund Control Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One way you can guard against deficiency is to create a reserve Fund Control Point. Control Point funding levels are defined by your budget plan and are set by your Fiscal Officer or Medical Center Director, so you will need to plan ahead if you want to incorporate a reserve Fund Control Point into your budget. You can also use the rollover switch in IFCAP to rollover the money that your Control Points do not spend into this Control Point and save it for unanticipated spending. Create a Control Point, and name it Contingency or Reserve. Make sure that the funds roll over into the reserve Control Point.

### How to Monitor FMS Status of Funds Reports for Deficits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FMS Status of Sub-allowances Report will list the balances and deficits (if any) for the Control Points.

### How to Transfer Funds Among Control Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

You can transfer funds among Control Points if the Control Points receive their money from the same fund and the funds are for the same quarter.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Transaction Menu from the Funds Distribution Program Menu.

Select Transfer From/To Control Point from the Transaction Menu.

Accounting Technician Menu ...

Funds Distribution Program Menu ...

Payment/Invoice Tracking Menu ...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu ...

Budget Utilities Menu ...

Print Menu ...

FMS Documents Inquiry/Error Process ...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Transfer From/To Control Point

#### Transfer Funds Setup

Enter a station number and fiscal year. Enter the Control Point from which you want to withdraw the funds at the Transfer from Control Point: prompt. Enter the Control Point into which you want to deposit the funds. Enter the fiscal quarter and the amount to transfer. Enter the date at which you want IFCAP to make the transaction. At the Recurring/Non-Recurring: prompt, enter R if the funding for the CP is from your budget or NR if the funding is from another budget. Non-Recurring means the funding is a one-time expense for a specific program, project, trip, or purchase. Recurring does not create a recurring appropriation: it merely describes the source of funds. This categorization allows IFCAP users to monitor expenses from different sources of funds. Enter a description of the transfer if you like. You may review a summary of the transaction if you like.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

...Hmmm, Let me think about this for a moment...

TRANSFER FROM CONTROL POINT: 105 LAB TESTING 105

...OK? Yes// (Yes)

TRANSFER TO CONTROL POINT: 108 LAB TESTING 108

...OK? Yes// (Yes)

FOR WHICH QUARTER: 4

AMOUNT TO TRANSFER: 10 \$ 10.00

TRANSACTION DATE: OCT 3,1994// (OCT 03, 1994)

RECURRING/NON-RECURRING: NON-RECURRING

DESCRIPTION:

1\>User fee

2\>

EDIT Option:

Do you want to review this entry? YES// (YES)

Transfer Transaction Summary

To Control Point: 108 LAB TESTING 108

From Control Point: 105 LAB TESTING 105

Transaction Date: OCT 3,1994

Quarter: 4th

Amount to be Transferred: \$ 10.00

R/NR: NON-RECURRING

Annualization: \$ 0.00

Description: User fee

#### Edit Transfer Funds

You may edit the information you just entered. If the information on the transaction is correct, post the transaction. IFCAP actually creates two transactions: the first one for withdrawal and the second one for the deposit. IFCAP will list these two transaction numbers. Answer “N” at the Make Another Transfer?: prompt to return to the Transaction Menu.

> Do you want to edit this entry? NO// (NO)

> Are you ready to post this transaction? YES// (YES)

> ...Hmmm, let me think about this for a moment...

> Finished. The following transactions have been created

> in file 421 (Funds distribution):

> 688-94-0141

> 688-94-0142

> Make another transfer? YES// N (NO)

> Add New Transaction (Ceiling)

> Edit Existing, Unreleased Transaction

> Delete Unreleased Transaction

> Transfer From/To Control Point

> Release Transaction

> Monthly Budget Distribution

> Generate FMS Budget Documents

> Accrual (Monthly)

> Carry Forward Quarterly

> Enter FCP Adjustment Data

> Multiple Transaction Menu...

> Quarterly Rollover Fund Control Point Balance

> Year to Date Accrual Extract

> Select Transaction Menu Option:

### How to Freeze the Spending of a Control Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

If a Control Point is threatened with a deficit, the Budget Analyst can notify the Control Point Clerk to reconcile the Control Point. As a last resort, further purchases can be "frozen" by returning purchases back to the Control Point. If the Control Point is not set to over commit, Fiscal personnel should decide if Accounting or Budget personnel should monitor the Control Point transactions to control the deficit.

#### How to Return a Purchase to the Control Point

To return a purchase to the Control Point, tell the Accounting Technician or Purchasing Agent to return the Purchase Order by using the “Return PO to Supply” option under the Document Processing Menu. The Purchasing Agent may also return the 2237 to the service.

#### Request Additional Funds from VISN CFO

#### Procedure

Request additional funds only to prevent deficiency due to additional expenses you feel the Medical Center should not absorb. Be prepared to justify the funds as recovery for unexpected and previously unfunded obligations. Contact the VISN CFO and explain why your facility needs additional funds. If approved, the CFO will initiate a Transfer of Dispersing Authority (TDA), transferring funds to your budget.

#### Enter the TDA Funds into Your Budget

Assign the funds from the TDA into the over committed Control Points and adjust the IFCAP records accordingly. Go to the section in this user guide on how to fund Control Points.

#### Record the Distribution of the TDA Funds

You may use the Monthly Budget Distribution option in IFCAP to record non-cumulative monthly distribution of Transfer of Disbursing Authority (TDA) funds.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Transaction Menu from the Funds Distribution Program Menu.

Select Monthly Budget Distribution from the Transaction Menu.

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

FMS Documents Inquiry

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu ...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Monthly Budget Distribution

#### Select TDA Number

Enter a station number and a fiscal year. Enter the TDA number.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

Select TDA NUMBER FOR STATION 688, FY 94: ???

CHOOSE FROM:

1 5101 KATEY TEST

1 5102 KATEY TESTING

1 101 LAB TESTING 101

432 102 LAB TESTING 102

460 101 LAB TESTING 101

5269 5102 KATEY TESTING

Select TDA NUMBER FOR STATION 688, FY 94: 1

1 1 688-94-0081 5101 KATEY TEST

2 1 688-94-0084 5102 KATEY TESTING

3 1 688-94-0092 101 LAB TESTING 101

CHOOSE 1-3: 3 688-94-0092

#### Distribute TDA Funds

IFCAP will prompt you to distribute this TDA among the twelve months of the fiscal year. You can enter another TDA to edit at the Select TDA Number for Station: prompt or press the Enter key to return to the Transaction Menu.

TDA IS DISTRIBUTED AS FOLLOWS:

1ST QTR 2ND QTR 3RD QTR 4TH QTR

1000000 0 0 0

ENTER THE NON-CUMULATIVE DISTRIBUTION FOR THIS TDA

OCT NON-CUM: 500000// 0

NOV NON-CUM: 0//

DEC NON-CUM: 500000// 0

JAN NON-CUM: 0//

FEB NON-CUM: 0//

MAR NON-CUM: 0//

APR NON-CUM: 0// 100000

MAY NON-CUM: 0// 900000

JUN NON-CUM: 0// 0

JUL NON-CUM: 0//

AUG NON-CUM: 0//

SEP NON-CUM: 0//

DISTRIBUTION IS CORRECT BY QUARTER

Select TDA NUMBER FOR STATION 688, FY 94:

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

FMS Documents Inquiry

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu ...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option:

## Supplementary Budget Analyst Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the IFCAP options available to Budget Analysts that have not been mentioned previously in this manual. You may not have all of the menus defined here.

Your local IRM service controls the assignment of IFCAP menus to users.

### Options in the Transaction Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Delete Unreleased Transaction

You can delete a transaction if a Control Point User has not released it to Fiscal Service for processing.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Transaction Menu from the Funds Distribution Program Menu.

Select Delete Unreleased Transaction from the Transaction Menu.

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

FMS Documents Inquiry

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Delete Unreleased Transaction

#### Select Transaction

Enter a station number and a fiscal year. Enter the transaction number you want to delete at the Select Sequence Number for FY: prompt. IFCAP will prompt you to confirm that you want to delete the transaction. IFCAP will delete the transaction and allow you to delete another transaction or return to the Transaction Menu.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

Select Sequence Number for FY 94: ???

CHOOSE FROM:

0054 019 SPD

0070

0071

0076 201 LAB TESTING 201

0077 202 LAB TESTING 202

0080 5101 KATEY TEST

0081 5101 KATEY TEST

0082 5101 KATEY TEST

0083 5102 KATEY TESTING

0084 5102 KATEY TESTING

0086 5101 KATEY TEST

0087 103 LAB TESTING 103

0088 101 LAB TESTING 101

0089 101 LAB TESTING 101

0090 103 LAB TESTING 103

0091 101 LAB TESTING 101

0093 101 LAB TESTING 101

Select Sequence Number for FY 94: 0086 688-94-0086 5101 KATEY TEST

ARE YOU SURE YOU WANT TO DELETE THIS TRANSACTION? NO// Y (YES)

Transaction Deleted.

Do you wish to delete another transaction for 688-94? n (NO)

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data (FISCAL)

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option:

### Options on the Multiple Transaction Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Create/Post Multiple Transaction

#### Introduction

Use this option when you need to make several adjustments to a single Control Point or multiple Control Points. The system will assign a temporary transaction number that is used to keep track of the transaction if, for some reason, you do not proceed to post it to the Control Points and want to edit it later with the Post/Edit option.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu Select Transaction Menu from the Funds Distribution Program Menu.

Select Multiple Transaction Menu from the Transaction Menu.

Select Create/Post Multiple Transaction from the Multiple Transaction Menu.

> Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

> Transaction Menu...

> Budget Utilities Menu...

> Print Menu...

> Select Funds Distribution Program Menu Option: Transaction Menu

> Add New Transaction (Ceiling)

> Edit Existing, Unreleased Transaction

> Delete Unreleased Transaction

> Transfer From/To Control Point

> Release Transaction

> Monthly Budget Distribution

> Generate FMS Budget Documents

> FMS Documents Inquiry

> Accrual (Monthly)

> Carry Forward Quarterly Enter FCP Adjustment Data

> Multiple Transaction Menu...

> Quarterly Rollover Fund Control Point Balance

> Year to Date Accrual Extract

> Select Transaction Menu Option: Multiple Transaction Menu

> Create/Post Multiple Transaction

> Post/Edit Temporary Transaction

> Select Multiple Transaction Menu Option: Create/Post Multiple Transaction

#### Create Multiple Transaction

Enter a station number and a fiscal year. Record the transaction number that IFCAP assigns to the transaction. Enter the date that the transaction should occur at the Transaction Date: prompt. Enter a Control Point.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

This has been assigned TRANSACTION NUMBER: T-00012.

Please note and use for editing of this transaction.

TRANSACTION DATE: JUN 8,1994// (JUN 08, 1994)

Select CONTROL POINT: 101 LAB TESTING 101

...OK? Yes// (Yes)

Are you adding '101 LAB TESTING' as a new CONTROL POINT (the 1st for this MULTIPLE DISTRIBUTION)? N// Y (Yes)

#### Fund Control Point

IFCAP will ask you how much money you want to fund the Control Point for each fiscal quarter. IFCAP will ask you whether the funding comes from recurring or non-recurring funds. Specifying “recurring” at the Recurring/Non-Recurring: prompt does not create a recurring transaction, but identifies the source of funds, instead. If you want to provide funding to another Control Point, enter it at the Select Control Point: prompt. Enter a description of the transaction.

> 1ST QTR: 333 \$ 333.00

> 2ND QTR: 112 \$ 112.00

> 3RD QTR: 123 \$ 123.00

> 4TH QTR: 533 \$ 533.00

> TOTAL FUNDING= \$ 1101.00

> RECURRING/NON-RECURRING: NON-RECURRING//

> Select CONTROL POINT:

> DESCRIPTION:

> 1\>This is a multiple transaction for a widget.

> 2\>

> EDIT Option:

> Do you want to review this transaction? YES// (YES)

> DEVICE: LAT RIGHT MARGIN: 80//

#### Review of Multiple Transaction

IFCAP will create the multiple-distribution listing, which includes the transaction number, the Control Point, and the amount of the transaction for each fiscal quarter. If you post the transaction, IFCAP will transfer the transaction to the funds distribution file for processing and delete the temporary transaction number from its records. You can then edit another transaction or return to the Multiple Transaction Menu. You may also use the Release Transaction option to release the transaction you just posted.

MULTIPLE DISTRIBUTION LISTING JUN 8,1994 11:25 PAGE 1

TRANSACTION

NUMBER DESCRIPTION

CONTROL

POINT R/NR

ANNUALIZATION

1ST QTR 2ND QTR 3RD QTR

4TH QTR AMOUNT

-------------------------------------------------------------------------------------

T-00012 This is a multiple transaction for a widget.

101 NR 333.00 112.00 123.00

533.00

--------------------------------------------------------------------------------------

TOTAL 333.00 112.00 123.00

533.00

Are you ready to post this transaction? YES// (YES)

101 LAB TESTING Filed with transaction number 688-00-0023

\<Transfer to Funds Distribution File Completed.\>

\<Temporary Transaction Number T-00012 has been Deleted.\>

Enter another transaction? NO// (NO)

Create/Post Multiple Transaction

Post/Edit Temporary Transaction

Select Multiple Transaction Menu Option:

#### Post/Edit Temporary Transaction

#### Introduction

Use this option to edit existing temporary transactions and post them to the Funds distribution file for release.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Transaction Menu from the Funds Distribution Program Menu.

Select Multiple Transaction Menu from the Transaction Menu.

Select Post/Edit Temporary Transaction from the Multiple Transaction Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

FMS Documents Inquiry

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu ...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Multiple Transaction Menu

Create/Post Multiple Transaction

Post/Edit Temporary Transaction

Select Multiple Transaction Menu Option: Post/Edit Temporary Transaction

#### Select/Edit Temporary Transaction

Enter a station number and a fiscal year. Enter the number of the temporary transaction you want to post and/or edit. Enter three question marks (???) at the Select TEMPORARY TRANSACTION NUMBER: to see the list of available temporary transactions. You may edit the Control Point and the funding of the transaction before you post it.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

Select TEMPORARY TRANSACTION NUMBER: ???

CHOOSE FROM:

4 T-00004

5 T-00005

6 T-00006

7 T-00007

8 T-00008

9 T-00009

10 T-00010

11 T-00011

Select TEMPORARY TRANSACTION NUMBER: 10 T-00010

...OK? Yes// (Yes)

Do you want to edit this transaction? NO// Y (YES)

TRANSACTION DATE: APR 1,1994//

Select CONTROL POINT: 071 CANTEEN//

CONTROL POINT: 071 CANTEEN//

1ST QTR: 400 \$ 400.00

2ND QTR: 950 \$ 950.00

3RD QTR: 200 \$ 200.00

4TH QTR: 450 \$ 450.00

TOTAL FUNDING= \$ 2000.00

#### Review a Transaction

IFCAP will ask you whether the funding comes from recurring or non-recurring funds. Specifying “recurring” at the RECURRING/NON-RECURRING: prompt does not create a recurring transaction: it just identifies a feature of the source of funds. If you want to provide funding to another Control Point, enter it at the Select Control Point: prompt. Enter a description of the transaction. You may review the transaction if you like.

RECURRING/NON-RECURRING: NON-RECURRING//

Select CONTROL POINT:

DESCRIPTION:

1\>Promotional expenses for canteen

2\>

EDIT Option:

Do you want to review this transaction? YES// (YES)

DEVICE: LAT RIGHT MARGIN: 80//

MULTIPLE DISTRIBUTION LISTING JUN 8,1994 14:16 PAGE 1

TRANSACTION

NUMBER DESCRIPTION

CONTROL

POINT R/NR

ANNUALIZATION

1ST QTR 2ND QTR 3RD QTR

4TH QTR AMOUNT

--------------------------------------------------------------------------------------

T-00010 Promotional expenses for canteen

071 NR 400.00 950.00 200.00

450.00

--------------------------------------------------------------------------------------

TOTAL 400.00 950.00 200.00

450.00

#### Post Transaction

If you post the transaction, IFCAP will transfer the transaction to the funds distribution file for processing and delete its temporary transaction number from its records. You can then edit another transaction or return to the Multiple Transaction Menu. You can also use the Release Transaction Option to release the transaction you just posted.

Are you ready to post this transaction? YES// (YES)

101 LAB TESTING Filed with transaction number 688-00-0024

\<Transfer to Funds Distribution File Completed.\>

\<Temporary Transaction Number T-00012 has been Deleted.\>

Enter another transaction? NO// (NO)

Create/Post Multiple Transaction

Post/Edit Temporary Transaction

Select Multiple Transaction Menu Option:

### Quarterly Rollover Fund Control Point Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

This report allows you to determine the amount of rollover funds for the quarter, the Control Points from which the rollover came, and the Control Points that received the rollover funds.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu.

Select Transaction Menu from the Funds Distribution Program Menu.

Select Quarterly Rollover Fund Control Point Balance from the Transaction Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Quarterly Rollover Fund Control Point Balance

#### Select Single or Multiple Year Appropriation

Enter a station number, a fiscal year and a fiscal quarter. You may see the Control Points funded by single-year appropriations or multi-year appropriations, but not both. IFCAP will list each rollover by the Control Points from which the rollover came, the Control Points that received the rollover funds, and the amount of the rollover. Enter a caret (^) at the Select Station Number: prompt to return to the Transaction Menu.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

Select FISCAL QUARTER: 4// 3

Select one of the following:

1 Single Year Appropriation Fund Control Points

2 Multiple Year Appropriation Fund Control Points

Select Number: : 1 Single Year Appropriation Fund Control Points

Description:

DEVICE: LAT

IFCAP Rollover Fund Control Point Balance List Printed on 10/05/1994

For Budget Fiscal Year: 1994 Quarter: 3

Roll 097 TRANSFER WITH PGM to 112 SURGICAL SERVICE \$200307.55

Roll 101 LAB TESTING 101 to 033 337 Basil Pharmacy Test \$1521205.53

Finished. The following transactions have been created

in file 421 (Fund Distribution):

688-00-0025

688-00-0026

Select STATION NUMBER ('^' TO EXIT): 688// ^

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option:

### Accrual (Monthly)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will create an accrual report for IFCAP purchase card orders.

#### Configuring the Accrual (Monthly) Option to Run Automatically

The Accrual (Monthly) option must be scheduled to run at 1:00AM on the first day of each month. Use the 'Schedule/Unschedule Options' option in the Taskman Management Menu to select to enter the following values at these prompts:

QUEUED TO RUN AT WHAT TIME: DEC 1,1996@01:00

RESCHEDULING FREQUENCY: 1M (1@01:00)

TASK PARAMETERS: 999

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu.

Select Transaction Menu from the Funds Distribution Program Menu. Select Accrual (Monthly) from the Transaction Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option: Accrual (Monthly)

#### Compile/Print Monthly Accrual Prompts

1.  Enter a station number. If your site has multiple stations, enter a question mark at the prompt to see a list of available stations for your site.
2.  Enter the month and year for the accrual you want to compile. IFCAP will display the same month expressed as a fiscal month and year.
3.  At the Select Number: prompt, enter 1. If data for the month you selected has already been compiled, IFCAP will display the last date and time that data for this month was compiled. IFCAP will warn you that if you recompile this data, you will overwrite all edits made to the accrual.
4.  Enter “Y” at the Recompile Accrual Report?: prompt.
5.  Enter “Y” at the Ready to Print?: prompt.
6.  Enter an output device. IFCAP will compile the accrual data and send the IFCAP Accrual Report to the output device you selected.
7.  Enter another month and year at the For Accrual Month/Year: prompt or enter a caret (^) to return to the Transaction Menu.

Select STATION NUMBER ('^' TO EXIT): 612// 688 WASHINGTON, DC

For Accrual Month/Year: 11/96// Fiscal Month/Year: 02/1997

Select one of the following:

1 Compile/Print Monthly Accrual

2 Edit Monthly Accrual Amount

3 Generate/Rebuild FMS SV-Document

Select Number: 1 Compile/Print Monthly Accrual

Ready to Compile/Print? NO// YES DEVICE: LAT

Compiling...

IFCAP Accrual Report for 11/1996 Printed on 11/15/1996

Station: 688

FUND/BBFY/AO/ACC/CC/BOC UNPAID PO UNRECON

ACCRUAL

0110/1997///840100/1092 7.50

1.  7.50

SUBTOTAL 7.50

1.  7.50

0160A1/1997/10/0100201C3/800100/2510 138.00 0.00

138.00

0160A1/1997/10/0100201C3/800100/2660 41.00 0.00

41.00

0160A1/1997/10/0100201C3/810800/2511 13.00 0.00

13.00

0160A1/1997/10/0100201C3/810800/2580 63.90 0.00

63.90

0160A1/1997/10/0100201C3/810800/2660 570.00 0.00

570.00

SUBTOTAL 825.90

0.0 825.90

0160A1/1997/10/010050100/850100/2220 22.00 0.00

22.00

SUBTOTAL 22.00

0.00 22.00

0160A1/1997/10/894/824300/2510 318.00

0.00 318.00

SUBTOTAL 318.00 0.00

318.00

0160A7/1997/10/012/810800/2510 44.00

0.00 44.00

SUBTOTAL 44.00

0.00 44.00

4537B/1994/90/010044100/600000/2697 200.00 0.00

200.00

4537B/1994/90/010044100/600000/2698 100.00 0.00

100.00

SUBTOTAL 300.00 0.00

300.00

TOTAL 1517.40

0.00 1517.40

Accrual amount followed by '\*' means edited amount.

Report ends, enter 'RETURN' to continue.:

For Accrual Month/Year: 11/96// ^

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option:

#### Edit Monthly Accrual Amount Prompts

Enter a station number. If your site has multiple stations, enter a question mark at the prompt to see a list of available stations for your site.

Enter the month and year for the accrual you want to compile. IFCAP will display the same month expressed as a fiscal month and year.

At the Select Number: prompt, enter 2. Enter “Y” at the Ready to Edit?: prompt.

Select a fund code. If you do not know the entire fund code, enter the first few digits of the number and IFCAP will generate a list of available fund codes. If you do not know the number at all, enter two question marks and IFCAP will list the available fund codes. IFCAP will display the accrual account, the unpaid purchase card order amount, the unreconciled amount, and the calculated accrual amount.

Enter the new amount at the Edited Accrual Amount: prompt.

Enter another fund code at the Select Fund Code: prompt or press the Enter key.

Enter another month and year at the For Accrual Month/Year: prompt or enter a caret (^) to return to the Transaction Menu.

Select STATION NUMBER ('^' TO EXIT): 612// 688 WASHINGTON, DC

For Accrual Month/Year: 11/96// Fiscal Month/Year: 02/1997

Select one of the following:

1 Compile/Print Monthly Accrual

2 Edit Monthly Accrual Amount

3 Generate/Rebuild FMS SV-Document

Select Number: 2 Edit Monthly Accrual Amount

Ready to Edit? NO// YES

--------------------------------------------------------------------------------------

Select Fund Code or FCP/PRJ (ACC) Code: 01 1

1 0110/1997///840100/1092

2 0160A1/1997/10/0100201C3/800100/2510

3 0160A1/1997/10/0100201C3/800100/2660

4 0160A1/1997/10/0100201C3/810800/2511

5 0160A1/1997/10/0100201C3/810800/2580

TYPE '^' TO STOP, OR

CHOOSE 1-5: 3

Accrual Account: 0160A1/1997/10/0100201C3/800100/2660

Unpaid P.C.O Amount: 41.00 Unreconciled Amount: 0.00

Calculated Accrual Amount: 41.00

EDITED ACCRUAL AMOUNT: 42.50

COST CENTER: 800100 Plant Operations//

BOC: 2660 Operating Supplies and Materials//

--------------------------------------------------------------------------------------

Select Fund Code or FCP/PRJ (ACC) Code:

For Accrual Month/Year: 11/96// ^

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option:

#### Generate/Rebuild FMS SV-Document Prompts

Enter a station number. If your site has multiple stations, enter a question mark at the prompt to see a list of available stations for your site.

Enter the month and year for the accrual you want to compile. IFCAP will display the same month expressed as a fiscal month and year.

At the Select Number: prompt, enter 3.

Enter “Y” at the Ready to Generate/Rebuild Document?: prompt. IFCAP will generate a monthly accrual FMS SV document for the month you selected.

Enter another month and year at the For Accrual Month/Year: prompt or enter a caret (^) to return to the Transaction Menu.

After the SVs for FMS are generated, the Purchase Card Order Year to Date Accrual extract is generated. This extract’s data is sent to the Financial Services Center (FSC) to support data needs of the iFAMS implementation. This extract generation can also be triggered by execution of the separate menu option Year to Date Accrual Extract \[PRCB YTD ACCRUAL EXTRACT\] on the Transaction menu.

Select STATION NUMBER ('^' TO EXIT): 999// 999 ANYWHERE,ANYPLACE

For Accrual Month/Year: 11/96// Fiscal Month/Year: 02/1997

Select one of the following:

1 Compile/Print Monthly Accrual

2 Edit Monthly Accrual Amount

3 Generate/Rebuild FMS SV-Document

Select Number: 3 Generate/Rebuild FMS SV-Document

Ready to Generate/Rebuild Document? NO// YES

Generating the monthly accrual FMS SV-Document

Generating YTD Accrual Data Extract...

Requested Start Time: NOW// (NOV 30, 1996@10:32:08)

For Accrual Month/Year: 11/96// ^

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data

Multiple Transaction Menu ...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Select Transaction Menu Option:

### Carry Forward Quarterly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables the budget analyst to move open transactions and unspent dollars to the next open quarter automatically. This facilitates the reconciliation of the Sub-allowance balance in FMS and the control point balance in IFCAP.

#### Menu Navigation

Select Funds Distribution Program Menu Option: Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Accrual (Monthly)

Carry Forward Quarterly

Enter FCP Adjustment Data (FISCAL)

Multiple Transaction Menu...

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

#### Station Selection

If you have multiple stations supported by your IFCAP system, you will need to run the Carry Forward process separately for each station number.

> **NOTE:** Recalculate ALL your control points first! Then run the Carry Forward option.

Select STATION NUMBER ('^' TO EXIT): 658// SALEM, VA

Select one of the following:

1 Carry forward Outstanding Requests

2 Carry forward balances for all control points

3 Carry forward balances for a single control point

Select Number:

#### Outstanding Requests

The 1st step is to move any outstanding requests (transactions that are not in a Transaction Complete status) from the closing quarter to the new open quarter. This step defines what quarter is going to be opened. This step MUST be done. The system will display the oldest OPEN quarter. The user is then prompted for the quarter being carried forward. In this example the response would be: 00-3.

Select STATION NUMBER ('^' TO EXIT): 658// SALEM, VA

Select one of the following:

1 Carry forward Outstanding Requests

2 Carry forward balances for all control points

3 Carry forward balances for a single control point

Select Number: 1 Carry forward Outstanding Requests

The oldest OPEN quarter in file is 2000-3.

For Budget Fiscal Year - Quarter (YY-Q): 00-3

Ready to Run? NO// YES

DEVICE: ;;9999 IRMS BLDG 74 ROOM 227E

IFCAP Carry Forward Outstanding Requests from Qtr 00-3 to 00-4

Station: 658 Printed on 07/07/2000

658-00-1-019-0001 ENTERED

658-00-1-019-0003 APPROVED

#### Balances for ALL Control Points

The 2nd step in the Carry Forward process enables the Budget Analyst to move control balances from the closing quarter to the new Open quarter. Any balance, positive, or negative, will be moved to the new open quarter.

> **NOTE:** Balances on Single – Fiscal Year control points may not be moved beyond the 4th Quarter of the Fiscal Year. Balances on a multi-year control point may not be moved beyond the 4th quarter of the final year of the funding, (i.e., multi-year funds for 1998-2000 may not be moved beyond 4th quarter of the FY 2000).

The movement of the balance is done by a two-step process.

1.  The software will review each control point and determine what Ceiling transaction is needed to bring the Fiscal Unobligated column to zero. A Ceiling entry is created in the Closing Quarter for whatever amount is required to make the Fiscal Unobligated column go to zero. The reverse Ceiling entry was created in the Opening Quarter to move that balance to the new quarter. This Ceiling transaction will be applied to both the Control Point Uncommitted Column and the Fiscal Unobligated Column.
2.  The software will then review each control point and determine whether the CP \$Balance column has a zero balance. If it does not, the software will determine what budget transaction is needed to bring the CP \$Balance field to zero. An Adjustment entry is then created in the Closing Quarter for whatever amount is required to make the CP \$Balance column a zero. The reverse Adjustment entry is created in the Opening Quarter to move that balance to the new quarter.

> **NOTE:** The balance is determined by looking at Part 1 - the IFCAP transactions and Part 2- the FMS transactions.

Select Transaction Menu Option: CARRY Forward Quarterly

Select STATION NUMBER ('^' TO EXIT): 658// SALEM, VA

Select one of the following:

1 Carry forward Outstanding Requests

2 Carry forward balances for all control points

3 Carry forward balances for a single control point

Select Number: 2 Carry forward balances for all control points

The oldest OPEN quarter in file is 2000-4.

For Budget Fiscal Year - Quarter (YY-Q): 00-3

Ready to Run? NO// YES

DEVICE: ;;9999 IRMS BLDG 74 ROOM 227E

IFCAP Carry Forward Balances for All CP'S from Qtr 00-3 to 00-4

Station: 658 Printed on 07/07/2000

003 RES SALARIES (CEI) \$0.00

003 RES SALARIES (ADJ) \$0.00

009 FIS RESIDENTS (CEI) \$61414.00

009 FIS RESIDENTS (ADJ) \$120.00

010 ADMINISTRATIVE TRAINEES (CEI) \$0.00

010 ADMINISTRATIVE TRAINEES (ADJ) \$0.00

011 COS C&A'S (CEI) \$0.00

011 COS C&A’S (ADJ) \$0.00

012 FIS SALARIES (CEI) \$-11936.00

012 FIS SALARIES (ADJ) \$0.00

#### Balances for a Single Control Point

Occasionally monies may appear in a closed quarter. This step enables the Budget Analyst to move the balance from a previously closed quarter to the subsequent quarter. (this quarter may also be a closed quarter). The user would then Carry Forward from that closed quarter to the next quarter. This step would be repeated until the balance had been moved to the current Open quarter. The same two-step process is used to determine the value the transactions will have.

#### Mail Bulletins

When the Carry Forward transactions are created a Mail bulletin is sent to the Control Point Users.

Subj: IFCAP Carry Forward Balances for All CP'S from Qtr 00-3 to 00-4

\[#9432\] 07 Jul 00 09:06 1 line

From: IFUSER, ONE In 'IN' basket. Page 1

--------------------------------------------------------------------------------------

060 FISCAL SVC Qtr 00-3 closed. \$10020017.43 carried forward.

Enter message action (in IN basket): Ignore//

Subj: IFCAP Carry Forward Balances for All CP'S from Qtr 00-3 to 00-4

\[#9433\] 07 Jul 00 09:06 1 line

From: IFUSER, ONE In 'IN' basket. Page 1

--------------------------------------------------------------------------------------

060 FISCAL SVC Qtr 00-3 adjusted with \$-35691.48.

Enter message action (in IN basket): Ignore//

Subj: IFCAP Carry Forward Balances for All CP'S from Qtr 00-3 to 00-4 \[#9523\] 07 Jul 00 09:08 1 line

From: IFUSER, ONE In 'IN' basket. Page 1

--------------------------------------------------------------------------------------

990 SUPPLY FUND Qtr 00-3 closed. \$635161.60 carried forward.

Enter message action (in ‘IN’ basket): Ignore//

Subj: IFCAP Carry Forward Balances for All CP'S from Qtr 00-3 to 00-4

\[#9524\] 07 Jul 00 09:08 1 line

From: IFUSER, ONE In 'IN' basket. Page 1

--------------------------------------------------------------------------------------

990 SUPPLY FUND Qtr 00-3 adjusted with \$20070.48.

Enter message action (in ‘IN’ basket): Ignore//

#### End of Year Carry Forward

You must always do Step 1 – moving transactions – even at the end of the Fiscal Year. If you have set the Site Parameter switch to NO – your open transactions for multi-year control points will not move forward. The Application Coordinator can set the switch.

Then do Step 2 to move balances. Only balances on multi-year control points will move forward.

Select IFCAP Application Coordinator Menu Option: SITE Parameters

STATION NUMBER: 658

STATION: 658//

FACILITY TYPE: VAMC// ^CARRY FORWARD 4TH QTR REQUESTS

CARRY FORWARD 4TH QTR REQUESTS:

The field is used to control the 4th quarter outstanding requests being carried forward to the new fiscal year.

Choose from:

Y YES

N NO

CARRY FORWARD 4TH QTR REQUESTS: NO

### Options in the Print Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu ...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report of Unpaid PC Transactions by FCP

#### Selected Control Points

#### Introduction

Use this option to generate the Funds distribution Control Point Display report, which lists quarterly obligations by transaction number for a set of Control Points that you select. This report provides the transaction number and the funding by quarter. This is the budget record of the Control Point funding.

#### Select Fund Control Point

Enter a station number and a fiscal year. Enter one or more Fund Control Points.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

Select FUND CONTROL POINT: 101 LAB TESTING 101 ...............

ANOTHER FUND CONTROL POINT: 105 LAB TESTING 105 ……

ANOTHER FUND CONTROL POINT: 103 LAB TESTING 103 ..

ANOTHER FUND CONTROL POINT:

DEVICE: LAT

#### Interpreting the Report

IFCAP will display each funding transaction, the date the transaction took place, whether the funding was from recurring or non-recurring funds, the amount of each funding by quarter, and the total funding for the year, beginning with the first Control Point you specified. The report will have quarterly and annual subtotals for each Control Point, and quarterly and annual totals for all of the Control Points combined.

FUNDS DISTRIBUTION CONTROL POINT DISPLAY JUN 9,1994 09:10 PAGE 1

TRANSACTION TRANSACTION ANNUALIZATION

NUMBER DATE REC/NON-REC AMOUNT

1ST QTR 2ND QTR 3RD QTR 4TH QTR

TOTAL

DESCRIPTION

--------------------------------------------------------------------------------------

CONTROL POINT: 103 LAB TESTING 103

688-94-0087 MAY 27,1994 NON-RECURRING 0.00

-20.00

-20.00

688-94-0090 MAY 27,1994 NON-RECURRING 0.00

-10.00

-10.00

--------------------------------------------------------------------------------------

SUBTOTAL -30.00 0.00 0.00

0.00 -30.00

FUNDS DISTRIBUTION CONTROL POINT DISPLAY JUN 9,1994 09:10 PAGE 2

TRANSACTION TRANSACTION ANNUALIZATION

NUMBER DATE REC/NON-REC AMOUNT

1ST QTR 2ND QTR 3RD QTR 4TH QTR

TOTAL

DESCRIPTION

--------------------------------------------------------------------------------------

CONTROL POINT: 105 LAB TESTING 105

688-94-0099 JUN 8,1994 NON-RECURRING

100.00

100.00

Transfer for shared expense tracked at CP 105

--------------------------------------------------------------------------------------

SUBTOTAL 100.00 0.00 0.00

0.00 100.00

--------------------------------------------------------------------------------------

TOTAL 70.00 0.00 0.00

0.00 70.00

#### Range of Transactions

#### Introduction

Use this option to generate a listing of a range of funds distribution transactions that you select. This report prints the transaction number, Control Point number, TDA number, transaction date, and a breakdown of funding by quarter.

#### Select Range of Transactions

Enter a station number and a fiscal year. Enter the first transaction you want in the report at the Start with Transaction Number: prompt. Enter the last transaction you want in the report at the Go to Transaction Number: prompt. IFCAP finds these numbers by looking at the suffix of the transaction number. For example, since 51 is entered at the Go To: prompt, the last transaction number on the report will end in “0051”. After printing the report, IFCAP will return to the Print Menu.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

START WITH TRANSACTION NUMBER: 1//

GO TO TRANSACTION NUMBER: LAST// 51

DEVICE: HOME// LAT

FUNDS DISTRIBUTION RANGE OF TRANSACTIONS DISPLAY

JUN 9,1994 09:15 PAGE 1

TRANSACTION CONTROL TDA TRANSACTION

NUMBER POINT NUMBER DATE

NUMBER

1ST QTR 2ND QTR 3RD QTR 4TH QTR

TOTAL

DESCRIPTION

--------------------------------------------------------------------------------------

688-94-0046 9988

0.00

688-94-0047 101

0.00

688-94-0048 101 APR 19,1994

5.01 2.02

5.03 5.04 17.10

FUNDS DISTRIBUTION RANGE OF TRANSACTIONS DISPLAY

JUN 9,1994 09:15 PAGE 2

TRANSACTION CONTROL TDA TRANSACTION

NUMBER POINT NUMBER DATE

NUMBER

1ST QTR 2ND QTR 3RD QTR 4TH QTR

TOTAL

DESCRIPTION

--------------------------------------------------------------------------------------

688-94-0049 101 APR 19,1994

-200.00

-200.00

688-94-0050 102 APR 19,1994

200.00

200.00

688-94-0051 9988 APR 19,1994

-123.00

-123.00

--------------------------------------------------------------------------------------

TOTAL -117.99 2.02

5.03 5.04 -105.90

PRESS RETURN TO CONTINUE

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report of Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option:

#### Transfer of Disbursing Authority

#### Introduction

This option prints a report on all Transfers of Disbursing Authority (TDAs) for a facility, or a range of TDAs that you select. This report prints the TDA number, TDA date, transaction number, Control Point number, description, and breakdown of funding by quarter.

#### Compile/Print Report

Enter a Station number and Fiscal Year. IFCAP will list the transactions by TDA number, date, transaction number, and Control Point.

#### Detailed Appropriation Summary

#### Introduction

Use this option to generate a listing (by Appropriation) of all TDAs received by the facility.

This list includes a line of details for each TDA. This detailed summary prints the transaction numbers, Control Point numbers, TDA numbers, transaction dates, and breakdown of funding by quarter for all appropriations in IFCAP.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

Beginning TDA Number: 1// 1

Ending TDA Number: 9999// 9999

DEVICE: LAT

FUNDS DISTRIBUTION TRANSFER OF DISBURSING AUTHORITY (TDA) LISTING

JUN 9,1994 09:54 PAGE 1

TRANSACTION CONTROL TDA TRANSACTION

NUMBER POINT NUMBER DATE

NUMBER

1ST QTR 2ND QTR 3RD QTR 4TH QTR

TOTAL

DESCRIPTION

--------------------------------------------------------------------------------------

1 MAY 26,1994 688-94-0081 5101

1000000.00 1000000.00 11000000.00 10000000.00

23000000.00

--------------------------------------------------------------------------------------

1 MAY 26,1994 688-94-0084 5102

123456.00

123456.00

TEST RELEASE

--------------------------------------------------------------------------------------

1 MAY 31,1994 688-94-0092 101

1000000.00 1000000.00

TO ALLOW RECEIVING REPORT TEST

#### Compile/Print Report

Enter a station number and a fiscal year. IFCAP will list the transactions for each appropriation by transaction number and Control Point. This can be a rather lengthy report; only print it if you cannot obtain the information you need using one of the other reports.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

DEVICE: LAT

FUNDS DISTRIBUTION APPROPRIATION SUMMARY (DETAIL) REPORT

JUN 9,1994 10:19 PAGE 1

TRANSACTION CONTROL TDA TRANSACTION

NUMBER POINT NUMBER DATE

NUMBER

1ST QTR 2ND QTR 3RD QTR 4TH QTR

TOTAL

DESCRIPTION

--------------------------------------------------------------------------------------

APPROPRIATION: 36\_/\_0181

CONTROL POINT: 201 LAB TESTING 201

688-94-0074 201 MAY 1,1994

-100.00

-100.00

688-94-0076 201 MAY 1,1994

-100.00

-100.00

--------------------------------------------------------------------------------------

SUBTOTAL -100.00 0.00 -100.00 0.00

-200.00

FUNDS DISTRIBUTION APPROPRIATION SUMMARY (DETAIL) REPORT

JUN 9,1994 10:19 PAGE 2

TRANSACTION CONTROL TDA TRANSACTION

NUMBER POINT NUMBER DATE

NUMBER

1ST QTR 2ND QTR 3RD QTR 4TH QTR

--------------------------------------------------------------------------------------

CONTROL POINT: 202 LAB TESTING 202

688-94-0075 202 MAY 1,1994

100.00

100.00

688-94-0077 202 MAY 1,1994

100.00

100.00

--------------------------------------------------------------------------------------

SUBTOTAL 100.00 0.00 100.00 0.00

200.00

SUBTOTAL 0.00 0.00 0.00 0.00

0.00

FUNDS DISTRIBUTION APPROPRIATION SUMMARY (DETAIL) REPORT

JUN 9, 1994 10:19 PAGE 3

TRANSACTION CONTROL TDA TRANSACTION

NUMBER POINT NUMBER DATE

NUMBER

1ST QTR 2ND QTR 3RD QTR 4TH QTR

--------------------------------------------------------------------------------------

APPROPRIATION: 36_0151.007

688-94-0064 9988 APR 26,1994

100.00

100.00

--------------------------------------------------------------------------------------

SUBTOTAL -35.01 0.00 0.00 0.00

-35.01

SUBTOTAL -35.01 0.00 0.00 0.00

-35.01

TOTAL 2039303.10 3672205.20 25045203.33 14059274.44 44815986.07

#### Appropriation Summary Totals

#### Introduction

Use this option to generate a report of TDAs received by the facility. This report is only a summary and prints only the total dollar value of all the quarters funded. The first line is a Control Point subtotal; the second is a subtotal of the appropriation number. A grand total is given for the station number.

#### Compile/Print Report

Enter a station number and a fiscal year. IFCAP will list the total amounts for each appropriation and every Control Point within that appropriation. The report will also list totals for all of the funding appropriations combined.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

DEVICE: LAT

FUNDS DISTRIBUTION APPROPRIATION SUMMARY (TOTALS)

JUN 9,1994 11:50 PAGE 1

1ST QTR 2ND QTR 3RD QTR 4TH QTR

TOTAL

-----------------------------------------------------------------------------

APPROPRIATION: 688-94-36\_/\_0161.001

CONTROL POINT: 019 SPD

SUBTOTAL 1.10 1.40 1.20 1.30

5.00

SUBTOTAL 1.40 1.10 1.20 1.30

5.00

APPROPRIATION: 688-94-36_0151.007

CONTROL POINT: 101 LAB TESTING 101

SUBTOTAL -2116.99 -341.00 999601.03 22794.04

1019937.08

CONTROL POINT: 102 LAB TESTING 102

SUBTOTAL 2300.00 200.00 45800.00 400.00

48700.00

SUBTOTAL 183.01 -141.00 1045401.03 23194.04

1068637.08

APPROPRIATION: 688-94-36_0160.020

CONTROL POINT: 9988 LAB TESTING 988 S

SUBTOTAL 0.00 -35.01 -35.01 0.00

0.00

SUBTOTAL 0.00 -35.01 -35.01 0.00

0.00

TOTAL 2039303.10 3672205.20 25045203.33 14059274.44

44815986.07

#### FTEE Summary by Appropriation

#### Introduction

This option prints a report (by Appropriation) of FTEE (Full Time Employee Equivalent) information received on TDAs by station number and Fiscal Year. The report prints the amount of FTEE assigned to each TDA number.

#### Compile/Print Report

Enter a station number and a fiscal year. IFCAP will display each appropriation and the TDAs for that appropriation, and the FTEE for each TDA.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

DEVICE: LAT RIGHT MARGIN: 80//

FTEE SUMMARY BY APPROPRIATION JUN 9,1994 12:08 PAGE 1

NON

TDA TRANSACTION RECURRING RECUR TRNG TOTAL

NUMBER TDA DATE NUMBER FTEE FTEE FTEE FTEE

DESCRIPTION

--------------------------------------------------------------------------------------

APPROPRIATION: 688-94-36_0151.007

1 MAY 31,1994 688-94-0092 0.0

TO ALLOW RECEIVING REPORT TEST

432 MAY 26,1994 688-94-0085 0.0

TESTING

460 JUN 3,1994 688-94-0089 120.0 10.0 100.0 230.0

Training program

--------------------------------------------------------------------------------------

SUBTOTAL 100.0 120.0 10.0 230.0

TOTAL 100.0 120.0 10.0 230.0

TOTAL 100.0 120.0 10.0 230.0

#### Supplementary Options in the Budget Distribution Reports Menu

This menu contains options that generate quarterly, biannual and fiscal year Budget Distribution Reports (RD285). The instructions in the next section will use the Complete Fiscal Year report as an example.

#### Budget Distribution Reports

#### 1st Quarter Report

This report presents the data for the 1st quarter of a specified Fiscal year.

#### 2nd Quarter Report

This report presents the data for the 2nd quarter of a specified Fiscal year.

#### 3rd Quarter Report

This report presents the data for the 3rd quarter of a specified Fiscal year.

#### 4th Quarter Report

This report presents the data for the 4th quarter of a specified Fiscal year.

#### April - September

This report presents the data for the second half of the Fiscal year.

#### October - March

This report presents the data for the 1st half of a specified Fiscal year.

#### Complete Fiscal Year

This report presents the data for the full Fiscal year.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Print Menu from the Funds Distribution Program Menu.

Select Budget Distribution Reports Menu from the Print Menu.

Select a report duration from the Budget Distribution Reports Menu. You can select a report for a quarter, a six-month report, or a report for the entire fiscal year.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report on Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option: Budget Distribution Reports Menu

1st Quarter Report

2nd Quarter Report

3rd Quarter Report

4th Quarter Report

April – September

October – March

Complete Fiscal Year

Select Budget Distribution Reports Menu Option: Complete Fiscal Year

#### Compile/Print Report

Select a Station Number and a fiscal year. IFCAP will print the report, listing the budget distribution by budget sort category.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 93// 94

...Excuse me, let me put you on 'HOLD' for a second...

DEVICE: LAT RIGHT MARGIN: 80//

BUDGET DISTRIBUTION SUMMARY ENTIRE FISCAL YEAR

JUN 9,1994 12:29 PAGE 1

TRANSACTION TDA

NUMBER NUMBER

OCT - CUM NOV - CUM DEC - CUM JAN – CUM FEB -CUM MAR - CUM

APR - CUM MAY - CUM JUN - CUM JUL – CUM AUG - CUM SEP - CUM

DESCRIPTION

--------------------------------------------------------------------------------------

BUDGET SORT CATEGORY: 26 TRAINING

688-94-0089 460

Training program

SUBTOTAL

0.00 0.00 0.00 0.00 0.00 0.00

0.00 0.00 0.00 0.00 0.00 0.00

0.00 0.00 0.00 0.00 0.00 0.00

0.00 0.00

TOTAL

0.00 0.00 0.00 0.00 0.00 0.00

0.00 0.00 0.00 0.00 0.00 0.00

0.00 0.00 0.00 0.00 0.00 0.00

0.00 0.00

#### Control Point List

#### Introduction

Use this option to print the overcommit status of the Control Points and what users are assigned to each Control Point.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Print Menu from the Funds Distribution Program Menu.

Select Control Point List from the Print Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu ...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report of Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option: Control Point List

#### Compile/Print Report

IFCAP will print the program, name and number of each Control Point, what over commit status has been assigned to it, the users of that Control Point, and their level of access.

After printing the report, IFCAP will return to the Print Menu.

LIST OF CONTROL POINTS OCT 5,1994 12:08 PAGE 1

SERVICE

ROLL

OVER OVERCOMMIT?

USER LEVEL OF ACCESS

--------------------------------------------------------------------------------------

CONTROL POINT: 066 NEW FCP TEST

CDL

FUND: 0129A1 A/O: 10 PGM: 70

FCP/PRJ: AB3118 OC: JOB:

NO OVERCOMMIT PERMIT

IFUSER, TWO CONTROL POINT OFFICIAL

CONTROL POINT: 101 LAB TESTING 101

FIS

FUND: 0160A1 A/O: 10 PGM: 70

FCP/PRJ: 300 OC: JOB:

033 CURRENT AND FUTURE Q

IFUSER, THREE CONTROL POINT OFFICIAL

IFUSER, FOUR CONTROL POINT OFFICIAL

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu ...

826 (IFCAP) Report

Detailed Report on Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option:

#### FCP BOC List

#### Introduction

This report is similar to the one on the Cost Center Management menu but lists the Control Points and their associated budget object codes. This report is very long.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Print Menu from the Funds Distribution Program Menu.

Select FCP BOC List from the Print Menu.

Accounting Technician Menu ...

Funds Distribution Program Menu ...

Payment/Invoice Tracking Menu ...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report on Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option: FCP BOC List

#### Compile/Print Report 

IFCAP will print a report listing the available budget object codes for every Control Point.

DEVICE: LAT RIGHT MARGIN: 80//

FCP BOC LIST JUN 10,1994 14:22 PAGE 1

COST

CONTROL POINT CENTER OVERCOMMIT?

AUTHORIZED BOC

--------------------------------------------------------------------------------------

009 TRAINEE SALARIES 8401 CURRENT AND FUTURE QUARTERS

1031 Other Health Technicians and Aides not Previously Identified

1043 VA Fellows as RWJ Clinical Scholars

#### Control Point PO List

#### Introduction

This option lists the status of purchase orders, listed by Control Point for a range of dates that you specify.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Print Menu from the Funds Distribution Program Menu.

Select Control Point PO List from the Print Menu

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu ...

Control Point List

FCP BOC List

Control Point PO List Audit Reports Menu ...

826 (IFCAP) Report

Detailed Report on Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option: Control Point PO List

#### Compile/Print Report

IFCAP will print the FCP PO Status Report, which lists every active purchase order for each Control Point.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="13"><blockquote>
<p>START WITH FCP: FIRST//</p>
<p>START WITH DATE SIGNED: FIRST// DEVICE: LAT RIGHT MARGIN: 80//</p>
<p>FCP PO STATUS JUN 10,1994 14:50 PAGE 1</p>
<p>P.O. # STATUS PO DATE TOTAL</p>
</blockquote>
<p>--------------------------------------------------------------------------------------</p>
<blockquote>
<p>FCP: 101 ISC2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>B40034</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">MAR</td>
<td colspan="2"><blockquote>
<p>9,1994</p>
</blockquote></td>
<td colspan="3">503.00</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>B40029</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">MAR</td>
<td colspan="2"><blockquote>
<p>4,1994</p>
</blockquote></td>
<td colspan="3">503.00</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>B40028</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PPM Clerk Signature</p>
</blockquote></td>
<td colspan="2">MAR</td>
<td colspan="2"><blockquote>
<p>4,1994</p>
</blockquote></td>
<td colspan="3">24.00</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>B40027</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">MAR</td>
<td colspan="2"><blockquote>
<p>4,1994</p>
</blockquote></td>
<td colspan="3">40.00</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>B40026</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">MAR</td>
<td colspan="2"><blockquote>
<p>3,1994</p>
</blockquote></td>
<td colspan="3">24.00</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>B40025</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">MAR</td>
<td colspan="2"><blockquote>
<p>3,1994</p>
</blockquote></td>
<td colspan="3">84.00</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>B40024</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Ordered</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>and Obligated</p>
</blockquote></td>
<td colspan="2">MAR</td>
<td colspan="2"><blockquote>
<p>2,1994</p>
</blockquote></td>
<td colspan="3">254.75</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>B40023</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">FEB</td>
<td colspan="2"><blockquote>
<p>24,1994</p>
</blockquote></td>
<td colspan="3">100.00</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>B40021</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">FEB</td>
<td colspan="2"><blockquote>
<p>24,1994</p>
</blockquote></td>
<td colspan="3">20.00</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>B40019</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">FEB</td>
<td colspan="2"><blockquote>
<p>24,1994</p>
</blockquote></td>
<td colspan="3">0.25</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>B40017</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">FEB</td>
<td colspan="2"><blockquote>
<p>23,1994</p>
</blockquote></td>
<td colspan="3">0.25</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>B40016</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Partial</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Order Received (Amended)</p>
</blockquote></td>
<td colspan="2">FEB</td>
<td colspan="2"><blockquote>
<p>22,1994</p>
</blockquote></td>
<td colspan="3">257.51</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>B40013</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Fiscal Action</p>
</blockquote></td>
<td colspan="2">FEB</td>
<td colspan="2"><blockquote>
<p>4,1994</p>
</blockquote></td>
<td colspan="3">251.00</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>SUBTOTAL</p>
</blockquote></td>
<td colspan="11">2061.76</td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>FCP PO STATUS</p>
<p>P.O. #</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STATUS</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>JUN 10,1994 PO DATE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>14:50</p>
</blockquote></td>
<td><blockquote>
<p>PAGE 2</p>
</blockquote></td>
<td><blockquote>
<p>TOTAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="13"><blockquote>
<p>FCP: 102 LAB TESTING 102</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B40058</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>Ordered and Obligated (Amended)</p>
</blockquote></td>
<td colspan="2">JUN</td>
<td colspan="2"><blockquote>
<p>7,1994</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>47.92</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SUBTOTAL</p>
</blockquote></td>
<td colspan="12">47.92</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL</p>
</blockquote></td>
<td colspan="12">2109.68</td>
</tr>
</tbody>
</table>

#### (IFCAP) Report

#### Introduction

Use this option to list Ceiling Transaction Totals for user-selected Quarter and FYTD obligations for Control Points. It also lists by Control Point within Appropriation. Using this option will list ceiling transactions, obligations, unobligated balances and FYTD obligations for Control Points within a specified quarter.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Print Menu from the Funds Distribution Program Menu.

Select 826 (IFCAP) Report from the Print Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report on Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option: 826 (IFCAP) Report

#### Compile/Print Report

Enter a station number and a Control Point. Enter a fiscal year and a Control Point. IFCAP will list the cost ceiling, obligations, unobligated balance, and obligations for the fiscal year to date for each Control Point, grouped by appropriation. The report will list totals for each appropriation and grand totals for the service. After printing the report, IFCAP will return to the Print Menu.

Select STATION NUMBER ('^' TO EXIT): 503// ALTOONA, PA

Sele6ct FISCAL YEAR ('^' to EXIT): 94//

Select FISCAL QUARTER: 3//

DEVICE: HOME// LAT RIGHT MARGIN: 80//

STATUS OF FUNDS - 826 REPORT STATION NO: 503 PAGE: 1

\* = DEACTIVATED CONTROL POINT

FISCAL YEAR: 94

QUARTER: 3

UNOBLIGATED

COST CEILING OBLIGATIONS

BALANCE FYTD

FUND CONTROL POINT FOR QTR FOR QTR

FOR QTR OBLIGATIONS

-------------------------------------------------------------------------------------

APPROPRIATION: 364/\_0161.001

019 SPD 1,005,000.00 0.00

1,005,000.00 531.21

033 PHARMACY 1,853,476.00 0.00

1,853,476.00 0.00

120 DIETETIC SU 1,000,000.00 0.00

1,000,000.00 0.00

203 STUDENT 2,000,000.00 1,000,000.00

1,000,000.00 0.00

204 STUDENT 2,000,000.00 1,000,000.00

1,000,000.00 0.00

205 STUDENT 2,000,000.00 1,000,000.00

1,000,000.00 0.00

206 STUDENT 2,000,000.00 1,000,000.00

1,000,000.00 0.00

207 STUDENT 2,000,000.00 0.00

2,000,000.00 0.00

208 STUDENT 1,000,000.00 0.00

1,000,000.00 0.00

TOTAL: 14,858,476.00 4,000,000.00

10,858,476.00 531.21

APPROPRIATION: 364/\_0181

201 LAB TESTING 2,000,000.00 1,000,000.00

1,000,000.00 0.00

202 LAB TESTING 2,000,000.00 1,000,000.00

1,000,000.00 0.00

TOTAL: 4,000,000.00 2,000,000.00

2,000,000.00 0.00

STATION TOTALS: 18,858,476.00 6,000,000.00 12,858,476.00

531.21

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu ...

826 (IFCAP) Report

Detailed Report of Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option:

#### Introduction

This option allows you to print a 2237 for any Control Point you are authorized to use.

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu. Select Print Menu from the Funds Distribution Program Menu.

Select Display 2237 Request from the Print Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report on Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accruals

Select Print Menu Option: Display 2237 Request

#### Select Transaction

Enter a fiscal year and a fiscal quarter. Enter a Control Point and a transaction number. If you do not know the transaction number, enter three question marks at the Select Control Point Activity Transaction Number: prompt, and IFCAP will display the available transactions. Once you have chosen a transaction, IFCAP will display the 2237 form or 1358 Obligation form for that transaction.

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: 101 LAB TESTING 101

...OK? Yes// (Yes)

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???

Attempting lookup in transaction file.

Attempting lookup using 688-94-3-101 (STA \# - FY - QTR - FCP)

1 688-94-3-101-0138 OBL IFVENDOR, FOUR C45097

2 688-94-3-101-0139 OBL IFVENDOR, ONE

TEST ITEM \#11

3 688-94-3-101-0140 OBL IFVENDOR, SIX

4 688-94-3-101-0141 OBL IFVENDOR, FOUR C45107

5 688-94-3-101-0143 OBL

TYPE '^' TO STOP, OR

CHOOSE 1-5: 4

688-94-3-101-0141 JUN 10,1994@15:17:31 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Requestor: \|Date Requested: \|Obligation No.:

IFUSER, FIVE \|APR 8,1994 \| 688-C45107

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Vendor: \|Contract Number:

IFVENDOR, FOUR \|

Name and Title Approving Off.: \|Signature: \|Date Signed:

IFUSER, FIVE \|/ES/ IFUSER, FIVE \|APR 8,1994@08:18:04

\| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FUND CERTIFICATION: The supplies and services listed on this request are properly chargeable to the following allotments, the available balances of which are sufficient to cover the cost thereof, and funds have been obligated.

Appropriation & Acct. Symbols \|Obligated By: \|Date Obligated:

688-3640151-101-820111-2343 \|/ES/ IFUSER, FIVE \|APR 8,1994

\| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

688-94-3-101-0141 688-C45107 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:

--------------------------------------------------------------------------

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated: 688-3640151-101-820111-2343 \|/ES/ IFUSER, FIVE \|APR 8,1994

Authority: SUB:

SERIVCE START DATE: SERVICE END DATE:

Purpose:

1358 DEMO

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ESTIMATED OBLIGATION RECAP

DATE REF# CPA# AMOUNT BALANCE

04/08 0001 688-94-3-101-0141 \$ 5000.00 \$ 5000.00

04/08 0002 688-94-3-101-0142 \$ -2000.00 \$ 3000.00

AUTH. AUTH. CUMULATIVE UNLIQ

DATE SEQ# REFERENCE AMOUNT BALANCE AUTH. AMT. LIQUID BAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

688-94-3-101-0142 688-C45107 PAGE 3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORIZATION & ORDER RECORD LIQUIDATION RECORD

AUTH. AUTH. CUMULATIVE UNLIQ

DATE SEQ# REFERENCE AMOUNT BALANCE AUTH. AMT. LIQUID BAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTALS \$0.00 \$0.00 \$0.00 \$3000.00

VA Form 4-1358a-ADP (NOV 1987)

#### FCP Accounting Elements

#### Introduction

This option will list all Fund Control Points and their FMS accounting elements (station, fund, administrative office, program, FCP/PRJ (project), object class, job).

#### Menu Navigation

Select Funds Distribution Program Menu from the Funds Distribution & Accounting Menu.

Select Print Menu from the Funds Distribution Program Menu.

Select FCP Accounting Elements from the Print Menu.

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report on Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option: FCP Accounting Elements

#### Select Sort by Criteria

Press the Enter key at the Sort By: prompt to sort the list by Fund Control Point number or enter a question mark to list all the other ways you can sort the information in the report.

> SORT BY: NUMBER// ?

> ANSWER WITH FIELD NUMBER, OR LABEL

> Do you want the entire FIELD List? Y (Yes)

> CHOOSE FROM:

> .01 STATION NAME

> 1 CONTROL POINT NAME (multiple)

> 2 FUND RELEASING OFFICIAL (multiple)

> 3 STATION OVERCOMMIT SWITCH

> 3.1 STATION ROLLOVER OF EOQ BAL.

> 4 SUPPLY FUND CAP

> 5 INVENTORY VALUE

> 6 DUE-IN VALUE

> 7 TOTAL CAP AVAILABLE

> 8 PRINT ON DEMAND

> 9 STATION OPEN QUARTER DATE

> 10 EDI ORDER RELEASE

> 11 SITE ALL/DELIVERY ORDER SWITCH

> TYPE '-' IN FRONT OF NUMERIC-VALUED FIELD TO SORT FROM HI TO LO

> TYPE '+' IN FRONT OF FIELD NAME TO GET SUBTOTALS BY THAT FIELD,

> '#' TO PAGE-FEED ON EACH FIELD VALUE, '!' TO GET RANKING NUMBER,

> '@' TO SUPPRESS SUB-HEADER, '\]' TO FORCE SAVING SORT TEMPLATE

> TYPE ';TXT' AFTER FREE-TEXT FIELDS TO SORT NUMBERS AS TEXT

> TYPE \[TEMPLATE NAME\] IN BRACKETS TO SORT BY PREVIOUS SEARCH RESULTS

> TYPE 'BY(0)' TO DEFINE RECORD SELECTION AND SORT ORDER

#### Compile/Print Report

You can limit the report to start at a number, station name, etc., that you specify, or press the Enter key at the Start With: prompt to list all data. Enter an output device. IFCAP will list the Fund Control Point accounting elements, sorted by the criterion that you specified at the Sort By: prompt. After printing or displaying the report, IFCAP will return to the Print Menu.

START WITH NUMBER: FIRST//

DEVICE: LAT RIGHT MARGIN: 80//

FUND CONTROL POINT ACC. ELEMENTS LIST NOV 2,1994 15:11 PAGE 1

CONTROL POINT ACTIVE/INACTIVE

OBJECT

FUND A/O PROGRAM FCP/PRJ JOB CLASS

--------------------------------------------------------------------------------------

STATION: 61

STATION: 123

STATION: 452

STATION: 503

FCP:

FCP: 101 TEST CP

91 02 AA 894 11

FCP: 111 FIRST

50 02 AA 894 11 24

STATION: 695

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report on Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

Select Print Menu Option:

### Options in the Audit Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu...

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu...

826 (IFCAP) Report

Detailed Report of Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review

Fiscal Pending Action

History of Purchase Card Transactions

Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card

Transactions Year To Date Accrual

Select Print Menu Option: Audit Reports Menu

Control Point Activity File Inquiry

Procurement and Accounting Transactions Inquiry

Select Audit Reports Menu Option:

#### Control Point Activity File Inquiry

#### Introduction

This option lists all of the information available for a transaction, including its source of funds, the date it was obligated, and who made the request.

#### Select Transaction Number

Enter a transaction number at the Select Control Point Activity Number: prompt. If you do not know the transaction number, enter three question marks at the prompt and IFCAP will list the available transactions.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Select CONTROL POINT ACTIVITY NUMBER: ???</p>
<p>CHOOSE FROM:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>503-93-2-009-0001</td>
<td><blockquote>
<p>OBL</p>
</blockquote></td>
<td><blockquote>
<p>C30001</p>
</blockquote></td>
</tr>
<tr class="even">
<td>503-93-2-009-0002</td>
<td><blockquote>
<p>OBL</p>
</blockquote></td>
<td><blockquote>
<p>C30002</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>503-93-2-009-0003</td>
<td><blockquote>
<p>OBL</p>
</blockquote></td>
<td><blockquote>
<p>C30003</p>
</blockquote></td>
</tr>
<tr class="even">
<td>503-93-2-009-0004</td>
<td><blockquote>
<p>OBL</p>
</blockquote></td>
<td><blockquote>
<p>C30004</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>503-93-2-009-0005</td>
<td><blockquote>
<p>OBL</p>
</blockquote></td>
<td><blockquote>
<p>C30005</p>
</blockquote></td>
</tr>
<tr class="even">
<td>503-93-2-009-0006</td>
<td><blockquote>
<p>OBL</p>
</blockquote></td>
<td><blockquote>
<p>C30006</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>503-93-2-009-0007</td>
<td><blockquote>
<p>ADJ</p>
</blockquote></td>
<td><blockquote>
<p>C30001</p>
</blockquote></td>
</tr>
<tr class="even">
<td>503-93-2-009-0008</td>
<td><blockquote>
<p>ADJ</p>
</blockquote></td>
<td><blockquote>
<p>C30001</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>503-93-2-009-0009</td>
<td colspan="2"><blockquote>
<p>ADJ C30001</p>
</blockquote></td>
</tr>
<tr class="even">
<td>503-93-2-009-0010</td>
<td colspan="2"><blockquote>
<p>OBL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>503-93-2-009-0011</td>
<td colspan="2"><blockquote>
<p>OBL</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Select CONTROL POINT ACTIVITY NUMBER: 0009 688-94-3-8101-0009</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Interpreting Processing History

IFCAP will list the “processing history” of the transaction, including the Control Point, the name of the requestor, and the cost of the transaction. You may look at the processing history of another transaction by entering another transaction number at the Select Control Point Activity Number: prompt or press the Enter key to return to the Audit Reports Menu.

Processing History for:

TRANSACTION NUMBER: 688-94-3-8101-0009 TRANSACTION TYPE: OBLIGATION

FORM TYPE: 1358 ORDER STATION NUMBER: 688

DATE OF REQUEST: SEP 1700 CONTROL POINT: 8101 KATEY

ACCOUNTING DATA: 3640151.007 COST CENTER: 820111 LAB TEST CC

BOC1: 2580 Miscellaneous Contractual BOC1 \$ AMOUNT: 40000

BBFY: 1994 FCP/PRJ: 0100201A3

COMMITTED (ESTIMATED) COST: 40000 DATE COMMITTED: JUN 1, 1994

TRANSACTION \$ AMOUNT: 40000 REQUESTOR: IFUSER, SIX

VALIDATION VERSION: 1

JUSTIFICATION: TEST

Select CONTROL POINT ACTIVITY NUMBER:

Control Point Activity File Inquiry

Procurement and Accounting Transactions Inquiry

Select Audit Reports Menu Option:

#### Procurement and Accounting Transactions Inquiry

#### Introduction

This option creates a report of the “processing history” of the transaction, including the Control Point, the budget object code (BOC), and the item description. This is a long report.

#### Select Transaction Number

Enter a transaction number at the Control Point Activity Number: prompt. If you do not know the transaction number, enter three question marks at the prompt and IFCAP will display the available transactions.

Select CONTROL POINT ACTIVITY NUMBER: ???

CHOOSE FROM:

503-A30001 04-13-93 ST Complete Order Received FCP: 019

\$ 74.00

503-A30002 04-28-93 ST Complete Order Received But Not Ob FCP: 019

\$ 42.00

503-A30003 04-28-93 ST Complete Order Received But Not Ob FCP: 019

\$ 199.80

503-A30004 05-05-93 ST Complete Order Received But Not Ob FCP: 019

\$ 119.48

503-A30005 08-04-93 ST Complete Order Received FCP: 7001

\$ 100.00

503-A30006 08-31-93 ST Complete Order Received But Not Ob FCP: 019

\$ 11.34

503-A30007 09-02-93 ST Complete Order Received But Not Ob FCP: 019

\$ 20.00

503-A30008 09-30-93 ST Complete Order Received But Not Ob FCP: 019

\$ 577.00

503-A30009 10-04-93 ST Complete Order Received FCP: 019

\$ 68.04

503-A30010 10-04-93 ST Complete Order Received FCP: 7001

\$ 130.41

503-A30011 10-04-93 ST Transaction Complete FCP: 7001

\$ 150.06

Select CONTROL POINT ACTIVITY NUMBER: A30001 503-A30001 04-13-93

ST Complete Order Received

FCP: 019 \$ 74.00

#### Interpreting Processing History

IFCAP will list the “processing history” of the transaction, including the Control Point, the budget object code (BOC), and the item description. You cannot edit a transaction once it has been released to Fiscal: you can only view it. IFCAP will list the “processing history” of the transaction, including the budget object code, the name of the requestor, and the cost of the transaction. You cannot edit a transaction once it has been released to Fiscal: you can only view it. You may look at the processing history of another transaction by entering another transaction number at the Select Procurement & Accounting Transactions Purchase Order Number: prompt or press the Enter key to return to the Audit Reports Menu.

Processing History for:

PURCHASE ORDER NUMBER: 503-A30001

METHOD OF PROCESSING: INVOICE/RECEIVING REPORT

FCP: 019 SPD APPROPRIATION: 3630160.001.01

COST CENTER: 828100

BOC1: 2632 Other Medical and Dental Supplies

SUBAMOUNT1: 74 DELIVERY DATE: APR 14, 1993

PRIMARY 2237: 503-93-3-019-0032 EST. SHIPPING AND/OR HANDLING: \$25.00

LINE-ITEM COUNT: 3 TOTAL AMOUNT: 74

NET AMOUNT: 74 LIQUIDATED AMOUNT: 74

EST. SHIPPING LINE-ITEM NO.: 3 VENDOR: IFVENDOR, ONE/HOSPITAL PRODUCTS DIV

REQUESTING SERVICE: SPD SHIP TO: WAREHOUSE

VERBAL PURCHASE ORDER (Y/N): YES CONFIRMATION COPY (Y/N): NO

F.O.B. POINT: ORIGIN SOURCE CODE: 2

PROPOSAL: N/A PRIORITY OF 2237: EMERGENCY

PURCHASING/PPM AGENT: IFUSER, ONE DELIVERY LOCATION: SPD

P.O. DATE: APR 13, 1993, EMERGENCY ORDER?: YES

EXPENDABLE/NONEXPENDABLE: EXPENDABLE LOCAL PROCUREMENT REASON CODE: 1

CERTIFIED P.O.: NO

LINE-ITEM NUMBER: 1 QUANTITY: 5

UNIT OF PURCHASE: BX BOC: 2632 Other Medical and Dental

ITEM MASTER FILE NO.: 30 EST. UNIT COST: 5

ACTUAL UNIT COST: \$5.0000 2237 REFERENCE \#: 503-93-3-019-0032

PACKAGING MULTIPLE: 6 NSN: 6510-01-344-4047

SKU: RO UNIT CONVERSION FACTOR: 6

DESCRIPTION:

ADHESIVE TAPE

TOTAL COST: 25 FEDERAL SUPPLY CLASSIFICATION: 6510

DESCRIPTION LINE COUNT: 1

OBLIGATED BOC: 2632 Other Medical and Dental Supplies

QUANTITY PREVIOUSLY RECEIVED: 5

DATE RECEIVED: APR 13, 1993, QTY BEING RECEIVED: 5

AMOUNT: 25 PARTIAL NUMBER: 1

CONSUMER LEVEL: 96 DO NOT B/O: DO NOT B/O

LINE-ITEM NUMBER: 2 QUANTITY: 24

UNIT OF PURCHASE: EA BOC: 2632 Other Medical and Dental

ITEM MASTER FILE NO.: 43 EST. UNIT COST: 1

ACTUAL UNIT COST: \$1.0000 2237 REFERENCE \#: 503-93-3-019-0032

PACKAGING MULTIPLE: 1 NSN: 6505-01-269-1744

SKU: EA UNIT CONVERSION FACTOR: 1

DESCRIPTION:

APHERESIS KIT-BLOOD CELLS-CONTAINS ONE 100ML BOTTLE OF 9% SODIUM CHLORIDE

TOTAL COST: 24 FEDERAL SUPPLY CLASSIFICATION: 6505

DESCRIPTION LINE COUNT: 3

OBLIGATED BOC: 2632 Other Medical and Dental Supplies

QUANTITY PREVIOUSLY RECEIVED: 24

DATE RECEIVED: APR 13, 1993 QTY BEING RECEIVED: 24

AMOUNT: 24 PARTIAL NUMBER: 1

CONSUMER LEVEL: 40 DO NOT B/O: DO NOT B/O

DRUG TYPE CODE: OTHER DRUGS

PROMPT PAYMENT PERCENT: NET DAYS (TERM): 30

SUPPLY STATUS: Complete Order Received

SUPPLY STATUS ORDER: 30 ESTIMATED ORDER?: NO

FISCAL STATUS ORDER: 35

AMOUNT: 74 TYPE CODE: A2

COMP. STATUS/BUSINESS: Z2 PREF. PROGRAM: K

BREAKOUT CODE: OO

TT/DATE/REF: 921.00.041393. A30001APR 13,1993@16:38:33

OBLIGATED BY: IFUSER, ONE CODE SHEET NUMBER: 2970

VALIDATION CODE: /ES/IFCAP INSTRUCTOR DATE SIGNED: APR 13, 1993@16:38:33

VALIDATION VERSION: 1 ESIG CODE: 10454

TT/DATE/REF: DEC 8,1993@13:08:32 OBLIGATED BY: IFUSER, SEVEN

CODE SHEET NUMBER: 3012 VALIDATION CODE: /ES/IFUSER, SEVEN

DATE SIGNED: DEC 8, 1993@13:08:32 VALIDATION VERSION: 1

ESIG CODE: 7151

NUMBER: 1 DATE: APR 13, 1993

VALIDATION VERSION: 1

BOC1: 2632 Other Medical and Dental Supplies

SUBAMOUNT1: 74 PROCESSED BY FISCAL?: YES

WAREHOUSE APPROVED BY: IFUSER, ONE VALIDATION CODE: /ES/IFCAP INSTRUCTOR

FINAL: FINAL

WAREHOUSE DATE/TIME SIGNED: APR 13, 1993@16:41:48

TOTAL AMOUNT: 74 LINECOUNT: 2

RECEIVED BY (PPM OR DELV.PT.): IFUSER, EIGHT

RECEIVED BY VALIDATION CODE: /ES/V(\`7n:\_F.NNhb\g\$p/e\$

DATE RECEIVED (AT DELV.PT.): APR 13, 1993@16:47:43

RECEIVED BY (AT DELIVERY PT.): IFUSER, EIGHT

RECV.REPORT TRANS.TO AUSTIN: 503-RR-A30001-1

LOG RR CODE SHEETS DONE?: NO VALIDATION VERSION: 1

ESIG CODE: 10454 RCVD BY VALIDATION VERSION: 1

RCVD BY ESIG CODE: 16169

PO PRINTED TIME: APR 13, 1993@16:38 VALIDATION CODE: /ES/IFCAP INSTRUCTOR

VALIDATION DATE/TIME: APR 13, 1993@16:37

AGENT ASSIGNED P.O.: IFUSER, ONE DATE P.O. ASSIGNED: APR 13, 1993@16:34

INVOICE ADDRESS: FMS-VA-1-503 EDI MESSAGE NO.: 3660

VALIDATION VERSION: 1 ESIG CODE: 10454

2237 REFERENCE NUMBER: 503-93-3-019-0032

ACCOUNTABLE OFFICER: IFUSER, ONE VALIDATION CODE: /ES/IFCAP INSTRUCTOR

DATE SIGNED: APR 13, 1993

CURRENT STATUS: Sent to Purchasing & Contracting

CP FUND STATUS: INSUFFICIENT FUNDS TYPE OF REQUEST: UNPOSTED

SOURCE OF REQUEST: NOT AVAILABLE FROM ANY OF THESE SOURCES

INVENTORY/DISTRIBUTION POINT: 688-SPD ESIG CODE: 10454

VALIDATION VERSION: 1

PURCHASE METHOD: 3

DEPARTMENT NUMBER: 421 DOCUMENT IDENTIFIER/COMMON NO.: A0001

MONTH (c): 04 QUARTER (c): 3

LAST DIGIT OF FISCAL YEAR (c): 3

Select CONTROL POINT ACTIVITY NUMBER:

Control Point Activity File Inquiry

Procurement and Accounting Transactions Inquiry

Select Audit Reports Menu Option:

### Supplementary Options on the FCP/BOC/SA Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Options in the BOC Management Menu

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Budget Utilities Menu

Edit Budget Categories

FMS Exception Transaction Report

Repost FMS Exceptions

Clear FMS Add/Edit BOC

Exception File Entries

Clear Program Lock

Dictionary Management Menu...

Create New Code Sheet

Display Control Point Official's Balance

FCP/BOC/SA Management Menu...

Recalculate All Fund Control Point Balances

Transaction Report – eCMS/IFCAP

Select Budget Utilities Menu Option: FCP/BOC/SA Management Menu

BOC Management Menu...

Cost Center Management Menu...

Fund Control Point Management Menu...

Select FCP/BOC/SA Management Menu Option: BOC Management Menu

Add/Edit BOC

Deactivate BOC

Reactivate BOC

BOC Listing

Select BOC Management Menu Option:

#### Add/Edit BOC

#### Introduction

This option allows you to add a new budget object code or change the name of an existing budget object code. Whenever the program offices in VA Central Office change the budget object codes that you use, you will have to use this option to make the necessary changes to the Budget Object Code File. You can use this option to create new entries or to change the name or number of existing entries.

#### Select Budget Object Code (BOC)

Enter a budget object code name. If you do not know the budget object code name, type three question marks at the Select Budget Object Code Name: prompt and IFCAP will list the available BOCs. You may also change the name and the description (but not the number) or the BOC using this option. You may add or edit another BOC at the Select next BOC: prompt or press the Enter key to return to the BOC Management Menu.

Select BUDGET OBJECT CODE NAME: ???

CHOOSE FROM:

1001 1001 Administrative Personnel not Otherwise Classified

1002 1002 Clerical Personnel

1008 1008 Wage Rate Employees

1009 1009 Purchase and Hire

1014 1014 Respiratory Therapist

Select BUDGET OBJECT CODE NAME: 1007 Computer Systems Analyst, Programmers, Keypunch

& Operators

Are you sure that you wish to deactivate this Budget Object Code? YES// (YES)

--Budget Object Code has been deactivated

You may enter a new BUDGET OBJECT CODE, if you wish Enter the 4-digit BOC number,

a space and the BOC name. Answer must be 3-79 characters in length

Select next BOC:

Add/Edit BOC

Deactivate BOC

Reactivate BOC

BOC Listing

Select BOC Management Menu Option:

#### Deactivate BOC

#### Introduction

This option deactivates a budget object code, making it unavailable for assignment to a Cost Center.

#### Select BOC

Enter a budget object code name at the Select Budget Object Code Name: prompt. If you do not know the budget object code name, type three question marks at the prompt and IFCAP will list the available BOCs. You may either enter another budget object code to be deactivated at the Select Next BOC: prompt or press the Enter key to return to the BOC Management Menu.

Select BUDGET OBJECT CODE NAME: ???

CHOOSE FROM:

1001 1001 Administrative Personnel not Otherwise Classified

1002 1002 Clerical Personnel

1001 1001 Administrative Personnel not Otherwise Classified

1002 1002 Clerical Personnel

1007 1007 Computer Systems Analyst, Programmers, Keypunch & Operators

1008 1008 Wage Rate Employees

1009 1009 Purchase and Hire

1014 1014 Respiratory Therapist

Select BUDGET OBJECT CODE NAME: 1007 Computer Systems Analyst, Programmers, Keypunch

& Operators

Are you sure that you wish to deactivate this Budget Object Code? YES// (YES)

--Budget Object Code has been deactivated

Select Next BOC:

Add/Edit BOC

Deactivate BOC

Reactivate BOC

BOC Listing

Select BOC Management Menu Option:

#### Reactivate BOC

#### Introduction

Use this option to make a budget object code available for use that was previously deactivated. This option makes a budget object code available for assignment to a Cost Center.

#### Select BOC

Enter a budget object code name at the Select Budget Object Code Name: prompt. If you do not know the budget object code name, type three question marks at the prompt and IFCAP will list the available BOCs. You may either enter another BOC to be reactivated at the Select Next BOC: prompt or press the Enter key to return to the BOC Management Menu.

Select BUDGET OBJECT CODE NAME: ???

CHOOSE FROM:

1007 1007 Computer Systems Analyst, Programmers, Keypunch & Operators

1036 1036 Radiology Technician

1050 1050 Trainees-Administrative Training Program

1060 1060 Professional Nurses

1067 1067 LVN

1069 1069 WOC Employees Receiving QS&L

1070 1070 Expanded Dental Auxiliaries

Select BUDGET OBJECT CODE NAME: 1007 Computer Systems Analyst, Programmers, Keypunch

& Operators

Are you sure that you wish to reactivate this Budget Object Code? YES// (YES)

--Budget Object Code has been reactivated

Select Next BUDGET OBJECT CODE:

Add/Edit BOC

Deactivate BOC

Reactivate BOC

BOC Listing

Select BOC Management Menu Option:

#### BOC Listing

#### Introduction

This option will print a list of the budget object codes on your system, showing you their descriptions, if any, and whether or not they have been deactivated.

#### Compile/Print List

Enter the first BOC number you want to see on the list at the Start with Number: First// prompt or press the Enter key to list all of the BOCs. The list will show the BOC number, name and description, and whether or not the BOC has been deactivated. After creating the list, IFCAP will return to the BOC Management Menu.

START WITH NUMBER: FIRST//

DEVICE: LAT RIGHT MARGIN: 80//

BUDGET OBJECT CODE LISTING (\*\*=DEACTIVATED) JUN 13,1994 11:01 PAGE 1

--------------------------------------------------------------------------------------

1001 Administrative Personnel not Otherwise Classified

Excludes secretaries and all other clerical type employees.

1002 Clerical Personnel

Includes secretaries and clerk typists file clerks and other

clerical type personnel.

1007 Computer Systems Analyst, Programmers, Keypunch & Operators

Includes computer systems analysts, programmers, and keypunch.

operators and computer operators.

1008 Wage Rate Employees

1009 Purchase and Hire

1014 Respiratory Therapist

BUDGET OBJECT CODE LISTING (\*\*=DEACTIVATED) JUN 13,1994 11:01 PAGE 2

-------------------------------------------------------------------------------------------------

1015 Physical Therapist

1016 Occupational Therapist

1017 Other Therapists

Includes corrective, manual arts, recreation and educational therapists.

1018 Dietitian

1019 Dietetic Technician

1020 Social Worker

1021 Social Worker Aides and Technicians

1022 Radiology Technologist

Includes Diagnostic and Therapeutic Radiology

Add/Edit BOC

Deactivate BOC

Reactivate BOC

BOC Listing

Select BOC Management Menu Option:

### Options in the Cost Center Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Add/Edit Cost Center

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Budget Utilities Menu

Add/Edit Cost Center

Deactivate Cost Center

Reactivate Cost Center

Cost Center Listing List

Cost Centers with Associated BOC

Select Cost Center Management Menu Option:

#### Introduction

This option allows you to add a new Cost Center or edit the name of an existing Cost Center. You can also use this option to edit the list of allowable budget object codes for a Cost Center.

#### Select Cost Center

Enter a cost center name or number. You may enter a new one if you wish. You may also type three question marks at the prompt to see a list of available cost centers you can edit. If you are editing a cost center, you can change the name and description of the cost center, but not the number. You can also edit the list of valid budget object codes for the cost center.

> Select COST CENTER NAME: ???

> CHOOSE FROM:

> 100000 100000 General Admin-Central Off Staff (Excl of Oper Depts) –

> Summary of Accts

> 110100 110100 Office of the Secretary

> 110200 110200 Off of Assoc Deputy Admstr for Congressional & Intergovt'l

> Affairs

> 110300 110300 Board of Contract Appeals

> 110400 110400 Office of Equal Opportunity

> 110500 110500 Board of Veterans Appeals

> You may enter a new COST CENTER, if you wish Enter the 6 digit cost center

> number, a space and the cost center

> name. Answer must be 4-79 characters in length (no decimal allowed)

> Select COST CENTER NAME: 110500 Board of Veterans Appeals

> Do you need to edit the Cost Center Name? NO// Y (YES)

> You may edit only the NAME of this Cost Center, you may NOT change the number

> Do you REALLY wish to change the NAME of this Cost Center? YES// (YES)

> Cost Center NAME: Board of Veterans Appeals// Replace

> DESCRIPTION:

> 1\>Includes Chairman, all Board of Veterans Appeals Board Sections, Medical

> 2\>Advisors, Administrative Services, and related costs.

> EDIT Option:

> Do you wish to edit the BOC list for this Cost Center? YES// (YES)

> Do you want me to add or delete ALL BOCs to this cost center before

> you begin editing the budget object code list? NO// (NO)

> Select BOC: 3121 Office Equipment//

> Select next COST CENTER:

#### Deactivate Cost Center

#### Introduction

Use this option to deactivate a Cost Center. Once the Cost Center has been deactivated it will not be available to any other option in the system.

#### Select Cost Center

Enter a cost center. If you do not know the name of the cost center you want to deactivate, type three question marks at the Select Cost Center Name: prompt and IFCAP will list the available cost centers. You may enter another cost center to deactivate at the Select Next Cost Center: prompt or press the Enter key to return to the Cost Center Management Menu.

Select COST CENTER NAME: ???

CHOOSE FROM:

100000 100000 General Admin-Central Off Staff (Excl of Oper Depts) -

Summary of Accts

110100 110100 Office of the Secretary

110200 110200 Off of Assoc Deputy Admstr for Congressional & Intergovt'l

Affairs

110300 110300 Board of Contract Appeals

110500 110500 Board of Veterans Appeals

111600 111600 Office of Public and Consumer Affairs

Select COST CENTER NAME: 110500 Board of Veterans Appeals

Are you sure that you wish to deactivate this Cost Center? YES// (YES)

--Cost Center has been

deactivated

Select Next COST CENTER:

Add/Edit Cost Center

Deactivate Cost Center

Reactivate Cost Center

Cost Center Listing List

Cost Centers with Associated BOC

Select Cost Center Management Menu Option:

#### Reactivate Cost Center

#### Introduction

Using this option makes a Cost Center available for use that was previously deactivated, making it available to the rest of the system.

#### Select Cost Center

Enter a cost center. If you do not know the name of the cost center you want to reactivate, type three question marks at the Select Cost Center Name: prompt and IFCAP will list the available cost centers. You may enter another cost center to reactivate at the Select Next Cost Center: prompt or press the Enter key to return to the Cost Center Management Menu.

Select COST CENTER NAME: ???

CHOOSE FROM:

110400 110400 Office of Equal Opportunity

110500 110500 Board of Veterans Appeals

110600 110600 Off of the Assoc Deputy Admstr for Public & Consumer Affairs

110700 110700 Off of the Assoc Deputy Admstr for Info Resources Management

110800 110800 Office of the Associate Deputy Administrator for Logistics

130100 130100 Office of Info Mgmt & Stats

131100 131100 Statistical Policy and Research Service

Select COST CENTER NAME: 130100 Office of Info Mgmt & Stats

Are you sure that you wish to reactivate this Cost Center? YES// Y (YES)

--Cost Center has been reactivated

Select Next COST CENTER:

Add/Edit Cost Center

Deactivate Cost Center

Reactivate Cost Center

Cost Center Listing

List Cost Centers with Associated BOC

#### Cost Center Listing

#### Introduction

Use this option to print a list of Cost Center numbers and names, including the long description. This option prints a very long listing of the Cost Centers. You can choose to print just a range of numbers, which is more practical. Note that this listing also shows the deactivated Cost Centers.

#### Compile/Print List

Enter the first cost center you want to see on the list at the Start With Number: First// prompt or press the Enter key to list all of the cost centers. The list will show the cost center number, name and description, and whether or not the cost center has been deactivated. After creating the list, IFCAP will return to the Cost Center Management Menu.

START WITH COST CENTER NUMBER: FIRST//

DEVICE: LAT RIGHT MARGIN: 80//

COST CENTER LISTING (\*\*=DEACTIVATED) JUN 13,1994 13:18 PAGE 1

--------------------------------------------------------------------------------------

100000 General Admin-Central Off Staff (Excl of Oper Depts) - Summary of Accts

110100 Office of the Secretary

Includes Secretary, Special Assistants, Deputy Secretary, Directors, Special Projects Staff, Management Control Staff, Executive Secretariat and immediate office personnel and related costs. NOTE; use of budget object code 2577 is restricted to cost applicable to limitation .022 "Official Representation Expense".

110200 Off of Assoc Deputy Admstr for Congressional & Intergovt'l Affairs

Includes Associate Deputy Administrator Staff, Congressional Affairs Staff, Intergovernmental Affairs Staff, immediate office

personnel and related costs.

Add/Edit Cost Center

Deactivate Cost Center

Reactivate Cost Center

Cost Center Listing

List Cost Centers with Associated BOC

Select Cost Center Management Menu Option:

#### List Cost Centers with Associated BOC

#### Introduction

This listing is similar to the cost center listing, but includes all the associated budget object codes. The report generated by this option can be very long unless you limit the report to a range of cost centers.

#### Compile/Print List

Enter the first cost center you want to see on the list at the Start with Number: First// prompt or press the Enter key to list all of the cost centers. The list will show the cost center number, name and description, and its associated budget object codes. After creating the list, IFCAP will return to the Cost Center Management Menu.

START WITH COST CENTER NUMBER: FIRST//

DEVICE: LAT RIGHT MARGIN: 80//

COST CENTER LIST-WITH ASSOC. BOC JUN 13,1994 13:34 PAGE 1

BOC

-----------------------------------------------------------------------------------

100000 General Admin-Central Off Staff (Excl of Oper Depts) - Summary of Accts

1104 Overtime Pay

110100 Office of the Secretary

Includes Secretary, Special Assistants, Deputy Secretary,

Directors, Special Projects Staff, Management Control Staff,

Executive Secretariat and immediate office personnel and related

costs. NOTE: use of budget object code 2577 is restricted to cost

applicable to limitation .022 "Official Representation Expense".

1090 Administrative and Clerical Personnel Not Otherwise Cla

1091 Federal, Summer Employment Program for Youth-Summer Aids

1092 Stay-In-School Program Part-Time Employment of Needy St

1093 Subsistence & Temp Exp, Real Estate Costs & Misc Exp-PL

1095 Employee Salary Continuation

1096 Computer Sys Analyst, Programmers, Keypunch & Computer

1098 Wage Rate Employees

2101 Permanent Duty Travel

110200 Off of Assoc Deputy Admstr for Congressional & Intergovt'l Affairs

Includes Associate Deputy Administrator Staff, Congressional Affairs Staff, Intergovernmental Affairs Staff, immediate office

personnel and related costs.

1090 Administrative and Clerical Personnel Not Otherwise

Add/Edit Cost Center

Deactivate Cost Center

Reactivate Cost Center

Cost Center Listing

List Cost Centers with Associated BOC

Select Cost Center Management Menu Option:

### Options in the Fund Control Point Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Budget Utilities Menu

Edit Budget Categories

FMS Exception Transaction Report

Repost FMS Exceptions

Clear FMS Exception File Entries

Clear Program Lock

Dictionary Management Menu...

Create New Code Sheet

Display Control Point Official's Balance

FCP/BOC/SA Management Menu...

Recalculate All Fund Control Point Balances

Transaction Report – eCMS/IFCAP

Select Budget Utilities Menu Option: FCP/BOC/SA Management Menu

BOC Management Menu...

Cost Center Management Menu...

Fund Control Point Management Menu...

Select FCP/BOC/SA Management Menu Option: Fund Control Point Management Menu

Add/Edit Control Point

Deactivate a Fund Control Point

Reactivate a Fund Control Point

Place Released Ceiling Transaction in CP File

Display Control Point Committed Transactions

Reset FCP Yearly Accounting Element & ACT Code

#### Place Released Ceiling Transaction in Control Point File

#### Introduction

Use this option when you automate Control Points at your facility. In most cases, you will be planning the implementation of IFCAP at the Control Point level in stages. Use this option after you have Released all Funding (Ceiling) Transactions for your facility and a Control Point is just now being automated, in other words, the funds have already been released automatically. You cannot re-release the ceiling, but you can use this option to enter the ceiling amount into the Control Point Official's balance. This option will not place an entry onto the budget balance for the Control Point; because this entry was made when the original transaction was posted. Fiscal service uses this option to enter a ceiling transaction into a Control Point file. Only use this option when a Control Point is being automated after funds have already been released through the fund distribution option.

#### Ceiling Transaction Setup

Enter a Station number, a fiscal year, and a fiscal quarter. Enter a Control Point. If you do not know the name of the Control Point, enter three question marks at the Select Control Point: prompt. IFCAP will assign a transaction number to the transaction you are creating. You may assign a Sort Group if you like. Enter the amount that you want to enter into the Control Point balance at the Ceiling \$ Amount: prompt. Enter the date that you want IFCAP to allocate the funds at the Date Allocated: prompt. Press the Enter key at the Reference Number: prompt. Add comments if you like. You may enter another ceiling transaction or enter “N” at the Would You Like to Enter Another Ceiling Transaction?: prompt to return to the Fund Control Point Management Menu.

> Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

> Select FISCAL YEAR ('^' to EXIT): 94//

> Select QUARTER: 3//

> Select CONTROL POINT: 101 LAB TESTING 101// ???

> CHOOSE FROM:

> 73 073 ENGINEERING

> 101 101 LAB TESTING 101

> 102 102 LAB TESTING 102

> 103 103 LAB TESTING 103

> 104 104 LAB TESTING 104

> 105 105 LAB TESTING 105

> Select CONTROL POINT: 101 LAB TESTING 101//

> ...OK? Yes// (Yes)

> This transaction is assigned transaction number: 688-94-3-101-0267

> SORT GROUP:

> DATE ALLOCATED: T+1 (JUN 14, 1994)

> REFERENCE NUMBER:

> CEILING \$ AMOUNT: 10000 \$ 10000.00

> COMMENTS:

> 1\>

> Would you like to enter another Ceiling transaction? YES// n (NO)

> Add/Edit Control Point

> Deactivate a Fund Control Point

> Reactivate a Fund Control Point

> Place Released Ceiling Transaction in CP File

> Display Control Point Committed Transactions

> Reset FCP Yearly Accounting Element & ACT Code

> Select Fund Control Point Management Menu Option:

#### Deactivate a Fund Control Point

#### Introduction

Use this option to mark a Fund Control Point as "INACTIVE". This option is used when you want to deactivate, either temporarily or permanently, a Control Point. This will make the Control Point unavailable to IFCAP users.

#### Deactivate the Control Point

Enter a station number and the Control Point you want to deactivate. Enter I at the Active/Inactive Control Point: prompt. Press the Enter key at the Select Fund Control Point: prompt to return to the Fund Control Point Management Menu.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select Fund Control Point: 61

Active/Inactive Control Point: ACTIVE// INACTIVE

Select Fund Control Point:

Add/Edit Control Point

Deactivate a Fund Control Point

Reactivate a Fund Control Point

Place Released Ceiling Transaction in CP File

Display Control Point Committed Transactions

Reset FCP Yearly Accounting Element & ACT Code

Select Fund Control Point Management Menu Option:

#### Reactivate a Fund Control Point

#### Introduction

Use this option to put a deactivated Control Point back in service.

#### Reactivate the Control Point

Enter a station number and the Control Point you want to deactivate. Enter A at the Active/Inactive Control Point: prompt. Press the Enter key at the Select Fund Control Point: prompt to return to the Fund Control Point Management Menu.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select Fund Control Point: ???

CHOOSE FROM:

9 009 TRAINEE SALARIES

61 061 TEST 061

521 521 RESEARCH

777 777 DO NOT USE

891 891 ISC

949 949 MCCR TRAVEL

1201 1201 RESIDENT ENGINEER

1601 1601 CANTEEN

Select Fund Control Point: 949 MCCR TRAVEL

Active/Inactive Control Point: INACTIVE// ACTIVE

Select Fund Control Point:

Add/Edit Control Point

Deactivate a Fund Control Point

Reactivate a Fund Control Point

Place Released Ceiling Transaction in CP File

Display Control Point Committed Transactions

Reset FCP Yearly Accounting Element & ACT Code

Select Fund Control Point Management Menu Option:

#### Display Control Point Committed Transactions

#### Introduction

This report will generate a display of committed transactions for one or more Control Points that you select.

#### Compile/Print List

Enter the first Control Point you want to see on the list at the Start with Control Point: First// prompt or press the Enter key to list all of the Control Points. Enter the first date of committed transactions you want to see on the list at the Start with Date Committed: First// prompt or press the Enter key to see all of the transactions. The list will show the Control Point number and name and its associated transactions. After creating the list, IFCAP will return to the Fund Control Point Management Menu.

This report will generate a display of committed

transactions for one or more control points which you select

Select FISCAL YEAR: 00//

Select QUARTER: 4//

Select CONTROL POINT: 101 LAB TESTING 101//

...OK? Yes// (Yes)Enter control point at end of range.

(For a range of 1-n, enter n. For one control point, enter that control point.)

Select CONTROL POINT: 990 SUPPLY FUND 4537B 90 0100 016144100

DEVICE: LAT RIGHT MARGIN: 80//

COMMITTED TRANSACTION LISTING JUN 13,1994 14:15 PAGE 1

COMMITTED

TRANSACTION (ESTIMATED)

TRANSACTION NUMBER TYPE COST STATUS

--------------------------------------------------------------------------------

CONTROL POINT: 001 SUPPLY

DATE COMMITTED: NOV 18,1993

688-94-1-001-0005

PPM Clerk OBLIGATION 12.00 Assigned to

DATE COMMITTED: JAN 6,1994

688-94-2-001-0007 OBLIGATION 23.84

688-94-2-001-0006

Accountable Officer Si OBLIGATION 1.00 Pending

CONTROL POINT: 071 CANTEEN

DATE COMMITTED: NOV 18,1993

688-94-1-071-0005

Pending Return of OBLIGATION 10.00 Held in P&C

DATE COMMITTED: DEC 10,1993

688-94-1-071-0005

Pending Return of OBLIGATION 10.00 Held in P&C

DATE COMMITTED: DEC 10,1993

688-94-1-071-0006

Pending Return of OBLIGATION 10.00 Held in P&C

DATE COMMITTED: MAR 1,1994

688-94-4-071-0017 OBLIGATION

688-94-2-071-0011 OBLIGATION 101.00

688-94-2-071-0007 OBLIGATION 100.00

End of report

Add/Edit Control Point Deactivate a Fund Control Point Reactivate a Fund Control Point

Place Released Ceiling Transaction in CP File Display Control Point Committed Transactions Reset FCP Yearly Accounting Element & ACT Code

Select Fund Control Point Management Menu Option:

#### Reset FCP Yearly Accounting Elements

#### Introduction

Use this option to reset the FCP yearly accounting elements to the current Fund Control Point accounting elements.

#### Select Control Point

IFCAP will display the station number and ask you to enter a Fund Control Point. Enter the fiscal year for which you want to change the codes. IFCAP will display the CURRENT codes for the Fund Control Point (as defined in the Add/Edit Control Point option) on the left side of the screen. The existing elements for the fiscal year you selected are displayed on the right side of the screen. If you wish to Reset the values displayed on the right side of the screen to match the values displayed on the left side – Enter “Y” at the Reset the fiscal year 99 Sub allowance Account?: prompt. If you want this data to be filed into the file - Enter “Y” at the Ready to File?: prompt to transmit the reset command. Enter another Control Point at the Select Control Point: prompt or press the Enter key to return to the Fund Control Point Management Menu.

STATION: 688

Select Fund Control Point Management Menu Option: RESet FCP Yearly Accounting Element & ACT Code

STATION: 658

--------------------------------------------------------------------------------------

Select Fund Control Point: 110 FIS STATION TRVL 0160A7 10 0100 010042116

For Budget Fiscal Year: 1999

CURRENT FCP ACCOUNTING ELEMENTS FISCAL YEAR FCP ACCOUNTING ELEMENTS

BBFY: 1998 FISCAL

YEAR: 99

FUND: 0160A1

FUND: 0160A1

APPROPRI: 36_0160

APPROPRI: 36_0160

A/O: 10

A/O: 10

PROGRAM: 0100

PROGRAM: 0100

FCP/PRJ: 010042100

FCP/PRJ: 010042116

OBJECT CLASS:

OBJECT CLASS:

JOB:

JOB:

Reset the fiscal year 99 Suballowance Account? NO// YES

Ready to File? NO// YES

### Options on Budget Utilities Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

Select Funds Distribution Program Menu Option: Budget Utilities Menu

Edit Budget Categories

FMS Exception Transaction Report

Repost FMS Exceptions

Clear FMS Exception File Entries

Clear Program Lock

Dictionary Management Menu...

Create New Code Sheet

Display Control Point Official's Balance

FCP/BOC/SA Management Menu...

Recalculate All Fund Control Point Balances

Transaction Report – eCMS/IFCAP

Select Budget Utilities Menu Option

#### Edit Budget Categories

#### Introduction

This option allows you to edit the RD 285 (budget) categories used on the Budget Distribution reports. You can change an existing category, add to the selections, or delete an entry that is no longer needed.

#### Budget Category

Enter the name of the budget category you wish to edit. If you do not know the name of the budget category, enter three question marks at the Select Budget Distribution Codes Name: prompt and IFCAP will list the available budget categories. You may change the name of the budget, its abbreviation, and its sort order. The sort order is the order in which the budget categories will appear in the budget distribution reports.

Select BUDGET DISTRIBUTION CODES NAME: ???

CHOOSE FROM:

1 ALL OTHER

2 RECURRING PERSONAL SERVICES

3 NR ALL OTHER

4 NR .23

5 19 REPL EQUIP

You may enter new BUDGET DISTRIBUTION CODES, if you wish

This is the distribution code number.

Select BUDGET DISTRIBUTION CODES NAME: 2 RECURRING PERSONAL SERVICES

NAME: RECURRING PERSONAL SERVICES//

ABBREVIATION: RPS//

SORT ORDER: 1//

#### Display Control Point Official's Balance

#### Introduction

This option allows you to display the unobligated balance for a selected Fund Control Point. The unobligated balance is the available balance available to the Control Point Official.

#### Compile/Print Report

You can create a report for all Control Points, or for a single Control Point that you define. Enter a Station Number, a fiscal year, and a fiscal quarter. Enter a Control Point. If you do not know the name of the Control Point you want to display, enter three question marks at the Select Control Point: prompt and IFCAP will list the available Control Points. IFCAP will list every 2237 for the Control Point and every purchase order transaction that is not assigned to a 2237 and provide summary totals for the Control Point at the end of the report. Enter a Station Number at the Select Station Number: prompt to create another report or type a caret(^) and press the Enter key to return to the Budget Utilities Menu.

Do you wish a report for ALL Control Points? NO// (NO)

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 94//

Select QUARTER: 3//

Select CONTROL POINT: 101 LAB TESTING 101

...OK? Yes// (Yes)

Would you like a summary report (bottom line balances only)? YES// n (NO)

DEVICE: LAT

CONTROL POINT BALANCE - 688-94-3-101- JUN 13,1994@14:40:35 PAGE 1

FISCAL

FYQSeq# TXN OBL \# AP/OB DT COMM \$AMT CP \$BAL OBL \$AMT UNOBL \$BAL

----------------------------------------------------------------------------------003

CEI 500000.00 500000.00 500000.00 500000.00

0046 CEI 25000.00 525000.00 25000.00 525000.00

0138 OBL C45097 APR 1,1994 500.00 524500.00 500.00 524500.00

0141 OBL C45107 APR 8,1994 5000.00 519500.00 5000.00 519500.00

0142 ADJ C45107 APR 8,1994 -2000.00 521500.00 -2000.00 521500.00

0144 OBL C45108 APR 8,1994 10.00 521490.00 10.00 521490.00

\_\_\_\_\_\_\_\_\_\_\_PO TRANSACTIONS WITHOUT 2237\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PO/ PO COMMITTED OBL/CEIL UNOBLIG

OBL# DATE (EST) COST CP BALANCE \$ AMOUNT BALANCE

===============================================================================-

688-A40860 114.50 1524161.45 114.50 1524870.03

688-A40858 588.00 1523573.45 588.00 1524282.03

688-A40857 490.00 1523083.45 490.00 1523792.03

688-A40856 637.00 1522446.45 637.00 1523155.03

PO transaction (no 2237) total for this quarter: \$21918.90

FMS transaction total for this quarter: \$0.00

===============================================================================-

TOTAL COMMITTED, NOT OBLIGATED: \$708.58

Total uncommitted balance from current and prior quarters: \$742680.10

Select STATION NUMBER ('^' TO EXIT): 688// ^

Edit Budget Categories

FMS Exception Transaction Report

Repost FMS Exceptions

Clear FMS Exception File Entries

Clear Program Lock

Dictionary Management Menu...

Create New Code Sheet

Display Control Point Official's Balance

FCP/BOC/SA Management Menu...

Display Control Point Official's Balance

FCP/BOC/SA Management Menu...

Recalculate All Fund Control Point Balances

Transaction Report – eCMS/IFCAP

Select Budget Utilities Menu Option:

#### Introduction

Use this option to recalculate all Fund Control Balances for the Control Point Activity user. This option is included in your menu to update balances for all automated Fund Control Points. This recalculation is necessary when the computer "crashes" (loses power). The transactions being processed when a "crash" occur do not update the Control Point records. Therefore, you may need to use this option to recalculate the Fund Control Point balances in Fiscal.

#### Recalculate

IFCAP will recalculate the Control Point Balances for all of the stations in your system. After recalculating the balances for all of the Stations in your system, IFCAP will return to the Budget Utilities Menu.

> Select FISCAL YEAR: 94//

> Recalculate all stations/control points balances for fiscal year: 00 Select QUARTER: 3//

> Submit RECALCULATE ALL CONTROL POINT BALANCES to the TASK MANAGER? YES//

> Requested Start Time: NOW// (JUL 20, 1994@18:39:06)

> RECALCULATE ALL CONTROL POINT BALANCES HAS TASK NUMBER 223756

#### Clear Program Lock

#### Introduction

This option allows the user to clear a program lock and continue processing. This option clears up a lock that has been placed on batch transmission or on releasing the budget figures for a station.

This can occur when someone else is using the option and the system will not allow a second person to perform the same function, or when a system error or power problem interrupts a function. Never proceed with further processing after a lock until you have used this option to clear the lock.

### Supplementary Options - FMS Documents Inquiry/Error Process Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: FMS Documents Inquiry/Error Process

SOAR Enter/Edit Date When SOs become Ars

FMS Documents Inquiry

Rejected FMS Document Process

#### Enter/Edit Date When SOs become ARs

#### Introduction

At the close of each Fiscal Year the FMS system runs a process which takes all open Accrued Services obligations and converts them from transaction type SO to transaction type AR. Any future adjustments to these obligations must refer to them as ARs not SOs. In order to ensure that the IFCAP system knows when to send a transaction as an AR (i.e., when the document is accrued in FMS), an option is used to enter the date that FMS will run the conversion process. Starting the next day, a prior year document will be sent to Austin referencing an AR instead of an SO. This date field must be populated at the close of each Fiscal Year with the appropriate date provided by the FMS office.

#### Enter the Date

Enter the date on which FMS will accrue their prior year documents.

(8/25/2000 – 8/25/2001): October 11, 1998// 100600 October 6, 2000

IFCAP will allow SO’s to be sent to Austin as AR’s starting on 10/7/00.

Is this correct?? NO// Yes

#### Transactions Generated to FMS

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AMENDMENT TYPE</p>
</blockquote></th>
<th><blockquote>
<p>SO Format Selected</p>
</blockquote></th>
<th><blockquote>
<p>AR Format Selected</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cancel</p>
</blockquote></td>
<td><blockquote>
<p>SO.X to decrease $</p>
</blockquote></td>
<td><blockquote>
<p>AR.X to cancel accrual</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SO.X to cancel PO</p>
</blockquote></td>
<td><blockquote>
<p>SO.X to decrease $</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>SO.X to cancel PO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Fund Control Point or Vendor Edit</p>
</blockquote></td>
<td><blockquote>
<p>SO.X to decrease $</p>
</blockquote></td>
<td><blockquote>
<p>AR.X to cancel accrual</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SO.X to cancel PO</p>
</blockquote></td>
<td><blockquote>
<p>SO.X to decrease $</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>SO.E to re-establish PO</p>
</blockquote></td>
<td><blockquote>
<p>SO.X to cancel PO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>SO.E to re-establish PO</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Change PO Number</p>
</blockquote></td>
<td><blockquote>
<p>SO.X to decrease $</p>
</blockquote></td>
<td><blockquote>
<p>AR.X to cancel accrual</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>SO.X to cancel PO</p>
</blockquote></td>
<td><blockquote>
<p>SO.X to decrease $</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SO.E to establish new PO</p>
</blockquote></td>
<td><blockquote>
<p>SO.X to cancel PO</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>SO.E to establish new PO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

When prior year amendments or adjustments to prior year 1358s are processed in IFCAP, the transactions listed under the SO Format Selected column will be generated if the user selected the SO format; the transactions under the AR Format Selected column will be generated if the user specifies AR format. If the document being processed is not prior to the year, the user will not be prompted for format, and the system will generate the documents associated with the SO format.

Rejected AR documents may be viewed and/or rebuilt and transmitted through options on the Accounting Technician Menu.

> Document Processing

> FMS Rejected Obligation Document Processing

> FMS Inquiry Rejected Obligation Documents

> FMS Rebuild/Transmit Rejected Obligation Documents

#### FMS Documents Inquiry

#### Introduction

Use this option to display the status of both manual and IFCAP created FMS documents.

#### Select Transaction Type and Budget Document ID

Enter a station number. Enter the type of transaction you want to view or print at the Select Transaction Type: prompt. Enter the identification number of the document at the FMS Budget Document ID: prompt. If you do not know the number, enter three question marks and IFCAP will list the available identification numbers.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: SA Suballowance

FMS Budget Document ID: ???

CHOOSE FROM:

SA-688FC0059

SA-688FC0060

SA-688FC0061

FMS Budget Document ID: SA-688FC0060

#### Interpreting the Data

IFCAP will list the document identification number, its description, its status, when it was created, and other descriptive information about the document. Enter another ID number at the FMS Budget Document ID: prompt or press the Enter key to quit or enter another transaction type. Enter a transaction type at the Select Transaction Type: prompt or press the Enter key to return to the FMS Documents Inquiry/Error Process menu.

FMS Document: SA-688FC0060

Description: AUTO FMS DOC 'SA'

Status: TRANSMITTED

Created: MAR 15, 1994@08:24:49

FMS Doc Date: //1700

Doc Year:

Quarter:

Station \#:

FCP \#:

\$Amount: 0.00

BBFY:

FMS Action:

FMS Budget Document ID:

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type:

SOAR Enter/Edit Date When SOs become ARs

FMS Documents Inquiry Rejected FMS Document Process

Select FMS Documents Inquiry/Error Process Option:

#### Rejected FMS Document Process

#### Introduction

This option provides the user with the ability to view, edit and retransmit funding documents that were rejected by FMS.

#### File Regenerated Document

Enter a station number. Enter the type of transaction you want to view or print at the Select Transaction Type: prompt. Enter the identification number of the document at the FMS Budget Document ID: prompt. If you do not know the number, enter three question marks and IFCAP will list the available identification numbers.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: SA Suballowance

FMS Rejected Budget Document ID: ???

CHOOSE FROM:

SA-688FC0059

SA-688FC0060

SA-688FC0061

FMS Rejected Budget Document ID: SA-688FC0061

#### Interpreting the Data

IFCAP will list the document identification number, its description, its status, when it was created, and other descriptive information about the document. Enter the date that you want to assign to the change at the FMS Transaction Date: prompt. Enter “Y” at the Ready to File Regenerated FMS Document?: to file the regenerated FMS document. Enter another ID number at the FMS Budget Document ID: prompt or press the Enter key to quit or enter another transaction type. Enter a transaction type at the Select Transaction Type: prompt or press the Enter key to return to the FMS Documents Inquiry/Error Process menu.

FMS Document: SA-688FC0061

Description: AUTO FMS DOC 'SA'

Status: TRANSMITTED

Created: MAR 15, 1994@08:25:22

FMS Doc Date: //1700

Doc Year:

Quarter:

Station \#:

FCP \#:

\$Amount: 0.00

BBFY:

FMS Action:

FMS Transaction Date: July 20, 1994// (JULY 20, 1994)

Accounting Period (MM/YY): JUL 1994// (JUL 1994)

Ready To File Regenerated FMS Document? NO// Y

\<Filed\>

FMS Rejected Budget Document ID:

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type:

SOAR Enter/Edit Date When SOs become ARs

FMS Documents Inquiry

Rejected FMS Document Process

Select FMS Documents Inquiry/Error Process Option:

### Supplementary Options in the Dictionary Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Budget Utilities Menu

Edit Budget Categories

FMS Exception Transaction Report

Repost FMS Exceptions

Clear Program Lock

Dictionary Management Menu...

Display Control Point Official's Balance

FCP/CC/BOC Management Menu...

Recalculate All Fund Control Point Balances

Transaction Report – eCMS/IFCAP

Select Budget Utilities Menu Option: Dictionary Management Menu

#### Introduction

This menu allows you to enter/edit/list 'dictionaries' of funds, appropriations, or required fields, or any other dictionaries created at your station.

#### Load Standard Dictionary

#### Introduction

Use this option to load a standard dictionary.

#### Select a Standard Dictionary

At the Select Standard Dictionary: prompt, enter the name of the standard dictionary you want to load. If you do not know the name of the dictionary, enter three question marks and IFCAP will list the available dictionaries.

Select Standard Dictionary: ???

CHOOSE FROM:

DVSN ADMINISTRATION /STAFF OFFICE

JOBT JOB NUMBER

OCLS OBJECT CLASS

PCLS PROGRAM

PGMT FUND CONTROL/PROJECT

RSRC REVENUE SOURCE

SOBJ SUB-OBJECT

SREV SUB-REV SOURCE

Select Standard Dictionary: DVSN ADMINISTRATION /STAFF OFFICE

#### Select Entry

The next prompt will ask you for an entry in the dictionary. Enter three question marks to see a list of the available entries.

Select ADMINISTRATION /STAFF OFFICE: ???

CHOOSE FROM:

10 VETERANS HEALTH ADMINISTRATION

20 VETERANS BENEFITS ADMINISTRATION

40 NATIONAL CEMETERY SYSTEM

90 OFFICE OF ACQUISITION AND MATERIAL MANAGEMENT

02 DISTRICT COUNSEL

04 OFFICE OF FIRM

05 OFFICE OF ACQUISITION AND FACILITIES

08 CONSTRUCTION MANAGEMENT

08A CONSTRUCTION MANAGEMENT

20A VETERANS BENEFITS ADMINISTRATION -LGY

CONV OFFICE OF FIRM

You may enter a new PRCD SD ADMINISTRATIVE OFFICE, if you wish

This field is the code of administrative office.

Select ADMINISTRATION /STAFF OFFICE: 40

#### Edit Entry

You may edit the number code assigned to the entry, the description of the dictionary, and the status of the entry. You may enter another entry or press the Enter key to return to the Dictionary Management Menu.

> **NOTE:** Some users will see a "Fix Value:" prompt after the Status: prompt. This prompt is for users that have access to IFCAP code. This prompt represents IFCAP code assigned to the entry. Do not enter anything at this prompt unless instructed to do so by the IFCAP development staff or IRM Service.

CODE: 40//

DESCRIPTION: NATIONAL CEMETERY SYSTEM Replace

STATUS: A// ???

This field is the status of the entry in file.

CHOOSE FROM:

A ACTIVE

I INACTIVE

O OBSOLETE

STATUS: A//

FIX VALUE: 40//

Select ADMINISTRATION /STAFF OFFICE:

#### Standard Dictionary List

#### Introduction

Use this option to list standard dictionary entries.

#### Select Dictionary

Enter a dictionary at the Select Standard Dictionary: prompt. If you do not know the name of the dictionary, enter three question marks at the prompt and IFCAP will list the available dictionaries. Enter an output device at the Device: prompt.

Select Standard Dictionary: ???

CHOOSE FROM:

DDE DOCUMENT DATA ELEMENT

DOCT DOCUMENT TYPE

DVSN ADMINISTRATION /STAFF OFFICE

JOBT JOB NUMBER OCLS OBJECT CLASS

PCLS PROGRAM PGMT FUND CONTROL/PROJECT

RPTG REPORTING CATEGORY

RSRC REVENUE SOURCE

SEC1 FMS DOCUMENT SEC1 CODE

SOBJ SUB-OBJECT

SREV SUB-REV SOURCE

Select Standard Dictionary: DDE DOCUMENT DATA ELEMENT

DEVICE: LAT RIGHT MARGIN: 80//

#### Compile/Print List

IFCAP will list the items in the dictionary you chose. Enter another dictionary name at the Select Standard Dictionary: prompt or press the Enter key to return to the Dictionary Management Menu.

DDE-DOCUMENT DATA ELEMENT List NOV 8,1994 16:25 PAGE 1

Code Description Status Fix Value

--------------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 15%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>A/O</p>
</blockquote></th>
<th><blockquote>
<p>ADMINISTRATION OFFICE</p>
</blockquote></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>AO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BOC</p>
</blockquote></td>
<td><blockquote>
<p>BUDGET OBJECT (SUBACCOUNT)</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>BOC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>COST CENTER</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>CC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FCP/PRJ</p>
</blockquote></td>
<td><blockquote>
<p>FCP/PRJ</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>FCPRJ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JOB</p>
</blockquote></td>
<td><blockquote>
<p>JOB</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>JOB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OC</p>
</blockquote></td>
<td><blockquote>
<p>OBJECT CLASS</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>OC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PGM</p>
</blockquote></td>
<td><blockquote>
<p>PROGRAM</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>PGM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RC</p>
</blockquote></td>
<td><blockquote>
<p>REPORTING CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>RC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RS</p>
</blockquote></td>
<td><blockquote>
<p>REVENUE SOURCE</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>REV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STATION</p>
</blockquote></td>
<td><blockquote>
<p>STATION</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>SITE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SUB BOC</p>
</blockquote></td>
<td><blockquote>
<p>SUB BOC</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>SBOC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SUB CC</p>
</blockquote></td>
<td><blockquote>
<p>SUB-COST CENTER</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>SCC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SUB RS</p>
</blockquote></td>
<td><blockquote>
<p>SUB-REVENUE SOURCE</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>SREV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SUB STATION</p>
</blockquote></td>
<td><blockquote>
<p>SUB-STATION</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>SSITE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Select Standard Dictionary:</p>
<p>Load Standard Dictionary Standard Dictionary List Dictionary List Menu ...</p>
<p>Generate New Fiscal Year Fund/Required Table Fund/Appropriation Enter/Edit</p>
<p>Define Standard Dictionary Fund Enter/Edit</p>
<p>Required Fields Edit</p>
<p>Select Dictionary Management Menu Option:</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Options on the Dictionary List Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Accounting Technician Menu...

Funds Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Funds Distribution & Accounting Menu Option: Funds Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Funds Distribution Program Menu Option: Budget Utilities Menu

Edit Budget Categories

FMS Exception Transaction Report

Repost FMS Exceptions

Clear FMS Exception File Entries

Clear Program Lock

Dictionary Management Menu...

Display Control Point Official's Balance

FCP/CC/BOC Management Menu...

Recalculate All Fund Control Point Balances

Transaction Report – eCMS/IFCAP

Select Budget Utilities Menu Option: Dictionary Management Menu

Load Standard Dictionary

Standard Dictionary List

Dictionary List Menu...

Generate New Fiscal Year Fund/Required Table

Fund/Appropriation Enter/Edit

Define Standard Dictionary

Fund Enter/Edit

Required Fields Edit

Select Dictionary Management Menu Option: Dictionary List Menu

Standard Dictionary List

Fund List

Fund/Appropriation List

Required Fields List

Select Dictionary List Menu Option: Standard Dictionary List

#### Standard Dictionary List (All)

#### Introduction

Use this option to list all defined standard dictionaries.

#### Compile/Print List

Enter an output device at the Device: prompt. IFCAP will create the "IFCAP Standard Dictionary List," which lists the standard dictionaries in the system by code, name, status (Active, Inactive, or Obsolete), Site E/E, and F/V used. After printing the report, IFCAP will return to the Dictionary List Menu.

DEVICE: LAT RIGHT MARGIN: 80//

IFCAP Standard Dictionary List NOV 8,1994 16:36 PAGE 1

SITE FV

CODE NAME STATUS

E/E USED

--------------------------------------------------------------------------------------

DDE DOCUMENT DATA ELEMENT I NO

YES

File Name: PRCD SD DOCUMENT DATA ELEMENT

DOCT DOCUMENT TYPE I NO

YES

File Name: PRCD SD DOCUMENT TYPE

DVSN ADMINISTRATION /STAFF OFFICE A NO YES

NO NO

File Name: PRCD SD OBJECT CLASS

PCLS PROGRAM A

NO YES

File Name: PRCD SD PROGRAM

Select Fund: 1030

1 1030 1994 1994

2 1030 1993 1993

3 1030 1995 1995

CHOOSE 1-3: 3 1995 1995

DEVICE: LAT RIGHT MARGIN: 80//

#### Fund List

#### Introduction

Use this option to list funds.

#### Compile/Print List

Enter an output device at the Device: prompt. IFCAP will create the "IFCAP Fund List," which lists each fund, its description, the BBFY, the EBFY, and the status (Active, Inactive, or Obsolete). After printing the report, IFCAP will return to the Dictionary List Menu.

DEVICE: LAT RIGHT MARGIN: 80//

IFCAP Fund List 8,1994 16:41 PAGE 1

FUND DESCRIPTION BBFY EBFY ST

-------------------------------------------------------------------------------------

1210 'CONSCIENCE' FUND CONTRIBUTION 1993 1993 A

1299 GIFTS TO USA NOT CLASS 1994 1994 A

1411 LOAN INTEREST TO VETS & RESERV 1993 1993 A

1435 PROPRIET INTEREST NOT CLASS 1993 1993 A

1807 REFUND OF ERRONEOUS RECEIPTS 1994 1994 A

2431 CHARGES FOR MEDICAL SERV - VA 1994 1994 A

2466 LOAN GUARANTEE HOUSING 1994 1994 A

2473 CONTRIB FROM MIL PERSONNEL 1994 1994 A

2473.1 MILITARY ED ASST - ARMY 1993 1993 A

2473.2 MILITARY ED ASST - AIR FORCE 1993 1993 A

2473.3 MILITARY ED ASST - NAVY 1993 1993 A

2473.4 MILITARY ED ASST - MARINES 1993 1993 A

2473.5 MILITARY ED ASST - COAST GUARD 1993 1993 A

2473.6 MILITARY ED ASST - NOAA 1993 1993 A

2473.7 MILITARY ED ASST - PUB HEALTH 1994 1994 A

2814 OTHER REPAY - INVEST & RECOVER 1994 1994 A

8180G GENERAL POST FUND - GENERAL 1994 1994 A

8180S GENERAL POST FUND - SPECIFIC 1993 1993 A

8180S A 1995 1995 A

AMAF ASSETS & MISC ACQ FUND 1993 1993 A

AMAF ASSETS & MISC ACCTS FUND 1994 1994 A

Standard Dictionary List

Fund List

Fund/Appropriation List

Required Fields List

Select Dictionary List Menu Option:

### Fund/Appropriation List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

This option lists all entries in file \#420, the Fund Control Point file.

#### Compile/Print List

Enter an output device at the Device: prompt. IFCAP will create the "PRCD Fund/Appropriation Code List," listing each fund, its appropriation, FY pattern, APPR. PAT A/R, and PGM.LIM.ANA ACC. After printing the list, IFCAP will return to the Dictionary List Menu.

DEVICE: LAT RIGHT MARGIN: 80//

PRCD FUND/APPROPRIATION CODE LIST NOV 8,1994 16:52

PAGE 1

PGM.LIM.ANA FY

FUND APPROPRIATION PATTERN APPR. PAT A/R ACC

-------------------------------------------------------------------------------------

11 20X6133 X11

14 36 F3875 X14

15 36 0869 X15

16 36 0891 X16

17 36 1030 X17

18 36 1060 X18

19 36 1099 X19

20 36b1210 X20

21 36 1299 X21

22 36 1411 X22

23 36 1422 X23

24 36 1435 X24 36 1435

Standard Dictionary List

Fund List

Fund/Appropriation List

Required Fields List

Select Dictionary List Menu Option:

#### Required Fields List

#### Introduction

This option allows the user to list the Required Field file settings. These file settings allow IFCAP to determine the information it requires the user to enter to complete each FMS document.

> **NOTE:** This report will be very long if you create it for all funds. Create the report for a single fund if you can.

#### Select Fund

Enter 1 at the Select: prompt if you want to list all required fields for all funds.

> **NOTE:** This report will be very long if you create it for all funds. Create the report for a single fund if you can.

Enter 2 at the prompt to select a single fund. If you enter 2 to list a single fund, IFCAP will ask you for the fund number. Enter an output device at the Device: prompt.

Select one of the following:

1 ALL

2 SELECT FOR FUND

Select: : 2 SELECT FOR FUND

Select Fund: ???

CHOOSE FROM:

1030 1994 1994

1030 1993 1993

1030 1995 1995

1060 1994 1994

1060 1993 1993

1060 1995 1995

1099 1994 1994

1099 1993 1993

1099 1995 1995

1210 1994 1994

1210 1993 1993

1210 1995 1995

1299 1994 1994

1299 1993 1993

1299 1995 1995

1411 1993 1993

1411 1994 1994

1422 1993 1993

1422 1994 1994

1435 1994 1994

1435 1989 1989

Select Fund: 1030

1 1030 1994 1994

2 1030 1993 1993

3 1030 1995 1995

CHOOSE 1-3: 3 1995 1995

DEVICE: LAT RIGHT MARGIN: 80//

#### Compile/Print List

IFCAP will print the "IFCAP Document Required Fields List" report, listing each fund in the report by BBFY, EBFY, FMS document type, the required data element, and if data is required for that data element. Enter another fund at the Select Fund: prompt, ore press the Enter key. Enter 1 or 2 at the Select: prompt to create another report or press the Enter key to return to the Dictionary List Menu.

IFCAP Document Required Fields List NOV 8,1994 17:18 PAGE 1

DATA

FUND BBFY EBFY DOCUMENT TYPE DATA ELEMENT REQUIRED

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1030 1995 1995 ALLOWANCE A/O

NO

1995 1995 FCP/PRJ

NO

1995 1995 OC

NO

1995 1995 PGM

NO

1995 1995 STATION

NO

1995 1995 GL A/O

NO

1995 1995 CC

NO

1995 1995 FCP/PRJ

NO

1995 1995 JOB

NO

1995 1995 RC

NO

1995 1995 STATION

YES

1995 1995 SUB CC

NO

1995 1995 SUB STATION

OPTIONAL

1995 1995 REVENUE A/O

NO

1995 1995 CC

NO

1995 1995 SUB RS

NO

1995 1995 SUB STATION

OPTIONAL

1995 1995 SPENDING A/O

NO

1995 1995 BOC

NO

1995 1995 CC

NO

1995 1995 FCP/PRJ

NO

1995 1995 JOB

NO

1995 1995 RC

NO

1995 1995 RS

YES

1995 1995 STATION

NO

1995 1995 SUB BOC

NO

1995 1995 SUB CC

NO

1995 1995 SUB STATION

OPTIONAL

1995 1995 SUBALLOWANCE A/O

NO

1995 1995 FCP/PRJ

NO

1995 1995 OC

NO

1995 1995 STATION

NO

Select Fund:

Select one of the following:

1 ALL

2 SELECT FOR FUND

Select: :

Standard Dictionary List

Fund List

Fund/Appropriation List

Required Fields List

Select Dictionary List Menu Option:

### Fund/Appropriation Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Use this option to add/edit fund/appropriation information of File (#420.3).

#### Menu Navigation

Select Budget Utilities Menu Option: Dictionary Management Menu

Load Standard Dictionary

Standard Dictionary List

Dictionary List Menu...

Generate New Fiscal Year Fund/Required Table

Fund/Appropriation Enter/Edit

Define Standard Dictionary

Fund Enter/Edit

Required Fields Edit

Select Dictionary Management Menu Option

#### Select/Add Fund

Enter the fund or appropriation code at the Select Appropriation's Fund: prompt. You may enter a new code if you wish. If you do not know the code, enter three question marks and IFCAP will list the available codes.

Select Appropriation's Fund: ???

CHOOSE FROM:

14 36F3875

15 36 0869

16 36 0891

21 36 1299

22 36 1411

50 36\_/\_0161

51 36\_/\_0161.001

52 36 3220

52 36\_/\_0161.007

53 other series

53 36\_/\_0161.001 (016)

54 36X4538

54 36\_/\_0161.007 (016)

You may enter a new PRCD FUND/APPROPRIATION CODE, if you wish

Enter a fund code defined in FUND file.

Select Appropriation's Fund: 36F3875

1 36F3875 36F3875

2 36F3875 36F3875

3 36F3875 36F3875

CHOOSE 1-3: 1

#### Edit Fund or Appropriation

You may enter or edit the fund, the appropriation, the FY pattern, or the appropriation pattern for the Accounts Receivable service. The FY pattern is the fiscal year (FY) associated with the Appropriation Limitation Department (YALD) code. The current FY is indicated with an "X" and the second FY with a "Y". Enter the appropriation pattern for the Accounts receivable service at the Appropriate Pattern for A/R Svc: prompt. Enter another fund or appropriation code at the Select Appropriation's Fund: prompt or press the Enter key to return to the Dictionary Management Menu.

FUND: 3875// APPROPRIATION: 36F3875//

REVOLVING FUND: ???

This is a revolving fund indicator.

Choose from:

Y YES

N NO

REVOLVING FUND:

FY PATTERN: ???

This is the fiscal year (FY) associated with the Appropriation

Limitation Department (YALD) code. The current FY is indicated with

an "x" and the second FY with a "y".

FY PATTERN:

APPROP. PATTERN FOR A/R SVC: 36F3875// ???

This is the appropriation pattern for the Accounts

Receivable Service.

APPROP. PATTERN FOR A/R SVC: 36F3875//

--------------------------------------------------------------------------------------

Select Appropriation's Fund:

Load Standard Dictionary

Standard Dictionary List

Dictionary List Menu...

Generate New Fiscal Year Fund/Required Table

Fund/Appropriation Enter/Edit

Define Standard Dictionary

Fund Enter/Edit

Required Fields Edit

Select Dictionary Management Menu Option:

### Define Standard Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Use this option to define the information in a standard dictionary.

#### Select Standard Dictionary

Enter the dictionary name at the Select Standard Dictionary: prompt. If you do not know the name of the dictionary, enter three question marks and IFCAP will list the available dictionaries.

Select Standard Dictionary: ???

CHOOSE FROM:

DDE DOCUMENT DATA ELEMENT

DOCT DOCUMENT TYPE

DVSN ADMINISTRATION /STAFF OFFICE

JOBT JOB NUMBER

OCLS OBJECT CLASS

PCLS PROGRAM

PGMT FUND CONTROL/PROJECT

RPTG REPORTING CATEGORY

RSRC REVENUE SOURCE

SEC1 FMS DOCUMENT SEC1 CODE

SOBJ SUB-OBJECT

SREV SUB-REV SOURCE

You may enter a new PRCD STANDARD DICTIONARY, if you wish

This is a standard dictionary code.

Select Standard Dictionary: DDE DOCUMENT DATA ELEMENT

#### Edit Dictionary

You may edit the code name assigned to the dictionary, the dictionary name, the status (Active, Inactive, or Obsolete), the file name or number of the dictionary, whether sites are allowed to edit the dictionary, and if a fixed value is used in programming. Enter another dictionary at the Select Standard Dictionary: prompt or press the Enter key to return to the Dictionary Management Menu.

CODE: DDE//

NAME: DOCUMENT DATA ELEMENT Replace STATUS: I//

FILE NAME/NUMBER: PRCD SD DOCUMENT DATA ELEMENT// SITE EDIT ALLOWED: NO//

FIX VALUE USED IN PROGRAMING: YES//

Select Standard Dictionary:

Load Standard Dictionary

Standard Dictionary List

Dictionary List Menu...

Generate New Fiscal Year Fund/Required Table

Fund/Appropriation Enter/Edit

Define Standard Dictionary

Fund Enter/Edit

Required Fields Edit

Select Dictionary Management Menu Option:

### Fund Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Use this option to enter or edit the information in the fund dictionary.

#### Select/Add Fund

Enter the name of the fund at the Select Fund: prompt. You may also enter a new fund, if you wish. If you do not know the name of the fund, enter three question marks and IFCAP will list the available funds.

Select Fund: ???

CHOOSE FROM:

1030 1994 1994

1030 1993 1993

1030 1995 1995

1060 1994 1994

1060 1993 1993

You may enter a new PRCD FUND, if you wish

Answer must be 3-6 characters in length.

Select Fund: 1030

1 1030 1994 1994

2 1030 1993 1993

3 1030 1995 1995

CHOOSE 1-3: 3

FUND: 1030//

#### Edit Fund

You may edit the description of the fund, the beginning and ending fiscal year of the fund, and whether or not programs and subprograms within the same fund can transfer funds. At the Gross/Net prompt, enter G if the fund is not eligible for prompt payment discounts or N if the fund is eligible. You may also change the status of the fund to (A)ctive, (I)nactive, or (O)bsolete. Enter another fund at the Select Fund: prompt or press the Enter key to return to the Dictionary Management Menu.

DESCRIPTION: A// A4

BUDGET FISCAL YEAR BEGIN: 1995//

BUDGET FISCAL YEAR END 1995//

FUND PROGRAM TRANSFER ALLOWED: NO// ???

This will allow program/subprogram transfers within a fund if it is 'yes'.

CHOOSE FROM:

Y YES

N NO

FUND PROGRAM TRANSFER ALLOWED: NO//

GROSS/NET: NET// ???

This is used to store GROSS/NET data.

CHOOSE FROM:

G GROSS

N NET

GROSS/NET: NET//

STATUS: A//

--------------------------------------------------------------------------------------

Select Fund:

Load Standard Dictionary

Standard Dictionary List

Dictionary List Menu...

Generate New Fiscal Year Fund/Required Table

Fund/Appropriation Enter/Edit

Define Standard Dictionary

Fund Enter/Edit

Required Fields Edit

Select Dictionary Management Menu Option:

### Required Fields Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

This option allows the user to edit the Required Field file settings. These file settings allow IFCAP to determine the information it requires the user to enter to complete each FMS document.

#### Select Fund

Enter the fund for which you want to change the required fields at the Select Fund: prompt. If you do not know the fund, enter three question marks and IFCAP will list the available funds.

Enter/Edit Budget/Document Required Data----------

Select Fund: ???

CHOOSE FROM:

1030 1994 1994

1030 1993 1993

1030 1995 1995

1060 1994 1994

1060 1993 1993

1060 1995 1995

1099 1994 1994

Select Fund: 1030

1 1030 1994 1994

2 1030 1993 1993

3 1030 1995 1995

CHOOSE 1-3: 3

#### Select Document Type

Enter the document type that you would like to edit at the Select Document Type: prompt. Enter the data element of the document that you would like to edit at the Select Data Element: prompt.

> Select Document Type: ???

> CHOOSE FROM:

> ALLOWANCE

> GL

> REVENUE

> SPENDING

#### Data Required Setup

Enter whether you want IFCAP to require data for the data element at the Data Required: prompt. Enter another data element that you would like to edit or press the Enter key. Enter another fund or press the Enter key to return to the Dictionary Management Menu.

DATA REQUIRED: NO// ???

This is used to store DATA REQUIRED data.

Choose from:

Y YES

N NO

O OPTIONAL

DATA REQUIRED: NO//

1030 / ALLOWANCE BUDGET----------

Select Data Element:

Enter/Edit Budget/Document Required Data----------

Select Fund:

## Error Messages and their Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### FMS Error Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FMS documents are generated automatically as a result of certain IFCAP processes. For example, creation and generation of ceiling transactions in IFCAP results in Sub- allowance (SA) documents being created and transmitted to FMS. Additionally, when Accounting obligates purchase orders, processes receiving reports or invoices for payment, various types of FMS documents are automatically sent to Austin.

In designing the interface with FMS, IFCAP developers have built-in various edit checks to prevent rejection of FMS documents. An example of such functionality is the Required Fields File, explained earlier in this document, which ensures that all fields required for a given fund and type of FMS document are present on that FMS document before transmitting it to FMS. Even so, it is impossible to prevent every scenario that might cause FMS documents to reject. It is far less likely that the documents that IFCAP creates automatically will be rejected, compared with the documents that users create manually, using the FMS Code Sheet Menu’s Create a Code Sheet option. That is because the automatic document processes contain more built-in protection against document rejection in FMS.

Because rejection of FMS documents is, to some extent, inevitable, there are options to assist users in correction and retransmission of the rejected documents. IFCAP will allow the user to correct the source document, rebuild the document, and retransmit it to FMS.

When FMS rejects a document, it will send an error message containing all relevant FMS error codes to the appropriate recipients the following day. Appropriate recipients are those who are defined in the FCP file (420) to receive FMS notifications for their Fund Control Point (FCP). When the user has corrected a rejected document, the new document will automatically be transmitted to Austin. The only exceptions are the Budget documents (SA, ST, and AT), which must be generated again with the Generate FMS Budget Documents option of the Fund Distribution Module. IFCAP transactions are transmitted to the FMS system in Austin as electronic mail messages. These messages list the FMS document types they contain in the Subj: line of the message.

Outgoing Message to FMS:

> Subj: GCS TRANSACTION FMS:SO, VR, IV \[#21381\] 07 Jul 94 14:55 13 Lines

> From: POSTMASTER in 'IN' basket. Page 1

> -------------------------------------------------------------------------------------

> CTL^IFC^FMS^612^DOC^SO^10 ^612029^612C40011

> ^19940707^135811^001^001^001^~

> BAT^~MO0^612029^~

> DOC^~MO1^SO^612C40011 ^10 ^Y^~

> MO2^94^07^07^^^^^^M^~

> MO3^^^^^^^01^^^^^^^^^^^^^^^^^^^10.00^~ LIN^~MOA^001^^^^94^^0160A1^612^^181000^00^0100201B1^2660^^^^10.00^D^~{

> CTL^IFC^FMS^612^VRQ^ ^ ^

> 61294070010^19940707^135931^001^001^001^~

> VRQ^940707^135930^612^1981^768765498^^AMER SOCIETY OF ADDICTION

> MEDI^5225 WISCO

> NSIN AVENUE N^SUITE 409^WASHINGTON^DC^20015^T^Y^C^N^A^~{

> CTL^IFC^FMS^612^DOC^IV^10 ^ ^612I40004

> ^19940707^140821^001^001^001^~ DOC^~IV1^IV^612I40004 ^10 ^Y^~

> IV2^94^07^07^^^^^E^^^^^^^^^^^^94411020035^340.00^~

> LIN^~IVA^001^189.60^I^^^^^612^^^^^^^^SFCS^^^06^^^94^^0160A1^612^^

> 844100^00^19EA

> 40200^2660^~IVB^01^~ LIN^~IVA^002^150.40^I^^^^^612^^^^^^^^SFPR^^^07^^^94^^0160A1^612^^

> 844100^00^19EA

> 40200^2660^~IVB^01^~{

> Select MESSAGE Action: DELETE (from IN basket)// S

> Select BASKET:

Once the message is received in the FMS system a mail message is returned to the site- confirming acceptance of the message, including the original message number.

Confirmation Message returning from Austin:

> Subj: EDO1381 FMS CONFIRMATION \[#21382\] 07 JUL 94 14:08 CST 2

> Lines

> From: POSTMASTER@FOC-AUSTIN.VA.GOV in 'IN' basket. Page 1

> ----------------------------------------------------------------------------------

> Ref: Your FMS message \#21381 with Austin ID \#38883674, is assigned confirmation number 941881357664928.

> Select MESSAGE Action: DELETE (from IN basket)// S

> Select BASKET:

If a document from IFCAP is rejected in FMS, the FMS mail group will receive an electronic mail message from FMS notifying them of the rejected document. The message will include the FMS error code and a brief description of the error. The action the user must take to correct the rejected document varies according to the type of document that has rejected.

### Stack Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accounting Technician Menu has an option to allow inquiry into all documents and give users the status on each document. The data can be gathered by document type, status or a group of status. The user can see the document with or without code sheet information. For access to this option, contact your IRM service.

Accounting Technician Menu...

Fund Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Fund Distribution & Accounting Menu Option: Accounting Technician Menu

Document Processing Menu...

Accounting Utilities Menu...

Reprint Menu...

Receiving Report Transmission Menu...

Fee Basis - IFCAP Code Sheet Menu...

FMS Code Sheet Menu...

Select Accounting Technician Menu Option: FMS Code Sheet Menu

Code Sheet Edit

Create a Code Sheet

Delete a Code Sheet

Keypunch a Code Sheet

Purge Transmission Records/Code Sheets

Retransmit Stack File Document

Review a Code Sheet

Stack Status Report

Select FMS Code Sheet Menu Option: STACK Status Report

START with TRANSACTION CODE: FIRST// SA

END with TRANSACTION CODE: LAST// ST

Print documents created after DATE: JAN 1,1993// 7/4 (JUL 04,1994)

Select one of the following:

Q QUEUED FOR TRANSMISSION

M MARKED FOR IMMEDIATE TRANSMISSION BY EVENT

T TRANSMITTED

E ERROR DURING TRANSMISSION

A ACCEPTED BY FMS

R REJECTED BY FMS

N TRANSMITTED WITH NO CONFIRMATION MESSAGE RETURNED

Select STATUS(s) to display: REJECTED BY FMS

Select one of the following:

Q QUEUED FOR TRANSMISSION

M MARKED FOR IMMEDIATE TRANSMISSION BY EVENT

T TRANSMITTED

E ERROR DURING TRANSMISSION

A ACCEPTED BY FMS

R REJECTED BY FMS

N TRANSMITTED WITH NO CONFIRMATION MESSAGE RETURNED

Select STATUS(s) to display:

SELECTED STATUS(s) to display:

REJECTED BY FMS

Print DESCRIPTION of event? NO// Y (YES)

Print DOCUMENT code sheets? NO// (NO)

DEVICE: HOME// LAT

\<\*\> please wait \<\*\>

GCS STACK FILE STATUS REPORT JUL 08, 1994@11:40:51 PAGE 1

TC-TRAN CODE -BATNUM DATE@TIME CREATED STATUS

-------------------------------------------------------------------------------------

SO-612A40024 JUL 05, 1994@12:18:59 REJECTED BY FMS

DESCR: Purchase Order Obligation

MAIL MSGS: 21291 CONFIRMATION:

TOTAL CODE SHEETS: 1

Select FMS Code Sheet Menu Option: Stack Status Report

START with TRANSACTION CODE: FIRST// PV

END with TRANSACTION CODE: LAST// PVZ

Print documents created after DATE: JAN 1,1993//6/19 (JUN 19, 1994)

Select one of the following:

Q QUEUED FOR TRANSMISSION

M MARKED FOR IMMEDIATE TRANSMISSION BY EVENT

T TRANSMITTED

E ERROR DURING TRANSMISSION

A ACCEPTED BY FMS

R REJECTED BY FMS

N TRANSMITTED WITH NO CONFIRMATION MESSAGE RETURNED

Select STATUS(s) to display: REJECTED BY FMS

Select one of the following:

Q QUEUED FOR TRANSMISSION

M MARKED FOR IMMEDIATE TRANSMISSION BY EVENT

T TRANSMITTED

E ERROR DURING TRANSMISSION

A ACCEPTED BY FMS

R REJECTED BY FMS

N TRANSMITTED WITH NO CONFIRMATION MESSAGE RETURNED

Select STATUS(s) to display:

SELECTED STATUS(s) to display:

REJECTED BY FMS

Print DESCRIPTION of event? NO// Y (YES)

Print DOCUMENT code sheets? NO// Y (YES)

DEVICE: HOME// LAT

\<\*\> please wait \<\*\>

GCS STACK FILE STATUS REPORT JUL 25, 1994@15:11:02 PAGE 1

TC-TRAN CODE -BATNUM DATE@TIME CREATED STATUS

--------------------------------------------------------------------------------------

PV-612C4500800 JUN 20, 1994@14:49:04 REJECTED BY FMS

DESCR: WASH ISC TESTING PV

MAIL MSGS: 19520 CONFIRMATION:

\*\*\* ACTUAL CODE SHEET:

CTL^IFC^FMS^612^DOC^PV^10 ^ ^612C4500800^19940620^144904^001^001^001^~

DOC^~PV1^PV^612C4500800^10 ^~

PV2^06^05^94^^^^^E^01^^^^^^^^^^THISISFAK^^1.00^~

PV3^^^^^^^^^^^^^TEST 1^^^^^^^^X^^^~

LIN^~

PVA^001^SO^612C45008 ^001^94^06^02^^^^^^^^^^^^^^^^^^^^^94^06^05^^10000.00^I^P^9

4^05^21^^^~

PVB^^^^^^^1.00^~

\*\*\* END OF CODE SHEET \*\*\*

TOTAL CODE SHEETS: 1

Code Sheet Edit

Create a Code Sheet

Delete a Code Sheet

Keypunch a Code Sheet

Purge Transmission Records/Code Sheets

Retransmit Stack File Document

Review a Code Sheet

Stack Status Report

Select FMS Code Sheet Menu Option:

### Funds Distribution Error Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Funds Distribution Module has a new menu for inquiring to and correcting Sub allowance (SA), Sub allowance Transfer (ST) and Allowance Transfer (AT) documents from FMS that may reject because of FMS errors. The Budget Analyst (BA) can inquire as to which documents may have been rejected and obtain status for the others.

FUNd Distribution & Accounting Menu

Accounting Technician Menu...

Fund Distribution Program Menu...

Payment/Invoice Tracking Menu...

Select Fund Distribution & Accounting Menu Option: FUNd Distribution Program Menu

Transaction Menu...

Budget Utilities Menu...

Print Menu...

FMS Documents Inquiry/Error Process...

Review VENDOR REQUEST

Select Fund Distribution Program Menu Option: FMS Documents Inquiry/Error Process

SOAR Enter/Edit Date When SOs become ARs

FMS Documents Inquiry

Rejected FMS Document Process

Select FMS Documents Inquiry/Error Process Option: FMS Documents Inquiry

Select STATION NUMBER ('^' TO EXIT): 542// 612 MARTINEZ, CA

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: SA Suballowance

FMS Budget Document ID: ?

ANSWER WITH GENERIC CODE SHEET STACK DOCUMENT IDENTIFIER

DO YOU WANT THE ENTIRE GENERIC CODE SHEET STACK LIST? Y (YES)

CHOOSE FROM:

SA-612FC0001

SA-612FC0002

SA-612FC0003

SA-612FC0004

SA-612FC0005

SA-612FC0006

SA-612FC0007

SA-612FC0008

SA-612FC0009

SA-612FC0010

'^' TO STOP: ^

FMS Budget Document ID: SA-612FC0056

FMS Document: SA-612FC0056

Description: Original Auto SA Document

Status: REJECTED

Created: JUL 6, 1994@08:02:38

FMS Doc Date: 07/06/1994

Doc Year: 94

Quarter: 4

Sation \#: 612

FCP \#: 120

\$Amount: 70000.00

BBFY: 1994

FMS Action: C

FMS Budget Document ID: SA-612FC0057

FMS Document: SA-612FC0057

Description: Original Auto SA Document

Status: REJECTED

Created: JUL 6, 1994@08:02:41

FMS Doc Date: 07/06/1994

Doc Year: 94

Quarter: 4

Sation \#: 612

FCP \#: 1333

\$Amount: 80000.00

BBFY: 1994

FMS Action: A

FMS Budget Document ID:

FMS Budget Document ID: NOT FOUND!

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: ST Suballowance Transfer

FMS Budget Document ID: ?

ANSWER WITH GENERIC CODE SHEET STACK DOCUMENT IDENTIFIER

DO YOU WANT THE ENTIRE GENERIC CODE SHEET STACK LIST? Y (YES)

CHOOSE FROM:

ST-612FC0034

ST-612FC0061

FMS Budget Document ID: ST-612FC0061

FMS Document: ST-612FC0061

Description: Original Auto ST Document

Status: REJECTED

Created: JUL 6, 1994@16:16:11

FMS Doc Date: 07/06/1994

Doc Year: 94

Quarter: 4

Sation \#: 612

From FCP \#: 120

\$Amount: 100.00

BBFY: 1994

To FCP#: 122

FMS Budget Document ID:

FMS Budget Document ID: NOT FOUND!

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: AT Allowance Transfer

FMS Budget Document ID: ?

ANSWER WITH GENERIC CODE SHEET STACK DOCUMENT IDENTIFIER

DO YOU WANT THE ENTIRE GENERIC CODE SHEET STACK LIST? Y (YES)

CHOOSE FROM:

AT-612FC0031

AT-612FC0065

FMS Budget Document ID: AT-612FC0065

FMS Document: AT-612FC0065

Description: Original Auto AT Document

Status: REJECTED

Created: JUL 7, 1994@12:31:21

FMS Doc Date: 07/07/1994

Doc Year: 94

Quarter: 4

Sation \#: 612

From FCP \#: 102

\$Amount: 100.00

BBFY: 1994

To FCP#: 910

FMS Budget Document ID:

FMS Budget Document ID: NOT FOUND!

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type:

SOAR Enter/Edit Date When SOs become ARs

FMS Documents Inquiry

Rejected FMS Document Process

Select FMS Documents Inquiry/Error Process Option:

The Budget Analyst will need to correct the errors according to the error codes on the DCT mail message returned from Austin. After the errors are corrected, the BA can regenerate the rejected document. For FMS budget documents created in IFCAP, errors will generally arise for only two reasons.

Insufficient Funds at Allowance Level

An SA document can be rejected because there was not enough money at the Allowance (station) level to distribute the ceiling to the FCP. If this is the case, the user has two options. The first is to wait until VACO has funded the allowance level with sufficient funds to cover the ceiling, then regenerate the document. The second is to “undo” the ceiling by using the “Place Released Ceiling Transaction in CP File” option. The user would enter a negative ceiling here, to back out the ceiling that rejected in FMS, and, correctly, no FMS document would be sent as a result of using this transaction. Now the IFCAP control point is again in sync with the FMS control point budget.

There is one caveat, however. There is currently no way to “cancel” or “delete” a rejected FMS document from the IFCAP stack file. Therefore, this rejected document remains in the file until one year after the transaction date when IFCAP purges it from its records.

Set-up of FCP is Invalid

Another reason that budget documents can reject is that the combination of budget elements coded on the initial SA for the FCP are not valid in FMS. The FMS error message will tell the user what is wrong with the budget set-up. The user will then go to the Add/Edit Control Point option, correct the FMS budget element(s) in question, and then simply regenerate the document. The user will NOT re-create the ceiling and/or transfer.

Rejected FMS Document Process (Regeneration):

SOAR Enter/Edit Date When SOs become ARs

FMS Documents Inquiry

Rejected FMS Document Process

Select FMS Documents Inquiry/Error Process Option: REJected FMS Document Process

Select STATION NUMBER ('^' TO EXIT): 542// 612 MARTINEZ, CA

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: SA Suballowance

FMS Rejected Budget Document ID: SA-612FC0062

FMS Document: SA-612FC0062

Description: Original Auto SA Document

Status: REJECTED

Created: JUL 6, 1994@16:32:19

FMS Doc Date: 07/06/1994

Doc Year: 94

Quarter: 4

Sation \#: 612

FCP \#: 434

\$Amount: 15000.00

BBFY: 1994

FMS Action: A

Ready To File Regenerated FMS Document? YES

\<Filed\>

FMS Rejected Budget Document ID:

FMS Rejected Budget Document ID: NOT FOUND!

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: ST Suballowance Transfer

FMS Rejected Budget Document ID: ?

ANSWER WITH GENERIC CODE SHEET STACK DOCUMENT IDENTIFIER

DO YOU WANT THE ENTIRE GENERIC CODE SHEET STACK LIST? Y (YES)

CHOOSE FROM:

ST-612FC0034

ST-612FC0061

FMS Rejected Budget Document ID: ST-612FC0061

FMS Document: ST-612FC0061

Description: Original Auto ST Document

Status: REJECTED

Created: JUL 6, 1994@16:16:11

FMS Doc Date: 07/06/1994

Doc Year: 94

Quarter: 4

Sation \#: 612

From FCP \#: 120

\$Amount: 100.00

BBFY: 1994

To FCP#: 122

Ready To File Regenerated FMS Document? YES

\<Filed\>

FMS Rejected Budget Document ID:

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: AT Allowance Transfer

FMS Rejected Budget Document ID: ?

ANSWER WITH GENERIC CODE SHEET STACK DOCUMENT IDENTIFIER

DO YOU WANT THE ENTIRE GENERIC CODE SHEET STACK LIST? Y (YES)

CHOOSE FROM:

AT-612FC0031

AT-612FC0065

AT-612FC0072

FMS Rejected Budget Document ID: FC0065 AT-612FC0065

FMS Document: AT-612FC0065

Description: Original Auto AT Document

Status: REJECTED

Created: JUL 7, 1994@12:31:21

FMS Doc Date: 07/07/1994

Doc Year: 94

Quarter: 4

Sation \#: 612

From FCP \#: 102

\$Amount: 100.00

BBFY: 1994

To FCP#: 910

Ready To File Regenerated FMS Document? YES

\<Filed\>

FMS Rejected Budget Document ID:

Select one of the following:

SA Suballowance

ST Suballowance Transfer

AT Allowance Transfer

Select Transaction Type: SOAR Enter/Edit Date When SOs become Ars

FMS Documents Inquiry

Rejected FMS Document Process

Select FMS Documents Inquiry/Error Process Option:

### How To Correct Errors Using the Accounting Technician's Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accounting Technician's Menu allows users to correct any (MO or SO) document by reviewing and editing the original purchase order or 1358 document. Once edited the document will be rebuilt and transmitted to FMS. For access to this option, contact your IRM service.

FMS Inquiry Rejected Obligation Documents:

Document Processing Menu...

Accounting Utilities Menu...

Reprint Menu...

Receiving Report Transmission Menu...

Fee Basis - IFCAP Code Sheet Menu...

FMS Code Sheet Menu...

Select Accounting Technician Menu Option: Document Processing Menu

1358 Processing Menu...

Amendment Processing

General Post Funds Requests Processing

Invoice Processing (ACCTG) Menu...

Obligation Processing

Process Receiving Report

Return Purchase Order to Supply

Return PO Amendment to Supply

Stacked Fiscal Documents Menu...

FMS Rejected Obligation Document Processing...

Select Document Processing Menu Option: FMS Rejected Obligation Document Processing

FMS Inquiry Rejected Obligation Documents...

FMS Rebuild/Transmit Rejected Obligation Documents...

Select FMS Rejected Obligation Document Processing Option: FMS Inquiry Rejected

Obligation Documents

MO/SO Rejected Document Inquiry for P.O.

SO Rejected Document Inquiry for 1358s

Select FMS Inquiry Rejected Obligation Documents Option: MO/SO Rejected Document Inquiry for P.O.

MO/SO Rejected Document Inquiry for P.O.

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select Stack Document for Inquiry: SO-688A40412

Select one of the following:

MO Miscellaneous Order

SO Service Order

Select Transaction Type: SO Service Order

FMS Document: SO-612A40024

Description: Purchase Order Obligation

Status: REJECTED BY FMS

Created: JUL 5, 1994@12:18:59

This FMS document has been rejected due to one or more errors.

The Certified Invoice will now be displayed for your review.

Please review the source document very carefully and take

the appropriate corrective action.

Press 'RETURN' to continue

PURCHASE ORDER: 612-A40024 STATUS: Transaction Complete

M.O.P.: CERTIFIED INVOICE LAST PARTIAL RECD.:

REQUESTING SERVICE: PPM

VENDOR: IFVENDOR, FIVE U.S. SHIP TO: Warehouse

HIGHWAY \#1 V.A. Medical Center

FAIRLESS HILLS, PA 19030 8403 Colesville Rd

800 555-5555 Silver Sprin, MD 20910

DELIVERY HOURS:

8:00 AM - 4:30 PM

--------------------------------------------------------------------------------------

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 161000 \| \| FAR 13

TYPE: PURCHASE ORDER \| \|AGENT:

DELIVER ON/BEFORE 7/15/94 \|CONTRACT: \| IFUSER, NINE

DISCOUNT TERM: NET30 \| \|DATE: 7/5/94

APP: 364/50161.001-120 \| \|ESTIMATED

\| \|TOTAL: 3.00

--------------------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------------

1 TEST 1 EA 3.00 3.00

\*\*\* ESTIMATED PURCHASE ORDER \*\*\*

END OF DISPLAY – PRESS RETURN OR ENTER '^' TO HALT:

Select Stack Document for Inquiry:

Select Stack Document for Inquiry: NOT FOUND!

Select one of the following:

MO Miscellaneous Order

SO Service Order

Select Transaction Type:

MO/SO Rejected Document Inquiry for P.O.

SO Rejected Document Inquiry for 1358s

Select FMS Inquiry Rejected Obligation Documents Option:

FMS Inquiry Rejected Obligation Documents ...

FMS Rebuild/Transmit Rejected Obligation Documents ...

Select FMS Rejected Obligation Document Processing Option: FMS REbuild/Transmit Rejected Obligation Documents

MO/SO Rebuild/Transmit for P.O.

SO Rebuild/Transmit for 1358s

Select FMS Rebuild/Transmit Rejected Obligation Documents Option: MO/SO Rebuild/Transmit for P.O.MO/SO Rebuild/Transmit for P.O.

Select STATION NUMBER ('^' TO EXIT): 542// 612 MARTINEZ, CA

Select one of the following:

MO Miscellaneous Order

SO Service Order

Select Transaction Type: MO Miscellaneous Order

Select Stack Document for Rebuild/Transmit: A40030

1 A40030 MO-612A40030

2 A40030 MO-612A40030 -612036

3 A40030 MO-612A40030 -612038

4 A40030 MO-612A40030 -612039

5 A40030 MO-612A40030 -612040

CHOOSE 1-5: 1 MO-612A40030

FMS Document: MO-612A40030

Description: Purchase Order Obligation Rebuild/Transmit

Status: REJECTED BY FMS

Created: JUL 11, 1994@16:42:54

This FMS document has rejected due to one or more errors.

The Purchase Order can now be displayed for your review.

Please review the source document very carefully and take

the appropriate corrective action.

Do you wish to display the source document? YES// YES

PURCHASE ORDER: 612-A40030 STATUS: Complete Order Received (Amended)

M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.: 1 07/11/94

REQUESTING SERVICE: SUPPLY

VENDOR: IFVENDOR, TWO SHIP TO: Warehouse

28200 Wick Road V.A. Medical Center

ROMULUS, MI 48174 8403 Colesville Rd

313 555-5555 Silver Sprin, MD 20910

DELIVERY HOURS:

8:00 AM - 4:30 PM

DELIVERY LOCATION: SUPPLY

--------------------------------------------------------------------------------------

FOB POINT: ORIGIN \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 844100 \| \|FAR 13

TYPE: PURCHASE ORDER \| \|AGENT:

DELIVER ON/BEFORE 7/21/94 \|CONTRACT: \|IFUSER, TEN

DISCOUNT TERM: NET30 \| \|DATE: 7/11/94

APP: 3640160.001.01-1102 \| \|

\| \|TOTAL: 18871.11

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------------

1 LOTS OF GOOD STUFF 110 EA 1 55.5555 17111.11

NSN: 7510-00-123-7777

QTY PREV RCVD: 100

PARTIAL NO.: 1

Items per EA: 1

3 GOOD STUFF 10 EA 150.00 1500.00

Items per EA: 1

4 MORE GOOD STUFF 10 EA 25.00 250.00

Items per EA: 1

5 EST. SHIPPING AND/OR HANDLING 10.00

Ifcap Training

V.A. TRANSACTION NUMBERS:

612-94-4-1102-0044

AMENDMENT NUMBER: 1 EFFECTIVE DATE: 7/11/94

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------------

\*ADDED THROUGH AMENDMENT\*

Item No. 3 Item Master File No.

GOOD STUFF

Items per EA: NSN:

10 EA at \$ 150.0000 = \$ 1500.00

AMENDMENT NUMBER: 2 EFFECTIVE DATE: 7/11/94

\*\*Currently:

Item No. 1 Item Master File No. 5505

LOTS OF GOOD STUFF

Items per EA: 1 NSN: 7510-00-123-7777

110 EA at \$ 150.00 = \$ 16500.00

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------------

\*\*Will now be AMENDED to read:

Item No. 1 Item Master File No. 5505

LOTS OF GOOD STUFF

Items per EA: 1 NSN: 7510-00-123-7777

110 EA \$ 155.5555 = \$ 17111.11

AMENDMENT NUMBER: 3 EFFECTIVE DATE: 7/12/94

\*ADDED THROUGH AMENDMENT\*

Item No. 4 Item Master File No.

MORE GOOD STUFF

Items per EA: 1 NSN:

10 EA at \$ 25.0000 = \$ 250.00

AMENDMENT NUMBER: 4 EFFECTIVE DATE: 7/12/94

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------------

\*\*Currently:

Item No. 1 Item Master File No. 5505

LOTS OF GOOD STUFF

Items per EA: 1 NSN: 7510-00-123-7777

100 EA at \$ 155.56 = \$ 15555.55

\*\*Will now be AMENDED to read:

Item No. 1 Item Master File No. 5505

LOTS OF GOOD STUFF

Items per EA: 1 NSN: 7510-00-123-7777

110 EA \$ 155.5555 = \$ 17111.11

Review a Receiving Report ? NO// (NO)

Do you wish to rebuild and retransmit this FMS document? YES//

PURCHASE ORDER - 612-A40030

COST CENTER: 844100 CONTROL POINT: 1102 MED CARE TEST2

BOC \#1: 2660 AMOUNT: \$ 18861.11

BOC \#2: 2661 AMOUNT: \$ 0.00

BOC \#3: 2660 AMOUNT: \$ 10.00

Justification(s):

Transaction Number: 612-94-4-1102-0044

Required for recreational activities in employee wellness.

The information listed above is recorded on this PURCHASE ORDER.

Is the above information correct? YES// NO

Should the Cost Center or BOC information be edited at this time? NO// YES

...now editing the Cost Center...

COST CENTER: 844100//

...now editing the BOCs...

Do you wish to assign the same BOC to ALL items? NO//

Do you wish to edit specific line items? YES//

Select ITEM: 1 LOTS OF GOOD STUFF

STK#: NSN: 7510-00-123-7777

BOC: 2660 Operating Supplies and Ma Replace ... With 2661

Replace

2661 Expendable Furniture and

2661 Expendable Furniture and Fixtures and Decoras

Select ITEM:

...now recalculating FMS commodity lines...

PURCHASE ORDER - 612-A40030

COST CENTER: 844100 CONTROL POINT: 1102 MED CARE TEST2

BOC \#1: 2660 AMOUNT: \$ 1750.00

BOC \#2: 2661 AMOUNT: \$ 17111.11

BOC \#3: 2660 AMOUNT: \$ 10.00

Justification(s):

Transaction Number: 612-94-4-1102-0044

Required for recreational activities in employee wellness.

The information listed above is recorded on this PURCHASE ORDER.

Is the above information correct? YES//

Net Cost of Order: \$ 18871.11

Control Point Balances

Uncommitted Balance: \$ 166962.85

Unobligated Balance: \$ 174399.35

Committed, Not Obligated: \$ 7436.50

OK to Continue? YES// YES

Select Obligation Processing Date: JUL 11,1994// (JUL 11, 1994)

This Purchase Order Obligation will now generate the

Original Entry Miscellaneous Order (MO) Document. The MO Document

will be marked for transmission to FMS.

Transmit this Document to FMS? YES//

The Electronic Signature must now be entered to generate the MO Document.

Enter ELECTRONIC SIGNATURE CODE: Thank you.

...now generating the FMS Miscellaneous Order (MO) Document...

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

Select Stack Document for Rebuild/Transmit:

Select Stack Document for Rebuild/Transmit: NOT FOUND!

Select one of the following:

MO Miscellaneous Order

SO Service Order

Select Transaction Type:

MO/SO Rebuild/Transmit for P.O.

SO Rebuild/Transmit for 1358s

Select FMS Rebuild/Transmit Rejected Obligation Documents Option:

FMS Inquiry Rejected Obligation Documents...

FMS Rebuild/Transmit Rejected Obligation Documents...

Select FMS Rejected Obligation Document Processing Option:

### Payment Error Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Payment vouchers transmitted to FMS may sometimes reject. The Accounting Technician has 2 options under the Invoice Processing (ACCTG) Menu to help view and correct (PV) type of documents and return corrected document to FMS for processing: the Payment Voucher (PV) Inquiry option and the FMS Payment Voucher Error Processing option. For access to this option, contact your IRM service.

Payment Voucher (PV) Inquiry:

Accounting Technician Menu Document

Processing Menu...

Accounting Utilities Menu...

Reprint Menu...

Receiving Report Transmission Menu...

Fee Basis –

IFCAP Code Sheet Menu...

FMS Code Sheet Menu...

Select Accounting Technician Menu Option: Document Processing Menu

The system can now generate a report that will list the type and

number of each document that is ready for processing at this

time.

But it may take a while to complete.

Do you want to run the report at this time? NO//

1358 Processing Menu...

Amendment Processing

General Post Funds Requests Processing

Invoice Processing (ACCTG) Menu...

Obligation Processing

Process Receiving Report

Return Purchase Order to Supply

Return PO Amendment to Supply

Stacked Fiscal Documents Menu...

FMS Rejected Obligation Document Processing...

Select Document Processing Menu Option: Invoice Processing (ACCTG) Menu

Invoice Processing for Payment

Return Invoice to Voucher Audit

PV Payment Voucher (PV) Inquiry

FMS Payment Voucher Error Processing

View Certified Invoice

Select Invoice Processing (ACCTG) Menu Option: Payment Voucher (PV) InquiryPayment Voucher (PV) Inquiry

Select STATION NUMBER ('^' TO EXIT): 542// 612 MARTINEZ, CA

Select one of the following:

PV Payment Voucher

Select Transaction Type: PV Payment Voucher

Payment Voucher NumberC40011 PV-612C4001100

FMS Document: PV-612C4001100

Description: Payment Voucher

Status: REJECTED BY FMS

Created: JUL 7, 1994@13:55:02

This FMS document has been rejected due to one or more errors.

The Certified Invoice will now be displayed for your review.

Please review the source document very carefully and take

the appropriate corrective action.

Press 'RETURN' to continue:

...Alright, I'm tired. Please hold on...

INVOICE TRACKING LIST JUL 26,1994 09:09 PAGE 1

--------------------------------------------------------------------------------------

ID NUMBER: 40075 INVOICE/BILL NUMBER: 123

DATE OF INVOICE: JUL 7, 1994, DATE INVOICE RECEIVED: JUL 7, 1994

INVOICE TYPE: NORMAL PURCHASE ORDER POINTER: 612-C40011

VENDOR: IFVENDOR, THREE DISCOUNT DAYS: 0

DISCOUNT TERMS: STANDARD AMOUNT CERTIFIED FOR PAYMENT: \$110.00

DATE GOODS/SERVICE RECEIVED: JUL 7, 1994

CERTIFICATION REQUIRED?: YES STATION NUMBER: 612

PURCHASE ORDER NUMBER: 612-C40011 FMS PAYMENT VOUCHER \#: 612C4001100

GROSS AMOUNT OF INVOICE: \$110.00 NET DAYS: 30

STATUS: Transaction Complete EXPANDED PO NUMBER: 612-C40011

CURRENT INVOICE LOCATION: FISCAL

D/T CHARGED TO CURRENT LOC: JUL 7, 1994@13:53

DATE RETURNED TO FISCAL: JUL 7, 1994, CERTIFIED FOR PAYMENT BY: IFUSER, NINE

COMPLETED IN ACCOUNTING BY: IFUSER, NINE

CERTIFIED BY VALIDATION CODE: /ES/IFUSER, NINE

COMPLETED BY VALIDATION CODE: /ES/IFUSER, NINE

INVOICE TRACKING LIST JUL 26, 1994@09:09 PAGE 2

-------------------------------------------------------------------------------------

CHARGED TO CURRENT LOCATION BY: IFUSER, NINE

CERTIFIED BY VALIDATION VER: 1 CERTIFIED BY ESIG CODE: 5711

COMPLETED BY VALIDATION VER: \<HIDDEN\> COMPLETED BY ESIG CODE: 5711

CERTIFIED BY SIG DATE/TIME: JUL 7, 1994@13:53:43

COMPLETED BY SIG DATE/TIME: JUL 7, 1994@13:55

CERTIFYING SERVICE: FISCAL

DATE/TIME CHARGED OUT: JUL 7, 1994@13:53

CHARGED BY: IFUSER, NINE

CERTIFYING SERVICE: FISCAL

DATE/TIME CHARGED OUT: JUL 7, 1994@13:53

CHARGED BY: IFUSER, NINE

BOC: 2660 Operating Supplies and Materials

ACCOUNTING LINE AMOUNT: \$120.00 LIQUIDATION AMOUNT: \$110.00

LIQUIDATION CODE: PARTIAL FMS LINE \#: 1

PROMPT PAYMENT TERMS \#: 1 DISCOUNT PERCENT: NET

DISCOUNT DAYS: 30

Press 'RETURN' to continue:

Payment Voucher Number

Payment Voucher Number NOT FOUND!

Select one of the following:

PV Payment Voucher

Select Transaction Type:

Invoice Processing for Payment

Return Invoice to Voucher Audit

PV Payment Voucher (PV) Inquiry

FMS Payment Voucher Error Processing

View Certified Invoice

FMS Payment Voucher Error Processing:

Select Invoice Processing (ACCTG) Menu Option: FMS Payment Voucher Error ProcessingFMS Payment Voucher Error Processing

Select Payment Voucher Number: PV-612C4001100

FMS Document: PV-612C4001100

Description: Payment Voucher

Status: REJECTED BY FMS

Created: JUL 7, 1994@13:55:02

This FMS document has been rejected due to one or more errors.

\*\*PONUM=PV-612C4001100

The Certified Invoice can now be displayed for your review.

Please review the source document very carefully and take

the appropriate corrective action.

Do you wish to display the source document? YES// NO

Do you wish to rebuild and retransmit this FMS document? YES//

Select STATION NUMBER ('^' TO EXIT): 612// MARTINEZ, CA

Does this invoice need to be processed by Voucher Audit? NO// Y (YES)

ARE YOU SURE? YES// (YES)

Status has been changed from 'Transaction Complete'

to 'Awaiting Voucher Audit Review'.

Press 'RETURN' to continue:

Select Payment Voucher Number: PV-612C4001100

FMS Document: PV-612C4001100

Description: Payment Voucher

Status: REJECTED BY FMS

Created: JUL 7, 1994@13:55:02

This FMS document has been rejected due to one or more errors.

\*\*PONUM=PV-612C4001100

The Certified Invoice can now be displayed for your review.

Please review the source document very carefully and take

the appropriate corrective action.

Do you wish to display the source document? YES// NO

Do you wish to rebuild and retransmit this FMS document? YES//

Select STATION NUMBER ('^' TO EXIT): 612// MARTINEZ, CA

Does this invoice need to be processed by Voucher Audit? NO// (NO)

Status has been changed from 'Awaiting Voucher Audit Review'

to 'In Accounting'.

Do you wish to process this invoice at this time? YES// (YES)

Switching to 'Process Invoice in Accounting' Module.

Unliquidated obligation amounts and BOCs on this order are:

\$110.00 2660 Operating Supplies and Materials

Total Invoice Amount Certified for Payment=\$110.00

Select BOC: 2660 Operating Supplies and Materials

//

BOC: 2660 Operating Supplies and Materials//

FMS Line \#1

ACCOUNTING LINE AMOUNT: 120.00// 110.00

LIQUIDATION AMOUNT: 110.00//

LIQUIDATION CODE: PARTIAL//

Select BOC:

OK to process this payment to FMS? NO// Y (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Transferring invoice data to PV documents for transmission to FMS.

Returning to 'Process FMS/CAPPS Error Message' Module.

Press 'RETURN' to continue:

FMS Payment Voucher Error Processing

Select Payment Voucher Number:

Select Payment Voucher Number: NOT FOUND!

Select one of the following:

PV Payment Voucher

Select Transaction Type:

Invoice Processing for Payment

Return Invoice to Voucher Audit

PV Payment Voucher (PV) Inquiry

FMS Payment Voucher Error Processing

View Certified Invoice

Select Invoice Processing (ACCTG) Menu Option:

### GIP Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GIP module has no error processing options. Current functionality will keep Internal Voucher (IV) documents updated with balances from FMS. IFCAP sends an IV document to Austin when the warehouse posts an issue book order. Users will no longer see a code sheet for issue book orders. For access to this option, contact your IRM service.

### Error Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FMS uses error listing to aid sites in interpreting the error codes and learn possible solutions. This error listing has over 10,000 entries. This listing is in the FMS Error Guide, available at your IRM service.

## eCMS/IFCAP Message Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP interfaces with the eCMS (electronic Contract Management System) which is hosted at the Austin Information Technology Center (AITC). The Accountable Officer sends approved 2237s to eCMS via HL7 messaging. The Contracting Officer in eCMS is able to Return the 2237s back to IFCAP if additional edits are needed or if it needs to be processed within IFCAP or if it needs to be Cancelled. A new menu option: Transaction Report – eCMS/IFCAP on the Budget Utilities menu is available to those Users who are assigned the new Security Key \[PRCHJFIS\].

A report can be generated for a single 2237, a single eCMS Contact, by date range, a specific Station Number, a specific fund control point, a specific messaging Event type, multiple Event types or ALL the records.

> **NOTE:** if your Station is using the IFCAP sub-station functionality, a report can be generated for a specific Station sub-station.

Select Budget Utilities Menu Option: transaction Report - eCMS/IFCAP

Select a single 2237 TRANSACTION NUMBER? NO//

Select a single eCMS Contact? NO//

Select ALL DATES: (SEP 04, 2012 - JUL 26, 2013)? NO//

Starting date: TODAY// 050113 (MAY 01, 2013)

Ending date: TODAY// 070113 (JUL 01, 2013)

Select a single STATION NUMBER? NO//

Select a single FUND CONTROL POINT? NO//

TRANSACTION EVENTS:

1 Sent to eCMS (includes resent 2237s)

2 Returned to Accountable Officer

3 Returned to Control Point

4 Cancelled within eCMS

Select one or more of the above events: 1-4//

Display event ERROR TEXT? NO//

All eCMS 2237s matching your selections below will be displayed:

All eCMS Contacts

Dates: (MAY 01, 2013 - JUL 01, 2013)

All Stations and Substations

All Fund Control Points

Event Types selected are:

1 = Sent to eCMS (includes resent 2237s)

2 = Returned to Accountable Officer

3 = Returned to Control Point

4 = Cancelled within eCMS

A note will display any errors, but not the full text.

DEVICE: HOME// 0;80;999 SSH VIRTUAL TERMINAL

JUL 26, 2013@12:18 eCMS/IFCAP TRANSACTION LOG REPORT p. 1

eCMS 2237: ALL eCMS Contact: ALL Station: ALL

Report Date Range: MAY 01, 2013 - JUL 01, 2013 Control Point: ALL

Events: Sent to eCMS, Returned to AO, Returned to CP, Cancelled within eCMS

IFCAP Reference Message Event Event Date

--------------------------------------------------------------------------------------

987-13-3-013-0024 2237 SENT JUN 17, 2013@12:59:36

ACKNOWLEDGED: JUN 17, 2013@13:00:22

987-13-3-013-0024 RETURN TO CONTROL POINT JUN 17, 2013@13:21:38

ACKNOWLEDGED: JUN 17, 2013@13:21:39

eCMS CONTACT: <Ecms.User1@med.va.gov> PHONE: 501-234-5678

RETURN/CANCEL DATE: JUN 17, 2013@12:21:35

REASON: Returned to the Control Point Level in IFCAP

987-13-3-013-0025 2237 SENT JUN 17, 2013@15:07:33

ACKNOWLEDGED: JUN 17, 2013@15:09:14

987-13-3-043-0021 2237 SENT JUN 17, 2013@13:57:21

ACKNOWLEDGED: (Pending) \<= awaiting an

application acknowledgement

This 2237 SENT has ERROR TEXT.

987-13-3-043-0027 2237 SENT JUN 20, 2013@09:53:14

ACKNOWLEDGED: JUN 20, 2013@09:54:19

987-13-3-043-0027 2237 CANCELLED BY ECMS JUN 20, 2013@10:38:56

ACKNOWLEDGED: JUN 20, 2013@10:38:57

eCMS CONTACT: <Ecms.User1@med.va.gov> PHONE: 501-234-5678

RETURN/CANCEL DATE: JUN 20, 2013@09:38:55

REASON: Cancel the PR and Return to IFCAP

987-13-3-043-0029 2237 SENT JUN 18, 2013@11:05:19

ACKNOWLEDGED: JUN 18, 2013@11:07:36

987-13-3-043-0035 RETURN TO ACCOUNTABLE OFFICER JUN 20, 2013@11:31:26

ACKNOWLEDGED: JUN 20, 2013@11:31:27

eCMS CONTACT: <Ecms.User1@med.va.gov> PHONE: 501-234-5678

RETURN/CANCEL DATE: JUN 20, 2013@10:31:24

REASON: Returned to the Accountable Officer Level in IFCAP

987-13-3-144-0019 2237 RESENT JUN 21, 2013@11:57:05

ACKNOWLEDGED: JUN 21, 2013@11:58:59

886-13-4-081-0024 2237 SENT JUL 01, 2013@16:17:25

ACKNOWLEDGED: JUL 01, 2013@16:20:03

This 2237 SENT has ACKNOWLEDGMENT ERROR TEXT.

987-13-4-081-0025 2237 SENT JUL 01, 2013@17:34:42

ACKNOWLEDGED: JUL 01, 2013@17:36:20

END OF REPORT

## Menu Outline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists each menu option assigned to the standard menu configuration for a Budget Analyst. Main menu options are flush left. Subordinate options are spaced to the right. For example, if you wanted to use the "Edit Existing, Unreleased Transaction" option, you would select "Funds Distribution Program Menu", then "Transaction Menu", then "Edit Existing, Unreleased Transaction".

Funds Distribution Program Menu

Transaction Menu

Add New Transaction (Ceiling)

Edit Existing, Unreleased Transaction

Delete Unreleased Transaction

Transfer From/To Control Point

Release Transaction

Monthly Budget Distribution

Generate FMS Budget Documents

Multiple Transaction Menu

Create/Post Multiple Transaction

Post/Edit Temporary Transaction

Quarterly Rollover Fund Control Point Balance

Year to Date Accrual Extract

Budget Utilities Menu

Edit Budget Categories

FMS Exception Transaction Report

Repost FMS Exceptions

Clear FMS Exception File Entries

Clear Program Lock

Dictionary Management Menu

Standard Dictionary List

Dictionary List Menu

Standard Dictionary List

Fund List

Fund/Appropriation List

Required Fields List

Generate New Fiscal Year Fund/Required Table

Fund/Appropriation Enter/Edit

Define Standard Dictionary

Fund Enter/Edit

Required Fields Edit

Display Control Point Official's Balance

FCP/CC/BOC Management Menu

BOC Management Menu

Add/Edit BOC

Deactivate BOC

Reactivate BOC

BOC Listing

Cost Center Management Menu

Add/Edit Cost Center

Deactivate Cost Center

Reactivate Cost Center

Cost Center Listing

List Cost Centers with Associated BOC

Fund Control Point Management Menu

Add/Edit Control Point

Deactivate a Fund Control Point

Reactivate a Fund Control Point

Place Released Ceiling Transaction in CP File

Display Control Point Committed Transactions

Reset FCP Yearly Accounting Element & ACT Code

Recalculate All Fund Control Point Balances

Transaction Report – eCMS/IFCAP

Print Menu

Selected Control Points

Range of Transactions

Transfer of Disbursing Authority

Detailed Appropriation Summary

Appropriation Summary Totals

FTEE Summary by Appropriation

Budget Distribution Reports Menu

1st Quarter Report

2nd Quarter Report

3rd Quarter Report

4th Quarter Report

April - September

October - March

Complete Fiscal Year

Control Point List

FCP BOC List

Control Point PO List

Audit Reports Menu

Control Point Activity File Inquiry

Procurement and Accounting Transactions Inquiry

826 (IFCAP) Report

Detailed Report of Unpaid PC Transactions by FCP

Display 2237 Request

FCP Accounting Elements

Fiscal Daily Review Fiscal Pending Action

History of Purchase Card Transactions Purchase Card Statistics

Reconciled Purchase Card Transactions

Unreconciled Austin Payment Transactions

Unreconciled Purchase Card Transactions

Year To Date Accrual

FMS Documents Inquiry/Error Process

SOAR Enter/Edit Date When SOs become ARs

FMS Documents Inquiry

Rejected FMS Document Process

Review VENDOR REQUEST

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>1358</strong></p>
</blockquote></th>
<th><blockquote>
<p>VA Form 1358 Estimated Obligation or Change in Obligation.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>2138</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 90-2138, Order for Supplies or Services. First page of a VA Purchase Order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>2139</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>2237</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 90-2237, Request, Turn-in and Receipt for Property or Services. Used to request goods and services.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>A&amp;MM</strong></p>
</blockquote></td>
<td><blockquote>
<p>Acquisition and Materiel Management Service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>AACS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Automated Allotment Control System--Central computer system developed by VHA to disburse funding from VACO to field stations.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Accounting Technician</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fiscal employee responsible for obligation and payment of received goods and services. Accounting Technicians process accounting transactions and transmit them to FMS.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Activity Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>The last two digits of the AACS number. It is defined by each station.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ADP Security Officer</strong></p>
</blockquote></td>
<td><blockquote>
<p>The individual at your station who’s is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ALD Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>Appropriation Limitation Department. A set of Fiscal codes that identifies the appropriation used for funding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Allowance table</strong></p>
</blockquote></td>
<td><blockquote>
<p>Reference table in FMS that provides financial information at the level immediately above the AACS, or sub-allowance level.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Amendment</strong></p>
</blockquote></td>
<td><blockquote>
<p>A document which changes the information contained in a specified Purchase Order. Amendments are processed by the Purchasing &amp; Contracting section of A&amp;MM and obligated by Fiscal Service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>AMIS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Automated Management Information System.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Application Coordinator</strong></p>
</blockquote></td>
<td><blockquote>
<p>The individuals responsible for the implementation, training and trouble-shooting of a software package within a service. IFCAP requires there be an Application Coordinator designated for Fiscal Service, Supply Service, and for the Control Points (Requesting Services).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Approve Requests</strong></p>
</blockquote></td>
<td><blockquote>
<p>The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or other request form and transmit said request to Supply/Fiscal.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Authorization</strong></p>
</blockquote></td>
<td><blockquote>
<p>A charge to an obligated 1358. Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Authorization Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>The amount of money remaining that can be authorized against the 1358. The service balance minus total authorizations.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Batch Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Breakout Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>A set of A&amp;MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Budget Analyst</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fiscal employee responsible for distributing and transferring funds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Budget Object Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes replace sub accounts in IFCAP 5.1. Budget object codes are listed in the left column of MP4 Part V, Appendix B-1.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Budget Sort Category</strong></p>
</blockquote></td>
<td><blockquote>
<p>Used by Fiscal Service to identify the allocation of funds throughout their facility.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Ceiling Transactions</strong></p>
</blockquote></td>
<td><blockquote>
<p>Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Classification of Request</strong></p>
</blockquote></td>
<td><blockquote>
<p>An identifier a Control Point can assign to track requests that fall into a category, e.g., Memberships, Replacement Parts, Food Group III.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Common Numbering Series</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering Series used by each facility.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Control Point</strong></p>
</blockquote></td>
<td><blockquote>
<p>Financial element, existing ONLY in IFCAP, which corresponds to the ACCS number in FMS. Also, the division of monies to a specified service, activity or purpose from an appropriation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Control Point Clerk</strong></p>
</blockquote></td>
<td><blockquote>
<p>The user within the service who is designated to input requests (2237s) and maintain the Control Point records for a Service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Control Point Official</strong></p>
</blockquote></td>
<td><blockquote>
<p>The individual authorized to expend government funds for ordering of supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Control Point Official's Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Control Point Requestor</strong></p>
</blockquote></td>
<td><blockquote>
<p>The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&amp;MM.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Cost Center</strong></p>
</blockquote></td>
<td><blockquote>
<p>“Subsection” of a Fund Control Point. Cost centers allow fiscal staff to create total expense reports for a section or service, and allow requestors to assign requests to that section or service. Cost centers are listed in the left column of MP-4 Part V, Appendix B-1.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Cost Center</strong></p>
</blockquote></td>
<td><blockquote>
<p>A subdivision of a Fund Control Point, which tells which service/section, is being charged for a request/order.</p>
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
<p><strong>Deficiency</strong></p>
</blockquote></td>
<td><blockquote>
<p>When a budget has obligated and expended more than it was funded (see MP-4, Part V, Section C).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Delinquent Delivery Listing</strong></p>
</blockquote></td>
<td><blockquote>
<p>A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Direct Delivery Patient</strong></p>
</blockquote></td>
<td><blockquote>
<p>A patient who has been designated to have goods delivered directly to him/her from the vendor.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Discount Item</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a</p>
<p>percentage or a set dollar value.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>eCMS</strong></p>
</blockquote></td>
<td><blockquote>
<p>The VA’s electronic Contract Management System hosted at the Austin Information Technology Center in Austin, Texas.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>EDI Vendor</strong></p>
</blockquote></td>
<td><blockquote>
<p>A vendor with whom the VA has negotiated an arrangement to accept and fill orders electronically.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Electronic Data Interchange (EDI)</strong></p>
</blockquote></td>
<td><blockquote>
<p>Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Electronic Signature</strong></p>
</blockquote></td>
<td><blockquote>
<p>The electronic signature code replaces the written signature on all IFCAP documents used within your facility.</p>
<p>Documents going off-station will require a written signature as well.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Expenditure Request</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>FCP</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fund Control Point (see Control Point).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Federal Tax ID</strong></p>
</blockquote></td>
<td><blockquote>
<p>A unique number that identifies your station to the Internal Revenue Service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Fiscal Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidation submitted against the obligation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Fiscal Quarter</strong></p>
</blockquote></td>
<td><blockquote>
<p>The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Fiscal Year</strong></p>
</blockquote></td>
<td><blockquote>
<p>Twelve-month period from October 1 to September 30.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>FMS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Financial Management System, which has replaced CALM as the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>FOB</strong></p>
</blockquote></td>
<td><blockquote>
<p>Freight on Board. An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means that shipping charges are due to the shipper, and must be paid when the shipper arrives at the warehouse with the item.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>FPDS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Federal Procurement Data System.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>FTEE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned an FTEE of 0.5, as would a full-time employee that worked for half of a year.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Fund Control Point</strong></p>
</blockquote></td>
<td><blockquote>
<p>CALM accounting element that is not used by FMS.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Funds Control</strong></p>
</blockquote></td>
<td><blockquote>
<p>A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Funds Distribution</strong></p>
</blockquote></td>
<td><blockquote>
<p>A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>GBL</strong></p>
</blockquote></td>
<td><blockquote>
<p>Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of $250.00.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>GL</strong></p>
</blockquote></td>
<td><blockquote>
<p>General Ledger.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Identification Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>A computer-generated number assigned to a code sheet.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Imprest Funds</strong></p>
</blockquote></td>
<td><blockquote>
<p>Monies used for cash or 3rd party draft purchases at a VA facility.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Integrated Supply Management System (ISMS)</strong></p>
</blockquote></td>
<td><blockquote>
<p>ISMS is the system that replaced LOG I for Expendable Inventory.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ISMS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Integrated Supply Management System.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Item File</strong></p>
</blockquote></td>
<td><blockquote>
<p>A listing of items specified by A&amp;MMS as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Item History</strong></p>
</blockquote></td>
<td><blockquote>
<p>Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Item Master Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>A computer generated number used to identify an item in the Item File.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Justification</strong></p>
</blockquote></td>
<td><blockquote>
<p>A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Liquidation</strong></p>
</blockquote></td>
<td><blockquote>
<p>The amount of money on the invoice from the vendor for the authorization. They are processed through payment/invoice tracking.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LOG I</strong></p>
</blockquote></td>
<td><blockquote>
<p>LOG I is the name of the Logistics A&amp;MM computer located at the Austin Data Processing Center. This system continues to support the Consolidated Memorandum of Receipt.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Mandatory Source</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Federal Agency that sells supplies and services to the VA. VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MSC Confirmation Message</strong></p>
</blockquote></td>
<td><blockquote>
<p>A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of CALM Code Sheets.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Obligation</strong></p>
</blockquote></td>
<td><blockquote>
<p>The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of a Purchase Order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Obligation (Actual) Amount</strong></p>
</blockquote></td>
<td><blockquote>
<p>The actual dollar figure obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document on IFCAP.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Obligation Data</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Control Point option that allows the Control Point Clerk to enter data not recorded by IFCAP.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Obligation Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>The C-prefix number that Fiscal Service assigns to the 1358.</p>
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
<tr class="odd">
<td><blockquote>
<p><strong>PAID</strong></p>
</blockquote></td>
<td><blockquote>
<p>Paid Accounting Integrated Data.</p>
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
<p>Pending Accounting Transaction number - the primary FMS reference number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Personal Property Management</strong></p>
</blockquote></td>
<td><blockquote>
<p>A section of A&amp;MM Service responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process all requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PPM</strong></p>
</blockquote></td>
<td><blockquote>
<p>Personal Property Management.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Procurement Request Cards</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 10-7142. Used to order items repetitively.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Program Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>Accounting element that identifies the VA initiative or program that the purchase will support.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Prompt Payment Terms</strong></p>
</blockquote></td>
<td><blockquote>
<p>The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchase History Add (PHA)</strong></p>
</blockquote></td>
<td><blockquote>
<p>Information about purchase orders which is automatically sent to Austin for archiving. This same transaction is also used to send a PO for EDI processing.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Purchase Order</strong></p>
</blockquote></td>
<td><blockquote>
<p>A government document authorizing the purchase of the goods or services at the terms indicated.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchase Order Acknowledgment</strong></p>
</blockquote></td>
<td><blockquote>
<p>Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Purchase Order Status</strong></p>
</blockquote></td>
<td><blockquote>
<p>The status of completion of a purchase order (e.g., Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchasing Agents</strong></p>
</blockquote></td>
<td><blockquote>
<p>A&amp;MM employees legally empowered to create purchase orders to obtain goods and services from commercial vendors.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Quarterly Report</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Control Point listing of all transactions (Ceilings, Obligations, Adjustments) made to a Control Point's Funds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Quotation for Bid</strong></p>
</blockquote></td>
<td><blockquote>
<p>Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Receiving Report</strong></p>
</blockquote></td>
<td><blockquote>
<p>Report that Warehouse Clerk creates to record that the warehouse has received an item.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Receiving Report</strong></p>
</blockquote></td>
<td><blockquote>
<p>The VA document used to indicate the quantity and dollar value of the goods being received.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Reference Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>Also known as the Transaction Number. The computer generated number that identifies a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point - 4 digit Sequence Number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Repetitive (PR Card) Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>See Item Master Number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Repetitive Item List</strong></p>
</blockquote></td>
<td><blockquote>
<p>A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate requests from the list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Requestor</strong></p>
</blockquote></td>
<td><blockquote>
<p>See “Control Point Requestor.”</p>
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
<p>A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Section Request</strong></p>
</blockquote></td>
<td><blockquote>
<p>A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Service Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>SF-18</strong></p>
</blockquote></td>
<td><blockquote>
<p>Request for Quotation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>SF-30</strong></p>
</blockquote></td>
<td><blockquote>
<p>Amendment of Solicitation/Modification of Contract.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Short Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>A phrase that describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE- SURGICAL MEDIUM).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Site Parameters</strong></p>
</blockquote></td>
<td><blockquote>
<p>Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Sort Group</strong></p>
</blockquote></td>
<td><blockquote>
<p>An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Sort Order</strong></p>
</blockquote></td>
<td><blockquote>
<p>The order in which the budget categories will appear on the budget distribution reports.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Special Remarks</strong></p>
</blockquote></td>
<td><blockquote>
<p>A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Stacked Documents</strong></p>
</blockquote></td>
<td><blockquote>
<p>The POs, RRs &amp; 1358s that are sent electronically to Fiscal and stored in a file rather than being printed immediately.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Status of Funds</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fiscal's on-line status report of the monies available to a Control Point. FMS updates this information automatically.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Sub-control Point</strong></p>
</blockquote></td>
<td><blockquote>
<p>A specific budget within a Control Point, defined by a Control Point user.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Sub-cost Center</strong></p>
</blockquote></td>
<td><blockquote>
<p>A subcategory of Cost Center. In IFCAP 5.1, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.</p>
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
<p>See "Transfer of Disbursing Authority."</p>
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
<p>The total amount of the liquidation against the 1358 obligation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Transaction Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>The number of the transaction that funded a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Transmission Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traffic.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Type Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>A set of A&amp;MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Vendor file</strong></p>
</blockquote></td>
<td><blockquote>
<p>An IFCAP file of vendors solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. File 440 contains information about the vendors solicited by your station. The debtor's address may be drawn from this file, but is maintained separately. If the desired vendor is not in the file, contact A&amp;MM Service to have it added.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Vendor IDus Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>The ID number assigned to a vendor by FMS.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VRQ</strong></p>
</blockquote></td>
<td><blockquote>
<p>FMS Vendor Request document. When users send vendor information to FMS, FMS sends a VRQ document to IFCAP with the vendor information, ensuring that the information in the IFCAP vendor file matches the information in the FMS vendor table.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1358, 95, 139
2237, 35, 93, 95, 135, 206
826 (IFCAP) Report, 89
AACS, 16
Accounting Technician, 35, 140, 170, 185, 197
Accrual (Monthly), 53
Add New Transaction (Ceiling), 15
Add/Edit BOC, 112
Add/Edit Control Point, 7, 132, 181
Add/Edit Cost Center, 118
Audit Reports Menu, 102, 104, 106
BOC, 110
BOC Listing, 116
Budget Distribution Reports Menu, 78
budget object code (BOC), 105, 106
Budget Object Code (BOC), 112
Clear Program Lock, 137
Control Point List, 81, 82
Control Point Official, 1, 13, 19, 126, 135
Control Point PO List, 87
cost center listing, 123
Cost Center Listing, 122
Create a Code Sheet, 168
Create/Post Multiple Transaction, 42
Date Committed, 130
Deactivate BOC, 113
Deactivate Cost Center, 119
Define Standard Dictionary, 162
Display 2237 Request, 94
Display Control Point Committed Transactions, 130
FCP BOC List, 85
fiscal year, 1, 16, 17, 20, 23, 26, 32, 36, 37, 40, 43, 47, 51, 67, 69, 73, 75, 77, 78, 80, 91, 95, 126, 132, 135, 160, 164
Fiscal Year, 5, 9, 12, 63, 66, 72, 77, 78, 138
FMS, iv, 1, 2, 3, 5, 12, 13, 22, 23, 30, 59, 61, 63, 98, 138, 139, 140, 142, 154, 156, 165, 168, 169, 170, 175, 181, 185, 197, 201, 205
FMS Documents Inquiry, 138, 141, 143
FMS Documents Inquiry/Error Process Menu, 138
FMS Inquiry Rejected Obligation Documents, 185
FMS Payment Voucher Error Processing, 197
From/To Control Point, 31
FTEE, 77
Fund Enter/Edit, 163
Fund List, 152
Generate FMS Budget Documents, 22, 168
List Cost Centers with Associated BOC, 123
Load Standard Dictionary, 145
Monthly Budget Distribution, 35
Multiple Transaction Menu, 42, 44, 46, 49
Payment Voucher (PV) Inquiry, 197
Place Released Ceiling Transaction in CP File, 181
Post/Edit Temporary Transaction, 46
Procurement and Accounting Transactions Inquiry, 105
purchase order, 135, 168, 185
Purchase Order, 106
Quarterly Rollover Fund Control Point Balance, 50
Reactivate a Fund Control Point, 129
Reactivate BOC, 115
Reactivate Cost Center, 121
Rejected FMS Document Process, 142, 181
Release Transaction, 19, 44, 49
Required Fields Edit, 165
Required Fields List, 154, 156
Stack Status Report, 170
Standard Dictionary List, 150, 151
transaction date, 69, 72, 181
Transaction Date, 23, 43, 142
transaction number, 43, 44, 49, 67, 69, 72, 73, 95, 104, 105, 106, 127
Transaction Number, 69, 104, 105
TRANSACTION NUMBER, 47
Transfer of Disbursing Authority, 72
Unreleased Transaction, 25, 39, 209
