---
title: IFCAP Version 5.1 DynaMed-IFCAP Implementation Guide
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: anchor
doc_subject: DynaMed-IFCAP
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: PRC
patch_ver: 5.1
patch_id: PRC*5.1
group_key: "PRC:PRC:5.1"
file_numbers: 
  - 410
  - 411
  - 441
  - 442
security_keys: []
menu_options: 7
description: 
audience: 
keywords: 
  - strong
  - class
  - dynamed
  - ifcap
  - table
  - even
  - contents
  - message
  - vendor
  - control
page_count: 0
word_count: 36337
section_count: 65
table_count: 106
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1dynamed_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1dynamed_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/001.png)

Integrated Funds Distribution,  
Control Point Activity,  
Accounting and Procurement  
(IFCAP)

*(for REDACTED VAMC only)*

June 29, 2005

DynaMed-IFCAP  
Implementation Guide

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Preface](#preface)
- [Introduction](#introduction)
  - [What is the DynaMed-IFCAP Interface?](#what-is-the-dynamed-ifcap-interface)
  - [Background and History](#background-and-history)
  - [DynaMed-IFCAP Relationship](#dynamed-ifcap-relationship)
    - [Interface Requirements](#interface-requirements)
    - [Business Rules](#business-rules)
  - [Using the DynaMed-IFCAP Implementation Guide](#using-the-dynamed-ifcap-implementation-guide)
    - [Special Terminology](#special-terminology)
    - [Relationship of this Guide to other IFCAP Documentation](#relationship-of-this-guide-to-other-ifcap-documentation)
    - [Icons Used in Boxed Notes](#icons-used-in-boxed-notes)
    - [Typography Used](#typography-used)
    - [Reference Numbering System](#reference-numbering-system)
  - [Package Operation](#package-operation)
  - [How the Interface Works](#how-the-interface-works)
- [Modifications to IFCAP](#modifications-to-ifcap)
  - [Accommodating Use of DynaMed](#accommodating-use-of-dynamed)
  - [System Parameter PRCV COTS INVENTORY](#system-parameter-prcv-cots-inventory)
  - [IFCAP Events That Update DynaMed](#ifcap-events-that-update-dynamed)
  - [DynaMed Events That Update IFCAP](#dynamed-events-that-update-ifcap)
    - [“Subscriptions” for Fund Control Point Balance Information](#subscriptions-for-fund-control-point-balance-information)
    - [Issue Book Form Type Not Available](#issue-book-form-type-not-available)
  - [Prompts Removed from IFCAP Options](#prompts-removed-from-ifcap-options)
    - [Process Issue Book Orders](#process-issue-book-orders)
    - [Do You Wish to Re-Use the RIL?](#do-you-wish-to-re-use-the-ril)
  - [Exiting Option to Generate PCard Orders Discouraged](#exiting-option-to-generate-pcard-orders-discouraged)
  - [Restrictions on DynaMed-Generated RILs](#restrictions-on-dynamed-generated-rils)
  - [Restrictions on 2237s “Returned to Service”](#restrictions-on-2237s-returned-to-service)
  - [Restrictions on Item Numbers Less Than 100,000](#restrictions-on-item-numbers-less-than-100000)
  - [Display of DynaMed Information on RIL](#display-of-dynamed-information-on-ril)
  - [Display of DynaMed Information on 2237 Documents](#display-of-dynamed-information-on-2237-documents)
- [IFCAP Functionality Using the Interface](#ifcap-functionality-using-the-interface)
  - [Replenishing Supplies](#replenishing-supplies)
    - [The Audit File](#the-audit-file)
    - [Using DynaMed Requisitions in IFCAP](#using-dynamed-requisitions-in-ifcap)
    - [Using Repetitive Item Lists (RILs)](#using-repetitive-item-lists-rils)
    - [Using 2237s](#using-2237s)
    - [Reports](#reports)
    - [Creating Purchase Orders and Purchase Card Orders](#creating-purchase-orders-and-purchase-card-orders)
    - [Processing Amendments](#processing-amendments)
    - [Processing Receipts](#processing-receipts)
    - [Processing Adjustments](#processing-adjustments)
  - [Issue Books and Adjustments](#issue-books-and-adjustments)
  - [Fiscal Updates and Fund Control Point Balances](#fiscal-updates-and-fund-control-point-balances)
  - [Item File Updates](#item-file-updates)
  - [Vendor File Updates](#vendor-file-updates)
    - [### New Report Displays Item and Associated Vendors with Vendor \#](#new-report-displays-item-and-associated-vendors-with-vendor)
- [Interface Activation, Maintenance, and Troubleshooting](#interface-activation-maintenance-and-troubleshooting)
  - [Preparing to Activate the DynaMed-IFCAP Interface](#preparing-to-activate-the-dynamed-ifcap-interface)
    - [Coordinate Plans with Staff](#coordinate-plans-with-staff)
    - [Enter the Fund Control Points into DynaMed](#enter-the-fund-control-points-into-dynamed)
    - [Set Up DynaMed System with the DUZ of its Users](#set-up-dynamed-system-with-the-duz-of-its-users)
    - [Standardize the Item and Vendor Files](#standardize-the-item-and-vendor-files)
    - [The Vendo/Item File Relationship](#the-vendoitem-file-relationship)
    - [Setup Common Number Series for Processing Issue Book Transactions](#setup-common-number-series-for-processing-issue-book-transactions)
    - [Discuss Interface Communications Issues](#discuss-interface-communications-issues)
    - [Run Item and Vendor Update Routines](#run-item-and-vendor-update-routines)
    - [Attach New Report (DynaMed Item Display with Vendor \#) to User Menus](#attach-new-report-dynamed-item-display-with-vendor-to-user-menus)
    - [Attach New Report (DynaMed RIL's Needing Action) to User Menus](#attach-new-report-dynamed-rils-needing-action-to-user-menus)
    - [Verify Appropriate Staff Are Set to Receive Interface Activity Messages](#verify-appropriate-staff-are-set-to-receive-interface-activity-messages)
  - [Activating the DynaMed-IFCAP Interface](#activating-the-dynamed-ifcap-interface)
    - [Verify Patch Installation](#verify-patch-installation)
    - [Mark Options Out of Order](#mark-options-out-of-order)
    - [Set up Mail Groups](#set-up-mail-groups)
    - [Set Up AFREE Cross-Reference](#set-up-afree-cross-reference)
    - [Set up Connectivity Values](#set-up-connectivity-values)
    - [Add Options to Appropriate Menus](#add-options-to-appropriate-menus)
    - [Set DynaMed “Switch”](#set-dynamed-switch)
    - [Populate and Initialize Record Checksum File](#populate-and-initialize-record-checksum-file)
    - [Test Connectivity/Establish Subscriptions](#test-connectivityestablish-subscriptions)
    - [Other Ways to Check Connectivity](#other-ways-to-check-connectivity)
  - [Maintenance and Troubleshooting](#maintenance-and-troubleshooting)
    - [The Audit File](#the-audit-file-1)
    - [MailMan Messages](#mailman-messages)
  - [De-activating the Interface](#de-activating-the-interface)
    - [Issues to Consider](#issues-to-consider)
    - [Terminating Interface: Setting PRCV COTS INVENTORY Switch to Zero](#terminating-interface-setting-prcv-cots-inventory-switch-to-zero)
- [Technical Summary](#technical-summary)
  - [Routines Affected](#routines-affected)
  - [Templates Affected](#templates-affected)
  - [Bulletins Affected](#bulletins-affected)
  - [Data Dictionaries Affected](#data-dictionaries-affected)
  - [Field Definitions Affected](#field-definitions-affected)
  - [Data Entries Affected](#data-entries-affected)
  - [Unique Records Affected](#unique-records-affected)
  - [Mail Groups Affected](#mail-groups-affected)
  - [Options Affected](#options-affected)
  - [Protocols Affected](#protocols-affected)
  - [HL7 Application Parameters Affected](#hl7-application-parameters-affected)
  - [HL7 Logical Links Affected](#hl7-logical-links-affected)
  - [HL7 Messages and Interface Specifications](#hl7-messages-and-interface-specifications)
  - [Data Map Record Formats Affected](#data-map-record-formats-affected)
  - [File/Global Size Changes Affected](#fileglobal-size-changes-affected)
  - [Mail Groups Affected](#mail-groups-affected-1)
  - [Security Keys Affected](#security-keys-affected)
  - [Options Affected](#options-affected-1)
  - [Remote Procedure Call (RPC) Affected](#remote-procedure-call-rpc-affected)
  - [Constants Defined in Interface Affected](#constants-defined-in-interface-affected)
  - [Variables Defined in Interface Affected](#variables-defined-in-interface-affected)
  - [Types Defined in Interface Affected](#types-defined-in-interface-affected)
  - [Graphic User Interface (GUI) Affected](#graphic-user-interface-gui-affected)
  - [GUI Classes Defined Affected](#gui-classes-defined-affected)
  - [Current Form Affected](#current-form-affected)
  - [Modified Form Affected](#modified-form-affected)
  - [Components on Form Affected](#components-on-form-affected)
  - [Events Affected](#events-affected)
  - [Methods Affected](#methods-affected)
  - [Special References Affected](#special-references-affected)
  - [Class Events Affected](#class-events-affected)
  - [Class Methods Affected](#class-methods-affected)
  - [Class Properties Affected](#class-properties-affected)
  - [Uses Clause Affected](#uses-clause-affected)
  - [Form Affected](#form-affected)
  - [Function Affected](#function-affected)
  - [Dialog Affected](#dialog-affected)
  - [Help Frame Affected](#help-frame-affected)
- [INDEX](#index)
|               |          |                                                                                              |           |
|---------------|----------|----------------------------------------------------------------------------------------------|-----------|
| Date          | Revision | Description                                                                                  | Author(s) |
| October 2011  | 2.0      | Patch PRC\*5.1\*158 Modification of title for IFCAP VA Form 1358. See page [F-1](#PRC_158a). | REDACTED  |
| June 29, 2005 | 1.0      | Initial issue                                                                                | REDACTED  |
|               |          |                                                                                              |           |
|               |          |                                                                                              |           |
|               |          |                                                                                              |           |
|               |          |                                                                                              |           |
Table D-13. HL7 Table 0357 Standard Error Codes

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DynaMed-IFCAP Interface was designed for use *only* at REDACTED VAMC. No decision has been made as to whether this software interface will be deployed for use at other facilities.

This document describes the DynaMed-IFCAP Interface, shows how to use the interface, and lays out the business rules required to successfully operate using both DynaMed and IFCAP at REDACTED.

The users of this interface will be primarily Inventory Managers, Control Point users and Purchasing Agents.

This document does *not* explain basic IFCAP processes (e.g., how to process a 2237). For instructions on how to perform specific IFCAP tasks that use the available IFCAP options, consult the appropriate IFCAP user’s guide. This Guide supplements, but does not replace, the series of IFCAP Version 5.1 User Guides. This document, as well as the IFCAP Version 5.1 User Guides, is available online at:

<http://www.va.gov/vdl/Financial_Admin.asp?appID=42>

Likewise, this document does *not* explain how DynaMed works. Documentation on DynaMed is available for REDACTED users online at:

REDACTED

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/002.png)</td>
<td><p>If your copy of this document has been downloaded to a local file:</p>
<p>▪ Please make certain your copy is current. Compare the <strong>Revision History</strong> (page <a href="#revision-history">iii</a>) of this copy with that of the original at</p>
<p><a href="http://www.va.gov/vdl/Financial_Admin.asp?appID=42">http://www.va.gov/vdl/Financial_Admin.asp?appID=42</a></p>
<p>▪ Make sure that you are storing all related files in the same local directory. If you don’t, then the hyperlinks may not work.</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/003.png)</td>
</tr>
</tbody>
</table>

# Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is the DynaMed-IFCAP Interface?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DynaMed-IFCAP Interface is an automated, real-time link between two disparate systems, IFCAP and DynaMed. It is over this interface that messages needed to manage and replenish supplies are communicated. For the most part, these transfers take place transparently, with no overt action required by users.

## Background and History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Fiscal Year 2004, REDACTED Veterans Affairs Medical Center (VAMC) was the VHA test site for the CoreFLS (*Core Financial and Logistics System*) project. The test involved the use of several interfaced commercial off-the-shelf (COTS) systems, to handle financial and logistics functions. One of those systems was a medical inventory system called *DynaMed,*® provided by Information Control Incorporated (IC). In October 2003, IFCAP was made into a “read-only” system.

On July 26, 2004, the decision was made to suspend development and use of CoreFLS and to revert to the *Integrated Funds Distribution, Control Point Activity, Accounting and Procurement* (*IFCAP*) software, which is an application in the Veterans Health Information Systems & Technology Architecture (VistA).

In early August, 2004, REDACTED VAMC was given authority to continue its use of DynaMed in a stand-alone mode. The site would utilize IFCAP for all functions except Inventory tracking.

In October 2004, an Interim Solution was instituted in which IFCAP was reactivated and the stand-alone DynaMed was installed. Data had to be entered into both systems and this resulted in some changes to the way IFCAP works at REDACTED VAMC, as well as changes to the processes at REDACTED. The Interim Solution was to be temporary with an interface to be developed between DynaMed and IFCAP in 2005.

Beginning October 1, 2004, the Interim Solution was activated and design of the automated interface began. This Guide explains the interface and identifies the modifications that were made to the IFCAP processes to support the interaction between the two systems.

## DynaMed-IFCAP Relationship

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A generic description of DynaMed appears in Appendix A. More information about how DynaMed and IFCAP work together will be presented in succeeding chapters of this Guide. For now, perhaps the most important facts to remember are these:

Table 1‑1. DynaMed-IFCAP Relationship

|                                                                                                                       |                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DynaMed...                                                                                                            | IFCAP...                                                                                                                                                                 |
| Handles all inventory-related functions and is the “system of record” for Inventory items                             | Handles all purchasing-related functions and is the Procurement “system of record”                                                                                       |
| Originates all orders for Inventory items                                                                             | Accepts requisition data from DynaMed                                                                                                                                    |
| Receives information about Items from IFCAP                                                                           | Is the “system of record” for Item files and sends updates on Items to DynaMed                                                                                           |
| Receives information about Vendors from IFCAP                                                                         | Is the “system of record” for Vendor File and sends update on Vendors to DynaMed                                                                                         |
| Receives from IFCAP the Control Point balance data to support requisition ordering.                                   | As the Financial “system of record,” sends to DynaMed the Control Point balance data to support requisition ordering.                                                    |
| Sends cost associated with Issue Book (IB) posting and Inventory Adjustment                                           | Receives the cost associated with Issue Book (IB) posting and Inventory Adjustments from DynaMed                                                                         |
| Handles all issue book and inventory adjustments                                                                      | Receives adjustments data, posting appropriate data to the Control Point balance and generating transactions to FMS upon receipt of appropriate information from DynaMed |
| As an inventory system, is primarily item-driven                                                                      | Is both item- and order-driven                                                                                                                                           |
| Is interested in purchase orders or fiscal records only as this data relates to the individual items in its inventory | Is interested in items, vendors, orders and fiscal records                                                                                                               |

### Interface Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The REDACTED VAMC developed the requirements for the DynaMed-IFCAP Interface with cooperation from Information Control and the VHA Office of Information. These requirements focused on automating the manual interfaces between IFCAP and DynaMed in use at REDACTED in order to eliminate the time-consuming and error-prone manual dual-entry processes. A complete user Requirements List is available at REDACTED

These real-time processes are:

- Verify funding is available before permitting orders or Inventory transfers to proceed
- Automatically translate DynaMed order replenishment lists into IFCAP Repetitive Item Lists (RILs)
- Prohibit creation and processing of Issue Books in IFCAP (because DynaMed provides Inventory functions including Issue Books).
- Automatically update DynaMed due-ins when a RIL is cancelled; when an IFCAP 2237 request is approved or cancelled; when an IFCAP purchase order or its amendment is signed or cancelled; when items are received; and when receiving reports are adjusted or cancelled. Updates must include 2237 transaction numbers, Purchase Order numbers and other IFCAP data as appropriate.
- Automatically commit funds in IFCAP with the 1% surcharge; update Fund Control Point balances to reflect transfers and supply fund inventory adjustments, including those for returned or refused items; and to create documents to update the Financial Management System (FMS).
- Automatically update the DynaMed Master Catalogue table (item catalog) whenever the IFCAP Item Master File is updated, and standardize the item numbering method in both systems New Items added will have numbers starting with 150000 and above.
- Automatically update the DynaMed Vendor table (vendor catalog) whenever the IFCAP Vendor File is updated.

### Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the above programmatic requirements, *business rules* have been identified that are essential to successful operation of the Interface. These rules are enforced through administrative processes, rather than through software coding.

- All requisitions for inventory items originate in DynaMed.
- All 2237s for Inventory items are created via the Requisition from DynaMed.
- DynaMed RILs may not be copied or edited.

## Using the DynaMed-IFCAP Implementation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Special Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, references to “the Guide” should be interpreted to mean the *DynaMed-IFCAP Implementation Guide* (this document). Likewise, the terms “interface,” “interfaces,” or “the interface” refer to the DynaMed-IFCAP Interface. Finally, the phrase “the systems” should be interpreted to mean the DynaMed system and the IFCAP system, operating together or separately.

For specific definitions of terms and explanations of acronyms used in the interface, IFCAP and DynaMed, see the glossary at Appendix F.

### Relationship of this Guide to other IFCAP Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document supplements the series of IFCAP version 5.1 Guides and Manuals (e.g., Application Coordinator User's Guide, Purchase Card User's Guide).[^1]

A complete listing of Revisions made to IFCAP to support the interface is in Chapter 2. The Guide addresses the functionality and changes associated with the interface. Persons requiring more information about IFCAP or DynaMed are asked to refer to appropriate manuals.

### Icons Used in Boxed Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whenever you need to be aware of something important or informative, the Guide will display a boxed note with an icon to alert you, usually in the left margin. For an example, see the warning in section 1.5.

Table 1‑2. Icons Used in Boxed Notes

| Icon                                                                                                | Meaning                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/004.png) | Warning: Something that could affect your use of the DynaMed-IFCAP Interface or of the material available in the databases.                                                             |
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/005.png) | Information: Additional information that might be helpful to you or something you need to know about, but which is not critical to understanding or use of the DynaMed-IFCAP Interface. |
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/006.png) | Tip*:* Advice on how to more easily navigate or use the Guide or the software.                                                                                                              |
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/007.png)                                                   | Technical Note: Information primarily of interest to software developers, IRM or EVS personnel. Most IFCAP users can usually safely ignore such notes.                                      |

### Typography Used

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the Guide, the following fonts are used for the purposes indicated in the following table.

Table 1‑3. Typography Used for IFCAP Screens

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 33%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Typeface</th>
<th>Usage</th>
<th>Examples</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Courier New 9-point (black)</td>
<td>Computer screen shot text (as for menus and options)</td>
<td><p>Unposted Dietetic Cost Report (option title)</p>
<p>Inventory File Maintenance Menu ... (menu title)</p></td>
</tr>
<tr class="even">
<td><strong>Courier New 9-point (black), bold</strong></td>
<td>User input or response to prompt</td>
<td><strong>File Inquiry</strong> (in response to the prompt Select the Inventory File Maintenance Menu Option:)</td>
</tr>
<tr class="odd">
<td rowspan="4">Arial 9-point, regular or bold</td>
<td rowspan="4">Pointer text (as for menu options) and explanatory text, shown with an arrow pointing to the text being explained, and with shaded background. When parts of the Guide are shown (as in the first two examples), the volume or section references are hyperlinks.</td>
<td>See <a href="../Glossary/Glossary_DynaMed-IFCAP_Interface.doc">Glossary</a></td>
</tr>
<tr class="even">
<td>Refer to 1.3.2</td>
</tr>
<tr class="odd">
<td><strong>See note at end of table</strong></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

Table 1‑4. Typography Used Elsewhere in the Guide

| Typeface  | Usage                                                                                                                                                                                  | Examples                                                                                                                                                                                                                                                        |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blue text | Hyperlinks[^2] to other documents or places in the current document may not appear blue if not supported by your software settings, but they will stand out from the surrounding text. | See the pointer text examples immediately above. The first example ( See [Glossary](../Glossary/Glossary_DynaMed-IFCAP_Interface.doc)) is a hyperlink to another document, while the second ( Refer to 1.3.2) is a cross-reference to a point in this document. |

### Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Guide uses the same paragraph numbering system as in the original IFCAP user’s guides, but you should not expect a direct correlation between sections in the original IFCAP guides and this Guide. Nonetheless, the general numbering principles, which allow readers to understand how the sections of the Guide relate to each other, still apply. For example, this paragraph is paragraph 1.4.5. This means that this paragraph is the fifth main paragraph for the fourth section of Chapter 1. If there were two subparagraphs to this main paragraph, they would be numbered 1.4.5.1 and 1.4.5.2. Shown graphically:

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/008.png) |
|---------------------------------------------------|

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options available to IFCAP users are grouped based on the type of work the person performs within IFCAP. Users are grouped into various categories, called “roles.”

The options available to you in your IFCAP role are referred to as your “menu” (or menus, since you may have more than one assigned). You may also have both menus and options (called “screens” or “forms”) in DynaMed if inventory control is a part of your job.

IFCAP users will see the same IFCAP menus and options formerly used, although some options and choices within options may be programmatically disabled, and some may be administratively restricted from use.

If the menus shown in this Guide include options that you do not see on your screen, do not panic! If you do not understand the question, are unsure of how to respond, or do not know what to enter at a prompt, enter one, two or three question marks (?). IFCAP will list your available options, explain the prompt, or display a list of options from which to choose. The more question marks you enter at the prompt, the more detailed information the program will provide.

## How the Interface Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table that follows summarizes the interaction between DynaMed and IFCAP. More details are provided in succeeding sections of this Guide.

Table 1‑5. Interaction between DynaMed and IFCAP

| System  | Action                                                                                                                                                                                       |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DynaMed | A system-generated Daily Order (Requisition) or a user-generated Manager Order (Requisition) is sent automatically to IFCAP                                                                  |
| IFCAP   | Receives the DynaMed Requisition and automatically converts it into a RIL                                                                                                                    |
| IFCAP   | User may not Edit the RIL (*Business Rule*), but may cancel the RIL in its entirety                                                                                                          |
| IFCAP   | From the DynaMed RIL, User may generate a 2237 or a Purchase Card order                                                                                                                      |
| IFCAP   | Sends update message to DynaMed when any of several “events” occur (*see* Section 2.2)                                                                                                       |
| DynaMed | Inventory Managers “subscribe” to funds updates from IFCAP concerning Fund Control Points the Manager is interested in. Funds balances are then available from within DynaMed.               |
| DynaMed | Sends update messages to IFCAP when it is necessary to update the Control Point balances as a result of inventory changes, or when FMS must be notified of revisions to the inventory value. |

# Modifications to IFCAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accommodating Use of DynaMed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP is a product that contains several modules. In order for the site to maintain accurate inventory records, the DynaMed system needs to interface with several of these modules, including Procurement, Budget and the Control Point. In order to accommodate use of the DynaMed program, several modifications have been made to IFCAP. These modifications are designed so that any site *not* using DynaMed will be unaffected.

## System Parameter PRCV COTS INVENTORY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An IFCAP system parameter called PRCV COTS INVENTORY has been added to allow IFCAP to determine whether or not the site is using DynaMed. This parameter has the settings of ‘0’ (meaning “None”) or ‘1’ (meaning “DynaMed”). A value of ‘0’ signifies the site is using the standard IFCAP inventory package of GIP. Setting the flag to ‘1’ will indicate to IFCAP that DynaMed is the site’s inventory package, supplanting the Generic Inventory Program (GIP) and any other program. Currently, the only COTS system defined by the prompt is DynaMed. This parameter is also sometimes referred to simply as “the switch.”

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/009.png)</td>
<td><p><em>Technical Note:</em> The system parameter definition is as follows:</p>
<p>NAME: PRCV COTS INVENTORY DISPLAY TEXT: COTS Inventory</p>
<p>MULTIPLE VALUED: No VALUE TERM: 0 or 1</p>
<p>VALUE DATA TYPE: set of codes VALUE DOMAIN: 0:NONE;1:DYNAMED</p>
<p>INSTANCE DATA TYPE: numeric</p>
<p>DESCRIPTION:</p>
<p>This parameter identifies which COTS product is being utilized for the</p>
<p>inventory management system of the site. The current values are:</p>
<p>0 NONE - means no COTS product is being used and the inventory</p>
<p>management system in use is GIP/IFCAP</p>
<p>1 DYNAMED - means the DynaMed product is being used</p>
<p>PRECEDENCE: 1 ENTITY FILE: SYSTEM</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/010.png)</td>
</tr>
</tbody>
</table>

When the parameter is set to ‘1’:

- DynaMed becomes the “system of record” for Inventory.
- DynaMed will send requisitions to IFCAP for processing. IFCAP will receive from DynaMed lists of supplies to be purchased for site replenishment. The list will enter the IFCAP Control Point Module, where it will be used to create a Repetitive Item List (RIL) from which the user can generate either 2237 document(s) or Purchase Card (PC) order(s). All items which enter IFCAP in this manner are marked with the DynaMed Document ID so that DynaMed can later make the appropriate match-up with the item records in the DynaMed tables.
- IFCAP will send notification to DynaMed when various “events” occur during IFCAP processing, as defined in section 2.3.
- DynaMed will send notification to IFCAP when specified events occur in DynaMed, as outlined in section 2.4.
- Some IFCAP features no longer needed by site users (because of functionality provided by DynaMed) have been removed from user menus and option lists, and a few other restrictions have also been placed on IFCAP users. *See* sections 2.4.2 through 2.9.
- Some information that is unique to DynaMed will be displayed on IFCAP documents. *See* section 2.11.
- Inventory Managers using DynaMed may subscribe to funds updates from IFCAP. *See* the DynaMed user documentation.

## IFCAP Events That Update DynaMed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When any of the following events occur in IFCAP, an update message is automatically sent to DynaMed:

- Event 1: Processing of Requisition (if any requisition item is rejected, an update message is sent to cause removal of that item from the DynaMed due-ins)
- Event 2: Deletion (Cancellation) of a RIL (DynaMed-generated RILs cannot be edited in IFCAP)
- Event 3: Update[^3] of 2237
- Event 4: Update<sup>3</sup> of Purchase Order, PCard Orders and Amendments
- Event 5: Update<sup>3</sup> on Receiving Report Activity
- Event 7: Fund Control Point Balance Updates
- Event 8: Updates to the Item Master (including those made directly by the user or indirectly by processes occurring in IFCAP)
- Event 9: Updates to the Vendor Master (including those made directly by the user or indirectly by processes occurring in IFCAP)

Each event message updates the DynaMed Due-In information for the associated item.

## DynaMed Events That Update IFCAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the system parameter PRCV COTS INVENTORY is set to ‘1’ (meaning “DynaMed”), DynaMed becomes the system of record for Inventory.

All requisitions for inventory items are created in DynaMed, and then transmitted to IFCAP, where a RIL is automatically created for use in IFCAP.

All Issue Book and stock transfer activity will occur in DynaMed and will be communicated to IFCAP only when it is necessary to update the Control Point balances, or when FMS must be notified of revisions to the inventory value. IFCAP option changes related to Issue Book transactions are reflected in removal of the ability to access the Issue Book form (see section 2.5.1).

A new “subscription” process enables Inventory Managers to monitor the status of funds from within DynaMed. These subscriptions are recorded in IFCAP, and new and cancelled subscription requests issued from DynaMed therefore update IFCAP.

### “Subscriptions” for Fund Control Point Balance Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to control the channeling of Fund Control Point balance updates to Inventory Managers, a “subscription” process has been set up. See the DynaMed user documentation for more information on this process from the user point of view. This process is completely transparent to IFCAP users, and does not directly affect operation of IFCAP.

### Issue Book Form Type Not Available

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Control Point Module, there are several form types that can be used to create a transaction. Since the DynaMed-IFCAP Interface does not make use of the “Issue Book” Form Type (Form 5), that IFCAP form is no longer allowed at a DynaMed site. IFCAP users will no longer have this option available.

Here is a sample dialogue of what will be seen when the IFCAP user processes a 2237 request deriving from a DynaMed-generated RIL, starting from the Repetitive Item List Menu:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>DynaMed Item Display with Vendor #</p>
<p>Select Process a Request Menu Option: REPetitive Item List Menu</p>
<p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Dynamed RIL's Needing Action</p>
<p>Select Repetitive Item List Menu Option: GENerate Requests From Repetitive Item</p>
<p>List Entry</p>
<p>This option generates requests with permanent transaction numbers from</p>
<p>entries in the repetitive item list file.</p>
<p>Are you sure you are ready to proceed? No// Y (Yes)</p>
<p>Select REPETITIVE ITEM LIST ENTRY NUMBER: 100-05-3-076-828100-0045 04-26-05</p>
<p># OF ITEMS: 1TOTAL COST: 2000.04</p>
<p>Select FISCAL YEAR: 05//</p>
<p>You may use either the current quarter or the repetitive item</p>
<p>list quarter to generate requests.</p>
<p>Use repetitive item list quarter? Yes// (Yes)</p>
<p>DEVICE: HOME// INCOMING TELNET Right Margin: 80//</p>
<p>GENERATE REQUESTS FROM REPETITIVE ITEM LIST FILEDATE: JUN 15,2005@11:07</p>
<p>Requests Generated From Repetitive Item List Entry # 100-05-3-076-828100-0045</p>
<p>--------------------------------------------------------------------------------</p>
<p>A request with Transaction Number 100-05-3-076-1064 has been generated.</p>
<p>The vendor for this request is EXAMPLE COMPANY MEDICAL (1625)</p>
<p>Now entering items for this request.</p>
<p>Do you wish to edit this request? No// (No)</p>
<p>Current Control Point balance: $694785.78</p>
<p>Estimated cost of this request: $2000.04</p>
<p>Is this request ready for approval? Yes// N (No)</p>
<p>Finished building request.</p>
<p>This request contains 1 item. The total cost for this request is $2000.04</p>
<p>--------------------------------------------------------------------------------</p>
<p>Total no. of requests generated: 1 Total no. of items (all requests): 1</p>
<p>Total committed (estimated) cost (all requests) : $2000.04</p>
<p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Dynamed RIL's Needing Action</p>
<p>Select Repetitive Item List Menu Option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Prompts Removed from IFCAP Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Process Issue Book Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the PRCV COTS INVENTORY flag is set to DynaMed, the prompt, “Process Issue Book Orders?// No” will not appear in the Accountable Officer option:

- Process a Request in PPM \[PRCHPM REQST\]

Since no issue books are to be created in IFCAP while the interface is active, there is no need for this prompt.

### Do You Wish to Re-Use the RIL?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When generating 2237s or Purchase Card orders from RILS created by the receipt of information from DynaMed, users will not be prompted to retain the RIL for re-use. These RILS will automatically be deleted at the conclusion of the process. This action is necessary as the items in the RIL are tied to special one-time orders in DynaMed. The affected options include:

- Generate Requests From Repetitive Item List Entry \[PRCSRI GENERATE\]
- Create P/C Order From Repetitive Item List \[PRCH CREATE PURCHASE CARD\]

## Exiting Option to Generate PCard Orders Discouraged

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the user is creating Purchase Card (PCard) orders from a *user-generated* RIL, there will be no change in this process.

> In the Create P/C Order From Repetitive Item List option \[PRCH CREATE PURCHASE CARD\], it is possible to exit the option prior to moving all items from the RIL to PC orders. Because RILs containing DynaMed-requested items are automatically deleted when the user exits, there are additional prompts that will appear if the user tries to prematurely exit via an up-arrow ( ^ ) while processing a RIL containing DynaMed-generated items.

|                                                                                                     |                                                                                                   |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/011.png) | *Warning:* If the user chooses to exit anyway, the RIL will be deleted and cannot be re-used. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/012.png) |

A sample dialogue and printout is included here:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Process Purchase Card Menu Option: CREate P/C Order From Repetitive Item</p>
<p>List</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select REPETITIVE ITEM LIST ENTRY NUMBER: 100-05-2-076-828100-3705 03-10-05</p>
<p># OF ITEMS: 1TOTAL COST: 100.80</p>
<p>This repetitive item list has the following vendors:</p>
<p>RANDOMVENDOR NUMBER: 111</p>
<p>ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES</p>
<p><strong>PURCHASE ORDER: ^</strong></p>
<p>NOTE: This RIL Contains DynaMed Orders!!!</p>
<p>-----------------------------------------</p>
<p>You must enter a valid PURCHASE ORDER NUMBER to continue. If no valid</p>
<p>PURCHASE ORDER is entered, all items remaining on the RIL will be deleted.</p>
<p><strong>Do you want to exit and delete the RIL?? NO// YES</strong></p>
<p>NOTE: This RIL Contains DynaMed Orders!!!</p>
<p>-----------------------------------------</p>
<p>You must enter a valid PURCHASE ORDER NUMBER to continue. If no valid</p>
<p>PURCHASE ORDER is entered, all items remaining on the RIL will be deleted.</p>
<p><strong>Are you sure that you want to cancel ALL DynaMed Orders on this RIL?? NO// YES</strong></p></td>
</tr>
<tr class="even">
<td><p>Total number of requests generated: 0</p>
<p>Total cost of all requests: $0.00</p></td>
</tr>
</tbody>
</table>

## Restrictions on DynaMed-Generated RILs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RILs created through the interface with DynaMed will not be accessible from the option:

- Edit Repetitive Item List Entry \[PRCSRI EDIT\]

Trying to access a DynaMed-created RIL while in EDIT will cause the message…

\*\* This RIL originated from DynaMed and cannot be edited \*\*

… to be displayed and the user to exit the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select REPETITIVE ITEM LIST #: 100-05-2-076-828100-3705 03-10-05 # OF ITEMS:</p>
<p>1TOTAL COST: 100.80</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td> This RIL originated from DynaMed and cannot be edited </td>
</tr>
</tbody>
</table>

|                                                                                                     |                                                                                                                                                                               |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/013.png) | RILS created in IFCAP by an IFCAP user may be edited as usual. It is important to note, however, that DynaMed will not be “aware” of any items created by means of such RILs. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/014.png) |

## Restrictions on 2237s “Returned to Service”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to prevent the same DynaMed ID from appearing on multiple POs or from being deleted in the 2237 while still active on a purchase order, IFCAP will no longer allow Purchasing to return any 2337 containing DynaMed requested items if the 2237 being returned ‘parented’ other 2237s.

DynaMed-generated 2237s that were not split and are children of parent 2237s, and 2237s not derived from a DynaMed-generated RIL, may be returned to Service as usual.

To accommodate this revision the option:

- Request Further Clarification or Return to Service \[PRCHPC RETURN REQUEST\]

has been modified to restrict the user to only be able to select a request of further clarification when the 2237 selected in the option contains 2237 requested items and is a parent to another 2237.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER ('^' TO EXIT): 100// REDACTED VAMC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>2237 TRANSACTION NUMBER: 100-05-2-076-0598 Sent to Purchasing &amp; Contracting OBL COMPANY HEALTHCARE /I</p>
<p>CONTROL-4C PLUS TRIPAK LO/NORM/HI 3.3ML-9S</p>
<p>CURRENT STATUS: Sent to Purchasing &amp; Contracting// ??</p>
<p>This is the current status of the 2237 request.</p>
<p>Choose from:</p>
<p>Request Clarification by Service for P&amp;C 75</p></td>
</tr>
<tr class="even">
<td>CURRENT STATUS: Sent to Purchasing &amp; Contracting//</td>
</tr>
</tbody>
</table>

## Restrictions on Item Numbers Less Than 100,000

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will automatically generate item numbers that will be used as the DynaMed SKU number. When DynaMed is the indicated inventory system, the number must be in the range that DynaMed will accept (6-digit number not less than 100,000). IFCAP will prevent users from entering any new items below 100,000. The user should always enter NEW when adding a brand new Item to the IFCAP file. IFCAP will generate a number in the 150,000 range. If the user determines that a number greater than 100000 exists in DynaMed but is not in IFCAP, the user may enter that number into IFCAP to ensure the two systems have the same item number for that Item.

|                                                                                                     |                                                                                     |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/015.png) | *Note:* DynaMed at REDACTED VAMC does not have any items with numbers under 100,000 | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/016.png) |

## Display of DynaMed Information on RIL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DynaMed Doc ID and Date Needed By Fields will be displayed when displaying or printing a DynaMed generated RIL. The display and option name are shown here:

- Print/Display Repetitive Item List Entry \[PRCSRI PRINT/DISPLAY\]

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select REPETITIVE ITEM LIST #: 100-05-2-00076-828100-0003 03-23-05 # OF ITEMS: 3TOTAL COST: 330.77</p>
<p>DEVICE: HOME// INCOMING TELNET Right Margin: 80//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>REPETITIVE ITEM LIST #: 100-05-2-00076-828100-0003DATE: MAR 29, 2005@08:26:11 PAGE 1</p>
<p>ITEM NO. SHORT DESCRIPTION QUANTITY UNIT COST U/P</p>
<p>--------------------------------------------------------------------------------</p>
<p>VENDOR: RANDOMVENDOR (111)</p>
<p>106701 SUTURE-VICRYL-0-J287 5 20.16 BX</p>
<p>DM DOC ID: 5074-5114-222 DATE NEEDED BY: Mar 27, 2005</p>
<p>106750 SUTURE-PROLENE-1-0-8 2 33.56 BX</p>
<p>DM DOC ID: 5074-5115-222 DATE NEEDED BY: Mar 27, 2005</p>
<p>106749 SUTURE-PROLENE-2-0-8 5 32.57 BX</p>
<p>DM DOC ID: 5074-5116-222 DATE NEEDED BY: Mar 27, 2005</p>
<p>TOTAL # OF ITEMS: 3 TOTAL COST: 330.77</p>
<p>--------------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td>TOTAL # OF ITEMS (ALL VENDORS): 3 TOTAL COST (ALL VENDORS): 330.77</td>
</tr>
</tbody>
</table>

## Display of DynaMed Information on 2237 Documents 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Items on 2237s created from DynaMed-generated RILs will include a date by which that item needs to be received by the requesting stockroom. This date will be displayed when the user is prompted to enter a delivery schedule within the 2237. The affected options include:

- New 2237 (Service) Request \[PRCSENRB\]
- Edit a 2237 (Service) \[PRCSEDTD\]

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CLASSIFICATION OF REQUEST:</p>
<p>SORT GROUP:</p>
<p>DATE OF REQUEST: APR 5,2005//</p>
<p>REQUESTOR: REDACTED//</p>
<p>REQUESTING SERVICE: ACQUISITION &amp; MATERIEL MGMT.//</p>
<p>DATE REQUIRED: MAY 5,2005//</p>
<p>PRIORITY OF REQUEST: STANDARD//</p>
<p>SPECIAL REMARKS:</p>
<p>1&gt;</p>
<p>COST CENTER: 615300 Inventory and Di</p>
<p>VENDOR: RANDOMVENDOR//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select LINE ITEM NUMBER: 5//</p>
<p>LINE ITEM NUMBER: 5//</p>
<p>ITEM MASTER FILE NO.: 106701//</p>
<p>BOC: 2696 Supply Fund - Subs</p>
<p>QUANTITY: 5//</p></td>
</tr>
<tr class="even">
<td><p>QTY BEG BAL: 5</p>
<p>DynaMed's DATE NEEDED BY: Apr 19, 2005</p>
<p>Select DELIVERY SCHEDULE: 5</p>
<p>Are you adding '5' as a new DELIVERY SCHEDULE (the 1ST for this ITEM)? No// y</p>
<p>(Yes)</p>
<p>DELIVERY DATE: 0419 (APR 19, 2005)</p>
<p>Delivery date must be later than Request's required date.</p>
<p>DELIVERY DATE: APR 19,2005// ^</p>
<p>Select DELIVERY SCHEDULE:</p>
<p>Select LINE ITEM NUMBER: 4 106750 SUTURE-PROLENE-1-0-8</p>
<p>LINE ITEM NUMBER: 4//</p>
<p>ITEM MASTER FILE NO.: 106750//</p>
<p>BOC: 2696 Supply Fund - Subs</p>
<p>QUANTITY: 3//</p>
<p>QTY BEG BAL: 3</p>
<p>DynaMed's DATE NEEDED BY: Apr 19, 2005</p>
<p>Select DELIVERY SCHEDULE:</p>
<p>Select LINE ITEM NUMBER: 3 106749 SUTURE-PROLENE-2-0-8</p>
<p>LINE ITEM NUMBER: 3//</p>
<p>ITEM MASTER FILE NO.: 106749//</p>
<p>BOC: 2696 Supply Fund - Subs</p>
<p>QUANTITY: 4//</p>
<p>QTY BEG BAL: 4</p>
<p>DynaMed's DATE NEEDED BY: Apr 19, 2005</p>
<p>Select DELIVERY SCHEDULE:</p>
<p>Select LINE ITEM NUMBER: 2 106701 SUTURE-VICRYL-0-J287</p>
<p>LINE ITEM NUMBER: 2//</p>
<p>ITEM MASTER FILE NO.: 106701//</p>
<p>BOC: 2696 Supply Fund - Subs</p>
<p>QUANTITY: 5//</p>
<p>QTY BEG BAL: 5</p>
<p>DynaMed's DATE NEEDED BY: Apr 19, 2005</p>
<p>Select DELIVERY SCHEDULE:</p>
<p>Select LINE ITEM NUMBER: 1 106750 SUTURE-PROLENE-1-0-8</p>
<p>LINE ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.: 106750//</p>
<p>BOC: 2696 Supply Fund - Subs</p>
<p>QUANTITY: 1//</p>
<p>QTY BEG BAL: 1</p>
<p>DynaMed's DATE NEEDED BY: Apr 13, 2005</p>
<p>Select DELIVERY SCHEDULE:</p>
<p>Select LINE ITEM NUMBER:</p>
<p>COMMITTED (ESTIMATED) COST: 302.28//</p>
<p>DATE COMMITTED: APR 5,2005//</p>
<p>TRANSACTION BEG BAL: 302.28</p></td>
</tr>
<tr class="odd">
<td><p>Select SUB-CONTROL POINT:</p>
<p>DELIVER TO/LOCATION: bdl3</p>
<p>JUSTIFICATION:</p>
<p>1&gt;need it</p>
<p>2&gt;</p>
<p>EDIT Option:</p>
<p>ORIGINATOR OF REQUEST: cz</p>
<p>1 CZEKAJ,NAME CC 192 REDACTED TEST LAB</p>
<p>2 CZ MJSDHU,NAME1 CZ 5D NURSE</p>
<p>3 CZ MXUUDT,JELUAHT CZ 138M</p>
<p>4 CZ MDASHYKHUFHU,JEHTSHU LLBH ZLUN (PHYSICIAN) CZ</p>
<p>5 CZ MLSNBX,JEUDTSXWEHU ZI MD BHQHUAN EDAAT (PHYSICIAN) CZ</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 1 CZEKAJ,NAME CC 192 REDACTED TEST LAB</p>
<p>COMMENTS:</p>
<p>1&gt;</p></td>
</tr>
<tr class="even">
<td><p>Current Control Point balance: $-1238.10</p>
<p>Estimated cost of this request: $302.28</p>
<p>Is this request ready for approval? Yes// n (No)</p></td>
</tr>
</tbody>
</table>

In addition, the “Date Needed By” field will appear on the 2237 printout. The DynaMed requisition number, which uniquely identifies the activity associated with their request to replenish the item in a particular stockroom, will also be displayed. This unique request number is known as the “DynaMed Document ID” \[DM DOC ID\] in IFCAP and as the “DynaMed Document Number” in DynaMed.

- Print/Display Request Form \[PRCSPRF\]

A sample dialogue and printout is included here:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select CONTROL POINT: 076 WARD MEDICAL SUPPLIES// 0160A1 10 0100 0100441S9</p>
<p>Select Process a Request Menu Option: PRINT/Display Request Form</p>
<p>Select CONTROL POINT: 076 WARD MEDICAL SUPPLIES 0160A1 10 0100 0100441S9</p>
<p>Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: 100-05-2-076-0639 OBL RANDOMVENDOR</p>
<p>Print administrative certification page of 2237? Yes// (Yes)</p>
<p>DEVICE: HOME// INCOMING TELNET Right Margin: 80//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PRIORITY: STANDARD</p>
<p>MAR 24, 2005@09:30:37 100-05-2-076-0639</p>
<p>--------------------------------------------------------------------------------</p>
<p>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</p>
<p>--------------------------------------------------------------------------------</p>
<p>TO: A&amp;MM Officer Requesting Office</p>
<p>ACQUISITION &amp; MATERIEL MGMT. (90)</p>
<p>----------------------- --------------------------------------------------------</p>
<p>Action Requested Date Prepared Date Required</p>
<p>Delivery MAR 23, 2005 APR 22, 2005</p>
<p>----------------------- --------------------- ----------------------------------</p>
<p>ITEM NO. DESCRIPTION QUANTITY UNIT ESTIMATED</p>
<p>OR STOCK NO. UNIT COST</p>
<p>--------------------------------------------------------------------------------</p>
<p>ERH34 1 ITEM ID NO. 106701 SUTURE,VICRYL,UND</p>
<p>BRD,SZ 0,54IN,REEL</p>
<p>PKG: 12 per BX DM Doc ID:</p>
<p>5063-5130-222 Date Needed By: Mar</p>
<p>15, 2005 5 BX 21.0000</p>
<p>TOTAL COST: $105.00</p>
<p>--------------------------------------------------------------------------------</p>
<p>Press return to continue, uparrow (^) to exit:</p>
<p>100-05-2-076-0639</p>
<p>--------------------------------------------------------------------------------</p>
<p>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</p>
<p>--------------------------------------------------------------------------------</p>
<p>VENDOR INFORMATION: NO: 111</p>
<p>VENDOR: RANDOMVENDOR</p>
<p>HEALTH CARE SYSTEMS INC. PHONE: 800-255-2500</p>
<p>425 EXAMPLE RD ACCT. #: BP:7920 FM:7927</p>
<p>PO BOX 100</p>
<p>ANYTOWN,NJ 99999</p>
<p>--------------------------------------------------------------------------------</p>
<p>Ref. Voucher Number:</p>
<p>--------------------------------------------------------------------------------</p>
<p>JUSTIFICATION OF NEED OR TURN-IN</p>
<p>--------------------------------------------------------------------------------</p>
<p>Originator of Request:</p>
<p>Signature of Initiator Signature of Approving Official Date</p>
<p>REDACTED</p>
<p>------------------------------------ -------------------------------------------</p>
<p>Press return to continue, uparrow (^) to exit:</p>
<p>100-05-2-076-0639</p>
<p>--------------------------------------------------------------------------------</p>
<p>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</p>
<p>--------------------------------------------------------------------------------</p>
<p>Appropriation and Accounting Symbols</p>
<p>100-3650160-076-828100-2632 0100441S9</p>
<p>--------------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td>Press return to continue:</td>
</tr>
</tbody>
</table>

# IFCAP Functionality Using the Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DynaMed-IFCAP Interface is actually not a single interface, but rather a series of “touch points” where each program interacts with the other. This chapter will explain each of these touch points and includes a process flow diagram and tables explaining the overall processes affected by the Interface.

This chapter is split into five sections describing the five major processes affected by implementation of the DynaMed-IFCAP Interface:

1.  Replenishing Supplies (ordering supplies from an outside source)
2.  Issue Books and Adjustments
3.  Fiscal Updates/Fund Control Point Balance Maintenance
4.  Item File Maintenance
5.  Vendor File Maintenance

Each section will include a table summarizing the flow of information between IFCAP and DynaMed for the process being explained. The following table defines the symbols in the process flow tables.

|        |                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------|
| Symbol | Indicates data flow...                                                                               |
|        | From DynaMed to IFCAP                                                                                |
|        | From IFCAP to DynaMed                                                                                |
|        | Internal within IFCAP or DynaMed                                                                     |
| M  | Data updates are performed manually in appropriate system, or other actions are taken by individuals |

## Replenishing Supplies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                     |                                                                                                                                                                                                                                                                               |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/017.png) | All inventory requests must originate from DynaMed, the inventory system. Requests entered directly into IFCAP *will not update* DynaMed Due-Ins. Because of this, *new items cannot be added to existing 2237s and purchase orders created from DynaMed-generated RILs.* | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/018.png) |

DynaMed builds a message to communicate to IFCAP its requests for replenishment. Upon receipt of this message, IFCAP builds a RIL. RILs built from a DynaMed message differ from other RILs in IFCAP in that each item includes the DynaMed order request number (the DynaMed Document ID or DM DOC ID) and a date by which that item is desired to be received in the requesting stockroom (Date Needed By). The Date Needed By is used when setting up delivery schedules in 2237s. IFCAP uses the DM DOC ID to determine whether or not to send information back to update due-ins in DynaMed (updates on items that were not generated from DynaMed are not sent to DynaMed).

|                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/019.png) | *Note:* A transaction concerning replenishment of supplies passed between IFCAP and DynaMed that cannot be processed by the receiving system will be communicated to designated users of the affected IFCAP control point. To receive these messages, an individual must be an official or clerk of the affected control point and have the notification designee flag set to 'YES'. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/020.png) |

The basic process is the same regardless of whether the DynaMed requisition results in an IFCAP Purchase Order or Purchase Card (PCard) Order, but there are some differences. These differences are noted in the following two tables.

Table 3‑1. Supply Replenishment Using IFCAP Purchase Order

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 39%" />
<col style="width: 7%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2">Step</th>
<th rowspan="2">DynaMed</th>
<th rowspan="2">Data Flow</th>
<th rowspan="2">IFCAP</th>
</tr>
<tr class="odd">
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td><p><em>Inventory User:</em> Generate DynaMed Requisitions</p>
<p><em>System:</em> Push data to IFCAP to generate RIL</p></td>
<td></td>
<td><em>System:</em> Automatically create RIL from pushed DynaMed data</td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td></td>
<td></td>
<td><em>Control Point User:</em> Generate 2237 from RIL (answer “YES” to “Do you want to edit?” prompt)</td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td></td>
<td></td>
<td><em>Control Point User:</em> Edit and approve 2237 in IFCAP</td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td><em>System</em>: Update Due-ins with 2237 data</td>
<td></td>
<td><em>Accountable Officer:</em> Approve 2237, assign to Purchasing</td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td></td>
<td></td>
<td><em>Purchasing Agent:</em> Create Purchase Order with ‘INVOICING/RECEIVING REPORT’ or ‘PURCHASE CARD’ Method of Processing</td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td><em>System</em>: Update due-ins with PO data</td>
<td></td>
<td><em>Approving Official/Buyer/Purchasing Agent:</em> Sign Purchase Order or, later, its Amendment</td>
</tr>
<tr class="odd">
<td><strong>7</strong></td>
<td><em>System</em>: Update due-ins with Amendment data</td>
<td></td>
<td><em>Approving Official/Buyer/Purchasing Agent:</em> Sign Amendment to PO</td>
</tr>
<tr class="even">
<td><strong>8</strong></td>
<td><em>System</em>: Update due-ins with receipt data</td>
<td></td>
<td><em>Warehouseman:</em> Generate Receiving Report, sign it, and receive items in IFCAP</td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td><em>Inventory User:</em> Generate Putlist</td>
<td><strong>M</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>10</strong></td>
<td><em>Inventory User:</em> Put received items on shelf</td>
<td><strong>M</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>11</strong></td>
<td></td>
<td></td>
<td><em>Fiscal:</em> Process PORR information</td>
</tr>
<tr class="even">
<td><strong>12</strong></td>
<td></td>
<td></td>
<td><em>System:</em> Update Fiscal, FCP &amp; FMS</td>
</tr>
</tbody>
</table>

Table 3‑2. Supply Replenishment Using IFCAP Purchase Card (PCard) Order

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 39%" />
<col style="width: 7%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2">Step</th>
<th rowspan="2">DynaMed</th>
<th rowspan="2">Data Flow</th>
<th rowspan="2">IFCAP</th>
</tr>
<tr class="odd">
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td><p><em>Inventory User:</em> Generate DynaMed Requisitions</p>
<p><em>System:</em> Push data to IFCAP to generate RIL</p></td>
<td></td>
<td><em>System:</em> Automatically create RIL from pushed DynaMed data</td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td></td>
<td></td>
<td><em>PCard User:</em> Create Purchase Card Order.</td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td><em>System</em>: Update due-ins with PO data</td>
<td></td>
<td><em>Approving Official:</em> Sign PCard Order</td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td><em>System:</em> Update due-ins with amended data</td>
<td></td>
<td><em>PCard User</em>: Create PCard Order amendment (if needed)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><em>Pcard Approver:</em> Sign Amendment to PO</td>
</tr>
<tr class="even">
<td><strong>5</strong></td>
<td></td>
<td><strong>M</strong></td>
<td><em>Initiator:</em> Receive Order from Vendor</td>
</tr>
<tr class="odd">
<td><strong>6</strong></td>
<td><em>System</em>: Update due-ins with receipt data.</td>
<td></td>
<td><em>Warehouseman:</em> Generate Receiving Report, sign it, and receive items in IFCAP</td>
</tr>
<tr class="even">
<td><strong>7</strong></td>
<td><em>Inventory User:</em> Generate Putlist.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>8</strong></td>
<td><em>Inventory User:</em> Put received items on shelf</td>
<td><strong>M</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>9</strong></td>
<td></td>
<td></td>
<td><em>System:</em> Process PORR information for Fiscal</td>
</tr>
<tr class="odd">
<td><strong>10</strong></td>
<td></td>
<td></td>
<td><em>System:</em> Update FCP &amp; FMS</td>
</tr>
</tbody>
</table>

### The Audit File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When IFCAP builds the RIL, it also adds appropriate information to the DYNAMED IFCAP INTERFACE AUDIT (File \#414.02) (referred to simply as “the Audit File”). This file is not accessed by the user options, but is updated in the background when:

- A new DynaMed RIL is built
- A DynaMed RIL is generated into a 2237 or a purchase card order
- A 2237 or purchase card order containing DynaMed requested items is cancelled
- DynaMed Requested Items are deleted from a 2237 or purchase order
- A Receiving Report containing DynaMed requested items is deleted

This file may be helpful when questions arise concerning discrepancies between IFCAP and DynaMed. MailMan messages will be created by the system in the event that it cannot update the audit file or it finds a problem with the file. These messages will be forwarded to the members of the PRCV Audit File Alerts mail group. This mail group is new with this interface

### Using DynaMed Requisitions in IFCAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The replenishment process begins in DynaMed, where Manager Orders and Daily Cycle requisitions are generated. When the requisition is created in DynaMed, messages with requisition data are sent across the Interface to IFCAP. Once the message reaches IFCAP, a Repetitive Item List (RIL) is automatically created.

### Using Repetitive Item Lists (RILs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Constraints on Repetitive Item Lists

RILs generated from DynaMed requests for replenishment are governed by the following restrictions:

- RILs cannot be edited (although they can be deleted or cancelled).

> *Editing a RIL could introduce potential inconsistencies with DynaMed Due-ins. Since the RIL is not a permanent accountable document, it was decided it would be best to wait until items were on a 2237 before any editing occurred.*

- RILs cannot be re-used, and users will not be prompted to allow re-use.

> *DynaMed RILs cannot be re-used because each item is linked via the new IFCAP field DynaMed Document ID \[DM DOC ID\] to a unique request number (DynaMed Document Number) in the DynaMed database. Since each DynaMed Document Number can only be associated in DynaMed with a single purchase order, the DM DOC ID must not be duplicated in another IFCAP 2237 or Purchase Order. It is for this reason that users are not prompted to re-use these RILs, and such RILs are automatically deleted after use.*

- RILs containing DynaMed-requested items are intended to be used in generating only Purchase Card orders and 2237s.

> *According to the needs of the REDACTED VAMC, the DynaMed-IFCAP Interface was not set up to accommodate generating anything except a 2237 or Purchase Card (PCard) Order from a DynaMed RIL.*

#### New Report Identifying DynaMed RILs 

A new report, DynaMed RILs Needing Action, provides a quick look at the DynaMed RILs waiting to be processed in IFCAP.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Repetitive Item List Menu Option: DynaMed RIL's Needing Action</p>
<p>DEVICE: ;;99999 INCOMING TELNET Right Margin: 80//</p>
<p>DYNAMED IFCAP INTERFACE AUDIT SEARCH JUN 13,2005 12:28 PAGE 1</p>
<p>RIL# ENTERED BY NAME</p>
<p>VENDOR ITEM DATE NEEDED BY</p>
<p>--------------------------------------------------------------------------------</p>
<p>DATE/TIME CREATED IN DYNAMED: APR 12,2005 11:01</p>
<p>100-05-3-076-828100-0017</p>
<p>RANDOMVENDOR 106701 APR 16,2005</p>
<p>100-05-3-076-828100-0017</p>
<p>RANDOMVENDOR 106749 APR 16,2005</p>
<p>100-05-3-076-828100-0017</p>
<p>RANDOMVENDOR 106750 APR 16,2005</p>
<p>DATE/TIME CREATED IN DYNAMED: APR 19,2005 14:12</p>
<p>100-05-3-076-828100-0032 REDACTED</p>
<p>EXAMPLECO INC 106725 JUN 15,2005</p>
<p>100-05-3-076-828100-0032 REDACTED</p>
<p>SAMPLENAME 106706 APR 23,2005</p>
<p>100-05-3-076-828100-0032 REDACTED</p>
<p>UNIVERSAL HOME HEALTH 106763 APR 23,2005</p>
<p>100-05-3-076-828100-0032 REDACTED</p>
<p>RANDOMVENDOR 106701 APR 23,2005</p>
<p>100-05-3-076-828100-0032 REDACTED</p>
<p>EXAMPLECO INC 106741 APR 21,2005</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Processing a Repetitive Item List 

|                                                                                                     |                                                                                         |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/021.png) | *Warning:* You may not edit a DynaMed-generated RIL. You may only process or delete it. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/022.png) |

Once created in IFCAP, a DynaMed RIL can only be processed in one of three ways. These activities include:

- Canceling the RIL

> *Canceling a RIL automatically triggers a message to DynaMed to cancel the associated DynaMed Due-ins.*

- Generating a 2237

> *No update is sent to DynaMed as a result of the 2237 being generated; that comes later in the process when the 2237 is Approved or Cancelled.*

- Generating a Purchase Card Order

> *No update is sent to DynaMed as a result of the PC order being generated; that comes later in the process when it is Approved or Cancelled.*

|                                                                                                     |                                                                                                                                                                                                                  |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/023.png) | *Warning:* Up-arrowing ( ^ ) out of the RIL to generate Purchase Card Orders will cause all items on the RIL to be deleted. Those items not yet moved to a Purchase Card Order will be cancelled in DynaMed. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/024.png) |

### Using 2237s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Constraints on Using 2237s

2237s created from DynaMed RILs can be edited, cancelled, and approved. The REDACTED VAMC indicated that items not requested from the DynaMed systems would not be added to an existing 2237 created from a DynaMed RIL. Therefore, *no items should be added to a DynaMed 2237*, as they will not automatically update DynaMed.

|                                                                                                     |                                                                                                                                                                                                                                                                                                                                    |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/025.png) | *Warning:* The prohibition on adding items during an edit of a DynaMed-generated 2237 is a Business Rule, and is not enforced by the Interface software. Users must exercise due care in editing 2237s, because items added during a 2237 edit session will be unknown to DynaMed—and therefore cannot be received into inventory. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/026.png) |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/027.png)</td>
<td><p><em>Technical Notes:</em></p>
<ol type="1">
<li><p>The Issue Book Form Type on the 2237 is no longer available for sites using the DynaMed inventory system.</p></li>
<li><p>You should not use the “Copy a Transaction” option for 2237s created from a DynaMed-generated RIL, as this will not automatically update DynaMed.</p></li>
<li><p>You should not use the “Change Existing Transaction Number” option for any DynaMed-generated inventory request, because there is potential for creating problems with the interface.</p></li>
</ol></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/028.png)</td>
</tr>
</tbody>
</table>

If IFCAP encounters any item on a DynaMed-generated 2237 that is missing a DynaMed Document ID, it will notify the members of the PRCV Audit File Alerts Mail Group (see section 4.2.3.2) that the DynaMed Document ID is missing.

#### New “Date Needed By” Field

While editing a DynaMed 2237, users will note a new date field (Date Needed By) that is displayed to assist the Control Point staff in filling in the IFCAP delivery schedule. See section 2.11 for an example of how this date is displayed.

#### Processing a 2237

Transactions will be sent to update DynaMed Due-Ins when certain activities occur. These activities include:

- Canceling the 2237

> *Canceling a 2237 automatically triggers a message to DynaMed to cancel the associated DynaMed Due-ins.*

- Deleting one or more items from the 2237

> *Canceling one or more items from the 2237 automatically triggers a message to DynaMed to cancel the associated DynaMed Due-ins.*

- Approving the 2237

> *An update is sent to DynaMed when the Approving Official approves the 2237.*

#### Splitting 2237s

Placing DynaMed requested items from a single 2237 onto separate purchase orders will not adversely affect the DynaMed-IFCAP Interface. However, it is strongly advised that the comment field created when a 2237 is split *not* be deleted or edited.

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Date Needed By and DynaMed Document ID will display on the display or printout of a 2237 transaction that was created from a RIL containing DynaMed requested items

### Creating Purchase Orders and Purchase Card Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When creating a purchase order for DynaMed requested items, select either the INVOICING/RECEIVING REPORT or PURCHASE CARD method of processing. Although IFCAP allows other methods of processing to be selected, these other methods are not designed to work with the Interface. Since updates from IFCAP to DynaMed are closely controlled, several rules must be observed when creating purchase orders or purchase card orders:

|                                                                                                     |                                                                                                                                                                                                                                            |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/029.png) | Use *only* the INVOICING/RECEIVING REPORT or PURCHASE CARD method of processing for DynaMed-related purchase orders. Using other methods of processing may yield unexpected results and are not guaranteed to update DynaMed appropriately | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/030.png) |

|                                                                                                     |                                                                                                                                                                                                                                                                                        |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/031.png) | In the User’s purchase card orders, the ‘Receiving Requested’ field containing DynaMed requested items is always set to Yes. This ensures that DynaMed will be alerted of receipt activity, will be able to update their due-ins and will be able to complete their receiving process. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/032.png) |

|                                                                                                     |                                                                                                                                                          |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/033.png) | Items should not be added to purchase orders or purchase card orders created from a DynaMed-generated RIL, as this will not automatically update DynaMed | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/034.png) |

|                                                                                                     |                                                                                                    |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/035.png) | Purchasing Agents should not add a non-DynaMed 2237 to a purchase order containing a DynaMed 2237. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/036.png) |

|                                                                                                     |                                                                                                                                                  |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/037.png) | Purchase orders created from a DynaMed-generated RIL may not have an item packing multiple greater than “1” when the unit of purchase is “Each.” | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/038.png) |

IFCAP will build and transmit update messages to DynaMed whenever:

- A Purchase order containing DynaMed-requested items is approved by the Approving Official
- A DynaMed-requested item is deleted from a Purchase Order (*note:* this does *not* include disassociating the 2237 from a Purchase Order)
- A Purchase Card order containing DynaMed-requested items is deleted

### Processing Amendments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Amendments are communicated to DynaMed when:

- The amendment is one of the following types:

| 1   | Line Item Edit    |
|-----|-------------------|
| 2   | Line Item Delete  |
| 3   | Change Vendor     |
| 4   | Replace PO Number |
| 5   | Authority Edit    |

- The delivery date is changed
- The amendment is signed (supply or Purchase Card Orders)
- The amendment is processed by Fiscal Service

|                                                                                                     |                                                                                                                |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/039.png) | Items may not be added through the amendment process to a purchase order created from a DynaMed-generated RIL. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/040.png) |

### Processing Receipts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will alert DynaMed of receipts containing DynaMed-requested items after the Warehouse has approved the Receiving Report in IFCAP. Notice of deleted Receiving Reports will also be communicated.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/041.png)</td>
<td><p><em>Note:</em></p>
<p>In order to better track quantities, the due-in amount must be adjusted to reflect any difference in the quantity ordered, even if the ordered quantity is amended after a receipt.</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/042.png)</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/043.png)</td>
<td><p><em>Note:</em> Please be aware that changes in cost <em>should</em> be addressed <em>before</em> receiving the order. Any item price change done through the amendment process after the item is received must be addressed manually in DynaMed using the K-9 screen to correct the item cost. Alternatively, you may:</p>
<ol type="1">
<li><p>Delete the Receiving Report (if not processed in Fiscal) or do an adjustment voucher to cancel the receipt for the item</p></li>
<li><p>Do an amendment for change in cost for the item</p></li>
<li><p>Then receive the item again with the corrected cost</p></li>
</ol></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/044.png)</td>
</tr>
</tbody>
</table>

|                                                                                                     |                                                                                                                              |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/045.png) | *Note:* Quantities for inventory items must always be received in whole numbers—no fractional quantity receipts are allowed. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/046.png) |

### Processing Adjustments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adjustments are sent to DynaMed as soon as they are signed. Notification to DynaMed is not dependent on Fiscal processing of the receipt.

## Issue Books and Adjustments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/047.png) | *Note:* Anyone using DynaMed in a manner that generates Issue Book Transactions to IFCAP *must* be a user in the IFCAP control point associated with the stockroom buying from Supply. Any issue book transaction received by IFCAP that is associated with a DynaMed user who is not a user in the buying control point will be rejected, and will not be processed to update the control point balance or FMS as expected. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/048.png) |

Upon activation of the DynaMed-IFCAP Interface (with its subsequent update interface to FMS), IFCAP will build *internal voucher* (IV) original and modification documents to reflect sale of goods by the Supply Fund warehouse inventory to other inventories, as well as any returns or refusals of goods from the warehouse that take place within DynaMed. An IV is created when an item is transferred from the warehouse to other using service stockroom, or when an adjustment to a stockroom transfer is accomplished through the return or refusal process in DynaMed. IFCAP will also build *standard voucher* (SV) documents to reflect changes in the value of the Supply Fund warehouse inventory stock when adjustments are made in DynaMed.

In the case of the IV process, DynaMed sends a message to IFCAP that creates entry records in the Control Point Activity File (File \# 410), which in turn updates the Fund Control Point (FCP) balances for the two control points involved in the transfer (decrease in one FCP and increase in the other FCP). For the original IV this running balance update includes the 1% surcharge added to the inventory value of the item(s). The surcharge is not refunded in IV adjustments for returns or refusals. These entries appear in the control Point's Running Balance. The appropriate FMS documents are then generated and sent to Austin to ensure accurate updating of the General Ledger.

In the case of the SV, DynaMed sends a transaction to IFCAP, and IFCAP creates an FMS code sheet to update Supply Fund Inventory Value in FMS. No FCP updates are necessary.

The IV and SV documents will also appear on the Stack Status Report \[PRC GECS STACK REPORT\]. In the event of a rejection, the Fiscal user will have to go online in FMS to correct the transaction, as it can not be reprocessed in either IFCAP or DynaMed.

In the following display, sample 2-sided transactions for Issue Book original and modifications for obligation IV-100i56036 are bolded.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CONTROL POINT BALANCE - 100-05-3-076- WARD JUN 08, 2005@12:20:27 PAGE 1</p>
<p>FISCAL</p>
<p>FYQSeq# TXN OBL # AP/OB DT COMM $AMT CP $BAL OBL $AMT UNOBL $BAL</p>
<p>--------------------------------------------------------------------------------</p>
<p>0531018 CEI 06/06/05 -1000.00 712011.62 -1000.00 6258599.57</p>
<p>0531020 ISS I56027 06/07/05 216.10 711795.52 216.10 6258383.47</p>
<p>0531021 ISS I56028 06/07/05 191.40 711604.12 191.40 6258192.07</p>
<p>0531022 ISS I56029 06/07/05 543.95 711060.17 543.95 6257648.12</p>
<p>0531023 ISS I56030 06/07/05 624.48 710435.69 624.48 6257023.64</p>
<p>0531024 ISS I56031 06/07/05 220.28 710215.41 220.28 6256803.36</p>
<p>0531025 ISS I56032 06/07/05 99.99 710115.42 99.99 6256703.37</p>
<p>0531026 ISS I56033 06/07/05 312.29 709803.13 312.29 6256391.08</p>
<p>0531027 ISS I56034 06/07/05 404.64 709398.49 404.64 6255986.44</p>
<p>0531028 ISS I56035 06/07/05 807.75 708590.74 807.75 6255178.69</p>
<p><strong>0531029 ISS I56036 06/07/05 5272.48 703318.26 5272.48 6249906.21</strong></p>
<p>0531030 ISS I56037 06/07/05 1039.63 702278.63 1039.63 6248866.58</p>
<p>0531031 ADJ I56035-ADJ 06/07/05 -108.86 702387.49 -108.86 6248975.44</p>
<p>0531032 ADJ I56036-ADJ 06/07/05 -108.86 702496.35 -108.86 6249084.30</p>
<p>0531033 ADJ U50082-1 06/08/05 0.00 702496.35 0.00 6249084.30</p>
<p><strong>0531034 ADJ I56036-ADJ 06/08/05 -235.82 702732.17 -235.82 6249320.12</strong></p>
<p>0531035 ADJ I56031-ADJ 06/08/05 -798.72 703530.89 -798.72 6250118.84</p>
<p><strong>0531036 ADJ I56036-ADJ 06/08/05 -798.72 704329.61 -798.72 6250917.56</strong></p>
<p>Press return to continue, uparrow (^) to exit:</p>
<p>CONTROL POINT BALANCE - 100-05-3-4537- SUPPLY JUN 08, 2005@12:20:27 PAGE 1</p>
<p>FISCAL</p>
<p>FYQSeq# TXN OBL # AP/OB DT COMM $AMT CP $BAL OBL $AMT UNOBL $BAL</p>
<p>--------------------------------------------------------------------------------</p>
<p>0510269 CEI 06/06/05 500.00 1092168.73 500.00 1220199.56</p>
<p>0530270 ISS I56027 06/07/05 -216.10 1092384.83 -216.10 1220415.66</p>
<p>0530271 ISS I56028 06/07/05 -191.40 1092576.23 -191.40 1220607.06</p>
<p>0530272 ISS I56029 06/07/05 -543.95 1093120.18 -543.95 1221111.01</p>
<p>0530273 ISS I56030 06/07/05 -624.48 1093744.66 -624.48 1221775.49</p>
<p>0530274 ISS I56031 06/07/05 -220.28 1093964.94 -220.28 1221995.77</p>
<p>0530275 ISS I56032 06/07/05 -99.99 1094064.93 -99.99 1222095.76</p>
<p>0530276 ISS I56033 06/07/05 -312.29 1094377.22 -312.29 1222408.05</p>
<p>0530277 ISS I56034 06/07/05 -404.64 1094781.86 -404.64 1222812.69</p>
<p>0530278 ISS I56035 06/07/05 -807.75 1095589.61 -807.75 1223620.44</p>
<p><strong>0530279 ISS I56036 06/07/05 -5272.48 1100862.09 -5272.48 1228892.92</strong></p>
<p>0530280 ISS I56037 06/07/05 -1039.63 1101901.72 -1039.63 1229932.55</p>
<p>0530281 ADJ I56035-ADJ 06/07/05 108.86 1101792.86 108.86 1229823.69</p>
<p><strong>0530282 ADJ I56036-ADJ 06/07/05 108.86 1101684.00 108.86 1229714.83</strong></p>
<p><strong>0530283 ADJ I56036-ADJ 06/08/05 235.82 1101448.18 235.82 1229479.01</strong></p>
<p>0530284 ADJ I56031-ADJ 06/08/05 798.72 1100649.46 798.72 1228680.29</p>
<p><strong>0530285 ADJ I56036-ADJ 06/08/05 798.72 1099850.74 798.72 1227881.57</strong></p>
<p>Press return to continue, uparrow (^) to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/049.png)</td>
<td><p><em>Note:</em> Since all this is done in DynaMed, and the IB Form Type is not available on the new 2237 Request option, then the following options are no longer to be used in conjunction with IB requests.</p>
<ul>
<li><p>Edit a 2237 (Service) [PRCSEDTD]</p></li>
<li><p>New 2237 (Service) Request [PRCSENRB]</p></li>
<li><p>Copy a Transaction [PRCSECP]</p></li>
<li><p>Edit a Request (Section) [PRCSEDRS]</p></li>
<li><p>Enter a Request (Section) [PRCSENRS]</p></li>
<li><p>Copy a Transaction (Section) [PRCSCPY]</p></li>
</ul></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/050.png)</td>
</tr>
</tbody>
</table>

## Fiscal Updates and Fund Control Point Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DynaMed users (generally inventory managers) may subscribe to updates on specified IFCAP fund control point (FCP) balances. This process periodically sends the Fund Control Point Uncommitted Balance for current Fiscal Year and Future Fiscal Year to DynaMed. When a DynaMed user is creating due-ins, these amounts plus the total of the order being built, are displayed on the DynaMed screen.

In IFCAP, a new subscription file (File \#414.03) has been established to record subscriptions and subscription cancellations. DynaMed sends subscription and cancellation requests to IFCAP. Once the subscription is entered, IFCAP sends messages to DynaMed whenever specified events occur that affect the balances. For balance updates (modifications), IFCAP sends the following to DynaMed in an MFN^M01 message: to DynaMed in an MFN^M01 message:

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>Fiscal Year</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>1st Quarter Uncommitted Balance</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>FCP</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>2nd Quarter Uncommitted Balance</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>Station</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>3rd Quarter Uncommitted Balance</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td><ul>
<li><blockquote>
<p>4th Quarter Uncommitted Balance</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

An FCP Monitor task loops through the Fund Control Point (File \#420) file, essentially computing the “running total” of the uncommitted balances for the control point, and if it notes a change to the balances since the last time the monitor ran, the new balances will be sent to DynaMed.

To implement the logic that handles this event, additional code checks that: (1) the site is a DynaMed site and (2) the control point affected is being monitored (that is, there is a corresponding entry in the subscription file). When both conditions are met, the delivery of an HL7 message to DynaMed is scheduled.

For more information on how this process is seen from DynaMed, see the *DynaMed User Manual*, available at REDACTED

## Item File Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IFCAP Item Master File (IMF) has been designated as the file of record for items. For this reason all changes, additions and modifications are entered first into the IFCAP IMF and are then transmitted to the DynaMed Master Catalog.

Changes to the Item File may occur during the processing of Purchase Orders. Those changes are also transmitted to the DynaMed Master Catalog via the background task PRCV ITEM UPDATE TO DYNAMED, which is a nightly ITEM Master File update to DynaMed.

Table 3‑3. Item File Updates Flow

| Step  | DynaMed                                 | Data Flow | IFCAP                                                                                   |
|-------|-----------------------------------------|-----------|-----------------------------------------------------------------------------------------|
|       |                                         |           |                                                                                         |
| 1 | *System:* Update DynaMed Master Catalog |           | *User:* Add a new item to IFCAP Item Master File (IMF)                                  |
| 2 | *System:* Update DynaMed Master Catalog |           | *User:* Edit, Inactivate or reactivate an existing item in IFCAP Item Master File (IMF) |

|                                                                                                     |                                                                                                                                                                      |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/051.png) | When entering or editing an item in the Item Master File, items may not have vendors with a packaging multiple greater than “1” when the unit of purchase is “Each.” | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/052.png) |

|                                                                                                     |                                                                                                                                                                                                                             |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/053.png) | *Note:* Updates to the Item Master File not done directly through the Item Edit option, such as when editing an item on a purchase order, will be sent to DynaMed via a batched job and may not be immediately transmitted. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/054.png) |

## Vendor File Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IFCAP Vendor Master File (VMF) has been designated as the file of record for vendors. For this reason all changes, additions and additions occur first in the VMF, then are transmitted to the DynaMed Catalog Master. Under most circumstances, this data exchange is accomplished during a periodic “batch” process (as of this writing, every three hours). There are, however, special rules to cover the occasion when item data is to be transmitted from IFCAP to DynaMed and a vendor is associated with that item.

|                                                                                                     |                                                                                                                                                                                                                                                                                                                                                              |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/055.png) | When the vendor associated with one or more item(s) is modified via an IFCAP event that sends information about those item(s) back to DynaMed, the revised vendor data is transmitted prior to the item data; this gives DynaMed both sets of data affecting procurement of the item(s). No user action is required; this process takes place automatically. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/056.png) |

Table 3‑4. Vendor File Updates Flow

| Step  | DynaMed                                | Data Flow | IFCAP                                                                                        |
|-------|----------------------------------------|-----------|----------------------------------------------------------------------------------------------|
|       |                                        |           |                                                                                              |
| 1 | *System:* Update DynaMed Vendor Master |           | *User:* Add a new Vendor to IFCAP Vendor Master File (VMF)                                   |
| 2 | *System:* Update DynaMed Vendor Master |           | *User:* Edit, Inactivate or Re-activate an existing Vendor in IFCAP Vendor Master File (VMF) |

### ### New Report Displays Item and Associated Vendors with Vendor \# 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new report, DynaMed Item Display with Vendor \#, provides a list of items with the associated vendors and vendor numbers.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select ITEM MASTER NUMBER: 42</p>
<p>1 42 CONTROL-4C PLUS TRIPAK LO/NORM/HI 3.3ML-9S</p>
<p>2 420-7715 8006 NITROFURANTOIN MACRO CAP-100MG-1M</p>
<p>3 420-7716 4958 NITROFURANTOIN MACRO CAP-50MG-1M</p>
<p>4 420-9859 17674 BANDAGE-ELAS-ROLLED-4INX5YD-20S</p>
<p>5 421-6429 20371 STOCKING-ANTI EMBOLISM-KNEE-XLRG LONG</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 1 42 CONTROL-4C PLUS TRIPAK LO/NORM/HI 3.3ML-9S</p>
<p>DEVICE: INCOMING TELNET Right Margin: 80//</p>
<p>NUMBER: 42 NIF ITEM NUMBER:</p>
<p>SHORT DESCRIPTION: CONTROL-4C PLUS TRIPAK LO/NORM/HI 3.3ML-9S</p>
<p>DESCRIPTION:</p>
<p>CONTROLS, TRIPACK LOW/NORMAL/HIGH, 3.3ML, 4C PLUS COULTER 7546771</p>
<p>MFG PART NO.:</p>
<p>BOC: 2631 Drugs, Medicines and Chemical Supplies</p>
<p>FSC: 6550 NSN:</p>
<p>LAST VENDOR ORDERED: (9618) COMPANY HEALTHCARE /I V SYSTEMS</p>
<p>MANDATORY SOURCE:</p>
<p>FCP: 100:076 PREFERRED VENDOR:</p>
<p>VENDOR: (206) ARANDOM SCIENTIFIC INC</p>
<p>UNIT OF PURCHASE: PG UNIT COST: 111.28</p>
<p>PACKAGING MULTIPLE: 9 UNIT CONVERSION FACTOR: 1</p>
<p>VENDOR STOCK #: 194-324 CONTRACT: V573P-3027/CONS</p>
<p>VENDOR: (217) ARANDOM SCIENTIFIC INC</p>
<p>UNIT OF PURCHASE: PG UNIT COST: 111.28</p>
<p>PACKAGING MULTIPLE: 9 UNIT CONVERSION FACTOR: 1</p>
<p>VENDOR STOCK #: 194-324 CONTRACT: V573P-3027/CONS</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Interface Activation, Maintenance, and Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Preparing to Activate the DynaMed-IFCAP Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Coordinate Plans with Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A&MM and Control Point Staff will be impacted by activating this patch. Be certain that any preliminary tasks have been identified and addressed. In addition, the site may choose to modify the way or volume of business initiated while implementing this interface in order to minimize any complications.

### Enter the Fund Control Points into DynaMed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DynaMed system must be set up to send the correct Fund Control Point to IFCAP or each of its stockrooms. Conversely, DynaMed must be able to recognize the correct stockroom for messages from IFCAP.

### Set Up DynaMed System with the DUZ of its Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Dictionary on DynaMed must be set up with the IFCAP DUZ of all DynaMed users. This is necessary in order that the systems will be able to validate transactions and process them.

### Standardize the Item and Vendor Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The item numbers for stock must be the same in both the IFCAP Item Master and the DynaMed Master Catalogue. The interface uses the item number in it inventory-related transactions.

### The Vendo/Item File Relationship

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The preferred and mandatory vendors must be set up the same way for each system. Inconsistencies will prevent IFCAP from successfully generating a RIL from a DynaMed request for replenishment.

### Setup Common Number Series for Processing Issue Book Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Using the Establish Common Number Series, reset Next Number to be a higher value (incremented by 1) than the current setting.
- This will ensure that any I5 numbers already entered manually into FMS will not be selected automatically by the Interface software.

### Discuss Interface Communications Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Discuss Communications issues related to the interface with all appropriate groups. Work may be needed on the VistA Interface Engine and in DynaMed in order to activate the interface.

### Run Item and Vendor Update Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To permit the IFCAP system to notify DynaMed if Items or Vendors are added or edited, the software tracks a checksum of the current record. If the checksum changes, IFCAP sends the updated record to DynaMed.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/057.png)</td>
<td><p><em>Technical Notes:</em></p>
<p>Run the Routines to populate the Record Checksum File (#414.04) for the current values of records in the Master Item File (#441) and the Vendor File (#440).</p>
<p>Run INIT^PRCVIT and INIT^PRCVNDR.</p>
<p>See section 4.2.8.1</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/058.png)</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/059.png)</td>
<td><p><em>Technical Note:</em></p>
<p>The Vendor Update background task and the Item background task should be scheduled to run before the Daily Cycle is run in DynaMed. This will ensure that the DynaMed user has the opportunity to update the DynaMed tables with the most recent data available before the ordering cycle occurs.</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/060.png)</td>
</tr>
</tbody>
</table>

### Attach New Report (DynaMed Item Display with Vendor \#) to User Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We suggest this report be attached to the following menus:

- Control Point Official and Clerks: under the Process a Request menu
- Pcard Users: under the Process Purchase Card Menu
- Purchasing Agent: under the Purchase Orders Menu

### Attach New Report (DynaMed RIL's Needing Action) to User Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We suggest this report be attached to the following menus:

- Control Point Official and Clerks: under the Repetitive Item List Menu
- PCard Users: under the Process Purchase Card Menu

### Verify Appropriate Staff Are Set to Receive Interface Activity Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fund Control Point staff working with the interface must meet the following criteria in order to receive updates concerning interface activity:

- The individual must be an official or a clerk for the fund control point of interest.
- The individual must have the Notification Designee flag set to ‘yes’

## Activating the DynaMed-IFCAP Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to activate the interface, the site must set the system parameter definition for PRCV COTS INVENTORY. See section 2.2 for more information on this parameter.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/061.png)</td>
<td><p><em>Technical Notes:</em></p>
<p>These 2 options <em><strong>must</strong></em> be started prior to users using the system:</p>
<p>PRCV ITEM UPDATE TO DYNAMED</p>
<p>PRCV VENDOR UPDATE TO DYNAMED</p>
<p>Be certain that these are scheduled to run <em>after</em> completing the other set-up steps.</p>
<p>The funds monitor must also be started (see instructions below).</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/062.png)</td>
</tr>
</tbody>
</table>

### Verify Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify PRC\*5.1\*81 is installed as per the instructions after verifying that all released IFCAP patches are installed.

### Mark Options Out of Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Keep staff out of IFCAP during the set up process after installing PRC\*5.1\*81 by marking the following IFCAP options Out Of Order:

- Item File Edit \[PRCHPC ITEM EDIT\]
- Combined A&MM Menu \[PRCHUSER MASTER\]
- Control Point Official's Menu \[PRCSCP OFFICIAL\]
- Delivery Orders Menu \[PRCH DELIVERY ORDER MENU\]
- Funds Distribution & Accounting Menu \[PRCF MASTER\]
- IFCAP Application Coordinator Menu \[PRCHUSER COORDINATOR\]
- Purchase Card Menu \[PRCH PURCHASE CARD MENU\]
- New Purchase Order \[PRCHPC PO ADD\]
- Edit an Incomplete Purchase Order \[PRCHPC PO EDIT\]
- Edit Direct Delivery Order for Purchase Card \[PRCH PC DIRECT DELIVERY2\]
- New Direct Delivery Order for Purchase Card \[PRCH PC DIRECT DELIVERY1\]
- Item File Edit \[PRCHPC ITEM EDIT\]
- Vendor File Edit \[PRCHPC VEN EDIT\]
- Direct Delivery Patient Edit \[PRCHPC PAT EDIT\]
- Inactivate Item \[PRCHPC ITEM INACTIVATE\]
- Reactivate Item \[PRCHPC ITEM REACTIVATE\]
- Inactivate Vendor \[PRCHPC VEN INACTIVATE\]
- Reactivate Vendor \[PRCHPC VEN REACTIVATE\]
- Setup AR selected vendors \[PRCO AR SUPPLY VENDOR EDIT\]
- Item File Edit \[PRCHPC ITEM EDIT\]
- New Simplified Purchase Card Order \[PRCH ENTER SIMPLIFIED ORDER\]
- \*\*\> Locked with ADBW PRCH SIMPLE ORDER
- Edit Simplified Purchase Card Order \[PRCH EDIT SIMPLIFIED ORDER\]
- New Detailed Purchase Card Order \[PRCH ENTER DETAILED ORDER\]
- Edit Detailed Purchase Card Order \[PRCH EDIT DETAILED ORDER\]
- Create P/C Order From Repetitive Item List \[PRCH CREATE PURCHASE CARD\]
- Convert P/C Order to a Delivery Order \[PRCH CONV P/C ORDER TO A DEL\]
- New Repetitive Item List (Enter) \[PRCSRI ENTER\]
- Edit Repetitive Item List Entry \[PRCSRI EDIT\]
- Delete Repetitive Item List Entry \[PRCSRI DELETE\]
- Print/Display Repetitive Item List Entry \[PRCSRI PRINT/DISPLAY\]
- Generate Requests From Repetitive Item List Entry \[PRCSRI GENERATE\]
- Enter Delivery Order \[PRCH ENTER DELIVERY ORDER\]
- Edit Delivery Order \[PRCH EDIT DELIVERY ORDER\]
- Enter Pharmaceutical PV Order \[PRCH ENTER PHARMACY ORDER\]
- Edit Pharmaceutical PV Order \[PRCH EDIT PHARMACY ORDER\]
- Create Delivery Order From Repetitive Item List \[PRCH CREATE DEL ORDER\]
- New Invoice \[PRCFD ADD NEW INVOICE\]
- Edit FMS Vendor Payment Information \[PRCFD VENDOR EDIT\]
- Incomplete Invoice Edit \[PRCFD EDIT INCOMPLETE INVOICE\]

### Set up Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set up the following mail groups.

#### PRCV Item Vendor Edits 

Make the following people subscribers to this mail group:

- AM&M Staff who maintain the Item and Vendor Files
- SPD Staff who maintain the Item and Vendor Files
- IFCAP Coordinator
- IRM staff

#### PRCV Audit File Alerts

This mail group should include the IFCAP Application Coordinator and anyone who needs to be notified of inconsistencies in the Audit File or the system’s inability to update this file.

### Set Up AFREE Cross-Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set up the AFREE cross-reference on File \#441. This will take approximately 1 minute.

- Lock File \#441 (^PRC(441)
- Re-index File \#441 as shown:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Utility Functions Option: RE-Index File</p>
<p>MODIFY WHAT FILE: ITEM MASTER//</p>
<p>THERE ARE 18 INDICES WITHIN THIS FILE</p>
<blockquote>
<p>DO YOU WISH TO RE-CROSS-REFERENCE ONE PARTICULAR INDEX? No// Y (Yes)</p>
<p>What type of cross-reference (Traditional or New)?Traditional// NEW</p>
</blockquote>
<p>File: ITEM MASTER (#441)</p>
<blockquote>
<p>Select Subfile:</p>
<p>Current Indexes on file #441:</p>
<p>534 'AFREE' index</p>
<p>Which Index do you wish to re-cross-reference? 534// ?</p>
</blockquote>
<p>Select one of the following:</p>
<p>534 AFREE</p>
<blockquote>
<p>Which Index do you wish to re-cross-reference? 534// AFREE</p>
<p>Do you want to delete the existing 'AFREE' cross-reference? YES</p>
</blockquote>
<p>Do you want to re-build the 'AFREE' cross reference? YES ...DONE!</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Release the lock on File \#441 (^PRC(441)

### Set up Connectivity Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The listener for this build is the multi-listener in use at the site. Verify your local Vitria box is set up to send transactions associated with this interface to the port where this multi-listener resides.
- The client link PRCVDYNA needs to be set up with the IP address and a port number of your local Vitria box. Please verify the following settings for this link:

NODE: PRCVDYNA

> LLP TYPE: TCP

DEVICE TYPE: Non-Persistent Client

AUTOSTART: Enabled

RE-TRANSMISSION ATTEMPTS: 3

> EXCEED RE-TRANSMIT ACTION: ignore

> TCP/IP SERVICE TYPE: CLIENT (SENDER)

> PERSISTENT: NO

- The facility for IFCAP will default to

> \<station number\> ^ \<station domain\> ^ DNS

> If this is not what you want to use, you will need to populate the Facility field in each HL7 Application Parameter in the PRCV_IFCAP series. This value must be coordinated with your DynaMed systems representative as they will also need to enter this into their system.

- The facility name for DynaMed must be entered into the facility prompt of the HL7 Application Parameter called PRCV_DYNAMED. The value should be populated based on instructions included with the install and must be coordinated with your DynaMed systems representative as they will also need to enter this into their system.
- After the set up is completed, 'start the PRCVDYNA link'. If the listener is not up, get that started as well.

### Add Options to Appropriate Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add these two options to their appropriate menus:

#### DynaMed RIL's Needing Action

> \[PRCV DYNAMED RIL'S NEED ACTION\]

Add to the following menus:

- Repetitive Item List Menu \[PRCSRI MENU\]
- Process Purchase Card Menu \[PRCH PROCESS PC\]

#### PRCV ITEM WITH VENDOR#

Add to the following menus: 

 

- Process Purchase Card Menu    \[PRCH PROCESS PC\]
- Process a Request Menu     \[PRCSER\]   
- Purchase Orders Menu     \[PRCHPC PO\]
- Display/Print Menu (PPM)    \[PRCHPM DISPLAY MENU\]

### Set DynaMed “Switch”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set the system parameter definition for PRCV COTS INVENTORY to 1 (DYNAMED).

When the patch is first installed the value of the parameter will be null. The value of this parameter can be viewed at any time by executing the following code:

- \>W \$\$CHK^PRCVITMU

This actually causes the following code to be executed:

> W \$\$GET^XPAR("SYS","PRCV COTS INVENTORY",1,"Q")

To set the interface up to work with DynaMed, execute the following:

- D EN^XPAR("SYS","PRCV COTS INVENTORY",1,1,.PRCVEM)

Verify the set worked. If anything is returned in PRCVEM, try the code again. If the problem continues, contact EVS.

- \>W \$\$CHK^PRCVITMU

1

- \>ZW PRCVEM

PRCVEM=0

If you need to turn the interface setting back to not use DynaMed, the code to execute is:

- \>D EN^XPAR("SYS","PRCV COTS INVENTORY",1,0,.PRCVEM) \<to use IFCAP\>
- \>ZW PRCVEM

PRCVEM=0

- \>W \$\$CHK^PRCVITMU

0

### Populate and Initialize Record Checksum File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Populate the Record Checksum File (#414.04) for the current values of records in the Master Item File (#441) and the Vendor file (#440). These routines will tie up the PC for the period of time they take to run.

This process may take up to 30 minutes, and will tie up the PC until it is finished.

D INIT^PRCVINIT

 

Item file checksum initialization beginning...

 

Item file checksum initialization complete!

 

Vendor file checksum initialization beginning...

 

Vendor file checksum initialization complete!

Possible errors:

The site parameter is not properly set for use of the COTS Inventory interface!

> *Solution:* You must set the PRCV COTS Inventory system parameter to 1 prior to running this routine.

Item or Vendor file checksum has already been initialized!

> *Solution:* If the routine needs to be re-run, you need to delete whatever now exists for ^PRCV(414.04, 1) and ^PRCV(414.04,2).

Item file checksum initialization failed!

*Solution:* Contact EVS.

Vendor file checksum initialization failed!

*Solution:* Contact EVS.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/063.png)</td>
<td><p><em>Technical Notes:</em></p>
<p>Only Items whose IENs are greater than or equal to 100,000 will have checksums added to File 414.04. This is because items less than 100,000 are not used by DynaMed.</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/064.png)</td>
</tr>
</tbody>
</table>

### Test Connectivity/Establish Subscriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Start the Monitor

The fund monitor adds two new fields to File \#411:

FCP MONITOR STATUS (#106)

FCP MONITOR RUNNING? (#107)

Each is a set of codes. The permissible values for \#106 are:

0 NOT USED

1 ENABLED

2 NOT ENABLED

A screen limits the permissible values to 'NOT USED' at sites not using the DynaMed interface.

Field \#107 is not editable, and it is not intended that users modify it directly. The values are

0 NO

1 YES

There are a number of entry points that may be used to query or control the monitor. To check whether or not it is running, use \$\$ISRUN

\>W \$\$ISRUN^PRCVMON

0

(This call looks at Field \#107.)

> **NOTE:** If for any reason the value of this field is incorrect, it can be set manually as follows:

\>D SETRUN^PRCVMON(0)

Manual setting should not normally be required. Keep in mind that calling this entry point inappropriately can cause problems for the FCP monitor.

To get the current status (Field \#106) use \$\$GETSTAT

\>W \$\$GETSTAT^PRCVMON

2

If the monitor is running, it can be stopped by setting the status to 2 'NOT ENABLED'. To allow it to run again, set it to 1 'ENABLED'. Note, however, that this does not start the monitor.

The status can be changed as follows:

\>D SETSTAT^PRCVMON(1)

Setting status to ENABLED

Finally, if the status is ENABLED, the monitor may be started (scheduled to run) as follows:

\>D SCHED^PRCVMON

The FCP monitor (task \# 25014) was scheduled to run at May 25, 2005@15:53:20

If it is already running, an error message will be displayed

\>D SCHED^PRCVMON

The FCP monitor is already running!

Finally, in TaskMan, the process appears as follows:

25017: RUN^PRCVMON, FCP Balance Monitor. No device. VAH,ROU.

From Today at 15:58, By you. Started running Today at 15:58.

Job \#: 540086750 \[203111DE\]

Executing this process will change the output on a FileMan Inquiry on file 414.03 for the FCP entry (entries). The output will now contain data for Fiscal Year Balances.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>STATION: 100 SUBSCRIPTION: 24</p>
<p>SUBSCRIPTION TYPE: FCP Running Balance</p>
<p>CREATED: MAY 04, 2005@11:37:27 ACTIVE: YES</p>
<p>FISCAL YEAR: 90</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 0</p>
<p>FISCAL YEAR: 91</p>
<p>ATTRIBUTE: 1 VALUE: -8310</p>
<p>ATTRIBUTE: 2 VALUE: -1300</p>
<p>ATTRIBUTE: 3 VALUE: -6000</p>
<p>ATTRIBUTE: 4 VALUE: -5430</p>
<p>FISCAL YEAR: 92</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 0</p>
<p>FISCAL YEAR: 93</p>
<p>ATTRIBUTE: 1 VALUE: -18320</p>
<p>ATTRIBUTE: 2 VALUE: -684</p>
<p>ATTRIBUTE: 3 VALUE: -1310</p>
<p>ATTRIBUTE: 4 VALUE: -45910.05</p>
<p>FISCAL YEAR: 94</p>
<p>ATTRIBUTE: 1 VALUE: -41917.84</p>
<p>ATTRIBUTE: 2 VALUE: -22320.46</p>
<p>ATTRIBUTE: 3 VALUE: -34274.39</p>
<p>ATTRIBUTE: 4 VALUE: -34503.19</p>
<p>FISCAL YEAR: 95</p>
<p>ATTRIBUTE: 1 VALUE: -38082.46</p>
<p>ATTRIBUTE: 2 VALUE: -33985.52</p>
<p>ATTRIBUTE: 3 VALUE: -34994.36</p>
<p>ATTRIBUTE: 4 VALUE: -35687.96</p>
<p>FISCAL YEAR: 96</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: -979.2</p>
<p>ATTRIBUTE: 3 VALUE: -134</p>
<p>ATTRIBUTE: 4 VALUE: 21.48</p>
<p>FISCAL YEAR: 97</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: -1037.1</p>
<p>FISCAL YEAR: 98</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: -2704</p>
<p>FISCAL YEAR: 99</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 0</p>
<p>FISCAL YEAR: 00</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 0</p>
<p>FISCAL YEAR: 01</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 0</p>
<p>FISCAL YEAR: 02</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 3</p>
<p>FISCAL YEAR: 03</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 2347.87</p>
<p>FISCAL YEAR: 04</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 81500</p>
<p>FISCAL YEAR: 05</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: -20714.69</p>
<p>ATTRIBUTE: 4 VALUE: 0</p>
<p>FISCAL YEAR: 06</p>
<p>ATTRIBUTE: 1 VALUE: 0</p>
<p>ATTRIBUTE: 2 VALUE: 0</p>
<p>ATTRIBUTE: 3 VALUE: 0</p>
<p>ATTRIBUTE: 4 VALUE: 0</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Stopping the Monitor

The monitor can be shutdown by entering D SETSTAT^PRCVMON(2). It may take a while to stop.

#### Set Up Subscriptions

Inventory Managers must subscribe to the IFCAP control point associated with their Inventory Point. See the DynaMed manual for instructions.

On the DynaMed system, set up a subscription for each stockroom/Fund Control Point of interest. The subscription will be transmitted to IFCAP and set up in file \#414.03 COTS INVENTORY SUBSCRIPTION CONTROL.

After the first subscription request is completed, use FileMan Inquiry to look in file 414.03 for the control point subscribed to:

STATION: 100 SUBSCRIPTION: 24

SUBSCRIPTION TYPE: FCP Running Balance

CREATED: MAY 04, 2005@11:37:27 ACTIVE: YES

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/065.png)</td>
<td><p><em>Technical Note:</em> You should be aware that if you re-install in a system with a running monitor, you'll get an error like this:</p>
<p>1 error logged on 6/6/2005</p>
<p>1) &lt;EDITED&gt;^PRCVMON 13:29:27 XXXX8,TOU 547164951 NLA0::547</p>
<p>The error is harmless (you only need restart the monitor), but if you want to avoid an error, do the following:</p>
<p>1. Check to see if the monitor is running (W $$ISRUN^PRCVMON will work).</p>
<p>2. If it is, set the status to NOT ENABLED as follows:</p>
<p>XXXX8&gt;D SETSTAT^PRCVMON(2)</p>
<p>Setting status to NOT ENABLED</p>
<p>XXXX8&gt;</p>
<p>3. Wait for the monitor to stop (it may take a couple of minutes). To verify that it has stopped, simply do the following:</p>
<p>XXXX8&gt;W $$ISRUN^PRCVMON</p>
<p>0</p>
<p>4. When you get a return value of 0, it has stopped and you may proceed with the install.</p>
<p>5. To start it again, first set the status back to enabled</p>
<p>XXXX8&gt;D SETSTAT^PRCVMON(1)</p>
<p>Setting status to ENABLED</p>
<p>XXXX8&gt;</p>
<p>and then schedule (start) the monitor:</p>
<p>XXXX8&gt;D SCHED^PRCVMON</p>
<p>The FCP monitor (task # 32939) was scheduled to run at Jun 06, 2005@15:21:55</p>
<p>XXXX8&gt;</p>
<p>6. In the case of an &lt;EDITED&gt; error, it won't be possible to execute the error trap. Therefore, if this error occurs, it will also be necessary to reset the run state to 0 with</p>
<p>D SETRUN^PRCVMON(0)</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/066.png)</td>
</tr>
</tbody>
</table>

### Other Ways to Check Connectivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The easiest way to test connectivity after subscriptions are set up or to test may be to edit an item or vendor and then restore that record to its original value. (This step requires temporarily removing the Out of Order flag from the Edit Item or Edit Vendor menu).

#### Schedule Options

Schedule the following options to run every three hours via Schedule/Unschedule Options \[XUTM SCHEDULE\]:

PRCV ITEM UPDATE TO DYNAMED

PRCV VENDOR UPDATE TO DYNAMED

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 84%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/067.png)</td>
<td><p><em>Technical Note:</em></p>
<p>This step should only be done after the Checksum File has been initiated (see step #5, section <a href="#populate-and-initialize-record-checksum-file">4-8</a>.</p></td>
<td>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/068.png)</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: PRCV ITEM UPDATE TO DYNAMED</p>
<p>Menu Text: Nightly ITEM master file update TASK ID: 15231</p>
<p>__________________________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: APR 19,2005@01:00</p>
<p>DEVICE FOR QUEUED JOB OUTPUT:</p>
<p>UEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 1D</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING: Persistent</p>
<p>_______________________________________________________________________________</p>
<p>Exit Save Next Page Refresh</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

These options should be scheduled to run periodically (at this writing, they run every 3 hours). We recommend running the vendor update 1 ½ hours before the DynaMed Daily Cycle is run and the Item Update 1 hours before the daily cycle.

You also need to schedule FCP MONITOR – See section 4.2.8.1.

## Maintenance and Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The Audit File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assist in following messages transmitted between IFCAP and DynaMed concerning progress on DynaMed’s requests to IFCAP for replenishment of supplies, a new IFCAP file has been created to help link the DynaMed Document ID with the appropriate documents in IFCAP. This file is the DYNAMED IFCAP INTERFACE AUDIT FILE (#414.02). The file is first set up when IFCAP is able to create a RIL from a DynaMed request message.

The Audit File is updated when:

- A DynaMed requisition is received
- A 2237 is built, approved or cancelled
- An item is deleted from a 2237 or Purchase Order
- A Purchase Card order is created from a DynaMed-generated RIL
- A Purchase Card Order is deleted
- A Receiving Report is deleted

|                                                   |                                                                                                                                                                                                                                      |                                                   |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/069.png) | *Technical Note:* The DYNAMED IFCAP INTERFACE AUDIT FILE is File \#414.02 and is subscripted by the DM DOC ID. It has a 'C' cross reference for external RIL number, and a ‘D’ cross reference for external 2237 transaction number. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/070.png) |

The RIL# and 2237# should always accurately reflect where the DM DOC ID resides or resided. If a PC was created, that PO# should be in the audit file.

The deleted fields (Date/Time Removed and Who Deleted) should be populated whenever the RIL is deleted, a 2237 or PC order is cancelled or an item is deleted from the 2237 or PO).

To view the audit file, use a DM DOC ID:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION: INQUIRE TO FILE ENTRIES</p>
<p>OUTPUT FROM WHAT FILE: DYNAMED IFCAP INTERFACE AUDIT//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select DYNAMED IFCAP INTERFACE AUDIT DM DOC ID: 5074-1004-222</p>
<p>ANOTHER ONE:</p>
<p>STANDARD CAPTIONED OUTPUT? Yes// (Yes)</p>
<p>Include COMPUTED fields: (N/Y/R/B): NO// Y Computed Fields</p></td>
</tr>
<tr class="even">
<td><p>DM DOC ID: 5074-1004-222 ITEM: 106750</p>
<p>VENDOR: RANDOMVENDOR ENTERED BY: REDACTED</p>
<p>RIL#: 100-05-2-076-828100-3764</p>
<p>DATE/TIME CREATED IN IFCAP: MAR 29, 2005@06:13:20</p>
<p>DATE/TIME CREATED IN DYNAMED: MAR 29, 2005@06:16:30</p>
<p>2237#: 100-05-2-076-0689</p>
<p>DATE/TIME REMOVED FROM IFCAP: MAR 29, 2005@10:12:09</p>
<p>WHO DELETED: REDACTED DATE NEEDED BY: APR 02, 2005</p></td>
</tr>
</tbody>
</table>

### MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whenever errors are communicated to IFCAP concerning the DynaMed-IFCAP Interface or if IFCAP identifies problems, a MailMan message will be sent to the designated Fund Control Point staff. See for sample messages.

## De-activating the Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Should the DynaMed-IFCAP Interface need to be deactivated for any reason, it is recommended that a complete analysis be done to ensure that the transition process considers all factors necessary to guarantee smooth operations and uninterrupted patient care.

### Issues to Consider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Among the issues to consider are:

1\. What processing is underway in IFCAP that DynaMed needs to be updated about? How will this update occur?

2\. What processing is underway in DynaMed that IFCAP or FMS needs to know about? How will this be done?

3\. What reports need to be generated on each system in order to identify the current status of each system? What reports should be generated to keep the systems in synch?

4\. What method will be used to handle inventory and purchasing after the interface is disabled?

### Terminating Interface: Setting PRCV COTS INVENTORY Switch to Zero

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At a minimum, the site may want to set the PRCV COTS INVENTORY switch to ‘0’ (“None”). Setting this switch to ‘0’ produces the following results:

- RIL, 2237, Purchase Order and Receipt data will no longer be communicated to DynaMed.
- The Audit File will no longer be updated with information about the processing of DynaMed requested items
- The Accountable Officer *will be* prompted to answer the question ‘Process Issue Books?’
- The 2237 Issue Book Form *will be* available to the Control Point staff
- Subscriptions, Fund Balances, Item/Vendor Updates will no longer update DynaMed
- Issue Book Activity can again be done in IFCAP

#### Other Considerations

There are no other considerations at this time.

#### Clean Up Files

- 414.02 Audit File
- 414.03 Subscription
- 414.04 Record Checksum

|                                                   |                                                                                                                                              |                                                   |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/071.png) | *Technical Note:* It may also be necessary to clean fields or cross references associated with files 410.3, 410, 442, or 411. See Chapter 5. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/072.png) |

# Technical Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IFCAP routines are affected by implementation of the DynaMed-IFCAP Interface. All are stated under the assumption that DynaMed is active at the site. For example, if a routine is shown below as having been modified to “Do not call EN^PRCHG1,” this is true only if DynaMed is active at the site.

Table 5‑1. Routines Affected

| Routine Name | Action      | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRC5181P     | Modified    | \[Details to be provided later.\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PRCFAC3      | Modified    | Send Vendor Update information to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PRCFFM2M     | Modified    | Add a line to call routine PRCVPOU which will pass the PO amendment information to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRCFFMOM     | Modified    | Add a line to call routine PRCVPOU which will pass the PO amendment information to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRCH442      | Modified    | Set PRCVDYN flag if RIL was created through DynaMed interface; enable use of DynaMed Document ID and Date Needed By in IFCAP; automatically delete RIL when finished; send MailMan message if problems encountered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PRCH442A     | Modified    | When DynaMed RIL is being processed, warn user of RIL deletion if no PO number entered; force Requested Receipt? response to YES.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PRCHAM       | Modified    | Transmit RR Adjustment info to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PRCHE        | Modified    | Send Vendor Update information to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PRCHEA       | Modified    | Alert DynaMed of cancelled PO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PRCHEA1      | Modified    | Send Vendor Update information to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PRCHG        | Modified    | Do not call EN^PRCHG1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PRCHNPO4     | Modified    | Send the signed PO to DynaMed if the site is using DynaMed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PRCHREC      | Modified    | While processing the signed receiving report, alert DynaMed of the activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRCHREC2     | Modified    | While processing the signed receiving report, alert DynaMed of the activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRCHSP1      | Modified    | Add DynaMed Document ID (DM Doc ID) to values being copied from 2237 to PO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRCORV1      | Modified    | Send Vendor Update information to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PRCOVUP      | Modified    | Send Vendor Update information to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PRCPSFIV     | Modified    | Entry Point for building IV for DynaMed inventory transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PRCPSFSV     | Modified    | Entry Point for building SV for DynaMed inventory transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PRCSAPP2     | Modified    | If DynaMed transaction is being approved, and it is being sent to Fiscal, then agreed-upon data is also passed to DynaMed; all line item data to be passed to DynaMed on a DynaMed-related transaction is recorded in File 410 at this point for an approved 2237.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PRCSCK       | Modified    | If Item Multiple node 4 exists, then display Date Needed By for DynaMed transactions only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PRCSCPY      | Modified    | Remove Issue Books as a valid selection from the selection list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PRCSD121     | Modified    | When printing a 2237 to the screen, display new fields DM Doc ID and Date Needed By from DynaMed for each line item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PRCSEA       | Modified    | Update Audit file and send message to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PRCSEB       | Modified    | Remove Issue Books as a valid selection from the selection list (in TYPE+1, set DIC(“S”)=”I Y\>1 & (Y\<5)”).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRCSEB0      | Modified    | Remove Issue Books as a valid selection from the selection list (in EDTD5+5, set DIC(“S”)=”I Y\>1 & (Y\<5)” ).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PRCSECP      | Modified    | Remove Issue Books as a valid selection from the selection list (in TYPE+2, set DIC(“S”)=”I Y\>(.5) & (Y\<5)” ).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PRCSP121     | Modified    | Edit PRCARD to add DynaMed Document ID (DM Doc ID) (410.02, 17) and Date Needed By (410.02, 18) fields to print out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PRCSRIE1     | Modified    | Update Audit File and send message to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PRCSRIG1     | Modified    | Do not allow DynaMed transaction (RIL) to be re-used. Code modified to skip over the prompt; user will not be prompted for the “re-use” question.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PRCSRIG2     | Modified    | Added code in ITEMG1 to capture data from two new fields in files 410 and 410.3: DM Doc ID (410 \#17, 410.3 \#6) and Date Needed (410 \#18, 410.3 \#7). Added variables PRCSDN, PRCSDTN in ITEMG.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PRCSRIP      | Modified    | Added code to display DM DOC ID and Date Needed By fields for RILs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PRCV442A     | Added (New) | Used to compile an array of data and send it to the messaging routine ^PRCVPOSD. Output includes: Purchase Order IEN for which the DynaMed transaction will be built; DM Doc ID; date/time item was deleted or order cancelled; DUZ of user doing deletion or cancellation; item information; date/time deleted receiving report was first created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PRCV442B     | Added (New) | Takes input from one of several routines and passes the EIN of the purchase order to the message routine so it can pull data from ^TMP. Data is basically same as shown above for PRCV442A.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PRCVBLD      | Added (New) | Builds HL7 messages using templates from File 414.01.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PRCVEE1      | Added (New) | Passes Inventory Messages from IFCAP to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PRCVEE5      | Added (New) | Receives an HL7 ACK (acknowledgment) message from DynaMed and processes it to IFCAP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PRCVFMS1     | Added (New) | Generate IV from DynaMed information passed to IFCAP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PRCVFMS2     | Added (New) | \[Details to be provided later.\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PRCVIBF      | Added (New) | Called by PRCVIB1 when DynaMed transfers Issue Book Fund information to IFCAP. This routine performs Issue Book Fund Commitment and Posting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRCVIBH      | Added (New) | Receives and parses Issue Book Fund Transfer Messages from DynaMed. Generates and Sends acknowledgement back to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PRCVIMF      | Added (New) | Called by IFCAP routines which update ITEM record from time to time. May also be a daily batch run for any updates in the ITEM Master File.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRCVINIT     | Added (New) | Outputs written messages to end users based on successful execution of the routines called.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRCVIT       | Added (New) | \[Details to be provided later.\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PRCVITMU     | Added (New) | This routine provides a number of utilities for determining whether a given site is using DynaMed and for managing item numbers of DynaMed sites. In each case, an extrinsic is called from a specified entry point in the routine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PRCVLIC      | Added (New) | Creates update message when a 2237 line item is cancelled (deleted).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PRCVMON      | Added (New) | This utility runs as a background process. For each subscribed fund (in File \#414.03), it periodically fetches all uncommitted balances for the Control Point from File \#420. It then compares those values with balances stored in File \#414.03, updating those balances at the same time. If any change in an uncommitted balance is detected, the new balances will be published to DynaMed. The entry point RUN^PRCVMON will be associated with a scheduled option (name TBD) that will run periodically (we anticipate recommending once every 15 minutes). Preliminary testing indicates that the overhead will be 0.1-0.5 CPU seconds per Control Point monitored, and that set should be small (perhaps 10-20). At this point, only minimal effort has been made to optimize this utility, but its running time could probably be improved considerably. |
| PRCVNDR      | Added (New) | Designed to create and send Vendor File update HL7 messages when transmission is needed, either immediately after the file update or once a day.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PRCVPOSD     | Added (New) | This routine uses data passed via the input array (PRCVINP) to construct a properly formatted HL7 message of the ORM^O01 event type which will be passed to the VistA HL7 package through a call to INIT^HLFNC2. Some FileMan calls and manipulation of format is necessary to prepare the data properly for the agreed-upon messaging specifications. Response messages of the ORR^O02 event type will also be routed through the VistA HL7 package to this routine and parsed for processing accordingly.                                                                                                                                                                                                                                                                                                                                                         |
| PRCVPOU      | Added (New) | Called from Purchase Order Amendment process to transfer the information in the form of HL7 message through routine PRCVPOSD to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PRCVRC1      | Added (New) | This routine silently builds a RIL in the Repetitive Item List File (File \#410.3) from data passed from the DynaMed requisition. It also validates the NIF# and BOC but does not save to a file in IFCAP; sends message to DynaMed if validation fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PRCVRC2      | Added (New) | Provides validation data for use in PRCVRC1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRCVRC3      | Added (New) | Provides error codes for use in PRCVRC1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PRCVRCA      | Added (New) | This routine extracts RIL cancellation data and passes it to Routine PRCVEE1, which formats data into HL7 Message and then sends data to DynaMed. It also updates relevant info in Audit File \#414.02. A bulletin is sent if the DynaMed Document ID (DM DOC ID) is missing from an item or if record doesn't get updated properly in Audit File.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PRCVRCG      | Added (New) | Parses incoming messages from Subscription Activity on DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PRCVRE1      | Added (New) | Receives an HL7 message from DynaMed and processes it to IFCAP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PRCVREA      | Added (New) | Receives an HL7 message from DynaMed and processes it to IFCAP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PRCVRRA      | Added (New) | During Receiving Report Adjustment process, transfers the information in the form of HL7 message through routine PRCVPOSD to DynaMed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PRCVSUB      | Added (New) | This routine provides entry points for adding, looking up and deleting fund balance subscriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PRCVTAP      | Added (New) | This routine extracts 2237 APPROVED data and passes that information to routine PRCVEE1, which formats data into HL7 Message and then sends data to DynaMed. It also updates relevant information in Audit File \#414.02. A bulletin is sent if the DynaMed Document ID (DM DOC ID) is missing from an item or if record doesn't get updated properly in Audit File.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PRCVTCA      | Added (New) | This routine extracts 2237 data when a user enters through the option “Cancel a Permanent Transaction \[PRCSCT\]” and passes that information to routine PRCVEE1, which formats data into HL7 Message and then sends data to DynaMed. It also updates relevant information in Audit File \#414.02. A bulletin is sent if the DynaMed Document ID (DM DOC ID) is missing from an item or if record doesn't get updated properly in Audit File.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRCVUTSC     | Added (New) | Used to convert escape sequences to special characters and vice versa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PRCVVMF      | Added (New) | Used to build an HL7 message to pass to an external inventory system for purposes of communicating a Vendor Update in the form of an MFN^M01 HL7 version 2.4 Master File Update message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Templates Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following templates are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑2. Templates Affected

| Template Name                                             | Action      | Comments                      |
|-----------------------------------------------------------|-------------|-------------------------------|
| PRCV DYNAMED RIL'S NEED ACTION (sort and print templates) | Added (New) | FILE \#414.02. See Table 5‑8. |
| PRCV ITEM DISPLAY                                         | Added (New) | FILE \#441. See Table 5‑8.    |
| PRCV DYNAMED RIL'S NEED ACTION                            | Added (New) | FILE \#414.02. See Table 5‑8. |

## Bulletins Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IFCAP bulletins are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑3. Bulletins Affected

| Bulletin Name         | Action      | Comments                                                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------------------------------------|
| PRCV_AUDIT_FILE_ERROR | Added (New) | Sends MailMan message alerting user(s) of error(s) encountered during processing of DynaMed-generated items. |

## Data Dictionaries Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IFCAP data dictionaries are affected by implementation of the DynaMed-IFCAP Interface. Complete details are available in the System Design Document.

Table 5‑4. Data Dictionaries Affected

| Data Dictionary Name                          | Action      | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CONTROL POINT ACTIVITY (#410)                 | Modified    | New fields added                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DYNAMED IFCAP INTERFACE AUDIT (File \#414.02) | Added (New) | This file retains data that is normally deleted from IFCAP files. The data held in this file will be retained for a brief period of time (TBD) and purged after this retention period. Several new routines (such as PRCVRC1, PRCVRC2, PRCVRC3, PRCVLIC, PRCV442A, PRCVTAP) specific to DynaMed interface will be populating data in this file.                                                                                                                                                                          |
| MESSAGE TEMPLATE (#414.01)                    | Added (New) | This will be a largely static file, containing one entry per message template (i.e., for each message built using PRCVBLD together with a mapping of HL7 data fields to M globals). The number of entries should remain small unless the builder is used for other purposes. The most important field is a word-processing field (#10) that contains the message template (an XML document).                                                                                                                             |
| PRCV SUBSCRIPTION (#414.03)                   | Added (New) | Used to maintain a list of subscriptions which, for the purposes of this interface, is a list of Control Points referenced by DynaMed. Update messages will be sent to DynaMed when the uncommitted balances for one of these Control Points changes. The file will be queried whenever these balances are recalculated. New records may be added when a QSB^HL7 message (create subscription) arrives from DynaMed, and will be deleted (if present) when a QCN^HL7 message (cancel subscription) arrives from DynaMed. |
| PROCUREMENT & ACCOUNTING TRANSACTIONS (#442)  | Modified    | New fields added, edited existing field, added cross-reference.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RECORD CHECKSUM FILE (#414.04)                | Added (New) | Use to store checksums associated with objects such as file records. The reason for this level of generality is that it is at times convenient to associate a checksum with a subset of fields in a file (or possibly other objects). This means it may be necessary to support more than one checksum on the same file or other type of object class.                                                                                                                                                                   |
| REPETITIVE ITEM LIST (#410.3)                 | Modified    | New fields added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Field Definitions Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IFCAP field definitions are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑5. Field Definitions Affected

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 13%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Definition Name</th>
<th>Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DATE NEEDED BY (Subfile #410.02)</td>
<td>Added (New)</td>
<td><p>File: Control Point Activity #410</p>
<p>Subfile: Item #410.02</p>
<p>This field holds a date when DynaMed anticipates an item should arrive. It is received in a Repetitive Item List (RIL) transaction for each item and then it is REDACTEDied on to 2237 and then to Purchase Order as the item is processed through IFCAP.</p></td>
</tr>
<tr class="even">
<td>DATE NEEDED BY (Subfile #410.31)</td>
<td>Added (New)</td>
<td><p>File: Repetitive Item List #410.3</p>
<p>Subfile: Item #410.31</p>
<p>This date is entered on the DynaMed system at the time the item is being requested. This Date is received in a transaction from DynaMed. It resides first in the RIL, it is pushed to the 2237, and then to the Purchase Order as the item is processed through IFCAP.</p></td>
</tr>
<tr class="odd">
<td>DATE/TIME IN DynaMed (File #410.3)</td>
<td>Added (New)</td>
<td><p>File: Repetitive Item List #410.3</p>
<p>This date and time signifies when a Requisition was generated in DynaMed. This date is passed by DynaMed and it is used to determine Fiscal Year and Quarter for the transaction in IFCAP. This is the time stamp when a requisition was created in DynaMed. This date determines the Fiscal Year and Quarter for the transaction.</p></td>
</tr>
<tr class="even">
<td>DM DOC ID (Subfile 410.31)</td>
<td>Added (New)</td>
<td><p>File: Repetitive Item List #410.3</p>
<p>Subfile: Item #410.31</p>
<p>This is DynaMed's unique number (Document ID) associated with each item that is sent on a request order from DynaMed. It is composed of 1 digit for Year concatenated with 3 digit Julian Date a dash, concatenated with 4 digit Sequential Number and a dash, concatenated up to 6 characters (ex YDDD-9999-CCCCCC).</p>
<p>This number is provided by DynaMed; no user input is required. DynaMed allows 16 characters maximum.</p></td>
</tr>
<tr class="odd">
<td>DM DOC ID (Subfile #410.02)</td>
<td>Added (New)</td>
<td><p>File: Repetitive Item List #410</p>
<p>Subfile: Item #410.02</p>
<p>This is DynaMed's unique number (Document ID) associated with each item that is sent on a request order from DynaMed. It is composed of 1 digit for Year concatenated with 3 digit Julian Date a dash, concatenated with 4 digit Sequential Number and a dash, concatenated up to 6 characters (ex YDDD-9999-CCCCCC).</p>
<p>This number is provided by DynaMed; no user input is required. DynaMed allows 16 characters maximum.</p></td>
</tr>
<tr class="even">
<td>DM DOC ID (File #442.01)</td>
<td>Added (new)</td>
<td><p>This is DynaMed's unique number (Document ID) associated with each item that is sent on a request order from DynaMed. It is composed of 1 digit for Year concatenated with 3 digit Julian Date a dash, concatenated with 4 digit Sequential Number and a dash, concatenated up to 6 characters (ex YDDD-9999-CCCCCC).</p>
<p>This number is provided by DynaMed; no user input is required. DynaMed allows 16 characters maximum.</p></td>
</tr>
<tr class="odd">
<td>ISSUE BOOK BATCH ID (File# 410)</td>
<td>Added (New)</td>
<td>This is the Batch ID of the Issue Book sent from DynaMed to uniquely identify the Issue Book. Answer must be 1-25 characters in length.</td>
</tr>
<tr class="even">
<td>LINE ITEM NUMBER (File #410.02)</td>
<td>Added (New)</td>
<td>Added new-style MUMPS cross reference to field that runs when a line item entry in the 2237 is deleted. Set Logic is simply QUIT. Kill Logic is D EN^PRCVLIC. The following fields are extracted for the logic: Line Item Number (#.01), Quantity (#2), Unit of Purchase (#3), BOC (#4), Item Master File No (#5), Stock Number (#6), Est. Item Unit Cost (#7), DM Doc ID (#17), Date Needed By (#18).</td>
</tr>
<tr class="odd">
<td>(File #411)</td>
<td></td>
<td><p>Added two new fields:</p>
<p>FCP MONITOR STATUS (#106) / set of codes: 0 'NOT USED',1 'ENABLED',2 'NOT ENABLED'</p>
<p>FCP MONITOR RUNNING? (#107) / set of codes: 0 'NO', 1 'YES'</p></td>
</tr>
<tr class="even">
<td>LINE ITEM NUMBER (File #442 - Subfile #442.01)</td>
<td>Modified</td>
<td>Added an “AK” new-style cross reference. Also modified Kill logic to .01 field to invoke PRCV442B to build a message to DynaMed when an item is deleted from a purchase order</td>
</tr>
</tbody>
</table>

## Data Entries Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Unique Records Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IFCAP unique records are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑6. Unique Records Affected

| Unique Record Name                                                                   | Action      | Comments                  |
|--------------------------------------------------------------------------------------|-------------|---------------------------|
| DYNAMED SYSTEM FLAG (PRCV COTS INVENTORY) (File 8989.51, Parameter Tools Definition) | Added (New) | Value: 0: None;1: DynaMed |

## Mail Groups Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following mail groups are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑7. Mail Groups Affected

| Mail Group Name        | Action      | Comments            |
|------------------------|-------------|---------------------|
| PRCV Item Vendor Edits | Added (New) | See section 4.2.3.1 |
| PRCV Audit File Alerts | Added (New) | See section 4.2.3.2 |

## Options Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑8. Options Affected

| Option Name                    | Action      | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRCV DYNAMED RIL'S NEED ACTION | Added (New) | These two options are reports that will not be needed unless the Interface is functioning. For this reason, the IRM will need to assign these options to existing menus when the interface is activated. The RIL's NEED ACTION report lists all DM RILs not yet used to generate 2237s or PC orders. The ITEM DISPLAY lists information associated with an item specified by the user. This display includes the internal vendor number in addition to the vendor's name for every vendor associated with the item. |
| PRCV ITEM DISPLAY WITH VENDOR# |             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PRCV ITEM UPDATE TO DYNAMED    | Added (New) | These two options are scheduled if the Interface is activated (Item Update, Vendor Update). They work in the background comparing the checksum file to the calculated checksum for a vendor or item record. If a discrepancy is found, that record is sent to DynaMed and the checksum file is updated with the new checksum for the record sent.                                                                                                                                                                   |
| PRCV VENDOR UPDATE TO DYNAMED  |             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Protocols Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IFCAP HL7 protocols are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑9. Protocols Affected

| Protocol Name                                                    | Action      | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRCV 410 2237 LINE ITEM CANCEL {PRCV Cancel Line Item From 2237} | Added (New) | Protocol PRCV 442 ITEM DELETE is one of two (PRCV 410 2237 LINE ITEM CANCEL is the other) that do not conform to the naming convention used in this project for HL7 protocols, as they are not HL7 protocols. These two protocols are neither event protocols nor subscriber protocols, and they do not relate directly to the interface. They exist only to assist with collecting information when item deletion occurs and their activation is triggered from a kill command in the data dictionary. |
| PRCV 442 ITEM DELETE                                             |             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRCV_DYNAMED_01_EV_REQUISITION_SEND                              | Added (New) | The event driver HL7 Protocol used to receive Requisition Messages from DynaMed into IFCAP                                                                                                                                                                                                                                                                                                                                                                                                              |
| PRCV_DYNAMED_01_SU_REQUISITION_SEND                              | Added (New) | Other HL7 subscription protocol for Requisition Send Messages                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PRCV_DYNAMED_05_EV_ITEM_UPDATE                                   | Added (New) | This event subscriber HL7 Protocol is used to (1) Receive DFT^P03 messages from the DynaMed inventory system; (2) Transfer ACK^P03 messages to the DynaMed inventory system.                                                                                                                                                                                                                                                                                                                            |
| PRCV_DYNAMED_05_SU_ITEM_UPDATE                                   | Added (New) | Other HL7 Subscription Protocol                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRCV_DYNAMED_20_EV_FUND_BAL_SUBSCRIBE                            | Added (New) | Other HL7 Event Protocol for subscriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PRCV_DYNAMED_20_SU_FUND_BAL_SUBSCRIBE                            | Added (New) | Other HL7 Subscription Protocol for subscriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRCV_DYNAMED_21_EV_FUND_BAL_CANCEL_SUB                           | Added (New) | Other HL7 Event Protocol for Cancellation of Subscriptions                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PRCV_DYNAMED_21_SU_FUND_BAL_CANCEL_SUB                           | Added (New) | Other HL7 subscription protocol for cancellation of subscriptions                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRCV_DYNAMED_22_EV_FUND_BAL_DATA                                 | Added (New) | Other HL7 Event Protocol for Funds Balance                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PRCV_DYNAMED_22_SU_FUND_BAL_DATA                                 | Added (New) | Other HL7 subscription protocol for Funds Balance                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRCV_DYNAMED_IV_SV_RECEIVE                                       | Added (New) | Event subscriber HL7 Protocol used to receive ORM^O01 messages from the DynaMed inventory system.                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRCV_DYNAMED_IV_SV_SEND                                          | Added (New) | Event driver HL7 Protocol used to send ORR^O02 messages to the DynaMed inventory system.                                                                                                                                                                                                                                                                                                                                                                                                                |
| PRCV_IFCAP_01_EV_DYNAMED_UPDATE                                  | Added (New) | Other HL7 Event Protocol                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PRCV_IFCAP_02_EV_DYNAMED_UPDATE                                  | Added (New) | Update DynaMed for changes to 2237, approval of 2237, or cancellation of RIL/2237                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRCV_IFCAP_02_EV_OBL/AMEND                                       | Added (New) | Event driver HL7 Protocol used to send ORM^O01 messages to the inventory system.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRCV_IFCAP_02_SU_DYNAMED_UPDATE                                  | Added (New) | Other HL7 subscription protocol for RIL/2237 cancel/edit/approval                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRCV_IFCAP_02_SU_OBL/AMEND                                       | Added (New) | Event subscriber HL7 Protocol used to receive ORR^O02 messages from the inventory system.                                                                                                                                                                                                                                                                                                                                                                                                               |
| PRCV_IFCAP_03_EV_REC/ADJ                                         | Added (New) | Event driver HL7 Protocol used to send ORM^O01 messages to the inventory system.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRCV_IFCAP_03_SU_REC/ADJ                                         | Added (New) | Event subscriber HL7 Protocol used to receive ORR^O02 messages from the inventory system.                                                                                                                                                                                                                                                                                                                                                                                                               |
| PRCV_IFCAP_04_EV_VEND_UPD                                        | Added (New) | Event driver HL7 Protocol used to send MFK^M01 messages to the inventory system.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRCV_IFCAP_04_SU_VEND_UPD                                        | Added (New) | Event subscriber HL7 Protocol used to receive MFK^M01 messages from the inventory system.                                                                                                                                                                                                                                                                                                                                                                                                               |
| PRCV_IFCAP_05_EV_ITEM_UPD                                        | Added (New) | Event driver HL7 Protocol used to send MFK^M01 item update messages to the inventory system.                                                                                                                                                                                                                                                                                                                                                                                                            |
| PRCV_IFCAP_05_SU_ITEM_UPD                                        | Added (New) | Event subscriber HL7 Protocol used to receive MFK^M01 item update response messages from the inventory system.                                                                                                                                                                                                                                                                                                                                                                                          |

## HL7 Application Parameters Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IFCAP HL7 application parameters are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑10. HL7 Application Parameters Affected

| HL7 Application Parameter Name | Action      | Comments                                                                                                  |
|--------------------------------|-------------|-----------------------------------------------------------------------------------------------------------|
| PRCV_DYNAMED                   | Added (New) | Site value populated based on instructions included with install (for example, set to 100DY for REDACTED) |
| PRCV_IFCAP_2237                | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_FBAL                | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_FCAN                | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_FSUB                | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_IT                  | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_IVSV                | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_PO                  | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_RECV                | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_REQ                 | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |
| PRCV_IFCAP_VEN                 | Added (New) | Site ^ Domain ^DNS - Will be built from HL7 site parameters                                               |

## HL7 Logical Links Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IFCAP HL7 logical links are affected by implementation of the DynaMed-IFCAP Interface.

Table 5‑11. HL7 Logical Links Affected

| HL7 Application Logical Link Name | Action      | Comments                          |
|-----------------------------------|-------------|-----------------------------------|
| PRCVDYNA                          | Added (New) | \[Details to be provided later.\] |

## HL7 Messages and Interface Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Appendix B.

## Data Map Record Formats Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One-time updates of the item- and vendor-related DynaMed data tables were made, using output from the corresponding IFCAP files (ITEM MASTER, \#441 and VENDOR MASTER, \#440). Only currently active vendors and currently active contracts were exported. Vendors were selected on the basis of being associated as sources for active items with Item Master file numbers 100000 or higher. The following record formats were required.

Table 5‑12. Data Map Record Formats Affected

| Data Map Record Format Name | Action      | Comments                          |
|-----------------------------|-------------|-----------------------------------|
| VENDOR EXPORT RECORD        | Added (New) | For Vendor Extract.               |
| CONTRACT RECORD             | Added (New) | \[Details to be provided later.\] |
| ITEM SOURCING RECORD        | Added (New) | \[Details to be provided later.\] |
| MANDATORY SOURCE RECORD     | Added (New) | For Item Extract.                 |
| PREFERRED VENDOR RECORD     | Added (New) | For Item Extract.                 |

## File/Global Size Changes Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Mail Groups Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 4.2.3.

## Security Keys Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Options Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 4.2.6.

## Remote Procedure Call (RPC) Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Constants Defined in Interface Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Variables Defined in Interface Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Types Defined in Interface Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Graphic User Interface (GUI) Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## GUI Classes Defined Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Current Form Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Modified Form Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Components on Form Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Events Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Methods Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Special References Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Class Events Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Class Methods Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Class Properties Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Uses Clause Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Form Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Function Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Dialog Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Help Frame Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

Figure 5‑1. DynaMed-IFCAP Sequence

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/073.png) |
|-----------------------------------------------------------------------------------------------------|

See Appendix E for detailed process flow charts.

####### About DynaMed

\[*Adapted from* <http://www.info-control.com/material_mngmt/faq.htm>\]

DynaMed is an automated inventory management, order requisition and distribution system for healthcare providers. The standard DynaMed software has been modified for use in the Federal government and, more specifically, in the REDACTED VAMC environment.

DynaMed user documentation will be provided separately. *See* REDACTED

In the modified, “standalone” version being used at REDACTED, DynaMed offers the following features.

######## General System Features

- Supports diverse types of warehouses and stockrooms including warehouse distribution centers and stockrooms, including central supply, pharmacies, supply processing and distribution (SPD), operating rooms, laboratories, and linen exchange
- Replenishment orders are processed based on item counts and min/max levels
- Supports stock and non-stock (fringe) items
- Allows unit of purchase, unit of measure, unit of issue and conversion factors to be defined for each stock item in each stockroom
- Calculates appropriate reorder points and requisition objectives for each stockroom item based on historical usage levels and delivery times for stock and cart items monthly
- Maintains single item number for an item, regardless of vendor or unit of measure ordered
- Users are assigned to user groups, restricting access to specific menus and screens for improved security and ease of use.

######## Functional Capabilities

- Maintain Warehouse, Stockroom and Stock item Transactions
- Maintain Cart and Cart Item Transactions
  - PAR
  - Exchange
  - Case
- Process Customer Orders and Stockroom Requisitions
- Process Receipt of Stock items
- Process Stockroom Inventories
- Process Cart Inventories
- Process Inventory Adjustments, Returns, and Corrections
- Display and Cancel Customer Orders and Stockroom Requisitions
- Generate Standard Reports

######## Capability Details

######### Maintain Stockroom and Stock item Transactions

- DynaMed maintains stock item information by stockroom. This information is used by the system to control inventory levels and to trigger requisitions. Stock item information includes the following:
  - UPN and/or hospital-specific unique stock item number and name
  - Stock item security code
  - Unit of Purchase, unit of measure, unit of issue and UI/UM conversion factors
  - Location or locations of the stock item within stockroom
  - Computer generated random storage locations
  - Unit of issue price
  - Quantity on hand (system maintained)
  - Reorder and requisition objective points for the stock item
  - Stock item due-in and due-out quantities (system calculated based on user orders and stockroom requisitions)
  - Vendor or supplier of item, and average order ship time
  - Patient chargeable item flag, and expiration dated/lot item flags
  - Latex flag
- Supports non-issuable items with management, tracking and reporting functionality
- Supports shipping charges and average moving price for stockroom items

######### Process Customer Orders and Stockroom Requisitions

- Automatically updates stock item quantity on hand (QOH) when a customer order is processed
- DynaMed supports backorders for customers and carts independently and automatically creates the required backorder record when a stock item cannot be filled
- Assigns a unique document number to each stock item within a requisition
- Stock item requisitions are linked to the ordering stockroom
- The system automatically creates a stockroom requisition for stock items when the stock item net assets falls below the stock item's reorder point
- The stockroom manager can manually process requisitions for stock items already registered in the stockroom. The manager may also declare, register and requisition new stock items for the master item list.
- The system can record Purchase Order numbers, PO notes, Vendor names and expected receipt date for tracking purchases of stock items.

######### Process Receipt of Stock items

- Accepts full or partial receipt of stock items. Stock items may be received in either UI or UM to accommodate partial shipments
- Upon receipt, the system fills all backorders, prints out the picklist and then puts the remaining balance into inventory
- Automatically adjusts the stock item balances and changes or closes out the user backorder (if applicable) and the stockroom requisition
- Stockroom requisitions and the user backorder remain open until the order is completely filled, canceled, or closed out
- Following receipt, DynaMed automatically converts the unit of issue to the unit of measure based on the stock item's unit of issue/unit of measure conversion factor
- DynaMed displays and generates a report of all stock items backordered listing quantity due in, supplier, price, and order status
- DynaMed generates a receiving report by stockroom

######### Process Stockroom Inventories

- Automatically updates and adjusts stock item quantities based on results of inventory and makes all the appropriate accounting entries

######### Process Inventory Adjustments, Returns, and Corrections

- The adjustments may be made to the stock item quantity on hand in the event that:
  - Stock items are lost, broken, spoiled, outdated, or if additional items are discovered
  - It is discovered that one stock item was mistaken for another during receipt
  - The stock item is recalled or otherwise returned to the vendor
- DynaMed automatically notifies the user when: the adjustment does not match the current received quantity; adjustments bring the quantity on hand to zero; or all items are not available to assemble the surgical pack or instrument kit
- When a customer returns a stock item, DynaMed automatically issues a customer credit and increases the inventory quantity

######### Display and Cancel Customer Orders and Stockroom Requisitions

- DynaMed displays and permits cancellation of existing customer backorders and stockroom requisitions for a specific stock item
- Automatically decreases the quantity due in or due out based on the cancellation type
- Supports PO line item cancellation and item cancellation

####### HL7 Implementation

This appendix provides an overview of the HL7 transaction packets that are used by this interface.

######## Message Structure

This is HL7’s unit of communication. It conveys a single activity and takes the following format:

Header Segment (MSH)

Segment Name \<delimiter\> \<field\> \<delimiter\> \<field\> \<delimiter\>…

Segment Name \<delimiter\> \<field\> \<delimiter\> \<field\> \<delimiter\>…

Table B- 1. The Message Header (MSH)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 44%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>Sequence</th>
<th>Element Name</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Field Separator</td>
<td>| (the pipe character)</td>
</tr>
<tr class="even">
<td>2</td>
<td>Encoding Characters</td>
<td>^~\&amp;</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sending Application</td>
<td>PRCV_</td>
</tr>
<tr class="even">
<td>4</td>
<td>Sending Facility</td>
<td><p>Station^Domain^DNS if IFCAP</p>
<p>100DY if DynaMed</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Receiving Application</td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>Receiving Facility</td>
<td><p>Station^Domain^DNS if IFCAP</p>
<p>100DY if DynaMed</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Date/Time of Message</td>
<td>YYYYMMDDHHMMSS</td>
</tr>
<tr class="even">
<td>8</td>
<td>Security</td>
<td>&lt;not used&gt;</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Message Type</td>
<td><p>Message ^Event</p>
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
<p>(In Vista, pulled from Site Parameters unless overridden in event protocol)</p></td>
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

Table B- 2. The MSA Segment

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 44%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>Sequence</th>
<th>Element Name</th>
<th>Comments</th>
</tr>
</thead>
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

######## Message/Event Types Used

Within this interface, the following Message/Event Types are used:

Table B- 3. Messages Sent to DynaMed

| Message^Event | Application Acknowledgment | Activity                                                                                |
|---------------|----------------------------|-----------------------------------------------------------------------------------------|
| ORM^O01       | ORR^O02                    | Updates on POs including approvals, amendments, cancellations, receipts and adjustments |
| OMN^O07       | ORN^O07                    | Deletion of RILS, Updates to 2237s including approvals and cancellations                |
| MFN^M01       | MFK^M01                    | Updates of Item records, vendor records, and Fund Control Point balances                |

Table B- 4. Messages Sent to IFCAP

| Message^Event | Application Acknowledgment | Activity                                                                                    |
|---------------|----------------------------|---------------------------------------------------------------------------------------------|
| OMN^O07       | ORN^O07                    | Requistions for supply replenishment via procurement                                        |
| DFT^P03       | ACK^P03                    | Update Fund Control Points and trigger message to FMS due to Issue Book activity in DynaMed |
| QSB^Q16       | ACK^Q16                    | Create Subscription to receive balance updates for Fund Control Point                       |
| QCN^J02       | ACK^Q02                    | Cancel Subscription for receiving balance updates on a fund control point                   |

Specific information may be obtained from the HL7 Manual (VistA Health Level Seven Site Manager & Developer Manual) and through the data dictionaries.

Table B- 5. Application ACK for Response to Requisition Send Message

ORN^O08

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 20%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><p><strong>Message</strong></p>
<p><strong>Position</strong></p></th>
<th><strong>Comments or Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Field Separator</td>
<td>MSH-1</td>
<td>|</td>
</tr>
<tr class="odd">
<td>Encoding Characters</td>
<td>MSH-2</td>
<td>^~\&amp;</td>
</tr>
<tr class="even">
<td>Sending Application</td>
<td>MSH-3</td>
<td>PRCV_IFCAP_REQ</td>
</tr>
<tr class="odd">
<td>Sending Facility –name space ID</td>
<td>MSH-4.1</td>
<td>100</td>
</tr>
<tr class="even">
<td>Sending Facility – universal ID</td>
<td>MSH-4.2</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Sending Facility – Universal ID type</td>
<td>MSH-4.3</td>
<td>DNS</td>
</tr>
<tr class="even">
<td>Receiving Application</td>
<td>MSH-5</td>
<td>PRCV_DYNAMED</td>
</tr>
<tr class="odd">
<td>Receiving Facility – name space ID</td>
<td>MSH-6.1</td>
<td>100DY</td>
</tr>
<tr class="even">
<td>Receiving Facility – Universal ID</td>
<td>MSH-6.2</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Receiving Facility – Universal ID Type</td>
<td>MSH-6.3</td>
<td>DNS</td>
</tr>
<tr class="even">
<td>Date/Time of Message</td>
<td>MSH-7</td>
<td>Yyyymmddhhmmss+/-zzzz</td>
</tr>
<tr class="odd">
<td>Message Type – Message Type</td>
<td>MSH-9.1</td>
<td>ORN</td>
</tr>
<tr class="even">
<td>Message Type – Event Trigger</td>
<td>MSH-9.2</td>
<td>O08</td>
</tr>
<tr class="odd">
<td>Message Control ID</td>
<td>MSH-10</td>
<td>Populated by Vitria upon Creation</td>
</tr>
<tr class="even">
<td>Processing ID</td>
<td>MSH-11</td>
<td>P or T</td>
</tr>
<tr class="odd">
<td>Version ID</td>
<td>MSH-12</td>
<td>2.4</td>
</tr>
<tr class="even">
<td>Accept Acknowledgment Type</td>
<td>MSH-15</td>
<td>AL</td>
</tr>
<tr class="odd">
<td>Application Acknowledgment Type</td>
<td>MSH-16</td>
<td>AL</td>
</tr>
<tr class="even">
<td>Country Code</td>
<td>MSH-17</td>
<td>USA</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Acknowledgement Code</td>
<td>MSA-1</td>
<td>AA, AE, or AR</td>
</tr>
<tr class="odd">
<td>Message Control ID</td>
<td>MSA-2</td>
<td>Control ID from Original Message</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Error Location - Segment</td>
<td>ERR-2.1</td>
<td>Segment where error occurred</td>
</tr>
<tr class="even">
<td>Error Location – Segment Sequence</td>
<td>ERR-2.2</td>
<td>Line Item where error occurred</td>
</tr>
<tr class="odd">
<td>Error Location – Field Position</td>
<td>ERR-2.3</td>
<td>Field in segment where error occured</td>
</tr>
<tr class="even">
<td>HL7 Error Code – Identifier</td>
<td>ERR-3.1</td>
<td>Code from table 207 that defines error</td>
</tr>
<tr class="odd">
<td>HLO7 Error Code – text</td>
<td>ERR-3.2</td>
<td>Text of error</td>
</tr>
<tr class="even">
<td>HL7 Error Code – table</td>
<td>ERR-3.3</td>
<td>Table Name</td>
</tr>
<tr class="odd">
<td>Severity</td>
<td>ERR-4</td>
<td>E or W</td>
</tr>
<tr class="even">
<td>Application Error Code - Identifier</td>
<td>ERR-5.1</td>
<td>Code from User Table 0533</td>
</tr>
<tr class="odd">
<td>Application Error Code - Text</td>
<td>ERR-5.2</td>
<td>Text description of error</td>
</tr>
<tr class="even">
<td>Application Error Parameter</td>
<td>ERR-6</td>
<td>DynaMed Document ID</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Comment</td>
<td>NTE-3</td>
<td>Count of items, errors and non-errors</td>
</tr>
</tbody>
</table>

Table B- 6. Application ACK from RIL/2237 Cancel/Update/Approve

ORN^O08

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 20%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><p><strong>Message</strong></p>
<p><strong>Position</strong></p></th>
<th><strong>Comments or Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Field Separator</td>
<td>MSH-1</td>
<td>|</td>
</tr>
<tr class="odd">
<td>Encoding Characters</td>
<td>MSH-2</td>
<td>^~\&amp;</td>
</tr>
<tr class="even">
<td>Sending Application</td>
<td>MSH-3</td>
<td>PRCV_DYNAMED</td>
</tr>
<tr class="odd">
<td>Sending Facility – Name Space ID</td>
<td>MSH-4.1</td>
<td>100DY</td>
</tr>
<tr class="even">
<td>Sending Facility – Universal ID</td>
<td>MSH-4.2</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Sending Facility – Universal ID Type</td>
<td>MSH-4.3</td>
<td>DNS</td>
</tr>
<tr class="even">
<td>Receiving Application</td>
<td>MSH-5</td>
<td>PRCV_IFCAP_REQ</td>
</tr>
<tr class="odd">
<td>Receiving Facility Name Space ID</td>
<td>MSH-6.1</td>
<td>100</td>
</tr>
<tr class="even">
<td>Receiving Facility – Universal ID</td>
<td>MSH-6.2</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Receiving Facility – Universal ID Type</td>
<td>MSH-6.3</td>
<td>DNS</td>
</tr>
<tr class="even">
<td>Date/Time of Message</td>
<td>MSH-7</td>
<td>Yyyymmddhhmmss+/-zzzz</td>
</tr>
<tr class="odd">
<td>Message Type – Message Type</td>
<td>MSH-9.1</td>
<td>ORN</td>
</tr>
<tr class="even">
<td>Message Type – Event Trigger</td>
<td>MSH-9.2</td>
<td>O08</td>
</tr>
<tr class="odd">
<td>Message Control ID</td>
<td>MSH-10</td>
<td>Populated by Vitria upon Creation</td>
</tr>
<tr class="even">
<td>Processing ID</td>
<td>MSH-11</td>
<td>P or T</td>
</tr>
<tr class="odd">
<td>Version ID</td>
<td>MSH-12</td>
<td>2.5</td>
</tr>
<tr class="even">
<td>Accept Acknowledgment Type</td>
<td>MSH-15</td>
<td>AL</td>
</tr>
<tr class="odd">
<td>Application Acknowledgment Type</td>
<td>MSH-16</td>
<td>AL</td>
</tr>
<tr class="even">
<td>Country Code</td>
<td>MSH-17</td>
<td>USA</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Acknowledgement Code</td>
<td>MSA-1</td>
<td>AA, AE, or AR</td>
</tr>
<tr class="odd">
<td>Message Control ID</td>
<td>MSA-2</td>
<td>Control ID from Original Message</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Error Location – Segment</td>
<td>ERR-2.1</td>
<td>Segment where error occurred</td>
</tr>
<tr class="even">
<td>Error Location – Segment Sequence</td>
<td>ERR-2.2</td>
<td>Line item where error occurred</td>
</tr>
<tr class="odd">
<td>Error Location – Field Position</td>
<td>ERR-2.3</td>
<td>Field in segment where error occured</td>
</tr>
<tr class="even">
<td>HL7 Error Code - Identifier</td>
<td>ERR-3.1</td>
<td>Code from table 207 that defines error</td>
</tr>
<tr class="odd">
<td>HL7 Error Code - Text</td>
<td>ERR-3.2</td>
<td>Text of error</td>
</tr>
<tr class="even">
<td>HL7 Error Code – Name of Coding System</td>
<td>ERR-3.3</td>
<td>HL70357</td>
</tr>
<tr class="odd">
<td>Severity</td>
<td>ERR-4</td>
<td>E or W</td>
</tr>
<tr class="even">
<td>Application Error Code - Identifier</td>
<td>ERR-5.1</td>
<td>Code from User Table 0533</td>
</tr>
<tr class="odd">
<td>Application Error Code – Text</td>
<td>ERR-5.2</td>
<td>Text description</td>
</tr>
<tr class="even">
<td>Application Error Parameter</td>
<td>ERR-6</td>
<td>RIL or 2237 Number</td>
</tr>
</tbody>
</table>

Table B- 7. Message Sending Requisition for RIL Build

OMN^O07

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 20%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><p><strong>Message</strong></p>
<p><strong>Position</strong></p></th>
<th><strong>Comments or Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Field Separator</td>
<td>MSH-1</td>
<td>|</td>
</tr>
<tr class="odd">
<td>Encoding Characters</td>
<td>MSH-2</td>
<td>^~\&amp;</td>
</tr>
<tr class="even">
<td>Sending Application</td>
<td>MSH-3</td>
<td>PRCV_DYNAMED</td>
</tr>
<tr class="odd">
<td>Sending Facility</td>
<td>MSH-4</td>
<td>100DY</td>
</tr>
<tr class="even">
<td>Receiving Application</td>
<td>MSH-5</td>
<td>PRCV_IFCAP_REQ</td>
</tr>
<tr class="odd">
<td>Receiving Facility – Namespace ID</td>
<td>MSH-6.1</td>
<td>Station#</td>
</tr>
<tr class="even">
<td>Receiving Facility – universal ID</td>
<td>MSH-6.2</td>
<td>Domian</td>
</tr>
<tr class="odd">
<td>Receiving Facility – Universal ID Type</td>
<td>MSH-6-3</td>
<td>DNS</td>
</tr>
<tr class="even">
<td>Date/Time of Message</td>
<td>MSH-7</td>
<td>Yyyymmddhhmmss+/-zzzz</td>
</tr>
<tr class="odd">
<td>Message Type – message type</td>
<td>MSH-9.1</td>
<td>OMN</td>
</tr>
<tr class="even">
<td>Message Type – event trigger</td>
<td>MSH-9.2</td>
<td>O07</td>
</tr>
<tr class="odd">
<td>Message Control ID</td>
<td>MSH-10</td>
<td>Populated by Vitria upon Creation</td>
</tr>
<tr class="even">
<td>Processing ID</td>
<td>MSH-11</td>
<td>P or T</td>
</tr>
<tr class="odd">
<td>Version ID</td>
<td>MSH-12</td>
<td>2.4</td>
</tr>
<tr class="even">
<td>Accept Acknowledgment Type</td>
<td>MSH-15</td>
<td>AL</td>
</tr>
<tr class="odd">
<td>Application Acknowledgment Type</td>
<td>MSH-16</td>
<td>AL</td>
</tr>
<tr class="even">
<td>Country Code</td>
<td>MSH-17</td>
<td>USA</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Order Control</td>
<td>ORC-1</td>
<td>DYN000555</td>
</tr>
<tr class="odd">
<td>Fund Control Point</td>
<td>ORC-3</td>
<td>076</td>
</tr>
<tr class="even">
<td>Date/Time Created</td>
<td>ORC-9</td>
<td>3005100714.21-400</td>
</tr>
<tr class="odd">
<td>Entered By –ID number</td>
<td>ORC-10.1</td>
<td>54432</td>
</tr>
<tr class="even">
<td>Entered by – family name</td>
<td>ORC-10.2</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Entered by – given name</td>
<td>ORC_10.3</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Entered by – assigning authority</td>
<td>ORC_10.9</td>
<td>100</td>
</tr>
<tr class="odd">
<td>Cost Center</td>
<td>ORC-17</td>
<td>810000</td>
</tr>
<tr class="even">
<td>Ordering Facility</td>
<td>ORC-21</td>
<td>100</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Requisition Line Number</td>
<td>RQD-1</td>
<td>Counter</td>
</tr>
<tr class="odd">
<td>Internal Item Number</td>
<td>RQD-2</td>
<td>3045-2345-999</td>
</tr>
<tr class="even">
<td>Item Number</td>
<td>RQD-3</td>
<td>103041</td>
</tr>
<tr class="odd">
<td>Quantity</td>
<td>RQD-5</td>
<td>125</td>
</tr>
<tr class="even">
<td>Date Needed</td>
<td>RQD-10</td>
<td>20051021</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Est. Item Unit Cost</td>
<td>RQ1-1</td>
<td>3.41</td>
</tr>
<tr class="odd">
<td>BOC</td>
<td>RQ1-3</td>
<td>4435</td>
</tr>
<tr class="even">
<td>Vendor Pointer</td>
<td>RQ1-4</td>
<td>1217</td>
</tr>
<tr class="odd">
<td>NIF Number</td>
<td>RQ1-5</td>
<td>49948</td>
</tr>
</tbody>
</table>

Table B- 8. Message from IFCAP for RIL/2237 Cancel/Edit/Approve

OMN^O07

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 20%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><p><strong>Message</strong></p>
<p><strong>Position</strong></p></th>
<th><strong>Comments or Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Field Separator</td>
<td>MSH-1</td>
<td>|</td>
</tr>
<tr class="odd">
<td>Encoding Characters</td>
<td>MSH-2</td>
<td>^~\&amp;</td>
</tr>
<tr class="even">
<td>Sending Application</td>
<td>MSH-3</td>
<td>PRCV_IFCAP_2237</td>
</tr>
<tr class="odd">
<td>Sending Facility – name space id</td>
<td>MSH-4.1</td>
<td>Station#</td>
</tr>
<tr class="even">
<td>Sending Facility – Universal ID</td>
<td>MSH-4.2</td>
<td>Domain</td>
</tr>
<tr class="odd">
<td>Sending Facility – universal ID type</td>
<td>MSH-4.3</td>
<td>DNS</td>
</tr>
<tr class="even">
<td>Receiving Application</td>
<td>MSH-5</td>
<td>PRCV_DYNAMED</td>
</tr>
<tr class="odd">
<td>Receiving Faciltity – namespace id</td>
<td>MSH-6.1</td>
<td>100DY</td>
</tr>
<tr class="even">
<td>Receiving Facility – Universal ID</td>
<td>MSH-6.2</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Receiving Facility – Universal ID type</td>
<td>MSH-6.3</td>
<td>DNS</td>
</tr>
<tr class="even">
<td>Date/Time of Message</td>
<td>MSH-7</td>
<td>Yyyymmddhhmmss+/-zzzz</td>
</tr>
<tr class="odd">
<td>Message Type –Message Type</td>
<td>MSH-9.1</td>
<td>OMN</td>
</tr>
<tr class="even">
<td>Message Type – Trigger event</td>
<td>MSH-9.2</td>
<td>O07</td>
</tr>
<tr class="odd">
<td>Message Control ID</td>
<td>MSH-10</td>
<td>Populated by Vitria upon Creation</td>
</tr>
<tr class="even">
<td>Processing ID</td>
<td>MSH-11</td>
<td>P or T</td>
</tr>
<tr class="odd">
<td>Version ID</td>
<td>MSH-12</td>
<td>2.4</td>
</tr>
<tr class="even">
<td>Accept Acknowledgment Type</td>
<td>MSH-15</td>
<td>AL</td>
</tr>
<tr class="odd">
<td>Application Acknowledgment Type</td>
<td>MSH-16</td>
<td>AL</td>
</tr>
<tr class="even">
<td>Country Code</td>
<td>MSH-17</td>
<td>USA</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Order Control</td>
<td>ORC-1</td>
<td>CA for Cancel, RO for revision, NW for Approval</td>
</tr>
<tr class="odd">
<td>Date/Time Created</td>
<td>ORC-9</td>
<td>300512130424-400</td>
</tr>
<tr class="even">
<td>Entered By – ID number</td>
<td>ORC-10,1</td>
<td>4543</td>
</tr>
<tr class="odd">
<td>Entered by – familiy name</td>
<td>ORC-10.2</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Entered by first name</td>
<td>ORC_10.3</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Entered by – Assigning authority</td>
<td>ORC_10.9</td>
<td>100</td>
</tr>
<tr class="even">
<td>Ordering Facility</td>
<td>ORC-21</td>
<td>100</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Requisition Line Number</td>
<td>RQD-1</td>
<td>Counter</td>
</tr>
<tr class="odd">
<td>Internal Item Number</td>
<td>RQD-2</td>
<td>3005-847-948</td>
</tr>
<tr class="even">
<td>Item Number</td>
<td>RQD-3</td>
<td>106107</td>
</tr>
<tr class="odd">
<td>Packaging Multiple</td>
<td>RQD-4</td>
<td>1</td>
</tr>
<tr class="even">
<td>Quantity</td>
<td>RQD-5</td>
<td>125</td>
</tr>
<tr class="odd">
<td>Unit of Purchase</td>
<td>RQD-6</td>
<td>EA</td>
</tr>
<tr class="even">
<td>2237 Identifier</td>
<td>RQD-9</td>
<td>100-05-3-8110000-8477</td>
</tr>
<tr class="odd">
<td>Date Needed</td>
<td>RQD-10</td>
<td>20051221</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Est. Item Unit Cost</td>
<td>RQ1-1</td>
<td>3.56</td>
</tr>
<tr class="even">
<td>Vendor Stock Number</td>
<td>RQ1-2</td>
<td>83874HH84838</td>
</tr>
<tr class="odd">
<td>BOC</td>
<td>RQ1-3</td>
<td>4567</td>
</tr>
<tr class="even">
<td>Vendor Pointer and FMS Vendor Pointer</td>
<td>RQ1-4 .1</td>
<td>47764</td>
</tr>
<tr class="odd">
<td>FMS Vendor pointer</td>
<td>RQ1-4.4</td>
<td>383884</td>
</tr>
<tr class="even">
<td>NIF Item Number</td>
<td>RQ1-5</td>
<td>8767553</td>
</tr>
</tbody>
</table>

####### HL7 Message Details 

######## Transmission Packaging

All transactions are transmitted within the MLLP specifications outlined in the Health Level Seven (HL7) standard and are packaged as follows:

Starting block = ASCII 11

Data

REDACTEDiage return

Ending block = ASCII 28

REDACTEDiage return

|                                                                                                     |                                                                                                                     |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/074.png) | *Note:* The final version of this Guide will include HL7 message samples. See Appendix D for sample error messages. | ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/075.png) |

####### Standard Error Codes and Messages

######## HL7 Error Codes

The codes shown in the tables below will be used wherever applicable. These codes and the “fields to be returned” (in the error message) are stored in a separate global, which the M code creating the error message accesses to build the message.

######### HL7 Table 0357

HL7 Table 0357 identifies the HL7 error code, and is populated in HL7 segment ERR-3.1 for the Error Condition Code and in ERR-3.2 for the Description of the Error. For most of the errors generated, these two fields will be "207" and "Application Internal Error" respectively.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 40%" />
<col style="width: 32%" />
<col style="width: 9%" />
<col style="width: 3%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"><p><strong>Error code</strong></p>
<p><strong>PRCV*</strong></p></th>
<th rowspan="2"><strong>Description of error</strong></th>
<th rowspan="2">Fields To Be Returned</th>
<th rowspan="2"><strong>Severity*</strong></th>
<th colspan="2"><strong>System</strong></th>
</tr>
<tr class="odd">
<th><strong>DM</strong></th>
<th><strong>IFCAP</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>Passed ^XTMP global invalid</p>
</blockquote></td>
<td><blockquote>
<p>Passed global name</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td><blockquote>
<p>No message data for passed-in Message ID</p>
</blockquote></td>
<td><blockquote>
<p>Message ID</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td><blockquote>
<p>FCP/CC combination invalid</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, FCP, CC</p>
</blockquote></td>
<td>0</td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td><blockquote>
<p>Invalid date/time msg created</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Create D/T</p>
</blockquote></td>
<td>0</td>
<td>X</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td><blockquote>
<p>Invalid fy for date/time msg created</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Create D/T</p>
</blockquote></td>
<td>0</td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td><blockquote>
<p>Invalid qtr for date/time msg created</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Create D/T</p>
</blockquote></td>
<td>0</td>
<td>X</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>7</strong></td>
<td><blockquote>
<p>Error generating transaction number</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, FCP, CC, Create D/T</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><strong>8</strong></td>
<td><blockquote>
<p>Invalid DUZ/LN/FN combination</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, DUZ, LN, FN</p>
</blockquote></td>
<td>0</td>
<td>X</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td><blockquote>
<p>Item not in Item Master file</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #</p>
</blockquote></td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td><strong>10</strong></td>
<td><blockquote>
<p>Quantity not numeric</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #, Quantity</p>
</blockquote></td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>11</strong></td>
<td><blockquote>
<p>Item unit cost not numeric</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #, Unit Cost</p>
</blockquote></td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td><strong>12</strong></td>
<td><blockquote>
<p>Date Needed not in future</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #, Date Needed</p>
</blockquote></td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>13</strong></td>
<td><blockquote>
<p>Vendor not in Vendor file</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Vendor #</p>
</blockquote></td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td><strong>14</strong></td>
<td><blockquote>
<p>Invalid vendor/item relationship</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #, Vendor #</p>
</blockquote></td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>15</strong></td>
<td><blockquote>
<p>Invalid vendor name found</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #, Vendor #</p>
</blockquote></td>
<td>1</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><strong>16</strong></td>
<td><blockquote>
<p>Unable to add detail record to RIL</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #</p>
</blockquote></td>
<td>1</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><strong>17</strong></td>
<td><blockquote>
<p>Invalid NIF number for item</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #, NIF #</p>
</blockquote></td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td><strong>18</strong></td>
<td><blockquote>
<p>Invalid BOC for item</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #, BOC</p>
</blockquote></td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>19</strong></td>
<td><blockquote>
<p>Invalid site/FCP/CC/BOC combination</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, FCP, CC, BOC</p>
</blockquote></td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td><strong>20</strong></td>
<td><blockquote>
<p>Duplicate Message Control ID</p>
</blockquote></td>
<td><blockquote>
<p>Message ID</p>
</blockquote></td>
<td>0</td>
<td>X</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>21</strong></td>
<td><blockquote>
<p>Missing message control ID</p>
</blockquote></td>
<td></td>
<td>0</td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td><strong>22</strong></td>
<td><blockquote>
<p>Error adding transaction number to 410.1</p>
</blockquote></td>
<td><blockquote>
<p>Message ID, Item #, FCP, CC, STA</p>
</blockquote></td>
<td>1</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

######### HL7 Table 0533

HL7 Table 0533 is a user defined table of specific errors that can be generated by any application. Table D-2 includes three significant pieces of data:

- The severity of the error. This is either an "E" (error) or a "W" (warning), indicating the criticality of the error.
- The Error Code. This is a code number to specify the error. It is a numeric value preceded by "PRCV" or some other string, if the error is related to some error condition outside of IFCAP.
- Text description of the error. The Severity Value is found in HL7 segment ERR-4. The Error Code and Text description are in segments ERR-5.1 and ERR-5.2, respectively.

Table D-2. HL7 Table 0533 Error Codes

| Code | Error text                           | Severity | Status | Date Submitted | Date Approved |
|----------|------------------------------------------|--------------|------------|--------------------|-------------------|
| PRCV1    | Malformed XTMP global                    | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV2    | No message data for passed-in message id | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV3    | FCP/CC combination invalid               | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV4    | Invalid date/time mesg created           | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV5    | Invalid fy for date/time mesg created    | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV6    | Invalid qtr for date/time mesg created   | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV7    | Error generating transaction number      | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV8    | Invalid or missing DUZ                   | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV9    | Item invalid or inactivated              | E            | Approved   | 5/18/05            | 5/24/05           |
| PRCV10   | Quantity not numeric                     | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV11   | Item unit cost not numeric               | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV12   | Date Needed not in future                | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV13   | Vendor not in Vendor file                | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV14   | Invalid vendor/item relationship         | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV15   | Invalid vendor name found                | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV16   | Unable to add detail record to RIL       | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV17   | Invalid NIF number for item              | W            | Approved   | 2/11/05            | 2/16/05           |
| PRCV18   | Invalid BOC for item                     | W            | Approved   | 2/11/05            | 2/16/05           |
| PRCV19   | Invalid site/FCP/CC/BOC combination      | W            | Approved   | 2/11/05            | 2/16/05           |
| PRCV20   | Duplicate message control ID             | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV21   | Missing message control ID               | E            | Approved   | 2/11/05            | 2/16/05           |
| PRCV22   | Duplicate DM Doc ID                      | E            | Approved   | 4/26/05            | 5/5/05            |
| PRCV23   | Error creating Audit file entry          | E            | Approved   | 4/26/05            | 5/5/05            |
| PRCV24   | Missing DynaMed Document ID              | E            | Approved   | 4/26/05            | 5/5/05            |
| PRCV25   | FCP invalid                              | E            | Approved   | 4/29/05            | 5/5/05            |
| PRCV26   | Required Field is not populated          | E            | Approved   | 4/26/05            | 5/5/05            |
| PRCV27   | Invalid Timestamp                        | E            | Approved   | 4/26/05            | 5/5/05            |
| PRCV28   | Invalid Expected Receiving Date          | E            | Approved   | 4/26/05            | 5/5/05            |
| PRCV29   | Invalid Unit of Purchase                 | E            | Approved   | 4/26/05            | 5/5/05            |
| PRCV30   | Dynamed Document ID cancelled            | E            | Approved   | 4/27/05            | 5/5/05            |
| PRCV31   | Dynamed Document ID not found            | E            | Approved   | 4/27/05            | 5/5/05            |
| PRCV32   | Invalid Station-Hospital Identifier      | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV33   | Item Description is missing              | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV34   | Invalid Contract Date                    | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV35   | Invalid Unit of Purchase Price Date      | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV36   | Item Inactive Date is missing            | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV37   | Replacement Item information is invalid  | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV38   | Unit of Issue is invalid                 | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV39   | Re-usable Item indicator is invalid      | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV40   | FSC Code is invalid                      | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV41   | Hazardous Material Flag is invalid       | E            | Approved   | 5/16/05            | 5/18/05           |
| PRCV42   | FCP/Station Combination Invalid          | E            | Approved   | 5/19/05            | 5/24/05           |
| PRCV43   | FCP dollar amount not numeric            | E            | Approved   | 5/19/05            | 5/24/05           |
| PRCV44   | Invalid FCP Balance                      | E            | Approved   | 5/19/05            | 5/24/05           |

######## Sample Error Messages

Following are samples of email error messages sent to the PRCV Audit File Alerts Mail Group.

Figure D‑1. Sample Error Message: Trouble Inserting Data into File 414.02

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: ERROR WHILE PROCESSING DYNAMED-RELATED DATA ITEM [#4196]</p>
<p>03/18/05@10:53 14 lines</p>
<p>From: DOCUMENT PROCESSOR In 'IN' basket. Page 1</p>
<p>-------------------------------------------------------------------------------</p>
<p>While generating PC orders from RIL# 100-05-2-076-828100-3724</p>
<p>involving an item with DynaMed Doc ID #: &lt;SEE BELOW&gt;,</p>
<p>the following error occurred: unable to enter PO# for item in audit file (#414</p>
<p>.02).</p>
<p>The DynaMed DOC ID gets saved into the Audit file when a request is received from DynaMed and a RIL is built. This value is the key used to update Due-ins in DynaMed. Therefore</p>
<p>PLEASE INCLUDE APPROPRIATE DYNAMED USERS WHEN RESOLVING THIS ERROR</p>
<p>The following data pertains to this transaction:</p>
<p>ITEM# 24 placed on PO# 100-U50062 has DM DOC ID# &lt;missing&gt;</p>
<p>ITEM# 42 placed on PO# 100-U50061 has DM DOC ID# 4004-0001-TESTID</p>
<p>ITEM# 75 placed on PO# 100-U50060 has DM DOC ID# &lt;missing&gt;</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Translation:</p>
<p>For items 24 and 75, there was no DM DOC ID set up in the RIL file. Therefore, IFCAP will be unable to update DynaMed about these RILS. It may be the audit File was or was not set up when the RIL was created. It may be that something deleted the DM DOC ID from the RIL file. It is recommended that all values for this RIL are researched. A complete listing of the items received via this RIL should be available by looking at the ‘C’ cross reference of file 414.02. You may also want to check DynaMed to get information associated with the outstanding due-ins for this item and stockroom.</p>
<p>For item 42, the system had trouble inserting data into file 414.02. This could indicate a possible systemic problem.</p></td>
</tr>
</tbody>
</table>

Figure D-2. Sample Error Message: Document ID Not Set Up in Audit File

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: ERROR WHILE PROCESSING DYNAMED-RELATED DATA ITEM [#5207]</p>
<p>04/05/05@16:46 13 lines</p>
<p>From: DOCUMENT PROCESSOR In 'IN' basket. Page 1</p>
<p>-------------------------------------------------------------------------------</p>
<p>While deleting a line item from a purchase order involving an item with DynaMed Doc ID #: 5074-5244-222, the following error occurred: 5074-5244-222 is not in file 414.02 - can't add related data.</p>
<p>The DynaMed DOC ID gets saved into the Audit file when a request is received from DynaMed and a RIL is built. This value is the key used to update Due-ins in DynaMed. Therefore</p>
<p>PLEASE INCLUDE APPROPRIATE DYNAMED USERS WHEN RESOLVING THIS ERROR</p>
<p>The following data pertains to this transaction:</p>
<p>Purchase Order# 100-U50077</p>
<p>ITEM# 106701</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em><strong>Translation:</strong></em> This implies that the Document ID was not set up in the audit file when the RIL was created. It may indicate a bug in the RIL code or a bug that caused this subscript to be deleted by later processing. It may also be a sign of a systemic issue.</td>
</tr>
</tbody>
</table>

Figure D-3. Sample Error Message: Item Missing DynaMed DOC ID

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: ERROR WHILE PROCESSING DYNAMED-RELATED DATA ITEM [#5377] 06/10/05@13:46</p>
<p>14 lines</p>
<p>From: DOCUMENT PROCESSOR In 'IN' basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>While doing an approval of the 2237 #: 100-05-3-4537-1210</p>
<p>involving an item with DynaMed Doc ID #: ...None Found,</p>
<p>the following error occurred: The line item ien: 128280 is missing it's DM DOC</p>
<p>ID..</p>
<p>The DynaMed DOC ID gets saved into the Audit file when a request is</p>
<p>received from DynaMed and a RIL is built. This value is the key used</p>
<p>to update Due-ins in Dynamed. Therefore</p>
<p>PLEASE INCLUDE APPROPRIATE DYNAMED USERS WHEN RESOLVING THIS ERROR</p>
<p>The following data pertains to this transaction:</p>
<p>2237 #: 100-05-3-4537-1210</p>
<p>Item's IEN: 128280</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em><strong>Translation:</strong></em> This implies that the items specified (which did not have the field DM DOC ID populated) were added and that the 2237 was approved. When the update went to DynaMed, DynaMed had information only for the item(s) that originated in DynaMed (that is, those which did have a DM DOC ID).</td>
</tr>
</tbody>
</table>

Figure D-4. Sample Error Message: Item Missing from Audit File

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: ERROR WHILE PROCESSING DYNAMED-RELATED DATA ITEM [#6577]</p>
<p>05/17/05@14:38 16 lines</p>
<p>From: DOCUMENT PROCESSOR In 'IN' basket. Page 1</p>
<p>-------------------------------------------------------------------------------</p>
<p>While canceling a line item during edit of 2237 #100-05-3-076-0958</p>
<p>involving an item with DynaMed Doc ID #: 5124-5369-222,</p>
<p>the following error occurred: the item is missing from the DynaMed Audit file (</p>
<p>#414.02).</p>
<p>The DynaMed DOC ID gets saved into the Audit file when a request is</p>
<p>received from DynaMed and a RIL is built. This value is the key used</p>
<p>to update Due-ins in DynaMed. Therefore</p>
<p>PLEASE INCLUDE APPROPRIATE DYNAMED USERS WHEN RESOLVING THIS ERROR</p>
<p>The following data pertains to this transaction:</p>
<p>2237 #: 100-05-3-076-0958</p>
<p>Date/time deleted: 3050517.14303</p>
<p>Who deleted: REDACTED (35993)</p>
<p>Item #: 106749</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em><strong>Translation:</strong></em> While canceling a line item for the 2237 indicated, IFCAP attempted to update the Audit File record for the item containing this DM Doc ID value, but the appropriate cross reference used to locate the record is missing. The Audit File entry for this item was not updated.</td>
</tr>
</tbody>
</table>

Figure D-5. Sample Error Message: Unable to Update Audit File

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: ERROR WHILE PROCESSING DYNAMED-RELATED DATA ITEM [#7412]</p>
<p>06/02/05@16:03 15 lines</p>
<p>From: DOCUMENT PROCESSOR In 'IN' basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>While updating the DynaMed IFCAP Interface Audit file (#414.02) involving an item with DynaMed Doc ID #: 063-5234-222, the following error occurred: unable to add update to Audit file entry.</p>
<p>The DynaMed DOC ID gets saved into the Audit file when a request is received from DynaMed and a RIL is built. This value is the key used to update Due-ins in DynaMed. Therefore</p>
<p>PLEASE INCLUDE APPROPRIATE DYNAMED USERS WHEN RESOLVING THIS ERROR</p>
<p>The following data pertains to this transaction:</p>
<p>2237 #: 100-05-2-076-1014</p>
<p>Item #: 106701</p>
<p>Error text: The IENS ',' has an empty comma-piece.</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em><strong>Translation:</strong></em> IFCAP attempted to update the Audit File record for the item with the given DM Doc ID value but the data structure used to perform the update was malformed for data-related reasons. The Audit File entry for the item was not updated.</td>
</tr>
</tbody>
</table>

######## RIL Build Error Messages

Message structure is shown in the following table:

Table D-3. RIL Build Error Message Structure

| Message…              | Explanation/Content                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------|
| Source:               | DynaMed sends IFCAP a Requisition. IFCAP returns the error message:                     |
| Mail Message Sender:  | IFCAP/DynaMed Interface                                                                 |
| Mail Message Subject: | RIL build errors in HL7 Message                                                         |
| Mail Message Line:    | Error in Requisition Header for xxxx from HL7 message DYNxxxxxx error number Error Text |

Error text is described in the following table:

Table D-4. RIL Build Error Text Explanation

| Error Text                               | Severity | Explanation                                                                             | Impact                                                | Action               |
|------------------------------------------|----------|-----------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------|
| Wrong Message Type/ Wrong Event Type     | E        | The DynaMed System sent a bad message                                                   | RIL not built                                         | \[To be determined\] |
| Message contains multiple FCP’s or CC’s  | E        | The requisition contains multiple Fund Control Points or Cost Centers                   | RIL not built                                         | \[To be determined\] |
| HL7 Segment length greater than 1K       | E        | The requisition has too much information in it                                          | RIL not built                                         | \[To be determined\] |
| Malformed XTMP global                    | E        | An internal file is corrupt                                                             | Item reported is not added to a RIL                   | Contact EVS          |
| No message data for passed-in message id | E        |                                                                                         | Item reported is not added to a RIL                   |                      |
| FCP/CC combination invalid               | E        | The FCP and the Cost Center combination are not permitted                               | The requisition is not built into a RIL               |                      |
| Invalid date/time mesg created           | E        | The internal date and time of the requisition is not correct                            | The requisition is not built into a RIL               | Contact EVS          |
| Invalid fy for date/time mesg created    | E        | The Fiscal Year for the requisition is not valid                                        | The requisition is not built into a RIL               |                      |
| Invalid qtr for date/time mesg created   | E        | The Fiscal Quarter for the requisition is not valid                                     | The requisition is not built into a RIL               |                      |
| Error generating transaction number      | E        |                                                                                         |                                                       |                      |
| Invalid or missing DUZ                   | E        | The requisition was created by someone that was not authorized to build the requisition | The requisition is not built into a RIL               |                      |
| Item not in Item Master file             | E        | The item sent from DynaMed is not in IFCAP                                              | The item is not added to a RIL.                       |                      |
| Quantity not numeric                     | E        | The quantity is not a number                                                            | The item is not added to a RIL.                       |                      |
| Item unit cost not numeric               | E        | The unit cost of the item is not a number                                               | The item is not added to a RIL                        |                      |
| Date Needed not in future                | E        | The Date Needed is not equal to or greater than today                                   | The item is not added to a RIL                        |                      |
| Vendor not in Vendor file                | E        | The Vendor for the item is not in IFCAP                                                 | The item is not added to a RIL                        |                      |
| Invalid vendor/item relationship         | E        | The item is not ordered from the specified vendor                                       | The item is not added to a RIL                        |                      |
| Unable to add detail record to RIL       | E        | For some undetermined reason, the item was not added to the RIL                         | The item is not added to a RIL                        |                      |
| Invalid NIF number for item              | W        | The National Item File number from DynaMed for the item does not match what is in IFCAP | The item is added to the RIL. This is a warning only. |                      |
| Invalid BOC for item                     | W        | The Budget Office Code from DynaMed for the item does not match what is in IFCAP        | The item is added to the RIL. This is a warning only. |                      |
| Invalid site/FCP/CC/BOC combination      | W        | The combination of FCP, CC and BOC is not valid                                         | The item is added to the RIL. This is a warning only. |                      |
| Duplicate message control ID             | E        | The requisition has been sent from DynaMed more than once.                              | The requisition is not converted into a RIL           | Contact EVS          |
| Missing message control ID               | E        | The requisition was sent incorrectly from DynaMed                                       | The requisition is not converted into a RIL           | Contact EVS          |
| Duplicate DM Doc ID                      | E        | The item is a duplicate of an item already sent from DynaMed                            | The item is not added to the RIL.                     | Contact EVS.         |
| Error creating Audit file entry          | E        | An internal error in processing the requisition occurred                                |                                                       |                      |
| Missing DynaMed Document ID              | E        | The item is not coming from DynaMed                                                     | The item is not added to the RIL                      |                      |
| FCP invalid                              | E        | The Fund Control Point is invalid for the entire requisition                            | The requisition is not converted into a RIL           |                      |
| Required Field is not populated          | E        | If specified, a specific piece of data was not sent from DynaMed to IFCAP               | The item is not added to the RIL                      |                      |
| Invalid Timestamp                        | E        | The date and time of the requisition is not valid                                       | The item is not added to the RIL                      |                      |
| Dynamed Document ID not found            | E        | The internal reference to DynaMed for the item is missing.                              | The item is not added to the RIL                      |                      |

######## RIL/2237 Item Cancellation Messages

Message structure is shown in the following table:

Table D-5. RIL/2237 Item Cancellation or Approval Error Message Structure

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Message…</th>
<th>Explanation/Content</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Source:</td>
<td>IFCAP cancels a RIL or Cancels an item in a 2237, or Cancels an entire 2237, or Approves a 2237 and DynaMed sends the following error message</td>
</tr>
<tr class="even">
<td>Mail Message Sender:</td>
<td>IFCAP/DynaMed Interface</td>
</tr>
<tr class="odd">
<td>Mail Message Subject:</td>
<td>IFCAP to DynaMed (RIL or 2237) Errors (RIL number or 2237 Number)</td>
</tr>
<tr class="even">
<td>Mail Message Line:</td>
<td>Error in Requisition Header for xxxx from HL7 message DYNxxxxxx error number Error Text</td>
</tr>
<tr class="odd">
<td>or:</td>
<td><p>In (RIL or 2237) (RIL number or 2237 number) the following occurred</p>
<p>For Line item [line item number] the [field name] had the following (Warning or Error)</p>
<p>Note: Line item number is the <em>n</em><sup>th</sup> item in the RIL or 2237, that is, the 5<sup>th</sup> item, 10<sup>th</sup> item, etc.</p></td>
</tr>
</tbody>
</table>

Error text is described in the following table:

Table D-6. RIL/2237 Item Cancellation or Approval Error Text Explanation

| Error Text                                                                |     | Severity | Explanation                                                                     | Impact                           | Action               |
|---------------------------------------------------------------------------|-----|----------|---------------------------------------------------------------------------------|----------------------------------|----------------------|
| In (RIL or 2237) (RIL number or 2237 number) there was a bad message type | E   |          | The IFCAP System sent a bad message                                             | Message from IFCAP not processed | \[To be determined\] |
| FCP/CC combination invalid                                                | E   |          | The FCP and the Cost Center combination are not permitted                       |                                  |                      |
| Invalid date/time mesg created                                            | E   |          | The internal date and time of the message is not correct                        |                                  | Contact EVS          |
| Invalid fy for date/time mesg created                                     | E   |          | The Fiscal Year for the transaction is not valid                                |                                  |                      |
| Invalid qtr for date/time mesg created                                    | E   |          | The Fiscal Quarter for the message is not valid                                 |                                  |                      |
| Error generating transaction number                                       | E   |          |                                                                                 |                                  |                      |
| Invalid or missing DUZ                                                    | E   |          | The message was created by someone that was not authorized to build the message |                                  |                      |
| Item not in Item Master file                                              | E   |          | The item sent from IFCAP is not in DynaMed                                      |                                  |                      |
| Quantity not numeric                                                      | E   |          | The quantity is not a number                                                    |                                  |                      |
| Item unit cost not numeric                                                | E   |          | The unit cost is not a number                                                   |                                  |                      |
| Vendor not in Vendor file                                                 | E   |          | The vendor for the item does not exist in DynaMed                               |                                  |                      |
| Invalid vendor/item relationship                                          | E   |          | The item is not approved for the vendor in DynaMed                              |                                  |                      |
| Invalid vendor name found                                                 | E   |          | The vendor name is not in the DynaMed system                                    |                                  |                      |
| Duplicate message control ID                                              | E   |          | The message has already been sent to DynaMed                                    |                                  | Contact IRM          |
| Missing message control ID                                                | E   |          | The message sent from IFCAP was incorrect formate                               |                                  | Contact IRM          |
| Duplicate DM Doc ID                                                       | E   |          |                                                                                 |                                  |                      |
| Error creating Audit file entry                                           | E   |          |                                                                                 |                                  |                      |
| Missing DynaMed Document ID                                               | E   |          | The DynaMed internal reference number is missing                                |                                  |                      |
| FCP invalid                                                               | E   |          | The Fund Control Point was not valid                                            |                                  |                      |
| Required Field is not populated                                           | E   |          | Some Field in the message was missing                                           |                                  |                      |
| Invalid Timestamp                                                         | E   |          | The data and/or time on the message was not valid                               |                                  | Contact IRM          |
| Invalid Unit of Purchase                                                  | E   |          | The unit of purchase for the item was not what was in DynaMed                   |                                  |                      |

######## PO Obligation/Amendment/Receipt/Adjustment Messages

Message structure is shown in the following table:

Table D-7. PO Obligation/Amendment/Receipt/Adjustment Error Message Structure

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Message…</th>
<th>Explanation/Content</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Source:</td>
<td>IFCAP sends DynaMed a PO Obligation/Amendment/Receiving Report/or Receiving Report Adjustment. DynaMed returns the error message:</td>
</tr>
<tr class="even">
<td>Mail Message Sender:</td>
<td>DynaMed</td>
</tr>
<tr class="odd">
<td>Mail Message Subject:</td>
<td>IFCAP to DynaMed (RIL or 2237) Errors (RIL number or 2237 Number)</td>
</tr>
<tr class="even">
<td>Mail Message Capture:</td>
<td><p>Subj: Inventory System PO # 100-U50097 Errors May 05, 2005@13:36:53</p>
<p>[#6143] 05/05/05@13:36 2 lines</p>
<p>From: IFCAP/COTS INVENTORY INTERFACE In 'IN' basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>At Line Number 1 involving Document ID 5117-9999-222 the following errors occurred:</p>
<p>DynaMed Document ID Cancelled</p></td>
</tr>
</tbody>
</table>

Error text is described in the following table:

Table D-8. PO Obligation/Amendment/Receipt/Adjustment Error Text Explanation

| Error Text                               | Severity | Explanation                                                               | Impact                                                | Action                                                                                                      |
|------------------------------------------|----------|---------------------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Wrong Message Type/ Wrong Event Type     |          | The VistA system sent a bad message                                       | PO: The event failed to post into the DynaMed system. | PO: Adjust corresponding element in DynaMed if possible, or request DynaMed support person make adjustment. |
| No message data for passed-in message id |          | The VistA system sent a blank message body                                |                                                       |                                                                                                             |
| Invalid date/time mesg created           |          | The internal date and time of the requisition is not correct              |                                                       |                                                                                                             |
| Error generating transaction number      |          | DynaMed could not create an internal process ID for this event.           |                                                       |                                                                                                             |
| Invalid or missing DUZ                   |          | User identification information was missing from the message              |                                                       |                                                                                                             |
| Item not in Item Master file             |          | DynaMed can’t rectify an item number to their internal tables             |                                                       |                                                                                                             |
| Quantity not numeric                     |          | A quantity on the order is not numeric                                    |                                                       |                                                                                                             |
| Item unit cost not numeric               |          | The unit cost of the item is not a number                                 |                                                       |                                                                                                             |
| Vendor not in Vendor file                |          | The Vendor is not in DynaMed                                              |                                                       |                                                                                                             |
| Invalid vendor/item relationship         |          | The item is not ordered from the specified vendor                         |                                                       |                                                                                                             |
| Missing DynaMed Document ID              |          | The item is missing the DynaMed Doc ID                                    |                                                       |                                                                                                             |
| Required Field is not populated          |          | If specified, a specific piece of data was not sent from IFCAP to DynaMed |                                                       |                                                                                                             |
| Invalid Timestamp                        |          | The date and time of the requisition is not valid                         |                                                       |                                                                                                             |
| Dynamed Document ID not found            |          | The internal reference to DynaMed for the item is missing.                |                                                       |                                                                                                             |

######## Vendor Update Error Messages

Message structure is shown in the following table:

Table D-9. Vendor Update Error Message Structure

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Message…</th>
<th>Explanation/Content</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Source:</td>
<td>IFCAP sends DynaMed a Vendor Update. DynaMed returns the error message:</td>
</tr>
<tr class="even">
<td>Mail Message Sender:</td>
<td>DynaMed</td>
</tr>
<tr class="odd">
<td>Mail Message Capture:</td>
<td><p>Subj: DynaMed Vendor # 19710 Update Errors May 10, 2005@12:14:08 [#6225]</p>
<p>05/10/05@12:14 6 lines</p>
<p>From: IFCAP/COTS INVENTORY INTERFACE In 'IN' basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>Unable to update Vendor in DynaMed.</p>
<p>During a Vendor Update to DynaMed the following errors occurred:</p>
<p>Error generating transaction number</p></td>
</tr>
</tbody>
</table>

Error text is described in the following table:

Table D-10. Vendor Update Error Text Explanation

| Error Text                               | Severity | Explanation                                                               | Impact                                                  | Action                                                                                                      |
|------------------------------------------|----------|---------------------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Wrong Message Type/ Wrong Event Type     |          | The VistA system sent a bad message                                       | Vend: The event failed to post into the DynaMed system. | PO: Adjust corresponding element in DynaMed if possible, or request DynaMed support person make adjustment. |
| No message data for passed-in message id |          | The VistA system sent a blank message body                                |                                                         |                                                                                                             |
| Invalid date/time mesg created           |          | The internal date and time of the requisition is not correct              |                                                         |                                                                                                             |
| Error generating transaction number      |          | DynaMed could not create an internal process ID for this event.           |                                                         |                                                                                                             |
| Invalid or missing DUZ                   |          | User identification information was missing from the message              |                                                         |                                                                                                             |
| Vendor not in Vendor file                |          | The Vendor is not in DynaMed                                              |                                                         |                                                                                                             |
| Required Field is not populated          |          | If specified, a specific piece of data was not sent from IFCAP to DynaMed |                                                         |                                                                                                             |
| Invalid Timestamp                        |          | The date and time of the requisition is not valid                         |                                                         |                                                                                                             |

####### Interface Process Flow Charts

See following pages for process flow charts. See page [E-11](#_Ref106524270) for flow legend and page [E-12](#_Ref106524277) for file and field legends.

Figure 5‑2. Flow Chart: Requisition to RIL Events

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/076.png) |
|-----------------------------------------------------------------------------------------------------|

Figure 5‑3. Flow Chart: Purchase Order Events

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/077.png) |
|-----------------------------------------------------------------------------------------------------|

Figure 5‑4. Flow Chart: Purchase Card Order Events

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/078.png) |
|------------------------------------------------------------------------------------------------------|

Figure 5‑5. Flow Chart: Amendment and Receiving Events

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/079.png) |
|------------------------------------------------------------------------------------------------------|

Figure 5‑6. Flow Chart: Posted Issue Book and Stock Transfers (Issue Request)

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/080.png) |
|------------------------------------------------------------------------------------------------------|

Figure 5‑7. Flow Chart: Posted Issue Book and Stock Transfers (Item Return)

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/081.png) |
|------------------------------------------------------------------------------------------------------|

Figure 5‑8. Flow Chart: Audit File Updates

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/082.png) |
|------------------------------------------------------------------------------------------------------|

Figure 5‑9. Flow Chart: Item and Vendor File Management

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/083.png) |
|------------------------------------------------------------------------------------------------------|

Figure 5‑10. Flow Chart: Fund Control Point Balance Update

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/084.png) |
|------------------------------------------------------------------------------------------------------|

<span id="_Ref106524270" class="anchor"></span>Figure 5‑11. Flow Chart: Process Flow Legend

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/085.png) |
|----------------------------------------------------|

<span id="_Ref106524277" class="anchor"></span>Figure 5‑12. Flow Chart: File and Field Legend

| ![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/086.png) |
|--------------------------------------------------------------------------------------------|

####### Glossary

This glossary defines terms used in the DynaMed-IFCAP Interface development effort. Please note that these definitions are those that pertain to the IFCAP *as it was reactivated at REDACTED VAMC* and the *stand-alone version* of DynaMed being used at REDACTED, which may not necessarily be the same as terms used for the DynaMed version which was formerly integrated as part of the Core Financial and Logistics System (CoreFLS). Please pay particular attention to terms which may have different meanings in IFCAP and DynaMed; these are identified with the appropriate label in the Definition/Discussion column. Likewise, terms that are unique to Health Level 7 (HL7) processes are identified with the *HL7* label.

Related Document:

- [HL7 Glossary of Terms](file:///\\vhabayfas1\Public\Dynamed%20User%20Documentation\Interface_Documents\HL7_Glossary_of_terms.pdf)

REDACTED

Contents:

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 0%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
</colgroup>
<tbody>
<tr class="odd">
<td>0-9</td>
<td>A</td>
<td colspan="2">B</td>
<td>C</td>
<td>D</td>
<td>E</td>
<td>F</td>
<td>G</td>
<td>H</td>
<td>I</td>
<td>J</td>
<td>K</td>
<td>L</td>
<td>M</td>
<td>N</td>
<td>O</td>
<td>P</td>
<td>Q</td>
<td>R</td>
<td>S</td>
<td>T</td>
<td><a href="#G_U">U</a></td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>Y</td>
<td>Z</td>
</tr>
<tr class="even">
<td colspan="3">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/087.png)</td>
<td colspan="25"><p>If you are viewing this document onscreen, you can jump to the Glossary listings that begin with a specific character by clicking on one of the blue hyperlinks on the contents bar immediately above. If a character is grayed out on the bar, it indicates there are no options beginning with that character.</p>
<p>![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/088.png)To return to the hyperlink contents bar above, click the “return” button at the end of each section.</p></td>
</tr>
</tbody>
</table>

|                                                              |                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 0-9                                                          |                                                                                                                        |
| <span id="PRC_158a" class="anchor"></span>Term               | Definition / Discussion                                                                                                |
| 1358                                                         | *IFCAP:* VA Form 1358, *Estimated Obligation or Change in Obligation*                                                  |
| 2138                                                         | *IFCAP:* VA Form 90-2138, *Order for Supplies or Services* (first page of a VA Purchase Order)                         |
| 2139                                                         | *IFCAP:* VA Form 90-2139, *Order for Supplies or Services* (Continuation) (continuation sheet for Form 90-2138)        |
| 2237                                                         | *IFCAP:* VA Form 90-2237, *Request, Turn-in and Receipt for Property or Services* (used to request goods and services) |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/089.png)](#G_TOC) |                                                                                                                        |

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">A</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A&amp;MM</td>
<td><em>See</em> <strong>Acquisition and Materiel Management</strong> (Service)</td>
</tr>
<tr class="even">
<td>AAC</td>
<td><em>See</em> <strong>Austin Automation Center</strong></td>
</tr>
<tr class="odd">
<td>AC</td>
<td><em>See</em> <strong>Application Coordinator</strong></td>
</tr>
<tr class="even">
<td>Accept Acknowledgment</td>
<td><em>HL7: See</em> <strong>Commit Acknowledgment</strong></td>
</tr>
<tr class="odd">
<td>ACK</td>
<td><em>HL7: See</em> <strong>Acknowledgment</strong></td>
</tr>
<tr class="even">
<td>Accountable Officer</td>
<td><em>See</em> <strong>PPM Accountable Officer</strong></td>
</tr>
<tr class="odd">
<td>Accounting Technician (AT)</td>
<td><em>IFCAP:</em> Fiscal employee responsible for obligation and payment of received goods and services.</td>
</tr>
<tr class="even">
<td>Account Processing Code (APC)</td>
<td><em>DynaMed:</em> The code or reference number used to refer to a stockroom (SAPC), customer (CAPC), purchasing (PAPC), or other DynaMed inventory structure.</td>
</tr>
<tr class="odd">
<td>Acknowledgment (ACK)</td>
<td><p><em>HL7:</em> Acknowledgments (or ACKs) may be broadly divided into two groups: application acknowledgments and accept (or commit) acknowledgments. Each group is further subdivided into three subgroups: successful acknowledgment, error messages and rejects. The last two types of acknowledgments are sometimes referred to as <em>negative acknowledgments</em> or NAKs.</p>
<p><em>● Application acknowledgments</em> consist of messages sent by software applications to a peer program. These messages indicate successful processing (by the application or the HL7 subsystem, as appropriate).</p>
<p><em>● Accept (or commit) acknowledgments</em> consist of messages used by the HL7 subsystem to control message transmission. These messages indicate that some error condition exists and serve to communicate that error to the peer</p>
<p><em>● Reject messages</em> are used to indicate that the message could not be processed for some reason (<em>i.e.</em>, it was "rejected").</p>
<p>The term ACK is also used to indicate a specific HL7 message type that can be used to send acknowledgments when no other special message type is defined for that purpose. Whenever used in reference to HL7 messaging, should always be in CAPS (<em>e.g.,</em> ACK or NAK).</p></td>
</tr>
<tr class="even">
<td>Acquisition and Materiel Management (Service) (A&amp;MM)</td>
<td>VA Service responsible for contracting and for overseeing the acquisition, storage, and distribution of supplies, services, and equipment used by VA facilities</td>
</tr>
<tr class="odd">
<td>Adjusted/Returned Value</td>
<td><em>DynaMed:</em> The dollar value of the item involved in the return or inventory adjustment, based on the quantity adjusted or returned and the item’s unit of issue price.</td>
</tr>
<tr class="even">
<td>Admission, Discharge and Transfer (ADT)</td>
<td>Provides for transmitting new or updated demographic and visit information about patients. Generally information will be entered into an ADT system and passed to the nursing, ancillary and financial systems either in the form of an unsolicited update or in response to a record-oriented query.</td>
</tr>
<tr class="odd">
<td>ADP Security Officer (ADPSO)</td>
<td>The individual at a station who is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.</td>
</tr>
<tr class="even">
<td>ADPSO</td>
<td><em>See</em> <strong>ADP Security Officer</strong></td>
</tr>
<tr class="odd">
<td>ADT</td>
<td><em>See</em> <strong>Admission, Discharge and Transfer (ADT)</strong></td>
</tr>
<tr class="even">
<td>Amendment</td>
<td><em>IFCAP:</em> A document that changes the information contained in a specified approved Purchase Order. Amendments are processed by the Purchasing &amp; Contracting section of <strong>A&amp;MM</strong> and obligated, directly or indirectly, by <strong>Fiscal Service</strong>.</td>
</tr>
<tr class="odd">
<td>American Standard Code for Information Interchange (ASCII)</td>
<td>A standard coding scheme that assigns numeric values to letters, numbers, punctuation marks, and control characters, to achieve compatibility among different computers and peripherals. There are 128 standard ASCII codes each of which can be represented by a 7 digit binary number: 0000000 through 1111111, plus parity. Each character is assigned a unique integer value. The values 0 to 31 are used for non-printing control codes, and the range from 32 to 137 is referred to as the standard ASCII character set. All computers that use ASCII can understand the standard ASCII character set. The extended ASCII character set (from code 128 through code 255) is assigned variable sets of characters by computer hardware manufacturers and software developers, and is not necessarily compatible between different computers.</td>
</tr>
<tr class="even">
<td>AO</td>
<td><em>See</em> <strong>Approving Official</strong></td>
</tr>
<tr class="odd">
<td>APC</td>
<td><em>DynaMed: See</em> <strong>Account Processing Code</strong></td>
</tr>
<tr class="even">
<td>Application Acknowledgment</td>
<td><p><em>HL7:</em> A message sent back to the sending system of a message acknowledging completion of processing of the message by the application.</p>
<p><em>Note:</em> On this project, the preferred term is <strong>Commit Acknowledgment.</strong></p></td>
</tr>
<tr class="odd">
<td>Application Coordinator (AC)</td>
<td><em>IFCAP:</em> The individual responsible for the implementation, training and trouble-shooting of a software package within a service. <strong>IFCAP</strong> requires there be an Application Coordinator designated for both the <strong>Fiscal</strong> Service and the <strong>A&amp;MM</strong> Service. This may be the same person, or different persons, depending on the organization’s needs. At REDACTED, there are separate coordinators assigned to each of these two services.</td>
</tr>
<tr class="even">
<td>Approve Requests</td>
<td><em>IFCAP:</em> The use of an electronic signature by a <strong>Control Point Officia</strong>l to approve a <strong>2237, 1358</strong> or other request form and transmit the request to <strong>A&amp;MM</strong> and/or <strong>Fiscal</strong>.</td>
</tr>
<tr class="odd">
<td>Approving Official (AO)</td>
<td><em>IFCAP:</em> A user who reviews <strong>Purchase Card</strong> reconciliations to ensure that they are correct and complete, and approves them if appropriate.</td>
</tr>
<tr class="even">
<td>Area</td>
<td><em>DynaMed:</em> Stockroom location.</td>
</tr>
<tr class="odd">
<td>ASCII</td>
<td><em>See</em> <strong>American Standard Code for Information Interchange</strong></td>
</tr>
<tr class="even">
<td>AT</td>
<td><em>See</em> <strong>Accounting Technician</strong></td>
</tr>
<tr class="odd">
<td>Austin Automation Center (AAC)</td>
<td><p><em>IFCAP related:</em> The AAC is a federal data center within the <strong>VA</strong>. Located in Austin, Texas, the AAC is aligned under the Office of Information and Technology (OI&amp;T) in Washington, DC, and provides a full complement of cost-efficient e-government solutions and enterprise ”best practices” to its customers. AAC provides services to VA and other federal agencies. AAC is the physical location of many of the "systems" used by VA, including the <strong>Financial Management System (FMS)</strong>. Many of the national databases are located there.</p>
<p><em>See</em> REDACTED</p></td>
</tr>
<tr class="even">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/090.png)</a></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">B</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Batch Number</td>
<td><em>IFCAP:</em> A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or <strong>Transmission Number</strong>.</td>
</tr>
<tr class="even">
<td>BOC</td>
<td><em>See</em> <strong>Budget Object Code</strong></td>
</tr>
<tr class="odd">
<td>Breakout Code</td>
<td><em>IFCAP:</em> A set of <strong>A&amp;MM</strong> codes which identifies a vendor by the type of ownership (<em>e.g.</em>, minority-owned, Vietnam veteran-owned, Small Business Total Set Aside, etc.).</td>
</tr>
<tr class="even">
<td>Brother Cart</td>
<td><em>DynaMed:</em> One of a pair of identical carts that are mobile and exchanged between the stockroom, where they are restocked, and the ward that uses the items. <em>See also</em> <strong>Mother Cart.</strong></td>
</tr>
<tr class="odd">
<td>Budget Object Code (BOC)</td>
<td><p><em>IFCAP:</em> BOCs are used to classify the type of personal service, supplies or service (see listing in VA Handbook 4671.2, or at…</p>
<p>REDACTED Any combination of BOCs can be associated with <strong>CC</strong>s, unless specified. Each <strong>Control Point</strong> is assigned one or more BOCs. The BOC enables budgeting and tracking control point spending by type of supplies or service. BOC helps to define “what” is being purchased. It is sometimes referred to as the sub-account.</p>
<p><em>In DynaMed,</em> this is called the Nature of Expense (NOE).</p></td>
</tr>
<tr class="even">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/091.png)</a></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">C</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CAPC</td>
<td><em>DynaMed: See</em> <strong>Account Processing Code</strong></td>
</tr>
<tr class="even">
<td>Cart</td>
<td><em>DynaMed.</em> Storage location for inventory items in the stockroom or hospital.</td>
</tr>
<tr class="odd">
<td>Cart Level</td>
<td><em>DynaMed:</em> When the <strong>Cart</strong> reaches the <strong>Cart Reorder Point</strong>, the system replenishes the cart to the item quantity, or cart level.</td>
</tr>
<tr class="even">
<td>Cart Reorder Point (ROP)</td>
<td><em>DynaMed:</em> If stock levels drop below the designated reorder point, the system automatically replenishes stock levels to the set cart level.</td>
</tr>
<tr class="odd">
<td>Cart ROP</td>
<td><em>DynaMed. See</em> <strong>Cart Reorder Point.</strong></td>
</tr>
<tr class="even">
<td>Catalog Master</td>
<td><em>DynaMed:</em> <em>See</em> <strong>Master Catalog.</strong></td>
</tr>
<tr class="odd">
<td>Catalog Master Item</td>
<td><em>DynaMed: See:</em> <strong>Master Catalog Item.</strong></td>
</tr>
<tr class="even">
<td>CC</td>
<td><em>See</em> <strong>Cost Center.</strong> <em>Also see</em> <strong>Credit Charge.</strong></td>
</tr>
<tr class="odd">
<td>CCA</td>
<td><em>See</em> <strong>Clinger-Cohen Act</strong></td>
</tr>
<tr class="even">
<td>CCS</td>
<td><em>See</em> <strong>Credit Card System</strong></td>
</tr>
<tr class="odd">
<td>Ceiling Transactions</td>
<td><em>IFCAP:</em> Funding distributed from <strong>Fiscal Service</strong> to IFCAP <strong>Control Points</strong> for spending. The <strong>Budget Analyst</strong> initiates these transactions using the Funds Distribution options.</td>
</tr>
<tr class="even">
<td>CF</td>
<td><em>DynaMed. See</em> <strong>Conversion Factor.</strong></td>
</tr>
<tr class="odd">
<td>Classification of Request</td>
<td><em>IFCAP:</em> An identifier a <strong>Control Point</strong> can assign to track requests that fall into a category, <em>e.g.</em>, Memberships, Replacement Parts, Food Group III.</td>
</tr>
<tr class="even">
<td>Clinger-Cohen Act (CCA)</td>
<td><p>The Clinger-Cohen Act (CCA) started the VA down the road to <strong>COTS</strong>. The federal Office of Management and Budget outlined the Act’s COTS requirements in <strong>OMB Circular No. A-130, §8b:</strong></p>
<p><em>Acquisition of Information Technology. Agencies shall:</em></p>
<p><em>(a) Acquire information technology in a manner that makes use of full and open competition and that maximizes return on investment;</em></p>
<p><em>(b) Acquire off-the-shelf software from commercial sources, unless the cost effectiveness of developing custom software to meet mission needs is clear and has been documented;</em></p>
<p><em>(c) Acquire information technology in accordance with OMB Circular No. A-109, "Acquisition of Major Systems," where appropriate; and</em></p>
<p><em>(d) Acquire information technology in a manner that considers the need for accommodations of accessibility for individuals with disabilities to the extent that needs for such access exist.</em></p>
<p><em>Source:</em> <a href="http://www.whitehouse.gov/omb/circulars/a130/a130.html">http://www.whitehouse.gov/omb/circulars/a130/a130.html</a></p>
<p><em>See also</em> <a href="http://www.gao.gov/policy/itguide/criteria.htm#CCA">http://www.gao.gov/policy/itguide/criteria.htm#CCA</a></p></td>
</tr>
<tr class="odd">
<td>Commercial Off-the-Shelf (COTS)</td>
<td>The term COTS describes software or hardware products that are ready-made and available for sale to the general public. For example, Microsoft Office is a COTS product that is a packaged software solution for businesses. COTS products are designed to be implemented easily into existing systems without the need for customization. <em>Also see</em> <strong>Clinger-Cohen Act</strong>.</td>
</tr>
<tr class="even">
<td>Commit Acknowledgment</td>
<td><p><em>HL7:</em> An <strong>HL7</strong> message sent back to the sending system of a message acknowledging receipt of the message. The receiving system commits the message to safe storage in a manner that releases the sending system from any obligation to resend the message. A response is returned to the initiator indicating successful receipt and secure storage of the information.</p>
<p><em>Note:</em> On this project, <em>Commit Acknowledgment</em> is preferred over the equivalent <em>Application Acknowledgment.</em></p>
<p><em>See also:</em> <strong>Acknowledgment, Application Acknowledgment,</strong> and <strong>Negative Acknowledgment</strong></p></td>
</tr>
<tr class="odd">
<td>Common Numbering Series</td>
<td><em>IFCAP:</em> This is a pre-set series of <strong>Procurement and Accounting Transaction</strong> (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders, Requisitions or Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering Series used by each facility.</td>
</tr>
<tr class="even">
<td>Control Point (CP)</td>
<td><em>IFCAP:</em> A Control Point is used to divide funds into separate accounts and to permit the tracking of monies to a specified service, activity or purpose from an Appropriation or Fund. This element exists only in IFCAP. A CP corresponds to a set of elements in the <strong>Financial Management System</strong> that include the <strong>Account Classification Code</strong> (ACC) and which define the Sub-Allowance in <strong>FMS</strong>.</td>
</tr>
<tr class="odd">
<td>Control Point Clerk (CPC)</td>
<td><em>IFCAP:</em> The user within the service who is designated to input requests (<strong>2237</strong>s) and maintain the <strong>Control Point</strong> records for a Service.</td>
</tr>
<tr class="even">
<td>Control Point Official (CPO)</td>
<td><em>IFCAP:</em> The individual authorized to expend government funds for ordering of supplies and services for their <strong>Control Point</strong>(s). This person has all of the options the <strong>Control Point Clerk</strong> has plus the ability to approve requests by using their electronic signature code.</td>
</tr>
<tr class="odd">
<td>Control Point Official's Balance</td>
<td><em>IFCAP:</em> A running record of all the transactions generated and approved for a <strong>Control Point</strong> from within <strong>IFCAP</strong> and also effects changes to the control point that are initiated directly from within the <strong>FMS</strong>. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="even">
<td>Control Point Requestor (CPR)</td>
<td><em>IFCAP:</em> The lowest level <strong>Control Point</strong> user, who can only enter temporary requests (<strong>2237</strong>s, <strong>1358</strong>s) to a <strong>Control Point</strong>. CPRs can only view or edit their own requests. A <strong>Control Point Clerk</strong> or <strong>Control Point Official</strong> must make these requests permanent before they can be approved and transmitted to <strong>A&amp;MM</strong>.</td>
</tr>
<tr class="odd">
<td>Controlling Stockroom</td>
<td><em>DynaMed:</em> The controlling stockroom maintains control of the <strong>Master Catalog</strong> entry for items and is, in some cases, the only stockroom authorized to make certain changes to items.</td>
</tr>
<tr class="even">
<td>Conversion Factor</td>
<td><em>DynaMed:</em> The ratio between the unit of measure and the unit of issue.</td>
</tr>
<tr class="odd">
<td>Core Financial and Logistics System (CoreFLS)</td>
<td>CoreFLS was designed as a state-of-the-art integrated software package that would replace a diverse mixture of old-technology systems, including <strong>IFCAP,</strong> with an integrated commercial off-the-shelf system solution. The new software was to be used by every financial and logistics office within the VA Central Office (VACO), the Veterans Health Administration (VHA), the Veterans Benefits Administration (VBA), and the National Cemetery Administration (NCA). The REDACTED VAMC was chosen as the primary pilot site for introduction of CoreFLS. On July 26, 2004, VA management decided to suspend development efforts on CoreFLS, and directed reversion to IFCAP at REDACTED. Later, the decision was made to use the <strong>DynaMed</strong> package in conjunction with IFCAP at REDACTED.</td>
</tr>
<tr class="even">
<td>CoreFLS</td>
<td><em>See</em> <strong>Core Financial and Logistics System</strong></td>
</tr>
<tr class="odd">
<td>Cost Center (CC)</td>
<td><p><em>IFCAP:</em> Cost Centers are unique numbers that define a specific service (<em>e.g.,</em> 842100 or 421 Fiscal Service). One cost center must be attached to every <strong>Fund Control Point</strong>. This enables costs to be captured by service. Several Cost Centers can be associated with one control point in a one (CP)-to-many (CC) relationship. Cost Centers are standardized (<strong>VHA</strong> uses 8000 series). The Cost Center list may be found in VA Handbook 4671.1 and at…</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>COTS</td>
<td><em>See</em> <strong>Commercial Off-the-Shelf</strong></td>
</tr>
<tr class="odd">
<td>CP</td>
<td><em>See</em> <strong>Control Point</strong></td>
</tr>
<tr class="even">
<td>CPC</td>
<td><em>See</em> <strong>Control Point Clerk</strong></td>
</tr>
<tr class="odd">
<td>CPC</td>
<td><em>See</em> <strong>Control Point Clerk</strong></td>
</tr>
<tr class="even">
<td>CPO</td>
<td><em>See</em> <strong>Control Point Official</strong></td>
</tr>
<tr class="odd">
<td>CPO</td>
<td><em>See</em> <strong>Control Point Official</strong></td>
</tr>
<tr class="even">
<td>CPR</td>
<td><em>See</em> <strong>Control Point Requestor</strong></td>
</tr>
<tr class="odd">
<td>CPR</td>
<td><em>See</em> <strong>Control Point Requestor</strong></td>
</tr>
<tr class="even">
<td>Credit Card System (CCS)</td>
<td>CCS is the database in Austin that processes the credit card information from the external Credit Card Vendor system and then passes information on to <strong>FMS</strong> and IFCAP.</td>
</tr>
<tr class="odd">
<td>Credit Charge (CC)</td>
<td>Used by <strong>FMS</strong> and <strong>CCS</strong> for charges paid to vendors through the Credit Card payment process.</td>
</tr>
<tr class="even">
<td>Customer</td>
<td><em>DynaMed:</em> The receiver of stockroom items, which often includes nursing units or other medical specialties.</td>
</tr>
<tr class="odd">
<td>Customer Account Processing Code (CAPC)</td>
<td><em>DynaMed. See</em> <strong>Account Processing Code</strong></td>
</tr>
<tr class="even">
<td>Customer Type</td>
<td><em>DynaMed:</em> The customer type code. EC indicates external customer, IC indicates internal customer, and ES indicates external stockroom.</td>
</tr>
<tr class="odd">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/092.png)</a></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 16%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">D</th>
</tr>
<tr class="odd">
<th>Term</th>
<th colspan="2">Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Data Type</td>
<td colspan="2"><em>HL7:</em> <strong>HL7</strong> provides a special set of HL7 data types into which data elements are categorized. These are defined in Chapter 2 of Health Level Seven, Version 2.4. <em>See also the document</em> <a href="../User%20Documentation/More%20about%20HL7.doc">More About HL7</a>.</td>
</tr>
<tr class="even">
<td>Date Committed</td>
<td colspan="2"><em>IFCAP:</em> The date that <strong>IFCAP</strong> committed funds to the purchase or expenditure.</td>
</tr>
<tr class="odd">
<td>Default</td>
<td colspan="2">A suggested response that is provided by the system. For example, a transaction date that matches the system date may be offered as the default.</td>
</tr>
<tr class="even">
<td>Deficiency</td>
<td colspan="2"><em>IFCAP:</em> Condition that exists when a budget has obligated and expended more than it was funded.</td>
</tr>
<tr class="odd">
<td>Delinquent Delivery Listing</td>
<td colspan="2"><em>IFCAP:</em> A listing of all the <strong>Purchase Orders</strong> that have not had all the items received by the Warehouse on <strong>IFCAP</strong>. It is used to contact the vendor for updated delivery information.</td>
</tr>
<tr class="even">
<td>Delivery Order</td>
<td colspan="2"><em>IFCAP:</em> An order for an item that the <strong>VA</strong> purchases through an established contract with a vendor who supplies the items.</td>
</tr>
<tr class="odd">
<td>Direct Delivery Patient</td>
<td colspan="2"><em>IFCAP:</em> A patient who has been designated to have goods delivered directly to him/her from the vendor.</td>
</tr>
<tr class="even">
<td>Discount Item</td>
<td colspan="2"><em>IFCAP:</em> This is a trade discount on a <strong>Purchase Order</strong>. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.</td>
</tr>
<tr class="odd">
<td>Document Number</td>
<td colspan="2"><em>DynaMed:</em> The number which uniquely identifies each item record in the DynaMed database. It consists of:</td>
</tr>
<tr class="even">
<td></td>
<td>Y</td>
<td>Last digit of current calendar Year ( 0 - 9 )</td>
</tr>
<tr class="odd">
<td></td>
<td>DDD</td>
<td>The Julian Date ( 001 - 366 )</td>
</tr>
<tr class="even">
<td></td>
<td>9999</td>
<td>Serial Number from ‘0001’ to ‘9999’</td>
</tr>
<tr class="odd">
<td></td>
<td>CCCCCC</td>
<td>Stockroom APC (Account Processing Code) (up to 6 alphanumeric characters)</td>
</tr>
<tr class="even">
<td></td>
<td colspan="2">These elements are concatenated with no spaces and no separators: YDDD9999CCCCCC.</td>
</tr>
<tr class="odd">
<td>Due In</td>
<td colspan="2"><em>DynaMed:</em> A request in DynaMed by a stockroom for an inventory item.</td>
</tr>
<tr class="even">
<td>DUZ</td>
<td colspan="2"><p><em>IFCAP:</em> DUZ is a variable name in the <strong>VistA</strong> environment that uniquely identifies a user. It is a numeric field and is established for each user when the user is first given login codes. The DUZ is stored in the user “New Person” file (File 200).</p>
<p>If a user moves to a different medical facility and new login codes are generated, then the user will be given a new, unique DUZ number for that facility. If a user has access to multiple work areas in a facility (for example, a development environment, a test environment, and a production environment), then a unique DUZ will be generated for that user for each environment.</p>
<p><em>DynaMed:</em> In the REDACTED DynaMed-IFCAP Interface <em>only</em>, the DUZ combined with <strong>Station Number</strong> is used to uniquely identify an individual in both systems, so that security can be maintained. In addition, the DUZ/Station Number combination is sent to DynaMed from IFCAP when transactions are pushed from IFCAP to DynaMed.</p></td>
</tr>
<tr class="odd">
<td>DynaMed</td>
<td colspan="2">An automated inventory management, order requisition and distribution system for healthcare providers, published by <strong>Information Control, LLC.</strong> DynaMed provided the inventory management functionality for <strong>CoreFLS.</strong> This project is developing an interface between IFCAP and the DynaMed product for use at REDACTED VAMC. DynaMed runs under the UNIX operating system and uses an <strong>Oracle</strong> database. <em>See also</em> <a href="http://www.info-control.com/material_mngmt/index.html">http://www.info-control.com/material_mngmt/index.html</a></td>
</tr>
<tr class="even">
<td colspan="3"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/093.png)</a></td>
</tr>
</tbody>
</table>

| E                                                            |                                                                                                                                                                                                  |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                                                                          |
| EDI                                                          | *See*Electronic Data Interchange                                                                                                                                                            |
| EDI Vendor                                                   | A vendor with whom the VA has negotiated an arrangement to conduct business via Electronic Data Interchange, including the submission, acceptance and filling of orders electronically.  |
| Electronic Data Interchange (EDI)                            | A method of electronically exchanging business documents according to established rules and formats.                                                                                             |
| Electronic Signature                                         | *IFCAP:* The electronic signature code replaces the written signature on all IFCAP documents used within the facility. Documents going off-station will require a written signature as well. |
| Expenditure Request                                          | *IFCAP:* A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).                                                    |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/094.png)](#G_TOC) |                                                                                                                                                                                                  |

| F                                                            |                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                     |
| Federal Procurement Data System (FPDS)                       | The FPDS is the central repository of statistical information on Federal contracting. The system contains detailed information on contract actions over \$25,000 and summary data on procurements of less than \$25,000. The Executive departments and agencies award over \$200 billion annually for goods and services. The system can identify who bought what, from whom, for how much, when and where. |
| FCP                                                          | *See*Fund Control Point (*see also*Control Point).                                                                                                                                                                                                                                                                                                                                                |
| Federal Tax ID                                               | *IFCAP:* A unique number that identifies a given station to the Internal Revenue Service.                                                                                                                                                                                                                                                                                                                   |
| Financial Management System (FMS)                            | The centralized primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.                          |
| Financial Services Center (FSC)                              | FSC is located in Austin, Texas, and operates as a VA Enterprise Center, provides a full range of financial services to the Department of Veterans Affairs and other federal agencies. *See* REDACTED                                                                                                                                                                                                   |
| Fiscal (Service)                                             | *IFCAP:* Fiscal Service is responsible for the VA facility's financial activities including development of departmental budgets, maintenance of cost control systems, preparation of statistical reports, and managing disbursements and receipts.                                                                                                                                                      |
| Fiscal Quarter                                               | The Fiscal Year is broken into four three-month quarters. The first fiscal quarter for the federal government begins on October 1.                                                                                                                                                                                                                                                                      |
| Fiscal Year (FY)                                             | Twelve-month period from October 1 through September 30.                                                                                                                                                                                                                                                                                                                                                    |
| FMS                                                          | *See*Financial Management System                                                                                                                                                                                                                                                                                                                                                                       |
| FOB                                                          | *See*Freight on Board                                                                                                                                                                                                                                                                                                                                                                                  |
| FPDS                                                         | *See*Federal Procurement Data System                                                                                                                                                                                                                                                                                                                                                                   |
| Freight on Board (FOB)                                       | A delivery term used to indicate who is responsible for payment of freight costs. FOB “Destination” means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. FOB “Origin” means that shipping charges are due to the shipper, and must be paid when the shipper arrives at the warehouse with the item.   |
| Fringe Item                                                  | *DynaMed:* An item ordered by a stockroom but not stocked in that stockroom. Provides the same functionality found in a pass-through or virtual stockroom.                                                                                                                                                                                                                                                  |
| FSC                                                          | *See*Financial Services Center                                                                                                                                                                                                                                                                                                                                                                         |
| Fund Control Point (FCP)                                     | *See*Control Point                                                                                                                                                                                                                                                                                                                                                                                     |
| Funds Control                                                | A group of Control Point options that allow the Control Point Clerk and/or Control Point Official to maintain and reconcile their funds.                                                                                                                                                                                                                                                        |
| FY                                                           | *See*Fiscal Year                                                                                                                                                                                                                                                                                                                                                                                       |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/095.png)](#G_TOC) |                                                                                                                                                                                                                                                                                                                                                                                                             |

| H                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| HCPCS Code                                                   | *See*Healthcare Common Procedure Coding System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Health Level 7 (HL7)                                         | Health Level Seven is one of several American National Standards Institute (ANSI) -accredited Standards Developing Organizations operating in the healthcare arena. "Level Seven" refers to the highest level of the International Standards Organization's (ISO) communications model for Open Systems Interconnection (OSI)— the application level. The application level addresses definition of the data to be exchanged, the timing of the interchange, and the communication of certain errors to the application. The seventh level supports such functions as security checks, participant identification, availability checks, exchange mechanism negotiations and, most importantly, data exchange structuring. HL7 focuses on the interface requirements of the entire health care organization. Source: <http://www.hl7.org/about/>. *See also the document* [More About HL7](..\User%20Documentation\More%20about%20HL7.doc). |
| Healthcare Common Procedure Coding System (HCPCS Code)       | Indicates the reimbursement code used when billing Medicare and other insurers for supplies, materials, injections, and other services and procedures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Heartbeat                                                    | *Heartbeat is a VIE development monitoring tool to monitor connectivity and connection models. Heartbeat is a VIE development monitoring tool to monitor connectivity and connection models.Heartbeat* is a VIE development monitoring tool to monitor connectivity and connection models.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| HL7                                                          | *See*Health Level 7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/096.png)](#G_TOC) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">I</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IC</td>
<td><em>See</em> <strong>Information Control, LLC</strong></td>
</tr>
<tr class="even">
<td>ICD</td>
<td><em>See</em> <strong>Interface Control Document</strong></td>
</tr>
<tr class="odd">
<td>Identification Number</td>
<td><em>IFCAP:</em> A computer-generated number assigned to an entity, such as a code sheet.</td>
</tr>
<tr class="even">
<td>IDL</td>
<td><em>See</em> <strong>Interface Definition Language</strong></td>
</tr>
<tr class="odd">
<td>IFCAP</td>
<td><em>See</em> <strong>Integrated Funds Distribution, Control Point Activity, Accounting and Procurement</strong></td>
</tr>
<tr class="even">
<td>IM</td>
<td><em>See</em> <strong>Inventory Manager</strong></td>
</tr>
<tr class="odd">
<td>IMF</td>
<td><em>See</em> <strong>Item Master File</strong></td>
</tr>
<tr class="even">
<td>Information Control, LLC (IC)</td>
<td>Software development company that produced the version of the <strong>DynaMed</strong> software used in conjunction with the DynaMed-IFCAP Interface. <em>See</em> <a href="http://www.info-control.com/">http://www.info-control.com/</a></td>
</tr>
<tr class="odd">
<td>Information Resources Management (IRM)</td>
<td>The service which manages information and computing resources. Usually, this refers to the information resources staff at a <strong>VAMC</strong>, and that is the usage on this project.</td>
</tr>
<tr class="even">
<td>Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)</td>
<td>The <strong>VistA</strong> package that enables VA personnel to manage funding, procurement and distribution of materials.</td>
</tr>
<tr class="odd">
<td>Interface Control Document (ICD)</td>
<td>Document that describes the project, its scope and purpose, and how the interface(s) between the various software packages work.</td>
</tr>
<tr class="even">
<td>Interface Definition Language (IDL)</td>
<td><p>The Interface Definition Language (IDL) is a language for specifying operations (procedures or functions), parameters to these operations, and data types. The purpose of an IDL is to define a protocol between client and server processes so that they can communicate with each other at a level higher than simple byte strings in a heterogeneous networking environment.</p>
<p><em>Sources:</em> <a href="http://www.accord.com/products/doc/IDL.html">http://www.accord.com/products/doc/IDL.html</a>, <a href="http://www.opengroup.org/onlinepubs/9629399/chap4.htm">http://www.opengroup.org/onlinepubs/9629399/chap4.htm</a></p></td>
</tr>
<tr class="odd">
<td>Internal Sourcing</td>
<td><em>DynaMed:</em> A flag indicating whether the vendor is an internal or external source of supply. If Internal Sourcing designates “Yes,” DynaMed requires the user to identify the stockroom set as the source of supply.</td>
</tr>
<tr class="even">
<td>Internal Voucher (IV)</td>
<td><p><em>DynaMed:</em> An IV is created when an item is transferred from the warehouse to other using service stockroom, or when an adjustment to a stockroom transfer is accomplished through the return or refusal process in DynaMed. <em>See also</em> <strong>Standard Voucher (SV).</strong></p>
<p><em>Note:</em> For those familiar with inventory systems, this same terminology is used in the Generic Inventory Program (GIP).</p></td>
</tr>
<tr class="odd">
<td>Inventory Manager (IM)</td>
<td><em>DynaMed:</em> The individual responsible for managing inventory in a stock room, ward, or similar resource (what is called the <strong>Control Point</strong> in <strong>IFCAP).</strong></td>
</tr>
<tr class="even">
<td>IRM</td>
<td><em>See</em> <strong>Information Resources Management</strong></td>
</tr>
<tr class="odd">
<td>Item File</td>
<td><em>See</em> <strong>Item Master File</strong></td>
</tr>
<tr class="even">
<td>Item History</td>
<td><em>IFCAP:</em> Procurement information stored in the <strong>Item File</strong>. A history is kept by <strong>Control Point</strong> and is available to the <strong>Control Point</strong> at time of request.</td>
</tr>
<tr class="odd">
<td>Item Master File (IMF)</td>
<td><p><em>IFCAP:</em> A listing of items specified by <strong>A&amp;MM</strong> service as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.</p>
<p><em>DynaMed:</em> The corresponding file in DynaMed is the <strong>Master Catalog.</strong> It is an exact copy of the IFCAP Item Master file.</p></td>
</tr>
<tr class="even">
<td>Item Master Number</td>
<td><p><em>IFCAP:</em> A computer generated number used to identify an item in the <strong>Item File</strong>.</p>
<p><em>DynaMed:</em> The corresponding name in DynaMed is the <strong>Master Catalog Item Number.</strong></p></td>
</tr>
<tr class="odd">
<td>IV</td>
<td><em>DynaMed:</em> <em>See</em> <strong>Internal Voucher.</strong></td>
</tr>
<tr class="even">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/097.png)</a></td>
</tr>
</tbody>
</table>

| J                                                            |                                                                                                                                                                                                     |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                                                                             |
| Justification                                                | *IFCAP:* A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source. |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/098.png)](#G_TOC) |                                                                                                                                                                                                     |

| L                                                            |                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                               |
| Liquidation                                                  | *IFCAP:* The amount of money posted to the 1358 or Purchase Order as a payment to the vendor. Liquidations are processed through payment/invoice tracking.                                                                                                                                                                                                                                    |
| Location Capacity                                            | *DynaMed:* The maximum number of items users may place in a location.                                                                                                                                                                                                                                                                                                                                 |
| LOG I                                                        | LOG I is the Logistics A&MM computer located at the Austin Automation Center. This system continues to support the Consolidated Memorandum of Receipt.                                                                                                                                                                                                                                |
| Lower Layer Protocol (LLP)                                   | *HL7:* Defined by the *HL7 Implementation Guide*. An LLP provides for a degree of lower layer communications functionality, such as flow control and error recovery, needed between systems in a networked environment. Examples include the Minimal Lower Layer Protocol (MLLP). *See* <http://www.hl7.org/memonly/downloads/Attachment_Specifications/CDAR1AIS0000R021_ImplementationGuide.pdf> |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/099.png)](#G_TOC) |                                                                                                                                                                                                                                                                                                                                                                                                       |

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">M</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>M</td>
<td><p><em>M</em> is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. MUMPS data structures are sparse, using strings of characters as subscripts.</p>
<p><em>M</em> was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.</p>
<p><em>See also the document</em> <a href="../User%20Documentation/More%20about%20M.doc">More About M</a>.</p></td>
</tr>
<tr class="even">
<td>MailMan</td>
<td><em>IFCAP:</em> The mail manager communications service integrated into <strong>VistA</strong>. MailMan provides human-to-human email, database-to-database data transfers, machine-to-human reports, application software releases, patch releases, and <strong>HL7</strong> batch messages.</td>
</tr>
<tr class="odd">
<td>Mandatory Source</td>
<td><em>IFCAP:</em> Any federal government agency that sells supplies and services to the <strong>VA</strong>. Includes the VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.</td>
</tr>
<tr class="even">
<td>Mandatory Vendor</td>
<td><em>IFCAP:</em> Non-Warehouse fund control points are required to procure certain items only from the Warehouse. For such items, the Warehouse is the <em>mandatory vendor</em> for that item, non-Warehouse FCPs cannot order from any other source. If a Warehouse fund control point processes the requirement, the Warehouse user is presented a list of vendors for the item, with the <strong>Preferred Vendor</strong> at the top of the list. In addition, some items may have a mandatory source <em>other</em> than the Warehouse designated; in such cases, all users (including the Warehouse) are required to order from that vendor. <em>See also</em> <strong>Preferred Vendor.</strong></td>
</tr>
<tr class="odd">
<td>Master Catalog</td>
<td><em>DynaMed:</em> The file containing the list of items which can be ordered, inventoried, or otherwise controlled. The corresponding file in IFCAP is the <strong>Item Master File.</strong></td>
</tr>
<tr class="even">
<td>Master Catalog Item</td>
<td><em>DynaMed.</em> An item in the Master Catalog file. The corresponding name in IFCAP is the <strong>Item Master Number</strong>.</td>
</tr>
<tr class="odd">
<td>Message</td>
<td><p><em>HL7:</em> A message is the atomic unit of data transferred between systems. It is comprised of a group of segments in a defined sequence. Each message has a message type that defines its purpose. For example, the ADT (admissions/discharge/transfer) Message type is used to transmit portions of a patient’s ADT data from one system to another. A three character code contained within each message identifies its type.</p>
<p><em>Source:</em> Health Level Seven, <em>Health Level Seven, Version 2.3.1</em>, copyright 1999, p. E-18., quoted in <a href="http://www.va.gov/vdl/VistA_Lib/Infrastructure/Health_Level_7_(HL7)/hl71_6p93sp.doc">http://www.va.gov/vdl/VistA_Lib/Infrastructure/Health_Level_7_(HL7)/hl71_6p93sp.doc</a></p></td>
</tr>
<tr class="even">
<td>Message Delimiter</td>
<td><em>HL7:</em> In constructing an <strong>HL7</strong> <strong>Message</strong>, certain characters are used to separate different parts of the message. These include the Segment Terminator, the Field Separator, the Component Separator, the Sub- Component Separator, Repetition Character, and the Escape Character.</td>
</tr>
<tr class="odd">
<td>Message Header (MSH)</td>
<td><em>HL7:</em> Specific segment of an <strong>HL7</strong> <strong>Message</strong> that defines the intent, source, destination, and some specifics of the syntax of a message. The Message Header (MSH) segment is always the first segment in every HL7 message (except for batch HL7 messages, which begin with BHS or FHS segments). This HL7 segment contains control fields that characterize any one particular HL7 message.</td>
</tr>
<tr class="even">
<td>Message ID (MID)</td>
<td><p><em>HL7:</em> The <em>Message ID</em> is an <strong>ASCII</strong> string that uniquely identifies each HL7 message. It is included in <strong>MSH</strong> Field 10 of every generated message.</p>
<p><em>Also called</em> Message Control ID.</p></td>
</tr>
<tr class="odd">
<td>Message Type</td>
<td><em>HL7:</em> Each <strong>HL7</strong> <strong>Message</strong> has a 3-character message type that defines its purpose. For example, the ADT (admissions/discharge/transfer) Message Type is used to transmit portions of a patient’s ADT data from one system to another. The Message type code (one component of a message header's Message Type field) is defined by HL7 Table 0076, Message type. <em>See also</em> <a href="..\User%20Documentation\More%20about%20HL7.doc">More About HL7</a>.</td>
</tr>
<tr class="even">
<td>MID</td>
<td><em>See</em> <strong>Message ID</strong></td>
</tr>
<tr class="odd">
<td>Middleware</td>
<td><em>HL7:</em> In computing, middleware consists of software agents acting as an intermediary between different application components. It is used most often to support complex, distributed applications. The software agents involved may be one or many. The <strong>Vitria</strong> <em>BusinessWare</em> product is an example of middleware.</td>
</tr>
<tr class="even">
<td>Minimal Lower Layer Protocol (MLLP, MLP)</td>
<td><em>HL7:</em> <em>Multiple lower level protocol (MLLP) Multiple lower level protocol (MLLP)</em>MLLP is a transport specification, widely used in the <strong>HL7</strong> community, although not actually part of the HL7 standard. It is a very simple <strong>Lower Layer Protocol</strong> that simply delimits messages. It is used in LAN-based networking environments such as TCP/IP that provide a reliable byte stream (flow control and error recovery are provided by the network), but insufficient session control to support HL7. <em>Sources:</em> <a href="http://www.va.gov/vdl/VistA_Lib/Infrastructure/Health_Level_7_(HL7)/hl71_6p93sp.doc">http://www.va.gov/vdl/VistA_Lib/Infrastructure/Health_Level_7_(HL7)/hl71_6p93sp.doc</a> and <a href="http://www.hl7.org/Library/Committees/cq/mllp_transport_specification.PDF">http://www.hl7.org/Library/Committees/cq/mllp_transport_specification.PDF</a></td>
</tr>
<tr class="odd">
<td>MLP</td>
<td><em>See</em> <strong>Minimal Lower Layer Protocol</strong></td>
</tr>
<tr class="even">
<td>MLLP</td>
<td><em>See</em> <strong>Minimal Lower Layer Protocol</strong></td>
</tr>
<tr class="odd">
<td>Mother Cart</td>
<td><em>DynaMed:</em> Supply cart for a group or family of similar carts. The stockroom supplies the Mother cart and the child carts. Cart ID of the Mother cart for the cart listed. <em>See also</em> <strong>Brother Cart.</strong></td>
</tr>
<tr class="even">
<td>MSC Confirmation Message</td>
<td><em>IFCAP:</em> A <strong>Mailman</strong> message generated by the Austin Message Switching Center that assigns an <strong>FMS</strong> number to an <strong>IFCAP</strong> transmission of documents.</td>
</tr>
<tr class="odd">
<td>MSH</td>
<td><em>See</em> <strong>Message Header</strong></td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td><em>See</em> <strong>M</strong></td>
</tr>
<tr class="odd">
<td>MWB</td>
<td><em>See</em> <strong>Messaging Workbench</strong></td>
</tr>
<tr class="even">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/100.png)</a></td>
</tr>
</tbody>
</table>

| N                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                           |
| NAK                                                          | *See*Negative Acknowledgment                                                                                                                                                                                                                                                                                                                                                                                 |
| National Cemetery Administration (NCA)                       | The federal agency responsible for providing burial benefits to veterans and eligible dependents. The delivery of these benefits involves managing 120 National Cemeteries nationwide, providing grave markers worldwide, administering the State Cemetery Grants Program that complements the National Cemeteries network, and providing Presidential Memorial Certificates to next of kin of deceased veterans. |
| Nature of Expense (NOE)                                      | *DynaMed. See*Budget Object Code.                                                                                                                                                                                                                                                                                                                                                                            |
| NCA                                                          | *See*National Cemetery Administration                                                                                                                                                                                                                                                                                                                                                                        |
| Negative Acknowledgment (NAK)                                | A transmission control character used to indicate that a transmitted message was received with errors or corrupted or that the receiving station is not ready to accept transmissions. The receiver sends the code to the sender to indicate that the transmission must be resent. *See also*Acknowledgment, Commit Acknowledgment, and Application Acknowledgment.                                      |
| Net Asset                                                    | *DynaMed:* Sum of the current quantity on hand, less quantity due out, plus quantity due in.                                                                                                                                                                                                                                                                                                                      |
| NOE                                                          | *DynaMed. See*Nature of Expense.                                                                                                                                                                                                                                                                                                                                                                             |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/101.png)](#G_TOC) |                                                                                                                                                                                                                                                                                                                                                                                                                   |

| O                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Obligation                                                   | The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.                                                                                                                                                                                                                                                                                                                                                                    |
| Obligation (Actual) Amount                                   | *IFCAP:* The actual dollar figure obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document on IFCAP.                                                                                                                                                                                                                                                            |
| Obligation Data                                              | *IFCAP:* A Control Point option that allows the Control Point Clerk and/or Budget Analyst to enter data not recorded by IFCAP.                                                                                                                                                                                                                                                                                                                                 |
| Obligation Number                                            | The 6-character string assigned to a Purchase Order by IFCAP (*e.g.,* A50002).                                                                                                                                                                                                                                                                                                                                                                                         |
| Oracle                                                       | In the context of this document, Oracle® refers to a relational database management system software package. It is the underlying database for the DynaMed software product. *Note:* Oracle was also part of the former CoreFLS software product, and provided an intermediary database link between parts of CoreFLS. As used in this project, the term “Oracle” does *not* refer to a standalone Oracle database; *that* particular “Oracle” went away with CoreFLS. |
| Organization Code                                            | *IFCAP:* Accounting element functionally comparable to Cost Center but used to organize purchases by the budget that funded them, not the purposes for spending the funds.                                                                                                                                                                                                                                                                                             |
| OSI                                                          | *See*Open Systems Interconnection                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Outstanding 2237                                             | *IFCAP:*A&MM report that lists all the IFCAP generated 2237s pending action in A&MM.                                                                                                                                                                                                                                                                                                                                                                          |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/102.png)](#G_TOC) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">P</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PAPC</td>
<td><em>DynaMed. See</em> <strong>Purchasing Account Processing Code</strong></td>
</tr>
<tr class="even">
<td>Partial</td>
<td><em>IFCAP:</em> A <strong>Purchase Order Receiving Report</strong> that accounts for only a part of the items ordered on a <strong>Purchase Order</strong> (<em>i.e.,</em> not all of the items have yet been accounted for).</td>
</tr>
<tr class="odd">
<td>Partial Date</td>
<td><em>IFCAP:</em> The date that a warehouse clerk created a <strong>Receiving Report</strong> for a partial shipment.</td>
</tr>
<tr class="even">
<td>PAT</td>
<td><em>See</em> <strong>Procurement and Accounting Transaction</strong></td>
</tr>
<tr class="odd">
<td>PAT Number</td>
<td><em>IFCAP:</em> <strong>Procurement and Accounting Transaction</strong> number— the primary FMS reference number. <em>See also</em> <strong>Obligation Number.</strong></td>
</tr>
<tr class="even">
<td>PCard</td>
<td><em>See</em> <strong>Purchase Card</strong></td>
</tr>
<tr class="odd">
<td>Personal Property Management (PPM)</td>
<td>A section of <strong>A&amp;MM Service</strong> responsible for screening all requests for those items available from a <strong>Mandatory Source</strong>, VA Excess or bulk sale. This service also processes all requisitions for goods from Federal Agencies and equipment requests. In addition, PPM maintains the inventory of Warehouse stocked items and all equipment at the facilities they support. Now referred to at most sites as <strong>Acquisition and Materiel Management</strong> Service or <strong>A&amp;MM</strong>. <em>See also</em> <strong>Requisition.</strong></td>
</tr>
<tr class="even">
<td>Picklist</td>
<td><em>DynaMed:</em> Picking is a process that allows items to be withdrawn (as for issue to a customer) from inventory stock. The pick process is based on a list of items called a Picklist. A Picklist displays item names, quantities, and locations. <em>See also</em> <strong>Putlist.</strong></td>
</tr>
<tr class="odd">
<td>PL 100-32</td>
<td><em>See</em> <strong>Public Law 100-32</strong></td>
</tr>
<tr class="even">
<td>PO</td>
<td><em>See</em> <strong>Purchase Order</strong></td>
</tr>
<tr class="odd">
<td>PORR</td>
<td><em>See</em> <strong>Purchase Order Receiving Report</strong></td>
</tr>
<tr class="even">
<td>Procurement and Accounting Transaction (PAT) Number</td>
<td><em>IFCAP:</em> A common identifier (number) used by Purchasing and Contracting, <strong>Personal Property Management</strong>, Accounting Technicians and Imprest Funds Clerks to identify <strong>Purchase Orders</strong>, <strong>Requisitions</strong>, and Accounting Transactions on IFCAP.</td>
</tr>
<tr class="odd">
<td>PPM</td>
<td><em>See</em> <strong>Personal Property Management</strong></td>
</tr>
<tr class="even">
<td>PPM Accountable Officer</td>
<td><em>IFCAP:</em> A person who reviews <strong>2237</strong> transactions to ensure they are complete and approved by the Control Point Official for a valid control point. This person also routes received 2237s to others in Purchasing for follow up. <em>See</em> <strong>Personal Property Management</strong>.</td>
</tr>
<tr class="odd">
<td>Preferred Vendor (PV)</td>
<td><em>IFCAP:</em> For most items, a <em>preferred vendor</em> (defined as the vendor from which the item is usually ordered, because we have negotiated good terms with that vendor, or our experience tells us this vendor is the most reliable, or has good quality control, or whatever...) has been assigned. All other things being equal, the item must be procured from that preferred vendor. When the Warehouse processes an order, a list of available vendors for the item is presented; if a preferred vendor has been associated with the item <em>for that FCP</em>, the preferred vendor will appear at the top of the list. In order for a “preferred vendor” to display as such, it must be established in the Item Master File for a specific fund control point. This is accomplished by using the “Item File Edit Option” in the Purchasing Agent Menu or the Accountable Officer Menu. (It is not automatically populated.) <em>See also</em> <strong>Mandatory Vendor</strong>.</td>
</tr>
<tr class="even">
<td>Program Code</td>
<td><em>IFCAP:</em> Accounting element that identifies the <strong>VA</strong> initiative or program that the purchase will support.</td>
</tr>
<tr class="odd">
<td>Prompt Payment Terms</td>
<td>The discount given to the <strong>VA</strong> for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).</td>
</tr>
<tr class="even">
<td>Public Law 100-32</td>
<td><p>Public Law 100-322 authorizes <strong>VA</strong> to establish research corporations and defines their powers. It also established a Vet Center National Plan specifying, among other things, the locations of various VA facilities.</p>
<p>Various events trigger submission of the IFCAP PRCHOUT P.L. 100-322 report, the “PL 100-32 Report.” For example, a co-location of a Vet Center after January 1988 must be reported to Congress as a revision of the Vet Center National Plan pursuant to 38 U.S.C. (United States Code) Section 1712A as amended by Public Law 100-322. These reports are available through the Statistics menu using the options PRCHOUT P.L. 100-322 REASON or PRCHOUT P.L. 100-322.</p></td>
</tr>
<tr class="odd">
<td>Purchase Card (PCard)</td>
<td><em>IFCAP:</em> A debit card that a <strong>Purchase Card User</strong> employs to make purchases. Purchase Cards use money from a deposited balance of <strong>VA</strong> funds.</td>
</tr>
<tr class="even">
<td>Purchase Card Coordinator</td>
<td><em>IFCAP:</em> A person authorized by a <strong>VA</strong> station to monitor and resolve delinquent purchase card orders, help VA services record, edit and approve purchase card orders in a timely manner, assign purchase cards to IFCAP users, and monitor the purchase card expenses of <strong>VAMC</strong> services.</td>
</tr>
<tr class="odd">
<td>Purchase Card Orders (PCard Orders)</td>
<td><em>IFCAP:</em> Orders funded by a <strong>Purchase Card.</strong></td>
</tr>
<tr class="even">
<td>PCard User</td>
<td><em>See</em> <strong>Purchase Card User</strong></td>
</tr>
<tr class="odd">
<td>Purchase Card User</td>
<td><em>IFCAP:</em> A person who uses a <strong>Purchase Card</strong>. Purchase Card Users are responsible for recording their purchase card orders in IFCAP.</td>
</tr>
<tr class="even">
<td>Purchase History Add (PHA)</td>
<td><em>IFCAP:</em> A transaction containing information about purchase orders which is automatically sent to Austin for archiving. This same transaction is also used to send a <strong>PO</strong> for <strong>EDI</strong> processing.</td>
</tr>
<tr class="odd">
<td>Purchase History Modify (PHM)</td>
<td><em>IFCAP:</em> A transaction containing information about amendments, which is automatically sent to Austin for archiving.</td>
</tr>
<tr class="even">
<td>Purchase Order (PO)</td>
<td><p><em>IFCAP:</em> A government document (VA Form 90-2138, <em>Order for Supplies or Services</em> and VA Form 90-2139, <em>Order for Supplies or Services (Continuation)</em>), authorizing the purchase of goods or services at the terms indicated. Under <strong>IFCAP</strong>, the 2138/2139 provide in one set of forms a purchase or delivery order, vendor’s invoice, and receiving report. They will be used in lieu of but in the same manner as Optional Form 347, <em>Order for Supplies or Services</em>, Optional Form 348, <em>Order for Supplies or Services Schedule-Continuation</em>, and Standard Form 1449, <em>Solicitation/Contract/Order for Commercial Items</em>. <em>See also</em> <strong>Requisition</strong> and <a href="http://www1.va.gov/oamm/vaar/vaar813.htm#813307">VAAR PART 813.307 Forms</a>.</p>
<p><em>DynaMed:</em> Although DynaMed does not track POs as such, it does record the PO number associated with a specific inventory item, once data for that PO has been supplied by IFCAP.</p></td>
</tr>
<tr class="odd">
<td>Purchase Order Acknowledgment</td>
<td><em>IFCAP:</em> Information returned by the vendor describing the status of items ordered (<em>e.g.,</em> “10 CRTs shipped, 5 CRTs backordered”).</td>
</tr>
<tr class="even">
<td>Purchase Order Receiving Report (PORR)</td>
<td><em>IFCAP:</em> Report that the <strong>Warehouse Clerk</strong> creates to record that the warehouse has received an item; or, the VA document used to indicate the quantity and dollar value of the goods being received.</td>
</tr>
<tr class="odd">
<td>Purchase Order Status</td>
<td><em>IFCAP:</em> The status of completion of a <strong>Purchase Order</strong> (<em>e.g.</em>, Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).</td>
</tr>
<tr class="even">
<td>Purchasing Account Processing Code (PAPC)</td>
<td><em>DynaMed: See</em> <strong>Account Processing Code</strong></td>
</tr>
<tr class="odd">
<td>Purchasing Agents</td>
<td><strong>A&amp;MM</strong> employees legally empowered to create <strong>Purchase Orders</strong> to obtain goods and services from commercial vendors.</td>
</tr>
<tr class="even">
<td>Putaway</td>
<td><p><em>DynaMed:</em> As inventory is received, especially when inventories are large, determining the correct location for placement is difficult in many large warehouses. Often, the result is that inventory is placed into warehouse locations that make it difficult to pick during order fulfillment. In extreme cases, inventory can even become lost.</p>
<p>DynaMed provides advice to warehouse personnel as to which zones and bins are available for use and which bins should be used. This advice is based upon certain information that warehouse personnel provide about the warehouse facility and the inventory.</p></td>
</tr>
<tr class="odd">
<td>Putlist</td>
<td><em>DynaMed:</em> A list of items to put away in the stockroom. Includes locations and quantities for all items listed. <em>See also</em> <strong>Picklist.</strong></td>
</tr>
<tr class="even">
<td>PV</td>
<td><em>See</em> <strong>Preferred Vendor</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/103.png)</a></td>
</tr>
</tbody>
</table>

| Q                                                            |                                                                                                                                     |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                             |
| Quarterly Report                                             | *IFCAP:* A Control Point listing of all transactions (Ceilings, Obligations, Adjustments) made against a Control Point's Funds. |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/104.png)](#G_TOC) |                                                                                                                                     |

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">R</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Receiving Report</td>
<td><em>See</em> <strong>Purchase Order Receiving Report</strong></td>
</tr>
<tr class="even">
<td>Reconciliation</td>
<td><em>IFCAP:</em> Comparing of two records to validate IFCAP Purchase Card orders. <strong>Purchase Card Users</strong> compare IFCAP generated purchase card order data with the <strong>Credit Charge</strong> transaction sent from the <strong>CCS</strong> in Austin.</td>
</tr>
<tr class="odd">
<td>Reference Number</td>
<td><em>IFCAP:</em> The computer generated number that identifies a request. It is comprised of the: <strong>Station Number</strong>, the <strong>Fiscal Year</strong>, <strong>Fiscal Quarter</strong>, the <strong>Control Point</strong>, and a 4-digit sequence number, in the format STA-FY-Q-FCP-NNNN. The FCP is a 3- or 4-digit number. Example: 100-04-3-012-0001.. <em>Also known as</em> the <strong>Transaction Number</strong>.</td>
</tr>
<tr class="even">
<td>Reorder Point (ROP)</td>
<td><em>DynaMed:</em> The stock level below which the system automatically generates a replenishment order for the item.</td>
</tr>
<tr class="odd">
<td>Repetitive (PR Card) Number</td>
<td><em>See</em> <strong>Item Master Number</strong></td>
</tr>
<tr class="even">
<td><p>Repetitive Item List</p>
<p>(RIL)</p></td>
<td><p><em>IFCAP:</em> A method the <strong>Control Point</strong> uses to order items in the Item File. The Control Point enters the <strong>Item Master Number</strong>, the quantity and vendor; IFCAP can sort and generate <strong>2237</strong> requests from the list. The auto-generate feature within the Inventory portion of the package can be used to create an RIL.</p>
<p><em>Note:</em> In the REDACTED interface <em>only</em>, <strong>DynaMed</strong> sends messages that cause a RIL to be generated in IFCAP. The RIL is then processed in IFCAP.</p></td>
</tr>
<tr class="odd">
<td>Req</td>
<td><em>See</em> <strong>Requisition</strong></td>
</tr>
<tr class="even">
<td>Requestor</td>
<td><em>See</em> <strong>Control Point Requestor</strong></td>
</tr>
<tr class="odd">
<td>Requirements Analyst</td>
<td><em>IFCAP:</em> A person who monitors warehouse inventories, creates picking tickets, and creates <strong>Requisitions</strong> and <strong>Purchase Orders</strong> to replenish warehouse stock.</td>
</tr>
<tr class="even">
<td>Requisition</td>
<td><p><em>DynaMed:</em> In <strong>DynaMed,</strong> a <em>requisition</em> (or “req”) is a list of required items that are to be procured, as well as the authorization to initiate the procurement process</p>
<p><em>Under <strong>VistA</strong>, the term “requisition” signifies an acquisition made from another government agency, when an</em> <strong>SF-49</strong> <em>was used instead of the usual</em> <strong>Purchase Order</strong> <em>(</em><strong>VA Form 2138</strong><em>). A requisition was assigned a</em> <strong>PAT Number</strong> <em>generated from its designated common numbering series.</em></p>
<p><em>IFCAP:</em> For sites using <strong>DynaMed</strong>, the VistA definition is no longer used, and the DynaMed requisition may be used to create a <strong>Repetitive Item List (RIL)</strong>, a <strong>2237</strong> and, later, a <strong>Purchase Order</strong> in <strong>IFCAP</strong>.</p></td>
</tr>
<tr class="odd">
<td>Requisition Objective (RO)</td>
<td><em>DynaMed:</em> Goal for reordering the item in the stockroom. Once the item reaches the reorder point (ROP), the system reorders it in a multiple of the conversion factor to the reorder level.</td>
</tr>
<tr class="even">
<td>RIL</td>
<td><em>See</em> <strong>Repetitive Item List</strong></td>
</tr>
<tr class="odd">
<td>RO</td>
<td><em>See</em> <strong>Requisition Objective.</strong></td>
</tr>
<tr class="even">
<td>ROP</td>
<td><em>See</em> <strong>Reorder Point.</strong></td>
</tr>
<tr class="odd">
<td>RR</td>
<td><em>See</em> <strong>Purchase Order Receiving Report</strong></td>
</tr>
<tr class="even">
<td>Running Balance</td>
<td><em>IFCAP:</em> A running record of all the transactions generated and approved for a <strong>Control Point</strong>. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="odd">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/105.png)</a></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">S</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SAPC</td>
<td><em>DynaMed. See</em> <strong>Stockroom Account Processing Code</strong></td>
</tr>
<tr class="even">
<td>Section Request</td>
<td><em>IFCAP:</em> A temporary request for goods and/or services entered by a <strong>Control Point Requestor</strong>. These requests may or may not be made permanent by the <strong>Control Point Clerk/Official</strong>.</td>
</tr>
<tr class="odd">
<td>Service Balance</td>
<td><em>IFCAP:</em> The amount of money on the on the original <strong>1358</strong> and any adjustments to that <strong>1358</strong> when created by that service in their <strong>Fund Control Point</strong>. This amount is reduced by any authorizations created by the service.</td>
</tr>
<tr class="even">
<td>SF-49</td>
<td><em>See</em> <strong>Standard Form 49</strong></td>
</tr>
<tr class="odd">
<td>Short Description</td>
<td><em>IFCAP:</em> A phrase that describes the item in the <strong>Item File</strong>. The description is 3 to 60 characters in length, and consists of what the item is, the kind of item, and the size of item (<em>e.g.,</em> GLOVE-SURGICAL MEDIUM).</td>
</tr>
<tr class="even">
<td>Site Parameters</td>
<td><p><em>IFCAP:</em> Accounting and administrative information (such as <strong>Station Number</strong>, Cashier's address, printer location, etc.) that is unique to a given station. All of IFCAP at a given site uses a single Site Parameter file.</p>
<p><em>See also</em> <strong>System Parameters</strong>.</p></td>
</tr>
<tr class="odd">
<td>SKU</td>
<td><em>See</em> <strong>Stock Keeping Unit.</strong></td>
</tr>
<tr class="even">
<td>SLC</td>
<td><em>See</em> <strong>Stockage List Code.</strong></td>
</tr>
<tr class="odd">
<td>Sort Group</td>
<td><em>IFCAP:</em> An identifier, which a <strong>Control Point</strong> can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.</td>
</tr>
<tr class="even">
<td>Special Remarks</td>
<td><em>IFCAP:</em> A field on the <strong>Control Point Request</strong> that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.</td>
</tr>
<tr class="odd">
<td>Stacked Documents</td>
<td><em>IFCAP:</em> The <strong>Purchase Orders, Requisitions,</strong> and <strong>1358</strong>s that are sent electronically to <strong>Fiscal</strong> and stored in a file for printing at a later time rather than being printed immediately.</td>
</tr>
<tr class="even">
<td>Standard Form 49 (SF-49)</td>
<td><em>Requisition/Procurement Request for Equipment Supplies or Services</em>. A federal government form used to request acquisition of materials from other federal agencies. <em>See</em> <a href="http://contacts.gsa.gov/webforms.nsf/0/C2E9B6F2409D139A852569B40005C037/$file/gs49.pdf">http://contacts.gsa.gov/webforms.nsf/0/C2E9B6F2409D139A852569B40005C037/$file/gs49.pdf</a>. <em>See also</em> <strong>Standard Forms</strong> and <strong>Requisition.</strong></td>
</tr>
<tr class="odd">
<td>Standard Forms</td>
<td>“Standard” forms are those approved by the U.S. General Services Administration (GSA) for mandatory use by government agencies or establishments, unless a specific exemption is obtained.</td>
</tr>
<tr class="even">
<td>Standard Voucher (SV)</td>
<td><p><em>DynaMed:</em></p>
<p><em>See also</em> <strong>Internal Voucher (IV).</strong></p>
<p><em>Note:</em> For those familiar with inventory systems, this same terminology is used in the Generic Inventory Program (GIP).</p></td>
</tr>
<tr class="odd">
<td>Station Number</td>
<td><em>IFCAP:</em> Station numbers are the official identification numbers for funding and budgetary purposes, and for describing the sphere of authority of an organizational entity designated by the Secretary. A uniform station numbering system provides a unique identifier for each station and allows for easier association and integration of data among systems. A three-digit identifier is to be used Department wide for all purposes where a coded station identifier is required. Where another department, such as the Department of the Treasury, requires a station number of four or more digits, the VA three-digit station number will be preceded by as many zeroes as are needed to comply with the requesting department’s needs. In some cases, a two-character modifier may be added to uniquely identify specific facilities within a given station, like a medical center or domiciliary division of a complex station. The Station Number is stored in the Institution File (File 004). <em>Source:</em> <a href="http://www.warms.vba.va.gov/admin20/mp_1/part2/ch34.doc">http://www.warms.vba.va.gov/admin20/mp_1/part2/ch34.doc</a>. <em>See also</em> <strong>DUZ.</strong></td>
</tr>
<tr class="even">
<td>Stock Keeping Unit (SKU)</td>
<td><p><em>DynaMed:</em> Unique identifier for the item across the enterprise. Item stock number. Main and unique identifier for the item throughout the system.</p>
<p><em>IFCAP:</em> Corresponds with Item Number.</p></td>
</tr>
<tr class="odd">
<td>Stockage List Code (SLC)</td>
<td><em>DynaMed:</em> Determines whether the Inventory Manager or the system controls item stock levels, or whether the item is a fringe item.</td>
</tr>
<tr class="even">
<td>Stockroom Account Processing Code (SAPC)</td>
<td><em>DynaMed. See</em> <strong>Account Processing Code</strong></td>
</tr>
<tr class="odd">
<td>Sub-Cost Center</td>
<td><em>IFCAP:</em> A subcategory of <strong>Cost Center</strong>. <strong>IFCAP</strong> does not utilize a “sub-cost center” field, but will send <strong>FMS</strong> the last two digits of the cost center as the FMS “sub-cost center” field.</td>
</tr>
<tr class="even">
<td>SV</td>
<td><em>DynaMed. See</em> <strong>Standard Voucher (SV).</strong></td>
</tr>
<tr class="odd">
<td>System Parameters</td>
<td><p><em>IFCAP:</em> Information about the IFCAP system that is unique to a given system. An entry in this file is used to indicate which inventory system is used for that system (at REDACTED, for example, a system parameter is set to indicate that DynaMed is the inventory system in use).</p>
<p><em>See also</em> <strong>Site Parameters</strong>.</p></td>
</tr>
<tr class="even">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/106.png)</a></td>
</tr>
</tbody>
</table>

| T                                                            |                                                                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                                                |
| Tasked Job                                                   | A computer job, usually a printout, which has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them. |
| Transaction Number                                           | *IFCAP:* The number of the transaction that funded a Control Point. *Same as*Reference Number.                                                                |
| Transmission Number                                          | *IFCAP:* A sequential number given to a data string when it is transmitted to the Austin Data Processing Center; used for tracking message traffic.                    |
| Type Code                                                    | *IFCAP:* A set of A&MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.                              |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/107.png)](#G_TOC) |                                                                                                                                                                        |

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><span id="G_U" class="anchor"></span>U</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UI</td>
<td><em>See</em> <strong>Unit of Issue.</strong></td>
</tr>
<tr class="even">
<td>UM</td>
<td><em>See</em> <strong>Unit of Measure.</strong></td>
</tr>
<tr class="odd">
<td>Unit of Issue (UI)</td>
<td><p><em>DynaMed:</em> The measure by which the stockroom issues the item.</p>
<p><em>See also</em> <strong>Conversion Factor</strong></p></td>
</tr>
<tr class="even">
<td>Unit of Measure (UM)</td>
<td><p><em>DynaMed:</em> Unit type for stockroom receipt of an item. Equal to the unit of purchase for stock items users receive from a vendor. Equal to the unit of issue of the supplying stockroom for stock items users receive from another stockroom.</p>
<p><em>See also</em> <strong>Conversion Factor</strong></p></td>
</tr>
<tr class="odd">
<td>Unit of Purchase (UOP)</td>
<td><em>DynaMed:</em> Unit size for stockroom receipt of an item. Examples are BXT = box of 100 and BGT = bag of 100.</td>
</tr>
<tr class="even">
<td>Unit of Purchase Conflict</td>
<td><em>DynaMed:</em> Occurs when the user orders the item in one unit of measure, then receives it in a different unit of measure. Users resolve the unit of purchase conflict in DynaMed Menu Item D7, Receipt Verification – UOP Conflict.</td>
</tr>
<tr class="odd">
<td>UOP</td>
<td><em>See</em> <strong>Unit of Purchase.</strong></td>
</tr>
<tr class="even">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/108.png)</a></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">V</th>
</tr>
<tr class="odd">
<th>Term</th>
<th>Definition / Discussion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA</td>
<td><em>See</em> <strong>Veterans Affairs</strong> (Department of)</td>
</tr>
<tr class="even">
<td>VACO</td>
<td><em>See</em> <strong>Veterans Affairs Central Office</strong></td>
</tr>
<tr class="odd">
<td><p>VA Form 90-2138 (2138)</p>
<p>VA Form 90-2139 (2139)</p>
<p>VA Form 90-2138-ADP</p>
<p>VA Form 90-2139-ADP</p></td>
<td><em>IFCAP:</em> VA Form 90-2138, Order for Supplies or Services; VA Form 90-2139, Order for Supplies or Services (Continuation); VA Form 90-2138-ADP, Purchase Order for Supplies or Services; and VA Form 90-2139-ADP, Order for Supplies and Services (Continuation). See <strong>Purchase Order.</strong></td>
</tr>
<tr class="even">
<td>VAMC</td>
<td><em>Acronym for</em> <strong>Veterans Affairs Medical Center</strong></td>
</tr>
<tr class="odd">
<td>Vendor file</td>
<td><em>IFCAP:</em> An IFCAP file of vendor information solicited by the facility. This file contains ordering and billing addresses, contract information, <strong>FPDS</strong> information and telephone numbers. The debtor's address may be drawn from this file, but is maintained separately.</td>
</tr>
<tr class="even">
<td>Vendor ID Number</td>
<td><em>IFCAP:</em> The ID number assigned to a vendor by the <strong>FMS</strong> Vendor unit. The ID number is stored in the Vendor File (File 440)</td>
</tr>
<tr class="odd">
<td>Vendor Request (VRQ) (message)</td>
<td><em>IFCAP:</em> When a new vendor is added to <strong>IFCAP</strong> a Vendor Request (VRQ) message is sent electronically to the Austin <strong>FMS</strong> Vendor unit to determine if the vendor exists in the central vendor system. If the vendor is not in the system, Austin will confirm information and establish the vendor in the central file. If vendor exists in central file already, Austin will verify the data. <em>See also</em> <strong>Vendor Update</strong>.</td>
</tr>
<tr class="even">
<td>Vendor Update (VUP) (message)</td>
<td><em>IFCAP:</em> This message is sent electronically from the FMS system to all IFCAP sites to ensure that the local vendor file contains the same data as the central vendor file in Austin. This message will contain the FMS Vendor ID for the vendor and also the Alternate Address Indicator if applicable. <em>See also</em> <strong>Vendor Request.</strong></td>
</tr>
<tr class="odd">
<td>Veterans Affairs (Department of) (VA)</td>
<td>The Department of Veterans Affairs (VA) was established on March 15, 1989, succeeding the Veterans Administration. It is responsible for providing federal benefits to veterans and their dependents.</td>
</tr>
<tr class="even">
<td>Veterans Affairs Central Offices (VACO)</td>
<td>Collective term that includes the Washington, DC, “headquarters” units of the Department of <strong>Veterans Affairs</strong>, such as the <strong>Veterans Health Administration, Veterans Benefits Administration,</strong> <strong>National Cemetery Administration,</strong> etc. (<em>see</em> REDACTED</td>
</tr>
<tr class="odd">
<td>Veterans Benefits Administration (VBA)</td>
<td>Agency that manages and provides benefits and services to the veteran population through 58 VA regional offices. Some of the benefits and services provided by VBA to veterans and their dependents include compensation and pension, education, loan guaranty, and insurance.</td>
</tr>
<tr class="even">
<td>Veterans Health Administration (VHA)</td>
<td>Agency that manages the VA health care system of VA medical centers nationwide. The VHA also conducts research and education, and provides emergency medical preparedness.</td>
</tr>
<tr class="odd">
<td>Veterans Health Information Systems &amp; Technology Architecture</td>
<td>VistA was introduced in 1996. It is a rich, automated environment that supports day-to-day operations at local <strong>VA</strong> health care facilities. VistA is built on a client-server architecture, which ties together workstations and personal computers with graphical user interfaces at <strong>VHA</strong> facilities, as well as software developed by local medical facility staff. VistA also includes the links that allow commercial off-the-shelf software and products to be used with existing and future technologies. VistA does not include the Decision Support System (DSS) and other national databases that might be derived from locally generated data.</td>
</tr>
<tr class="even">
<td>VHA</td>
<td><em>See</em> <strong>Veterans Health Administration</strong></td>
</tr>
<tr class="odd">
<td>VIE</td>
<td><em>See</em> <strong>VistA Interface Engine</strong></td>
</tr>
<tr class="even">
<td>VistA</td>
<td><em>See</em> <strong>Veterans Health Information Systems &amp; Technology Architecture</strong></td>
</tr>
<tr class="odd">
<td>VistA Interface Engine (VIE)</td>
<td><p><em>Option 1:</em></p>
<p>The VIE is the mechanism by which data is transferred between <strong>DynaMed</strong> and <strong>IFCAP.</strong> In the current implementation, this is accomplished through use of the <strong>Vitria</strong> <em>BusinessWare</em> software product. VIE composes the actual <strong>HL7</strong> messages used to transfer data between <strong>IFCAP</strong> and <strong>DynaMed</strong>.</p>
<p><em>Option 2:</em></p>
<p>VIE provides routing functionality for HL7 messages between <strong>VistA</strong> and <strong>DynaMed</strong>. It is based on a <strong>middleware</strong> product called <em>BusinessWare</em>, from Vitria Technology Inc. VIE also provides the mapping between HL7 and relational tables.</p></td>
</tr>
<tr class="even">
<td>Vitria</td>
<td><p>Vitria is both a software company (Vitria Technology Inc.) and a <strong>middleware</strong> product. The DynaMed-IFCAP Interface project uses the <em>Vitria:BusinessWare</em> platform, which is the basis for the <strong>VistA Interface Engine.</strong> <em>Source:</em> <a href="http://www.vitria.com/products/platform/">http://www.vitria.com/products/platform/</a></p>
<p><em>Note:</em> References are sometimes heard to “the Vitria box,” meaning the physical computing platform on which VIE runs. Since the basis for VIE could change at any time, it’s probably best to avoid this usage. Instead, one could refer to “the VIE box.”</p></td>
</tr>
<tr class="odd">
<td>VRQ</td>
<td><em>See</em> <strong>Vendor Request</strong></td>
</tr>
<tr class="even">
<td>VUP</td>
<td><em>See</em> <strong>Vendor Update</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><a href="#G_TOC">![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/109.png)</a></td>
</tr>
</tbody>
</table>

| W                                                            |                                                                                                                                         |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Term                                                         | Definition / Discussion                                                                                                                 |
| Warehouse Clerk                                              | *IFCAP:* The person who records arrival of procured items in the warehouse, delivers the items, and records any shipping discrepancies. |
| [![](ifcap-version-5-1-dynamed-ifcap-implementation-guide/110.png)](#G_TOC) |                                                                                                                                         |

# INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1358 F-1, F-4
2138 F-1, F-23, F-29
2139 F-1, F-23, F-29
2237 v, 1-3, 1-6, 2-1, 2-2, 2-3, 2-5, 2-10, 3-1, 3-2, 3-4, 3-5, 3-6, 3-7, 3-8, 3-13, 4-15, 4-17, 5-1, 5-3, 5-7, 5-8, 5-9, 5-10, B-3, B-7, D-6, D-10, D-13, F-1, F-4, F-21
2237 Approve B-5
2237 Cancel B-5
2237 Documents 2-8
2237 Error Text Explanation D-11
2237 Returned to Service 2-7
2237 Update B-5
A&MM 4-1, 4-4, F-3
AAC F-4
About DynaMed A-1
AC F-4
Accept Acknowledgment F-2
Accommodating Use of DynaMed 2-1
Account Processing Code F-2
Accountable Officer 2-5, 4-17, F-2
Accounting Technician F-2
ACK B-4, B-5, F-2
Acknowledgment F-2
Acquisition and Materiel Management F-3
Activating 4-3
Add Options to Appropriate Menus 4-7
Adjusted/Returned Value F-3
Adjustments 3-10
Adjustments, Returns, and Corrections A-3
Admission, Discharge and Transfer F-3
ADP Security Officer F-3
ADPSO F-3
ADT F-3
AFREE Cross-Reference 4-5
Amendment F-3
Amendment and Receiving Events E-5
Amendments 3-9
American Standard Code for Information Interchange F-3
AO F-3
APC F-2, F-3
Application Acknowledgment F-4
Application Coordinator F-4
Appropriate Staff 4-3
Approve Requests F-4
Area F-4
ASCII F-3
Associated Vendors with Vendor \# 3-16
AT F-2
Audit File 3-3, 4-15, 4-17, D-4, D-6, D-7
Audit File Updates E-8
Austin Automation Center F-4
available
option 1-6
Background 1-1
Batch Number F-4
BOC F-5
Breakout Code F-5
Brother Cart F-5
Budget Object Code F-5
Bulletins 5-5
Business Rules 1-3
Cancel Customer Orders A-3
Cancel Customer Orders Requisitions A-3
Capability Details A-2
CAPC F-9
Cart F-5
Cart Level F-5
Cart Reorder Point F-5
CC F-8
CCA F-6
CCS F-8
Ceiling Transactions F-6
Classification of Request F-6
Clean Up Files 4-17
Clinger-Cohen Act F-6
Commercial Off-the-Shelf F-6
Commit Acknowledgment F-6
Common Numbering Series F-7
Connectivity 4-14
Connectivity Values 4-6
Constraints on Repetitive Item Lists 3-4
Constraints on Using 2237s 3-6
Control Point F-7
Control Point Clerk F-7
Control Point Official F-7
Control Point Official's Balance F-7
Control Point Requestor F-7
Controlling Stockroom F-7
Conversion Factor F-7
Coordinate Plans with Staff 4-1
Core Financial and Logistics System 1-1, F-8
CoreFLS F-8
Cost Center F-8
COTS F-6
CP F-7
CPC F-7
CPO F-7
CPR F-7
Creating Purchase Orders 3-8
Credit Card System F-8
Credit Charge F-8
Customer F-8
Customer Account Processing Code F-9
Customer Orders A-2
Customer Type F-9
data
read-only 1-4
Data Dictionaries 5-5
Data Entries 5-8
Data Map Record 5-12
Data Type F-9
Date Committed F-9
Date Needed By\\ Field 3-7
De-activating the Interface 4-16
Default F-9
Deficiency F-9
Delinquent Delivery Listing F-9
Delivery Order F-9
Department of Veterans Affairs F-30
Direct Delivery Patient F-9
Discount Item F-9
Display on 2237 Documents 2-8
Display on RIL 2-8
DM DOC ID 3-2
Document ID Not Set Up in Audit File D-4
Document Number F-9
Due In F-10
DUZ F-10
DUZ of Users 4-1
DynaMed F-10
DynaMed Switch 4-7
EDI F-11
EDI Vendor F-10
Electronic Data Interchange F-11
Electronic Signature F-11
Establish Subscriptions 4-9
Events That Update DynaMed 2-2
Events That Update IFCAP 2-3
Expenditure Request F-11
FCP F-12
Federal Procurement Data System F-11
Federal Tax ID F-11
Field Definitions 5-6
File 414.02 D-4
Financial Management System F-11
Financial Services Center F-11
Fiscal Quarter F-12
Fiscal Service F-12
Fiscal Updates 3-13
Fiscal Year F-12
Flow Chart: File and Field Legend E-12
Flow Charts E-1
FMS F-11
FOB F-12
FPDS F-11
Freight on Board F-12
Fringe Item F-12
FSC F-11
Functional Capabilities A-1
Fund Control Point F-12
Fund Control Point Balance Information 2-3
Fund Control Point Balance Update E-10
Fund Control Point Balances 3-13
Fund Control Points 4-1
Funds Control F-12
FY F-12
Glossary F-1
HCPCS Code F-13
Health Level 7 F-13
Healthcare Common Procedure Coding System F-13
Heartbeat F-13
help function 1-6
History 1-1
HL7 5-11, B-1, F-13
HL7 Error Codes D-1
HL7 Glossary of Terms F-1
HL7 Implementation B-1
HL7 Logical Links 5-12
HL7 Message Details C-1
HL7 Message Header B-1
HL7 Message Structure B-1
HL7 Message/Event Types B-2
HL7 Messages 5-12, D-1
HL7 Messages Sent B-3
HL7 Sample Error Messages D-3
HL7 Table 0357 D-1
HL7 Table 0533 D-2
HL7 Transmission Packaging C-1
IC F-14
ICD F-14
Icons 1-4
Identification Number F-13
Identifying DynaMed RILs 3-5
IDL F-14
IFCAP 1-1, F-14
user’s guides v
IFCAP Functionality 3-1
IFCAP Relationship 1-1
IFCAP Sequence 5-16
IM F-15
IMF F-15
Information Control, LLC F-14
Information Resources Management F-14
Integrated Funds Distribution, Control Point Activity, Accounting and Procurement F-14
Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) 1-1
Interface 1-6
Interface Activation 4-1
Interface Communications Issues 4-2
Interface Control Document F-14
Interface Definition Language F-14
Interface Requirements 1-2
Internal Sourcing F-14
Internal Voucher F-14
Inventory Adjustments A-3
Inventory Manager F-15
IRM F-14
Issue Book Form Type Not Available 2-3
Issue Books 3-10
Issues to Consider 4-16
Item Approval Messages D-10
Item Cancellation or Approval Messages D-10
Item Display with Vendor \# 4-2
Item File 3-14, 4-1, F-15
Item File Management E-9
Item History F-15
Item Master File F-15
Item Master Number F-15
Item Missing DynaMed DOC ID D-5
Item Missing from Audit File D-6
Item Numbers Less Than 100,000 2-7
Item Update Routines 4-2
IV F-14
Justification F-15
Legacy IFCAP
Manual 1-3
options v
user 1-6
Liquidation F-16
LLP F-16
Location Capacity F-16
Lower Layer Protocol F-16
M F-16
Mail Groups 4-5, 5-9
MailMan F-16
MailMan Messages 4-16
Maintenance 4-1, 4-15
Mandatory Source F-16
Mandatory Vendor F-17
Mark Options Out of Order 4-4
Master Catalog F-17
Master Catalog Item F-17
menu
user 1-6
Message F-17
Message Delimiter F-17
Message from IFCAP B-7
Message Header F-17
Message ID F-17
Message Type F-18
MID F-17
Middleware F-18
Minimal Lower Layer Protocol F-18
missing option 1-6
MLLP F-18
MLP F-18
Monitor 4-9
Mother Cart F-18
MSC Confirmation Message F-18
MSH F-17
NAK F-19
National Cemetery Administration F-19
Nature of Expense F-19
NCA F-19
Negative Acknowledgment F-19
Net Asset F-19
NOE F-19
numbering principles 1-5
Obligation F-19
Obligation (Actual) Amount F-19
Obligation Data F-19
Obligation Number F-19
Operation 1-6
option
available 1-6
missing 1-6
Options 5-9
Oracle F-20
Organization Code F-20
other IFCAP Documentation 1-4
Outstanding 2237 F-20
PAPC F-23
Partial F-20
Partial Date F-20
PAT Number F-20, F-21
PCard F-22
PCard Orders 2-5, F-22
PCard User F-22
Personal Property Management F-20
PHA F-22
PHM F-22
Picklist F-21
PO F-23
PO Error Text Explanation D-13
PO Messages D-13
PORR F-23
Posted Issue Book E-7
Posted Issue Book and Stock Transfers E-6
PPM F-20
PPM Accountable Officer F-21
PR Card F-24
PRCV D-2
PRCV Audit File Alerts 3-4, 3-7, 4-5, D-3
PRCV COTS Inventory 4-9
PRCV COTS INVENTORY 2-1, 2-5, 4-3, 4-7, 4-17
PRCV ITEM UPDATE TO DYNAMED 3-14, 4-14
PRCV Item Vendor Edits 4-5
PRCV ITEM WITH VENDOR# 4-7
PRCV VENDOR UPDATE TO DYNAMED 4-14
Preferred Vendor F-21
Preparing to Activate 4-1
Process Flow Legend E-11
Process Issue Book Orders 2-5
Processing a 2237 3-7
Processing Issue Book Transactions 4-2
Processing Receipts 3-9
Procurement and Accounting Transaction Number F-21
Program Code F-21
prompt 1-6
Prompt Payment Terms F-21
Protocols 5-10
Public Law 100-32 F-22
Purchase Card F-22
Purchase Card Coordinator F-22
Purchase Card Order 3-3
Purchase Card Order Events E-4
Purchase Card Orders 3-8, F-22
Purchase Card User F-22
Purchase History Add F-22
Purchase History Modify F-22
Purchase Order 3-2, F-23
Purchase Order Acknowledgment F-23
Purchase Order Events E-3
Purchase Order Receiving Report F-23
Purchase Order Status F-23
Purchase Orders 3-8
Purchasing Account Processing Code F-23
Purchasing Agents F-23
Putaway F-23
Putlist F-24
PV F-21
Quarterly Report F-24
question mark 1-6
read-only 1-4
Receipt of Stock A-3
Receipts 3-9
Receiving Report F-24
Reconciliation F-24
Record Checksum File 4-8
Reference Number F-24
Removed Prompts from IFCAP Options 2-5
Reorder Point F-24
Repetitive Item List 3-6, F-25
Repetitive Item Lists 3-4
Repetitive Number F-24
Replenishing Supplies 3-1
Reports 3-8
Requirements Analyst F-25
Requisition F-25
Requisition Objective F-25
Requisition to RIL Events E-2
Requisitions in IFCAP 3-4
Response to Requisition B-4
Restrictions 2-6, 2-7
Re-Use the RIL 2-5
RIL 2-8, B-5, D-10, F-25
RIL Build B-6, D-8
RIL Error Message Structure D-8
RIL Error Messages D-8
RIL Error Text Explanation D-8, D-11
RILs 3-4, 3-5
RIL's Needing Action 4-3, 4-7
RO F-25
role
user 1-6
ROP F-5, F-24
Routines 5-1
Running Balance F-25
SAPC F-27
Schedule Options 4-14
Section Request F-26
Service Balance F-26
Setup Common Number Serie 4-2
SF-49 F-26
Short Description F-26
Site Parameters F-26
SKU F-27
SLC F-27
Sort Group F-26
Special Remarks F-26
Special Terminology 1-3
Stacked Documents F-26
Standard Form 49 F-26
Standard Forms F-26
Standard Voucher F-27
Standardize the Item and Vendor Files 4-1
Station Number F-27
Stock item Transactions A-2
Stock Keeping Unit F-27
Stock Transfers E-7
Stockage List Code F-27
Stockroom Account Processing Code F-27
Stockroom Inventories A-3
Stockroom Requisitions A-2
Stockroom Transactions A-2
Stopping the Monitor 4-12
Sub-Cost Center F-27
Subscriptions 2-3, 4-12
Supply Replenishment 3-2
SV F-27
System Features A-1
System Parameter 2-1
System Parameters F-28
Tasked Job F-28
Technical Summary 5-1
Templates 5-5
Test Connectivity 4-9
Transaction Number F-28
Transmission Number F-28
Troubleshooting 4-1, 4-15
Type Code F-28
Typography 1-4
UI F-28
UM F-29
Unable to Update Audit File D-7
Unique Records 5-8
Unit of Issue F-28
Unit of Measure F-29
Unit of Purchase F-29
Unit of Purchase Conflict F-29
UOP F-29
user
Legacy IFCAP 1-6
menu 1-6
role 1-6
VA F-30
VA Form 90-2138 F-29
VA Form 90-2138-ADP F-29
VA Form 90-2139 F-29
VA Form 90-2139-ADP F-29
VACO F-30
VBA F-30
Vendor file F-30
Vendor File 3-14, 4-1
Vendor File Management E-9
Vendor ID Number F-30
Vendor Request message F-30
Vendor Update Error Messages D-15
Vendor Update Error Text Explanation D-15
Vendor Update message F-30
Vendor Update Routines 4-2
Vendor/Item File Relationship 4-1
Verify Patch Installation 4-4
Veterans Affairs Central Offices F-30
Veterans Benefits Administration F-30
Veterans Health Administration F-30
Veterans Health Information Systems & Technology Architecture 1-1, F-31
Veterans Health Information Systems & Technology Architecture (VistA) 1-1
VHA F-30
VIE F-31
VistA 1-1, F-31
VistA Interface Engine F-31
Vitria F-31
VRQ F-30
VUP F-30
Warehouse Clerk F-32
[^1]: See <http://www.va.gov/vdl/Financial_Admin.asp?appID=42>
[^2]: A hyperlink in this document is similar to those found on Internet pages, except that it usually opens another MS Office (*e.g.* Word or Excel) document. Other links, called cross-references, take you to specified points in the current document.
[^3]: Generally, “update” includes cancellation, approval, obligation of the instrument, or deletion of one or more items.
