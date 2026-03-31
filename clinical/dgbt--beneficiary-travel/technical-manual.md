---
title: Beneficiary Travel Version 1 Technical Manual (Updated with DGBT*1*41)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: (Updated with DGBT*1*41)
app_code: DGBT
app_name: Beneficiary Travel
section: CLI
app_status: active
pkg_ns: DGBT
patch_ver: 1
patch_id: DGBT*1
group_key: "DGBT:DGBT:1"
file_numbers: []
security_keys: []
menu_options: 4
description: The Indianapolis VAMC developed the Class 3 web-based Beneficiary Travel (BT) Dashboard to assist users in making faster, more accurate decisions on mileage reimbursement for travel claims. The VHA Chief Business Office requested the BT Dashboard package be implemented as part of the Cost Efficiency
audience: 
keywords: 
  - travel
  - table
  - contents
  - beneficiary
  - class
  - dashboard
  - package
  - dgbt
  - claims
  - patient
page_count: 0
word_count: 6095
section_count: 27
table_count: 1
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: February 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt_1_41_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt_1_41_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=123"
---

![](beneficiary-travel-version-1-technical-manual-updated-with-dgbt-1-41/001.png)

Beneficiary Travel

Technical Manual

February 2024

Beneficiary Travel Patch DGBT\*1\*41

Office of Information and Technology (OIT)

Product Development

