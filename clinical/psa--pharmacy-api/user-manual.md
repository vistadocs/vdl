---
consolidated_title: "drug accountability/inventory interface user manual"
app_code: PSA
doc_type: UM
master_source: "Drug Accountability/Inventory Interface Version 3 User Manual (Updated PSA*3*79)"
master_pub_date: October 1997
consolidated_from: 2 versions
prior_versions:
  - "Drug Accountability/Inventory Interface Version 3 User Manual (PSA*3*85)"
---

DRUG ACCOUNTABILITY/ INVENTORY INTERFACE USER MANUAL

> ![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/001.png)

> Version 3.0

> October 1997

> (Revised August 2018)

Office of Information and Technology

Enterprise Program Management Office

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. Either update the existing manual with the Change Pages document, or replace it with the updated manual.

> **NOTE:** The Change Pages document may include unedited pages needed for two-sided copying. Only edited pages display the patch number and revision date in the page footer.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision Pages</strong></th>
<th><p><strong>Patch</strong></p>
<blockquote>
<p><strong>Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/18</td>
<td><blockquote>
<p><u>107-116</u></p>
</blockquote></td>
<td><blockquote>
<p>PSA*3*79</p>
</blockquote></td>
<td><blockquote>
<p>Added (DAU) GUI to use Two Factor Authentication (2FA) which will require the use of a Personal Identity Verification (PIV) card.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>05/09</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSA*3*69</p>
</blockquote></td>
<td><blockquote>
<p>Added new option, Return Drug Credit Menu.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

\<This page is intentionally left blank\>

Preface

