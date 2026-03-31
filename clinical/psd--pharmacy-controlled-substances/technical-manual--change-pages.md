---
consolidated_title: "technical manual change pages"
app_code: PSD
doc_type: TM
master_source: "PSD*3*64 Technical Manual Change Pages"
master_pub_date: March 1997
consolidated_from: 5 versions
prior_versions:
  - "PSD*3*69 Technical Manual Change Pages"
  - "PSD*3*71 Technical Manual Change Pages"
  - "PSD*3*73 Technical Manual Change Pages"
  - "PSD*3*76 Technical Manual Change Pages"
---

> ![](psd-3-64-technical-manual-change-pages/001.png)

CONTROLLED SUBSTANCES (CS)

> TECHNICAL MANUAL

# Version 3.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Version 3.0](#version-30)
- [Revision History](#revision-history)
> March 1997
> (Revised August 2008)
> Department of Veterans Affairs
> V*IST*A Health Systems Design & Development

# Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<td>08/08</td>
<td><blockquote>
<p>24, 25, 38</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*64</p>
</blockquote></td>
<td><p>New menu options added to the Transfer Green Sheet Menu</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/03</td>
<td><blockquote>
<p>19-20,</p>
<p>44-45</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*40</p>
</blockquote></td>
<td>Added two new reports associated with the Electronic Order Entry for Schedule II Controlled Substances project to the <em>Production Repo</em>rts [PSD PRODUCTION REPORTS] menu: <em>Digitally Signed CS Orders Report</em> [PSD DIGITALLY SIGNED ORDERS] and <em>Digitally Signed OP Released Rx Report</em> [PSD DIG. SIGNED RELEASED RX].</td>
</tr>
<tr class="odd">
<td>04/03</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*41</p>
</blockquote></td>
<td><p>Updated the manual to Standards. Added the <em>CS Monitoring Menu</em></p>
<p>options and routines.</p></td>
</tr>
<tr class="even">
<td>03/97</td>
<td></td>
<td></td>
<td>Original Released Technical Manual.</td>
</tr>
</tbody>
</table>

> August 2008 Controlled Substances V. 3.0 i Technical Manual

> \<This page is intentionally left blank.\>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PSD ERR/ADJ EDIT</p>
<p><strong>Lock:</strong> PSD ERROR</p></td>
<td>PSDERD</td>
<td><p><em>Enter Error/Adjustment Resolution</em></p>
<p>This option allows designated Pharmacy Supervisors the ability to enter a resolution comment for each error or adjustment created when using the barcode TRAKKER.</p></td>
</tr>
<tr class="even">
<td>PSD ERR/ADJ PENDING REPORT <strong>Lock:</strong> PSD ERROR</td>
<td>PSDERP</td>
<td><p><em>List Pending Errors/Adjustments Logged by TRAKKER</em></p>
<p>This option lists all pending errors/adjustments logged from the barcode TRAKKER for a specific Dispensing Site within a given time frame.</p></td>
</tr>
<tr class="odd">
<td><p>PSD ERR/ADJ RESOLVED REPORT</p>
<p><strong>Lock:</strong> PSD ERROR</p></td>
<td>PSDERCP</td>
<td><p><em>Print Resolved Errors/Adjustments Log</em> This report prints a listing of all resolved errors/adjustments logged by the barcode</p>
<p>TRAKKER for a specific Dispensing Site within a given time frame.</p></td>
</tr>
<tr class="even">
<td>PSD EXISTING GS</td>
<td>PSDEXGS</td>
<td><p><em>Add Existing Green Sheets at Setup</em></p>
<p>This option provides pharmacy the ability to enter existing Green Sheets and active orders on an NAOU, at package setup. These orders may be tracked through the CS software.</p></td>
</tr>
<tr class="odd">
<td>PSD EXP REPORT</td>
<td>PSDEXP</td>
<td><p><em>Expiration Date Report</em></p>
<p>This option will print a Controlled Substances Expiration Date Report for a single NAOU, several NAOUs, or ALL NAOUs. This report may be sorted by DATE/DRUG/NAOU or by DATE/NAOU/DRUG.</p></td>
</tr>
<tr class="even">
<td>PSD GS DISCREPANCY REPORT</td>
<td>PSDCRP</td>
<td><p><em>Completed Green Sheet Discrepancy Report</em> This report lists all Green Sheets with a completion status of MATH ERROR, GREEN</p>
<p>SHEET NOT SIGNED BY NURSE, or OTHER -</p>
<p>REFERRED TO SUPERVISOR. This report may be printed for a single NAOU, several NAOUs, or ALL NAOUs.</p></td>
</tr>
<tr class="odd">
<td>PSD GS HISTORY</td>
<td>PSDGSH</td>
<td><p><em>Green Sheet History</em></p>
<p>The Green Sheet history provides pharmacy with a detailed account of every transaction affecting this VA FORM 10-2638. This history may be displayed to the user's screen or directed to a printer.</p></td>
</tr>
<tr class="even">
<td>PSD GS LISTING</td>
<td>PSDGSL</td>
<td><p><em>Listing of Green Sheet Log</em></p>
<p>This option numerically lists all Green Sheets for a given date range or for a given Green Sheet number range. The logs list Green Sheet number, date dispensed, and current status.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD GS REC PCA/INF FOR PATIENT</td>
<td>PSDNTTPC</td>
<td><p><em>Receive GS for PCA/Infusion Signed Out to Patient</em></p>
<p>This option provides nurses the ability to receive Green Sheets for PCA/Infusions from another NAOU. The transferring of these Green Sheets between NAOUs requires two processing steps.</p>
<p>Step 1 – Transfer GS for PCA/Infusion Signed Out to Patient</p>
<p>Step 2 – Receive GS for PCA/Infusion Signed Out to Patient</p></td>
</tr>
<tr class="even">
<td>PSD GS TRANS NOT RECD (NAOU)</td>
<td>PSDNBT</td>
<td><p><em>Transferred Green Sheets - Pending NAOU Receipt</em></p>
<p>This report lists all Green Sheets that have been transferred from an NAOU and are pending receipt in another NAOU.</p></td>
</tr>
<tr class="odd">
<td>PSD GS TRANS PCA/INF PATIENT</td>
<td>PSDNTFPC</td>
<td><p><em>Transfer GS for PCA/Infusion Signed Out to Patient</em></p>
<p>This option provides nurses the ability to transfer Green Sheets for PCA/Infusions to another NAOU. The transferring of these Green Sheets between NAOUs requires two processing steps.</p>
<p>Step 1 – Transfer GS for PCA/Infusion Signed Out to Patient</p>
<p>Step 2 – Receive GS for PCA/Infusion Signed Out to Patient</p></td>
</tr>
<tr class="even">
<td>PSD GS TRANSFER (NAOU) REPORT</td>
<td>PSDNTR</td>
<td><p><em>Green Sheet Transfer Between NAOUs Report</em> This report lists all Green Sheets transferred and received between NAOUs for a given date range. This report may be printed for a single NAOU,</p>
<p>several NAOUs, or ALL NAOUs.</p></td>
</tr>
<tr class="odd">
<td>PSD INACTIVATE NAOU</td>
<td>PSDNACT</td>
<td><p><em>Inactivate NAOU</em></p>
<p>This option will allow a user to inactivate an NAOU. An inactivation date may be entered for a future time.</p></td>
</tr>
<tr class="even">
<td>PSD INACTIVATE NAOU STOCK DRUG</td>
<td>PSDNSTK</td>
<td><p><em>Inactivate NAOU Stock Drug</em></p>
<p>This option is used to inactivate a drug that is currently on a NAOU stock list. Drugs should not be deleted, but simply inactivated.</p></td>
</tr>
<tr class="odd">
<td>PSD INFUSION MENU</td>
<td></td>
<td><p><em>Infusion Order Processing Menu</em></p>
<p>This menu contains the infusion order/entry and transferring a Green Sheet options associated with the IV pharmacist processing a CS infusion order.</p></td>
</tr>
</tbody>
</table>

> 24 Controlled Substances V. 3.0 August 2008

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><p><strong>Menu Items:</strong></p>
<p>PSD INFUSION O/E</p>
<p><em>Infusion Order Entry</em></p>
<p>PSD NURSE TRANSFER GS</p>
<p><em>Transfer Green Sheet and Drug to another NAOU Transfer GS for PCA/Infusion Signed Out to Patient</em></p></td>
</tr>
<tr class="even">
<td>PSD INFUSION O/E</td>
<td>PSDORV</td>
<td><p><em>Infusion Order Entry</em></p>
<p>The IV pharmacist uses this option to electronically request CS drugs used in IV orders. Only infusion orders requiring the VA FORM 10- 2638 should be requested using this option.</p></td>
</tr>
<tr class="odd">
<td>PSD INSP LOG BY RECD DATE</td>
<td>PSDRLOG</td>
<td><p><em>Inspector's Log by Rec'd Date</em></p>
<p>This report lists all dispensing transactions for Narcotic Area of Use received within a given date range. The data includes dispensing number, drug name, date received, quantity received, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.</p></td>
</tr>
<tr class="even">
<td>PSD INSP PLACE HOLD</td>
<td>PSDCSI</td>
<td><p><em>Place Green Sheet on Hold</em></p>
<p>This option allows the CS Inspector to place a Green Sheet on hold for review.</p></td>
</tr>
<tr class="odd">
<td>PSD INSP REMOVE HOLD</td>
<td>PSDRSI</td>
<td><p><em>Remove Green Sheet from Hold</em></p>
<p>This option allows the CS Inspector to remove a Green Sheet from hold.</p></td>
</tr>
<tr class="even">
<td><p>PSD INSPECTOR MENU</p>
<p><strong>Action:</strong> I '$D(PSDSITE) D</p>
<p>^PSDSET</p>
<p><strong>Exit Action:</strong> K PSDSITE</p></td>
<td></td>
<td><p><em>Controlled Substances Inspector Menu</em></p>
<p>This menu contains all options associated with a CS inspection.</p>
<p><strong>Menu Items:</strong></p>
<p>PSD INSP PLACE HOLD</p>
<p><em>Place Green Sheet on Hold</em></p>
<p>PSD INSP REMOVE HOLD</p>
<p><em>Remove Green Sheet from Hold</em></p>
<p>PSD PRINT INSPECTOR LOG</p>
<p><em>Inspector's Log for Controlled Substances</em></p>
<p>PSD PRT GS INSP HOLD</p>
<p><em>Under Inspector's Review - Green Sheets</em></p>
<p>PSD INVEN SHEET PRT</p>
<p><em>Inventory Sheet Print</em></p></td>
</tr>
</tbody>
</table>

> August 2008 Controlled Substances V. 3.0 25

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><p>PSD INSP LOG BY RECD DATE</p>
<p><em>Inspector's Log by Rec'd Date</em></p>
<p>PSD IRL INSP MENU</p>
<p><em>Barcode TRAKKER for CS Inspections</em></p>
<p>PSD GS HISTORY</p>
<p><em>Green Sheet History</em></p>
<p>PSD NAOU BALANCE REPORT</p>
<p><em>Narcotic Count - Shift Report</em></p></td>
</tr>
<tr class="even">
<td>PSD INVEN SHEET PRT</td>
<td>PSDBALI</td>
<td><p><em>Inventory Sheet Print</em></p>
<p>This option prints an Inspector's Sheet, which is used to inventory on-hand amounts within a pharmacy-dispensing site (vault). This form lists current on-hand amounts and provides a blank space for the inspector to list actual on-hand counts. A signature line is included on each page. This sheet may be generated for one drug, some drugs, or ALL drugs. The drugs are listed alphabetically.</p></td>
</tr>
<tr class="odd">
<td>PSD INVEN TYPE EDIT</td>
<td>PSDNVT</td>
<td><p><em>Inventory Types - Enter/Edit</em></p>
<p>This option will edit the entries in the AOU INVENTORY TYPE file (#58.16) used to classify NAOU drugs.</p></td>
</tr>
<tr class="even">
<td>PSD INVEN TYPE PRINT</td>
<td>INVEN^PSDPRT</td>
<td><p><em>Print Inventory Types</em></p>
<p>Use this option to print the entries in the AOU INVENTORY TYPE file (#58.16) used to classify NAOU stocked drugs.</p></td>
</tr>
<tr class="odd">
<td>PSD IRL INSP DATA</td>
<td>UPLOAD^PSDUP3</td>
<td><p><em>Send Inspections Inventory TRAKKER Data to DHCP</em></p>
<p>This option contains the access to upload or send narcotic vault inspections inventory from the</p>
<p>barcode TRAKKER to <strong>V</strong><em>IST</em><strong>A</strong>.</p></td>
</tr>
<tr class="even">
<td>PSD IRL INSP MENU</td>
<td></td>
<td><p><em>Barcode TRAKKER for CS Inspections</em></p>
<p>This menu contains the options associated with performing narcotic vault inspections using the barcode TRAKKER device.</p>
<p><strong>Menu Items:</strong></p>
<p>PSD IRL INSPECTOR INV</p>
<p><em>Load Software and Insp. Inventory into TRAKKER</em></p></td>
</tr>
</tbody>
</table>

> 26 Controlled Substances V. 3.0 August 2008

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><p>PSD IRL INSP DATA</p>
<p>Send Inspections Inventory TRAKKER Data to DHCP</p></td>
</tr>
<tr class="even">
<td>PSD IRL INSPECTOR INV</td>
<td>PSDUP3</td>
<td><p><em>Load Software and Insp. Inventory into TRAKKER</em></p>
<p>This option contains the access to download an IRL program to the TRAKKER and download the narcotic inspections inventory to the TRAKKER. This option is used for the Narcotic Inspectors only.</p></td>
</tr>
<tr class="odd">
<td>PSD IRL INV DATA</td>
<td>UPLOAD^PSDUP2</td>
<td><p><em>Send Vault TRAKKER Inventory Data to DHCP</em> This option contains the access to upload or send vault inventory from the barcode TRAKKER to</p>
<p><strong>V</strong><em>IST</em><strong>A</strong>.</p></td>
</tr>
<tr class="even">
<td>PSD IRL INV MENU</td>
<td></td>
<td><p><em>Barcode TRAKKER for Inventory</em></p>
<p>This menu contains the options associated with performing narcotic vault inventories using the barcode TRAKKER device.</p>
<p><strong>Menu Items:</strong></p>
<p>PSD IRL VAULT INV</p>
<p><em>Load Software and Inventory into TRAKKER</em></p>
<p>PSD IRL INV DATA</p>
<p><em>Send Vault TRAKKER Inventory Data to DHCP</em></p></td>
</tr>
<tr class="odd">
<td>PSD IRL VAULT INV</td>
<td>PSDUP2</td>
<td><p><em>Load Software and Inventory into TRAKKER</em> This option contains the access to download an IRL program to the TRAKKER and download the vault inventory to the TRAKKER, in one step.</p>
<p>This option is used for pharmacy service only.</p></td>
</tr>
<tr class="even">
<td>PSD LABEL DRUG/NUMBER</td>
<td>PSDLBL</td>
<td><p><em>Label for Dispensing (Barcode)</em></p>
<p>This option allows pharmacy to print the dispensing number/drug barcode label that is attached to the drug delivered to the NAOUs.</p></td>
</tr>
<tr class="odd">
<td>PSD LABEL INSP</td>
<td>PSDLBLI</td>
<td><p><em>Inspectors Label Print</em></p>
<p>This option allows the inspector or Pharmacy Supervisor to print the CS Inspector's barcode labels.</p></td>
</tr>
<tr class="even">
<td><p>PSD LABEL PHARM</p>
<p><strong>Lock:</strong> PSDMGR</p></td>
<td>PSDLBL3</td>
<td><p><em>Print Pharmacist ID Labels</em></p>
<p>This option allows Pharmacy Supervisors to print the pharmacists barcoded ID label. This label is scanned when pharmacists inventory CS drugs in the dispensing vault.</p></td>
</tr>
</tbody>
</table>

> August 2008 Controlled Substances V. 3.0 27

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD LABEL VAULT</td>
<td>PSDLBL1</td>
<td><p><em>Barcode Drug Labels for Vault</em></p>
<p>This option allows pharmacy to print the barcode labels for dispensing-site (vault) stocked drugs.</p></td>
</tr>
<tr class="even">
<td>PSD MARK</td>
<td>PSDAPU</td>
<td><p><em>Mark/Unmark Drugs for Controlled Substances Use</em></p>
<p>This option provides the ability to mark/unmark entries in the DRUG file (#50) for use with the CS package.</p></td>
</tr>
<tr class="odd">
<td><p>PSD MENU</p>
<p><strong>Action:</strong> I '$D(PSDSITE) D</p>
<p>^PSDSET</p>
<p><strong>Exit Action:</strong> K PSDSITE</p></td>
<td></td>
<td><p><em>Controlled Substances Menu</em></p>
<p>This menu contains access to all options associated with the CS module of the Pharmacy software.</p>
<p><strong>Menu Items:</strong></p>
<p>PSD MGR</p>
<p><em>Supervisor (CS) Menu</em></p>
<p>PSD TRANSACTION MENU</p>
<p><em>Pharmacist Menu</em></p>
<p>PSD PRODUCTION REPORTS</p>
<p><em>Production Reports</em></p>
<p>PSD PHARM TECH</p>
<p><em>Technician (CS Pharmacy) Menu</em></p>
<p>PSD LABEL VAULT</p>
<p><em>Barcode Drug Labels for Vault</em></p></td>
</tr>
<tr class="even">
<td>PSD MFG REPORT PRINT</td>
<td>PSDPMFG</td>
<td><p><em>Manufacturer and Narcotic Information Report</em> This report prints an alphabetical listing of all ACTIVE drugs within an ACTIVE NAOU that have been defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This</p>
<p>report lists NAOU, drug name, manufacturer, lot #, expiration date, narcotic breakdown unit, and narcotic package size. This report may be sorted alphabetically by NAOU, then drug name or drug name, then NAOU. The user may select one NAOU, several NAOUs, or all NAOUs to print.</p></td>
</tr>
<tr class="odd">
<td>PSD MFG/LOT/EXP DATE EDIT</td>
<td>PSDMFG</td>
<td><p><em>Manufacturer, Lot #, and Exp. Date - Enter/Edit</em> This option allows the user to enter or edit manufacturer, lot #, and expiration dates for</p>
<p>stocked drugs in an NAOU.</p></td>
</tr>
</tbody>
</table>

> 28 Controlled Substances V. 3.0 August 2008

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD NURSE ORDER MENU</td>
<td></td>
<td><p><em>Ordering Menu</em></p>
<p>This menu contains options for ordering and checking on orders.</p>
<p><strong>Menu Items:</strong></p>
<p>PSD ORDER ENTRY</p>
<p><em>CS Order Entry For Ward</em></p>
<p>PSD PEND NAOU ORDERS</p>
<p><em>Pending CS Orders Report for an NAOU</em></p>
<p>PSD NOT DELIVERED NURSE</p>
<p><em>Orders Filled Not Delivered</em></p>
<p>PSD NURSE PRIORITY ORDER CHECK</p>
<p><em>Check on Priority Orders</em></p>
<p>PSD NURSE INFUSION</p>
<p><em>Infusion or PCA Syringe Order Entry For Patient</em></p></td>
</tr>
<tr class="even">
<td>PSD NURSE PRIORITY ORDER CHECK</td>
<td>PSDEM4</td>
<td><p><em>Check on Priority Orders</em></p>
<p>This option will check the status of Priority Orders that Pharmacy has filled today for a selected NAOU.</p></td>
</tr>
<tr class="odd">
<td>PSD NURSE REC TRANSFER GS</td>
<td>PSDNTT</td>
<td><p><em>Receive Green Sheet &amp; Drug from another NAOU</em> This option provides nurses the ability to receive CS drugs and their associated Green Sheet from another NAOU. The transferring of CS drugs between NAOUs requires two processing steps.</p>
<blockquote>
<p>Step 1 - Transfer Green Sheet and Drug to another NAOU</p>
<p>Step 2 - From an NAOU - Receive Green Sheet Transfer &amp; Drug</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSD NURSE REPRINT 2321</td>
<td>PSDRPT</td>
<td><p><em>Reprint Transfer Between NAOUs (VA FORM 10- 2321)</em></p>
<p>Nurses may reprint the transfer between NAOUs form (in lieu of VA FORM 10-2321) for any Green Sheet and drug transferred from their NAOU. The form may be reprinted only if the transferred Green Sheet and drug has not been received into the NAOU receiving the transfer.</p></td>
</tr>
<tr class="odd">
<td>PSD NURSE SHIFT LOG</td>
<td>PSDNSCL</td>
<td><p><em>Ward (NAOU) Drug History</em></p>
<p>Use this report to list all ACTIVE CS orders currently on a specific NAOU.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD NURSE SUPR MENU</td>
<td rowspan="7"></td>
<td><p><em>Nursing Supervisor Menu</em></p>
<p>This is a menu with special options to support the signing out of CS.</p>
<p><strong>Menu Items:</strong></p>
<p>PSD NAOU BAL INITIAL</p>
<p><em>Initialize NAOU Drug Balance</em></p></td>
</tr>
<tr class="even">
<td></td>
<td><p>PSD NAOU ADJ</p>
<p><em>Balance Adjustments - NAOU</em></p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>PSD PAT INQUIRY</p>
<p><em>Patient/Location Inquiry</em></p></td>
</tr>
<tr class="even">
<td></td>
<td><p>PSD EMERGENCY ORDER REPORT</p>
<p><em>Unscheduled Order Report</em></p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>PSD EXP REPORT</p>
<p><em>Expiration Date Report</em></p></td>
</tr>
<tr class="even">
<td></td>
<td><p>PSD PAT ID LIST</p>
<p><em>Patient ID List Print</em></p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>PSD NURSE DELAYED DISPENSE</p>
<p><em>Delayed Sign Out Dose for Patient</em></p></td>
</tr>
<tr class="even">
<td>PSD NURSE TRANS GS MENU</td>
<td rowspan="5"></td>
<td><blockquote>
<p><em>Transfer Green Sheet Menu</em></p>
<p>Use this menu to transfer and receive Green Sheets between NAOUs.</p>
<p><strong>Menu Items:</strong></p>
<p>PSD NURSE TRANSFER GS</p>
<p><em>Transfer Green Sheet and Drug to another NAOU</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>PSD NURSE REC TRANSFER GS</p>
<p><em>Receive Green Sheet &amp; Drug from another NAOU</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PSD GS TRANS PCA/INF PATIENT</p>
<p><em>Transfer GS for PCA/Infusion Signed Out to Patient</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>PSD GS REC PCA/INF FOR PATIENT</p>
<p><em>Receive GS for PCA/Infusion Signed Out to Patient</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PSD NURSE REPRINT 2321</p>
<p><em>Reprint Transfer Between NAOUs (VA FORM 10-</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> 38 Controlled Substances V. 3.0 August 2008

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><p><em>2321)</em></p>
<p>PSD GS TRANS NOT RECD (NAOU)</p>
<p><em>Transferred Green Sheets - Pending NAOU Receipt</em></p></td>
</tr>
<tr class="even">
<td>PSD NURSE TRANSFER GS</td>
<td>PSDNTF</td>
<td><p><em>Transfer Green Sheet and Drug to another NAOU</em> This option provides nurses the ability to transfer CS drugs and their associated Green Sheet to another NAOU. The transferring of CS drugs between NAOUs requires two processing steps.</p>
<p>Step 1 - Transfer Green Sheet and Drug to another NAOU</p>
<blockquote>
<p>Step 2 - From an NAOU - Receive Green Sheet Transfer &amp; Drug</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSD NURSE WASTE</td>
<td>PSDRFW</td>
<td><p><em>Record Delayed Wastage</em></p>
<p>This option can be used when a dispensed dose needs to be wasted.</p></td>
</tr>
<tr class="even">
<td>PSD ON-HAND</td>
<td>PSDBAL</td>
<td><p><em>List On-Hand Amounts</em></p>
<p>This option lists current on-hand amounts for drugs stocked in a pharmacy-dispensing site (vault). The report is selectable by one drug, some drugs, or ALL drugs. The drugs are listed alphabetically to the user's screen or a selected printer.</p></td>
</tr>
<tr class="odd">
<td><p>PSD ON-HAND TECH</p>
<p><strong>Lock:</strong> PSD TECH</p></td>
<td>PSDBAL</td>
<td><p><em>List On-Hand Amounts</em></p>
<p>This option lists current on-hand amounts for drugs stocked in a pharmacy-dispensing site (vault). The report is selectable by one drug, some drugs, or ALL drugs. The drugs are listed alphabetically.</p></td>
</tr>
<tr class="even">
<td>PSD ORDER ENTRY</td>
<td>PSDORN</td>
<td><p><em>CS Order Entry For Ward</em></p>
<p>Use this option to electronically request CS drugs from pharmacy requiring the VA FORM 10-2638.</p></td>
</tr>
<tr class="odd">
<td>PSD OUTPATIENT</td>
<td>PSDOPT</td>
<td><p><em>Outpatient Rx's</em></p>
<p>This option provides pharmacy the ability to log outpatient prescriptions from their CS dispensing vault. The pharmacist will select an outpatient prescription and the software will display the most recently filled Rx. It will display new, refill, and partial prescriptions.</p></td>
</tr>
<tr class="even">
<td>PSD PAT ID LIST</td>
<td>PSDLBLP</td>
<td><p><em>Patient ID List Print</em></p>
<p>This option supports the printing of barcode labels for patient ID.</p></td>
</tr>
</tbody>
</table>

> April 2003 Controlled Substances V. 3.0 39

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD PAT INQUIRY</td>
<td>PSDPATI</td>
<td><p><em>Patient/Location Inquiry</em></p>
<p>This option may be used to verify the location of a patient.</p></td>
</tr>
<tr class="even">
<td>PSD PEND NAOU ORDERS</td>
<td>PSDORSN</td>
<td><p><em>Pending CS Orders Report for an NAOU</em></p>
<p>Use this option to list all pending CS orders. This report may be generated for a single drug or ALL drugs within the NAOU.</p></td>
</tr>
<tr class="odd">
<td>PSD PEND VAULT ORDERS</td>
<td>PSDORST</td>
<td><p><em>Pending CS Orders by Dispensing Site</em></p>
<p>Pharmacy uses this option to list all pending CS orders for a specific dispensing site.</p></td>
</tr>
</tbody>
</table>

> 40 Controlled Substances V. 3.0 August 2008

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSD*3*73 Technical Manual Change Pages

## \<This page is intentionally left blank.\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><p>PSD PRINT VAULT TRANSFERS</p>
<p><em>Transfer Drugs between Dispensing Sites Report</em></p>
<p>PSD PRT GS PICKED UP</p>
<p><em>GS Picked Up Awaiting Pharmacy Review</em></p>
<p>PSD INSP LOG BY RECD DATE</p>
<p><em>Inspector's Log by Rec'd Date</em></p>
<p>PSD RX DISPENSING REPORT</p>
<p><em>Rx (Prescription) Outpatient Dispensing Report</em></p>
<p>PSD DIGITALLY SIGNED ORDERS</p>
<p><em>Digitally Signed CS Orders Report</em></p>
<p>PSD DIG. SIGNED RELEASED RX</p>
<p><em>Digitally Signed OP Released Rx Report</em></p>
<p><span id="_bookmark1" class="anchor"></span>PSD CS PRESCRIPTIONS REPORT</p>
<p><em>Controlled Substance Prescriptions Report</em></p>
<p>PSD DEA SUBOXONE</p>
<p><em>DEA DATA – Waived Practitioner Report</em></p></td>
</tr>
<tr class="even">
<td>PSD PRT GS INSP HOLD</td>
<td>PSDPSI</td>
<td><p><em>Under Inspector's Review - Green Sheets</em></p>
<p>This report lists all Green Sheets placed on hold for review by a CS Inspector.</p></td>
</tr>
<tr class="odd">
<td>PSD PRT GS PICKED UP</td>
<td>PSDCPO</td>
<td><p><em>GS Picked Up Awaiting Pharmacy Review</em></p>
<p>This report lists all Green Sheets picked up by pharmacy but still awaiting a pharmacy review.</p></td>
</tr>
<tr class="even">
<td>PSD PURCHASE ORDER REVIEW</td>
<td>PSDREV</td>
<td><p><em>Purchase Order Review</em></p>
<p>Use this option to review all receipt transactions for a selected purchase order.</p></td>
</tr>
<tr class="odd">
<td>PSD PURGE</td>
<td>PSDPRG</td>
<td><p><em>Purge CS WORKSHEET File</em></p>
<p>This option purges the CS WORKSHEET file (#58.85) nightly. The CS WORKSHEET file (#58.85) is the holding area for CS order requests pending pharmacy processing. The data should remain in the file until orders have been received on an NAOU or cancelled. Once the order is received on an NAOU or cancelled, the data is purged from the file using this background job.</p>
<p>This routine should run nightly. The time to queue this option to run should not conflict with system backup.</p></td>
</tr>
<tr class="even">
<td>PSD PV INVOICE REVIEW</td>
<td>PSDREPV</td>
<td><p><em>Invoice Review (Prime Vendor)</em></p>
<p>To list all receipts that has been posted for a selected Prime Vendor invoice number.</p></td>
</tr>
<tr class="odd">
<td>PSD READY GS FOR PICKUP</td>
<td>PSDNCGS</td>
<td><p><em>Complete a Green Sheet - Ready for Pickup</em></p>
<p>Use this option to complete a CS Administration Record (VA FORM 10-2638).</p></td>
</tr>
<tr class="even">
<td>PSD REC GS</td>
<td>PSDNRGS</td>
<td><p><em>Receipt of Controlled Substance from Pharmacy</em></p>
<p>Use this option to receive CS orders with a Green Sheet (VA FORM 10-2638).</p></td>
</tr>
</tbody>
</table>

> May 2013 Controlled Substances V. 3.0 45

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD REPRINT MENU</td>
<td></td>
<td><p><em>Reprint Reports Menu</em></p>
<p>This menu allows various narcotic reports and forms to be reprinted. To ensure drug accountability, certain CS documents should only be printed once. This option allows the reprinting of these controlled records.</p>
<p><strong>Menu Items:</strong></p>
<p>PSD REPRINT 2321</p>
<p><em>Reprint Disp/Receiving Report (VA FORM 10- 2321)</em></p>
<p>PSD REPRINT 2638</p>
<p><em>Green Sheet Reprint (VA FORM 10-2638)</em></p>
<p>PSD REPRINT WORKSHEET</p>
<p><em>Dispensing Worksheet Reprint</em></p>
<p>PSD REPRINT LABEL</p>
<p><em>Label Reprint for Dispensing Drug</em></p>
<p>PSD NURSE REPRINT 2321</p>
<p><em>Reprint Transfer Between NAOUs (VA FORM 10- 2321)</em></p></td>
</tr>
<tr class="even">
<td>PSD REPRINT WORKSHEET</td>
<td>PSDRWK</td>
<td><p><em>Dispensing Worksheet Reprint</em></p>
<p>Pharmacy personnel use this option to reprint a dispensing worksheet. The previously printed dispensing worksheet, for a given dispensing site, is utilized in reprinting this listing. The sort selected during the original printing of the worksheet sequences these orders. The reprinted worksheet lists a worksheet number assigned to this order, drug, quantity ordered, dispense to location, ordered by, comments and blanks for manufacturer, lot #, and expiration date. If this order has been processed by pharmacy since the original printing, the worksheet number will display as asterisk (*). A new worksheet will not be generated during the reprinting process.</p></td>
</tr>
<tr class="odd">
<td>PSD RX DISPENSING REPORT</td>
<td>PSDOPTR</td>
<td><p><em>Rx (Prescription) Outpatient Dispensing Report</em> A report sorted by drug, prescription number, or inventory type for a date range of outpatient</p>
<p>dispensing.</p></td>
</tr>
</tbody>
</table>

> 46 Controlled Substances V. 3.0 April 2003 Technical Manual

### From: PSD*3*71 Technical Manual Change Pages

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
<td>04/2011</td>
<td><blockquote>
<p><a href="\l"><u>i,</u></a> <a href="#_bookmark2"><u>15</u>,</a> <a href="#_bookmark1"><u>41-</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*71</p>
</blockquote></td>
<td>Clarified description of PSD TECH ADV key. Corrected option name in</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><a href="#_bookmark1"><u>41c</u>,</a> <a href="#_bookmark3"><u>97-98</u></a></p>
</blockquote></td>
<td></td>
<td>PSD TRAN entry. Made revision to PSD PHARM TECH option</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>description.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/2010</td>
<td><blockquote>
<p>15, 41-41c,</p>
<p>97-98</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*69</p>
</blockquote></td>
<td>Added description of patch’s new security key PSD TECH ADV, and options from the pharmacist menu added to the Technician (CS Pharmacy) Menu [PSD PHARM TECH], which allow holders of this new key to perform these additional functions.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/08</td>
<td><blockquote>
<p>24, 37, 39,</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*64</p>
</blockquote></td>
<td>New menu options added to the Transfer Green Sheet Menu</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/03</td>
<td><blockquote>
<p>19-20,</p>
<p>44-45</p>
</blockquote></td>
<td><blockquote>
<p>PSD*3*40</p>
</blockquote></td>
<td>Added two new reports associated with the Electronic Order Entry for Schedule II Controlled Substances project to the <em>Production Repo</em>rts [PSD PRODUCTION REPORTS] menu: <em>Digitally Signed CS Orders Report</em> [PSD DIGITALLY SIGNED ORDERS] and <em>Digitally Signed OP Released Rx Report</em> [PSD DIG. SIGNED RELEASED RX].</td>
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
<p>options and routines.</p></td>
</tr>
<tr class="odd">
<td>03/97</td>
<td></td>
<td></td>
<td>Original Released Technical Manual.</td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

### Stand-Alone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All of the CS package options have been designed to stand alone. All pharmacy personnel may be assigned the *Controlled Substances Menu* \[PSD MENU\] as a menu option. Pharmacy managers may be assigned the *CS Monitoring Menu* \[PSD NM MENU\] option. All nursing personnel, using the CS software, may be assigned the *Controlled Substances Nurses’ (CS) Menu* \[PSD NURSE MENU\] as a menu option. Controlled Substances inspectors may be assigned the *Controlled Substances Inspector Menu* \[PSD INSPECTOR MENU\] option and the *CS Monitoring Menu* \[PSD NM MENU\] option. Each option utilizes the package-wide variable PSDSITE that is set as users enter the package.

> Controlled Substances [(](#_bookmark0)CS) V. 3.0 package technicians may be assigned the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\] option. They may also be assigned the PSD TECH ADV security key. With the PSD TECH ADV security key, technicians can perform the functions from the pharmacist menu that have been added to the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\]. <span id="_bookmark2" class="anchor"></span>The CS technician may perform all the *Outpatient Rx’s* menu functions except releasing a prescription.

### Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD AMIS</td>
<td>PSDAMIS</td>
<td><p><em>AMIS Report</em></p>
<p>This option provides the pharmacy with AMIS report information by NAOU.</p></td>
</tr>
<tr class="even">
<td>PSD BALANCE ADJUSTMENT REVIEW</td>
<td>PSDADJD</td>
<td><p><em>Balance Adjustment Report</em></p>
<p>This report allows the selection of drugs and a date range for which to review all balance adjustments.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD BALANCE ADJUSTMENTS <strong>Lock:</strong> PSDMGR</td>
<td>PSDADJ</td>
<td><p><em>Balance Adjustments</em></p>
<p>This option is used to review or enter adjustments needed to correct the balance of a drug. CS drugs not dispensed with a VA FORM 10-2638 returned to stock, or returned to manufacturer and held for destruction are deducted from the vault on-hand amount using this option.</p></td>
</tr>
<tr class="even">
<td>PSD BALANCE INITIALIZE</td>
<td>PSDADJI</td>
<td><p><em>Initialize Balance at Setup</em></p>
<p>This option will be used at package initialization only. It provides pharmacy a method of entering on-hand balances for CS drugs stocked within their dispensing vaults. The drugs will be listed alphabetically, displaying narcotic breakdown and package size for each. This option should be used only when the CS package is ready to be "turned on" for production use.</p></td>
</tr>
<tr class="odd">
<td>PSD COMPLETE GS</td>
<td>PSDGSRV</td>
<td><p><em>Complete Green Sheet</em></p>
<p>Pharmacy uses this option to complete a reviewed Green Sheet. Green Sheets with no discrepancies, math errors, drugs returned to stock, and drugs holding for destruction, associated with this Green Sheet, are processed utilizing this option.</p></td>
</tr>
<tr class="even">
<td>PSD CORRECT EXISTING GS</td>
<td>EN2^PSDCOR</td>
<td><p><em>Existing Green Sheets Correction</em></p>
<p>This option allows the pharmacy supervisor access to make corrective actions on CS orders. The CS software allows pharmacy to add existing Green Sheets active orders on an NAOU at package setup. These orders may be tracked using the CS software. Sometimes one of these existing Green Sheets may be incorrectly entered in the software. Using this option, the pharmacy supervisor may delete this erroneous existing Green Sheet. An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions.</p></td>
</tr>
<tr class="odd">
<td>PSD CORRECT GS STATUS</td>
<td>EN3^PSDCOR</td>
<td><p><em>Error on Completed Green Sheets</em></p>
<p>This option allows the Pharmacy Supervisor to correct the completed status of a Green Sheet from COMPLETED - REVIEWED to COMPLETED - PENDING PROBLEM</p>
<p>RESOLUTION. An entry in the CS CORRECTION LOG file (#58.87) will be created</p>
<p>to track this error.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSD PHARM TECH</td>
<td></td>
<td><p><em>Technician (CS Pharmacy) Menu</em></p>
<p>This menu provides the Pharmacy Technicians access to options associated with requesting, receiving, and processing CS orders handled by pharmacy and nursing. This menu is a combination of CS options used by both pharmacy technicians and RPhs. ![](psd-3-71-technical-manual-change-pages/002.png)<strong>Note: Some menu items are accessed by certain keys.</strong></p>
<p><strong>Menu Items:</strong></p>
<p>PSD WORKSHEET PRINT</p>
<p><em>Print CS Dispensing Worksheet</em></p>
<p>PSD WORKSHEET DISPENSING</p>
<p><em>Fill/Dispense CS Orders from Worksheet</em></p>
<p>PSD PRINT GS PICKUP</p>
<p><em>Green Sheet Ready for Pickup Log</em></p>
<p>PSD PICKUP GS</p>
<p><em>Pick Up Green Sheet</em></p>
<p>PSD ORDER ENTRY</p>
<p><em>CS Order Entry For Ward</em></p>
<p>PSD REC GS</p>
<p><em>Receipt of Controlled Substance from Pharmacy</em></p>
<p>PSD COMPLETE GS</p>
<p><em>Complete Green Sheet</em></p>
<p>PSD GS HISTORY</p>
<p><em>Green Sheet History</em></p>
<p>PSD ON-HAND TECH</p>
<p><em>List On-Hand Amounts</em></p>
<p>PSD DAILY LOG TECH</p>
<p><em>Daily Activity Log (in lieu of VA FORM 10-2320)</em></p>
<p>PSD PRINT VAULT TRANSFERS TECH</p>
<p><em>Transfer Drugs between Dispensing Sites Report</em></p>
<p>PSD RECEIPTS MENU</p>
<p><em>Receipts Into Pharmacy menu.</em></p>
<p>PSD DISPENSING MENU</p>
<p><em>Dispensing Menu</em></p>
<p>PSD DESTROY MENU</p>
<p><em>Destructions Menu</em></p>
<p>PSD MFG/LOT/EXP DATE EDIT</p>
<p><em>Manufacturer, Lot #, and Exp. Date - Enter/Edit</em></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><p>Complete Green Sheet [PSD COMPLETE GS]</p>
<p>Destroyed Drugs Report [PSD DEST DRUGS REPORT]</p>
<p>DEA Form 41 Destroyed Drugs Report [PSD DESTROY DEA41]</p>
<p>Destructions Holding Report [PSD DESTRUCTION HOLDING]</p>
<p>Add Existing Green Sheets at Setup [PSD EXISTING GS]</p>
<p>Green Sheet Transfer Between NAOUs Report [PSD GS TRANSFER (NAOU) REPORT]</p>
<p>Transfer Drugs between Dispensing Sites [PSD TRANSFER VAULT DRUGS]</p>
<p>Receipts Into Pharmacy [PSD RECEIPTS MENU] menu.</p>
<p>PSD RECEIVING</p>
<p><em>Receiving</em></p>
<p>PSD PURCHASE ORDER REVIEW</p>
<p><em>Purchase Order Review</em></p>
<p>PSD CP TRANSACTION REVIEW</p>
<p><em>Control Point Transaction Review</em></p>
<p>PSD DRUG RECEIPT HISTORY</p>
<p><em>Drug Receipt History</em></p>
<p>PSD PV INVOICE REVIEW</p>
<p><em>Invoice Review (Prime Vendor)</em></p>
<p>Dispensing Menu [PSD DISPENSING MENU] PSD WORKSHEET PRINT</p>
<p><em>Print CS Dispensing Worksheet</em></p>
<p>PSD WORKSHEET DISPENSING</p>
<p><em>Fill/Dispense CS Orders from Worksheet</em></p>
<p>PSD PRINT 2321</p>
<p><em>Dispensing/Receiving Report (VA FORM 10- 2321)</em></p>
<p>PSD PRINT 2638</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Routine</th>
<th>Menu Text / Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><p><em>Green Sheet - Print (VA FORM 10-2638)</em></p>
<p>Reprint Reports Menu [PSD REPRINT MENU]</p>
<p>PSD REPRINT 2321</p>
<p><em>Reprint Disp/Receiving Report (VA FORM 10- 2321)</em></p>
<p>PSD REPRINT 2638</p>
<p><em>Green Sheet Reprint (VA FORM 10-2638)</em></p>
<p>PSD REPRINT WORKSHEET</p>
<p><em>Dispensing Worksheet Reprint</em></p>
<p>PSD REPRINT LABEL</p>
<p><em>Label Reprint for Dispensing Drug</em></p>
<p>PSD NURSE REPRINT 2321</p>
<p><em>Reprint Transfer Between NAOUs (VA FORM 10- 2321</em></p>
<p>PSD DISPENSE W/O GS</p>
<p><em>Pharmacy Dispense without (VA FORM 10-2638)</em></p>
<p>PSD LABEL DRUG/NUMBER</p>
<p><em>Label for Dispensing (Barcode)</em></p>
<p>PSD DISPENSE TO NDES</p>
<p><em>Narcotic Dispensing Equipment Orders</em></p>
<p>Destructions Menu [PSD DESTROY MENU] PSD DEST NON-CS DRUG</p>
<p><em>Hold a CS Drug (No Inventory Update)</em></p>
<p>PSD DEST TEXT DRUG</p>
<p><em>Non-VA Drug Placed on Hold for Destruction</em></p>
<p>PSD MFG/LOT/EXP DATE EDIT</p>
<p><em>Manufacturer, Lot #, and Exp. Date - Enter/Edit</em></p>
<p>PSD OUTPATIENT</p>
<p><em>Outpatient Rx's</em></p>
<p><strong>Note: The CS technician may perform all the Outpatient Rx's menu functions except releasing a prescription.</strong></p></td>
</tr>
</tbody>
</table>

![](psd-3-71-technical-manual-change-pages/003.png)

> *(This page included for two-sided copying.)*

> PSD TECH Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* \[PSD ON- HAND TECH\], *Transfer Drugs between Dispensing Sites Report* \[PSD PRINT VAULT TRANSFERS TECH\], and

> the *Daily Activity Log (in lieu of VA FORM 10-2320)* \[PSD DAILY LOG TECH\] options on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\].

> <span id="_bookmark3" class="anchor"></span>PSD TECH ADV Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the *Receipts Into Pharmacy* \[PSD RECEIPTS MENU\], *Dispensing Menu* \[PSD DISPENSING MENU\], *Destructions Menu* \[PSD DESTROY MENU\], *Manufacturer, Lot \#, and Exp. Date - Enter/Edit* \[PSD MFG/LOT/EXP\], *Outpatient Rx's* \[PSD OUTPATIENT\], *Complete Green Sheet* \[PSD COMPLETE GS\], *Destroyed Drugs Report* \[PSD DEST DRUGS REPORT\], *DEA Form 41 Destroyed Drugs Report* \[PSD DESTROY DEA41\], *Destructions Holding Report* \[PSD DESTRUCTION HOLDING\], *Add Existing Green Sheets at Setup* \[PSD EXISTING GS\], *Green Sheet Transfer Between NAOUs Report* \[PSD GS TRANSFER (NAOU) REPORT\],

> *Transfer Drugs between Dispensing Sites* \[PSD TRANSFER VAULT DRUGS\] options on the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\]. The CS technician may perform all functions of the *Outpatient Rx’s* \[PSD OUTPATIENT\] option except releasing prescriptions.

> PSD TRAN Allocate this key only to the Inpatient Pharmacy Coordinator. This key controls the access to the *NAOU to NAOU Transfer Stock Entries* \[PSD TRANSFER NAOU\] option. Users can copy stock entries from one NAOU into another NAOU or from an Auto Replenishment/Ward Stock (AR/WS) Area Of Use (AOU) into an NAOU.

> PSJ PHARM TECH Allocate this key to pharmacy technicians handling

> controlled substances orders.

> PSJ RNURSE Allocate this key to nurses who request and receive controlled substances orders on the wards.

> PSJ RPHARM Allocate this key to pharmacists who can dispense and receive controlled substances drugs.

> Satellite Vault An NAOU set up as a secondary dispensing site.

> Stock Drug A drug (from the DRUG file (#50)) stored in an NAOU.

> Stock Level The quantity of a drug stocked in a specific NAOU.

> TRAKKER A barcode collection system utilized by scanning barcode labels or pressing the keypad.

> V*IST*A Veterans Health Information Systems and Technology Architecture

> Ward (for Drug) The name of the ward or wards that will use this particular drug. It is important to accurately answer this prompt because this is the link between the Inpatient Medications

> V. 5.0 package and the Controlled Substances V. 3.0 package. The Inpatient Medications V. 5.0 package looks at this field to know if the drug is a CS stocked drug.

### From: PSD*3*76 Technical Manual Change Pages

## ORDERED - NOT PROCESSED—

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ordered by nursing but not processed by pharmacy.

> PROCESSED - NOT DISPENSED—Processed (filled) by pharmacy but not yet dispensed.

> FILLED - NOT DELIVERED—Dispensed and verified by pharmacy but not delivered to the requesting NAOU.

> DELIVERED - ACTIVELY ON NAOU—Drug stored

> on the NAOU.

## COMPLETED - GREEN SHEET READY FOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PICKUP—Nursing has flagged the Green Sheet ready for pharmacy pickup.

## COMPLETED - GREEN SHEET PICKED UP—Green

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sheet returned to pharmacy but not yet reviewed.

> COMPLETED - REVIEWED—Pharmacy has reviewed the Green Sheet.

## COMPLETED - PENDING PROBLEM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> RESOLUTION—Pharmacy has reviewed the Green Sheet and a problem exists.

> CANCELLED—Order cancelled.

> TRANSFERRED TO ANOTHER NAOU—Order and

> drug transferred to another NAOU.

> UNDER REVIEW BY INSPECTOR—Order and drug pulled from NAOU by CS Inspector for review.

> LOGGED BY TRAKKER—All drug doses from this order have been logged out to patients using the TRAKKER.

> <span id="_bookmark0" class="anchor"></span>PSD ERROR Allocate this key to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various errors and exception conditions generated when entries are filed from the barcode TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER.

> PSD NURSE Allocate this key to nurses, usually LPNs, who may only receive and administer controlled substances drugs, but cannot place order requests.

> PSD PARAM Allocate this key to only the Inpatient Pharmacy Coordinators. This key controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site.

> 96 Controlled Substances V. 3.0 May 2013

> PSD TECH Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* \[PSD ON- HAND TECH\], *Transfer Drugs between Dispensing Sites Report* \[PSD PRINT VAULT TRANSFERS TECH\], and

> the *Daily Activity Log (in lieu of VA FORM 10-2320)* \[PSD DAILY LOG TECH\] options on the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\].

> PSD TECH ADV Allocate this key to specific control substance technicians

> who perform advance functions. This key controls access to the *Receipts Into Pharmacy* \[PSD RECEIPTS MENU\], *Dispensing Menu* \[PSD DISPENSING MENU\], *Destructions Menu* \[PSD DESTROY MENU\], *Manufacturer, Lot \#, and Exp. Date - Enter/Edit* \[PSD MFG/LOT/EXP\], *Outpatient Rx's* \[PSD OUTPATIENT\], *Complete Green Sheet* \[PSD COMPLETE GS\], *Destroyed Drugs Report* \[PSD DEST DRUGS REPORT\], *DEA Form 41 Destroyed Drugs Report* \[PSD DESTROY DEA41\], *Destructions Holding Report* \[PSD DESTRUCTION HOLDING\], *Add Existing Green Sheets at Setup* \[PSD EXISTING GS\], *Green Sheet Transfer Between NAOUs Report* \[PSD GS TRANSFER (NAOU) REPORT\],

> *Transfer Drugs between Dispensing Sites* \[PSD TRANSFER VAULT DRUGS\] options on the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\]. The CS technician may perform all functions of the *Outpatient Rx’s* \[PSD OUTPATIENT\] option except releasing prescriptions.

> PSD TRAN Allocate this key only to the Inpatient Pharmacy Coordinator. This key controls the access to the *NAOU to NAOU Transfer Stock Entries* \[PSD TRANSFER NAOU\] option. Users can copy stock entries from one NAOU into another NAOU or from an Auto Replenishment/Ward Stock (AR/WS) Area Of Use (AOU) into an NAOU.

> PSDMGR Allocate this key to the Inpatient Pharmacy Coordinators. This key controls the editing of CS files for package set up and it locks the *Supervisor (CS) Menu* option.

> PSDRPH This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement

> Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.

> PSJ PHARM TECH Allocate this key to pharmacy technicians handling

> controlled substances orders.

> PSJ RNURSE Allocate this key to nurses who request and receive controlled substances orders on the wards.

> PSJ RPHARM Allocate this key to pharmacists who can dispense and receive controlled substances drugs.

> Satellite Vault An NAOU set up as a secondary dispensing site.

> Stock Drug A drug (from the DRUG file (#50)) stored in an NAOU.

> Stock Level The quantity of a drug stocked in a specific NAOU.

> TRAKKER A barcode collection system utilized by scanning barcode labels or pressing the keypad.

> V*IST*A Veterans Health Information Systems and Technology Architecture

> Ward (for Drug) The name of the ward or wards that will use this particular drug. It is important to accurately answer this prompt because this is the link between the Inpatient Medications

> V. 5.0 package and the Controlled Substances V. 3.0 package. The Inpatient Medications V. 5.0 package looks at this field to know if the drug is a CS stocked drug.
