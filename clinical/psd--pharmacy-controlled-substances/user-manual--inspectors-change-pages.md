---
consolidated_title: "inspectors user manual change pages"
app_code: PSD
doc_type: UM
master_source: "PSD*3*76 Inspectors User Manual Change Pages"
master_pub_date: March 1997
consolidated_from: 3 versions
prior_versions:
  - "PSD*3*69 Inspectors User Manual Change Pages"
  - "PSD*3*71 Inspectors User Manual Change Pages"
---

> ![](psd-3-76-inspectors-user-manual-change-pages/001.png)

CONTROLLED SUBSTANCES (CS)

> INSPECTOR’S USER MANUAL

## Version 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> March 1997

> (Revised May 2013)

> Department of Veterans Affairs Product Development

## Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<th><strong>Date</strong></th>
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
<td>05/2013</td>
<td><blockquote>
<p>i, ii, <a href="#_bookmark0"><u>24-26</u>,</a></p>
<p><a href="#_bookmark2"><u>27-28</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*76</p>
</blockquote></td>
<td><p>Updated Glossary with description of patch’s new security key PSDRPH</p>
<p>Updated Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td><blockquote>
<p><a href="#_bookmark1"><u>25-26</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*71</p>
</blockquote></td>
<td><p>Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2010</td>
<td><blockquote>
<p>24-26, 28</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*69</p>
</blockquote></td>
<td><p>Added description of patch’s new security key PSD TECH ADV, and PSD TECH key.</p>
<p>Added PSD TECH ADV and PSD TECH key to index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/03</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*41</p>
</blockquote></td>
<td><p>Updated the manual to Standards. Added the <em>CS Monitoring Menu</em></p>
<p>options.</p></td>
</tr>
<tr class="odd">
<td>03/97</td>
<td></td>
<td></td>
<td>Original Released Inspector’s Manual.</td>
</tr>
</tbody>
</table>

