---
consolidated_title: "pharmacist's user manual change pages"
app_code: PSD
doc_type: UM
master_source: "PSD*3*69 Pharmacist's User Manual Change Pages"
master_pub_date: March 1997
consolidated_from: 3 versions
prior_versions:
  - "PSD*3*71 Pharmacist's User Manual Change Pages"
  - "PSD*3*76 Pharmacist's User Manual Change Pages"
---

> ![](psd-3-69-pharmacist-s-user-manual-change-pages/001.png)

CONTROLLED SUBSTANCES PHARMACIST’S USER MANUAL

> Version 3.0

> March 1997

> (Revised May 2010)

> Department of Veterans Affairs Software Service

> Clinical Ancillary Product Line

> Revision History

> The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.

> Note: The Change Pages document may include unedited pages needed for two- sided copying. Only edited pages display the patch number and revision date in the page footer.

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
<td>05/2010</td>
<td><blockquote>
<p><a href="#_bookmark0"><u>44-45</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*69</p>
</blockquote></td>
<td><blockquote>
<p>Added description of patch’s new security key PSD TECH ADV, and PSD TECH key.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>05/2010</td>
<td><blockquote>
<p><a href="#_bookmark1"><u>50</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*69</p>
</blockquote></td>
<td><blockquote>
<p>PSD TECH and PSD TECH ADV entries added to the Index <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>03/1997</td>
<td></td>
<td></td>
<td><blockquote>
<p>Original Released Pharmacist’s Guide.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# TRANSFERRED TO ANOTHER NAOU Order


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [TRANSFERRED TO ANOTHER NAOU Order](#transferred-to-another-naou-order)
- [> 1358 obligation number, 5](#1358-obligation-number-5)
- [B](#b)
- [C](#c)
- [D](#d)
- [E](#e)
- [F](#f)
- [G](#g)
- [H](#h)
- [I](#i)
- [L](#l)
- [M](#m)
- [N](#n)
- [O](#o)
- [<u>Order Entry Steps</u>, 21](#uorder-entry-stepsu-21)
- [P](#p)
> and drug transferred to another NAOU.
> UNDER REVIEW BY INSPECTOR Order and
> drug pulled from NAOU by CS Inspector for review.
> LOGGED BY TRAKKER All drug doses from this order have been logged out to patients using the TRAKKER. (Not currently used in Version 2.0.)
> Prescription Status A prescription can have one of the following status.
> CANCELLED This term is now referred to throughout the software as Discontinued.(See Discontinued.)
> DELETED This status is used when a prescription is deleted. Prescriptions are no longer physically deleted from the system, but marked as deleted.
> Once a prescription is marked deleted no access is allowed other than view.
> HOLD A prescription that was placed on hold due to reasons determined by the pharmacist.
> NON-VERIFIED There are two types of non- verified statuses. Depending on a site parameter, prescriptions entered by a technician do not become active until they are reviewed by a pharmacist.
> Until such review, they remain non-verified and cannot be printed, canceled or edited except through the Verification menu.
> The second non-verified status is given to prescriptions when a drug/drug interaction is encountered during the new order entry or editing of a prescription.
> PENDING A prescription which has been entered through OERR.
> SUSPENDED A prescription which will be filled at some future date.
> PSD ERROR This key should be allocated to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various error and exception conditions generated when entries are filed from the barcode TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER.
> PSD NURSE This key should be allocated to nurses, usually LPNs, who may only receive and administer controlled substances but cannot place the order requests.
> PSD PARAM This key should be allocated only to the Inpatient Pharmacy Package Coordinator(s). This lock controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site (vault).
> <span id="_bookmark0" class="anchor"></span>PSD TECH Allocate this key to control substance technicians.
> This key controls access to the *List On-Hand Amounts* \[PSD ON-HAND TECH\], *Transfer Drugs between Dispensing Sites Report* \[PSD PRINT VAULT TRANSFERS TECH\], and the *Daily Activity Log (in lieu of VA FORM 10-2320)* \[PSD DAILY LOG TECH\] options on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\].
> PSD TECH ADV Allocate this key to specific control substance
> technicians who perform advance functions. This key controls access to the *Receipts Into Pharmacy* \[PSD RECEIPTS MENU\], *Dispensing Menu* \[PSD DISPENSING MENU\], *Destructions Menu* \[PSD DESTROY MENU\], *Manufacturer, Lot \#, and Exp. Date - Enter/Edit* \[PSD MFG/LOT/EXP\], and *Outpatient Rx's* \[PSD OUTPATIENT\] on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\].
> PSD TRAN This key should be allocated to the Inpatient Pharmacy Coordinator(s). This key controls the access to the Transfer NAOU Stock Entries option. Users can copy stock entries from one NAOU into another NAOU or from an AR/WS AOU into an NAOU.
> PSDMGR This key should be allocated to the Inpatient Pharmacy Supervisor and Package Coordinator(s) or his/her designee. This lock controls the editing of CS files for package set up. This key locks the *Supervisor’s Menu* options \[PSD MGR\].
> PSJ PHARM TECH This key should be allocated to pharmacy
> technicians handling narcotic orders.
> PSJ RNURSE This key should be allocated to nurses who request narcotic orders, receive, and administer
> controlled substances on the wards.
> PSJ RPHARM This key should be given to pharmacists dispensing and receiving narcotic orders.
> Satellite Vault An NAOU set up as a secondary dispensing site.
> Stock Drug A drug (from the DRUG file) stored in an NAOU.
> Stock Level The quantity of a drug stocked in a specific NAOU.
> TRAKKER A barcode collection system utilized by scanning barcode labels or by pressing the key pad on the barcode reader device.
> V*IST*A Veterans Health Information Systems and Technology Architecture
> Ward (for Drug) The name of the ward or wards that will use this
> particular drug. It is important to accurately answer this prompt because this is the link between the Unit Dose package and the Controlled Substances package. The Unit Dose package looks at this field to know if the drug is a Controlled Substances stocked drug.
> *(This page included for two-sided copying.)*
Index

# > 1358 obligation number, 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Barcode TRAKKER for Inventory, 29

# C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> COMPLETE - PENDING PROBLEM RESOLUTION., 15 COMPLETE - REVIEWED, 15

> Complete Green Sheet, 15

> Control Point Transaction number, 5 Control Point Transaction Review, 6 CS Order Entry For Ward, 25

# D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Destroy a Controlled Substances Drug, 23 Destructions Menu, 23

> Dispensing Menu, 7

> Dispensing/Receiving Report (VA FORM 10-2321), 9 Drug Receipt History, 6

# E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Electronic Signature, 3 Electronic Signature Codes, 3

# F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Fill/Dispense CS Orders from Worksheet, 7

# G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> G.Controlled Substances Team@ISC-BIRM, i GREEN SHEET NOT SIGNED BY NURSE, 15

> Green Sheet Reprint (VA FORM 10-2638), 10 Green Sheet—Print (VA FORM 10-2638), 9

# H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Hold a CS Drug (No Inventory Update), 23

# I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IFCAP purchase orders, 5 Infusion Order Entry, 21

> Index

> Infusion Order Processing Menu, 21 Intranet, 4

> Invoice Review (Prime Vendor), 6

# L

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Label for Dispensing (Barcode), 12 Label Reprint for Dispensing Drug, 11

> Load Software and Inventory into TRAKKER, 29

# M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Manufacturer, Lot \#, and Exp. Date—Enter/Edit, 35 Master Vault, 5

> MATH ERROR, 15

# N

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Narcotic Dispensing Equipment Orders, 13 NO DISCREPANCY, 15

> Non—VA Drug Placed on Hold for Destruction, 23

# O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Order Entry Banner, 42 ORDER ENTRY BANNER, 25

# <u>Order Entry Steps</u>, 21

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> OTHER - REFERRED TO PHARMACY SUPERVISOR, 15

> Outpatient RX’s, 17

# P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pharmacy Dispense without (VA FORM 10-2638), 12 Prime Vendor receipts, 5

> Print CS Dispensing Worksheet, 7 PSD ERROR, 44

> PSD NURSE, 44

> PSD PARAM, 44

> <span id="_bookmark1" class="anchor"></span>PSD TECH, 44

> PSD TECH ADV, 44 PSD TRAN, 44

> PSDMGR, 19, 45

> PSJ PHARM TECH, 45 PSJ RNURSE, 45

> PSJ RPHARM, 45

> purchase order number, 5 Purchase Order Review, 6

> 50 Controlled Substances V. 3.0 May 2010 Pharmacist User Manual

> PSD\*3\*69