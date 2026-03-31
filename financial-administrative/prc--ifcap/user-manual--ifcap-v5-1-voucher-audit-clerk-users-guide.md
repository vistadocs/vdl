---
title: IFCAP Version 5.1 Voucher Audit Clerk User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Voucher Audit Clerk User's Guide
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
menu_options: 11
description: 
audience: 
keywords: 
  - invoice
  - strong
  - payment
  - number
  - table
  - contents
  - vendor
  - class
  - certified
  - order
page_count: 0
word_count: 15044
section_count: 64
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1voucher_audit_clerk.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1voucher_audit_clerk.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Voucher Audit ClerkUser's Guide

![](ifcap-version-5-1-voucher-audit-clerk-user-s-guide/001.png)

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
<td><p>Updates based on patch PRC*5.1*252.</p>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p></td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="odd">
<td>October 2011</td>
<td>3.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See page <a href="#PRC_158_A">42</a>.</td>
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

########### Preface

This manual explains how to use the options in the Payment/Invoice Tracking Menu of the Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) System to build and maintain an invoice tracking system.

Table of Contents

# INTRODUCTION


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [INTRODUCTION](#introduction)
  - [The Role of the Voucher Audit Clerk](#the-role-of-the-voucher-audit-clerk)
  - [How to Use This Manual](#how-to-use-this-manual)
  - [Reference Numbering System](#reference-numbering-system)
  - [Package Management, Legal Requirements and Security Measures](#package-management-legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
  - [Improved Use of Available Cross-References](#improved-use-of-available-cross-references)
    - [Introduction](#introduction-1)
    - [Changes in Payment/Invoice Tracking File Design](#changes-in-paymentinvoice-tracking-file-design)
    - [FMS Document Creation](#fms-document-creation)
    - [Sub-cost Center Change](#sub-cost-center-change)
    - [Changes to Fields to Accommodate FMS.](#changes-to-fields-to-accommodate-fms)
    - [Processing to Accommodate FMS](#processing-to-accommodate-fms)
- [New Invoice](#new-invoice)
  - [Introduction](#introduction-2)
  - [Menu Path](#menu-path)
  - [Get Tracking Number](#get-tracking-number)
  - [Select Order](#select-order)
  - [Review Order Data](#review-order-data)
  - [Confirm Order Selection](#confirm-order-selection)
  - [Enter Date](#enter-date)
  - [Enter Amount](#enter-amount)
- [LOG-IN CERTIFIED INVOICES FROM SERVICES](#log-in-certified-invoices-from-services)
  - [Introduction](#introduction-3)
  - [Menu Path](#menu-path-1)
  - [Processing](#processing)
  - [Enter Amount](#enter-amount-1)
- [APPROVE PAYMENT OF INVOICES ALREADY CHECKED IN](#approve-payment-of-invoices-already-checked-in)
  - [Introduction](#introduction-4)
  - [Approve](#approve)
  - [Edit Data](#edit-data)
  - [View Order](#view-order)
  - [Information Display](#information-display)
  - [Confirm Order Selection](#confirm-order-selection-1)
  - [Enter Discount](#enter-discount)
- [VIEW CERTIFIED INVOICE](#view-certified-invoice)
  - [Menu Path](#menu-path-2)
  - [Select Invoice Tracking Number](#select-invoice-tracking-number)
  - [Listing](#listing)
- [CREATE/REPRINT A SUSPENSION LETTER](#createreprint-a-suspension-letter)
  - [Introduction](#introduction-5)
  - [Menu Path](#menu-path-3)
  - [Enter Tracking ID](#enter-tracking-id)
  - [Suspension Letter](#suspension-letter)
- [DELETE CERTIFIED INVOICE](#delete-certified-invoice)
  - [Introduction](#introduction-6)
  - [Menu Path](#menu-path-4)
  - [Select Invoice Number](#select-invoice-number)
  - [Delete Invoice](#delete-invoice)
- [EDIT FMS VENDOR PAYMENT INFORMATION](#edit-fms-vendor-payment-information)
  - [Introduction](#introduction-7)
  - [Menu Path](#menu-path-5)
  - [Select Vendor](#select-vendor)
  - [Edit Information](#edit-information)
  - [Enter Vendor Type](#enter-vendor-type)
- [GENERATE OVERDUE INVOICE BULLETINS](#generate-overdue-invoice-bulletins)
  - [Introduction](#introduction-8)
  - [Menu Path](#menu-path-6)
  - [Enter Date and Time](#enter-date-and-time)
- [HISTORY - CODE SHEET/OBLIGATION (PAT) NUMBER](#history-code-sheetobligation-pat-number)
  - [Introduction](#introduction-9)
  - [Menu Path](#menu-path-7)
  - [Select Order Number](#select-order-number)
- [INCOMPLETE INVOICE EDIT](#incomplete-invoice-edit)
  - [Introduction](#introduction-10)
  - [Menu Path](#menu-path-8)
  - [Enter Tracking ID](#enter-tracking-id-1)
  - [Display Data](#display-data)
  - [View Order](#view-order-1)
  - [Enter Discount](#enter-discount-1)
- [PRINT CERTIFIED INVOICE OVERDUE REPORTS](#print-certified-invoice-overdue-reports)
  - [Introduction](#introduction-11)
  - [Menu Path](#menu-path-9)
  - [Enter Printer Name](#enter-printer-name)
- [RECHARGE AN INVOICE](#recharge-an-invoice)
  - [Introduction](#introduction-12)
  - [Menu Path](#menu-path-10)
  - [Enter Tracking ID](#enter-tracking-id-2)
  - [Display Data](#display-data-1)
- [SEND CERTIFIED INVOICE DUE BULLETIN](#send-certified-invoice-due-bulletin)
  - [Introduction](#introduction-13)
  - [Menu Path](#menu-path-11)
  - [Select Station Number](#select-station-number)
- [GLOSSARY](#glossary)
- [INDEX](#index)

## The Role of the Voucher Audit Clerk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Voucher Audit Clerk inspects invoices, maintains invoice records, and records and edits payment information. This role is essential in IFCAP, because Voucher Audit Clerks ensure that vendors are paid promptly and correctly.

## How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual explains how to perform the role of the Voucher Audit Clerk by dividing that role into small, manageable tasks. The authors of this manual have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new Voucher Audit Clerks to use this manual as a tutorial by following the instructions from beginning to end. Experienced Voucher Audit Clerks can use this manual as a reference tool by using the index and table of contents.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1. All clear? Actually, all this means is that users that want to divide their reading into manageable lessons can concentrate on one section and all of its subsections, e.g., section 1.3.5.4 and all of its subsections would make a coherent lesson.

## Package Management, Legal Requirements and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use IFCAP to audit vouchers, Voucher Audit Clerks are given access to a set of IFCAP menu options designed for their use. Additional menu options are controlled by the use of access “keys.” The Information Resources Management Service at their facility administers these access keys to individual Voucher Audit Clerks. Also, each Voucher Audit Clerk is assigned a “signature code” that functions legally as their signature. Voucher Audit Clerks must enter this signature to create any form in IFCAP that would require an authorizing signature if they created the form manually.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document explains how to use the Payment/Invoice Tracking Menu in IFCAP. Novice Voucher Audit Clerks will be unfamiliar with the information that some of the IFCAP prompts require. IFCAP provides three levels of explanations for the prompts. Enter a question mark at the prompt to read a description of the prompt, two question marks to read a more complex explanation of the prompt, and three question marks to read a complete description of the prompt and read a list of acceptable responses to the prompt.

## Improved Use of Available Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The cross-references between Invoices, Purchase orders, Vendors, and Fund Control Points are part of the IFCAP database and are used as reference information by IFCAP to provide information in new ways. IFCAP performs the new cross-references listed below.

#### Invoices by Expanded Purchase Order Number

There is a “D” cross-reference in the Invoice Tracking File (#421.5). This cross reference allows the user, while entering a new invoice, to view any other invoices that have already been entered for the purchase order. The system asks if the user would like to view other invoices for the Purchase order. If the user enters “Y(yes),” the system displays a list of invoices to choose from. The invoice display will be in the standard “captioned” output, similar to what appears when performing a VA File Man file inquiry.

#### Purchase Orders by Vendor

There is a “C” cross-reference in the Invoice Tracking File (#421.5). This cross-reference allows the user to view any other invoices that have already been entered for the same vendor. The system asks if the user would like to view other invoices for the vendor. If the user enters “Y(yes),” the system displays a list of invoices to choose from. The invoice display will be in the standard “captioned” output, similar to what appears when performing a VA File Man file inquiry.

#### Purchase Orders by Fund Control Point 

There is an “E” cross-reference in the Procurement & Accounting Transactions File (#442). This cross-reference allows users, when entering a new invoice or selecting an existing one, to pull up a list of PAT Numbers for a given FCP upon entering the FCP number at the “PAT Number:” prompt.

#### Invoices by FMS Payment Voucher (PV) Document Number

There is an “F” cross-reference in the Invoice Tracking File (#421.5). This cross-reference allows users, when selecting an invoice, to enter an FMS Payment Voucher (PV) document number. The system will display the invoice corresponding (by way of this cross-reference) to the PV document.

### Changes in Payment/Invoice Tracking File Design

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the data fields already mentioned, the Payment/Invoice Tracking File design includes two multiple fields required to maintain compatibility with FMS. The software will support up to 999-budget object code (BOC) accounting line items per invoice. The BOC and line amount fields have been relocated into an Accounting Line multiple field with a maximum of 999 allowable occurrences. The fields related to payment terms are located in a Prompt Payment Terms multiple field with a maximum of three allowable occurrences.

### FMS Document Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will create and transmit FMS Payment Voucher (PV) documents to FMS. This type of document notifies FMS of certified invoices processed in IFCAP. The PV document is initiated upon processing of the invoice for payment in Accounting.

### Sub-cost Center Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP uses the last two digits of the cost center as the sub-cost center. Most cost centers currently end in “00,” but if they end in some other numerical combination, the value of the last two digits will be the sub-cost center sent to FMS. IFCAP will continue to have only one field, cost center, but will send FMS two values. For example, if the cost center in IFCAP were 870011, IFCAP would send FMS the value of 870000 as the cost center, and 11 as the sub-cost center. VACO will define and provide any sub-cost centers to IFCAP stations.

### Changes to Fields to Accommodate FMS.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To allow IFCAP to prepare the PV document, the input templates use the following fields.

- Prompt Pay Type
- Partial/Final (P/F) Indicator
- Date Stamp

The following fields are stored in the Invoice Tracking file ( \#421.5), but the user will never see them unless they review the actual FMS document (either by going directly into FMS to view it, or by reviewing a rejected PV document). These fields are required on the PV document, but IFCAP will not prompt the user for them; it will derive them from information it stores elsewhere.

<u>Reference Document Trans Number.</u> This is the FMS transaction number of the “reference” FMS obligation document. In the case of a PV document, there is a corresponding SO document. The SO document notified FMS of an obligation, and the PV notifies FMS of a certified invoice approved for payment. The SO is the PV’s “reference” document. The user does not need to enter many of the FMS PV required fields because IFCAP can derive them from the “reference” SO document.

<u>Reference Document Trans Code.</u> This is the transaction code (a two letter code in FMS that specifies the type of an FMS document) of the reference obligation document. In the case of PV documents, the Reference Document Trans Code is “SO,” unless the obligation is a prior year obligation and is auto-accrued. In that case, the code is "AR."

### Processing to Accommodate FMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is an Edit FMS Vendor Payment Information option. It is provided in Payment Invoice Tracking to allow the Voucher Audit Clerk to edit the name or payment information. This option creates a VRQ (Vendor Request) transaction to FMS. The VRQ sent to FMS will request that FMS either add the vendor to the FMS vendor file (if the vendor is not in the file), or update the information for the vendor in the vendor file (if the vendor is in the file).

When the request reaches FMS, it is reviewed by the Austin Vendorizing Unit.” This team investigates each request to determine whether the FMS vendor file should be changed based on the request. If the team determines that the request is valid, FMS will return the values that IFCAP sent on a VUP (Vendor Update) transaction. If the Austin Vendorizing Unit determines that the request is invalid, it will return corrected values for the fields that IFCAP sent it on the VRQ. In either case, the field values on the VUP returned from FMS will be used to overwrite the same fields in the IFCAP vendor file to keep the IFCAP vendor file in sync with the FMS vendor file.

During the entry of a new invoice or a change to an incomplete invoice, the Voucher Audit Clerk may add a vendor, if none was specified on the 1358.

# New Invoice

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Invoice Tracking process starts with the invoice received at the station. The invoice is then reviewed and logged into the IFCAP Payment/Invoice Tracking module where its movement thru the process is monitored. Options listed below are used to process the Invoice and move it to the Accounting Technician.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: New Invoice

## Get Tracking Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the Station number. At the Enter Invoice Tracking Number: prompt, enter N for new. IFCAP will add a new number to the invoice-tracking file. Record this number on the invoice. This will be the invoice tracking ID number.

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, NV

Enter Invoice Tracking Number: N

Are you adding '2' as a new INVOICE TRACKING (the 2ND)? No// Y (Yes)

Adding 2 to Invoice Tracking File.

## Select Order 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Look at the purchase order to make sure that the purchase order is the correct purchase order for the invoice. Enter the purchase order number from the invoice into IFCAP. If you do not know the purchase order number, enter a question mark and IFCAP will list the available purchase order numbers.

Select PAT Number: ?

Enter PO number, Vendor, Fund Control Point, Method of Processing,

Inventory/Distribution Point or Requisition Number.

ANSWER WITH PROCUREMENT & ACCOUNTING TRANSACTIONS

PURCHASE ORDER NUMBER, OR METHOD OF PROCESSING, OR FCP, OR VENDOR

DO YOU WANT THE ENTIRE PROCUREMENT & ACCOUNTING TRANSACTIONS LIST? y (YES)

CHOOSE FROM:

999-C82121 08-10-98 ST Pending Fiscal Action FCP: 101 \$ 366.4

999-C90001 11-10-98 CI Partial Order Received (Amended) FCP: 101 \$ 50

999-C90002 11-17-98 ST Partial Received But Not Obligated FCP: 101 \$ 76.1

999-C90003 11-22-98 ST Complete Order Received But Not Ob FCP: 101 \$ 12.3

999-C90004 11-22-98 ST Complete Order Received But Not Ob FCP: 101 \$ 10

99-C90005 11-24-98 ST Ordered and Obligated (Amended) FCP: 101 \$ 26.85

999-C90006 11-24-98 ST Complete Order Received But Not Ob FCP: 101 \$ 12.3

999-C90007 11-24-98 ST Ordered and Obligated FCP: 101 \$ 20

999-C90008 12-01-98 ST Cancelled Order FCP: 101 \$ 0

999-C90009 12-01-98 ST Ordered and Obligated (Amended) FCP: 101 \$ 20

999-C90010 12-02-98 ST Ordered and Obligated FCP: 101 \$ 30

Select PAT Number: C82121 999-C82121 08-10-98 ST Pending Fiscal Action

FCP: 101 \$ 366.4

## Review Order Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may review an entire purchase order by answering YES to the prompt: Do you need to view the entire PO?. You will see the vendor, the requestor, the total cost, and the description for each line item.

Do you need to view the entire PO? NO// y (YES)

HOOSE 1-5: 1 111-C90001 12-30-98 CI Transaction Complete

FCP: 060 \$ 145.00

Purchase Order \#: 111-C90001 PO Date: DEC 30,1998

FOB: DESTINATION Method of Payment: CERTIFIED INVOICE

Terms: NET 30 P/A: IFBUYER,ONE

FCP: 060 PSYCHIATRY

Vendor: SAM'S OPTICAL

FMS Vendor Code: Alternate Address Indicator:

Ordering Address: Payment Address:

555 TOWN SQUARE 555 TOWN SQUARE

ANYTOWN, VA 99999 ANYTOWN, VA 99999

Do you need to view the entire PO? NO// Y (YES)

PURCHASE ORDER: 111-C90001 STATUS: Transaction Complete

M.O.P.: CERTIFIED INVOICE LAST PARTIAL RECD.:

REQUESTING SERVICE: PSYCHIATRY

VENDOR: IFVENDOR,ONE SHIP TO: 394I STREET RD

1 TOWN BLVD V.A. Medical Center

ANYTOWN, VA 99999 3240 GENESSE ST

555 163 0550 MYTOWN, NJ 99999

DELIVERY HOURS:

\- 4PM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 850400 \| \| FAR 13

TYPE: \*DELIVERY & PURCHASE ORDER\| \|AGENT:

DELIVER ON/BEFORE 1/9/1999 \|CONTRACT: \| IFBUYER,ONE

IFBUYER,ON

DISCOUNT TERM: NET30 \| \|DATE: 12/30/1998

APP: 3690160-060 \| \|ESTIMATED

\| \|TOTAL: 145.00

--------------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

1 STUFF 1 EA 145.00 145.00

Items per EA: 1

BOC: 2580 FMS LINE: 001

\*\*\* ESTIMATED PURCHASE ORDER \*\*\*

END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:

Purchase Order \#: 111-C90001 PO Date: DEC 30,1998

FOB: DESTINATION Method of Payment: CERTIFIED INVOICE

Terms: NET 30 P/A: IFBUYER,ONE

FCP: 060 PSYCHIATRY

Vendor: IFVENDOR,ONE

FMS Vendor Code: Alternate Address Indicator:

Ordering Address: Payment Address:

555 TOWN SQUARE 555 TOWN SQUARE

ANYTOWN, VA 99999 ANYTOWN, VA 99999

## Confirm Order Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you to verify that the purchase order matches the invoice. You may also review other invoices for the Purchase Order. Verify that the vendor is correct for the invoice. You may edit the vendor information if it is incorrect or incomplete. You may also review other invoices for the vendor. At the Certification Required by non-Fiscal Service?: prompt, enter N if the service has already certified the invoice for payment and Y if the invoice will be sent to a Service for certification. Enter the purchase order number, the PO Suffix and the invoice or bill number from the vendor’s invoice. IFCAP will check to see if the invoice number is a duplicate.

Is this the correct Purchase Order for this Invoice? YES// y (YES)

Do you want to review other Invoices for this Purchase Order? NO// N (NO)

Is this the correct Vendor for this Invoice? YES// Y (YES)

Do you want to edit this Vendor's information? NO// N (NO)

Do you want to review other Invoices for this VENDOR? NO// N (NO)

Certification Required by non-Fiscal Service?: YES // Y YES

Purchase Order Number =\> 999-C90001

PO SUFFIX: ??

This is the suffix number assigned by Fiscal for

tracking purposes.

INVOICE/BILL NUMBER: 1 Checking for duplicate invoices . . .

1 8006 129 1023 Transaction Complete 999-C80009-1191

2 8006 170 999-C70037

3 8006 302 Incomplete 111-C90001

4 8006 303 111-C90001

## Enter Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date on the invoice at the Date of Invoice: prompt. Enter the date the invoice was received. Enter the type of prompt invoice payment at the Prompt Pay Type: prompt. Enter the percent discount for prompt payment at the Prompt Payment Terms \#: prompt. Enter the amount of days before the prompt payment deadline at the Discount Days: prompt. IFCAP will add this number to today’s date and ask you to confirm the prompt payment deadline at the Discount Days: prompt.

This filed contains the number of days during which the discount may be taken.

Up to three sets of Prompt Payment Terms may be sent to FMS on the PV document. Enter a 1, 2, or 3 to indicate which set of Terms you want to enter or edit.

DATE OF INVOICE: T (FEB 23, 2000)

DATE INVOICE RECEIVED: TODAY// (FEB 23, 2000)

PROMPT PAY TYPE: NORMAL// NORMAL Normal

Select PROMPT PAYMENT TERMS \#: 1//

DISCOUNT PERCENT: NET//

DISCOUNT DAYS: 30//

Select PROMPT PAYMENT TERMS \#:

## Enter Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the total amount of the Invoice at the Gross Amount of Invoice prompt. Enter any applicable Shipping Charges at the Gross Shipping Charges prompt. Enter the Certifying Official’s name for the Control Point at the Select Certifying Service: prompt. If you wish to accept the invoice for further processing, enter Yes. Entering N will assign the document a status of Incomplete and the user will have to edit the document and change the status to complete the process. If the invoice has not yet been certified, enter N at the, Is this document ready to go to accounting?: prompt and send the invoice to the Certifying Official. If the invoice has been certified, answer Y at the prompt. Enter your electronic signature code. Enter N at the Do You Wish to Enter Another Invoice?: prompt to return to the Payment/Invoice Tracking Menu.

GROSS AMOUNT OF INVOICE: ??

Enter the Gross Amount of Invoice, INCLUDING the shipping charges. The

decimal point must be used if cents are entered. Type a Number between

.01 and 9999999.99, 2 Decimal Digits

GROSS AMOUNT OF INVOICE: 100 \$ 100.00

GROSS SHIPPING: \$ 0.00

Accept invoice for further processing? YES// (YES)

Do you wish to forward this invoice for signature at this time? YES// (YES)

Select CERTIFYING SERVICE: 04 FISCAL 04

DATE DUE IN FISCAL: T+7// (MAR 26, 2000)

Please forward actual invoice to service for signature.

Status is set to 'Pending Service Certification'.

Do you wish to enter another invoice? YES// n (NO)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option

# LOG-IN CERTIFIED INVOICES FROM SERVICES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains how to record the return of certified invoices from the services. This option changes the status of the invoice to "Awaiting Voucher Audit Review."

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Review VENDOR REQUEST (this option will appear if Fiscal reviews Vendor requests)

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: Log-in Certified Invoices from Services

This option allows you to check in documents from the services.

It sets the current location as Fiscal and shows the status as

'Awaiting Voucher Audit Review'.

## Processing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can choose to process each invoice for payment as you check them in from the requesting service, or just record the return of the invoice to Fiscal. If you answer 'YES,' you will be prompted for the items necessary to complete the Voucher Audit information. If you answer N at the Do You Wish To Process Each Document As It Is Checked In?: prompt, you will have to process each document by using the Approve Payment of Invoices Already Checked In option under the Payment /Invoice Tracking Menu. If the Invoice was not approved, use the option to record the return of the Invoice to FISCAL and enter the Approved amount of zero. Logging the Invoice in through this option will halt the generation of overdue bulletins for this Invoice. Enter a station number. Enter the Section or Service accepting receipt of the document. Enter the invoice tracking number. If you do not know the invoice tracking number, enter three question marks at the prompt and IFCAP will list the available invoices. Chapter 4 in this manual discusses approving payment of invoices already checked in.

Do you wish to process each document as it is checked in? YES// (YES)

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, NV

Select Fiscal Section Accepting Receipt of Document: ???

Choose from:

6 FISCAL 04

Select Fiscal Section Accepting Receipt of Document: 6 FISCAL 04

...OK? Yes// (Yes)

Select/Barcode INVOICE TRACKING NUMBER: ???

Choose from:

1 1 C00002 Pending Service Certification 999-C00002

3 3 1 Pending Service Certification 999-C00002

4 4 1 Pending Service Certification 999-C90002

Select/Barcode INVOICE TRACKING NUMBER: 1 C00002 Pending Service Certification 999-A00002

## Enter Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the amount of the invoice that is certified for payment. Enter the amount approved to pay for shipping costs for the invoice. Enter the date that the goods were received. If the amount certified is less than the amount of the invoice, IFCAP will display the prompt 'Suspension Letter Required?:' Enter Y is you want to send a suspension letter to the vendor explaining why you are not paying the entire invoice balance/ Enter Y at the Is This Document Ready To Go To Accounting? prompt. Enter your electronic signature code. Press the Enter key at the Select/Barcode Next Invoice Tracking Number: prompt to return to the Payment/Invoice Tracking Menu.

Amount of Invoice =\> \$ 6910.00

AMOUNT CERTIFIED FOR PAYMENT: 6,910.00// \$ 6910.00

Shipping on Invoice =\> \$ 1.00

APPROVED SHIPPING AMOUNT: 1.00// \$ 1.00

DATE GOODS/SERVICE RECEIVED: T (JUL 29, 1994) Data appears OK for payment.

Is this document ready to go to accounting? YES// (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Status has been changed from 'Awaiting Voucher Audit Review'

to 'In Accounting'.

Select/Barcode Next INVOICE TRACKING NUMBER:

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option:

# APPROVE PAYMENT OF INVOICES ALREADY CHECKED IN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you approve payment of invoices already checked in, IFCAP sends the invoice to the Accounting Technician who processes it and transmits a PV document to the Austin Finance Center (AFC). The AFC generates the actual payment to the vendor. It is important to approve payment of invoices in a timely fashion. Delinquent payments disqualify Control Points from receiving prompt payment discounts. If an invoice was not approved for payment at the time it was logged into the Payment/Invoice Tracking system, you can use the Approve Payment of Invoices Already Checked In option to process the Invoice and pass it to the Accounting Technician for payment processing.

## Approve 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the Station number and select an Invoice to process. Enter the tracking number of the Invoice you wish to process.

Select OPTION NAME: APPROVE PAYMENT OF INVOICES AL PRCFD APPROVE PAYMENT

Approve Payment of Invoices Already Checked in

Approve Payment of Invoices Already Checked in

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, NV

Select/Barcode INVOICE TRACKING NUMBER: ??

21 21 MI0002 Awaiting Voucher Audit Review 999-C70007

30 30 ERC0001 Awaiting Voucher Audit Review 999-C70009

## Edit Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user will be given the opportunity to edit the basic invoice information if needed. The purchase order may be displayed.

Select Payment/Invoice Tracking Menu Option: APProve Payment of Invoices Already

Checked in

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, NV

Select/Barcode INVOICE TRACKING NUMBER: 307 AMS1234

Awaiting Voucher Audit Review 999-C00001-0033

Do you wish to edit any of the basic invoice information? NO// Y (YES)

Select PAT Number: 999-C00001//

Purchase Order \#: 999-C00001 PO Date: OCT 15,1999

FOB: DESTINATION Method of Payment: CERTIFIED INVOICE

Terms: NET 30 P/A: IFBUYER,TWO

FCP: 060 Fiscal Service

Vendor: SAMPLCO INTERNATIONAL

FMS Vendor Code: 930867113 Alternate Address Indicator: 05

Ordering Address: Payment Address:

100 BOULEVARD DEPT LA 21061

SUITE 110 2222 WEST STREET

ROOM 10, POD 12 PASADENA, CA 91185

ANYTOWN, GA 11111

Do you need to view the entire PO? NO// Y (YES)

## View Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may view the purchase order.

PURCHASE ORDER: 999-C00001 STATUS: Pending Fiscal Action

M.O.P.: CERTIFIED INVOICE LAST PARTIAL RECD.:

REQUESTING SERVICE: FISCAL

VENDOR: IFVENDOR,TWO SHIP TO: ANYTOWN VAMC

1000 ALLIES V.A. Medical Center

SUITE 110 50 TOWNSHIP Street, NW

ROOM 10, POD 1 ANYTOWN, NV 99999

ANYTOWN, GA 11111

555-333-8888

FMS Vendor Code: 93086711305

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 842000 \| \| FAR 13

TYPE: DELIVERY ORDER \| \|AGENT:

DELIVER ON/BEFORE 10/15/1999 \|CONTRACT: \| IFBUYER,TWO

DISCOUNT TERM: NET30 \| V999-E540206 \|DATE: 10/15/1999

APP: 3600160-060 \| \|ESTIMATED

\| \|TOTAL: 200.00

--------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

-----------------------------------------------------------------------------

1 Service on copier 4 HR 50.00 200.00

BOC: 2580 FMS LINE: 001 CONTRACT: V999-E540206

\*\*\* ESTIMATED PURCHASE ORDER \*\*\*

END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:

## Information Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the purchase order number, whether the vendor has included shipping charges on the invoice (FOB: Destination) or if shipping costs are due upon delivery (FOB: Origin). IFCAP will also list the terms of payment, the purchasing agent who created the purchase order, and the Fund Control Point for the purchase order. IFCAP will also list the vendor, the ordering address and the payment address.

Purchase Order \#: 999-C00001 PO Date: OCT 15,1999

FOB: DESTINATION Method of Payment: CERTIFIED INVOICE

Terms: NET 30 P/A: IFBUYER,TWO

FCP: 060 Fiscal Service

Vendor: SAMPLCO INTERNATIONAL

FMS Vendor Code: 930867113 Alternate Address Indicator: 05

Ordering Address: Payment Address:

1000 ALLIES DEPT LA 21061

SUITE 110 2222 WEST STREET

ROOM 10, POD 1 PASADENA, CA 91185

ANYTOWN, GA 11111

## Confirm Order Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you to confirm that the purchase order is the correct purchase order for the invoice. You may review other invoices for the purchase order, or review other invoices for the vendor. Enter Y at the Is Certification Required? prompt if the requesting service has to certify payment before the invoice is paid. If so, enter whether the service has certified the invoice. Enter the purchase order suffix, if there is one. The purchase order suffix is a number that Fiscal Service assigns to the purchase order for tracking purposes. At the Invoice/Bill Number: prompt, enter the vendor's invoice number or bill number. IFCAP will check for duplicate invoices. If IFCAP finds a duplicate invoice, you will receive a message stating that the invoice was a duplicate. Enter the date the vendor assigned to the invoice, the date that the VA received the invoice, and the invoice type. Enter the terms of prompt payment established with the vendor.

Is this the correct Purchase Order for this Invoice? YES// (YES)

Do you want to review other Invoices for this Purchase Order? NO// (NO)

Is this the correct Vendor for this Invoice? YES// (YES)

Do you want to edit this Vendor's information? NO// (NO)

Do you want to review other Invoices for this VENDOR? NO// (NO)

Certification Required by non-Fiscal Service?: YES

// N NO

Purchase Order Number =\> 999-C00001

PO SUFFIX: 0033//

INVOICE/BILL NUMBER: AMS1234// Checking for duplicate invoices . . .

none found.

DATE OF INVOICE: JUN 3,2000//

DATE INVOICE RECEIVED: JUN 5,2000//

## Enter Discount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the discount percent for prompt payment, and the amount of days from the date on the invoice before the prompt payment term expires. A maximum of three Prompt Payment Terms may be entered for a single Invoice. Enter the gross invoice amount and gross shipping charges.

> **NOTE:** IFCAP asks for the gross amount because the prompt payment discount has yet to be determined and the amount certified might be less than the amount on the invoice.

IFCAP will ask you to confirm the invoice amount and shipping charges. Enter the date that the goods or services were received. Forward the invoice record to accounting. Enter your electronic signature code. Press the Enter key at the Select/Barcode Next Invoice Tracking Number: prompt to return to the Payment/Invoice Tracking Menu.

PROMPT PAY TYPE: NORMAL// Normal

Select PROMPT PAYMENT TERMS \#: 1//

PROMPT PAYMENT TERMS \#: 1//

DISCOUNT PERCENT: NET//

DISCOUNT DAYS: 30//

Select PROMPT PAYMENT TERMS \#:

GROSS AMOUNT OF INVOICE: 195.00// \$ 195.00

GROSS SHIPPING: 5.00// \$ 5.00

Accept invoice for further processing? YES// (YES)

Amount of Invoice =\> \$ 195.00

AMOUNT CERTIFIED FOR PAYMENT: 195// \$ 195.00

Shipping on Invoice =\> \$ 5.00

APPROVED SHIPPING AMOUNT: 5// \$ 5.00

DATE GOODS/SERVICE RECEIVED: 052500 (MAY 25, 2000)

Data appears OK for payment.

Is this document ready to go to accounting? YES// (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Status has been changed from 'Awaiting Voucher Audit Review'

to 'In Accounting'

# VIEW CERTIFIED INVOICE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: View Certified Invoice

## Select Invoice Tracking Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number. Enter an invoice tracking ID number. If you do not know the invoice ID number, enter three question marks at the prompt and IFCAP will list the available invoices.

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN,NV

Select INVOICE TRACKING ID NUMBER: ???

CHOOSE FROM:

8 8 1 In Accounting 999-6969

9 9 123 In Accounting 999-C40208

10 10 343434 Transaction Complete 999-C40209

11 11 THX-1138 In Accounting 999-C12121

12 12 3 Awaiting Voucher Audit Review 999-C40412

13 13 1 In Accounting 999-C40407

Select INVOICE TRACKING ID NUMBER: 10 343434 Transaction Complete 999-C40209

## Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the "Invoice Tracking List," comprehensive information about the invoice, the purchase order, the terms of payment, and the status of the purchase order. It also displays certification data about the invoice for payment and the Service for which the purchase order was created. Enter a caret (^) at the Select Station Number: prompt to return to the Payment/Invoice Tracking Menu.

INVOICE TRACKING LIST JUL 29,1994 12:57 PAGE 1

--------------------------------------------------------------------------------

ID NUMBER: 10 DOCUMENT LOCATOR NUMBER: 03247999002

INVOICE/BILL NUMBER: 343434 DATE OF INVOICE: FEB 1, 1994

DATE INVOICE RECEIVED: FEB 1, 1994

PROMPT PAY TYPE: MONEY MANAGEMENT EXEMPT - NORMAL

PURCHASE ORDER POINTER: 999-A40209 VENDOR: IFVENDOR,THREE

DISCOUNT DAYS: 0 DISCOUNT TERMS: STANDARD

AMOUNT CERTIFIED FOR PAYMENT: \$60.00 LIQUIDATION CODE: COMPLETE

LIQUIDATION AMOUNT 1: \$6,000.00

DATE GOODS/SERVICE RECEIVED: FEB 1, 1994

PAYMENT TO BE SENT TO: : FMS CERTIFICATION REQUIRED?: YES

STATION NUMBER: 999

PURCHASE ORDER NUMBER: 999-C40209 GROSS AMOUNT OF INVOICE: \$60.00

NET DAYS: 30 STATUS: Transaction Complete

EXPANDED PO NUMBER: 999-C40209 CURRENT INVOICE LOCATION: FISCAL

D/T CHARGED TO CURRENT LOC: FEB 1, 1994@11:07

NET PAYMENT DATE: MAR 3, 1994 DATE RETURNED TO FISCAL: FEB 1, 1994

CERTIFIED FOR PAYMENT BY: IFBUYER,THREE

CERTIFIED BY VALIDATION CODE: /ES/ IFBUYER,THREE

CHARGED TO CURRENT LOCATION BY: IFBUYER,THREE

CERTIFIED BY VALIDATION VER: 1 CERTIFIED BY ESIG CODE: 7793

CERTIFIED BY SIG DATE/TIME: FEB 1, 1994@11:08:02

CERTIFYING SERVICE: FISCAL

DATE/TIME CHARGED OUT: FEB 1, 1994@11:06

CHARGED BY: IFBUYER,THREE

CERTIFYING SERVICE: FISCAL

DATE/TIME CHARGED OUT: FEB 1, 1994@11:07

CHARGED BY: IFBUYER,THREE

# CREATE/REPRINT A SUSPENSION LETTER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP users may create a suspension letter whenever the payment to the vendor is less than the amount requested on the Invoice. Suspension letters explain to the vendor why the invoice is not being paid in full and list the amount you are deducting from the invoice payment.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option:

## Enter Tracking ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter an invoice tracking ID number. If you do not know the invoice ID number, enter three question marks at the prompt and IFCAP will list the available invoice numbers. Enter Y at the Suspension Letter Required?: prompt to create a suspension of payment letter. Enter or edit the reason for the suspension. Print the letter. Select an output device.

Select INVOICE TRACKING ID NUMBER: ??

DEVICE:

295295 1 Transaction Complete 999-C95017-1

296 296 2 Transaction Complete 999-C95017-1

297 297 3 Transaction Complete 999-C95017-1

298 298 4 In Accounting 999-C95017-1

299 299 991234 In Accounting 999-C95017-1

304 304 898778 Pending Service Certification 111-C90001

305 305 12345 Incomplete 999-C90008

306 306 y8987 In Accounting 999-C00014

Select INVOICE TRACKING ID NUMBER: 306 y8987 In Accounting 999-C00014

SUSPENSION LETTER REQUIRED?: YES//

REASON FOR SUSPENSION:

1\>Repairs not completed. Waiting for a part. Repairman is to return

2\>when part is delivered.

3\>Labor charges were \$650.00. Part could not be installed - not correct

4\>part.

EDIT Option:

Are you ready to print the letter? YES// (YES)

## Suspension Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will create a suspension of payment letter, listing the vendor address, the vendor contact, and the deduction. You may use this letter to inform the vendor of the deduction. Press the Enter key at the Select Invoice Tracking ID Number: prompt to return to the Payment/Invoice Tracking Menu.

IFVENDOR,FOUR

2 North Plaza

TOWNSHIP, North Dakota 54345

Your recent claim voucher - Invoice Number y8987 - has been

approved, and a check will be forwarded promptly.

As explained below it was necessary to make a deduction from

the amount claimed. If a credit memo is issued to clear

your accounting records of this overcharge, DO NOT send us a

copy.

Should you submit a reclaim voucher, please return this

letter with it and also enclose a supporting statement or

additional evidence substantiating your claim.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Amount Claimed: \| Amount Deducted: \| Amount Approved:

\| \|

\$750.00 \| \$100.00 \| \$650.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Repairs not completed. Waiting for a part. Repairman is to

return when part is delivered. Labor charges were \$650.00.

Part could not be installed - not correct part.

Sincerely,

Fiscal (04)

50 Ivy Street

ANYTOWN, District Of Columbia 20002

Fiscal

2000 Main St

Suite 3

Silver Spring, Maryland 20910

Select INVOICE TRACKING ID NUMBER:

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option:

# DELETE CERTIFIED INVOICE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to delete incomplete certified invoices. IFCAP will only allow you to delete certified invoices with a status of Incomplete.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: Delete Certified Invoice

## Select Invoice Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number. Enter a certified invoice number. If you do not know the invoice number, enter three question marks and IFCAP will list the available invoice numbers.

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN,NV

Select CERTIFIED INVOICE: ???

CHOOSE FROM:

5 5 5 Incomplete 999-C40007

30 30 1 Incomplete 999-C40301

32 32 Incomplete 999-C40301

Select CERTIFIED INVOICE: 32 Incomplete 999-C40301

## Delete Invoice

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you to confirm that you want to delete the invoice, and return to the Payment/Invoice Tracking Menu.

Are you SURE you want to delete this record? NO// Y (YES)

Certified Invoice Record Deleted

Select Payment/Invoice Tracking Menu Option:

# EDIT FMS VENDOR PAYMENT INFORMATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users have to edit FMS vendor payment information to ensure that payments go to the correct vendor and address. When you send vendor information to FMS, FMS sends a Vendor Update (VUP) to IFCAP, ensuring that the IFCAP vendor file corresponds to the FMS vendor table. Vendors that your facility uses more than once have to be established in the Austin Finance Center database. This policy expedites payment, because many VA offices use the same vendors. The Austin Finance Center also generates the tax forms for established vendors.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: Edit FMS Vendor Payment Information

## Select Vendor 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number. Enter a vendor name. You can enter a new vendor if you like. IFCAP will list the current FMS vendor information on the vendor, and ask you to confirm that you want to edit the information.

Edit FMS Vendor Payment Information

Select VENDOR NAME: IFVENDOR,FIVE IFVENDOR,FIVE PH:555 288-1999 NO: 40386

PAY ADD:477 MYTOWN FMS: IFVENDOR,FIVE

MYTOWN, CA 11111 CODE:T05257589 FAX:

...OK? Yes// (Yes)

Review current payment information on this Vendor? YES//

Edit FMS Vendor Payment Information

Payment Information

Vendor Name: IFVENDOR,FIVE

Vendor Number: 40386 Non-Recurring/Recurring: RECURRING

FMS Vendor Code: 405257588

Alternate Address Indicator:

Address: 477 MYTOWN

MYTOWN, CA 11111

Edit the payment information on Vendor record? YES//

## Edit Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can enter or edit the vendor name, the tax or Social Security number, the payment contact person, the phone number to contact for payment information, and the payment address. Enter Y at the 1099 Vendor Indicator: prompt if a 1099 form is completed for the vendor. A 1099 form is an IRS form for reporting self-employed income.

Edit FMS Vendor Payment Information

NAME: IFVENDOR,FIVE Replace

TAX ID/SSN: 000057555

SSN/TAX ID INDICATOR: T

FMS VENDOR CODE: 000057555//

ALT-ADDR-IND:

PAYMENT CONTACT PERSON: IFVENDOR,SIX

PAYMENT PHONE NO.: 555-876-0000

ORDERING ADDRESS: 999 BAY DRIVE

MYTOWN, CALIFORNIA 11111

PAYMENT ADDRESS1: 477 MYTOWN//

PAYMENT ADDRESS2:

PAYMENT CITY: MYTOWN//

PAYMENT STATE: CALIFORNIA//

PAYMENT ZIP CODE: 11111//

1099 VENDOR INDICATOR: NO//

## Enter Vendor Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a vendor type. If you do not know the appropriate vendor type for the vendor, enter three question marks and IFCAP will list the available vendor types. Enter a Dun & Bradstreet number for the vendor if one is available. After the edit of the information is done, IFCAP will determine if a VRQ needs to be sent to the Austin Vendorizing unit. Press the Enter key at the Select Vendor Name: prompt to return to the Payment/Invoice Tracking Menu.

VENDOR TYPE: COMMERCIAL// ???

Choose from:

A AGENT CASHIER

C COMMERCIAL

E EMPLOYEE

F FEDERAL GOVERNMENT

G GSA

I INDIVIDUALS-OTHER

O OTHER COUNTRIES

R COMMERCIAL-RECURRING PMTS

U UTILITY COMPANIES

V VETERANS

K CANTEEN

VENDOR TYPE: COMMERCIAL//

DUN & BRADSTREET \#:

The system determined that no VRQ needed or could be created.

Select VENDOR NAME:

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option:

# GENERATE OVERDUE INVOICE BULLETINS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Overdue invoice bulletins remind the service to review and certify the invoice and return it to Fiscal so the vendor can be paid. The Generate Overdue Invoice Bulletins option allows the Voucher Auditor to manually generate electronic messages to the Control Point Clerks and Officials notifying them of overdue invoices. This option may be scheduled to run automatically each day. Contact your ADPAC or IRM staff if you wish to have the option set up as a Tasked job.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: Generate Overdue Invoice Bulletins

## Enter Date and Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will describe the option you selected, and ask you to confirm the option. Enter a station number. Enter the date and the time that you would like IFCAP to send the bulletins. IFCAP will send overdue invoice bulletins to the services in the form of MailMan messages. IFCAP will return to the Payment/Invoice Tracking Menu.

Select Payment/Invoice Tracking Menu Option: Generate Overdue Invoice Bulletins

This Option Generates Messages to those services having outstanding

and late certified invoices.

OK to Continue? YES// (YES)

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN,NV

Enter DATE & TIME to run. NOW// (OCT 21, 1994@11:32) \<Request Queued\>

# HISTORY - CODE SHEET/OBLIGATION (PAT) NUMBER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains how to create a report of all the code sheets that were created for a particular Procurement and Accounting Transaction (PAT) number. PAT numbers are defined by the common accounting numbering series in MP-4, Part V. The report will list each PAT number, the date it was assigned to a request, the FMS documents created for it, and who approved each document.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: History - Code Sheet/Obligation (PAT) Number

## Select Order Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a purchase order number. If you do not know the purchase order number, enter three question marks at the Purchase Order Number: prompt and IFCAP will list the available purchase order numbers. Enter another purchase order at the Another One: prompt, or press the Enter key. You may view the entire order including amendments and receiving reports if necessary.

PURCHASE ORDER NUMBER: ???

36 A90033 999-A90033 01-13-99 ST Pending Contracting Officers Signa

FCP: 060 \$ 0.00

37 A90034 999-A90034 01-13-99 ST Ordered and Obligated

FCP: 060 \$ 36.00

38 A90035 999-A90035 01-14-99 ST Partial Order Received (Amended)

FCP: 060 \$ 150.00

39 A90036 999-A90036 01-14-99 ST Transaction Complete (Amended)

FCP: 060 \$ 375.00

40 A90037 999-A90037 01-21-99 ST Partial Order Received

FCP: 060 \$ 25.00

CHOOSE 1-40: 39 999-A90036 01-14-99 ST Transaction Complete (Amended)

FCP: 060 \$ 375.00

ANOTHER ONE:

PURCHASE ORDER NUMBER: 999-A90036

DATE: 1/14/1999 FCP: 060 FISCAL SERVICES

STATUS: Transaction Complete (Amended)

VENDOR: IFVENDOR,TWO TOTAL: 375.00

FMS DOCUMENT(S):

TT/SC TR DATE REF SIG DATE/TIME SIGNED BY:

MO.E 011499 A90036 JAN 14, 1999@15:09:27 SILVA,REGINA

RR.E 011499 A90036 JAN 14, 1999@15:13:46 SILVA,REGINA

RR.M 011499 A90036 JAN 14, 1999@15:19:46 SILVA,REGINA

RR.E 011499 A90036 JAN 14, 1999@15:26:12 SILVA,REGINA

Would you like to review the entire purchase order? NO// y (YES)

PURCHASE ORDER: 999-A90036 STATUS: Transaction Complete (Amended)

M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.: 3 01/14/99

REQUESTING SERVICE: FISCAL

VENDOR: IFVENDOR,TWO SHIP TO: ANYTOWN VAMC

1000 BOULEVARD V.A. Medical Center

SUITE 110 50 TOWNSHIP Street, NW

ROOM 10, POD 1 ANYTOWN, NV 99999

ANYTOWN, GA 11111

555-333-8888

FMS Vendor Code: 93086711305

\*EDI ORDER\* DO NOT MAIL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 842100 \| \| FAR 13

TYPE: PURCHASE ORDER \|AGENT:

DELIVER ON/BEFORE 1/24/1999 \|CONTRACT: \| IFBUYER,FOUR

DISCOUNT TERM: NET30 \| \|DATE: 1/14/1999

APP: 3690160-060 \| \|

\| \|TOTAL: 375.00

--------------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

1 Test MWV-0698-22266 5 EA 75.00 375.00

QTY PREV RCVD: 5

PARTIAL NO.: 1,2,3

Items per EA: 1

BOC: 2660 FMS LINE: 001

AMENDMENT NUMBER: 1 EFFECTIVE DATE: 1/14/1999

Adjustment Voucher for Purchase Order 999-A90036

Item No. 1 MWV-0698-22266

Items per EA: 1

5 EA at \$ 75.00 = \$ 375.00

ORIGINALLY QTY RECEIVED = 5 ,COST = \$ 375

will now read: QTY RECEIVED=3, COST=\$225

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

Vendor: IFVENDOR,TWO

APPROPRIATION: 3690160

This Receiving Report will now read:

Total Amount: 225

Review a Receiving Report ? NO// Yes

Select PARTIAL DATE: ?

Answer with PARTIAL NUMBER, or DATE

Choose from:

1 JAN 14, 1999

2 JAN 14, 1999

3 JAN 14, 1999@12:00

Select PARTIAL DATE:

Select PARTIAL DATE: 1 1-14-1999

PURCHASE ORDER: 999-A90036 STATUS: Transaction Complete (Amended)

PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 1 1/14/1999

--------------------------------------------------------------------------------

UNIT QTY TOTAL

ITEM DESCRIPTION QTY UNIT COST REC COST

--------------------------------------------------------------------------------

1 Test MWV-0698-22266 5 EA 75.00 5 375.00

Total Amount: 375.00

Processed By: /ES/ IFBUYER,FOUR

ENTER \<CR\> TO CONTINUE

Select PARTIAL DATE:

# INCOMPLETE INVOICE EDIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are interrupted during the data entry process, the invoice will have a status of 'Incomplete.' An invoice will remain in the incomplete status until you have entered appropriate data and either sent the invoice to the service for certification or transmitted the required information to Fiscal for payment processing.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: Incomplete Invoice Edit

## Enter Tracking ID 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number and an invoice tracking ID number. If you do not know the invoice ID number, enter three question marks at the prompt and IFCAP will list the available invoice numbers. Enter the PAT number for the invoice. The PAT number is the primary reference number used to determine the payment status of invoices.

Select Payment/Invoice Tracking Menu Option: INComplete Invoice Edit

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, NV

Select INVOICE TRACKING ID NUMBER: 306 y8987 Incomplete 999-C00014

Select PAT Number: 999-C00014//

## Display Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the purchase order number, whether the vendor has included shipping charges on the invoice (FOB: Destination) or if shipping costs are due upon delivery (FOB: Origin). IFCAP will also list the terms of payment, the purchasing agent who created the purchase order, and the Fund Control Point for the purchase order. IFCAP will also list the vendor, the ordering address and the payment address.

Purchase Order \#: 999-C00014 PO Date: APR 10,2000

FOB: DESTINATION Method of Payment: CERTIFIED INVOICE

Terms: NET 30 P/A: IFBUYER,ONE

FCP: 060 Fiscal Service

Vendor: IFVENDOR,FOUR

FMS Vendor Code: 780000987 Alternate Address Indicator

Ordering Address: Payment Address:

301 GRAND PLACE 23 NEW ROAD

MONTVALE, NJ 07645 TOWNSHIP, ND 54345

Do you need to view the entire PO? NO//

## View Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may view the entire purchase order if you like. IFCAP will ask you to confirm that the purchase order is the correct purchase order for the invoice. You may review other invoices for the purchase order, or review other invoices for the vendor. If the requesting service has already certified the invoice for payment Enter N at the Is Certification Required prompt\> Enter the purchase order suffix, if there is one. The purchase order suffix is a number that Fiscal Service assigns to the purchase order for tracking purposes. At the Invoice/Bill Number: prompt, enter the vendor's invoice number or bill number. IFCAP will check for duplicate invoices. If IFCAP finds a duplicate invoice, you will receive an electronic mail message stating that the invoice was a duplicate. Enter the date the vendor assigned to the invoice, the date that the VA received the invoice, and the invoice type. Enter the terms of prompt payment established with the vendor.

Is this the correct Purchase Order for this Invoice? YES// (YES)

Do you want to review other Invoices for this Purchase Order? NO// (NO)

Is this the correct Vendor for this Invoice? YES// (YES)

Do you want to edit this Vendor's information? NO// (NO)

Do you want to review other Invoices for this VENDOR? NO// (NO)

Certification Required by non-Fiscal Service?: NO

//

Purchase Order Number =\> 999-C00014

PO SUFFIX: 22//

INVOICE/BILL NUMBER: y8987// Checking for duplicate invoices . . .

none found.

DATE OF INVOICE: APR 10,2000//

DATE INVOICE RECEIVED: APR 10,2000//

PROMPT PAY TYPE: NORMAL// Normal

## Enter Discount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the percent of discount for the prompt payment at the Discount Percent: prompt. Enter the number of days discount will be effective at the Discount Days: prompt. Enter the total of the Invoice at the Gross Amount of Invoice: prompt and, if applicable, enter the shipping amount at the Gross Amount of Shipping: prompt. If the Invoice is not ready for further processing enter N. Forward the invoice to the service for signature if required. Enter the service to which the invoice will be sent, and the date that the invoice is due in Fiscal Service. IFCAP will change the status of the invoice to "Pending Service Certification."

Enter Y to accept the invoice for further processing. Enter Y to process the Invoice for payment immediately. Enter the amount of the Invoice. If the amount certified for payment is different than the default amount, the user may change it. Enter the approved Shipping amount. Enter the Date the Goods/services were received. If the amount approved for payment is less than the Invoice amount the user will have an opportunity to generate a Suspension letter and enter the reason for the difference in payment amount. Enter the printer device where the Suspension letter is to print. Enter your electronic signature code. The status will be changed to “In Accounting.” You can edit another incomplete invoice or return to the Payment/Invoice Tracking Menu.

Select PROMPT PAYMENT TERMS \#: 1//

PROMPT PAYMENT TERMS \#: 1//

DISCOUNT PERCENT: NET//

DISCOUNT DAYS: 30//

Select PROMPT PAYMENT TERMS \#:

GROSS AMOUNT OF INVOICE: 650.00// 750.00 \$ 750.00

GROSS SHIPPING: 0.00// \$ 0.00

Accept invoice for further processing? YES// (YES)

Do you wish to process this item for payment now? YES// (YES)

Amount of Invoice =\> \$ 750.00

AMOUNT CERTIFIED FOR PAYMENT: 750// 650.00 \$ 650.00

Shipping on Invoice =\> \$ 0.00

APPROVED SHIPPING AMOUNT: 0 \$ 0.00

DATE GOODS/SERVICE RECEIVED: T (APR 10, 2000)

Amount Certified is less than Amount Invoiced.

SUSPENSION LETTER REQUIRED?: Y YES

REASON FOR SUSPENSION:

1\>Repairs not completed. Waiting for a part. Repairman is to return

2\>when part is delivered.

3\>Labor charges were \$650.00. Part could not be installed - not correct part.

4

EDIT Option:

Do you wish to print the suspension letter at this time? NO //

Is this document ready to go to accounting? YES// (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Status has been changed from 'Incomplete'

to 'In Accounting'

# PRINT CERTIFIED INVOICE OVERDUE REPORTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users print certified invoice overdue reports to ensure that Control Points return invoices in time to receive prompt payment discounts.

## Menu Path 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: Print Certified Invoice Overdue Reports

## Enter Printer Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Choose an output device. IFCAP will list each certified invoice due for payment under a discount for prompt payment and each certified invoice due for net payment, grouped by invoice location (for example, 'In Fiscal,' Pending Service Certification,' 'Awaiting Voucher Audit Review'). After printing the list, IFCAP will return to the Payment/Invoice Tracking Menu.

DEVICE: LAT

Select Payment/Invoice Tracking Menu Option: PRINt Certified Invoice Overdue Rep

orts

DEVICE: UCX/TELNET

CERTIFIED INVOICES DUE FOR DISCOUNT PAYMENT APR 10,2000 18:01 PAGE 1

DISCOUNT GROSS

PAYMENT NET PAYMENT INVOICE

ID NUMBER P.O. \# DATE DATE AMOUNT

STATUS

--------------------------------------------------------------------------------

CURRENT INVOICE LOCATION: MEDICAL ADMINISTRATION

304 111-C90001 APR 21,2000 APR 6,2000 18.00

Pending Service Certification

CERTIFIED INVOICES DUE FOR NET PAYMENT APR 10,2000 18:01 PAGE 1

GROSS

NET PAYMENT INVOICE

ID NUMBER P.O. \# DATE AMOUNT

STATUS

--------------------------------------------------------------------------------

CURRENT INVOICE LOCATION: FISCAL

299 999-C95017 OCT 16,1999 10.00

In Accounting

CURRENT INVOICE LOCATION: MEDICAL ADMINISTRATION

304 111-C90001 APR 6,2000 18.00

Pending Service Certification

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option:

# RECHARGE AN INVOICE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an invoice is sent (charged) to the wrong service, use this procedure to charge the invoice to the correct service. This option allows Fiscal Service to reassign the invoice from one service to another.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: Recharge an Invoice

## Enter Tracking ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number and an invoice tracking ID number. If you do not know the invoice ID number, enter three question marks at the prompt and IFCAP will list the available invoice numbers.

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, NV

Select INVOICE TRACKING ID NUMBER: ???

Choose from:

3 3 1 Pending Service Certification 999-C00002

4 4 1 Pending Service Certification 999-C90002

Select INVOICE TRACKING ID NUMBER: 1 C00002 Awaiting Voucher Audit Review 999-A00002

## Display Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the service to which the invoice is presently charged and ask the user to confirm they want to charge it to another service. Enter the service name. IFCAP will change the status of the invoice to "Pending Service Certification," if the invoice was not already at that status. The Date due in Fiscal may be changed if necessary. Enter N at the Do You Want To Recharge Another Invoice?: prompt to return to the Payment/Invoice Tracking Menu.

Invoice is currently in FISCAL.

Do you want to recharge it to someone else? YES//

Select SERVICE/SECTION NAME: 2 INFORMATION SYSTEMS CENTER

...OK? Yes// (Yes)

DATE DUE IN FISCAL: MAR 21,2000//

Recharge Completed.

Status has been changed from 'Awaiting Voucher Audit Review'

to 'Pending Service Certification'.

Do you want to recharge another invoice? NO// (NO)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option:

# SEND CERTIFIED INVOICE DUE BULLETIN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is tasked to run nightly, to generate bulletins for CI’s due in 7 days, but the user can select this option from the menu to generate the CI’s due bulletins at any time. Both the invoice number and the PO number are added to the mail message. This option alerts the service that an Invoice is due back in Fiscal in 7 days. This option is different from the Generate Overdue Bulletins because this option advises the Service they have an Invoice pending certification 7 days before that Invoice becomes Overdue.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Invoice

Log-in Certified Invoices from Services

Approve Payment of Invoices Already Checked in

View Certified Invoice

Create/Reprint a Suspension Letter

Delete Certified Invoice

Edit FMS Vendor Payment Information

Generate Overdue Invoice Bulletins

History - Code Sheet/Obligation (PAT) Number

Incomplete Invoice Edit

Print Certified Invoice Overdue Reports

Recharge an Invoice

Send CI's Due Bulletin

Select Payment/Invoice Tracking Menu Option: Send CI's Due Bulletin

## Select Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number. IFCAP will ask you to confirm that you want to generate the bulletin, and queue the output to the printer. IFCAP will return to the Payment/Invoice Tracking Menu.

Select STATION NUMBER ('^' TO EXIT): 999// ANYTOWN, NV

This option generates bulletins to those services having

a Certified Invoice due in Fiscal on MAR 21, 2000.

This job is scheduled to run on a daily basis

Are you sure you want to run this option manually?

Okay to continue? YES

Request Queued.

# GLOSSARY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 68%" />
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
<td>The last two digits of the AACS number. Each station defines it.</td>
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
<td>The C prefix number that Fiscal Service assigns to the 1358.</td>
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
<td>A Control Point listing of all transactions (Ceilings, Obligations, and Adjustments) made against a Control Point's Funds.</td>
</tr>
<tr class="even">
<td><strong>Quotation for Bid</strong></td>
<td>Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors. May be created automatically and transmitted electronically within the Purchasing Agent's module.</td>
</tr>
<tr class="odd">
<td><strong>Receiving Report</strong></td>
<td>Report that Warehouse Clerk creates to record that the warehouse has received an item.</td>
</tr>
<tr class="even">
<td><strong>Receiving Report</strong></td>
<td>The VA document used to indicate the quantity and dollar value of the goods being received.</td>
</tr>
<tr class="odd">
<td><strong>Reconciliation</strong></td>
<td>Comparing of two records to validate IFCAP Purchase Card orders. Purchase Card Users compare IFCAP generated purchase card order data with the CC transaction sent from the CCS system in Austin.</td>
</tr>
<tr class="even">
<td><strong>Reference Number</strong></td>
<td>Also known as the Transaction Number. The computer generated number that identifies a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point - 4-digit Sequence Number.</td>
</tr>
<tr class="odd">
<td><strong>Repetitive (PR Card) Number</strong></td>
<td>See Item Master Number.</td>
</tr>
<tr class="even">
<td><p><strong>Repetitive Item List</strong></p>
<p><strong>(RIL)</strong></p></td>
<td>A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate 2237 requests from the list. A RIL can be created by using the Auto-Generate feature within the Inventory portion of the package.</td>
</tr>
<tr class="odd">
<td><strong>Requestor</strong></td>
<td>See “Control Point Requestor.”</td>
</tr>
<tr class="even">
<td><strong>Requisition</strong></td>
<td>An order from a Government vendor.</td>
</tr>
<tr class="odd">
<td><strong>Running Balance</strong></td>
<td>A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="even">
<td><strong>Section Request</strong></td>
<td>A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.</td>
</tr>
<tr class="odd">
<td><strong>Service Balance</strong></td>
<td>The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.</td>
</tr>
<tr class="even">
<td><strong>SF-18</strong></td>
<td>Request for Quotation.</td>
</tr>
<tr class="odd">
<td><strong>SF-30</strong></td>
<td>Amendment of Solicitation/Modification of Contract.</td>
</tr>
<tr class="even">
<td><strong>Short Description</strong></td>
<td>A phrase that describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).</td>
</tr>
<tr class="odd">
<td><strong>Site Parameters</strong></td>
<td>Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.</td>
</tr>
<tr class="even">
<td><strong>Sort Group</strong></td>
<td>An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.</td>
</tr>
<tr class="odd">
<td><strong>Sort Order</strong></td>
<td>The order in which the budget categories will appear on the budget distribution reports.</td>
</tr>
<tr class="even">
<td><strong>Special Remarks</strong></td>
<td>A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.</td>
</tr>
<tr class="odd">
<td><strong>Stacked Documents</strong></td>
<td>The POs, RRs &amp; 1358s that are sent electronically to Fiscal and stored in a file for printing at a later time rather than being printed immediately.</td>
</tr>
<tr class="even">
<td><strong>Status of Funds</strong></td>
<td>Fiscal's on-line status report of the monies available to a Control Point. FMS updates this information automatically.</td>
</tr>
<tr class="odd">
<td><strong>Sub-control Point</strong></td>
<td>A user-defined assignment of all or part of a ceiling transaction to a specific category (sub-control point) within a Control Point. Transactions can then be posted against this sub-control point and a report can be generated to track use of specified funding within the overall control point.</td>
</tr>
<tr class="even">
<td><strong>Sub-cost Center</strong></td>
<td>A subcategory of Cost Center. IFCAP will not utilize a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field.</td>
</tr>
<tr class="odd">
<td><strong>Tasked Job</strong></td>
<td>A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.</td>
</tr>
<tr class="even">
<td><strong>TDA</strong></td>
<td>See "Transfer of Disbursing Authority."</td>
</tr>
<tr class="odd">
<td><strong>Total Authorizations</strong></td>
<td>The total amount of the authorizations created for the 1358 obligation.</td>
</tr>
<tr class="even">
<td><strong>Total Liquidations</strong></td>
<td>The total amount of the liquidations against the 1358 obligation.</td>
</tr>
<tr class="odd">
<td><strong>Transaction Number</strong></td>
<td>The number of the transaction that funded a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.</td>
</tr>
<tr class="even">
<td><strong>Transfer of Disbursing Authority</strong></td>
<td>The method used to allocate funds to a VA facility.</td>
</tr>
<tr class="odd">
<td><strong>Transmission Number</strong></td>
<td>A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traffic.</td>
</tr>
<tr class="even">
<td><strong>Type Code</strong></td>
<td>A set of A&amp;MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.</td>
</tr>
<tr class="odd">
<td><strong>Vendor file</strong></td>
<td>An IFCAP file of vendor information solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. The debtor's address may be drawn from this file, but is maintained separately. If the desired vendor is not in the file, contact A&amp;MM Service to have it added.</td>
</tr>
<tr class="even">
<td><strong>Vendor ID Number</strong></td>
<td>The ID number assigned to a vendor by the FMS Vendor unit.</td>
</tr>
<tr class="odd">
<td><strong>VRQ</strong></td>
<td>FMS Vendor Request document. When a new vendor is added to IFCAP a VRQ message is sent electronically to the Austin FMS Vendor unit to determine if the vendor exists in the central vendor system. If the vendor is not in the system, Austin will confirm information and establish the vendor in the central file. If vendor exists in central file already, Austin will verify the data. See also VUP.</td>
</tr>
<tr class="even">
<td><strong>VUP</strong></td>
<td>Vendor Update Message. This message is sent electronically from the FMS system to ALL IFCAP sites to ensure that the local vendor file contains the same data as the central vendor file in Austin. This message will contain the FMS Vendor ID for the vendor and also the Alternate Address Indicator if applicable. See also VRQ.</td>
</tr>
</tbody>
</table>

# INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1099, 33
Accounting Technician, 16
APPROVE PAYMENT OF INVOICES ALREADY CHECKED IN, 16
Budget Object Code (BOC), 3
CREATE/REPRINT A SUSPENSION LETTER, 24
DELETE CERTIFIED INVOICE, 28
Edit FMS Vendor Payment Information, 4
EDIT FMS VENDOR PAYMENT INFORMATION, 30
FMS, 3, 4, 30, 31, 36
FOB, 19
Generate Overdue Invoice Bulletins, 35
GENERATE OVERDUE INVOICE BULLETINS, 35
INCOMPLETE INVOICE EDIT, 41
New Invoice, 5
PRINT CERTIFIED INVOICE OVERDUE REPORTS, 45
Purchase Order, 2, 37
RECHARGE AN INVOICE, 48
SEND CERTIFIED INVOICE DUE BULLETIN, 50
VIEW CERTIFIED INVOICE, 22
VRQ, 4
