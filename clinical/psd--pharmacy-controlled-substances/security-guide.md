---
consolidated_title: "package security guide change pages"
app_code: PSD
doc_type: SG
master_source: "PSD*3*76 Package Security Guide Change Pages"
master_pub_date: March 1997
consolidated_from: 3 versions
prior_versions:
  - "PSD*3*69 Package Security Guide Change Pages"
  - "PSD*3*71 Package Security Guide Change Pages"
---

> ![](psd-3-76-package-security-guide-change-pages/001.png)

CONTROLLED SUBSTANCES

Package Security Guide

> Version 3.0

> March 1997

> (Revised May 2013)

> Department of Veterans Affairs Product Development

> Revision History

> The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>05/2013</p>
</blockquote></td>
<td><blockquote>
<p>i, ii, <a href="#_bookmark0"><u>2-3</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*76</p>
</blockquote></td>
<td><blockquote>
<p>Added description of patch’s new security key PSDRPH</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/2011</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0"><u>2-3</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*71</p>
</blockquote></td>
<td><blockquote>
<p>Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>05/2010</p>
</blockquote></td>
<td><blockquote>
<p>1-2</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*69</p>
</blockquote></td>
<td><blockquote>
<p>Added description of patch’s new security key PSD TECH ADV. Added Revision History.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/97</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Original Released Package Security Guide.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

> Package Security

> The Controlled Substances module does not contain any VA FileMan security codes except for programmer security (@) on the data dictionaries for the CS files.

> Security with respect to standard options in the module is implemented by carefully assigning option to users and through the use of security keys.

# Options


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Options](#options)
- [Keys](#keys)
- [Hardware Requirements](#hardware-requirements)
> All pharmacy personnel can be assigned the *PSD MENU* option as the primary menu option.
> Nursing personnel can be assigned the *PSD NURSE MENU* option.
> Controlled Substances Inspectors can be assigned the *PSD INSPECTOR MENU*
> option.
> Some stations design their own menus for individual users. If this is the case, then the top level CS menu must contain the following entry and exit code in the OPTION file (#19):
> ENTRY ACTION: I’\$D(PSDSITE) D ^PSDSET EXIT ACTION: K PSDSITE
> This entry and exit code must be present because the PSDSITE variable is set as users enter the package. If the Kernel’s ^OPTION NAME feature is used to jump directly into lower levels of the CS package, then the “Inpatient Site Name” prompt must be answered in order to define the PSDSITE variable. All options are independently invocable, however, if the instructions above are not followed, users will be repeatedly asked to select an inpatient site if there are two or more sites flagged for CS use.

# Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the users are assigned the primary menu option, it is necessary to give the appropriate security keys to each user as required. There are ten keys associated with CS.

> Package Security

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>PSD ERROR</strong></p>
</blockquote></th>
<th><blockquote>
<p>This key should be allocated to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various error and exception conditions generated when entries are filed from the barcode TRAKKER. Also, holders of this key receive electronic mail messages created using the TRAKKER.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>PSD NURSE</strong></p>
</blockquote></td>
<td><blockquote>
<p>This key should be allocated to nurses, usually LPNs, who can only receive and administer controlled substances but cannot place the order requests.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSD PARAM</strong></p>
</blockquote></td>
<td><blockquote>
<p>This key should be allocated <strong>only</strong> to the Inpatient Pharmacy Package Coordinator or his/her designee. This key controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site (vault).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PSD TECH</strong></p>
</blockquote></td>
<td><blockquote>
<p>Allocate this key to control substance technicians. This key controls access to the <em>List On-Hand Amounts</em> [PSD ON- HAND TECH], <em>Transfer Drugs between Dispensing Sites Report</em> [PSD PRINT VAULT TRANSFERS TECH], and the</p>
<p><em>Daily Activity Log (in lieu of VA FORM 10-2320)</em> [PSD DAILY LOG TECH] options on the Technician (CS Pharmacy) Menu [PSD PHARM TECH].</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><span id="_bookmark0" class="anchor"></span><strong>PSD TECH ADV</strong></p>
</blockquote></td>
<td><blockquote>
<p>Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the <em>Receipts Into Pharmacy</em> [PSD RECEIPTS MENU], <em>Dispensing Menu</em> [PSD DISPENSING MENU], <em>Destructions Menu</em> [PSD DESTROY MENU], <em>Manufacturer, Lot #, and Exp. Date - Enter/Edit</em> [PSD MFG/LOT/EXP], <em>Outpatient Rx's</em> [PSD OUTPATIENT], <em>Complete Green Sheet</em> [PSD COMPLETE GS], <em>Destroyed Drugs Report</em> [PSD DEST DRUGS REPORT], <em>DEA Form 41 Destroyed Drugs Report</em> [PSD DESTROY DEA41], <em>Destructions Holding Report</em> [PSD DESTRUCTION HOLDING], <em>Add Existing Green Sheets at Setup</em> [PSD EXISTING GS], <em>Green Sheet Transfer Between NAOUs Report</em> [PSD GS TRANSFER (NAOU) REPORT], <em>Transfer</em></p>
<p><em>Drugs between Dispensing Sites</em> [PSD TRANSFER VAULT DRUGS] options on the <em>Technician (CS Pharmacy) Menu</em> [PSD PHARM TECH]. The CS technician may perform all</p>
<p>functions of the <em>Outpatient Rx’s</em> [PSD OUTPATIENT] option except releasing prescriptions.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Package Security

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>PSD TRAN</strong></p>
</blockquote></th>
<th><blockquote>
<p>This key should be allocated <strong>only</strong> to the Inpatient Pharmacy Package Coordinators. This key controls access to the <em>NAOU to NAOU Transfer Stock Entries</em> [PSD TRANSFER NAOU] option. Users can copy the stock entries from one NAOU into other NAOUs or from AR/WS AOU into an NAOU.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>PSDMGR</strong></p>
<p><strong>PSDRPH</strong></p>
<p><strong>PSJ PHARM TECH</strong></p>
<p><strong>PSJ RNURSE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Allocate this key to the Inpatient Pharmacy Coordinators. This key controls the editing of CS files for package set up and it locks the <em>Supervisor (CS) Menu</em> option.</p>
<p>This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.</p>
<p>This key should be allocated to pharmacy technicians handling narcotic orders.</p>
<p>This key should be allocated to nurses who request narcotic orders, receive, and administer controlled substances on the wards.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSJ RPHARM</strong></p>
</blockquote></td>
<td><blockquote>
<p>This key should be allocated to pharmacists dispensing and receiving narcotic orders.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following equipment is recommended to successfully implement Version 3.0 Intermec TRAKKER 9440 (Barcode Reader)

> HP LaserJet III (or any compatible laser printer)

> VT320 (bi-directional only) or any bi-directional flow CRT

> The laser single sheet feed printer is required to print the VA FORM 10-2638 and barcode ID labels. It is recommended that the printer be physically located in the narcotic vault for efficiency and security.

> *(This page included for two-sided copying.)*