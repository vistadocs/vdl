---
title: Drug Accountability/Inventory Interface Version 3 Technical Manual/Security Guide (Updated PSA*3*69)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: PSA
app_name: "Pharmacy: Drug Accountability"
section: CLI
app_status: active
pkg_ns: PSA
patch_ver: 3
patch_id: PSA*3
group_key: "PSA:PSA:3"
file_numbers: []
security_keys: []
menu_options: 2
description: Drug Accountability/Inventory Interface (DA) Version 3.0 provides functionality that interfaces with prime vendor invoice data. It provides Pharmacy with the capability to match National Drug Codes (NDC) in the invoice data to NDC in the DRUG file (#50). The invoice data is uploaded, processed, and
audience: 
keywords: 
  - strong
  - class
  - table
  - style
  - width
  - even
  - drug
  - contents
  - invoice
  - number
page_count: 0
word_count: 12367
section_count: 23
table_count: 15
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: October 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Drug_Accountability/psa_3_tm_r0509.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Drug_Accountability/psa_3_tm_r0509.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=87"
---

![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/001.png)

DRUG ACCOUNTABILITY/INVENTORY INTERFACE(DA)TECHNICAL MANUAL/SECURITY GUIDE

October 1997

(Revised May 2009)

Office of Enterprise Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Orientation](#orientation)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Installation](#installation)
  - [Data Flow](#data-flow)
  - [Resource Requirements](#resource-requirements)
  - [Site Parameters](#site-parameters)
  - [Hardware Requirements](#hardware-requirements)
- [Routine List](#routine-list)
- [File List](#file-list)
  - [GIP Interface Files](#gip-interface-files)
  - [Prime Vendor Interface](#prime-vendor-interface)
  - [Return Drug Credit Menu](#return-drug-credit-menu)
  - [File Descriptions](#file-descriptions)
- [Exported Options](#exported-options)
  - [Menus](#menus)
    - [GIP Interface](#gip-interface)
    - [Prime Vendor Interface](#prime-vendor-interface-1)
    - [Return Drug Credit Menu](#return-drug-credit-menu-1)
  - [Options](#options)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Software Product Security](#software-product-security)
  - [Legal Requirements](#legal-requirements)
  - [Sign-On Event](#sign-on-event)
  - [Electronic Signatures](#electronic-signatures)
  - [Security Keys used in DA](#security-keys-used-in-da)
  - [File Security](#file-security)
  - [Mail Groups](#mail-groups)
- [# Glossary](#glossary)
- [Appendix A - XTMP(“PSAPV”) Global Layout](#appendix-a-xtmppsapv-global-layout)
  - [^XTMP(“PSAPV”,CTRL#,”IN”) – Invoice data](#xtmppsapvctrlin-invoice-data)
  - [XTMP(“PSAPV”,CTRL#,”IT”,LINE ITEM#) – Line Item Data](#xtmppsapvctrlitline-item-line-item-data)
  - [XTMP(“PSAPV”,CTRL#,”IT”,LINE ITEM#, “SUP”) – Supply Line Item Data](#xtmppsapvctrlitline-item-sup-supply-line-item-data)
- [Appendix B - Invoice file with formatting errors](#appendix-b-invoice-file-with-formatting-errors)
- [# Appendix C - ASC X12 Electronic Data Interchange Draft Specifications](#appendix-c-asc-x12-electronic-data-interchange-draft-specifications)
The table below lists changes made since the initial release of this manual. Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. Either update the existing manual with the Change Pages document, or replace it with the updated manual.
> **NOTE:** The Change Pages document may include unedited pages needed for two-sided copying. Only edited pages display the patch number and revision date in the page footer.
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision Pages</strong></td>
<td><strong>Patch Number</strong></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>05/09</td>
<td><a href="#P69_v">v-vi</a>, <a href="#P69_10">10-12</a>, <a href="#return-drug-credit-menu">14-20</a>, <a href="#P69_25">25</a></td>
<td>PSA*3*69</td>
<td><p>Added menu item Return Drug Credit [PSA RETURN DRUG MENU], options, file list, and security key PSARET. Added the following routines: PSANDCUT, PSARDCBA, PSARDCBL, PSARDCIT, PSARDCRD, PSARDCRP, PSARDCRS, PSARDCU1, and PSARDCUT.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/08</td>
<td>9-12, 30</td>
<td>PSA*3*67</td>
<td><p>Added XTMP Line Item Data.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/06</td>
<td>10-12, 19-20, 24</td>
<td>PSA*3*51</td>
<td><p>Added new routine PSAOUT, new option PSA OUTDATED MEDICATIONS and updated the security keys section.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>06/03</td>
<td>All</td>
<td>PSA*3*26</td>
<td>Updated manual to current Standards. Left Appendix C as is since it is a document in itself. Added new routines and deleted PROCOMM PLUS Prime Vendor information in Appendix B and throughout the manual.</td>
</tr>
<tr class="even">
<td>02/02</td>
<td><p>iia-iib;</p>
<p>v-(vi);</p>
<p>9-20;</p>
<p>(25)-26b.</p></td>
<td>PSA*3*21</td>
<td><p>Add Revision History pages iia and iib;</p>
<p>Update Table of Contents;</p>
<p>Revise sections to add new routines related to setting up/editing a pharmacy location, selecting from multiple divisions, editing verified invoice data, and updating the Drug File,</p>
<p>Revise sections to add a new File, DA Upload (#58.812),</p>
<p>Revise sections to add new options to delete unprocessed invoices and edit verified invoices;</p>
<p>Update Software Product Security section to reflect new file and to add information on mail groups.</p>
<p>Unchanged pages included for two-sided copying as needed.</p></td>
</tr>
<tr class="odd">
<td>10/97</td>
<td></td>
<td></td>
<td>Original Released Technical Manual.</td>
</tr>
</tbody>
</table>
\<This page is intentionally left blank\>
Preface
Version 3.0 of the Drug Accountability/Inventory Interface (DA) software provides functionality to maintain a perpetual inventory of drugs. Interfacing with the Generic Inventory Package (GIP) or the prime vendors’ invoice data increments drug balances in pharmacy locations and master vaults. Pharmacy’s dispensing software packages pass dispensing data to DA V. 3.0 then decrements the drug balances in pharmacy locations. The DA V. 3.0 software package is intended for pharmacists, pharmacy technicians, and pharmacy procurement agents who are familiar with the prime vendor or GIP ordering process.
\<This page is intentionally left blank\>
Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Drug Accountability/Inventory Interface (DA) Version 3.0 provides functionality that interfaces with prime vendor invoice data. It provides Pharmacy with the capability to match National Drug Codes (NDC) in the invoice data to NDC in the DRUG file (#50). The invoice data is uploaded, processed, and verified. Version 3.0 also provides the capability to transfer drugs between pharmacy locations and tracks those transfers.

> **IMPORTANT:** Once verified (prime vendor interface) or received (GIP interface), the drug balances are incremented in the pharmacy location and/or master vault. The invoiced drug’s order unit is compared to the ORDER UNIT field (#12) in the DRUG file (#50) and the dispense units per order unit is compared to the DISPENSE UNITS PER ORDER UNIT field (#15) in the DRUG file (#50). If the order unit and dispense units per order unit are the same, the NDC (#31), price per order unit (#13), and price per dispense unit (#16) fields in the DRUG file (#50) may be updated.

The following condition must be met to update the NDC field (#31).

- If the invoice NDC is different from the NDC field (#31), the NDC field (#31) is overwritten with the invoiced NDC.

The following condition must be met to update the price per order unit field (#13) and price per dispense unit field (#16).

- If the invoiced price per order unit is different than the price per order unit field (#13), the price per order unit field (#13) is overwritten with the new prorated price per order unit. The price per dispense unit field (#16) is also overwritten with the new prorated price per dispense unit.

This technical manual provides additional information for package coordinators, supervisors, and Information Resource Management (IRM) Staff. Users who are not familiar with Veterans Health Information Systems and Technology Architecture (V*IST*A) software may also wish to refer to documentation for VA Kernel.

![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/002.png)Note: The Security Guide information has been included in this manual under the Software Product Security section.

\<This page is intentionally left blank\>

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

> Example: *DrugAccountability Menu* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them.

> Example: “DATE:” indicates a screen prompt.

- Responses in bold face indicate what the user is to type in.

> Example: If the displayed transfer information is correct, enter YES.

- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.

> Example: Press \<Tab\> to move the cursor to the next field.

> Press \<Enter\> to select the default.

- ![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/003.png)Note: Indicates especially important or helpful information.
- ![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/004.png) Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.

Example: ![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/005.png) This option is locked by the PSA ORDERS key.

- ?, ??, ??? One, two, or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.
- ^ Up Caret (arrow or a circumflex) and pressing \<Enter\> can be used to exit the current option.

  \<This page is intentionally left blank\>

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For installation of the DA Version 3.0 V*IST*A software package, please refer to the Installation Guide.

If the site will be interfacing with the prime vendor’s invoice data, contact the prime vendor to obtain their invoice data software and installation instructions.

## Data Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

GIP Interface Data Flow

![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/006.png)

  
Prime Vendor Data Flow

![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/007.png)

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 3.0 of the DA package requires, at least, the following VA software applications and commercial package.

<u>V*IST*A Software Package</u> <u>Minimum Version Required</u>

Controlled Substances (CS) 3.0 (Must be patched up to and

including Patch PSD\*3.0\*6)

Kernel 8.0

Kernel Toolkit 7.3

MailMan 7.1

VA FileMan 21.0

National Drug File (NDF) 3.16

Pharmacy Data Management (PDM) 1.0

Inpatient Medications 4.5 (Must be patched up to and including Patch PSJ\*4.5\*44)

Automatic Replenishment/Ward Stock 2.3

Outpatient Pharmacy 6.0 (Must be patched up to and including Patch PSO\*6.0\*155)

If the site will be setting up an Inpatient and/or Combined (Inpatient/Outpatient) pharmacy location, these software packages must be installed to collect unit dose and IV dispensing data.

If the site will be setting up an Outpatient and/or Combined (Inpatient/

Outpatient) pharmacy location, this software package must be installed to collect prescription data.

## Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no site parameters to be set.

## Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility must support a port-to-port connection between the V*IST*A system and the prime vendor PC system.

<u>  
</u>

\<This page is intentionally left blank\>

# Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains an alphabetized routine list and a description of each routine for DA Version 3.0.

#### Routine List and Routine Descriptions

| Routine Names | Routine Descriptions                                           |
|-------------------|--------------------------------------------------------------------|
|                   |                                                                    |
| PSABRKU1          | Upload and Process Prime Vendor Invoice Data                       |
| PSABRKU2          | Automatic processing of invoices                                   |
| PSABRKU3          | Upload and Process Prime Vendor Invoice Data - CONT'D              |
| PSABRKU4          | Upload and Process Prime Vendor Invoice Data - CONT'D              |
| PSABRKU5          | Upload and Process Prime Vendor Invoice Data - CONT'D              |
| PSABRKU6          | Upload and Process Prime Vendor Invoice Data - CONT'D              |
| PSABRKU8          | Upload and Process Prime Vendor Invoice Data Utility               |
| PSACON            | Display Connected Drug and Procurement History                     |
| PSACON1           | Display Connected Drug and Procurement History - CONT'D            |
| PSACON2;          | Display Connected Drug and Procurement History - CONT'D            |
| PSACONW           | Display Connected Drug and Procurement History - CONT'D            |
| PSACOST           | Invoice Cost Summary                                               |
| PSACREDO          | Outstanding Credits                                                |
| PSACREDR          | Credit Resolution                                                  |
| PSADA             | Pharmacy Location Lookup Utility                                   |
| PSADAI            | Drug Balances by Location                                          |
| PSADJ             | Balance Adjustments                                                |
| PSADJI            | Balance Initialization                                             |
| PSADJR            | Balance Adjustments History                                        |
| PSADRU            | Drugs Not Found in Linked Inventory                                |
| PSADRUG           | Add/edit Pharmacy Location drugs                                   |
| PSADRUGP          | Enter/Edit a Drug                                                  |
| PSAENT            | Set Up/Edit a Pharmacy Location                                    |
| PSAENTO           | Set Up/Edit a Pharmacy Location - CONT'D                           |
| PSAENVIR          | Environment Check                                                  |
| PSAGIP            | DA receiving from GIP                                              |
| PSAGIP1           | DA receiving from GIP - CONT'D                                     |
| PSAHIS            | Drug Transaction History                                           |
| PSAHIS1           | Drug Transaction History - CONT'D                                  |
| PSALEVEL          | Enter/Edit Stock and Reorder Levels                                |
| PSALEVRP          | Stock and Reorder Report                                           |
| PSALFA            | Automated DRUG/ITEM MASTER file Link by Federal Stock Number (FSN) |
| PSALFM            | Controlled Connection by FSN Match                                 |

|                                                  |                                                            |
|--------------------------------------------------|------------------------------------------------------------|
| Routine Names                                | Routine Descriptions                                   |
| PSALFS                                           | Report Potential FSN Matches                               |
| PSALNA                                           | Automated DRUG/ITEM MASTER file Link by NDC                |
| PSALND                                           | Report Potential NDC Matches                               |
| PSALNM                                           | NDC Duplicates Report (ITEM MASTER file)                   |
| PSALOC                                           | Set Up/Edit a Pharmacy Location                            |
| PSALOC1                                          | Set Up/Edit a Pharmacy Location                            |
| PSALOC2                                          | Set Up/Edit a Pharmacy Location                            |
| PSALOCO                                          | Set Up/Edit a Pharmacy Location                            |
| PSALOG                                           | Unposted Procurement History                               |
| PSALOG0                                          | Unposted Procurement History - CONT'D                      |
| PSALOG1                                          | Unposted Procurement History - CONT'D                      |
| PSALOG1H                                         | Unposted Procurement History - CONT'D                      |
| PSALOG2                                          | Post Drug Procurement History                              |
| PSALOG3                                          | Post Drug Procurement History - CONT'D                     |
| PSALOGON                                         | Logon Utility                                              |
| PSAMON                                           | Monthly Summary                                            |
| PSAMON1                                          | Monthly Summary - CONT’D                                   |
| PSANAC                                           | Populate Pharmacy Location with Inventory Items            |
| PSANDC                                           | NDC Duplicates Report                                      |
| PSANDF                                           | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSANDF1                                          | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| <span id="P69_10" class="anchor"></span>PSANDCUT | Utility for handling NDC (National Drug Code)              |
| PSAOP                                            | Outpatient Dispensing (Single Drug)                        |
| PSAOP1                                           | Outpatient Dispensing (Single Drug) & (All Drugs)          |
| PSAOP2                                           | Outpatient Dispensing (All Drugs)                          |
| PSAOP3                                           | Nightly Background Job                                     |
| PSAOP4                                           | Outpatient Dispensing (Single Drug) & (All Drugs) - CONT'D |
| PSAORDP                                          | Print Orders                                               |
| PSAORDP1                                         | Print Orders - CONT'D                                      |
| PSAORDP2                                         | Print Orders - CONT'D                                      |
| PSAOUT                                           | Outdated Medications                                       |
| PSAP67                                           | New Prime Vendor field checker/displayer                   |
| PSAPOST                                          | Post Init                                                  |
| PSAPROC                                          | Process Uploaded Prime Vendor Invoice Data                 |
| PSAPROC1                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSAPROC2                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSAPROC3                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSAPROC4                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSAPROC5                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSAPROC6                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSAPROC7                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSAPROC8                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| PSAPROC9                                         | Process Uploaded Prime Vendor Invoice Data - CONT'D        |
| Routine Names                                | Routine Descriptions                                   |
| PSAPSI                                           | IV Dispensing (Single Drug)                                |
| PSAPSI1                                          | IV Dispensing (Single Drug) & (All Drugs)                  |
| PSAPSI2                                          | IV Dispensing (All Drugs)                                  |
| PSAPSI3                                          | Nightly Background Job                                     |
| PSAPSI4                                          | IV Dispensing (Single Drug) & (All Drugs)                  |
| PSAPSI5                                          | Nightly Background Job - CONT'D                            |
| PSAPUR                                           | Nightly Background Job - CONT'D                            |
| PSAPV                                            | Processor and Verifier                                     |
| PSARDCBA                                         | Listman – Display Return Drug Batch                        |
| PSARDCBL                                         | Listman – Display Return Drug Batch List                   |
| PSARDCIT                                         | Listman – Display Return Drug Batch Item                   |
| PSARDCRD                                         | Return Drug Report (Detailed)                              |
| PSARDCRP                                         | Return Drug Report (Driver)                                |
| PSARDCRS                                         | Return Drug Report (Summary)                               |
| PSARDCU1                                         | Return Drug utility routine 2                              |
| PSARDCUT                                         | Return Drug utility routine 1                              |
| PSAREC                                           | Receiving Directly into Drug Accountability                |
| PSAREC1                                          | Receiving Directly into Drug Accountability - CONT'D       |
| PSAREORD                                         | Nightly Background Job - CONT’D                            |
| PSAREPV                                          | Invoice Review                                             |
| PSAREV                                           | Purchase Order Review                                      |
| PSAREVC                                          | Control Point Transaction Review                           |
| PSAREVD                                          | Drug Receipt History Review                                |
| PSARIN                                           | Loadable Inventory Items Report                            |
| PSARWS                                           | Collect Ward Stock Data                                    |
| PSASIG                                           | Transfer Signature Sheet                                   |
| PSATI                                            | Single Drug Match                                          |
| PSATRAN                                          | Transfer Drugs between Pharmacies                          |
| PSATRAN1                                         | Transfer Drugs between Pharmacies - CONT’D                 |
| PSAUDP                                           | Nightly Background Job - CONT'D                            |
| PSAUNI                                           | Unlinked Drugs in the ITEM MASTER file                     |
| PSAUNL                                           | Connect Unlinked DRUG/ITEM MASTER file Entries             |
| PSAUNM                                           | Report of Unlinked DRUG/ITEM MASTER file Entries           |
| PSAUP                                            | Upload and Process Prime Vendor Invoice Data               |
| PSAUP1                                           | Upload and Process Prime Vendor Invoice Data - CONT'D      |
| PSAUP2                                           | Upload and Process Prime Vendor Invoice Data - CONT'D      |
| PSAUP3                                           | Upload and Process Prime Vendor Invoice Data - CONT'D      |
| PSAUP4                                           | Upload and Process Prime Vendor Invoice Data - CONT'D      |
| PSAUP5                                           | Upload and Process Prime Vendor Invoice Data - CONT'D      |
| PSAUP6                                           | Upload and Process Prime Vendor Invoice Data - CONT'D      |
| PSAUTL                                           | GIP Utility                                                |
| PSAUTL1                                          | Prime Vendor Invoice Data Utility                          |
| PSAUTL2                                          | Upload and Process Prime Vendor Invoice Data Utility       |

|                   |                                                               |
|-------------------|---------------------------------------------------------------|
| Routine Names | Routine Descriptions                                      |
| PSAUTL3           | Upload and Process Prime Vendor Invoice Data Utility – CONT'D |
| PSAUTL4           | Verify Invoices Utility                                       |
| PSAVER            | Verify Invoices                                               |
| PSAVER1           | Verify Invoices - CONT'D                                      |
| PSAVER2           | Verify Invoices - CONT'D                                      |
| PSAVER3           | Verify Invoices - CONT'D                                      |
| PSAVER4           | Verify Invoices - CONT'D                                      |
| PSAVER5           | Verify Invoices - CONT'D                                      |
| PSAVER6           | Verify Invoices - CONT'D                                      |
| PSAVER7           | Verify Invoices - CONT'D                                      |
| PSAVER8           | Multiple Division Selection                                   |
| PSAVERA           | Change verified invoice data                                  |
| PSAVERA1          | Edit previously verified invoices                             |
| PSAVERA2          | Edit previously verified invoices \#2                         |
| PSAVERA3          | Record Transaction & Update DRUG file                         |
| PSAVIN            | Report of Inventory items' link to DRUG file                  |
| PSAVIN1           | Physical Inventory Balance Review                             |
| PSAVIN2           | Compares Prices (DA/GIP)                                      |
| PSAVINC           | Update Prices                                                 |
| PSAWARD           | Set Up/Edit a Pharmacy Location                               |

# File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package requires 23 files in addition to those of the Kernel and other files to which it points. Information about all files, including these can be obtained by using the VA FileMan to generate a list of file attributes.

## GIP Interface Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Numbers | File Names                        |
|------------------|---------------------------------------|
|                  |                                       |
| 42               | WARD LOCATION                         |
| 50               | DRUG                                  |
| 50.8             | IV STATS                              |
| 51.5             | ORDER UNIT                            |
| 52               | PRESCRIPTION                          |
| 52.6             | IV ADDITIVES                          |
| 52.7             | IV SOLUTIONS                          |
| 58.1             | PHARMACY AOU STOCK                    |
| 58.5             | AR/WS STATS                           |
| 58.8             | DRUG ACCOUNTABILITY STATS             |
| 58.81            | DRUG ACCOUNTABILITY TRANSACTION       |
| 58.812           | DA UPLOAD                             |
| 58.84            | DRUG ACCOUNTABILITY TRANSACTION TYPE  |
| 59               | OUTPATIENT SITE                       |
| 59.4             | INPATIENT SITE                        |
| 59.7             | PHARMACY SYSTEM                       |
| 410              | CONTROL POINT ACTIVITY                |
| 441              | ITEM MASTER                           |
| 442              | PROCUREMENT & ACCOUNTING TRANSACTIONS |
| 445              | GENERIC INVENTORY                     |
| 445.2            | INVENTORY TRANSACTION                 |

## Prime Vendor Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Numbers | File Names                       |
|------------------|--------------------------------------|
|                  |                                      |
| 42               | WARD LOCATION                        |
| 50               | DRUG                                 |
| 50.8             | IV STATS                             |
| 51.5             | ORDER UNIT                           |
| 52               | PRESCRIPTION                         |
| 52.6             | IV ADDITIVES                         |
| 52.7             | IV SOLUTIONS                         |
| 58.1             | PHARMACY AOU STOCK                   |
| 58.5             | AR/WS STATS                          |
| 58.8             | DRUG ACCOUNTABILITY STATS            |
| 58.81            | DRUG ACCOUNTABILITY TRANSACTION      |
| 58.812           | DA UPLOAD                            |
| 58.84            | DRUG ACCOUNTABILITY TRANSACTION TYPE |
| 58.811           | DRUG ACCOUNTABILITY ORDER FILE       |
| 59               | OUTPATIENT SITE                      |
| 59.4             | INPATIENT SITE                       |
| 59.7             | PHARMACY SYSTEM                      |
| 8980             | KERMIT HOLDING                       |

## Return Drug Credit Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Numbers | File Names                       |
|------------------|--------------------------------------|
| 50               | DRUG                                 |
| 51.5             | ORDER UNIT                           |
| 58.35            | RETURN DRUG                          |
| 58.36            | RETURN DRUG CONTRACTOR/MFR           |
| 58.8             | DRUG ACCOUNTABILITY STATS            |
| 58.81            | DRUG ACCOUNTABILITY TRANSACTION      |
| 58.84            | DRUG ACCOUNTABILITY TRANSACTION TYPE |
| 59               | OUTPATIENT SITE                      |
| 200              | NEW PERSON                           |

## File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

58.35 RETURN DRUG FILE

This file contains a record for all the drugs that are returned to a contractor and/or manufacturer for a credit or to be destroyed. It includes drug items that have been credited, denied, or are still pending.

58.36 RETURN DRUG CONTRACTOR/MFR FILE

This file contains contractors and/or manufacturers to whom drugs are returned for credit or destruction. This file is pointed to by the CONTRACTOR/MANUFACTURER field (#4) of the RETURN BATCH sub-field (#58.351) of the RETURN DRUG (#58.35) file.

58.8 DRUG ACCOUNTABILITY STATS FILE

This file contains data associated with the Pharmacy Drug Accountability Stats location. Entries in this file may be edited but not deleted. Entries in this file should NOT be edited directly using VA FileMan.

This file is designed to be shared between the DA V. 3.0 module and the Controlled Substances V. 3.0 module of the Pharmacy software. The Controlled Substances V. 3.0 module will recognize a location as a Narcotic Area of Use (NAOU). The menu *Inactivate NAOU* \[PSD INACTIVATE NAOU\] option is used to inactivate NAOUs no longer in use. The menu *Inactivate NAOU Stock Drug* \[PSD INACTIVATE NAOU STOCK DRUG\] option is used to inactivate drugs no longer stocked within that NAOU.

<u>INPUT TEMPLATE(S):</u> <u>PRINT TEMPLATE(S):</u>

PSAENT PSAINV

PSAGIP

58.81 DRUG ACCOUNTABILITY TRANSACTION FILE

This file contains the data associated with drug accountability transactions. This file design is to share between the DA V. 3.0 module and the Controlled Substances V. 3.0 module. Entries in this file should NOT be edited directly for Controlled Substances V. 3.0 use. The CS V. 3.0 module contains all appropriate checks for this file’s use.

812. DA UPLOAD

This file contains Supply Items and Order Units used in matching uploaded Prime Vendor invoice data.

The user inputs the name of a supply item and the item's corresponding Vendor Stock Number (VSN). When an item is uploaded from the vendor, the DA V. 3.0 software attempts to identify the item by the NDC. If a match cannot be found, the entries in this file will be checked.

By storing the supply items, the user does not have to identify the item on the invoice as a supply item each time it is uploaded.

The Prime Vendor ships drugs in a variety of order unit sizes. In some instances, the order unit on an invoiced item does not match the order unit in the facility's files. When this occurs the user has to perform a manual match on the item.

By entering the order unit sent by the Prime Vendor to the order unit in V*IST*A, the matching can be performed automatically during the upload process.

58.84 DRUG ACCOUNTABILITY TRANSACTION TYPE FILE

This file contains the standard types of transactions utilized in the pharmacy DA V. 3.0 package. This file is shared between the DA V. 3.0 module and the Controlled Substances V. 3.0 module. This is a standard file exported by both the Controlled Substances V. 3.0 and DA V. 3.0 modules and additional entries should not be added. Existing data will be merged.

![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/008.png)Note: Data comes with this file and overwrites the existing data.

58.811 DRUG ACCOUNTABILITY ORDER FILE

This file contains prime vendor pharmacy orders with all adjustments. The prime vendor invoice data is uploaded from the prime vendor. All data is processed and verified before it increments the drug balances in DA pharmacy locations.

None XTMP(“PSAPV”)

This temporary file holds the uploaded invoice data that has not been processed. When the data is processed, it is moved to the DRUG ACCOUNTABILITY ORDER file (#58.811). If data in this file is not processed or more data is not added to this file for 16 days, a MailMan message is sent to holders of the PSA ORDERS key. The message states that if the invoices are not processed in four calendar days or if more invoices are not uploaded in four calendar days, the invoices in the file will be deleted. If the data remains unprocessed and data is not added to the file for five more days, all data in the file is deleted. (See Appendix A for the field layout.)

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package exports the menus. The main menu is *DrugAccountability Menu* \[PSA DRUG ACCOUNTABILITY MENU\] option.

Example: Drug Accountability Menu

1 GIP Interface Menu ...

2 Prime Vendor Interface ...

3 Return Drug Credit Menu ...

### GIP Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the site will only interface with the Generic Inventory Package (GIP), the *GIP Interface Menu* \[PSA GIP INTERFACE MENU\] option must be distributed to Chief of Pharmacy or a designee. It contains the following menus.

1 Connection Menu (DRUG file/ITEM MASTER file) ...

2 Pharmacy Location Maintenance Menu ...

3 Receipts Menu ...

4 Dispensing Menu ...

5 Maintenance Reports Menu ...

### Prime Vendor Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the site will interface with the prime vendor invoice data, the *GIP Interface Menu* \[PSA GIP INTERFACE MENU\] option and *Prime Vendor Interface menu* \[PSA PRIME VENDOR INTERFACE\] option must be distributed. Most drugs will be purchased from the prime vendor. For the drugs that cannot be purchased from the prime vendor, it is necessary to interface with the Generic Inventory Package to receive them into pharmacy location and/or master vault. Therefore, the main menu of *DrugAccountability Menu* \[PSA DRUG ACCOUNTABILITY MENU\] option must be distributed to Chief of Pharmacy, or a designee, plus the purchasing agent in Pharmacy.

### Return Drug Credit Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Return Drug Credit Menu* \[PSA RET DRG MENU\] option is accessible for users holding the PSORPH (pharmacist key) security key. Other users must be assigned the PSORET security key before they can access this menu.

1 Batch Work List \[PSA RET DRG BATCH WORKLIST\]

2 Batch Complete List \[PSA RET DRG BAT COMPLETE LIST\]

3 View/Update Batch \[PSA RET DRG VIEW/UPDATE BATCH\]

4 Return Drug Credit Report \[PSA RET DRG REPORT\]

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package exports the following options.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>OPTION</strong></th>
<th><strong>MENU TEXT</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSA ACTIVE DRUGS/ITEM FILE</td>
<td>Active, Unlinked Drugs in the ITEM MASTER file</td>
</tr>
<tr class="even">
<td>PSA BALANCE ADJUSTMENTS</td>
<td><p>Balance Adjustments</p>
<p>Locked by the PSAMGR key</p></td>
</tr>
<tr class="odd">
<td>PSA BALANCE ADJUSTMENTS REPORT</td>
<td>Balance Adjustments History</td>
</tr>
<tr class="even">
<td>PSA BALANCE INITIALIZE</td>
<td>Balance Initialization</td>
</tr>
<tr class="odd">
<td>PSA COMPARISON REPORT</td>
<td>DRUG file/ITEM MASTER file Comparison Report</td>
</tr>
<tr class="even">
<td>PSA CONNECTION MENU</td>
<td>Connection Menu (DRUG file/ITEM MASTER file)</td>
</tr>
<tr class="odd">
<td>PSA CP TRANSACTION REVIEW</td>
<td>Control Point Transaction Review</td>
</tr>
<tr class="even">
<td>PSA CREDIT RESOLUTION</td>
<td><p>Credit Resolution</p>
<p>Locked by the PSAMGR key</p></td>
</tr>
<tr class="odd">
<td>PSA DELETE INVOICES</td>
<td>Delete Un-processed Invoices</td>
</tr>
<tr class="even">
<td>PSA DISPENSING MENU</td>
<td>Dispensing Menu</td>
</tr>
<tr class="odd">
<td>PSA DISPLAY CONNECTED DRUG</td>
<td>Display Connected Drug and Procurement History</td>
</tr>
<tr class="even">
<td>PSA DISPLAY LOCATION</td>
<td>Drug Balances by Location</td>
</tr>
<tr class="odd">
<td>PSA DRUG ACCOUNTABILITY MENU</td>
<td>Drug Accountability Menu</td>
</tr>
<tr class="even">
<td>PSA DRUG DISPLAY</td>
<td>Drug Transaction History</td>
</tr>
<tr class="odd">
<td>PSA DRUG ENTER/EDIT</td>
<td>Enter/Edit a Drug</td>
</tr>
<tr class="even">
<td>PSA DRUG HISTORY</td>
<td>Drug Receipt History Review</td>
</tr>
<tr class="odd">
<td>PSA DRUG INQUIRE</td>
<td>Inquire/Compare DRUG file/ITEM MASTER file</td>
</tr>
<tr class="even">
<td>PSA DRUGS NOT IN INVENTORY</td>
<td>Drugs Not Found in Linked Inventory</td>
</tr>
<tr class="odd">
<td>PSA EDIT VERIFIED INVOICE</td>
<td>Edit Verified Invoices</td>
</tr>
<tr class="even">
<td>PSA FSN AUTO LOOP</td>
<td>Automated DRUG/ITEM MASTER file Link by FSN</td>
</tr>
<tr class="odd">
<td>PSA FSN CONTROL LOOP</td>
<td>Controlled Connection by FSN Match</td>
</tr>
<tr class="even">
<td>PSA FSN MENU</td>
<td>FSN Menu</td>
</tr>
<tr class="odd">
<td>PSA FSN REPORT</td>
<td>Report Potential FSN Matches</td>
</tr>
<tr class="even">
<td>PSA GIP COMPARE</td>
<td>Physical Inventory Balance Review</td>
</tr>
<tr class="odd">
<td>PSA GIP CONT BAL UPDATE</td>
<td>Update Prices</td>
</tr>
<tr class="even">
<td>PSA GIP DISCREPANCIES</td>
<td>Compare Prices (DA/GIP)</td>
</tr>
<tr class="odd">
<td>PSA GIP INTERFACE MENU</td>
<td>GIP Interface Menu</td>
</tr>
<tr class="even">
<td>PSA GIP LINK REPORT</td>
<td>Report of Inventory Items' Link to DRUG file</td>
</tr>
<tr class="odd">
<td>PSA GIP LOCATION MENU</td>
<td>Pharmacy Location Maintenance Menu</td>
</tr>
<tr class="even">
<td>PSA GIP MAINTENANCE RPT MENU</td>
<td>Maintenance Reports Menu</td>
</tr>
<tr class="odd">
<td>PSA GIP MENU</td>
<td>Inventory Interface</td>
</tr>
<tr class="even">
<td>PSA GIP POPULATE</td>
<td>Populate Pharmacy Location with Inventory Items</td>
</tr>
<tr class="odd">
<td>PSA GIP REPORT</td>
<td>Loadable Inventory Items Report</td>
</tr>
<tr class="even">
<td>PSA GUI UPLOAD</td>
<td>UPLOAD UTILITY</td>
</tr>
<tr class="odd">
<td>PSA INVOICE COST SUMMARY</td>
<td>Invoice Cost Summary</td>
</tr>
<tr class="even">
<td>PSA INVOICE REVIEW</td>
<td>Invoice Review</td>
</tr>
<tr class="odd">
<td>PSA IV ALL DRUGS</td>
<td>IV Dispensing (All Drugs)</td>
</tr>
<tr class="even">
<td>PSA IV ALL LOCATIONS</td>
<td>All Location Dispense/Purge</td>
</tr>
<tr class="odd">
<td>PSA IV SINGLE</td>
<td>IV Dispensing (Single Drug)</td>
</tr>
<tr class="even">
<td>PSA LOCATION EDIT</td>
<td>Set Up/Edit a Pharmacy Location</td>
</tr>
<tr class="odd">
<td>PSA MONTHLY SUMMARY</td>
<td>Monthly Summary</td>
</tr>
<tr class="even">
<td>PSA MSG RECIPIENTS</td>
<td>Setup Mail Message Recipients</td>
</tr>
<tr class="odd">
<td>PSA NDC AUTO LOOP</td>
<td>Automated DRUG/ITEM MASTER file Link by NDC</td>
</tr>
<tr class="even">
<td>PSA NDC CONTROL LOOP</td>
<td>Controlled Connection by NDC Match</td>
</tr>
<tr class="odd">
<td>PSA NDC DUPLICATE REPORT</td>
<td>NDC Duplicates Report (ITEM MASTER file)</td>
</tr>
<tr class="even">
<td>PSA NDC MENU</td>
<td>NDC Menu</td>
</tr>
<tr class="odd">
<td>PSA NDC REPORT</td>
<td>Report Potential NDC Matches</td>
</tr>
<tr class="even">
<td>PSA OP ALL DRUGS</td>
<td>Outpatient Dispensing (All Drugs)</td>
</tr>
<tr class="odd">
<td>PSA OP SINGLE</td>
<td>Outpatient Dispensing (Single Drug)</td>
</tr>
<tr class="even">
<td>PSA ORDERS ALERT</td>
<td>Prime Vendor Processing/Verifying Alerts at Signon</td>
</tr>
<tr class="odd">
<td>PSA ORDERS MENU</td>
<td><p>Orders Menu</p>
<p>Locked by the PSA ORDERS key</p></td>
</tr>
<tr class="even">
<td>PSA OUTDATED MEDICATIONS</td>
<td>Outdated Medications</td>
</tr>
<tr class="odd">
<td>PSA OUTSTANDING CREDITS</td>
<td>Outstanding Credits</td>
</tr>
<tr class="even">
<td>PSA POSTED DRUG REPORT</td>
<td>Posted Drug Procurement History</td>
</tr>
<tr class="odd">
<td>PSA PRIME VENDOR INTERFACE</td>
<td>Prime Vendor Interface Menu</td>
</tr>
<tr class="even">
<td>PSA PRINT ORDERS</td>
<td><p>Print Orders</p>
<p>Locked by the PSA ORDERS key</p></td>
</tr>
<tr class="odd">
<td>PSA PROCESS PRIME VENDOR DATA</td>
<td><p>Process Uploaded Prime Vendor Invoice Data</p>
<p>Locked by the PSA ORDERS key</p></td>
</tr>
<tr class="even">
<td>PSA PROCESSOR AND VERIFIER</td>
<td><p>Processor and Verifier</p>
<p>Locked by the PSA ORDERS key</p></td>
</tr>
<tr class="odd">
<td>PSA PURCHASE ORDER REVIEW</td>
<td>Purchase Order Review</td>
</tr>
<tr class="even">
<td>PSA PV DRUG ENTER/EDIT</td>
<td>Enter/Edit a Drug</td>
</tr>
<tr class="odd">
<td>PSA PV LOCATION MENU</td>
<td>Pharmacy Location Maintenance Menu</td>
</tr>
<tr class="even">
<td>PSA PV MAINTENANCE RPT MENU</td>
<td>Maintenance Reports Menu</td>
</tr>
<tr class="odd">
<td>PSA RECEIPT MENU</td>
<td>Receiving Menu</td>
</tr>
<tr class="even">
<td>PSA RECEIPTS MENU</td>
<td>Receipts Menu</td>
</tr>
<tr class="odd">
<td>PSA RECEIVING</td>
<td>Receiving Directly into Drug Accountability</td>
</tr>
<tr class="even">
<td>PSA RET DRG BAT COMPLETE LIST</td>
<td>Batch Complete List</td>
</tr>
<tr class="odd">
<td>PSA RET DRG BATCH WORKLIST</td>
<td>Batch Work List</td>
</tr>
<tr class="even">
<td>PSA RET DRG MENU</td>
<td>Return Drug Credit Menu</td>
</tr>
<tr class="odd">
<td>PSA RET DRG REPORT</td>
<td>Return Drug Credit Report</td>
</tr>
<tr class="even">
<td>PSA RET DRG VIEW/UPDATE BATCH</td>
<td>View/Update Batch</td>
</tr>
<tr class="odd">
<td>PSA SINGLE DRUG MATCH</td>
<td>Single Drug Match</td>
</tr>
<tr class="even">
<td>PSA STOCK &amp; REORDER LEVEL RPT</td>
<td>Stock and Reorder Level</td>
</tr>
<tr class="odd">
<td>PSA STOCK AND REORDER LEVELS</td>
<td>Enter/Edit Stock and Reorder Levels</td>
</tr>
<tr class="even">
<td>PSA TRANSFER DRUGS</td>
<td><p>Transfer Drugs Between Pharmacies</p>
<p>Locked by the PSAMGR key</p></td>
</tr>
<tr class="odd">
<td>PSA TRANSFER SIGNATURE SHEET</td>
<td>Transfer Signature Sheet</td>
</tr>
<tr class="even">
<td>PSA UNLINKED LOOP</td>
<td>Connect Unlinked DRUG/ITEM MASTER file Entries</td>
</tr>
<tr class="odd">
<td>PSA UNLINKED REPORT</td>
<td>Report of Unlinked DRUG/ITEM MASTER file Entries</td>
</tr>
<tr class="even">
<td>PSA UNPOST PROCUREMENT HISTORY</td>
<td>Unposted Procurement History</td>
</tr>
<tr class="odd">
<td>PSA UPLOAD PRIME VENDOR DATA</td>
<td><p>Upload and Process Prime Vendor Invoice Data</p>
<p>Locked by the PSA ORDERS key</p></td>
</tr>
<tr class="even">
<td>PSA VERIFY INVOICES</td>
<td><p>Verify Invoices</p>
<p>Locked by the PSA ORDERS key</p></td>
</tr>
</tbody>
</table>

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At present, the DA V. 3.0 package does not provide for archiving of its data.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DRUG ACCOUNTABILITY TRANSACTION file (#58.81) and the DRUG ACCOUNTABILITY ORDER file (#58.811) are purged by the same nightly job of *All LocationDispense/Purge*, \[PSA IV ALL LOCATIONS\] option. All transactions greater than 120 days in the DRUG ACCOUNTABILITY TRANSACTION file (#58.81) are purged. The orders in the DRUG ACCOUNTABILITY ORDER file (#58.811) are purged if they are greater than the number of days in the DRUG ACCOUNTABILITY STATS file’s (#58.8) DAYS TO KEEP INVOICE DATA field (#35) or greater than 120 days if the field is blank. This job should be scheduled to run during non-peak hours to lessen the impact on system operations. Once scheduled, this job will reschedule to run again every 24 hours.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None of the DA V. 3.0 package routines are designed for calling outside of the package.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DA V. 3.0 has IA agreements with Automatic Replenishment/Ward Stock, Controlled Substances, Inpatient Medications, Outpatient Pharmacy, National Drug File, Pharmacy Data Management, and Kernel. For complete information regarding the IA agreements for DA V. 3.0, please refer to the *DBA* \[DBA\] menu option on FORUM and then the *Integration Agreements* option.

> \<This page is intentionally left blank\>

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package does not require a Standards and Conventions Committee (SACC) agreement.

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package does not contain any package-wide variables.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements.

## Sign-On Event

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Prime Vendor Processing/Verifying Alerts at Signon 

\[PSA ORDERS ALERT\]

The *Prime Vendor Processing/Verifying Alerts at Signon* \[PSA ORDERS ALERT\] option checks to see if there are any invoices that need to be processed or verified by a user that holds the PSA ORDERS key. If so, a message is displayed when the user signs on the system stating the number of invoices the user needs to process and/or verify.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic signatures may be established in two ways. The IRM service can enter a code for the user. Alternately, the *Electronic Signature code Edit* \[XUSESIG\] option is provided by Kernel for the user to accomplish this task. In Kernel V. 8, the *Electronic Signature code Edit* \[XUSESIG\] option has been tied to the *User’s Toolbox* \[XUSERTOOLS\] submenu, for easy access by all users.

## Security Keys used in DA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The security keys listed below control the access necessary to operate the DA V. 3.0 software.

<u>GIP Interface</u>

The following keys should be assigned to the Chief of Pharmacy or a designee.

> PSAMGR This security key locks the *Balance Adjustments* \[PSA BALANCE ADJUSTMENTS\] option*, Credit Resolution* \[PSA CREDIT RESOLUTION\] option*,* and the *Transfer Drugs Between Pharmacies* \[PSA TRANSFER DRUGS\] option.

<u>Prime Vendor Interface</u>

The following keys should be assigned to the Chief of Pharmacy or a designee.

> PSAMGR This security key locks the *Balance Adjustments* \[PSA BALANCE ADJUSTMENTS\] option, *Credit Resolution* \[PSA CREDIT RESOLUTION\] option*, Delete Unprocessed Invoices* \[PSA DELETE INVOICES\] option, *Edit Verified Invoices* \[PSA EDIT VERIFIED INVOICE\] option, *Outdated Medications* \[PSA OUTDATED MEDICATIONS\] option, *Setup Mail Message Recipients* \[PSA MSG RECIPIENTS\] option, and the *Transfer Drugs Between Pharmacies* \[PSA TRANSFER DRUGS\] option.

> PSA ORDERS This security key locks the *Orders Menu* \[PSA ORDERS MENU\] option, *Credit Resolution* \[PSA CREDIT RESOLUTION\] option, *Print Orders* \[PSA PRINT ORDERS\] option, *Process Uploaded Prime Vendor Invoice Data* \[PSA PROCESS PRIME VENDOR DATA\] option, and *Verify Invoices* \[PSA VERIFY INVOICES\] option*.*

This key should be assigned to the Pharmacy purchasing agent.

> PSA ORDERS This security key locks the *Orders Menu* \[PSA ORDERS MENU\] option, *Credit Resolution* \[PSA CREDIT RESOLUTION\] option, *Print Orders* \[PSA PRINT ORDERS\] option, *Process Uploaded Prime Vendor Invoice Data* \[PSA PROCESS PRIME VENDOR DATA\] option, and *Verify Invoices* \[PSA VERIFY INVOICES\] option.

<span id="P69_25" class="anchor"></span><u>Return Drug Credit Menu</u>

At least one of the following keys should be assigned to the Chief of Pharmacy or a designee.

> PSARET, PSORPH These security keys lock the *Batch Work List* \[PSA RET DRG BATCH WORK LIST\] option*, Batch Complete List* \[PSA RET DRG BATCH COMPLETE LIST\] option*,View/Update Batch* \[PSA RET DRG VIEW/UPDATE BATCH\] option, and the *Return Drug Credit Report* \[PSA RET DRG REPORT\] option.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package requires 23 files in addition to those of the Kernel and other files to which it points, for example, the PATIENT file (#2). Information about all files, including these can be obtained by using the VA FileMan to generate a list of file attributes.

<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 45%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File Numbers</td>
<td><h4 id="file-names" class="unnumbered">File Names</h4></td>
<td><strong>DD</strong></td>
<td><strong>RD</strong></td>
<td><strong>WR</strong></td>
<td><strong>DEL</strong></td>
<td><h4 id="laygo" class="unnumbered">LAYGO</h4></td>
</tr>
<tr class="even">
<td><blockquote>
<p>58.8</p>
</blockquote></td>
<td>DRUG ACCOUNTABILITY STATS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>58.81</p>
</blockquote></td>
<td>DRUG ACCOUNTABILITY TRANSACTION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>58.811</p>
</blockquote></td>
<td>DRUG ACCOUNTABILITY ORDER</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>58.812</p>
</blockquote></td>
<td>DA UPLOAD</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>58.84</p>
</blockquote></td>
<td>DRUG ACCOUNTABILITY TRANSACTION TYPE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td>DRUG</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DA V. 3.0 uses two mail groups for transferring information to the user.

<u>PSA NDC UPDATES</u>

This mail group is accessed to determine the personnel who should be notified by the DA V. 3.0 software when an item’s price or NDC has changed.

<u>PSA REORDER LEVEL</u>

This mail group contains the personnel who are to receive the message generated for the drugs whose stock level has fallen below the reorder level. Previously, anyone holding the PSA ORDERS key would receive this message.

\<This page is intentionally left blank\>

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DA Acronym for Drug Accountability/Inventory Interface V. 3.0.

FSN Acronym for Federal Stock Number.

GIP Acronym for Generic Inventory Package that automatically generates purchase orders and manages inventory.

Master Vault An inventory location created to store a select group of controlled substances and track their balance and activity.

Pharmacy Location An inventory location created to store a select group or all of non-controlled drugs to track their balance and activity.

Prime Vendor A vendor who is on contract with the VA to be the main supplier of drugs.

Process Invoices To process invoices, the prime vendor’s invoice data is matched to the data in V*IST*A and the data is validated. Matching is accomplished by comparing the line item data on the invoice with its entry in the DRUG file (#50). Validating is accomplished by confirming the quantity received verses the quantity invoiced. Anyone holding the PSA ORDERS key can process the invoice.

V*IST*A Acronym for Veterans Health Information Systems and Technology Architecture.

XTMP file The XTMP file is a temporary file that holds the uploaded invoices that have not been processed. The invoice data remains in this file up to 21 days.

\<This page is intentionally left blank\>

# Appendix A - XTMP(“PSAPV”) Global Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ^XTMP(“PSAPV”,CTRL#,”IN”) – Invoice data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Piece 1 Invoice Date

> Piece 2 Invoice Number

> Piece 3 Order Date

> Piece 4 Order Number

> Piece 5 Delivery Date Requested

> Piece 6 Invoice’s Delivery Date

> Piece 7 Pharmacy Location IEN – File \#58.8 IEN

> Piece 8 Invoice Status (“OK”= Uploaded no errors “P”= Processed, “”=Uploaded with errors)

> Piece 9 “CS” if at least 1 item is a CS

> Piece 10 “ALL CS” if all items are CS

> Piece 11 Date Drugs Received

> Piece 12 Master Vault IEN -- File \#58.8 IEN

> Piece 13 “SUP” if all supplies items on invoice

## XTMP(“PSAPV”,CTRL#,”IT”,LINE ITEM#) – Line Item Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Piece 1 Quantity

> Piece 2 Unit of Measure ~ FILE \#51.5 IEN

Piece 3 Unit Price

> Piece 4 NDC ~ \# with same NDC ~ Different Vendor Stock Number (VSN) ~ “1” if overwrite

Piece 5 VSN ~ \# with same VSN ~ Different NDC

> Piece 6 File \#50 IEN

> Piece 7 File \#50 SYNONYM IEN ~ New SYNONYM?

> Piece 8 Adjusted Quantity

> Piece 9 Adjusted Quantity DUZ

> Piece 10 Adjusted Quantity Date

> Piece 11 Adjusted Quantity Reason

> Piece 12 Adjusted File \#51.5 IEN

> Piece 13 Adjusted Order Unit DUZ

> Piece 14 Adjusted Order Unit Date

> Piece 15 Adjusted File \#50 IEN

> Piece 16 Adjusted File \#50 IEN DUZ

> Piece 17 Adjusted File \#50 IEN Date

> Piece 18 Line Item Status ( “”=Uploaded With Errors, “OK”= Uploaded Without Errors, “P” = Processed)

> Piece 19 “CS” if item is a CS

> Piece 20 Dispense Units per Order Unit

> Piece 21 Reorder Level

> Piece 22 Invoice’s. Price per Order Unit Correct?

> Piece 23 File Price per Order Unit

> Piece 24 Price per Order Unit DUZ

> Piece 25 Price per Order Unit Date

> Piece 26 Universal Product Code (UPC) ~ \# with same UPC ~ Different UPC

> Piece 27 Stock Level

> Piece 28 Generic Description

> Piece 29 Item Description

> Piece 30 Inner Pack Unit of Measure Code (i.e. \# pills in bottle)

> Piece 31 Package Size (i.e. \# bottles in sell unit)

## XTMP(“PSAPV”,CTRL#,”IT”,LINE ITEM#, “SUP”) – Supply Line Item Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Piece 1 DUZ

> Piece 2 Date

> Piece 3 “SUPPLY ITEM” or Supply item description

# Appendix B - Invoice file with formatting errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data is sent from the prime vendor in the Accredited Standards Committee (ASC) X12 release 3.2 formatting for an invoice transaction (set \#810). The formatting specifications document is *ASC X12 Electronic Data Interchange Draft Specifications for Prime Vendor Interface with Decentralized Hospital Computer Program*. It is part of the contract between the VA and the prime vendor. The DA V. 3.0 software checks the INVOICE.DAT formatting to assure formatting rules have been followed. There are many rules that may cause an error.

Many different errors may be listed under the “ERROR MESSAGES:” section on the screen.

In the following table, the reason the error message was displayed and the actions needed to fix the error are listed.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Problem Explanation</td>
<td>Action</td>
</tr>
<tr class="even">
<td>INVOICE.DAT contains data out of sequence, missing data, and/or incorrect data.</td>
<td><p>1. DO NOT upload more data until this problem is resolved.</p>
<p>2. Record or screen print the errors.</p>
<p>3. Call the prime vendor and report all errors.</p>
<p>4. Instruct the prime vendor to create a new corrected INVOICE.DAT file.</p>
<p>5. Delete INVOICE.DAT and INVCRC.DAT from the PCs root directory.</p>
<p>6. When the corrected data is ready, retrieve the invoice data from the prime vendor again.</p>
<p>7. Upload the new invoice data.</p></td>
</tr>
</tbody>
</table>

In the following table, the reason the error message was displayed and the action needed to fix the error are listed.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Problem Explanation</td>
<td>Action</td>
</tr>
<tr class="even">
<td>The data element or segment terminator in INVOICE.DAT is null. They can never be null.</td>
<td><p>1. DO NOT upload more data until this problem is resolved.</p>
<p>2. Call the prime vendor and report the error.</p>
<p>3. Instruct the prime vendor to create a new corrected INVOICE.DAT file.</p>
<p>4. Delete INVOICE.DAT and INVCRC.DAT from the root directory on Pharmacy’s prime vendor PC.</p>
<p>5. When the corrected data is ready, retrieve the invoice data from the prime vendor again.</p>
<p>6. Select the <em>Upload and Process Prime Vendor</em> <em>Invoice Data</em> [PSA UPLOAD PRIME VENDOR DATA] option again to upload the new invoice data.</p></td>
</tr>
</tbody>
</table>

The software looks at the uploaded unprocessed and processed invoices to see if the incoming invoices have already been received. If so, the invoice number, invoice date, order number, order date, and invoice status is displayed.

There are no valid invoices to process.

|                                                                                                                          |             |
|--------------------------------------------------------------------------------------------------------------------------|-------------|
| Problem Explanation                                                                                                      | Action      |
| All of the invoices that were just uploaded were previously uploaded and/or processed. There are no invoices to process. | Do nothing. |

# # Appendix C - ASC X12 Electronic Data Interchange Draft Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<This page is intentionally left blank\>

![](drug-accountability-inventory-interface-version-3-technical-manual-security-guid/009.png)

ASC X12Electronic Data InterchangeDraft Specificationsfor Prime Vendor Interfacewith Decentralized Hospital Computer Program(DHCP)May 1995

Department of Veteran Affairs

Information Systems Center

Birmingham, Alabama

Table of Contents

1\. Purpose 1

2\. Overview 1

2.1 Statement of Intent 1

2.2 Scope and Audience 1

3\. General Specifications 2

3.1 Segment Requirement Designators 2

3.2 Data Element 2

> A. Data Element Types 2

> B. Data Element Length 2

3.3 Data Element Descriptions 3

> Table 1: Interchange Control Header (ISA) 3

> Table 2: Functional Group Header (GS) 5

> Table 3: Transaction Set Header (ST). 6

> Table 4: Beginning Segment for Invoice (BIG) 7

> Table 5: Reference Numbers (REF) 8

> Table 6: Name (N1) 9

> Table 7: Additional Name Information (N2) 9

> Table 8: Address Information (N3) 10

> Table 9: Geographic Location (N4) 10

> Table 10: Terms of Sale/Deferred Terms of Sale (ITD) -- Optional segment 11

> Table 11: Date/Time Reference (DTM) 12

> Table 12: Baseline Item Data (Invoice) (IT1) 13

> Table 13: Transaction Totals (CTT) 15

> Table 14: Transaction Set Trailer (SE) 16

> Table 15: Functional Group Trailer (GE) 16

> Table 16: Interchange Control Trailer (IEA) 17

3.4 Implementation and Control Structure 18

> A. Implementation. 18

> B. Control Structure 18

> C. Segment Layout 19

3.5 Transaction Set 810 Examples 20

> Example 1: Template of a Transaction Set 20

> Example 2: Mock Transaction Set 21

ASC X12, Electronic Data InterchangePrime Vendor Interface Specifications1. Purpose

This document specifies an interface to the Decentralized Hospital Computer Program

(DHCP) based on the ASC X12 Protocol for Electronic Data Interchange (EDI). It is the

intent that this interface form the basis for creating export files compatible with the

DHCP Prime Vendor Interface. Outlined are the segments and data elements which

will be used by all prime vendors to export Invoice data to such an interface. The

segments and data elements which are used from the 810 transaction set will still be

in strict accordance with the ASC X12 Standard as set forth in the Draft Version 3

Release 2. It is the responsibility of the Department of Veteran Affairs, Birmingham

Information Systems Center (ISC) to update these guidelines for the 810 transaction

set as it pertains to the prime vendor. The following information is provided as a

specific guide, however, the vendor shall refer to ASC X12 Version 3 Release 2

documentation for details concerning the general rules and standards of the ASC X12

810 transaction set.

2. Overview*2.1 Statement of Intent  
*

Birmingham Information Systems Center (ISC) plans to implement a generic interface

to DHCP for prime vendors exporting invoice files to be used within DHCP. The

vendor will continue to provide the normal paper invoices and related

documents as agreed upon prior to this interface. The file format will adhere to the

ASC X12 Standard, Draft Version 3 Release 2 and the guidelines as set forth in this

document. This form of EDI seems to be prevalent within the health care industry and

the method for exchange of information will be compatible in the future should the

Department of Veterans Affairs decide to implement interactive EDI.

*2.2 Scope and Audience*

This document describes the file format for electronic invoicing data as exported by

prime vendors. It is intended for use by vendors offering proposals concerning prime

vendor contracts and provides guidelines on the specific data and data format

required for a successful interface with DHCP.

3. General Specifications*3.1 Segment Requirement Designators*

> M = Required by the ASC X12 Version 3 Release 2 Standard or as a part of the

> Prime Vendor Interface specifications.

> R = Required by DHCP

> O = Optional

*3.2 Data Element*

A. Data Element Types

> AN = String containing letters, digits, spaces, and/or special characters

> DT = Date

> ID = Identifier

> N = Numeric

> R = Decimal

> TM = Time

B. Data Element Length

> The Data Element length is the range, minimum to maximum, of the number of

> character positions available to represent the data element.

*3.3 Data Element Descriptions*

Table 1: Interchange Control Header

> Sample: ISA^00^ ^00^ ^ZZ^ 999999 ^ZZ^588 ^950214^1005^U^00200^900456789^0^P^\>~ Name and Description Requirement

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>ISA01</td>
<td>I01.</td>
<td><p><strong>Authorization Information Qualifier</strong></p>
<p>This qualifier identifies the type of information in the</p>
<p>Authorization information.</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td><p>00 - No Authorization Information</p>
<p>Present</p></td>
</tr>
<tr class="even">
<td>ISA02</td>
<td>I02</td>
<td><p><strong>Authorization Information</strong></p>
<p>This information is used for additional identification or</p>
<p>authorization of the sender or the data in the interchange.</p></td>
<td>M</td>
<td>AN</td>
<td>10/10</td>
<td>Leave blank</td>
</tr>
<tr class="odd">
<td>ISA03</td>
<td>I03</td>
<td><p><strong>Security Information Qualifier</strong></p>
<p>This qualifier is used for identifying the type of information in</p>
<p>the security information</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td>00 - No Security Information Present</td>
</tr>
<tr class="even">
<td>ISA04</td>
<td>I04</td>
<td><p><strong>Security Information</strong></p>
<p>This is used for identifying the security information about the</p>
<p>sender of the data in the interchange.</p></td>
<td>M</td>
<td>AN</td>
<td>10/10</td>
<td>Leave blank</td>
</tr>
<tr class="odd">
<td>ISA05</td>
<td>I05</td>
<td><p><strong>Interchange ID Qualifier</strong></p>
<p>This qualifier indicates the system (or method) of code</p>
<p>structure used to designate the sender or receiver ID element</p>
<p>that is being qualified.</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td>ZZ - Mutually Defined</td>
</tr>
<tr class="even">
<td>ISA06</td>
<td>I06</td>
<td><p><strong>Interchange Sender ID</strong></p>
<p>This is the identification code of the sender.</p></td>
<td>M</td>
<td>AN</td>
<td>15/15</td>
<td><p>Dunn &amp; Bradstreet number or</p>
<p>vendor telephone number</p></td>
</tr>
<tr class="odd">
<td>ISA07</td>
<td>I05</td>
<td><p><strong>Interchange ID Qualifier</strong></p>
<p>This qualifier indicates the system (or method) of code</p>
<p>structure used to designate the sender or receiver ID element</p>
<p>that is being qualified.</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td>ZZ - Mutually Defined</td>
</tr>
<tr class="even">
<td>ISA08</td>
<td>I07</td>
<td><p><strong>Interchange Receiver ID</strong></p>
<p>This is the identification code of the receiver of the data.</p></td>
<td>M</td>
<td>AN</td>
<td>15/15</td>
<td>588 or Customer Account Number</td>
</tr>
<tr class="odd">
<td>ISA09</td>
<td>I08</td>
<td><p><strong>Interchange Date</strong></p>
<p>This is the date in YYMMDD format</p></td>
<td>M</td>
<td>DT</td>
<td>6/6</td>
<td></td>
</tr>
</tbody>
</table>

Table 1: Interchange Control Header - Continued

Reference Data ElementDesignator No. Name and Description Requirement

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>ISA10</td>
<td>I09</td>
<td><p><strong>Interchange Time</strong></p>
<p>Time is expressed in 24-hour clock time (HHMMSS). The</p>
<p>time range is 000000 through 235959.</p></td>
<td>M</td>
<td>TM</td>
<td>4/4</td>
<td></td>
</tr>
<tr class="even">
<td>ISA11</td>
<td>I10</td>
<td><p><strong>Interchange Control ID</strong></p>
<p>This code identifies the agency responsible for the control</p>
<p>standard used by the message.</p></td>
<td>M</td>
<td>ID</td>
<td>1/1</td>
<td><p>U - U.S. EDI Community of ASC</p>
<p>X12, TDCC, &amp; UCS</p></td>
</tr>
<tr class="odd">
<td>ISA12</td>
<td>I11</td>
<td><p><strong>Interchange Version Number</strong></p>
<p>This is the version number of the interchange control</p>
<p>segments.</p></td>
<td>M</td>
<td>TM</td>
<td>5/5</td>
<td><p>00200 - Standard Issued as ASNI</p>
<p>X12.5 - 1987</p></td>
</tr>
<tr class="even">
<td>ISA13</td>
<td>I12</td>
<td><p><strong>Interchange Control Number</strong></p>
<p>This number uniquely identifies the interchange data to the</p>
<p>sender. Note: This is the same number as in the IEA02 data</p>
<p>element.</p></td>
<td>M</td>
<td>N</td>
<td>9/9</td>
<td></td>
</tr>
<tr class="odd">
<td>ISA14</td>
<td>I13</td>
<td><p><strong>Acknowledgment Requested</strong></p>
<p>This is sent by the sender to request an interchange</p>
<p>acknowledgment.</p></td>
<td>M</td>
<td>ID</td>
<td>1/1</td>
<td>0 - No acknowledgment requested</td>
</tr>
<tr class="even">
<td>ISA15</td>
<td>I14</td>
<td><p><strong>Test Indicator</strong></p>
<p>This indicates whether data enclosed by this interchange</p>
<p>envelope is test or production.</p></td>
<td>M</td>
<td>ID</td>
<td>1/1</td>
<td>P - Production</td>
</tr>
<tr class="odd">
<td>ISA16</td>
<td>I15</td>
<td><p><strong>Sub-element Separator</strong></p>
<p>Reserved for future expansion in separating data element</p>
<p>subgroups. It must be different from the data element</p>
<p>separator<strong>.</strong></p></td>
<td>M</td>
<td>AN</td>
<td>1/1</td>
<td></td>
</tr>
</tbody>
</table>

Table 2: Functional Group Header

Sample: GS^IN^999999^588^950214^1005^012345678^X^003020~

Description Requirement

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>GS501</td>
<td>479</td>
<td><p><strong>Functional ID Code</strong></p>
<p>This code identifies a group of application related</p>
<p>transaction sets.</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td>IN - Invoice</td>
</tr>
<tr class="even">
<td>GS02</td>
<td>142</td>
<td><p><strong>Application Sender’s Code</strong></p>
<p>This code identifies the party sending the transmission. The</p>
<p>codes are agreed to by the trading partners.</p></td>
<td>M</td>
<td>AN</td>
<td>2/15</td>
<td><p>Dunn &amp; Bradstreet number or</p>
<p>vendor telephone number</p></td>
</tr>
<tr class="odd">
<td>GS03</td>
<td>124</td>
<td><p><strong>Application Receiver’s Code</strong></p>
<p>This code identifies the party receiving the transmission.</p>
<p>The codes are agreed to by the trading partners.</p></td>
<td>M</td>
<td>AN</td>
<td>2/15</td>
<td>588 or Customer Account Number</td>
</tr>
<tr class="even">
<td>GS04</td>
<td>373</td>
<td><p><strong>Date</strong></p>
<p>The date is in YYMMDD format.</p></td>
<td>M</td>
<td>DT</td>
<td>6/6</td>
<td></td>
</tr>
<tr class="odd">
<td>GS05</td>
<td>337</td>
<td><p><strong>Time</strong></p>
<p>Time is expressed in 24-hour clock time ( HHMMSS). The</p>
<p>time range is 000000 through 235959.</p></td>
<td>M</td>
<td>TM</td>
<td>4/6</td>
<td></td>
</tr>
<tr class="even">
<td>GS06</td>
<td>28</td>
<td><p><strong>Group Control Number</strong></p>
<p>This is an assigned number that is initiated and maintained</p>
<p>by the sender. . Note: This is the same Group Control</p>
<p>Number as in the GE102 data element.</p></td>
<td>M</td>
<td>N</td>
<td>1/9</td>
<td></td>
</tr>
<tr class="odd">
<td>GS07</td>
<td>455</td>
<td><p><strong>Responsible Agency Code</strong></p>
<p>This is used with data element GS08 to identify the issuer of</p>
<p>the standard.</p></td>
<td>M</td>
<td>ID</td>
<td>1/2</td>
<td><p>X - Accredited Standards</p>
<p>Committee X12</p></td>
</tr>
<tr class="even">
<td>GS08</td>
<td>480</td>
<td><p><strong>Version/Release/Industry Identifier Code</strong></p>
<p>This indicates the version, release, subrelease, and industry</p>
<p>identifier (including GS and GE segments) of the EDI</p>
<p>standard being used.</p></td>
<td>M</td>
<td>AN</td>
<td>1/12</td>
<td><p>003020 - Draft Standards</p>
<p>Approved by ASC X12 though</p>
<p>June 1991.</p></td>
</tr>
</tbody>
</table>

Table 3: Transaction Set Header (ST)

Sample: ST^810^000000022~

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>ST01</td>
<td>143</td>
<td><p><strong>Transaction Set ID Code</strong></p>
<p>This code is a unique identification of a transaction set.</p></td>
<td>M</td>
<td>ID</td>
<td>3/3</td>
<td>810 - X12.2 Invoice</td>
</tr>
<tr class="even">
<td>ST02</td>
<td>329</td>
<td><p><strong>Transaction Set Control Number</strong></p>
<p>The control number is assigned by the originator for the</p>
<p>transaction set. The entry a four-digit number with leading</p>
<p>zeros beginning with 0001 at the start of a new entry. It</p>
<p>increments by one (+1) for every transaction set exported on</p>
<p>that business day. Note: This is the same control number</p>
<p>as in the SE02 data element</p></td>
<td>M</td>
<td>AN</td>
<td>4/9</td>
<td></td>
</tr>
</tbody>
</table>

Type Length  
Table 4: Beginning Segment for Invoice (BIG)

Sample: BIG^950214^201^950214^P2O01~

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>BIG01</td>
<td>245</td>
<td><p><strong>Invoice Date</strong></p>
<p>This is the invoice issue date.</p></td>
<td>M</td>
<td>DT</td>
<td>6/6</td>
<td></td>
</tr>
<tr class="even">
<td>BIG02</td>
<td>76</td>
<td><p><strong>Invoice Number</strong></p>
<p>The number is the identifying number assigned by issuer.</p></td>
<td>M</td>
<td>AN</td>
<td>1/22</td>
<td></td>
</tr>
<tr class="odd">
<td>BIG03</td>
<td>323</td>
<td><p><strong>Purchase Order Date</strong></p>
<p>This date is assigned by the Department of Veterans Affairs.</p></td>
<td>R</td>
<td>DT</td>
<td>6/6</td>
<td></td>
</tr>
<tr class="even">
<td>BIG04</td>
<td>324</td>
<td><p><strong>Purchase Order Number</strong></p>
<p>This is the identifying purchase order number as assigned</p>
<p>by the Department of Veterans Affairs .</p></td>
<td>R</td>
<td>AN</td>
<td>1/22</td>
<td></td>
</tr>
<tr class="odd">
<td><p>BIG05 thru</p>
<p>BIG07</p></td>
<td></td>
<td>not used</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 5: Reference Numbers (REF)

> Sample: REF^CR^23201~

> REF^TJ^102030~

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>REF01</td>
<td>128</td>
<td><p><strong>Reference Number Qualifier</strong></p>
<p>The code qualifies the reference number.</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td><p>CR - Customer Reference</p>
<p>Number</p>
<p>TJ - Federal Taxpayer’s</p>
<p>Identification Number</p></td>
</tr>
<tr class="even">
<td>REF02</td>
<td>127</td>
<td><p><strong>Reference Number</strong></p>
<p>If the Reference Number Qualifier REF01 is <strong>CR</strong>, enter the</p>
<p>customer account number. If the Reference Number</p>
<p>Qualifier is <strong>TJ</strong>, enter the federal taxpayer’s identification</p>
<p>number.</p></td>
<td>R</td>
<td>AN</td>
<td>1/30</td>
<td></td>
</tr>
<tr class="odd">
<td>REF03</td>
<td></td>
<td>not used</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 6: Name (N1)

Sample: N1^BY^VA MEDICIAL CENTER^21^RA1000C00~

N1^DS^DRUGS DISTRIBUTOR INC.^21^KA1000R00~

N1^ST^VA MEDICAL CENTER^21^JR1000P00~

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>N101</td>
<td>98</td>
<td><p><strong>Entity Identifier Code</strong></p>
<p>This identifies an organizational entity or a physical location.</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td><p>BY - Buying Party (purchaser)</p>
<p>DS - Distributor</p>
<p>ST - Ship To</p></td>
</tr>
<tr class="even">
<td>N102</td>
<td>93</td>
<td><p><strong>Name</strong></p>
<p>This is a free-form name.</p></td>
<td>R</td>
<td>AN</td>
<td>1/35</td>
<td></td>
</tr>
<tr class="odd">
<td>N103</td>
<td>66</td>
<td><p><strong>Identification Code Qualifier</strong></p>
<p>This designates the system/method of code structure used</p>
<p>for Identification Code (67).</p></td>
<td>R</td>
<td>ID</td>
<td>1/2</td>
<td><p>21 - Health Care Industry ID</p>
<p>Number</p></td>
</tr>
<tr class="even">
<td>N104</td>
<td>67</td>
<td><p><strong>Identification Code</strong></p>
<p>This code identifies the party (as indicated in data element</p>
<p>N103)</p></td>
<td>R</td>
<td>ID</td>
<td>2/17</td>
<td><p>Health Industry Number (HIN) of</p>
<p>the Buying Party (BY), Distributor</p>
<p>(DS), and Ship To (ST)</p></td>
</tr>
</tbody>
</table>

Table 7: Additional Name Information (N2) -- This segment is optional if N3 contains data.

Sample: N2^DEPARTMENT OF VETERANS AFFAIRS~

> N2^DEPARTMENT OF VETERANS AFFAIRS^~

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>N201</td>
<td>93</td>
<td><p><strong>Name</strong></p>
<p>This is a continuation of the free-form name in N201.</p></td>
<td>R</td>
<td>AN</td>
<td>1/35</td>
<td></td>
</tr>
<tr class="even">
<td>N202</td>
<td>93</td>
<td><p><strong>Name</strong></p>
<p>This is a continuation of the free-form name in N201.</p></td>
<td>O</td>
<td>AN</td>
<td>1/35</td>
<td></td>
</tr>
</tbody>
</table>

Table 8: Address Information (N3) -- This segment is optional if N2 contains data.

Sample: N3^123 VETERANS BLVD.~

> N3^456 DRUG LANE~

> N3^123 VETERANS BLVD.^RECEIVING DEPT.~

Reference Data Element

|                |         |                          |                            |          |            |          |
|----------------|---------|--------------------------|----------------------------|----------|------------|----------|
| Reference  |         | Data Element         |                            |          |            |          |
| Designator | No. | Name and Description | Requirement Designator | Type | Length | Code |
| N301           | 166     | Address Information  | M                          | AN       | 1/35       |          |
| N302           | 166     | Address Information  | O                          | AN       | 1/35       |          |

Table 9: Geographic Location (N4)

Sample: N4^LOUISVILLE^KY^40202~

> N4^LEXINGTON^KY^40601~

> N4^LOUISVILLE^KY^40202~

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>N401</td>
<td>19</td>
<td><p><strong>City Name</strong></p>
<p>This is free-form text for the city name.</p></td>
<td>M</td>
<td>AN</td>
<td>2/19</td>
<td></td>
</tr>
<tr class="even">
<td>N402</td>
<td>156</td>
<td><p><strong>State or Province Code</strong></p>
<p>This is the standard U.S. two letter state abbreviation.</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td></td>
</tr>
<tr class="odd">
<td>N403</td>
<td>116</td>
<td><p><strong>Postal Code</strong></p>
<p>This code defines international postal.</p>
<p>Note: The U.S. zip code is either 5 digits or 5 digits + 4</p>
<p>digits separated by a dash (e.g., 231434595)</p></td>
<td>M</td>
<td>ID</td>
<td>4/9</td>
<td></td>
</tr>
<tr class="even">
<td>N404-N406</td>
<td></td>
<td>not used</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 10: Terms of Sale/Deferred Terms of Sale (ITD) -- Optional segment.

Sample: ITD^14^^^950301^15^950302^16^34.67~

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>ITD01</td>
<td>336</td>
<td><p><strong>Terms Type Code</strong></p>
<p>This identifies the type of payment terms.</p></td>
<td>O</td>
<td>ID</td>
<td>2/2</td>
<td>14 - Previously Agreed Upon</td>
</tr>
<tr class="even">
<td>ITD02</td>
<td></td>
<td>not used</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ITD03</td>
<td>338</td>
<td><p><strong>Terms Discount %</strong></p>
<p>This is the terms of the discount percentage, expressed as a</p>
<p>percent, available to the purchaser if an invoice is paid on or</p>
<p>before the Terms Discount Due Date.</p></td>
<td>O</td>
<td>R</td>
<td>1/6</td>
<td></td>
</tr>
<tr class="even">
<td>ITD04</td>
<td>370</td>
<td><p><strong>Terms Discount Due Date</strong></p>
<p>This is the date payment is due if the discount is to be</p>
<p>earned. The date is in YYMMDD format.</p></td>
<td>O</td>
<td>DT</td>
<td>6/6</td>
<td></td>
</tr>
<tr class="odd">
<td>ITD05</td>
<td>351</td>
<td><p><strong>Terms Discount Days Due</strong></p>
<p>This is the number of days in the terms discount period by</p>
<p>which payment is due if the terms discount is earned.</p></td>
<td>O</td>
<td>N</td>
<td>1/3</td>
<td></td>
</tr>
<tr class="even">
<td>ITD06</td>
<td>446</td>
<td><p><strong>Terms Net Due Date</strong></p>
<p>This is the date when the total invoice amount becomes due.</p></td>
<td>O</td>
<td>DT</td>
<td>6/6</td>
<td></td>
</tr>
<tr class="odd">
<td>ITD07</td>
<td>386</td>
<td><p><strong>Terms Net Days</strong></p>
<p>This is the number of days until the total invoice amount is</p>
<p>due (discount is not applicable).</p></td>
<td>O</td>
<td>N</td>
<td>1/3</td>
<td></td>
</tr>
<tr class="even">
<td>ITD08</td>
<td>362</td>
<td><p><strong>Terms Discount Amount</strong></p>
<p>This is the total amount of the terms discount.</p></td>
<td>O</td>
<td>N</td>
<td>1/10</td>
<td></td>
</tr>
<tr class="odd">
<td><p>ITD09 thru</p>
<p>ITD15</p></td>
<td></td>
<td>not used</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 11: Date/Time Reference ( DTM)

Sample: DTM^002^950210~

> DTM^035^950212~

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>DTM01</td>
<td>374</td>
<td><p><strong>Date/Time Qualifier</strong></p>
<p>This specifies the type of date and/or time.</p></td>
<td>M</td>
<td>ID</td>
<td>3/3</td>
<td><p>002 - Delivery Requested</p>
<p>035 – Delivered</p></td>
</tr>
<tr class="even">
<td>DTM02</td>
<td>373</td>
<td><p><strong>Date</strong></p>
<p>This is in YYMMDD format.</p></td>
<td>R</td>
<td>DT</td>
<td>6/6</td>
<td></td>
</tr>
<tr class="odd">
<td><p>DTM03 &amp;</p>
<p>DTM05</p></td>
<td></td>
<td>not used</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 12: Baseline Item Data (Invoice) (IT1)

Sample: IT1^1^12^CC^9.32^DS^ND^00032227780^VN^46789~

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>IT101</td>
<td>350</td>
<td><p><strong>Assigned Identification</strong></p>
<p>The ID consists of alphanumeric characters assigned for</p>
<p>differentiation within a transaction set. Note: This data</p>
<p>element contains the line item number in order of</p>
<p>appearance on the invoice. The format is positive numbers</p>
<p>with no decimal places.</p></td>
<td>R</td>
<td>AN</td>
<td>1/11</td>
<td></td>
</tr>
<tr class="even">
<td>IT102</td>
<td>358</td>
<td><p><strong>Quantity Invoiced</strong></p>
<p>The quantity is the number of units involved.</p></td>
<td>M</td>
<td>R</td>
<td>1/10</td>
<td></td>
</tr>
<tr class="odd">
<td>IT103</td>
<td>355</td>
<td><p><strong>Unit of Measure Code</strong></p>
<p>This code identifies the basic unit of measure as follows:</p>
<p>AM Ampoule JR Jar</p>
<p>BG Bag KG Kilogram</p>
<p>BI Bar LB Pound</p>
<p>BO Bottle ME Milligram</p>
<p>BX Box ML Milliliter</p>
<p>CC Cubic Centimeter OZ Ounce</p>
<p>KA Cake PK Package</p>
<p>CN Can PH Pack (PAK)</p>
<p>CH Container PT Pint</p>
<p>CA Case QT Quart</p>
<p>CT Carton RA Rack</p>
<p>DI Dispenser RL Roll</p>
<p>DR Drum ST Set</p>
<p>EA Each TY Tray</p>
<p>GA Gallon TB Tube</p>
<p>GR Gram VI Vial</p></td>
<td>M</td>
<td>ID</td>
<td>2/2</td>
<td><p>See the data element’s</p>
<p>description.</p></td>
</tr>
<tr class="even">
<td>IT104</td>
<td>212</td>
<td><p><strong>Unit Price</strong></p>
<p>This is the price per unit of product.</p></td>
<td>M</td>
<td>R</td>
<td>1/14</td>
<td></td>
</tr>
</tbody>
</table>

Table 12: Baseline Item Data (Invoice) (IT1) - Continued

Reference Data Element

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>IT105</td>
<td>639</td>
<td><p><strong>Basic Unit Price Code</strong></p>
<p>This identifies the type of unit price for an item.</p></td>
<td>R</td>
<td>ID</td>
<td>2/2</td>
<td>DS - Discount</td>
</tr>
<tr class="even">
<td>IT106</td>
<td>235</td>
<td><p><strong>Product/Service ID Qualifier</strong></p>
<p>This identifies the type or source of the descriptive number</p>
<p>used in the Product/Service ID (IT107).</p></td>
<td>R</td>
<td>ID</td>
<td>2/2</td>
<td>ND - National Drug Code (NDC)</td>
</tr>
<tr class="odd">
<td>IT107</td>
<td>234</td>
<td><p><strong>Product/Service ID</strong></p>
<p>This is an identifying number for a product or service as</p>
<p>indicated by IT106. Enter the product’s national drug code.</p></td>
<td>R</td>
<td>AN</td>
<td>12/12</td>
<td></td>
</tr>
<tr class="even">
<td>IT108</td>
<td>235</td>
<td><p><strong>Product/Service ID Qualifier</strong></p>
<p>This code identifies the type or source of the descriptive</p>
<p>number used in the Product/Service ID (IT109).</p></td>
<td>R</td>
<td>ID</td>
<td>2/2</td>
<td>VN - Vendor’s Item Number</td>
</tr>
<tr class="odd">
<td>IT109</td>
<td>234</td>
<td><p><strong>Product/Service ID</strong></p>
<p>This is an identifying number for a product or service as</p>
<p>indicated by IT108. Enter the vendor’s item number.</p></td>
<td>R</td>
<td>AN</td>
<td>1/30</td>
<td></td>
</tr>
<tr class="even">
<td>IT110</td>
<td>235</td>
<td><p><strong>Product/Service ID Qualifier</strong></p>
<p>This identifies the type or source of the descriptive number</p>
<p>used in the Product/Service ID (IT111) for medical supplies.</p></td>
<td>R</td>
<td>ID</td>
<td>2/2</td>
<td><p>UP - UPC Consumer Package</p>
<p>Code</p></td>
</tr>
<tr class="odd">
<td>IT111</td>
<td>234</td>
<td><p><strong>Product/Service ID</strong></p>
<p>This is an identifying number for a product or service as</p>
<p>indicated by IT110. Enter the product’s consumer package</p>
<p>code for medical supplies.</p></td>
<td>R</td>
<td>AN</td>
<td>1/30</td>
<td></td>
</tr>
<tr class="even">
<td><p>IT112 thru</p>
<p>IT125</p></td>
<td></td>
<td>not used</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 13: Transaction Totals (CTT)

Sample: CTT^2^^^^^^CLOSED~

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>CTT01</td>
<td>354</td>
<td><p><strong>Number of Line Items</strong></p>
<p>This is the total number of IT1 line items in the transaction</p>
<p>set.</p></td>
<td>M</td>
<td>N</td>
<td>1/6</td>
<td></td>
</tr>
<tr class="even">
<td><p>CTT02 thru</p>
<p>CTT06</p></td>
<td></td>
<td>not used</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CTT07</td>
<td>352</td>
<td><p><strong>Description</strong></p>
<p>This description is the purchase order status. If all items on</p>
<p>the purchase order have been shipped, enter the word</p>
<p><strong>Closed</strong>. If items on the purchase order are outstanding,</p>
<p>enter the word <strong>Partial</strong>.</p></td>
<td>R</td>
<td>AN</td>
<td>1/80</td>
<td><p>Closed</p>
<p>Partial</p></td>
</tr>
</tbody>
</table>

Table 14: Transaction Set Trailer (SE)

Sample: SE^23^000000022~

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>SE01</td>
<td>96</td>
<td><p><strong>Number of Included Segments</strong></p>
<p>This is the total number of segments in the transaction set</p>
<p>including ST and SE segments.</p></td>
<td>M</td>
<td>N0</td>
<td>1/6</td>
<td></td>
</tr>
<tr class="even">
<td>SE02</td>
<td>329</td>
<td><p><strong>Transaction Set Control Number</strong></p>
<p>The control number is assigned by the originator for the</p>
<p>transaction set.</p>
<p>Note: This is the same control number as in the ST02 data</p>
<p>element.</p></td>
<td>M</td>
<td>AN</td>
<td>4/9</td>
<td></td>
</tr>
</tbody>
</table>

Table 15: Functional Group Trailer

Sample: GE^1^012345678~

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>GE01</td>
<td>97</td>
<td><p><strong>Number of Transaction Sets Included</strong></p>
<p>This is the total number of transaction sets included in the</p>
<p>functional group or interchange (transmission) group</p>
<p>terminated by the trailer containing this element. There is</p>
<p>only one transaction set of 810.</p></td>
<td>M</td>
<td>ID</td>
<td>1/6</td>
<td>1</td>
</tr>
<tr class="even">
<td>GE02</td>
<td>28</td>
<td><p><strong>Group Control Number</strong></p>
<p>This is the assigned number that is initiated and maintained</p>
<p>by the sender. Note: This is the same Group Control</p>
<p>Number as in the GS06 data element.</p></td>
<td>M</td>
<td>No</td>
<td>1/9</td>
<td></td>
</tr>
</tbody>
</table>

Length Code

Table 16: Interchange Control Trailer

Sample: IEA^1^900456789~

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Reference</strong></td>
<td colspan="5"><strong>Data Element</strong></td>
</tr>
<tr class="even">
<td><strong>Designator</strong></td>
<td><strong>No.</strong></td>
<td><strong>Name and Description</strong></td>
<td><strong>Requirement Designator</strong></td>
<td><strong>Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>Code</strong></td>
</tr>
<tr class="odd">
<td>IEA01</td>
<td>I16</td>
<td><p><strong>Number of Included Functional Groups</strong></p>
<p>This is the number of functional groups included in a</p>
<p>transmission. There is only one transaction type.</p></td>
<td>M</td>
<td>N</td>
<td>1/5</td>
<td>1</td>
</tr>
<tr class="even">
<td>IEA02</td>
<td>I12</td>
<td><p><strong>Interchange Control Number</strong></p>
<p>This uniquely identifies the interchange data to the sender.</p>
<p>Note: This is the same number as in the ISA13 data</p>
<p>element.</p></td>
<td>M</td>
<td>N</td>
<td>9/9</td>
<td></td>
</tr>
</tbody>
</table>

*3.4 Implementation and Control Structure*

A. Implementation

The vendor will provide the export file as described in this document. This

export file should be available to DHCP, in the user's personal computer

operating system, no later than 7:00 A.M. (VAMC site local time) of the

scheduled delivery day of the confirmed invoice transaction. This will allow for

the information to be processed into DHCP in a timely manner. This file will be

located in the Root Directory (i.e., C:\\ and will be named INVOICE.DAT. If

more than one invoice is to be exported for the same business day or if the file

already exists from previous exports, subsequent transaction sets will be

appended to the INVOICE.DAT file. A file containing the Cyclical Redundancy

Check (CRC) value of the export file (INVOICE.DAT) will also be exported as

outlined below. This file will also be in the Root Directory on the user's PC.

The CRC value will be recalculated and a new .CRC file will be created in place

of the previous one every time a new transaction set is appended to the

INVOICE.DAT file. It will be named with the same 8 character name as the

export file and have an extension of .CRC (i.e., INVOICE.CRC). The following is

the format for the CRC file:

INVOICE.DAT^2043^CRC~

Where INVOICE.DAT is the export file name and 2043 is the CRC value. This

file <u>will not</u> contain any other data whatsoever.

> **NOTE:** This does not preclude the vendor from providing the normal paper

invoices and related documents as agreed upon prior to this interface.

B. Control Structure

The INVOICE.CRC file will use the caret (^) as the data element delimiter and

the tilde (~) as the segment line terminator followed by a carriage return.

In the INVOICE.DAT file, the data element delimiter and segment line

terminator are defined in the ISA segment. Segments do not have to be

terminated by a carriage return. The transaction set should look like the

sample on page 21. Segment lines cannot exceed 245 characters each. All

other rules of ASC X12 Draft Version 3 Release 2 apply.

C. Segment Layout

ISA \<--------------------------------------------------------------------

GS \<---------------------------------------------- \|

ST \<--------------------------- \| \|

BIG \| \| \|

REF \| \| \|

N1 \| \| \|

N2 \| \| \|

N3 \| I \| G \|

N4 \| N \| R \| I

ITD \| V \| O \| N

DTM \| O \| U \| T

IT1 \<-- \| I \| P \| E

... \| line items \| C \| \| R

IT1 \<-- \| E \| O \| C

CTT \| \| F \| H

SE \<--------------------------- \| \| A

ST \<--------------------------- \| I \| N

BIG \| \| N \| G

REF \| I \| V \| E

N1 \| N \| O \|

N2 \| V \| I \| D

N3 \| O \| C \| A

N4 \| I \| E \| T

ITD \| C \| S \| A

DTM \| E \| \|

IT1 \<-- \| \| \|

... \| line items \| \| \|

IT1 \<-- \| \| \|

CTT \| \| \|

SE \<--------------------------- \| \|

GE \<---------------------------------------------- \|

IEA \<--------------------------------------------------------------------

*  
3.5 Transaction Set 810 Examples*

Electronic Invoice Transaction Set 810

(As Used for the Prime Vendor Interface)

The Prime Vendor sends one electronic invoice (INVOICE NUM) to a VA facility’s

pharmacy. The pharmacy is using the Tax Identification Number to uniquely

identify the vendor, the product's National Drug Code (NDC) to cross-reference

with the vendor's product item number, and the UPC Consumer Code to

uniquely identify a medical supply. Data Element values in quotes (i.e., "PO

NUM") are symbolic in nature and are not intended as the literal representation

of valid data as in Example 1. Example 2 is a sample of what actual data might

look like.

Example 1: Template of a Transaction Set

> ISA^00^ ^00^ ^ZZ^"DUNN & BRADSTREET#"^ZZ^588 ^950214^

> 1005^U^00200^”INTERCHANGE CONTROL \#”^0^P^\>~

> GS^IN^"DUNN & BRADSTREET#"^588^950214^1005^”GROUP CONTROL \#”^X^003020~

> ST^810^"TRANACTION SET CONTROL \#"~

> BIG^950214^"INVOICE#"^950214^"PURCHASE ORDER#"~

> REF^CR^"CONSUMER REFERENCE \#"~

> REF^TJ^"VENDOR'S FEDERAL TAX ID#"~

> N1^BY^"BUYING PARTY NAME"^21^"HEALTH INDUSTRY ID#"~

> N2^"BUYING PARTY NAME CONT."^"BUYING PARTY NAME CONT."~

> N3^"ADDRESS INFO"^"ADDRESS INFO"~

> N4^"CITY NAME"^"STATE CODE"^"ZIP CODE"~

> N1^DS^"DISTRIBUTOR NAME"^21^"HEALTH INDUSTRY ID#"~

> N2^"DISTRIBUTOR NAME CONT."^"DISTRIBUTOR NAME CONT."~

> N3^"ADDRESS INFO"^"ADDRESS INFO"~

> N4^"CITY NAME"^"STATE CODE"^"ZIP CODE"~

> N1^ST^"SHIP TO NAME"^21^"HEALTH INDUSTRY ID#"~

> N2^"SHIP TO NAME CONT."^"SHIP TO NAME CONT."~

> N3^"ADDRESS INFO"^"ADDRESS INFO"~

> N4^"CITY NAME"^"STATE CODE"^"ZIP CODE"~

> ITD^14^^^"PAYMENT DATE"^15^"PAYMENT DUE DATE"^16^"TOTAL AMT"~

> DTM^002^"DELIVERY REQUESTED DATE"~

> DTM^035^"DELIVERY DATE"~

> IT1^1^12^CC^9.32^DS^ND^"NDC#"^VN^VENDOR ITEM \#^UP^

> "UPC CONSUMER CODE"~

> IT1^2^10^CA^21.50^DS^ND^"NDC#"^VN^VENDOR ITEM \#^UP^

> "UPC CONSUMER CODE"~

> CTT^2^^^^^^CLOSED~

> SE^23^"TRANSACTION SET CONTROL#"~

> GE^1^"GROUP CONTROL \#"~

> IEA^1^"INTERCHANGE CONTROL \#"~

Example 2: Mock Transaction Set

> ISA^00^ ^00^ ^ZZ^999999 ^ZZ^588 ^

> 950214^1005^U^00200^900456789^0^P^\>~

> GS^IN^999999^588^950214^1005^012345678^X^003020~

> ST^810^000000022~

> BIG^950214^201^950214^P2O01~

> REF^CR^23201~

> REF^TJ^102030~

> N1^BY^VA MEDICIAL CENTER^21^RA1000C00~

> N2^DEPARTMENT OF VETERANS AFFAIRS~

> N3^123 VETERANS BLVD.~

> N4^LOUISVILLE^KY^40202~

> N1^DS^DRUGS DISTRIBUTOR INC.^21^KA1000R00~

> N3^456 DRUG LANE~

> N4^LEXINGTON^KY^40601~

> N1^ST^VA MEDICAL CENTER^21^JR1000P00~

> N2^DEPARTMENT OF VETERANS AFFAIRS^~

> N3^123 VETERANS BLVD.^RECEIVING DEPT.~

> N4^LOUISVILLE^KY^40202~

> ITD^14^^^950301^15^950302^16^34.67~

> DTM^002^950210~

> DTM^035^950212~

> IT1^1^12^CC^9.32^DS^ND^00032227780^VN^46789~

> IT1^2^10^CA^21.50^DS^ND^00181053725^VN^878212~

> CTT^2^^^^^^CLOSED~

> SE^23^000000022~

> GE^1^012345678~

> IEA^1^900456789~

\<This page is intentionally left blank\>