The Drug Accountability/Inventory Interface program (referred to as DA) V. 3.0 works toward a perpetual inventory for each Veterans Affairs facility’s pharmacy. This is achieved by tracking drugs through pharmacy locations based on the connection between the DRUG (#50) file and ITEM MASTER file (#441) or between the prime vendor’s invoice file and the DRUG file (#50).

\<This page is intentionally left blank\>

Table of Contents

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
    - [Package Functional Description](#package-functional-description)
    - [About This Manual](#about-this-manual)
    - [Icons](#icons)
    - [Special Instructions for the “First Time” Computer User](#special-instructions-for-the-first-time-computer-user)
    - [Special Notations](#special-notations)
- [Section One: GIP Interface Menu](#section-one-gip-interface-menu)
    - [Connection Menu (DRUG file/ITEM MASTER file)](#connection-menu-drug-fileitem-master-file)
    - [Pharmacy Location Maintenance Menu](#pharmacy-location-maintenance-menu)
    - [Receipts Menu](#receipts-menu)
    - [Dispensing Menu](#dispensing-menu)
    - [Maintenance Reports Menu](#maintenance-reports-menu)
- [Section Two: Prime Vendor Interface Menu](#section-two-prime-vendor-interface-menu)
    - [Pharmacy Location Maintenance Menu](#pharmacy-location-maintenance-menu-1)
    - [Dispensing Menu](#dispensing-menu-1)
    - [Orders Menu](#orders-menu)
    - [Maintenance Reports Menu](#maintenance-reports-menu-1)
- [Section Three: Return Drug Credit Menu](#section-three-return-drug-credit-menu)
    - [Batch Work List](#batch-work-list)
    - [Batch Complete List](#batch-complete-list)
    - [View/Update Batch](#viewupdate-batch)
    - [Return Drug Credit Report](#return-drug-credit-report)
- [Section Four: GUI Upload Program](#section-four-gui-upload-program)
  - [Using the GUI Upload Program](#using-the-gui-upload-program)
  - [Invoice Files](#invoice-files)
  - [Non-PIV/Alternate Logon](#non-pivalternate-logon)
- [Glossary](#glossary)
- [Index](#index)

### Package Functional Description 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DA V. 3.0 software package provides functionality to maintain a perpetual inventory of drugs. Interfacing with the Generic Inventory Package (GIP) and the prime vendors’ invoice data increments drug balances in pharmacy locations and master vaults. Pharmacy’s dispensing software packages pass dispensing data to DA V. 3.0 which decrements the drug balances in pharmacy locations.

### About This Manual 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual contains a description of all DA V. 3.0 options. It is divided into two sections. The first section consists of *GIP Interface Menu* options. The second section consists of *Prime Vendor InterfaceMenu* options. A glossary is located at the end of this manual and contains definitions of commonly used words.

### Icons 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Icons used to highlight key points in this manual are defined as follows:
- Note: Indicates especially important or helpful information.
- Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.
Example: This option is locked by the PSA ORDERS key.
Drug Accountability/Inventory 1 August 2018
> Interface V. 3.0
> User Manual

### Special Instructions for the “First Time” Computer User 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user is unfamiliar with the DA V. 3.0 package or other Veterans Health Information Systems and Technology Architecture (V*IST*A) software applications, it is recommended that the user study the DHCP (Decentralized Hospital Computer Program) *User’s Guide to Computing.* This orientation guide is a comprehensive handbook benefiting first time users of any V*IST*A application. The purpose of the introductory material is to help the user become familiar with basic computer terms and the components of a computer. It is reproduced and distributed periodically by the Kernel Development Group. To request a copy, contact the local Information Resources Management (IRM) staff.

### Special Notations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this manual, the user’s response is in bold type, but will not appear on the screen as bold. The bold part of the entry is the letter or letters that must be typed so that the computer can identify the response. In most cases, the user need only enter the first few letters. This increases speed and accuracy.
Every typed response must be followed by pressing the return key (or enter key for some keyboards). Whenever the return or enter key should be pressed, the user will see the symbol \<Enter\>. This symbol is not shown but is implied if there is bold input.
Throughout the package, help frames may be accessed from most prompts by entering one, two, or three question marks (?, ??, ???).
Within the examples representing actual terminal dialogues, the author may offer information about the dialogue. This information is enclosed in brackets (e.g., *\[Select Print Device\])* and will not appear on the screen.

# Section One: GIP Interface Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA GIP INTERFACE MENU\]

The *GIP Interface Menu* option assists in the maintenance of a Pharmacy perpetual inventory by interfacing with the Generic Inventory Package (GIP). The options available through the GIP interface are listed below.

Example: GIP Interface Menu

1.  Connection Menu (DRUG file/ITEM MASTER file) ...
2.  Pharmacy Location Maintenance Menu ...
3.  Receipts Menu ...
4.  Dispensing Menu ... 5 Maintenance Reports Menu ...

### Connection Menu (DRUG file/ITEM MASTER file) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA CONNECTION MENU\]

A crucial step in attaining drug accountability is a direct link between the DRUG file (#50) and the ITEM MASTER file (#441). This menu contains tools to assist with this link. If the user’s station has concentrated on accurate entries in the National Drug Code (NDC) fields of these two files, then the *NDC Menu* option may be the most efficient way to approach the link. If the user feels that the Federal Stock Number/National Stock Number (FSN/NSN) field may provide more effective linking, the *FSN Menu* option exists for that choice. For those drugs or pharmaceuticals that cannot be linked by either NDC or FSN, the *Single Drug Match* option, *Report of Unlinked DRUG/ITEM MASTER fileEntries* option*,* and the *Connect Unlinked DRUG/ITEM MASTER file Entries* option offer a last resort using a free text pick and match, or if a path to the National Drug File (NDF) exists with NDCs, a match can be attempted in that fashion.

Once linked, the ITEM MASTER file (#441) provides up-to-date packaging and prices for all procurement sources. This facilitates the receiving process and opens the door for the GIP interface.

Example: Connection Menu (DRUG file/ITEM MASTER file)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th>NDC Menu…</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>FSN Menu…</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>Single Drug Match</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>Report of Unlinked DRUG/ITEM MASTER file Entries</td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>Connect Unlinked DRUG/ITEM MASTER file Entries</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>Active, Unlinked Drugs in the ITEM MASTER file</td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>Display Connected Drug and Procurement History</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>8</p>
</blockquote></th>
<th>Unposted Procurement History</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td>Posted Drug Procurement History</td>
</tr>
</tbody>
</table>

#### NDC Menu 

> \[PSA NDC MENU\]

This menu contains options to link drug entries in the ITEM MASTER file (#441) to NDC matched entries in the DRUG file (#50). If an ITEM MASTER file (#441) entry has an NDC that matches a DRUG file (#50) entry, then data from the two files can be compared. The *Report Potential NDC Matches* option report is available to show all the entries that can be matched by

NDC. Once the matches have been reviewed, they can be acted on with a controlled connection (drug-by-drug), or with an automated connection, which links the files wherever an NDC match occurs.

Example: NDC Menu

1.  NDC Duplicates Report (ITEM MASTER file)
2.  Report Potential NDC Matches
3.  Controlled Connection by NDC Match
4.  Automated DRUG/ITEM MASTER file Link by NDC
5.  Inquire/Compare DRUG file/ITEM MASTER file
6.  DRUG file/ITEM MASTER file Comparison Report

#### NDC Duplicates Report (ITEM MASTER file) 

> \[PSA NDC DUPLICATE REPORT\]

Currently in Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP), the same NDC cannot be entered for two different items. Since the NDC is relied on to link the DRUG file (#50) to the ITEM MASTER file (#441), it is important that the proper entry is located. The *NDC Duplicates Report* option scans through all the entries in the ITEM MASTER file (#441) looking for entries sharing the same NDC. Through printing this report and working with the local Acquisition and Materiel Management Service (A&MMS) Purchasing Agent, the user can ensure the ITEM MASTER file (#441) entries have the correct NDC before linking with the DRUG file (#50). The report lists the NDC, item number, item description, and vendor name.

#### Report Potential NDC Matches 

> \[PSA NDC REPORT\]

The *Report Potential NDC Matches* option scans through the DRUG file (#50) looking for drugs with an NDC that have not been inactive. If the same NDC can be located in the ITEM MASTER file (#441), this potential match is displayed. The report also indicates unmatched FSNs with the drug name.

> **NOTE:** It would be a good idea to first run this report and review the potential matches before considering either the controlled or automated connection options. The report lists the DRUG file’s (#50) NDC and drug name plus the potentially matched ITEM MASTER file’s (#441) item number and item description.

#### Controlled Connection by NDC Match 

> \[PSA NDC CONTROL LOOP\]

The *Controlled Connection by NDC Match* option moves through the same entries identified in the *Report Potential NDC Matches* option and provides the opportunity to link them one at a time. If the controller chooses not to link an entry, the option will continue to the next drug.

#### Automated DRUG/ITEM MASTER file Link by NDC 

> \[PSA NDC AUTO LOOP\]

The *Automated DRUG/ITEM MASTER file Link by NDC* option allows the user to link the entries identified in the *Report Potential NDC Matches* option simultaneously. The user will be prompted to select a device to direct the listing of links as they occur.

> **NOTE:** It is important to review the *Report Potential NDC Matches* option before considering using this option.

#### Inquire/Compare DRUG file/ITEM MASTER file 

> \[PSA DRUG INQUIRE\]

The *Inquire/Compare DRUG file/ITEM MASTER file* option displays packaging and price information from the DRUG file (#50) and ITEM MASTER file (#441) when identical NDCs exist regardless of whether linking has occurred. This option displays the entries one at a time while the next option, *DRUG file/ITEM MASTER file Comparison Report* option, shows a range of entries.

The report lists the DRUG file’s (#50) drug name, NDC, price per order unit (PPOU), order unit, packaging, price per dispense unit (PPDU), and dispense unit. It also lists the ITEM MASTER file’s (#441) item description, NDC, price per order unit (PPOU), order unit, date of price, packaging, price per dispense unit (PPDU) for each order unit, and the vendor name.

#### DRUG file/ITEM MASTER file Comparison Report 

> \[PSA COMPARISON REPORT\]

The *DRUG file/ITEM MASTER file Comparison Report* option allows the user to select a short range of DRUG file (#50) and ITEM MASTER file (#441) comparative information on packaging and pricing. The report lists the DRUG file’s (#50) drug name, drug number, NDC, price per order unit (PPOU), order unit, dispense units per order unit (DUOU), price per dispense unit (PPDU), and dispense unit. It also lists the ITEM MASTER file’s (#441) item name, item number, National Stock Number (NSN), NDC, price per dispense unit (PPDU), and vendor name.

#### FSN Menu 

> \[PSA FSN MENU\]

Similar to the *NDC menu* option, this menu contains options to link DRUG file (#50) entries with a FSN to the ITEM MASTER file (#441). If an ITEM MASTER file (#441) entry has a National Stock Number (NSN) that matches a DRUG file (#50) FSN, then the two files can be linked. The *Report Potential FSN Matches* option shows all the entries that can be matched by FSN. Once the matches have been reviewed, they can be acted on with a controlled connection (drug-by-drug) or with an automated connection (linking all drugs with an NDC match).

Example: FSN Menu

1.  Report Potential FSN Matches
2.  Controlled Connection by FSN Match
3.  Automated DRUG/ITEM MASTER file Link by FSN

#### Report Potential FSN Matches 

> \[PSA FSN REPORT\]

The *Report Potential FSN Matches* option scans through the DRUG file (#50) looking for drugs that have an FSN and have not been inactive. If the same NSN is located in the ITEM MASTER file (#441), the entries from each file will be displayed as a potential match. It is a good idea to first run this report and review the potential matches before considering either the controlled or automated connection options. The report lists DRUG file’s (#50) drug name and NDC with the ITEM MASTER file’s (#441) matching item number and item name.

#### Controlled Connection by FSN Match 

> \[PSA FSN CONTROL LOOP\]

The *Controlled Connection by FSN Match* option allows movement through the entries identified in the *Report Potential FSN Matches* option and links them one at a time. If the user chooses not to link an entry, the option will continue to the next drug.

#### Automated DRUG/ITEM MASTER file Link by FSN 

> \[PSA FSN AUTO LOOP\]

The *Automated DRUG/ITEM MASTER file Link by FSN* option allows the user to move through the same entries identified in the *Report Potential FSN Matches* option and link them all at once. The user is asked to select a device to print the listing of links as they occur.

> **NOTE:** It is important to run the *Report Potential FSN Matches* option first and review before considering using this option.

#### Single Drug Match 

> \[PSA SINGLE DRUG MATCH\]

The *Single Drug Match* option links one drug at a time, finding matches between the DRUG file (#50) and ITEM MASTER file (#441). The system attempts first to match by NDC, displaying matches for approval. If no NDC match is found, the system searches for matches of the DRUG file’s (#50) FSN field (#6) to the ITEM MASTER file’s (#441) NSN field (#5). If located, the match is displayed for approval. If there are still no matches, then the user can look directly at the ITEM MASTER file (#441). The user can select a match by entering the first three or four letters of the generic or brand name. Finally, if the drug is linked to the NDF, the user can search each NDC for a match in the ITEM MASTER file (#441). Some drugs in the NDF may contain as many as thirty or forty NDCs. This process can be exited at any time. When using this option to review an existing link, the link between a particular item can be broken by entering the “@” character.

#### Report of Unlinked DRUG/ITEM MASTER file Entries 

> \[PSA UNLINKED REPORT\]

The *Report of Unlinked DRUG/ITEM MASTER file Entries* option can be run at any point in the linking process to see what entries are not yet linked to the ITEM MASTER file (#441). If the user is considering using the *Connect Unlinked DRUG/ITEM MASTER file Entries* option, this report will provide a helpful preview of the unlinked drugs. The report lists the drug name, FSN, NDC, and yes/no if the NDC is in the NDF.

#### Connect Unlinked DRUG/ITEM MASTER file Entries 

> \[PSA UNLINKED LOOP\]

The *Connect Unlinked DRUG/ITEM MASTER file Entries* option scans through the DRUG file (#50) looking for drugs not yet linked to the ITEM MASTER file (#441) that are not inactive.

The user may preview the unlinked entries by running the *Report of Unlinked DRUG/ITEM MASTER file Entries* option. Whenever the option is exited, the last drug linked, date, time, and the user’s name will be stored. The next user will have the choice of resuming with this drug upon entering this option.

#### Active, Unlinked Drugs in the ITEM MASTER file 

> \[PSA ACTIVE DRUGS/ITEM MASTER FILE\]

The *Active, Unlinked Drugs in the ITEM MASTER file* option allows the user to scan the ITEM MASTER file (#441) for drugs not yet linked to the DRUG file (#50), which have been purchased since the last date entered. The report lists the ITEM MASTER file’s (#441) item number, item name, NSN, vendor name of the last vendor purchased from, NDC, and the items long description.

#### Display Connected Drug and Procurement History 

> \[PSA DISPLAY CONNECTED DRUG\]

The *Display Connected Drug and Procurement History* option displays the comparison data for both the DRUG (#50) and ITEM MASTER files (#441) if a connection was made. The display will show a procurement history for a selected date range and control point, and the vendor’s price/packaging data.

#### Unposted Procurement History 

> \[PSA UNPOST PROCURMENT HISTORY\]

The *Unposted Procurement History* option prints a report listing all pharmacy procurements for a selected month. The report includes a detailed list of each item procured, the quantity received, the NDC, the DRUG file’s (#50) generic drug name, and vendor name.

> **NOTE:** If the user chooses to print this report to a printer, the following prompts will not be seen: “Print item totals?” and “Would you like a list of high dollar items?”. If the user wishes to respond to these questions, this report will need to be displayed on the

> screen.

#### Posted Drug Procurement History 

> \[PSA POSTED DRUG REPORT\]

The *Posted Drug Procurement History* option produces an alphabetical listing of drugs procured from the warehouse for a selected month. The report lists the primary inventory point, item number, item name, quantity ordered, quantity received, packaging, price per order unit (PPOU), total cost for the item, date purchased, and transaction number. A total for each item is printed for the quantity ordered, quantity received, and total cost.

> **NOTE:** If the user chooses to print the *Posted Drug Procurement History* on a printer, the following prompt will not be seen: “Would you like a list of high dollar items?”. If the user wishes to respond to this question, this report will need to be displayed on the screen.

### Pharmacy Location Maintenance Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA GIP LOCATION MENU\]

The *Pharmacy Location MaintenanceMenu* contains options that set up and edit pharmacy locations. The drug balances can be initialized and adjusted. Drug prices in the DRUG file (#50) are compared with prices in the Generic Inventory. Items can be loaded and reports can be generated from a primary inventory point to a pharmacy location.

The following options are used for setting up and monitoring drug on-hand quantities within a pharmacy location:

Example: Pharmacy Location Maintenance Menu

1.  Set Up/Edit a Pharmacy Location
2.  Balance Adjustments
3.  Balance Initialization
4.  Enter/Edit a Drug 5 Inventory Interface ...
6.  Update Prices
7.  Transfer Drugs Between Pharmacies

#### Set Up/Edit a Pharmacy Location 

> \[PSA LOCATION EDIT\]

The *Set Up/Edit a Pharmacy Location* option provides the capability to create a pharmacy location and connect it with a primary inventory point.

Creating the Pharmacy Location

U<u>About Pharmacy Locations</u>U

Locations are Outpatient (OP), Inpatient (IP), or a Combined (OP/IP). The user can have more than one location - even more than one type of location (for instance, a multi-divisional facility might procure for several divisions).

The User can create a location for each Inpatient or Outpatient site in order to track drug balances separately. Or, create a Combined location, like ALABASTER, that tracks Inpatient and Outpatient drug balances together.

U<u>Choosing a Site Name</u>U

How the site will track the drugs will depend on the type of pharmacy location chosen.

The three choices are Inpatient, Outpatient, or Combined.

- Inpatient: will track drugs only in the Inpatient dispensing site.
- Outpatient: will track drugs only in the Outpatient pharmacy/clinic.
- Combined: tracks all the drugs together in the Inpatient dispensing site and the Outpatient pharmacy/clinic. Only one total per drug is received.

A site is the physical location where drugs are stored and dispensed. If the facility maintains more than one Inpatient or Outpatient site, the user will be asked to choose a site for this pharmacy location.

> ![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/002.png)

> Multi-divisional facilities can track drugs in a variety of locations.

U

<u>Entering Wards for Inpatient Sites</u>U

Assign wards to each Inpatient site. Each ward can be connected to only one Inpatient site. This information affects the gathering of IV and Unit Dose dispensing data.

Example: Create a Pharmacy Location—Single Inpatient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select GIP Interface Option: <strong>2</strong> Pharmacy Location Maintenance Menu</p>
<ol type="1">
<li><p>Set Up/Edit a Pharmacy Location</p></li>
<li><p>Balance Adjustments</p></li>
<li><p>Balance Initialization</p></li>
<li><p>Enter/Edit a Drug</p></li>
<li><p>Inventory Interface ...</p></li>
<li><p>Update Prices</p></li>
</ol>
<p>Select Pharmacy Location Maintenance Menu Option: <strong>1</strong> Set Up/Edit a Pharmacy Location</p>
<p>Select one of the following:</p>
<ol type="1">
<li><p>INPATIENT</p></li>
<li><p>OUTPATIENT</p></li>
<li><p>COMBINED (IP/OP)</p></li>
</ol>
<p>Select Pharmacy type: <strong>1</strong> INPATIENT</p>
<p>Creating INPATIENT</p>
<p>For the purpose of collecting Unit Dose and IV dispensing data, any ward at which such dispensing might ever occur should be added. The ONLY reason to NOT add a ward would be if the dispensing at that ward should NOT update COMBINED (IP/OP).</p>
<blockquote>
<p><em>[There is NO harm in adding inactive wards.]</em></p>
</blockquote>
<p>INPATIENT is linked to 1 WEST, 1 SOUTH, 1 NORTH, 2 WEST, 2 SOUTH, 2 NORTH,</p>
<p>2 EAST, 1 EAST, 3 WEST, 3 EAST, 3 SOUTH, 4 EAST, 4 NORTH, 5 WEST, 5 EAST,</p>
<p>5 SOUTH, 6 WEST, 6 SOUTH, 7 EAST, 7 WEST, 8 EAST, 8 WEST.</p>
<p>INPATIENT DISPENSING UPDATE?: <em>[Mark with Y if you have established current balances.]</em></p>
<p>PRIME VENDOR?: YES// <strong>??</strong></p>
<p>To more efficiently process Prime Vendor receipts, setting this flag to</p>
<p>"Yes" will allow you to store an obligation number. This number will then be offered as a default whenever using the Receive Directly into Drug Accountability option on the Receiving Menu.</p>
<p>CHOOSE FROM:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>PRIME VENDOR?: YES// <strong>&lt;Enter&gt;</strong></p>
<p>CURRENT PRIME VENDOR PO#: 521-A70005// <strong>&lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Create a Pharmacy Location—Single Outpatient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Pharmacy Location Maintenance Menu Option: <strong>1</strong> Set Up/Edit a Pharmacy Location Select one of the following:</p>
<ol type="1">
<li><p>INPATIENT</p></li>
<li><p>OUTPATIENT</p></li>
<li><p>COMBINED (IP/OP)</p></li>
</ol>
<p>Select Pharmacy type: <strong>2</strong> OUTPATIENT</p>
<p>Outpatient site selection affects the collection of dispensing data.</p>
<p>OUTPATIENT SITE: PELHAM// <strong>?</strong></p>
<p>Enter the Outpatient Site from which to gather prescription dispensing data.</p>
<p>ANSWER WITH PHARMACY SITE NAME, OR SITE NUMBER, OR RELATED INSTITUTION: PELHAM</p>
<p>OUTPATIENT SITE: PELHAM// <strong>&lt;Enter&gt;</strong></p>
<p>PRIME VENDOR?: <strong>??</strong></p>
<p>To more efficiently process Prime Vendor receipts, setting this flag to "Yes" will allow you to store an obligation number. This number will then be offered as a default whenever using the Receive Directly into</p>
<p>Drug Accountability option on the Receiving Menu. CHOOSE FROM:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>PRIME VENDOR?: YES// <strong>&lt;Enter&gt;</strong></p>
<p>CURRENT PRIME VENDOR PO#: 521-A70005// <strong>&lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Create a Pharmacy Location—Combined (Inpatient and Outpatient)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Pharmacy Location Menu Maintenance Option: <strong>1</strong> Set Up/Edit a Pharmacy Location</p>
<p>Select one of the following:</p>
<ol type="1">
<li><p>INPATIENT</p></li>
<li><p>OUTPATIENT</p></li>
<li><p>COMBINED (IP/OP)</p></li>
</ol>
<p>Select Pharmacy type: <strong>3</strong> COMBINED (IP/OP)</p>
<p>Creating COMBINED</p>
<p>For the purpose of collecting Unit Dose and IV dispensing data, any ward at which such dispensing might ever occur should be added. The ONLY reason to NOT add a ward would be if the dispensing at that ward should NOT update COMBINED (IP/OP).</p>
<p>COMBINED is linked to 1 WEST, 1 SOUTH, 1 NORTH, 2 WEST, 2 SOUTH, 2 NORTH,</p>
<p>2 EAST, 1 EAST, 3 WEST, 3 EAST, 3 SOUTH, 4 EAST, 4 NORTH, 5 WEST, 5 EAST, 5 SOUTH, 6 WEST, 6 SOUTH, 7 EAST, 7 WEST, 8 EAST, 8 WEST.</p>
<p>Outpatient site selection affects the collection of dispensing data.</p>
<p>OUTPATIENT SITE: MAYLENE// <strong>&lt;Enter&gt;</strong> INPATIENT DISPENSING UPDATE?: <strong>&lt;Enter&gt;</strong></p>
<p>PRIME VENDOR?: YES// <strong>??</strong></p>
<p>To more efficiently process Prime Vendor receipts, setting this flag to "Yes" will allow you to store an obligation number. This number will then be offered as a default whenever using the Receive Directly into</p>
<p>Drug Accountability option on the Receiving Menu. CHOOSE FROM:</p>
<p>1 YES</p>
<p>0 NO</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

PRIME VENDOR?: YES// \<Enter\>

CURRENT PRIME VENDOR PO#: 521-A70005// \<Enter\>

*\[At this point the prompts will be the same regardless of pharmacy location type.\]*

U

<u>Changing a Pharmacy Location Type</u>U

- The user can change a Combined location to a separate Inpatient and Outpatient location. If the Outpatient activity needs to be tracked, the user must create an Outpatient location.
- A site with an existing Inpatient and Outpatient location can be changed to a Combined location.

U<u>Connecting with the Primary Inventory Point</u>U

The next prompt is the primary inventory point. The connection to a primary inventory point automates the receiving process. Connecting to multiple primary inventory points is allowed.

Only primary inventory points marked with “D” for Drug Accountability in the GENERIC INVENTORY file’s (#445) SPECIAL INVENTORY POINT TYPE field (#15) can be connected.

The receipt failure notification prompt generates mail messages when items are received that are not connected to the DRUG file (#50) or not stocked in the pharmacy location. This will help track drugs only if the drugs stocked in the primary inventory point directly coincide with the drugs in the pharmacy location. If the primary inventory point and pharmacy location inventories are not congruent, receipt failure notification will probably not be helpful.

Example: Connecting with the Primary Inventory Point

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select PRIMARY INVENTORY POINT(S): <strong>?</strong></p>
<p>ANSWER WITH PRIMARY INVENTORY POINT(S)</p>
<p>YOU MAY ENTER A NEW PRIMARY INVENTORY POINT(S), IF YOU WISH</p>
<p>For Controlled Substances enter the name of the Pharmacy Inventory</p>
<p>Point which contains ONLY the controlled substances stored in the Pharmacy MASTER VAULT.</p>
<p>Must be Special Inventory Type "D" for Drug Accountability. ANSWER WITH GENERIC INVENTORY INVENTORY POINT</p>
<p>CHOOSE FROM:</p>
<p>521-INPATIENT PHARMACY PRIMARY</p>
<p>521-OUTPATIENT PHARMACY PRIMARY</p>
<p><em>[If the system does not display primary inventory points to choose from, you must mark your</em> <em>primary inventory point as a pharmacy location.]</em></p>
<p>Select PRIMARY INVENTORY POINT(S): <strong>521-INPAT</strong>IENT PHARMACY PRIMARY</p>
<p>ARE YOU ADDING '521-INPATIENT PHARMACY' AS</p>
<p>A NEW PRIMARY INVENTORY POINT(S) (THE 1ST FOR THIS DRUG ACCOUNTABILITY STATS)? <strong>Y</strong> (YES)</p>
<p>RECEIPT MAIL GROUP: <strong>??</strong></p>
<p>Enter the name of the mail group that should receive messages whenever inventory items cannot be received into a pharmacy location and also this same group will receive DRUG file price update messages. RECEIPT MAIL GROUP: <strong>GROUP</strong></p>
<p>The GROUP mail group has not been created!</p>
<p>Messages can't be sent until creation.</p>
<p>RECEIPT FAILURE NOTIFICATION?: <strong>?</strong></p>
<p>Enter "1" or "Y" to transmit a mailman message to the receiver and the</p>
<p>RECEIPT FAILURE mail group each time a failure occurs.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CHOOSE FROM:

1 YES

0 NO

RECEIPT FAILURE NOTIFICATION?: ??-----------------------------------------report continues---------------------------------------- Example: Connecting with the Primary Inventory Point (continued)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>If a Drug Accountability location is linked to a primary inventory point, items received into the primary inventory point will also be updated in the Drug accountability location. If items are received that are not connected to the DRUG file (#50) or not stocked in the Drug Accountability location, and this field is set to “YES”, the receiver and the RECEIPT FAILURE mail group will be notified with a list of failed items.</p>
<p>Choose from</p>
<p>1 YES</p>
<p>0 NO</p>
<p><em>[Mark Y if your primary inventory point is populated only with drugs designated in the pharmacy location. If your primary inventory point contains drugs not tracked in your pharmacy location, leave this field blank or mark with N.]</em> RECEIPT FAILURE NOTIFICATION?: <strong>YES</strong> Would you like to loop through 521-INPATIENT PHARMACY'S items to check for any new entries that are ready to load? <strong>YES</strong> Load inventory quantities also? Yes// <strong>?</strong></p>
<p><em>[Inventory quantities will be multiplied by the dispensing unit conversion factor.]</em></p>
<p>Load inventory quantities also? Yes// <strong>&lt;Enter&gt;</strong></p>
<p>OK to load TRIFLUOPERAZINE HCL 5MG TAB from the DRUG file</p>
<p>linked to inventory item: TRIFLUOPERAZINE? Yes// <strong>&lt;Enter&gt;</strong> TRIFLUOPERAZINE HCL 5MG TAB</p>
<p>ARE YOU ADDING 'TRIFLUOPERAZINE HCL 5MG TAB' AS A NEW DRUG (THE 6TH FOR THIS DRUG ACCOUNTABILITY</p>
<p>STATS)? <strong>Y</strong> (YES)</p>
<p>DRUG BALANCE: 2500// <strong>&lt;Enter&gt;</strong></p>
<p>Updating Beginning balance and transaction history.</p>
<p>Add/edit drugs? No// <strong>&lt;Enter&gt;</strong></p>
<p>Inactive Date: <strong>&lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Receipt Failure Notification Message

Subj: Failed DA/GIP Receipts for 521-93-1-023-0004 \[#356992\]

01 Dec 92 15:11 CST 2 Lines

From: Failed Receipt Notifier in 'IN' basket. Page 1

-----------------------------------------------------------------------------

\#9 DOXORUBICIN HYDROCHLORIDE-POSTED STOCK INJECTION-VI NOT STOCKED. 430 NITROGLYCERIN-POSTED STOCK TRANSDERMAL SYSTEM 25MG-30S NOT LINKED.

#### Balance Adjustments 

> \[PSA BALANCE ADJUSTMENTS\]

The *Balance Adjustments* option allows the user to review and/or enter an adjustment to correct the balance of a drug.

This option is locked by the PSAMGR key.

#### Balance Initialization 

> \[PSA BALANCE INITIALIZE\]

The *Balance Initialization* option allows the user to establish the balance for any drugs in the pharmacy location that do not have a balance.

#### Enter/Edit a Drug 

> \[PSA DRUG ENTER/EDIT\]

The *Enter/Edit a Drug* option is used to add a new drug to the pharmacy location or establish or display the balance of an existing drug.

#### Inventory Interface 

> \[PSA GIP MENU\]

The following options are used for reporting and loading items from a primary inventory point to a pharmacy location:

Example: Inventory Interface Menu

1.  Report of Inventory Items’ Link to DRUG file
2.  Loadable Inventory Items Report
3.  Populate Pharmacy Location with Inventory Items
4.  Drugs Not Found in Linked Inventory
5.  Physical Inventory Balance Review
6.  Compare Prices (DA/GIP)

#### Report of Inventory Items’ Link to DRUG file 

> \[PSA GIP LINK REPORT\]

The *Report of Inventory Items’ Link to DRUG file* option shows which inventory items are linked to the DRUG file (#50). If there is a link, the report will show the specific link between the inventory and the DRUG file (#50). Drugs must be linked to be loaded in the *Populate Pharmacy Location with Inventory Items* option. The report lists the item number, item description, and the linked drug name.

#### Loadable Inventory Items Report 

> \[PSA GIP REPORT\]

The *Loadable Inventory Items Report* option shows the inventory items with DRUG file (#50) links not yet added to a selected pharmacy location. These drugs will be loaded in the *Populate Pharmacy Location with Inventory Items* option. The report lists the item number, item name, linked drug, order unit balance, order unit, dispense unit balance, and dispense unit.

#### Populate Pharmacy Location with Inventory Items 

> \[PSA GIP POPULATE\]

The *Populate Pharmacy Location with Inventory Items* option loads linked drugs from the primary inventory point into a selected pharmacy location. The user can view the list of loadable items before loading. This same list is available under the *Loadable Inventory Items’ Report* option.

#### Drugs Not Found in Linked Inventory 

> \[PSA DRUGS NOT IN INVENTORY\]

The *Drugs Not Found in Linked Inventory* option lists the drugs in a pharmacy location that have not been loaded into the corresponding primary inventory point. The report lists drug name, connected item number, connected item name, and the primary inventory point that stocks the item.

#### Physical Inventory Balance Review 

> \[PSA GIP COMPARE\]

The *Physical Inventory Balance Review* option displays selected drugs with their pharmacy location balance and primary inventory point balance.

#### Compare Prices (DA/GIP) 

> \[PSA GIP DISCREPANCIES\]

The *Compare Prices (DA/GIP)* option lists DA V. 3.0 prices in comparison with Generic Inventory Package’s prices and the conversion factor.

#### Update Prices 

> \[PSA GIP CONT BAL UPDATE\]

The *Update Prices* option allows a comparison of prices in the DRUG file (#50) with prices in the Generic Inventory Package and then it will update the DRUG file (#50) if desired.

#### Transfer Drugs Between Pharmacies 

> \[PSA TRANSFER DRUGS\]

The *Transfer Drugs Between Pharmacies* option allows a pharmacist to move drugs between pharmacy locations. The number of dispense units to be moved is subtracted from the dispensing pharmacy location and added to the receiving pharmacy location. A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET may be printed after all transfers are completed.

This option is locked by the PSAMGR and PSJ RPHARM keys.

Example: One Active Pharmacy Location

There is only one active pharmacy location. There must be at least two to transfer drugs.

If there is only one active pharmacy location, the user is exited from the option.

Example: More than One Active Pharmacy Location

Enter your Current Signature Code: SIGNATURE VERIFIED

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: RIVERCHASE (IP)
3.  OUTPATIENT: PELHAM (OP)

Select Transfer from Pharmacy: (1-3): 1

Select the pharmacy location that will transfer the drug. This pharmacy location will have its drug balance decreased when the transfer is complete.

Example: Transfer Drugs between Pharmacies

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

Select DRUG: ACETAMINOPHEN 325MG TAB CN103

Dispense Unit: TAB Current Balance: 60

Enter Quantity to Transfer: (1-60): 10

Select the drug and number of dispense units to be transferred.

Choose the pharmacy location receiving the transferred drugs:

1.  INPATIENT: RIVERCHASE (IP)
2.  OUTPATIENT: PELHAM (OP)

Select Transfer to Pharmacy: (1-2): 2

Select the pharmacy that will receive the drug. Its balance will be increased when the transfer is complete.

INPATIENT: PELHAM (OP) does not stock ACETAMINOPHEN 325MG TAB!

Do you want to continue? YES

Answer yes if it is okay to now stock this drug in the receiving pharmacy location.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>----------------------------------------------------------------------------- ACETAMINOPHEN 325MG TAB</p>
<p>Transferring: 10 (TAB)</p>
<p>From: COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)</p>
<p>To : OUTPATIENT: PELHAM (OP)</p>
<p>-----------------------------------------------------------------------------</p>
<p>Is this OK? NO// <strong>YES</strong></p>
<p>Updating pharmacy on-hand balances now............. Done!</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the displayed transfer information is correct, enter YES. The drug balance in the transferring pharmacy location is decreased. The drug balance in the receiving pharmacy location is increased. If the drug is new to the receiving pharmacy location, a MailMan message is sent to holders of the PSAMGR key letting them know that a new drug is being added to that location. The MailMan message lists the drug, dispense unit, number of dispense units transferred, pharmacist who initiated the transfer, transferring pharmacy location, and the receiving pharmacy location.

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP) Select DRUG: \<Enter\>-----------------------------------------report continues----------------------------------------

If there are more drugs to be transferred to the <u>same</u> pharmacy location, the user can select them now. If not, press \<Enter\> to select the next transferring pharmacy location.

Example: Transfer Drugs between Pharmacies (continued)

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: RIVERCHASE (IP)
3.  OUTPATIENT: PELHAM (OP)

Select Transfer from Pharmacy: (1-3): ^

If the user wants to transfer drugs from another pharmacy location, select that location now. If the user is finished transferring drugs, enter \<^\>.

Print transfer signature sheets? Y// \<Enter\>

DEVICE: HOME// *\[Select Print Device\]*

A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET can be printed at this

time for all the transfers just entered. This sheet prints the transfer data for each unique combination of pharmacy locations. It is used to record the signature of the person who received the drugs. See the *Transfer Signature Sheet* option for an example of this sheet.

### Receipts Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RECEIPTS MENU\]

Options on this menu process receipts for purchase orders, control point transactions, and prime vendors.

Example: Receipts Menu

1.  Receiving Directly into Drug Accountability
2.  Purchase Order Review
3.  Control Point Transaction Review
4.  Drug Receipt History Review
5.  Invoice Review

#### Receiving Directly into Drug Accountability 

> \[PSA RECEIVING\]

This option processes prime vendor receipts from an invoice, updating the balance, transaction file, and monthly activity.

> **IMPORTANT:** Once received, the drug balances are incremented in the pharmacy location and/or master vault.

The invoiced drug’s order unit is compared to the ORDER UNIT field (#12) in the DRUG file

(#50) and the dispense units per order unit (DUOU) is compared to the DISPENSE UNITS PER ORDER UNIT field (#15) in the DRUG file (#50). If the order unit and dispense units per order unit (DUOU) are the same, the NDC (#31), PRICE PER ORDER UNIT (#13), and PRICE PER DISPENSE UNIT (#16) fields in the DRUG file (#50) may be updated.

The following condition must be met to update the NDC field (#31).

- If the invoice NDC is different from the NDC field (#31), the NDC field (#31) is overwritten with the invoiced NDC.

The following condition must be met to update the PRICE PER ORDER UNIT field (#13) and PRICE PER DISPENSE UNIT field (#16).

- If the invoiced price per order unit (PPOU) is different than the PRICE PER ORDER UNIT field (#13), the PRICE PER ORDER UNIT field (#13) is overwritten with the new prorated price per order unit (PPOU). The PRICE PER DISPENSE UNIT field (#16) is also overwritten with the new prorated price per dispense unit (PPDU).

Example: Receiving Directly into Drug Accountability V. 3.0

1.  Receiving Directly into Drug Accountability
2.  Purchase Order Review
3.  Control Point Transaction Review
4.  Drug Receipt History Review
5.  Invoice Review

Select Receiving Menu Option: 1 Receiving Directly into Drug Accountability

Select one of the following:

1.  INPATIENT
2.  OUTPATIENT
3.  COMBINED (IP/OP)

Select Pharmacy type: 1 INPATIENT

Because there is more than one Inpatient Site at this facility, I need you to select an AR/WS Inpatient Site Name: PELHAM

COMBINED (IP/OP) for PELHAM

The current Prime Vendor PO# for this location doesn't seem current.

-----------------------------------------report continues----------------------------------------Example: Receiving Directly into Drug Accountability V. 3.0 (continued)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Would you like to correct it? Yes// <strong>&lt;Enter&gt;</strong></p>
<p>CURRENT PRIME VENDOR PO#: 521-C70001// <strong>&lt;Enter&gt;</strong></p>
<p>Select Prime Vendor Obligation Number: 521-C70001// <strong>&lt;Enter&gt;</strong> 08-25-92 ST Pending Fiscal Action</p>
<p>FCP: 022 $ 6000</p>
<p>Select Pharmacy Transaction number: <strong>521-97-1-022-0001</strong></p>
<p>Please enter the Prime Vendor Invoice number: <strong>??</strong></p>
<p>To allow the entering of a Prime Vendor Invoice number for a receipt. The IFCAP Purchase Order number may be used all month and there may not be a corresponding IFCAP transaction number for each Prime Vendor receipt.</p>
<p>The invoice will be stored, allowing look-ups for receipts against this invoice.</p>
<p>Please enter the Prime Vendor Invoice number: <strong>119202</strong></p>
<p>Select INPATIENT drug: <strong>METO</strong>PROLOL TARTRATE 50MG TAB CV100 NDC: 64738-8236-1 <strong>&lt;Enter&gt;</strong></p>
<p>Order Unit: BT <strong>&lt;Enter&gt;</strong> BOTTLE</p>
<p>Dispense Units: <strong>TAB</strong></p>
<p>Dispense Units per Order Unit: 1000// <strong>&lt;Enter&gt;</strong></p>
<p>Price per Order Unit: (0-9999): 93.6 <strong>&lt;Enter&gt;</strong></p>
<p>Quantity received: (0-9999999):25 <strong>&lt;Enter&gt;</strong> Converted quantity: 25000 Okay to post? Yes// <strong>YES</strong></p>
<p>There were 60 on hand. There are now 25060 on hand.</p>
<p>Updating monthly receipts and transaction history.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Purchase Order Review 

> \[PSA PURCHASE ORDER REVIEW\]

The *Purchase Order Review* option reviews all receipt transactions for a selected purchase order. It lists the purchase order number, purchase order date, receiving pharmacy location, date and time the drug was received, drug name, quantity received, and the name of the person who received the drugs.

#### Control Point Transaction Review 

> \[PSA CP TRANSACTION REVIEW\]

The *Control Point Transaction Review* option reviews the receipt transactions processed for a selected control point transaction number. The report format is the same as the Purchase Order Review report.

#### Drug Receipt History Review 

> \[PSA DRUG HISTORY\]

The *Drug Receipt History Review* option reviews drugs received over a selected time range for a selected drug. One, many, or all drugs can be printed. The report lists the drug name, receiving pharmacy location, date and time the drug was received, quantity received, and the person’s name that received the drug.

#### Invoice Review 

> \[PSA INVOICE REVIEW\]

The *Invoice Review* option lists all receipts posted for a selected prime vendor invoice number. The report lists the invoice number, receiving pharmacy location, date and time the drug was received, quantity received, and the person’s name that received the drug.

### Dispensing Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DISPENSING MENU\]

When the *All Location Dispense/Purge* option is scheduled to run nightly, dispensing is collected automatically for all Automatic Replenishment/Ward Stock, Unit-Dose, IV, and Outpatient drugs that are housed in a pharmacy location. If new IV or Outpatient drugs are added to a location and the user wants to gather dispensing history for up to the last sixty days, the options on this menu may help.

Example: Dispensing Menu

1.  IV Dispensing (Single Drug)
2.  IV Dispensing (All Drugs)
3.  Outpatient Dispensing (Single Drug)
4.  Outpatient Dispensing (All Drugs)

#### IV Dispensing (Single Drug) 

> \[PSA IV SINGLE\]

The *IV Dispensing (Single Drug)* option collects intravenous (IV) dispensing information for a single drug in a location from the IV STATS file (#50.8). If present, the last IV collection date is used as a starting point. Otherwise, the user-selected date is used. The *Drug Transaction History* option can be run to produce a report with which to verify dispensing information. The report lists the pharmacy location that dispensed the IV, the date it was dispensed, total dispensed, price per dispense unit (PPDU), and total cost.

#### IV Dispensing (All Drugs) 

> \[PSA ALL DRUGS\]

The *IV Dispensing (All Drugs)* option collects IV dispensing information for all drugs from the IV STATS file (#50.8). If present, the last IV collection date is used as a starting point. Otherwise, the user needs to enter a date from which to begin collection. The report lists the pharmacy location that dispensed the IV, the date it was dispensed, total dispensed, price per dispense unit (PPDU), and total cost.

#### Outpatient Dispensing (Single Drug) 

> \[PSA OP SINGLE\]

The *Outpatient Dispensing (Single Drug)* option collects Outpatient (OP) dispensing information for a single drug from the PRESCRIPTION file (#52). If present, the last OP dispensing date is used as a starting point. Otherwise, the user will need to enter a date from which to begin collection. A report of the updating lists the drug name, date dispensed, total dispensed units dispensed, price per dispense unit (PPDU), dispense unit, total cost per date dispensed, and total cost for all dispensed dates.

#### Outpatient Dispensing (All Drugs) 

> \[PSA OP ALL DRUGS\]

The *Outpatient Dispensing (All Drugs)* option collects OP dispensing information for all drugs in this location from the PRESCRIPTION file (#52). If present, the last OP dispensing date is used as a starting point. Otherwise, the user will need to enter a date from which to begin collection.

A report of the updating lists the drug name, date dispensed, total dispensed units dispensed, price per dispense units (PPDU), dispense unit, total cost per date dispensed, and total cost for all dispensed dates.

### Maintenance Reports Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA GIP MAINTENANCE RPT MENU\]

The *Maintenance ReportsMenu* contains options that generate reports on balance adjustments, drug balances by location, monthly summary, and drug transaction history reports.

Example: Maintenance Reports Menu

1.  Balance Adjustments History
2.  Drug Balances by Location
3.  Drug Transaction History 4 Monthly Summary

5 Transfer Signature Sheet

#### Balance Adjustments History 

> \[PSA BALANCE ADJUSTMENTS REPORT\]

The *Balance Adjustments History* option reviews adjustments and transfers of a drug. The report lists the drug, transaction date and time, adjustment quantity, transfer quantity, transaction, adjustment reason, and pharmacy location that sent or received the transferred drug.

#### Drug Balances by Location 

> \[PSA DISPLAY LOCATION\]

The *Drug Balances by Location* option generates a report by pharmacy location listing each of its drugs’ names, quantity on hand, and dispense unit.

#### Drug Transaction History 

> \[PSA DRUG DISPLAY\]

The *Drug Transaction History* option provides a transaction history for one, many, or all drug(s) within the pharmacy location for a given date range. It lists the date range, drug, beginning date, beginning balance, transaction date and time, transaction quantity, transaction type, person who made the transaction, and resulting balance.

If the transaction is <u>receiving</u> drugs, the purchase order number, transaction number, and invoice number are also listed.

If the transaction is <u>dispensing</u>, the report designates where the dispensing took place (Inpatient Medications or Outpatient pharmacy).

#### Monthly Summary 

> \[PSA MONTHLY SUMMARY\]

The *Monthly Summary* option allows the user to print a pharmacy location’s detailed or summary monthly report of transactions made on one, many, or all drugs.

If the user selects the detailed report, the drug, beginning balance, total receipts, total dispensed, total adjustments, total transfers, and ending balance or one, many, or all drugs in the selected pharmacy location is printed.

If the user selects the summary report, the detailed report prints then a separate summary report follows. The summary report contains the drug, total receipts, total dispensed, total adjustments, and total transfers for one, many, or all drugs in the selected pharmacy location. A total line for the total receipts, total dispensed, total adjustments, and total transfers is printed.

#### Transfer Signature Sheet 

> \[PSA TRANSFER SIGNATURE SHEET\]

The *Transfer Signature Sheet* option prints a report of all transferred drugs within a specific date range. This report is used to record the signature of the person who received the drugs or to review transfer history.

Example: Transfer Signature Sheet

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: RIVERCHASE (IP)
3.  OUTPATIENT: PELHAM (OP)

Select Transfer from Pharmacy: (1-3): 1

Select the pharmacy location that will send the drugs to the other pharmacy location.

Choose the pharmacy location receiving the transferred drugs:

1.  INPATIENT: RIVERCHASE (IP)
2.  OUTPATIENT: PELHAM (OP)

Select Transfer to Pharmacy: (1-2): 2

Select the pharmacy location that will receive the drugs from the transferring pharmacy locations.

Beginning Date: 8 12 (AUG 12, 1997)

Ending Date : 8 12 (AUG 12, 1997)

DEVICE: HOME// *\[Select Print Device\]*-----------------------------------------report continues----------------------------------------Example: Transfer Signature Sheet (continued)

Enter the date range to print the transfer signature sheets.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>AUG 12,1997@12:40 D R U G A C C O U N T A B I L I T Y Page: 1</p>
<p>DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET</p>
<p>COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)</p>
<p>TRANSFERRED TO: OUTPATIENT: PELHAM (OP)</p>
<p>-----------------------------------------------------------------------------</p>
<p>TRANSFER DATE QTY DRUG NEW BALANCE</p>
<p>----------------------------------------------------------------------------- Aug 12, 1997@12:40 10 ACETAMINOPHEN 325MG TAB 50</p>
<p>Dispensed by: DAPHARMACIST51,THREE Rec'd by: ____________________________</p>
<p>(Full Name) (Full Name)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> \<This page is intentionally left blank.\>

# Section Two: Prime Vendor Interface Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA PRIME VENDOR INTERFACE\]

The *Prime Vendor Interface Menu* assists in the maintaining a perpetual drug inventory by interfacing with the prime vendor’s invoice data.

Example: Prime Vendor Interface Menu

1.  Pharmacy Location Maintenance Menu ...
2.  Dispensing Menu ...
3.  Orders Menu ... 4 Maintenance Reports Menu ...

### Pharmacy Location Maintenance Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA PV LOCATION MENU\]

The *Pharmacy Location MaintenanceMenu* contains options that set up and edit pharmacy locations. The drug balances can be initialized and adjusted. A new drug can be added to a pharmacy location or existing drug balances can be displayed. The drug stock and reorder levels can be entered and edited.

Example: Pharmacy Location Maintenance Menu

1.  Set Up/Edit a Pharmacy Location
2.  Balance Adjustments
3.  Balance Initialization
4.  Enter/Edit a Drug
5.  Enter/Edit Stock and Reorder Levels
6.  Transfer Drugs Between Pharmacies
7.  Setup Mail Message Recipients
8.  Outdated Medications

#### Set Up/Edit a Pharmacy Location 

> \[PSA LOCATION EDIT\]

The *Set Up/Edit a Pharmacy Location* option creates and edits a pharmacy location. The pharmacy location’s name, location type, and drugs can be entered and edited. If it is an Inpatient pharmacy location, wards can also be linked and unlinked. If it is an Outpatient pharmacy location, IV rooms can be linked and unlinked.

Creating the Pharmacy Location<u>About Pharmacy Locations</u>

Locations are Outpatient (OP), Inpatient (IP), or a Combined (IP/OP). More than one location is available - even more than one type of location (for instance, a multi-divisional facility might procure for several combined locations).

Create a location for each Inpatient or Outpatient site in order to track drug balances separately. Or, create a Combined location, like ALABASTER, that tracks Inpatient and Outpatient drug balances together.

<u>Choosing a Site Name</u>

How the site will track the drugs will depend on the type of pharmacy location that is chosen.

The three choices are Inpatient, Outpatient, or Combined.

- Inpatient: will track drugs only in the Inpatient dispensing site.
- Outpatient: will track drugs only in the Outpatient pharmacy/clinic.
- Combined: tracks all the drugs together in the Inpatient dispensing site and the Outpatient pharmacy/clinic. Only one total per drug is received.

A site is the physical location where drugs are stored and dispensed. If the facility maintains more than one Inpatient or Outpatient site, the user will be asked to choose a site for this pharmacy location.

> ![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/003.png)

> Multi-divisional facilities can track drugs in a variety of locations.

<u>Entering Wards for Inpatient Sites</u>

Assign wards to each Inpatient site. Each ward can be connected to only one Inpatient site. This information affects the gathering of IV and Unit Dose dispensing data.

Example: Create a Pharmacy Location—Single Inpatient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Prime Vendor Interface Menu Option: <strong>1</strong> Pharmacy Location Maintenance Menu</p>
<ol type="1">
<li><p>Set Up/Edit a Pharmacy Location</p></li>
<li><p>Balance Adjustments</p></li>
<li><p>Balance Initialization</p></li>
<li><p>Enter/Edit a Drug</p></li>
<li><p>Enter/Edit Stock and Reorder Levels</p></li>
<li><p>Transfer Drugs Between Pharmacies</p></li>
<li><p>Setup Mail Message Recipients</p></li>
<li><p>Outdated Medications</p></li>
</ol>
<p>Select Pharmacy Location Maintenance Menu Option: <strong>1</strong> Set Up/Edit a Pharmacy Location</p>
<p>Select one of the following:</p>
<ol type="1">
<li><p>INPATIENT</p></li>
<li><p>OUTPATIENT</p></li>
<li><p>COMBINED (IP/OP)</p></li>
</ol>
<p>Select Pharmacy type: <strong><u>1</u></strong> INPATIENT</p>
<p>Creating INPATIENT</p>
<p>For the purpose of collecting Unit Dose and IV dispensing data, any ward at which such dispensing might ever occur should be added. The ONLY reason to NOT add a ward would be if the dispensing at that ward should NOT update COMBINED (IP/OP).</p>
<blockquote>
<p><em>[There is NO harm in adding inactive wards.]</em></p>
</blockquote>
<p>INPATIENT is linked to 1 WEST, 1 SOUTH, 1 NORTH, 2 WEST, 2 SOUTH, 2 NORTH,</p>
<p>2 EAST, 1 EAST, 3 WEST, 3 EAST, 3 SOUTH, 4 EAST, 4 NORTH, 5 WEST, 5 EAST,</p>
<p>5 SOUTH, 6 WEST, 6 SOUTH, 7 EAST, 7 WEST, 8 EAST, 8 WEST.</p>
<p>Add/edit drugs? No// <strong>&lt;Enter&gt;</strong> NO</p>
<p>Maintain reorder levels: YES// <strong>&lt;Enter&gt;</strong></p>
<p>Days to keep invoice data: <strong>180</strong></p>
<p>Inactive Date: <strong>&lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Create a Pharmacy Location—Single OutpatientExample: Create a Pharmacy Location—Combined (Inpatient and Outpatient)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Pharmacy Location Maintenance Menu Option: <strong>1</strong> Set Up/Edit a Pharmacy Location</p>
<p>Select one of the following:</p>
<ol type="1">
<li><p>INPATIENT</p></li>
<li><p>OUTPATIENT</p></li>
<li><p>COMBINED (IP/OP)</p></li>
</ol>
<p>Select Pharmacy type: <strong>3</strong> COMBINED (IP/OP)</p>
<p>Creating COMBINED</p>
<p>For the purpose of collecting Unit Dose and IV dispensing data, any ward at which such dispensing might ever occur should be added. The ONLY reason to NOT add a ward would be if the dispensing at that ward should NOT update COMBINED (IP/OP).</p>
<p>COMBINED is linked to 1 WEST, 1 SOUTH, 1 NORTH, 2 WEST, 2 SOUTH, 2 NORTH,</p>
<p>2 EAST, 1 EAST, 3 WEST, 3 EAST, 3 SOUTH, 4 EAST, 4 NORTH, 5 WEST, 5 EAST,</p>
<p>5 SOUTH, 6 WEST, 6 SOUTH, 7 EAST, 7 WEST, 8 EAST, 8 WEST.</p>
<p>Outpatient site selection affects the collection of dispensing data.</p>
<p>OUTPATIENT SITE: // <strong>MAYLENE</strong></p>
<p>Add/edit drugs? NO// <strong>&lt;Enter&gt;</strong> NO</p>
<p>MAYLENE Outpatient Site</p>
<p>Link or unlink Iv room (L/U): <strong>L</strong>ink</p>
<p>Enter the IV rooms that receive IVs from the outpatient site.</p>
<p>Select IV ROOM NAME: <strong>MAYLENE</strong> IV ROOM #1</p>
<p>Select IV ROOM NAME: <strong>&lt;Enter&gt;</strong></p>
<p>MAYLENE Outpatient Site</p>
<p>IV rooms to be linked: MAYLENE IV ROOM #1</p>
<p>Should the IV rooms be linked? N// <strong>Y</strong>ES</p>
<p>Linking IV rooms.</p>
<p>The IV rooms were linked successfully.</p>
<p>Maintain reorder levels: YES// <strong>&lt;Enter&gt;</strong></p>
<p>Days to keep invoice data: <strong>180</strong></p>
<p>Inactive Date: <strong>&lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<u>Changing a Pharmacy Location Type</u>

- The user can change a Combined location to a separate Inpatient and Outpatient location. If the Outpatient activity needs to be tracked, the user must create an Outpatient location.
- A site with an existing Inpatient and Outpatient location can be changed to a Combined location.

#### Balance Adjustments 

> \[PSA BALANCE ADJUSTMENTS\]

The *Balance Adjustments* option allows the user to review and/or enter an adjustment to correct the balance of a drug.

This option is locked by the PSAMGR key.

#### Balance Initialization 

> \[PSA BALANCE INITIALIZE\]

The *Balance Initialization* option establishes the balance for any drugs that do not yet have a balance.

#### Enter/Edit a Drug 

> \[PSA PV DRUG ENTER/EDIT\]

The *Enter/Edit a Drug* option adds a new drug to the pharmacy location. If the drug is being added to the location and the location maintains stock and reorder levels, it prompts for the stock and reorder levels. It also displays the balance of an existing drug.

#### Enter/Edit Stock and Reorder Levels 

> \[PSA STOCK AND REORDER LEVELS\]

The *Enter/Edit Stock and Reorder Levels* option flags a pharmacy location or master vault to maintain or not maintain the stock and reorder levels. If the flag is set to YES, the user enters the drugs’ stock and reorder levels. These levels are used to determine if a mail message should be sent with the drugs that need to be ordered. Only holders of the PSJ RPHAM pharmacist key can set levels in master vaults.

The mail message is sent to the holders of the PSA ORDERS key. It is sent if at least one drug’s balance is equal to or less than the reorder level. The message lists the drug name, stock level, current balance, and number of dispense units to order for the pharmacy location or master vault. The number of dispense units to order is determined by subtracting the current balance from the stock level. If the user is not a pharmacist, only the pharmacy location data is sent. If the user is a pharmacist, the pharmacy location and master vault data are sent.

#### Transfer Drugs Between Pharmacies 

> \[PSA TRANSFER DRUGS\]

The *Transfer Drugs Between Pharmacies* option allows a pharmacist to move drugs between pharmacy locations. The number of dispense units to be moved is subtracted from the dispensing pharmacy location and added to the receiving pharmacy location. A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET may be printed after all transfers are completed.

This option is locked by the PSAMGR and PSJ RPHARM keys.

Example: One Active Pharmacy Location

There is only one active pharmacy location.

There must be at least two to transfer drugs.

If there is only one active pharmacy location, the user is exited from the option.

Example: More than One Active Pharmacy Location

Enter your Current Signature Code: SIGNATURE VERIFIED

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: PELHAM (IP)
3.  OUTPATIENT: HELENA (OP)

Select Transfer from Pharmacy: (1-3): 1

Select the pharmacy location that will transfer the drug. This pharmacy location will have its drug balance decreased when the transfer is complete.

Example: Transfer Drugs between Pharmacies

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

Select DRUG: ACETAMINOPHEN 325MG TAB CN103

Dispense Unit: TAB Current Balance: 60

Enter Quantity to Transfer: (1-60): 10

Select the drug and number of dispense units to be transferred.

Choose the pharmacy location receiving the transferred drugs:

1.  INPATIENT: PELHAM (IP)
2.  OUTPATIENT: HELENA (OP)

Select Transfer to Pharmacy: (1-2): 2

Select the pharmacy that will receive the drug. Its balance will be increased when the transfer is complete.

INPATIENT: HELENA (OP) does not stock ACETAMINOPHEN 325MG TAB!

Do you want to continue? YES

Answer yes if it is okay to now stock this drug in the receiving pharmacy location.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>----------------------------------------------------------------------------- ACETAMINOPHEN 325MG TAB</p>
<p>Transferring: 10 (TAB)</p>
<p>From: COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)</p>
<p>To : OUTPATIENT: HELENA (OP)</p>
<p>-----------------------------------------------------------------------------</p>
<p>Is this OK? NO// <strong>YES</strong></p>
<p>Updating pharmacy on-hand balances now............. Done!</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the displayed transfer information is correct, enter YES. The drug balance in the transferring pharmacy location is decreased. The drug balance in the receiving pharmacy location is increased. If the drug is new to the receiving pharmacy location, a mail message is sent to holders of the PSAMGR key letting them know that a new drug is being added to that location. The mail message lists the drug, dispense unit, number of dispense units transferred, pharmacist who initiated the transfer, transferring pharmacy location, and the receiving pharmacy location.

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP) Select DRUG: \<Enter\>-----------------------------------------report continues----------------------------------------

If there are more drugs to be transferred to the *same* pharmacy location, the user can select them now. If not, press \<ENTER\> to select the next transferring pharmacy location.

Example: Transfer Drugs between Pharmacies

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: PELHAM (IP)
3.  OUTPATIENT: HELENA (OP)

Select Transfer from Pharmacy: (1-3): ^

If the user wants to transfer drugs from another pharmacy location, select that location now. If the user is finished transferring drugs, enter \<^\>.

Print transfer signature sheets? Y// \<Enter\>

DEVICE: HOME// *\[Select Print Device\]*

A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET can be printed at this

time for all the transfers just entered. This sheet prints the transfer data for each unique combination of pharmacy locations. It is used to record the signature of the person who received the drugs. See the *Transfer Signature Sheet* option for an example of this sheet.

#### Setup Mail Message Recipients 

> \[PSA MSG RECIPIENTS\]

The *Setup Mail Message Recipients* option is used to enter/delete personnel from the two mail groups used for notifying personnel of a change in NDC and/or Drug Price, and when drugs are below reorder levels.

See Section 3.3.7 under The Orders Menu for more detailed information.

This option is locked with the PSAMGR key.

#### Outdated Medications 

> \[PSA OUTDATED MEDICATIONS\]

The *Outdated Medications* option gives the user the ability to select and store drugs that are to be returned to the manufacturer.

This option is locked with the PSAMGR key.

NOTES:

Marking a drug as Returned to Manufacturer does not create any adjustment to inventory quantities.

This option should only be used for non-controlled substances. Controlled substances that are to be returned should be documented in the Controlled Substances package.

Example: Enter Outdated Medications to Return to Manufacturer

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Drug Accountability Menu Option: <strong>PHAR</strong>macy Location Maintenance Menu Select Pharmacy Location Maintenance Menu Option: <strong>8</strong> Outdated Medications</p>
<p>Select one of the following:</p>
<ol type="1">
<li><p>Print Report</p></li>
<li><p>Enter drugs Return to Manufacturer</p></li>
</ol>
<p>Enter response: <strong>2</strong> Enter drugs Return to Manufacturer</p>
<p>Scan Drug barcode or enter a drug name :</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

At this point you can scan a barcode to enter the drug.

Scan Drug barcode or enter a drug name: 028105004806

The software is programmed to try to match the item in several different ways. If the item cannot be located, the user will prompted to enter a drug name.

Select Drug : ACETA

1.  ACETAMINOPHEN 1000MG TABLET CN100
2.  ACETAMINOPHEN 325MG C.T. CN103
3.  ACETAMINOPHEN 325MG TABLET CN103
4.  ACETAMINOPHEN 650MG SUPPOS. CN103 02-03-01
5.  ACETAMINOPHEN ELIX. 160MG/5ML 4OZ CN103

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 3 ACETAMINOPHEN 325MG TABLET

Once the correct drug is entered, additional information is requested.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Number of containers : <strong>1</strong></p>
<p>Quantity being returned: : <strong>100</strong></p>
<p>Package type: BT// &lt;<strong>Enter</strong>&gt; BOTTLE</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Pressing the Enter key automatically selects the default value shown to the left of the double slashes</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Is it ok to file the data entered? YES// Updating Destruction holding file.</p>
<p>Updating Drug Accountability Transaction file.</p>
<p>Enter RETURN to continue or '^' to exit: <strong>^</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After all items have been selected, the program will ask if a report is desired.

> Would you like to print the returns report ? YES// \<Enter\>

> If you are returning the items to the manufacturer at this time, the program will add today's date to the item to show when it was actually returned.

> Are you returning the items to the manufacturer at this time? YES// \<Enter\>

The default start date for the report is 90 days in the past. In this example the report was requested on January 11, 2006.

Beginning Date: OCT 13, 2005// \<Enter\> (OCT 13, 2005)

DEVICE: HOME// \<Enter\> GENERIC INCOMING TELNET

This report can also be run when the manufacturer arrives to receive the medications. When the report is generated, the date is added to the item in the file for future reference.

### Dispensing Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DISPENSING MENU\]

The *Dispensing Menu* contains options that assist with the gathering of dispensing activity from other Pharmacy packages.

Example: Dispensing Menu

1.  IV Dispensing (Single Drug)
2.  IV Dispensing (All Drugs)
3.  Outpatient Dispensing (Single Drug)
4.  Outpatient Dispensing (All Drugs)

#### IV Dispensing (Single Drug) 

> \[PSA IV SINGLE\]

The *IV Dispensing (Single Drug)* option collects IV dispensing information for a single drug in a location from the IV STATS file (#50.8). If present, the last IV collection date is used as a starting point. Otherwise, the user-selected date is used. The *Drug Transaction History* option can be run to produce a report with which to verify dispensing information. The report lists the pharmacy location that dispensed the IV, the date it was dispensed, total dispensed, price per dispense unit (PPDU), and total cost.

#### IV Dispensing (All Drugs) 

> \[PSA ALL DRUGS\]

The *IV Dispensing (All Drugs)* option collects IV dispensing information for all drugs from the IV STATS file (#50.8). If present, the last IV collection date is used as a starting point. Otherwise, the user needs to enter a date from which to begin collection. The report lists the pharmacy location that dispensed the IV, the date it was dispensed, total dispensed, price per dispense unit (PPDU), and total cost.

#### Outpatient Dispensing (Single Drug) 

> \[PSA OP SINGLE\]

The *Outpatient Dispensing (Single Drug)* option collects OP dispensing information for a single drug from the PRESCRIPTION file (#52). If present, the last OP dispensing date is used as a starting point. Otherwise, the user will need to enter a date from which to begin collection. A report of the updating lists the drug name, date dispensed, total dispensed units dispensed, price per dispense units (PPDU), dispense unit, total cost per date dispensed, and total cost for all dispensed dates.

#### Outpatient Dispensing (All Drugs) 

> \[PSA OP ALL DRUGS\]

The *Outpatient Dispensing (All Drugs)* option collects OP dispensing information for all drugs in this location from the PRESCRIPTION file (#52). If present, the last OP dispensing date is used as a starting point. Otherwise, the user will need to enter a date from which to begin collection.

A report of the updating lists the drug name, date dispensed, total dispensed units dispensed, price per dispense units (PPDU), dispense unit, total cost per date dispensed, and total cost for all dispensed dates.

### Orders Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA ORDERS MENU\]

The *Orders Menu* allows the user to process, verify, and print prime vendor invoices. It also allows memo data to be entered.

This option is locked by the PSA ORDERS key.

Example: Orders Menu

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th>Process Uploaded Prime Vendor Invoice Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>Verify Invoices</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>Print Orders</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>Credit Resolution</td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>Edit Verified Invoices</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>Delete Un-processed Invoices</td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>Setup Mail Message Recipients</td>
</tr>
</tbody>
</table>

> **NOTE:** With the release of patch PSA\*3\*26, the past *Upload and Process Prime Vendor*

> *Invoice Data* option (on the *Orders Menu* option) is replaced with a Graphical User Interface (GUI) program which performs this function. See Section Three: GUI Upload Program for more information.

#### Process Uploaded Prime Vendor Invoice Data 

> \[PSA PROCESS PRIME VENDOR DATA\]

Processing an invoice is matching the line items to the DRUG file (#50) and validating the invoice. To validate the invoice, the processor confirms all line item data. If the quantity received is different than the invoice quantity, the processor enters an adjustment. The processor also validates the drug, unit price, order unit, and the dispense units per order unit (DUOU). If the pharmacy location or master vault is flagged to maintain stock levels, the first time the drug is received the processor may enter the stock and reorder levels. Anyone holding the PSA ORDERS key can process the invoice.

This option is locked by the PSA ORDERS key

Example: Process Uploaded Prime Vendor Invoice Data

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Orders Menu Option: <strong>PROC</strong>ess Uploaded Prime Vendor Invoice Data</p>
<p>Enter your Current Signature Code: SIGNATURE VERIFIED</p>
<p>The invoices are being assigned to the pharmacy location. Please wait....</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

-----------------------------------------report continues----------------------------------------

If there is only one pharmacy location and the invoice contains at least one drug that is not marked as a controlled substance, the software automatically assigns the invoice to the pharmacy location.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

If there is more than one active pharmacy location, the active locations are listed. The user is asked to assign the invoice to one of the locations.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;&lt;&lt; ASSIGN A PHARMACY LOCATION SCREEN &gt;&gt;&gt;</p>
<p>----------------------------------------------------------------------------- 1. COMBINED (IP/OP): ALABASTER VAMC INPATIENT (IP)</p>
<p>ALABASTER VAMC OUTPATIENT (OP) 2. OUTPATIENT: PELHAM CLINIC (OP)</p>
<p>Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 1997</p>
<p>Some controlled substances</p>
<p>Pharmacy Location: (1-2): <strong>1</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** If controlled substances were found on the invoice one of two things will happen.

1)  If the invoice contains drugs that are marked as a controlled substance and drugs that are not marked as controlled substances, the user will assign a master vault and pharmacy location to the invoice. When the pharmacy location is assigned the message “Some controlled substances” will appear below the invoice data to let the user know that a master vault will be assigned, as shown on the previous box.
2)  If all of the drugs are marked as a controlled substance the user will only assign the invoice to a master vault. If all of the drugs are marked as a controlled substance, the message “\*\*All controlled substances” will appear below the invoice data to let the user know that a pharmacy location was not assigned, as shown in the box below.

If NO drugs were marked as a controlled substance, the invoice will only be assigned to a pharmacy location.

\<\<\< ASSIGN A MASTER VAULT SCREEN \>\>\>

----------------------------------------------------------------------------- 1. MASTER VAULT 1

2\. MASTER VAULT 2

Order#: C2529410 Invoice#: 54733371 Invoice Date: Jan 07, 1997

\*\* All controlled substances

Select Master Vault: (1-2): 2

Enter RETURN to continue or '^' to exit: \<Enter\>-----------------------------------------report continues---------------------------------------- If there is more than one active master vault, the active ones are listed and the user is asked to assign the invoice to one of the vaults.

If there is only one master vault and the invoice contains at least one drug that is marked as a controlled substance, the invoice is automatically assigned to the master vault.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

The invoices are being assigned to the master vault. Please wait..

\<\<\< PROCESS ENTIRE INVOICE SCREEN \>\>\>

No errors have been detected on the following invoices. If there are no corrections, you can change the invoices' status to "Processed" by selecting them from the list. If you do have corrections, press the return key then a second list will be displayed. You will be able to choose the invoices from that list and enter corrections.

Choose the invoices from the list you want to process.

=============================================================================

1\. Order#: C5914005 Invoice#: 5471741 Invoice Date: Jul 07, 1997

=============================================================================

Select invoices to process: (1-1): 1-----------------------------------------report continues----------------------------------------

There are three reasons, or a combination of the three reasons, why invoices will be listed on the PROCESS ENTIRE INVOICE SCREEN. Use the chart to help decide which actions to take.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>(1) If all of the invoices are <u>supply</u> invoices, whose items will never be in the DRUG file (#50), the entire invoice can be processed at one time.</th>
<th>Select those invoices for processing.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>(2) If all the invoices contained <u>drugs</u> that were <u>found</u> in the DRUG file (#50) and all required data was also found.</td>
<td>Select those invoices for processing.</td>
</tr>
<tr class="even">
<td>(3) If all the invoices contained <u>drugs</u> that were <u>not found</u> in the DRUG file (#50), it flags it as a possible supply invoice. This will probably occur more often in the beginning because more items will not be matched to the DRUG file (#50).</td>
<td>Do not choose this invoice for processing. Press <strong>&lt;Enter&gt;</strong>. This will take the user to another screen so the line items can be edited.</td>
</tr>
<tr class="odd">
<td>(4) If there is a <u>combination</u> of invoices that contain all supply items or all drugs found together with drugs that have not been found.</td>
<td><p>Select only those invoices that contain all supply items or all found drugs for processing.</p>
<p>After processing the above invoices, another screen will be displayed for editing the line items not found.</p></td>
</tr>
</tbody>
</table>

| \(5\) If all of the invoices contained drugs that were not found. | Press \<Enter\>. The user will be taken to another screen to be able to edit the invoices. |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------|

Example: Process Uploaded Prime Vendor Invoice Data (continued)All Supply Items

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;&lt;&lt; PROCESS ENTIRE INVOICE SCREEN &gt;&gt;&gt;</p>
<p>Order#: 97038069 Invoice#: 016187568 Invoice Date: Feb 19, 1997</p>
<p>============================================================================</p>
<p>Are all the items on the invoice supply items? N// <strong>Y</strong>ES</p>
<p>Are you sure? Y// <strong>&lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The invoice’s status will be changed to Processed.

All Drugs Found

\<\<\< PROCESS ENTIRE INVOICE SCREEN \>\>\>

Order#: Y5014006 Invoice#: 5473337 Invoice Date: Feb 07, 1997

============================================================================ Date received: Feb 07, 1997// \<Enter\>

The invoice status has been changed to Processed!

The invoice’s status will be changed to Processed.

All Drugs Not Found in DRUG File (#50)

\<\<\< PROCESS ENTIRE INVOICE SCREEN \>\>\>

Order#: 97038069 Invoice#: 016187568 Invoice Date: Feb 19, 1997

============================================================================

Are all the items on the invoice supply items? N// \<Enter\>

If this type of invoice was selected in error, answer NO to the prompt and the user will be returned to the PROCESS ENTIRE INVOICE SCREEN.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; EDIT INVOICES TO BE PROCESSED SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>More data is needed on the following invoices. Choose the invoices from the list you want to edit.</p>
<p>----------------------------------------------------------------------------- 1. Order#: C2529410 Invoice#: 071070 Invoice Date: Jan 09, 1997</p>
<p>2. Order#: C2529410 Invoice#: 54733371 Invoice Date: Jan 07, 1997</p>
<p>-----------------------------------------------------------------------------</p>
<p>Select invoices to edit: (1-2): <strong>1,2</strong></p>
<p>Do you want to select the line items to be edited (S) or</p>
<p>have them automatically (A) displayed for you?: (S/A): A//<strong>&lt;Enter&gt;</strong> automatically displayed</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

-----------------------------------------report continues----------------------------------------

Select the invoices that need to be edited.

If the user chooses to select the line items to be edited (S), the user will have to know which information is missing/incorrect. If the user chooses to have the line items automatically (A) displayed, the software will prompt for only missing/incorrect information. When this method of processing is chosen, the software may read some information as correct such as the quantity received, when in fact a bottle was broken in shipment. The user will need to change this information on the “last chance edit” screen that will appear after the software finishes automatically processing the invoice. It is suggested that the user select automatic display.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

\<\<\< EDIT INVOICES TO BE PROCESSED SCREEN \>\>\>

Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 2006

-----------------------------------------------------------------------------

MASTER VAULT: ALABASTER

PHARMACY LOCATION:

COMBINED (IP/OP): ALABASTER VAMC INPATIENT (IP)

ALABASTER VAMC OUTPATIENT (OP)

Date received: Jul 07, 1997// 7 8

If the drugs were not received on the default date, enter the correct date at this time. Both of the dates will be stored for future reference.

In the example below, the software displays the first line item with <u>missing</u> or <u>incorrect</u> data.

Automatic Processing - Drug Found in DRUG File (#50)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; PROCESS LINE ITEM SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 2006</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 DACARBAZINE 100MG INJ</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 5</p>
<p>Order Unit : CT NDC: 000836-4565-10</p>
<p>Unit Price : $4.48 VSN: 562188</p></td>
</tr>
<tr class="odd">
<td>PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000 PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1</td>
</tr>
<tr class="even">
<td><p>Dispense Units: TAB</p>
<p>Dispense Units Per Order Unit: Blank</p>
<p>Stock Level : 1200</p>
<p>Reorder Level : 600</p>
<p>DISPENSE UNITS: TAB</p>
<p>DISPENSE UNIT PER ORDER UNIT: <strong>1000</strong></p></td>
</tr>
</tbody>
</table>

-----------------------------------------report continues----------------------------------------

The drug was found in the DRUG file (#50) and only dispense units per order unit (DUOU) was missing.

Example: Process Uploaded Prime Vendor Invoice Data (continued)National Drug File (NDF) Used for Suggested Match

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; PROCESS LINE ITEM SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>Order#: H7564729 Invoice#: 1448168 Invoice Date: Mar 31, 2006</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 UNKNOWN ITEM</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 1</p>
<p>Order Unit : EA NDC: 000024-0325-02 Unit Price : $21.26 VSN: 000083</p></td>
</tr>
<tr class="odd">
<td>PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000 PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1</td>
</tr>
<tr class="even">
<td><p>Dispense Units: Blank</p>
<p>Dispense Units Per Order Unit: Blank</p>
<p>Stock Level : Blank</p>
<p>Reorder Level : Blank</p>
<p>The NDC has the VA Product Name of DACARBAZINE 100MG/VIL INJ</p>
<p>Is DACARBAZINE 100MG/VIL INJ the drug you received? N// <strong>YES</strong></p></td>
</tr>
</tbody>
</table>

The drug could not be found in the DRUG file (#50) but the NDC and its corresponding VA product name was located in the NDF. The DRUG file (#50) contains (1) one drug with the same VA product name. If the drug with the same VA product name is the actual drug that was received, answer YES and the drugs data will be redisplayed on the screen. If it was not, answer NO and then the user will be able to select the correct drug from the DRUG file (#50).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; PROCESS LINE ITEM SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>Order#: 97045660 Invoice#: 016187424 Invoice Date: Feb 19, 2006</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 UNKNOWN ITEM</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 1</p>
<p>Order Unit : VI NDC: 000264-7800-00 Unit Price : $13.48 VSN: 337485</p>
<p>PV-Drug-Description : HYDROCORT AC CRM 1% ALP 30GM@ PV-DUOU : 28.4</p>
<p>PV-Drug-Generic Name : HYDROCORTISONE PV-Units: 1</p>
<p>Dispense Units: Blank</p>
<p>Dispense Units Per Order Unit: Blank</p>
<p>Stock Level : Blank</p>
<p>Reorder Level : Blank</p>
<p>The NDC has the VA Product Name of HYDROCORTISONE 1% CREAM,TOP The following drugs have the same VA Product Name.</p>
<ol type="1">
<li><p>HYDROCORTISONE 1% CREAM</p></li>
<li><p>HYDROCORTISONE 1% CREAM JAR</p></li>
</ol>
<p>Select the received drug or</p>
<p>enter "^" to select the drug from the DRUG file.: (1-5):<strong>1</strong></p></td>
</tr>
</tbody>
</table>

-----------------------------------------report continues---------------------------------------- The drug could not be found in the DRUG file (#50) but the NDC and its corresponding VA

product name was located in the NDF. The DRUG file (#50) contains multiple drugs with the same VA product name. If one of the drugs listed is the actual drug that was received, the user can select it. If it was not, enter an \<^\> to select the drug from the DRUG file (#50).

Example: Process Uploaded Prime Vendor Invoice Data (continued)Vendor’s Stock Number has Changed

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; PROCESS LINE ITEM SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 2006</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 DACARBAZINE 100MG INJ</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 2</p>
<p>Order Unit : BT NDC: 000034-5624-01 Unit Price : $7.57 VSN: 627635</p></td>
</tr>
<tr class="odd">
<td>PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000 PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1</td>
</tr>
<tr class="even">
<td><p>Dispense Units: TAB</p>
<p>Dispense Units Per Order Unit: 300</p>
<p>Stock Level : 2000</p>
<p>Reorder Level : 2000</p>
<p>There is a change in NDC’s Vendor Stock Number (VSN).</p>
<p>New VSN: 627635</p>
<p>Old VSN: 327635</p>
<p>Is the new VSN correct? Y// <strong>&lt;Enter&gt;</strong></p></td>
</tr>
</tbody>
</table>

If the new vendor stock number is correct, it will overwrite the old. If the old vendor stock number is correct, the new vendor stock number will be discarded.

Multiple Drugs in DRUG File (#50) with the Same NDC and VSN

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; PROCESS LINE ITEM SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>Order#: C5014006 Invoice#: 5473337 Invoice Date: Oct 07, 2006</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 UNKNOWN ITEM</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 12</p>
<p>Order Unit : BT NDC: 999999-9999-99</p>
<p>Unit Price : $0.81 VSN: 051219</p>
<p>PV-Drug-Description : HYDROCORT AC CRM 1% ALP 30GM@ PV-DUOU : 28.4 PV-Drug-Generic Name : HYDROCORTISONE PV-Units: 1</p>
<p>Dispense Units: GM</p>
<p>Dispense Units Per Order Unit: 28.4</p>
<p>Stock Level : 600 Reorder Level : 600</p>
<p>There is more than one item in the DRUG file with the same NDC and Vendor Stock Number.</p>
<ol type="1">
<li><p>HYDROCORTISONE 1% CREAM</p></li>
</ol>
<p>Order Unit: EA Price Per Order Unit : $0.81</p>
<p>Vendor: DRUGS CORPORATION VSN: 051219</p>
<ol start="2" type="1">
<li><p>HYDROCORTISONE 1% CREAM JAR</p></li>
</ol>
<p>Order Unit: BT Price Per Order Unit : $0.81 Vendor: DRUGS CORPORATION VSN: 051219 3. Select another drug.</p></td>
</tr>
</tbody>
</table>

Select the invoiced drug: (1-3): <sup>1</sup>-----------------------------------------report continues----------------------------------------

If the received drug is listed, select that drug. If not, choose “Select another drug”, and the user will be able to choose the correct drug from the DRUG file (#50).

Example: Process Uploaded Prime Vendor Invoice Data (continued)Drug Not Found in NDF and DRUG File (#50)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;&lt;&lt; PROCESS LINE ITEM SCREEN &gt;&gt;&gt;</p>
<p>Order#: C2529411 Invoice#: 071070 Invoice Date: Jan 09, 2006</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 UNKNOWN ITEM</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 12</p>
<p>Order Unit : Blank NDC: 000013-8303-04</p>
<p>Unit Price : $95.00 VSN: 014142</p></td>
</tr>
<tr class="odd">
<td>PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000 PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1</td>
</tr>
<tr class="even">
<td><p>Dispense Units: Blank</p>
<p>Dispense Units Per Order Unit: Blank</p>
<p>Stock Level : Blank</p>
<p>Reorder Level: Blank</p>
<p>If the item will never be in the DRUG, press the Return key then answer YES to the “Is this a supply item?” prompt. To bypass this line item, enter “^” then press the Return key.</p>
<p>Select Drug: <strong>DACARBAZINE 100MG INJ</strong> TAB MS200 N/F</p></td>
</tr>
</tbody>
</table>

Screen Display with Updated Data from a Drug Match

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; PROCESS LINE ITEM SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 2006</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 DACARBAZINE 100MG INJ</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 12</p>
<p>Order Unit : (Blank) NDC: 000013-8303-04 Unit Price : $95.00 VSN: 014142</p></td>
</tr>
<tr class="odd">
<td>PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000 PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1</td>
</tr>
<tr class="even">
<td><p>Dispense Units: TAB</p>
<p>Dispense Units Per Order Unit: Blank</p>
<p>Stock Level : 1200</p>
<p>Reorder Level : 600</p>
<p>DISPENSE UNITS: TAB</p>
<p>DISPENSE UNIT PER ORDER UNIT: <strong>100</strong></p></td>
</tr>
</tbody>
</table>

When the drug is selected, the screen clears and the same line item is displayed with the selected drug’s data. The drug-specific data displayed is in the second half of the display -- Dispense Units, Dispense Units Per Order Unit (DUOU), Stock Level, and Reorder Level.

> Do you want to change the invoice's status to Processed? NO

The software has detected no missing or incorrect data. If the user thinks any of the data is incorrect, answer NO, and the chance to make corrections in the next screen is given. If the user has no corrections to make, answer YES.

The user will also be able to make corrections in the next screen, but be forewarned, if the edited information is found “valid” by the software the status WILL BE CHANGED to “Processed” and the invoice will be passed to the verifier.

> \*\* The invoice's status has not been changed to Processed.

-----------------------------------------report continues---------------------------------------- If the software found missing or incorrect data, the invoice cannot be placed in a processed status. The invoice’s data can be edited by selecting the “last chance edit” or by reentering the option then selecting automatic display.

Example: Process Uploaded Prime Vendor Invoice Data (continued)Last Chance Edit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>If you are changing the status of an invoice to Processed, this is the last time you will be allowed to edit it before it goes to the verifier. If you are not changing the status of an invoice to Processed, you can edit it now.</p>
<p>You can edit the invoice's delivery date, pharmacy location, master vault, and the line item's drug, quantity received, order unit, and dispense units per order unit. The reorder level can be edited if the pharmacy location or master vault is set up to track the reorder levels.</p>
<p>Edit invoices? N// <strong>YES</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the answer is NO, the option will exit. If the answer is YES, the user will be able to select the invoice and line items to be edited plus having the ability to edit the assigned pharmacy location and/or master vault.

Yes to last chance edit or if you choose to select the line items to be edited (instead of automatic display)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;&lt;&lt; EDIT INVOICE SCREEN &gt;&gt;&gt;</p>
<p>Choose the invoices to be edited. You can edit the invoice's date received and the line item's drug, quantity received, and order unit. The reorder level can be edited if the pharmacy location or master vault is set up to track the reorder levels.</p>
<p>-----------------------------------------------------------------------------</p>
<ol type="1">
<li><p>Order#: C2529410 Invoice#: 071070 Invoice Date: Jan 09, 1997</p></li>
<li><p>Order#: C2529410 Invoice#: 54733371 Invoice Date: Jan 07, 1997</p></li>
</ol>
<p>Select invoices: (1-2): <strong>1</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

\<\<\< EDIT INVOICE SCREEN \>\>\>

Order#: C2529410 Invoice#: 071070 Invoice Date: Jul 07, 1997

----------------------------------------------------------------------------- Date received: Jul 08, 1997// \<Enter\>

MASTER VAULT: PELHAM CLINIC

Select Master Vault: PELHAM CLINIC// \<Enter\>

COMBINED (IP/OP): Louisville Inpatient Medications (IP)

Louisville Outpatient Pharmacy (OP) Select Pharmacy Location: COMBINED (IP/OP)// \<Enter\>

Line Item Numbers: 562188,627635

Select Line Item Number: 562188-----------------------------------------report continues----------------------------------------The user can change the date the drugs were actually received. The pharmacy location and/or master vault that will receive the drugs on the invoice can also be changed. At “Line Item Numbers”, <u>all</u> of the line numbers will be listed to reference when the user is entering the line number at the line number prompt. The user is not allowed to enter a range of numbers. Enter one line number; make the edits, and then another “Select Line Item Number” prompt is displayed. When the user is finished making the corrections, press \<Enter\> at the “Select Line Item Number” prompt.Note: If the prime vendor is AmeriSource Health Services, the line numbers are the vendor stock numbers for the line item’s drug.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;&lt;&lt; EDIT INVOICE SCREEN &gt;&gt;&gt;</p>
<p>Order#: C2529411 Invoice#: 071070 Invoice Date: Jul 07, 2006</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 DACARBAZINE 100MG INJ</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 5</p>
<p>Order Unit : CT NDC: 000536-4565-10</p>
<p>Unit Price : $4.48 VSN: 262188</p></td>
</tr>
<tr class="odd">
<td>PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000 PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1</td>
</tr>
<tr class="even">
<td><p>-----------------------------------------------------------------------------</p>
<ol type="1">
<li><p>Drug</p></li>
<li><p>Quantity Received</p></li>
<li><p>Order Unit</p></li>
<li><p>Dispense Units Per Order Unit</p></li>
</ol>
<p>Edit fields: (1-4): <strong>2</strong></p>
<p>QUANTITY RECEIVED: 5// <strong>4</strong></p>
<p>ADJUSTMENT REASON: <strong>1 CARTON WAS NOT DELIVERED</strong></p>
<p>Do you want to change the invoice's status to Processed? <strong>Y</strong>ES</p></td>
</tr>
</tbody>
</table>

Enter YES if the invoice is completely correct. The user will not be able to edit it again when the option is exited. Enter NO if the user needs to edit the invoice again. This is accomplished by selecting the *Process Uploaded Prime Vendor Invoice Data* option.

Invoices that have been moved to the status of Processed are reviewed for notable changes of

Order Units, Dispense Units Per Order Unit (DUOU), Price Per Dispense Unit (PPDU), and

NDCs. If there are changes the user is presented an informational note on their screen and then a

PRE Verification 'Order' : 'Invoice' Variance Report Mailman message is sent to the G.PSA NDC UPDATES mail group.

Example: Informational Note

PRE Verify C502395300 : 7229924053 Variance Report

Noted differences between the invoice line items and the drug file have been found. A mail message is being sent to G.PSA NDC UPDATES.

Please check the message for accuracy.

\<cr\> - continue:

Example: Mailman Message

Subj: PRE Verify C502395300 : 7229924053 Variance Report \[#1986002\]

04/01/05@18:29 11 lines

From: PSAperson,One In 'IN' basket. Page 1

------------------------------------------------------------------------------- PRE Verify C502395300 : 7229924053 Variance Report

Example: Process Uploaded Prime Vendor Invoice Data (continued)

1.  ACETAMINOPHEN WITH CODEINE 30MG

DUOU Old: 485 New: 1000

OU Old: CO New: BT

PPDU Old: 1.2371 New: 0.6000

2.  METHADONE 10MG TAB

DUOU Old: 40 New: 100 PPDU Old: 0.1938 New: 0.0771

#### Verify Invoices 

> \[PSA VERIFY INVOICES\]

The *Verify Invoices* option validates processed invoices. The verifier and processor cannot be the same person. If the invoice contains at least one drug marked as a controlled substance, only pharmacists holding the PSA ORDERS key can verify the invoice.

This option is locked by the PSA ORDERS key.

> **IMPORTANT:** Once verified, the drug balances are incremented in the pharmacy location and/or master vault.

The following condition must be met to update the NDC field (#31).

- If the invoice NDC is different from the NDC field (#31), the NDC field (#31) is overwritten with the invoiced NDC.

The following condition must be met to update the PRICE PER ORDER UNIT field (#13) and PRICE PER DISPENSE UNIT field (#16).

- If the invoiced price per order unit (PPOU) is different than the PRICE PER ORDER UNIT field (#13), the PRICE PER ORDER UNIT field (#13) is overwritten with the new prorated price per order unit (PPOU). The PRICE PER DISPENSE UNIT field (#16) is also overwritten with the new prorated price per dispense unit (PPDU).

Example: Verify InvoicesNo Invoice(s) to be Verified Messages

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>There is at least one invoice that needs to be verified. However, invoices cannot be verified by the same person who processed them and a pharmacist must verify invoices that contain a drug marked as a controlled substance.</p>
<p>There are no invoices you can verify because the invoice(s) meet one of the above conditions.</p>
<p>There are no invoices that need to be verified.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Invoice(s) to be Verified Messages

Enter your Current Signature Code: SIGNATURE VERIFIED

Print processed invoices? N// \<Enter\>-----------------------------------------report continues----------------------------------------

If the user chooses to print the processed invoices, ALL processed invoices will be printed. This includes the invoices that CANNOT be verified. If the user wants to print specific invoices, select the *Print Orders* option from the *Orders Menu*.

Example: Verify Invoices (continued)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; VERIFY ENTIRE INVOICE SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>If there are no corrections, you can change the invoices' status to "Verified" by selecting them from the list. If you do have corrections, press the return key then a second list will be displayed. You will be able to choose the invoices from that list and enter corrections.</p>
<p>Choose the invoices from the list you want to verify.</p>
<p>=============================================================================</p>
<p>1. Order#: C7564729 Invoice#: 1448168 Invoice Date: Jul 31, 1997 2. Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997</p>
<p>3. Order#: C7611902 Invoice#: 2165990 Invoice Date: Jul 03, 1997</p>
<p>============================================================================= Select invoices to verify: (1-3): <strong>1,3</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

When the user chooses the invoices from this list to verify, the status will be changed to Verified. Invoices not selected from the list will automatically be displayed on the EDIT INVOICES TO BE VERIFIED SCREEN so that changes can be made.

Verifying Invoices That Do Not Need to Be Edited

\<\<\< VERIFY ENTIRE INVOICE SCREEN \>\>\>

=============================================================================

1.  Order#: C7564729 Invoice#: 1448168 Invoice Date: Jul 31, 1997 COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

MASTER VAULT: MASTER VAULT 1

2.  Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997 COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

MASTER VAULT: MASTER VAULT 1

Are you sure these invoices' status should be changed to Verified? N// YES

Answer YES if the listed invoices and corresponding pharmacy location and/or master vault are correct.

Answer NO if an incorrect invoice is chosen or if the listed information is incorrect. The user will be returned to the previous VERIFY ENTIRE INVOICE SCREEN to reselect invoices.

........

Order# C7564729 Invoice# 1448168's status has been changed to Verified!

.........................................

Order#: C7611902 Invoice#: 2165983’s status has been changed to Verified!

-----------------------------------------report continues---------------------------------------- When changing the status has been answered YES, the above messages will be displayed as the invoice’s status is being changed. Upon exiting this option, a background job is run immediately which will add the receipts to the drug balances in the pharmacy location and/or master vault. The status will then be changed to Completed.

Invoices that have been moved to the status of completed are reviewed for notable changes of

Order Units, Dispense Units Per Order Unit (DUOU), Price Per Dispense Unit (PPDU), and NDCs. If there are changes a POST Verification 'Order' : 'Invoice' Variance Mailman message is sent to the G.PSA NDC UPDATES mail group.

Example: Verify Invoices (continued)EXAMPLE: Mailman Message

Subj: POST Verify C502395300 : 7229924053 Variance Report \[#1986002\]

04/01/05@18:29 11 lines

From: PSAperson,One In 'IN' basket. Page 1

-------------------------------------------------------------------------------

PRE Verify C502395300 : 7229924053 Variance Report

1.  ACETAMINOPHEN WITH CODEINE 30MG

DUOU Old: 485 New: 1000

OU Old: CO New: BT

PPDU Old: 1.2371 New: 0.6000

2.  METHADONE 10MG TAB

DUOU Old: 40 New: 100

PPDU Old: 0.1938 New: 0.0771

Selecting Invoices to be Edited

\<\<\< EDIT INVOICES TO BE VERIFIED SCREEN \>\>\>

Choose the invoices from the list you want to edit.

----------------------------------------------------------------------------- 1.Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997

-----------------------------------------------------------------------------

Select invoices to edit: (1-1): 1

If an invoice was not chosen to be verified previously or if the software found an error in the invoice, this screen will be displayed.

Editing the Invoice Data and Selecting Line Items to be Edited

\<\<\< EDIT INVOICES TO BE VERIFIED SCREEN \>\>\>

Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997

-----------------------------------------------------------------------------

Date received: Jul 03, 1997// 7 4

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

PHARMACY LOCATION: COMBINED (IP/OP)// \<Enter\>

Select Line#: ?

Answer with LINE ITEM DATA LINE ITEM NUMBER

Choose from:

659631

938662

Select Line#: 659631

The user is able to change the date the drugs were received and the pharmacy location and/or master vault that will receive the drugs on this invoice. Any line items that might need to be edited can also be chosen.

Example: Verify Invoices (continued)Selecting Line Item Fields to be Edited

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; EDIT INVOICES TO BE VERIFIED SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DACARBAZINE 100MG INJ</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 2</p>
<p>Order Unit : EA NDC: 000781-1766-10</p>
<p>Unit Price : $11.10 VSN: 659631</p></td>
</tr>
<tr class="odd">
<td>PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000</td>
</tr>
<tr class="even">
<td><p>PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1</p>
<p>Dispense Units: TAB</p>
<p>Dispense Units Per Order Unit: 1000</p>
<p>Stock Level : 2000</p>
<p>Reorder Level : 500</p>
<p>-----------------------------------------------------------------------------</p>
<ol type="1">
<li><p>Drug</p></li>
<li><p>Quantity Received</p></li>
<li><p>Order Unit</p></li>
<li><p>Dispense Units per Order Unit</p></li>
<li><p>Stock Level</p></li>
<li><p>Reorder Level</p></li>
</ol>
<p>Edit fields: (1-6): <strong>3,4,6</strong></p></td>
</tr>
</tbody>
</table>

-----------------------------------------report continues----------------------------------------

The user is able to select more than one field to be edited; however only the Stock Level and Reorder Level fields will be shown and allowed for editing if the assigned pharmacy location or master vault maintains reorder levels.

Editing Line Item Fields

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&lt;&lt;&lt; EDIT INVOICES TO BE VERIFIED SCREEN &gt;&gt;&gt;</p>
</blockquote>
<p>Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 DACARBAZINE 100MG INJ</td>
</tr>
<tr class="even">
<td><p>Qty Invoiced: 2</p>
<p>Order Unit : EA NDC: 000781-1766-10</p>
<p>Unit Price : $11.10 VSN: 659631</p></td>
</tr>
<tr class="odd">
<td>PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000 PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1</td>
</tr>
<tr class="even">
<td><p>Dispense Units: TAB</p>
<p>Dispense Units Per Order Unit: 1000</p>
<p>Stock Level : 2000</p>
<p>Reorder Level : 500</p>
<p>-----------------------------------------------------------------------------</p>
<p>ORDER UNIT: EA// <strong>BT</strong> BOTTLE</p>
<p>DISPENSE UNIT PER ORDER UNIT: 1000//<strong>@</strong></p>
<p>The dispense units per order unit must be entered to change the status of the invoice to Verified.</p>
<p>Do you want to enter the data now? Y//<strong>NO</strong></p></td>
</tr>
</tbody>
</table>

REORDER LEVEL (in Dispense Units): (0-99999): 500// 600

Select Line#: \<Enter\>Example: Verify Invoices (continued)Missing or Incorrect Data Found on Invoice

\*\* The invoice has not been placed in a Verified status!

Enter RETURN to continue or '^' to exit:

Do you want to print the verification error report? N// YES

DEVICE: HOME//*\[Select Print Device\]*Verification Error Report

\<\<\< VERIFICATION ERROR REPORT \>\>\>

Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 3, 1997

----------------------------------------------------------------------------- Line# 659631: Dispense unit per order unit

\*\* The invoice has not been placed in a Verified status!

-----------------------------------------report continues----------------------------------------

The user will receive this report listing the line item number and field(s) where an error or missing data was found.

No Errors Found on Invoice

Do you want to change the invoice's status to Verified?

If the answer is NO, the invoice will remain in a processed status and the user will be able to reselect it for verification, by choosing the *Verify Invoices* option. If the answer is YES, the user will receive a message stating that the invoice’s status has been changed to Verified.

Printing the NEW DRUG REPORT

The verified invoices contain new drugs for the assigned pharmacy location and/or master vault. A report will print by pharmacy location/master vault listing the new drugs. Use the Balance Adjustment option to enter an adjustment that reflects the total dispense units on hand for each new drug.

It is suggested that you send the report to a printer.

DEVICE: HOME// *\[Select Print Device\]*

\<\<\< NEW DRUG REPORT \>\>\>

PHARMACY LOCATION

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

=============================================================================

IMIPRAMINE HCL 50MG TAB

-----------------------------------------------------------------------------

PENTOBARBITAL SODIUM 100MG CAP

A MailMan message is also sent to the members of the G.PSA NDC UPDATES mail group identifying the pharmacy locations and the drugs that may need more data, such as current balance, stock level, and reorder levels entered to complete their setup.

Example:

Subj: New Drugs Added by Order: CX45678989 Invoice: 45789000C \[#1997035\]

08/24/05@13:45 54 lines

From: VERIFIED BY: DAPHARMACIST52,THREE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

New Drugs Added by Order: CX45678989 Invoice: 45789000C

Verified by: DAPHARMACIST52,THREE

Please use DA and CS menus to populate the balances, stock and re-order levels.

MASTER VAULT

CAFFEINE & SOD BENZOATE 500MG/2ML

CODEINE 15MG & APC C.T.

FENTANYL 0.05MG/ML 5ML S.S.

METHADONE 5MG TAB

MORPHINE 15MG/ML 20ML INJ

OUTPATIENT

ACETAMINOPHEN 500MG CAPSULE

ACETAZOLAMIDE 125MG TAB

ACETAZOLAMIDE 500MG INJ

ATENOLOL 100MG TAB

ATENOLOL 50MG TAB

CAFFEINE & SOD BENZOATE 500MG/2ML

CATAPRES .3MG TAB

FUROSEMIDE 10MG/ML 10ML INJ

MINOCYCLINE 100MG CAP

Upon exiting this option, a background job is run immediately which will add the receipts to the drug balances in the pharmacy location and/or master vault. The status will then be changed to Completed.

#### Print Orders 

> \[PSA PRINT ORDERS\]

The *Print Orders* option generates invoices by entering the order number, invoice number, or invoice status.

> This option is locked with the PSA ORDERS key.

- If the invoice has not been processed, the PRIME VENDOR UPLOAD REPORT prints.
- If the invoice has been processed, the PRIME VENDOR ORDER REPORT prints.

Example: Print OrdersPrint by Order Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>O Order Number</p>
<p>I Invoice Number</p>
<p>S Invoice Status</p>
<p>Print by Order#, Invoice#, or Invoice Status: O// <strong>&lt;Enter&gt;</strong></p>
<p>Select ORDER NUMBER: <strong>C7611902</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Select ORDER NUMBER: C7611903

> Select ORDER NUMBER: C7611904

> DEVICE: HOME// *\[Select Print Device\]*

When the user chooses to print by order number, the opportunity will be given to keep inputting as many order numbers as needed. All invoices for that order will print.

Print by Invoice Number

Select one of the following:

O Order Number

I Invoice Number

S Invoice Status

Print by Order#, Invoice#, or Invoice Status: O// Invoice Number

-----------------------------------------------------------------------------

Select ORDER NUMBER: C7611902

Invoice# 2165983

-----------------------------------------------------------------------------

Select ORDER NUMBER: C5014004

Select INVOICE NUMBER: 5471738

Select INVOICE NUMBER: 5471740

Select INVOICE NUMBER: \<Enter\>

----------------------------------------------------------------------------- Select ORDER NUMBER: \<Enter\>

DEVICE: HOME// *\[Select Print Device\]*

When the selection to print by invoice number is invoked, the order number is the first prompt. This is because the vendors may use the same invoice number more than once for different orders. Therefore there can be the same invoice number with different data for different orders. If there is more than one invoice for the order the user will be able to enter them. If there is only one invoice for the order, the invoice number will automatically be displayed.

Print by Invoice Status

Select one of the following:

O Order Number

I Invoice Number

S Invoice Status

Print by Order#, Invoice#, or Invoice Status: O// S Invoice Status

Select Unprocessed or Processed Invoice Status: (U/P): Unprocessed

If Unprocessed is chosen, all of the uploaded invoices that have not been processed will print. If Processed is chosen, all processed invoices that have not be verified will print.

#### Credit Resolution 

> \[PSA CREDIT RESOLUTION\]

The *Credit Resolution* option allows the user to enter credit memo data.

It is locked with the PSA ORDERS and PSAMGR keys<sub>.</sub>

When an adjustment is made to the invoice that decreases the total cost, the invoice is flagged as awaiting a credit. The invoice will continue to be flagged until the total credits equal the adjustment(s). If the user receives a credit memo and are unsure which invoice to apply the credit to, use the Outstanding Credits option under the Maintenance Reports Menu to print a report of all outstanding credits.

#### Edit Verified Invoices 

> \[PSA EDIT VERIFIED INVOICE\]

It is locked with the PSAMGR key.

The *Edit Verified Invoices* option allows the user to change elements of a verified invoice.

Example: Edit Verified Invoices

> Select Orders Menu Option: Edit Verified Invoices

> VERIFIED INVOICE ALTERATION SCREEN

The user selects an order number with a status of verified.

Select Order Number: C18442037N

\[Then selects an invoice from the order\]

Select Invoice Number: 2054031 03-16-01

-----------------------------------------report continues---------------------------------------- A screen with the available line items is displayed.

Example: Edit Verified Invoices (continued)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>EDIT VERIFIED INVOICED ITEM SCREEN</p>
<p>====================================================================</p>
<p>Order</p>
<p># Drug/Item Name Unit Qnty. NDC</p>
<p>====================================================================</p>
<p>1 ACETAMINOPHEN 1000MG TABLET BT 15 063481013275</p>
<p>Enter the corresponding item number to edit: <strong>1</strong> *ACETAMINOPHEN 1000MG TABLET Qty Invoiced: 15</p>
<p>Order Unit : BT (BT) NDC: 063481-0132-75</p>
<p>Unit Price : $1.71 VSN: 4003463</p>
<p>Dispense Units: MG</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Dispense Units Per Order Unit: 1000

=========================================================================

Select (D)rug or (O)rder Unit

The user can opt to alter the drug name or the associated order unit.

Select (D)rug or (O)rder Unit drug

Current Drug : ACETAMINOPHEN 1000MG TABLET

Select name of Correct Drug: ACETAMINOPHEN 325MG TABLET CN103

After selection of the drug, the program will compare the data in the invoice, with the data in the Drug file. The user will then be asked to enter the Dispense Units, and Dispense Units per Order Unit (DUOU).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Comparing drug file data...</p>
<p>Please Enter an appropriate Dispense Unit</p>
<p>DISPENSE UNIT: TAB// <strong>&lt;Enter&gt;</strong></p>
<p>Please enter the appropriate Dispense Units per order unit</p>
<p>DISPENSE UNITS PER ORDER UNIT: 1000// <strong>100</strong></p>
<p>Are you sure about this ? NO// <strong>?</strong></p>
<p>Answer yes, and the data on file for the current drug will be transferred to the new drug selection. That includes Order Unit, Dispense Unit, Dispense Units per Order Unit, etc.</p>
<p>Are you sure about this ? NO// <strong>Y</strong></p>
<p>Removing 15 from ACETAMINOPHEN 1000MG TABLET</p>
<p>Adding 15 to ACETAMINOPHEN 325MG TABLET Entering new drug selection as an adjustment. updating pharmacy location file. updating transaction file.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Delete Un-processed Invoices 

> \[PSA DELETE INVOICES\]

It is locked with the PSAMGR key<sub>.</sub>

The *Delete Un-processed Invoices* option deletes any un-processed invoices older than the date the user specifies. Only personnel who hold the PSAMGR key will have access to this process.

Example: Delete Un-processed Invoices

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Orders Menu Option: <strong>Del</strong>ete Un-processed Invoices</p>
<p>Delete invoices older than what date: <strong>T-6M</strong> Finished</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Mail Message Recipients 

> \[PSA MSG RECIPIENTS\]

It is locked with the PSAMGR key.

The *Setup Mail Message Recipients* option is used to enter/delete personnel from the two mail groups used for notifying personnel of a change in NDC and/or Drug Price, and when drugs are below reorder levels.

Example: Setup Mail Message Recipients

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Orders Menu Option: <strong><u>S</u></strong>etup Mail Message Recipients</p>
<p>SETUP RECIPIENTS OF MAILMESSAGE SCREEN</p>
<p>====================================================================</p>
<p>Currently, any user who holds the 'PSA ORDERS' key, receives the mail message</p>
<p>'Drug Balances Below Reorder Level' &amp; 'NDC/PRICE change messages'.</p>
<p>Two mail groups have been established to determine who receives the message.</p>
<p>Members added to the mail group must first possess the 'PSA ORDERS' key.</p>
<p>Do you want to edit the users for the PSA REORDER LEVEL mail group? YES//<strong>&lt;Enter&gt;</strong></p>
<p>Select NEW PERSON NAME: <strong>DAPHARMACIST52,THREE</strong></p>
<p>Select 'A' to Add the user or 'D' to delete the user. ADD//<strong>&lt;Enter&gt;</strong></p>
<p>task completed.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

There are two messages the user could receive from either action, the messages are: “task completed” and “Sorry, couldn’t perform task.” These messages are self-explanatory. If the program says it couldn’t perform the task of adding the user, which means that the user is already a member of the mail group. The same holds true for deleting users.

Example: Setup Mail Message Recipients (continued)

Trying to add the same user again:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select NEW PERSON NAME: <strong>DAPHARMACIST52,THREE</strong></p>
<p>Select 'A' to Add the user or 'D' to delete the user. ADD//<strong>&lt;Enter&gt;</strong> Sorry, couldn't perform action</p>
<p>Select NEW PERSON NAME: <strong>&lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Press \<Enter\> to access the next mail group.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Do you want to edit the users for the PSA NDC UPDATES mail group? YES//<strong>&lt;Enter&gt;</strong></p>
<p>Select NEW PERSON NAME: <strong>DAPHARMACIST52,THREE</strong></p>
<p>Select 'A' to Add the user or 'D' to delete the user. ADD//<strong>&lt;Enter&gt;</strong> task completed</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The message displayed when trying to add a user who is already on file:

Select NEW PERSON NAME: DAPHARMACIST52,THREE

Select 'A' to Add the user or 'D' to delete the user. ADD//\<Enter\> Sorry, couldn't perform action.

To delete a user from the mail group:

Select NEW PERSON NAME: DAPHARMACIST52,THREE Select 'A' to Add the user or 'D' to delete the user. ADD//D task completed.

Select NEW PERSON NAME: \<Enter\>

Press ENTURN/ENTER to continue: \<Enter\>

Select Orders Menu Option:

### Maintenance Reports Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA PV MAINTENANCE RPT MENU\]

The *Maintenance ReportsMenu* contains options that generate reports on balance adjustments, drug transaction history, drug balances by pharmacy location, invoice cost summary, monthly summary, processor and verifier of an invoice, and stock and reorder levels for drugs in a pharmacy location.

Example: Maintenance Reports Menu

1.  Balance Adjustments History
2.  Drug Balances by Location
3.  Drug Transaction History
4.  Invoice Cost Summary
5.  Monthly Summary
6.  Outstanding Credits
7.  Processor and Verifier
8.  Stock and Reorder Level
9.  Transfer Signature Sheet

#### Balance Adjustments History 

> \[PSA BALANCE ADJUSTMENTS REPORT\]

The *Balance Adjustments History* option reviews adjustments and transfers of a drug. The report lists the drug, transaction date and time, adjustment quantity, transfer quantity, transaction, adjustment reason, and pharmacy location that sent or received the transferred drug.

#### Drug Balances by Location 

> \[PSA DISPLAY LOCATION\]

The *Drug Balances by Location* option generates a report by pharmacy location listing each of its drugs’ name, quantity on hand, dispense unit, and total inventory.

#### Drug Transaction History 

> \[PSA DRUG DISPLAY\]

The *Drug Transaction History* option provides a transaction history for one, many, or all drug(s) within the pharmacy location for a given date range. It lists the date range, drug, beginning and ending dates, beginning balance, transaction date, transaction quantity, transaction type, person who made the transaction, and resulting balance.

If the transaction is <u>receiving</u> drugs, the purchase order number, transaction number, and invoice number are also listed.

If the transaction is <u>dispensing</u>, the report designates where the dispensing took place. It’s either Inpatient or Outpatient dispensing.

#### Invoice Cost Summary 

> \[PSA INVOICE COST SUMMARY\]

The *Invoice Cost Summary* option generates a report of all invoices’ cost data for a date range. It lists the order number, invoice number, invoice date, total invoice cost, total adjusted cost, and cost difference.

#### Monthly Summary 

> \[PSA MONTHLY SUMMARY\]

The *Monthly Summary* option allows the user to print a pharmacy location’s detailed or summary monthly report of transactions made on one, many, or all drugs.

If the user selects the detailed report, the drug, beginning balance, total receipts, total dispensed, total adjustments, total transfers, and ending balance or one, many, or all drugs in the selected pharmacy location is printed.

If the user selects the summary report, the detailed report prints then a separate summary report follows. The summary report contains the drug, total receipts, total dispensed, total adjustments, and total transfers for one, many, or all drugs in the selected pharmacy location. A total line for the total receipts, total dispensed, total adjustments, and total transfers is printed.

#### Outstanding Credits 

> \[PSA OUTSTANDING CREDITS\]

The *Outstanding Credits* option displays or prints invoice data for all invoices that have outstanding credits. A detailed or summary report may be selected.

<u>Detailed Report</u>

If the detailed report is selected, the summary data prints along with the line item information that caused the need for a credit. The line item data that prints are the line item’s number, drug, adjusted field’s name, adjustment comments, invoiced data, and adjusted data.

Example: Detailed Report

DRUG ACCOUNTABILITY/INVENTORY INTERFACE

OUTSTANDING CREDITS REPORT

PAGE 1 INVOICE ADJUSTED RECEIVED OUTST. DRUG &

INVOICE# DATE COST COST CREDITS CREDIT LINE# ADJUST REASON INV ADJ ------------------------------------------------------------------------------------------------

ORDER#: C5014003 (\$6376.18)

I845966 10/01/97 4440.04 4441.87 0.00 -1.83 2 AMPICILLIN 500MG CAP 0 1

QTY: DID NOT ORDER THIS

I845967 10/02/97 1938.38 1934.31 0.00 4.07 10 METOPROLOL 50MG TAB 12 11

QTY: 1 BOTTLE BROKEN

ORDER TOTAL 2.24

------------------------------------------------------------------------------------------------ ORDER#: C5014004 (\$17.92)

5471738 10/07/97 22.40 17.92 0.00 4.48 8 AMPICILLIN 250MG CAP 5 4

QTY: 1 BOTTLE MISSING

ORDER TOTAL 4.48

------------------------------------------------------------------------------------------------ GRAND TOTAL 6.72

<u>Summary Report</u>

If the summary report is selected, the order number, total adjusted cost of the order, invoice number, invoice date, invoiced cost, adjusted cost, credit amount received, invoice’s outstanding credit amount, total order’s outstanding credit amount, and grand total outstanding credit amount will be displayed.

Example: Summary Report

DRUG ACCOUNTABILITY/INVENTORY INTERFACE

OUTSTANDING CREDITS REPORT

PAGE 1

RUN DATE: 10/17/97@0822

INVOICE ADJUSTED RECEIVED OUTST.

INVOICE# DATE COST COST CREDITS CREDIT

-------------------------------------------------------------------------------

ORDER#: C5014003 (\$6376.18)

I845966 10/01/97 4440.04 4441.87 0.00 -1.83

I845967 10/02/97 1938.38 1934.31 0.00 4.07 ORDER TOTAL 2.24

ORDER#: C5014004 (\$17.92)

5471738 10/07/97 22.40 17.92 0.00 4.48

ORDER TOTAL 4.48

-------------------------------------------------------------------------------

GRAND TOTAL 6.72

#### Processor and Verifier 

> \[PSA PROCESSOR AND VERIFIER\]

The *Processor and Verifier* option generates a report containing invoices’ processor and verifier information for a date range. It lists the order number, invoice number, invoice date, processor’s name, process date, verifier’s name, and verification date.

#### Stock and Reorder Level 

> \[PSA STOCK & REORDER LEVEL RPT\]

The *Stock and Reorder Level* option prints a report by pharmacy location and/or master vault. The report contains the drug name, stock level, and reorder level. Only a pharmacist can enter the stock and reorder levels for a master vault. Since all drugs received are automatically added to a pharmacy location, it is advised that this report be queued to run during non-peak hours.

#### Transfer Signature Sheet 

> \[PSA TRANSFER SIGNATURE SHEET\]

The *Transfer Signature Sheet* option prints a report of all transferred drugs within a specific date range. This report is used to record the signature of the person who received the drugs or to review transfer history.

Example: Transfer Signature Sheet

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: PELHAM (IP)
3.  OUTPATIENT: HELENA (OP)

Select Transfer from Pharmacy: (1-3): 1

Select the pharmacy location that will send the drugs to the other pharmacy location.

Choose the pharmacy location receiving the transferred drugs:

1.  INPATIENT: PELHAM (IP)
2.  OUTPATIENT: HELENA (OP)

Select Transfer to Pharmacy: (1-2): 2

Select the pharmacy location that will receive the drugs from the transferring pharmacy locations.

Beginning Date: 8 12 (AUG 12, 1997)

Ending Date : 8 12 (AUG 12, 1997)

DEVICE: HOME// *\[Select Print Device\]*

Enter the date range to print the transfer signature sheets.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>AUG 12,1997@12:40 D R U G A C C O U N T A B I L I T Y Page: 1</p>
<p>DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET</p>
<p>COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)</p>
<p>TRANSFERRED TO: OUTPATIENT: HELENA (OP)</p>
<p>-----------------------------------------------------------------------------</p>
<p>TRANSFER DATE QTY DRUG NEW BALANCE</p>
<p>----------------------------------------------------------------------------- Aug 12, 1997@12:40 10 ACETAMINOPHEN 325MG TAB 50</p>
<p>Dispensed by: <strong>DAPHARMACIST51,THREE</strong> Rec'd by: ____________________________</p>
<p>(Full Name) (Full Name)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

\<This page is intentionally left blank.\>

# Section Three: Return Drug Credit Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG MENU\]

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/004.png)Users need at least one of the following security keys: PSORPH or PSARET. The PSORPH key is a security key in the Outpatient Pharmacy application intended to be assigned to the pharmacist staff. The PSARET key is a security key in the Drug Accountability application and is intended to be used by non-pharmacist personnel involved in the process of returning drugs to the return drug contractor.

The *Return Drug Credit Menu* may be used to document drugs returned and their status over time as they are picked up by the contracting company. In addition, the *Return Drug Credit Menu* may be used to document when a notification of credit is received and when the actual credit is received. A report produces a list of drugs for a given period of time with the status of each drug noted. The user also has the ability to remove drugs that have been entered in error and update inventory tracking.

Example: Return Drug Credit Menu

1.  Batch Work List \[PSA RET DRG BATCH WORKLIST\]
2.  Batch Complete List \[PSA RET DRG BAT COMPLETE LIST\]
3.  View/Update Batch \[PSA RET DRG VIEW/UPDATE BATCH\]
4.  Return Drug Credit Report \[PSA RET DRG REPORT\]

### Batch Work List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG BATCH WORKLIST\]

The *Batch Work List* option allows the user to add, edit, pick up, complete, or cancel a batch in addition to update credits and edit and cancel individual items. Only items with a status of Awaiting Pickup and Picked Up are displayed in this option.

To complete the process of returning drugs for credit, perform the following steps.

1.  Add a return contractor (first time) 4. Pick up the batch
2.  Add a batch 5. Update credit
3.  Add items (drugs) to the batch 6. Complete the batch

#### Adding a Return Contractor 

The user must first have a return contractor defined before they can add a batch with items for return. From the “Return Drug Batch List” screen, type CON at the “Select Action” prompt and add the return contractor information. This is usually performed the first time the *Batch Work List* option is used or when the return contractor changes.

#### Adding a Batch 

When adding a batch, a batch ID called a batch \# is automatically assigned and the user assigns the return contractor who is picking up the drugs as shown in the following example. The batch \# format is MMYY-NNN where MM is the current month, YY is the current year, and NNN is the incrementing number of the same month/year batch. Each new batch is automatically assigned the status of Awaiting Pickup.

Example: Adding a Batch

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return Drug Batch List Sep 19, 2008@10:08:21 Page: 1 of 2 Pharmacy Location: OUTPATIENTNo Inpatient or Outpatient Sites defined</p>
<p>Date Range : ALL</p>
<p>DATE DATE DATE TOTAL # OF</p>
<p># BATCH # CREATED PICKED UP COMPLETED CREDIT RETURN CONTRACTOR ITEMS</p>
<p>AWAITING PICKUP</p>
<ol type="1">
<li><p>0908-001 09/04/08 0.00 MORRISON CONTRACTING 14</p></li>
<li><p>0908-002 09/05/08 0.00 MORRISON CONTRACTING 1</p></li>
<li><p>0908-003 09/06/08 0.00 ANWER CONTRACTING CO 2</p></li>
<li><p>0908-005 09/07/08 0.00 JEN MANUFACTURING 1</p></li>
<li><p>0908-006 09/08/08 0.00 MORRISON CONTRACTING 6</p></li>
<li><p>0908-007 09/09/08 0.00 MORRISON CONTRACTING 5</p></li>
<li><p>0908-008 09/10/08 0.00 MORRISON CONTRACTING 10</p></li>
<li><p>0908-009 09/11/08 0.00 MORRISON CONTRACTING 8</p></li>
<li><p>0908-010 09/12/08 0.00 MORRISON CONTRACTING 7</p></li>
<li><p>0908-011 09/13/08 0.00 MORRISON CONTRACTING 3</p></li>
<li><p>0908-012 09/14/08 0.00 MORRISON CONTRACTING 12</p></li>
<li><p>0908-013 09/15/08 0.00 MORRISON CONTRACTING 5</p></li>
<li><p>0908-017 09/16/08 0.00 MORRISON CONTRACTING 4</p></li>
<li><p>0908-018 09/17/08 0.00 MORRISON CONTRACTING 2</p></li>
<li><p>0908-019 09/18/08 0.00 MORRISON CONTRACTING 0</p></li>
</ol>
<p>+ Select the entry # to view or ?? for more actions ADD New Batch SEL Select Batch CON Rtn Contractor Add/Edit Select Action: Next Screen// <strong>ADD</strong> <strong>&lt;Enter&gt;</strong> New Batch</p>
<p>New Batch #: 0908-020</p>
<p>RETURN CONTRACTOR: MORRISON CONTRACTING SERVICES</p>
<p>Save Batch? NO// <strong>YES &lt;Enter&gt;</strong> Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Editing a Batch 

The user can edit the batch information from the “Return Drug Batch” screen. At each prompt, the user has the opportunity to enter batch related information, such as the return contractor and the reference \#. The reference \# is the return contractor batch ID number the user receives from the return contractor when the batch is picked up. Adding Items (Drugs) to a Batch

After a batch has been added, the user is taken to the next screen, “Return Drug Batch”, where items that are being returned can be added to the batch. The user can enter the following information about the item being returned.

Drug\* Number of Dispense Unit per Order

Manufacturer Unit\*

> National Drug Code (NDC)

> Order Unit\*

> Number of Order Units\*

> Number of Dispense Units\*

> Dispense Unit

> \* Required fields

Example: Adding Items to a Batch

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return Drug Batch Sep 19, 2008@10:08:29 Page: 0 of 0</p>
<p>Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08 Batch Number : 0908-020 Status: AWAITING PICKUP</p>
<p>Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up:</p>
<p>Reference # : Total Batch Credit: $0.00</p>
<p>ORD ORDER DISP DISP ACTUAL # RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT($)</p>
<p>This batch contains no return items.</p>
<p>Select the entry # to view or ?? for more actions</p>
<p>ADD New Item CRE Credit Update SEL Select Item</p>
<p>EDT Edit Batch PKP Pick up Batch</p>
<p>CAN Cancel Batch COM Complete Batch</p>
<p>Select Action: Quit// <strong>ADD</strong> <strong>&lt;Enter&gt;</strong> New Item</p>
<p>DRUG: <strong>MEPERIDINE</strong></p>
<ol type="1">
<li><p>MEPERIDINE 100MG SYRINGE CN101</p></li>
<li><p>MEPERIDINE 25MG SYRINGE CN101</p></li>
<li><p>MEPERIDINE 50MG SYRINGE CN101</p></li>
<li><p>MEPERIDINE 50MG TAB CN101</p></li>
<li><p>MEPERIDINE 50MG/5ML ELIXIR (OZ) CN101 Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p></li>
</ol>
<p>CHOOSE 1-5: <strong>4</strong> <strong>&lt;Enter&gt;</strong> MEPERIDINE 50MG TAB CN101 MFR: <strong>TEST MFR &lt;Enter&gt;</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>If File #50 contains this information, it is populated for the user; otherwise, the user is prompted to enter values that are saved for this item but are not saved to File #50.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>NDC: 00555-0381-04// <strong>&lt;Enter&gt;</strong> 00555-0381-04</p>
<p>ORDER UNIT: BOTTLE</p>
<p>DISPENSE UNIT: TABLET</p>
<p>NUMBER OF TABLET(S) PER BOTTLE: 500</p>
<p>NUMBER OF BOTTLE(S) TO RETURN: <strong>5 &lt;Enter&gt;</strong></p>
<p>NUMBER OF TABLET(S) TO RETURN: 2500// <strong>&lt;Enter&gt;</strong></p>
<p>UPC: <strong>&lt;Enter&gt;</strong></p>
<p>EXPIRATION DATE: <strong>07/01/08 &lt;Enter&gt;</strong> (JUL 01, 2008)</p>
<p>RETURN REASON: <strong>? &lt;Enter&gt;</strong></p>
<p>Select the reason why the drug is being returned to the contractor/ manufacturer. Choose from:</p>
<p>E EXPIRED</p>
<p>R RECALLED</p>
<p>D DAMAGED</p>
<p>O OVERSTOCKED</p>
<p>M MISCELLANEOUS</p>
<p>X DESTRUCTION</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Universal Product Code (UPC)

> Expiration Date

> Return Reason\*

> Update Inventory\*

> RETURN REASON: EXPIRED \<Enter\>

> UPDATE INVENTORY: NO// \<Enter\>

> Save Item? YES// \<Enter\>

> Saving...OK

> Add another Item? YES// NO \<Enter\>

At this point, the drug has been successfully added to the batch and the user is prompted whether or not he or she wants to add another drug. From the “Return Drug Batch” screen, the user can add more items, edit the selected item, edit the batch information, cancel the batch, update credit of items, pick up the batch, or complete the batch.

Return Drug Batch Sep 19, 2008@10:11:30 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08 Batch Number : 0908-020 Status: AWAITING PICKUP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up:

Reference \# : Total Batch Credit: \$0.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$) 1 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 0.00

Select the entry \# to view or ?? for more actions

ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit//

#### Editing an Item 

The user can edit the item information. From the “Return Drug Batch” screen, select the item to edit. From the “Return Drug Item” screen, type EDT for Edit Item and press \<Enter\>. Each item’s field is presented with the current value as the default. To keep the default and continue to the next field, press \<Enter\>. Otherwise, type the new value and press \<Enter\> to update it and continue to the next field. When all fields have been addressed, at the “Save Item?” prompt, type Y for YES and press \<Enter\>. The changes to the fields are saved, and the activity log is updated and displays the changes below the drug information on the “Return Drug Item” screen.

#### Picking up a Batch 

After all items have been entered into a batch and when the return contractor is ready to physically pick up the drugs, the batch may be marked as picked up. At this point, credits can be entered for each item in the batch. Credits can be updated while marking the batch as picked up or later if needed, however a batch can be marked as picked up only once. NOTE: After a batch has been marked as picked up, it can no longer be cancelled. The following example shows a batch being marked as picked up and credits being updated during pickup.

Example: Picking up a Batch and Updating Credits

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return Drug Batch Sep 19, 2008@10:11:30 Page: 1 of 1</p>
<p>Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08 Batch Number : 0908-020 Status: AWAITING PICKUP</p>
<p>Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up:</p>
<p>Reference # : Total Batch Credit: $0.00</p>
<p>ORD ORDER DISP DISP ACTUAL</p>
<p># RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT($)</p>
<ol type="1">
<li><p>BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00</p></li>
<li><p>MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 0.00 3 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 0.00</p></li>
</ol>
<p>Select the entry # to view or ?? for more actions</p>
<p>ADD New Item CRE Credit Update SEL Select Item</p>
<p>EDT Edit Batch PKP Pick up Batch</p>
<p>CAN Cancel Batch COM Complete Batch</p>
<p>Select Action: Quit// <strong>PKP</strong> <strong>&lt;Enter&gt;</strong> Pick up Batch</p>
<p>RETURN CONTRACTOR: MORRISON CONTRACTING SERVICES// RETURN CONTRACTOR REF#: <strong>2242 &lt;Enter&gt;</strong></p>
<p>Do you want to update credit for items? YES// <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p>E ESTIMATED</p>
<ol type="A">
<li><p>ACTUAL</p></li>
<li><p>BOTH</p></li>
</ol>
<p>CREDIT TYPE: A// <strong>BOTH &lt;Enter&gt;</strong></p>
<p>ITEM(S): (1-3): <strong>3 &lt;Enter&gt;</strong></p>
<p>Item 3: MEPERIDINE 50MG TAB (00555-0381-04) - Quantity: 5 (BOTTLE)</p>
<p>ESTIMATED CREDIT AMOUNT: <strong>100</strong> <strong>&lt;Enter&gt;</strong></p>
<p>ACTUAL CREDIT AMOUNT: <strong>75 &lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Return Drug Batch Sep 19, 2008@10:14:18 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: PICKED UP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13

Reference \# : 2242 Total Batch Credit: \$75.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1.  BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00
2.  MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 0.00 3 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00

Enter ?? for more actions ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit//

#### Updating Credits 

The Credit Update action is available after the batch has been picked up and before the batch has been completed. When updating credits and prompted to enter the credit amount, estimated or actual, keep in mind that it is the total credit for the total number of order units of that item being returned that should be entered, not the credit amount for one order unit of that item. On the “Return Drug Batch” screen, the “Total Batch Credit” reflects the total actual credit amount that has been entered for each item in the batch. If only an estimated amount has been entered, the “Total Batch Credit” will still be \$0.00. The following is an example of entering both estimated and actual credit.

Example: Updating a Credit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return Drug Batch Sep 19, 2008@10:14:18 Page: 1 of 1</p>
<p>Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08 Batch Number : 0908-020 Status: PICKED UP</p>
<p>Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13</p>
<p>Reference # : 2242 Total Batch Credit: $75.00</p>
<p>ORD ORDER DISP DISP ACTUAL</p>
<p># RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT($)</p>
<ol type="1">
<li><p>BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00</p></li>
<li><p>MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 0.00 3 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00</p></li>
</ol>
<p>Enter ?? for more actions</p>
<p>ADD New Item CRE Credit Update SEL Select Item</p>
<p>EDT Edit Batch PKP Pick up Batch</p>
<p>CAN Cancel Batch COM Complete Batch</p>
<p>Select Action: Quit// <strong>CRE</strong> <strong>&lt;Enter&gt;</strong> Credit Update</p>
<p>Select one of the following:</p>
<p>E ESTIMATED</p>
<ol type="A">
<li><p>ACTUAL</p></li>
<li><p>BOTH</p></li>
</ol>
<p>CREDIT TYPE: A// <strong>BOTH &lt;Enter&gt;</strong></p>
<p>ITEM(S): (1-3): <strong>2 &lt;Enter&gt;</strong></p>
<p>Item 2: MEDROXYPROGESTERONE 100MG (00009-0248-02) - Quantity: 15 (BOX)</p>
<p>ESTIMATED CREDIT AMOUNT: <strong>45 &lt;Enter&gt;</strong></p>
<p>ACTUAL CREDIT AMOUNT: <strong>60 &lt;Enter&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Notice the “Total Batch Credit” has been updated to reflect the actual credit amount from both items in this batch.

Return Drug Batch Sep 19, 2008@10:15:06 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: PICKED UP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13

Reference \# : 2242 Total Batch Credit: \$135.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1.  BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00
2.  MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 60.00 3 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00

Enter ?? for more actions

ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit//

#### Completing a Batch 

After the batch has been picked up and all credits have been updated, the user can complete the batch. From the “Return Drug Batch List” screen, select the batch and the “Return Drug Batch” screen appears. At the “Select Action” prompt, type COM for Complete Batch and press \<ENTER\>. At the “Complete Batch?” prompt, type Y for Yes and press \<ENTER\>. The batch status has changed from Picked Up to Completed. And, the batch has moved from being displayed under the *Batch Work List* option to being displayed under the *Batch Complete List* option. This also finishes the process of returning drugs for credit.

> **NOTE:** Any item without an actual credit amount is marked DENIED when the batch is being completed and a message appears before the user can continue completing the batch as shown in the following example.

Example: Completing a Batch with One Item Denied

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return Drug Batch Sep 19, 2008@10:15:06 Page: 1 of 1</p>
<p>Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08 Batch Number : 0908-020 Status: PICKED UP</p>
<p>Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13</p>
<p>Reference # : 2242 Total Batch Credit: $135.00</p>
<p>ORD ORDER DISP DISP ACTUAL</p>
<p># RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT($)</p>
<ol type="1">
<li><p>BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00</p></li>
<li><p>MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 60.00 3 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00</p></li>
</ol>
<p>Enter ?? for more actions</p>
<p>ADD New Item CRE Credit Update SEL Select Item</p>
<p>EDT Edit Batch PKP Pick up Batch</p>
<p>CAN Cancel Batch COM Complete Batch</p>
<p>Select Action: Quit// <strong>COM</strong> <strong>&lt;Enter&gt;</strong> Complete Batch</p>
<p>WARNING: The following items will have their CREDIT STATUS set to DENIED because no credit amount has been entered for them:</p>
<p>----------------------------------------------------------- RETURN DRUG (NDC) DISP QTY UNIT</p>
<p>----------------------------------------------------------- BACLOFEN 10MG TABS (00028-0023-01) 3 TABLET</p>
<p>Complete Batch? NO// <strong>YES &lt;Enter&gt;</strong></p>
<p>Completing Batch...OK</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Batch Complete List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG BAT COMPLETE LIST\]

The *Batch Complete List* option allows the user to view a comprehensive list of the batches with any status: Awaiting Pickup, Picked Up, Cancelled, and Completed. Additional features include editing the contractor/manufacturer and adding/editing/cancelling a batch and an item as done from the *Batch Work List* \[PSA RET DRG BATCH WORKLIST\] option.

### View/Update Batch 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG VIEW/UPDATE BATCH\]

The *View/Update Batch* option allows the user to avoid extra steps and go straight to the batch if the batch number or the contractor reference \# are known. The “Return Drug Batch List” screen is available then allowing the user to add, edit, pick up, complete, or cancel a batch in addition to update credits and edit and cancel items all as done from the *Batch Work List* option.

### Return Drug Credit Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG REPORT\]

The *Return Drug Credit Report* option allows the user to produce reports, either detailed or summarized, on the batches. Use filtering information to include the batches of interest.

On the summary format report, the “ACTUAL CREDIT\$” column is included on reports that have a STATUS of COMPLETED only. On the detailed format report, the “Total Batch Credit” is included on reports that have a STATUS of COMPLETED only.

Example: Report – Summary Format

Return Drug Credit Report (SUMMARY) Page: 1

PHARM LOCATION: OUTPATIENTNo Inpatient or Outpa STATUS: COMPLETED

Date Range: 09/19/08 THRU 09/19/08 Run Date: 09/19/08@10:16:17

--------------------------------------------------------------------------------

ORD ORDER DISP DISP UPD ACTUAL

DRUG (NDC) QTY UNIT QTY UNIT INV CREDIT\$

--------------------------------------------------------------------------------

Batch \#: 0908-020 Date Completed: 09/19/08 - MORRISON CONTRACTING SERVICES

BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET NO

MEDROXYPROGESTERONE (00009-0248-02) 15 BOX 15 VIAL NO 60.00 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET NO 75.00

======== BATCH ENTRIES: 3 BATCH TOTAL: \$135.00

CREDIT TOTAL: \$135.00 Enter RETURN to continue or '^' to exit:

Example: Report – Detailed Format

Return Drug Credit Report (DETAILED) Page: 1

PHARM LOCATION: OUTPATIENTNo Inpatient or Outpatient Sit BATCH \#: 0908-020

CONTRACTOR/MFR: MORRISON CONTRACTING SERVICES STATUS: COMPLETED

Date Range: 09/19/08 THRU 09/19/08 Run Date: 09/19/08@10:16:58

Total Batch Credit: \$135.00

-------------------------------------------------------------------------------- Drug: BACLOFEN 10MG TABS Credit Status: DENIED

Manufacturer: TEST MFR Credit Amount:

NDC: 00028-0023-01 Exp. Date: 09/15/09

Rtrn Ord Qty: 3 BOTTLE Created By: USER,ONE

Rtrn Disp Qty: 3 TABLET Created On: 09/19/08

UPC: Upd Inventory: NO

Return Rsn: DAMAGED

--------------------------------------------------------------------------------

Drug: MEDROXYPROGESTERONE 100MG Credit Status: ACTUAL

Manufacturer: TEST MFR Credit Amount: \$60.00 (ACTUAL)

NDC: 00009-0248-02 Exp. Date: 10/31/09

Rtrn Ord Qty: 15 BOX Created By: USER,ONE

Rtrn Disp Qty: 15 VIAL Created On: 09/19/08

UPC: Upd Inventory: NO

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return Rsn: DAMAGED</p>
<p>-------------------------------------------------------------------------------- Press ENTER to Continue or ^ to Exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Return Drug Credit Report (DETAILED) Page: 2

PHARM LOCATION: OUTPATIENTNo Inpatient or Outpatient Sit BATCH \#: 0908-020

CONTRACTOR/MFR: MORRISON CONTRACTING SERVICES STATUS: COMPLETED

Date Range: 09/19/08 THRU 09/19/08 Run Date: 09/19/08@10:17:13 Total Batch Credit: \$135.00

--------------------------------------------------------------------------------

Drug: MEPERIDINE 50MG TAB Credit Status: ACTUAL

Manufacturer: TEST MFR Credit Amount: \$75.00 (ACTUAL)

NDC: 00555-0381-04 Exp. Date: 07/01/08

Rtrn Ord Qty: 5 BOTTLE Created By: USER,ONE

Rtrn Disp Qty: 2500 TABLET Created On: 09/19/08

UPC: Upd Inventory: NO

Return Rsn: EXPIRED

--------------------------------------------------------------------------------

Enter RETURN to continue or '^' to exit:

\<This page is intentionally left blank\>

# Section Four: GUI Upload Program 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is locked with the PSA ORDERS key.

The PSA_MCKESSON_UPLOAD GUI application allows authorized users to upload McKesson invoice data from a user’s workstation to VistA. VistA patch PSA\*3.0\*79 incorporates needed enhancements to the GUI upload program for Two-Factor Authentication (2FA) compliance.

## Using the GUI Upload Program 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the PSA_MCKESSON_UPLOAD icon located on the Pharmacy PC’s desktop. The program checks for the existence of the invoice file and the security file. Security checks are run to ensure the file has not been tampered with.

> \*\*\*Note\*\*\* C:\DAU will be the default location where the application will look for the invoices.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/005.png)

Figure 1-1: Example of desktop shortcut icon.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Note:</strong></th>
<th rowspan="2"><blockquote>
<p>If secured invoices are saved to a location other than C:\DAU or an invoice error condition exists refer to section 5.2</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/006.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Select the Correct VistA Session 

If a secured invoice file is found and security checks passed, the “Connect To” dialog appears.

Click the down-arrow, select the appropriate account (if more than one exists), and click “OK”.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/007.png)

Figure 1-2: Example of broker connection Connect To Dialog Box

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Note:</strong></th>
<th rowspan="2"><blockquote>
<p>The broker connection dialog box may not display if the PSA</p>
<p>_MCKESSON_UPLOAD desktop shortcut is configured to connect to a specific VistA instance.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/008.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### PIV Certificate Selection 

After clicking OK the PIV Certificate selection dialog box appears. Select a valid security certificate and click OK.

![Figure 1-3 Security certificate window](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/009.png)

*Figure 1-3 Security certificate window*

After clicking OK the PIV PIN dialog box appears. Enter the associated PIV pin and click OK.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/010.png)

Figure 1-4: Example of PIV PIN dialog box.

The System Use Notification dialog box appears, click OK.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/011.png)

Figure 1-5: Example System Use Notification dialog box.

The Select Division dialog box appears, select the correct division and click “OK”.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/012.png)

Figure 1-6: Example Select Division dialog box.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Note:</strong></th>
<th rowspan="2"><blockquote>
<p>The Select Division dialog box may not display if the user has only been assigned one division.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/013.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### VistA Invoice Upload 

After clicking “OK”, the invoice is uploaded into VistA and a dialog box opens and displays information confirming the invoice data has been transferred to VistA. The upload utility automatically deletes the “.dat” file once upload completes. Click OK.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/014.png)

Figure 1-7: Example of successful upload screen.

The program will automatically shut down at this point.

#### VistA Upload Status Report 

An Upload Status Report will be sent to the user via Mailman with details and the status of the upload.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/015.png)

Figure 1-8: Example of VistA MailMan Upload Status report.

## Invoice Files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Invoice File Locations and Navigation 

The DAU GUI UPLOAD program searches for invoice files in C:\DAU\\ on the users workstation by default. If the invoice file is saved to a location other than C:\DAU\\ a dialog box will open and display “Unable to Find Invoice.”

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/016.png)

Figure 1-9: Example Error message “Unable to Find Invoice” dialog box.

The user should then select the Find Invoice option located under the File menu.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/017.png)

Example 1-10: Example Find Invoice

Navigate to where you stored the file on the workstation. When the appropriate folder is opened, the program will search for the Invoice file using predefined search parameters. If the file is found, the filename will display in the text box at the bottom of the screen. Click on the file name to select and click OPEN continue processing. You can also Double Click on the file to select and continue processing.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/018.png)

Figure 1-11: Example Invoice File Found

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Note:</strong></th>
<th rowspan="2"><blockquote>
<p>You can also Double Click the invoice file to select it and continue processing.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/019.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Invoice Error conditions 

After an invoice is selected for processing, checks are performed to verify the file meets requirements and has not been tampered with. If the file does not pass the required checks an error message will display. If you encounter an error condition with an invoice file, delete it from your workstation and download a new copy of the invoice.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/020.png)

Figure 1-12: Example Invoice PO ID# not valid length.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/021.png)

Figure 1-13: Example Invoice Failed Security Check

## Non-PIV/Alternate Logon 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you lose your PIV card or forget it, there is an alternative way to log into DAU using your access and verify code. Each user should be assigned an access code and a verify code. You will need to check with your local facility to get your access and verify codes, if necessary.

> To logon using the Access and Verify Codes, follow these steps after double-clicking the PSA_MCKESSON_UPLOAD icon on your desktop and selecting the invoice to upload:

1.  When presented with the PIV Card selection screen, cancel the certificate selection. The VistA logo window and the VistA Sign-on dialog will appear.
2.  If the Connect To dialog appears, click the down-arrow, select the appropriate account (if more than one exists), and click OK.
3.  Type your access code into the Access Code field and press the Tab key.
4.  Type the verify code into the verify code field and press the Enter key or click OK.

![](drug-accountability-inventory-interface-version-3-user-manual-updated-psa-3-79/022.png)

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>A&amp;MMS</strong></th>
<th><p>The procurement section within the VA. It is the</p>
<p>Acquisition and Materiel Management Service (A&amp;MMS).</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Alternate vendors</strong></td>
<td>Vendors who are not prime vendors.</td>
</tr>
<tr class="even">
<td><strong>Automated Connection</strong></td>
<td>A user initiated linking of multiple DRUG file (#50) entries to ITEM MASTER file (#441) entries. Because matching is not based upon user approval, this process should not be used without first reviewing the Report of Potential matches.</td>
</tr>
<tr class="odd">
<td><strong>Control Point Transaction</strong></td>
<td>The permanent number that identifies a request,</td>
</tr>
<tr class="even">
<td><strong>Number</strong></td>
<td>consisting of station number-fiscal year-quarter-control point-sequence number.</td>
</tr>
<tr class="odd">
<td><strong>Controlled Connection</strong></td>
<td>A user controlled process to link DRUG file (#50) entries to ITEM MASTER file (#441) entries. Each match is displayed and linked only after the user approves.</td>
</tr>
<tr class="even">
<td><strong>Controlled Substance</strong></td>
<td>A drug that has been marked for tracking through the Controlled Substances package. It is usually a narcotic.</td>
</tr>
<tr class="odd">
<td><strong>Credit</strong></td>
<td>This is money due to the VA facility from the prime vendor. When an invoice dollar amount is more than the adjusted dollar amount, DA V. 3.0 flags it as an outstanding credit. When the facility receives a credit memo, the credit data is entered in DA V. 3.0.</td>
</tr>
<tr class="even">
<td><strong>Dispense Units per Order</strong></td>
<td>This is the total number of dispense units contained in one</td>
</tr>
<tr class="odd">
<td><strong>Unit</strong></td>
<td>order unit. For example, if a case is ordered containing 12 bottles with 1,000 tablets in each bottle, the dispense unit per order unit is 12,000 per the following equation:</td>
</tr>
</tbody>
</table>
> Dispense Units: TAB
> Order Unit : CS
> The case contains 12 bottles of 1,000 tablets
> 12 x 1,000 = 12,000 DISPENSE UNITS PER ORDER UNIT: 12,000
<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Dispensing Unit</strong></th>
<th>This field is used to indicate the pharmacy dispensing units when converting the unit per issue to the pharmacy dispensing units.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Dispensing Unit Conversion</strong></td>
<td>This field is multiplied by the quantity on hand in</td>
</tr>
<tr class="even">
<td><strong>Factor</strong></td>
<td>unit per issue to generate the quantity in pharmacy dispensing units.</td>
</tr>
<tr class="odd">
<td><strong>Drug</strong></td>
<td>A substance used to treat illness or disease.</td>
</tr>
<tr class="even">
<td><strong>Drug Accountability/</strong></td>
<td>The creation of a perpetual inventory for VA facility</td>
</tr>
<tr class="odd">
<td><strong>Inventory Interface</strong></td>
<td>pharmacies. This inventory, or pharmacy location, can</td>
</tr>
<tr class="even">
<td></td>
<td>be an Inpatient, Outpatient, or Combined operation. If the facility is interfacing with GIP, the pharmacy location must be linked to a primary inventory point to enable receiving. Dispensing activity will be gathered from the appropriate pharmacy packages [e.g., Outpatient Pharmacy, Inpatient Medications (Unit Dose and Intravenous), Automatic Replenishment and Ward Stock (AR/WS)].</td>
</tr>
<tr class="odd">
<td><p><strong>Drug Accountability</strong></p>
<p><strong>Location</strong></p></td>
<td>A pharmacy that stores and dispenses drugs.</td>
</tr>
<tr class="even">
<td><strong>DRUG file (#50)</strong></td>
<td>A <strong>V</strong><em>IST</em><strong>A</strong> file used by Pharmacy software products. This file is used to list generic drug products and holds the information related to each drug that can be used to fill a prescription.</td>
</tr>
<tr class="odd">
<td><strong>Federal Stock Number</strong></td>
<td>This field exists in the DRUG file (#50) and corresponds</td>
</tr>
<tr class="even">
<td><strong>(FSN)</strong></td>
<td>to the National Stock Number field in the ITEM MASTER file (#441). It is used as a tool for connecting these files.</td>
</tr>
<tr class="odd">
<td><strong>GIP</strong></td>
<td>The Generic Inventory Package is the VA software package that automatically generates purchase orders and manages inventory.</td>
</tr>
<tr class="even">
<td><strong>IFCAP</strong></td>
<td>The Integrated Funds Distribution, Control Point Activity, Accounting and Procurement is the VA software package that tracks procurement and payment.</td>
</tr>
<tr class="odd">
<td><strong>Inpatient Site</strong></td>
<td>An area within a facility that treats patients that have been admitted. If the facility has more than one Inpatient dispensing area, it is necessary to link each pharmacy location to the appropriate Inpatient site (area) for the</td>
</tr>
</tbody>
</table>
> collection of dispensing data.
<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Item</strong></td>
<td><p>It is a specific drug product in the ITEM MASTER file</p>
<p>(#441) that references the way it is packaged (i.e., Prozac</p>
<p>25 mg., 250 tabs/bottle).</p></td>
</tr>
<tr class="even">
<td><strong>ITEM MASTER file (#441)</strong></td>
<td>A <strong>V</strong><em>IST</em><strong>A</strong> file used by the IFCAP software. This file is used to store items. The file contains descriptive information for all items that are ordered. It contains information needed for purchasing or ordering items.</td>
</tr>
<tr class="odd">
<td><strong>Invoice</strong></td>
<td>A bill for ordered goods. Each invoice is numbered. See entry for Order Number vs. Item Number.</td>
</tr>
<tr class="even">
<td><strong>Line Item</strong></td>
<td>This is the information on the invoice for an ordered drug.</td>
</tr>
<tr class="odd">
<td><strong>National Drug Code (NDC)</strong></td>
<td>A field that exists in the DRUG file (#50), ITEM MASTER file (#441 ) and NDF. With some formatting adjustments the field is used to match entries in otherwise unlinked files and open the door for comparative displays and reports. The code itself contains a maximum of 12 digits. The first six digits are the manufacturer’s code, the next four are the product code, and the last two digits are the package code.</td>
</tr>
<tr class="even">
<td><strong>National Stock Number</strong></td>
<td>This field exists in the ITEM MASTER file (#441) <strong>(NSN)</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>and corresponds to the FSN field (#6) in the DRUG file (#50). It is used as a connecting tool for these files.</td>
</tr>
<tr class="even">
<td><strong>Order</strong></td>
<td>VA’s request for goods from the vendor.</td>
</tr>
<tr class="odd">
<td><strong>Order Number vs.</strong></td>
<td>An order number is a VA number by which to</td>
</tr>
<tr class="even">
<td><strong>Invoice Number</strong></td>
<td>charge the ordered goods. The invoice number is the vendor’s number for billing the ordered goods. There can be many invoice numbers assigned to one order number because by law, certain drugs have to be placed on an invoice by itself. Also drugs can come from different distribution centers, which necessitates different invoice numbers.</td>
</tr>
<tr class="odd">
<td><strong>Outpatient Site</strong></td>
<td>An area within a facility that treats patients that are not admitted to the facility. If a facility has more than one Outpatient dispensing area, it is necessary to link each pharmacy location to the appropriate Outpatient site (area)</td>
</tr>
</tbody>
</table>
> for the collection of Outpatient dispensing data.
<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Perpetual Inventory</strong></td>
<td>The capability to maintain an accurate balance at the dispense unit level (such as tablets, capsules) for a select group of items.</td>
</tr>
<tr class="even">
<td><strong>Pharmacy Location</strong></td>
<td>An inventory location created to store a select group of drugs and track their balance and activity.</td>
</tr>
<tr class="odd">
<td><strong>Posted Procurement</strong></td>
<td>Purchases made from the Acquisition and Materiel Management Service (A&amp;MMS) warehouse.</td>
</tr>
<tr class="even">
<td><strong>Primary Inventory Point</strong></td>
<td>Within the IFCAP Personal Property Management (PPM) module, an option enables the creation of a primary inventory point for each Service that manages a Fund Control Point. The Primary–General Inventory/Distribution Menu [PRCP MAIN MENU] provides Service level management of a primary inventory point. Similar to a pharmacy location, a primary inventory point houses a select group of items and provides tools (bar coding) for physical counts and auto-generation of orders. It is the connecting of the DRUG file (#50)/ITEM MASTER file (#441) and the linking of a pharmacy location to a primary inventory point that will automate receiving. Connection to multiple primary inventory points is allowed.</td>
</tr>
<tr class="odd">
<td><strong>Prime Vendor</strong></td>
<td>A vendor who is on contract with the VA to be the main supplier of drugs.</td>
</tr>
<tr class="even">
<td><strong>Process</strong></td>
<td><p>Process is matching invoice data with data in <strong>V</strong><em>IST</em><strong>A</strong> and validating the data. Matching is accomplished by</p>
<p>comparing the line item data on the invoice with its entry in the DRUG file (#50). Validating is accomplished by confirming the quantity received vs. the quantity invoiced. Anyone holding the PSA ORDERS key can process the invoice.</p></td>
</tr>
<tr class="odd">
<td><strong>Reorder Level</strong></td>
<td>The minimum amount of dispense units to keep in the pharmacy location or master vault. A MailMan message is sent to holders of the PSA ORDERS key when the current drug balance is equal to or less than the reorder level. A nightly job sends the mail message if there is at least one drug at or below this level.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Special Inventory Type</strong></th>
<th>A GENERIC INVENTORY file (#445) switch field</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>field (#15)</strong></td>
<td><p>that controls receipt updates to other packages.</p>
<p>When it is set to “D”, this field located in the <em>Set Up/Edit a</em></p></td>
</tr>
</tbody>
</table>
> *Pharmacy Location* option of the *Pharmacy Location Maintenance Menu* will update the pharmacy DA V. 3.0 package when the primary quantity on-hand is changed.
| Stock Level             | The stock level is the ideal number of a drug’s dispense unit to keep on the shelf. When the drug reaches the reorder level, the number of dispense units to be ordered is determined by subtracting the current balance from the stock level. The result appears on the nightly background job mail message as the amount of dispense units to order.                                                                                     |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unit of Issue           | The packaging unit used at the inventory point to distribute the item.                                                                                                                                                                                                                                                                                                                                                                     |
| Unit of Issue Packaging | The number for converting the unit of issue into                                                                                                                                                                                                                                                                                                                                                                                           |
| Multiple                | individual items.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Unposted Procurement    | Any purchases made from other than the A&MM warehouse.                                                                                                                                                                                                                                                                                                                                                                                     |
| Upload                  | Upload is the transfer of the prime vendor’s invoice data from the prime vendor PC in pharmacy, into V*IST*A. Anyone holding the PSA ORDERS key can upload this data.                                                                                                                                                                                                                                                              |
| Verify                  | To confirm correctness of invoice data. Verification only occurs after the data has been processed. Once verified, balances are incremented. If there is at least one drug marked as a controlled substance on the invoice, only a <u>pharmacist</u> holding the PSA ORDERS key can verify the invoice. If there are no controlled substances, anyone who did not process the invoice, holding the PSA ORDERS key, can verify the invoice. |
| V*IST*A                 | Veterans Health Information Systems and Technology Architecture                                                                                                                                                                                                                                                                                                                                                                            |
| X12                     | A structured format for sending data. The invoice data file from the prime vendor is in this format.                                                                                                                                                                                                                                                                                                                                       |
> \<This page is intentionally left blank\>

# Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A
About Pharmacy Locations ....................................................................................................................................................... 10, 30
About This Manual ......................................................................................................................................................................... 1
Access and Verify Code Screen ...................................................................................................................................................... 82
Active, Unlinked Drugs in the ITEM MASTER file .................................................................................................................... 8
All Drugs Found ............................................................................................................................................................................... 45
All Drugs Not Found in DRUG File (#50) .......................................................................................................................................... 45
All Supply Items .............................................................................................................................................................................. 45
Automated DRUG/ITEM MASTER file Link by FSN ................................................................................................................ 7
Automated DRUG/ITEM MASTER file Link by NDC ............................................................................................................... 5
Automatic Processing ..................................................................................................................................................................... 46
> BBalance Adjustments .............................................................................................................................................................. 15, 35
Balance Adjustments History ................................................................................................................................................ 25, 63
Balance Initialization .............................................................................................................................................................. 16, 35
Batch Complete List ........................................................................................................................................................................ 77
Batch Work List ............................................................................................................................................................................... 69
> C
Changing a Pharmacy Location Type ........................................................................................................................................ 14, 34
Choosing a Site Name ............................................................................................................................................................... 11, 31
Compare Prices (DA/GIP) ........................................................................................................................................................... 17
Connect Unlinked DRUG/ITEM MASTER file Entries .............................................................................................................. 8
Connecting to the IP Address Screen .......................................................................................................................................... 82
Connecting with the Primary Inventory Point ................................................................................................................................ 14
Connection Menu (DRUG file/ITEM MASTER file .................................................................................................................... 3
Control Point Transaction Review .............................................................................................................................................. 22
Controlled Connection by FSN Match .......................................................................................................................................... 6
Controlled Connection by NDC Match ......................................................................................................................................... 5
Create a Pharmacy Location—Combined (Inpatient and Outpatient) ...................................................................................... 13, 34
Create a Pharmacy Location—Single Inpatient ..............................................................................................................12, 14, 15, 32
Create a Pharmacy Location—Single Outpatient ...................................................................................................................... 13, 33
Creating the Pharmacy Location ............................................................................................................................................... 10, 30
Credit Resolution .......................................................................................................................................................................... 59
> DDelete Un-processed Invoices ....................................................................................................................................................... 61
Detailed Report ............................................................................................................................................................................... 65
Dispensing Menu ..................................................................................................................................................................... 23, 40
Display Connected Drug and Procurement History .................................................................................................................... 8
Drug Balances by Location .................................................................................................................................................... 25, 63 DRUG file/ITEM MASTER file Comparison Report .................................................................................................................. 6
Drug Found in DRUG File (#50) .................................................................................................................................................... 46
Drug Not Found in NDF and DRUG File (#50) .................................................................................................................................. 49
Drug Receipt History Review....................................................................................................................................................... 23
Drug Transaction History ...................................................................................................................................................... 25, 63
Drugs Not Found in Linked Inventory ........................................................................................................................................ 17
> EEdit Verified Invoices ................................................................................................................................................................... 60
Editing Line Item Fields ................................................................................................................................................................... 56
Editing the Invoice Data and Selecting Line Items to be Edited ...................................................................................................... 55
Enter/Edit a Drug ................................................................................................................................................................... 16, 35
Enter/Edit Stock and Reorder Levels ......................................................................................................................................... 35
Entering Wards for Inpatient Sites ............................................................................................................................................ 12, 32
Error Screen for any Failed Security Measures ......................................................................................................................... 81
> FFSN Menu ........................................................................................................................................................................................ 6
> GGIP Interface Menu ........................................................................................................................................................................ 3 GUI Upload Program ....................................................................................................................................................................... 81
> IIcons ................................................................................................................................................................................................. 1
Inquire/Compare DRUG file/ITEM MASTER file ...................................................................................................................... 5
Inventory Interface ....................................................................................................................................................................... 16
Invoice Cost Summary ................................................................................................................................................................. 64
Invoice Review .............................................................................................................................................................................. 23
Invoice(s) to be Verified Messages ................................................................................................................................................. 53
IV Dispensing (All Drugs) ...................................................................................................................................................... 24, 41
IV Dispensing (Single Drug) .................................................................................................................................................. 23, 40
> L
Last Chance Edit .............................................................................................................................................................................. 50
Loadable Inventory Items Report ............................................................................................................................................... 17
> MMaintenance Reports Menu ................................................................................................................................................... 25, 63
Missing or Incorrect Data Found on Invoice ................................................................................................................................... 57
Monthly Summary .................................................................................................................................................................. 26, 64
More than One Active Pharmacy Location ............................................................................................................................... 18, 36
Multiple Drugs in DRUG File (#50) with the Same NDC and VSN .................................................................................................... 48
> N
National Drug File (NDF) Used for Suggested Match ...................................................................................................................... 47 NDC Duplicates Report (ITEM MASTER file) ........................................................................................................................... 4
NDC Menu....................................................................................................................................................................................... 4
No Errors Found on Invoice ............................................................................................................................................................ 57
No Invoice(s) to be Verified Messages ............................................................................................................................................ 53
> O
One Active Pharmacy Location ................................................................................................................................................. 18, 36
Orders Menu ................................................................................................................................................................................. 42
Outdated Medications .................................................................................................................................................................... 38
Outpatient Dispensing (All Drugs) ........................................................................................................................................ 24, 41
Outpatient Dispensing (Single Drug) .................................................................................................................................... 24, 41
Outstanding CreditsDetailed Report ........................................................................................................................................................................ 65
Summary Report ..................................................................................................................................................................... 65
> PPackage Functional Description .................................................................................................................................................... 1
Pharmacy Location Maintenance Menu ................................................................................................................................. 9, 29
Physical Inventory Balance Review ............................................................................................................................................. 17
Populate Pharmacy Location with Inventory Items .................................................................................................................. 17
Posted Drug Procurement History ................................................................................................................................................ 9
Prime Vendor Interface Menu ..................................................................................................................................................... 29
Print by Invoice Number ................................................................................................................................................................. 59
Print by Invoice Status .................................................................................................................................................................... 59
Print by Order Number ................................................................................................................................................................... 58
Print Orders .................................................................................................................................................................................. 58
Printing the NEW DRUG REPORT .................................................................................................................................................... 57
Processor and Verifier .................................................................................................................................................................. 66
Purchase Order Review ................................................................................................................................................................ 22
> RReceipt Failure Notification Message .......................................................................................................................................... 15
Receipts Menu ............................................................................................................................................................................... 20 Receiving Directly into Drug Accountability .................................................................................................................. 20, 21, 22
Report of Inventory Items’ Link to DRUG file .......................................................................................................................... 16
Report of Unlinked DRUG/ITEM MASTER file Entries ............................................................................................................ 7
Report Potential FSN Matches ...................................................................................................................................................... 6
Report Potential NDC Matches ..................................................................................................................................................... 4
Return Drug Credit Menu ............................................................................................................................................................... 69
Return Drug Credit Report .............................................................................................................................................................. 78
Revision History ............................................................................................................................................................................... i
> S
Screen Display with Updated Data from a Drug Match .................................................................................................................. 49
Selecting Invoices to be Edited ....................................................................................................................................................... 55
Selecting Line Item Fields to be Edited ........................................................................................................................................... 56
Set Up/Edit a Pharmacy Location ......................................................................................................................................... 10, 29
Setup Mail Message Recipients .............................................................................................................................................. 38, 61
Single Drug Match .......................................................................................................................................................................... 7 Special Instructions for the First Time Computer User .............................................................................................................. 2
Special Notations ............................................................................................................................................................................. 2
Stock and Reorder Level .............................................................................................................................................................. 66
Successful Upload Screen ............................................................................................................................................................. 83
Summary Report ............................................................................................................................................................................. 66
> T
To delete a user from the mail group ............................................................................................................................................. 62
Transfer Drugs Between Pharmacies .................................................................................................................................... 18, 36
Transfer Signature Sheet ....................................................................................................................................................... 26, 67
> U
Unable to Locate Invoice File .......................................................................................................................................................... 85
Unposted Procurement History ..................................................................................................................................................... 8
Update Prices ................................................................................................................................................................................ 18
Upload GUI Program ....................................................................................................................................................................... 81
Upload Status Report via MailMan............................................................................................................................................. 84
Uploading of Invoices Screen ....................................................................................................................................................... 83
> V
Vendor’s Stock Number has Changed ............................................................................................................................................. 48
Verification Error Report................................................................................................................................................................. 57
Verify Invoices .............................................................................................................................................................................. 52
Verifying Invoices That Do Not Need to Be Edited ......................................................................................................................... 54 View/Update Batch ......................................................................................................................................................................... 77


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Drug Accountability/Inventory Interface Version 3 User Manual (PSA*3*85)

### NDC Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA NDC MENU\]

This menu contains options to link drug entries in the ITEM MASTER file (#441) to NDC matched entries in the DRUG file (#50). If an ITEM MASTER file (#441) entry has an NDC that matches a DRUG file (#50) entry, then data from the two files can be compared. The *Report Potential NDC Matches* option report is available to show all the entries that can be matched by

NDC. Once the matches have been reviewed, they can be acted on with a controlled connection (drug-by-drug), or with an automated connection, which links the files wherever an NDC match occurs.

Example: NDC Menu

1.  NDC Duplicates Report (ITEM MASTER file)
2.  Report Potential NDC Matches
3.  Controlled Connection by NDC Match
4.  Automated DRUG/ITEM MASTER file Link by NDC
5.  Inquire/Compare DRUG file/ITEM MASTER file
6.  DRUG file/ITEM MASTER file Comparison Report
1.  
2.  1.  
    2.  
3.  
4.  1.  
    2.  

#### NDC Duplicates Report (ITEM MASTER file) 

> \[PSA NDC DUPLICATE REPORT\]

Currently in Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP), the same NDC cannot be entered for two different items. Since the NDC is relied on to link the DRUG file (#50) to the ITEM MASTER file (#441), it is important that the proper entry is located. The *NDC Duplicates Report* option scans through all the entries in the ITEM MASTER file (#441) looking for entries sharing the same NDC. Through printing this report and working with the local Acquisition and Materiel Management Service (A&MMS) Purchasing Agent, the user can ensure the ITEM MASTER file (#441) entries have the correct NDC before linking with the DRUG file (#50). The report lists the NDC, item number, item description, and vendor name.

#### Report Potential NDC Matches 

> \[PSA NDC REPORT\]

The *Report Potential NDC Matches* option scans through the DRUG file (#50) looking for drugs with an NDC that have not been inactive. If the same NDC can be located in the ITEM MASTER file (#441), this potential match is displayed. The report also indicates unmatched FSNs with the drug name.

> **NOTE:** It would be a good idea to first run this report and review the potential matches before considering either the controlled or automated connection options. The report lists the DRUG file’s (#50) NDC and drug name plus the potentially matched ITEM MASTER file’s (#441) item number and item description.

#### Controlled Connection by NDC Match 

> \[PSA NDC CONTROL LOOP\]

The *Controlled Connection by NDC Match* option moves through the same entries identified in the *Report Potential NDC Matches* option and provides the opportunity to link them one at a time. If the controller chooses not to link an entry, the option will continue to the next drug.

#### Automated DRUG/ITEM MASTER file Link by NDC 

> \[PSA NDC AUTO LOOP\]

The *Automated DRUG/ITEM MASTER file Link by NDC* option allows the user to link the entries identified in the *Report Potential NDC Matches* option simultaneously. The user will be prompted to select a device to direct the listing of links as they occur.

> **NOTE:** It is important to review the *Report Potential NDC Matches* option before considering using this option.

#### Inquire/Compare DRUG file/ITEM MASTER file 

> \[PSA DRUG INQUIRE\]

The *Inquire/Compare DRUG file/ITEM MASTER file* option displays packaging and price information from the DRUG file (#50) and ITEM MASTER file (#441) when identical NDCs exist regardless of whether linking has occurred. This option displays the entries one at a time while the next option, *DRUG file/ITEM MASTER file Comparison Report* option, shows a range of entries.

The report lists the DRUG file’s (#50) drug name, NDC, price per order unit (PPOU), order unit, packaging, price per dispense unit (PPDU), and dispense unit. It also lists the ITEM MASTER file’s (#441) item description, NDC, price per order unit (PPOU), order unit, date of price, packaging, price per dispense unit (PPDU) for each order unit, and the vendor name.

#### DRUG file/ITEM MASTER file Comparison Report 

> \[PSA COMPARISON REPORT\]

The *DRUG file/ITEM MASTER file Comparison Report* option allows the user to select a short range of DRUG file (#50) and ITEM MASTER file (#441) comparative information on packaging and pricing. The report lists the DRUG file’s (#50) drug name, drug number, NDC, price per order unit (PPOU), order unit, dispense units per order unit (DUOU), price per dispense unit (PPDU), and dispense unit. It also lists the ITEM MASTER file’s (#441) item name, item number, National Stock Number (NSN), NDC, price per dispense unit (PPDU), and vendor name.

### FSN Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA FSN MENU\]

Similar to the *NDC menu* option, this menu contains options to link DRUG file (#50) entries with a FSN to the ITEM MASTER file (#441). If an ITEM MASTER file (#441) entry has a National Stock Number (NSN) that matches a DRUG file (#50) FSN, then the two files can be linked. The *Report Potential FSN Matches* option shows all the entries that can be matched by FSN. Once the matches have been reviewed, they can be acted on with a controlled connection (drug-by-drug) or with an automated connection (linking all drugs with an NDC match).

Example: FSN Menu

1.  Report Potential FSN Matches
2.  Controlled Connection by FSN Match
3.  Automated DRUG/ITEM MASTER file Link by FSN
    1.  
    1.  

#### Report Potential FSN Matches 

> \[PSA FSN REPORT\]

The *Report Potential FSN Matches* option scans through the DRUG file (#50) looking for drugs that have an FSN and have not been inactive. If the same NSN is located in the ITEM MASTER file (#441), the entries from each file will be displayed as a potential match. It is a good idea to first run this report and review the potential matches before considering either the controlled or automated connection options. The report lists DRUG file’s (#50) drug name and NDC with the ITEM MASTER file’s (#441) matching item number and item name.

#### Controlled Connection by FSN Match 

> \[PSA FSN CONTROL LOOP\]

The *Controlled Connection by FSN Match* option allows movement through the entries identified in the *Report Potential FSN Matches* option and links them one at a time. If the user chooses not to link an entry, the option will continue to the next drug.

#### Automated DRUG/ITEM MASTER file Link by FSN 

> \[PSA FSN AUTO LOOP\]

The *Automated DRUG/ITEM MASTER file Link by FSN* option allows the user to move through the same entries identified in the *Report Potential FSN Matches* option and link them all at once. The user is asked to select a device to print the listing of links as they occur.

> **NOTE:** It is important to run the *Report Potential FSN Matches* option first and review before considering using this option.

### Single Drug Match 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA SINGLE DRUG MATCH\]

The *Single Drug Match* option links one drug at a time, finding matches between the DRUG file (#50) and ITEM MASTER file (#441). The system attempts first to match by NDC, displaying matches for approval. If no NDC match is found, the system searches for matches of the DRUG file’s (#50) FSN field (#6) to the ITEM MASTER file’s (#441) NSN field (#5). If located, the match is displayed for approval. If there are still no matches, then the user can look directly at the ITEM MASTER file (#441). The user can select a match by entering the first three or four letters of the generic or brand name. Finally, if the drug is linked to the NDF, the user can search each NDC for a match in the ITEM MASTER file (#441). Some drugs in the NDF may contain as many as thirty or forty NDCs. This process can be exited at any time. When using this option to review an existing link, the link between a particular item can be broken by entering the “@” character.

### Report of Unlinked DRUG/ITEM MASTER file Entries 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA UNLINKED REPORT\]

The *Report of Unlinked DRUG/ITEM MASTER file Entries* option can be run at any point in the linking process to see what entries are not yet linked to the ITEM MASTER file (#441). If the user is considering using the *Connect Unlinked DRUG/ITEM MASTER file Entries* option, this report will provide a helpful preview of the unlinked drugs. The report lists the drug name, FSN, NDC, and yes/no if the NDC is in the NDF.

### Connect Unlinked DRUG/ITEM MASTER file Entries 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA UNLINKED LOOP\]

The *Connect Unlinked DRUG/ITEM MASTER file Entries* option scans through the DRUG file (#50) looking for drugs not yet linked to the ITEM MASTER file (#441) that are not inactive.

The user may preview the unlinked entries by running the *Report of Unlinked DRUG/ITEM MASTER file Entries* option. Whenever the option is exited, the last drug linked, date, time, and the user’s name will be stored. The next user will have the choice of resuming with this drug upon entering this option.

### Active, Unlinked Drugs in the ITEM MASTER file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA ACTIVE DRUGS/ITEM MASTER FILE\]

The *Active, Unlinked Drugs in the ITEM MASTER file* option allows the user to scan the ITEM MASTER file (#441) for drugs not yet linked to the DRUG file (#50), which have been purchased since the last date entered. The report lists the ITEM MASTER file’s (#441) item number, item name, NSN, vendor name of the last vendor purchased from, NDC, and the items long description.

### Display Connected Drug and Procurement History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DISPLAY CONNECTED DRUG\]

The *Display Connected Drug and Procurement History* option displays the comparison data for both the DRUG (#50) and ITEM MASTER files (#441) if a connection was made. The display will show a procurement history for a selected date range and control point, and the vendor’s price/packaging data.

### Unposted Procurement History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA UNPOST PROCURMENT HISTORY\]

The *Unposted Procurement History* option prints a report listing all pharmacy procurements for a selected month. The report includes a detailed list of each item procured, the quantity received, the NDC, the DRUG file’s (#50) generic drug name, and vendor name.

> **NOTE:** If the user chooses to print this report to a printer, the following prompts will not be seen: “Print item totals?” and “Would you like a list of high dollar items?”. If the user wishes to respond to these questions, this report will need to be displayed on the screen.

### Posted Drug Procurement History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA POSTED DRUG REPORT\]

The *Posted Drug Procurement History* option produces an alphabetical listing of drugs procured from the warehouse for a selected month. The report lists the primary inventory point, item number, item name, quantity ordered, quantity received, packaging, price per order unit (PPOU), total cost for the item, date purchased, and transaction number. A total for each item is printed for the quantity ordered, quantity received, and total cost.

> **NOTE:** If the user chooses to print the *Posted Drug Procurement History* on a printer, the following prompt will not be seen: “Would you like a list of high dollar items?”. If the user wishes to respond to this question, this report will need to be displayed on the screen.

### Set Up/Edit a Pharmacy Location 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA LOCATION EDIT\]

The *Set Up/Edit a Pharmacy Location* option provides the capability to create a pharmacy location and connect it with a primary inventory point.

Creating the Pharmacy Location

U<u>About Pharmacy Locations</u>U

Locations are Outpatient (OP), Inpatient (IP), or a Combined (OP/IP). The user can have more than one location - even more than one type of location (for instance, a multi-divisional facility might procure for several divisions).

The User can create a location for each Inpatient or Outpatient site in order to track drug balances separately. Or, create a Combined location, like ALABASTER, that tracks Inpatient and Outpatient drug balances together.

U<u>Choosing a Site Name</u>U

How the site will track the drugs will depend on the type of pharmacy location chosen.

The three choices are Inpatient, Outpatient, or Combined.

- Inpatient: will track drugs only in the Inpatient dispensing site.
- Outpatient: will track drugs only in the Outpatient pharmacy/clinic.
- Combined: tracks all the drugs together in the Inpatient dispensing site and the Outpatient pharmacy/clinic. Only one total per drug is received.

A site is the physical location where drugs are stored and dispensed. If the facility maintains more than one Inpatient or Outpatient site, the user will be asked to choose a site for this pharmacy location.

> ![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/002.png)

> Multi-divisional facilities can track drugs in a variety of locations.

U

<u>Entering Wards for Inpatient Sites</u>U

Assign wards to each Inpatient site. Each ward can be connected to only one Inpatient site. This information affects the gathering of IV and Unit Dose dispensing data.

Example: Create a Pharmacy Location—Single Inpatient

Select GIP Interface Option: 2 Pharmacy Location Maintenance Menu

1.  Set Up/Edit a Pharmacy Location
2.  Balance Adjustments
3.  Balance Initialization
4.  Enter/Edit a Drug
5.  Inventory Interface ...
6.  Update Prices

Select Pharmacy Location Maintenance Menu Option: 1 Set Up/Edit a Pharmacy Location

Select one of the following:

1.  INPATIENT
2.  OUTPATIENT
3.  COMBINED (IP/OP)

Select Pharmacy type: 1 INPATIENT

Creating INPATIENT

For the purpose of collecting Unit Dose and IV dispensing data, any ward at which such dispensing might ever occur should be added. The ONLY reason to NOT add a ward would be if the dispensing at that ward should NOT update COMBINED (IP/OP).

*\[There is NO harm in adding inactive wards.\]*

INPATIENT is linked to 1 WEST, 1 SOUTH, 1 NORTH, 2 WEST, 2 SOUTH, 2 NORTH,

2 EAST, 1 EAST, 3 WEST, 3 EAST, 3 SOUTH, 4 EAST, 4 NORTH, 5 WEST, 5 EAST,

5 SOUTH, 6 WEST, 6 SOUTH, 7 EAST, 7 WEST, 8 EAST, 8 WEST.

INPATIENT DISPENSING UPDATE?: *\[Mark with Y if you have established current balances.\]*

PRIME VENDOR?: YES// ??

To more efficiently process Prime Vendor receipts, setting this flag to

"Yes" will allow you to store an obligation number. This number will

then be offered as a default whenever using the Receive Directly into

Drug Accountability option on the Receiving Menu.

CHOOSE FROM:

1 YES

0 NO

PRIME VENDOR?: YES// \<Enter\>

CURRENT PRIME VENDOR PO#: 521-A70005// \<Enter\>

Example: Create a Pharmacy Location—Single Outpatient

Select Pharmacy Location Maintenance Menu Option: 1 Set Up/Edit a Pharmacy Location

Select one of the following:

1.  INPATIENT
2.  OUTPATIENT
3.  COMBINED (IP/OP)

Select Pharmacy type: 2 OUTPATIENT

Outpatient site selection affects the collection of dispensing data.

OUTPATIENT SITE: PELHAM// ?

Enter the Outpatient Site from which to gather prescription dispensing

data.

ANSWER WITH PHARMACY SITE NAME, OR SITE NUMBER, OR RELATED INSTITUTION: PELHAM

OUTPATIENT SITE: PELHAM// \<Enter\>

PRIME VENDOR?: ??

To more efficiently process Prime Vendor receipts, setting this flag to

"Yes" will allow you to store an obligation number. This number will then

be offered as a default whenever using the Receive Directly into

Drug Accountability option on the Receiving Menu.

CHOOSE FROM:

YES

NO

PRIME VENDOR?: YES// \<Enter\>

CURRENT PRIME VENDOR PO#: 521-A70005// \<Enter\>

Example: Create a Pharmacy Location—Combined (Inpatient and Outpatient)

Select Pharmacy Location Menu Maintenance Option: 1 Set Up/Edit a Pharmacy Location

Select one of the following:

1.  INPATIENT
2.  OUTPATIENT
3.  COMBINED (IP/OP)

Select Pharmacy type: 3 COMBINED (IP/OP)

Creating COMBINED

For the purpose of collecting Unit Dose and IV dispensing data, any ward

at which such dispensing might ever occur should be added. The ONLY

reason to NOT add a ward would be if the dispensing at that ward should

NOT update COMBINED (IP/OP).

COMBINED is linked to 1 WEST, 1 SOUTH, 1 NORTH, 2 WEST, 2 SOUTH, 2 NORTH,

2 EAST, 1 EAST, 3 WEST, 3 EAST, 3 SOUTH, 4 EAST, 4 NORTH, 5 WEST, 5 EAST, 5

SOUTH, 6 WEST, 6 SOUTH, 7 EAST, 7 WEST, 8 EAST, 8 WEST.

INPATIENT DISPENSING UPDATE?: \<Enter\>

Outpatient site selection affects the collection of dispensing data.

OUTPATIENT SITE: MAYLENE// \<Enter\>

PRIME VENDOR?: YES// ??

To more efficiently process Prime Vendor receipts, setting this flag to

"Yes" will allow you to store an obligation number. This number will then

be offered as a default whenever using the Receive Directly into

Drug Accountability option on the Receiving Menu.

CHOOSE FROM:

1 YES

0 NO

PRIME VENDOR?: YES// \<Enter\>

CURRENT PRIME VENDOR PO#: 521-A70005// \<Enter\>

*\[At this point the prompts will be the same regardless of pharmacy location type.\]*

U

<u>Changing a Pharmacy Location Type</u>U

- The user can change a Combined location to a separate Inpatient and Outpatient location. If the Outpatient activity needs to be tracked, the user must create an Outpatient location.
- A site with an existing Inpatient and Outpatient location can be changed to a Combined location.

U<u>Connecting with the Primary Inventory Point</u>U

The next prompt is the primary inventory point. The connection to a primary inventory point automates the receiving process. Connecting to multiple primary inventory points is allowed.

Only primary inventory points marked with “D” for Drug Accountability in the GENERIC INVENTORY file’s (#445) SPECIAL INVENTORY POINT TYPE field (#15) can be connected.

The receipt failure notification prompt generates mail messages when items are received that are not connected to the DRUG file (#50) or not stocked in the pharmacy location. This will help track drugs only if the drugs stocked in the primary inventory point directly coincide with the drugs in the pharmacy location. If the primary inventory point and pharmacy location inventories are not congruent, receipt failure notification will probably not be helpful.

Example: Connecting with the Primary Inventory Point

Select PRIMARY INVENTORY POINT(S): ?

ANSWER WITH PRIMARY INVENTORY POINT(S)

YOU MAY ENTER A NEW PRIMARY INVENTORY POINT(S), IF YOU WISH

For Controlled Substances enter the name of the Pharmacy Inventory

Point which contains ONLY the controlled substances stored in the Pharmacy MASTER VAULT.

Must be Special Inventory Type "D" for Drug Accountability.

ANSWER WITH GENERIC INVENTORY INVENTORY POINT

CHOOSE FROM:

521-INPATIENT PHARMACY PRIMARY

521-OUTPATIENT PHARMACY PRIMARY

*\[If the system does not display primary inventory points to choose from, you must mark yourprimary inventory point as a pharmacy location.\]*

Select PRIMARY INVENTORY POINT(S): 521-INPATIENT PHARMACY PRIMARY

ARE YOU ADDING '521-INPATIENT PHARMACY' AS

A NEW PRIMARY INVENTORY POINT(S) (THE 1ST FOR THIS DRUG ACCOUNTABILITY STATS)? Y (YES)

RECEIPT MAIL GROUP: ??

Enter the name of the mail group that should receive messages

whenever inventory items cannot be received into a pharmacy location

and also this same group will receive DRUG file price update

messages.

RECEIPT MAIL GROUP: GROUP

The GROUP mail group has not been created!

Messages can't be sent until creation.

RECEIPT FAILURE NOTIFICATION?: ?

Enter "1" or "Y" to transmit a mailman message to the receiver and the

RECEIPT FAILURE mail group each time a failure occurs.

CHOOSE FROM:

1 YES

0 NO

RECEIPT FAILURE NOTIFICATION?: ??

If a Drug Accountability location is linked to a primary inventory point,

items received into the primary inventory point will also be updated in

the Drug accountability location. If items are received that are not

connected to the DRUG file (#50) or not stocked in the Drug Accountability

location, and this field is set to “YES”, the receiver and the RECEIPT

FAILURE mail group will be notified with a list of failed items.

Choose from

1 YES

0 NO

*\[Mark Y if your primary inventory point is populated only with drugs designated in thepharmacy location. If your primary inventory point contains drugs not tracked in your pharmacy location, leave this field blank or mark with N.\]* RECEIPT FAILURE NOTIFICATION?: YES Would

you like to loop through 521-INPATIENT PHARMACY'S items to check for any new entries that are ready to load? YES Load inventory quantities also? Yes// ?

*\[Inventory quantities will be multiplied by the dispensing unit conversionfactor.\]*

Load inventory quantities also? Yes// \<Enter\>

OK to load TRIFLUOPERAZINE HCL 5MG TAB from the DRUG file

linked to inventory item: TRIFLUOPERAZINE? Yes// \<Enter\> TRIFLUOPERAZINE HCL 5MG TAB

ARE YOU ADDING 'TRIFLUOPERAZINE HCL 5MG TAB' AS A NEW DRUG (THE 6TH FOR THIS DRUG ACCOUNTABILITY

STATS)? Y (YES)

DRUG BALANCE: 2500// \<Enter\>

Updating Beginning balance and transaction history.

Add/edit drugs? No// \<Enter\>

Inactive Date: \<Enter\>

Example: Receipt Failure Notification Message

Subj: Failed DA/GIP Receipts for 521-93-1-023-0004 \[#356992\]

01 Dec 92 15:11 CST 2 Lines

From: Failed Receipt Notifier in 'IN' basket. Page 1

-----------------------------------------------------------------------------

\#9 DOXORUBICIN HYDROCHLORIDE-POSTED STOCK INJECTION-VI NOT STOCKED. 430

NITROGLYCERIN-POSTED STOCK TRANSDERMAL SYSTEM 25MG-30S NOT LINKED.

### Balance Adjustments 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA BALANCE ADJUSTMENTS\]

The *Balance Adjustments* option allows the user to review and/or enter an adjustment to correct the balance of a drug.

This option is locked by the PSAMGR key.

### Balance Initialization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA BALANCE INITIALIZE\]

The *Balance Initialization* option allows the user to establish the balance for any drugs in the pharmacy location that do not have a balance.

### Enter/Edit a Drug 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DRUG ENTER/EDIT\]

The *Enter/Edit a Drug* option is used to add a new drug to the pharmacy location or establish or display the balance of an existing drug.

### Inventory Interface 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA GIP MENU\]

The following options are used for reporting and loading items from a primary inventory point to a pharmacy location:

Example: Inventory Interface Menu

1.  Report of Inventory Items’ Link to DRUG file
2.  Loadable Inventory Items Report
3.  Populate Pharmacy Location with Inventory Items
4.  Drugs Not Found in Linked Inventory
5.  Physical Inventory Balance Review
6.  Compare Prices (DA/GIP)
    1.  
    2.  
    3.  
    4.  
    5.  
    6.  
    7.  
    8.  
    9.  
    10. 
    11. 
    12. 
    13. 

#### Report of Inventory Items’ Link to DRUG file 

> \[PSA GIP LINK REPORT\]

The *Report of Inventory Items’ Link to DRUG file* option shows which inventory items are linked to the DRUG file (#50). If there is a link, the report will show the specific link between the inventory and the DRUG file (#50). Drugs must be linked to be loaded in the *Populate Pharmacy Location with Inventory Items* option. The report lists the item number, item description, and the linked drug name.

#### Loadable Inventory Items Report 

> \[PSA GIP REPORT\]

The *Loadable Inventory Items Report* option shows the inventory items with DRUG file (#50) links not yet added to a selected pharmacy location. These drugs will be loaded in the *Populate Pharmacy Location with Inventory Items* option. The report lists the item number, item name, linked drug, order unit balance, order unit, dispense unit balance, and dispense unit.

#### Populate Pharmacy Location with Inventory Items 

> \[PSA GIP POPULATE\]

The *Populate Pharmacy Location with Inventory Items* option loads linked drugs from the primary inventory point into a selected pharmacy location. The user can view the list of loadable items before loading. This same list is available under the *Loadable Inventory Items’ Report* option.

#### Drugs Not Found in Linked Inventory 

> \[PSA DRUGS NOT IN INVENTORY\]

The *Drugs Not Found in Linked Inventory* option lists the drugs in a pharmacy location that have not been loaded into the corresponding primary inventory point. The report lists drug name, connected item number, connected item name, and the primary inventory point that stocks the item.

#### Physical Inventory Balance Review 

> \[PSA GIP COMPARE\]

The *Physical Inventory Balance Review* option displays selected drugs with their pharmacy location balance and primary inventory point balance.

#### Compare Prices (DA/GIP) 

> \[PSA GIP DISCREPANCIES\]

The *Compare Prices (DA/GIP)* option lists DA V. 3.0 prices in comparison with Generic Inventory Package’s prices and the conversion factor.

### Update Prices 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA GIP CONT BAL UPDATE\]

The *Update Prices* option allows a comparison of prices in the DRUG file (#50) with prices in the Generic Inventory Package and then it will update the DRUG file (#50) if desired.

### Transfer Drugs Between Pharmacies 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA TRANSFER DRUGS\]

The *Transfer Drugs Between Pharmacies* option allows a pharmacist to move drugs between pharmacy locations. The number of dispense units to be moved is subtracted from the dispensing pharmacy location and added to the receiving pharmacy location. A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET may be printed after all transfers are completed.

This option is locked by the PSAMGR and PSJ RPHARM keys.

Example: One Active Pharmacy Location

There is only one active pharmacy location.

There must be at least two to transfer drugs.

If there is only one active pharmacy location, the user is exited from the option.

Example: More than One Active Pharmacy Location

Enter your Current Signature Code: SIGNATURE VERIFIED

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: RIVERCHASE (IP)
3.  OUTPATIENT: PELHAM (OP)

Select Transfer from Pharmacy: (1-3): 1

Select the pharmacy location that will transfer the drug. This pharmacy location will have its drug balance decreased when the transfer is complete.

Example: Transfer Drugs between Pharmacies

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

Select DRUG: ACETAMINOPHEN 325MG TAB CN103

Dispense Unit: TAB Current Balance: 60

Enter Quantity to Transfer: (1-60): 10

Select the drug and number of dispense units to be transferred.

Choose the pharmacy location receiving the transferred drugs:

1.  INPATIENT: RIVERCHASE (IP)
2.  OUTPATIENT: PELHAM (OP)

Select Transfer to Pharmacy: (1-2): 2

Select the pharmacy that will receive the drug. Its balance will be increased when the transfer is complete.

INPATIENT: PELHAM (OP) does not stock ACETAMINOPHEN 325MG TAB!

Do you want to continue? YES

Answer yes if it is okay to now stock this drug in the receiving pharmacy location.

-----------------------------------------------------------------------------

ACETAMINOPHEN 325MG TAB

Transferring: 10 (TAB)

From: COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

To : OUTPATIENT: PELHAM (OP)

-----------------------------------------------------------------------------

Is this OK? NO// YES

Updating pharmacy on-hand balances now............. Done!

If the displayed transfer information is correct, enter YES. The drug balance in the transferring pharmacy location is decreased. The drug balance in the receiving pharmacy location is increased. If the drug is new to the receiving pharmacy location, a MailMan message is sent to holders of the PSAMGR key letting them know that a new drug is being added to that location. The MailMan message lists the drug, dispense unit, number of dispense units transferred, pharmacist who initiated the transfer, transferring pharmacy location, and the receiving pharmacy location.

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

Select DRUG: \<Enter\>

If there are more drugs to be transferred to the <u>same</u> pharmacy location, the user can select them now. If not, press \<Enter\> to select the next transferring pharmacy location.

Example: Transfer Drugs between Pharmacies (continued)

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: RIVERCHASE (IP)
3.  OUTPATIENT: PELHAM (OP)

Select Transfer from Pharmacy: (1-3): ^

If the user wants to transfer drugs from another pharmacy location, select that location now. If the user is finished transferring drugs, enter \<^\>.

Print transfer signature sheets? Y// \<Enter\>

DEVICE: HOME// *\[Select Print Device\]*

A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET can be printed at this

time for all the transfers just entered. This sheet prints the transfer data for each unique combination of pharmacy locations. It is used to record the signature of the person who received the drugs. See the *Transfer Signature Sheet* option for an example of this sheet.

### Receiving Directly into Drug Accountability 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RECEIVING\]

This option processes prime vendor receipts from an invoice, updating the balance, transaction file, and monthly activity.

> **IMPORTANT:** Once received, the drug balances are incremented in the pharmacy location and/or master vault.

The invoiced drug’s order unit is compared to the ORDER UNIT field (#12) in the DRUG file

(#50) and the dispense units per order unit (DUOU) is compared to the DISPENSE UNITS PER ORDER UNIT field (#15) in the DRUG file (#50). If the order unit and dispense units per order unit (DUOU) are the same, the NDC (#31), PRICE PER ORDER UNIT (#13), and PRICE PER DISPENSE UNIT (#16) fields in the DRUG file (#50) may be updated.

The following condition must be met to update the NDC field (#31).

- If the invoice NDC is different from the NDC field (#31), the NDC field (#31) is overwritten with the invoiced NDC.

The following condition must be met to update the PRICE PER ORDER UNIT field (#13) and PRICE PER DISPENSE UNIT field (#16).

- If the invoiced price per order unit (PPOU) is different than the PRICE PER ORDER UNIT field (#13), the PRICE PER ORDER UNIT field (#13) is overwritten with the new prorated price per order unit (PPOU). The PRICE PER DISPENSE UNIT field (#16) is also overwritten with the new prorated price per dispense unit (PPDU).

Example: Receiving Directly into Drug Accountability V. 3.0

1.  Receiving Directly into Drug Accountability
2.  Purchase Order Review
3.  Control Point Transaction Review
4.  Drug Receipt History Review
5.  Invoice Review

Select Receiving Menu Option: 1 Receiving Directly into Drug Accountability

Select one of the following:

1.  INPATIENT
2.  OUTPATIENT
3.  COMBINED (IP/OP)

Select Pharmacy type: 1 INPATIENT

Because there is more than one Inpatient Site at this facility, I need you to select an AR/WS Inpatient Site Name: PELHAM

COMBINED (IP/OP) for PELHAM

The current Prime Vendor PO# for this location doesn't seem current.

-----------------------------------------report continues----------------------------------------

Example: Receiving Directly into Drug Accountability V. 3.0 (continued)

Would you like to correct it? Yes// \<Enter\>

CURRENT PRIME VENDOR PO#: 521-C70001// \<Enter\>

Select Prime Vendor Obligation Number: 521-C70001// \<Enter\> 08-25-92 ST Pending

Fiscal Action

FCP: 022 \$ 6000

Select Pharmacy Transaction number: 521-97-1-022-0001

Please enter the Prime Vendor Invoice number: ??

To allow the entering of a Prime Vendor Invoice number for a receipt. The

IFCAP Purchase Order number may be used all month and there may not be a

corresponding IFCAP transaction number for each Prime Vendor receipt.

The invoice will be stored, allowing look-ups for receipts against this invoice.

Please enter the Prime Vendor Invoice number: 119202

Select INPATIENT drug: METOPROLOL TARTRATE 50MG TAB CV100

NDC: 64738-8236-1 \<Enter\>

Order Unit: BT \<Enter\> BOTTLE

Dispense Units: TAB

Dispense Units per Order Unit: 1000// \<Enter\>

Price per Order Unit: (0-9999): 93.6 \<Enter\>

Quantity received: (0-9999999):25 \<Enter\> Converted quantity: 25000 Okay

to post? Yes// YES

There were 60 on hand. There are now 25060 on hand.

Updating monthly receipts and transaction history.

### Purchase Order Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA PURCHASE ORDER REVIEW\]

The *Purchase Order Review* option reviews all receipt transactions for a selected purchase order. It lists the purchase order number, purchase order date, receiving pharmacy location, date and time the drug was received, drug name, quantity received, and the name of the person who received the drugs.

### Control Point Transaction Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA CP TRANSACTION REVIEW\]

The *Control Point Transaction Review* option reviews the receipt transactions processed for a selected control point transaction number. The report format is the same as the Purchase Order Review report.

### Drug Receipt History Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DRUG HISTORY\]

The *Drug Receipt History Review* option reviews drugs received over a selected time range for a selected drug. One, many, or all drugs can be printed. The report lists the drug name, receiving pharmacy location, date and time the drug was received, quantity received, and the person’s name that received the drug.

### Invoice Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA INVOICE REVIEW\]

The *Invoice Review* option lists all receipts posted for a selected prime vendor invoice number. The report lists the invoice number, receiving pharmacy location, date and time the drug was received, quantity received, and the person’s name that received the drug.

### IV Dispensing (Single Drug) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA IV SINGLE\]

The *IV Dispensing (Single Drug)* option collects intravenous (IV) dispensing information for a single drug in a location from the IV STATS file (#50.8). If present, the last IV collection date is used as a starting point. Otherwise, the user-selected date is used. The *Drug Transaction History* option can be run to produce a report with which to verify dispensing information. The report lists the pharmacy location that dispensed the IV, the date it was dispensed, total dispensed, price per dispense unit (PPDU), and total cost.

### IV Dispensing (All Drugs) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA ALL DRUGS\]

The *IV Dispensing (All Drugs)* option collects IV dispensing information for all drugs from the IV STATS file (#50.8). If present, the last IV collection date is used as a starting point. Otherwise, the user needs to enter a date from which to begin collection. The report lists the pharmacy location that dispensed the IV, the date it was dispensed, total dispensed, price per dispense unit (PPDU), and total cost.

### Outpatient Dispensing (Single Drug) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA OP SINGLE\]

The *Outpatient Dispensing (Single Drug)* option collects Outpatient (OP) dispensing information for a single drug from the PRESCRIPTION file (#52). If present, the last OP dispensing date is used as a starting point. Otherwise, the user will need to enter a date from which to begin collection. A report of the updating lists the drug name, date dispensed, total dispensed units dispensed, price per dispense unit (PPDU), dispense unit, total cost per date dispensed, and total cost for all dispensed dates.

### Outpatient Dispensing (All Drugs) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA OP ALL DRUGS\]

The *Outpatient Dispensing (All Drugs)* option collects OP dispensing information for all drugs in this location from the PRESCRIPTION file (#52). If present, the last OP dispensing date is used as a starting point. Otherwise, the user will need to enter a date from which to begin collection.

A report of the updating lists the drug name, date dispensed, total dispensed units dispensed, price per dispense units (PPDU), dispense unit, total cost per date dispensed, and total cost for all dispensed dates.

### Balance Adjustments History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA BALANCE ADJUSTMENTS REPORT\]

The *Balance Adjustments History* option reviews adjustments and transfers of a drug. The report lists the drug, transaction date and time, adjustment quantity, transfer quantity, transaction, adjustment reason, and pharmacy location that sent or received the transferred drug.

### Drug Balances by Location 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DISPLAY LOCATION\]

The *Drug Balances by Location* option generates a report by pharmacy location listing each of its drugs’ names, quantity on hand, and dispense unit.

### Drug Transaction History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DRUG DISPLAY\]

The *Drug Transaction History* option provides a transaction history for one, many, or all drug(s) within the pharmacy location for a given date range. It lists the date range, drug, beginning date, beginning balance, transaction date and time, transaction quantity, transaction type, person who made the transaction, and resulting balance.

If the transaction is <u>receiving</u> drugs, the purchase order number, transaction number, and invoice number are also listed.

If the transaction is <u>dispensing</u>, the report designates where the dispensing took place (Inpatient Medications or Outpatient pharmacy).

### Monthly Summary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA MONTHLY SUMMARY\]

The *Monthly Summary* option allows the user to print a pharmacy location’s detailed or summary monthly report of transactions made on one, many, or all drugs.

If the user selects the detailed report, the drug, beginning balance, total receipts, total dispensed, total adjustments, total transfers, and ending balance or one, many, or all drugs in the selected pharmacy location is printed.

If the user selects the summary report, the detailed report prints then a separate summary report follows. The summary report contains the drug, total receipts, total dispensed, total adjustments, and total transfers for one, many, or all drugs in the selected pharmacy location. A total line for the total receipts, total dispensed, total adjustments, and total transfers is printed.

### Transfer Signature Sheet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA TRANSFER SIGNATURE SHEET\]

The *Transfer Signature Sheet* option prints a report of all transferred drugs within a specific date range. This report is used to record the signature of the person who received the drugs or to review transfer history.

Example: Transfer Signature Sheet

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: RIVERCHASE (IP)
3.  OUTPATIENT: PELHAM (OP)

Select Transfer from Pharmacy: (1-3): 1

Select the pharmacy location that will send the drugs to the other pharmacy location.

Choose the pharmacy location receiving the transferred drugs:

1.  INPATIENT: RIVERCHASE (IP)
2.  OUTPATIENT: PELHAM (OP)

Select Transfer to Pharmacy: (1-2): 2

Select the pharmacy location that will receive the drugs from the transferring pharmacy locations.

Beginning Date: 8 12 (AUG 12, 1997)

Ending Date : 8 12 (AUG 12, 1997)

DEVICE: HOME// *\[Select Print Device\]*

Enter the date range to print the transfer signature sheets.

AUG 12,1997@12:40 D R U G A C C O U N T A B I L I T Y Page: 1

DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

TRANSFERRED TO: OUTPATIENT: PELHAM (OP)

-----------------------------------------------------------------------------

TRANSFER DATE QTY DRUG NEW BALANCE

-----------------------------------------------------------------------------

Aug 12, 1997@12:40 10 ACETAMINOPHEN 325MG TAB 50

Dispensed by: DAPHARMACIST51,THREE Rec'd by: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

(Full Name) (Full Name)

> \<This page is intentionally left blank.\>

### Set Up/Edit a Pharmacy Location 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA LOCATION EDIT\]

The *Set Up/Edit a Pharmacy Location* option creates and edits a pharmacy location. The pharmacy location’s name, location type, and drugs can be entered and edited. If it is an Inpatient pharmacy location, wards can also be linked and unlinked. If it is an Outpatient pharmacy location, IV rooms can be linked and unlinked.

Creating the Pharmacy Location<u>About Pharmacy Locations</u>

Locations are Outpatient (OP), Inpatient (IP), or a Combined (IP/OP). More than one location is available - even more than one type of location (for instance, a multi-divisional facility might procure for several combined locations).

Create a location for each Inpatient or Outpatient site in order to track drug balances separately. Or, create a Combined location, like ALABASTER, that tracks Inpatient and Outpatient drug balances together.

<u>Choosing a Site Name</u>

How the site will track the drugs will depend on the type of pharmacy location that is chosen.

The three choices are Inpatient, Outpatient, or Combined.

- Inpatient: will track drugs only in the Inpatient dispensing site.
- Outpatient: will track drugs only in the Outpatient pharmacy/clinic.
- Combined: tracks all the drugs together in the Inpatient dispensing site and the Outpatient pharmacy/clinic. Only one total per drug is received.

A site is the physical location where drugs are stored and dispensed. If the facility maintains more than one Inpatient or Outpatient site, the user will be asked to choose a site for this pharmacy location.

> ![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/003.png)

> Multi-divisional facilities can track drugs in a variety of locations.

<u>Entering Wards for Inpatient Sites</u>

Assign wards to each Inpatient site. Each ward can be connected to only one Inpatient site. This information affects the gathering of IV and Unit Dose dispensing data.

Example: Create a Pharmacy Location—Single Inpatient

Select Prime Vendor Interface Menu Option: 1 Pharmacy Location Maintenance Menu

1.  Set Up/Edit a Pharmacy Location
2.  Balance Adjustments
3.  Balance Initialization
4.  Enter/Edit a Drug
5.  Enter/Edit Stock and Reorder Levels
6.  Transfer Drugs Between Pharmacies
7.  Setup Mail Message Recipients
8.  Outdated Medications

Select Pharmacy Location Maintenance Menu Option: 1 Set Up/Edit a Pharmacy Location

Select one of the following:

1.  INPATIENT
2.  OUTPATIENT
3.  COMBINED (IP/OP)

Select Pharmacy type: <u>1</u> INPATIENT

Creating INPATIENT

For the purpose of collecting Unit Dose and IV dispensing data, any ward

at which such dispensing might ever occur should be added. The ONLY reason

to NOT add a ward would be if the dispensing at that ward should NOT

update COMBINED (IP/OP).

*\[There is NO harm in adding inactive wards.\]*

INPATIENT is linked to 1 WEST, 1 SOUTH, 1 NORTH, 2 WEST, 2 SOUTH, 2 NORTH,

2 EAST, 1 EAST, 3 WEST, 3 EAST, 3 SOUTH, 4 EAST, 4 NORTH, 5 WEST, 5 EAST,

5 SOUTH, 6 WEST, 6 SOUTH, 7 EAST, 7 WEST, 8 EAST, 8 WEST.

Add/edit drugs? No// \<Enter\> NO

Maintain reorder levels: YES// \<Enter\>

Days to keep invoice data: 180

Inactive Date: \<Enter\>

Example: Create a Pharmacy Location—Single Outpatient

Select Pharmacy Location Maintenance Menu Option: 1 Set Up/Edit a Pharmacy Location

Select one of the following:

1 INPATIENT

2 OUTPATIENT

3 COMBINED (IP/OP)

Select Pharmacy type: 2 OUTPATIENT

Outpatient site selection affects the collection of dispensing data.

OUTPATIENT SITE: PELHAM//?

Enter the Outpatient Site from which to gather collection of dispensing

data.

ANSWER WITH PHARMACY SITE NAME, OR SITE NUMBER, OR RELATED INSTITUTION: PELHAM

OUTPATIENT SITE PEHLHAM// \<Enter\>

Add/edit drugs? NO?? \<Enter\> NO

PELHAM Outpatient Site

Currently linked IV Rooms: PELHAM IV ROOM \#1

Link or unlink IV room (L/U): Link

Enter the IV rooms that receive IVs from the outpatient site.

Select IV ROOM NAME: PELHAM Room \#2

Select IV ROOM NAME: \<Enter\>

PELHAM Outpatient Site

IV rooms to be linked: PELHAM IV ROOM \#2

Should the IV rooms be linked? N// YES

Linking IV rooms.

The IV rooms were linked successfully.

Maintain reorder levels: YES?? \<Enter\>

Days to keep invoice data: 180

Inactive Date: \<Enter\>

Example: Create a Pharmacy Location—Combined (Inpatient and Outpatient)

Select Pharmacy Location Maintenance Menu Option: 1 Set Up/Edit a Pharmacy Location

Select one of the following:

1.  INPATIENT
2.  OUTPATIENT
3.  COMBINED (IP/OP)

Select Pharmacy type: 3 COMBINED (IP/OP)

Creating COMBINED

For the purpose of collecting Unit Dose and IV dispensing data, any ward

at which such dispensing might ever occur should be added. The ONLY

reason to NOT add a ward would be if the dispensing at that ward should

NOT update COMBINED (IP/OP).

COMBINED is linked to 1 WEST, 1 SOUTH, 1 NORTH, 2 WEST, 2 SOUTH, 2 NORTH,

2 EAST, 1 EAST, 3 WEST, 3 EAST, 3 SOUTH, 4 EAST, 4 NORTH, 5 WEST, 5 EAST,

5 SOUTH, 6 WEST, 6 SOUTH, 7 EAST, 7 WEST, 8 EAST, 8 WEST.

Outpatient site selection affects the collection of dispensing data.

OUTPATIENT SITE: // MAYLENE

Add/edit drugs? NO// \<Enter\> NO

MAYLENE Outpatient Site

Link or unlink Iv room (L/U): Link

Enter the IV rooms that receive IVs from the outpatient site.

Select IV ROOM NAME: MAYLENE IV ROOM \#1

Select IV ROOM NAME: \<Enter\>

MAYLENE Outpatient Site

IV rooms to be linked: MAYLENE IV ROOM \#1

Should the IV rooms be linked? N// YES

Linking IV rooms.

The IV rooms were linked successfully.

Maintain reorder levels: YES// \<Enter\>

Days to keep invoice data: 180

Inactive Date: \<Enter\><u>Changing a Pharmacy Location Type</u>

- The user can change a Combined location to a separate Inpatient and Outpatient location. If the Outpatient activity needs to be tracked, the user must create an Outpatient location.
- A site with an existing Inpatient and Outpatient location can be changed to a Combined location.

### Balance Adjustments 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA BALANCE ADJUSTMENTS\]

The *Balance Adjustments* option allows the user to review and/or enter an adjustment to correct the balance of a drug.

This option is locked by the PSAMGR key.

### Balance Initialization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA BALANCE INITIALIZE\]

The *Balance Initialization* option establishes the balance for any drugs that do not yet have a balance.

### Enter/Edit a Drug 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA PV DRUG ENTER/EDIT\]

The *Enter/Edit a Drug* option adds a new drug to the pharmacy location. If the drug is being added to the location and the location maintains stock and reorder levels, it prompts for the stock and reorder levels. It also displays the balance of an existing drug.

### Enter/Edit Stock and Reorder Levels 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA STOCK AND REORDER LEVELS\]

The *Enter/Edit Stock and Reorder Levels* option flags a pharmacy location or master vault to maintain or not maintain the stock and reorder levels. If the flag is set to YES, the user enters the drugs’ stock and reorder levels. These levels are used to determine if a mail message should be sent with the drugs that need to be ordered. Only holders of the PSJ RPHARM pharmacist key can set levels in master vaults.

The mail message is sent to the holders of the PSA ORDERS key. It is sent if at least one drug’s balance is equal to or less than the reorder level. The message lists the drug name, stock level, current balance, and number of dispense units to order for the pharmacy location or master vault. The number of dispense units to order is determined by subtracting the current balance from the stock level. If the user is not a pharmacist, only the pharmacy location data is sent. If the user is a pharmacist, the pharmacy location and master vault data are sent.

### Transfer Drugs Between Pharmacies 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA TRANSFER DRUGS\]

The *Transfer Drugs Between Pharmacies* option allows a pharmacist to move drugs between pharmacy locations. The number of dispense units to be moved is subtracted from the dispensing pharmacy location and added to the receiving pharmacy location. A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET may be printed after all transfers are completed.

This option is locked by the PSAMGR and PSJ RPHARM keys.

Example: One Active Pharmacy Location

There is only one active pharmacy location.

There must be at least two to transfer drugs.

If there is only one active pharmacy location, the user is exited from the option.

Example: More than One Active Pharmacy Location

Enter your Current Signature Code: SIGNATURE VERIFIED

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: PELHAM (IP)
3.  OUTPATIENT: HELENA (OP)

Select Transfer from Pharmacy: (1-3): 1

Select the pharmacy location that will transfer the drug. This pharmacy location will have its drug balance decreased when the transfer is complete.

Example: Transfer Drugs between Pharmacies

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

Select DRUG: ACETAMINOPHEN 325MG TAB CN103

Dispense Unit: TAB Current Balance: 60

Enter Quantity to Transfer: (1-60): 10

Select the drug and number of dispense units to be transferred.

Choose the pharmacy location receiving the transferred drugs:

1.  INPATIENT: PELHAM (IP)
2.  OUTPATIENT: HELENA (OP)

Select Transfer to Pharmacy: (1-2): 2

Select the pharmacy that will receive the drug. Its balance will be increased when the transfer is complete.

INPATIENT: HELENA (OP) does not stock ACETAMINOPHEN 325MG TAB!

Do you want to continue? YES

Answer yes if it is okay to now stock this drug in the receiving pharmacy location.

-------------------------------------------------------------------------------

ACETAMINOPHEN 325MG TAB

Transferring: 10 (TAB)

From: COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

To : OUTPATIENT: HELENA (OP)

--------------------------------------------------------------------------------

Is this OK? NO// YES

Updating pharmacy on-hand balances now.............. Done!

If the displayed transfer information is correct, enter YES. The drug balance in the transferring pharmacy location is decreased. The drug balance in the receiving pharmacy location is increased. If the drug is new to the receiving pharmacy location, a mail message is sent to holders of the PSAMGR key letting them know that a new drug is being added to that location. The mail message lists the drug, dispense unit, number of dispense units transferred, pharmacist who initiated the transfer, transferring pharmacy location, and the receiving pharmacy location.

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP) Select

DRUG: \<Enter\>

If there are more drugs to be transferred to the *same* pharmacy location, the user can select them now. If not, press \<ENTER\> to select the next transferring pharmacy location.

Example: Transfer Drugs between Pharmacies

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: PELHAM (IP)
3.  OUTPATIENT: HELENA (OP)

Select Transfer from Pharmacy: (1-3): ^

If the user wants to transfer drugs from another pharmacy location, select that location now. If the user is finished transferring drugs, enter \<^\>.

Print transfer signature sheets? Y// \<Enter\>

DEVICE: HOME// *\[Select Print Device\]*

A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET can be printed at this

time for all the transfers just entered. This sheet prints the transfer data for each unique combination of pharmacy locations. It is used to record the signature of the person who received the drugs. See the *Transfer Signature Sheet* option for an example of this sheet.

### Setup Mail Message Recipients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA MSG RECIPIENTS\]

The *Setup Mail Message Recipients* option is used to enter/delete personnel from the two mail groups used for notifying personnel of a change in NDC and/or Drug Price, and when drugs are below reorder levels.

See Section 3.3.7 under The Orders Menu for more detailed information.

This option is locked with the PSAMGR key.

### Outdated Medications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA OUTDATED MEDICATIONS\]

The *Outdated Medications* option gives the user the ability to select and store drugs that are to be returned to the manufacturer.

This option is locked with the PSAMGR key.

NOTES:

Marking a drug as Returned to Manufacturer does not create any adjustment to inventory quantities.

This option should only be used for non-controlled substances. Controlled substances that are to be returned should be documented in the Controlled Substances package.

Example: Enter Outdated Medications to Return to Manufacturer

Select Drug Accountability Menu Option: PHARmacy Location Maintenance Menu

Select Pharmacy Location Maintenance Menu Option: 8 Outdated

Medications

Select one of the following:

1.  Print Report
2.  Enter drugs Return to Manufacturer

Enter response: 2 Enter drugs Return to Manufacturer

Scan drug barcode or enter a drug name:

At this point you can scan a barcode to enter the drug.

Scan Drug barcode or enter a drug name: 028105004806

The software is programmed to try to match the item in several different ways. If the item cannot be located, the user will prompted to enter a drug name.

Select Drug : ACETA

1.  ACETAMINOPHEN 1000MG TABLET CN100
2.  ACETAMINOPHEN 325MG C.T. CN103
3.  ACETAMINOPHEN 325MG TABLET CN103
4.  ACETAMINOPHEN 650MG SUPPOS. CN103 02-03-01
5.  ACETAMINOPHEN ELIX. 160MG/5ML 4OZ CN103

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 3 ACETAMINOPHEN 325MG TABLET

Once the correct drug is entered, additional information is requested.

Number of containers : 1

Quantity being returned: : 100

Package type: BT// \<Enter\> BOTTLE

Is it ok to file the data entered? YES// Updating

Destruction holding file.

Updating Drug Accountability Transaction file.

Enter RETURN to continue or '^' to exit: ^

\*Pressing the Enter key automatically selects the default value shown to the left of the double slashes

After all items have been selected, the program will ask if a report is desired.

Would you like to print the returns report ? YES// \<Enter\>

If you are returning the items to the manufacturer at this time, the program will add today's date to the item to show when it was actually returned.

Are you returning the items to the manufacturer at this time? YES// \<Enter\>

The default start date for the report is 90 days in the past. In this example the report was requested on January 11, 2006.

Beginning Date: OCT 13, 2005// \<Enter\> (OCT 13, 2005)

DEVICE: HOME// \<Enter\> GENERIC INCOMING TELNET

This report can also be run when the manufacturer arrives to receive the medications. When the report is generated, the date is added to the item in the file for future reference.

### IV Dispensing (Single Drug) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA IV SINGLE\]

The *IV Dispensing (Single Drug)* option collects IV dispensing information for a single drug in a location from the IV STATS file (#50.8). If present, the last IV collection date is used as a starting point. Otherwise, the user-selected date is used. The *Drug Transaction History* option can be run to produce a report with which to verify dispensing information. The report lists the pharmacy location that dispensed the IV, the date it was dispensed, total dispensed, price per dispense unit (PPDU), and total cost.

### IV Dispensing (All Drugs) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA ALL DRUGS\]

The *IV Dispensing (All Drugs)* option collects IV dispensing information for all drugs from the IV STATS file (#50.8). If present, the last IV collection date is used as a starting point. Otherwise, the user needs to enter a date from which to begin collection. The report lists the pharmacy location that dispensed the IV, the date it was dispensed, total dispensed, price per dispense unit (PPDU), and total cost.

### Outpatient Dispensing (Single Drug) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA OP SINGLE\]

The *Outpatient Dispensing (Single Drug)* option collects OP dispensing information for a single drug from the PRESCRIPTION file (#52). If present, the last OP dispensing date is used as a starting point. Otherwise, the user will need to enter a date from which to begin collection. A report of the updating lists the drug name, date dispensed, total dispensed units dispensed, price per dispense units (PPDU), dispense unit, total cost per date dispensed, and total cost for all dispensed dates.

### Outpatient Dispensing (All Drugs) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA OP ALL DRUGS\]

The *Outpatient Dispensing (All Drugs)* option collects OP dispensing information for all drugs in this location from the PRESCRIPTION file (#52). If present, the last OP dispensing date is used as a starting point. Otherwise, the user will need to enter a date from which to begin collection.

A report of the updating lists the drug name, date dispensed, total dispensed units dispensed, price per dispense units (PPDU), dispense unit, total cost per date dispensed, and total cost for all dispensed dates.

### Process Uploaded Prime Vendor Invoice Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA PROCESS PRIME VENDOR DATA\]

Processing an invoice is matching the line items to the DRUG file (#50) and validating the invoice. To validate the invoice, the processor confirms all line item data. If the quantity received is different than the invoice quantity, the processor enters an adjustment. The processor also validates the drug, unit price, order unit, and the dispense units per order unit (DUOU). If the pharmacy location or master vault is flagged to maintain stock levels, the first time the drug is received the processor may enter the stock and reorder levels. Anyone holding the PSA ORDERS key can process the invoice.

This option is locked by the PSA ORDERS key

Example: Process Uploaded Prime Vendor Invoice Data

Select Orders Menu Option: PROCess Uploaded Prime Vendor Invoice Data

Enter your Current Signature Code: SIGNATURE VERIFIED

The invoices are being assigned to the pharmacy location. Please wait....

-----------------------------------------report continues--------------------------------

If there is only one pharmacy location and the invoice contains at least one drug that is not marked as a controlled substance, the software automatically assigns the invoice to the pharmacy location.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

If there is more than one active pharmacy location, the active locations are listed. The user is asked to assign the invoice to one of the locations.

\<\<\< ASSIGN A PHARMACY LOCATION SCREEN \>\>\>

-----------------------------------------------------------------------------

1\. COMBINED (IP/OP): ALABASTER VAMC INPATIENT (IP)

ALABASTER VAMC OUTPATIENT (OP)

2\. OUTPATIENT: PELHAM CLINIC (OP)

Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 1997

Some controlled substances

Pharmacy Location: (1-2): 1Note: If controlled substances were found on the invoice one of two things will happen.

1)  If the invoice contains drugs that are marked as a controlled substance and drugs that are not marked as controlled substances, the user will assign a master vault and pharmacy location to the invoice. When the pharmacy location is assigned the message “Some controlled substances” will appear below the invoice data to let the user know that a master vault will be assigned, as shown on the previous box.
2)  If all of the drugs are marked as a controlled substance the user will only assign the invoice to a master vault. If all of the drugs are marked as a controlled substance, the message “\*\*All controlled substances” will appear below the invoice data to let the user know that a pharmacy location was not assigned, as shown in the box below.

If NO drugs were marked as a controlled substance, the invoice will only be assigned to a pharmacy location.

\<\<\< ASSIGN A MASTER VAULT SCREEN \>\>\>

-----------------------------------------------------------------------------

1\. MASTER VAULT 1

2\. MASTER VAULT 2

Order#: C2529410 Invoice#: 54733371 Invoice Date: Jan 07, 1997

\*\* All controlled substances

Select Master Vault: (1-2): 2

Enter RETURN to continue or '^' to exit: \<Enter\>

If there is more than one active master vault, the active ones are listed and the user is asked to assign the invoice to one of the vaults.

If there is only one master vault and the invoice contains at least one drug that is marked as a controlled substance, the invoice is automatically assigned to the master vault.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

The invoices are being assigned to the master vault. Please wait..

\<\<\< PROCESS ENTIRE INVOICE SCREEN \>\>\>

No errors have been detected on the following invoices. If there are no

corrections, you can change the invoices' status to "Processed" by selecting

them from the list. If you do have corrections, press the return key then a

second list will be displayed. You will be able to choose the invoices from

that list and enter corrections.

Choose the invoices from the list you want to process.

=============================================================================

1\. Order#: C5914005 Invoice#: 5471741 Invoice Date: Jul 07, 1997

=============================================================================

Select invoices to process: (1-1): 1-----------------------------------------report continues--------------------------------

There are three reasons, or a combination of the three reasons, why invoices will be listed on the PROCESS ENTIRE INVOICE SCREEN. Use the chart to help decide which actions to take.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Reason (s)</th>
<th>Actions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>(1) If all of the invoices are <u>supply</u> invoices, whose items will never be in the DRUG file (#50), the entire invoice can be processed at one time.</td>
<td>Select those invoices for processing.</td>
</tr>
<tr class="even">
<td>(2) If all the invoices contained <u>drugs</u> that were <u>found</u> in the DRUG file (#50) and all required data was also found.</td>
<td>Select those invoices for processing.</td>
</tr>
<tr class="odd">
<td>(3) If all the invoices contained <u>drugs</u> that were <u>not found</u> in the DRUG file (#50), it flags it as a possible supply invoice. This will probably occur more often in the beginning because more items will not be matched to the DRUG file (#50).</td>
<td>Do not choose this invoice for processing. Press <strong>&lt;Enter&gt;</strong>. This will take the user to another screen so the line items can be edited.</td>
</tr>
<tr class="even">
<td>(4) If there is a <u>combination</u> of invoices that contain all supply items or all drugs found together with drugs that have not been found.</td>
<td><p>Select only those invoices that contain all supply items or all found drugs for processing.</p>
<p>After processing the above invoices, another screen will be displayed for editing the line items not found.</p></td>
</tr>
<tr class="odd">
<td>(5) If all of the invoices contained drugs that were not found.</td>
<td>Press <strong>&lt;Enter&gt;</strong>. The user will be taken to another screen to be able to edit the invoices.</td>
</tr>
</tbody>
</table>

Example: Process Uploaded Prime Vendor Invoice Data (continued)

All Supply Items

\<\<\< PROCESS ENTIRE INVOICE SCREEN \>\>\>

Order#: 97038069 Invoice#: 016187568 Invoice Date: Feb 19, 1997 ============================================================================

Are all the items on the invoice supply items? N// YES

Are you sure? Y// \<Enter\>

The invoice’s status will be changed to Processed.

All Drugs Found

\<\<\< PROCESS ENTIRE INVOICE SCREEN \>\>\>

Order#: Y5014006 Invoice#: 5473337 Invoice Date: Feb 07, 1997

============================================================================

Date received: Feb 07, 1997// \<Enter\>

The invoice status has been changed to Processed!

The invoice’s status will be changed to Processed.

All Drugs Not Found in DRUG File (#50)

\<\<\< PROCESS ENTIRE INVOICE SCREEN \>\>\>

Order#: 97038069 Invoice#: 016187568 Invoice Date: Feb 19, 1997

============================================================================

Are all the items on the invoice supply items? N// \<Enter\>

If this type of invoice was selected in error, answer NO to the prompt and the user will be returned to the PROCESS ENTIRE INVOICE SCREEN.

\<\<\< EDIT INVOICES TO BE PROCESSED SCREEN \>\>\>

More data is needed on the following invoices. Choose the invoices from

the list you want to edit.

-----------------------------------------------------------------------------

1\. Order#: C2529410 Invoice#: 071070 Invoice Date: Jan 09, 1997

2\. Order#: C2529410 Invoice#: 54733371 Invoice Date: Jan 07, 1997

-----------------------------------------------------------------------------

Select invoices to edit: (1-2): 1,2

Do you want to select the line items to be edited (S) or

have them automatically (A) displayed for you?: (S/A): A//\<Enter\> automatically displayed

Select the invoices that need to be edited.

If the user chooses to select the line items to be edited (S), the user will have to know which information is missing/incorrect. If the user chooses to have the line items automatically (A) displayed, the software will prompt for only missing/incorrect information. When this method of processing is chosen, the software may read some information as correct such as the quantity received, when in fact a bottle was broken in shipment. The user will need to change this information on the “last chance edit” screen that will appear after the software finishes automatically processing the invoice. It is suggested that the user select automatic display.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

\<\<\< EDIT INVOICES TO BE PROCESSED SCREEN \>\>\>

Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 2006

-----------------------------------------------------------------------------

MASTER VAULT: ALABASTER

PHARMACY LOCATION:

COMBINED (IP/OP): ALABASTER VAMC INPATIENT (IP)

ALABASTER VAMC OUTPATIENT (OP)

Date received: Jul 07, 1997// 7 8

If the drugs were not received on the default date, enter the correct date at this time. Both of the dates will be stored for future reference.

In the example below, the software displays the first line item with <u>missing</u> or <u>incorrect</u> data.

Automatic Processing - Drug Found in DRUG File (#50)

\<\<\< PROCESS LINE ITEM SCREEN \>\>\>

Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 2006

-----------------------------------------------------------------------------

1 DACARBAZINE 100MG INJ

Qty Invoiced: 5

Order Unit : CT NDC: 000836-4565-10

Unit Price : \$4.48 VSN: 562188

PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000

PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1

Dispense Units: TAB

Dispense Units Per Order Unit: Blank

Stock Level : 1200

Reorder Level : 600

DISPENSE UNITS: TAB

DISPENSE UNIT PER ORDER UNIT: 1000

The drug was found in the DRUG file (#50) and only dispense units per order unit (DUOU) was missing.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

National Drug File (NDF) Used for Suggested Match

\<\<\< PROCESS LINE ITEM SCREEN \>\>\>

Order#: H7564729 Invoice#: 1448168 Invoice Date: Mar 31, 2006

-----------------------------------------------------------------------------

1 UNKNOWN ITEM

Qty Invoiced: 1

Order Unit : EA NDC: 000024-0325-02

Unit Price : \$21.26 VSN: 000083

PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000

PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1

Dispense Units: Blank

Dispense Units Per Order Unit: Blank

Stock Level : Blank

Reorder Level : Blank

The NDC has the VA Product Name of DACARBAZINE 100MG/VIL INJ

Is DACARBAZINE 100MG/VIL INJ the drug you received? N// YES

The drug could not be found in the DRUG file (#50) but the NDC and its corresponding VA product name was located in the NDF. The DRUG file (#50) contains (1) one drug with the same VA product name. If the drug with the same VA product name is the actual drug that was received, answer YES and the drugs data will be redisplayed on the screen. If it was not, answer NO and then the user will be able to select the correct drug from the DRUG file (#50).

\<\<\< PROCESS LINE ITEM SCREEN \>\>\>

Order#: 97045660 Invoice#: 016187424 Invoice Date: Feb 19, 2006

1 UNKNOWN ITEM

Qty Invoiced: 1

Order Unit : VI NDC: 000264-7800-00

Unit Price : \$13.48 VSN: 337485

PV-Drug-Description : HYDROCORT AC CRM 1% ALP 30GM@ PV-DUOU : 28.4

PV-Drug-Generic Name : HYDROCORTISONE PV-Units: 1

Dispense Units: Blank

Dispense Units Per Order Unit: Blank

Stock Level : Blank

Reorder Level : Blank

The NDC has the VA Product Name of HYDROCORTISONE 1% CREAM,TOP The

following drugs have the same VA Product Name.

HYDROCORTISONE 1% CREAM

HYDROCORTISONE 1% CREAM JAR

Select the received drug or

enter "^" to select the drug from the DRUG file.: (1-5):1-----------------------------------------report continues---------------------------------------- The drug could not be found in the DRUG file (#50) but the NDC and its corresponding VA product name was located in the NDF. The DRUG file (#50) contains multiple drugs with the same VA product name. If one of the drugs listed is the actual drug that was received, the user can select it. If it was not, enter an \<^\> to select the drug from the DRUG file (#50).

Example: Process Uploaded Prime Vendor Invoice Data (continued)

Vendor’s Stock Number has Changed

\<\<\< PROCESS LINE ITEM SCREEN \>\>\>

Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 2006

-----------------------------------------------------------------------------

1 DACARBAZINE 100MG INJ

Qty Invoiced: 2

Order Unit : BT NDC: 000034-5624-01

Unit Price : \$7.57 VSN: 627635

PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000

PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1

Dispense Units: TAB

Dispense Units Per Order Unit: 300

Stock Level : 2000

Reorder Level : 2000

There is a change in NDC’s Vendor Stock Number (VSN).

New VSN: 627635

Old VSN: 327635

Is the new VSN correct? Y// \<Enter\>

If the new vendor stock number is correct, it will overwrite the old. If the old vendor stock number is correct, the new vendor stock number will be discarded.

Multiple Drugs in DRUG File (#50) with the Same NDC and VSN

\<\<\< PROCESS LINE ITEM SCREEN \>\>\>

Order#: C5014006 Invoice#: 5473337 Invoice Date: Oct 07, 2006

-----------------------------------------------------------------------------

1 UNKNOWN ITEM

Qty Invoiced: 12

Order Unit : BT NDC: 999999-9999-99

Unit Price : \$0.81 VSN: 051219

PV-Drug-Description : HYDROCORT AC CRM 1% ALP 30GM@ PV-DUOU :28.4

PV-Drug-Generic Name : HYDROCORTISONE PV-Units: 1

Dispense Units: GM

Dispense Units Per Order Unit: 28.4

Stock Level : 600

Reorder Level : 600

There is more than one item in the DRUG file with

the same NDC and Vendor Stock Number.

1\. HYDROCORTISONE 1% CREAM

Order Unit: EA Price Per Order Unit : \$0.81

Vendor: DRUGS CORPORATION VSN: 051219

2\. HYDROCORTISONE 1% CREAM JAR

Order Unit: BT Price Per Order Unit :

\$0.81 Vendor: DRUGS CORPORATION VSN: 051219

3\. Select another drug.

Select the invoiced drug: (1-3): <sup>1</sup>-----------------------------------------report continues----------------------------------------

If the received drug is listed, select that drug. If not, choose “Select another drug”, and the user will be able to choose the correct drug from the DRUG file (#50).

Example: Process Uploaded Prime Vendor Invoice Data (continued)

Drug Not Found in NDF and DRUG File (#50)

\<\<\< PROCESS LINE ITEM SCREEN \>\>\>

Order#: C2529411 Invoice#: 071070 Invoice Date: Jan 09, 2006

-----------------------------------------------------------------------------

1 UNKNOWN ITEM

Qty Invoiced: 12

Order Unit : Blank NDC: 000013-8303-04

Unit Price : \$95.00 VSN: 014142

PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000

PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1

Dispense Units: Blank

Dispense Units Per Order Unit: Blank

Stock Level : Blank

Reorder Level: Blank

If the item will never be in the DRUG, press the Return key then

answer YES to the “Is this a supply item?” prompt. To bypass this line

item, enter “^” then press the Return key.

Select Drug: DACARBAZINE 100MG INJ TAB MS200 N/F

Screen Display with Updated Data from a Drug Match

\<\<\< PROCESS LINE ITEM SCREEN \>\>\>

Order#: C5914004 Invoice#: 5471738 Invoice Date: Jul 07, 2006

-----------------------------------------------------------------------------

1 DACARBAZINE 100MG INJ

Qty Invoiced: 12

Order Unit : (Blank) NDC: 000013-8303-04

Unit Price : \$95.00 VSN: 014142

PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000

PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1

Dispense Units: TAB

Dispense Units Per Order Unit: Blank

Stock Level : 1200

Reorder Level : 600

DISPENSE UNITS: TAB

DISPENSE UNIT PER ORDER UNIT: 100

When the drug is selected, the screen clears and the same line item is displayed with the selected drug’s data. The drug-specific data displayed is in the second half of the display -- Dispense Units, Dispense Units Per Order Unit (DUOU), Stock Level, and Reorder Level.

Do you want to change the invoice's status to Processed? NO

The software has detected no missing or incorrect data. If the user thinks any of the data is incorrect, answer NO, and the chance to make corrections in the next screen is given. If the user has no corrections to make, answer YES.

The user will also be able to make corrections in the next screen, but be forewarned, if the edited information is found “valid” by the software the status WILL BE CHANGED to “Processed” and the invoice will be passed to the verifier.

\*\* The invoice's status has not been changed to Processed.

-----------------------------------------report continues----------------------------------------

If the software found missing or incorrect data, the invoice cannot be placed in a processed status. The invoice’s data can be edited by selecting the “last chance edit” or by reentering the option then selecting automatic display.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

Last Chance Edit

If you are changing the status of an invoice to Processed, this is the

last time you will be allowed to edit it before it goes to the

verifier. If you are not changing the status of an invoice to

Processed, you can edit it now.

You can edit the invoice's delivery date, pharmacy location, master vault, and

the line item's drug, quantity received, order unit, and dispense units per

order unit. The reorder level can be edited if the pharmacy location or master

vault is set up to track the reorder levels.

Edit invoices? N// YES

If the answer is NO, the option will exit. If the answer is YES, the user will be able to select the invoice and line items to be edited plus having the ability to edit the assigned pharmacy location and/or master vault.

Yes to last chance edit or if you choose to select the line items to be edited (instead of automatic display)

\<\<\< EDIT INVOICE SCREEN \>\>\>

Choose the invoices to be edited. You can edit the invoice's date received and the line item's drug, quantity received, and order unit. The reorder level can be edited if the pharmacy location or master vault is set up to track the reorder levels.

1.  Order#: C2529410 Invoice#: 071070 Invoice Date: Jan 09, 1997
2.  Order#: C2529410 Invoice#: 54733371 Invoice Date: Jan 07, 1997

Select invoices: (1-2): 1

\<\<\< EDIT INVOICE SCREEN \>\>\>

Order#: C2529410 Invoice#: 071070 Invoice Date: Jul 07, 1997

-----------------------------------------------------------------------------

Date received: Jul 08, 1997// \<Enter\>

MASTER VAULT: PELHAM CLINIC

Select Master Vault: PELHAM CLINIC// \<Enter\>

COMBINED (IP/OP): Louisville Inpatient Medications (IP)

Louisville Outpatient Pharmacy (OP) Select Pharmacy Location:

COMBINED (IP/OP)// \<Enter\>

Line Item Numbers: 562188,627635

Select Line Item Number: 562188-----------------------------------------report continues----------------------------------------

The user can change the date the drugs were actually received. The pharmacy location and/or master vault that will receive the drugs on the invoice can also be changed. At “Line Item Numbers”, <u>all</u> of the line numbers will be listed to reference when the user is entering the line number at the line number prompt. The user is not allowed to enter a range of numbers. Enter one line number; make the edits, and then another “Select Line Item Number” prompt is displayed. When the user is finished making the corrections, press \<Enter\> at the “Select Line Item Number” prompt.

> **NOTE:** If the prime vendor is AmeriSource Health Services, the line numbers are the vendor stock numbers for the line item’s drug.

Example: Process Uploaded Prime Vendor Invoice Data (continued)

\<\<\< EDIT INVOICE SCREEN \>\>\>

Order#: C2529411 Invoice#: 071070 Invoice Date: Jul 07, 2006

-----------------------------------------------------------------------------

1 DACARBAZINE 100MG INJ

Qty Invoiced: 5

Order Unit : CT NDC: 000536-4565-10

Unit Price : \$4.48 VSN: 262188

PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000

PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1

-----------------------------------------------------------------------------

1.  Drug
2.  Quantity Received
3.  Order Unit
4.  Dispense Units Per Order Unit

Edit fields: (1-4): 2

QUANTITY RECEIVED: 5// 4

ADJUSTMENT REASON: 1 CARTON WAS NOT DELIVERED

Do you want to change the invoice's status to Processed? YES

Enter YES if the invoice is completely correct. The user will not be able to edit it again when the option is exited. Enter NO if the user needs to edit the invoice again. This is accomplished by selecting the *Process Uploaded Prime Vendor Invoice Data* option.

Invoices that have been moved to the status of Processed are reviewed for notable changes of Order Units, Dispense Units Per Order Unit (DUOU), Price Per Dispense Unit (PPDU), and NDCs. If there are changes the user is presented an informational note on their screen and then a PRE Verification 'Order' : 'Invoice' Variance Report Mailman message is sent to the G.PSA NDC UPDATES mail group.

Example: Informational Note

PRE Verify C502395300 : 7229924053 Variance Report

Noted differences between the invoice line items and the drug file have been found. A mail message is being sent to G.PSA NDC UPDATES.

Please check the message for accuracy.

\<cr\> - continue:

Example: Mailman Message

Subj: PRE Verify C502395300 : 7229924053 Variance Report \[#1986002\]

04/01/05@18:29 11 lines

From: PSAperson,One In 'IN' basket. Page 1

-------------------------------------------------------------------------------

PRE Verify C502395300 : 7229924053 Variance Report

Example: Process Uploaded Prime Vendor Invoice Data (continued)

1.  ACETAMINOPHEN WITH CODEINE 30MG

DUOU Old: 485 New: 1000

OU Old: CO New: BT

PPDU Old: 1.2371 New: 0.6000

2.  METHADONE 10MG TAB

DUOU Old: 40 New: 100

PPDU Old: 0.1938 New: 0.0771

### Verify Invoices 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA VERIFY INVOICES\]

The *Verify Invoices* option validates processed invoices. The verifier and processor cannot be the same person. If the invoice contains at least one drug marked as a controlled substance, only pharmacists holding the PSA ORDERS key can verify the invoice.

This option is locked by the PSA ORDERS key.

> **IMPORTANT:** Once verified, the drug balances are incremented in the pharmacy location and/or master vault.

The following condition must be met to update the NDC field (#31).

- If the invoice NDC is different from the NDC field (#31), the NDC field (#31) is overwritten with the invoiced NDC.

The following condition must be met to update the PRICE PER ORDER UNIT field (#13) and PRICE PER DISPENSE UNIT field (#16).

- If the invoiced price per order unit (PPOU) is different than the PRICE PER ORDER UNIT field (#13), the PRICE PER ORDER UNIT field (#13) is overwritten with the new prorated price per order unit (PPOU). The PRICE PER DISPENSE UNIT field (#16) is also overwritten with the new prorated price per dispense unit (PPDU).

Example: Verify Invoices

No Invoice(s) to be Verified Messages

There is at least one invoice that needs to be verified. However, invoices cannot be verified

by the same person who processed them and a pharmacist must verify invoices that contain a

drug marked as a controlled substance.

There are no invoices you can verify because the invoice(s) meet one of the

above conditions.

There are no invoices that need to be verified.

Invoice(s) to be Verified Messages

Enter your Current Signature Code: SIGNATURE VERIFIED

Print processed invoices? N// \<Enter\>

If the user chooses to print the processed invoices, ALL processed invoices will be printed. This includes the invoices that CANNOT be verified. If the user wants to print specific invoices, select the *Print Orders* option from the *Orders Menu*.

Example: Verify Invoices (continued)

\<\<\< VERIFY ENTIRE INVOICE SCREEN \>\>\>

If there are no corrections, you can change the invoices' status

to "Verified" by selecting them from the list. If you do have

corrections, press the return key then a second list will be

displayed. You will be able to choose the invoices from that list

and enter corrections.

Choose the invoices from the list you want to verify.

=============================================================================

1\. Order#: C7564729 Invoice#: 1448168 Invoice Date: Jul 31, 1997

2\. Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997

3\. Order#: C7611902 Invoice#: 2165990 Invoice Date: Jul 03, 1997

=============================================================================

Select invoices to verify: (1-3): 1,3

When the user chooses the invoices from this list to verify, the status will be changed to Verified. Invoices not selected from the list will automatically be displayed on the EDIT INVOICES TO BE VERIFIED SCREEN so that changes can be made.

Verifying Invoices That Do Not Need to Be Edited

\<\<\< VERIFY ENTIRE INVOICE SCREEN \>\>\>

=============================================================================

1.  Order#: C7564729 Invoice#: 1448168 Invoice Date: Jul 31, 1997

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

MASTER VAULT: MASTER VAULT 1

2.  Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

MASTER VAULT: MASTER VAULT 1

Are you sure these invoices' status should be changed to Verified? N// YES

Answer YES if the listed invoices and corresponding pharmacy location and/or master vault are correct.

Answer NO if an incorrect invoice is chosen or if the listed information is incorrect. The user will be returned to the previous VERIFY ENTIRE INVOICE SCREEN to reselect invoices.

........

Order# C7564729 Invoice# 1448168's status has been changed to Verified!

.........................................

Order#: C7611902 Invoice#: 2165983’s status has been changed to Verified!

When changing the status has been answered YES, the above messages will be displayed as the invoice’s status is being changed. Upon exiting this option, a background job is run immediately which will add the receipts to the drug balances in the pharmacy location and/or master vault. The status will then be changed to Completed.

Invoices that have been moved to the status of completed are reviewed for notable changes of Order Units, Dispense Units Per Order Unit (DUOU), Price Per Dispense Unit (PPDU), and NDCs. If there are changes a POST Verification 'Order' : 'Invoice' Variance Mailman message is sent to the G.PSA NDC UPDATES mail group.

Example: Mailman Message

Subj: POST Verify C502395300 : 7229924053 Variance Report \[#1986002\]

04/01/05@18:29 11 lines

From: PSAperson,One In 'IN' basket. Page 1

-------------------------------------------------------------------------------

PRE Verify C502395300 : 7229924053 Variance Report

ACETAMINOPHEN WITH CODEINE 30MG

DUOU Old: 485 New: 1000

OU Old: CO New: BT

PPDU Old: 1.2371 New: 0.6000

METHADONE 10MG TAB

DUOU Old: 40 New: 100

PPDU Old: 0.1938 New: 0.0771

Selecting Invoices to be Edited

\<\<\< EDIT INVOICES TO BE VERIFIED SCREEN \>\>\>

Choose the invoices from the list you want to edit.

-----------------------------------------------------------------------------

1.Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997

-----------------------------------------------------------------------------

Select invoices to edit: (1-1): 1

If an invoice was not chosen to be verified previously or if the software found an error in the invoice, this screen will be displayed.

Editing the Invoice Data and Selecting Line Items to be Edited

\<\<\< EDIT INVOICES TO BE VERIFIED SCREEN \>\>\>

Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997

-----------------------------------------------------------------------------

Date received: Jul 03, 1997// 7 4

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

PHARMACY LOCATION: COMBINED (IP/OP)// \<Enter\>

Select Line#: ?

Answer with LINE ITEM DATA LINE ITEM NUMBER

Choose from:

659631

938662

Select Line#: 659631

The user is able to change the date the drugs were received and the pharmacy location and/or master vault that will receive the drugs on this invoice. Any line items that might need to be edited can also be chosen.

Example: Verify Invoices (continued)

Selecting Line Item Fields to be Edited

\<\<\< EDIT INVOICES TO BE VERIFIED SCREEN \>\>\>

Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997

-----------------------------------------------------------------------------

DACARBAZINE 100MG INJ

Qty Invoiced: 2

Order Unit : EA NDC: 000781-1766-10

Unit Price : \$11.10 VSN: 659631

PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000

PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1

Dispense Units: TAB

Dispense Units Per Order Unit: 1000

Stock Level : 2000

Reorder Level : 500

-----------------------------------------------------------------------------

1.  Drug
2.  Quantity Received
3.  Order Unit
4.  Dispense Units per Order Unit
5.  Stock Level
6.  Reorder Level

Edit fields: (1-6): 3,4,6

The user is able to select more than one field to be edited; however only the Stock Level and Reorder Level fields will be shown and allowed for editing if the assigned pharmacy location or master vault maintains reorder levels.

Editing Line Item Fields

\<\<\< EDIT INVOICES TO BE VERIFIED SCREEN \>\>\>

Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 03, 1997

-----------------------------------------------------------------------------

1 DACARBAZINE 100MG INJ

Qty Invoiced: 2

Order Unit : EA NDC: 000781-1766-10

Unit Price : \$11.10 VSN: 659631

PV-Drug-Description : DACARBAZINE 100MG INJ PV-DUOU : 1000

PV-Drug-Generic Name : DACARBAZINE 100MG/VIL INJ PV-UNITS : 1

Dispense Units: TAB

Dispense Units Per Order Unit: 1000

Stock Level : 2000

Reorder Level : 500

-----------------------------------------------------------------------------

ORDER UNIT: EA// BT BOTTLE

DISPENSE UNIT PER ORDER UNIT: 1000//@

The dispense units per order unit must be entered to change

the status of the invoice to Verified.

Do you want to enter the data now? Y//NO

REORDER LEVEL (in Dispense Units): (0-99999): 500// 600

Select Line#: \<Enter\>

Example: Verify Invoices (continued)

Missing or Incorrect Data Found on Invoice

\*\* The invoice has not been placed in a Verified status!

Enter RETURN to continue or '^' to exit:

Do you want to print the verification error report? N// YES

DEVICE: HOME//*\[Select Print Device\]*

Verification Error Report

\<\<\< VERIFICATION ERROR REPORT \>\>\>

Order#: C7611902 Invoice#: 2165983 Invoice Date: Jul 3, 1997

-----------------------------------------------------------------------------

Line# 659631: Dispense unit per order unit

\*\* The invoice has not been placed in a Verified status!

The user will receive this report listing the line item number and field(s) where an error or missing data was found.

No Errors Found on Invoice

Do you want to change the invoice's status to Verified?

If the answer is NO, the invoice will remain in a processed status and the user will be able to reselect it for verification, by choosing the *Verify Invoices* option. If the answer is YES, the user will receive a message stating that the invoice’s status has been changed to Verified.

Printing the NEW DRUG REPORT

The verified invoices contain new drugs for the assigned pharmacy location

and/or master vault. A report will print by pharmacy location/master vault

listing the new drugs. Use the Balance Adjustment option to enter an adjustment

that reflects the total dispense units on hand for each new drug.

It is suggested that you send the report to a printer.

DEVICE: HOME// \[Select Print Device\]

\<\<\< NEW DRUG REPORT \>\>\>

PHARMACY LOCATION

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

=============================================================================

IMIPRAMINE HCL 50MG TAB

-----------------------------------------------------------------------------

PENTOBARBITAL SODIUM 100MG CAP

A MailMan message is also sent to the members of the G.PSA NDC UPDATES mail group identifying the pharmacy locations and the drugs that may need more data, such as current balance, stock level, and reorder levels entered to complete their setup.

Example: Mailman Message

Subj: New Drugs Added by Order: CX45678989 Invoice: 45789000C \[#1997035\]

08/24/05@13:45 54 lines

From: VERIFIED BY: DAPHARMACIST52,THREE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

New Drugs Added by Order: CX45678989 Invoice: 45789000C

Verified by: DAPHARMACIST52,THREE

Please use DA and CS menus to populate the balances, stock and re-order levels.

MASTER VAULT

CAFFEINE & SOD BENZOATE 500MG/2ML

CODEINE 15MG & APC C.T.

FENTANYL 0.05MG/ML 5ML S.S.

METHADONE 5MG TAB

MORPHINE 15MG/ML 20ML INJ

OUTPATIENT

ACETAMINOPHEN 500MG CAPSULE

ACETAZOLAMIDE 125MG TAB

ACETAZOLAMIDE 500MG INJ

ATENOLOL 100MG TAB

ATENOLOL 50MG TAB

CAFFEINE & SOD BENZOATE 500MG/2ML

CATAPRES .3MG TAB

FUROSEMIDE 10MG/ML 10ML INJ

MINOCYCLINE 100MG CAP

Upon exiting this option, a background job is run immediately which will add the receipts to the drug balances in the pharmacy location and/or master vault. The status will then be changed to Completed.

### Print Orders 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA PRINT ORDERS\]

The *Print Orders* option generates invoices by entering the order number, invoice number, or invoice status.

> This option is locked with the PSA ORDERS key.

- If the invoice has not been processed, the PRIME VENDOR UPLOAD REPORT prints.
- If the invoice has been processed, the PRIME VENDOR ORDER REPORT prints.

Example: Print Orders

Print by Order Number

Select one of the following:

O Order Number

I Invoice Number

S Invoice Status

Print by Order#, Invoice#, or Invoice Status: O// \<Enter\>

Select ORDER NUMBER: C7611902

Select ORDER NUMBER: C7611903

Select ORDER NUMBER: C7611904

DEVICE: HOME// \[Select Print Device\]

When the user chooses to print by order number, the opportunity will be given to keep inputting as many order numbers as needed. All invoices for that order will print.

Print by Invoice Number

Select one of the following:

O Order Number

I Invoice Number

S Invoice Status

Print by Order#, Invoice#, or Invoice Status: O// Invoice Number

-----------------------------------------------------------------------------

Select ORDER NUMBER: C7611902

Invoice# 2165983

-----------------------------------------------------------------------------

Select ORDER NUMBER: C5014004

Select INVOICE NUMBER: 5471738

Select INVOICE NUMBER: 5471740

Select INVOICE NUMBER: \<Enter\>

-----------------------------------------------------------------------------

Select ORDER NUMBER: \<Enter\>

DEVICE: HOME// *\[Select Print Device\]*

When the selection to print by invoice number is invoked, the order number is the first prompt. This is because the vendors may use the same invoice number more than once for different orders. Therefore there can be the same invoice number with different data for different orders. If there is more than one invoice for the order the user will be able to enter them. If there is only one invoice for the order, the invoice number will automatically be displayed.

Print by Invoice Status

Select one of the following:

O Order Number

I Invoice Number

S Invoice Status

Print by Order#, Invoice#, or Invoice Status: O// S Invoice Status

Select Unprocessed or Processed Invoice Status: (U/P): Unprocessed

If Unprocessed is chosen, all of the uploaded invoices that have not been processed will print. If Processed is chosen, all processed invoices that have not be verified will print.

### Credit Resolution 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA CREDIT RESOLUTION\]

The *Credit Resolution* option allows the user to enter credit memo data.

It is locked with the PSA ORDERS and PSAMGR keys<sub>.</sub>

When an adjustment is made to the invoice that decreases the total cost, the invoice is flagged as awaiting a credit. The invoice will continue to be flagged until the total credits equal the adjustment(s). If the user receives a credit memo and are unsure which invoice to apply the credit to, use the Outstanding Credits option under the Maintenance Reports Menu to print a report of all outstanding credits.

### Edit Verified Invoices 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA EDIT VERIFIED INVOICE\]

It is locked with the PSAMGR key.

The *Edit Verified Invoices* option allows the user to change elements of a verified invoice.

Example: Edit Verified Invoices

Select Orders Menu Option: Edit Verified Invoices

VERIFIED INVOICE ALTERATION SCREEN

The user selects an order number with a status of verified.

Select Order Number: C18442037N

\[Then selects an invoice from the order\]

Select Invoice Number: 2054031 03-16-01

-----------------------------------------report continues----------------------------------------

A screen with the available line items is displayed.

Example: Edit Verified Invoices (continued)

EDIT VERIFIED INVOICED ITEM SCREEN

====================================================================

Order

\# Drug/Item Name Unit Qnty. NDC ====================================================================

1 ACETAMINOPHEN 1000MG TABLET BT 15 063481013275

Enter the corresponding item number to edit: 1 \*ACETAMINOPHEN 1000MG TABLET

Qty Invoiced: 15 Order Unit : BT (BT) NDC: 063481-0132-75

Unit Price : \$1.71 VSN: 4003463

Dispense Units: MG

Dispense Units Per Order Unit: 1000

=========================================================================

Select (D)rug or (O)rder Unit

The user can opt to alter the drug name or the associated order unit.

Select (D)rug or (O)rder Unit drug

Current Drug : ACETAMINOPHEN 1000MG TABLET

Select name of Correct Drug: ACETAMINOPHEN 325MG TABLET CN103

After selection of the drug, the program will compare the data in the invoice, with the data in the Drug file. The user will then be asked to enter the Dispense Units, and Dispense Units per Order Unit (DUOU).

Comparing drug file data...

Please Enter an appropriate Dispense Unit

DISPENSE UNIT: TAB// \<Enter\>

Please enter the appropriate Dispense Units per order unit

DISPENSE UNITS PER ORDER UNIT: 1000// 100

Are you sure about this ? NO// ?

Answer yes, and the data on file for the current drug will be transferred to the new drug selection. That includes Order Unit, Dispense Unit, Dispense Units per Order Unit, etc.

Are you sure about this ? NO// Y

Removing 15 from ACETAMINOPHEN 1000MG TABLET

Adding 15 to ACETAMINOPHEN 325MG TABLET Entering new drug selection as an adjustment. updating pharmacy location file. updating transaction file.

### Delete Un-processed Invoices 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DELETE INVOICES\]

It is locked with the PSAMGR key<sub>.</sub>

The *Delete Un-processed Invoices* option deletes any un-processed invoices older than the date the user specifies. Only personnel who hold the PSAMGR key will have access to this process.

Example: Delete Un-processed Invoices

Select Orders Menu Option: Delete Un-processed Invoices

Delete invoices older than what date: T-6M Finished

### Setup Mail Message Recipients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA MSG RECIPIENTS\]

It is locked with the PSAMGR key.

The *Setup Mail Message Recipients* option is used to enter/delete personnel from the two mail groups used for notifying personnel of a change in NDC and/or Drug Price, and when drugs are below reorder levels.

Example: Setup Mail Message Recipients

Select Orders Menu Option: <u>S</u>etup Mail Message Recipients

SETUP RECIPIENTS OF MAILMESSAGE SCREEN

====================================================================

Currently, any user who holds the 'PSA ORDERS' key, receives the mail message

'Drug Balances Below Reorder Level' & 'NDC/PRICE change messages'.

Two mail groups have been established to determine who receives the message.

Members added to the mail group must first possess the 'PSA ORDERS' key.

Do you want to edit the users for the PSA REORDER LEVEL mail group? YES//\<Enter\>

Select NEW PERSON NAME: DAPHARMACIST52,THREE

Select 'A' to Add the user or 'D' to delete the user. ADD//\<Enter\>

task completed.

There are two messages the user could receive from either action, the messages are: “task completed” and “Sorry, couldn’t perform task.” These messages are self-explanatory. If the program says it couldn’t perform the task of adding the user, which means that the user is already a member of the mail group. The same holds true for deleting users.

Example: Setup Mail Message Recipients (continued)

Trying to add the same user again:

Select NEW PERSON NAME: DAPHARMACIST52,THREE

Select 'A' to Add the user or 'D' to delete the user. ADD//\<Enter\>

Sorry,couldn't perform action

Select NEW PERSON NAME: \<Enter\>

Press \<Enter\> to access the next mail group.

Do you want to edit the users for the PSA NDC UPDATES mail group? YES//\<Enter\>

Select NEW PERSON NAME: DAPHARMACIST52,THREE

Select 'A' to Add the user or 'D' to delete the user. ADD//\<Enter\>

task completed

The message displayed when trying to add a user who is already on file:

Select NEW PERSON NAME: DAPHARMACIST52,THREE

Select 'A' to Add the user or 'D' to delete the user. ADD//\<Enter\>

Sorry, couldn't perform action.

To delete a user from the mail group:

Select NEW PERSON NAME: DAPHARMACIST52,THREE

Select 'A' to Add the user or 'D' to delete the user. ADD//D task completed.

Select NEW PERSON NAME: \<Enter\>

Press ENTURN/ENTER to continue: \<Enter\>

Select Orders Menu Option:

### Balance Adjustments History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA BALANCE ADJUSTMENTS REPORT\]

The *Balance Adjustments History* option reviews adjustments and transfers of a drug. The report lists the drug, transaction date and time, adjustment quantity, transfer quantity, transaction, adjustment reason, and pharmacy location that sent or received the transferred drug.

### Drug Balances by Location 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DISPLAY LOCATION\]

The *Drug Balances by Location* option generates a report by pharmacy location listing each of its drugs’ name, quantity on hand, dispense unit, and total inventory.

### Drug Transaction History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA DRUG DISPLAY\]

The *Drug Transaction History* option provides a transaction history for one, many, or all drug(s) within the pharmacy location for a given date range. It lists the date range, drug, beginning and ending dates, beginning balance, transaction date, transaction quantity, transaction type, person who made the transaction, and resulting balance.

If the transaction is <u>receiving</u> drugs, the purchase order number, transaction number, and invoice number are also listed.

If the transaction is <u>dispensing</u>, the report designates where the dispensing took place. It’s either Inpatient or Outpatient dispensing.

### Invoice Cost Summary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA INVOICE COST SUMMARY\]

The *Invoice Cost Summary* option generates a report of all invoices’ cost data for a date range. It lists the order number, invoice number, invoice date, total invoice cost, total adjusted cost, and cost difference.

### Monthly Summary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA MONTHLY SUMMARY\]

The *Monthly Summary* option allows the user to print a pharmacy location’s detailed or summary monthly report of transactions made on one, many, or all drugs.

If the user selects the detailed report, the drug, beginning balance, total receipts, total dispensed, total adjustments, total transfers, and ending balance or one, many, or all drugs in the selected pharmacy location is printed.

If the user selects the summary report, the detailed report prints then a separate summary report follows. The summary report contains the drug, total receipts, total dispensed, total adjustments, and total transfers for one, many, or all drugs in the selected pharmacy location. A total line for the total receipts, total dispensed, total adjustments, and total transfers is printed.

### Outstanding Credits 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA OUTSTANDING CREDITS\]

The *Outstanding Credits* option displays or prints invoice data for all invoices that have outstanding credits. A detailed or summary report may be selected.

<u>Detailed Report</u>

If the detailed report is selected, the summary data prints along with the line item information that caused the need for a credit. The line item data that prints are the line item’s number, drug, adjusted field’s name, adjustment comments, invoiced data, and adjusted data.

Example: Detailed Report

DRUG ACCOUNTABILITY/INVENTORY INTERFACE

OUTSTANDING CREDITS REPORT

PAGE 1 INVOICE ADJUSTED RECEIVED OUTST. DRUG &

INVOICE# DATE COST COST CREDITS CREDIT LINE# ADJUST REASON INV ADJ ------------------------------------------------------------------------------------------------

ORDER#: C5014003 (\$6376.18)

I845966 10/01/97 4440.04 4441.87 0.00 -1.83 2 AMPICILLIN 500MG CAP 0 1

QTY: DID NOT ORDER THIS

I845967 10/02/97 1938.38 1934.31 0.00 4.07 10 METOPROLOL 50MG TAB 12 11

QTY: 1 BOTTLE BROKEN

ORDER TOTAL 2.24

------------------------------------------------------------------------------------------------ ORDER#: C5014004 (\$17.92)

5471738 10/07/97 22.40 17.92 0.00 4.48 8 AMPICILLIN 250MG CAP 5 4

QTY: 1 BOTTLE MISSING

ORDER TOTAL 4.48

------------------------------------------------------------------------------------------------ GRAND TOTAL 6.72

<u>Summary Report</u>

If the summary report is selected, the order number, total adjusted cost of the order, invoice number, invoice date, invoiced cost, adjusted cost, credit amount received, invoice’s outstanding credit amount, total order’s outstanding credit amount, and grand total outstanding credit amount will be displayed.

Example: Summary Report

DRUG ACCOUNTABILITY/INVENTORY INTERFACE

OUTSTANDING CREDITS REPORT

PAGE 1

RUN DATE: 10/17/97@0822

INVOICE ADJUSTED RECEIVED OUTST.

INVOICE# DATE COST COST CREDITS CREDIT

-------------------------------------------------------------------------------

ORDER#: C5014003 (\$6376.18)

I845966 10/01/97 4440.04 4441.87 0.00 -1.83

I845967 10/02/97 1938.38 1934.31 0.00 4.07

ORDER TOTAL 2.24

ORDER#: C5014004 (\$17.92)

5471738 10/07/97 22.40 17.92 0.00 4.48

ORDER TOTAL 4.48

-------------------------------------------------------------------------------

GRAND TOTAL 6.72

### Processor and Verifier 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA PROCESSOR AND VERIFIER\]

The *Processor and Verifier* option generates a report containing invoices’ processor and verifier information for a date range. It lists the order number, invoice number, invoice date, processor’s name, process date, verifier’s name, and verification date.

### Stock and Reorder Level 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA STOCK & REORDER LEVEL RPT\]

The *Stock and Reorder Level* option prints a report by pharmacy location and/or master vault. The report contains the drug name, stock level, and reorder level. Only a pharmacist can enter the stock and reorder levels for a master vault. Since all drugs received are automatically added to a pharmacy location, it is advised that this report be queued to run during non-peak hours.

### Transfer Signature Sheet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA TRANSFER SIGNATURE SHEET\]

The *Transfer Signature Sheet* option prints a report of all transferred drugs within a specific date range. This report is used to record the signature of the person who received the drugs or to review transfer history.

Example: Transfer Signature Sheet

Choose the pharmacy location transferring the drugs:

1.  COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)
2.  INPATIENT: PELHAM (IP)
3.  OUTPATIENT: HELENA (OP)

Select Transfer from Pharmacy: (1-3): 1

Select the pharmacy location that will send the drugs to the other pharmacy location.

Choose the pharmacy location receiving the transferred drugs:

1.  INPATIENT: PELHAM (IP)
2.  OUTPATIENT: HELENA (OP)

Select Transfer to Pharmacy: (1-2): 2

Select the pharmacy location that will receive the drugs from the transferring pharmacy locations.

Beginning Date: 8 12 (AUG 12, 1997)

Ending Date : 8 12 (AUG 12, 1997)

DEVICE: HOME// *\[Select Print Device\]*

Enter the date range to print the transfer signature sheets.

AUG 12,1997@12:40 D R U G A C C O U N T A B I L I T Y Page: 1

DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

TRANSFERRED TO: OUTPATIENT: HELENA (OP)

-----------------------------------------------------------------------------

TRANSFER DATE QTY DRUG NEW BALANCE

-----------------------------------------------------------------------------

Aug 12, 1997@12:40 10 ACETAMINOPHEN 325MG TAB 50

Dispensed by: DAPHARMACIST51,THREE Rec'd by: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

(Full Name) (Full Name)

### Adding a Return Contractor 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user must first have a return contractor defined before they can add a batch with items for return. From the “Return Drug Batch List” screen, type CON at the “Select Action” prompt and add the return contractor information. This is usually performed the first time the *Batch Work List* option is used or when the return contractor changes.

### Adding a Batch 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When adding a batch, a batch ID called a batch \# is automatically assigned and the user assigns the return contractor who is picking up the drugs as shown in the following example. The batch \# format is MMYY-NNN where MM is the current month, YY is the current year, and NNN is the incrementing number of the same month/year batch. Each new batch is automatically assigned the status of Awaiting Pickup.

Example: Adding a Batch

Return Drug Batch List Sep 19, 2008@10:08:21 Page: 1 of 2

Pharmacy Location: OUTPATIENTNo Inpatient or Outpatient Sites defined

Date Range : ALL

DATE DATE DATE TOTAL \# OF

\# BATCH \# CREATED PICKED UP COMPLETED CREDIT RETURN CONTRACTOR ITEMS

AWAITING PICKUP

1.  0908-001 09/04/08 0.00 MORRISON CONTRACTING 14
2.  0908-002 09/05/08 0.00 MORRISON CONTRACTING 1
3.  0908-003 09/06/08 0.00 ANWER CONTRACTING CO 2
4.  0908-005 09/07/08 0.00 JEN MANUFACTURING 1
5.  0908-006 09/08/08 0.00 MORRISON CONTRACTING 6
6.  0908-007 09/09/08 0.00 MORRISON CONTRACTING 5
7.  0908-008 09/10/08 0.00 MORRISON CONTRACTING 10
8.  0908-009 09/11/08 0.00 MORRISON CONTRACTING 8
9.  0908-010 09/12/08 0.00 MORRISON CONTRACTING 7
10. 0908-011 09/13/08 0.00 MORRISON CONTRACTING 3
11. 0908-012 09/14/08 0.00 MORRISON CONTRACTING 12
12. 0908-013 09/15/08 0.00 MORRISON CONTRACTING 5
13. 0908-017 09/16/08 0.00 MORRISON CONTRACTING 4
14. 0908-018 09/17/08 0.00 MORRISON CONTRACTING 2
15. 0908-019 09/18/08 0.00 MORRISON CONTRACTING 0

\+ Select the entry \# to view or ?? for more actions

ADD New Batch SEL Select Batch CON Rtn Contractor Add/Edit Select

Action: Next Screen// ADD\<Enter\> New Batch

New Batch \#: 0908-020

RETURN CONTRACTOR: MORRISON CONTRACTING SERVICES

Save Batch? NO// YES \<Enter\> Please wait...

2.  
3.  1.  
    2.  
    3.

### Editing a Batch 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can edit the batch information from the “Return Drug Batch” screen. At each prompt, the user has the opportunity to enter batch related information, such as the return contractor and the reference \#. The reference \# is the return contractor batch ID number the user receives from the return contractor when the batch is picked up. Adding Items (Drugs) to a Batch

After a batch has been added, the user is taken to the next screen, “Return Drug Batch”, where items that are being returned can be added to the batch. The user can enter the following information about the item being returned.

Drug\*

Manufacturer

National Drug Code (NDC)

Order Unit\*

Number of Dispense Units\*

Dispense Unit

Number of Dispense Unit Order Unit\*

Number of Order Units\*

Universal Product Code (UPC)

Expiration Date

Return Reason\*

Update Inventory\*

\* Required fields

Example: Adding Items to a Batch

Return Drug Batch Sep 19, 2008@10:08:29 Page: 0 of 0

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: AWAITING PICKUP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up:

Reference \# : Total Batch Credit: \$0.00

ORD ORDER DISP DISP ACTUAL \#

RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

This batch contains no return items.

Select the entry \# to view or ?? for more actions

ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit// ADD\<Enter\> New Item

DRUG: MEPERIDINE

1.  MEPERIDINE 100MG SYRINGE CN101
2.  MEPERIDINE 25MG SYRINGE CN101
3.  MEPERIDINE 50MG SYRINGE CN101
4.  MEPERIDINE 50MG TAB CN101
5.  MEPERIDINE 50MG/5ML ELIXIR (OZ) CN101 Press \<RETURN\>

to see more, '^' to exit this list, OR

CHOOSE 1-5: 4\<Enter\> MEPERIDINE 50MG TAB CN101 MFR:

TEST MFR \<Enter\>NDC: 00555-0381-04// \<Enter\> 00555- 0381-04ORDER UNIT: BOTTLEDISPENSE UNIT: TABLETNUMBER OF TABLET(S) PER BOTTLE: 500

NUMBER OF BOTTLE(S) TO RETURN: 5 \<Enter\>

NUMBER OF TABLET(S) TO RETURN: 2500// \<Enter\>

UPC: \<Enter\>

EXPIRATION DATE: 07/01/08 \<Enter\> (JUL 01,

2008\)

RETURN REASON: ? \<Enter\>

Select the reason why the drug is being returned to the contractor/ manufacturer. Choose from:

E EXPIRED

R RECALLED

D DAMAGED

O OVERSTOCKED

M MISCELLANEOUS

X DESTRUCTION

RETURN REASON: EXPIRED \<Enter\>

UPDATE INVENTORY: NO// \<Enter\>

Save Item? YES// \<Enter\>

Saving...OK

Add another Item? YES// NO \<Enter

At this point, the drug has been successfully added to the batch and the user is prompted whether or not he or she wants to add another drug. From the “Return Drug Batch” screen, the user can add more items, edit the selected item, edit the batch information, cancel the batch, update credit of items, pick up the batch, or complete the batch.

Return Drug Batch Sep 19, 2008@10:11:30 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: AWAITING PICKUP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up:

Reference \# : Total Batch Credit: \$0.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 0.00

Select the entry \# to view or ?? for more actions

ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit//

### Editing an Item 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can edit the item information. From the “Return Drug Batch” screen, select the item to edit. From the “Return Drug Item” screen, type EDT for Edit Item and press \<Enter\>. Each item’s field is presented with the current value as the default. To keep the default and continue to the next field, press \<Enter\>. Otherwise, type the new value and press \<Enter\> to update it and continue to the next field. When all fields have been addressed, at the “Save Item?” prompt, type Y for YES and press \<Enter\>. The changes to the fields are saved, and the activity log is updated and displays the changes below the drug information on the “Return Drug Item” screen.

### Picking up a Batch 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After all items have been entered into a batch and when the return contractor is ready to physically pick up the drugs, the batch may be marked as picked up. At this point, credits can be entered for each item in the batch. Credits can be updated while marking the batch as picked up or later if needed, however a batch can be marked as picked up only once. NOTE: After a batch has been marked as picked up, it can no longer be cancelled. The following example shows a batch being marked as picked up and credits being updated during pickup.

Example: Picking up a Batch and Updating Credits

Return Drug Batch Sep 19, 2008@10:11:30 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: AWAITING PICKUP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up:

Reference \# : Total Batch Credit: \$0.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1.  BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00
2.  MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 0.00
3.  MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 0.00

Select the entry \# to view or ?? for more actions

ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit// PKP\<Enter\> Pick up Batch

RETURN CONTRACTOR: MORRISON CONTRACTING

SERVICES// RETURN CONTRACTOR REF#: 2242 \<Enter\>

Do you want to update credit for items? YES// \<Enter\>

Select one of the following:

E ESTIMATED

A ACTUAL

B BOTH

CREDIT TYPE: A// BOTH \<Enter\>

ITEM(S): (1-3): 3 \<Enter\>

Item 3: MEPERIDINE 50MG TAB (00555-0381-04) - Quantity: 5 (BOTTLE)

ESTIMATED CREDIT AMOUNT: 100\<Enter\>

ACTUAL CREDIT AMOUNT: 75 \<Enter\>

Return Drug Batch Sep 19, 2008@10:14:18 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: PICKED UP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13

Reference \# : 2242 Total Batch Credit: \$75.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1 BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00

2 MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 0.00

3 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00

Enter ?? for more actions

ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit//

1.

### Updating Credits 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Credit Update action is available after the batch has been picked up and before the batch has been completed. When updating credits and prompted to enter the credit amount, estimated or actual, keep in mind that it is the total credit for the total number of order units of that item being returned that should be entered, not the credit amount for one order unit of that item. On the “Return Drug Batch” screen, the “Total Batch Credit” reflects the total actual credit amount that has been entered for each item in the batch. If only an estimated amount has been entered, the “Total Batch Credit” will still be \$0.00. The following is an example of entering both estimated and actual credit.

Example: Updating a Credit

Return Drug Batch Sep 19, 2008@10:14:18 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: PICKED UP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13

Reference \# : 2242 Total Batch Credit: \$75.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1.  BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00
2.  MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 0.00
3.  MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00

Enter ?? for more actions

ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit// CRE\<Enter\> Credit Update

Select one of the following:

E ESTIMATED

A ACTUAL

B BOTH

CREDIT TYPE: A// BOTH \<Enter\>

ITEM(S): (1-3): 2 \<Enter\>

Item 2: MEDROXYPROGESTERONE 100MG (00009-0248-02) - Quantity: 15 (BOX)

ESTIMATED CREDIT AMOUNT: 45 \<Enter\>

ACTUAL CREDIT AMOUNT: 60 \<Enter\>

Notice the “Total Batch Credit” has been updated to reflect the actual credit amount from both items in this batch.

Return Drug Batch Sep 19, 2008@10:15:06 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: PICKED UP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13

Reference \# : 2242 Total Batch Credit: \$135.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1.  BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00
2.  MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 60.00

3 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00

Enter ?? for more actions

ADD New Item CRE Credit Update SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit//

### Completing a Batch 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the batch has been picked up and all credits have been updated, the user can complete the batch. From the “Return Drug Batch List” screen, select the batch and the “Return Drug Batch” screen appears. At the “Select Action” prompt, type COM for Complete Batch and press \<ENTER\>. At the “Complete Batch?” prompt, type Y for Yes and press \<ENTER\>. The batch status has changed from Picked Up to Completed. And, the batch has moved from being displayed under the *Batch Work List* option to being displayed under the *Batch Complete List* option. This also finishes the process of returning drugs for credit.

> **NOTE:** Any item without an actual credit amount is marked DENIED when the batch is being completed and a message appears before the user can continue completing the batch as shown in the following example.

Example: Completing a Batch with One Item Denied

Return Drug Batch Sep 19, 2008@10:15:06 Page: 1 of 1

Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08

Batch Number : 0908-020 Status: PICKED UP

Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13

Reference \# : 2242 Total Batch Credit: \$135.00

ORD ORDER DISP DISP ACTUAL

\# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1.  BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00
2.  MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 60.00
3.  MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00

Enter ?? for more actions

ADD New Item CRE Credit Update

SEL Select Item

EDT Edit Batch PKP Pick up Batch

CAN Cancel Batch COM Complete Batch

Select Action: Quit// COM\<Enter\> Complete Batch

> **WARNING:** The following items will have their CREDIT STATUS

set to DENIED because no credit amount has been

entered for them:

-----------------------------------------------------------

RETURN DRUG (NDC) DISP QTY UNIT

-----------------------------------------------------------

BACLOFEN 10MG TABS (00028-0023-01) 3 TABLET

Complete Batch? NO// YES \<Enter\>

Completing Batch...OK

### Select the Correct VistA Session 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a secured invoice file is found and security checks passed, the “Connect To” dialog appears.

Click the down-arrow, select the appropriate account (if more than one exists), and click “OK”.

Figure : Example of Broker Connection Connect To Dialog Box

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/007.png)

> ![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/008.png) Note: The broker connection dialog box may not display if the PSA_MCKESSON_UPLOAD desktop shortcut is configured to connect to a specific VistA instance.

### PIV Certificate Selection 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After clicking OK the PIV Certificate selection dialog box may appear. If the dialog box appears, then select a valid security certificate and click OK.

Figure : Security certificate window

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/009.png)

After clicking OK the PIV PIN dialog box appears. Enter the associated PIV pin and click OK.

Figure : Example of PIV PIN dialog box

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/010.png)

The System Use Notification dialog box appears, click OK.

Figure : Example System Use Notification Dialog Box

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/011.png)

The Select Division dialog box appears, select the correct division and click “OK”.

Figure : Example Select Division Dialog Box

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/012.png)

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/013.png) Note: The Select Division dialog box may not display if the user has only been assigned one division.

### VistA Invoice Upload 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After clicking “OK”, the invoice is uploaded into VistA and a dialog box opens and displays information confirming the invoice data has been transferred to VistA. The upload utility automatically deletes the “.dat” file once upload completes. Click OK.

Figure : Example of Successful Upload Screen

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/014.png)

The program will automatically shut down at this point.

### VistA Upload Status Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Upload Status Report will be sent to the user via Mailman with details and the status of the upload.

Figure : Example of VistA MailMan Upload Status report

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/015.png)

### Invoice File Locations and Navigation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DAU GUI UPLOAD program searches for invoice files in C:\DAU\\ on the users workstation by default. If the invoice file is saved to a location other than C:\DAU\\ a dialog box will open and display “Unable to Find Invoice.”

Figure : Example Error Message, Unable to Find Invoice

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/016.png)

The user should then select the Find Invoice option located under the File menu.

Figure : Example Find Invoice

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/017.png)

Navigate to where you stored the file on the workstation. When the appropriate folder is opened, the program will search for the Invoice file using predefined search parameters. If the file is found, the filename will display in the text box at the bottom of the screen. Click on the file name to select and click OPEN to continue processing. You can also Double Click on the file to select and continue processing.

Figure : Example Invoice File Found

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/018.png)

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/019.png) Note: You can also Double Click the invoice file to select it and continue processing.

### Invoice Error conditions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After an invoice is selected for processing, checks are performed to verify the file meets requirements and has not been tampered with. If the file does not pass the required checks, an error message will display. The invoice may be automatically deleted from the workstation. If you encounter an error condition with an invoice file, delete it from your workstation (if not automatically deleted) and download a new copy of the invoice.

Figure : Example Invoice PO ID# Not Valid Length

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/020.png)

Figure : Example Invoice Failed Security Check

![](drug-accountability-inventory-interface-version-3-user-manual-psa-3-85/021.png)
