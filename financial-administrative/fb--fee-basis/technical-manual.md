---
title: Fee Basis Version 3.5 Technical Manual/Security Guide (1995)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: FB
patch_ver: 3.5
patch_id: FB*3.5
group_key: "FB:FB:3.5"
file_numbers: 
  - 2
  - 162
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - blockquote
  - colspan
  - class
  - even
  - basis
  - style
  - width
  - strong
  - table
  - fbaa
page_count: 0
word_count: 36927
section_count: 21
table_count: 5
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/FB_3_5_TM_R1217.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/FB_3_5_TM_R1217.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=40"
---

Department of Veterans AffairsFee BasisTechnical Manual

![](fee-basis-version-3-5-technical-manual-security-guide-1995/001.png)

Version 3.5January 1995Revised January 2018Office of Information and Technology (OI&T)Product Development

#########  Revision History

Initiated on 12/29/04

![](fee-basis-version-3-5-technical-manual-security-guide-1995/002.png)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 50%" />
<col style="width: 17%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description (Patch # if applic.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Project Manager</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Technical Writer</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Jan 2018</td>
<td><p>Fee Basis Patch FB*3.5*158:</p>
<ul>
<li><blockquote>
<p>Batch Numbers will increase in size from 5 digits to 7 digits.</p>
</blockquote></li>
<li><blockquote>
<p>Batches that are 7 years old or older can be scheduled to purge on a monthly basis.</p>
</blockquote></li>
<li><blockquote>
<p>Batch files, transmitted to Central Fee, for inpatient, outpatient, and pharmacy claims will be updated to include data elements, previously transmitted via Vitria, as well as additional claim data.</p>
</blockquote></li>
<li><blockquote>
<p>Allow a maximum of 5 CARCs per claim line item with a maximum of 2 RARCs per CARC to be entered.</p>
</blockquote></li>
<li><blockquote>
<p>Software was also modified to decrease the maximum number of lines in a batch due to the addition of new fields in the batch.</p>
</blockquote>
<ul>
<li><p>OUTPATIENT: Previously users were able to have 85 lines in a batch; this is now changed to a maximum of 50 lines per batch.  </p></li>
<li><p>INPATIENT: Previously users were able to have 42 lines in a batch; this is now changed to a maximum of 30 lines per batch.</p></li>
</ul></li>
<li><blockquote>
<p>Associate CARCs with CORE Business Scenarios so that once a CARC and scenario is established, only additional CARCs from the same scenario can be selected.</p>
</blockquote></li>
<li><blockquote>
<p>Set up the Fee Basis data dictionary to support RARC to CARC relationships, still allowing for the selection of CARCless RARCs. Also support relationships between CARCs and Groups, and RARCs and Groups.</p>
</blockquote></li>
</ul>
<p>Populates ADJUSTMENT REASON (CARC) file (#161.91) with associated REMITTANCE REMARK (RARC) codes, CORE SENARIO, and ADJUSTMENT GROUPs (CAGC) to be complaint with CORE-required Code Combinations for CORE-defined Business Scenarios for the Phase III CORE 360 Uniform Use of Claim Adjustment Reason Codes and Remittance Advice Remark Codes (835) Rule version 3.3.0 June 2016.</p></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Oct 2016</td>
<td><p>VistA Fee Separation of Duties, Patch FB*3.5*154:</p>
<ul>
<li><blockquote>
<p>Three new security keys are implemented.</p>
</blockquote></li>
<li><blockquote>
<p>Locks on existing functionality and menu options are revised and software is modified to enforce separation of duties.</p>
</blockquote></li>
<li><blockquote>
<p>An existing problem with the identification of the associated authorization for outpatient payments and inpatient ancillary payments is resolved.</p>
</blockquote></li>
<li><blockquote>
<p>The software is modified to prevent an undefined error when a prescription is deleted.</p>
</blockquote></li>
</ul>
<blockquote>
<p>The software is modified to prevent an undefined error when rejected payments are re-initiated.</p>
</blockquote></td>
<td><blockquote>
<p>VistA Fee Separation of Duties Project Team</p>
</blockquote></td>
<td><blockquote>
<p>VistA Fee Separation of Duties Project Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>May 2016</td>
<td><p>Fee Basis, Patch FB*3.5*165</p>
<p>This patch deletes inappropriate reject flags from old payments, removes old payments with payment confirmation or cancellation data from in-process batches, and enhances the Print Rejected Payment Items report.</p>
<p>Three (3) Post-Inits/install routines were added to the Routines chapter in this document:</p>
<ul>
<li><p>FBXIP165</p></li>
<li><p>FBXI165A</p></li>
<li><p>FBXI165C</p></li>
</ul>
<p>Existing routine updated (along with the description):</p>
<blockquote>
<p>FBAARJP</p>
</blockquote></td>
<td><blockquote>
<p>VistA Fee Separation of Duties Project Team</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>11/2014</td>
<td><p>Patch FB*3.5*123 – VA-DoD VistA Fee IPAC Interface Enhancements.</p>
<blockquote>
<p>This patch includes changes to VistA Fee to allow payments from the VA to the DoD to flow through the Dept. of Treasury Intra-Governmental Payment and Collections (IPAC) System.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10/2014</td>
<td><p>Patch FB*3.5*151, Fee Basis Separation of Duties – Retain historical information enhancement. Documentation updates:</p>
<ul>
<li><p>Reformatted title page and updated footers.</p></li>
<li><p>Added storage requirements to Introduction chapter under Resource Requirements.</p></li>
<li><p>Added four new routines (FBAAAUD, FBAAAUDR, FBUCAUD, and FBXIP151) to Routines chapter.</p></li>
<li><p>Exported Options chapter:</p>
<ul>
<li><blockquote>
<p>Added option Historical Authorization Data Report [FBAA AUTH DATA AUDIT RPT] under Outputs Main Menu (FBAA OUTPUTS MENU).</p>
</blockquote></li>
<li><blockquote>
<p>Added Historical Authorization Data Report to Menu Diagram under Outputs Main Menu (FBAA OUTPUTS MENU).</p>
</blockquote></li>
</ul></li>
<li><p>Added VA FileMan to Subscriber Integration Agreements to External Relations chapter.</p></li>
</ul>
<p>Added new monitored fields to Security chapter under Audit Trails section.</p></td>
<td><blockquote>
<p>VistA Fee Separation of Duties Project Team</p>
</blockquote></td>
<td><blockquote>
<p>VistA Fee Separation of Duties Project Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9/2014</td>
<td><p>Fee Basis FB*3.5*139</p>
<p>Updated Title page</p>
<p>Updated Revision History, p i-ii</p>
<p>Updated Table of Contents, p iii-ivi</p>
<p>This patch introduces ICD-10 Advanced Search Functionality and other updates for ICD-10 Remediation. Changes in this manual include:</p>
<ul>
<li><p>Five new routines (FBASF, FBASFL, FBASFU, FBICD9 and FBICDP)</p></li>
</ul>
<blockquote>
<p>Two new ICD-10 fields,</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>1/2013</td>
<td><p>Fee Basis FB*3.5*132</p>
<p>This patch enhances the interface between VistA Fee Basis and Central Fee to improve the consistency of payment line item data between the systems. This will prevent duplicate ICN payments by ensuring that a payment line cannot be reprocessed in VistA Fee Basis unless it has been removed from Central Fee.</p>
<p>Changes to VistA Fee Basis documented in this manual are:</p>
<ul>
<li><p>New mail group: FEE FINANCE</p></li>
<li><p>New bulletin: FBAA SERVER</p></li>
<li><p>New routines.</p></li>
<li><p>Addition of new and modified options.</p></li>
<li><p>New Security Keys: FBAAFINANCE and FBAAREJECT</p></li>
</ul>
<blockquote>
<p>New file: FEE BASIS PAYMENT REJECT CODE (#161.99)</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9/2012</td>
<td><blockquote>
<p>Updated from Patch Review feedback. Removed references print and sort template that is not used.</p>
<p>Updated for FB*3.5*135 Fee 5010, added UCID field data to files 161.4, 162, and 162.5. Added UCID Menu and testing options. For Future Use: Added file 161.9 to hold FB provider data which is transferred to IB file 335.93 via a new scheduled Option FEE BASIS PAID TO IB (Not turned on). Added field #40 ALLOW FB PAID TO IB to site parameter file 161.4.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9/2012</td>
<td><blockquote>
<p>Patch FB*3.5*124 miscellaneous changes; NO CHANGES affecting Fee Basis Security or Technical components.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5/2012</td>
<td><blockquote>
<p>Patch FB*3.5*108 Pages. 5, 7, 79-94</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4/2012</td>
<td><p>Documentation updates for Patch FB*3.5*131:</p>
<ul>
<li><blockquote>
<p>Three new server options (not attached to any menu).</p>
</blockquote></li>
</ul>
<blockquote>
<p>Three new routines (called by the new options) that delete a message from the Postmaster mailbox and then quit.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11/2011</td>
<td><blockquote>
<p>Updated for FB*3.5*122 and FB*3.5*133, Fee 5010 EDI, Sections: General Information, Routines, Files, Exported Options, Glossary.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6/2011</p>
</blockquote></td>
<td><blockquote>
<p>Project ARCH, FB*3.5*119 Sections: Introduction, Routines, Files, External Relations.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5/2011</p>
</blockquote></td>
<td><blockquote>
<p>1358 Segregation of Duties FB*3.5*117 Sections: Routines, Exported Options.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5/2011</p>
</blockquote></td>
<td><blockquote>
<p>Updated for FB*3.5*121 Fee 5010, updated menu diagrams, added Appendix B. Sections: Implementation and Maintenance, Files, Exported Options, Appendix B.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2/2010</td>
<td><blockquote>
<p>Updated for the Fee Data HERO Project FB*3.5*107 and FB*3.5*108</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2/2007</td>
<td><blockquote>
<p>Updated for the NPI Project, FB*3.5*98 (Appendix A added)</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td><blockquote>
<p>Updated to comply with SOP192-352 Displaying Sensitive Data.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td><blockquote>
<p>Pdf file checked for accessibility to readers with disabilities.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

Table of Contents

Preface

The Fee Basis Technical Manual details various technical characteristics of the DHCP Fee Basis software product. This manual was produced by the Albany Information Systems Center to provide necessary information for use in the technical operation of the DHCP Fee Basis software package, Version 3.5. It should be noted that this manual is intended for use by technical computer personnel and is not designed for use by the typical end user.

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Namespace Conventions](#namespace-conventions)
  - [Integrity Checker](#integrity-checker)
  - [Obsolete Options](#obsolete-options)
  - [Resource Requirements](#resource-requirements)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Site Configurable Parameters](#site-configurable-parameters)
  - [Site Parameters Not Edited by Users (Edited by Routines)](#site-parameters-not-edited-by-users-edited-by-routines)
  - [Mail Groups](#mail-groups)
  - [Bulletins](#bulletins)
- [Routines](#routines)
  - [Routine List with Descriptions](#routine-list-with-descriptions)
  - [Callable Routines](#callable-routines)
- [# Files](#files)
  - [Main Globals and Files](#main-globals-and-files)
  - [Globals to Journal](#globals-to-journal)
  - [File List](#file-list)
  - [File Flow Chart](#file-flow-chart)
  - [Templates](#templates)
    - [Input Templates](#input-templates)
    - [Print Templates](#print-templates)
    - [Sort Templates](#sort-templates)
    - [Modifications to Fee Basis Files](#modifications-to-fee-basis-files)
- [Exported Options](#exported-options)
  - [Fee Basis Menus and Options](#fee-basis-menus-and-options)
  - [Menu Diagram Fee Basis Main Menu](#menu-diagram-fee-basis-main-menu)
- [Archiving and Purging](#archiving-and-purging)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [How to Generate On-Line Documentation](#how-to-generate-on-line-documentation)
- [Security](#security)
  - [General Security](#general-security)
    - [Audit Trails](#audit-trails)
    - [Security Keys](#security-keys)
    - [Legal Requirements](#legal-requirements)
  - [File Protection](#file-protection)
- [Glossary](#glossary)
- [Appendix A – Transmission Mappings[^1]](#appendix-a-transmission-mappings1)
  - [<table>](#table)
- [Appendix B – Transmission Mappings from Central Fee](#appendix-b-transmission-mappings-from-central-fee)
- [Appendix C – CARC/RARC Relationships](#appendix-c-carcrarc-relationships)
The VISTA Fee Basis package provides a range of software supporting the Department of Veterans Affairs fee for service (Fee Basis) program. A veteran is authorized Fee Basis care if s/he is legally eligible for such care and VA facilities are not feasibly available to meet the patient's medical needs. The authorization may be for short-term care, ID card status for ongoing outpatient care, home nursing services which authorize home nursing visits, community nursing home, or contract hospital. Veterans authorized Fee Basis care may receive reimbursement for their travel expenses from their home to the fee provider and/or prescription services in emergent situations.
The Fee Basis package interfaces with the ADT (Admission-Discharge-Transfer) VISTA module of the PIMS (MAS) package to provide users access to registration data entered through ADT options. It integrates with VA FileMan to give non-programmer personnel the ability to extract reports with ease. It interacts with the IFCAP package in the passing of data for posting to 1358s. It integrates with the Integrated Billing (IB) package for patient insurance data and provider data for potentially cost recoverable claims (added for FB\*3.5\*135). It allows users to enter and track unauthorized claims for all Fee Basis programs. Use of the Fee Basis software provides for more efficient and accurate operation of the Fee Basis programs with reduction of paperwork, savings in man-hours, and minimization of error.
Fee Basis also integrates with the Clinical Reminders package to Clinical Reminders (DBIA \#5619) to provide Clinical Reminders with two functions to list the patient’s ARCH (Access Received Closer to Home) eligibility of a certain date range and a list of all patients and their ARCH Eligibility. Added for FB\*3.5\*119.
Related manuals include the Fee Basis User Manual, which describes the functionality and use of the software; the Fee Basis Installation Guide, which provides step-by-step instructions for installing the software, the Fee Basis Guidebook supplied by Central Office.
The Fee Basis software provides menus for the four fee for service programs: Medical Fee, Pharmacy Fee, Community Nursing Home, and Civil Hospital. There are also menus for processing unauthorized claims and answering telephone inquiries regarding payments.
Some of the options in the Medical Fee Main Menu are utilized to:
- Authorize Fee Basis treatment
- Enter vendors or payments
- Create, close out, and release batches of invoices
- Record travel payments
- Establish site parameters
- Queue Fee Basis batch data for transmission to Austin, TX
The Pharmacy Fee section of the Fee Basis package provides the means to administer the Hometown Pharmacy program, which provides payment for medications furnished to eligible veterans on an emergency basis.
The Community Nursing Home section provides the means to pay for nursing home care provided to VA in-patients who are placed in nursing homes in the community for an authorized period of time at VA expense.
The Civil Hospital section provides the ability to pay for care provided to veterans who are determined to be legally and medically eligible for care and who are admitted to a private hospital in emergency situations where VA facilities are not feasibly available.
The Unauthorized Claims section provides the means to process unauthorized claims, which are expenses for inpatient medical services obtained by eligible veterans without prior authorization from the VA.
The Telephone Inquiry Menu contains the options that are used to answer inquiries from vendors and/or veterans regarding payments or checks.
General Information

## Namespace Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace assigned to the Fee Basis package is FB.

## Integrity Checker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fee Basis package has its own integrity checker. The routine is FBNTEG and should be used after the installation of a patch to verify that the patch was installed correctly. Integrity values will be supplied in the patch module.

## Obsolete Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options may be deleted.

FBAA VENDOR CLEANUP

FBAA MRA VENDOR ADD FO

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Formula for TUs: (# of FEE patients/160,000) + .04 = TUs needed

Storage requirements:

> Initial: .004 Mbytes/FEE patient

> Additional: (# of inpatient invoices X 435)/1,000,000

> (# of inpatient authorizations X 700)/1,000,000 (# of unauthorized claims X 630)/1,000,000

Equipment requirements: Increase from Fee Basis version 3.0 for inpatient invoices for Fee 5010 EDI provider data; \# of inpatient invoices X 335 is now X 435 for FB\*3.5\*133.

Additional storage is required for records entered or modified after the installation of patch FB\*3.5\*151:

- 480 additional bytes per authorization in the FEE BASIS PATIENT (#161) file to support the new data audit on selected fields.
- 3000 additional bytes per claim in the FEE BASIS UNAUTHORIZED CLAIMS (#162.7) file to support the new data audit on selected fields.

*(This page included for two-sided copying.)*

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several parameters associated with the Fee Basis package that are site configurable. Each of these parameters may be set through the Supervisor Main Menu using the Site Parameter Enter/Edit option. The following is an example of what might appear on the screen while using the Site Parameter Enter/Edit option. User responses are shown in boldface type. Descriptions of the site configurable parameters begin on the following page.

Select Supervisor Main Menu Option: SITE Parameter Enter/Edit

Select Site: VAMC SITE NY

STATION OF JURISDICTION NAME: VAMC SITE NY// \<RET\> STATION ADDRESS LINE 1: 128 HOLLAND AVE// \<RET\> STATION ADDRESS LINE 2: \<RET\>

STATION ADDRESS LINE 3: \<RET\> CITY: ALBANY// \<RET\>

STATE: VAMC STATE// \<RET\> ZIP: 99999// \<RET\>

STATION TELEPHONE NUMBER: 563-7788 OR 456-7766 Replace \<RET\> APPROVING OFFICIAL FOR 7079: REDACTED// \<RET\>

TITLE OF APPROVING OFFICIAL: CENTER DIRECTOR// MEDICAL CENTER DIRECTOR MEDICAID DISPENSING FEE: 2.95// \<RET\>

MEDICAL PAYMENT VENDOR DISPLAY: YES// \<RET\>

PHARMACY PAYMNT VENDOR DISPLAY: YES// \<RET\> DEFAULT AUTH. TIME RANGE: 1095// \<RET\>

ASK VENDOR DURING AUTH.: YES// \<RET\>

MAX \# PAYMENT LINE ITEMS: 85// \<RET\>

MAX \# CH PAYMENT LINES: 42// \<RET\>

MAX \# CNH PAYMENT LINES: 61// \<RET\>

EDIT AUTH. DURING PAYMENT: YES// \<RET\>

\*ASK PROGRAM SPECIFIC AUTH.: YES// \<RET\> APPROVING OFFICIAL FOR 7078: Dr. DOCTOR// \<RET\>

TITLE 7078 APPROVING OFFICIAL: Assoc. Chief of Staff Replace \<RET\>

COPIES OF 7078 TO BE PRINTED: 1// \<RET\>

PSA DEFAULT INSTITUTION: ALBANY MEDICAL CENTER// \<RET\> 7078 DEFAULT AUTH SERVICE TEXT:

> 1\>NOTIFICATION OF HOSPITALIZATION RECEIVED WITHIN 72 HOURS OF ADMISSION. 2\>HOSPITALIZATION UNTIL STABLE OR UNLESS FURTHER APPROVED BY FEE BASIS 3\>CLINIC DIRECTOR -

> 4\>

> 5\>MED/SURG PAYMENTS AT DRG RATES IN ACCORDANCE WITH PPS. PSY 6\>PAYMENTS AT 72% OF BILLED CHARGES FOR AUTHORIZED DATES OF CARE

EDIT Option: \<RET\>

TRACK INCOMPLETE UNAUTHORIZED CLAIMS?: YES// \<RET\>

'INITIAL ENTRY' STATUS FOR U/C: \<RET\>

UNAUTHORIZED CLAIM PRINTER: \<RET\>

UNAUTHORIZED CLAIM LETTER: AUTOMATIC PRINT// \<RET\>

NUMBER OF COPIES: 1// \<RET\>

PRINT U/C ON LETTERHEAD?: \<RET\>

STATION NAME (EDITABLE): VAMC SITE NY// \<RET\>

UC LETTER LINES AFTER CC:

ALLOW FB PAID TO IB: YES//

Select Site:

## Site Configurable Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STATION OF JURISDICTION NAME          | The name of the Clinic of Jurisdiction for which these site parameters are defined. There can be only one entry in this file.                                                                                                                                                                                                                                                                                                                                     |
| STATION ADDRESS LINE 1                | Street address line 1 of this COJ. This data will be printed on the authorization, VA Form 10-7079.                                                                                                                                                                                                                                                                                                                                                               |
| STATION ADDRESS LINE 2                | Street address line 2 of this COJ. This address line will also print on the authorization, VA Form 10-7079.                                                                                                                                                                                                                                                                                                                                                       |
| STATION ADDRESS LINE 3                | Line 3 of the COJ's street address.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| CITY                                  | The city in the COJ's mailing address.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| STATE                                 | The state in the COJ's mailing address.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ZIP                                   | Zip code for the COJ.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| STATION TELEPHONE NUMBER              | The telephone number to which Fee Basis inquiries should be directed.                                                                                                                                                                                                                                                                                                                                                                                             |
| APPROVING OFFICIAL FOR 7079           | The name of the approving official authorizing Fee Basis services. This name will be printed on the authorization, VA Form 10-7079.                                                                                                                                                                                                                                                                                                                               |
| TITLE OF APPROVING OFFICIAL           | The title of the approving official. This title will be printed on the authorization, VA Form 10-7079.                                                                                                                                                                                                                                                                                                                                                            |
| MEDICAID DISPENSING FEE               | The dollar amount of the Medicaid dispensing fee for this COJ. Dispensing fees, which are approved by Medicaid, vary from COJ to COJ.                                                                                                                                                                                                                                                                                                                             |
| MEDICAL PAYMENT VENDOR DISPLAY        | This parameter is used to indicate whether the vendor's demographic data will be displayed and made editable during the entering of a medical payment.                                                                                                                                                                                                                                                                                                            |
| PHARMACY PAYMNT VENDOR DISPLAY        | If there is a "Y" in this field, the vendor demographics will be displayed during the Enter Pharmacy Invoice option.                                                                                                                                                                                                                                                                                                                                              |
| DEFAULT AUTH. TIME RANGE              | The number of days of the usual long-term authorization. The data entered here will be added to the Authorization From Date and that date will become the default To Date for the authorization. For example, if the normal long-term authorization is one year, 364 would be entered in this parameter.                                                                                                                                                          |
| ASK VENDOR DURING AUTH                | A "YES" response results in asking for a vendor when using the Enter Authorization option.                                                                                                                                                                                                                                                                                                                                                                        |
| MAX \# PAYMENT LINE ITEMS             | The maximum number of payment line items that will be allowed in a batch for outpatient and ancillary. Any number between 1 and 85 is acceptable. This value is checked during the Enter Payment options and will warn the clerks when they are within 20 of the maximum. It will prevent the clerks from exceeding this number.                                                                                                                                  |
| MAX \# CH PAYMENT LINES               | The maximum number of payment line items that will be allowed in a batch for Civil Hospital. Any number between 1 and 42 is acceptable. This value is checked during the Enter Payment options and will warn the clerks when they are within 20 of the maximum. It will prevent the clerks from exceeding this number.                                                                                                                                            |
| MAX \# CNH PAYMENT LINES              | The maximum number of payment line items that will be allowed in a batch for Contract Nursing Home. Any number between 1 and 61 is acceptable. This value is checked during the Enter Payment options and will warn the clerks when they are within 20 of the maximum. It will prevent the clerks from exceeding this number.                                                                                                                                     |
| EDIT AUTH.DURING PAYMENT              | This field is used to indicate that editing of the AUTHORIZATION REMARKS field and the 3 DX fields is allowable during the Enter Payment options. It is normally used for six months immediately after installing the Fee Basis software because the Remarks and DX data were not available for downloading from Central Fee system.                                                                                                                              |
| \*ASK PROGRAM SPECIFIC AUTH.          | A "YES" answer to this site parameter will show only those authorizations that are program-specific. An example would be the display for selection of only Community Nursing Home authorizations when entering CNH payments.                                                                                                                                                                                                                                      |
| APPROVING OFFICIAL FOR 7078           | The default approving official for VA Form 10-7078s.                                                                                                                                                                                                                                                                                                                                                                                                              |
| TITLE 7078 APPROVING OFFICIAL         | The title of the default approving official for VA Form 10-7078s.                                                                                                                                                                                                                                                                                                                                                                                                 |
| COPIES OF 7078 TO BE PRINTED          | Indicates the default number of copies to be printed for each VA Form 10-7078 generated.                                                                                                                                                                                                                                                                                                                                                                          |
| PSA DEFAULT INSTITUTION               | The station number for the transmission of data to Austin is determined using this field. In almost all cases, your facility should be entered.                                                                                                                                                                                                                                                                                                                   |
| 7078 DEFAULT AUTH SERVICE TEXT        | A free text entry for special remarks, instructions, etc. pertaining to the authorization, which will appear in Section 6 of VA Form 10-7078.                                                                                                                                                                                                                                                                                                                     |
| TRACK INCOMPLETE UNAUTHORIZED CLAIMS? | This field indicates whether or not incomplete unauthorized claims should be tracked. Enter "YES" to track incomplete claims; otherwise only complete claims can be tracked. The response is a numeric character, with 1 equal to "YES" and 0 equal to "NO".                                                                                                                                                                                                      |
| 'INITIAL ENTRY' STATUS FOR U/C        | If this field is filled in, then minimum data is required for entering an unauthorized claim. This is designed for sites who have streamlined their workload, where only one user enters the unauthorized claims received, and another reviews the claim for completeness and makes the necessary requests, etc. The response is the numeric character 1 to activate; otherwise, leave this field blank.                                                          |
| UNAUTHORIZED CLAIM PRINTER            | Select a printer device name. NOTE: This is not a pointer field. The exact name must be entered.                                                                                                                                                                                                                                                                                                                                                                  |
| UNAUTHORIZED CLAIM LETTER             | Indicate how you wish your unauthorized claim letters to print. Enter an "A" if the Unauthorized Claim Printer is dedicated, and you always wish a letter to print when it has been changed to the appropriate status. Enter a "B" if the Unauthorized Claim Printer is not dedicated, or you wish to batch print letters of claims, which have changed to the appropriate status. Do not enter anything if you will be manually generating your own form letter. |
| NUMBER OF COPIES                      | This field indicates the number of copies of a letter to be printed. The maximum number of copies allowed is five.                                                                                                                                                                                                                                                                                                                                                |
| PRINT U/C ON LETTERHEAD?              | No entry is necessary if you will not be printing letters. Enter the numeric character 1 if your site will be printing unauthorized claims letters on letterhead.                                                                                                                                                                                                                                                                                                 |
| STATION NAME (EDITABLE)               | This is the first line of the return address. The data is pulled from Field \#.01 and can be edited at this prompt.                                                                                                                                                                                                                                                                                                                                               |
| ALLOW FB PAID TO IB: YES/ /           | Setting this parameter to ‘YES’ allows provider information from Fee Basis claims that are potentially cost recoverable to be saved to the FEE BASIS PAID TO IB FILE (161.9) during batch processing and passed to the Integrated Billing file IB NON/OTHER VA BILLING PROVIDER (#335.93) by the scheduled option FB PAID TO IB.                                                                                                                                  |

\*Will be deleted in future version

## Site Parameters Not Edited by Users (Edited by Routines)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                                 | Description                                                                                                                                                                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FPPS TRANSMIT START                      | This is the start date and time for the beginning of the FB FPPS TRANSMIT menu option. This value will be auto-populated by the menu option to help track when the last time a batch was started. FB\*3.5\*121.                 |
| FPPS TRANSMIT END                        | This is the finish date and time for the FB FPPS TRANSMIT menu option. This value will be auto-populated by the menu option to help track when the last time a batch finished. FB\*3.5\*121.                                    |
| (#39) UNIQUE CLAIM IDENTIFIER SEQ \[3F\] | This field contains a sequence number, which is incremented programmatically during Fee Basis Payment entry.                                                                                                                    |
| (#80) LAST IPAC NUMBER                   | This is the last number used to create the ID# field in the IPAC VENDOR AGREEMENT file (#161.95). This number is automatically incremented for each new IPAC vendor agreement that is created. Field created with FB\*3.5\*123. |

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 32%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Suggested Members</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FEE</td>
<td>Individuals who should receive confirmation messages from Austin and notifications from the VistA Fee Basis software.</td>
<td><p>This mail group is used to receive confirmation and daily reports from Austin DPC.</p>
<p>The VistA Fee Basis software also sends notification of events to this mail group.</p></td>
</tr>
<tr class="even">
<td>FEE FINANCE</td>
<td>This mail group was created for finance staff. The messages sent to this mail group are also sent to another mail group (FEE). Since the FEE mail group also receives messages that may not be of interest to finance staff, the separate FEE FINANCE mail group was created.</td>
<td><p>This mail group receives messages from the Fee Basis software when exceptions occur during processing of messages sent by Central Fee that are related to payment batches previously transmitted to Central Fee.</p>
<p>The FBAA BATCH SERVER, FBAA VOUCHER SERVER, and FBAA REJECT SERVER options may send a message to this mail group.</p></td>
</tr>
</tbody>
</table>

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Cause</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FBAA SERVER</td>
<td>This bulletin is used by the FBAA BATCH SERVER, FBAA VOUCHER SERVER, and FBAA REJECT SERVER options to notify users of a problem while processing applicable transactions from Central Fee.</td>
<td><p>Contains the following information:</p>
<ul>
<li><p>Date and time.</p></li>
<li><p>Name of the sender of the server request.</p></li>
<li><p>Name of the option which was requested by Mailman.</p></li>
<li><p>Subject of the message which requested a server.</p></li>
<li><p>The internal number of the message requesting a server.</p></li>
<li><p>Comments appended to the bulletin. These may include errors trapped by the server software and/or the operating system, as well as general purpose messages.</p></li>
<li><p>Text to be appended to the message subject.</p></li>
</ul></td>
</tr>
</tbody>
</table>

*(This page included for two-sided copying.)*

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routine List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of routines contained in the Fee Basis package with a brief description of each.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FB1358</td>
<td><blockquote>
<p>IFCAP 1358 obligation utilities.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FB35P50</td>
<td><blockquote>
<p>Post init routine to identify corrupt vendor file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAA79, FBAA79A</td>
<td><blockquote>
<p>Prints VA Form 7079 in response to a request for outpatient medical services.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAAUD</td>
<td><blockquote>
<p>Called by data dictionary of the FEE BASIS PATIENT (#161) file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAAUDR</td>
<td><blockquote>
<p>Historical Authorization Data Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAAUD</td>
<td><blockquote>
<p>Called by data dictionary of the FEE BASIS PATIENT (#161) file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAAUDR</td>
<td><blockquote>
<p>Historical Authorization Data Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAAUT</td>
<td><blockquote>
<p>Runs the Enter/Edit Authorization option and is used to enter or edit an authorization for Fee Basis services.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAAV</td>
<td><blockquote>
<p>Flags a vendor for addition to the Central Fee file in Austin, Texas.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAABDL</td>
<td><blockquote>
<p>Allows the user to delete batches that meet necessary criteria.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAABET</td>
<td><blockquote>
<p>Allows the user to edit a batch type and obligation number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAABPG</td>
<td><blockquote>
<p>Allows the purging of the FEE BASIS BATCH file (#161.7).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAABS</td>
<td><blockquote>
<p>Displays available information for a selected batch based on the status of the batch.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAABT</td>
<td><blockquote>
<p>Prints out the statuses of all active batches.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAACCB, FBAACCB0, FBAACCB1, FBAACCB2</td>
<td><blockquote>
<p>Runs the Close-out Batch option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAACFE</td>
<td><blockquote>
<p>Contract file enter/edit.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAACH</td>
<td><blockquote>
<p>Displays the ID card history for a patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAACIE</td>
<td><blockquote>
<p>Allows the user to complete a pharmacy invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAACLU</td>
<td><blockquote>
<p>Shows the user who last entered or changed an authorization.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAACO, FBAACO1, FBAACO3, FBAACO4, FBAACO5</td>
<td><blockquote>
<p>Allows users to enter a medical payment.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAACO0</td>
<td><blockquote>
<p>Displays the FEE BASIS PATIENT file (#161) address information for a patient. The information may also be edited via this routine.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAACO2</td>
<td><blockquote>
<p>Processes duplicate payments and, if requested, stores them as a MEDICAL denial.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAACR</td>
<td><blockquote>
<p>Prints out the cost report for Outpatient Medical.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAADCB</td>
<td><blockquote>
<p>Displays batches that have been closed but not yet certified by the supervisor.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAADD</td>
<td><blockquote>
<p>Causes an entire batch to be rejected.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAADD1</td>
<td><blockquote>
<p>Reprocess overdue batch.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAADEM, FBAADEM1</td>
<td><blockquote>
<p>Displays veteran demographics.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAADOB</td>
<td><blockquote>
<p>Displays any available information about open batches.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAADV</td>
<td><blockquote>
<p>Places a vendor in DELETE status on the local system only.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAEAR</td>
<td><blockquote>
<p>Allows a user to enter any necessary authorization remarks.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAELT</td>
<td><blockquote>
<p>Enter or edit suspension letters.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAEPI, FBAAEPI1</td>
<td><blockquote>
<p>Allows the user to edit a pharmacy invoice that was previously entered.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAESP</td>
<td><blockquote>
<p>Allows the Fee Basis supervisor to enter or edit site parameters.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAETA</td>
<td><blockquote>
<p>If there is a travel payment, it is entered via this routine.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAFA</td>
<td><blockquote>
<p>File adjustments for medical/ancillary payments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAFED</td>
<td><blockquote>
<p>FPPS data edit outpatient/ancillary invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAFR</td>
<td><blockquote>
<p>File remittance remarks for medical/ancillary payments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAFS</td>
<td><blockquote>
<p>Outpatient fee schedule.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAFSF</td>
<td><blockquote>
<p>Outpatient 75<sup>th</sup> percentile fee schedule.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAFSR</td>
<td><blockquote>
<p>RBRVS fee schedule.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAIAD, FBAAIAE, FBAAIAV</td>
<td><blockquote>
<p>Add, edit, delete, display IPAC agreement information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAIAQ, FBAAIAU</td>
<td><blockquote>
<p>Manage IPAC agreement MRA status and transmission.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAIAR, FBAAIARA</td>
<td><blockquote>
<p>IPAC Vendor DoD Invoice Report (Summary Report)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAIAR1, FBAAIAR2</td>
<td><blockquote>
<p>DoD Invoice Number Inquiry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAIARB, FBAAIARC, FBAAIARD</td>
<td><blockquote>
<p>IPAC Vendor Payment Report (Detail Report)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAALB</td>
<td><blockquote>
<p>Provides a record of payments in any batch.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAALPI</td>
<td><blockquote>
<p>Lists invoices that are ready for PIMS (MAS) completion. If a user wishes to complete an invoice after viewing all those ready for completion, then control is transferred to routine FBAACIE.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAALU</td>
<td><blockquote>
<p>References the CPT file for CPT Code lookups.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAMP, FBAAMP1</td>
<td><blockquote>
<p>Allows multiple payments to be entered for a vendor.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAMPG1</td>
<td><blockquote>
<p>Allows the user to automatically purge transmitted Delete type and Reinstate type MRAs.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAMPRG</td>
<td><blockquote>
<p>Purges transmitted MRAs.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAMST</td>
<td><blockquote>
<p>MST report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAOB</td>
<td><blockquote>
<p>Allows a user to create and open a batch.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAODP, FBAAODP0</td>
<td><blockquote>
<p>Allows a payment to be deleted.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPAA</td>
<td><blockquote>
<p>Allows adding to, or editing of, the Fee schedule.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPAR</td>
<td><blockquote>
<p>Payment Aging Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPAY</td>
<td><blockquote>
<p>Compiles the Fee schedule.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPCC</td>
<td><blockquote>
<p>Prints a list of all currently issued Fee Basis ID cards.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPCS</td>
<td><blockquote>
<p>Report Cost/Savings from RBRVS fee schedule.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPDM</td>
<td><blockquote>
<p>Creates a Patient MRA Delete type transaction.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPET, FBAAPET1</td>
<td><blockquote>
<p>Allows a user to edit medical payments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPGL</td>
<td><blockquote>
<p>Post payments to COREFLS.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPH</td>
<td><blockquote>
<p>Provides a payment history listing for a veteran.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPHV</td>
<td><blockquote>
<p>Allows the user to void a pharmacy payment.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPI</td>
<td><blockquote>
<p>Displays patient demographics and Fee Basis authorizations.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPIE, FBAAPIE1</td>
<td><blockquote>
<p>Allows a user to enter a Fee Basis pharmacy invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPII</td>
<td><blockquote>
<p>Displays a selected pharmacy invoice.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPIN, FBAAPIN1</td>
<td><blockquote>
<p>Displays detail line items associated with a selected invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPIP</td>
<td><blockquote>
<p>Used to assign a batch number to a completed pharmacy invoice prior to payment being sent to Austin.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPIS</td>
<td><blockquote>
<p>Displays the status of a selected pharmacy invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPLU</td>
<td><blockquote>
<p>Allows the user to look up a pharmacy vendor payment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPM</td>
<td><blockquote>
<p>Creates a Patient MRA transaction.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPOC</td>
<td><blockquote>
<p>Prints all obsolete Fee Basis ID cards.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPP, FBAAPP0</td>
<td><blockquote>
<p>Allows a pharmacist to review a Fee Basis prescription.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPPH</td>
<td><blockquote>
<p>Provides a Fee Basis pharmacy prescriptions history list for a patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPRC</td>
<td><blockquote>
<p>Prints a report of contact.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAPRGS</td>
<td><blockquote>
<p>Prints out the status of the Fee Basis Purge.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAPV</td>
<td><blockquote>
<p>Lists all vendors that are awaiting Austin approval.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAARB</td>
<td><blockquote>
<p>Allows a previously closed batch to be reopened.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAARD, FBAARD0</td>
<td><blockquote>
<p>Allows all rejects that were entered in error to be deleted.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAARD1, FBAARD2, FBAARD3</td>
<td><blockquote>
<p>Allows reject codes to be deleted for a particular item.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAARJP</td>
<td><blockquote>
<p>Prints all rejects pending PIMS (MAS) action.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAARMRA</td>
<td><blockquote>
<p>Retransmits MRAs for a specified date.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAROC</td>
<td><blockquote>
<p>Allows a user to enter a report of contact.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAARP</td>
<td><blockquote>
<p>Runs the reimbursement payment option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAARR, FBAARR0, FBAARR2, FBAARR3</td>
<td><blockquote>
<p>Allows any rejected line items to be reinitiated and assigned to a new batch.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAARR1</td>
<td><blockquote>
<p>Reinitiates an entire batch.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAARV</td>
<td><blockquote>
<p>Reactivates a previously deleted vendor in the CENTRAL FEE VENDOR file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAS79</td>
<td><blockquote>
<p>Allows a single VA Form 10-7079 to be printed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAASAP</td>
<td><blockquote>
<p>Displays all authorization information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAASCB, FBAASCB0</td>
<td><blockquote>
<p>Allows a Fee Basis supervisor to release a batch.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAASDR</td>
<td><blockquote>
<p>Generates the Fee Basis 1358 Segregation of Duty Report. FB*3.5*117</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAASL, FBAASL1, FBAASL1B, FBAASLP, FBCHSL1, FBCHSLP</td>
<td><blockquote>
<p>Allows the user to print suspension letters.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAASOUT</td>
<td><blockquote>
<p>Generates the output for the Fee schedule.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAASTA</td>
<td><blockquote>
<p>Responsible for displaying a user's sign-on status. It displays a list of all open batches for the current user, including the type of batch, the batch number, the obligation number, and the date that the batch was opened.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAATIC</td>
<td><blockquote>
<p>Allows the user to terminate an existing ID card.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAUTL</td>
<td><blockquote>
<p>Utility routine for the Fee Basis package. It performs various tasks such as setting the FBSITE(0) and FBSITE(1) variables to Fee Basis site parameters, getting the next available batch number or invoice number, and determining the length of time that a vendor has been in DELETE status.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAUTL1, FBAAUTL2</td>
<td><blockquote>
<p>Utility routines. They contain various functions such as posting increases/decreases to 1358s and selecting veterans and authorizations.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAUTL3</td>
<td><blockquote>
<p>Supported call to be used by IFCAP to determine the System Identifier for the 994 code sheets.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAUTL4, FBAAUTL5</td>
<td><blockquote>
<p>Used to build the "AE" cross-reference in File #162 and retrieve the CPT and modifier from the cross-reference.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAUTL6</td>
<td><blockquote>
<p>Utility routine. Used to validate/correct socioeconomic groups extrinsic functions.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAUTL7</td>
<td><blockquote>
<p>Utility routine. Used to set the “AE” cross-reference when SERVICE PROVIDED field is added or modified.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAUTL8</td>
<td><blockquote>
<p>Utility routine. Used to convert first five digits of SSN to “X” and only display the last four digits of the SSN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAUVC</td>
<td><blockquote>
<p>Updates vendor codes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAV0, FBAAV01</td>
<td><blockquote>
<p>Responsible for sending Fee Basis data to Austin.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAV1</td>
<td><blockquote>
<p>Transmits Vendor MRA data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAV2</td>
<td><blockquote>
<p>Transmits Pharmacy payments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAV3</td>
<td><blockquote>
<p>Transmits Travel payments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAV4</td>
<td><blockquote>
<p>Transmits patient MRAs.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAV5</td>
<td><blockquote>
<p>Creates transactions for CH/CNH payments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAV6</td>
<td><blockquote>
<p>Creates transactions to send to the Pricer System.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAV8</td>
<td><blockquote>
<p>Transmits IPAC Agreement MRAs.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAVD, FBAAVD2</td>
<td><blockquote>
<p>Displays vendor demographics and allows the user to edit the data displayed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAVD1</td>
<td><blockquote>
<p>Displays CNH vendor specifics.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAVD3</td>
<td><blockquote>
<p>Edit vendor FPDS data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAVD4</td>
<td><blockquote>
<p>Special routine for entering/inactivating/deleting NPI in file 161.2.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAVLU</td>
<td><blockquote>
<p>Looks up payments to a vendor for a specified time frame.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAVP, FBAAVP0</td>
<td><blockquote>
<p>Allows the user to either void or cancel the void on a medical payment.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAVR, FBAAVR0, FBAAVR1, FBAAVR2, FBAAVR3, FBAAVR4,</td>
<td><blockquote>
<p>Allows the user to specify local rejects and finalize a batch.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAVR5</td>
<td><blockquote>
<p>Generate voucher batch msg.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAAVR6</td>
<td><blockquote>
<p>Resend voucher batch msg.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAAVS</td>
<td><blockquote>
<p>Displays payment data for a selected patient and vendor.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBARCH0</td>
<td><blockquote>
<p>Stores the eligibility status for Project ARCH. FB*3.5*119</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBASF</td>
<td><blockquote>
<p>Advanced Search Functionality – asks for full or partial ICD-10 Diagnosis code and calls the Lexicon ICD-10 diagnosis search function to display the results.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBASFL</td>
<td><blockquote>
<p>Advanced Search Functionality – displays a listing of ICD-10 diagnosis codes based on search entry.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBASFU</td>
<td><blockquote>
<p>Advanced Search Functionality utilities.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBAUTHP</td>
<td><blockquote>
<p>Displays an authorization on screen for a specific authorization number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBBPG7Y</td>
<td><blockquote>
<p>Purge Batch File entries after seven years.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCH78, FBCH780, FBCH78A</td>
<td><blockquote>
<p>Sets up a VA Form 10-7078 authorization for CH.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHACT, FBCHACT0, FBCHACT1</td>
<td><blockquote>
<p>Calculates non-VA hospital activity and non-VA unauthorized days of activity.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHC78</td>
<td><blockquote>
<p>Allows a user to cancel a VA Form 10-7078.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHCD</td>
<td><blockquote>
<p>Completes disposition of an authorization.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHCO</td>
<td><blockquote>
<p>Allows entry of CH ancillary payments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHCR, FBCHCR1</td>
<td><blockquote>
<p>Prints out the cost report for Civil Hospital or Contract Nursing Home. The output may be for authorized or unauthorized care.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHDEL</td>
<td><blockquote>
<p>Deletes a notification/request.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHDI</td>
<td><blockquote>
<p>Displays an inpatient invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHDI2</td>
<td><blockquote>
<p>Displays an invoice for Civil Hospital.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHDIN</td>
<td><blockquote>
<p>Deletes an inpatient invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHDUC</td>
<td><blockquote>
<p>Displays unauthorized claims.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHEAP</td>
<td><blockquote>
<p>Allows the completion of a payment by adding the amount paid passed back from the Austin Pricer.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHEP, FBCHEP1</td>
<td><blockquote>
<p>Allows entry/edit of a CH payment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHEUC, FBCHEUC1, FBCHEUC2</td>
<td><blockquote>
<p>Allows entry/edit of an unauthorized claim.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHFA</td>
<td><blockquote>
<p>File adjustments for CH/CNH payment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHFED</td>
<td><blockquote>
<p>FPPS data edit for inpatient invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHFR</td>
<td><blockquote>
<p>File remittance remarks for CH/CNH payments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHP78</td>
<td><blockquote>
<p>Generates a VA Form 10-7078.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHPET</td>
<td><blockquote>
<p>Allows the user to edit an ancillary payment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHPH, FBCHPH0</td>
<td><blockquote>
<p>Displays a patient payment history.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHPRC, FBCHPRC1</td>
<td><blockquote>
<p>Prints a report of contact for CH.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHPSA, FBCHPSA0, FBCHPSA1</td>
<td><blockquote>
<p>Used to calculate dollar amounts by primary service area.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHREQ, FBCHREQ1</td>
<td><blockquote>
<p>Used for the notification/request process of Civil Hospital.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHREQ2</td>
<td><blockquote>
<p>Allows the user to reconsider a denied Civil Hospital notification.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHRJP</td>
<td><blockquote>
<p>Used to print rejected payment items from the Austin Pricer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHROC</td>
<td><blockquote>
<p>Used to input a report of contact for the Civil Hospital program.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHRR</td>
<td><blockquote>
<p>Used to reinitiate rejects from the pricer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHSCB</td>
<td><blockquote>
<p>Used by the Fee Basis supervisor to release batches to the pricer.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHSL1, FBCHSLP</td>
<td><blockquote>
<p>Print suspension letters.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHSTA</td>
<td><blockquote>
<p>Displays pending inpatient dispositions.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHSTAT</td>
<td><blockquote>
<p>Generates the request statistics report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCHVH</td>
<td><blockquote>
<p>Used to produce the inpatient vendor payment history.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHVP</td>
<td><blockquote>
<p>Allows the user to either void or cancel the void on an inpatient invoice.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCKDIS, FBCKDIS1</td>
<td><blockquote>
<p>Used to display payment information for a user-specified check number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCNHCEN</td>
<td><blockquote>
<p>Prints a report of census data for a user-specified date in Civil Hospital or Community Nursing Home.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCSV1</td>
<td><blockquote>
<p>Utilities for code set versioning.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCTAU, FBCTAU1, FBCTAU10,FBCTAU11, FBCTAU2, FBCTAU3, FBCTAU4, FBCTAU5, FBCTAU6, FBCTAU7, FBCTAU8, FBCTAU9</td>
<td><blockquote>
<p>Generated from FBAA AUTHORIZATION input template file 161.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBCTV, FBCTV1,FBCTV2, FBCTV3</td>
<td><blockquote>
<p>Generated from FB VENDOR UPDATE input template file 161.2.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBDOC</td>
<td><blockquote>
<p>Contains documentation for other Fee Basis routines.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBFHFT1</td>
<td><blockquote>
<p>FPPS HL7 FT1 segment.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBFHLD3</td>
<td><blockquote>
<p>Get data for outpatient/ancillary invoice.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBFHLD5</td>
<td><blockquote>
<p>Get data for pharmacy invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBFHLD9</td>
<td><blockquote>
<p>Get data for inpatient invoice.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBFHLL</td>
<td><blockquote>
<p>FPPS queued invoice file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBFHLP</td>
<td><blockquote>
<p>FPPS message purge.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBFHLS, FBFHLS1</td>
<td><blockquote>
<p>Build HL7 message segments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBFHLU</td>
<td><blockquote>
<p>FPPS HL utilities.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBFHLX, FBFHLX1,FBFHLX2</td>
<td><blockquote>
<p>Transmit HL7 messages to FPPS. FBFHLX2 was added in FB*3.5*122</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBFHORC</td>
<td><blockquote>
<p>FPPS HL7 ORC segment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBFPAR, FBFPCI</td>
<td><blockquote>
<p>FPPS audit report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBFPDS</td>
<td><blockquote>
<p>Report of vendors without FPDS data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBFPTR</td>
<td><blockquote>
<p>FPPS transmit report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBGMT2</td>
<td><blockquote>
<p>Fee Basis portion of GMT2.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBHLZFE</td>
<td><blockquote>
<p>Create HL7 ZFE segments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBICD9</td>
<td><blockquote>
<p>ICD-9 Diagnosis Code Utilities</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBICDP</td>
<td><blockquote>
<p>ICD-9 &amp; 10 Procedure Code Utilities</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBIDCARD</td>
<td><blockquote>
<p>Add an entry in Fee Basis ID card.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBLTCAR, FBLTCAR2</td>
<td><blockquote>
<p>LTC authorization reports.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBMON</td>
<td><blockquote>
<p>Monitor the FB FPPS TRANSMIT option. FB*3.5*122</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBMRASVR, FBMRASV1, FBMRASV2</td>
<td><blockquote>
<p>Updates the DHCP database automatically upon receipt of add or FBMRASV2 change confirmation from Austin.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHACT</td>
<td><blockquote>
<p>Used to output the Community Nursing Home Activity Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHAMI1</td>
<td><blockquote>
<p>Calculates/validates the AMIS 349 Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHAMI2</td>
<td><blockquote>
<p>Provides a report of all CNH stays in excess of 90 days.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHAMIE</td>
<td><blockquote>
<p>Outputs all CNH admissions and discharges within a user specified time frame.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHAMIS</td>
<td><blockquote>
<p>Calculates the 349 AMIS report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHDEC, FBNHDIEP</td>
<td><blockquote>
<p>Displays an episode of care for CNH.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHDLAD, FBNHDLDI,</td>
<td><blockquote>
<p>Deletes admissions, discharges, and transfers for CNH.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHEA, FBNHED</td>
<td><blockquote>
<p>Enters admissions/discharges for CNH.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHEAU2</td>
<td><blockquote>
<p>Asks rates for a CNH Authorization.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHEDA1, FBNHEDAT, FBNHEAU1, FBNHEAUT</td>
<td><blockquote>
<p>Enter/edit CNH authorizations.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHEDAD</td>
<td><blockquote>
<p>Edits the admission type for CNH.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHEDDI</td>
<td><blockquote>
<p>Edits the discharge type for CNH.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHEDPA</td>
<td><blockquote>
<p>Edits a payment for CNH.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHEDTR</td>
<td><blockquote>
<p>Edits the transfer type for CNH.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHEP, FBNHEP1, FBNHEP2</td>
<td><blockquote>
<p>Used to enter a CNH payment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHET</td>
<td><blockquote>
<p>Used to enter a transfer for CNH.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHEXP</td>
<td><blockquote>
<p>Produces a list of CNHs with contracts expiring within 90 days.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHPAMS</td>
<td><blockquote>
<p>Used to print AMIS reports.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHPC, FBNHPC1</td>
<td><blockquote>
<p>Posts commitments to 1358s.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHPLT</td>
<td><blockquote>
<p>Prints CNH payments and totals for a specified month.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHRAT, FBNHRAT1</td>
<td><blockquote>
<p>Posts new rates for a veteran.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHRC</td>
<td><blockquote>
<p>Allows the user to change a rate for a veteran within the authorization.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHRCS, FBNHRCS1, FBNHRCS2, FBNHRCS3, FBNHRCS4</td>
<td><blockquote>
<p>Used for reporting Nursing Homes that have active contracts with the VA.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHRDEL</td>
<td><blockquote>
<p>Allows the deletion of a rate if the rate has not been used yet.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNHROS</td>
<td><blockquote>
<p>Prints nursing home rosters.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNPILK</td>
<td><blockquote>
<p>NPI lookup routine.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBNTEG, FBNTEG0</td>
<td><blockquote>
<p>Calculates a checksum which might be used to check the integrity of a routine against values entered for Fee Basis patches in the NATIONAL PATCH file on FORUM.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBPAID, FBPAID1, FBPAID2</td>
<td><blockquote>
<p>Executed by the PAID server to process check information from FMS as it is confirmed by the treasury.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBPAID3,FBPAID3A</td>
<td><blockquote>
<p>FOR FUTURE USE: Executed during PAID server processing to populate, FEE BASIS PAID TO IB FILE (161.9). Contains entry point for scheduled option FEE BASIS PAID TO IB which transfers information from 161.9 to the IB NON/OTHER VA BILLING PROVIDER FILE (#335.93) (Added for patch FB*3.5*135)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBPAID3B</td>
<td><blockquote>
<p>FOR FUTURE USE: Provides reporting options to test data in FEE BASIS PAID TO IB FILE (161.9) FB*3.5*135</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBPATDAT</td>
<td><blockquote>
<p>Notification about patient data change.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBPAY, FBPAY2, FBPAY21, FBPAY3, FBPAY67, FBPAY671</td>
<td><blockquote>
<p>Provides output for vendor or veteran payment histories.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBPCR, FBPCR2, FBPCR3, FBPCR67, FBPCR671</td>
<td><blockquote>
<p>Output potential cost recovery cases for selected Primary Service Areas and user specified date ranges.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBPCR4</td>
<td><blockquote>
<p>LTC phase 3 utilities.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBPHON, FBPHON1, FBPHON2</td>
<td><blockquote>
<p>Called by VA List Manager, performs the building of the payment list for display, as well as process all actions that are selectable for the list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBPMRG, FBPMRG1</td>
<td><blockquote>
<p>Fee Basis patient merge routine. Called during patient (file #2) merge due to AFFECTS RECORD MERGE in PACKAGE file (#9.4).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBPRE35</td>
<td><blockquote>
<p>Pre-init to check versions of packages.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBPRICE, FBPRICE1</td>
<td><blockquote>
<p>Builds a transaction to send to the Austin Pricer System.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBPST35, FBPST35A, FBPST35B, FBPST35C, FBP35D</td>
<td><blockquote>
<p>Post-init routines.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBRVU</td>
<td><blockquote>
<p>RVU utilities.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBRXFA</td>
<td><blockquote>
<p>File adjustments for pharmacy payments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBRXFED</td>
<td><blockquote>
<p>FPPS data edit pharmacy invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBRXFR</td>
<td><blockquote>
<p>File remittance remarks for pharmacy payments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBRXUTL</td>
<td><blockquote>
<p>Fee Basis pharmacy utility.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBSHAUT</td>
<td><blockquote>
<p>Enter/edit state home authorization.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBSHRAD</td>
<td><blockquote>
<p>Report active authorizations for date.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBSHUTL</td>
<td><blockquote>
<p>State home utilities.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBSVBR</td>
<td><blockquote>
<p>Called by FBAA BATCH SERVER option to process Payment Batch Result messages from Central Fee. (Patch FB*3.5*131 and FB*3.5*132)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBSVPR</td>
<td><blockquote>
<p>Called by FBAA REJECT SERVER option to process Post Voucher Reject messages from Central Fee. (Patch FB*3.5*131 and FB*3.5*132)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBSVVA</td>
<td><blockquote>
<p>Called by FBAA VOUCHER SERVER option to process Voucher Batch Acknowledgement messages from Central Fee. (Patch FB*3.5*131 and FB*3.5*132)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCAUD</td>
<td><blockquote>
<p>Called by data dictionary of the FEE BASIS UNAUTHORIZED CLAIMS (#162.7) file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCDD, FBUCDD1</td>
<td><blockquote>
<p>Called by the data dictionaries of the FEE BASIS UNAUTHORIZED CLAIMS file (#162.7) and FEE BASIS SITE PARAMETERS file (#161.4).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCDE</td>
<td><blockquote>
<p>Unauthorized EDI claims that were not approved.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCDIS</td>
<td><blockquote>
<p>Displays unauthorized claims.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCDUP</td>
<td><blockquote>
<p>Provides a check for duplicate unauthorized claims.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCED, FBUCED0, FBUCED1</td>
<td><blockquote>
<p>Allows a user to perform various edits to the FEE BASIS UNAUTHORIZED CLAIMS file (#162.7), FEE BASIS UNAUTHORIZED CLAIMS PENDING INFO file (#162.8), or FEE BASIS UNAUTHORIZED REQUESTED INFORMATION file (#162.93).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCEN, FBUCEN1</td>
<td><blockquote>
<p>Allows the user to enter a new unauthorized claim.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCEVT</td>
<td><blockquote>
<p>Called prior to and after an event to an unauthorized claim, it captures the claim information needed to update the status, expiration date, and other data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCEX</td>
<td><blockquote>
<p>Provides a listing of those claims due to expire for a given date range selected by a user. It also removes the expiration date and updates the disposition to ABANDONED for those claims which have expired. A listing of abandoned claims is also provided.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCLET, FBUCLET0, FBUCLET1, FBUCLET2</td>
<td><blockquote>
<p>Prints out the unauthorized claims associated with a primary claim.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCLINK, FBUCLNK1</td>
<td><blockquote>
<p>Associates unauthorized claims with a primary.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCMBS</td>
<td><blockquote>
<p>Millennium act emergency care summit.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCMEA</td>
<td><blockquote>
<p>Unauthorized main menu entry action.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCOUT, FBUCOUT1</td>
<td><blockquote>
<p>Output routines for unauthorized claims. FBUCOUT prints unauthorized claims by status. FBUCOUT1 prints all unauthorized claims for either a vendor, veteran, or other party.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCPAY</td>
<td><blockquote>
<p>Payment driver for unauthorized claims.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCPEND</td>
<td><blockquote>
<p>Provides information on unauthorized claims pending information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCSTAT</td>
<td><blockquote>
<p>Provides unauthorized claims disposition and status statistics.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUCUPD, FBUCUPD1</td>
<td><blockquote>
<p>Determines the following: if a letter needs to be printed, the current status of a claim, expiration date, disposition date, date valid claim received, and date of original disposition. The appropriate fields are updated in the FEE BASIS UNAUTHORIZED CLAIMS file (#162.7), and the appropriate letter may be printed. Depending upon the disposition, the authorization may be updated in the FEE BASIS PATIENT file (#161).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUCUTL, FBUCUTL1, FBUCUTL2, FBUCUTL3, FBUCUTL4, FBUCUTL5, FBUCUTL6, FBUCUTL7, FBUCUTL8, FBUCUTL9</td>
<td><blockquote>
<p>Utility routines for the unauthorized claims options.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUINS</td>
<td><blockquote>
<p>Allows users to add insurance information for a veteran.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUTL, FBUTL1, FBUTL2, FBUTL3, FBUTL4, FBUTL4A, FBUTL5 FBUTL6</td>
<td><blockquote>
<p>Utility routines for the Fee Basis package.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUTL7</td>
<td><blockquote>
<p>Utility routine for Fee Basis Contracts.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBUTL8</td>
<td><blockquote>
<p>Utility routine for HIPAA 5010 providers. FB*3.5*122</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBUTL135, FBUTL136</td>
<td><blockquote>
<p>Utility routines for Unique Claim IDentifier (UCID) FB*3.5*135</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBVDISP</td>
<td><blockquote>
<p>Contains the vendor identifiers that are output on any vendor lookup.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBVISTBR</td>
<td><blockquote>
<p>List of authorizations for blind rehab.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBXBIPS, FBXCIPS, FBXDIPS, FBXEIPS, FBXIP110</td>
<td><blockquote>
<p>Post install routines.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBXIP100, FBXIP102, FBXIP104, FBXIP105, FBXIP108, FBXIP109, FBXIP111, FBXIP112, FBXIP121, FBXIP132, FBXIP133, FBXIP151, FBXIP19, FBXIP19A, FBXIP20, FBXIP22, FBXIP23,FBXPIP24, FBXIP27, FBXIP29, FBIXIP30, FBXIP32, FBXIP32A, FBXIP34, FBXIP35, FBXIP36, FBXIP37, FBXIP38, FBXIP39, FBXIP4, FBXIP44, FBXIP45, FBXIP48, FBXIP49, FBXIP53, FBXIP54,FBXIP61, FBXIP91,</td>
<td><blockquote>
<p>Patch install routines.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBXIP92, FBXIP99, FBXIPJNE</td>
<td><blockquote>
<p>Patch install routines, cont.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBXIP33</td>
<td><blockquote>
<p>Import GPCI/Zip code data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBXIP33A</td>
<td><blockquote>
<p>Import DOL MOD LVL tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBXIP33B</td>
<td><blockquote>
<p>Import DOL CPT data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBXIP69E, FBXIP76E, FBXIP77E, FBENVP65, FBXAIEN, FBXIP84E</td>
<td><blockquote>
<p>Environment check.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For IFCAP

> Routine Function Call: \$\$HDR^FBAAUTL3()

> This call returns the header necessary for the 994 code sheets in IFCAP (FEE for IFCAP V. 4.0 or FEN for IFCAP V. 5.0).

# # Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Main Globals and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The globals used in the Fee Basis Package are ^FB, ^FBAA, ^FBAAA, ^FB583, ^FB7078, ^FBAACNH, ^FBAAI, ^FBAAC, and ^FBAAV. The main files are FEE BASIS VENDOR (#161.2), FEE BASIS PATIENT (#161), FEE BASIS PAYMENT (#162), and FEE BASIS INVOICE (#162.5).

## Globals to Journal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that the following globals be journaled.

^FB, ^FBAA, ^FBAAA, ^FBAAC, ^FBAAV, ^FB583, ^FB7078, ^FBAACNH, ^FBAAI

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FILE NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>GLOBAL</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>^FBAAA(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>^FBAAV(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.21</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CNH CONTRACT</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.21,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.22</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CNH RATE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.22,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.23</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CNH AUTHORIZATION RATE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.23,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.25</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR CORRECTION</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.25,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.26</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT MRA</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.26,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.27</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS SUSPENSION</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.27,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.3*</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS LETTER</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.3,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.35</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PROJECT ARCH JUSTIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.35</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.4</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS SITE PARAMETERS</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.4,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.43</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CONTRACT</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.43,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.45</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT MOVES</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.45,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE CH REPORT OF CONTACT</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.5,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.6</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS SPECIALTY CODE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.6,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS BATCH</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.7,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.8</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PROGRAM</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.8,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.81</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PARTICIPATION CODE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.81,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.82</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PURPOSE OF VISIT</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.82,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.83</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS ID CARD AUDIT</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.83,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.9</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAID TO IB FILE</p>
</blockquote></td>
<td><blockquote>
<p>^FB(161.9,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.95</p>
</blockquote></td>
<td><blockquote>
<p>IPAC VENDOR AGREEMENT FILE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.95,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>161.96</p>
</blockquote></td>
<td><blockquote>
<p>IPAC VENDOR AGREEMENT MRA</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.96,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>161.99*</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT REJECT CODE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(161.99,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
<td><blockquote>
<p>^FBAAC(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PHARMACY INVOICE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(162.1,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE NOTIFICATION/REQUEST</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(162.2,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.3</p>
</blockquote></td>
<td><blockquote>
<p>FEE CNH ACTIVITY</p>
</blockquote></td>
<td><blockquote>
<p>^FBAACNH(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
<td><blockquote>
<p>^FB7078(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAAI(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.6</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS DISPOSITION CODE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(162.6,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED CLAIMS</p>
</blockquote></td>
<td><blockquote>
<p>^FB583(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.8</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED CLAIMS PENDING INFO</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(162.8,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.91</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED CLAIMS DISPOSITIONS</p>
</blockquote></td>
<td><blockquote>
<p>^FB(162.91,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.92</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED CLAIMS STATUS</p>
</blockquote></td>
<td><blockquote>
<p>^FB(162.92,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.93*</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED REQUESTED INFORMATION</p>
</blockquote></td>
<td><blockquote>
<p>^FB(162.93,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.94</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED DISAPPROVAL REASONS</p>
</blockquote></td>
<td><blockquote>
<p>^FB(162.94,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.95</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CHECK CANCELLATION REASON</p>
</blockquote></td>
<td><blockquote>
<p>^FB(162.95,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>163.85</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VA TYPE OF SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(163.85,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>163.98</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT METHODOLOGY</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(163.98,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>163.99*</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS FEE SCHEDULE</p>
</blockquote></td>
<td><blockquote>
<p>^FBAA(163.99,</p>
</blockquote></td>
</tr>
</tbody>
</table>

\*File comes with data

\*\*File comes with data, which will overwrite existing data, if specified.

## File Flow Chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 7%" />
<col style="width: 33%" />
<col style="width: 9%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><u>FILE # and NAME</u></strong></td>
<td colspan="2"><blockquote>
<p><strong><u>POINTS TO</u></strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong><u>POINTED TO BY</u></strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>161</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>161.23</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CNH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FEE BASIS PATIENT</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>AUTHORIZATION RATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PHARMACY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.8</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PROGRAM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.82</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PURPOSE OF VISIT</p>
</blockquote></td>
<td><blockquote>
<p>162.3</p>
</blockquote></td>
<td><blockquote>
<p>FEE CNH ACTIVITY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CLAIMS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ICD DIAGNOSIS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

File Flow Chart, cont.<u>FILE \# and NAME</u><u>POINTS TO</u><u>POINTED TO BY</u>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 7%" />
<col style="width: 33%" />
<col style="width: 9%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td>161.2</td>
<td></td>
<td></td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FEE BASIS VENDOR</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>STATE</p>
</blockquote></td>
<td><blockquote>
<p>161.21</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CNH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.6</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS SPECIALTY CODE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CONTRACT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.81</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PARTICIPATION</p>
</blockquote></td>
<td><blockquote>
<p>161.25</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CORRECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>161.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE CH REPORT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>OF CONTACT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PHARMACY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>INVOICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE NOTIFICATION/</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>REQUEST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.3</p>
</blockquote></td>
<td><blockquote>
<p>FEE CNH ACTIVITY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAU-</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>THORIZED CLAIMS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>161.21</td>
<td></td>
<td></td>
<td><blockquote>
<p>161.22</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CNH RATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FEE BASIS CNH</td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>CONTRACT</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>161.22</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FEE BASIS CNH RATE</td>
<td><blockquote>
<p>161.21</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CNH CONTRACT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>161.23</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FEE BASIS CNH</td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>AUTHORIZATION RATE</td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>161.25</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FEE BASIS VENDOR</td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>CORRECTION</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 7%" />
<col style="width: 34%" />
<col style="width: 9%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td>161.26</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FEE BASIS</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PATIENT MRA</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>161.27</td>
<td></td>
<td></td>
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FEE BASIS</td>
<td></td>
<td></td>
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PHARMACY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SUSPENSION</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE NOTIFICATION/</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>REQUEST</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
</tbody>
</table>

File Flow Chart, cont.<u>FILE \# and NAME</u><u>POINTS TO</u><u>POINTED TO BY</u>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 7%" />
<col style="width: 34%" />
<col style="width: 9%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td>161.3</td>
<td></td>
<td></td>
<td><blockquote>
<p>162.92</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHO-</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FEE BASIS LETTER</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RIZED CLAIMS STATUS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>161.4</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FEE BASIS SITE</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>STATE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PARAMETERS</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>161.43</td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FEE BASIS CONTRACT</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>161.5</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FEE CH REPORT</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>STATE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OF CONTACT</td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>162.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE NOTIFICATION/REQUEST</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>392.4</p>
</blockquote></td>
<td><blockquote>
<p>BENEFICIARY TRAVEL MODE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>OF TRANSPORTATION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>161.6</td>
<td></td>
<td></td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FEE BASIS</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>SPECIALTY CODE</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>161.7</td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FEE BASIS BATCH</td>
<td></td>
<td></td>
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PHARMACY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>INVOICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>161.8</td>
<td></td>
<td></td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FEE BASIS PROGRAM</td>
<td></td>
<td></td>
<td><blockquote>
<p>161.82</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PURPOSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>OF VISIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAU-</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>THORIZED CLAIMS</p>
</blockquote></td>
</tr>
</tbody>
</table>

161.9 2 PATIENT

FEE BASIS PAID 355.93 IB NON/OTHER VA BILLING

TO IB PROVIDER

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 33%" />
<col style="width: 1%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 22%" />
<col style="width: 1%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">161.81</td>
<td></td>
<td colspan="2"></td>
<td colspan="3"><blockquote>
<p>161.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2">FEE BASIS</td>
<td></td>
<td colspan="2"></td>
<td colspan="3"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2">PARTICIPATION CODE</td>
<td></td>
<td colspan="2"></td>
<td colspan="3"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>161.82</td>
<td colspan="3"><blockquote>
<p>161.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS PROGRAM</p>
</blockquote></td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>FEE BASIS PURPOSE</td>
<td colspan="3"></td>
<td colspan="2"></td>
<td><blockquote>
<p>162</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>OF VISIT</td>
<td colspan="3"></td>
<td colspan="2"></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>161.83</td>
<td colspan="3"><blockquote>
<p>2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td>FEE BASIS ID</td>
<td colspan="3"><blockquote>
<p>200</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td>CARD AUDIT</td>
<td colspan="3"></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

File Flow Chart, cont.<u>FILE \# and NAME</u><u>POINTS TO</u><u>POINTED TO BY</u>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 9%" />
<col style="width: 35%" />
<col style="width: 7%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td>161.95</td>
<td>161.2</td>
<td>FEE BASIS VENDOR</td>
<td>161.96</td>
<td>IPAC VENDOR AGREEMENT MRA</td>
</tr>
<tr class="even">
<td>IPAC VENDOR AGREEMENT FILE</td>
<td></td>
<td></td>
<td>162</td>
<td>FEE BASIS PAYMENT</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>162.1</td>
<td>FEE BASIS PHARMACY INVOICE</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>162.5</td>
<td>FEE BASIS INVOICE</td>
</tr>
<tr class="odd">
<td>161.96</td>
<td>161.95</td>
<td>IPAC VENDOR AGREEMENT FILE</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>162</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FEE BASIS PAYMENT</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>STATE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ICD DIAGNOSIS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>81</p>
</blockquote></td>
<td><blockquote>
<p>CPT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>81.3</p>
</blockquote></td>
<td><blockquote>
<p>CPT MODIFIER</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.27</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS SUSPENSION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS BATCH</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.8</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PROGRAM</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.82</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PURPOSE OF VISIT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.91</p>
</blockquote></td>
<td><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.92</p>
</blockquote></td>
<td><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.95</p>
</blockquote></td>
<td><blockquote>
<p>IPAC VENDOR AGREEMENT FILE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>CLAIMS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>162.95</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS CHECK CANCELLATION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>REASON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>163.85</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VA TYPE OF SERVICE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>163.98</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT METHODOLOGY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>353.1</p>
</blockquote></td>
<td><blockquote>
<p>PLACE OF SERVICE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>353.2</p>
</blockquote></td>
<td><blockquote>
<p>TYPE OF SERVICE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>162.1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FEE BASIS</td>
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>DRUG</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PHARMACY INVOICE</td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.27</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS SUSPENSION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS BATCH</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.95</p>
</blockquote></td>
<td><blockquote>
<p>IPAC VENDOR AGREEMENT FILE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CLAIMS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.95</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS CHECK CANCELLATION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>REASON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>162.2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>161.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE CH REPORT OF</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FEE NOTIFICATION/</td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CONTACT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>REQUEST</td>
<td><blockquote>
<p>161.27</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS SUSPENSION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>162.3</td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>162.3</p>
</blockquote></td>
<td><blockquote>
<p>FEE CNH ACTIVITY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FEE CNH ACTIVITY</td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.3</p>
</blockquote></td>
<td><blockquote>
<p>FEE CNH ACTIVITY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

File Flow Chart, cont.<u>FILE \# and NAME</u><u>POINTS TO</u><u>POINTED TO BY</u>

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 7%" />
<col style="width: 32%" />
<col style="width: 8%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>162.4</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA FORM 10-7078</td>
<td><blockquote>
<p>43.4</p>
</blockquote></td>
<td><blockquote>
<p>VA ADMITTING REGULATION</p>
</blockquote></td>
<td><blockquote>
<p>161.23</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS CNH AUTHO-</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>RIZATION RATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.8</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PROGRAM</p>
</blockquote></td>
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PHARMACY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE NOTIFICATION/</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>REQUEST</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>162.5</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FEE BASIS INVOICE</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>STATE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ICD DIAGNOSIS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>80.1</p>
</blockquote></td>
<td><blockquote>
<p>ICD OPERATION/PROCEDURE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>80.2</p>
</blockquote></td>
<td><blockquote>
<p>DRG</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.27</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS SUSPENSION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS BATCH</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.8</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PROGRAM</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.82</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PURPOSE OF VISIT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.91</p>
</blockquote></td>
<td><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.92</p>
</blockquote></td>
<td><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>161.95</p>
</blockquote></td>
<td><blockquote>
<p>IPAC VENDOR AGREEMENT FILE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>VA FORM 10-7078</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>162.6</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS DISPOSITION CODE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CLAIMS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.95</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS CHECK CANCELLATION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>REASON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>162.6</td>
<td></td>
<td></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FEE BASIS</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DISPOSITION CODE</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>162.7</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FEE BASIS</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>UNAUTHORIZED</td>
<td><blockquote>
<p>161.2</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PHARMACY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CLAIMS</td>
<td><blockquote>
<p>161.8</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS PROGRAM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CLAIMS</p>
</blockquote></td>
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.91</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CLAIMS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CLAIMS DISPOSITIONS</p>
</blockquote></td>
<td><blockquote>
<p>162.8</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.92</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CLAIMS PENDING INFO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CLAIMS STATUS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>162.94</p>
</blockquote></td>
<td><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>DISAPPROVAL REASONS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ICD DIAGNOSIS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

File Flow Chart, cont.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 27%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><u>FILE # and NAME</u></strong></td>
<td colspan="4"><blockquote>
<p><strong><u>POINTS TO</u></strong></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p><strong><u>POINTED TO BY</u></strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>162.8</td>
<td colspan="2"><blockquote>
<p>162.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td>FEE BASIS</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>CLAIMS</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td>UNAUTHORIZED</td>
<td colspan="2"><blockquote>
<p>162.93</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td>CLAIMS PENDING</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>REQUESTED INFORMATION</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td>INFO</td>
<td colspan="2"><blockquote>
<p>200</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">162.91</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>162.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS UNAUTHO-</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4">FEE BASIS UNAUTHORIZED</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>RIZED CLAIMS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2">CLAIMS DISPOSITIONS</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2">162.92</td>
<td colspan="2"><blockquote>
<p>161.3 FEE BASIS LETTER</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>162.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS UNAUTHO-</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2">FEE BASIS UNAUTHO-</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>RIZED CLAIMS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2">RIZED CLAIMS STATUS</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2">162.93</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="4">FEE BASIS UNAUTHORIZED</td>
<td colspan="2"><blockquote>
<p>162.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS UNAUTHORIZED</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4">REQUESTED INFORMATION</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>CLAIMS PENDING INFO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2">162.94</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>162.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS UNAUTHO-</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4">FEE BASIS UNAUTHORIZED</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>RIZED CLAIMS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2">DISAPPROVAL REASONS</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2">162.95</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>162</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2">FEE BASIS CHECK</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>162.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS PHARMACY</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4">CANCELLATION REASON</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>INVOICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2">163.85</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>162</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2">FEE BASIS VA TYPE</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2">OF SERVICE</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 43%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FILE #</strong></th>
<th><strong>TEMPLATE</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>161</td>
<td><p>FBAA AUTHORIZATION FBAA REPORT OF CONTACT FBNH EDIT AUTHORIZATION</p>
<p>FBNH ENTER AUTHORIZATION</p>
<p>FB UNAUTHORIZED UPDATE</p>
<p>FB UNAUTHORIZED EDIT</p></td>
<td><p>Enter medical authorization. Enter outpatient report of contact. Edit CNH authorization.</p>
<p>Enter CNH authorization.</p>
<p>Enter authorization based on discharge type of unauthorized claim.</p>
<p>If dispositioned claim has been reopened, this template is used to keep the authorization information in synch with the unauthorized claim.</p></td>
</tr>
<tr class="even">
<td>161.2</td>
<td>FBAA EDIT VENDOR FBAA NEW VENDOR FB VENDOR UPDATE</td>
<td><p>Edit Fee Basis vendor.</p>
<p>Enter new vendor.</p></td>
</tr>
<tr class="odd">
<td>161.21</td>
<td>FBNH ENTER CONTRACT</td>
<td>Update Austin vendor information. Enter Contract Nursing Home contract information.</td>
</tr>
<tr class="even">
<td>161.25</td>
<td>FBAA VENDOR MRA</td>
<td>Create a vendor MRA to send to Austin.</td>
</tr>
<tr class="odd">
<td>161.3</td>
<td>FBAA LETTERS</td>
<td>Enter suspension letters.</td>
</tr>
<tr class="even">
<td>161.4</td>
<td>FBAA SITE PARAMETERS</td>
<td>Enter/Edit site parameters.</td>
</tr>
<tr class="odd">
<td>161.5</td>
<td>FBCH ADD ROC</td>
<td>Add CH report of contact.</td>
</tr>
<tr class="even">
<td></td>
<td>FBCH EDIT ROC</td>
<td>Edit CH report of contact.</td>
</tr>
<tr class="odd">
<td></td>
<td>FBCH ENTER ROC</td>
<td>Enter CH report of contact.</td>
</tr>
<tr class="even">
<td>161.7</td>
<td>FBAA BATCH EDIT</td>
<td>Edit a batch.</td>
</tr>
<tr class="odd">
<td></td>
<td>FBAA MED IFCAP</td>
<td>Open a medical batch.</td>
</tr>
<tr class="even">
<td></td>
<td>FBAA PHARM IFCAP</td>
<td>Open a pharmacy batch.</td>
</tr>
<tr class="odd">
<td></td>
<td>FBAA TRAV IFCAP</td>
<td>Open a travel batch.</td>
</tr>
<tr class="even">
<td></td>
<td>FB CH OPEN BATCH</td>
<td>Open a CH batch.</td>
</tr>
<tr class="odd">
<td></td>
<td>FB CHNH OPEN BATCH</td>
<td>Open a CNH batch.</td>
</tr>
<tr class="even">
<td>162.1</td>
<td>FB ADD RX</td>
<td>Add a pharmacy prescription.</td>
</tr>
<tr class="odd">
<td>162.2</td>
<td>FBCH ENTER REQUEST</td>
<td>Enter a CH request/notification.</td>
</tr>
<tr class="even">
<td></td>
<td>FBCH REOPEN REQUEST</td>
<td>Reopen a CH request/notification.</td>
</tr>
<tr class="odd">
<td>162.4</td>
<td>FBCH EDIT 7078</td>
<td>Edit a CH 7078.</td>
</tr>
<tr class="even">
<td></td>
<td>FBCH ENTER 7078</td>
<td>Enter a CH 7078.</td>
</tr>
<tr class="odd">
<td></td>
<td>FBNH ENTER 7078</td>
<td>Enter a CNH 7078.</td>
</tr>
<tr class="even">
<td>162.5</td>
<td>FBCH EDIT PAYMENT</td>
<td>Edit a CH invoice.</td>
</tr>
<tr class="odd">
<td></td>
<td>FBCH ENTER PAYMENT</td>
<td>Enter a CH invoice.</td>
</tr>
<tr class="even">
<td></td>
<td>FBNH EDIT PAYMENT</td>
<td>Edit a CNH invoice.</td>
</tr>
<tr class="odd">
<td>162.7</td>
<td>FBCH UNAUTHORIZED CLAIM</td>
<td>Enter a CH unauthorized claim.</td>
</tr>
<tr class="even">
<td></td>
<td>FB UNAUTHORIZED ENTER</td>
<td>Enter an unauthorized claim.</td>
</tr>
<tr class="odd">
<td></td>
<td>FB UNAUTHORIZED UPDATE</td>
<td>Update certain unauthorized claims fields upon completion of enter/edit.</td>
</tr>
<tr class="even">
<td></td>
<td>FB UNAUTHORIZED EDIT</td>
<td>Modify/reopen an unauthorized claim.</td>
</tr>
<tr class="odd">
<td></td>
<td>FB UNAUTHORIZED APPEAL</td>
<td>Initiate appeal of unauthorized claim.</td>
</tr>
<tr class="even">
<td></td>
<td>FB UNAUTHORIZED APPEAL EDIT</td>
<td>Edit unauthorized claim.</td>
</tr>
<tr class="odd">
<td></td>
<td>FB UNAUTHORIZED COVA APPEAL</td>
<td>COVA appeal enter/edit.</td>
</tr>
<tr class="even">
<td></td>
<td>FB UNAUTHORIZED DISPOSITION</td>
<td>Disposition an unauthorized claim.</td>
</tr>
<tr class="odd">
<td></td>
<td>FB UNAUTHORIZED PREVIOUS</td>
<td>Return previous values due to incomplete transaction.</td>
</tr>
<tr class="even">
<td></td>
<td>FB UNAUTHORIZED LETTER UPDATE</td>
<td>Update unauthorized claim with information regarding letter (used if not sending letters with software).</td>
</tr>
<tr class="odd">
<td>162.8</td>
<td>FB UNAUTHORIZED PENDING</td>
<td>Enter the appropriate information on pending</td>
</tr>
<tr class="even">
<td>163.99</td>
<td>FBAA EDIT SCHEDULE</td>
<td>Edit Fee schedule.</td>
</tr>
</tbody>
</table>

### Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TEMPLATE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>161.7</p>
</blockquote></td>
<td><blockquote>
<p>FB BATCH LIST</p>
</blockquote></td>
<td><blockquote>
<p>List batch.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>FB UCID PAYMENT</p>
</blockquote></td>
<td><blockquote>
<p>List Unique Claim ID info for a FB Outpatient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FBAA RX PENDING</p>
</blockquote></td>
<td><blockquote>
<p>Prescriptions pending pharmacy review.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.2</p>
</blockquote></td>
<td><blockquote>
<p>FBCH PENDING REQUEST</p>
</blockquote></td>
<td><blockquote>
<p>Fee notifications/requests pending</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>FBCH 7078 CANCEL</p>
</blockquote></td>
<td><blockquote>
<p>Listing of cancelled 7078s.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FBUC STATUS BY PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>Status listing of unauthorized claims by patient.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>FBUC STATUS BY VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>Status listing of unauthorized claims by vendor.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Sort Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TEMPLATE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>161.7</p>
</blockquote></td>
<td><blockquote>
<p>FB BATCH LIST</p>
</blockquote></td>
<td><blockquote>
<p>List batch.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.1</p>
</blockquote></td>
<td><blockquote>
<p>FBAA RX PENDING</p>
</blockquote></td>
<td><blockquote>
<p>Prescriptions pending pharmacy review.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.2</p>
</blockquote></td>
<td><blockquote>
<p>FBCH PENDING REQUEST</p>
</blockquote></td>
<td><blockquote>
<p>Fee notifications/requests pending entitlement.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td><blockquote>
<p>FBCH 7078 CANCEL</p>
</blockquote></td>
<td><blockquote>
<p>Listing of cancelled 7078s.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162.7</p>
</blockquote></td>
<td><blockquote>
<p>FBUC STATUS BY PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>Status listing of unauthorized claims by patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>FBUC STATUS BY VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>Status listing of unauthorized claims by vendor.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Modifications to Fee Basis Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Changes to File \#161 for FB\*3.5\*119 as part of Project ARCH

GLOBAL MAP DATA DICTIONARY \#161 -- FEE BASIS PATIENT FILE

JUN 2,2011@07:51:27 PAGE 3 STORED IN ^FBAAA( (20 ENTRIES) SITE: SITENAME UCI: DEV,DEV

(VERSION 3.5)

-----------------------------------------------------------------------------

^FBAAA(D0,1,D1,100)= (#100) CLERK \[1P:200\] ^

^FBAAA(D0,1,D1,ADEL)= (#102) AUSTIN DELETE FLAG \[1F\] ^ (#103) DATE DELETE MRA ==\>TRANSMITTED \[2D\] ^

^FBAAA(D0,1,D1,C)= (#1) PRINT AUTHORIZATION (Y/N) \[1F\] ^ ^FBAAA(D0,2,0)=^161.02D^^ (#2) REPORT OF CONTACT

^FBAAA(D0,2,D1,0)= (#.01) DATE OF CONTACT \[1D\] ^ (#1) VENDOR/PROVIDER \[2F\] ^ ==\>(#1.5) VENDOR/PROVIDER TELEPHONE NO. \[3F\] ^ (#3) DX \[4F\] ^ ==\>(#5) INPUT DATE \[5D\] ^ (#3.5) TYPE OF CONTACT \[6S\] ^

^FBAAA(D0,2,D1,1,0)=^161.04^^ (#2) NARRATIVE ^FBAAA(D0,2,D1,1,D2,0)= (#.01) NARRATIVE \[1W\] ^ ^FBAAA(D0,2,D1,100)= (#100) CLERK \[1P:200\] ^

^FBAAA(D0,4)= (#.5) FEE ID CARD NUMBER \[1F\] ^ (#.6) FEE ID CARD ISSUE DATE ==\>\[2D\] ^ (#.7) REASON FOR CARD NUMBER CHANGE \[3F\] ^ (#.65) FEE ID ==\>CARD EXPIRATION DATE \[4D\] ^

^FBAAA(D0,ARCHFEE,0)=^161.011D^^ (#11) ARCH ELIGIBILITY ^FBAAA(D0,ARCHFEE,D1,0)= (#.01) ARCH ELIGIBILITY DATE \[1D\] ^ (#2) ARCH

> ==\>ELIGIBILITY \[2S\] ^

Changes to Fee Basis Invoice file (#162.5) for FB\*3.5\*121/FB\*3.5\*122/FB\*3.5\*135 as part of Fee 5010 EDI

…partial DD…

^FBAAI(D0,2)= (#45) DATE PAID \[1D\] ^ (#46) VENDOR INVOICE DATE \[2D\] ^ (#47) ==\>PROMPT PAY TYPE \[3S\] ^ (#48) CHECK NUMBER \[4F\] ^ (#49) ==\>CANCELLATION DATE \[5D\] ^ (#50) REASON CODE \[6P:162.95\] ^ (#51) ==\>CANCELLATION ACTIVITY \[7S\] ^ (#52) DISBURSED AMOUNT \[8N\] ^ ==\>(#53) INTEREST AMOUNT \[9N\] ^ (#54) COVERED DAYS \[10N\] ^ (#55) ==\>PATIENT CONTROL NUMBER \[11F\] ^ (#24.5) DRG WEIGHT \[12N\] ^ ==\>(#61) ROUTING NUMBER \[13F\] ^ (#62) ACCOUNT NUMBER \[14F\] ^ ==\>(#63) FINANCIAL INSTITUTION \[15F\]

^FBAAI(D0,4)= (#64) ATTENDING PROV NAME \[1F\] ^ (#65) ATTENDING PROV NPI \[2F\]

> ==\>^ (#66) ATTENDING PROV TAXONOMY CODE \[3F\] ^ (#67) OPERATING ==\>PROV NAME \[4F\] ^ (#68) OPERATING PROV NPI \[5F\] ^ (#69) ==\>RENDERING PROV NAME \[6F\] ^ (#70) RENDERING PROV NPI \[7F\] ^ ==\>(#71) RENDERING PROV TAXONOMY CODE \[8F\] ^ (#72) SERVICING PROV ==\>NAME \[9F\] ^ (#73) SERVICING PROV NPI \[10F\] ^ (#74) REFERRING ==\>PROV NAME \[11F\] ^ (#75) REFERRING PROV NPI \[12F\] ^

^FBAAI(D0,5)= (#80) SERVICING FACILITY ADDRESS \[1F\] ^ (#81) SERVICING ==\>FACILITY CITY \[2F\] ^ (#82) SERVICING FACILITY STATE \[3P:5\] ^ ==\>(#83) SERVICING FACILITY ZIP \[4F\] ^

==\>(#83) SERVICING FACILITY ZIP \[4F\] ^ (#85) UNIQUE CLAIM

==\>IDENTIFIER \[5F\] ^

^FBAAI(D0,RPROV,0)=^162.579^^ (#79) LINE ITEM RENDERING PROV ^FBAAI(D0,RPROV,D1,0)=(#.01) LINE ITEM NUMBER \[1N\] ^ (#.02) RENDERING

> ==\>PROV NAME \[2F\] ^ (#.03) RENDERING PROV NPI \[3F\] ==\>RENDERING PROV TAXONOMY CODE \[4F\]

Changes to Fee Basis Invoice file (#162.5) for FB\*3.5\*123 as part of VA/DoD VistA Fee IPAC Interface Enhancement

…partial DD…

^FBAAI(D0,5)= (#80) SERVICING FACILITY ADDRESS \[1F\] ^ (#81) SERVICING

==\>FACILITY CITY \[2F\] ^ (#82) SERVICING FACILITY STATE \[3P:5\] ^

==\>(#83) SERVICING FACILITY ZIP \[4F\] ^ (#85) UNIQUE CLAIM

==\>IDENTIFIER \[5F\] ^ ^ (#86) DoD INVOICE NUMBER \[7F\] ^ (#60)

==\>CONTRACT \[8P:161.43\] ^ (#39) ADMITTING DIAGNOSIS \[9P:80\] ^

==\>(#87) IPAC VENDOR AGREEMENT \[10P:161.95\] ^

Changes to Fee Basis Site Parameters file (#161.4) for FB\*3.5\*121/FB\*3.5\*135 as part of Fee 5010 EDI

…partial DD…

^FBAA(161.4,D0,2)= (#36) FPPS TRANSMIT START \[1D\] ^ (#37) FPPS TRANSMIT END

> ==\>\[2D\] ^ (#39) UNIQUE CLAIM IDENTIFIER SEQ \[3F\] ^

> ==\> (#40) ALLOW FB PAID TO IB \[4S\]

Changes to Fee Basis Site Parameters file (#161.4) for FB\*3.5\*123 as part of VA/DoD VistA Fee IPAC Interface Enhancement

…partial DD…

^FBAA(161.4,D0,IPAC)= (#80) LAST IPAC NUMBER \[1N\] ^

Changes to Fee Basis Vendor file (#161.2) for FB\*3.5\*121 as part of Fee 5010 EDI

…partial DD…

^FBAAV(D0,3)= ^ (#41.01) NPI \[2F\] ^ (#42) TAXONOMY CODE \[3F\]

Changes to Fee Basis Payment file (#162) for FB\*3.5\*121/FB\*3.5\*133/FB\*3.5\*135 as part of Fee 5010 EDI

…partial DD…

FBAAC(D0,1,D1,1,D2,1,D3,2)= (#33) VENDOR INVOICE DATE \[1D\] ^ (#34) PROMPT

==\>PAY TYPE \[2S\] ^ (#35) CHECK NUMBER \[3F\] ^ (#36)

==\>CANCELLATION DATE \[4D\] ^ (#37) REASON CODE

==\>\[5P:162.95\] ^ (#38) CANCELLATION ACTIVITY \[6S\] ^

==\> ^ (#40) DISBURSED AMOUNT \[8N\] ^ (#41) INTEREST

==\>AMOUNT \[9N\] ^ (#42) SITE OF SERVICE ZIP CODE

==\>\[10F\] ^ (#43) ANESTHESIA TIME (MINUTES) \[11N\] ^

==\>(#44) FEE SCHEDULE AMOUNT \[12N\] ^ (#45) FEE

==\>SCHEDULE \[13S\] ^ (#47) UNITS PAID \[14N\] ^ (#48)

==\>REVENUE CODE \[15P:399.2\] ^ (#49) PATIENT ACCOUNT

==\>NUMBER \[16F\] ^ (#55) ROUTING NUMBER \[17F\] ^

==\>(#56) ACCOUNT NUMBER \[18F\] ^ (#57) FINANCIAL

==\>INSTITUTION \[19F\] ^

^FBAAC(D0,1,D1,1,D2,1,D3,3)= (#50) FPPS CLAIM ID \[1F\] ^ (#51) FPPS LINE ITEM

==\>\[2F\] ^ (#73) LI RENDERING PROV NAME \[3F\] ^ (#74)

==\>LI RENDERING PROV NPI \[4F\] ^ (#75) LI RENDERING

==\>PROV TAXONOMY \[5F\] ^

^FBAAC(D0,1,D1,1,D2,1,D3,4)= (#58) ATTENDING PROV NAME \[1F\] ^ (#59) ATTENDING

==\>PROV NPI \[2F\] ^ (#60) ATTENDING PROV TAXONOMY

==\>CODE \[3F\] ^ (#61) OPERATING PROV NAME \[4F\] ^

==\>(#62) OPERATING PROV NPI \[5F\] ^ (#63) RENDERING

==\>PROV NAME \[6F\] ^ (#64) RENDERING PROV NPI \[7F\] ^

==\>(#65) RENDERING PROV TAXONOMY CODE \[8F\] ^ (#66)

==\>SERVICING PROV NAME \[9F\] ^ (#67) SERVICING PROV

==\>NPI \[10F\] ^ (#68) REFERRING PROV NAME \[11F\] ^

==\>(#69) REFERRING PROV NPI \[12F\] ^

^FBAAC(D0,1,D1,1,D2,1,D3,5)= (#76) SERVICING FACILITY ADDRESS \[1F\] ^ (#77)

==\>SERVICING FACILITY CITY \[2F\] ^ (#78) SERVICING

==\>FACILITY STATE \[3P:5\] ^ (#79) SERVICING FACILITY

==\>ZIP \[4F\] ^ (#81) UNQIUE CLAIM IDENTIFIER \[5F\]

Changes to Fee Basis Payment file (#162) for FB\*3.5\*123 as part of VA/DoD VistA Fee IPAC Interface Enhancement

…partial DD…

^FBAAC(D0,1,D1,1,D2,1,D3,3)= (#50) FPPS CLAIM ID \[1F\] ^ (#51) FPPS LINE ITEM

==\>\[2F\] ^ (#73) LI RENDERING PROV NAME \[3F\] ^ (#74)

==\>LI RENDERING PROV NPI \[4F\] ^ (#75) LI RENDERING

==\>PROV TAXONOMY \[5F\] ^ (#.05) IPAC AGREEMENT

==\>\[6P:161.95\] ^ (#.055) DoD INVOICE NUMBER \[7F\] ^

==\>(#54) CONTRACT \[8P:161.43\] ^

New file (#161.9) for /FB\*3.5\*135 as part of Fee 5010 EDI

^FB(161.9,D0,0)= (#.01) PATIENT \[1P:2\] ^ (#.02) PROGRAM \[2S\] ^ (#.03) FB

==\>INTERNAL CONTROL NUMBER \[3F\] ^ (#.04) PROCESS DATE \[4D\] ^

==\>(#.05) LI NUMBER \[5N\] ^ (#.06) PROVIDER TYPE \[6S\] ^ (#.07)

==\>IB NON/OTHER PROVIDER \[7P:355.93\] ^ (#.08) NPI ADDED \[8S\] ^

==\>(#.09) TAXONOMY ADDED \[9S\]

Changes to File \#161 for FB\*3.5\*139 as part of ICD-10 Remediation

…partial DD…

^FBAAA(D0,1,D1,C)= ^ (#.087) ICD DIAGNOSIS \[2P:80\] ^

Changes to File \#162.7 for FB\*3.5\*139 as part of ICD-10 Remediation

…partial DD…

^FB583(D0,DX)= ^ (#5.1) ICD DIAGNOSIS \[2P:80\] ^

Changes to Fee Basis Pharmacy Invoice file (#162.1) for FB\*3.5\*123 as part of VA/DoD VistA Fee IPAC Interface Enhancement

…partial DD…

^FBAA(162.1,D0,0)= (#.01) NUMBER \[1N\] ^ (#1) DATE CORRECT INVOICE RECV'D \[2D\]

==\>^ (#2) DATA ENTRY CLERK \[3P:200\] ^ (#3) VENDOR \[4P:161.2\]

==\>^ (#5) INVOICE STATUS \[5S\] ^ (#6) TOTAL AMOUNT CLAIMED

==\>\[6N\] ^ (#7) TOTAL AMOUNT PAID \[7N\] ^ (#1.5) DATE INVOICE

==\>ENTERED \[8D\] ^ (#8) TOTAL LINE COUNT \[9N\] ^ (#9) GENERIC

==\>DRUG NAME STATUS \[10S\] ^ (#10) BATCH ASSIGNED \[11P:161.7\]

==\>^ (#12) VENDOR INVOICE DATE \[12D\] ^ (#13) FPPS CLAIM ID

==\>\[13F\] ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ (#14) IPAC VENDOR

==\>AGREEMENT \[23P:161.95\] ^

^FBAA(162.1,D0,RX,D1,6)= (#39) DoD INVOICE NUMBER \[1F\] ^

Changes to Fee Basis Payment file (#162) for FB\*3.5\*158 as part of the Health Administration Product Enhancements (HAPE EDI PC) – Electronic Remittance Advice (ERA) Compliance project…partial DD…

^FBAAC(D0,1,D1,1,D2,1,D3,2)= (#33) VENDOR INVOICE DATE \[1D\] ^ (#34) PROMPT

==\>PAY TYPE \[2S\] ^ (#35) CHECK NUMBER \[3F\] ^ (#36)

==\>CANCELLATION DATE \[4D\] ^ (#37) REASON CODE

==\>\[5P:162.95\] ^ (#38) CANCELLATION ACTIVITY \[6S\] ^

==\>(#82) PAYMENT METHODOLOGY \[7P:163.98\] ^

^FBAAC(D0,1,D1,1,D2,1,D3,8,0)=^162.08P^^ (#53) REMITTANCE REMARK

^FBAAC(D0,1,D1,1,D2,1,D3,8,D4,0)= (#.01) REMITTANCE REMARK \[1P:161.93\] ^ (#1)

==\>ADJUSTMENT \[2N\] ^

^FBAAC(D0,1,D1,1,D2,1,D3,9)= (#83) AUTHORIZATION NUMBER \[1F\] ^

Changes to Fee Basis Pharmacy Invoice file (#162.1) for FB\*3.5\*158 as part of the HAPE EDI PC – ERA Compliance project

…partial DD…

^FBAA(162.1,D0,RX,D1,5,0)=^162.15P^^ (#38) REMITTANCE REMARK

^FBAA(162.1,D0,RX,D1,5,D2,0)= (#.01) REMITTANCE REMARK \[1P:161.93\] ^ (#1)

==\>ADJUSTMENT \[2N\] ^

^FBAA(162.1,D0,RX,D1,3)= (#36) FPPS LINE ITEM \[1F\] ^ (#40) AUTHORIZATION

==\>NUMBER \[2F\] ^

Changes to Fee Basis Invoice file (#162.5) for FB\*3.5\*158 as part of the HAPE EDI PC – ERA Compliance project

…partial DD…

^FBAAI(D0,7)= (#88) AUTHORIZATION NUMBER \[1F\] ^

^FBAAI(D0,9,0)=^162.559P^^ (#59) REMITTANCE REMARK

^FBAAI(D0,9,D1,0)= (#.01) REMITTANCE REMARK \[1P:161.93\] ^ (#1) ADJUSTMENT

==\>\[2N\] ^

Changes to Adjustment Reason file (#161.91) for FB\*3.5\*158 as part of the HAPE EDI PC – ERA Compliance project

…partial DD…

^FB(161.91,D0,RARC,0)=^161.915P^^ (#5) REMITTANCE REMARK

^FB(161.91,D0,RARC,D1,0)= (#.01) REMITTANCE REMARK \[1P:161.93\] ^

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Fee Basis Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fee Basis Main Menu \[FBAA MAIN MENU\]Civil Hospital Main Menu ... \[FBCH MAIN MENU\]

Notification/Request Menu ... \[FBCH NOTIFICATION MENU\]

> Enter a Request/Notification \[FBCH ENTER REQUEST\]

> Notification/Request Edit \[FBCH EDIT REQUEST\]

> Legal Entitlement \[FBCH LEGAL ENTITLEMENT\]

> Medical Entitlement \[FBCH MEDICAL ENTITLEMENT\]

> Display a Request/Notification \[FBCH DISPLAY REQUEST\]

> Delete Notification/Request \[FBCH DELETE REQUEST\]

> Edit Report of Contact - CH \[FBCH EDIT REPORT OF CONTACT\]

> Print Entitlement Audit \[FBCH PRINT REQUEST AUDIT\]

> \*\*\> Locked with FBAASUPERVISOR

> Print Report of Contact - CH \[FBCH PRINT REPORT OF CONTACT\]

> Reconsider a Denied Request \[FBCH REOPEN REQUEST\]

> \*\*\> Locked with FBAASUPERVISOR

> Requests Pending Entitlement \[FBCH PENDING REQUEST\]

> Update Report of Contact - CH \[FBCH UPDATE REPORT OF CONTACT\]

Disposition Menu ... \[FBCH DISPOSITION MENU\]

> Complete 7078/Authorization \[FBCH COMPLETE 7078\]

> Edit Completed 7078 \[FBCH EDIT 7078\]

> Display 7078/Authorization \[FBCH DISPLAY 7078\]

> Cancel 7078 Entered in Error \[FBCH CANCEL 7078\]

> \*\*\> Locked with FBAASUPERVISOR

> Print List of Cancelled 7078 \[FBCH PRINT CANCELLED 7078\]

> \*\*\> Locked with FBAASUPERVISOR

> Set-up a 7078 \[FBCH 7078 SETUP\]

Payment Process Menu ... \[FBCH PAYMENT MENU\]

> Ancillary Contract Hosp/CNH Payment \[FBCH ANCILLARY PAYMENT\]

> Complete a Payment \[FBCH COMPLETE PAYMENT\]

> Delete Inpatient Invoice \[FBCH DELETE INVOICE\]

> Edit Ancillary Payment \[FBCH EDIT ANCILLARY PAYMENT\]

> Enter Invoice/Payment \[FBCH ENTER PAYMENT\]

> Invoice Edit \[FBCH EDIT PAYMENT\]

> Multiple Ancillary Payments \[FBCH MULTIPLE PAYMENTS\]

> Patient Reimbursement for Ancillary Services \[FBCH ANCILLARY REIMBURSEMENT\]

> Reimbursement for Inpatient Hospital Invoice \[FBCH REIMBURSEMENT INVOICE\]

Batch Main Menu - CH ... \[FBCH BATCH OPTIONS\]

> Open a Batch \[FBCH OPEN BATCH\]

> Edit Batch data \[FBAA BATCH EDIT\]

> Close-out Batch \[FBAA CLOSE BATCH\]

> Re-open Batch \[FBAA REOPEN BATCH\]

> Pricer Batch Release \[FBCH PRICER RELEASE\]

> Re-initiate Pricer Rejected Items \[FBCH REINITIATE PRICER REJECTS\]

> Release a Batch \[FBAA SUPERVISOR RELEASE\]

> \*\*\> Locked with FBAASUPERVISOR

> Finalize a Batch \[FBAA FINALIZE BATCH\]

> Re-initiate Rejected Payment Items \[FBAA REINITIATE REJECTS\]

> Delete reject flag \[FBAA VOUCHER DELETE REJECT\]

> \*\*\> Locked with FBAAREJECT

> Status of Batch \[FBAA BATCH STATUS\]

> List Items in Batch \[FBAA LIST BATCH\]

> Batch Delete \[FBAA BATCH DELETE\]

> Open Ancillary Payment Batch \[FBCH OPEN ANCILLARY BATCH\]

Output Menu ... \[FBCH OUTPUT MENU\]

> 7078 Print \[FBCH PRINT 7078\]

> Check Display \[FB CHECK DISPLAY\]

> Civil Hospital Census Report \[FBCH CENSUS REPORT\]

> Cost Report for Civil Hospital \[FBCH COST REPORT\]

> Display Open Batches \[FBAA DISPLAY OPEN BATCHES\]

> FPPS Claim Inquiry \[FB FPPS CLAIM INQ\]

> Invoice Display \[FBCH INVOICE DISPLAY\]

> IPAC Vendor Reports ... \[FBAA IPAC VENDOR REPORT MENU\]

> DoD Invoice Number Inquiry \[FBAA IPAC DoD INVOICE INQUIRY\]

> IPAC Vendor DoD Invoice Report (Summary) \[FBAA IPAC DoD INVOICE RPT\]

> IPAC Vendor Payment Report (Detail) \[FBAA IPAC VENDOR PAYMENT RPT\]

> List Batches Pending Release \[FBAA LIST CLOSED BATCHES\]

> Non-VA Hospital Activity Report \[FBCH HOSPITAL ACTIVITY\]

> Payment Aging Report \[FB PAYMENT AGING RPT\]

> Pending Pricer Rejects \[FBCH PRICER REJECTS\]

> Potential Cost Recovery Report \[FB PCR\]

> Print Rejected Payment Items \[FBAA REJECT PRINT\]

> Request Statistics \[FBCH REQUEST STATS\]

> Unauthorized Claims Cost Report for Civil Hospital \[FBCH UC COST REPORT\]

> Vendor Payments Output \[FB PAY VENDOR\]

> Veteran Payments Output \[FB PAY VETERAN\]

Generic Pricer Interface \[FBCH GENERIC PRICER\]

Queue Data for Transmission \[FBAA QUEUE DATA FOR TRANS.\]

\*\*\> Locked with FBAASUPERVISOR

Community Nursing Home Main Menu ... \[FBCNH MAIN MENU\]

Authorization Main Menu - CNH ... \[FBCNH AUTHORIZATION MAIN MENU\]

> Enter CNH Authorization \[FBCNH ENTER AUTHORIZATION\]

> Edit CNH Authorization \[FBCNH EDIT AUTHORIZATION\]

> Cancel Authorization Entered in Error \[FBCNH CANCEL 7078\]

> \*\*\> Locked with FBAASUPERVISOR

> Change Existing Contract Rate for a Patient \[FBCNH RATE CHANGE\]

> Delete CNH Rate \[FBCNH DELETE RATE\]

> Display 7078/Authorization - CNH \[FBCNH DISPLAY 7078\]

> Enter Veteran Rates under new Vendor Contract \[FBCNH ENTER VETERAN RATES\]

> Print List of Cancelled 7078 \[FBCH PRINT CANCELLED 7078\]

> \*\*\> Locked with FBAASUPERVISOR

Batch Main Menu - CNH ... \[FBCNH BATCH MAIN MENU\]

> Batch Delete \[FBAA BATCH DELETE\]

> Close-out Batch \[FBAA CLOSE BATCH\]

> Delete reject flag \[FBAA VOUCHER DELETE REJECT\]

> \*\*\> Locked with FBAAREJECT

> Display Open Batches \[FBAA DISPLAY OPEN BATCHES\]

> Edit Batch data \[FBAA BATCH EDIT\]

> Finalize a Batch \[FBAA FINALIZE BATCH\]

> List Batches Pending Release \[FBAA LIST CLOSED BATCHES\]

> List Items in Batch \[FBAA LIST BATCH\]

> Open CNH Batch \[FBCNH OPEN BATCH\]

> Re-initiate Rejected Payment Items \[FBAA REINITIATE REJECTS\]

> Re-open Batch \[FBAA REOPEN BATCH\]

> Release a Batch \[FBAA SUPERVISOR RELEASE\]

> \*\*\> Locked with FBAASUPERVISOR

> Status of Batch \[FBAA BATCH STATUS\]

Fee Fund Control Main Menu - CNH ... \[FBCNH FUND CONTROL MAIN MENU\]

> Estimate Funds for Obligation \[FBCNH ESTIMATE FUNDS\]

> Post Commitments for Obligation \[FBCNH POST COMMITMENTS\]

LTC CNH Active Authorizations Report \[FBCNH LTC ACTIVE AUTHORIZ\]

LTC CNH Ending Authorizations Report \[FBCNH LTC ENDING AUTHORIZ\]

Movement Main Menu - CNH ... \[FBCNH MOVEMENT MAIN MENU\]

> Admit To CNH \[FBCNH ADMIT\]

> Delete Movement Menu ... \[FBCNH DELETE MOVEMENT MENU\]

> Admission Delete \[FBCNH DELETE ADMISSION\]

> Discharge Delete \[FBCNH DELETE DISCHARGE\]

> Transfer Delete \[FBCNH DELETE TRANSFER\]

> Discharge From CNH \[FBCNH DISCHARGE\]

> Display Episode Of Care \[FBCNH DISPLAY EPISODE OF CARE\]

> Edit Movement Menu ... \[FBCNH EDIT MOVEMENT\]

> Admission Edit \[FBCNH EDIT ADMISSION\]

> Discharge Edit \[FBCNH EDIT DISCHARGE\]

> Transfer Edit \[FBCNH EDIT TRANSFER\]

> Transfer Movement \[FBCNH TRANSFER\]

Output Main Menu - CNH ... \[FBCNH OUTPUTS MAIN MENU\]

> 7078 Print \[FBCH PRINT 7078\]

> Activity Report for CNH \[FBCNH ACTIVITY REPORT\]

> AMIS 349 Print \[FBCNH AMIS\]

> Check Display \[FB CHECK DISPLAY\]

> CNH Census Report \[FBCNH CENSUS REPORT\]

> CNH Stays in Excess of 90 Days \[FBCNH ADMISSIONS \> 90 DAYS\]

> Contract Expiration List \[FBCNH EXPIRATION REPORT\]

> Cost Report for Contract Nursing Home \[FBCNH COST REPORT\]

> Display Episode Of Care \[FBCNH DISPLAY EPISODE OF CARE\]

> FPPS Claim Inquiry \[FB FPPS CLAIM INQ\]

> Invoice Display \[FBCH INVOICE DISPLAY\]

> Nursing Home 10-0168 Report \[FBCNH RCS 10-0168 REPORT\]

> Payment & Totals Report - CNH \[FBCNH LIST PAYMENT & TOTALS\]

> Potential Cost Recovery Report \[FB PCR\]

> Print Rejected Payment Items \[FBAA REJECT PRINT\]

> Report of Admissions/Discharges for CNH \[FBCNH AMIE\]

> Roster Print \[FBCNH PRINT ROSTER\]

> Vendor Payments Output \[FB PAY VENDOR\]

> Veteran Payments Output \[FB PAY VETERAN\]

Payment Main Menu - CNH ... \[FBCNH PAYMENT MAIN MENU\]

> Delete Inpatient Invoice \[FBCH DELETE INVOICE\]

> Edit CNH Payment \[FBCNH EDIT PAYMENT\]

> Enter CNH Payment \[FBCNH ENTER PAYMENT\]

Queue Data for Transmission \[FBAA QUEUE DATA FOR TRANS.\]

\*\*\> Locked with FBAASUPERVISOR

Update Vendor Contract/Rates - CNH \[FBCNH UPDATE VENDOR CONTRACT\]

Medical Fee Main Menu ... \[FBAA MEDICAL MAIN MENU\]

Batch Main Menu ... \[FBAA BATCH MENU\]

> Active Batch Listing by Status \[FBAA ACTIVE BATCH LISTING\]

> Batch Delete \[FBAA BATCH DELETE\]

> Batch status for a Range of Batches \[FBAA BATCH RANGE\]

> Close-out Batch \[FBAA CLOSE BATCH\]

> Display Open Batches \[FBAA DISPLAY OPEN BATCHES\]

> Edit Batch data \[FBAA BATCH EDIT\]

> List Items in Batch \[FBAA LIST BATCH\]

> Open a Batch \[FBAA OPEN BATCH\]

> Re-open Batch \[FBAA REOPEN BATCH\]

> Release a Batch \[FBAA SUPERVISOR RELEASE\]

> \*\*\> Locked with FBAASUPERVISOR

> Status of Batch \[FBAA BATCH STATUS\]

Enter Authorization \[FBAA ENTER AUTHORIZATION\]

LTC Outpatient Active Authorizations Report \[FBAA LTC ACTIVE AUTHORIZ\]

LTC Outpatient Ending Authorization Report \[FBAA LTC ENDING AUTHORIZ\]

Outputs Main Menu ... \[FBAA OUTPUTS MENU\]

> Suspension Letter Print \[FBAA SUSPENSION LETTER PRINT\]

> Individual Suspension Letter Print \[FBAA SUSPENSION LETTER INDIV\]

> 7079 Print for Selected Patient \[FBAA PRINT 7079 SINGLE\]

> Check Display \[FB CHECK DISPLAY\]

> Display ID Card History for Patient \[FBAA DISPLAY ID CARD HISTORY\]

> FPPS Claim Inquiry \[FB FPPS CLAIM INQ\]

> Group 7079 Print \[FBAA PRINT 7079 GROUP\]

> \*\*\> Locked with FBAASUPERVISOR

> Historical Authorization Data Report \[FBAA AUTH DATA AUDIT RPT\]

> Invoice Display \[FBAA INVOICE DISPLAY\]

> IPAC Vendor Reports ... \[FBAA IPAC VENDOR REPORT MENU\]

> DoD Invoice Number Inquiry \[FBAA IPAC DoD INVOICE INQUIRY\]

> IPAC Vendor DoD Invoice Report (Summary) \[FBAA IPAC DoD INVOICE RPT\]

> IPAC Vendor Payment Report (Detail) \[FBAA IPAC VENDOR PAYMENT RPT\]

> MST Report \[FBAA MST REPORT\]

> Obsolete ID Cards List \[FBAA OBSOLETE ID CARDS\]

> Outpatient Cost Report \[FBAA COST REPORT\]

> Payment Aging Report \[FB PAYMENT AGING RPT\]

> Payment History Display \[FBAA PAYMENT HISTORY DISPLAY\]

> Potential Cost Recovery Report \[FB PCR\]

> Print Rejected Payment Items \[FBAA REJECT PRINT\]

> PSA Output Report \[FBCH PSA OUTPUT\]

> RBRVS Fee Schedule Cost Comparison \[FBAA COST COMPARISON\]

> Valid ID Cards List \[FBAA ID CARDS CURRENT LIST\]

> Vendor Payments Output \[FB PAY VENDOR\]

> Veteran Payments Output \[FB PAY VETERAN\]

Payment menu ... \[FBAA PAYMENT MENU\]

> Calculate Payment Amount \[FBAA FEE SCHEDULE RATE\]

> Delete Payment Entry \[FBAA DELETE PAYMENT\]

> Edit Payment \[FBAA EDIT PAYMENT\]

> Enter Payment \[FBAA ENTER PAYMENT\]

> Invoice Display \[FBAA INVOICE DISPLAY\]

> Multiple Payment Entry \[FBAA MULTIPLE PAYMENT ENTRY\]

> Re-initiate Rejected Payment Items \[FBAA REINITIATE REJECTS\]

> Reimbursement Payment Entry \[FBAA MEDICAL REIMBURSEMENT\]

> Travel Payment Only \[FBAA TRAVEL ENTRY\]

Registration Menu ... \[FBAA REGISTRATION MAIN MENU\]

> Authorization Display \[FBAA AUTHORIZATION DISPLAY\]

> Fee Patient Inquiry \[FBAA PATIENT INQUIRY\]

> Print Report of Contact \[FBAA PRINT REPORT OF CONTACT\]

> Report of Contact \[FBAA REPORT OF CONTACT\]

Supervisor Main Menu ... \[FBAA SUPERVISOR OPTIONS\]

\*\*\> Locked with FBAASUPERVISOR

> Clerk Look-Up For An Authorization \[FBAA CLERK LOOK-UP\]

> Contract File Enter/Edit \[FBAA CONTRACT FILE\]

> \*\*\> Locked with FBAASUPERVISOR

> Delete reject flag \[FBAA VOUCHER DELETE REJECT\]

> \*\*\> Locked with FBAAREJECT

> Edit Pharmacy Invoice Status \[FBAA EDIT INVOICE STATUS\]

> Enter/Edit Suspension Letters \[FBAA ENTER/EDIT LETTERS\]

> Fee Basis 1358 Segregation of Duty Report \[FB SEG DUTY RPT\]

> Fee Schedule Main Menu ... \[FBAA FEE SCHEDULE\]

> \*\*\> Locked with FBAASUPERVISOR

> Add/Edit Fee Schedule \[FBAA EDIT SCHEDULE\]

> Compile Fee Schedule \[FBAA CALCULATE SCHEDULE\]

> Print Fee Schedule \[FBAA PRINT SCHEDULE\]

> Finalize a Batch \[FBAA FINALIZE BATCH\]

> FPPS Update & Transmit Menu ... \[FB FPPS UPDATE MENU\]

> Outpatient/Ancillary Invoice Edit \[FBAA FPPS EDIT INVOICE\]

> \*\*\> Locked with FBAASUPERVISOR

> Pharmacy Invoice Edit \[FBRX FPPS EDIT INVOICE\]

> \*\*\> Locked with FBAASUPERVISOR

> Inpatient Invoice Edit \[FBCH FPPS EDIT INVOICE\]

> \*\*\> Locked with FBAASUPERVISOR

> Audit Report for FPPS Data \[FB FPPS AUDIT REPORT\]

> Report of Transmissions to FPPS \[FB FPPS TRANSMIT REPORT\]

> Purge Message Text \[FB FPPS PURGE\]

\*\*\> Locked with FBAASUPERVISOR

> List Batches Pending Release \[FBAA LIST CLOSED BATCHES\]

> MRA Main Menu ... \[FB MRA MAIN MENU\]

> Vendor MRA Main Menu ... \[FBAA VENDOR MRA MAIN MENU\]

> \*\*\> Locked with FBAASUPERVISOR

Update FMS Vendor File in Austin \[FBAA FMS UPDATE\]

\*\*\> Locked with FBAASUPERVISOR

Delete Vendor MRA \[FBAA MRA DELETE VENDOR\]

> \*\*\> Locked with FBAASUPERVISOR

Reinstate Vendor MRA \[FBAA MRA VENDOR REINSTATE\]

MRA'S Awaiting Austin Approval \[FBAA MRA'S AWAITING APPROVAL\]

> Veteran MRA Main Menu ... \[FBAA VETERAN MRA MAIN MENU\]

> Add type Veteran MRA \[FBAA MRA VETERAN ADD TYPE\]

> Change type Veteran MRA \[FBAA MRA VETERAN CHANGE TYPE\]

Delete type Veteran MRA \[FBAA MRA VETERAN DELETE TYPE\]

Reinstate type Veteran MRA \[FBAA MRA VETERAN REINSTATE\]

> Re-Transmit MRA's \[FBAA REQUEUE MRA\]

> \*\*\> Locked with FBAASUPERVISOR

> Purge Transmitted MRAs \[FBAA MRA PURGE\]

> \*\*\> Locked with FBAASUPERVISOR

> IPAC Agreement MRA Main Menu ... \[FBAA IPAC AGREEMENT MRA MENU\]

> Add Type IPAC Agreement MRA \[FBAA MRA IPAC ADD TYPE\]

> Change Type IPAC Agreement MRA \[FBAA MRA IPAC CHANGE TYPE\]

> Delete Type IPAC Agreement MRA \[FBAA MRA IPAC DELETE TYPE\]

> Pricer Batch Release \[FBCH PRICER RELEASE\]

> Print Rejected Payment Items \[FBAA REJECT PRINT\]

> Queue Data for Transmission \[FBAA QUEUE DATA FOR TRANS.\]

> \*\*\> Locked with FBAASUPERVISOR

> Re-initiate Rejected Payment Items \[FBAA REINITIATE REJECTS\]

> Release a Batch \[FBAA SUPERVISOR RELEASE\]

> \*\*\> Locked with FBAASUPERVISOR

> Reprocess Overdue Batch \[FBAA REPROCESS BATCH\]

> \*\*\> Locked with FBAASUPERVISOR

> Resend Completed Batch \[FBAA RESEND VOUCHER MSG\]

> \*\*\> Locked with FBAASUPERVISOR

> Site Parameter Enter/Edit \[FBAA ENTER SITE PARAMETERS\]

> \*\*\> Locked with FBAASUPERVISOR

> Unauthorized Claims File Menu ... \[FBUC FILE MENU\]

> Add New Person for Unauthorized Claim \[FBUC ADD NEW PERSON\]

> Disapproval Reasons File Enter/Edit \[FBUC DISAPPROVAL REASONS FILE\]

> Dispositions File Edit \[FBUC DISPOSITIONS FILE\]

> Request Info File Enter/Edit \[FBUC REQUEST INFO FILE\]

> Void Payment Main Menu ... \[FBAA VOID PAYMENT MENU\]

> CH Delete Void Payment \[FBCH DELETE VOID\]

> CH Void Payment \[FBCH VOID PAYMENT\]

> CNH Delete Void Payment \[FBCNH DELETE VOID\]

> CNH Void Payment \[FBCNH VOID PAYMENT\]

> Medical Delete Void Payment \[FBAA CANCEL MEDICAL VOID\]

> Medical Void Payment \[FBAA MEDICAL VOID PAYMENT\]

> Pharmacy Delete Void Payment \[FBAA CANCEL PHARMACY VOID\]

> Pharmacy Void Payment \[FBAA PHARMACY VOID PAYMENT\]

Terminate ID Card \[FBAA TERMINATE ID CARD\]

Vendor Menu ... \[FBAA VENDOR OPTIONS\]

IPAC Vendor Agreement Menu ... \[FBAA IPAC AGREEMENT MENU\]

Enter/Edit a new IPAC Agreement \[FBAA IPAC AGREEMENT ENTER/EDIT\]

\*\*\> Locked with FB IPAC VENDOR

Delete an IPAC agreement \[FBAA IPAC AGREEMENT DELETE\]

\*\*\> Locked with FB IPAC VENDOR

View IPAC Vendor Agreement \[FBAA IPAC AGREEMENT VIEW\]

Display,Enter,Edit Demographics \[FBAA VENDOR DEMOGRAPHICS\]

FPDS-Only Vendor Edit \[FBAA VENDOR FPDS-ONLY\]

List Vendors Without FPDS Data \[FB VEN FPDS BLANK\]

Payment Display for Patient \[FBAA VENDOR PAYMENT DISPLAY\]

Payment Look-up for Medical Vendor \[FBAA VENDOR LOOKUP\]

Pharmacy Vendor Payment Look-Up \[FBAA PHARMACY LOOKUP\]

Pharmacy Fee Main Menu ... \[FBAA PHARMACY MAIN MENU\]

Batch Menu - Pharmacy ... \[FBAA PHARMACY BATCH OPTIONS\]

Batch Delete \[FBAA BATCH DELETE\]

Close-out Batch \[FBAA CLOSE BATCH\]

Display Open Batches \[FBAA DISPLAY OPEN BATCHES\]

Edit Batch data \[FBAA BATCH EDIT\]

List Items in Batch \[FBAA LIST BATCH\]

Open a Pharmacy Batch \[FBAA OPEN PHARMACY BATCH\]

Re-open Batch \[FBAA REOPEN BATCH\]

Release a Batch \[FBAA SUPERVISOR RELEASE\]

\*\*\> Locked with FBAASUPERVISOR

Status of Batch \[FBAA BATCH STATUS\]

Check Display \[FB CHECK DISPLAY\]

Closeout Pharmacy Invoice \[FBAA CLOSE OUT INVOICE\]

Complete Pharmacy Invoice \[FBAA COMPLETE PHARMACY INVOICE\]

Display Pharmacy Invoice \[FBAA PHARMACY INVOICE DISPLAY\]

Edit Pharmacy Invoice \[FBAA EDIT PHARMACY INVOICE\]

Enter Pharmacy Invoice \[FBAA ENTER PHARMACY INVOICE\]

FPPS Claim Inquiry \[FB FPPS CLAIM INQ\]

List Invoices Pending MAS Completion \[FBAA PENDING MAS COMPLETION\]

List Pharmacy History \[FBAA PHARMACY HISTORY\]

Patient Re-imbursement \[FBAA REIMBURSEMENT PHARMACY\]

Pharmacy Invoice Status \[FBAA PHARMACY INVOICE STATUS\]

Potential Cost Recovery Report \[FB PCR\]

Prescriptions Pending Pharmacy Review \[FBAA LIST PENDING RX\]

Review Fee Prescription \[FBAA PHARMACY REVIEW\]

Vendor Payments Output \[FB PAY VENDOR\]

Veteran Payments Output \[FB PAY VETERAN\]

Project ARCH Menu ... \[FB PROJECT ARCH MENU\]

\*\*\> Locked with FB ARCH

> AD Add/Edit Project ARCH Eligibility \[FB ADD ARCH ELIGIBILITY\]

> \*\*\> Locked with FB ARCH

> VW View Project ARCH Eligibility \[FB VIEW ARCH ELIGIBILITY\]

> \*\*\> Locked with FB ARCH

> UP ARCH Eligibility Data Upload \[FB ARCH DATA UPLOAD\]

> \*\*\> Locked with FB ARCH

> RE ARCH Clinical Reminder Due Delay \[FB ARCH REMINDER DELAY\]

\*\*\> Locked with FB ARCH

State Home Main Menu ... \[FBSH MAIN MENU\]

Enter New State Home Authorization \[FBSH ENTER AUTH\]

Change a State Home Authorization \[FBSH CHANGE AUTH\]

Delete a State Home Authorization \[FBSH DELETE AUTH\]

Reinstate State Home Authorization \[FBSH REINSTATE AUTH\]

Active Authorization Report \[FBSH ACTIVE AUTH. REPORT\]

Telephone Inquiry Menu ... \[FB PHONE MENU\]

Check Display \[FB CHECK DISPLAY\]

IPAC Vendor Reports ... \[FBAA IPAC VENDOR REPORT MENU\]

DoD Invoice Number Inquiry \[FBAA IPAC DoD INVOICE INQUIRY\]

IPAC Vendor DoD Invoice Report (Summary) \[FBAA IPAC DoD INVOICE RPT\]

IPAC Vendor Payment Report (Detail) \[FBAA IPAC VENDOR PAYMENT RPT\]

Payment Listing for Vendor/Veteran \[FB VENDOR/VETERAN PAYMENTS\]

Vendor Payments Output \[FB PAY VENDOR\]

Veteran Payments Output \[FB PAY VETERAN\]

Unauthorized Claim Main Menu ... \[FBUC MAIN\]

Enter/Edit Unauthorized Claim Menu ... \[FBUC ENTER/EDIT\]

Enter Unauthorized Claim \[FBUC ENTER\]

Modify Unauthorized Claim \[FBUC MODIFY UNAUTHORIZED CLAIM\]

Disposition Unauthorized Claim \[FBUC DISPOSITION UNAUTH CLAIM\]

Re-open Unauthorized Claim \[FBUC REOPEN\]

Initiate Appeal for Unauthorized Claim \[FBUC INITIATE APPEAL\]

Appeal Edit for Unauthorized Claim \[FBUC APPEAL EDIT\]

COVA Appeal Enter/Edit \[FBUC COVA APPEAL\]

Request Information on Unauthorized Claim \[FBUC REQUEST INFORMATION\]

Receive Requested Information \[FBUC RECEIVE INFORMATION\]

Letters for Unauthorized Claim ... \[FBUC LETTERS\]

Update Date Letter Sent \[FBUC UPDATE DATE LETTER SENT\]

Batch Print Letters \[FBUC BATCH PRINT LETTERS\]

Reprint Letter(s) \[FBUC REPRINT LETTER(S)\]

Payments for Unauthorized Claims \[FBUC PAYMENTS\]

Outputs for Unauthorized Claims ... \[FBUC OUTPUTS\]

All Claims by Vendor/Veteran/Other \[FBUC ALL CLAIMS OUTPUT\]

Check Display \[FB CHECK DISPLAY\]

Disapproved EDI Claim Report \[FBUC DISAPPROVED EDI\]

Display Unauthorized Claim \[FBUC DISPLAY UNAUTHORIZED\]

Disposition/Status Statistics Display/Print \[FBUC STATS OUTPUT\]

Expiration Display/Print \[FBUC EXPIRE OUTPUT\]

FPPS Claim Inquiry \[FB FPPS CLAIM INQ\]

Millennium Act Emergency Care Summary Report \[FBUC MILL ACT SUMMARY\]

Status Display/Print of Unauthorized Claims \[FBUC STATUS OUTPUT\]

Unauthorized Claims Cost Report for Civil Hospital \[FBCH UC COST REPORT\]

Vendor Payments Output \[FB PAY VENDOR\]

Veteran Payments Output \[FB PAY VETERAN\]

Display Unauthorized Claim \[FBUC DISPLAY UNAUTHORIZED\]

Utilities for Unauthorized Claims ... \[FBUC UTILITIES\]

OPHTHALMIC GROUP WORLDWIDE INC. \[FBCNH VENDOR ENTER/EDIT\]

\*\*\> Locked with FBAA EDIT VENDOR

Add New Person for Unauthorized Claim \[FBUC ADD NEW PERSON\]

Associate an Unauthorized Claim to a Primary \[FBUC ASSOCIATE\]

Disassociate an Unauthorized Claim \[FBUC DISASSOCIATE\]

Delete Unauthorized Claim \[FBUC DELETE UNAUTHORIZED CLAIM\]

Return Address Display/Edit \[FBUC RETURN ADDRESS DIS/ED\]

Extension for Incomplete Mill Bill (1725) Claim \[FBUC EXTENSION\]

\*\*\> Locked with FBAASUPERVISOR

## Menu Diagram Fee Basis Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fee Basis Main Menu \[FBAA MAIN MENU\]

\|

\|

------Community Nursing Home Main Menu (FBCNH MAIN MENU)

> \|

> \|

> ----- Authorization ------------------------- Enter CNH

> Main Menu - CNH Authorization

> \[FBCNH \[FBCNH ENTER

> AUTHORIZATION AUTHORIZATION\]

> MAIN MENU\]

> \|

> \|---------------------------------- Edit CNH

> \| Authorization

> \| \[FBCNH EDIT

> \| AUTHORIZATION\]

> \|

> \|---------------------------------- Cancel

> \| Authorization

> \| Entered in Error

> \| \[FBCNH CANCEL

> \| 7078\]

> \| \*\*LOCKED:

> \| FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Change Existing

> \| Contract Rate

> \| for a Patient

> \| \[FBCNH RATE

> \| CHANGE\]

> \|

> \|---------------------------------- Delete CNH Rate

> \| \[FBCNH DELETE

> \| RATE\]

> \|

> \|---------------------------------- Display

> \| 7078/Authorizati

> \| on - CNH \[FBCNH

> \| DISPLAY 7078\]

> \|

> \|---------------------------------- Enter Veteran

> \| Rates under new

> \| Vendor Contract

> \| \[FBCNH ENTER

> \| VETERAN RATES\]

> \|

> \|---------------------------------- Print List of

> Cancelled 7078

> \[FBCH PRINT

> CANCELLED 7078\]

> \*\*LOCKED:

> FBAASUPERVISOR\*\*

> ----- Batch Main Menu ----------------------- Batch Delete

> \- CNH \[FBCNH BATCH MAIN MENU\] \[FBAA BATCH DELETE\]

> \|

> \|---------------------------------- Close-out Batch

> \| \[FBAA CLOSE

> \| BATCH\]

> \|

> \|---------------------------------- Delete reject

> \| flag \[FBAA

> \| VOUCHER DELETE

> \| REJECT\]

> \| \*\*LOCKED:

> \| FBAAREJECT\*\*

> \|

> \|---------------------------------- Display Open

> \| Batches \[FBAA

> \| DISPLAY OPEN

> \| BATCHES\]

> \|

> \|---------------------------------- Edit Batch data

> \| \[FBAA BATCH

> \| EDIT\]

> \|

> \|---------------------------------- Finalize a Batch

> \| \[FBAA FINALIZE

> \| BATCH\]

> \|

> \|---------------------------------- List Batches

> \| Pending Release

> \| \[FBAA LIST

> \| CLOSED BATCHES\]

> \|

> \|---------------------------------- List Items in

> \| Batch \[FBAA LIST

> \| BATCH\]

> \|

> \|---------------------------------- Open CNH Batch

> \| \[FBCNH OPEN

> \| BATCH\]

> \|

> \|---------------------------------- Re-initiate

> \| Rejected Payment

> \| Items \[FBAA

> \| REINITIATE

> \| REJECTS\]

> \|

> \|---------------------------------- Re-open Batch

> \| \[FBAA REOPEN

> \| BATCH\]

> \|

> \|---------------------------------- Release a Batch

> \| \[FBAA SUPERVISOR

> \| RELEASE\]

> \| \*\*LOCKED:

> \| FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Status of Batch

> \[FBAA BATCH

> STATUS\]

> ----- Fee Fund Control ---------------------- Estimate Funds

> Main Menu - CNH for Obligation

> \[FBCNH FUND \[FBCNH ESTIMATE

> CONTROL MAIN FUNDS\]

> MENU\]

> \|

> \|---------------------------------- Post Commitments

> for Obligation

> \[FBCNH POST

> COMMITMENTS\]

> --------------------------------------------- LTC CNH Active

> Authorizations

> Report \[FBCNH

> LTC ACTIVE

> AUTHORIZ\]

> --------------------------------------------- LTC CNH Ending

> Authorizations

> Report \[FBCNH

> LTC ENDING

> AUTHORIZ\]

> ----- Movement Main ------------------------- Admit To CNH

> Menu - CNH \[FBCNH ADMIT\]

> \[FBCNH MOVEMENT

> MAIN MENU\]

> \|

> \|-------------- Delete Movement --- Admission Delete

> \| Menu \[FBCNH \[FBCNH DELETE

> \| DELETE MOVEMENT ADMISSION\]

> \| MENU\]

> \| \|

> \| \|-------------- Discharge Delete

> \| \| \[FBCNH DELETE

> \| \| DISCHARGE\]

> \| \|

> \| \|-------------- Transfer Delete

> \| \[FBCNH DELETE

> \| TRANSFER\]

> \|

> \|

> \|---------------------------------- Discharge From

> \| CNH \[FBCNH

> \| DISCHARGE\]

> \|

> \|---------------------------------- Display Episode

> \| Of Care \[FBCNH

> \| DISPLAY EPISODE

> \| OF CARE\]

> \|

> \|-------------- Edit Movement ----- Admission Edit

> \| Menu \[FBCNH EDIT \[FBCNH EDIT

> \| MOVEMENT\] ADMISSION\]

> \| \|

> \| \|-------------- Discharge Edit

> \| \| \[FBCNH EDIT

> \| \| DISCHARGE\]

> \| \|

> \| \|-------------- Transfer Edit

> \| \[FBCNH EDIT

> \| TRANSFER\]

> \|

> \|

> \|---------------------------------- Transfer

> Movement \[FBCNH

> TRANSFER\]

> ----- Output Main Menu ---------------------- 7078 Print \[FBCH

> \- CNH \[FBCNH PRINT 7078\]

> OUTPUTS MAIN

> MENU\]

> \|

> \|---------------------------------- Activity Report

> \| for CNH \[FBCNH

> \| ACTIVITY REPORT\]

> \|

> \|---------------------------------- AMIS 349 Print

> \| \[FBCNH AMIS\]

> \|

> \|---------------------------------- Check Display

> \| \[FB CHECK

> \| DISPLAY\]

> \|

> \|---------------------------------- CNH Census

> \| Report \[FBCNH

> \| CENSUS REPORT\]

> \|

> \|---------------------------------- CNH Stays in

> \| Excess of 90

> \| Days \[FBCNH

> \| ADMISSIONS \> 90

> \| DAYS\]

> \|

> \|---------------------------------- Contract

> \| Expiration List

> \| \[FBCNH

> \| EXPIRATION

> \| REPORT\]

> \|

> \|---------------------------------- Cost Report for

> \| Contract Nursing

> \| Home \[FBCNH COST

> \| REPORT\]

> \|

> \|---------------------------------- Display Episode

> \| Of Care \[FBCNH

> \| DISPLAY EPISODE

> \| OF CARE\]

> \|

> \|---------------------------------- FPPS Claim

> \| Inquiry \[FB FPPS

> \| CLAIM INQ\]

> \|

> \|---------------------------------- Invoice Display

> \| \[FBCH INVOICE

> \| DISPLAY\]

> \|

> \|---------------------------------- Nursing Home

> \| 10-0168 Report

> \| \[FBCNH RCS

> \| 10-0168 REPORT\]

> \|

> \|---------------------------------- Payment & Totals

> \| Report - CNH

> \| \[FBCNH LIST

> \| PAYMENT &

> \| TOTALS\]

> \|

> \|---------------------------------- Potential Cost

> \| Recovery Report

> \| \[FB PCR\]

> \|

> \|---------------------------------- Print Rejected

> \| Payment Items

> \| \[FBAA REJECT

> \| PRINT\]

> \|

> \|---------------------------------- Report of

> \| Admissions/Disch

> \| arges for CNH

> \| \[FBCNH AMIE\]

> \|

> \|---------------------------------- Roster Print

> \| \[FBCNH PRINT

> \| ROSTER\]

> \|

> \|---------------------------------- Vendor Payments

> \| Output \[FB PAY

> \| VENDOR\]

> \|

> \|---------------------------------- Veteran Payments

> Output \[FB PAY

> VETERAN\]

> ----- Payment Main -------------------------- Delete Inpatient

> Menu - CNH Invoice \[FBCH

> \[FBCNH PAYMENT DELETE INVOICE\]

> MAIN MENU\]

> \|

> \|---------------------------------- Edit CNH Payment

> \| \[FBCNH EDIT

> \| PAYMENT\]

> \|

> \|---------------------------------- Enter CNH

> Payment \[FBCNH

> ENTER PAYMENT\]

> --------------------------------------------- Queue Data for

> Transmission

> \[FBAA QUEUE DATA

> FOR TRANS.\]

> \*\*LOCKED:

> FBAASUPERVISOR\*\*

> --------------------------------------------- Update Vendor

> Contract/Rates -

> CNH \[FBCNH

> UPDATE VENDOR

> CONTRACT\]

> --------------------------------------------- Vendor

> Enter/Edit

> \[FBCNH VENDOR

> ENTER/EDIT\]

> Civil Hospital Main Menu (FBCH MAIN MENU)

> \|

> \|

> ----- Notification/Request Menu ------------- Enter a Request/Notification

> \[FBCH NOTIFICATION MENU\] \[FBCH ENTER REQUEST\]

> \|

> \|---------------------------------- Notification/Request Edit

> \| \[FBCH EDIT REQUEST\]

> \|

> \|---------------------------------- Legal Entitlement \[FBCH

> \| LEGAL ENTITLEMENT\]

> \|

> \|---------------------------------- Medical Entitlement \[FBCH

> \| MEDICAL ENTITLEMENT\]

> \|

> \|---------------------------------- Display a Request/

> \| Notification

> \| \[FBCH DISPLAY REQUEST\]

> \|

> \|---------------------------------- Delete Notification/Request

> \| \[FBCH DELETE REQUEST\]

> \|

> \|---------------------------------- Edit Report of Contact - CH

> \| \[FBCH EDIT REPORT OF

> \| CONTACT\]

> \|

> \|---------------------------------- Print Entitlement Audit

> \| \[FBCH PRINT REQUEST AUDIT\]

> \| \*\*LOCKED: FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Print Report of Contact - CH

> \| \[FBCH PRINT REPORT OF

> \| CONTACT\]

> \|

> \|---------------------------------- Reconsider a Denied Request

> \| \[FBCH REOPEN REQUEST\]

> \| \*\*LOCKED: FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Requests Pending Entitlement

> \| \[FBCH PENDING REQUEST\]

> \|

> \|---------------------------------- Update Report of Contact –

> CH \[FBCH UPDATE REPORT OF

> CONTACT\]

> ----- Disposition Menu \[FBCH ---------------- Complete 7078/Authorization

> DISPOSITION MENU\] \[FBCH COMPLETE 7078\]

> \|

> \|---------------------------------- Edit Completed 7078 \[FBCH

> \| EDIT 7078\]

> \|

> \|---------------------------------- Display 7078/Authorization

> \| \[FBCH DISPLAY 7078\]

> \|

> \|---------------------------------- Cancel 7078 Entered in Error

> \| \[FBCH CANCEL 7078\]

> \| \*\*LOCKED: FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Print List of Cancelled 7078

> \| \[FBCH PRINT CANCELLED 7078\]

> \| \*\*LOCKED: FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Set-up a 7078 \[FBCH 7078

> SETUP\]

> ----- Payment Process Menu \[FBCH ------------ Ancillary Contract Hosp/CNH

> PAYMENT MENU\] Payment \[FBCH ANCILLARY

> \| PAYMENT\]

> \|

> \|---------------------------------- Complete a Payment \[FBCH

> \| COMPLETE PAYMENT\]

> \|

> \|---------------------------------- Delete Inpatient Invoice

> \| \[FBCH DELETE INVOICE\]

> \|

> \|---------------------------------- Edit Ancillary Payment \[FBCH

> \| EDIT ANCILLARY PAYMENT\]

> \|

> \|---------------------------------- Enter Invoice/Payment \[FBCH

> \| ENTER PAYMENT\]

> \|

> \|---------------------------------- Invoice Edit \[FBCH EDIT

> \| PAYMENT\]

> \|

> \|---------------------------------- Multiple Ancillary Payments

> \| \[FBCH MULTIPLE PAYMENTS\]

> \|

> \|---------------------------------- Patient Reimbursement for

> \| Ancillary Services \[FBCH

> \| ANCILLARY REIMBURSEMENT\]

> \|

> \|---------------------------------- Reimbursement for Inpatient

> Hospital Invoice \[FBCH

> REIMBURSEMENT INVOICE\]

> ----- Batch Main Menu - CH \[FBCH ------------ Open a Batch \[FBCH OPEN

> BATCH OPTIONS\] BATCH\]

> \|

> \|---------------------------------- Edit Batch data \[FBAA BATCH

> \| EDIT\]

> \|

> \|---------------------------------- Close-out Batch \[FBAA CLOSE

> \| BATCH\]

> \|

> \|---------------------------------- Re-open Batch \[FBAA REOPEN

> \| BATCH\]

> \|

> \|---------------------------------- Pricer Batch Release \[FBCH

> \| PRICER RELEASE\]

> \|

> \|---------------------------------- Re-initiate Pricer Rejected

> \| Items \[FBCH REINITIATE

> \| PRICER REJECTS\]

> \|

> \|---------------------------------- Release a Batch \[FBAA

> \| SUPERVISOR RELEASE\]

> \| \*\*LOCKED: FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Finalize a Batch \[FBAA

> \| FINALIZE BATCH\]

> \|

> \|---------------------------------- Re-initiate Rejected Payment

> \| Items \[FBAA REINITIATE

> \| REJECTS\]

> \|

> \|---------------------------------- Delete reject flag \[FBAA

> \| VOUCHER DELETE REJECT\]

> \| \*\*LOCKED: FBAAREJECT\*\*

> \|

> \|---------------------------------- Status of Batch \[FBAA BATCH

> \| STATUS\]

> \|

> \|---------------------------------- List Items in Batch \[FBAA

> \| LIST BATCH\]

> \|

> \|---------------------------------- Batch Delete \[FBAA BATCH

> \| DELETE\]

> \|

> \|---------------------------------- Open Ancillary Payment Batch

> \[FBCH OPEN ANCILLARY BATCH\]

> ----- Output Menu \[FBCH OUTPUT MENU\] -------- 7078 Print \[FBCH PRINT 7078\]

> \|

> \|---------------------------------- Check Display \[FB CHECK

> \| DISPLAY\]

> \|

> \|---------------------------------- Civil Hospital Census Report

> \| \[FBCH CENSUS REPORT\]

> \|

> \|---------------------------------- Cost Report for Civil

> \| Hospital \[FBCH COST REPORT\]

> \|

> \|---------------------------------- Display Open Batches \[FBAA

> \| DISPLAY OPEN BATCHES\]

> \|

> \|---------------------------------- FPPS Claim Inquiry \[FB FPPS

> \| CLAIM INQ\]

> \|

> \|---------------------------------- Invoice Display

> \| \[FBCH INVOICE

> \| DISPLAY\]

> \|

> \|-------------------- IPAC Vendor ------------1 DoD Invoice

> \| Reports \[FBAA Number Inquiry

> \| IPAC VENDOR \[FBAA IPAC DoD

> \| REPORT MENU\] INVOICE INQUIRY\]

> \| \|

> \| \|-------------------2 IPAC Vendor DoD

> \| \| Invoice Report

> \| \| (Summary) \[FBAA

> \| \| IPAC DoD INVOICE

> \| \| RPT\]

> \| \|

> \| \|-------------------3 IPAC Vendor

> \| Payment Report

> \| (Detail) \[FBAA

> \| IPAC VENDOR

> \| PAYMENT RPT\]

> \|

> \|

> \|---------------------------------- List Batches

> \| Pending Release

> \| \[FBAA LIST

> \| CLOSED BATCHES\]

> \|

> \|---------------------------------- Non-VA Hospital Activity

> \| Report \[FBCH HOSPITAL

> \| ACTIVITY\]

> \|

> \|---------------------------------- Payment Aging Report \[FB

> \| PAYMENT AGING RPT\]

> \|

> \|---------------------------------- Pending Pricer Rejects \[FBCH

> \| PRICER REJECTS\]

> \|

> \|---------------------------------- Potential Cost Recovery

> \| Report \[FB PCR\]

> \|

> \|---------------------------------- Print Rejected Payment Items

> \| \[FBAA REJECT PRINT\]

> \|

> \|---------------------------------- Request Statistics \[FBCH

> \| REQUEST STATS\]

> \|

> \|---------------------------------- Unauthorized Claims Cost

> \| Report for Civil Hospital

> \| \[FBCH UC COST REPORT\]

> \|

> \|---------------------------------- Vendor Payments Output \[FB

> \| PAY VENDOR\]

> \|

> \|---------------------------------- Veteran Payments Output \[FB

> PAY VETERAN\]

> --------------------------------------------- Generic Pricer Interface

> \[FBCH GENERIC PRICER\]

> --------------------------------------------- Queue Data for Transmission

> \[FBAA QUEUE DATA FOR TRANS.\]

> \*\*LOCKED: FBAASUPERVISOR\*\*

> Community Nursing Home Main Menu (FBCNH MAIN MENU)

> \|

> \|

> ----- Authorization ------------------------- Enter CNH

> Main Menu - CNH Authorization

> \[FBCNH \[FBCNH ENTER

> AUTHORIZATION AUTHORIZATION\]

> MAIN MENU\]

> \|

> \|---------------------------------- Edit CNH

> \| Authorization

> \| \[FBCNH EDIT

> \| AUTHORIZATION\]

> \|

> \|---------------------------------- Cancel

> \| Authorization

> \| Entered in Error

> \| \[FBCNH CANCEL

> \| 7078\]

> \| \*\*LOCKED:

> \| FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Change Existing

> \| Contract Rate

> \| for a Patient

> \| \[FBCNH RATE

> \| CHANGE\]

> \|

> \|---------------------------------- Delete CNH Rate

> \| \[FBCNH DELETE

> \| RATE\]

> \|

> \|---------------------------------- Display

> \| 7078/Authorizati

> \| on - CNH \[FBCNH

> \| DISPLAY 7078\]

> \|

> \|---------------------------------- Enter Veteran

> \| Rates under new

> \| Vendor Contract

> \| \[FBCNH ENTER

> \| VETERAN RATES\]

> \|

> \|---------------------------------- Print List of

> Cancelled 7078

> \[FBCH PRINT

> CANCELLED 7078\]

> \*\*LOCKED:

> FBAASUPERVISOR\*\*

> ----- Batch Main Menu ----------------------- Batch Delete

> \- CNH \[FBCNH \[FBAA BATCH

> BATCH MAIN MENU\] DELETE\]

> \|

> \|---------------------------------- Close-out Batch

> \| \[FBAA CLOSE

> \| BATCH\]

> \|

> \|---------------------------------- Delete reject

> \| flag \[FBAA

> \| VOUCHER DELETE

> \| REJECT\]

> \| \*\*LOCKED:

> \| FBAAREJECT\*\*

> \|

> \|---------------------------------- Display Open

> \| Batches \[FBAA

> \| DISPLAY OPEN

> \| BATCHES\]

> \|

> \|---------------------------------- Edit Batch data

> \| \[FBAA BATCH

> \| EDIT\]

> \|

> \|---------------------------------- Finalize a Batch

> \| \[FBAA FINALIZE

> \| BATCH\]

> \|

> \|---------------------------------- List Batches

> \| Pending Release

> \| \[FBAA LIST

> \| CLOSED BATCHES\]

> \|

> \|---------------------------------- List Items in

> \| Batch \[FBAA LIST

> \| BATCH\]

> \|

> \|---------------------------------- Open CNH Batch

> \| \[FBCNH OPEN

> \| BATCH\]

> \|

> \|---------------------------------- Re-initiate

> \| Rejected Payment

> \| Items \[FBAA

> \| REINITIATE

> \| REJECTS\]

> \|

> \|---------------------------------- Re-open Batch

> \| \[FBAA REOPEN

> \| BATCH\]

> \|

> \|---------------------------------- Release a Batch

> \| \[FBAA SUPERVISOR

> \| RELEASE\]

> \| \*\*LOCKED:

> \| FBAASUPERVISOR\*\*

> \|

> \|---------------------------------- Status of Batch

> \[FBAA BATCH STATUS\]

> ----- Fee Fund Control ---------------------- Estimate Funds

> Main Menu - CNH for Obligation

> \[FBCNH FUND \[FBCNH ESTIMATE

> CONTROL MAIN FUNDS\]

> MENU\]

> \|

> \|---------------------------------- Post Commitments

> for Obligation

> \[FBCNH POST

> COMMITMENTS\]

> --------------------------------------------- LTC CNH Active

> Authorizations

> Report \[FBCNH

> LTC ACTIVE

> AUTHORIZ\]

> --------------------------------------------- LTC CNH Ending

> Authorizations

> Report \[FBCNH

> LTC ENDING

> AUTHORIZ\]

> ----- Movement Main ------------------------- Admit To CNH

> Menu - CNH \[FBCNH ADMIT\]

> \[FBCNH MOVEMENT

> MAIN MENU\]

> \|

> \|---------------- Delete Movement - Admission Delete

> \| Menu \[FBCNH \[FBCNH DELETE

> \| DELETE MOVEMENT ADMISSION\]

> \| MENU\]

> \| \|

> \| \|------------ Discharge Delete

> \| \| \[FBCNH DELETE

> \| \| DISCHARGE\]

> \| \|

> \| \|------------ Transfer Delete

> \| \[FBCNH DELETE

> \| TRANSFER\]

> \|

> \|

> \|---------------------------------- Discharge From

> \| CNH \[FBCNH

> \| DISCHARGE\]

> \|

> \|---------------------------------- Display Episode

> \| Of Care \[FBCNH

> \| DISPLAY EPISODE

> \| OF CARE\]

> \|

> \|---------------- Edit Movement --- Admission Edit

> \| Menu \[FBCNH EDIT \[FBCNH EDIT

> \| MOVEMENT\] ADMISSION\]

> \| \|

> \| \|------------ Discharge Edit

> \| \| \[FBCNH EDIT

> \| \| DISCHARGE\]

> \| \|

> \| \|------------ Transfer Edit

> \| \[FBCNH EDIT

> \| TRANSFER\]

> \|

> \|

> \|---------------------------------- Transfer

> Movement \[FBCNH

> TRANSFER\]

> ----- Output Main Menu ---------------------- 7078 Print \[FBCH

> \- CNH \[FBCNH PRINT 7078\]

> OUTPUTS MAIN

> MENU\]

> \|

> \|---------------------------------- Activity Report

> \| for CNH \[FBCNH

> \| ACTIVITY REPORT\]

> \|

> \|---------------------------------- AMIS 349 Print

> \| \[FBCNH AMIS\]

> \|

> \|---------------------------------- Check Display

> \| \[FB CHECK

> \| DISPLAY\]

> \|

> \|---------------------------------- CNH Census

> \| Report \[FBCNH

> \| CENSUS REPORT\]

> \|

> \|---------------------------------- CNH Stays in

> \| Excess of 90

> \| Days \[FBCNH

> \| ADMISSIONS \> 90

> \| DAYS\]

> \|

> \|---------------------------------- Contract

> \| Expiration List

> \| \[FBCNH

> \| EXPIRATION

> \| REPORT\]

> \|

> \|---------------------------------- Cost Report for

> \| Contract Nursing

> \| Home \[FBCNH COST

> \| REPORT\]

> \|

> \|---------------------------------- Display Episode

> \| Of Care \[FBCNH

> \| DISPLAY EPISODE

> \| OF CARE\]

> \|

> \|---------------------------------- FPPS Claim

> \| Inquiry \[FB FPPS

> \| CLAIM INQ\]

> \|

> \|---------------------------------- Invoice Display

> \| \[FBCH INVOICE

> \| DISPLAY\]

> \|

> \|---------------------------------- Nursing Home

> \| 10-0168 Report

> \| \[FBCNH RCS

> \| 10-0168 REPORT\]

> \|

> \|---------------------------------- Payment & Totals

> \| Report - CNH

> \| \[FBCNH LIST

> \| PAYMENT &

> \| TOTALS\]

> \|

> \|---------------------------------- Potential Cost

> \| Recovery Report

> \| \[FB PCR\]

> \|

> \|---------------------------------- Print Rejected

> \| Payment Items

> \| \[FBAA REJECT

> \| PRINT\]

> \|

> \|---------------------------------- Report of

> \| Admissions/Disch

> \| arges for CNH

> \| \[FBCNH AMIE\]

> \|

> \|---------------------------------- Roster Print

> \| \[FBCNH PRINT

> \| ROSTER\]

> \|

> \|---------------------------------- Vendor Payments

> \| Output \[FB PAY

> \| VENDOR\]

> \|

> \|---------------------------------- Veteran Payments

> Output \[FB PAY

> VETERAN\]

> ----- Payment Main -------------------------- Delete Inpatient

> Menu - CNH Invoice \[FBCH

> \[FBCNH PAYMENT DELETE INVOICE\]

> MAIN MENU\]

> \|

> \|---------------------------------- Edit CNH Payment

> \| \[FBCNH EDIT

> \| PAYMENT\]

> \|

> \|---------------------------------- Enter CNH

> Payment \[FBCNH

> ENTER PAYMENT\]

> --------------------------------------------- Queue Data for

> Transmission

> \[FBAA QUEUE DATA

> FOR TRANS.\]

> \*\*LOCKED:

> FBAASUPERVISOR\*\*

> --------------------------------------------- Update Vendor

> Contract/Rates -

> CNH \[FBCNH

> UPDATE VENDOR

> CONTRACT\]

> --------------------------------------------- Vendor

> Enter/Edit

> \[FBCNH VENDOR

> ENTER/EDIT\]

> Medical Fee Main Menu (FBAA MEDICAL MAIN MENU)

> \|

> \|

> ----- Batch Main ---------------------------- Active

> Menu \[FBAA Batch

> BATCH Listing by

> MENU\] Status

> \| \[FBAA

> \| ACTIVE

> \| BATCH

> \| LISTING\]

> \|

> \|---------------------------------- Batch

> \| Delete

> \| \[FBAA

> \| BATCH

> \| DELETE\]

> \|

> \|---------------------------------- Batch

> \| status for

> \| a Range of

> \| Batches

> \| \[FBAA

> \| BATCH

> \| RANGE\]

> \|

> \|---------------------------------- Close-out

> \| Batch

> \| \[FBAA

> \| CLOSE

> \| BATCH\]

> \|

> \|---------------------------------- Display

> \| Open

> \| Batches

> \| \[FBAA

> \| DISPLAY

> \| OPEN

> \| BATCHES\]

> \|

> \|---------------------------------- Edit Batch

> \| data \[FBAA

> \| BATCH

> \| EDIT\]

> \|

> \|---------------------------------- List Items

> \| in Batch

> \| \[FBAA LIST

> \| BATCH\]

> \|

> \|---------------------------------- Open a

> \| Batch

> \| \[FBAA OPEN

> \| BATCH\]

> \|

> \|---------------------------------- Re-open

> \| Batch

> \| \[FBAA

> \| REOPEN

> \| BATCH\]

> \|

> \|---------------------------------- Release a

> \| Batch

> \| \[FBAA

> \| SUPERVISOR

> \| RELEASE\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|---------------------------------- Status of

> Batch

> \[FBAA

> BATCH

> STATUS\]

> --------------------------------------------- Enter

> Authorizat

> ion \[FBAA

> ENTER

> AUTHORIZAT

> ION\]

> --------------------------------------------- LTC

> Outpatient

> Active

> Authorizat

> ions

> Report

> \[FBAA LTC

> ACTIVE

> AUTHORIZ\]

> --------------------------------------------- LTC

> Outpatient

> Ending

> Authorizat

> ion Report

> \[FBAA LTC

> ENDING

> AUTHORIZ\]

> ----- Outputs ------------------------------- Suspension

> Main Menu Letter

> \[FBAA Print

> OUTPUTS \[FBAA

> MENU\] SUSPENSION

> \| LETTER

> \| PRINT\]

> \|

> \|---------------------------------- Individual

> \| Suspension

> \| Letter

> \| Print

> \| \[FBAA

> \| SUSPENSION

> \| LETTER

> \| INDIV\]

> \|

> \|---------------------------------- 7079 Print

> \| for

> \| Selected

> \| Patient

> \| \[FBAA

> \| PRINT 7079

> \| SINGLE\]

> \|

> \|---------------------------------- Check

> \| Display

> \| \[FB CHECK

> \| DISPLAY\]

> \|

> \|---------------------------------- Display ID

> \| Card

> \| History

> \| for

> \| Patient

> \| \[FBAA

> \| DISPLAY ID

> \| CARD

> \| HISTORY\]

> \|

> \|---------------------------------- FPPS Claim

> \| Inquiry

> \| \[FB FPPS

> \| CLAIM INQ\]

> \|

> \|---------------------------------- Group 7079

> \| Print

> \| \[FBAA

> \| PRINT 7079

> \| GROUP\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|---------------------------------- Historical

> \| Authorization

> \| Data

> \| Report

> \| \[FBAA AUTH

> \| DATA AUDIT

> \| RPT\]

> \|

> \|

> \|----------------------------------- Invoice

> \| Display

> \| \[FBAA

> \| INVOICE

> \| DISPLAY\]

> \|

> \|-------------- IPAC ---------------------------------1 DoD

> \| Vendor Invoice

> \| Reports Number

> \| \[FBAA IPAC Inquiry

> \| VENDOR \[FBAA IPAC

> \| REPORT DoD

> \| MENU\] INVOICE

> \| \| INQUIRY\]

> \| \|

> \| \|---------------------------------2 IPAC

> \| \| Vendor DoD

> \| \| Invoice

> \| \| Report

> \| \| (Summary)

> \| \| \[FBAA IPAC

> \| \| DoD

> \| \| INVOICE

> \| \| RPT\]

> \| \|

> \| \|---------------------------------3 IPAC

> \| Vendor

> \| Payment

> \| Report

> \| (Detail)

> \| \[FBAA IPAC

> \| VENDOR

> \| PAYMENT

> \| RPT\]

> \|

> \|

> \|---------------------------------- MST Report

> \| \[FBAA MST

> \| REPORT\]

> \|

> \|---------------------------------- Obsolete

> \| ID Cards

> \| List \[FBAA

> \| OBSOLETE

> \| ID CARDS\]

> \|

> \|---------------------------------- Outpatient

> \| Cost

> \| Report

> \| \[FBAA COST

> \| REPORT\]

> \|

> \|---------------------------------- Payment

> \| Aging

> \| Report \[FB

> \| PAYMENT

> \| AGING RPT\]

> \|

> \|---------------------------------- Payment

> \| History

> \| Display

> \| \[FBAA

> \| PAYMENT

> \| HISTORY

> \| DISPLAY\]

> \|

> \|---------------------------------- Potential

> \| Cost

> \| Recovery

> \| Report \[FB

> \| PCR\]

> \|

> \|---------------------------------- Print

> \| Rejected

> \| Payment

> \| Items

> \| \[FBAA

> \| REJECT

> \| PRINT\]

> \|

> \|---------------------------------- PSA Output

> \| Report

> \| \[FBCH PSA

> \| OUTPUT\]

> \|

> \|---------------------------------- RBRVS Fee

> \| Schedule

> \| Cost

> \| Comparison

> \| \[FBAA COST

> \| COMPARISON\]

> \|

> \|---------------------------------- Valid ID

> \| Cards List

> \| \[FBAA ID

> \| CARDS

> \| CURRENT

> \| LIST\]

> \|

> \|---------------------------------- Vendor

> \| Payments

> \| Output \[FB

> \| PAY

> \| VENDOR\]

> \|

> \|---------------------------------- Veteran

> Payments

> Output \[FB

> PAY

> VETERAN\]

> ----- Payment ------------------------------- Calculate

> menu \[FBAA Payment

> PAYMENT Amount

> MENU\] \[FBAA FEE

> \| SCHEDULE

> \| RATE\]

> \|

> \|---------------------------------- Delete

> \| Payment

> \| Entry

> \| \[FBAA

> \| DELETE

> \| PAYMENT\]

> \|

> \|---------------------------------- Edit

> \| Payment

> \| \[FBAA EDIT

> \| PAYMENT\]

> \|

> \|---------------------------------- Enter

> \| Payment

> \| \[FBAA

> \| ENTER

> \| PAYMENT\]

> \|

> \|---------------------------------- Invoice

> \| Display

> \| \[FBAA

> \| INVOICE

> \| DISPLAY\]

> \|

> \|---------------------------------- Multiple

> \| Payment

> \| Entry

> \| \[FBAA

> \| MULTIPLE

> \| PAYMENT

> \| ENTRY\]

> \|

> \|---------------------------------- Re-initiat

> \| e Rejected

> \| Payment

> \| Items

> \| \[FBAA

> \| REINITIATE

> \| REJECTS\]

> \|

> \|---------------------------------- Reimbursem

> \| ent

> \| Payment

> \| Entry

> \| \[FBAA

> \| MEDICAL

> \| REIMBURSEM

> \| ENT\]

> \|

> \|---------------------------------- Travel

> Payment

> Only \[FBAA

> TRAVEL

> ENTRY\]

> ----- Registrati----------------------------- Authorizat

> on Menu ion

> \[FBAA Display

> REGISTRATI \[FBAA

> ON MAIN AUTHORIZAT

> MENU\] ION

> \| DISPLAY\]

> \|

> \|---------------------------------- Fee

> \| Patient

> \| Inquiry

> \| \[FBAA

> \| PATIENT

> \| INQUIRY\]

> \|

> \|---------------------------------- Print

> \| Report of

> \| Contact

> \| \[FBAA

> \| PRINT

> \| REPORT OF

> \| CONTACT\]

> \|

> \|---------------------------------- Report of

> Contact

> \[FBAA

> REPORT OF

> CONTACT\]

> ----- Supervisor ---------------------------- Clerk

> Main Menu Look-Up

> \[FBAA For An

> SUPERVISOR Authorizat

> OPTIONS\] ion \[FBAA

> \*\*LOCKED: CLERK

> FBAASUPERV LOOK-UP\]

> ISOR\*\*

> \|

> \|---------------------------------- Contract

> \| File

> \| Enter/Edit

> \| \[FBAA

> \| CONTRACT

> \| FILE\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|---------------------------------- Delete

> \| reject

> \| flag \[FBAA

> \| VOUCHER

> \| DELETE

> \| REJECT\]

> \| \*\*LOCKED:

> \| FBAAREJECT

> \| \*\*

> \|

> \|---------------------------------- Edit

> \| Pharmacy

> \| Invoice

> \| Status

> \| \[FBAA EDIT

> \| INVOICE

> \| STATUS\]

> \|

> \|---------------------------------- Enter/Edit

> \| Suspension

> \| Letters

> \| \[FBAA

> \| ENTER/EDIT

> \| LETTERS\]

> \|

> \|---------------------------------- Fee Basis

> \| 1358

> \| Segregatio

> \| n of Duty

> \| Report \[FB

> \| SEG DUTY

> \| RPT\]

> \|

> \|-------------- Fee --------------- Add/Edit

> \| Schedule Fee

> \| Main Menu Schedule

> \| \[FBAA FEE \[FBAA EDIT

> \| SCHEDULE\] SCHEDULE\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \| \|

> \| \|-------------- Compile

> \| \| Fee

> \| \| Schedule

> \| \| \[FBAA

> \| \| CALCULATE

> \| \| SCHEDULE\]

> \| \|

> \| \|-------------- Print Fee

> \| Schedule

> \| \[FBAA

> \| PRINT

> \| SCHEDULE\]

> \|

> \|

> \|---------------------------------- Finalize a

> \| Batch

> \| \[FBAA

> \| FINALIZE

> \| BATCH\]

> \|

> \|-------------- FPPS -------------- Outpatient

> \| Update & /Ancillary

> \| Transmit Invoice

> \| Menu \[FB Edit \[FBAA

> \| FPPS FPPS EDIT

> \| UPDATE INVOICE\]

> \| MENU\] \*\*LOCKED:

> \| \| FBAASUPERV

> \| \| ISOR\*\*

> \| \|

> \| \|-------------- Pharmacy

> \| \| Invoice

> \| \| Edit \[FBRX

> \| \| FPPS EDIT

> \| \| INVOICE\]

> \| \| \*\*LOCKED:

> \| \| FBAASUPERV

> \| \| ISOR\*\*

> \| \|

> \| \|-------------- Inpatient

> \| \| Invoice

> \| \| Edit \[FBCH

> \| \| FPPS EDIT

> \| \| INVOICE\]

> \| \| \*\*LOCKED:

> \| \| FBAASUPERV

> \| \| ISOR\*\*

> \| \|

> \| \|-------------- Audit

> \| \| Report for

> \| \| FPPS Data

> \| \| \[FB FPPS

> \| \| AUDIT

> \| \| REPORT\]

> \| \|

> \| \|-------------- Report of

> \| \| Transmissi

> \| \| ons to

> \| \| FPPS \[FB

> \| \| FPPS

> \| \| TRANSMIT

> \| \| REPORT\]

> \| \|

> \| \|-------------- Purge

> \| Message

> \| Text \[FB

> \| FPPS

> \| PURGE\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|

> \|---------------------------------- List

> \| Batches

> \| Pending

> \| Release

> \| \[FBAA LIST

> \| CLOSED

> \| BATCHES\]

> \|

> \|-------------- MRA Main --------- Vendor MRA ------- Update FMS

> \| Menu \[FB Main Menu Vendor

> \| MRA MAIN \[FBAA File in

> \| MENU\] VENDOR MRA Austin

> \| \| MAIN MENU\] \[FBAA FMS

> \| \| \*\*LOCKED: UPDATE\]

> \| \| FBAASUPERV \*\*LOCKED:

> \| \| ISOR\*\* FBAASUPERV

> \| \| \| ISOR\*\*

> \| \| \|

> \| \| \|------------ Delete

> \| \| \| Vendor MRA

> \| \| \| \[FBAA MRA

> \| \| \| DELETE

> \| \| \| VENDOR\]

> \| \| \| \*\*LOCKED:

> \| \| \| FBAASUPERV

> \| \| \| ISOR\*\*

> \| \| \|

> \| \| \|------------ Reinstate

> \| \| \| Vendor MRA

> \| \| \| \[FBAA MRA

> \| \| \| VENDOR

> \| \| \| REINSTATE\]

> \| \| \|

> \| \| \|------------ MRA'S

> \| \| Awaiting

> \| \| Austin

> \| \| Approval

> \| \| \[FBAA

> \| \| MRA'S

> \| \| AWAITING

> \| \| APPROVAL\]

> \| \|

> \| \|

> \| \|------------- Veteran ---------- Add type

> \| \| MRA Main Veteran

> \| \| Menu \[FBAA MRA \[FBAA

> \| \| VETERAN MRA

> \| \| MRA MAIN VETERAN

> \| \| MENU\] ADD TYPE\]

> \| \| \|

> \| \| \|------------- Change

> \| \| \| type

> \| \| \| Veteran

> \| \| \| MRA \[FBAA

> \| \| \| MRA

> \| \| \| VETERAN

> \| \| \| CHANGE

> \| \| \| TYPE\]

> \| \| \|

> \| \| \|------------- Delete

> \| \| \| type

> \| \| \| Veteran

> \| \| \| MRA \[FBAA

> \| \| \| MRA

> \| \| \| VETERAN

> \| \| \| DELETE

> \| \| \| TYPE\]

> \| \| \|

> \| \| \|------------- Reinstate

> \| \| type

> \| \| Veteran

> \| \| MRA \[FBAA

> \| \| MRA

> \| \| VETERAN

> \| \| REINSTATE\]

> \| \|

> \| \|

> \| \|-------------------------------- Re-Transmi

> \| \| t MRA's

> \| \| \[FBAA

> \| \| REQUEUE

> \| \| MRA\]

> \| \| \*\*LOCKED:

> \| \| FBAASUPERV

> \| \| ISOR\*\*

> \| \|

> \| \|-------------------------------- Purge

> \| \| Transmitted

> \| \| MRAs

> \| \| \[FBAA MRA

> \| \| \*\*LOCKED:

> \| \| FBAASUPERV

> \| \| ISOR\*\*

> \| \| PURGE\]

> \| \|----------IPAC IPAC -------------- Add Type

> \| Agreement IPAC

> \| MRA Main Agreement

> \| Menu \[FBAA MRA \[FBAA

> \| IPAC MRA IPAC

> \| AGREEMENT ADD TYPE\]

> \| MRA MENU\]

> \| \|

> \| \|-------------- Change

> \| \| Type IPAC

> \| \| Agreement

> \| \| MRA \[FBAA

> \| \| MRA IPAC

> \| \| CHANGE

> \| \| TYPE\]

> \| \|

> \| \|-------------- Delete

> \| Type IPAC

> \| Agreement

> \| MRA \[FBAA

> \| MRA IPAC

> \| DELETE

> \| TYPE\]

> \|

> \|

> \|---------------------------------------------------- Pricer

> \| Batch

> \| Release

> \| \[FBCH

> \| PRICER

> \| RELEASE\]

> \|

> \|---------------------------------------------------- Print

> \| Rejected

> \| Payment

> \| Items

> \| \[FBAA

> \| REJECT

> \| PRINT\]

> \|

> \|---------------------------------------------------- Queue Data

> \| for

> \| Transmissi

> \| on \[FBAA

> \| QUEUE DATA

> \| FOR

> \| TRANS.\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|---------------------------------------------------- Re-initiat

> \| e Rejected

> \| Payment

> \| Items

> \| \[FBAA

> \| REINITIATE

> \| REJECTS\]

> \|

> \|---------------------------------------------------- Release a

> \| Batch

> \| \[FBAA

> \| SUPERVISOR

> \| RELEASE\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|---------------------------------------------------- Reprocess

> \| Overdue

> \| Batch

> \| \[FBAA

> \| REPROCESS

> \| BATCH\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|---------------------------------------------------- Resend

> \| Completed

> \| Batch

> \| \[FBAA

> \| RESEND

> \| VOUCHER

> \| MSG\]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|---------------------------------------------------- Site

> \| Parameter

> \| Enter/Edit

> \| \[FBAA

> \| ENTER SITE

> \| PARAMETERS

> \| \]

> \| \*\*LOCKED:

> \| FBAASUPERV

> \| ISOR\*\*

> \|

> \|-------------- Unauthoriz--------------------------- Add New

> \| ed Claims Person for

> \| File Menu Unauthoriz

> \| \[FBUC FILE ed Claim

> \| MENU\] \[FBUC ADD

> \| \| NEW

> \| \| PERSON\]

> \| \|

> \| \|-------------------------------- Disapprova

> \| \| l Reasons

> \| \| File

> \| \| Enter/Edit

> \| \| \[FBUC

> \| \| DISAPPROVA

> \| \| L REASONS

> \| \| FILE\]

> \| \|

> \| \|-------------------------------- Dispositio

> \| \| ns File

> \| \| Edit \[FBUC

> \| \| DISPOSITIO

> \| \| NS FILE\]

> \| \|

> \| \|-------------------------------- Request

> \| Info File

> \| Enter/Edit

> \| \[FBUC

> \| REQUEST

> \| INFO FILE\]

> \|

> \|

> \|-------------- Void -------------------------------- CH Delete

> Payment Void

> Main Menu Payment

> \[FBAA VOID \[FBCH

> PAYMENT DELETE

> MENU\] VOID\]

> \|

> \|-------------------------------- CH Void

> \| Payment

> \| \[FBCH VOID

> \| PAYMENT\]

> \|

> \|-------------------------------- CNH Delete

> \| Void

> \| Payment

> \| \[FBCNH

> \| DELETE

> \| VOID\]

> \|

> \|-------------------------------- CNH Void

> \| Payment

> \| \[FBCNH

> \| VOID

> \| PAYMENT\]

> \|

> \|-------------------------------- Medical

> \| Delete

> \| Void

> \| Payment

> \| \[FBAA

> \| CANCEL

> \| MEDICAL

> \| VOID\]

> \|

> \|-------------------------------- Medical

> \| Void

> \| Payment

> \| \[FBAA

> \| MEDICAL

> \| VOID

> \| PAYMENT\]

> \|

> \|-------------------------------- Pharmacy

> \| Delete

> \| Void

> \| Payment

> \| \[FBAA

> \| CANCEL

> \| PHARMACY

> \| VOID\]

> \|

> \|-------------------------------- Pharmacy

> Void

> Payment

> \[FBAA

> PHARMACY

> VOID

> PAYMENT\]

> --------------------------------------------------------------- Terminate

> ID Card

> \[FBAA

> TERMINATE

> ID CARD\]

> ----- Vendor --------IPAC IPAC ---------------------------------- Enter/Edit

> Menu \[FBAA Vendor a new IPAC

> VENDOR Agreement Agreement

> OPTIONS\] Menu \[FBAA \[FBAA IPAC

> \| IPAC AGREEMENT

> \| AGREEMENT ENTER/EDIT

> \| MENU\] \]

> \| \|

> \| \|---------------------------------- Delete an

> \| \| IPAC

> \| \| agreement

> \| \| \[FBAA IPAC

> \| \| AGREEMENT

> \| \| DELETE\]

> \| \|

> \| \|---------------------------------- View IPAC

> \| Vendor

> \| Agreement

> \| \[FBAA IPAC

> \| AGREEMENT

> \| VIEW\]

> \|------------------------------------------------------ Display,En

> \| ter,Edit

> \| Demographi

> \| cs \[FBAA

> \| VENDOR

> \| DEMOGRAPHI

> \| CS\]

> \|

> \|---------------------------------------------------- FPDS-Only

> \| Vendor

> \| Edit \[FBAA

> \| VENDOR

> \| FPDS-ONLY\]

> \|

> \|---------------------------------------------------- List

> \| Vendors

> \| Without

> \| FPDS Data

> \| \[FB VEN

> \| FPDS

> \| BLANK\]

> \|

> \|---------------------------------------------------- Payment

> \| Display

> \| for

> \| Patient

> \| \[FBAA

> \| VENDOR

> \| PAYMENT

> \| DISPLAY\]

> \|

> \|---------------------------------------------------- Payment

> \| Look-up

> \| for

> \| Medical

> \| Vendor

> \| \[FBAA

> \| VENDOR

> \| LOOKUP\]

> \|

> \|---------------------------------------------------- Pharmacy

> Vendor

> Payment

> Look-Up

> \[FBAA

> PHARMACY

> LOOKUP\]

> Pharmacy Fee Main Menu (FBAA PHARMACY MAIN MENU)

> \|

> \|

> ----- Batch Menu - Pharmacy \[FBAA ------- Batch Delete \[FBAA BATCH

> PHARMACY BATCH OPTIONS\] DELETE\]

> \|

> \|------------------------------ Close-out Batch \[FBAA CLOSE

> \| BATCH\]

> \|

> \|------------------------------ Display Open Batches \[FBAA

> \| DISPLAY OPEN BATCHES\]

> \|

> \|------------------------------ Edit Batch data \[FBAA BATCH

> \| EDIT\]

> \|

> \|------------------------------ List Items in Batch \[FBAA LIST

> \| BATCH\]

> \|

> \|------------------------------ Open a Pharmacy Batch \[FBAA

> \| OPEN PHARMACY BATCH\]

> \|

> \|------------------------------ Re-open Batch \[FBAA REOPEN

> \| BATCH\]

> \|

> \|------------------------------ Release a Batch \[FBAA

> \| SUPERVISOR RELEASE\]

> \| \*\*LOCKED: FBAASUPERVISOR\*\*

> \|

> \|------------------------------ Status of Batch \[FBAA BATCH

> STATUS\]

> ----------------------------------------- Check Display \[FB CHECK

> DISPLAY\]

> ----------------------------------------- Closeout Pharmacy Invoice

> \[FBAA CLOSE OUT INVOICE\]

> ----------------------------------------- Complete Pharmacy Invoice

> \[FBAA COMPLETE PHARMACY

> INVOICE\]

> ----------------------------------------- Display Pharmacy Invoice \[FBAA

> PHARMACY INVOICE DISPLAY\]

> ----------------------------------------- Edit Pharmacy Invoice \[FBAA

> EDIT PHARMACY INVOICE\]

> ----------------------------------------- Enter Pharmacy Invoice \[FBAA

> ENTER PHARMACY INVOICE\]

> ----------------------------------------- FPPS Claim Inquiry \[FB FPPS

> CLAIM INQ\]

> ----------------------------------------- List Invoices Pending MAS

> Completion \[FBAA PENDING MAS

> COMPLETION\]

> ----------------------------------------- List Pharmacy History \[FBAA

> PHARMACY HISTORY\]

> ----------------------------------------- Patient Re-imbursement \[FBAA

> REIMBURSEMENT PHARMACY\]

> ----------------------------------------- Pharmacy Invoice Status \[FBAA

> PHARMACY INVOICE STATUS\]

> ----------------------------------------- Potential Cost Recovery Report

> \[FB PCR\]

> ----------------------------------------- Prescriptions Pending Pharmacy

> Review \[FBAA LIST PENDING RX\]

> ----------------------------------------- Review Fee Prescription \[FBAA

> PHARMACY REVIEW\]

> ----------------------------------------- Vendor Payments Output \[FB PAY

> VENDOR\]

> ----------------------------------------- Veteran Payments Output \[FB

> PAY VETERAN\]

> Project ARCH Menu (FB PROJECT ARCH MENU)

> \*\*LOCKED: FB ARCH\*\*

> \|

> \|

> ---AD Add/Edit Project ARCH Eligibility

> \[FB ADD ARCH ELIGIBILITY\]

> \*\*LOCKED: FB ARCH\*\*

> ---VW View Project ARCH Eligibility \[FB

> VIEW ARCH ELIGIBILITY\]

> \*\*LOCKED: FB ARCH\*\*

> ---UP ARCH Eligibility Data Upload \[FB

> ARCH DATA UPLOAD\]

> \*\*LOCKED: FB ARCH\*\*

> ---RE ARCH Clinical Reminder Due Delay

> \[FB ARCH REMINDER DELAY\]

> \*\*LOCKED: FB ARCH\*\*

> State Home Main Menu (FBSH MAIN MENU)

> \|

> \|

> ----- Enter New State Home

> Authorization \[FBSH ENTER AUTH\]

> ----- Change a State Home Authorization

> \[FBSH CHANGE AUTH\]

> ----- Delete a State Home Authorization

> \[FBSH DELETE AUTH\]

> ----- Reinstate State Home

> Authorization \[FBSH REINSTATE

> AUTH\]

> ----- Active Authorization Report \[FBSH

> ACTIVE AUTH. REPORT\]

> Telephone Inquiry Menu (FB PHONE MENU)

> \|

> \|

> --------------------------------------------- Check Display \[FB CHECK

> DISPLAY\]

> ----- IPAC Vendor Reports \[FBAA IPAC -------1 DoD Invoice Number Inquiry

> VENDOR REPORT MENU\] \[FBAA IPAC DoD INVOICE

> \| INQUIRY\]

> \|

> \|---------------------------------2 IPAC Vendor DoD Invoice Report

> \| (Summary) \[FBAA IPAC DoD

> \| INVOICE RPT\]

> \|

> \|---------------------------------3 IPAC Vendor Payment Report

> (Detail) \[FBAA IPAC VENDOR

> PAYMENT RPT\]

> --------------------------------------------- Payment Listing for

> Vendor/Veteran \[FB

> VENDOR/VETERAN PAYMENTS\]

> --------------------------------------------- Vendor Payments Output \[FB PAY

> VENDOR\]

> --------------------------------------------- Veteran Payments Output \[FB

> PAY VETERAN\]

> Unauthorized Claim Main Menu (FBUC MAIN)

> \|

> \|

> ----- Enter/Edit Unauthorized Claim ----- Enter Unauthorized Claim \[FBUC

> Menu \[FBUC ENTER/EDIT\] ENTER\]

> \|

> \|------------------------------ Modify Unauthorized Claim

> \| \[FBUC MODIFY UNAUTHORIZED

> \| CLAIM\]

> \|

> \|------------------------------ Disposition Unauthorized Claim

> \| \[FBUC DISPOSITION UNAUTH

> \| CLAIM\]

> \|

> \|------------------------------ Re-open Unauthorized Claim

> \| \[FBUC REOPEN\]

> \|

> \|------------------------------ Initiate Appeal for

> \| Unauthorized Claim \[FBUC

> \| INITIATE APPEAL\]

> \|

> \|------------------------------ Appeal Edit for Unauthorized

> \| Claim \[FBUC APPEAL EDIT\]

> \|

> \|------------------------------ COVA Appeal Enter/Edit \[FBUC

> COVA APPEAL\]

> ----------------------------------------- Request Information on

> Unauthorized Claim \[FBUC

> REQUEST INFORMATION\]

> ----------------------------------------- Receive Requested Information

> \[FBUC RECEIVE INFORMATION\]

> ----- Letters for Unauthorized Claim ---- Update Date Letter Sent \[FBUC

> \[FBUC LETTERS\] UPDATE DATE LETTER SENT\]

> \|

> \|------------------------------ Batch Print Letters \[FBUC

> \| BATCH PRINT LETTERS\]

> \|

> \|------------------------------ Reprint Letter(s) \[FBUC

> REPRINT LETTER(S)\]

> ----------------------------------------- Payments for Unauthorized

> Claims \[FBUC PAYMENTS\]

> ----- Outputs for Unauthorized ---------- All Claims by

> Claims \[FBUC OUTPUTS\] Vendor/Veteran/Other \[FBUC ALL

> \| CLAIMS OUTPUT\]

> \|

> \|------------------------------ Check Display \[FB CHECK

> \| DISPLAY\]

> \|

> \|------------------------------ Disapproved EDI Claim Report

> \| \[FBUC DISAPPROVED EDI\]

> \|

> \|------------------------------ Display Unauthorized Claim

> \| \[FBUC DISPLAY UNAUTHORIZED\]

> \|

> \|------------------------------ Disposition/Status Statistics

> \| Display/Print \[FBUC STATS

> \| OUTPUT\]

> \|

> \|------------------------------ Expiration Display/Print \[FBUC

> \| EXPIRE OUTPUT\]

> \|

> \|------------------------------ FPPS Claim Inquiry \[FB FPPS

> \| CLAIM INQ\]

> \|

> \|------------------------------ Millennium Act Emergency Care

> \| Summary Report \[FBUC MILL ACT

> \| SUMMARY\]

> \|

> \|------------------------------ Status Display/Print of

> \| Unauthorized Claims \[FBUC

> \| STATUS OUTPUT\]

> \|

> \|------------------------------ Unauthorized Claims Cost

> \| Report for Civil Hospital

> \| \[FBCH UC COST REPORT\]

> \|

> \|------------------------------ Vendor Payments Output \[FB PAY

> \| VENDOR\]

> \|

> \|------------------------------ Veteran Payments Output \[FB

> PAY VETERAN\]

> ----------------------------------------- Display Unauthorized Claim

> \[FBUC DISPLAY UNAUTHORIZED\]

> ----- Utilities for Unauthorized -------- Vendor Enter/Edit \[FBCNH

> Claims \[FBUC UTILITIES\] VENDOR ENTER/EDIT\]

> \|

> \|------------------------------ Add New Person for

> \| Unauthorized Claim \[FBUC ADD

> \| NEW PERSON\]

> \|

> \|------------------------------ Associate an Unauthorized

> \| Claim to a Primary \[FBUC

> \| ASSOCIATE\]

> \|

> \|------------------------------ Disassociate an Unauthorized

> \| Claim \[FBUC DISASSOCIATE\]

> \|

> \|------------------------------ Delete Unauthorized Claim

> \| \[FBUC DELETE UNAUTHORIZED

> \| CLAIM\]

> \|

> \|------------------------------ Return Address Display/Edit

> \| \[FBUC RETURN ADDRESS DIS/ED\]

> \|

> \|------------------------------ Extension for Incomplete Mill

> Bill (1725) Claim \[FBUC

> EXTENSION\]

> \*\*LOCKED: FBAASUPERVISOR\*\*Non-Menu Diagram Exported Options

The following options do not appear on the menu but are exported with the package.

- FBAA BATCH SERVER (FB\*3.5\*131)

This server processes incoming Payment Batch Result messages from Central Fee.  The Payment Batch Result message is a response to a Payment Batch message.  The result message provides a count of accepted line items and identifies any line items that were rejected by Central Fee edit checks.

- FBAA MRA PURGE AUTO

> This option is taskable and will purge transmitted MRAs. It should be used <u>only</u> when you are sure Austin has received your MRA transmissions, since use of this option will prevent retransmission of MRAs. Upon successful completion of the purge, a mail message will be sent to a mail group confirming the purge specifics. Remember to add a mail group to the FBAA PURGE TRANSMITTED MRA'S bulletin.

- FBAA MRA SERVER

> This server processes all incoming MRA messages received from Austin through MailMan.

- FBAA PAID SERVER

> This server processes incoming payment information sent from FMS. The job will run in the background and will send a bulletin to the FEE mail group upon completion. The bulletin will detail the number of vendors found for each action type taken. FB\*3.5\*121 the message length from Central Fee is changing to 138 characters. The FBPAID and FBPAID1 routines were modified to accept either length (existing 82 or new 138 character) messages. See Appendix B for the 138 character message format.

- FBAA REJECT SERVER (FB\*3.5\*131)

This server processes incoming Post Voucher Reject messages from Central Fee.  The Post Voucher Reject message identifies payment line items that have been dropped from Central Fee after receipt of the Voucher Batch message for that line item.

- FBAA VOUCHER SERVER (FB\*3.5\*131)

This server processes incoming Voucher Batch Acknowledgement messages from Central Fee.  The Voucher Batch Acknowledgement message contains the Central Fee application acknowledgement for a Voucher Batch message.

- FBUC QUEUE BATCH PRINT

> If your letters are not automatically printed, and you choose not to use the Batch Print Letters option in the Letters for Unauthorized Claim submenu, this option should be run at least once a day.

- FBUC ABANDONED

> This option must be queued to run nightly. A device needs to be specified. It searches the FEE BASIS UNAUTHORIZED CLAIMS file (#162.7) for claims that have the status of INCOMPLETE UNAUTHORIZED CLAIM or APPEAL/ISSUED STATEMENT OF CASE.

> If the expiration date for these claims is met, the claim will be dispositioned to ABANDONED. A printout of those claims which were updated will print to the specified device.

- FB FPPS MONITOR (FB\*3.5\*122)

> If the FB FPPS TRANSMIT option is scheduled to run nightly, this option should be queued to run after it. It checks two new parameters in the FEE BASIS SITE PARAMETERS (#161.4) file to verify that the transmit option is being run in a timely manner (e.g. daily) and sends messages to G.FEE (local VistA users) and REDACTED (Purchased Care Business office) to alert users that payment data is has not been sent. This option may also be run interactively to check the status of the transmit option and can be added as a Fee user’s (e.g. Fee Administrator) secondary menu option. Running the option interactively does not send messages to any mail group.

> Example message to G.FEE mail group:

> Subj: FEE BASIS FPPS Transmit Issue Mar 24, 2011 \[#300421\] 03/24/11@06:01 5 lines From: FEE BASIS In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> Current date: Mar 24, 2011@06:00

> The FB FPPS TRANSMIT option has not run.

> The last completed transmission was on Mar 21, 2011@03:45

> Please check the FB FPPS TRANSMIT option for scheduling issues or errors. Enter message action (in IN basket): Ignore//

> Example message to Fee.EDI_Issues mail group:

REDACTED

- FB PAID TO IB (FB\*3.5\*135)

> FOR FUTURE USE: This run routine option is expected to be scheduled to run regularly after the FBAA PAID SERVER process has completed. This option populates the IB NON/OTHER VA BILLING PROVIDER file (335.93) with information from the FBAA PAID SERVER process that was saved to the FEE BASIS PAID TO IB file(161.9).

- FB PROVIDER TO IB REPORT (FB\*3.5\*135)

> FOR FUTURE USE: This run routine option displays information in the FEE BASIS PAID TO IB file (161.9). This option is for testing purposes to view data and could be added if needed as a secondary menu option.

- FB UCID UTILITY MENU (FB\*3.5\*135)

> This menu option is provided to validate Unique Claim IDentifier during testing of entry and edit functions. This menu option is not available on any existing FB menus, but could be added to a secondary menu. This contains two options: the FB UCID DISPLAY - Fee Basis Unique Claim Identifier Display option, and the FB UCID PAYMENT RPT - FB OUTPATIENT UCID REPORT option.

- FB UCID DISPLAY (FB\*3.5\*135)

> This option is provided to validate Unique Claim IDentifier during testing of entry and edit functions. This option is available on the FB UCID UTILITY MENU. This option has three selections used to display the Unique Claim Identifier. Inpatient invoices and Outpatient claims within a date range, Inpatients by Invoice number, or Outpatient by Vendor, Date of Service, and Procedure.

- FB UCID PAYMENT RPT (FB\*3.5\*135)

> This option is provided to validate the Unique Claim IDentifier during testing of entry and edit functions. This option is available on the FB UCID UTILITY MENU. This option is used to display all UCID’s for a single Outpatient by Vendor, Date of Service, and Procedure.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Archiving

There are currently no archiving capabilities within the Fee Basis package.

Purging

The Fee Basis package allows the user to purge transmitted delete type and reinstate type MRAs through the Purge Transmitted MRAs option under the Supervisor Main Menu of the Medical Fee Main Menu. A site may elect to run this purge manually through use of this option, or have the purge automatically run through a background task by setting up the FB MRA Purge Auto option through TaskMan. It will effectively purge the delete type and reinstate type MRAs automatically and forward a bulletin to the FEE mail group upon completion.

It should be noted that change type and add type MRAs will no longer be purged through use of these options. They will be cleaned up automatically upon confirmation from Austin on each respective transaction.

Contained in Version 3.0 of Fee Basis is a purge routine called FBAABPG. This routine should only be used when batch numbers exceed 9999000 and prior to the site reaching number 9999999 as the next available batch number. This information is found in the FEE BASIS SITE PARAMETERS file (#161.4), Field \#10.

A system backup should be completed prior to the execution of the purge routine. To initiate the purge, you will be prompted for a cutoff date. This date has to be in the past. All batches FINALIZED prior to this date and having no rejects pending will be purged from the FEE BASIS BATCH file (#161.7). All pointed to fields will be deleted as well as any cross-references which use the batch number. Below is a list of files which contain fields which could be affected by the purge.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td>FILE NUMBER</td>
<td><blockquote>
<p>FILE NAME</p>
</blockquote></td>
</tr>
<tr class="even">
<td>162</td>
<td><blockquote>
<p>FEE BASIS PAYMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>162.1</td>
<td><blockquote>
<p>FEE BASIS PHARMACY INVOICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>162.5</td>
<td><blockquote>
<p>FEE BASIS INVOICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>163</td>
<td><blockquote>
<p>FEE BASIS MEDICAL DENIALS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>163.1</td>
<td><blockquote>
<p>FEE BASIS PHARMACY DENIALS</p>
</blockquote></td>
</tr>
</tbody>
</table>

After the purge is complete, the number of batches purged and the To Date will be displayed. Also shown is the FBAA BATCH PURGE bulletin triggered to any mail group entered in the BULLETIN file for this message.

Since there will be a number of sets and kills made to global nodes during this purge, it is important to consider JOURNAL media requirements.

This purge may take a considerable amount of time; therefore, it is recommended the routine be run during off-hours.

The FBAABPG routine will not free up a large amount of disk space.

With DUZ and DT set as well as DUZ(0)="@" in programmer mode, do the following.

\>

\>D ^FBAABPG

The following is an example of the prompts and steps involved in executing the FBAABPG routine. User responses appear in boldface type.

This option is used to purge Fee Basis batch numbers for a time frame in the past. Do you want to continue? No// YES

Purge batch \#'s PRIOR to date : 1/1/93 (JAN 01, 1993)

DEVICE: HOME// QUEUE TO PRINT ON

DEVICE: HOME// A137 RIGHT MARGIN: 80// \<RET\>

\*\*\* BEGIN FEE BASIS BATCH NUMBER PURGE \*\*\*

.....................

> This option has purged 21 batch numbers

> finalized prior to 01/01/93 .

\*\*\* FEE BASIS BATCH NUMBER PURGE FINISHED \*\*\*

The following is an example of an FBAA BATCH PURGE bulletin.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 23%" />
<col style="width: 8%" />
<col style="width: 15%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 2%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4">MailMan message for EMP,NAME</td>
<td colspan="3">FEE SUPERVISOR</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Printed at</td>
<td>REDACTED</td>
<td colspan="2">11 Aug 93 14:41</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Subj:</td>
<td><blockquote>
<p>Fee</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Batch Numbers Purged</p>
</blockquote></td>
<td>[#23124]</td>
<td>11</td>
<td>Aug</td>
<td>93 14:41</td>
<td>1 Line</td>
<td></td>
</tr>
<tr class="even">
<td>From:</td>
<td colspan="2">POSTMASTER (Sender:</td>
<td colspan="2">EMP,NAME)</td>
<td>in</td>
<td colspan="2">'IN' basket.</td>
<td>Page</td>
<td>1</td>
</tr>
</tbody>
</table>

-----------------------------------------------------------------------------

EMP,NAME has run the Fee Batch Number purge routine. The batches were purged on 08/11/93. All batches that were finalized prior to 01/01/93 were purged. The total number of batches purged was 21.

Purging Batch File Entries That Are Seven Years Old or Greater

Purging batch file entries that are seven years old or greater can be accomplished by using the FBAA BATCH 7YR PURGE option off the Batch Main Menu. FBAA BATCH 7YR PURGE can also be set up at sites as a Scheduled Option. Its algorithm is similar to FBAABPG described above and results in a MailMan message also like the one described above. However, there are no user prompts or screen output. The routine executed is FBBPG7Y, and can be run in the foreground with the command: \>D EN^FBBPG7Y.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1. In order to run this package, your facility must be running a <u>minimum</u> of the following.

> VA File Manager V. 20.0

> NEW PERSON file (#200)

> Kernel V. 7.1

> Kernel Toolkit V. 7.2

> IFCAP V. 4.0

> Fee Basis V. 3.0 (if previously running Fee Basis)

> PIMS V. 5.3

> Integrated Billing V. 2.0

> CPT V. 5.0

The VistA Fee Basis software product is fully integrated with Version 20.0 of VA FileMan and Version 7.1 of the Kernel. Version 3.5 is also integrated with the 1358 module of IFCAP. When outpatient batches are released for payment, there will be a posting to the appropriate 1358. For inpatient batches, the estimated amount from the VA Form 10-7078, as well as the actual amount, will be posted to the 1358 when batches are released for payment. The Fee Basis package interfaces with the ADT (Admission-Discharge-Transfer) VISTA module of the PIMS (MAS) package to provide users access to registration data entered through ADT options. Integration with the PTF (Patient Treatment File) module of PIMS allows for the creation of non-VA PTF records. Integration with CPT V. 5.0 allows for entry of modifiers for CPT codes. The package also integrates with the Integrated Billing (IB) package for patient insurance data.

In order to make an entry in the NEW PERSON file (#200), the user must hold the XUSPF200 security key.

2. Fee Basis V. 3.5 custodial integration agreements.

IFCAP (DBIA \#287)

Fee Basis provides IFCAP with a way to determine Fee code sheet headers.

Clinical Reminders (DBIA \#5619)

Fee Basis provides Clinical Reminders with two functions to list the patient’s ARCH (Access Received Closer to Home) Eligibility of a certain date range and a list of all patients and their ARCH Eligibility. FB\*3.5\*119.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 22%" />
<col style="width: 37%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td>5619</td>
<td>NAME:</td>
<td><blockquote>
<p>PROJECT ARCH</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">CUSTODIAL PACKAGE:</td>
<td><blockquote>
<p>FEE BASIS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">SUBSCRIBING PACKAGE:</td>
<td><blockquote>
<p>CLINICAL REMINDERS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Clinical Reminders needs two functions to list the</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>patient's ARCH (Access Received Closer to Home)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Eligibility of a certain date range and a list of all</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>patients and their ARCH Eligibility.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>USAGE:</td>
<td><blockquote>
<p>Private</p>
</blockquote></td>
<td><blockquote>
<p>ENTERED: MAR 24,2011</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>STATUS:</td>
<td><blockquote>
<p>Active</p>
</blockquote></td>
<td><blockquote>
<p>EXPIRES:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

|              |               |
|--------------|---------------|
| DURATION:    | VERSION:      |
| FILE:        | ROOT:         |
| DESCRIPTION: | TYPE: Routine |

> This Integration agreement provides two functions. The output data comes from the ARCH ELIGIBILITY multiple from Fee Basis Patient file \#161.

> \$\$ELIG^FBARCH0 - lists the ARCH (Access Received Closer to Home) eligibility for a patient on a specific date range.

> \$\$LIST^FBARCH0 - provides a list of ARCH eligible patients on a specific date range.

> ROUTINE: FBARCH0 COMPONENT: ELIG

> VARIABLES: DFN Type: Input

> Patient IEN which is DINUM to the internal entry of file \#161.

> FBBDT Type: Input

> Starting/beginning date range of the listing.

> FBEDT Type: Input

> Ending date of the listing.

> FBDATA Type: Output

> An array of patient ARCH eligibility. This function returns the patient's ARCH eligibility. See example below:

> \> S A=\$\$ELIG^FBARCH0(DFN,3100930,3110305,.FBDATA) ZW FBDATA A=1 FBDATA(1)="1^3101130" FBDATA(2)="0^3101030" FBDATA(3)="1^3100930"

> COMPONENT: LIST

> VARIABLES: FBBDT Type: Input

> Starting/beginning date of the listing.

> FBEDT Type: Input

> Ending date of the listing. Output of this function will be in ^TMP(\$J,"ARCHFEE" global. Below is the example:

> \>S A=\$\$LIST^FBARCH0(3100930,3110305)

> Global ^TMP(\$J -- NOTE: translation in effect ^TMP(540785357,"ARCHFEE",1)="12^0^3100930"

> 2)="12^1^3100925"

> 3)="12^0^3100920"

> 4)="12^1^3100910"

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Piece 1</td>
<td colspan="2"><blockquote>
<p>= is the DFN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Piece</td>
<td>2</td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>is the ARCH Eligibility 1 = YES; 0 = NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Piece</td>
<td>3</td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>date of ARCH Eligibility</p>
</blockquote></td>
</tr>
</tbody>
</table>

3. Fee Basis V. 3.5 subscriber integration agreements.

IFCAP (DBIA \#s: 43, 315-A, 315-B, 315-C, 5573, 5574)

IFCAP provides Fee Basis with the following.

- Gets the IFCAP station number and uses it to determine whether an obligation number entered by the user exists in IFCAP.
- Returns all accounting numbers and symbols.
- Posts transactions to 1358.
- Determines whether a 1358 is open and available for posting.
- Verifies that a user can certify without violating 1358 segregation of duty. FB\*3.5\*117
- Returns the events and actors for a 1358 obligation. FB\*3.5\*117

Registration (DBIA \#s: 64, 186-C, 226-A, 226-B, 226-C, 226-D, 226-E, 226-F, 1011) Registration provides Fee Basis with the following.

- Look-up to the BENEFICIARY TRAVEL MODE OF TRANSPORTATION file (#392.4).
- Look-up to the PERIOD OF SERVICE file (#21).
- A call into the routine to create a PTF record.
- Calls to determine Category C status.
- A call into the registration routine.
- A call to display rated disabilities.
- A call to determine last Means Test for a patient.
- Ability to add insurance company information to the PATIENT file (#2).
- A routine to transmit records to a remote location.

Integrated Billing (DBIA \#s: 228-A, 228-B, 396)

Integrated Billing provides Fee Basis with the following.

- Look-up to the PLACE OF SERVICE file (#353.1).
- Look-up to the TYPE OF SERVICE file (#353.2).
- Ability to add insurance information.
- FOR FUTURE USE: Call IB API to move claim providers to IB NON/OTHER VA BILLING PROVIDER (#355.93) file.

Kernel (DBIA \#s: 290-A, 290-B)

Kernel provides Fee Basis with the following.

> • Ability to reference the DEVICE (%ZIS(1)) and TERMINAL TYPE (%ZIS(2)) files.

DRG Grouper (DBIA \#s: 993-A, 993-B, 1010)

DRG Grouper provides Fee Basis with the following.

- Look-up on the "AFEE" cross-reference in the PTF file (#45).
- Look-up to the PTF CLOSE OUT file (#45.84).
- Look-up to the PTF RELEASE file (#45.83).

VA FileMan (DBIA \#: 3352)

VA FileMan provides Fee Basis with the following.

- Ability to re-compile input templates that contain specific fields within a file.

*(This page included for two-sided copying.)*

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any Fee Basis option in File \#19 should be able to run independently provided the user has the appropriate keys.

FOR FUTURE USE: Patch FB\*3.5\*135 introduced File \#161.9 which is populated and self-purged if field \#40 ALLOW FEE BASIS PAID TO IB of file \#161.4 is set to ‘yes’. Entries in this file are processed by a scheduled option FB PAID TO IB which populates the IB NON/OTHER VA BILLING PROVIDER file \#335.93.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All variables associated with the Fee Basis package are of equal importance. There are no package-wide variables associated with this package.

# How to Generate On-Line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure Fee Basis technical documentation. On-line technical documentation pertaining to the Fee Basis software, in addition to that which is located in the help prompts and on the help screens which are found throughout the Fee Basis package, may be generated through utilization of several Kernel options. These include but are not limited to %INDEX; Menu Management, Inquire option and Print Option File; VA FileMan, Data Dictionary Utilities, List File Attributes.

Entering question marks at the "Select ... Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help for that option, if available.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the VISTA Kernel Reference Manual.

%INDEX

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adhere(s) to VistA Programming Standards. The %INDEX output may include the following components: compiled list of Errors and Warnings, Routine Listing, Local Variables, Global Variables, Naked Globals, Label References, and External References. By running %INDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from VISTA Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run %INDEX for the Fee Basis package, specify the following namespaces at the "routine(s) ?\>" prompt: FB\*.

Fee Basis initialization routines which reside in the UCI in which %INDEX is being run, as well as local routines found within the Fee Basis namespace, should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).

INQUIRE OPTION

This Menu Management option provides the following information about a specified option(s): option name, menu text, option description, type of option and lock, if any. In addition, all items on the menu are listed for each menu option.

To secure information about Fee Basis options, the user must specify the name or namespace of the option(s) desired. The namespace associated with the Fee Basis package is FB.

PRINT OPTION FILE

This utility generates a listing of options from the OPTION file. The user may choose to print all of the entries in this file or may elect to specify a single option or range of options. To obtain a list of Fee Basis options, the following option namespace should be specified: FB.

LIST FILE ATTRIBUTES

This VA FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates. For a comprehensive listing of Fee Basis files, please refer to the File Section of this manual.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>NOTICE</u>

Per VA Directive 6402 regarding security of software that affects financial systems, none of the Fee Basis routines or data dictionaries may be modified.

The Fee Basis package deals with activities and data related to the Fiscal and Fee Basis payment processes of your facility. The obvious need for package security has been addressed throughout this software, making every effort to restrict the mishandling of Fee Basis functionality. A significant amount of testing, as well as VA Central Office review, has been conducted on the entire Fee Basis package. Medical Administration Service and the Office of Budget and Finance have requested that each facility utilizing the Fee Basis package appreciate the sensitivity of these issues. It is for these reasons that each facility is reminded that local modification of the program code is expressly prohibited.

The modification of DHCP National Package software and Data Dictionaries is restricted to the adding of new data elements and to the creation of input/output templates necessary to meet the specific needs of the local facility.

The concern for package security extends to the menus assigned to the Fee Basis users. No Fee Basis user should have access to all of the options available. While a Fee Medical Clerk should be able to open, close, edit, or reopen a Fee Basis batch by utilizing multiple batch options, the Fiscal Voucher Clerk should only be able to finalize a Fee Basis batch. The standard menus that accompany this package were specifically designed to account for those functions that are performed in Fiscal and MAS. You do have the ability to customize menus for users, but be aware that a conflict of interest might arise.

### Audit Trails

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the FEE NOTIFICATION/REQUEST file (#162.2), the following two fields are sent out with audit turned on if they are changed.

- LEGAL ENTITLEMENT (162.2,8)
- MEDICAL ENTITLEMENT (162.2,11)

Patch FB\*3.5\*151 enhances the software to maintain a history of changes to the value of thirteen fields in the FEE BASIS UNAUTHORIZED CLAIMS (#162.7) file and five fields in the AUTHORIZATION multiple of the FEE BASIS PATIENT (#161) file. The system will retain the date and time of the change, the old value, the new value, and the person that made the change in a new DATA AUDIT multiple within the respective file. Once the patch is installed, the system will retain this information for the fields listed below.

Monitored fields in FEE BASIS UNAUTHORIZED CLAIMS (#162.7) file:

- STATUS (#24)
- DISPOSITION (#10)
- DATE CLAIM RECEIVED (#.01)
- DATE REQ INFO SENT (#19.6)
- DATE VALID CLAIM RECEIVED (#7)
- DATE OF DISPOSITION (#11)
- REOPEN CLAIM DATE (#21)
- NOTICE OF DISAGREEMENT RECV'D (#50)
- STATEMENT OF THE CASE ISSUED (#51)
- DATE SUBSTANTIVE APPEAL RECV'D (#52)
- DATE APPEAL DISPOSITIONED (#53)
- DATE APPEALED TO COVA (#54)
- DATE COVA APPEAL DISPOSITIONED (#55)

Monitored fields in AUTHORIZATION multiple of FEE BASIS PATIENT (#161) file:

- FROM DATE (#.01)
- TO DATE (#.02)
- DISCHARGE TYPE (#.06)
- PURPOSE OF VISIT CODE (#.07)
- TREATMENT TYPE CODE (#.095)

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FBAA ESTABLISH VENDOR</td>
<td>This Security Key allows a user to add vendors to the Fee Basis Vendor file (#161.2).</td>
</tr>
<tr class="even">
<td>FB ARCH</td>
<td><p>This Security Key allows authorized users to identify patients that were not included in the original Project ARCH Increment 1 eligibility dataset and allows them to be marked as being Project ARCH Eligible in the local VistA system. The system now allows locally added patients to be marked Not Project ARCH Eligible by users that hold the FB ARCH Security Key.</p>
<p>NOTE: The "View Project ARCH Eligibility" option allows authorized users to view nationally and locally identified Project ARCH patients.</p></td>
</tr>
<tr class="odd">
<td>FB IPAC VENDOR</td>
<td>This Security Key permits the holder to enter, edit, and delete IPAC Agreement records through the options on the IPAC Vendor Agreement Menu.</td>
</tr>
<tr class="even">
<td>FBAAFINANCE</td>
<td>This Security Key permits the holder to finalize (complete) a payment batch. That action generates the Voucher Batch message, which instructs Central Fee (Austin) to release the payments to a downstream payment system such as FMS. This security key would normally be assigned to finance staff responsible for completing the batch.</td>
</tr>
<tr class="odd">
<td>FBAAREJECT</td>
<td>This Security Key permits the holder to flag payment line items as locally rejected and to delete local reject flags that were entered in error.</td>
</tr>
<tr class="even">
<td>FBAASUPERVISOR</td>
<td>This Security Key provides authorized users access to all of the Fee Supervisor options.</td>
</tr>
<tr class="odd">
<td>XUSPF200</td>
<td>This Security Key is used when adding a person to the new person file (#200). Its holders are not required to enter a Social Security Number (SSN) upon input of the person.</td>
</tr>
</tbody>
</table>

### Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fee Basis software package makes use of Current Procedural Terminology (CPT) codes which is an AMA copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the American Medical Association.

## File Protection 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Electronic Data Interface contains files that are standardized. They carry a higher level of file protection with regard to Delete, Read, Write, and LAYGO access, and should not be edited locally unless otherwise directed. The data dictionaries for all files should NOT be altered.

The following is a list of recommended VA FileMan access codes associated with each file contained in the KIDS build for the EDI interface.

| FILE NUMBER | FILE NAME                 | DD ACCESS | RD ACCESS | WR ACCESS | DEL ACCESS | LAYGO ACCESS | AUDIT ACCESS |
|-----------------|-------------------------------|---------------|---------------|---------------|----------------|------------------|------------------|
| 161             | FEE BASIS PATIENT             | @             | \#            | \#            | \#             | \#               |                  |
| 161.2           | FEE BASIS VENDOR              | @             | \#            | \#            | \#             | \#               |                  |
| 161.21          | FEE BASIS CNH CONTRACT        | @             | \#            | \#            | \#             | \#               | \#               |
| 161.22          | FEE BASIS CNH RATE            | @             | \#            | \#            | \#             | \#               | \#               |
| 161.23          | FEE BASIS CNH                 |               |               |               |                |                  |                  |
|                 | AUTHORIZATION RATE            | @             | \#            | \#            | \#             | \#               | \#               |
| 161.25          | FEE BASIS VENDOR              |               |               |               |                |                  |                  |
|                 | CORRECTION                    | @             | \#            | \#            | \#             | \#               | \#               |
| 161.26          | FEE BASIS PATIENT MRA         | @             | \#            | \#            | \#             | \#               |                  |
| 161.27          | FEE BASIS SUSPENSION          | @             | \#            | @             | @              | @                |                  |
| 161.3           | FEE BASIS LETTER              | @             | \#            | \#            | \#             | \#               |                  |
| 161.4           | FEE BASIS SITE PARAMETERS     | @             | \#            | \#            | \#             | \#               |                  |
| 161.5           | FEE CH REPORT OF CONTACT      | @             | \#            | \#            | \#             | \#               | \#               |
| 161.6           | FEE BASIS SPECIALTY CODE      | @             | \#            | @             | @              | @                |                  |
| 161.7           | FEE BASIS BATCH               | @             | \#            | \#            | \#             | \#               |                  |
| 161.8           | FEE BASIS PROGRAM             | @             | \#            | @             | @              | @                |                  |
| 161.81          | FEE BASIS PARTICIPATION       |               |               |               |                |                  |                  |
|                 | CODE                          | @             | \#            | @             | @              | @                |                  |
| 161.82          | FEE BASIS PURPOSE OF VISIT    | @             | \#            | @             | @              | @                |                  |
| 161.83          | FEE BASIS ID CARD AUDIT       | @             | \#            | \#            | @              | \#               |                  |
| 161.84          | FEE BASIS CATEGORY OF CARE    | @             | @             | @             | @              | @                |                  |
| 161.95          | IPAC VENDOR AGREEMENT FILE    | @             | \#            | \#            | \#             | \#               |                  |
| 161.96          | IPAC VENDOR AGREEMENT MRA     | @             | \#            | \#            | \#             | \#               |                  |
| 161.99          | FEE BASIS PAYMENT REJECT CODE | @             |               | @             | @              | @                | @                |
| 162             | FEE BASIS PAYMENT             | @             | \#            | \#            | \#             | \#               |                  |
| 162.1           | FEE BASIS PHARMACY INVOICE    | @             | \#            | \#            | \#             | \#               |                  |
| 162.2           | FEE NOTIFICATION/REQUEST      | @             | \#            | \#            | \#             | \#               |                  |
| 162.3           | FEE CNH ACTIVITY              | @             | \#            | \#            | \#             | \#               |                  |
| 162.4           | VA FORM 10-7078               | @             | \#            | \#            | \#             | \#               |                  |
| 162.5           | FEE BASIS INVOICE             | @             | \#            | \#\`          | \#             | \#               |                  |
| 162.6           | FEE BASIS DISPOSITION CODE    | @             | \#            | @             | @              | @                |                  |
| 162.7           | FEE BASIS UNAUTHORIZED        |               |               |               |                |                  |                  |
|                 | CLAIMS                        | @             | \#            | \#            | \#             | \#               |                  |
| 162.8           | FEE BASIS UNAUTHORIZED        |               |               |               |                |                  |                  |
|                 | CLAIMS PENDING INFO           | @             | \#            | \#            | \#             | \#               |                  |
| 162.91          | FEE BASIS UNAUTHORIZED        |               |               |               |                |                  |                  |
|                 | CLAIMS DISPOSITIONS           | @             | \#            | @             | @              | @                | @                |
| 162.92          | FEE BASIS UNAUTHORIZED        |               |               |               |                |                  |                  |
|                 | CLAIMS STATUS                 | @             | \#            | @             | @              | @                | @                |
| 162.93          | FEE BASIS UNAUTHORIZED        |               |               |               |                |                  |                  |
|                 | REQUESTED INFORMATION         | @             | \#            | \#            | \#             | \#               | \#               |
| 162.94          | FEE BASIS UNAUTHORIZED        |               |               |               |                |                  |                  |
|                 | DISAPPROVAL REASONS           | @             | \#            | @             | @              | @                | @                |
| 162.95          | FEE BASIS CHECK               |               |               |               |                |                  |                  |
|                 | CANCELLATION REASON           | @             | \#            | @             | @              | @                |                  |
| 163.85          | FEE BASIS VA TYPE OF          |               |               |               |                |                  |                  |
|                 | SERVICE                       | @             | \#            | @             | @              | @                | @                |
| 163.99          | FEE BASIS FEE SCHEDULE        | @             | \#            | \#            | \#             | \#               |                  |

*(This page included for two-sided copying.)*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ancillary Cost Charges associated with a 7078/Authorization for Civil Hospital not paid
> directly to the contract hospital (e.g., physicians, lab services, etc.).
Batch Grouping by which fee basis bills are paid.
BVA Board of Veterans Appeals
C&P Compensation and Pension
CAQH Council for Affordable Quality Healthcare. Provides CORE certification test suite with step by step test scripts.
CARC Claim Adjustment Reason Code. The CARC provides the reason for the positive or negative financial adjustment specific to particular claim or service referenced in the transmitted v5010 X12 835. The external list of CARCs is maintained by the Codes Maintenance Committee established by the Blue Cross and Blue Shield Association, with a multi-stakeholder voting membership.
COJ Clinic of Jurisdiction
CORE Committee on Operating Rules for Information Exchange. CORE® is a multi-stakeholder initiative created, organized and facilitated by CAQH that is working to make it easier for physicians and hospitals to access eligibility, benefits and claim information for their patients at the point of care.
COVA Court of Veterans Appeals
DHCP Decentralized Hospital Computer Program
DRG Diagnostic Related Group
EDI Electronic Data Interchange
HAPE Health Administration Product Enhancements
HIPAA Health Insurance Portability and Accountability Act
IFCAP Integrated Funds Distribution, Control Point Activity, Accounting, and
> Procurement.
Invoice Statement of charges received from a vendor for Community Nursing
> Home, Civil Hospital, medical, or pharmacy services rendered to a
> Veteran.
IPAC Intragovernmental Payment and Collection. A system in the Department
> Treasury, which is used when the VA is making payment to the DoD for Veteran episodes of care in Military Treatment Facilities.
JCAHO Joint Commission on Accreditation of Health Care Organizations.
Legal Determination by the fee clerk, based on the veteran's
Entitlement entitlement to VA benefits, of legal eligibility for Civil Hospital.
Medical Determination by a VA physician, based on whether
Entitlement an emergency existed at the time of admission, of
> medical eligibility for Civil Hospital.
Military time The method of recording time that is the standard of the
> United States military.
MRA Master record adjustment
NPI National Provider Identifier – A unique ten digit, numerics only,
Number issued by the Center for Medicaid and Medicare Services
(CMS) to providers, both individual and organizational.
NVHS Non-VA Hospital System
NVP Non-VA Pricer System
Non-formulary A drug not on the routine pharmacy list for which the
Drug prescribing physician or the receiving patient must have prior
approval/authorization.
Obligation Numbers assigned by Fiscal Service representing
Numbers fee monies (long term, short term, travel, etc.) against which fee basis
batches are paid.
PC Purchased Care
Pricer A software package used by Austin to determine the medical
reimbursement amount for a specific DRG.
PSA Primary Service Area
RARC Remittance Advice Remark Code. Provides supplemental information about why a claim or service line is not paid in full. The external list of RARCs is maintained by the Centers for Medicare & Medicaid Services (CMS). The majority of CARCs do not require RARCs to complete the message; however, there are some specific CARCs that require use of an explanatory RARC.
\<RETURN\> or The key that is pressed after each response in order to
\<RET\> move the cursor to the next line and to enter your response into the
system.
Security Code A code assigned to the user that identifies the user to the
system and allows access to different areas within the
system. This includes access and verify codes as well as
security keys.
Special Key A key that instructs the system to perform a function. For instance, the
\<RET\> key not only moves you to the next prompt, it also enters the
information you have just keyed into the system.
Suspension Letter sent to vendors informing them of the difference
Letter between amount charged, amount paid, and the reason why.
UCID Unique Claim IDentifier - a unique 28 character identifier for Inpatient invoices, and Outpatient claims.
Unauthorized Payment for expenses of inpatient medical services
Claim obtained by eligible veterans without prior authorization
from the VA.
Up-arrow \<^\> The upper case character on the number "six" key. It is
used as a special function key.
Vendor Any provider of care (e.g., doctors, hospitals, pharmacies, etc.)
*(This page included for two-sided copying.)*

# Appendix A – Transmission Mappings[^1]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 35%" />
<col style="width: 13%" />
<col style="width: 0%" />
<col style="width: 34%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><h2 id="a-1-mra-mapping-c1">A-1 MRA Mapping C1</h2></th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th colspan="4"><blockquote>
<p><strong>LOCATED IN FILE 161.2</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>NOT IN FILE 161.2</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td>1</td>
<td colspan="3">RECORD TYPE CODE</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td>2</td>
<td colspan="3">ACTION CODE</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td>3 - 8</td>
<td colspan="3">STATION NUMBER</td>
</tr>
<tr class="even">
<td colspan="2">9 – 21</td>
<td>ID NUMBER (1)</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td>22</td>
<td colspan="3">FEE ONLY INDICATOR</td>
</tr>
<tr class="even">
<td colspan="2">23 – 24</td>
<td><blockquote>
<p>SPECIALTY CODE (.05)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">25 – 26</td>
<td><blockquote>
<p>PARTICIPANT CODE (7)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2">27 – 56</td>
<td><blockquote>
<p>NAME (.01)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">57 – 86</td>
<td><blockquote>
<p>STREET ADDRESS (2)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2">87 – 116</td>
<td><blockquote>
<p>STREET ADDRESS 2 (2.5)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">117 – 135</td>
<td><blockquote>
<p>CITY (3)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2">136 – 137</td>
<td><blockquote>
<p>STATE (4)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">138 – 146</td>
<td><blockquote>
<p>ZIP CODE (5)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2">147 – 148</td>
<td><blockquote>
<p>MAIL ROUTE CODE (5.18)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">149 – 151</td>
<td><blockquote>
<p>COUNTY CODE (5.5)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2">152</td>
<td><blockquote>
<p>PROVIDER CODE (30.05)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">156</td>
<td><blockquote>
<p>TAX ID/SSN FLAG (30.06)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2">157</td>
<td><blockquote>
<p>1099 VENDOR (30.03)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">158</td>
<td><blockquote>
<p>FMS VENDOR TYPE (30.04)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td>156–170</td>
<td colspan="3">DHCP INTERNAL CONTROL NUM</td>
</tr>
<tr class="odd">
<td colspan="2">171 – 182</td>
<td><blockquote>
<p>FPDS (24 &amp; 25)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2">183 – 192</td>
<td><blockquote>
<p>NPI (41.01)</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td>193</td>
<td colspan="3">'$'</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 33%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><h2 id="a-2-mra-mapping-c4"><br />
A-2 MRA Mapping C4</h2></th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th colspan="3"><blockquote>
<p><strong>LOCATED IN FILE 161.2</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>NOT IN FILE 161.2</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"></td>
<td></td>
<td>1</td>
<td colspan="2">RECORD TYPE CODE</td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td></td>
<td>2</td>
<td colspan="2">ACTION CODE</td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td></td>
<td>3-8</td>
<td colspan="2">STATION NUMBER</td>
</tr>
<tr class="even">
<td colspan="3">9 – 17</td>
<td><blockquote>
<p>ID NUMBER (1)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">18 - 21</td>
<td>CHAIN (C4, 8)</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td></td>
<td>22</td>
<td colspan="2">FEE ONLY INDICATOR</td>
</tr>
<tr class="odd">
<td colspan="3">23 – 52</td>
<td><blockquote>
<p>PHARMACY NAME (.01)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">53 – 82</td>
<td><blockquote>
<p>STREET ADDRESS (2)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">83 – 112</td>
<td><blockquote>
<p>STREET ADDRESS 2 (2.5)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">113 – 131</td>
<td><blockquote>
<p>CITY (3)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">132 – 133</td>
<td><blockquote>
<p>STATE (4)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">134 – 142</td>
<td><blockquote>
<p>ZIP CODE (5)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">143 – 144</td>
<td><blockquote>
<p>MAIL ROUTE CODE (5.18)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">145 – 147</td>
<td><blockquote>
<p>COUNTY CODE (5.5)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">148</td>
<td><blockquote>
<p>PROVIDER CODE (30.05)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">149</td>
<td><blockquote>
<p>TAX ID/SSN FLAG (30.06)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">150</td>
<td><blockquote>
<p>1099 VENDOR (30.03)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">151</td>
<td><blockquote>
<p>FMS VENDOR TYPE (30.04)</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td></td>
<td>152 – 166</td>
<td colspan="2">DHCP INTERNAL CONTROL NUM</td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td></td>
<td>167 – 178</td>
<td colspan="2">FILLER</td>
</tr>
<tr class="odd">
<td colspan="3">179 – 188</td>
<td>NPI (41.01)</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td></td>
<td>189</td>
<td colspan="2">'$'</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 33%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><h2 id="a-3-mra-mapping-c8">A-3 MRA Mapping C8</h2></th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th><strong>Pos</strong></th>
<th colspan="3"><blockquote>
<p><strong>IPAC Agreement MRA record</strong></p>
<p><strong>Description 161.95 Field#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3">1-1</td>
<td>Record Type Code</td>
<td>n/a</td>
<td colspan="2">“8”</td>
</tr>
<tr class="even">
<td colspan="3">2-2</td>
<td>Action Code</td>
<td>n/a</td>
<td colspan="2"><p>A for Add</p>
<p>C for Change</p>
<p>D for Delete</p></td>
</tr>
<tr class="odd">
<td colspan="3">3-8</td>
<td>Station Number</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">9-18</td>
<td>IPAC Agreement ID</td>
<td>.01</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">19-31</td>
<td>Vendor ID</td>
<td>1</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">32-35</td>
<td>Fiscal Year</td>
<td>2</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">36-95</td>
<td>Short Description</td>
<td>4</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">96-108</td>
<td>Sharing Agreement Number</td>
<td>5</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">109-109</td>
<td>Status</td>
<td>3</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">110-110</td>
<td>Delimiter (Block)</td>
<td>n/a</td>
<td colspan="2">“~”</td>
</tr>
<tr class="odd">
<td colspan="3">1-8</td>
<td>Customer ALC</td>
<td>6</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">9-35</td>
<td>Receiver TAS</td>
<td>7</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">36-62</td>
<td>Sender TAS</td>
<td>7.5</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">63-70</td>
<td>Agency Field Station Number</td>
<td>8</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">71-87</td>
<td>Obligating Document Number</td>
<td>9</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">88-88</td>
<td>Delimiter (Block)</td>
<td>n/a</td>
<td colspan="2">“~”</td>
</tr>
<tr class="odd">
<td colspan="3">1-60</td>
<td>Station Contact Name</td>
<td>10</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">61-77</td>
<td>Station Contact Phone</td>
<td>11</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">78-177</td>
<td>Station Contact E-mail</td>
<td>12</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">178-178</td>
<td>Delimiter (Block)</td>
<td>n/a</td>
<td colspan="2">“~”</td>
</tr>
<tr class="odd">
<td colspan="3">1-60</td>
<td>Complete Line of Accounting</td>
<td>13</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">61-61</td>
<td>Delimiter (Block)</td>
<td>n/a</td>
<td colspan="2">“~”</td>
</tr>
<tr class="odd">
<td colspan="3">1-200</td>
<td>Description of Goods and Services</td>
<td>14</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">201-201</td>
<td>Delimiter (Block)</td>
<td>n/a</td>
<td colspan="2">“~”</td>
</tr>
<tr class="odd">
<td colspan="3">1-220</td>
<td>Miscellaneous Information (1)</td>
<td>15</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">221-221</td>
<td>Delimiter (Block)</td>
<td>n/a</td>
<td colspan="2">“~”</td>
</tr>
<tr class="odd">
<td colspan="3">1-100</td>
<td>Miscellaneous Information (2)</td>
<td>16</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">101-101</td>
<td>Delimiter (Block)</td>
<td>n/a</td>
<td colspan="2">“~”</td>
</tr>
<tr class="odd">
<td colspan="3">102-102</td>
<td>Delimiter (Record)</td>
<td>n/a</td>
<td colspan="2">“$”</td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 0%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 32%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 2%" />
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="8"><h2 id="a-4-batch-header">A-4 Batch Header</h2></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>POSITION</strong></th>
<th colspan="2"><blockquote>
<p><strong>VARIABLE NAME</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3">1 – 3</td>
<td colspan="2">FBHD - value of FEE or FEN</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">4 – 5</td>
<td colspan="2">FBAABT - value of 'B3' FOR MEDICAL PAYMENTS;</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="2">" " 'B5' FOR HOMETOWN PHARMACY PAYMENTS;</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td colspan="2">" " 'C1' FOR VENDOR FILE ACTIVITIES;</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="2">" " 'C2' FOR VETERAN MRA ACTIVITIES;</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td colspan="2">" " 'C4' FOR PHARMACY FILE ACTIVITIES;</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="2">" " 'C8' FOR IPAC AGREEMENT MRA ACTIVITIES;</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td colspan="2">" " 'B2' FOR TRAVEL PAYMENTS;</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="2">" " 'B9' FOR CH/CNH;</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td colspan="2">" " 'BT'</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">6 – 13</td>
<td colspan="2">FBAACD - Date formatted MMDDYYYY</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">14 – 19</td>
<td colspan="2">FBAASN - Station number + ”-“ + substation number</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">20 – 26</td>
<td colspan="2">FBAABN - Batch Number</td>
<td colspan="2">.01</td>
<td>161.7</td>
<td colspan="2">NUMBER</td>
</tr>
<tr class="even">
<td colspan="3">27</td>
<td colspan="2">SPACE</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3">28- 38</td>
<td colspan="2">FBAAAP - amount with no decimal</td>
<td colspan="2">9</td>
<td>161.7</td>
<td colspan="2">TOTAL DOLLARS</td>
</tr>
<tr class="even">
<td colspan="3">39 – 40</td>
<td colspan="2">FBAACP Obligation number</td>
<td colspan="2">1</td>
<td>161.7</td>
<td colspan="2">OBLIGATION NUMBER</td>
</tr>
<tr class="odd">
<td colspan="3">41</td>
<td colspan="2">“ “ - SPACE</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="3">42</td>
<td colspan="2">“$” – RECORD DELIMITER</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 0%" />
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 0%" />
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><h2 id="a-5-b3-outpatientancillary-batch"><br />
A-5 B3 (Outpatient/Ancillary) Batch</h2></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>POSITION</strong></th>
<th><strong>VARIABLE NAME</strong></th>
<th><strong>FIELD #</strong></th>
<th colspan="2"><strong>FILE #</strong></th>
<th colspan="2"><strong>FIELD NAME</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td colspan="2">Value of '3'</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>2 – 7</td>
<td colspan="2">FBAASN</td>
<td colspan="2">16</td>
<td>161.7</td>
<td colspan="2">STATION NUMBER</td>
</tr>
<tr class="odd">
<td>8 – 17</td>
<td colspan="2">FBSSN</td>
<td colspan="2">9</td>
<td>2</td>
<td colspan="2">SSN</td>
</tr>
<tr class="even">
<td>18</td>
<td colspan="2">FBPAYT</td>
<td colspan="2">18</td>
<td>162</td>
<td colspan="2">PAYMENT TYPE CODE</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>'R' FOR REIMBURSEMENT;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>'S' FOR STATISTICAL;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>'V' FOR VENDOR;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>19 – 53</td>
<td colspan="2">FBPNAMX</td>
<td colspan="2">.01</td>
<td>2</td>
<td colspan="2">PATIENT NAME</td>
</tr>
<tr class="odd">
<td>54 - 66</td>
<td colspan="2">FBVID</td>
<td colspan="2">1</td>
<td>161.2</td>
<td colspan="2">VENDOR ID NUMBER</td>
</tr>
<tr class="even">
<td>67 - 74</td>
<td colspan="2">FBAP</td>
<td colspan="2">6;1;2;2</td>
<td>162</td>
<td colspan="2">AMOUNT PAYED</td>
</tr>
<tr class="odd">
<td>75 – 78</td>
<td colspan="2">FBAAON</td>
<td colspan="2">3</td>
<td>161.7</td>
<td colspan="2">TYPE</td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>'B3' FOR MEDICAL PAYMENTS</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>'B5' FOR HOMETOWN PHARMACY PAYMENTS</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>'C1' FOR VENDOR FILE ACTIVITIES</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>'C2' FOR VETERAN MRA ACTIVITIES</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>'C4' FOR PHARMACY FILE ACTIVITIES</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>'B2' FOR TRAVEL PAYMENTS;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>'B9' FOR CH/CNH</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>79</td>
<td colspan="2">FBSUSP</td>
<td colspan="2">6;1;2;4</td>
<td>162</td>
<td colspan="2">SUSPEND CODE</td>
</tr>
<tr class="even">
<td>80 – 81</td>
<td colspan="2">FBPOV</td>
<td colspan="2">6;1;2;16</td>
<td>162</td>
<td colspan="2">PURPOSE OF VISIT</td>
</tr>
<tr class="odd">
<td>82 - 83</td>
<td colspan="2">FBPATT</td>
<td colspan="2">6;1;2;15</td>
<td>162</td>
<td colspan="2">TREATMENT TYPE CODE</td>
</tr>
<tr class="even">
<td>84 – 91</td>
<td colspan="2">FBTD converts to FBTDSR1</td>
<td colspan="2">6;1;.01</td>
<td>162</td>
<td colspan="2">INITIAL TREATMENT DATE</td>
</tr>
<tr class="odd">
<td>92</td>
<td colspan="2">FBTT</td>
<td colspan="2">UNKNOWN =&gt;</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>93 – 100</td>
<td colspan="2">FBDIN</td>
<td colspan="2">6;1;2;13</td>
<td>162</td>
<td colspan="2">DATE CURRENT INVOICE RECEIVED</td>
</tr>
<tr class="odd">
<td>101 – 109</td>
<td colspan="2">FBINVN</td>
<td colspan="2">6;1;2;15</td>
<td>162</td>
<td colspan="2">INVOICE NUMBER</td>
</tr>
<tr class="even">
<td>110 – 142</td>
<td colspan="2">RESERVE FOR FUTURE USE</td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>143 - 144</td>
<td colspan="2">FBST</td>
<td colspan="2">1</td>
<td>5</td>
<td colspan="2">STATE</td>
</tr>
<tr class="even">
<td>145 - 147</td>
<td colspan="2">FBCTY</td>
<td colspan="2">5;.01;3</td>
<td>5</td>
<td colspan="2">VA COUNTY CODE</td>
</tr>
<tr class="odd">
<td>148 – 156</td>
<td colspan="2">FBZIP</td>
<td colspan="2"></td>
<td>2</td>
<td colspan="2">ZIP CODE</td>
</tr>
<tr class="even">
<td>157 – 159</td>
<td colspan="2">FBPSA</td>
<td colspan="2">6;1;2;12</td>
<td>162</td>
<td colspan="2">PRIMARY SERVICE</td>
</tr>
<tr class="odd">
<td>160 – 164</td>
<td colspan="2">FBCPT</td>
<td colspan="2">.01</td>
<td>81</td>
<td colspan="2">CPT CODE</td>
</tr>
<tr class="even">
<td>165 – 166</td>
<td colspan="2">FBPOS</td>
<td colspan="2">6;1;2;30</td>
<td>162</td>
<td colspan="2">PLACE OF SERVICE</td>
</tr>
<tr class="odd">
<td>167 – 168</td>
<td colspan="2">FBHCFA</td>
<td colspan="2">6;1;2;31</td>
<td>162</td>
<td colspan="2">HCFA TYPE OF SERVICE</td>
</tr>
<tr class="even">
<td>169 - 170</td>
<td colspan="2">FBVTOS</td>
<td colspan="2">6;1;2;29</td>
<td>162</td>
<td colspan="2">VA TYPE OF SERVICE</td>
</tr>
<tr class="odd">
<td>171 - 177</td>
<td colspan="2">FBPD</td>
<td colspan="2">6;1;2;28</td>
<td>162</td>
<td colspan="2">PRIMARY DIAGNOSIS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>178</p>
</blockquote></td>
<td colspan="2">COMPUTED</td>
<td colspan="2">6;1;2;33</td>
<td>162</td>
<td colspan="2">PROMPT PAY TYPE</td>
</tr>
<tr class="odd">
<td>179 -186</td>
<td colspan="2">SPACES</td>
<td colspan="2">NO FIELD ASSOCIATED</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>187 - 216</td>
<td colspan="2">FBPICN</td>
<td colspan="2">VISTA INTERNAL CONTROL NUMBER</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>217 – 214</td>
<td colspan="2"></td>
<td colspan="2">COMPUTE VENDOR INVOICE DATE</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>225 – 232</td>
<td colspan="2">FBADMIT</td>
<td colspan="2">3.5</td>
<td><blockquote>
<p>162.4</p>
</blockquote></td>
<td colspan="2">DATE OF ADMISSION</td>
</tr>
<tr class="odd">
<td>233 – 240</td>
<td colspan="2">FBDOB</td>
<td colspan="2"></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td colspan="2">DATE OF BIRTH</td>
</tr>
<tr class="even">
<td><blockquote>
<p>241</p>
</blockquote></td>
<td colspan="2">“~”</td>
<td colspan="2"></td>
<td></td>
<td colspan="2">BLOCK DELIMITER</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 0%" />
<col style="width: 23%" />
<col style="width: 1%" />
<col style="width: 15%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 34%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="9"><h2 id="a-6-b3-outpatientancillary-batch-line-2"><br />
A-6 B3 (Outpatient/Ancillary) Batch (Line 2)</h2></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>POSITION</strong></th>
<th colspan="2"><strong>VARIABLE NAME</strong></th>
<th colspan="2"><strong>FIELD #</strong></th>
<th><strong>FILE #</strong></th>
<th colspan="2"><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 – 5</td>
<td colspan="2"><blockquote>
<p>FBUNITS</p>
</blockquote></td>
<td colspan="2">6;1;2;47</td>
<td colspan="2">162</td>
<td><blockquote>
<p>UNITS PAID</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td colspan="2"><blockquote>
<p>FBAUTHF</p>
</blockquote></td>
<td colspan="2">„A‟ or „U‟</td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7 – 11</td>
<td colspan="2"><blockquote>
<p>FBMOD1</p>
</blockquote></td>
<td colspan="2">6;1;2;46;.01</td>
<td colspan="2">162</td>
<td><blockquote>
<p>CPT MODIFIER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>12 – 16</td>
<td colspan="2"><blockquote>
<p>FBMOD2</p>
</blockquote></td>
<td colspan="2">6;1;2;46;.01</td>
<td colspan="2">162</td>
<td><blockquote>
<p>CPT MODIFIER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>17 – 21</td>
<td colspan="2"><blockquote>
<p>FBMOD3</p>
</blockquote></td>
<td colspan="2">6;1;2;46;.01</td>
<td colspan="2">162</td>
<td><blockquote>
<p>CPT MODIFIER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>22 – 26</td>
<td colspan="2"><blockquote>
<p>FBMOD4</p>
</blockquote></td>
<td colspan="2">6;1;2;46;.01</td>
<td colspan="2">162</td>
<td><blockquote>
<p>CPT MODIFIER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>27 - 31</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FBADJR1</p>
</blockquote></td>
<td colspan="2">6;1;2;52;.01</td>
<td colspan="2">162</td>
<td><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>32 – 36</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FBADJR2</p>
</blockquote></td>
<td colspan="2">6;1;2;52;.01</td>
<td colspan="2">162</td>
<td><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>37 – 45</td>
<td colspan="2"><blockquote>
<p>AFADJA1</p>
</blockquote></td>
<td colspan="2">6;1;2;52;2</td>
<td colspan="2">162</td>
<td><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>46 – 54</td>
<td colspan="2"><blockquote>
<p>ABADJA2</p>
</blockquote></td>
<td colspan="2">6;1;2;52;2</td>
<td colspan="2">162</td>
<td><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>55 - 64</td>
<td colspan="2"><blockquote>
<p>NPI</p>
</blockquote></td>
<td colspan="2">41.01</td>
<td colspan="2">162</td>
<td><blockquote>
<p>NPI</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>65 - 84</td>
<td colspan="2"><blockquote>
<p>FBSCID</p>
</blockquote></td>
<td colspan="2">6;1;2;49</td>
<td colspan="2">162</td>
<td><blockquote>
<p>PATIENT ACCOUNT NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>85</td>
<td colspan="2"><blockquote>
<p>FBEDIF</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2">162</td>
<td><blockquote>
<p>EDI FLAG</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>86 - 105</td>
<td colspan="2"><blockquote>
<p>FBCNTRN</p>
</blockquote></td>
<td colspan="2">6;1;2;54</td>
<td colspan="2">162</td>
<td><blockquote>
<p>CONTRACT NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>106 – 115</td>
<td colspan="2"><blockquote>
<p>FBIA</p>
</blockquote></td>
<td colspan="2">6;1;2;.05</td>
<td colspan="2">162</td>
<td><blockquote>
<p>IPAC AGREEMENT (pointer to file 161.95)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>116 – 137</td>
<td colspan="2"><blockquote>
<p>FBDODINV</p>
</blockquote></td>
<td colspan="2">6;1;2;.055</td>
<td colspan="2">162</td>
<td><blockquote>
<p>DoD INVOICE NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>138</td>
<td colspan="2"><blockquote>
<p>“~”</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td><blockquote>
<p>BLOCK DELIMITER</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 23%" />
<col style="width: 1%" />
<col style="width: 15%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 34%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="8"><h2 id="a-7-b3-outpatientancillary-batch-line-3"><br />
A-7 B3 (Outpatient/Ancillary) Batch (Line 3)</h2></th>
</tr>
<tr class="odd">
<th><strong>POSITION</strong></th>
<th colspan="2"><strong>VARIABLE NAME</strong></th>
<th colspan="2"><strong>FIELD #</strong></th>
<th><strong>FILE #</strong></th>
<th colspan="2"><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 - 12</td>
<td><blockquote>
<p>FBFPPSID</p>
</blockquote></td>
<td colspan="2">6;1;2;50</td>
<td colspan="2">162</td>
<td><blockquote>
<p>FPPS CLAIM ID</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>13 - 41</td>
<td><blockquote>
<p>FBAUTHNUM</p>
</blockquote></td>
<td colspan="2">6;1;2;83</td>
<td colspan="2">162</td>
<td><blockquote>
<p>AUTHORIZATION NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>42 - 44</td>
<td><blockquote>
<p>FBLNITM</p>
</blockquote></td>
<td colspan="2">6;1;2;51</td>
<td colspan="2">162</td>
<td><blockquote>
<p>FPPS LINE ITEM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>45 – 56</td>
<td><blockquote>
<p>FBAMTC</p>
</blockquote></td>
<td colspan="2">6;1;2;1</td>
<td colspan="2">162</td>
<td><blockquote>
<p>AMOUNT CLAIMED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>57 - 58</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td colspan="2">6;1;2;52;1</td>
<td colspan="2">161.92</td>
<td><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>59 – 64</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>65 – 70</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>71 – 72</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td colspan="2">6;1;2;52;1</td>
<td colspan="2">161.92</td>
<td><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>73 – 78</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>79 – 84</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>85 – 86</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td colspan="2">6;1;2;52;1</td>
<td colspan="2">161.92</td>
<td><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>87 - 91</td>
<td><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td colspan="2">6;1;2;52;.01</td>
<td colspan="2">161.91</td>
<td><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>92 - 97</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>98 - 103</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>104 - 112</td>
<td><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td colspan="2">6;1;2;52;2</td>
<td colspan="2">162</td>
<td><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>113 - 114</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td colspan="2">6;1;2;52;1</td>
<td colspan="2">161.92</td>
<td><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>115 - 119</td>
<td><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td colspan="2">6;1;2;52;.01</td>
<td colspan="2">161.91</td>
<td><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>120 - 125</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>126 - 131</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>132 - 140</td>
<td><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td colspan="2">6;1;2;52;2</td>
<td colspan="2">162</td>
<td><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>141 – 142</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td colspan="2">6;1;2;52;1</td>
<td colspan="2">161.92</td>
<td><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>143 – 147</td>
<td><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td colspan="2">6;1;2;52;.01</td>
<td colspan="2">161.91</td>
<td><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>148 – 153</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>154 – 159</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td colspan="2">6;1;2;53;.01</td>
<td colspan="2">161.93</td>
<td><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>160 – 168</td>
<td><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td colspan="2">6;1;2;52;2</td>
<td colspan="2">162</td>
<td><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>169</td>
<td><blockquote>
<p>FBPYMTH</p>
</blockquote></td>
<td colspan="2">6;1;2;82</td>
<td colspan="2">163.98</td>
<td><blockquote>
<p>PAYMENT METHODOLOGY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>170</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td colspan="2">N/A</td>
<td colspan="2">N/A</td>
<td><blockquote>
<p>ADDITIONAL PAYMENT INDICATOR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>171</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td colspan="2">N/A</td>
<td colspan="2">N/A</td>
<td><blockquote>
<p>ADDITIONAL PAYMENT TYPE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>172 - 201</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td colspan="2">N/A</td>
<td colspan="2">N/A</td>
<td><blockquote>
<p>Parent Internal Control Number</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>202 - 203</td>
<td><blockquote>
<p>“~$”</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td><blockquote>
<p>BLOCK/RECORD DELIMITERS</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 26%" />
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 28%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><h2 id="a-8-b5-batch">A-8 B5 Batch</h2></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>POSITION</strong></th>
<th><strong>VARIABLE NAME</strong></th>
<th><strong>FIELD #</strong></th>
<th><strong>FILE #</strong></th>
<th colspan="2"><strong>FIELD NAME</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>Value of “5"</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>2 – 7</td>
<td colspan="2"><blockquote>
<p>FBAASN</p>
</blockquote></td>
<td>16</td>
<td>161.7</td>
<td colspan="2">STATION NUMBER</td>
</tr>
<tr class="odd">
<td>8 – 17</td>
<td colspan="2"><blockquote>
<p>FBSSN</p>
</blockquote></td>
<td>9</td>
<td>2</td>
<td colspan="2">SSN</td>
</tr>
<tr class="even">
<td>18</td>
<td colspan="2"><blockquote>
<p>FBPAYT 162.11</p>
<p>'R' FOR REIMBURSEMENT;</p>
<p>'S' FOR STATISTICAL;</p>
<p>'V' FOR VENDOR;</p>
</blockquote></td>
<td>16</td>
<td></td>
<td colspan="2">PAYMENT TYPE CODE</td>
</tr>
<tr class="odd">
<td>19 – 53</td>
<td colspan="2"><blockquote>
<p>FBPNAMX</p>
</blockquote></td>
<td>.01</td>
<td>2</td>
<td colspan="2">PATIENT NAME</td>
</tr>
<tr class="even">
<td>54 – 62</td>
<td colspan="2"><blockquote>
<p>FBVID</p>
</blockquote></td>
<td>1</td>
<td>161.2</td>
<td colspan="2">ID NUMBER</td>
</tr>
<tr class="odd">
<td>63 – 66</td>
<td colspan="2"><blockquote>
<p>FBCSN</p>
</blockquote></td>
<td>8</td>
<td>161.2</td>
<td colspan="2">CHAIN NUMBER</td>
</tr>
<tr class="even">
<td>67 – 74</td>
<td colspan="2"><blockquote>
<p>FBAC</p>
</blockquote></td>
<td>3</td>
<td>162.11</td>
<td colspan="2">AMOUNT CLAIMED</td>
</tr>
<tr class="odd">
<td>75 – 82</td>
<td colspan="2"><blockquote>
<p>FBAP</p>
</blockquote></td>
<td>6.5</td>
<td>162.11</td>
<td colspan="2">AMOUNT PAYED</td>
</tr>
<tr class="even">
<td>83 – 86</td>
<td colspan="2"><blockquote>
<p>FBAAON</p>
</blockquote></td>
<td>$E(161.7:1,3,6)</td>
<td>161.7</td>
<td colspan="2">OBLIGATION NUMBER</td>
</tr>
<tr class="odd">
<td>87</td>
<td colspan="2"><blockquote>
<p>FBSUSP</p>
</blockquote></td>
<td>.01</td>
<td>161.27</td>
<td colspan="2">SUSPENSE CODE</td>
</tr>
<tr class="even">
<td>88 - 95</td>
<td colspan="2"><blockquote>
<p>FBTD converts to FBTDSR1</p>
</blockquote></td>
<td>2</td>
<td>162.11</td>
<td colspan="2">DATE PRESCRIPTION FILLED</td>
</tr>
<tr class="odd">
<td>96 – 103</td>
<td colspan="2"><blockquote>
<p>FBRX</p>
</blockquote></td>
<td>.01</td>
<td>162.11</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>104 –111</td>
<td colspan="2"><blockquote>
<p>FBDIN</p>
</blockquote></td>
<td>1</td>
<td>162.1</td>
<td colspan="2">DATE CURRENT INVOICE RECEIVED</td>
</tr>
<tr class="odd">
<td>112 – 120</td>
<td colspan="2"><blockquote>
<p>FBINVN</p>
</blockquote></td>
<td>.01</td>
<td>162.1</td>
<td colspan="2">INVOICE NUMBER</td>
</tr>
<tr class="even">
<td>121 - 153</td>
<td colspan="2"><blockquote>
<p>SPACES</p>
</blockquote></td>
<td>FUTURE USE</td>
<td></td>
<td colspan="2">FUTURE USE (FOREIGN ADDRESS)</td>
</tr>
<tr class="odd">
<td>154 – 155</td>
<td colspan="2"><blockquote>
<p>FBST</p>
</blockquote></td>
<td>1</td>
<td>5</td>
<td colspan="2">STATE</td>
</tr>
<tr class="even">
<td>156 -158</td>
<td colspan="2"><blockquote>
<p>FBCTY</p>
</blockquote></td>
<td>2</td>
<td>5.01</td>
<td colspan="2">VA COUNTY CODE</td>
</tr>
<tr class="odd">
<td>159 – 167</td>
<td colspan="2"><blockquote>
<p>FBZIP</p>
</blockquote></td>
<td>4</td>
<td>162.11</td>
<td colspan="2">ZIP CODE</td>
</tr>
<tr class="even">
<td>168 – 170</td>
<td colspan="2"><blockquote>
<p>FBPSA</p>
</blockquote></td>
<td>25</td>
<td>162.11</td>
<td colspan="2">PRIMARY SERVICE FACILITY</td>
</tr>
<tr class="odd">
<td>171</td>
<td colspan="2"><blockquote>
<p>FBY</p>
</blockquote></td>
<td>29</td>
<td>162.11</td>
<td colspan="2">INTEREST INDICATOR</td>
</tr>
<tr class="even">
<td>172 – 179</td>
<td colspan="2"><blockquote>
<p>FBCLM</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2">DATE TO CALM</td>
</tr>
<tr class="odd">
<td>180 – 209</td>
<td colspan="2"><blockquote>
<p>FBPICN</p>
</blockquote></td>
<td>NO FIELD ASSOCIATED</td>
<td></td>
<td colspan="2">INTERNAL VISTA CONTROL NUMBER</td>
</tr>
<tr class="even">
<td>210 – 217</td>
<td colspan="2"><blockquote>
<p>FBVIN</p>
</blockquote></td>
<td>12</td>
<td>162.1</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>218</td>
<td colspan="2"><blockquote>
<p>“~”</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2">BLOCK DELIMITER</td>
</tr>
</tbody>
</table>

## <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 31%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="8"><h2 id="a-9-b5-batch-line-2">A-9 B5 Batch (Line 2)</h2></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>POSITION</strong></th>
<th><strong>VARIABLE NAME</strong></th>
<th colspan="2"><strong>FIELD #</strong></th>
<th colspan="2"><strong>FILE #</strong></th>
<th colspan="2"><strong>FIELD NAME</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 - 5</td>
<td colspan="2"><blockquote>
<p>FBADJR1</p>
</blockquote></td>
<td></td>
<td colspan="2">162.14</td>
<td colspan="3">ADJUSTMENT REASON</td>
</tr>
<tr class="even">
<td>6 - 10</td>
<td colspan="2"><blockquote>
<p>FBADJR2</p>
</blockquote></td>
<td></td>
<td colspan="2">162.14</td>
<td colspan="3">ADJUSTMENT REASON</td>
</tr>
<tr class="odd">
<td>11 - 19</td>
<td colspan="2"><blockquote>
<p>FBADJA1</p>
</blockquote></td>
<td></td>
<td colspan="2">162.14</td>
<td colspan="3">ADJUSTMENT AMOUNT</td>
</tr>
<tr class="even">
<td>20 - 28</td>
<td colspan="2"><blockquote>
<p>FBADJA2</p>
</blockquote></td>
<td></td>
<td colspan="2">162.14</td>
<td colspan="3">ADJUSTMENT AMOUNT</td>
</tr>
<tr class="odd">
<td>29 - 38</td>
<td colspan="2"><blockquote>
<p>FBNPI</p>
</blockquote></td>
<td>41.01</td>
<td colspan="2">161.2</td>
<td colspan="3">NATIONAL PROVIDER IDENTIFIER</td>
</tr>
<tr class="even">
<td>39</td>
<td colspan="2"><blockquote>
<p>FBEDIC</p>
</blockquote></td>
<td>13</td>
<td colspan="2">162.1</td>
<td colspan="3">EDI CLAIM FLAG</td>
</tr>
<tr class="odd">
<td>40 – 49</td>
<td colspan="2"><blockquote>
<p>FBIA</p>
</blockquote></td>
<td>14</td>
<td colspan="2">162.1</td>
<td colspan="3">IPAC VENDOR AGREEMENT</td>
</tr>
<tr class="even">
<td>50 - 71</td>
<td colspan="2"><blockquote>
<p>FBDODINV</p>
</blockquote></td>
<td>39</td>
<td colspan="2">162.11</td>
<td colspan="3">DoD INVOICE NUMBER</td>
</tr>
<tr class="odd">
<td>72 – 83</td>
<td colspan="2"><blockquote>
<p>FBFPPSID</p>
</blockquote></td>
<td>13</td>
<td colspan="2">162.1</td>
<td colspan="3">FPPS CLAIM ID</td>
</tr>
<tr class="even">
<td>84 – 112</td>
<td colspan="2"><blockquote>
<p>FBAUTHNUM</p>
</blockquote></td>
<td>4;40</td>
<td colspan="2">162.11</td>
<td colspan="3">AUTHORIZATION NUMBER</td>
</tr>
<tr class="odd">
<td>113 – 115</td>
<td colspan="2"><blockquote>
<p>FBLNITM</p>
</blockquote></td>
<td>4;36</td>
<td colspan="2">162.11</td>
<td colspan="3">FPPS LINE ITEM</td>
</tr>
<tr class="even">
<td>116 – 127</td>
<td colspan="2"><blockquote>
<p>FBAMTCLM</p>
</blockquote></td>
<td>4;3</td>
<td colspan="2">162.11</td>
<td colspan="3">AMOUNT CLAIMED</td>
</tr>
<tr class="odd">
<td>128 – 129</td>
<td colspan="2"><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>37;1</td>
<td colspan="2">161.92</td>
<td colspan="3">ADJUSTMENT GROUP</td>
</tr>
<tr class="even">
<td>130 – 135</td>
<td colspan="2"><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="odd">
<td>136 – 141</td>
<td colspan="2"><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="even">
<td>142 - 143</td>
<td colspan="2"><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>37;1</td>
<td colspan="2">161.92</td>
<td colspan="3">ADJUSTMENT GROUP</td>
</tr>
<tr class="odd">
<td>144 – 149</td>
<td colspan="2"><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="even">
<td>150 – 155</td>
<td colspan="2"><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="odd">
<td>156 – 157</td>
<td colspan="2"><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>37;1</td>
<td colspan="2">161.92</td>
<td colspan="3">ADJUSTMENT GROUP</td>
</tr>
<tr class="even">
<td>158 – 162</td>
<td colspan="2"><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td>37;.01</td>
<td colspan="2">161.91</td>
<td colspan="3">ADJUSTMENT REASON</td>
</tr>
<tr class="odd">
<td>163 – 168</td>
<td colspan="2"><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="even">
<td>169 – 174</td>
<td colspan="2"><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="odd">
<td>175 - 183</td>
<td colspan="2"><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td>37;2</td>
<td colspan="2">162.14</td>
<td colspan="3">ADJUSTMENT AMOUNT</td>
</tr>
<tr class="even">
<td>184 - 185</td>
<td colspan="2"><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>37;1</td>
<td colspan="2">162.14</td>
<td colspan="3">ADJUSTMENT GROUP</td>
</tr>
<tr class="odd">
<td>186 – 190</td>
<td colspan="2"><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td>37;.01</td>
<td colspan="2">161.91</td>
<td colspan="3">ADJUSTMENT REASON</td>
</tr>
<tr class="even">
<td>191 – 196</td>
<td colspan="2"><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="odd">
<td>197 – 202</td>
<td colspan="2"><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="even">
<td>203 - 211</td>
<td colspan="2"><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td>37;2</td>
<td colspan="2">162.14</td>
<td colspan="3">ADJUSTMENT AMOUNT</td>
</tr>
<tr class="odd">
<td>212 – 213</td>
<td colspan="2"><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>37;1</td>
<td colspan="2">161.92</td>
<td colspan="3">ADJUSTMENT GROUP</td>
</tr>
<tr class="even">
<td>214 – 218</td>
<td colspan="2"><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td>37;.01</td>
<td colspan="2">161.91</td>
<td colspan="3">ADJUSTMENT REASON</td>
</tr>
<tr class="odd">
<td>219 – 224</td>
<td colspan="2"><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="even">
<td>225 – 230</td>
<td colspan="2"><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>38;.01</td>
<td colspan="2">161.93</td>
<td colspan="3">REMITTANCE REMARK</td>
</tr>
<tr class="odd">
<td>231 - 239</td>
<td colspan="2"><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td>37;2</td>
<td colspan="2">162.14</td>
<td colspan="3">ADJUSTMENT AMOUNT</td>
</tr>
<tr class="even">
<td>240 – 251</td>
<td colspan="2"><blockquote>
<p>FBQNTY</p>
</blockquote></td>
<td>4;1.6</td>
<td colspan="2">162.11</td>
<td colspan="3">QUANTITY</td>
</tr>
<tr class="odd">
<td>252 -253</td>
<td colspan="2"><blockquote>
<p>“~$</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td colspan="3">BLOCK/RECORD DELIMITERS</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 1%" />
<col style="width: 26%" />
<col style="width: 1%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 7%" />
<col style="width: 24%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="9"><h2 id="a-10-b9-inpatient-batch">A-10 B9 Inpatient Batch</h2></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>POSITION</strong></th>
<th colspan="2"><strong>VARIABLE NAME</strong></th>
<th colspan="2"><strong>FIELD #</strong></th>
<th colspan="2"><strong>FILE #</strong></th>
<th colspan="3"><strong>FIELD NAME</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>Value of “9"</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="even">
<td>2 – 7</td>
<td colspan="2"><blockquote>
<p>FBAASN</p>
</blockquote></td>
<td colspan="2">16</td>
<td colspan="2">161.7</td>
<td colspan="3"><blockquote>
<p>STATION NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>8 – 17</td>
<td colspan="2"><blockquote>
<p>FBSSN</p>
</blockquote></td>
<td colspan="2">9</td>
<td colspan="2">2</td>
<td colspan="3"><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>18</td>
<td colspan="2"><blockquote>
<p>FBPAYT</p>
<p>'R' FOR REIMBURSEMENT;</p>
<p>'S' FOR STATISTICAL;</p>
<p>'V' FOR VENDOR;</p>
</blockquote></td>
<td colspan="2">18</td>
<td colspan="2">162</td>
<td colspan="3"><blockquote>
<p>PAYMENT TYPE CODE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>19 – 53</td>
<td colspan="2"><blockquote>
<p>FBPNAMX</p>
</blockquote></td>
<td colspan="2">.01</td>
<td colspan="2">2</td>
<td colspan="3"><blockquote>
<p>PATIENT NAME</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>54 – 66</td>
<td colspan="2"><blockquote>
<p>FBVID</p>
</blockquote></td>
<td colspan="2">1</td>
<td colspan="2">161.2</td>
<td colspan="3"><blockquote>
<p>MEDICAL VENDOR ID NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>67 – 75</td>
<td colspan="2"><blockquote>
<p>FBAP</p>
</blockquote></td>
<td colspan="2">8</td>
<td colspan="2">162.5</td>
<td colspan="3"><blockquote>
<p>AMOUNT PAYED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>76 – 79</td>
<td colspan="2"><blockquote>
<p>FBAAON</p>
</blockquote></td>
<td colspan="2">$E(161.7:1,3,6)</td>
<td colspan="2"></td>
<td colspan="3"><blockquote>
<p>OBLIGATION NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>80</td>
<td colspan="2"><blockquote>
<p>FBSUSP</p>
</blockquote></td>
<td colspan="2">10</td>
<td colspan="2">162.5</td>
<td colspan="3"><blockquote>
<p>SUSPEND CODE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>81 – 82</td>
<td colspan="2"><blockquote>
<p>FBPOV</p>
</blockquote></td>
<td colspan="2">21</td>
<td colspan="2">162.5</td>
<td colspan="3"><blockquote>
<p>PURPOSE OF VISIT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>83 - 84</td>
<td colspan="2"><blockquote>
<p>FBPATT</p>
</blockquote></td>
<td colspan="2">22</td>
<td colspan="2">162.5</td>
<td colspan="3"><blockquote>
<p>PATIENT TYPE</p>
<p>CODE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>85 – 92</td>
<td colspan="2"><blockquote>
<p>FBFTD</p>
</blockquote></td>
<td colspan="2">5</td>
<td colspan="2">162.5</td>
<td colspan="3"><blockquote>
<p>FROM DATE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>93 – 100</td>
<td colspan="2"><blockquote>
<p>FBTTD</p>
</blockquote></td>
<td colspan="2">6</td>
<td colspan="2">162.5</td>
<td colspan="3"><blockquote>
<p>TO DATE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>101 – 108</td>
<td colspan="2"><blockquote>
<p>FBDIN</p>
</blockquote></td>
<td colspan="2">1</td>
<td colspan="2">162.5</td>
<td colspan="3"><blockquote>
<p>DATE CURRENT</p>
<p>INVOICE RECEIVED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>109 – 117</td>
<td colspan="2"><blockquote>
<p>FBINVN</p>
</blockquote></td>
<td colspan="2">.01</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>INVOICE NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>118 – 123</td>
<td colspan="2"><blockquote>
<p>FBVMID</p>
</blockquote></td>
<td colspan="2">2</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>MEDICARE ID</p>
<p>NUMBER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>124 - 156</td>
<td colspan="2"><blockquote>
<p>SPACES</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="3"><blockquote>
<p>RESERVED FOR FOREIGN ADDRESS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>157 – 158</td>
<td colspan="2"><blockquote>
<p>FBST</p>
</blockquote></td>
<td colspan="2">1</td>
<td colspan="2"><blockquote>
<p>5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>STATE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>159 -161</td>
<td colspan="2"><blockquote>
<p>FBCTY</p>
</blockquote></td>
<td colspan="2">2</td>
<td colspan="2"><blockquote>
<p>5.01</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>VA COUNTY CODE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>162 – 170</td>
<td colspan="2"><blockquote>
<p>FBZIP</p>
</blockquote></td>
<td colspan="2">3</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ZIP CODE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>171 – 173</td>
<td colspan="2"><blockquote>
<p>FBPSA</p>
</blockquote></td>
<td colspan="2">23</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRIMARY SERVICE</p>
<p>FACILITY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>174</td>
<td colspan="2"><blockquote>
<p>FBPPT</p>
</blockquote></td>
<td colspan="2">47</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROMPT PAY TYPE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>175 – 182</td>
<td colspan="2"><blockquote>
<p>SPACES</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="3"><blockquote>
<p>DATE TO CALM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>183</td>
<td colspan="2"><blockquote>
<p>SPACE</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="odd">
<td>184 - 188</td>
<td colspan="2"><blockquote>
<p>SPACES</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="3"><blockquote>
<p>CPT FILLER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>189 – 195</td>
<td colspan="2"><blockquote>
<p>FBDX(1)</p>
</blockquote></td>
<td colspan="2">30</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>196</td>
<td colspan="2"><blockquote>
<p>FBPOA1</p>
</blockquote></td>
<td colspan="2">30.02</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>197 – 203</td>
<td colspan="2"><blockquote>
<p>FBDX(2)</p>
</blockquote></td>
<td colspan="2">31</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD2</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>204</td>
<td colspan="2"><blockquote>
<p>FBPOA2</p>
</blockquote></td>
<td colspan="2">31.02</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>205 – 211</td>
<td colspan="2"><blockquote>
<p>FBDX(3)</p>
</blockquote></td>
<td colspan="2">32</td>
<td colspan="2"><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD3</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>212</td>
<td colspan="2"><blockquote>
<p>FBPOA3</p>
</blockquote></td>
<td colspan="2">32.02</td>
<td colspan="2"><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 3</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>213 – 219</td>
<td colspan="2"><blockquote>
<p>FBDX(4)</p>
</blockquote></td>
<td colspan="2">33</td>
<td colspan="2"><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD4</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>220</td>
<td colspan="2"><blockquote>
<p>FBPOA4</p>
</blockquote></td>
<td colspan="2">33.02</td>
<td colspan="2"><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 4</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>221 – 227</td>
<td colspan="2"><blockquote>
<p>FBDX(5)</p>
</blockquote></td>
<td colspan="2">34</td>
<td colspan="2"><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD5</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>228</td>
<td colspan="2"><blockquote>
<p>FBPOA5</p>
</blockquote></td>
<td colspan="2">34.02</td>
<td colspan="2"><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 5</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>229</td>
<td colspan="2"><blockquote>
<p>“~”</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="3"><blockquote>
<p>BLOCK DELIMITER</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 1%" />
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 23%" />
<col style="width: 12%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><h2 id="a-11-b9-inpatient-batch-line-2">A-11 B9 Inpatient Batch (Line 2)</h2></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>POSITION</strong></th>
<th><strong>VARIABLE NAME</strong></th>
<th><strong>FIELD #</strong></th>
<th colspan="2"><strong>FILE #</strong></th>
<th colspan="3"><strong>FIELD NAME</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 - 23</td>
<td colspan="2"><blockquote>
<p>FBPICN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="3">VISTA INTERNAL CONTROL NUMBER</td>
<td></td>
</tr>
<tr class="even">
<td>24 - 31</td>
<td colspan="2"><blockquote>
<p>$$AUSDT^FBAAV3(+FBY)</p>
</blockquote></td>
<td>46</td>
<td>162.5</td>
<td colspan="3">VENDOR INVOICE DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>32 – 38</td>
<td colspan="2"><blockquote>
<p>FBPRC(1)</p>
</blockquote></td>
<td>40</td>
<td>162.5</td>
<td colspan="3">PRC1</td>
<td></td>
</tr>
<tr class="even">
<td>39 – 45</td>
<td colspan="2"><blockquote>
<p>FBPRC(2)</p>
</blockquote></td>
<td>41</td>
<td>162.5</td>
<td colspan="3">PRC2</td>
<td></td>
</tr>
<tr class="odd">
<td>46 – 52</td>
<td colspan="2"><blockquote>
<p>FBPRC(3)</p>
</blockquote></td>
<td>42</td>
<td>161.5</td>
<td colspan="3">PRC3</td>
<td></td>
</tr>
<tr class="even">
<td>53 – 59</td>
<td colspan="2"><blockquote>
<p>FBPRC(4)</p>
</blockquote></td>
<td>43</td>
<td>161.5</td>
<td colspan="3">PRC4</td>
<td></td>
</tr>
<tr class="odd">
<td>60 – 66</td>
<td colspan="2"><blockquote>
<p>FBPRC(5)</p>
</blockquote></td>
<td>44</td>
<td>161.5</td>
<td colspan="3">PRC5</td>
<td></td>
</tr>
<tr class="even">
<td>67 – 75</td>
<td colspan="2"><blockquote>
<p>FBAC</p>
</blockquote></td>
<td>7</td>
<td>162.5</td>
<td colspan="3">AMOUNT CLAIMED</td>
<td></td>
</tr>
<tr class="odd">
<td>76 - 84</td>
<td colspan="2"><blockquote>
<p>FBPA</p>
</blockquote></td>
<td>26</td>
<td>162.5</td>
<td colspan="3">PRICER AMOUNT</td>
<td></td>
</tr>
<tr class="even">
<td>85 – 88</td>
<td colspan="2"><blockquote>
<p>FBDRG</p>
</blockquote></td>
<td>24</td>
<td>162.5</td>
<td colspan="3">DISCHARGE DRG</td>
<td></td>
</tr>
<tr class="odd">
<td>89</td>
<td colspan="2"><blockquote>
<p>SPACE</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="even">
<td>90 – 97</td>
<td colspan="2"><blockquote>
<p>FBADMIT</p>
</blockquote></td>
<td>3.5</td>
<td>162.4</td>
<td colspan="3">DATE OF ADMISSION</td>
<td></td>
</tr>
<tr class="odd">
<td>98 – 105</td>
<td colspan="2"><blockquote>
<p>FBDISDT</p>
</blockquote></td>
<td>4.5</td>
<td>162.4</td>
<td colspan="3">DATE OF DISCHARGE</td>
<td></td>
</tr>
<tr class="even">
<td>106 – 113</td>
<td colspan="2"><blockquote>
<p>FBDOB</p>
</blockquote></td>
<td></td>
<td>2</td>
<td colspan="3">DATE OF BIRTH</td>
<td></td>
</tr>
<tr class="odd">
<td>114 – 116</td>
<td colspan="2"><blockquote>
<p>FBDIST</p>
</blockquote></td>
<td>1;.06</td>
<td>161</td>
<td colspan="3">DISCHARGE TYPE</td>
<td></td>
</tr>
<tr class="even">
<td>117 – 121</td>
<td colspan="2"><blockquote>
<p>FBCDAYS</p>
</blockquote></td>
<td>54</td>
<td>162.5</td>
<td colspan="3">COVERED DAYS</td>
<td></td>
</tr>
<tr class="odd">
<td>122</td>
<td colspan="2"><blockquote>
<p>FBAUTHF</p>
</blockquote></td>
<td>“A‟or“U‟</td>
<td></td>
<td colspan="3">AUTHORIZED/UNAUTHORIZED</td>
<td></td>
</tr>
<tr class="even">
<td>123 – 127</td>
<td colspan="2"><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td>8;.01</td>
<td>162.5</td>
<td colspan="3"><p>ADJUSTMENT</p>
<p>REASON</p></td>
<td></td>
</tr>
<tr class="odd">
<td>128 – 137</td>
<td colspan="2"><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td>8;2</td>
<td>162.5</td>
<td colspan="3"><p>ADJUSTMENT</p>
<p>AMOUNT</p></td>
<td></td>
</tr>
<tr class="even">
<td>138 – 147</td>
<td colspan="2"><blockquote>
<p>FBNPI</p>
</blockquote></td>
<td>41.01</td>
<td>161.2</td>
<td colspan="3">NPI</td>
<td></td>
</tr>
<tr class="odd">
<td>148 - 154</td>
<td colspan="2"><blockquote>
<p>FBDX(0)</p>
</blockquote></td>
<td>39</td>
<td>162.5</td>
<td colspan="3">ADMITTING DIAGNOSIS</td>
<td></td>
</tr>
<tr class="even">
<td>155 - 174</td>
<td colspan="2"><blockquote>
<p>FBCSID</p>
</blockquote></td>
<td>55</td>
<td>162.5</td>
<td colspan="3">PATIENT ACCOUNT NUMBER</td>
<td></td>
</tr>
<tr class="odd">
<td>175</td>
<td colspan="2"><blockquote>
<p>FBEDIF</p>
</blockquote></td>
<td>“Y” or “ “</td>
<td></td>
<td colspan="3">EDI CLAIM IDENTIFIER</td>
<td></td>
</tr>
<tr class="even">
<td>176 - 195</td>
<td colspan="2"><blockquote>
<p>FBCNTRN</p>
</blockquote></td>
<td>60</td>
<td>162.5</td>
<td colspan="3">CONTRACT NUMBER</td>
<td></td>
</tr>
<tr class="odd">
<td>196 – 205</td>
<td colspan="2"><blockquote>
<p>FBIA</p>
</blockquote></td>
<td>87</td>
<td>162.5</td>
<td colspan="3">IPAC VENDOR AGREEMENT</td>
<td></td>
</tr>
<tr class="even">
<td>206 - 227</td>
<td colspan="2"><blockquote>
<p>FBDODINV</p>
</blockquote></td>
<td>86</td>
<td>162.5</td>
<td colspan="3">DoD INVOICE NUMBER</td>
<td></td>
</tr>
<tr class="odd">
<td>228</td>
<td colspan="2"><blockquote>
<p>“~”</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="3">BLOCK DELIMITER</td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 1%" />
<col style="width: 26%" />
<col style="width: 0%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 23%" />
<col style="width: 11%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="8"><h2 id="a-12-b9-inpatient-batch-line-3">A-12 B9 Inpatient Batch (Line 3)</h2></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><strong>POSITION</strong></th>
<th><strong>VARIABLE NAME</strong></th>
<th colspan="2"><strong>FIELD #</strong></th>
<th><strong>FILE #</strong></th>
<th colspan="3"><strong>FIELD NAME</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 - 7</td>
<td colspan="3"><blockquote>
<p>FBICD(6)</p>
</blockquote></td>
<td>35</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">ICD CODE 6</td>
</tr>
<tr class="even">
<td>8</td>
<td colspan="3"><blockquote>
<p>FBPOA6</p>
</blockquote></td>
<td>35.02</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PRESENT ON ADMISSION 6</td>
</tr>
<tr class="odd">
<td>9 - 15</td>
<td colspan="3"><blockquote>
<p>FBICD(7)</p>
</blockquote></td>
<td>35.1</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">ICD COE 7</td>
</tr>
<tr class="even">
<td>16</td>
<td colspan="3"><blockquote>
<p>FBPOA7</p>
</blockquote></td>
<td>36.12</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PRESENT ON ADMISSION 7</td>
</tr>
<tr class="odd">
<td>17 - 23</td>
<td colspan="3"><blockquote>
<p>FBICD(8)</p>
</blockquote></td>
<td>35.2</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">ICD CODE 8</td>
</tr>
<tr class="even">
<td>24</td>
<td colspan="3"><blockquote>
<p>FBPOA8</p>
</blockquote></td>
<td>35.22</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PRESENT ON ADMISSION 8</td>
</tr>
<tr class="odd">
<td>25 - 31</td>
<td colspan="3"><blockquote>
<p>FBICD(9)</p>
</blockquote></td>
<td>35.3</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">ICD CODE 9</td>
</tr>
<tr class="even">
<td>32</td>
<td colspan="3"><blockquote>
<p>FBPOA9</p>
</blockquote></td>
<td>35.32</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PRESENT ON ADMISSION 9</td>
</tr>
<tr class="odd">
<td>33 - 39</td>
<td colspan="3"><blockquote>
<p>FBICD(10)</p>
</blockquote></td>
<td>35.4</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">ICD COE 10</td>
</tr>
<tr class="even">
<td>40</td>
<td colspan="3"><blockquote>
<p>FBPOA10</p>
</blockquote></td>
<td>35.42</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PRESENT ON ADMISSION 10</td>
</tr>
<tr class="odd">
<td>41 - 47</td>
<td colspan="3"><blockquote>
<p>FBPROC(6)</p>
</blockquote></td>
<td>44.06</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PROCEDURE 6</td>
</tr>
<tr class="even">
<td>48 - 54</td>
<td colspan="3"><blockquote>
<p>FBPROC(7)</p>
</blockquote></td>
<td>44.07</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PROCEDURE 7</td>
</tr>
<tr class="odd">
<td>55 - 61</td>
<td colspan="3"><blockquote>
<p>FBPROC(8)</p>
</blockquote></td>
<td>44.08</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PROCEDURE 8</td>
</tr>
<tr class="even">
<td>62 – 68</td>
<td colspan="3"><blockquote>
<p>FBPROC(9)</p>
</blockquote></td>
<td>44.09</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PROCEDURE 9</td>
</tr>
<tr class="odd">
<td>69 – 75</td>
<td colspan="3"><blockquote>
<p>FBPROC(10)</p>
</blockquote></td>
<td>44.1</td>
<td colspan="2"><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3">PROCEDURE 10</td>
</tr>
<tr class="even">
<td>76</td>
<td colspan="3"><blockquote>
<p>“~”</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td colspan="3">BLOCK DELIMITER</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 0%" />
<col style="width: 23%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><h2 id="a-13-b9-inpatient-batch-line-4">A-13 B9 Inpatient Batch (Line 4)</h2></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>POSITION</strong></th>
<th><blockquote>
<p><strong>VARIABLE NAME</strong></p>
</blockquote></th>
<th><strong>FIELD #</strong></th>
<th colspan="2"><strong>FILE #</strong></th>
<th colspan="2"><strong>FIELD NAME</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 – 7</td>
<td><blockquote>
<p>FBICD(11)</p>
</blockquote></td>
<td>35.5</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 11</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>FBPOA(11)</p>
</blockquote></td>
<td>35.52</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 11</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9 – 15</td>
<td><blockquote>
<p>FBICD(12)</p>
</blockquote></td>
<td>35.6</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 12</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td><blockquote>
<p>FBPOA(12)</p>
</blockquote></td>
<td>35.62</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 12</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17 – 23</td>
<td><blockquote>
<p>FBICD(13)</p>
</blockquote></td>
<td>35.7</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 13</p>
</blockquote></td>
</tr>
<tr class="even">
<td>24</td>
<td><blockquote>
<p>FBPOA(13)</p>
</blockquote></td>
<td>35.72</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 13</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>25 – 31</td>
<td><blockquote>
<p>FBICD(14)</p>
</blockquote></td>
<td>35.8</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 14</p>
</blockquote></td>
</tr>
<tr class="even">
<td>32</td>
<td><blockquote>
<p>FBPOA(14)</p>
</blockquote></td>
<td>35.82</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 14</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>33 – 39</td>
<td><blockquote>
<p>FBICD(15)</p>
</blockquote></td>
<td>35.9</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 15</p>
</blockquote></td>
</tr>
<tr class="even">
<td>40</td>
<td><blockquote>
<p>FBPOA(15)</p>
</blockquote></td>
<td>35.92</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>41 – 47</td>
<td><blockquote>
<p>FBICD(16)</p>
</blockquote></td>
<td>36</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 16</p>
</blockquote></td>
</tr>
<tr class="even">
<td>48</td>
<td><blockquote>
<p>FBPOA(16)</p>
</blockquote></td>
<td>36.02</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>49 – 55</td>
<td><blockquote>
<p>FBICD(17)</p>
</blockquote></td>
<td>36.1</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 17</p>
</blockquote></td>
</tr>
<tr class="even">
<td>56</td>
<td><blockquote>
<p>FBPOA(17)</p>
</blockquote></td>
<td>36.12</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 17</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>57 – 63</td>
<td><blockquote>
<p>FBICD(18)</p>
</blockquote></td>
<td>36.2</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 18</p>
</blockquote></td>
</tr>
<tr class="even">
<td>64</td>
<td><blockquote>
<p>FBPOA(18)</p>
</blockquote></td>
<td>36.22</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 18</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>65 – 71</td>
<td><blockquote>
<p>FBICD(19)</p>
</blockquote></td>
<td>36.3</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 19</p>
</blockquote></td>
</tr>
<tr class="even">
<td>72</td>
<td><blockquote>
<p>FBPOA(19)</p>
</blockquote></td>
<td>36.32</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>73 – 79</td>
<td><blockquote>
<p>FBICD(20)</p>
</blockquote></td>
<td>36.4</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 20</p>
</blockquote></td>
</tr>
<tr class="even">
<td>80</td>
<td><blockquote>
<p>FBPOA(20)</p>
</blockquote></td>
<td>36.42</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 20</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>81 – 87</td>
<td><blockquote>
<p>FBICD(21)</p>
</blockquote></td>
<td>36.5</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 21</p>
</blockquote></td>
</tr>
<tr class="even">
<td>88</td>
<td><blockquote>
<p>FBPOA(21)</p>
</blockquote></td>
<td>36.52</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 21</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>89 – 95</td>
<td><blockquote>
<p>FBICD(22)</p>
</blockquote></td>
<td>36.6</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 22</p>
</blockquote></td>
</tr>
<tr class="even">
<td>96</td>
<td><blockquote>
<p>FBPOA(22)</p>
</blockquote></td>
<td>36.62</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 22</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>97 – 103</td>
<td><blockquote>
<p>FBICD(23)</p>
</blockquote></td>
<td>36.7</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 23</p>
</blockquote></td>
</tr>
<tr class="even">
<td>104</td>
<td><blockquote>
<p>FBPOA(23)</p>
</blockquote></td>
<td>36.72</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 23</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>105 – 111</td>
<td><blockquote>
<p>FBICD(24)</p>
</blockquote></td>
<td>36.8</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 24</p>
</blockquote></td>
</tr>
<tr class="even">
<td>112</td>
<td><blockquote>
<p>FBPOA(24)</p>
</blockquote></td>
<td>36.82</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 24</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>113 – 119</td>
<td><blockquote>
<p>FBICD(25)</p>
</blockquote></td>
<td>36.9</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ICD CODE 25</p>
</blockquote></td>
</tr>
<tr class="even">
<td>120</td>
<td><blockquote>
<p>FBPOA(25)</p>
</blockquote></td>
<td>36.92</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PRESENT ON ADMISSION 25</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>121 – 127</td>
<td><blockquote>
<p>FBPROC(11)</p>
</blockquote></td>
<td>44.11</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 11</p>
</blockquote></td>
</tr>
<tr class="even">
<td>128 – 134</td>
<td><blockquote>
<p>FBPROC(12)</p>
</blockquote></td>
<td>44.12</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 12</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>135 – 141</td>
<td><blockquote>
<p>FBPROC(13)</p>
</blockquote></td>
<td>44.13</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 13</p>
</blockquote></td>
</tr>
<tr class="even">
<td>142 – 148</td>
<td><blockquote>
<p>FBPROC(14)</p>
</blockquote></td>
<td>44.14</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 14</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>149 – 155</td>
<td><blockquote>
<p>FBPROC(15)</p>
</blockquote></td>
<td>44.15</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 15</p>
</blockquote></td>
</tr>
<tr class="even">
<td>156 – 162</td>
<td><blockquote>
<p>FBPROC(16)</p>
</blockquote></td>
<td>44.16</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>163 – 169</td>
<td><blockquote>
<p>FBPROC(17)</p>
</blockquote></td>
<td>44.17</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 17</p>
</blockquote></td>
</tr>
<tr class="even">
<td>170 – 176</td>
<td><blockquote>
<p>FBPROC(18)</p>
</blockquote></td>
<td>44.18</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 18</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>177 – 183</td>
<td><blockquote>
<p>FBPROC(19)</p>
</blockquote></td>
<td>44.19</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 19</p>
</blockquote></td>
</tr>
<tr class="even">
<td>184 – 190</td>
<td><blockquote>
<p>FBPROC(20)</p>
</blockquote></td>
<td>44.2</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 20</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>191 – 197</td>
<td><blockquote>
<p>FBPROC(21)</p>
</blockquote></td>
<td>44.21</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 21</p>
</blockquote></td>
</tr>
<tr class="even">
<td>198 – 204</td>
<td><blockquote>
<p>FBPROC(22)</p>
</blockquote></td>
<td>44.22</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 22</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>205 – 211</td>
<td><blockquote>
<p>FBPROC(23)</p>
</blockquote></td>
<td>44.23</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 23</p>
</blockquote></td>
</tr>
<tr class="even">
<td>212 – 218</td>
<td><blockquote>
<p>FBPROC(24)</p>
</blockquote></td>
<td>44.24</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 24</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>219 – 225</td>
<td><blockquote>
<p>FBPROC(25)</p>
</blockquote></td>
<td>44.25</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PROCEDURE 25</p>
</blockquote></td>
</tr>
<tr class="even">
<td>226</td>
<td><blockquote>
<p>“~”</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>BLOCK DELIMITER</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 0%" />
<col style="width: 23%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><h2 id="a-14-b9-inpatient-batch-line-5">A-14 B9 Inpatient Batch (Line 5)</h2></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>POSITION</strong></th>
<th><blockquote>
<p><strong>VARIABLE NAME</strong></p>
</blockquote></th>
<th><strong>FIELD #</strong></th>
<th colspan="2"><strong>FILE #</strong></th>
<th colspan="2"><strong>FIELD NAME</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 – 12</td>
<td><blockquote>
<p>FBFPPSID</p>
</blockquote></td>
<td>56</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>FPPS CLAIM ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>13 – 41</td>
<td><blockquote>
<p>FBAUTHNUM</p>
</blockquote></td>
<td>88</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>AUTHORIZATION NUMBER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>42 – 50</td>
<td><blockquote>
<p>Claim Level Allowed Amount unavailable</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td>51 – 52</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>58;1</td>
<td><blockquote>
<p>161.92</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>53 – 58</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>59 – 64</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>65 - 66</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>58;1</td>
<td><blockquote>
<p>161.92</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>67 – 71</td>
<td><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td>58;.01</td>
<td><blockquote>
<p>161.91</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>72 – 77</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>78 – 83</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>84 – 93</td>
<td><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td>58;2</td>
<td><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>94 – 95</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>58;1</td>
<td><blockquote>
<p>161.92</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>96 – 100</td>
<td><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td>58;.01</td>
<td><blockquote>
<p>161.91</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>101 – 106</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>107 – 112</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>113 - 122</td>
<td><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td>58;2</td>
<td><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>123 – 124</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>58;1</td>
<td><blockquote>
<p>161.92</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>125 – 129</td>
<td><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td>58;.01</td>
<td><blockquote>
<p>161.91</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>130 – 135</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>136 – 141</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>142 - 151</td>
<td><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td>58;2</td>
<td><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>152 – 153</td>
<td><blockquote>
<p>FBADJG</p>
</blockquote></td>
<td>58;1</td>
<td><blockquote>
<p>161.92</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT GROUP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>154 – 158</td>
<td><blockquote>
<p>FBADJR</p>
</blockquote></td>
<td>58;.01</td>
<td><blockquote>
<p>161.91</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT REASON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>159 – 164</td>
<td><blockquote>
<p>FBRRC1</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>165 – 170</td>
<td><blockquote>
<p>FBRRC2</p>
</blockquote></td>
<td>59;.01</td>
<td><blockquote>
<p>161.93</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REMITTANCE REMARK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>171 - 180</td>
<td><blockquote>
<p>FBADJA</p>
</blockquote></td>
<td>58;2</td>
<td><blockquote>
<p>161.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADJUSTMENT AMOUNT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>181 – 188</td>
<td><blockquote>
<p>FBDRGWT</p>
</blockquote></td>
<td>24.5</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DRG WEIGHT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>189 – 198</td>
<td><blockquote>
<p>FBBILAMT</p>
</blockquote></td>
<td>6.6</td>
<td><blockquote>
<p>162.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>BILLED CHARGES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>199</td>
<td><blockquote>
<p>FBPAYMETH</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td>200</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>Y or ‘’</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADDITIONAL PAYMENT INDICATOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>201</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>‘A’ for Appeal or ‘U’ for Underpayment</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADDITIONAL PAYMENT TYPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>202 – 231</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PARENT INTERNAL CONTROL NUMBER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>232 - 233</td>
<td><blockquote>
<p>“~$</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>BLOCK/RECORD DELIMITERS</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Appendix B – Transmission Mappings from Central Fee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition of the interface between Central Fee and VistA Fee Basis. Central Fee sends a nightly Payment Confirmation file to VistA Fee Basis using MailMan. The following table defines the field/element Description in the fixed length message. Note: Fields from the mail message are filed to three different Fee Basis files in VistA depending on the Fee Program (FEE-PGM) fields in the message.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 19%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Central Fee Desc.</strong></th>
<th><strong>VistA FB File,Field</strong></th>
<th><strong>Col.</strong></th>
<th><strong>Length</strong></th>
<th><strong>Data Type</strong></th>
<th><strong>Example Data</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FEE-STATION</td>
<td>n/a</td>
<td>1</td>
<td>6</td>
<td>AlphaNum</td>
<td>402</td>
</tr>
<tr class="even">
<td>FEE-PGM</td>
<td>n/a</td>
<td>7</td>
<td>1</td>
<td>AlphaNum</td>
<td><p>3=Outpt file 162</p>
<p>5=Invoice file 162.5</p>
<p>9=Rx file file 162.1</p>
<p>T=Travel file 162</p></td>
</tr>
<tr class="odd">
<td>FEE-ACTY-CODE</td>
<td>n/a</td>
<td>8</td>
<td>1</td>
<td>AlphaNum</td>
<td><p>B=backout</p>
<p>C=confirmed</p>
<p>X=cancelled</p></td>
</tr>
<tr class="even">
<td>FEE-INTNL-CTL-NUM-30</td>
<td>n/a</td>
<td>9</td>
<td>n/a</td>
<td>Group</td>
<td>Represents the record to edit in the appropriate FB file</td>
</tr>
<tr class="odd">
<td>FEE-INTNL-CTL-1-7</td>
<td>Various fields representing the record to edit</td>
<td>9</td>
<td>7</td>
<td>AlphaNum</td>
<td>0000000</td>
</tr>
<tr class="even">
<td>FEE-INTNL-CTL-NUM-23</td>
<td>Various fields representing the record to edit</td>
<td>16</td>
<td>23</td>
<td>AlphaNum</td>
<td>0000000000015609¬51¬2¬1</td>
</tr>
<tr class="odd">
<td>FEE-CHK-NUM</td>
<td><p>Check Number</p>
<p>162,35</p>
<p>162.5,48</p>
<p>162.1, 30</p>
<p>162,9</p></td>
<td>39</td>
<td>8</td>
<td>AlphaNum</td>
<td>17041297</td>
</tr>
<tr class="even">
<td>FEE-CHK-DATE</td>
<td><p>Date Paid</p>
<p>162,12</p>
<p>162.5, 45</p>
<p>162.1,28</p>
<p>162,8</p></td>
<td>47</td>
<td>8</td>
<td>AlphaNum</td>
<td>20110314</td>
</tr>
<tr class="odd">
<td>FEE-INT-AMT</td>
<td><p>Interest Amount</p>
<p>162,41</p>
<p>162.5,53</p>
<p>162.1,35</p>
<p>162,14</p></td>
<td>55</td>
<td>8</td>
<td>Numeric<sup>1</sup></td>
<td>00000000</td>
</tr>
<tr class="even">
<td>FEE-CNC-DTE</td>
<td><p>Cancellation Date</p>
<p>162,36</p>
<p>162.5,49</p>
<p>162.1,31</p>
<p>162,10</p></td>
<td>63</td>
<td>8</td>
<td>AlphaNum</td>
<td>20110311 (if cancelled)</td>
</tr>
<tr class="odd">
<td>FEE-RSN-CODE</td>
<td><p>Reason Code</p>
<p>162,37</p>
<p>162.5,50</p>
<p>162.1,32</p>
<p>162,11</p></td>
<td>71</td>
<td>1</td>
<td>AlphaNum</td>
<td>U (if cancelled)</td>
</tr>
<tr class="even">
<td>FEE-CNC-CODE</td>
<td><p>Cancellation Activity</p>
<p>162,38</p>
<p>162.5,51</p>
<p>162.1,33</p>
<p>162,12</p></td>
<td>72</td>
<td>1</td>
<td>AlphaNum</td>
<td>X (if cancelled)</td>
</tr>
<tr class="odd">
<td>FEE-DBRS-AMT</td>
<td><p>Dispersed Amount</p>
<p>162,40</p>
<p>162.5,52</p>
<p>162.1,34</p>
<p>162,13</p></td>
<td>73</td>
<td>9</td>
<td>Numeric<sup>1</sup></td>
<td>000027741</td>
</tr>
<tr class="even">
<td>FEE-RTG-NUM<sup>2</sup></td>
<td><p>Routing Number</p>
<p>162,54</p>
<p>162.5,60</p></td>
<td>82</td>
<td>9</td>
<td>AlphaNum</td>
<td>256012974</td>
</tr>
<tr class="odd">
<td>FEE-ACCT-NUM<sup>2</sup></td>
<td><p>Account Number</p>
<p>162,55</p>
<p>162.5,61</p></td>
<td>91</td>
<td>17</td>
<td>AlphaNum</td>
<td>12345678911111</td>
</tr>
<tr class="even">
<td>FEE-BANK<sup>2</sup></td>
<td><p>Financial Institution</p>
<p>162,56</p>
<p>162.5,62</p></td>
<td>108</td>
<td>30</td>
<td>AlphaNum</td>
<td>WELLS FARGO</td>
</tr>
<tr class="odd">
<td>FEE-REC-END-IND</td>
<td>n/a</td>
<td>138</td>
<td>1</td>
<td>AlphaNum</td>
<td>$</td>
</tr>
</tbody>
</table>

1.  Numeric fields contain an implied two digit decimal, so 12345678 = \$123456.78
2.  New fields processed by FB\*3.5\*121.

# Appendix C – CARC/RARC Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FB\*3.5\*158 introduced CARC/RARC relationships. CARCs are stored in the ADJUSTMENT REASON file (#161.91) and RARCs are stored in the REMITTANCE REMARK file (#161.93). Patch 158 allows RARCs to be associated with specific CARCs so that, if a VistA Fee user selects a CARC and needs to enter RARCs, only associated RARCs can be selected, and all unrelated RARCs would be filtered out of lookup lists. If a CARC has no RARC relationships established, no RARCs are filtered and all RARCS are selectable.

The ADJUSTMENT REASON file (#161.91) contains a new multiple, REMITTANCE REMARK defined as follows:

161.915,.01 REMITTANCE REMARK 0;1 POINTER TO REMITTANCE REMARK FILE (#

161.93) (Multiply asked)

LAST EDITED: MAR 06, 2015

HELP-PROMPT: Enter an existing Remittance Remark Code

CROSS-REFERENCE: 161.915^B

1)= S ^FB(161.91,DA(1),"RARC","B",\$E(X,1,30),DA )=""

2)= K ^FB(161.91,DA(1),"RARC","B",\$E(X,1,30),DA)

To establish relationships between CARCs and RARCs, add RARCs to this multiple for each related CARC.

[^1]: Note: This specification was provided by Reddy Madipadga to Proxicom in 2006.