Revision History

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Change</th>
<th>Page</th>
<th>Date</th>
<th>Tech Writer,<br />
Project Manager</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DGBT*1*41</p>
<p>Removed decommissioned functions</p></td>
<td>Page 13</td>
<td>February 2024</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td><p>DGBT*1*40</p>
<p>Removed notes on decommissioned functions.</p></td>
<td><p>Page 4</p>
<p>Page 5</p>
<p>Page 13</p></td>
<td>December 2023</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>DGBT*1*32 – Two-factor authentication (2FA)</td>
<td>Page 29</td>
<td>October 2018</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td><p>DGBT*1*29 Informational Patch –</p>
<ul>
<li><p>EAS*1*113 – BT BULLETIN</p></li>
<li><p>EAS BT CLAIMS PROCESSING Bulletin</p></li>
<li><p>BT CLAIMS PROCESSING Mail Group</p></li>
</ul></td>
<td><p>Page 23</p>
<p>Page 23</p>
<p>Page 24</p></td>
<td>November 2015</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td><p>Patch 21 removed Distance Enter/Edit menu option from the Beneficiary Travel Menu.</p>
<ul>
<li><p>Removed Distance Enter/Edit menu option from the Dashboard Configuration section.</p></li>
<li><p>Removed Distance Enter/Edit menu option from the Menu Options section.</p></li>
</ul></td>
<td><p>Page 8</p>
<p>Page <a href="#remote-procedure-calls-rpcs">7</a></p></td>
<td>December, 2013</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>Removed Report of Claim Amounts from Sub Menu and added it to Main Menu. Added DGBT BENE TRAVEL REPORT, and removed DGBT BENE TRAVEL CLAIM AMT RPT.</td>
<td></td>
<td>February, 2013</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td><p>Incorporated changes identified by Cindy Heuer during HPS review on 01/14/2013.</p>
<ul>
<li><p>Removed track changes comments</p></li>
<li><p>Updated revision history</p></li>
<li><p>Added updates highlights to document</p></li>
<li><p>Changed month and year on cover page</p></li>
<li><p>Changed DGBTEDIT DENIAL LTRS to DGBT EDIT DENIAL LTRS in page 9.</p></li>
<li><p>Corrected font size and formatting on section <strong>DEDUCTIBLE PAID</strong>, “INPUT PARAMETER” in page 20.</p></li>
<li><p>Removed comments and changed the word Templates to Template in page 20.</p></li>
</ul>
<blockquote>
<p>In the list of FileMan Access codes,</p>
</blockquote>
<ul>
<li><p>file 392.6’s name should be BENEFICIARY TRAVEL DENIAL LETTERS (rather than BT Denial Letters).</p></li>
<li><p>file 392.7’s name should be BENEFICIARY TRAVEL BT Alternate Income Enter/Edit (rather than BT Deductible Waiver).</p></li>
<li><p>file 392.8’s name should be BENEFICIARY TRAVEL DENIAL REASONS (rather than BT Denial Reasons).</p></li>
<li><p>file 392.9’s name should be BT PATIENT ALTERNATE INCOME (rather than BT Patient Alternate In). </p></li>
<li><p>file 392.42’s name should be BT SPECIAL MODE OF TRANSPORTATION (rather than BT Special Mode of Trans).</p></li>
</ul></td>
<td></td>
<td>January, 2013</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>Accepted changes made by Cindy Heuer from HPS on 11/30/2012</td>
<td></td>
<td>December 2012</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td><p>BT Enhancement Changes: Patch DGBT_1*20.</p>
<ul>
<li><p>Add list of enhancements</p></li>
<li><p>Updated list of Called routines</p></li>
<li><p>Various structural changes including moving XINDEX and List File Attributes material to the Routines section and the Routines section entirely</p></li>
<li><p>Updated MAS Parameters List</p></li>
<li><p>Updated Security Key List</p></li>
<li><p>Updated Glossary</p></li>
<li><p>Removed Appendix A, VADPT Variables and inserted reference to separate VADPT documentation</p></li>
</ul></td>
<td><p>Page 1</p>
<p>Page 10</p>
<p>Pages 10-11</p>
<p>Page 13</p>
<p>Page 13</p>
<p>Page 23</p>
<p>Page 25</p></td>
<td>August 2012</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>Patch DGBT_1*19</td>
<td></td>
<td>July 2012</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Added a statement about BT Dashboard to the Introduction</p></li>
</ul></td>
<td>Page <a href="#introduction">1</a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Added statement about BT Dashboard to Namespace and Conventions</p></li>
</ul></td>
<td>Page <a href="#namespace-and-conventions">3</a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Added BT Dashboard to Parameter Rates Enter/Edit</p></li>
</ul></td>
<td>Page <a href="#bene-travel-account-file-setup">4</a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Added section: BT Dashboard Configuration</p></li>
<li><p>Added information about zeroing out Default Mileage</p></li>
</ul></td>
<td>Page <a href="#_Ref322937682"><span id="_Ref322937682" class="anchor"></span>iii</a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Added two BT Dashboard file numbers to File List</p></li>
</ul></td>
<td>Page <a href="#file-list">11</a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Added RPC Broker to External/Internal Relations</p></li>
</ul></td>
<td>Page <a href="#externalinternal-relations">16</a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Added two BT Dashboard file numbers to FileMan Access Codes</p></li>
</ul></td>
<td>Page <a href="#_Ref322937755">18</a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Updated Glossary</p></li>
</ul></td>
<td>Page <a href="#glossary">21</a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Added section: Appendix B Beneficiary Travel Dashboard</p></li>
</ul></td>
<td>Page <a href="#appendix-a-beneficiary-travel-dashboard">23</a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patch 14, 15 (ability to change rates removed)</td>
<td>Page <a href="\l">7</a></td>
<td>February 2008</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>Originally released</td>
<td></td>
<td>April 2002</td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Orientation](#orientation)
- [General Information](#general-information)
  - [Namespace and Conventions](#namespace-and-conventions)
  - [Integrity Checker](#integrity-checker)
  - [SACC Exemptions/Non-Standard Code](#sacc-exemptionsnon-standard-code)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Bene Travel Account File Setup](#bene-travel-account-file-setup)
  - [BT Certifying Official](#bt-certifying-official)
  - [COREFLS active](#corefls-active)
  - [BT Other Expenses Asked](#bt-other-expenses-asked)
  - [VA FileMan 22.0](#va-fileman-220)
- [Routines](#routines)
  - [Routines to Map](#routines-to-map)
  - [Called Routines](#called-routines)
    - [VAUTOMA](#vautoma)
    - [VADATE](#vadate)
    - [VALM1](#valm1)
  - [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
  - [Routine List](#routine-list)
- [XINDEX](#xindex)
- [List File Attributes](#list-file-attributes)
- [Files](#files)
  - [Globals and Files](#globals-and-files)
  - [File List](#file-list)
  - [Security Key List](#security-key-list)
- [Menu Options](#menu-options)
- [Generate Online Documentation](#generate-online-documentation)
  - [Menu Diagrams](#menu-diagrams)
  - [Exported Protocols](#exported-protocols)
  - [Exported Options](#exported-options)
  - [Exported List Templates](#exported-list-templates)
- [Archiving and Purging](#archiving-and-purging)
- [External/Internal Relations](#externalinternal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Security](#security)
  - [Security Keys](#security-keys)
  - [FileMan Access Codes](#fileman-access-codes)
- [EAS\1\113 - BT BULLETIN](#eas1113-bt-bulletin)
  - [EAS BT CLAIMS PROCESSING Bulletin](#eas-bt-claims-processing-bulletin)
  - [BT CLAIMS PROCESSING Mail Group](#bt-claims-processing-mail-group)
- [Glossary](#glossary)
- [Appendix A Beneficiary Travel Dashboard](#appendix-a-beneficiary-travel-dashboard)
  - [Introduction](#introduction-1)
  - [Process Flowchart of Operations](#process-flowchart-of-operations)
  - [Web and Operating System Components](#web-and-operating-system-components)
    - [Access to the Web Application](#access-to-the-web-application)
    - [Security for the Web Application](#security-for-the-web-application)
    - [.XML File](#xml-file)
The Beneficiary Travel options provide the ability to perform the functions involved in issuing beneficiary travel pay. Travel reimbursement is provided to specified categories of eligible veterans. Issuance of travel pay to the veterans in some of these categories is subject to a deductible per visit and per month. The deduction requirement may be waived for any veteran who meets specific criteria subject to the approval of the local medical center director or designee. Some of the categories have income limitations. An income certification form is completed and signed yearly by the veteran. Cash reimbursement is paid on VAF 70-3542d, Voucher for Cash Reimbursement of Beneficiary Travel Expenses.
Non-employee attendants who are eligible for travel reimbursement will be issued travel pay under the veteran's name in the computer.
Payment for travel by special mode (ambulance, hired car, handicapped van, etc.) may be authorized if medically necessary and approved BEFORE travel begins. Exception to this would be in cases of medical emergency where delay would be hazardous to life or health.
For claims with an account type of ALL OTHER, the system will compute the amount payable from factors such as account type, parameter set up of deductible amount per visit and per month, one-way or round-trip mileage, and applied costs. The amount payable for claims with an account type of C&P will also be computed by the system.
The Beneficiary Travel Dashboard (BT Dashboard) web application was released in 2012 as an accessory to the existing VistA Beneficiary Travel application. Travel clerks use BT Dashboard concurrently with the VistA BT claims functionality, usually on side-by-side screens, to calculate mileage with Bing™ Maps.
The Beneficiary Travel Enhancement Project (BT Enhancement) added several new features:
- Special Mode Trip Tracking
- Support for Common Carrier as a means of transportation
- Alternate POW and Hardship processing
- Manual waiver processing
- Automatic eligibility determination
- Automatic generation of denial of benefits letters
- The ability to edit the denial letter template (requires the user to have the new DGBT EDIT DENIAL LTRS security key)
- Improved trip tracking
- Automatic deductible zeroing for qualified veterans
- Sharing of claim data from other sites
- Enhanced reporting, including on-demand and queued reports

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the technical manual for the Beneficiary Travel software package. It is designed to provide necessary information for use in the technical operation of the Beneficiary Travel software product. The technical manual is intended for use by technical computer personnel and not the typical end user.

# General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Namespace and Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace assigned to Beneficiary Travel is DGBT. Beneficiary Travel Dashboard includes web components as well as operating system configuration.

The namespace for the Beneficiary Travel Dashboard package, classes, and Cache Server Pages (CSP) files is DGBT.

## Integrity Checker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Beneficiary Travel uses KIDS integrity checker. Under the installation option of the Kernel Installation Distribution System menu, select Verify Checksums in Transport Global to ensure that the routines are correct.

## SACC Exemptions/Non-Standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SACC exemptions/non-standard code in the Beneficiary Travel package.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Beneficiary Travel package may be tailored specifically to meet the needs of the various sites.

## Bene Travel Account File Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of patch DGBT\*1.0\*20 the following rules must be followed for entries in Beneficiary Travel Account file 392.3:

A. Sites must deactivate all accounts for mileage claims that are not of Type 4 (ALL OTHER) or Type 5 (C&P). Or, if the site wishes to keep any of the accounts with types other than 4 or 5 active, they can change that account type to 4 or 5. A site can have more than one account of type 4 or type 5, but the default will be the first active account type of 4 (ALL OTHER).
B. A site can have only one active special mode account type (Type 3). It must contain the exact text “SPECIAL MODE – NON-EMERGEN” in the text of the .01 ACCOUNT field. A 3-digit account code can precede or follow the required text. All other Type 3 entries must be deactivated.

## BT Certifying Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the name of the official which will appear on all VA Forms 70-3542d, Cash Reimbursement of Beneficiary Travel Expenses. If this field is left blank, the user's name will be printed followed by DESIGNEE OF CERTIFYING OFFICIAL.

## COREFLS active

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field determines if the Beneficiary Travel software uses vendors/carriers from the nationally held database of venders (COREFLS). In order for this field to be turned on, the CoreFLS package (CSL) must be installed in your system. By default this is set to NO and no editing is allowed, the software uses the vendor/carriers from the VENDOR file (#440).

## BT Other Expenses Asked

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is used to determine if the MEALS & LODGING and FERRY, BRIDGES, ETC. prompts will be asked in the Beneficiary Travel Claim Enter/Edit option. YES or NO.

Example

BT CERTIFYING OFFICIAL: BTOFFICIAL,ONE MAS

COREFLS ACTIVE: NO// (No Editing)

BT OTHER EXPENSES ASKED: YESNOTE: Some sites use the value in the FISCAL SYMBOLS field of the rates record for printing on the forms or reports. If your site requires this information, use the following FileMan instructions to update this field in the current rates record. Under direction of the Chief Business Office, do not change any of the other rate record fields.

## VA FileMan 22.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PATIENT TEAM ASSIGNMENT// 43.1 MAS EVENT RATES

(8 entries)

EDIT WHICH FIELD: ALL// FISCAL SYMBOLS

THEN EDIT FIELD:

Select MAS EVENT RATES DATE: 020108 FEB 01, 2008

FISCAL SYMBOLS: \<enter symbol for your site here\>

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Beneficiary Travel routines recommended for mapping.

## Called Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VADATE Generic Date Routine

VADPT Obtain Patient Information

VAUTOMA Generic One, Many, All Routine

VALM1 Returns the current date and time

Please refer to VADPT documentation for further information.

### VAUTOMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAUTOMA is a routine which will do a one/many/all prompt - returning the chosen values in a subscripted variable specified by the calling programmer.

Input variables:

> VAUTSTR string which describes what is to be entered.

> VAUTNI defines if array is sorted alphabetically or numerically.

> VAUTVB name of the subscripted variable to be returned.

> VAUTNALL define this variable if you do not want the user to be given the ALL option.

> Other variables as required by a call to ^DIC (see VA FileMan Programmers Manual).

Output variables:

> As defined in VAUTVB

### VADATE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VADATE is called it creates an array containing the current date in internal (FileMan) format and external VA-approved format.

### VALM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALM1 is called at the NOW^VALM1 which returns the current date and time in external VA-approved format.

## Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following RPCs are called by Beneficiary Travel Dashboard:

- VST1^ORWCV – gets list of visits/appointments when the travel clerk selects a new patient
- CONTEXT^TIUSRVLO – gets list of TIU notes when the travel clerk selects a new patient
- LIST^ORQQCN – gets list of consults when the travel clerk selects a new patient
- AGET^ORWORR – gets list of orders when travel clerk selects a new patient

  The following RPC is called by the Beneficiary Travel Package to retrieve the number of claims and amount of deductible paid by a patient during the current month:

RPC name in Remote Procedure file: DGBT CLAIM DEDUCTIBLE PAID

INPUT PARAMETER: PATIENT ICN

DESCRIPTION: PATIENTS ICN NUMBER FROM ^DPT(DFN).

INPUT PARAMETER: CLAIM DATE

DESCRIPTION: BENEFICIARY TRAVEL CLAIM DATE (NOT THE CURRENT DATE)

INPUT PARAMETER: DGBTRET

DESCRIPTION: The variable the return information will be returned in.

This invokes RPC^DGBTRDV to get any claim information, for the current patient at all sites visited during the current month.

The RPC retrieves a list treating facilities from file 391.91 and checks if the treatment date occurred during the current month. If the treatment date is within the current month then the RPC retrieves the number of trips, both one way and round trip, the amount of any deductible paid and/or whether the patient has a manual waiver at that site.

The following RPC Broker API is called at the remote facility to invoke the above BT RPC:

RPC Name in Remote Procedure file: XWB REMOTE RPC

D EN1^XWB2HL7(.DGBTRET,DGBTIEN,DGBTRPC,"",DGBTICN,DGBTDTI)

Variables passed in:

DGBTRET – Array name the remote site information is returned in.

DGBTIEN - The patients internal entry number from the ^DPT – the patient file.

DGBTRPC - The name of the RPC to use at the remote site.

DGBTICN - The patients ICN (Integration Control Number)

DGBTDTI - The claim date at the site making the request.

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain a listing of the routines contained in the Beneficiary Travel package.

1)  Programmer Options Menu
2)  Routine Tools Menu
3)  First Line Routine Print Option
4)  Routine Selector: DGBT\*

# XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to V*ist*A Programming Standards. The XINDEX output may include the following components: compiled list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from V*ist*A Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the Beneficiary Travel package, specify the following namespaces at the "routine(s)?\>" prompt: DGBT\*.

Beneficiary Travel initialization routines which reside in the UCI in which XINDEX is being run, compiled template routines, and local routines found within the Beneficiary Travel namespace can be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).

# List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

FileMan also provides additional display options, including custom tailored output that can be specified by the user.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Globals and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main global used in the Beneficiary Travel package is ^DGBT. Journaling of the ^DGBT global is mandatory.

The MAS EVENT RATE file and MAS PARAMETERS file belong to the Registration package and contain fields granting ownership to the Beneficiary Travel package.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following MAS Parameters file affects how Beneficiary Travel performs. For detailed information on each parameter, see the Beneficiary Travel User Guide.

FILE FILE

<u>NUMBER</u> <u>NAME</u> <u>GLOBAL</u>

43 MAS PARAMETERS ^DG(43,Field Field \#

BT CERTIFYING OFFICIAL (#720)

BT OTHER EXPENSES ASKED (#721)

USE TEMPORARY ADDRESS (#722)

43.1 MAS EVENT RATES ^DG(43.1,Field Field \#

DEDUCTIBLE/VISIT (#30.01)

DEDUCTIBLE/MONTH (#30.02)

MILEAGE RATE (#30.03)

FISCAL SYMBOLS (#30.04)

C&P REVIEW VISIT MILEAGE RATE (#30.05)

## Security Key List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DGBT EDIT DENIAL LTRS

DESCRIPTIVE NAME: NEEDED TO EDIT DENIAL LETTERS

PERSON LOOKUP: LOOKUP

DESCRIPTION: The Holder of this key will be allowed to edit the denial letter

templates.

DGBT LOCAL VENDOR

> DESCRIPTION: This key allows users to add a CoreFLS vendor from the

Nationally held database into the site's Local Vendor file (#392.31).

DGBT SUPERVISOR

DESCRIPTION: This key is to be given to MAS Supervisors to restrict access

to some of the Beneficiary Travel Options.

# Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main menu for Beneficiary travel is:

Beneficiary Travel Menu \[DGBT BENE TRAVEL MENU\]

Options included on the menu are:

| Option Name Displayed  | Option Name            | Security Key |
|----------------------------|----------------------------|------------------|
| Report of Claim Amounts    | DGBT BENE TRAVEL REPORT    |                  |
| View of Claim              | DGBT BENE TRAVEL VIEW      |                  |
| Beneficiary Travel Reports | DGBT TRAVEL REPORTS Menu   |                  |
| Summary Report             | DGBT SUMMARY REPORT        |                  |
| Audit Report               | DGBT AUDIT REPORT          |                  |
| Clerk Report               | DGBT CLERK REPORT          |                  |
| Travel Pattern Report      | DGBT TRAVEL PATTERN REPORT |                  |
| Special Mode Report        | DGBT SPECIAL MODE REPORT   |                  |
| Fiscal Report              | DGBT FISCAL REPORT         |                  |

# Generate Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain information about menus, exported protocols, exported options, and exported list templates concerning the Beneficiary Travel package.

## Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Programmers Options
2.  Menu Management
3.  Display Menus and Options Menu
4.  Diagram Menus
5.  Select User or Option Name: O.DGBT BENE TRAVEL MENU

## Exported Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VA FileMan Menu
2.  Print File Entries Option
3.  Output from what File: PROTOCOL
4.  Sort by: Name
5.  Start with name: DGBT to DGBTZ
6.  Within name, sort by: \<RET\>
7.  First print field: Name

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VA FileMan Menu
2.  Print File Entries Option
3.  Output from what File: OPTION
4.  Sort by: Name
5.  Start with name: DGBT to DGBTZ
6.  Within name, sort by: \<RET\>
7.  First print field: Name

## Exported List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VA FileMan Menu
2.  Print File Entries Option
3.  Output from what File: LIST TEMPLATE
4.  Sort by: Name
5.  Start with name: DGBT to DGBTZ
6.  Within name, sort by: \<RET\>
7.  First print field: Name

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving and purging capabilities connected to the Beneficiary Travel package.

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Minimums of VA FileMan V. 22.0, Kernel V. 8.0, Remote Procedure Call (RPC) Broker V.1.1, and PIMS V. 5.3 are required to run this package.

DBIA Agreements

The following are the steps you may take to obtain the database integration agreements for the Beneficiary Travel package.

DBIA Agreements - Custodial Package

1.  FORUM
2.  DBA Menu
3.  Integration Agreements Menu
4.  Custodial Package Menu
5.  Active by Custodial Package Option
6.  Select Package Name: Beneficiary Travel

DBIA Agreements - Subscriber Package

1.  FORUM
2.  DBA Menu
3.  Integration Agreements Menu
4.  Subscriber Package Menu
5.  Print Active by Subscriber Package Option
6.  Start with subscriber package: Beneficiary Travel

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the Beneficiary Travel package.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain information about the security keys contained in the Beneficiary Travel package.

1.  VA FileMan Menu
2.  Print File Entries Option
3.  Output from what File: SECURITY KEY
4.  Sort by: Name
5.  Start with name: DGBT to DGBTZ
6.  Within name, sort by: \<RET\>
7.  First print field: Name
8.  Then print field: Description

<span id="_Ref322937755" class="anchor"></span>

## FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of recommended FileMan Access Codes associated with each file contained in the Beneficiary Travel package. This list may be used to assist in assigning users appropriate FileMan Access Codes.

FILE FILE DD RD WR DEL LAYGO

<u>NUMBER</u> <u>NAME</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u>

43\*\* MAS PARAMETERS @ d D @ @

43.1\*\* MAS EVENT RATES @ d D D D

392 BENEFICIARY TRAVEL CLAIM @ d @ @ @

392.1 BENEFICIARY TRAVEL @ d D D D

DISTANCE

392.2 BENEFICIARY TRAVEL @ d D D D

CERTIFICATION

392.3 BENEFICIARY TRAVEL @ d @ @ @

ACCOUNT

392.4 BENEFICIARY TRAVEL MODE @ d D @ D

OF TRANSPORTATION

392.5 BENEFICIARY TRAVEL @ d D @ D  
DASHBOARD CONFIG

392.51 BENEFICIARY TRAVEL @ d @ @ @  
DASHBOARD AUDIT

392.15 BT REMOTE CLAIM CHECK @ d D @ D

392.31 LOCAL VENDOR @ d D @ D

392.41 BT CLAIM ELIGIBILITY CODE @ d D @ D

392.42 BT SPECIAL MODE OF @ d D @ D

TRANSPORTATION

392.6 BENEFICIARY TRAVEL DENIAL @ d D @ D

LETTERS

392.7 BENEFICIARY TRAVEL MANUAL @ d D @ D

DEDUCTIBLE WAIVER

392.8 BENEFICIARY TRAVEL DENIAL @ d D @ D

REASONS

392.9 BT PATIENT ALTERNATE INCOME @ d D @ D

\*\* Files owned by the Registration package contain fields belonging to the Beneficiary Travel package.

# EAS\*1\*113 - BT BULLETIN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the installation of EAS\*1\*113; a BT CLAIMS PROCESSING Mail group will be automatically created in VistA to receive a new BT Bulletin named EAS BT CLAIMS PROCESSING. Users who validate BT eligibility based on income or process BT claims should be added to the mail group.

When an IVM converted/reversal income test is received from ES, a check will be done to see if the BT Financial Indicator is different than the BT Financial Indicator on file (e.g. the new Financial Indicator is 1 (YES) and the BT Financial Indicator on File is 0 (No),or the new status is 0 (NO) and the BT Financial Indicator on File is 1 (Yes) or a null). If the BT Financial Indicator has changed, a bulletin will be sent to the BT CLAIMS PROCESSING Mail group.

The ES HL7 ORU-Z06 message sends the BT Financial Indicator (BTFI) to VistA in the ZMT-31 segment-sequence. The BTFI will be stored to the BT FINANCIAL INDICATOR (#4) field of the ANNUAL MEANS TEST (#408.31) file.

The BT Financial Indicator may be viewed on the Means Test or RX Copay Test summary screen using the View a Past Means Test \[DG MEANS TEST VIEW TEST\] or View a Past Copay Test \[DG CO-PAY TEST VIEW TEST\] options respectively.

## EAS BT CLAIMS PROCESSING Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EAS BT CLAIMS PROCESSING bulletin was created with the release of EAS\*1\*113.

NAME: EAS BT CLAIMS PROCESSING

SUBJECT: IVM - Beneficiary Travel Financial Indicator UPLOAD FOR \|10\|

RETENTION DAYS: 7 PRIORITY?: NO

MESSAGE:

An Income Verification Match verified Beneficiary Travel Information has been uploaded for the following patient.

Patient Name: \|1\|

Last 4 of SSN: \|2\|

ICN: \|3\|

DFN: \|4\|

STATION NUMBER: \|5\|

Prev Category: \|6\|

New Category: \|7\|

Date of Test: \|8\|

Income Year of Conversion: \|9\|

MAIL GROUP: BT CLAIMS PROCESSING

DESCRIPTION: The VistA System will trigger a BT Bulletin so that the

appropriate VistA staff will be notified of a change in the BT Financial

Indicator. A bulletin will be triggered in VistA and sent to the BT Claims

Processing mail group when there is a change to the BT Financial Indicator

received from the Enrollment System.

PARAMETER: 1

PARAMETER: 2

PARAMETER: 3

PARAMETER: 4

PARAMETER: 5

PARAMETER: 6

## BT CLAIMS PROCESSING Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BT CLAIMS PROCESSING mail group was created with the release of EAS\*1\*113. Users who validate BT eligibility based on income or process BT claims should be added to the mail group.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A&amp;A</td>
<td>Aid and Attendance</td>
</tr>
<tr class="even">
<td>Beneficiary</td>
<td><p>The party to whom the mileage reimbursement is owed. In most cases, the beneficiary is the same as the patient.</p>
<p>There are some exceptions. For instance, when the patient is under anesthesia and the caretaker presents the appointment documentation to the Travel Office.</p></td>
</tr>
<tr class="odd">
<td>Bing™ Maps API</td>
<td><p>Microsoft 3rd party application used with BT Dashboard. Bing Maps provides directions, mileage, and a visual map for the travel office personnel to use when determining the correct mileage between the beneficiary’s home and the treating VHA facility</p>
<p>Also provides the Application Programming Interface (API)</p></td>
</tr>
<tr class="even">
<td>BT</td>
<td>Beneficiary Travel</td>
</tr>
<tr class="odd">
<td>BTD</td>
<td>Beneficiary Travel Dashboard</td>
</tr>
<tr class="even">
<td>CBO</td>
<td>Chief Business Office</td>
</tr>
<tr class="odd">
<td>Class 1</td>
<td>Software produced and supported inside of the Product Development (PD) organization</td>
</tr>
<tr class="even">
<td>Class 3</td>
<td><p>Also known as Field Developed Software</p>
<p>Refers to all VHA software produced and supported outside of the Product Development (PD) organization</p></td>
</tr>
<tr class="odd">
<td>C&amp;P</td>
<td>Compensation &amp; Pension</td>
</tr>
<tr class="even">
<td>Consults</td>
<td><p>Consultations are used by care providers (doctors, nurses, pharmacists, and therapists, as well as their Clerical Staff) to make or service requests for consults on patients</p>
<p>Examples of Consults are: Radiology exams, appointment with a Social Worker, a request for a vision exam, etc.</p></td>
</tr>
<tr class="odd">
<td>CSP</td>
<td>Cache Server Pages</td>
</tr>
<tr class="even">
<td>Gateway</td>
<td><p>Gateway is a computer system that transfers data between normally incompatible applications or networks or which allows users of one system or network to gain access to another network or system</p>
<p>Also, provides protocol translations as needed</p></td>
</tr>
<tr class="odd">
<td>CSP Gateway</td>
<td>Caché Server Pages (CSP) technology allows you to build and deploy Web applications. CSP lets you dynamically generate Web pages, typically using data from a Caché database. These pages are dynamic; that is, the same page may deliver different content each time it is requested</td>
</tr>
<tr class="even">
<td>GUI</td>
<td>Graphical User Interface</td>
</tr>
<tr class="odd">
<td>InterSystems</td>
<td>The 3rd party vendor that provides a product known as InterSystems Cache</td>
</tr>
<tr class="even">
<td>KIDS</td>
<td>Kernel Installation and Distribution System</td>
</tr>
<tr class="odd">
<td>MAS</td>
<td>Medical Administration Service</td>
</tr>
<tr class="even">
<td>MT</td>
<td>Means Test</td>
</tr>
<tr class="odd">
<td>OIG</td>
<td>Office of Inspector General</td>
</tr>
<tr class="even">
<td>PIMS</td>
<td>Patient Information Management System</td>
</tr>
<tr class="odd">
<td>REST-API</td>
<td><p>The Bing™ Maps REST Services Application Programming Interface is a Representational State Transfer (REST) API used to find an address, retrieve a map with a pushpin, and a label, or get driving directions.</p>
<p>Users do these tasks by constructing a URL.</p></td>
</tr>
<tr class="even">
<td>Rx</td>
<td>Prescription</td>
</tr>
<tr class="odd">
<td>SACC</td>
<td>Standards and Conventions Committee</td>
</tr>
<tr class="even">
<td>SC%</td>
<td>Service Connected disability % determines the amount of VA benefits for which a veteran qualifies based on a service-connected injury(ies) or illness(es).</td>
</tr>
<tr class="odd">
<td>Section 508</td>
<td>A Public Law that agencies must provide employees and members of the public who have disabilities access to electronic and information technology that is comparable to the access available to employees and members of the public who are not individuals with disabilities.</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Social Security Number</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Veterans Affairs</td>
</tr>
<tr class="even">
<td>VACO</td>
<td>Veterans Affairs Central Office</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems Technology Architecture</td>
</tr>
<tr class="odd">
<td>VMS</td>
<td>Virtual Memory System</td>
</tr>
</tbody>
</table>

# Appendix A Beneficiary Travel Dashboard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Indianapolis VAMC developed the Class 3 web-based Beneficiary Travel (BT) Dashboard to assist users in making faster, more accurate decisions on mileage reimbursement for travel claims. The VHA Chief Business Office requested the BT Dashboard package be implemented as part of the Cost Efficiency Initiative, which is one of the VA Secretary’s 16 Major Transformation Initiatives (T-16). BT Dashboard functions as an accessory to the VistA Beneficiary Travel claims functionality. No data is entered or stored in this application.

The BT Dashboard is a web-based application designed to be used along with the existing VistA Beneficiary Travel claim features in concurrent sessions. For most effective use, travel clerks will have side-by-side monitors running a VistA Beneficiary Travel session on one screen and a BT Dashboard session on the other screen. BT Dashboard calculates the driving mileage from the patient’s address to a configured set of institutions. Using the Beneficiary Travel Claim menu, the application automatically synchronizes with travel claims as claims are created in VistA. BT Dashboard also displays patient appointments, notes, orders, consults, and past claims.

The locally-developed BT Dashboard package was accepted by OIT as a priority for conversion from Class 3 (local use) to Class 1 (VHA-wide use). In 2012, the BT Dashboard web application was installed and tested in production at thirteen VAMC facilities. This included individual VAMC web server installations, as well as several VAMCs in Region 1 where a single, centralized, web server was used. One server per region is the expected configuration to host the web side of BT Dashboard.

Summary of work steps using BT Dashboard and VistA Beneficiary Travel:

1.  Travel clerk opens a VistA session using the Beneficiary Travel menu.
2.  Travel clerk opens a BT Dashboard session.
3.  Travel clerk enters a new travel claim into VistA through the Claim Enter/Edit option.
4.  Travel clerk uses BT Dashboard to find and synchronize with the claim, extract the patient’s address from VistA, and calculate the distance between the patient’s home address and each VAMC and CBOC in the area using the Bing Maps API.
5.  BT Dashboard display:
1.  Patient name
1.  Patient address
2.  Service connection percentage
3.  Scheduled appointments and status of each appointment, notes, orders, consults, and claims
4.  Clinical inventory list of each facility within the area
5.  Mileage to configured facilities

No data is entered through BT Dashboard. BT Dashboard only displays mileage and other information. The travel clerk enters the mileage generated by BT Dashboard at the appropriate prompt while entering a travel claim in VistA.

## Process Flowchart of Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](beneficiary-travel-version-1-technical-manual-updated-with-dgbt-1-41/002.png)

Process Flowchart of Operations

## Web and Operating System Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DGBT\*1.0\*19 must be installed on each facility’s VistA system as a prerequisite to using BT Dashboard. For more information, refer to the DGBT\*1\*19 Patch Description and the BT Dashboard Installation Guide.

### Access to the Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Beneficiary Travel Dashboard is a web-based application that runs in the browser. The URL for the application can be obtained from an OI&T System Administrator.

In order to log into the Beneficiary Travel Dashboard you need to have the DGBT BENE TRAVEL MENU allocated as a primary or secondary menu option. Users of the BT VistA package should already have this option allocated.

### Security for the Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BT Dashboard is considered a minor application. BT Dashboard displays data that contains sensitive information, such as patient name, location of treatment, etc.

- Users must employ safeguards to ensure the security of the data contained within. Access is granted through a formal request process.
- Use your VistA Travel Claim package User ID and PIV card PIN for BT Dashboard.

BT Dashboard has undergone the development of an SRR (System Relevance Review) as part of the Certification Accreditation (C&A) process. This serves as the security baseline for specifications and design for BT Dashboard.

The CSP Gateway web server should be HTTPS enabled if possible. Obtain and install a security certification through the proper channels.

### .XML File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The .xml file containing the .csp and .cls source code can be obtained via FTP from Anonymous (see directions on patch DG\*1.0\*19). The .xml file has a timestamp in the file name indicating when the file was created

(e.g. BeneTravelDashboard_20120417_0834.xml for April 17, 2012 @ 8:34am).

The timestamp indicates the version of the file with the most recent version having the latest timestamp.