> \<This page is intentionally left blank.\>

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Version 3.0](#version-30)
  - [Revision History](#revision-history)
- [Introduction](#introduction)
- [Orientation](#orientation)
    - [Order Status (cont.) COMPLETED—GREEN SHEET PICKED UP Green](#order-status-cont-completedgreen-sheet-picked-up-green)
    - [COMPLETED—PENDING PROBLEM](#completedpending-problem)
- [Index](#index)
> The Controlled Substances (CS) computer software package V. 3.0 is one segment of the Veterans Health Information Systems and Technology Architecture (V*IST*A) in use at the Department of Veterans Affairs Medical Centers (VAMCs). This package provides functionality to monitor and track the receipt, inventory, and dispensing of all controlled substances. It also provides the pharmacy with the capability to define a controlled substance location and a list of controlled substances to maintain a perpetual inventory.
> This package provides the capability for pharmacy personnel to receive a Controlled Substances order, automatically update the quantity on hand, and view a receipt history. Nursing personnel are provided with the ability to request orders for Controlled Substances via on-demand requests. Pharmacy may dispense controlled substances via the software automating all necessary documents (VA FORMs 10-2321 and 10-2638) to complete an order request. The software provides functionality to record Automated Management Information System (AMIS) and cost data, address returns to stock, destructions, order cancellations, transfers between locations, and log outpatient prescriptions.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

> Example: *Controlled Substance Balances Report* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them. Example: “Select INPATIENT SITE NAME” indicates a screen prompt.
- Responses in bold face indicate what the user is to type in. Example: Okay to Continue? No// YES.
- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.

> Example: Press \<Tab\> to move the cursor to the next field.

> Press \<Enter\> to select the default.

### Order Status (cont.) COMPLETED—GREEN SHEET PICKED UP Green

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sheet returned to pharmacy but not yet reviewed.

> COMPLETED—REVIEWED Pharmacy has reviewed the Green Sheet .

### COMPLETED—PENDING PROBLEM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> RESOLUTION Pharmacy has reviewed the Green Sheet and a problem exists

> CANCELLED Order cancelled.

> TRANSFERRED TO ANOTHER NAOU Order and

> drug transferred to another NAOU.

> UNDER REVIEW BY INSPECTOR Order and drug pulled from NAOU by CS Inspector for review.

> LOGGED BY TRAKKER All drug doses from this order have been logged out to patients using the TRAKKER.

> <span id="_bookmark0" class="anchor"></span>PSD ERROR This key should be allocated to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various error and exception conditions generated when entries are filed from the barcode TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER.

> PSD NURSE This key should be allocated to nurses, usually LPNs, who may only receive and administer controlled substances but cannot place the order requests.

> PSD PARAM This key should be allocated only to the Inpatient Pharmacy Package Coordinator(s). This lock controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site (vault).

> PSD TECH Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* \[PSD ON- HAND TECH\], *Transfer Drugs between Dispensing Sites Report* \[PSD PRINT VAULT TRANSFERS TECH\], and

> the *Daily Activity Log (in lieu of VA FORM 10-2320)*\[PSD DAILY LOG TECH\] options on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\].

> <span id="_bookmark1" class="anchor"></span>PSD TECH ADV Allocate this key to specific control substance technicians

> who perform advance functions. This key controls access to the *Receipts Into Pharmacy* \[PSD RECEIPTS MENU\], *Dispensing Menu* \[PSD DISPENSING MENU\], *Destructions Menu* \[PSD DESTROY MENU\], *Manufacturer, Lot \#, and Exp. Date - Enter/Edit* \[PSD MFG/LOT/EXP\], *Outpatient Rx's* \[PSD OUTPATIENT\], *Complete Green Sheet* \[PSD COMPLETE GS\], *Destroyed Drugs Report* \[PSD DEST DRUGS REPORT\], *DEA Form 41 Destroyed Drugs Report* \[PSD DESTROY DEA41\], *Destructions Holding Report* \[PSD DESTRUCTION HOLDING\], *Add Existing Green Sheets at Setup* \[PSD EXISTING GS\], *Green Sheet Transfer Between NAOUs Report* \[PSD GS TRANSFER (NAOU) REPORT\],

> *Transfer Drugs between Dispensing Sites* \[PSD TRANSFER VAULT DRUGS\] options on the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\]. The CS technician may perform all functions of the *Outpatient Rx’s* \[PSD OUTPATIENT\] option except releasing prescriptions.

> PSD TRAN This key should be allocated to the Inpatient Pharmacy Coordinator(s). This key controls the access to the *NAOU to NAOU Transfer Stock Entries* \[PSD TRANSFER NAOU\] option. Users can copy stock entries from one NAOU into another NAOU or from an AR/WS AOU into an NAOU.

> PSDMGR This key should be allocated to the Inpatient Pharmacy Supervisor and Package Coordinator(s) or his/her designee. This lock controls the editing of Controlled Substances V.

> 3.0 files for package set up. This key locks the *Supervisor (CS) Menu* \[PSD MGR\] option.

> PSDRPH This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.

> PSJ PHARM TECH This key should be allocated to pharmacy technicians

> handling narcotic orders.

> PSJ RNURSE This key should be allocated to nurses who request narcotic orders, receive, and administer controlled substances on the wards.

> PSJ RPHARM This key should be given to pharmacists dispensing and receiving narcotic orders.

> Satellite Vault An NAOU set up as a secondary dispensing site.

> Stock Drug A drug (from the DRUG file) stored in an NAOU.

> Stock Level The quantity of a drug stocked in a specific NAOU.

> V*IST*A Veterans Health Information Systems and Technology Architecture

> Ward (for Drug) The name of the ward or wards that will use this particular drug. It is important to accurately answer this prompt because this is the link between the Inpatient Medications

> V. 5.0 package and the Controlled Substances V. 3.0 package. The Inpatient Medications V. 5.0 package looks at this field to know if the drug is a Controlled Substances stocked drug.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A
> Aid and Attendance 19
> AMIS 1
> B
> Barcode TRAKKER for CS Inspections 4
> C
> Controlled Substance Balances Report 3
> Controlled Substances Inspector Menu 3
> CS Inspector 3, 10, 11, 13, 15, 16, 18
> D
> DELIVERED - ACTIVELY ON NAOU 10
> Drug Accountability 13
> F
> Fee Basis 19
> G
> Green Sheet 3, 10, 21, 22, 23, 24
> Green Sheet History 10
> H
> Hidden Actions 2
> I
> Inspector’s Log by Rec’d Date 3
> Inspector’s Log for Controlled Substances 3
> IRL 4, 9
> L
> Load Software and Insp. Inventory into TRAKKER 4
> M
> MailMan Message 9
> N
> NAOU 3, 10, 21, 22, 23, 24, 26
> May 2013 Controlled Substances V. 3.0 27
> <span id="_bookmark2" class="anchor"></span>P
> Place Green Sheet on Hold 10
> PSD ERROR 24
> PSD NURSE 24
> PSD PARAM 24
> PSD TECH 24
> PSD TECH ADV 25
> PSD TRAN 25
> PSDMGR 25
> PSDRPH 25
> PSJ PHARM TECH 25
> PSJ RNURSE 26
> PSJ RPHARM 26
> R
> Remove Green Sheet from Hold 10
> S
> Send Inspections Inventory TRAKKER Data to DHCP 8
> T
> TRAKKER 4, 8, 9, 24
> U
> Under Inspector’s Review—Green Sheets 10
> UNDER REVIEW BY INSPECTOR 10
> V
> VA FORM 10-2321 1
> VA FORM 10-2638 1, 10
> VAMCs 1
> Vault 4, 5, 11, 13, 21, 24
> V*IST*A 1, 4, 8, 26


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSD*3*69 Inspectors User Manual Change Pages

## REQUESTED—NOT ORDERED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Requests created by batch processing but not yet approved.

## ORDERED—NOT PROCESSED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ordered by nursing but not processed by pharmacy.

> PROCESSED—NOT DISPENSED Processed (filled) by pharmacy but not yet dispensed.

> FILLED—NOT DELIVERED Dispensed and verified by pharmacy but not delivered to the requesting NAOU.

> DELIVERED—ACTIVELY ON NAOU Drug stored on the NAOU.

## COMPLETED—GREEN SHEET READY FOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PICKUP Nursing has flagged the Green Sheet ready for pharmacy pickup..
