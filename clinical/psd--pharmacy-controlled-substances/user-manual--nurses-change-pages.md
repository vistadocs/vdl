---
consolidated_title: "nurse's user manual change pages"
app_code: PSD
doc_type: UM
master_source: "PSD*3*69 Nurse's User Manual Change Pages"
master_pub_date: March 1997
consolidated_from: 3 versions
prior_versions:
  - "PSD*3*71 Nurse's User Manual Change Pages"
  - "PSD*3*76 Nurse's User Manual Change Pages"
---

> ![](psd-3-69-nurse-s-user-manual-change-pages/001.png)

CONTROLLED SUBSTANCES

> NURSES’ USER MANUAL

> Version 3.0

> March 1997

> (Revised August 2008)

> (Revised May 2010)

> Department of Veterans Affairs

> VistA Health Systems Design & Development

> \< This page intentionally left blank\>

> Revision History

> The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.

> Note: The Change Pages document may include unedited pages needed for two-sided copying. Only edited pages display the patch number and revision date in the page footer.

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
<p><a href="#_bookmark0"><u>34-35</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*69</p>
</blockquote></td>
<td><p>Added description of patch’s new security key PSD TECH ADV, and PSD TECH key.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/2010</td>
<td><blockquote>
<p><a href="#_bookmark1"><u>38</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*69</p>
</blockquote></td>
<td><p>Added PSD TECH ADV and PSD TECH keys to Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/08</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*64</p>
</blockquote></td>
<td><p>New menu options added to the Transfer Green Sheet Menu. Reformatted to conform to national standards.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

1)  Master Vault,
2)  Satellite Vault, and
3)  Narcotic Locations.

> NAOU Inventory Group An NAOU Inventory Group is defined by pharmacy to

> represent the Narcotic Areas of Use which are inventoried together as a group. By grouping the commonly inventoried NAOUs under an easy to remember group name, the elements of the inventory are established, and do not have to be redefined every time an inventory is scheduled.

> Narcotic Location An NAOU set up for the nursing wards, pharmacy IV room,

> or a pharmacy working stock area.

> Order Entry Banner Provides a free text field as a site parameter to appear upon

> Nursing CS Order Entry. When the user accesses the following 3 options, the free text field will be displayed:

1)  Nursing Order Entry
2)  Pharmacy Order Entry from Nursing
3)  Infusion Order Entry

> Order Status A processing status is attached to each Controlled Substances request order. The following are valid:

