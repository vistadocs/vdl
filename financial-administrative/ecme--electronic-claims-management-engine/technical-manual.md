---
title: ECME Technical Manual/Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: ECME /Security Guide
app_code: ECME
app_name: Electronic Claims Management Engine
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 30
description: 
audience: 
keywords: 
  - class
  - ecme
  - table
  - pharmacy
  - blockquote
  - contents
  - claims
  - even
  - ncpdp
  - claim
page_count: 0
word_count: 15961
section_count: 26
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=141"
---

# Electronic Claims Management Engine (ECME)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Electronic Claims Management Engine (ECME)](#electronic-claims-management-engine-ecme)
- [Technical Manual / Security Guide](#technical-manual-security-guide)
  - [Introduction](#introduction)
    - [Description of ECME Technical Manual](#description-of-ecme-technical-manual)
    - [Orientation](#orientation)
    - [List of Related Documentation](#list-of-related-documentation)
  - [ECME V. 1.0 Menus](#ecme-v-10-menus)
  - [Implementation and Maintenance](#implementation-and-maintenance)
    - [Site Parameters](#site-parameters)
    - [Editing the Basic Pharmacy ECME Parameters](#editing-the-basic-pharmacy-ecme-parameters)
    - [System Requirements](#system-requirements)
  - [Files](#files)
  - [Routines](#routines)
    - [Descriptions](#descriptions)
    - [### Callable Routines](#callable-routines)
  - [Templates](#templates)
    - [Print Templates](#print-templates)
    - [Input Templates](#input-templates)
    - [Sort Templates](#sort-templates)
    - [List Templates](#list-templates)
  - [Exported Options](#exported-options)
    - [Stand-alone Options](#stand-alone-options)
    - [Top-level Menus](#top-level-menus)
  - [Archiving and Purging](#archiving-and-purging)
    - [Archiving](#archiving)
    - [Purging](#purging)
  - [Callable Routines / Entry Points / Application Programmer Interfaces (APIs)](#callable-routines-entry-points-application-programmer-interfaces-apis)
    - [Callable Routines](#callable-routines-1)
    - [Application Programmer Interfaces (APIs)](#application-programmer-interfaces-apis)
    - [Entry Points](#entry-points)
  - [Protocols](#protocols)
  - [External Relations](#external-relations)
    - [Software Requirements](#software-requirements)
    - [Integration Agreements (INTEGRATION CONTROL REGISTRATIONS)](#integration-agreements-integration-control-registrations)
  - [Internal Relations](#internal-relations)
  - [Package-Wide Variables](#package-wide-variables)
    - [SACC Exemptions](#sacc-exemptions)
    - [Variables](#variables)
  - [Security Management](#security-management)
  - [Mail Groups and Mail Messages (Bulletins)](#mail-groups-and-mail-messages-bulletins)
  - [Remote Systems](#remote-systems)
  - [Archiving and Purging](#archiving-and-purging-1)
    - [Archiving](#archiving-1)
    - [Purging](#purging-1)
  - [Contingency Planning](#contingency-planning)
  - [Interfacing](#interfacing)
  - [Electronic Signatures](#electronic-signatures)
  - [Menus](#menus)
    - [Security Keys](#security-keys)
  - [File Security](#file-security)
  - [References](#references)
  - [Official Policies](#official-policies)
  - [Acronyms and Abbreviations](#acronyms-and-abbreviations)

# Technical Manual / Security Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ecme-technical-manual-security-guide/001.png)

August 2025

Office of Information and Technology (OIT)

Revision History

| Date    | Changed Pages                                                                                                                                                                                     | Description (Patch \# if applicable)                                                               | Author                                     |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------|
| 08/2025 | 11, 12, 15                                                                                                                                                                                        | Update for patch BPS\*1\*40                                                                        | VHA HF DSO MCCF ePharmacy Development Team |
| 05/2025 | 4, 7, 12, 15, 18, 20, 33-35                                                                                                                                                                       | Update for patch BPS\*1\*39                                                                        | REDACTED                                   |
| 05/2024 | 4, 12, 16, 19, 20, 22, 39, 41                                                                                                                                                                     | Update for patch BPS\*1\*36                                                                        | REDACTED                                   |
| 12/2022 | 5, 6                                                                                                                                                                                              | Update for patch BPS\*1\*33                                                                        | REDACTED                                   |
| 05/2021 | 10, 13, 17, 19, 21, 40, 42                                                                                                                                                                        | Update for patch BPS\*1\*28.                                                                       | REDACTED                                   |
| 01/2019 | 16, 20, 21                                                                                                                                                                                        | Update for patch BPS\*1\*24.                                                                       | REDACTED                                   |
| 07/2018 | 19, 20, 50                                                                                                                                                                                        | Update for patch BPS\*1\*23                                                                        | REDACTED                                   |
| 11/2017 | 10, 19, 48                                                                                                                                                                                        | Update for patch BPS\*1\*22.                                                                       | REDACTED                                   |
| 03/2017 | 19                                                                                                                                                                                                | Update for patch BPS\*1\*21.                                                                       | REDACTED                                   |
| 06/2016 | 7, 19, 21, 24, 25, 27, 28, 29, 34, 47, 48, 61, 71, 72, 76, 93                                                                                                                                     | Update for patch BPS\*1\*20.                                                                       | REDACTED                                   |
| 06/2015 | 7, 14, 18, 24, 26, 29, 72, 75, 76                                                                                                                                                                 | Update for patch BPS\*1\*19.                                                                       | REDACTED                                   |
| 02/2015 | 19,43, reformatted footers                                                                                                                                                                        | Update for patch BPS\*1.0\*17.                                                                     | LongView                                   |
| 11/2013 | i, ii, iii, iv, v, 19, 39, 40                                                                                                                                                                     | Update for patch BPS\*1.0\*15.                                                                     | REDACTED                                   |
| 02/2012 | 1, 7, 13, 15, 16, 17, 20, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 65, 66, 67, 68, 69, 71, 80, 81, 88, 103 | Update for patch BPS\*1.0\*11.                                                                     | REDACTED                                   |
| 10/2011 | 1, 2, 7, 10, 11, 13-17, 19, 21-29, 31, 33-43, 45, 46, 51, 57, 59, 61, 63, 67-68, 71, 73-75, 77, 79, 85, 88, 90, 93, 95                                                                            | Updates for Build BPS\*1.0\*10, v D.0.                                                             | REDACTED                                   |
| 11/2010 |                                                                                                                                                                                                   | Updates for patch BPS\*1\*9 (TRICARE Active release).                                              | REDACTED                                   |
| 08/2010 |                                                                                                                                                                                                   | Updates for BPS\*1\*8 (Coordination of Benefits release).                                          | REDACTED                                   |
| 07/2009 |                                                                                                                                                                                                   | ePHARMACY ENHANCEMENTS patch BPS\*1.0\*7                                                           | REDACTED                                   |
|         |                                                                                                                                                                                                   | ePHARMACY TRICARE SUPPORT FRAMEWORK patch BPS\*1\*6.                                               | REDACTED                                   |
| 10/2007 |                                                                                                                                                                                                   | ePHARMACY/ECME ENHANCEMENTS patch BPS\*1\*5.                                                       | REDACTED                                   |
| 12/2006 |                                                                                                                                                                                                   | RX NOT PROCESSED FOR SITE MESSAGE patch BPS\*1.0\*4.                                               | REDACTED                                   |
| 02/2007 |                                                                                                                                                                                                   | Updated for NPI patch BPS\*1\*2.                                                                   | REDACTED                                   |
| 08/2006 |                                                                                                                                                                                                   | Updated for interim patch BPS\*1\*3.                                                               | REDACTED                                   |
| 04/2006 |                                                                                                                                                                                                   | Initial release of the Electronic Claims Management Engine (ECME) Technical Manual/Security Guide. | REDACTED                                   |

<span id="_Toc192072569" class="anchor"></span>Table 1: Files

Table of Contents

List of Tables

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Description of ECME Technical Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Electronic Claims Management Engine (ECME) Technical Manual describes the technical and security aspects of the ECME V. 1.0 application. Its intended audience includes Health Systems Design & Development (HSD&D) developers, members of the Pharmacy Automated Data Processing Application Coordinator (ADPAC), and Information Resources Management Service (IRMS) staff. Users can find ECME V. 1.0 documentation, including any subsequent change pages affecting this guide, on the Veterans Health Information Systems and Technology Architecture (VistA) Documentation Library (VDL).

The ECME V. 1.0 application generates electronic claims in National Council for Prescription Drug Programs (NCPDP) in version D.0 format based on the Outpatient Pharmacy V. 7.0 workflow. Claims will also be processed in version D.0. format until all payers switch to NCPDP version D.0.–D.9.

ECME V. 1.0 performs the following tasks:

- Allows pharmacy users to submit, resubmit, and reverse electronic claims
- Provides reports for end users and management on claims status, transaction history, and system configuration standings
- Allows Pharmacy ADPACs and IRMs to configure ECME to pharmacy site specifications
- Allows users to submit eligibility verification transmissions for pharmacy insurance

The ECME package was originally released in two phases, a dormant phase (released on 10/20/2004), and an active phase. The BPS 1.0 Master Build was the dormant phase, releasing the ECME V. 1.0 package (which occupies the BPS namespace) in a dormant state and enhancing Integrated Billing (IB) V. 2, so that the user can link pharmacy groups with insurance group plans. In addition, during the dormant phase, each site should have already registered the pharmacy with the Financial Services Center (FSC).

The active phase allowed the ECME V. 1.0 package to produce electronic claims. These changes allowed the VistA software applications to transmit outpatient pharmacy prescription claims to payers electronically and to receive claim responses (which include Drug Utilization Responses (DURs) and warnings) on a real-time basis and in accordance with Healthcare Insurance Portability and Accountability Act (HIPAA) Electronic Data Interchange (EDI) transactions and NCPDP mandated format standards, specifically NCPDP Telecommunication Standard V. 5.1. A later release added the capability of sending claims in the NCPDP Telecommunication Standard V. D.0.

ECME V. 1.0 claims processing begins when events within Outpatient Pharmacy V. 7.0 meet specific criteria that indicate the system should generate an electronic claim.

To build a claim through ECME V. 1.0, the following must occur:

1.  The patient must be registered.
2.  The patient must have pharmacy insurance coverage.
3.  The patient must have a prescription for a non-service-connected condition and with a billable drug.

Logic embedded within ECME V. 1.0 manages the creation of the electronic claim, which requires integration with Integrated Billing (IB) V. 2.0, Pharmacy Data Management (PDM) V. 1.0, and the National Drug File (NDF) V. 4.0. ECME V. 1.0 also generates claims during Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0 processing for prescriptions that meet billing requirements; the prescriptions are suspended for CMOP fills.

The Veterans Health Administration (VHA) developed the ECME V. 1.0 software in order to comply with the Health Insurance Portability and Accountability Act of 1996, which requires health care providers to transmit outpatient pharmacy prescription claims to payers electronically in the NCPDP format, and to receive responses on a real-time basis. ECME V. 1.0 was derived from the Pharmacy Point of Sale V. 1.0 (POS) application developed by the Indian Health Service (IHS).

### Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide consistently uses the following notation to enhance readability.

- Screen prompts are denoted with quotation marks around them.  
  Example: the “Press ENTER to continue” prompt will display next.
- Menu options are italicized. Example: The Payable Claims Report option lists payable electronic claims in billed and paid amounts.
- Responses in bold face denote user input. Example: Select ECME Option: RPT.
- \<Enter\> indicates the user must press the Enter key (or Return key on some keyboards). Example: Type Y for Yes or N for No, and press \<Enter\>
- \<Tab\> indicates the user must press the Tab key. Example: Press \<Tab\> to move the cursor to the next field.
- Note indicates important or helpful information. Example:
1.  Important or helpful information.
- Key options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option. Example:

  Key The user cannot access the Pharmacy ECME Manager Menu options without the BPS MANAGER key.
- The user can enter one, two, or three question marks at any prompt to get online help.
- One question mark briefly states what information is appropriate for the prompt.
- Two question marks provide more detailed help, plus hidden actions.
- Three question marks give the most detailed help, including a list of possible answers, if appropriate.

Users can obtain online help in the following ways.

- Enter a question mark (?) for assistance in choosing actions at a prompt.
- Use the kernel routine, XINDEX, to produce detailed listings of the routines.
- Use VA FileMan to generate listings of data dictionaries for the files.

### List of Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Electronic Claims Management Engine V. 1.0 User ManualOutpatient Pharmacy V. 7.0 Technical Manual / Security Guide Change PagesOutpatient Pharmacy V. 7.0 User Manual Change PagesHIPAA NCPDP Connection for EDI Pharmacy (Active Release) Installation GuideHIPAA NCPDP Connection for EDI Pharmacy (Active Release) Release NotesHIPAA NCPDP IB/AR Release NotesPDM Technical Manual / Security Guide Change PagesPDM User's Manual Change PagesCMOP Technical Manual Change PagesCMOP User's Manual Change Pages*

## ECME V. 1.0 Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The complete list of ECME V. 1.0 menu options is shown below. The Claims Coordinator needs to access all ECME V. 1.0 options.

Key To view the complete ECME V. 1.0 menu structure, the user must hold the BPSMENU, BPS USER, BPS MANAGER, BPS MASTER, BPS REPORTS, and BPS SUPERVISOR keys.

U Claims Data Entry ScreenCOB ECME Pharmacy COB…

> SEC Potential Secondary Rx Claims Report

> TRI Potential Claims Report for Dual Eligible

> PRO Process Secondary / TRICARE Rx to ECME

MGR Pharmacy ECME Manager Menu…

> MNT ECME transaction maintenance options…

> UNS View / Unstrand Submissions Not Completed

> ROC Re-Open CLOSED Claim

> SET Pharmacy ECME Setup Menu…

> BAS Edit Basic ECME Parameters

> PHAR Edit ECME Pharmacy Data

> REG Register Pharmacy with Austin Automation Center

> STAT Statistics Screen

> CP ePharmacy Claim ParametersRPT Pharmacy Electronic Claims Reports…

> CLA Claim Results and Status…

> PAY Payable Claims Report

> REJ Rejected Claims Report

> ECMP COMP / ECME Activity Report

> REV Reversal Claims Report

> NYR Claims Submitted, Not Yet Released

> REC Recent Transactions

> DAY Totals by Date

> CLO Closed Claims Report

> NBS Non-Billable Status Report

> SPA Spending Account Report

> DUP Duplicate Claims Report

> ERR ePharmacy Bills Created with Errors

> OTH Other Reports…

> CRI ECME Claims-Response Inquiry

> PAY Payer Sheet Detail Report

> PHAR ECME Setup – Pharmacies Report

> TAT Turn-around time statistics

> VER View ePharmacy Rx

> OPR OPECC Productivity Report

## Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The site parameters consist of the editing of the basic pharmacy ECME parameters and the association of the outpatient sites with the ECME pharmacy.

### Editing the Basic Pharmacy ECME Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Edit Basic Pharmacy ECME Parameters* option allows the user to determine how long progress messages will display on the screen when claims are being processed in the foreground.

To edit this parameter, use the following menu path:

*ECME Main Menu* \[BPSMENU\] (Locked: BPSMENU)

*Pharmacy ECME Manager Menu* \[BPS MANAGER MENU\] (Locked: BPS MANAGER)

> *Pharmacy ECME Setup Menu* \[BPS SETUP MENU\]

> *Edit Basic Pharmacy ECME Parameters* \[BPS SETUP PART 1\] (Locked: BPS MASTER)

Example of Screen Print:

Edit Pharmacy ECME configuration

ECME timeout? (0 to 30 seconds) : 30//

Insurer Asleep Interval (0 to 29 minutes): 10//

Insurer Asleep Retries (0 to 99): 10//

Default Eligibility Pharmacy:

#### Associating the Outpatient Sites with an ECME Pharmacy

This option enables the pharmacy users to submit third party claims.

To edit this parameter, use the following menu path:

*ECME Main Menu \[BPSMENU\] (Locked: BPSMENU)Pharmacy ECME Manager Menu \[BPS MANAGER MENU\] (Locked: BPS MANAGER)*

> *Pharmacy ECME Setup Menu \[BPS SETUP MENU\] (Locked: BPS MASTER)*

> *Edit ECME Pharmacy Data \[BPS SETUP PHARMACY\] (Locked: BPS MASTER)*

The following is a list of prompts related to the Associating of Outpatient Sites with an ECME Pharmacy option:

- Select BPS PHARMACIES NAME: Enter a BPS PHARMACIES NAME, OR OUTPATIENT SITE. By entering a question mark (?), the system will return the available BPS Pharmacies. A new BPS Pharmacy can be entered, and the name must be 3 – 30 alphabetical characters (not numeric and cannot start with punctuation character).
- STATUS: Displays the current status (Active / Inactive). This is entered in the Register Pharmacy with Austin Automation Center option \[BPS SETUP REGISTER PHARMACY\] and is a read-only field on this screen.
- NCPDP \#: Displays the Pharmacy NCPDP \#. This is a number assigned to the pharmacy by the NCPDP and was formerly called NABP \# (National Association of Boards of Pharmacy number). This is entered in the Register Pharmacy with Austin Automation Center option \[BPS SETUP REGISTER PHARMACY\] and is a read-only field on this screen.
- NPI: Displays the Pharmacy National Provider Identifier (NPI). This number is assigned to the pharmacy by the Centers for Medicare and Medicaid Services (CMS) and was requested by the Central Business Office (CBO). It is automatically determined by linking an entry in BPS PHARMACIES (#9002313.56) to an Outpatient Site.
- Select OUTPATIENT SITE: Enter a new OUTPATIENT SITE. One or more of the VISTA Pharmacy package's OUTPATIENT SITE entries (file \#59) must be associated with an ECME Pharmacy entry.
- CMOP SWITCH: Enter ON to process CMOP claims via ECME, OFF to not process CMOP claims. Choose from 0-CMOP OFF/1-CMOP ON.
- AUTO-REVERSE PARAMETER: ECME uses the AUTO-REVERSE site parameter when determining whether non-released prescription claims (those that have a PAYABLE response) are to be automatically REVERSED. The AUTO-REVERSE site parameter is set for the number of days that ECME will wait before the claim is automatically REVERSED. ECME will allow the user to enter a number between 3-10 and ECME will wait the entered number of days before REVERSING the non-released Rx with a payable response returned by the payer. The suggested setting is 5.
- DEFAULT DEA \#: Many payers require the prescriber's Drug Enforcement Administration (DEA) number as part of the claim. If the pharmacy has a DEA \# that may be used in case a prescriber does not have this DEA \# on file, enter that default DEA \# here.
- Select BPS Pharmacy for CS or Enter to bypass: Some pharmacies do not dispense controlled substances (CS), sending CS prescriptions to another pharmacy to be filled. Entering a CS pharmacy at this prompt will cause the NPI of the CS pharmacy to be used for any third party claim submissions.

Example Screen Print:

Select BPS PHARMACIES NAME: XXXXXX VAMC PHARMACY

NAME: XXXXXX VAMC PHARMACY

STATUS: ACTIVE

NCPDP \#: XXXXXXX

NPI: XXXXXXXXX

Select OUTPATIENT SITE: XXXXXX VAMC PHARMACY// \<ENTER\>

OUTPATIENT SITE: XXXXXX VAMC PHARMACY// \<ENTER\>

Select OUTPATIENT SITE: \<ENTER\>

CMOP SWITCH: CMOP ON// \<ENTER\>

AUTO-REVERSE PARAMETER: 10// \<ENTER\>

DEFAULT DEA \#: XXXXXXXXXX// \<ENTER\>

\*\*\* BPS Pharmacy for CS is an optional field.

This field should only be used when a dispensing pharmacy does not

have a valid DEA Controlled Substance Registration Certificate

and therefore those products are dispensed by a different pharmacy.

Press Enter to bypass the prompt. \*\*\*

Select one of the following:

1 Pharmacy 001

2 Pharmacy 002

Select BPS Pharmacy for CS or Enter to bypass: // Pharmacy 001

NCPDP \#: XXXXXXXX

NPI: XXXXXXXX

Press enter to continue:

### System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific hardware requirements for the ECME V. 1.0 package.

#### Disk Space Requirements

Since this version is distributed using KIDS, the transport global is automatically deleted after the initial installation.

There are less than 200 BPS\* routines, which occupies less than one MB of space.

#### Journaling Globals

The ECME V. 1.0 package uses the namespace BPS. All BPS\* globals should be journaled if journaling is used.

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc192072570" class="anchor"></span>Table 2: Print Templates</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>Number</th>
<th>Global Location</th>
<th>Name</th>
<th>Brief Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>9002313.02</td>
<td>^BPSC(</td>
<td>BPS CLAIMS</td>
<td>Intermediate form of transmissions. Fields are stored in formatted form. Raw packet is also stored. Most fields are in Free Text format to accommodate NCPDP Standard formatting criteria and required field lengths. Fields other than those with decimals in the number correlate directly to the field numbers supplied in the NCPDP Data Dictionary.</td>
</tr>
<tr class="even">
<td>9002313.03</td>
<td>^BPSR(</td>
<td>BPS RESPONSES</td>
<td>This file stores the response information returned by the third-party payer. Most of the fields have 'raw' NCPDP data so it is formatted per the NCPDP specifications.</td>
</tr>
<tr class="odd">
<td>9002313.12</td>
<td>^BPS(9002313.12,</td>
<td>BPS LOG</td>
<td><p>This is the ECME log, which is used to store an audit trail of ECME activity.</p>
<p>There are currently two types of logs – one for transactions and another for purging.</p></td>
</tr>
<tr class="even">
<td>9002313.15</td>
<td>^BPS(9002313.15,</td>
<td>BPS ASLEEP PAYERS</td>
<td>This file is used to store payers that are asleep or should be ignored because they are asleep. Generally, there should be few or no entries in this file unless there are payers that are asleep.</td>
</tr>
<tr class="odd">
<td>9002313.19</td>
<td>^BPS(9002313.19,</td>
<td>BPS NCPDP PATIENT RELATIONSHIP CODE</td>
<td>Standard NCPDP Patient Relationship data to be used in submitting claims. The file and data should never be locally modified.</td>
</tr>
<tr class="even">
<td>9002313.2</td>
<td>^BPS(9002313.2,</td>
<td>BPS NCPDP OTHER PAYER AMT PAID QUAL</td>
<td>Static file to store the codes and descriptions for NCPDP field 342-HC (Other Payer Amount Paid Qualifier). These codes are used for secondary electronic claim transmissions to third party payers. No local changes should ever be made to this file.</td>
</tr>
<tr class="odd">
<td>9002313.21</td>
<td>^BPS(9002313.21,</td>
<td>BPS NCPDP PROFESSIONAL SERVICE CODE</td>
<td>Static file that is used to store the possible NCPDP PROFESSIONAL SERVICE CODE values, which are used for overriding DUR rejects. This file is populated by the installation and should not be edited by sites.</td>
</tr>
<tr class="even">
<td>9002313.22</td>
<td>^BPS(9002313.22,</td>
<td>BPS NCPDP RESULT OF SERVICE CODE</td>
<td>Static file used to store the possible NCPDP RESULT OF SERVICE CODE values, which are used for overriding DUR rejects. This file is populated by the installation and should not be edited by sites.</td>
</tr>
<tr class="odd">
<td>9002313.23</td>
<td>^BPS(9002313.23,</td>
<td>BPS NCPDP REASON FOR SERVICE CODE</td>
<td>Static file that is used to store the possible NCPDP REASON FOR SERVICE CODE values, which are used for overriding DUR rejects. This file is populated by the installation and should not be edited by sites.</td>
</tr>
<tr class="even">
<td>9002313.24</td>
<td>^BPS(9002313.24,</td>
<td>BPS NCPDP DAW CODE</td>
<td>Static file used to store NCPDP DAW (Dispense as Written) codes, which are used for prescription electronic claim transmission to third party payers. This file is populated by the installation and should not be edited by sites.</td>
</tr>
<tr class="odd">
<td>9002313.25</td>
<td>^BPS(9002313.25,</td>
<td>BPS NCPDP CLARIFICATION CODES</td>
<td>This file is used to store the possible NCPDP CLARIFICATION CODE values, which are used for overriding DUR rejects. No local changes should ever be made to this file. The data stored in this file are based on the NCPDP standards and are nationally distributed.</td>
</tr>
<tr class="even">
<td>9002313.26</td>
<td>^BPS(9002313.26,</td>
<td>BPS NCPDP PRIOR AUTHORIZATION TYPE CODE</td>
<td>This file comes with standard NCPDP prior authorization data to be used in submitting claims. The file and data should never be locally modified, edited or changed.</td>
</tr>
<tr class="odd">
<td>9002313.27</td>
<td>^BPS(9002313.27,</td>
<td>BPS NCPDP PATIENT RESIDENCE CODE</td>
<td>Standard NCPDP Patient Residence data used in submitting claims. The file and data should never be locally modified.</td>
</tr>
<tr class="even">
<td>9002313.28</td>
<td>^BPS(9002313.28,</td>
<td>BPS NCPDP PHARMACY SERVICE TYPE</td>
<td>Standard NCPDP Pharmacy Service Type data used in submitting claims. The file and data should never be locally modified.</td>
</tr>
<tr class="odd">
<td>9002313.29</td>
<td>^BPS(9002313.29,</td>
<td>BPS NCPDP DELAY REASON CODE</td>
<td>Standard NCPDP Delay Reason Code data used in submitting claims. The file and data should never be locally modified.</td>
</tr>
<tr class="even">
<td>9002313.31</td>
<td>^BPS(9002313.31,</td>
<td>BPS CERTIFICATION</td>
<td>This file holds data for development use in certifying software when required by clearinghouses and payers.</td>
</tr>
<tr class="odd">
<td>9002313.32</td>
<td>^BPS(9002313.32,</td>
<td>BPS PAYER RESPONSE OVERRIDES</td>
<td>This file is used to store Payer Response Overrides. This file should not be populated on production systems, only on test systems.</td>
</tr>
<tr class="even">
<td>9002313.34</td>
<td>^BPS(9002313.34,</td>
<td>BPS NCPDP PRESCRIBER PLACE OF SERVICE</td>
<td>This file is used to store the possible NCPDP PRESCRIBER PLACE OF SERVICE CODES, that can be sent with a claim.</td>
</tr>
<tr class="odd">
<td>9002313.35</td>
<td>^BPS(9002313.35,</td>
<td>BPS NCPDP BENEFIT STAGE INDICATOR</td>
<td>This file is used to store the possible NCPDP BENEFIT STAGE INDICATOR, that can be sent on a claim or returned by the payer.</td>
</tr>
<tr class="even">
<td>9002313.36</td>
<td>^BPS(9002313.36,</td>
<td>BPS NCPDP LTPAC DISPENSE FREQUENCY</td>
<td>This file is used to store the possible NCPDP LTPAC DISPENSE FREQUENCY, that can be sent on a claim.</td>
</tr>
<tr class="odd">
<td>9002313.37</td>
<td>^BPS(9002313.37,</td>
<td>BPS NCPDP PATIENT PAY COMPONENT QUALIFIER</td>
<td>This file is used to store the possible NCPDP PATIENT PAY COMPONENT QUALIFIER, that can be returned by the payer.</td>
</tr>
<tr class="even">
<td>9002313.38</td>
<td>^BPS(9002313.38,</td>
<td>BPS NCPDP OTHER PAYER PROGRAM TYPE</td>
<td>This file is used to store the possible NCPDP OTHER PAYER ADJUDICATED PROGRAM TYPE, that can be returned by the payer.</td>
</tr>
<tr class="odd">
<td>9002313.39</td>
<td>^BPS(9002313.39,</td>
<td>BPS NCPDP COMPOUND PROD ID QUALIFIER</td>
<td></td>
</tr>
<tr class="even">
<td>9002313.4</td>
<td>^BPS(9002313.4,</td>
<td>BPS NCPDP OTHER PHARMACY ID QUALIFIER</td>
<td></td>
</tr>
<tr class="odd">
<td>9002313.41</td>
<td>^BPS(9002313.41,</td>
<td>BPS NCPDP OTHER PRESCRIBER ID QUALIFIER</td>
<td></td>
</tr>
<tr class="even">
<td>9002313.42</td>
<td>^BPS(9002313.42,</td>
<td>BPS NCPDP INVALID PROVIDER DATA SOURCE</td>
<td></td>
</tr>
<tr class="odd">
<td>9002313.43</td>
<td>^BPS(9002313.43,</td>
<td>BPS NCPDP OTHER PAYER ID QUALIFIER</td>
<td></td>
</tr>
<tr class="even">
<td>9002313.44</td>
<td>^BPS(9002313.44,</td>
<td>BPS NCPDP HELP DESK PHONE NUMBER QUALIFIER</td>
<td></td>
</tr>
<tr class="odd">
<td>9002313.45</td>
<td>^BPS(9002313.45,</td>
<td>BPS NCPDP MEDICARE PART D COVERAGE CODE</td>
<td></td>
</tr>
<tr class="even">
<td>9002313.511</td>
<td>^BPS(9002313.511,</td>
<td>BPS NCPDP OVERRIDE</td>
<td>Contains values for override of specific NCPDP fields.</td>
</tr>
<tr class="odd">
<td>9002313.56</td>
<td>^BPS(9002313.56,</td>
<td>BPS PHARMACIES</td>
<td>Pharmacy-specific data -- NCPDP #, NPI, default DEA #, etc. One BPS PHARMACY has a list of one or more OUTPATIENT SITES (file 59)</td>
</tr>
<tr class="even">
<td>9002313.57</td>
<td>^BPSTL(</td>
<td>BPS LOG OF TRANSACTIONS</td>
<td>This file contains a copy of the BPS Transaction (#9002313.59) record after it completes (reaches 99%) and thus, provides a historical record of all completed transactions.</td>
</tr>
<tr class="odd">
<td>9002313.58</td>
<td>^BPSECX("S",</td>
<td>BPS STATISTICS</td>
<td>Statistics; displayed by the BPS STATISTICS SCREEN option.</td>
</tr>
<tr class="even">
<td>9002313.59</td>
<td>^BPST(</td>
<td>BPS TRANSACTION</td>
<td>This file stores the most recent transactions for an RX/Fill (Billing Request or Reversal) or Patient/Policy (Eligibility Verification). When complete (status 99), a copy of the record is placed in the BPS Log of Transactions file (#9002313.57).</td>
</tr>
<tr class="odd">
<td>9002313.77</td>
<td>^BPS(9002313.77,</td>
<td>BPS REQUESTS</td>
<td>This file is used to store data for queued requests before the ECME engine un-queues them during processing. The data stored in this file are used to create a record in BPS TRANSACTION file (#9002313.59) to build a claim request or reversal and send it to the insurer (payer). Generally, there should be few or no entries in this file unless there are stranded claims/reversal or requests that need to be un-stranded by the user.</td>
</tr>
<tr class="even">
<td>9002313.78</td>
<td>^BPS(9002313.78,</td>
<td>BPS INSURER DATA</td>
<td>This file is used to store insurers' details data returned by the Integrated Billing package to be used by the ECME engine to build claim requests and reversals and send them to insurers (payers). Generally, there should be few or no entries in this file unless there are stranded claims, reversal or requests that need to be un-stranded by the user.</td>
</tr>
<tr class="odd">
<td>9002313.83</td>
<td>^BPSF(9002313.83,</td>
<td>BPS RESULT CATEGORY</td>
<td>A list of the possible result categories, as returned by CATEG^BPSOSUC(). This table is overwritten by the installation.</td>
</tr>
<tr class="even">
<td>9002313.89</td>
<td>^BPSF(9002313.89,</td>
<td>BPS ERROR CODES</td>
<td>Obsolete.</td>
</tr>
<tr class="odd">
<td>9002313.91</td>
<td>^BPSF(9002313.91,</td>
<td>BPS NCPDP FIELD DEFS</td>
<td>The file of NCPDP Data Dictionary fields which are combined into formatted packets. Package installation updates this file.</td>
</tr>
<tr class="even">
<td>9002313.92</td>
<td>^BPSF(9002313.92,</td>
<td>BPS NCPDP FORMATS</td>
<td>Entries are commonly referred to as “payer sheets”. These are the formats for sending claims. This file was initially installed as part of the dormant release and updates are sent by the AITC via HL7. Never modify locally, except in cooperation with development.</td>
</tr>
<tr class="odd">
<td>9002313.93</td>
<td>^BPSF(9002313.93,</td>
<td>BPS NCPDP REJECT CODES</td>
<td>Rejection codes as defined by NCPDP. Never edit this file. Installation overwrites this file, totally.</td>
</tr>
<tr class="even">
<td>9002313.95</td>
<td>^BPSACR(,</td>
<td>BPS AUTO CLOSE REJECT CODES</td>
<td>Stores reject codes defined as auto close. Specific criteria, defined in this file, will be used to determine if a claim should automatically be closed upon the pharmacist ignoring a reject on the prescription.</td>
</tr>
<tr class="odd">
<td>9002313.99</td>
<td>^BPS(9002313.99,</td>
<td>BPS SETUP</td>
<td>ECME system parameters. Contains only one entry called MAIN SETUP ENTRY with an IEN of 1.</td>
</tr>
</tbody>
</table>

<span id="_Toc192072570" class="anchor"></span>Table 2: Print Templates

Data Dictionaries (DD) are part of the online documentation for this software application. Use VA FileMan List File Attributes \[DILIST\] option, under the Data Dictionary Utilities \[DI DDU\] option, to print the DDs.

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of routines exported by the ECME V. 1.0 package. Each routine’s first line contains a brief description of the routine’s function. Use the First Line Routine Print \[XU FIRST LINE PRINT\] option to print a list of just the first line of each BPS\* routine.

- 
- BPSACR
- BPSBCKJ
- BPSBUTL
- BPSCMT
- BPSCMT01
- BPSCT
- BPSECA1
- BPSECA8
- BPSECFM
- BPSECMC2
- BPSECMP2
- BPSECMPS
- BPSECX0
- BPSECX1
- BPSELG
- BPSFLD01
- BPSGRPL
- BPSKBERPT
- BPSJACK
- BPSJAREG
- BPSJHLI
- BPSJHLT
- BPSJINIT
- BPSJPHNM
- BPSJPREG
- BPSJUTL
- BPSJUTL1
- BPSJVAL
- BPSJVAL1
- BPSJVAL2
- BPSJZPR
- BPSJZQR
- BPSJZRP
- BPSMHDR
- BPSNCPD1
- BPSNCPD2
- BPSNCPD3
- BPSNCPD4
- BPSNCPD5
- BPSNCPD6
- BPSNCPD9
- BPSNCPDP
- BPSNPI
- BPSOPR
- BPSOPR2
- BPSOPR3
- BPSOS
- BPSOS03
- BPSOS2
- BPSOS2A
- BPSOS2B
- BPSOS2C
- BPSOS57
- BPSOS6M
- BPSOSC2
- BPSOSCA
- BPSOSCB
- BPSOSCC
- BPSOSCD
- BPSOSCE
- BPSOSCF
- BPSOSH2
- BPSOSH3
- BPSOSHF
- BPSOSHR
- BPSOSIY
- BPSOSIZ
- BPSOSK
- BPSOSL
- BPSOSL1
- BPSOSO
- BPSOSO1
- BPSOSO2
- BPSOSQ
- BPSOSQ2
- BPSOSQ4
- BPSOSQA
- BPSOSQC
- BPSOSQF
- BPSOSQG
- BPSOSQL
- BPSOSRB
- BPSOSRX
- BPSOSRX2
- BPSOSRX3
- BPSOSRX4
- BPSOSRX5
- BPSOSRX6
- BPSOSRX7
- BPSOSRX8
- BPSOSS8
- BPSOSSG
- BPSOSU
- BPSOSU1
- BPSOSU2
- BPSOSU3
- BPSOSU4
- BPSOSU5
- BPSOSU8
- BPSOSU9
- BPSOSUC
- BPSOSUD
- BPSOSUE
- BPSPHAR
- BPSPRRX
- BPSPRRX1
- BPSPRRX2
- BPSPRRX3
- BPSPRRX4
- BPSPRRX5
- BPSPRRX6
- BPSPRRX7
- BPSPSOU1
- BPSRCRI
- BPSRDT1
- BPSREOP
- BPSREOP1
- BPSRES
- BPSRES1
- BPSRPAY
- BPSRPT0
- BPSRPT1
- BPSRPT2
- BPSRPT3
- BPSRPT3A
- BPSRPT4
- BPSRPT5
- BPSRPT5A
- BPSRPT6
- BPSRPT7
- BPSRPT7A
- BPSRPT8
- BPSRPT8A
- BPSRPT9
- BPSRPT9A
- BPSRSELG
- BPSRSEV
- BPSRSHLD
- BPSRSINS
- BPSRSM
- BPSRSPRS
- BPSRSRLC
- BPSRSTPJ
- BPSSCR
- BPSSCR01
- BPSSCR02
- BPSSCR03
- BPSSCR04
- BPSSCR05
- BPSSCRCL
- BPSSCRCU
- BPSSCRCV
- BPSSCRDS
- BPSSCRDV
- BPSSCRL1
- BPSSCRLG
- BPSSCRN0
- BPSSCRPR
- BPSSCRRJ
- BPSSCRRS
- BPSSCRRV
- BPSSCRSL
- BPSSCRU1
- BPSSCRU2
- BPSSCRU3
- BPSSCRU4
- BPSSCRU5
- BPSSCRU6
- BPSSCRUD
- BPSSCRV1
- BPSSCRV2
- BPSTEST
- BPSTEST1
- BPSTEST2
- BPSTSET
- BPSTSET2
- BPSUSCR
- BPSUSCR1
- BPSUSCR2
- BPSUSCR4
- BPSUTIL
- BPSUTIL1
- BPSUTIL2
- BPSVRX
- BPSVRX1
- BPSVRX2
- BPSVRX3
- BPSWRKLS

### ### Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entry points provided by the ECME V. 1.0 package to other software packages can be found in the External Relationships section of this manual. No other routines are designated as callable from outside of this package.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name               | File         |
|--------------------|--------------|
| BPS TECH – FILES   | FILE (#1)    |
| BPS TECH – OPTIONS | OPTION (#19) |

<span id="_Toc192072571" class="anchor"></span>Table 3: Input Templates

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                     | File                         |
|--------------------------|------------------------------|
| BPSJ PHARMACY ENTER/EDIT | BPS PHARMACIES (#9002313.56) |
| BPSJ SITE SETUP          | BPS SETUP (#9002313.99)      |

<span id="_Toc192072572" class="anchor"></span>Table 4: Sort Templates

### Sort Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                 | File                          |
|----------------------|-------------------------------|
| BPS SETUP PHARMACIES | BPS PHARMACIES (# 9002313.56) |

<span id="_Toc192072573" class="anchor"></span>Table 5: Top-level Menus

### List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BPS AUTO CLOSE REJECTS

BPS LSTMN COMMENTS

BPS LSTMN DEVLOG

BPS LSTMN ECME REOPEN

BPS LSTMN ECME UNSTRAND

BPS LSTMN ECME USRSCR

BPS LSTMN LOG

BPS LSTMN RSCH MENU

BPS OPECC REJECT INFORMATION

BPS STATISTICS AND MANAGEMENT

BPS VIEW ECME RX

How to View List Templates using VA FileMan

Select VA FileMan Option: Inquire to File Entries

OUTPUT FROM WHAT FILE: LIST TEMPLATE//

Select LIST TEMPLATE NAME: BPS STATISTICS AND MANAGEMENT

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// - No record number (IEN), no Computed Fields

NAME: BPS STATISTICS AND MANAGEMENT TYPE OF LIST: PROTOCOL RIGHT MARGIN: 80

TOP MARGIN: 4 BOTTOM MARGIN: 18

OK TO TRANSPORT?: NOT OK

USE CURSOR CONTROL: YES PROTOCOL MENU: BPS PROTOCOL 2 SCREEN TITLE: ECME STATISTICS

ALLOWABLE NUMBER OF ACTIONS: 1 AUTOMATIC DEFAULTS: YES HIDDEN ACTION MENU: VALM HIDDEN ACTIONS

ARRAY NAME: ^TMP("BPSOS2",\$J) EXIT CODE: D EXIT^BPSOS2 HEADER CODE: D HDR^BPSOS2

HELP CODE: D HELP^BPSOS2 ENTRY CODE: D INIT^BPSOS2

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Stand-alone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the Electronic Claims Management Engine (ECME) V. 1.0 package options are designed to be “stand-alone,, that is, options can be accessed without first accessing the top-level menu. All the options can be placed on menus other than the original menu without any additional editing; users will still be required to hold the proper security key to gain access to each option.

### Top-level Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME Main Menu \[BPSMENU\] option is the top-level menu. It contains one user option, plus three BPS sub-menus.

| ECME                               | BPS                   |
|------------------------------------|-----------------------|
| ECME User Screen                   | \[BPS USER SCREEN\]   |
| ECME Pharmacy COB                  | \[BPS COB MENU\]      |
| Pharmacy ECME Manager Menu         | \[BPS MANAGER MENU\]  |
| Pharmacy Electronic Claims Reports | \[BPS MENU RPT MAIN\] |

<span id="_Toc192072574" class="anchor"></span>Table 6: Key Assignments

#### Key Assignment

The ECME Main Menu \[BPSMENU\] and its main sub-menus require users to possess Security Keys (file \#19.1) for access to the options.

The following keys control the ECME Main Menu and its three main sub-menus:

<table>
<caption><p><span id="_Toc192072575" class="anchor"></span>Table 7: Options</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Key</th>
<th>Menu</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BPSMENU</td>
<td>Required for the main ECME menu [BPSMENU].</td>
</tr>
<tr class="even">
<td>BPS USER</td>
<td>Required for the ECME User Screen [BPS USER SCREEN] and for the option “Process Secondary/TRICARE Rx to ECME” [BPS COB PROCESS SECOND TRICARE].</td>
</tr>
<tr class="odd">
<td>BPS MANAGER</td>
<td><p>Required for these ECME options:</p>
<ul>
<li><blockquote>
<p>Pharmacy ECME Manager Menu [BPS MANAGER MENU].</p>
</blockquote></li>
<li><blockquote>
<p>Statistics Screen [BPS STATISTICS SCREEN].</p>
</blockquote></li>
<li><blockquote>
<p>ECME transaction maintenance options [BPS MENU MAINTENANCE].</p>
</blockquote></li>
<li><blockquote>
<p>View/Unstrand Submissions Not Completed [BPS UNSTRAND SCREEN].</p>
</blockquote></li>
<li><blockquote>
<p>Re-Open CLOSED Claims [BPS REOPEN CLOSED CLAIMS].</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>BPS MASTER</td>
<td><p>Required for these ECME options:</p>
<ul>
<li><blockquote>
<p>Pharmacy ECME Setup Menu [BPS SETUP MENU].</p>
</blockquote></li>
<li><blockquote>
<p>Edit Basic ECME Parameters [BPS SETUP BASIC PARAMS].</p>
</blockquote></li>
<li><blockquote>
<p>Edit ECME Pharmacy Data [BPS SETUP PHARMACY].</p>
</blockquote></li>
<li><blockquote>
<p>Register Pharmacy with Austin Automation Center [BPS SETUP REGISTER PHARMACY].</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>BPS REPORTS</td>
<td><p>Required for these ECME options:</p>
<ul>
<li><blockquote>
<p>Pharmacy Electronic Claims Reports [BPS MENU RPT MAIN].</p>
</blockquote></li>
<li><blockquote>
<p>Claim Results and Status [BPS MENU RPT CLAIM STATUS].</p>
</blockquote></li>
<li><blockquote>
<p>Recent Transactions [BPS RPT RECENT TRANSACTIONS].</p>
</blockquote></li>
<li><blockquote>
<p>Closed Claims Report [BPS RPT CLOSED CLAIMS].</p>
</blockquote></li>
<li><blockquote>
<p>CMOP/ECME Activity Report [BPS RPT CMOP/ECME ACTIVITY].</p>
</blockquote></li>
<li><blockquote>
<p>Claims Submitted, Not Yet Released [BPS RPT NOT RELEASED].</p>
</blockquote></li>
<li><blockquote>
<p>Payable Claims Report [BPS RPT PAYABLE].</p>
</blockquote></li>
<li><blockquote>
<p>Payer Sheet Detail Report [BPS RPT PAYER SHEET DETAIL].</p>
</blockquote></li>
<li><blockquote>
<p>Rejected Claims Report [BPS RPT REJECTION].</p>
</blockquote></li>
<li><blockquote>
<p>Reversal Claims Report [BPS RPT REVERSAL].</p>
</blockquote></li>
<li><blockquote>
<p>Totals by Date [BPS RPT TOTALS BY DAY].</p>
</blockquote></li>
<li><blockquote>
<p>Turn-around time statistics [BPS RPT TURNAROUND STATS].</p>
</blockquote></li>
<li><blockquote>
<p>ECME Setup – Pharmacies Report [BPS RPT SETUP PHARMACIES].</p>
</blockquote></li>
<li><blockquote>
<p>ECME Claims-Response Inquiry [BPS RPT CLAIMS RESPONSE].</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Spending Account Report [BPS RPT SPENDING ACCOUNT].</p>
</blockquote></li>
<li><blockquote>
<p>Other Reports [BPS MENU RPT OTHER].</p>
</blockquote></li>
<li><blockquote>
<p>Non-Billable Status Report [BPS RPT NON-BILLABLE REPORT].</p>
</blockquote></li>
<li><blockquote>
<p>Duplicate Claims Report [BPS RPT DUPLICATE CLAIMS].</p>
</blockquote></li>
<li><blockquote>
<p>ePharmacy Bills Created with Errors [BPS RPT ERRORS].</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>BPS SUPERVISOR</td>
<td><p>Required for this ECME option:</p>
<ul>
<li><blockquote>
<p>OPECC Productivity Report [BPS OPECC PRODUCTIVITY REPORT].</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc192072575" class="anchor"></span>Table 7: Options

Hierarchy of ECME Menu Options and Security Keys:

ECME (BPSMENU) \*\*LOCKED: BPSMENU\*\*

\|

\|

--------------------------------------------------------U ECME User Screen

\[BPS USER SCREEN\]

\*\*LOCKED: BPS USER\*\*

--COB ECME Pharmacy ----------------------------------SEC Potential

COB \[BPS COB Secondary Rx

MENU\] Claims Report

\| \[BPS COB RPT

\| SECONDARY

\| CLAIMS\]

\|

\|-------------------------------------------TRI Potential Claims

\| Report for Dual

\| Eligible \[BPS

\| POTENTIAL CLAIMS

\| RPT DUAL\]

\|

\|-------------------------------------------PRO Process

Secondary/TRICAR

E Rx to ECME

\[BPS COB PROCESS

SECOND TRICARE\]

\*\*LOCKED: BPS USER\*\*

--MGR Pharmacy ECME --------MNT ECME transaction -----UNS View/Unstrand

Manager Menu maintenance Submissions Not

\[BPS MANAGER options \[BPS Completed \[BPS

MENU\] MENU UNSTRAND SCREEN\]

\*\*LOCKED: BPS MAINTENANCE\] \*\*LOCKED: BPS MANAGER\*\*

MANAGER\*\* \*\*LOCKED: BPS

\| MANAGER\*\*

\| \|

\| \|-----------------ROC Re Open CLOSED

\| Claim \[BPS

\| REOPEN CLOSED

\| CLAIM\]

\| \*\*LOCKED: BPS MANAGER\*\*

\|

\|

\|

\|

\|-----------------SET Pharmacy ECME --------BAS Edit Basic ECME

\| Setup Menu \[BPS Parameters \[BPS

\| SETUP MENU\] SETUP BASIC

\| \*\*LOCKED: BPS PARAMS\]

\| MASTER\*\* \*\*LOCKED: BPS MASTER\*\*

\| \|

\| \|----------------PHAR Edit ECME

\| \| Pharmacy Data

\| \| \[BPS SETUP

\| \| PHARMACY\]

\| \| \*\*LOCKED: BPS MASTER\*\*

\| \|

\| \|-----------------REG Register

\| Pharmacy with

\| Austin

\| Automation

\| Center \[BPS

\| SETUP REGISTER

\| PHARMACY\]

\| \*\*LOCKED: BPS MASTER\*\*

\|

\|

\|------------------------------------------STAT Statistics

\| Screen \[BPS

\| STATISTICS

\| SCREEN\]

\|

\|--------------------------------------------CP ePharmacy Claim

Parameters \[BPS AUTO

CLOSE REJECT\]

\*\*LOCKED: BPS

SUPERVISOR\*\*

\*\*LOCKED: BPS MANAGER\*\*

--RPT Pharmacy -------------CLA Claim Results --------PAY Payable Claims

Electronic and Status \[BPS Report \[BPS RPT

Claims Reports MENU RPT CLAIM PAYABLE\]

\[BPS MENU RPT STATUS\] \*\*LOCKED: BPS REPORTS\*\*

MAIN\] \*\*LOCKED: BPS REPORTS\*\*

\*\*LOCKED: BPS REPORTS\*\* \|

\|

\| \|

\| \|-----------------REJ Rejected Claims

\| \| Report \[BPS RPT

\| \| REJECTION\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|----------------ECMP CMOP/ECME

\| \| Activity Report

\| \| \[BPS RPT

\| \| CMOP/ECME

\| \| ACTIVITY\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------REV Reversal Claims

\| \| Report \[BPS RPT

\| \| REVERSAL\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------NYR Claims

\| \| Submitted, Not

\| \| Yet Released

\| \| \[BPS RPT NOT

\| \| RELEASED\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------REC Recent

\| \| Transactions

\| \| \[BPS RPT RECENT

\| \| TRANSACTIONS\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------DAY Totals by Date

\| \| \[BPS RPT TOTALS

\| \| BY DAY\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------CLO Closed Claims

\| \| Report \[BPS RPT

\| \| CLOSED CLAIMS\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------NBS Non-Billable Status

\| \| Report \[BPS RPT

\| \| NON-BILLABLE REPORT

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------SPA Spending Account

\| \| Report \[BPS RPT

\| \| SPENDING

\| \| ACCOUNT\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------DUP Duplicate Claims Report

\| \| Report \[BPS RPT

\| \| DUPLICATE CLAIMS\]

\| \| \*\*LOCKED: BPS REPORTS\*\*

\| \|

\| \|-----------------ERR ePharmacy Bill Created

\| with Errors \[BPS RPT

\| ERRORS\]

\| \*\*LOCKED: BPS REPORTS\*\*

\|

\|

\|-----------------OTH Other Reports --------CRI ECME

\[BPS MENU RPT Claims-Response

OTHER\] Inquiry \[BPS RPT

\*\*LOCKED: BPS CLAIMS RESPONSE\]

REPORTS\*\* \*\*LOCKED: BPS REPORTS\*\*

\|

\|-----------------PAY Payer Sheet

\| Detail Report

\| \[BPS RPT PAYER

\| SHEET DETAIL\]

\| \*\*LOCKED: BPS REPORTS\*\*

\|

\|----------------PHAR ECME Setup -

\| Pharmacies

\| Report \[BPS RPT

\| SETUP

\| PHARMACIES\]

\| \*\*LOCKED: BPS REPORTS\*\*

\|

\|-----------------TAT Turn-around time

\| statistics \[BPS

\| RPT TURNAROUND

\| STATS\]

\| \*\*LOCKED: BPS REPORTS\*\*

\|

\|-----------------VER View ePharmacy

\| Rx \[BPS RPT VIEW

\| ECME RX\]

\|

\|-----------------OPR OPECC

Productivity

Report \[BPS

OPECC

PRODUCTIVITY

REPORT\]

\*\*LOCKED: BPS

SUPERVISOR\*\*

#### Menu Placement

It is recommended that the user place the ECME V. 1.0 main menu and sub-menus on the Core Applications menu where the other package menus are found.

#### Options

The following options are exported with the ECME V. 1.0 package:

| Option Name                    | Menu Text                                       |
|--------------------------------|-------------------------------------------------|
| BPS AUTO CLOSE REJECT          | ePharmacy Claim Parameters                      |
| BPS MANAGER MENU               | Pharmacy ECME Manager Menu                      |
| BPS MENU MAINTENANCE           | ECME Transaction Maintenance Options            |
| BPS MENU RPT CLAIM STATUS      | Claim Results and Status                        |
| BPS MENU RPT MAIN              | Pharmacy Electronic Claims Reports              |
| BPS MENU RPT OTHER             | Other Reports                                   |
| BPS COB MENU                   | ECME Pharmacy COB                               |
| BPS COB PROCESS SECOND TRICARE | Process Secondary / TRICARE Rx to ECME          |
| BPS COB RPT SECONDARY CLAIMS   | Potential Secondary Rx Claims Report            |
| BPS POTENTIAL CLAIMS RPT DUAL  | Potential Claims Report for Dual Eligible       |
| BPS NIGHTLY BACKGROUND JOB     | BPS Nightly Background Job                      |
| BPS REOPEN CLOSED CLAIM        | Re-Open CLOSED Claim                            |
| BPS RPT RECENT TRANSACTIONS    | Recent Transactions                             |
| BPS RPT CLOSED CLAIMS          | Closed Claims Report                            |
| BPS RPT CMOP/ECME ACTIVITY     | CMOP / ECME Activity Report                     |
| BPS RPT NOT RELEASED           | Claims Submitted, Not Yet Released              |
| BPS RPT PAYABLE                | Payable Claims Report                           |
| BPS RPT PAYER SHEET DETAIL     | Payer Sheet Detail Report                       |
| BPS RPT REJECTION              | Rejected Claims Report                          |
| BPS RPT REVERSAL               | Reversal Claims Report                          |
| BPS RPT SETUP PHARMACIES       | ECME Setup - Pharmacies Report                  |
| BPS RPT TOTALS BY DAY          | Totals by Date                                  |
| BPS RPT TURNAROUND STATS       | Turn-around Time Statistics                     |
| BPS SETUP MENU                 | Pharmacy ECME Setup Menu                        |
| BPS SETUP BASIC PARAMS         | Edit Basic Pharmacy ECME Parameters             |
| BPS SETUP PHARMACY             | Edit ECME Pharmacy Data                         |
| BPS SETUP REGISTER PHARMACY    | Register Pharmacy with Austin Automation Center |
| BPS STATISTICS SCREEN          | Statistics Screen                               |
| BPS UNSTRAND SCREEN            | View / Unstrand Submissions Not Completed       |
| BPS USER SCREEN                | ECME User Screen                                |
| BPSMENU                        | ECME                                            |
| BPS RPT CLAIMS RESPONSE        | ECME Claims-Response Inquiry                    |
| BPS RPT NON-BILLABLE REPORT    | Non-Billable Status Report                      |
| BPS RPT SPENDING ACCOUNT       | Spending Account Report                         |
| BPS RPT VIEW ECME RX           | View ePharmacy Rx                               |
| BPS OPECC PRODUCTIVITY REPORT  | OPECC Productivity Report                       |
| BPS RPT DUPLICATE CLAIMS       | Duplicate Claims Report                         |
| BPS RPT ERRORS                 | ePharmacy Bills Created with Errors             |

<span id="_Toc192072576" class="anchor"></span>Table 8: External Options

The following external options are accessed by the ECME V. 1.0 package:

| Option Name | Menu Text | Package |
|-------------|-----------|---------|
| N/A         |           |         |

<span id="_Toc192072577" class="anchor"></span>Table 9: Menus

Example: How to View the Exported Options Using VA FileMan

VA FileMan 22.0

Select OPTION: 5 INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: OPTION// \<Enter\>

Select OPTION NAME: BPSMENU ECME

ANOTHER ONE: \<Enter\>

STANDARD CAPTIONED OUTPUT? Yes// \<Enter\> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// \<Enter\> - No record number (IEN), no Computed

Fields

DISPLAY AUDIT TRAIL? No// \<Enter\> NO

NAME: BPSMENU MENU TEXT: ECME

TYPE: menu CREATOR: ECMEuser,One

LOCK: BPSMENU PACKAGE: IHS PHARMACY POINT OF SALE

E ACTION PRESENT: YES HEADER PRESENT?: YES

DESCRIPTION: The main menu

ITEM: BPS MANAGER MENU SYNONYM: MGR

DISPLAY ORDER: 2

ITEM: BPS USER SCREEN SYNONYM: U

DISPLAY ORDER: 1

ITEM: BPS MENU RPT MAIN SYNONYM: RPT

DISPLAY ORDER: 4

ENTRY ACTION: K BPSQUIT D INIT^BPSMHDR I \$G(BPSQUIT) K BPSQUIT S XQUIT=1

HEADER: D HDR^BPSMHDR TIMESTAMP: 60116,62862

TIMESTAMP OF PRIMARY MENU: 60044,54655

UPPERCASE MENU TEXT: ECME

Select OPTION NAME:

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At present, the Electronic Claims Management Engine (ECME) V. 1.0 package does not provide for the archiving of its data.

### Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BPS Nightly Background Job, which should be scheduled to run nightly, will purge data older than 365 days from the BPS LOG (#9002313.12) file.

## Callable Routines / Entry Points / Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only calls into Electronic Claims Management Engine (ECME) V. 1.0 should be done by the Pharmacy package interface and Claims Tracking.

### Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no routines that are callable by the first routine line. Please see the API section for callable entry points in the routines.

### Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \$\$EN^BPSNCPDP

This API submits a billing request or reversal to ECME. The software uses Integrated Billing to determine if the claim is ECME billable. If it is, the claim will be put on a queue and processed. Use of \$\$EN^BPSNCPDP is supported by Integration Agreement \#4415 and is only available to Outpatient Pharmacy and Integrated Billing.

There are eighteen parameters that can be passed into this API.

1.  BRXIEN (required) – Prescription IEN, file \#52 (required).
2.  BFILL (optional) – Prescription Fill Number. If omitted, the first fill is assumed.
3.  DOS (optional) – Date of Service. If omitted, this will be calculated to be the released date of the prescription and fill. If the prescription and fill has not been released, it will be the current date. If the calculated date is on or after the expiration date of the prescription, and this is a resubmission, then the system will use the date of service from the initial claim.
4.  BWHERE (required) – Prescription Action string (optional). Allowed values:
- AREV = Auto-Reversal
- BB = Back Billing
- CRLB = CMOP / OPAI Release & Rebill
- CRLR = CMOP / OPAI Release & Reverse (successful release)
- CRLX = CMOP / OPAI unsuccessful release & reverse
- CRRL = CMOP / OPAI Release – Original claim not paid, submit another claim, no reversal
- DC = Discontinue – only reverse un-released PAYABLE DC's, release date check should be in calling routine.
- DE = Delete
- ED = Edit (includes RX release with NDC edit)
- ERES = Resubmit from ECME user screen
- ERWV = Resubmit Without Reversal from ECME user screen
- ERNB = Resubmit of a TRI / CVA non-billable entry from the ECME user screen
- EREV = Reversal from ECME user screen
- HLD = Put prescription on Hold
- OREV = Reversal from Outpatient Pharmacy edit screen
- RSNB = Resubmit Non-Billable TRICARE & CHAMPVA from PSO Reject Info Screen
- OF = Original Fill
- P2 = Original submission from PRO Option, no reversal
- P2S = Resubmit from PRO Option
- PC = Pull CMOPs
- PE = Pull early from suspense
- PL = Pull local from suspense
- PP = Pull RX (PP) action from Patient Prescription Processing option.
- RF = Refill
- RN = Renew
- RRL = Release – Original claim not paid, submit another claim, no reversal
- RS = Return-to-Stock
5.  BILLNDC (optional) – Valid NDC# with format 5-4-2 (optional). If omitted, the NDC for the prescription / fill is assumed.
6.  REVREAS (optional) – Reversal Reason
7.  DURREC (optional) – String of up to three sets of DUR info. Sets are delimited with "~". Each set consists of three "^" pieces:
- 1st piece – Professional Service Code
- 2nd piece – Reason for Service Code
- 3rd piece – Result of Service Code
8.  BPOVRIEN (optional) – Pointer to the BPS NCPDP OVERRIDE file (#9002313.511); only passed if there are overrides entered by a user via the Resubmit with Edits (RED) option.
9.  BPSCLARF (optional) – Submission Clarification Code to be included in the claim.
10. BPSAUTH (optional) – String of Prior Authorization info (optional) – Two "^" pieces:
- 1<sup>st</sup> piece – Prior Authorization Type Code
- 2<sup>nd</sup> piece – Prior Authorization Number
11. BPCOBIND (optional) – Coordination of Benefits (COB) indicator – 1- Primary, 2- Secondary. If omitted, defaults to 1.
12. BPJOBFLG (optional) – Background / foreground job flag:

B – if called by un-queuing logic in background

F – if called by other (foreground) processes (default)

13. BPREQIEN (optional) – IEN of the BPS REQUEST entry to be unqueued.
14. BPSCLOSE (optional) – Local array used for Close After Reversal functionality when the user had chosen to close the claim after successful reversal. Used with BWHERE="EREV" only. If claim needs to be closed then:

BPSCLOSE("CLOSE AFT REV")=1

BPSCLOSE("CLOSE AFT REV REASON")= IEN of file \#356.8

BPSCLOSE("CLOSE AFT REV COMMENT")= text of the comment

15. BPSPLAN (optional) – IEN of the entry in the GROUP INSURANCE PLAN file (#355.3).
16. BPSPRDAT (optional) – Array, passed by reference, which contains primary claim data that is needed to submit a secondary claim.

Format: BPSPRDAT(NCPDP field)

17. BPSRTYPE (optional) – Rate Type, IEN file \#399.3.
18. BPSDELAY (optional) – Delay Reason Code, IEN of BPS NCPDP DELAY REASON CODE, file \#9002313.29.

The output of this extrinsic function is a string in the format:

> RESPONSE^MESSAGE^ELIGIBILITY^CLAIMSTATUS^COB^RXCOB^INSURANCE

Where:

1.  RESPONSE indicates:

0 – Submitted through ECME

1 – No submission through ECME

2 – IB not billable

3 – Claim was closed, not submitted (RTS / Deletes)

4 – Unable to queue claim

5 – Incorrect information supplied to ECME

6 – Inactive ECME – Primarily used for TRICARE and CHAMPVA to indicate it is ok to process the prescription

10 – Reversal but no resubmit

4.  MESSAGE = Message associated with the response (error/submitted).
5.  ELIGIBILITY

V – Veteran

T – TRICARE

C – CHAMPVA

6.  CLAIMSTATUS = claim status (null or IN PROGRESS / E PAYABLE / etc.).
7.  COB = Coordination of Benefit indicator of the insurance as it is stored in the PATIENT file:

1 – primary

2 – secondary

3 – tertiary

8.  RXCOB = payer sequence indicator of the claim sent to the payer as a result of this call:

1 – primary

2 – secondary

9.  INSURANCE = Name of the insurance company that was billed as a result of this call.

Examples of returned values:

“0^Prescription XYZ successfully submitted to ECME for claim generation.^V^E PAYABLE”

“0^Reversing prescription 100469.^V^E REVERSAL ACCEPTED”

“1^ECME switch is not on for the site^T^E REVERSAL ACCEPTED

“2^Null DEA Special Handling field^V^”

“3^Claim was not payable so it has been closed. No ECME claim created.^V^E REJECTED”

“4^Error: There is a SCHEDULED request without ACTIVATED requests, RXIEN=XYZ, REFILL=0^V^IN PROGRESS”

“5^RX Action parameter missing^V^E PAYABLE”

#### \$\$EN^BPSNCPD9

This API submits an eligibility verification request to ECME. The software uses Integrated Billing to determine if the request is ECME billable. If it is, the request will be put on a queue and processed. Use of \$\$EN^BPSNCPD9 is supported by Integration Agreement \# 5576 and is only available to Integrated Billing.

Input Parameters:

- DFN (required) – Patient.
- BPSARRY- Array of values:
- "PLAN" (required) – IEN to the GROUP INSURANCE PLAN file (#355.3)
- "DOS" (required) – Date of Service
- "IEN" (optional) – IEN to PRESCRIPTION file (#52)
- "FILL NUMBER" (optional) – Fill Number
- "REL CODE" (optional) – Relationship Code
- "PERSON CODE" (optional) – Person Code

Return Value – A string with two pieces

- Piece 1 – 0: Not submitted or 1: Submitted.
- Piece 2 – Message with final disposition (submitted or reason not submitted).

#### \$\$STATUS^BPSOSRX

This API shows the status, or a claim submitted to ECME. Use of \$\$STATUS^BPSOSRX is supported by Integration Agreement \#4300 and is only available to Outpatient Pharmacy.

2.  If the claim has already been processed and it is resubmitted, a reversal will be done first, and then the resubmit will be done. Intervening calls to \$\$STATUS may show progress of the reversal before the resubmitted claim is processed.

Input Parameters:

- KEY1 (required) – First key of the request.
- KEY2 (required) – Second key of the request.
- QUE (optional) – Queue check flag, where:
- 0 – Do not check if a request is on the queue
- 1 (or null) – Check if a request is on the queue, defaults to 1
3.  External routines should either not pass this parameter or set it to 1. The values of 0 (zero) or null are reserved for internal ECME processing.
- BPRQIEN (optional) – BPS REQUESTS ien, file \#9002313.77.
- BPCOB (optional) – The payer sequence, where '1' indicates Primary and '2' indicates Secondary. If BPCOB is null, then Primary is assumed.

Return Value:

This function will return null if there is not ECME record for this request or a string in the format "RESULT^LAST UPDATE DATE/TIME^DESCRIPTION^STATUS %.”

Where:

- RESULT – Current status of the request. It can have one of three values:
- “SCHEDULED” for scheduled (not ACTIVATED) requests
- “IN PROGRESS” for incomplete request
- The final status for complete requests (see below)
- LAST UPDATE DATE/TIME – The FileMan date / time of the last update to the status of this request.
- DESCRIPTION is either:
- Incomplete requests will be the progress status (e.g., Waiting to Start, Transmitting, etc.)
- Completed requests will have either be:
  - The reason that the ECME process was aborted if the result is E OTHER.
  - If the result is not E OTHER, it will be similar to the RESULT.
- STATUS % – The completion percentage.
4.  99 is considered complete.

The possible final status values for:

- Claim Billing Requests
- E PAYABLE, E REJECTED, E CAPTURED, E DUPLICATE, E UNSTRANDED, E OTHER
- Claim Reversals
- E REVERSAL ACCEPTED, E REVERSAL REJECTED, E REVERSAL UNSTRANDED, E REVERSAL OTHER
- Eligibility Verification
- E ELIGIBILITY ACCEPTED, E ELIGIBILITY REJECTED, E ELIGIBILITY UNSTRANDED, E REVERSAL OTHER
- Any Submission Type
- CORRUPT

#### \$\$NABP^BPSBUTL

This extrinsic function returns the Service Provider ID for the most recent NCPDP claim for the prescription and fill. Use of \$\$NABP^BPSBUTL is supported by Integration Agreement \#4719.

Input Parameters:

- RXP (required) – IEN in the PRESCRIPTION file \#52.
- BFILL (optional) – The fill number. If BFILL is omitted, the first fill is assumed.

Return Value:

- Returns the value of the Service Provider ID field (201-B1) for the latest NCPDP claim. This field will have the NPI number.

#### \$\$CLAIM^BPSBUTL

This extrinsic function API is used to retrieve the most recent ECME transaction, claim, and response information related to a specific prescription and fill. Use of \$\$CLAIM^BPSBUTL is supported by Integration Agreement \#4719.

Input Parameters:

- RXI (required) – Prescription IEN (Pointer to the PRESCRIPTION File \[#52\]).
- RXR (optional) – Fill Number (0 for Original, 1 for 1st refill, 2 for the 2nd refill, etc.). Default to the original fill (0), if not passed in.
- COB (optional) – COB Indicator (1: Primary, 2: Secondary, 3: Tertiary). Defaults to primary (1) if not passed in.

Return Value. A following string with the following pieces:

- 1 – BPS TRANSACTION file (#9002313.59) pointer.
- 2 – BPS CLAIMS file (#9002313.02) pointer for the most recent billing request.
- 3 – BPS RESPONSES file (#9002313.03) pointer associated with the billing request returned in piece 2.
- 4 – BPS CLAIMS file (#9002313.02) pointer for the reversal claim if it is the most recent claim.
- 5 – BPS RESPONSES file (#9002313.03) pointer associated with the reversal claim returned in piece 4.
- 6 – Prescription / Service Reference Number (ECME Number) of the most recent claim.

#### \$\$DIVNCPDP^BPSBUTL

This extrinsic function API returns the NCPDP and NPI numbers for a specific outpatient site. Use of \$\$DIVNCPDP^BPSBUTL is supported by Integration Agreement \#4719.

Input Parameters:

- BPSDIV (required) – Pointer to the Outpatient Site file, \#59.

Return Value:

- Returns the NCPDP and NPI numbers associated with the Outpatient Site.
- Returns NULL if the Outpatient Site is not passed in, or if the Outpatient Site is not linked to a BPS Pharmacy.

#### \$\$ADDCOMM^BPSBUTL

This extrinsic function API is used to pass comments that will be stored in the BPS TRANSACTION file (#9002313.59) and displayed in the ECME User Screen. Use of \$\$ADDCOMM^BPSBUTL is supported by Integration Agreement \#4719.

Input Parameters:

- BPRX (required) – Pointer to the PRESCRIPTION File \[#52\]).
- BPREF (optional) – Fill Number (0 for Original, 1 for 1st refill, 2 for the 2nd refill, etc.). If not passed in, it will default to the original fill.
- BPRCMNT (required) – Comment to be added.
- BPBKG (optional – Indicates if the API was called by a background process.
5.  If this parameter value is 1, then the comment is stored in BPS TRANSACTION (#9002313.59) file with POSTMASTER as the user entering the comment.

Return Value:

- Returns 1 if the comments were added successfully.
- Returns -1 if the comments were not added successfully.

#### \$\$AMT^BPSBUTL

This API returns the Gross Amount Due for the given Rx, Fill, and COB.

Input Parameters:

- RX (required) – This is a pointer to the Prescription file \#52.
- RFILL (optional) – This is the fill number of the prescription. Defaults to original fill if not passed.
- COB (optional) – This is the COB payer sequence number of the ECME bill. Defaults to 1 (primary) if not passed.

Return Values:

- \$\$AMT (optional) – The function value is the value of the Gross Amount Due field (#902.15) from the \#9002313.59902 subfile of the BPS Transaction file.

#### \$\$NFLDT^BPSBUTL

This API returns the Next Available Fill Date from BPS RESPONSES File \#9002313.03.

Input Parameters:

- RX (required) – Pointer to the Prescription file \#52.
- RFILL (required) – This is the fill number of the prescription.
- COB (optional) – This is the COB payer sequence number of the original bill. Defaults to 1 (primary) if not passed.

Return Values:

- \$\$NFLDT Next Available Fill Date.

#### \$\$BBILL^BPSBUTL

Back Bill indicator from BPS CLAIMS file \#9002313.02. Returns 1 if RX ACTION code of "BB", "P2”, or "P2S" is found. Otherwise returns 0.

Input Parameters:

- RX (optional) – This is a pointer to the Prescription file \#52.
- RFILL (optional) – Fill / refill number. Defaults to 0 (original fill) if not passed.
- COB (optional) – This is the COB payer sequence number of the original bill. Defaults to 1 (primary) if not passed.

Return Values:

- \$\$BBILL – Back Bill Indicator:

1 – Back Bill

0 – Not a Back Bill

#### \$\$ELIG ^BPSBUTL

This API returns the Eligibility for the given Rx, Fill and COB.

Input Parameters:

- RX (required) – This is the pointer to the Prescription file \#52.
- RFILL (optional) – Fill / Refill number. Defaults to 0 (original fill) if not passed.
- COB (optional) – This is the COB payer sequence number of the ECME bill. Defaults to 1 (primary) if not passed.

Return Values:

- \$\$ELIG the function value is the value of the Gross Amount Due field (#901.04) from the BPS Transaction file \#9002313.59.

#### IBSEND^BPSECMP2

This API is called by Outpatient Pharmacy and the API will then compile the information needed to create a BILLING event in Integrated Billing. Use of IBSEND^BPSECMP2 is supported by Integration Agreement \#4411 and is only available to Outpatient Pharmacy.

Input Parameters:

- CLAIMIEN (required) – IEN from BPS CLAIMS, \#9002313.02.
- RESPIEN (required) – IEN from BPS Response (required).
- EVENT (optional) – This is used by PSO to create specific events (BILL).
- USER (optional / required) – User who is creating the event. This is required when EVENT is sent.

Return Value:

- None.

#### \$\$ECMEON^BPSUTIL

This extrinsic function API indicates whether the ECME switch is on for an Outpatient Site (file \#59). Use of \$\$ECMEON^BPSUTIL is supported by Integration Agreement \#4410 and is only available to Outpatient Pharmacy and CMOP.

Input Parameters:

- Site (required) – Pointer to Outpatient Site, file \#59.

Return Value:

- Returns 1 if the ECME switch is on for the outpatient site, or 0 (zero) if the ECME switch is off.

#### \$\$CMOPON^BPSUTIL

This extrinsic function API indicates whether the CMOP switch is on for an Outpatient Site (file \#59). Use of \$\$CMOPON^BPSUTIL is supported by Integration Agreement \#4410 and is only available to Outpatient Pharmacy and CMOP.

Input Parameters:

- Site (required) – Pointer to Outpatient Site file, \#59.

Return Value:

- Returns 1 if the CMOP switch is on for the outpatient site and 0 (zero) if the CMOP switch is off.

#### \$\$BPSPLN^BPSUTIL

This extrinsic function returns the insurance PLAN NAME field (#902.24) value from the BPS TRANSACTION file (#9002313.59). Use of \$\$BPSLN^BPSUTIL is supported by Integration Agreement \#4410 and is only available to Outpatient Pharmacy and CMOP.

Input Parameters:

- RXI (required) – IEN of the PRESCRIPTION file (#52).
- RXR (optional) – Fill Number. Defaults to original fill (0) if not passed in.

Return Value:

- The insurance PLAN NAME field (#902.24) value for the related entry in the BPS TRANSACTION file.

#### \$\$CLMECME^BPSUTIL2

This extrinsic function returns the latest date of service for the prescription fill that matches the date of service returned by the payer. It uses the BPS LOG OF TRANSACTIONS file (#9002313.57) to find the date. The returned date is used to automatically match electronic payments to claims. Use of \$\$CLMECME^BPSUTIL2 is supported by Integration Agreement \#6028 and is only available to the Integrated Billing (IB) application.

Input Parameters:

- ECME (required) – The ECME number of the prescription for which a bill is sought.
- RCDATE (optional) – The date of service returned by the payer with the payment data.

Return Value:

- The alternate date of service returned based on claim data in BPS LOG OF TRANSACTIONS file (#9002313.57)*.* This date is the closest date of service for the fill that matches the payer-provided date of service.

#### \$\$VALECME^BPSUTIL2

This extrinsic function *returns whether an ECME number is valid or not*. Use of \$\$VALECME^BPSUTIL2 is supported by Integration Agreement \#6139 and is available to the Accounts Receivable and Integrated Billing (IB) applications.

Input Parameters:

- ECMENUM (required) – The ECME number to be validated.

Return Value:

0 – Indicates the ECME number passed in is INVALID.

1 – Indicates the ECME number passed in is VALID.

#### \$\$DUR1^BPSNCPD3

This API returns an array of data to Outpatient Pharmacy, which is used to populate the reject multiple of the Prescription file and is displayed in the Reject Information Screen of the Third Party Payer Rejects – Worklist and Third Party Payer Rejects – View / Process options. Primarily, it is data from the BPS Response file but also includes some BPS Claims and BPS Transaction data. The use of DUR1^BPSNCPD3 is supported by Integration Agreement \#4560 and is only available to Outpatient Pharmacy.

Input Parameters:

- BRXIEN (required) – IEN of the PRESCRIPTION file (#52).
- BFILL (required) – Fill Number.
- BPRXCOB (optional) – Coordination of Benefits indicator (1-Primary, 2-Secondary). If not passed in, primary is assumed.

Return Values:

- DUR (passed by reference) – Array of data, which primarily comes from the BPS Response file but also includes data from BPS Claims and BPS Transaction.
- ERROR (passed by reference) – Array of data that is only returned if the data could not be gathered.

#### \$\$DURESP^BPSNCPD3

This API returns an array of data to Outpatient Pharmacy, which is a subset of the data returned by DUR1. It is data from the BPS Response file that is primarily used to populate the display of the Additional Reject Information screen in the Third-Party Payer Rejects – Worklist and Third-Party Payer Rejects – View / Process options. The use of DURESP^BPSNCPD3 is supported by Integration Agreement \#4560 and is only available to Outpatient Pharmacy.

Input Parameters:

- DURIEN (required) – IEN of the BPS RESPONSE file (#9002313.03).
- BPRXCOB (optional) – Coordination of Benefits indicator (1-Primary, 2-Secondary). If not passed in, primary is assumed.

Return Values:

- DUR (passed by reference) – Array of data, which comes from the BPS Response file.

### Entry Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see the API section for callable entry points.

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- BPS AUTO CLOSE REJECT EC
- BPS AUTO CLOSE REJECT EXIT
- BPS AUTO CLOSE REJECT MENU
- BPS ECMECL1 NTE
- BPS ECMESV1 NTE
- BPS OPECC REJECT INFO MEDICATION PROFILE
- BPS OPECC REJECT INFO PATIENT INFORMATION
- BPS OPECC REJECT INFO VIEW RX
- BPS OPECC REJECT MENU
- BPS OPECC REJECT VIEW ECME RX
- BPS P1 EXIT
- BPS P2 CONTINUOUS
- BPS P2 UPDATE
- BPS P2 ZERO
- BPS PROTOCOL 2
- BPS PRTCL CMT ADD
- BPS PRTCL CMT ADD PHARM
- BPS PRTCL CMT EXIT
- BPS PRTCL CMT MENU
- BPS PRTCL ECME INFO REPORT
- BPS PRTCL ECME USRSCR
- BPS PRTCL IBCNR EDIT PLAN
- BPS PRTCL IBCNR GROUP PLAN MATCH
- BPS PRTCL IBCNR PLAN MATCH
- BPS PRTCL LOG MENU
- BPS PRTCL REOPEN
- BPS PRTCL REOPEN EXIT
- BPS PRTCL REOPEN MENU
- BPS PRTCL RSCH CLAIM TRACKING
- BPS PRTCL RSCH ELIG INQ
- BPS PRTCL RSCH EXIT
- BPS PRTCL RSCH GRPL
- BPS PRTCL RSCH HIDDEN ACTIONS
- BPS PRTCL RSCH IB EVENT REPORT
- BPS PRTCL RSCH MENU
- BPS PRTCL RSCH ON HOLD COPAY
- BPS PRTCL RSCH RELEASE COPAY
- BPS PRTCL RSCH TPJI
- BPS PRTCL RSCH VIEW ELIGIBILITY
- BPS PRTCL RSCH VIEW INSURANCE
- BPS PRTCL RSCH VIEW PRESCRIPTION
- BPS PRTCL UNSTRAND
- BPS PRTCL UNSTRAND ALL
- BPS PRTCL UNSTRAND EXIT
- BPS PRTCL UNSTRAND PRINT
- BPS PRTCL UNSTRAND SELECT
- BPS PRTCL USRSCR CHANGE VIEW
- BPS PRTCL USRSCR CLAIM LOG
- BPS PRTCL USRSCR CLOSE
- BPS PRTCL USRSCR COMMENT
- BPS PRTCL USRSCR CONTINUOUS
- BPS PRTCL USRSCR DEVELOPER LOG
- BPS PRTCL USRSCR EXIT
- BPS PRTCL USRSCR HIDDEN ACTIONS
- BPS PRTCL USRSCR OPECC REJECT INFORMATION
- BPS PRTCL USRSCR OPEN/CLOSE NON-BILLABLE ENTRY
- BPS PRTCL USRSCR PHARM WRKLST
- BPS PRTCL USRSCR REOPEN CLOSED CLAIMS
- BPS PRTCL USRSCR RESEARCH MENU
- BPS PRTCL USRSCR RESUB NO REVERSE
- BPS PRTCL USRSCR RESUBMIT
- BPS PRTCL USRSCR RESUBMIT EDITS
- BPS PRTCL USRSCR REVERSE
- BPS PRTCL USRSCR SORTLIST
- BPS PRTCL USRSCR UPDATE
- BPS VALM DOWN A LINE
- BPS VALM FIRST SCREEN
- BPS VALM GOTO PAGE
- BPS VALM LAST SCREEN
- BPS VALM NEXT SCREEN
- BPS VALM PREVIOUS SCREEN
- BPS VALM PRINT SCREEN
- BPS VALM UP ONE LINE
- BPS VIEW ECME RX MENU
- BPS VRX NAV BILL LIST
- BPS VRX NAV BILLING EVENTS RPT
- BPS VRX NAV CRI
- BPS VRX NAV DG ELIG STATUS
- BPS VRX NAV DG ELIG VERIFICATION
- BPS VRX NAV ECME CLAIM LOG
- BPS VRX NAV INS POL
- BPS VRX NAV MED PROFILE
- BPS VRX NAV PRINT REPORT
- BPS VRX NAV TPJI AR ACCT PROFILE
- BPS VRX NAV TPJI AR COMMENT HISTORY
- BPS VRX NAV TPJI CLAIM INFORMATION
- BPS VRX NAV TPJI ECME RX INFO
- BPS VRX NAV VIEWRX
- BPSJ MFN REGISTER1
- BPSJ PAYER INPUT
- BPSJ PAYER RESPONSE
- BPSJ REGISTER

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software packages must be installed prior to ECME V. 1.0 installation.

- Health Level Seven (HL7) V. 1.6
- Integrated Billing (IB) V. 2.0
- Kernel V. 8.0
- MailMan V. 8.0
- National Drug File (NDF) V. 4.0
- Outpatient Pharmacy V. 7.0
- Pharmacy Data Management V. 1.0
- VA FileMan V. 22.0
- Visit Tracking V. 2.0
- Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0

  IMPORTANT: If the site plans to utilize the CMOP functionality, then CMOP V. 2.0 must also be installed.

### Integration Agreements (INTEGRATION CONTROL REGISTRATIONS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

eClaims Management Engine V1.0 has Data Base Integration Control registrations (ICR) with the packages listed above, in addition to Registration (DG) and Scheduling (SD). For complete information regarding the ICRs for E Claims Management Engine V1.0, please refer to the INTEGRATION CONTROL REGISTRATIONS \[DBA IA ISC\] option under the DBA \[DBA\] option on FORUM.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the ECME V. 1.0 package options are designed to stand-alone.

## Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### SACC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SACC exemptions for this package.

### Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the more important namespace variables by the ECME V. 1.0 package. These variables are listed here for support purposes only and can change from version to version.

BPS Array Variables

The BPS array contains all the information needed to build a claim. This information comes primarily from two sources, IB / Insurance and Pharmacy data.

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements. No additional security measures are to be applied other than those implemented through Menu Manager and the package routines. No additional licenses are necessary to run the software. Confidentiality of staff and patient data and the monitoring of this confidentiality are no different than with any other paper reference.

## Mail Groups and Mail Messages (Bulletins)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three mail groups in ECME.

- The mail group BPS OPECC should contain members who will monitor the ECME process.
- The mail group BPS TRICARE should contain members who will monitor the TRICARE process.
- The mail group BPS CHAMPVA should contain members who will monitor the CHAMPVA process.

There are seven MailMan messages (bulletins) sent by ECME.

- If an ECME transaction is missing the insurance information necessary to process the claim, an email bulletin will be sent to the BPS OPECC mail group before the claim processing terminates.
- The Auto-Reversal Process will send an email to the BPS OPECC mail group with a list of ECME claims that were auto-reversed.
- The VA SITE CONTACT in the BPS SETUP table will be notified of any difficulties encountered during the registration process.
- If a Veteran RX / fill cannot be queued for processing, an email is sent to the BPS OPECC mail group.
- If a TRICARE RX / fill cannot be queued for processing, an email is sent to the BPS TRICARE mail group.
- If a CHAMPVA RX / fill cannot be queued for processing, an email is sent to the BPS CHAMPVA mail group
- If a primary claim is closed by an Rx Return to Stock, an Rx Delete, or an Inpatient Auto Reversal and there is an open secondary claim, a bulletin will be sent to the BPS OPECC mail group so they can manually reverse (if needed) and close the secondary claim.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECME transmits prescription claims and eligibility verification requests to third-party payers via the Austin Information Technology Center (AITC) and the clearinghouse Emdeon via HL7. The claims messages sent and received must comply with the NCPDP V. D.0 Telecommunications Standard. The data on the claims transactions are controlled by fields defined on the payer sheets, which are created by the third-party payer. Generally, the data may include patient, insurance, provider, and prescription data. The payer response will include whether the claim was paid or rejected and possibly Drug Utilization Response (DUR) information. The number of transactions will vary depending on the frequency of prescriptions created at a site and how many of those claims can be third-party billed. The data is not encrypted between VistA and the AITC, which is inside the VA firewall.

ECME transmits registration data to the AITC via HL7. The registration data includes the site data (site number, site contacts, and site contact means) and pharmacy data (pharmacy contacts and contact means, NCPDP, pharmacy DEA, and lead pharmacist data). The AITC returns acknowledgement messages for each registration message it receives. There is a nightly job, which, if scheduled properly, will register the site and pharmacy once every day. The data is also sent if the user requests it via the Register Pharmacy with AITC option \[BPS SETUP REGISTER PHAMACY\]. The data is not encrypted between VistA and the AITC, which is inside the VA firewall.

ECME receives payer sheet table updates from the AITC via HL7. The payer sheet data is stored in the BPS NCPDP FORMATS table (#9002313.92). VistA will return acknowledgement messages for every table update it receives. Currently, the AITC updates the database about once a week and any updates will then be sent to the VistA sites. The data is not encrypted between VistA and the AITC, which is inside the VA firewall.

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At present, the ECME V. 1.0 package does not provide for the archiving of its data.

### Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BPS Nightly Background Job, which should be scheduled to run nightly, will purge data older than 365 days from the BPS LOG (#9002313.12) file.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a system failure occurs, check for stranded submissions via the View / Unstrand Submissions Not Completed option \[BPS UNSTRAND SCREEN\]. If any stranded submissions are found, unstrand them and reprocess them via the ECME User Screen option.

6.  Requests stranded in a 'Transmitting' state most likely indicate that there is a problem with HL7 processing at the site or at the AITC. If there is an HL7 problem and it is resolved, the submissions will transmit normally, and no other effort is needed. Only if it is verified that there is not an HL7 problem, then submissions in this state should be unstranded.

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specialized products embedded within or required by the ECME package.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no electronic signatures required by the ECME package.

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[BPSMENU\]

The complete list of ECME V. 1.0 menu options is shown below. The Claims Coordinator needs to access all ECME V. 1.0 options.

Key To view the complete ECME V. 1.0 menu structure, the user must hold the BPSMENU, BPS USER, BPS MANAGER, BPS MASTER, BPS REPORTS, and BPS SUPERVISOR keys.

| Option Name                    | Menu Text                                       |
|--------------------------------|-------------------------------------------------|
| BPS MANAGER MENU               | Pharmacy ECME Manager Menu                      |
| BPS STATS SCREEN               | Statistics Screen                               |
| BPS MENU MAINTENANCE           | ECME transaction maintenance options            |
| BPS MENU RPT CLAIM STATUS      | Claim Results and Status                        |
| BPS MENU RPT MAIN              | Pharmacy Electronic Claims Reports              |
| BPS MENU RPT OTHER             | Other Reports                                   |
| BPS COB MENU                   | ECME Pharmacy COB                               |
| BPS COB PROCESS SECOND TRICARE | Process Secondary / TRICARE Rx to ECME          |
| BPS COB RPT SECONDARY CLAIMS   | Potential Secondary Rx Claims Report            |
| BPS POTENTIAL CLAIMS RPT DUAL  | Potential Claims Report for Dual Eligible       |
| BPS NIGHTLY BACKGROUND JOB     | BPS Nightly Background Job                      |
| BPS RPT RECENT TRANSACTIONS    | Recent Transactions                             |
| BPS RPT CLOSED CLAIMS          | Closed Claims Report                            |
| BPS RPT CMOP/ECME ACTIVITY     | CMOP / ECME Activity Report                     |
| BPS RPT ERRONEOUS REV          | List Possible Erroneous Reversals               |
| BPS RPT NOT RELEASED           | Claims Submitted, Not Yet Released              |
| BPS RPT PAYABLE                | Payable Claims Report                           |
| BPS RPT PAYER SHEET DETAIL     | Payer Sheet Detail Report                       |
| BPS RPT REJECTION              | Rejected Claims Report                          |
| BPS RPT REVERSAL               | Reversal Claims Report                          |
| BPS RPT TOTALS BY DAY          | Totals by Date                                  |
| BPS SETUP MENU                 | Pharmacy ECME Setup Menu                        |
| BPS SETUP BASIC PARAMS         | Edit Basic Pharmacy ECME Parameters             |
| BPS RPT SETUP PHARMACIES       | ECME Setup – Pharmacies Report                  |
| BPS SETUP PHARMACY             | Edit Pharmacy ECME Pharmacy Data                |
| BPS SETUP REGISTER PHARMACY    | Register Pharmacy with Austin Automation Center |
| BPS RPT TURNAROUND STATS       | Turn-around time statistics                     |
| BPS UNSTRAND SCREEN            | View / Unstrand Submissions Not Completed       |
| BPS USER SCREEN                | Claims Data Entry Screen                        |
| BPSMENU                        | ECME                                            |
| BPS RPT CLAIMS RESPONSE        | ECME Claims-Response Inquiry                    |
| BPS RPT NON-BILLABLE REPORT    | Non-Billable Status Report                      |
| BPS RPT SPENDING ACCOUNT       | Spending Account Report                         |
| BPS RPT VIEW ECME RX           | View ePharmacy Rx                               |
| BPS OPECC PRODUCTIVITY REPORT  | OPECC Productivity Report                       |
| BPS RPT DUPLICATE CLAIMS       | Duplicate Claims Report                         |
| BPS RPT ERRORS                 | ePharmacy Bills Created with Errors             |

<span id="_Toc192072578" class="anchor"></span>Table 10: Security Keys

Example: How to View the Exported Options Using VA FileMan

VA FileMan 22.0

Select OPTION: 5 INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: OPTION// \<Enter\>

Select OPTION NAME: BPSMENU ECME

ANOTHER ONE: \<Enter\>

STANDARD CAPTIONED OUTPUT? Yes// \<Enter\> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// \<Enter\> - No record number (IEN), no Computed

Fields

DISPLAY AUDIT TRAIL? No// \<Enter\> NO

NAME: BPSMENU MENU TEXT: ECME

TYPE: menu CREATOR: ECMEuser,One

LOCK: BPSMENU PACKAGE: IHS PHARMACY POINT OF SALE

E ACTION PRESENT: YES HEADER PRESENT?: YES

DESCRIPTION: The main menu

ITEM: BPS MANAGER MENU SYNONYM: MGR

DISPLAY ORDER: 2

ITEM: BPS USER SCREEN SYNONYM: U

DISPLAY ORDER: 1

ITEM: BPS MENU RPT MAIN SYNONYM: RPT

DISPLAY ORDER: 4

ENTRY ACTION: K BPSQUIT D INIT^BPSMHDR I \$G(BPSQUIT) K BPSQUIT S XQUIT=1

HEADER: D HDR^BPSMHDR TIMESTAMP: 60116,62862

TIMESTAMP OF PRIMARY MENU: 60044,54655

UPPERCASE MENU TEXT: ECME

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc192072579" class="anchor"></span>Table 11: Acronyms and Abbreviations</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BPSMENU</td>
<td>Required for accessing the main ECME menu [BPSMENU].</td>
</tr>
<tr class="even">
<td>BPS USER</td>
<td><ul>
<li><blockquote>
<p>Required for accessing the ECME User’s Screen [BPS USER SCREEN]</p>
</blockquote></li>
<li><blockquote>
<p>Required for accessing the option Process Secondary/TRICARE Rx to ECME [BPS COB PROCESS SECOND TRICARE]</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>BPS MANAGER</td>
<td><p>Required for accessing the following ECME options:</p>
<ul>
<li><blockquote>
<p>Pharmacy ECME Manager Menu [BPS MANAGER MENU]</p>
</blockquote></li>
<li><blockquote>
<p>Statistics Screen [BPS STATISTICS SCREEN]</p>
</blockquote></li>
<li><blockquote>
<p>ECME transaction maintenance options [BPS MENU MAINTENANCE]</p>
</blockquote></li>
<li><blockquote>
<p>View/Unstrand Submissions Not Completed [BPS UNSTRAND SCREEN]</p>
</blockquote></li>
<li><blockquote>
<p>Re Open CLOSED Claims [BPS REOPEN CLOSED CLAIMS]</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>BPS MASTER</td>
<td><p>Required for accessing the following ECME options:</p>
<ul>
<li><blockquote>
<p>Pharmacy ECME Setup Menu [BPS SETUP MENU]</p>
</blockquote></li>
<li><blockquote>
<p>Edit Basic Pharmacy ECME Parameters [BPS SETUP BASIC PARAMS]</p>
</blockquote></li>
<li><blockquote>
<p>Edit ECME Pharmacy Data [BPS SETUP PHARMACY]</p>
</blockquote></li>
<li><blockquote>
<p>Register Pharmacy with Austin Automation Center [BPS SETUP REGISTER PHARMACY]</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>BPS REPORTS</td>
<td><p>Required for accessing the following ECME options:</p>
<ul>
<li><blockquote>
<p>Pharmacy Electronic Claims Reports [BPS MENU RPT MAIN]</p>
</blockquote></li>
<li><blockquote>
<p>Claim Results and Status [BPS MENU RPT CLAIM STATUS]</p>
</blockquote></li>
<li><blockquote>
<p>Recent Transactions [BPS RPT RECENT TRANSACTIONS]</p>
</blockquote></li>
<li><blockquote>
<p>Closed Claims Report [BPS RPT CLOSED CLAIMS]</p>
</blockquote></li>
<li><blockquote>
<p>CMOP/ECME Activity Report [BPS RPT CMOP/ECME ACTIVITY]</p>
</blockquote></li>
<li><blockquote>
<p>Claims Submitted, Not Yet Released [BPS RPT NOT RELEASED]</p>
</blockquote></li>
<li><blockquote>
<p>Payable Claims Report [BPS RPT PAYABLE]</p>
</blockquote></li>
<li><blockquote>
<p>Payer Sheet Detail Report [BPS RPT PAYER SHEET DETAIL]</p>
</blockquote></li>
<li><blockquote>
<p>Rejected Claims Report [BPS RPT REJECTION]</p>
</blockquote></li>
<li><blockquote>
<p>Reversal Claims Report [BPS RPT REVERSAL]</p>
</blockquote></li>
<li><blockquote>
<p>Totals by Date [BPS RPT TOTALS BY DAY]</p>
</blockquote></li>
<li><blockquote>
<p>Turn-around time statistics [BPS RPT TURNAROUND STATS]</p>
</blockquote></li>
<li><blockquote>
<p>ECME Setup – Pharmacies Report [BPS RPT SETUP PHARMACIES]</p>
</blockquote></li>
<li><blockquote>
<p>Spending Account Report [BPS RPT SPENDING ACCOUNT].</p>
</blockquote></li>
<li><blockquote>
<p>ECME Claims-Response Inquiry [BPS RPT CLAIMS RESPONSE]</p>
</blockquote></li>
<li><blockquote>
<p>Non-Billable Status Report [BPS RPT NON-BILLABLE REPORT]</p>
</blockquote></li>
<li><blockquote>
<p>Duplicate Claims Report [BPS RPT DUPLICATE CLAIMS]</p>
</blockquote></li>
<li><blockquote>
<p>ePharmacy Bills Created with Errors [BPS RPT ERRORS]</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>BPS SUPERVISOR</td>
<td><p>Required for this ECME option:</p>
<ul>
<li><blockquote>
<p>OPECC Productivity Report [BPS OPECC PRODUCTIVITY REPORT</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc192072579" class="anchor"></span>Table 11: Acronyms and Abbreviations

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All ECME V. 1.0 related files – BPS CLAIMS file (#9002313.02) through BPS SETUP file (#9002313.99) – have Audit (AUDIT), Data Dictionary (DD), Delete (DEL), Learn As You Go (LAYGO), and Write (WR) access codes of “@” and Read (RD) access codes of “Pp.”

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA Software Document Library
REDACTED
VA Software Document Library – Electronic Claims Management Engine (ECME)
REDACTED
NCPDP HIPAA Transactions documentation
REDACTED
HIPAA NCPDP Connection for EDI Pharmacy (Active Release)
REDACTED
NCPDP Basic Guide to Standards
REDACTED

## Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECME software is subject to VHA directive 2004-038 which forbids the local modification of Class I software.

## Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions and explanations for terms and acronyms relevant to the content presented within this document. For additional terms and acronyms, include references to other VA acronyms and glossary repositories (e.g., VA Acronym Lookup and OIT Master Glossary).

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym or Term</th>
<th>Definition / Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Administrative Code Sets</td>
<td>Code sets that characterize a general business situation rather than a medical condition or service.</td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td>Automated Data Processing Application Coordinator</td>
</tr>
<tr class="odd">
<td>AHA</td>
<td>American Hospital Association</td>
</tr>
<tr class="even">
<td>AITC</td>
<td>Austin Information Technology Center, formerly known as the Austin Automation Center (AAC).</td>
</tr>
<tr class="odd">
<td>AMA</td>
<td>American Medical Association – A professional association that represents the voice of the American medical profession and constitutes the partnership of physicians and physician’s professional associations dedicated to promoting the art and science of medicine and the betterment of public health.</td>
</tr>
<tr class="even">
<td>ANS</td>
<td>American National Standards – Standards developed and approved by organizations accredited by ANSI.</td>
</tr>
<tr class="odd">
<td>ANSI</td>
<td>American National Standards Institute – An organization that accredits various standards-setting committees, and monitors compliance with the open rule-making process that must be followed to qualify for ANSI accreditation.</td>
</tr>
<tr class="even">
<td>API</td>
<td>Application Programmer Interface</td>
</tr>
<tr class="odd">
<td>A/S</td>
<td>Administrative Simplification – Title II, Subtitle F, of HIPAA, which gives the Department Of Health And Human Services (DHHS) the authority to mandate the use of standards for the electronic exchange of health care data; to specify what medical and administrative code sets should be used within those standards; to require the use of national identification systems for health care patients, providers, payers (or plans), and employers (or sponsors); and to specify the types of measures required to protect the security and privacy of personally identifiable health care information.</td>
</tr>
<tr class="even">
<td>ASC</td>
<td>Accredited Standards Committee – An organization that has been accredited by American National Standards Institute (ANSI) for the development of American National Standards.</td>
</tr>
<tr class="odd">
<td>ASTM</td>
<td>American Society for Testing and Materials – A standards group that has published general guidelines for the development of standards, including those for health care identifiers.</td>
</tr>
<tr class="even">
<td>Back Door</td>
<td>System access via the roll and scroll, character, and Mumps based VistA application.</td>
</tr>
<tr class="odd">
<td>BCBSA</td>
<td>Blue Cross and Blue Shield Association – An association that represents the common interest of Blue Cross and Blue Shield health plans. The BCBSA maintains the Claim Adjustment Reason Codes code set.</td>
</tr>
<tr class="even">
<td>Business Model</td>
<td>A model of a business organization or process.</td>
</tr>
<tr class="odd">
<td>CBO</td>
<td>Central Business Office</td>
</tr>
<tr class="even">
<td>CDC</td>
<td>Centers for Disease Control</td>
</tr>
<tr class="odd">
<td>CHAMPVA Patient</td>
<td>A CHAMPVA patient is a patient that has CHAMPVA coverage only. The CHAMPVA insurance will be billed for the prescription. Generally, if the CHAMPVA insurance rejects the claim, then the medication will NOT be released to the patient.</td>
</tr>
<tr class="even">
<td>Clean Claim</td>
<td>An insurance claim that has no defect, impropriety (including any lack of any substantial documentation) or circumstance requiring special treatment that prevents timely payment from being made.</td>
</tr>
<tr class="odd">
<td>Clearinghouse (or Health Care Clearinghouse)</td>
<td>For health care, an organization that translates health care data to or from a standard format.</td>
</tr>
<tr class="even">
<td>CMOP</td>
<td>Consolidated Mail Outpatient Pharmacy</td>
</tr>
<tr class="odd">
<td>CMS</td>
<td>Centers for Medicare &amp; Medicaid Services – formerly Health Care Financing Administration (HCFA). The administration within HHS that is responsible for the national administration of the Medicaid and Medicare programs.</td>
</tr>
<tr class="even">
<td>CMS-1450</td>
<td>CMS’s name for the institutional uniform claim form, or UB-04.</td>
</tr>
<tr class="odd">
<td>CMS-1500</td>
<td>CMS’s name for the professional uniform claim form.</td>
</tr>
<tr class="even">
<td>COB</td>
<td>Coordination of Benefits – A provision that is intended to avoid claims payment delays and duplication of benefits when a person is covered by two or more plans providing benefits or services for medical, dental, or other care or treatment.</td>
</tr>
<tr class="odd">
<td>Code Set</td>
<td>Under HIPAA "codes used to encode data elements, tables of terms, medical concepts, diagnostic codes, or medical procedures. A code set includes the codes and descriptors of the codes." [45 CFR 162.103].</td>
</tr>
<tr class="even">
<td>Covered Entity</td>
<td>Under HIPAA, a health plan, healthcare clearinghouse or health care provider who transmits information in electronic form in connection with a transaction covered by this subchapter 160.103 of 45 CFR.</td>
</tr>
<tr class="odd">
<td>Current Procedural Terminology</td>
<td>A procedure code set maintained and copyrighted by the AMA and that has been selected for use under HIPAA for non-institutional and non-dental professional transactions.</td>
</tr>
<tr class="even">
<td>Data Element</td>
<td>Under HIPAA, this is "…the smallest named unit of information in a transaction." [45 CFR 162.103].</td>
</tr>
<tr class="odd">
<td>Data Mapping</td>
<td>The process of matching one set of data elements or individual code values to the closest equivalents in another set of them.</td>
</tr>
<tr class="even">
<td>Data Model</td>
<td>A conceptual model of the information needed to support a business function or process.</td>
</tr>
<tr class="odd">
<td>Data Set</td>
<td>Under HIPAA, this is "…a semantically meaningful unit of information exchanged between two parties to a transaction." [45 CFR 162.103].</td>
</tr>
<tr class="even">
<td>DAW</td>
<td>Dispense As Written</td>
</tr>
<tr class="odd">
<td>DD</td>
<td>Data Dictionary – A document or system that characterizes the data content of a system.</td>
</tr>
<tr class="even">
<td>DEA</td>
<td>Drug Enforcement Administration</td>
</tr>
<tr class="odd">
<td>Designated Code Set</td>
<td>A medical or administrative code set, which DHHS has designated for use in one or more of the HIPAA standards.</td>
</tr>
<tr class="even">
<td>Designated Data Content Committee or Designated DCC</td>
<td>An organization, which DHHS has designated for oversight of the business data content of one or more of the HIPAA-mandated transaction standards.</td>
</tr>
<tr class="odd">
<td>Designated Standard</td>
<td>A standard that DHHS has designated for use under the authority provided by HIPAA.</td>
</tr>
<tr class="even">
<td>DHCP</td>
<td>Decentralized Hospital Computer Program</td>
</tr>
<tr class="odd">
<td>DHHS or HHS</td>
<td>Department of Health and Human Services</td>
</tr>
<tr class="even">
<td>Dismissed</td>
<td>The ECME function of removing (not physically deleting) patient entries and / or prescriptions from viewing on the Claims Data Entry Screen.</td>
</tr>
<tr class="odd">
<td>DUR</td>
<td>Drug Utilization Response</td>
</tr>
<tr class="even">
<td>ECME</td>
<td>Electronic Claims Management Engine</td>
</tr>
<tr class="odd">
<td>EComm</td>
<td>Electronic Commerce – The exchange of business information by electronic means.</td>
</tr>
<tr class="even">
<td>EDI</td>
<td>Electronic Data Interchange – The transfer of data between different companies using networks, such as the Internet. As more and more companies are connected to the Internet, EDI is becoming increasingly important as an industry standard for companies to buy, sell, and trade information. ANSI has approved a set of EDI standards known as the X12 standards.</td>
</tr>
<tr class="odd">
<td>EKG</td>
<td>Electrocardiogram</td>
</tr>
<tr class="even">
<td>Finish</td>
<td>Term used for completing orders from Order Entry / Results Reporting V. 3.0.</td>
</tr>
<tr class="odd">
<td>‘Finish’ a Prescription</td>
<td>This process within VistA Outpatient Pharmacy V. 7.0 where a pharmacy prescription order has been reviewed by either a pharmacy technician or pharmacist and is the first step in processing a prescription in Pharmacy. If performed by a pharmacist with the appropriate security key, the prescription can be ‘Verified’ as well. See ‘Verify a Prescription’ for more information.</td>
</tr>
<tr class="even">
<td>Flat File</td>
<td>This term usually refers to a file that consists of a series of plain text records.</td>
</tr>
<tr class="odd">
<td>Front Door</td>
<td>System access via the Delphi, Graphical User Interface (GUI) based VistA application.</td>
</tr>
<tr class="even">
<td>FSC</td>
<td>Financial Services Center</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface – A graphical method of controlling how a user interacts with a computer to perform various tasks.</td>
</tr>
<tr class="even">
<td>HCPCS</td>
<td>HCFA Common Procedural Coding System – A medical code set that identifies health care procedures, equipment, and supplies for claim submission purposes. It is maintained by Health Care Financing Administration (HCFA), and has been selected for use in the HIPAA transactions. HCPCS Level I contain numeric CPT-4 codes, which are maintained by the AMA. HCPCS Level II contains alphanumeric codes used to identify various items and services that are not included in the CPT-4 code set. These are maintained by HCFA, BCBSA, and Health Insurance Association of America (HIAA). HCPCS Level III contains alphanumeric codes that are assigned by Medicaid State agencies to identify additional items and services not included in levels I and II. These are usually called "local codes”, and must have "W", "X", "Y", or "Z" in the first position. These codes are not named as HIPAA standard codes. HCPCS Procedure Modifier Codes can be used with all three levels, with the WA-ZY range used for locally assigned procedure modifiers.</td>
</tr>
<tr class="odd">
<td>Health Care Clearinghouse</td>
<td><p>Under HIPAA, this is "… a public or private entity that does either of the following processes or facilitates the processing of information received from another entity in a nonstandard format or containing nonstandard data content into standard data elements or a standard transaction.</p>
<p>Or receives a standard transaction from another entity and processes or facilitates the processing of [that] information into nonstandard format or nonstandard data content for a receiving entity." [45 CFR 160.103].</p></td>
</tr>
<tr class="even">
<td>Health Care Provider</td>
<td>Under HIPAA, this is "…a provider of services as defined in the section 1861(u) of the [Social Security] Act, 42 USC 1395x(u), a provider of medical or other health services as defined in section 1861(s) of the Act, 42 USC 1395(s), and any other person or organization who furnishes, bills, or is paid for health care in the normal course of business." [45 CFR 160.103]</td>
</tr>
<tr class="odd">
<td>Health Information</td>
<td>Under HIPAA this is "… any information, whether oral or recorded in any form or medium that (a)is created or received by a health care provider, health plan, public health authority, employer, life insurer, school or university, or health care clearinghouse, and (b) related to the past, present or future physical or mental health or condition of an individual, the provision of health care to an individual, or the past, present or future payment for the provision of health care to an individual." [45 CFR 160.103].</td>
</tr>
<tr class="even">
<td>Health Plan</td>
<td>Under HIPAA this is "…an individual or group plan that provides, or pay the cost of, medical care”. [45 CFR 160.103].</td>
</tr>
<tr class="odd">
<td>HFMA</td>
<td>Healthcare Financial Management Association – An organization for the improvement of the financial management of healthcare-related organizations. The HFMA sponsors some HIPAA educational seminars.</td>
</tr>
<tr class="even">
<td>HIAA</td>
<td>Health Insurance Association of America – An industry association that represents the interests of commercial health care insurers. The HIAA participates in the maintenance of some code sets, including HCPCS Level II codes.</td>
</tr>
<tr class="odd">
<td>HIPAA</td>
<td>Health Insurance Portability and Accountability Act of 1996 – A Federal law that makes several changes that have the goal of allowing persons to qualify immediately for comparable health insurance coverage when changing employment relationships. Title II, Subtitle F, of HIPAA gives HHS the authority to mandate the use of standards for the electronic exchange of health care data; to specify what medical and administrative code sets should be used within those standards; to require the use of national identification systems for health care patients, providers, payers (or plans), and employers (or sponsors); and to specify the types of measures required to protect the security and privacy of personally identifiable health care information. Also known as the Kennedy-Kassebaum Bill, the Kassebaum-Kennedy Bill, K2, or Public Law 104-191.</td>
</tr>
<tr class="even">
<td>HIPAA Data Dictionary or HIPAA DD</td>
<td>A data dictionary that defines and cross-references the contents of all X12 transactions included in the HIPAA mandate. It is maintained by X12N/TG3.</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>Health Level Seven – An ANSI-accredited group that defines standards for the cross-platform exchange of information within a health care organization. HL7 is responsible for specifying the Level Seven Open System Interconnection (OSI) standards for the health industry. Some HL7 standards will be encapsulated in the X12 standards used for transmitting claim attachments.</td>
</tr>
<tr class="even">
<td>HMO</td>
<td>Health Maintenance Organization</td>
</tr>
<tr class="odd">
<td>HSD&amp;D</td>
<td>Health Systems Design &amp; Development</td>
</tr>
<tr class="even">
<td>IB</td>
<td>Integrated Billing</td>
</tr>
<tr class="odd">
<td>ICD</td>
<td>International Classification of Diseases – A medical code set maintained by the World Health Organization (WHO). The primary purpose of this code set is to classify causes of death. A United States (US) extension of this coding system, maintained by the National Center for Health Statistics (NCHS) within the Centers for Disease Control (CDC), is used to identify morbidity factors, or diagnoses. The ICD-9-CM (Revision 9 Clinical Modification) codes have been selected for use in the HIPAA transactions.</td>
</tr>
<tr class="even">
<td>IG</td>
<td>Implementation Guide – A document explaining the proper use of a standard for a specific business purpose. The X12N HIPAA IGs are the primary reference documents used by those implementing the associated transactions and are incorporated into the HIPAA regulations by reference.</td>
</tr>
<tr class="odd">
<td>IHS</td>
<td>Indian Health Service</td>
</tr>
<tr class="even">
<td>Implementation Specification</td>
<td>Under HIPAA, this is "… the specific instructions for implementing a standard”. [45 CFR 160.103].</td>
</tr>
<tr class="odd">
<td>Information Model</td>
<td>A conceptual model of the information needed to support a business function or process.</td>
</tr>
<tr class="even">
<td>IRMS</td>
<td>Information Resources Management Service</td>
</tr>
<tr class="odd">
<td>ISO</td>
<td>International Standards Organization or International Organization for Standardization - An organization that coordinates the development and adoption of numerous international standards.</td>
</tr>
<tr class="even">
<td>J-Codes</td>
<td>Previously HCPCS Level II has contained a set of codes with a high-order value of "J" to identify some drugs and some other items. The final HIPAA transactions and code set rule states that any J-codes identifying drugs will be dropped from the HCPCS and NDC codes will be used to identify all drug products.</td>
</tr>
<tr class="odd">
<td>JCAHO</td>
<td>Joint Commission on Accreditation of Healthcare Organizations - In the future, the JCAHO may play a role in certifying these organizations compliance with the HIPAA A/S requirements.</td>
</tr>
<tr class="even">
<td>Maintain or Maintenance</td>
<td>Under HIPAA, this is "…activities necessary to support the use of a standard adopted by the Secretary, including technical corrections to an implementation specification, and enhancements or expansion of a code set. This term excludes the activities related to the adoption of a new standard or implementation specification, or modification to an adopted standard or implementation specification." [45 CFR 162.103].</td>
</tr>
<tr class="odd">
<td>Maximum Defined Data Set</td>
<td>Under HIPAA, this is "… all of the required data elements for a particular standard based on a specific implementation specification." [45 CFR 162.103]. A framework under HIPAA whereby an entity creating a transaction is free to include whatever data any receiver might want or need. The recipient of a maximum data set is free to ignore any portion of the data not needed to conduct the part of the associated business transaction, unless the nonessential data is needed for coordination of benefits.</td>
</tr>
<tr class="even">
<td>Medical Code Sets</td>
<td>Codes that characterize a medical condition or treatment. The code sets are usually maintained by professional societies and public health organizations.</td>
</tr>
<tr class="odd">
<td>Modify or Modification</td>
<td>Under HIPAA, refers to "a change adopted by the Secretary, through regulation, to a standard or an implementation specification." [45 CFR 160.102]</td>
</tr>
<tr class="even">
<td>MOU</td>
<td>Memorandum of Understanding – A document providing a general description of the kinds of responsibilities that are to be assumed by two or more parties in pursuit of some goal(s). Information that is more specific may be provided in an associated Statement Of Work (SOW).</td>
</tr>
<tr class="odd">
<td>NABP #</td>
<td>National Association of Boards of Pharmacy number. This term is obsolete; it has been superseded by the NCPDP number.</td>
</tr>
<tr class="even">
<td>National Employer ID</td>
<td>A system for uniquely identifying all sponsors of health care benefits.</td>
</tr>
<tr class="odd">
<td>National Patient ID</td>
<td>A system for uniquely identifying all recipients of health care services.</td>
</tr>
<tr class="even">
<td>National Payer ID</td>
<td>A system for uniquely identifying all organizations that pays for health care services. Also known as Health Plan ID or Plan ID.</td>
</tr>
<tr class="odd">
<td>National Provider Registry</td>
<td>The organization envisioned for assigning the National Provider IDs.</td>
</tr>
<tr class="even">
<td>NCHS</td>
<td>National Center for Health Statistics – An administration of HHS and CDC that oversees ICD coding.</td>
</tr>
<tr class="odd">
<td>NCPDP</td>
<td>National Council for Prescription Drug Programs – An ANSI-accredited group that maintains several standard formats for use by the retail pharmacy industry, some of which are included in the HIPAA mandates.</td>
</tr>
<tr class="even">
<td>NCPDP Batch Standard</td>
<td>An NCPDP standard designed for use by low-volume dispensers of pharmaceuticals, such as nursing homes. Version 1.0 of this standard has been mandated under HIPAA.</td>
</tr>
<tr class="odd">
<td>NCPDP Telecommunication Standards</td>
<td>An NCPDP standard designed for use by high-volume dispensers of pharmaceuticals, such as retail pharmacies. Version D.0 is one of the transaction standards under HIPAA</td>
</tr>
<tr class="even">
<td>NDC</td>
<td>National Drug Code – A medical code set that has been selected for use in the HIPAA transactions.</td>
</tr>
<tr class="odd">
<td>NDF</td>
<td>National Drug File</td>
</tr>
<tr class="even">
<td>NOI</td>
<td>Notice of Intent – A document that describes a subject area for which the Federal Government is considering developing regulations. It may describe what the government considers to be the relevant considerations and invite comments from interested parties. These comments can then be used in developing a Notice of Proposed Rulemaking (NPRM) or a final regulation.</td>
</tr>
<tr class="odd">
<td>Non-Formulary Drugs</td>
<td>The medications, which are defined as commercially available drug products not included in the VA National Formulary.</td>
</tr>
<tr class="even">
<td>NPF</td>
<td>National Provider File – The database envisioned for use in maintaining a national provider registry.</td>
</tr>
<tr class="odd">
<td>NPI</td>
<td>National Provider Identifier – A system for uniquely identifying all providers of health care services, supplies, and equipment.</td>
</tr>
<tr class="even">
<td>NPRM</td>
<td>Notice of Proposed Rulemaking – A document that describes and explains regulations that the Federal Government proposes to adopt at some future date, and invites interested parties to submit comments related to them. These comments can then be used in developing the final rules.</td>
</tr>
<tr class="odd">
<td>NPS</td>
<td>National Provider System – The administrative system envisioned for supporting a national provider registry.</td>
</tr>
<tr class="even">
<td>NSF</td>
<td>National Standard Format – Generically, this applies to any national standard format, but it is often used in a more limited way to designate the Professional EMC NSF, a 320-byte flat file record format used to submit professional claims.</td>
</tr>
<tr class="odd">
<td>NUBC</td>
<td>National Uniform Billing Committee – The committee established by the American Hospital Association (AHA) to develop a single billing form and standard data set that could be used nationwide by institutional providers and payers for handling health care claims.</td>
</tr>
<tr class="even">
<td>OIT</td>
<td>Office of Information and Technology</td>
</tr>
<tr class="odd">
<td>OMB</td>
<td>Office of Management &amp; Budget – A Federal Government agency that has a major role in reviewing proposed Federal regulations.</td>
</tr>
<tr class="even">
<td>Orderable Item</td>
<td>An Orderable Item name and dosage form that has no strength attached to it (e.g., Acetaminophen). The name with a strength attached is the Dispense Drug name (e.g., Acetaminophen 325mg).</td>
</tr>
<tr class="odd">
<td>OSI</td>
<td>Open System Interconnection – A multi-layer ISO data communications standard. Level Seven of this standard is industry-specific, and HL7 is responsible for specifying the level seven OSI standards for the health industry.</td>
</tr>
<tr class="even">
<td>Payer</td>
<td>In health care, an entity that assumes the risk of paying for medical treatments. This can be an uninsured patient, a self-insured employer, or a health care plan or Health Maintenance Organization (HMO).</td>
</tr>
<tr class="odd">
<td>PAYERID</td>
<td>HCFA’s term for the National Payer ID initiative.</td>
</tr>
<tr class="even">
<td>Payer Sheet</td>
<td>Entries in BPS NCPDP FORMATS (#9002313.92) are commonly referred to as "payer sheets."</td>
</tr>
<tr class="odd">
<td>PDM</td>
<td>Pharmacy Data Management</td>
</tr>
<tr class="even">
<td>Placeholders</td>
<td>Physical and / or logical data elements that are referenced and placed within a data structure that have a data definition but may or may not currently exist within the system. The value of these data elements is not currently maintained by the software but are established for future iterations of system development related to Billing Aware.</td>
</tr>
<tr class="odd">
<td>POS</td>
<td>Point of Sale</td>
</tr>
<tr class="even">
<td>Potentially Billable Event</td>
<td>A service, which has all required data elements associated with it. These data elements are collected in the VistA Clinical Application.</td>
</tr>
<tr class="odd">
<td>Professional Component</td>
<td>Charges for physician services. Examples include physician who reads the Electrocardiogram (EKG) and an Emergency Room physician who provides treatment.</td>
</tr>
<tr class="even">
<td>Provider Taxonomy Codes</td>
<td>A code set for identifying the provider type and area of specialization for all health care providers. A given provider can have several Provider Taxonomy Codes. The BCBSA maintains this code set.</td>
</tr>
<tr class="odd">
<td>RPCH</td>
<td>Regional Primary Care Hospital</td>
</tr>
<tr class="even">
<td>Secretary</td>
<td>Under HIPAA, this refers to the Secretary of the US Department of Health and Human Services or his/her designated representatives. [45 CFR 160.103].</td>
</tr>
<tr class="odd">
<td>Segment</td>
<td>Under HIPAA, this is "…a group of related data elements in a transaction”. [45 CFR 162.103].</td>
</tr>
<tr class="even">
<td>Service</td>
<td>Medical care and items such as medical diagnosis and treatment, drugs and biologicals, supplies, appliances, and equipment, medical social services, and use of hospital Regional Primary Care Hospital (RPCH) or Skilled Nursing Facility (SNF) facilities.</td>
</tr>
<tr class="odd">
<td>SNF</td>
<td>Skilled Nursing Facility</td>
</tr>
<tr class="even">
<td>SOW</td>
<td>Statement of Work – A document describing the specific tasks and methodologies that will be followed to satisfy the requirements of an associated contract or MOU.</td>
</tr>
<tr class="odd">
<td>SSO</td>
<td>Standard Setting Organization – Under HIPAA, this is "…an organization accredited by ANSI that develops and maintains standards for information transactions or data elements, or any other standard that is necessary for, or will facilitate the implementation of this part." [45 CFR 160.103].</td>
</tr>
<tr class="even">
<td>Standard</td>
<td>Under HIPAA, this is "… a prescribed set of rules, conditions, or requirements describing the following information for products, systems, services, or practices (1) Classification of components, (2) Specification of Materials, performance, or operations, (3) Delineation of procedures. [45 CFR 160.103]</td>
</tr>
<tr class="odd">
<td>Standard Transaction</td>
<td>Under HIPAA, this is "… a transaction that complies with the applicable standard adopted under this part." [45 CFR 162.103].</td>
</tr>
<tr class="even">
<td>Third (3rd) Party Claims</td>
<td>Health care insurance claims submitted to an entity for reimbursement of health care bills.</td>
</tr>
<tr class="odd">
<td>TPA</td>
<td>Third Party Administrator – An entity that processes health care claims and performs related business functions for a health plan.</td>
</tr>
<tr class="even">
<td>Transaction</td>
<td>Under HIPAA, this is "…the exchange of information between two parties to carry out financial or administrative activities related to health care." [45 CFR 160.103].</td>
</tr>
<tr class="odd">
<td>TRICARE Patient</td>
<td>A TRICARE patient is a patient that has TRICARE coverage. The TRICARE insurance will be billed for the prescription. Generally, if the TRICARE insurance rejects the claim, then the medication will NOT be released to the patient.</td>
</tr>
<tr class="even">
<td>UB-04</td>
<td>A uniform institutional claim form developed by the National Uniform Billing Committee (NUBC) that has been in use since 1993.</td>
</tr>
<tr class="odd">
<td>Unstructured Data</td>
<td>This term usually refers to data that is represented as free-form text, as an image, etc., where it is not practical to predict exactly what data will appear where.</td>
</tr>
<tr class="even">
<td>‘Verify’ a Prescription</td>
<td>After a prescription order has been ‘Finished’ the prescription must be ‘Verified’ by an authorized VistA user, through the administration of the system security key SOP. This is a critical step in the process of generating an electronic claim.</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture Acronym for Veterans Health Information Systems and Technology Architecture, the new name for Decentralized Hospital Computer Program (DHCP).</td>
</tr>
<tr class="odd">
<td>WEDI</td>
<td>Workgroup for Electronic Data Interchange - A health care industry group that lobbied for HIPAA A/S, and that has a formal consultative role under the HIPAA legislation.</td>
</tr>
<tr class="even">
<td>WHO</td>
<td>World Health Organization</td>
</tr>
</tbody>
</table>