# REQUESTED—NOT ORDERED


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [REQUESTED—NOT ORDERED](#requestednot-ordered)
- [ORDERED—NOT PROCESSED](#orderednot-processed)
- [COMPLETED—GREEN SHEET READY FOR](#completedgreen-sheet-ready-for)
- [COMPLETED—GREEN SHEET PICKED UP Green](#completedgreen-sheet-picked-up-green)
- [COMPLETED—PENDING PROBLEM](#completedpending-problem)
- [A](#a)
- [B](#b)
- [C](#c)
- [D](#d)
- [E](#e)
- [F](#f)
- [G](#g)
- [H](#h)
- [I](#i)
- [M](#m)
- [N](#n)
- [O](#o)
- [P](#p)
- [R](#r)
- [S](#s)
- [T](#t)
- [U](#u)
- [V](#v)
> Requests created by batch processing but not yet approved.

# ORDERED—NOT PROCESSED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ordered by nursing but not processed by pharmacy.

> PROCESSED—NOT DISPENSED Processed (filled) by pharmacy but not yet dispensed.

> FILLED—NOT DELIVERED Dispensed and verified by pharmacy but not delivered to the requesting NAOU.

> DELIVERED—ACTIVELY ON NAOU Drug stored on the NAOU.

# COMPLETED—GREEN SHEET READY FOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PICKUP Nursing has flagged the Green Sheet ready for pharmacy pickup.

# COMPLETED—GREEN SHEET PICKED UP Green

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sheet returned to pharmacy but not yet reviewed.

> COMPLETED—REVIEWED Pharmacy has reviewed the Green Sheet .

# COMPLETED—PENDING PROBLEM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> RESOLUTION Pharmacy has reviewed the Green Sheet and a problem exists

> CANCELLED Order cancelled.

> TRANSFERRED TO ANOTHER NAOU Order and

> drug transferred to another NAOU.

> UNDER REVIEW BY INSPECTOR Order and drug pulled from NAOU by CS Inspector for review.

> LOGGED BY TRAKKER All drug doses from this order have been logged out to patients using the TRAKKER. (Not currently used in Version 2.0.)

> PSD ERROR This key should be allocated to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various error and exception conditions generated when entries are filed from the barcode TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER.

> PSD NURSE This key should be allocated to nurses, usually LPNs, who may only receive and administer controlled substances but cannot place the order requests.

> PSD PARAM This key should be allocated only to the Inpatient Pharmacy Package Coordinator(s). This lock controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site (vault).

> <span id="_bookmark0" class="anchor"></span>PSD TECH Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* \[PSD ON- HAND TECH\], *Transfer Drugs between Dispensing Sites Report* \[PSD PRINT VAULT TRANSFERS TECH\], and

> the *Daily Activity Log (in lieu of VA FORM 10-2320)* \[PSD DAILY LOG TECH\] options on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\].

> PSD TECH ADV Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the *Receipts Into Pharmacy* \[PSD RECEIPTS MENU\], *Dispensing Menu* \[PSD DISPENSING MENU\], *Destructions Menu* \[PSD DESTROY MENU\], *Manufacturer, Lot \#, and Exp. Date - Enter/Edit* \[PSD MFG/LOT/EXP\], and *Outpatient Rx's* \[PSD OUTPATIENT\] on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\].

> PSD TRAN This key should be allocated to the Inpatient Pharmacy Coordinator(s). This key controls the access to the Transfer NAOU Stock Entries option. Users can copy stock entries from one NAOU into another NAOU or from an AR/WS AOU into an NAOU.

> PSDMGR This key should be allocated to the Inpatient Pharmacy Package Coordinator(s) or his/her designee. This lock controls the editing of CS files for package set up. This key locks the Supervisor’s Menu options \[PSD MGR\].

> PSJ PHARM TECH This key should be allocated to pharmacy technicians

> handling narcotic orders.

> PSJ RNURSE This key should be allocated to nurses who request narcotic orders, receive, and administer controlled substances on the wards.

> PSJ RPHARM This key should be given to pharmacists dispensing and receiving narcotic orders.

> Satellite Vault An NAOU set up as a secondary dispensing site.

> Stock Drug A drug (from the DRUG file) stored in an NAOU.

> Stock Level The quantity of a drug stocked in a specific NAOU.

> V*ist*A Veterans Health Information Systems and Technology Architecture

> Ward (for Drug) The name of the ward or wards that will use this particular drug. It is important to accurately answer this prompt because this is the link between the Unit Dose package and the Controlled Substances package. The Unit Dose package looks at this field to know if the drug is a Controlled Substances stocked drug.

> *(This page included for two-sided copying.)*

> Index

# A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Activity Report, 4

# B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Balance Adjustments - NAOU, 23 barcode labels, 5

# C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Check on Priority Orders, 12

> Completing a Green Sheet - Ready for Pickup, 15 CS Order Entry For Ward, 9

# D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Delayed Sign Out Dose for Patient, 22 Delivered-Actively on NAOU, 15 Delivered-Perpetual Inventory, 15

# E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Electronic Signature, 1, 20 E-mail, i

> Expiration Date Report, 26

# F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Filled not Delivered, 15

# G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Green Sheet History, 15

# H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Help Online, 19

# I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Infusion or PCA Syringe Order Entry For Patient, 10 Initialize NAOU Drug Balance, 22

# M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> multiple orders, 9

# N

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Narcotic Count - Shift Report, 18 Not Given, Return to Stock, 7 Nursing Supervisor Menu, 21

# O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> One-Time Request, 9 Order Entry Banner, 33

> , 10

> Orders Filled Not Delivered, 12 Orientation, 1

# P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient ID List Print, 5, 21

> Patient/Location Inquiry, 23

> <span id="_bookmark1" class="anchor"></span>Pending CS Orders Report for an NAOU, 12 PSD TECH, 34

> PSD TECH ADV, 35

# R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ready for Pick Up, 15

> Receipt of Controlled Substance from Pharmacy, 15, 17 *Receipt of Controlled Substances from Pharmacy*, 12 Receive Green Sheet & Drug from another NAOU, 16 Receive GS for PCA/Infusion Signed Out to Patient, 16 Record Defective Dose, 8

> Record Delayed Wastage, 6

> Report of Balance of drugs on NAOU, 18 Reprint Transfer Between NAOUs, 16

# S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Scheduled Delivery, 9

> Sign Out Doses for Patients, 3

> Steps to Prepare a Ward (NAOU) for use of a Radio Frequency Device, 27

# T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Transfer Green Sheet and Drug to another NAOU, 15 Transfer Green Sheet Menu, 15

> Transfer GS for PCA/Infusion Signed Out to Patient, 16 Transferred Green Sheets - Pending NAOU Receipt, 16

# U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Unscheduled Order Report, 23 Unscheduled Pick Up, 9

# V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Verify Count, 13