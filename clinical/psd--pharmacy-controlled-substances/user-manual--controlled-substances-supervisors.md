---
consolidated_title: "controlled substances supervisor's user manual"
app_code: PSD
doc_type: UM
master_source: "Controlled Substances Version 3 Supervisor's User Manual (Updated PSD*3*89)"
master_pub_date: March 1997
consolidated_from: 2 versions
prior_versions:
  - "Controlled Substances Version 3 Supervisor's User Manual (Updated PSD*3*84)"
---

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/001.png)

<span id="OLE_LINK1" class="anchor"></span>CONTROLLED SUBSTANCES (CS)

####### SUPERVISOR’S USER MANUAL

March 1997

(Revised November 2021)

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Preface](#preface)
- [Orientation](#orientation)
- [# Electronic Signature](#electronic-signature)
- [# Setting up the Controlled Substances package](#setting-up-the-controlled-substances-package)
- [# Supervisor (CS) Menu \[PSD MGR\]](#supervisor-cs-menu-psd-mgr)
  - [Set Up CS (Build Files) Menu ... \[PSD SETUP\]](#set-up-cs-build-files-menu-psd-setup)
  - [Site Parameters \[PSD SITE\]](#site-parameters-psd-site)
  - [Enter/Edit Menu ... \[PSD ENTER/EDIT MENU\]](#enteredit-menu-psd-enteredit-menu)
    - [Mark/Unmark Drugs for Controlled Substances Use \[PSD MARK\]](#markunmark-drugs-for-controlled-substances-use-psd-mark)
    - [Inventory Types - Enter/Edit \[PSD INVEN TYPE EDIT\]](#inventory-types-enteredit-psd-inven-type-edit)
    - [Enter/Edit CS Drug Location Codes \[PSD DRUG LOC EDIT\]](#enteredit-cs-drug-location-codes-psd-drug-loc-edit)
    - [Create/Edit the Narcotic Area of Use \[PSD NAOU EDIT\]](#createedit-the-narcotic-area-of-use-psd-naou-edit)
    - [Stock CS Drugs - Enter/Edit \[PSD STOCK DRUG EDIT\]](#stock-cs-drugs-enteredit-psd-stock-drug-edit)
    - [Manufacturer, Lot \#, and Exp. Date - Enter/Edit \[PSD MFG/LOT/EXP DATE EDIT \]](#manufacturer-lot-and-exp-date-enteredit-psd-mfglotexp-date-edit)
    - [Narcotic Breakdown Unit/Package Size - Enter/Edit \[PSD NARC EDIT\]](#narcotic-breakdown-unitpackage-size-enteredit-psd-narc-edit)
    - [NAOU Inventory Group - Enter/Edit \[PSD NAOU INV GROUP EDIT\]](#naou-inventory-group-enteredit-psd-naou-inv-group-edit)
  - [Ward (for Drug) Transfer \[PSD WARD CONVERSION\]](#ward-for-drug-transfer-psd-ward-conversion)
  - [Add/Delete Ward (for Drug) \[PSD WARD ADD/DEL\]](#adddelete-ward-for-drug-psd-ward-adddel)
  - [Inactivate NAOU \[PSD INACTIVATE NAOU\]](#inactivate-naou-psd-inactivate-naou)
  - [Inactivate NAOU Stock Drug \[PSD INACTIVATE NAOU STOCK DRUG\]](#inactivate-naou-stock-drug-psd-inactivate-naou-stock-drug)
  - [Transfer Stock Entries ... \[PSD TRANSFER MENU\]](#transfer-stock-entries-psd-transfer-menu)
    - [NAOU to NAOU Transfer Stock Entries \[PSD TRANSFER NAOU\]](#naou-to-naou-transfer-stock-entries-psd-transfer-naou)
    - [AOU to NAOU Transfer Entries \[PSD TRANSFER AOU\]](#aou-to-naou-transfer-entries-psd-transfer-aou)
  - [Sort NAOUs in Inventory Group \[PSD NAOU INV GROUP SORT\]](#sort-naous-in-inventory-group-psd-naou-inv-group-sort)
  - [Print CS Set Up Lists ... \[PSD PRINT SETUP LISTS\]](#print-cs-set-up-lists-psd-print-setup-lists)
    - [Drug File Stats for CS Drugs \[PSD DRUG FILE DATA\]](#drug-file-stats-for-cs-drugs-psd-drug-file-data)
    - [DEA Special Handling List \[PSD DEA LIST\]](#dea-special-handling-list-psd-dea-list)
    - [Print Inventory Types \[PSD INVEN TYPE PRINT\]](#print-inventory-types-psd-inven-type-print)
    - [List CS Drug Location Codes \[PSD DRUG LOC PRINT\]](#list-cs-drug-location-codes-psd-drug-loc-print)
    - [Show Narcotic Area of Use \[PSD NAOU PRINT\]](#show-narcotic-area-of-use-psd-naou-print)
    - [Stock Drug Print (Stock Level and Location) \[PSD STOCK PRINT\]](#stock-drug-print-stock-level-and-location-psd-stock-print)
    - [Stock Drug List (Inventory Type and Location) \[PSD STOCK LIST\]](#stock-drug-list-inventory-type-and-location-psd-stock-list)
    - [Breakdown/Dispensing Unit Report \[PSD STOCK UNIT LIST\]](#breakdowndispensing-unit-report-psd-stock-unit-list)
    - [Inventory Group List (80 column) \[PSD NAOU INV GROUP PRINT\]](#inventory-group-list-80-column-psd-naou-inv-group-print)
    - [Manufacturer and Narcotic Information Report \[PSD MFG REPORT PRINT\]](#manufacturer-and-narcotic-information-report-psd-mfg-report-print)
  - [Check Stocked Drugs for CS Use \[PSD DRUG CHECK\]](#check-stocked-drugs-for-cs-use-psd-drug-check)
  - [Initialize Balance at Setup \[PSD BALANCE INITIALIZE\]](#initialize-balance-at-setup-psd-balance-initialize)
- [# Management Reports ... \[PSD MGR REPORTS\]](#management-reports-psd-mgr-reports)
  - [Orders Filled Not Delivered \[PSD NOT DELIVERED\]](#orders-filled-not-delivered-psd-not-delivered)
  - [Pending CS Orders by Dispensing Site \[PSD PEND VAULT ORDERS\]](#pending-cs-orders-by-dispensing-site-psd-pend-vault-orders)
  - [Destructions Holding Report \[PSD DESTRUCTION HOLDING\]](#destructions-holding-report-psd-destruction-holding)
  - [DEA Form 41 Destroyed Drugs Report \[PSD DESTROY DEA41\]](#dea-form-41-destroyed-drugs-report-psd-destroy-dea41)
  - [Destroyed Drugs Report \[PSD DEST DRUGS REPORT\]](#destroyed-drugs-report-psd-dest-drugs-report)
  - [Edited Verified Orders Report \[PSD EDIT/CANC VER ORD RPT\]](#edited-verified-orders-report-psd-editcanc-ver-ord-rpt)
  - [Green Sheet Transfer Between NAOUs Report \[PSD GS TRANSFER (NAOU) REPORT\]](#green-sheet-transfer-between-naous-report-psd-gs-transfer-naou-report)
  - [Transferred Green Sheets - Pending NAOU Receipt PSD GS TRANS NOT RECD (NAOU)\]](#transferred-green-sheets-pending-naou-receipt-psd-gs-trans-not-recd-naou)
  - [Completed Green Sheet Discrepancy Report \[PSD GS DISCREPANCY REPORT\]](#completed-green-sheet-discrepancy-report-psd-gs-discrepancy-report)
  - [Correction Log Report \[PSD CORRECTION LOG REPORT\]](#correction-log-report-psd-correction-log-report)
  - [NAOU Usage Report \[PSD NAOU USAGE \]](#naou-usage-report-psd-naou-usage)
  - [AMIS Report \[PSD AMIS\]](#amis-report-psd-amis)
  - [Cost Reports \[PSD COST REPORTS\]](#cost-reports-psd-cost-reports)
  - [Listing of Green Sheet Log \[PSD GS LISTING\]](#listing-of-green-sheet-log-psd-gs-listing)
  - [Under Inspector’s Review - Green Sheets \[PSD PRT GS INSP HOLD\]](#under-inspectors-review-green-sheets-psd-prt-gs-insp-hold)
  - [Balance Adjustment Report \[PSD BALANCE ADJUSTMENT REVIEW\]](#balance-adjustment-report-psd-balance-adjustment-review)
  - [Balance Adjustments \[PSD BALANCE ADJUSTMENTS\]](#balance-adjustments-psd-balance-adjustments)
  - [Destructions Menu ... \[PSD DESTROY MENU\]](#destructions-menu-psd-destroy-menu)
    - [Hold a CS Drug (No Inventory Update) \[PSD DEST NON-CS DRUG\]](#hold-a-cs-drug-no-inventory-update-psd-dest-non-cs-drug)
    - [Non-VA Drug Placed on Hold for Destruction \[PSD DEST TEXT DRUG\]](#non-va-drug-placed-on-hold-for-destruction-psd-dest-text-drug)
    - [Destroy a Controlled Substances Drug \[PSD DESTROY DRUGS\]](#destroy-a-controlled-substances-drug-psd-destroy-drugs)
  - [Add Existing Green Sheets at Setup \[PSD EXISTING GS\]](#add-existing-green-sheets-at-setup-psd-existing-gs)
  - [Correction Menu ... \[PSD CORRECTION LOG\]](#correction-menu-psd-correction-log)
    - [Edit/Cancel Verified Orders \[PSD EDIT/CANC VER ORD\]](#editcancel-verified-orders-psd-editcanc-ver-ord)
    - [Correct Order Status - GS Ready for Pickup \[PSD CORRECT STATUS\]](#correct-order-status-gs-ready-for-pickup-psd-correct-status)
    - [Existing Green Sheets Correction \[PSD CORRECT EXISTING GS\]](#existing-green-sheets-correction-psd-correct-existing-gs)
    - [Error on Completed Green Sheets \[PSD CORRECT GS STATUS\]](#error-on-completed-green-sheets-psd-correct-gs-status)
    - [List Pending Errors/Adjustments Logged by TRAKKER \[PSD ERR/ADJ PENDING REPORT\]](#list-pending-errorsadjustments-logged-by-trakker-psd-erradj-pending-report)
    - [Enter Error/Adjustment Resolution \[PSD ERR/ADJ EDIT\]](#enter-erroradjustment-resolution-psd-erradj-edit)
    - [Print Resolved Errors/Adjustments Log \[PSD ERR/ADJ RESOLVED REPORT\]](#print-resolved-errorsadjustments-log-psd-erradj-resolved-report)
  - [Print Pharmacist ID Labels \[PSD LABEL PHARM\]](#print-pharmacist-id-labels-psd-label-pharm)
  - [Inspectors Label Print \[PSD LABEL INSP\]](#inspectors-label-print-psd-label-insp)
  - [Unscheduled Order Report \[PSD EMERGENCY ORDER REPORT\]](#unscheduled-order-report-psd-emergency-order-report)
- [Production Reports \[PSD PRODUCTION REPORTS\]](#production-reports-psd-production-reports)
  - [Pending CS Orders by Dispensing Site \[PSD PEND VAULT ORDERS\]](#pending-cs-orders-by-dispensing-site-psd-pend-vault-orders-1)
  - [Orders Filled Not Delivered \[PSD NOT DELIVERED\]](#orders-filled-not-delivered-psd-not-delivered-1)
  - [Inspector’s Log for Controlled Substances \[PSD PRINT INSPECTOR LOG\]](#inspectors-log-for-controlled-substances-psd-print-inspector-log)
  - [Inspector’s Log by Rec’d Date \[PSD INSP LOG BY RECD DATE\]](#inspectors-log-by-recd-date-psd-insp-log-by-recd-date)
  - [Stock Drug Print (Stock Level and Location) \[PSD STOCK PRINT\]](#stock-drug-print-stock-level-and-location-psd-stock-print-1)
  - [Green Sheet Ready for Pickup Log \[PSD PRINT GS PICKUP\]](#green-sheet-ready-for-pickup-log-psd-print-gs-pickup)
  - [GS Picked Up Awaiting Pharmacy Review \[PSD PRT GS PICKED UP\]](#gs-picked-up-awaiting-pharmacy-review-psd-prt-gs-picked-up)
  - [Pharmacy Dispensing Report \[PSD PRINT PHARM DISP\]](#pharmacy-dispensing-report-psd-print-pharm-disp)
  - [Daily Activity Log (in lieu of VA FORM 10-2320) \[PSD DAILY LOG\]](#daily-activity-log-in-lieu-of-va-form-10-2320-psd-daily-log)
  - [Transfer Drugs between Dispensing Sites Report \[PSD PRINT VAULT TRANSFERS\]](#transfer-drugs-between-dispensing-sites-report-psd-print-vault-transfers)
  - [Green Sheet History \[PSD GS HISTORY\]](#green-sheet-history-psd-gs-history)
  - [Expiration Date Report \[PSD EXP REPORT\]](#expiration-date-report-psd-exp-report)
  - [Inventory Sheet Print \[PSD INVEN SHEET PRT\]](#inventory-sheet-print-psd-inven-sheet-prt)
  - [List On-Hand Amounts \[PSD ON-HAND\]](#list-on-hand-amounts-psd-on-hand)
  - [Rx (Prescription) Outpatient Dispensing Report \[PSD RX DISPENSING REPORT\]](#rx-prescription-outpatient-dispensing-report-psd-rx-dispensing-report)
  - [OP CS Orders Report \[PSD DIGITALLY SIGNED ORDERS\]](#op-cs-orders-report-psd-digitally-signed-orders)
  - [OP Released Rx Report \[PSD DIG. SIGNED RELEASED RX\]](#op-released-rx-report-psd-dig-signed-released-rx)
  - [Controlled Substance Prescriptions Report \[PSD CS PRESCRIPTIONS REPORT\]](#controlled-substance-prescriptions-report-psd-cs-prescriptions-report)
  - [DEA DATA – Waived Practitioner Report \[PSD DEA SUBOXONE\]](#dea-data-waived-practitioner-report-psd-dea-suboxone)
- [Glossary](#glossary)
The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.
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
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2021</td>
<td><a href="#PSD_3_TOC">iii-v</a>, <a href="#op-released-rx-report-psd-dig.-signed-released-rx">41</a></td>
<td>PSD*3*89</td>
<td><p>Changed the Option Menu Text for two reports:</p>
<p>PSD DIGITALLY SIGNED ORDERS – OP CS Orders Report</p>
<p>PSD DIG. SIGNED RELEASED RX – OP Released Rx Report</p>
<p>Added filters to three reports to allow choosing the source of reported prescriptions – CPRS, eRx, CPRS+eRx, Written, or All.</p>
<p>PSD CS PRESCRIPTIONS REPORT</p>
<p>PSD DIGITALLY SIGNED ORDERS</p>
<p>PSD DIG. SIGNED RELEASED RX</p></td>
</tr>
<tr class="even">
<td>11/2018</td>
<td><a href="#PSD_3_84_BalanceDiscrepancyCheck"><u>15</u></a>, <a href="#PSD_3_84_DailyActivityLog"><u>37</u></a></td>
<td>PSD*3*84</td>
<td><p>Added "BALANCE DISCREPANCY CHECK" to the "WORKSHEET FOR CREATING/EDITING THE NARCOTIC AREA OF USE."</p>
<p>Updated the “Daily Activity Log (in lieu of VA FORM 10-2320)” report description and added a screenshot example.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>06/2018</td>
<td>45</td>
<td>PSD*3*82</td>
<td><p>Added NAOU Usage Report [PSD NAOU USAGE] option to the PSD TECH ADV key.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/2013</td>
<td>i, v,<br />
38, 46</td>
<td>PSD*3*73</td>
<td><p>Updated Table of Contents</p>
<p>Added new reports, Controlled Substance Prescriptions Report and DEA DATA – Waived Practitioner Report</p>
<p>Updated Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2013</td>
<td>i, ii, 44, 47-48</td>
<td>PSD*3*76</td>
<td><p>Updated Glossary with description of patch’s new security key PSDRPH</p>
<p>Updated Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>43-44</td>
<td>PSD*3*71</td>
<td><p>Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2010</td>
<td>43-44, 47</td>
<td>PSD*3*69</td>
<td><p>Added description of patch’s new security key PSD TECH ADV, and PSD TECH key.</p>
<p>Added PSD TECH ADV and PSD TECH key to index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/03</td>
<td>All</td>
<td></td>
<td><p>Updated the manual to Standards.</p>
<p>Added new <em>Digitally Signed CS Orders Report</em> [PSD DIGITALLY SIGNED ORDERS] and <em>Digitally Signed OP Released Rx Report</em> [PSD DIG. SIGNED RELEASED RX] options to the <em>Production Reports</em> [PSD PRODUCTION REPORTS] menu.</p></td>
</tr>
<tr class="odd">
<td>03/97</td>
<td></td>
<td></td>
<td>Original Released Supervisor’s User Manual.</td>
</tr>
</tbody>
</table>
(This page intentionally left blank for two-sided copying.)
Table of Contents<span id="PSD_3_TOC" class="anchor"></span>
(This page intentionally left blank for two-sided copying.)

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Controlled Substances (CS) computer software package V. 3.0 is one segment of the Veterans Health Information Systems and Technology Architecture (V*IST*A) in use at the Department of Veterans Affairs Medical Centers (VAMCs). This package provides functionality to monitor and track the receipt, inventory, and dispensing of all controlled substances. It also provides the pharmacy with the capability to define a controlled substance location and a list of controlled substances to maintain a perpetual inventory.

This package provides the capability for pharmacy personnel to receive a Controlled Substances order, automatically update the quantity on hand, and view a receipt history. Nursing personnel are provided with the ability to request orders for Controlled Substances via on-demand requests. Pharmacy may dispense controlled substances via the software automating all necessary documents (VA FORMs 10-2321 and 10-2638) to complete an order request. The software provides functionality to record Automated Management Information System (AMIS) and cost data, address returns to stock, destructions, order cancellations, transfers between locations, and log outpatient prescriptions.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

> Example: *Controlled Substance Balances Report* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them.

> Example: “Select INPATIENT SITE NAME” indicates a screen prompt.

- Responses in bold face indicate what the user is to type in.

> Example: Okay to Continue? No// YES.

- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.

> Example: Press \<Tab\> to move the cursor to the next field.

> Press \<Enter\> to select the default.

- ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/002.png)Note: Indicates especially important or helpful information.
- ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/003.png) Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.

Example: ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/004.png) The PSDMGR key is required. Please contact the Pharmacy Supervisor.

- ?, ??, ??? One, two, or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

> ^ Up Caret (arrow or a circumflex) and pressing \<Enter\> can be used to exit the current option.

# # Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In Controlled Substances, the Electronic Signature functionality will be used for identification for pharmacy personnel, nursing personnel, and narcotic inspectors.

> Identification will be used to reconfirm the identity of the user at the keyboard before proceeding with the next step in a critical process.

> In the documentation, when your Electronic Signature Code is to be entered, it is represented as XXXXXX.

> If you have not previously been issued an Electronic Signature code you can assign yourself one at any menu option by entering TBOX and then choosing Edit Electronic Signature Code. You can also enter “EDIT E and follow the prompts as shown on the next page.

> Electronic Signature Codes

> This option is designed to permit you to enter or change your

> Initials, Signature Block Information and Office Phone number.

> In addition, you are permitted to enter a new Electronic Signature Code

> or to change an existing code.

> INITIAL: OAC

> SIGNATURE BLOCK PRINTED NAME: ONE A CSNURSE

> SIGNATURE BLOCK TITLE: R.N.

> OFFICE PHONE: 555-7101

> ENTER NEW SIGNATURE CODE: XXXXXX(Signature Code will not appear on screen)

> RE-ENTER SIGNATURE CODE FOR VERIFICATION: XXXXXX

> DONE

(This page intentionally left blank for two-sided copying.)

# # Setting up the Controlled Substances package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 33%" />
<col style="width: 22%" />
<col style="width: 19%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>STEP</th>
<th>STEP DESCRIPTION</th>
<th>MENU PATH</th>
<th>OPTION</th>
<th>PAGE(S)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>The initial installation of this package will mark entries in your DRUG file based on the DEA, SPECIAL HANDLING field. Print the DEA Special Handling List and compare it to the drugs currently tracked on your 2320s to see if you need to mark or unmark any drugs. If not, go to step 3.</td>
<td><p>Controlled Substances Menu:</p>
<p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p>
<p>Print CS Set Up Lists Option:</p></td>
<td>DEA Special Handling List</td>
<td>22</td>
</tr>
<tr class="even">
<td>2</td>
<td>For a drug to be added to a Vault or Narcotic Area of Use (NAOU), it must be marked for Controlled Substances use.</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p>
<p>Enter/Edit Menu:</p></td>
<td>Mark/Unmark Drugs for Controlled Substances Use</td>
<td>11</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Identify which Inpatient Site(s) should be selectable for Controlled Substances.</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p></td>
<td>Site Parameters (requires PSD PARAM security key)</td>
<td>11</td>
</tr>
<tr class="even">
<td>4</td>
<td>Decide how many Master and Satellite vault(s) you will need and then create them. Worksheet on page 15.</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p></td>
<td><p>Create/Edit the Narcotic Area of Use</p>
<p>(NAOU)</p></td>
<td>14</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Define your NAOU Inventory types and descriptions.</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p>
<p>Enter/Edit Menu:</p></td>
<td>Inventory Types-Enter/Edit</td>
<td>11</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 31%" />
<col style="width: 22%" />
<col style="width: 19%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>STEP</th>
<th>STEP DESCRIPTION</th>
<th>MENU PATH</th>
<th>OPTION</th>
<th>PAGE(S)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>6</td>
<td>Enter your drug location codes</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build files) Menu:</p>
<p>Enter/Edit Menu:</p></td>
<td><p>Enter/Edit CS Drug Location</p>
<p>Codes</p></td>
<td>12</td>
</tr>
<tr class="even">
<td>7</td>
<td>Enter the drugs that are stocked in your Master Vault(s). A worksheet is available on page 15</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p>
<p>Enter/Edit Menu:</p></td>
<td>Stock CS Drugs-Enter/Edit</td>
<td>10</td>
</tr>
<tr class="odd">
<td>8</td>
<td>Create your NAOUs. A worksheet is available on page 13.</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p>
<p>Enter/Edit Menu:</p></td>
<td>Create/Edit the Narcotic Area of Use</td>
<td>14</td>
</tr>
<tr class="even">
<td>9</td>
<td>Enter the drugs that are stocked by a typical NAOU into an NAOU to be used as a pattern. A worksheet is available on page 15.</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p>
<p>Enter/Edit Menu:</p></td>
<td>Stock CS Drugs-Enter/Edit</td>
<td>16</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Transfer stock entries from your pattern NAOU to your other NAOUs.</td>
<td><p>Supervisor (CS) Menu:</p>
<p>Set Up CS</p>
<p>(Build Files) Menu:</p>
<p>Transfer Stock Entries Menu:</p></td>
<td><p>NAOU to NAOU Transfer Stock Entries</p>
<p>(This requires that PSD TRAN security key)</p></td>
<td>20</td>
</tr>
<tr class="even">
<td>11</td>
<td>Add existing green sheets.</td>
<td>Supervisor (CS) Menu:</td>
<td>Add Existing Green Sheets at Setup</td>
<td>30</td>
</tr>
<tr class="odd">
<td>12</td>
<td>If you do not wish to use a bar code tracker to inventory your vault(s), proceed to step 13. Otherwise, print pharmacist ID labels.</td>
<td>Supervisor (CS) Menu:</td>
<td><p>Print Pharmacist ID Labels</p>
<p>(This requires the PSDMGR security key)</p></td>
<td>32</td>
</tr>
<tr class="even">
<td>13</td>
<td>Initialize balances in vault by using the 2320 or use inventory sheet. You may want to enter high on hand quantities while you bring up NAOUs a few at a time and then follow with balance adjustments for the vault when all NAOUs are active.</td>
<td>Supervisor’s (CS) Menu:</td>
<td>Initialize Balance at Setup</td>
<td>24</td>
</tr>
</tbody>
</table>

(This page intentionally left blank for two-sided copying.)

# # Supervisor (CS) Menu \[PSD MGR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option supports activities to build and maintain the files needed to operate the Controlled Substances module of the Pharmacy software.

The *Supervisor (CS) Menu* option is locked with the PSDMGR key and assigned to the pharmacy supervisor(s) maintaining the narcotic vaults.

## Set Up CS (Build Files) Menu ... \[PSD SETUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Set Up CS (Build Files) Menu* supports the management of files used during the initial set up of the Controlled Substances module. It includes the creating, editing, and listing of data in the CS files. Be forewarned that it takes a considerable amount of time and effort to set up this module. Numerous worksheets and diagrams are provided throughout the manual to assist you in this task.

> The diagram on the following page points out the interrelationships of the Controlled Substances files.

> First the Narcotic Area of Use (NAOU) Inventory Types, displayed by AOU INVENTORY TYPE file (58.16), should be defined.

> Second the NAOU Drug Location Address Codes, represented in the AOU ITEM LOCATION file (#58.17), should be defined.

> The DRUG ACCOUNTABILITY STATS file (#58.8) and the DRUG ACCOUNTABILITY TRANSACTION file (#58.81) contain inventory levels and a history of narcotic orders. These entries located within these files are pointed to by other files. Several fields within these files are linked to other files; Drug points to the generic drug name from the DRUG file (#50); Inpatient Site points to the INPATIENT SITE file (#59.4) and the Primary Dispensing Site represents a Master or Satellite Vault maintained within the DRUG ACCOUNTABILITY STAS file (#58.8).

![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/005.png)

## Site Parameters \[PSD SITE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This includes selecting an inpatient site for Controlled Substances use and answering package specific questions concerning this site. This option is locked with the PSD PARAM key and is only given to the Pharmacy Package Coordinators using the CS software.

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/006.png) Note: If you wish to change the inpatient site that you selected simply return to this option and answer NO to remove the site for selection.

## Enter/Edit Menu ... \[PSD ENTER/EDIT MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu contains the enter/edit options associated with setting up the files for the Controlled Substances module.

### Mark/Unmark Drugs for Controlled Substances Use \[PSD MARK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to mark/unmark entries in the DRUG file (#50) for use with the Controlled Substances package. Every drug stocked within a Narcotic Area of Use MUST be marked for CS use.

### Inventory Types - Enter/Edit \[PSD INVEN TYPE EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will enter and edit the entries in the AOU INVENTORY TYPE file (#58.16) used to classify Narcotic Area of Use drugs. The information must be filled in here before you can edit any other files due to the fact that other files refer to these entries.

> Each NAOU can define their own type of Inventory. These can be as broad or narrow as needed. You might want to have inventory types such as oral solids, oral liquids, and solution sets. You also might want to break it down further and inventory scheduled narcotics separately from each other, or even create multiple inventory types (e.g., Schedule II Narcotics and Schedule V Narcotics).

> All of the inventory types are defined by the ward with one exception. The inventory type ALL should be a defined type in your existing AOU INVENTORY TYPE file. ALL is used when you wish to inventory all types on the same inventory sheet. Enter the name as ALL, with a description of Used to select all types.

### Enter/Edit CS Drug Location Codes \[PSD DRUG LOC EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to enter and edit the data for the location codes. These location codes identify the specific location of a drug in an NAOU or in the pharmacy. Up to three levels of coding are possible. For example, you could use the Medicine Room, Cabinet A, and Shelf 2 as the location area for one drug.

> The following are examples of drug address codes and code expansions that a site might use.

> <u>DRUG ADDRESS CODE</u> <u>CODE EXPANSION</u>

> MC1 Medicine Cabinet 1

> MC2 Medicine Cabinet 2

> CUR Clean Utility Room

> D1 Drawer 1

> D2 Drawer 2

> B1 Bin 1

> B2 Bin 2

> MR Medicine Room

> NC Narcotics Cabinet

> RA Rack A

> RB Rack B

> REF Refrigerator

> S1 Shelf 1

> S2 Shelf 2

> When implementing the Controlled Substances package, consider how to establish uniformity and consistency within all Narcotic Areas of Use, when possible. Determine a consistent way to code the locations and organize the Areas (e.g., always number or letter from left to right, top to bottom, or some other consistent fashion). This will help new employees locate drugs easier and check another employees’ NAOUs during times of leave.

> The following diagram illustrates how the drug address codes and expansions might be applied to a prototype NAOU. When drug address codes have been entered, a printout of the data can be made by using the List CS Drug Location Codes option.

  
DRUG ADDRESS CODE/EXPANSION

![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/007.png)

### Create/Edit the Narcotic Area of Use \[PSD NAOU EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A Narcotic Area of Use (NAOU) is a place where commonly stocked drugs are stored for use by pharmacy, wards, or treatment areas. An NAOU can serve one or more wards or clinics. The purpose of this option is to create or edit the Narcotic Areas of Use.

> If you want to create an NAOU under a different Inpatient Site that the one you chose when you signed-on, you must log off the computer and sign back on and select the new Inpatient Site.

> Your Vaults should be created in the following order:

> \(1\) Master Vault: This will be your primary dispensing vault for pharmacy.

> \(2\) Satellite Vault: If it is needed create it next. This will be the secondary dispensing vault for pharmacy.

> \(3\) Narcotic location: An NAOU set up for the nursing wards, pharmacy IV room, or a pharmacy working stock area.

> To set up File 58.8, DRUG ACCOUNTABILITY STATS file, data must be entered into the following fields using the *Create/Edit the Narcotic Area of Use* option:

> “Select NAOU:”

> Enter the name of the Narcotic Area of Use. This can represent a pharmacy narcotic vault, a pharmacy working stock area, a ward, a combination of wards, or, as in the case of cardiac cath lab, no ward.

> “LOCATION TYPE:”

> There are three types of Narcotic Areas of Use: 1) MASTER VAULT, 2) SATELLITE VAULT, and 3) NARCOTIC LOCATIONS. At this prompt you will answer M for Master vault, S for Satellite vault, or N for Narcotic location. Once an NAOU has been stocked with drugs, the location type cannot be changed, you can however transfer the information from a satellite vault to a master vault.

<u>  
WORKSHEET FOR CREATING/EDITING</u><u>THE NARCOTIC AREA OF USE</u>

<u>NAOU NAME:</u>

<u>Location Type:</u>

<u>? PRIMARY DISPENSING SITE:</u>

<u>† ASK MFG/LOT#/EXP. DATE?:</u>

<u>† AUTO GENERATE DISPENSING \#’S?:</u>

<u>\* LOW DISPENSING \#:</u>

<u>\* HIGH DISPENSING \#:</u>

<u>\* LAST DISPENSING \#:</u>

<u>†PRINT GREEN SHEET:</u>

<u>†GREEN SHEET STOCK:</u>

<u>† DISPENSING WORKSHEET SORT:</u>

<u>† DEFAULT GREEN SHEET PRINTER:</u>

<u>† DEFAULT REPORT PRINTER:</u>

<u>† DEFAULT LABEL PRINTER:</u>

<u>† PRIME VENDOR?:</u>

<u>† CURRENT PRIME VENDOR PO#:</u>

<span id="PSD_3_84_BalanceDiscrepancyCheck" class="anchor"></span><u>◊ BALANCE DISCREPANCY CHECK:</u>

<u>•USING PERPETUAL INVENTORY?:</u>

<u>•Is this a Pharmacy NAOU for Working Stock?:</u>

<u>NAOU NAME:</u>

<u>Location Type:</u>

<u>? PRIMARY DISPENSING SITE:</u>

<u>† ASK MFG/LOT#/EXP. DATE?:</u>

<u>† AUTO GENERATE DISPENSING \#’S?:</u>

<u>\* LOW DISPENSING \#:</u>

<u>\* HIGH DISPENSING \#:</u>

<u>\* LAST DISPENSING \#:</u>

<u>†PRINT GREEN SHEET:</u>

<u>†GREEN SHEET STOCK:</u>

<u>† DISPENSING WORKSHEET SORT:</u>

<u>† DEFAULT GREEN SHEET PRINTER:</u>

<u>† DEFAULT REPORT PRINTER:</u>

<u>† DEFAULT LABEL PRINTER:</u>

<u>† PRIME VENDOR?:</u>

<u>† CURRENT PRIME VENDOR PO#:</u>

<u>◊ BALANCE DISCREPANCY CHECK:</u>

<u>•USING PERPETUAL INVENTORY?:</u>

<u>•Is this a Pharmacy NAOU for Working Stock?:</u>

◊ = Will only appear if you are editing or creating a Master vault.

† = Will only appear if you are creating a Master or Satellite vault.

\* = Will only appear if you answered yes to AUTO GENERATE DISPENSING \#’S?

• = Will only appear if you are entering for a Narcotic location.

? = Will only appear if you are entering a Satellite vault or Narcotic location.

### Stock CS Drugs - Enter/Edit \[PSD STOCK DRUG EDIT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Using this option, you may enter or edit the list of drugs to be stocked in the Narcotic Area of Use; however, duplicate entries in this list will not be allowed. This is the most time-consuming part of setting up the package. For your pharmacy vaults, you should begin by entering all drugs that will be dispensed from that Narcotic Area of Use. For the narcotic locations, you may wish to begin by entering all drugs that Nursing is accustomed to stocking for the NAOU. A worksheet for creating Stock CS Drugs is located on the following page.

> The “Expiration Date:” prompt will accept prior years.

<u>  
PHARMACY NAOU STOCK FILE WORKSHEET</u>

Make copies of this worksheet to help determine inventory to be stocked in each NAOU. For each NAOU, list all drugs to be stocked.

<u>NAOU:</u>

> <u>Drug:</u>

> <u>Location:</u>

> <u> Ward (FOR Drug):</u>

> <u>Type:</u>

> <u>Stock Level:</u>

> <u>REORDER LEVEL:</u>

> <u>QUANTITY TO REORDER:</u>

> <u>\* BREAKDOWN UNIT:</u>

> <u>\* PACKAGE SIZE:</u>

> <u>† MAXIMUM QUANTITY PER ORDER:</u>

> <u>• MANUFACTURER:</u>

> <u>• LOT \#:</u>

> <u>• EXPIRATION DATE:</u>

<u>NAOU:</u>

> <u>Drug:</u>

> <u>Location:</u>

> <u> Ward (FOR Drug):</u>

> <u>Type:</u>

> <u>Stock Level:</u>

> <u>REORDER LEVEL:</u>

> <u>QUANTITY TO REORDER:</u>

> <u>\* BREAKDOWN UNIT:</u>

> <u>\* PACKAGE SIZE:</u>

> <u>† MAXIMUM QUANTITY PER ORDER:</u>

> <u>• MANUFACTURER:</u>

> <u>• LOT \#:</u>

> <u>• EXPIRATION DATE:</u>

\* = Are required to be answered by the dispensing site.

• = Are optional when entering a Narcotic Location.

† = Only asked for Master or Satellite vault.

 = Will only be asked when entering a Narcotic Location (NAOU).

### Manufacturer, Lot \#, and Exp. Date - Enter/Edit \[PSD MFG/LOT/EXP DATE EDIT \]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to edit the Manufacturer, Lot \#, and Expiration date for stocked drugs in the DRUG ACCOUNTABILITY STATS file. The drug must first have been added through the *Stock CS Drugs-Enter/Edit* option. This field, when defined, will print on the Pharmacy Dispensing Report and displayed on the request order to pharmacy.

### Narcotic Breakdown Unit/Package Size - Enter/Edit \[PSD NARC EDIT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> By using this option the user can enter or edit narcotic breakdown unit and narcotic package size for stocked drugs in an active NAOU. The breakdown unit for a bottle of 50 Tylox would be capsule and the package size would be 50. The breakdown unit for a box of 10 vials of Morphine would be vials, and the package size would be 10. If you were dispensing liquids in ML, then the breakdown unit would be ML. If you dispense by bottle, then bottle would be the breakdown unit. Package size would depend on whether the breakdown unit was ML or bottle.

### NAOU Inventory Group - Enter/Edit \[PSD NAOU INV GROUP EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An NAOU Inventory Group is defined by pharmacy to represent the Narcotic Areas of Uses which can be inventoried together as a group. By grouping the commonly inventoried NAOUs under an easy to remember group name, the elements of the inventory are established and do not have to be redefined every time the inventory is scheduled.

> NAOU Inventory Groups may be established to reflect different variations at the VAMC, grouped as the following examples, on any combination of these:

> \(1\) location (i.e., Emergency Room, clinic, or ward)

> \(2\) time—when the inventory takes place ( i.e., Monday Day Shift,

> M-W-F/Evenings)

> \(3\) category or types of drug to be inventoried (i.e., IV solutions & sets, bulk narcotics, or Schedule II)

> You will be able to continue to select NAOUs. If you choose only one NAOU continue to press the enter key until you reach the main menu.

> You can printout the data entered for your NAOU Inventory Groups by using the *Inventory Group List* option.

## Ward (for Drug) Transfer \[PSD WARD CONVERSION\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow the mass conversion for all drugs in a single NAOU, several NAOUs, or ^ALL NAOUs to be transferred from an old ward to a new ward. This capability was designed especially for situations such as the closing of a Ward for construction.

> If you answer yes to queuing the transfer, you will be able to request the time you wish the transfer to occur and will then be notified by MailMan when the job is completed; if no, the computer will flash a message at that time confirming the transfer.

## Add/Delete Ward (for Drug) \[PSD WARD ADD/DEL\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow a user to add or delete a ward (for drug) assignment for all stock drugs in one or more active NAOUs.

## Inactivate NAOU \[PSD INACTIVATE NAOU\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Inactive NAOUs will be excluded from Stock Drug Listings and other reports that are done on all NAOUs. An inactive NAOU will however be included on reports covering a period of time when the NAOU was still active.

> Order entry requests will not be permitted for inactive NAOUs, however, editing drug data such as manufacturer, lot number, expiration date for all NAOUs, and narcotic packaging information for vaults will be allowed. Under these circumstances, the NAOU name will be displayed with an “\*\*INACTIVE\*\*” flag.

> NAOUs are inactivated by entering a date that can be past, present, or future and are reactivated by deleting the inactivation date.

> If you inactivate all stocked drugs within an NAOU, the drugs must be reentered in one at a time to be reactivated.

## Inactivate NAOU Stock Drug \[PSD INACTIVATE NAOU STOCK DRUG\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to inactivate a drug that is currently stocked in an NAOU. Drugs should not be deleted, but simply made inactive. Inactivated drugs will not be included on the inventory sheet or on the NAOU stock list.

> When you want to reactivate an inactivated drug, you must use this option to delete the inactivation date therefore making it active again.

## Transfer Stock Entries ... \[PSD TRANSFER MENU\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is locked with the PSD TRAN key, and only the pharmacy supervisor(s) who maintain the narcotic vaults should be assigned this key.

> The ability to “copy” stock entries is useful in at least three cases. First, for stations setting up CS (Build Files) initially, you could establish a Generic NAOU with standard drugs which will be stocked by all NAOUs. Using this transfer option, the drugs could then be copied into all areas. You would have to edit each drug in each NAOU to enter the stock level, type, ward (for drug), and location.

> A second application might be for the creation of crash carts or after-hours dispensing machines with identical stock drugs, stock levels, and location codes. After an NAOU has been created, the transfer option could be used to clone all others.

> A third use for this option would be for adding new drugs to a number of NAOUs. For example, if drugs recently approved by the FDA have been added to your formulary, you could add this drug (or group of drugs) to a selected group of Narcotic Areas of Use.

### NAOU to NAOU Transfer Stock Entries \[PSD TRANSFER NAOU\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will “copy” the active stock entries from a selected Narcotic Area of Use into one or more selected NAOUs. As many as 10 NAOUs may be chosen for transfer at one time. You may transfer either drug name only, drug name/stock level/and location code, or drug name/stock level, location code, and inventory types. The copy process will not copy inactive drugs or duplicate entries. Thus, if an NAOU already contains Acetaminophen w/codeine 30MG TAB, and that item is in the Master NAOU, the drug will not be duplicated. The actual transfer takes place in a background job which is automatically queued. When the transfer is complete, you will be notified by a MailMan message.

### AOU to NAOU Transfer Entries \[PSD TRANSFER AOU\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will “copy” the active stock entries from a selected AR/WS Area of Use into one or more selected Controlled Substances Narcotic Areas of Use. As many as 10 NAOUs may be chosen for transfer at one time. You may transfer either the drug name only, the drug name/stock level/location code, or drug name/stock level/location code/and inventory types. The copy process will not copy inactive drugs or duplicate entries. Thus, if an NAOU already contains Acetaminophen w/codeine 30MG TAB, and that item is in the Master NAOU, the drug will not be duplicated. The actual transfer takes place in a background job which is queued automatically. When the transfer is complete, you will be notified by a MailMan message.

## Sort NAOUs in Inventory Group \[PSD NAOU INV GROUP SORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the user to change the order in which the NAOUs will sort within an inventory group. NAOUs should sort in the order that they will be visited but VA FileMan puts them in the order in which they were defined.

## Print CS Set Up Lists ... \[PSD PRINT SETUP LISTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option contains all reports or lists associated with setting up the files for the Controlled Substances module.

### Drug File Stats for CS Drugs \[PSD DRUG FILE DATA\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All drugs marked for CS package use will print on this report and the data may be used when loading stock drugs into an NAOU.

> Only the active Controlled Substances drugs will print.

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/008.png) Note: The AMIS and cost reports depend on accurate dispense unit and price per dispense unit information.

### DEA Special Handling List \[PSD DEA LIST\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report alphabetically lists the drug name, DEA Special Handling, and NDC data for all drugs within the DRUG file marked for Controlled Substances package use. This report will be helpful in researching drugs incorrectly marked for CS package use.

### Print Inventory Types \[PSD INVEN TYPE PRINT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print the list of inventory types and type descriptions defined in File 58.16-AOU INVENTORY TYPE file. These types are used to classify the items in an NAOU for inventory purposes.

### List CS Drug Location Codes \[PSD DRUG LOC PRINT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report will list the codes and code extensions used to define the location of drugs stocked in Narcotic Areas of Use or in the pharmacy.

### Show Narcotic Area of Use \[PSD NAOU PRINT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the user to print the NAOUs, Location Type, and Primary Dispensing Site created in the *Create/Edit the Narcotic Area of Use* option.

### Stock Drug Print (Stock Level and Location) \[PSD STOCK PRINT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report prints an alphabetic listing of all active drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This report lists NAOU, drug name, location, stock levels, all ward (for drug) assignments, and all inventory types.

### Stock Drug List (Inventory Type and Location) \[PSD STOCK LIST\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all active stocked drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This report can be sorted alphabetically or by inventory type/location/drug. The data includes NAOU, location, drug name, stock level, and reorder level. The report sorted by inventory type/location/drug will include the type as printed data. The report can be printed for a single, several, or all NAOUs.

### Breakdown/Dispensing Unit Report \[PSD STOCK UNIT LIST\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides an alphabetic listing of all active drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This listing includes breakdown unit, package size, dispense unit, and price per dispense unit.

### Inventory Group List (80 column) \[PSD NAOU INV GROUP PRINT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option prints a list of the currently defined NAOU inventory groups with their associated inventory types.

### Manufacturer and Narcotic Information Report \[PSD MFG REPORT PRINT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report prints an alphabetical listing of all ACTIVE drugs within an ACTIVE NAOU. This report lists NAOU, drug name, manufacturer, lot \#, expiration date, narcotic breakdown unit, and narcotic package size. This report may be sorted alphabetically by NAOU, then drug name or drug name, then NAOU. The user may select one, several, or all NAOUs to print.

## Check Stocked Drugs for CS Use \[PSD DRUG CHECK\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option queues a background job to check all ACTIVE drugs stocked, within an ACTIVE NAOU, for use with the Controlled Substances package. If a stocked drug has been unmarked for CS use the drug will then be inactivated. At job completion a MailMan message will be sent listing any drug discrepancies.

## Initialize Balance at Setup \[PSD BALANCE INITIALIZE\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will be used at package initialization only. It provides pharmacy a method of entering on-hand balances for Controlled Substances drugs stocked within their dispensing vaults. The drugs will be listed alphabetically, displaying narcotic breakdown and package size for each. This option should be used only when the Controlled Substances package is ready to be “turned on” for production use.

# # Management Reports ... \[PSD MGR REPORTS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option contains all reports or lists associated with drug accountability for narcotics.

## Orders Filled Not Delivered \[PSD NOT DELIVERED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates a list of all Controlled Substances orders filled from the pharmacy dispensing site (vault) but not yet delivered to the NAOUs. A summary total sorted by drug is also generated.

## Pending CS Orders by Dispensing Site \[PSD PEND VAULT ORDERS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pharmacy uses this option to list all pending Controlled Substances orders for a specific dispensing site.

## Destructions Holding Report \[PSD DESTRUCTION HOLDING\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a report that will only list the drugs that have been previously marked for destruction.

> DO NOT PRINT THIS REPORT IF YOU HAVE NOT PREVIOUSLY MARKED THE DRUGS.

> If you have not previously marked the drugs, the following information will help you determine which step you need to do before this report can be run. Each step will create a VA FORM 10-2321 Narcotic Dispensing/Receiving Report. When you have completed the step of your choice return to this option and print your report.

> 1\. If you have a Green Sheet number, you will need to go to the Pharmacist Menu and select the *Complete Green Sheet* option. Enter the completion status as Turned in for destruction. The system will assign a destruction holding number.

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/009.png) Note: The *Complete Green Sheet* option updates the Green Sheet status to Complete - Reviewed Turned in for destruction, the nursing records, the transaction history, and the DESTRUCTION file.

> 2\. If you do not have a Green Sheet number, you will need to go to the Supervisor (CS) Menu and select the *Balance Adjustments* option. After answering the prompts the system will assign a destruction holding number.

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/010.png) Note: The Balance Adjustments option updates the monthly adjustments, the transaction history, and the DESTRUCTION file. These drugs are actively stocked in the vault inventory.

> 3\. If you don’t know if the drug is stocked in vault, you will need to go to the *Supervisor (CS) Menu*, then the *Destructions Menu* and select the *Hold a CS Drug (No Inventory Update)* option. After answering the prompts the system will assign a destruction holding number for the drug name entered.

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/011.png) Note: The *Hold a CS Drug (No Inventory Update)* option does not update your inventory balances, it only creates an entry in the DESTRUCTIONS file. DRUG file (#50) is searched for the drug name entered.

> 4\. If the Drug is Non-VA issue (not in DRUG file), you will need to go to the *Supervisor (CS) Menu*, then the *Destructions Menu* and select the *Non-VA Drug Placed On Hold For Destruction* option. At the “DRUG ITEM” prompt you can enter information in a free text form. After answering the prompts the system will assign a destruction holding number.

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/012.png) Note: The *Non-VA Drug Placed on Hold for Destruction* does not update your inventory balances because the drug is not in the DRUG file.

## DEA Form 41 Destroyed Drugs Report \[PSD DESTROY DEA41\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists information on destroyed Controlled Substances that is required in completing the DEA FORM 41.

## Destroyed Drugs Report \[PSD DEST DRUGS REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists alphabetically by drug all destroyed controlled substances within a narcotic dispensing site, for a given period of time. Pharmacy supervisor certifying the destruction, quantity destroyed, and date destroyed are also included on this report. The report may be generated for a single drug, several drugs, or ALL drugs stocked within a specific dispensing site.

## Edited Verified Orders Report \[PSD EDIT/CANC VER ORD RPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all verified orders that have been edited or cancelled within a specified date range. Data listed includes pharmacy dispensing \# (Green Sheet \#), date edited, drug, type of action (edited or cancelled), original quantity, new quantity, and name of the pharmacist. The manufacturer, lot \#, or expiration date fields will also be listed if edited.

## Green Sheet Transfer Between NAOUs Report \[PSD GS TRANSFER (NAOU) REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all Green Sheets transferred and received between NAOUs for a given date range. This report may be printed for a single NAOU, several NAOUs, or ALL NAOUs.

## Transferred Green Sheets - Pending NAOU Receipt PSD GS TRANS NOT RECD (NAOU)\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all Green Sheets that have been transferred from an NAOU and are pending receipt in another NAOU.

## Completed Green Sheet Discrepancy Report \[PSD GS DISCREPANCY REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all Green Sheets with a completion status of MATH ERROR, GREEN SHEET NOT SIGNED BY NURSE, or OTHER - REFERRED TO SUPERVISOR. This report may be printed for a single NAOU, several NAOUs, or ALL NAOUs.

## Correction Log Report \[PSD CORRECTION LOG REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all corrective actions logged for a Green Sheet for a selected date range. This report may be generated by order status changes or by Green Sheet deletions.

## NAOU Usage Report \[PSD NAOU USAGE \]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report will print an NAOU drug usage report for a selected date range. The report may be sorted by drug (one, some, or ALL) or by NAOU (one, some, or ALL). A detailed list of orders, including the pharmacy dispensing \# (Green Sheet \#), date filled, quantity, and who ordered the drug will be printed. Summary totals by order and quantity are also generated.

## AMIS Report \[PSD AMIS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides the pharmacy with AMIS report information by NAOU.

## Cost Reports \[PSD COST REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides pharmacy with the cost reporting data for Controlled Substances drugs, by NAOU, for a specified date range.

## Listing of Green Sheet Log \[PSD GS LISTING\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option numerically lists all Green Sheets for a given date range or for a given Green Sheet number range. The logs list Green Sheet number, date dispensed, and current status.

## Under Inspector’s Review - Green Sheets \[PSD PRT GS INSP HOLD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all Green Sheets placed on hold for review by a Controlled Substances Inspector.

## Balance Adjustment Report \[PSD BALANCE ADJUSTMENT REVIEW\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this report to review adjustments that corrected the balance of a drug. Controlled Substances drugs that are deducted from the vaults on-hand balances using this option are drugs not dispensed with a VA FORM 10-3638, drugs that have been returned to stock, drugs returned to the manufacturer, or drugs on hold for destruction.

## Balance Adjustments \[PSD BALANCE ADJUSTMENTS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to review or enter adjustments needed to correct the on-hand balance of a drug. Controlled Substances drugs not dispensed with a VA FORM 10-2638 returned to stock or returned to manufacturer and held for destruction are deducted from the vault on-hand amount using this option.

> The numbers that appear in parenthesis at the “Enter adjustment quantity” prompt will start with a negative number (this is your current on-hand amount) and is the number that you cannot exceed if you choose to subtract an amount. The next number 999999, this is the highest amount that you can add to the current on-hand amount. These two numbers are separated by a hyphen.

> You will also be asked to give your Signature Code when using this option.

> Example:

> Select Supervisor (CS) Menu Option: BALAnce Adjustments

> Review? No// \<ENTER\> NO

> Select Dispensing Site: MAST VAU// \<ENTER\>

> Enter your Current Signature Code: XXXXXX SIGNATURE VERIFIED

> Select MAST VAU drug: DIAZEPAM 5MG TAB

> Current Balance: 1525 Breakdown Unit: TAB

> Enter adjustment quantity (with '-' if negative): (-1525-999999): -87

> Please enter reason for adjustment: ENTERED WRONG AMOUNT

> OK to post? Yes// \<ENTER\> YES

> There were 1525 on hand. There are now 1438 on hand.

> Updating monthly adjustments and transaction history.

> To be destroyed? No// \<ENTER\> NO

> Select MAST VAU drug:\<ENTER\>

## Destructions Menu ... \[PSD DESTROY MENU\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu allows pharmacy supervisors to maintain the necessary records when destroying a Controlled Substances drug.

### Hold a CS Drug (No Inventory Update) \[PSD DEST NON-CS DRUG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows pharmacy supervisors to place a Controlled Substances VA drug, from the DRUG file (#50), on hold for destruction. When using this option, the Controlled Substances inventory balance will not be updated. A CS DESTRUCTION file (#58.86) entry is now able to be traced through the CS software.

### Non-VA Drug Placed on Hold for Destruction \[PSD DEST TEXT DRUG\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the pharmacy supervisors to place a non-VA drug, not existing in the DRUG file (#50), on hold for destruction. A CS DESTRUCTION file (#58.86) entry is made and is now able to be traced through the CS software.

### Destroy a Controlled Substances Drug \[PSD DESTROY DRUGS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides the supervisor with the ability to enter the destruction information for any Controlled Substances drug being destroyed.

## Add Existing Green Sheets at Setup \[PSD EXISTING GS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides pharmacy the ability to enter existing Green Sheets and active orders on an NAOU, at package setup. These orders may be tracked through the Controlled Substances software.

## Correction Menu ... \[PSD CORRECTION LOG\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu option gives the pharmacy supervisor access to make corrective actions on Controlled Substances orders.

> Sometimes nursing may in error flag a Green Sheet ready for pharmacy pickup. Using this option, the pharmacy supervisor may change the Green Sheet order status from COMPLETED - GREEN SHEET READY FOR PICKUP

> to DELIVERED - ACTIVELY ON NAOU to correct this problem.

> The CS software allows pharmacy to add existing Green Sheets, active orders on an NAOU, at package setup. These orders may be tracked using the CS software. Sometimes one of these existing Green Sheets may be incorrectly entered in the software. Using this option, the pharmacy supervisor may delete this erroneous existing Green Sheet.

> An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions.

### Edit/Cancel Verified Orders \[PSD EDIT/CANC VER ORD\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option gives the pharmacy supervisor access to edit or cancel a verified order. The order must be edited or cancelled prior to being delivered to the NAOU. A verified order may be edited only once. It must be cancelled and re-entered if a second edit is required. Quantity, manufacturer, lot number, and expiration date are the only fields in which edits can be made.

### Correct Order Status - GS Ready for Pickup \[PSD CORRECT STATUS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option gives the pharmacy supervisor access to correct the order status of certain CS orders. Sometimes nursing may in error flag a Green Sheet ready for pharmacy pickup. Using this option, the pharmacy supervisor may change the Green Sheet order status from COMPLETED - GREEN SHEET READY FOR PICKUP to DELIVERED - ACTIVELY ON NAOU to correct this problem. An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions.

### Existing Green Sheets Correction \[PSD CORRECT EXISTING GS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option gives the pharmacy supervisor access to delete Green Sheets that were added using the *Add Existing Green Sheets* option. An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrections.

### Error on Completed Green Sheets \[PSD CORRECT GS STATUS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the Pharmacy Supervisor to correct the completed status of a Green Sheet from COMPLETED - REVIEWED to COMPLETED - PENDING PROBLEM RESOLUTION. An entry in the CS CORRECTION LOG file (#58.87) will be created to track this error.

### List Pending Errors/Adjustments Logged by TRAKKER \[PSD ERR/ADJ PENDING REPORT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option lists all pending errors/adjustments logged from the barcode TRAKKER for a specific Dispensing Site within a given time frame.

### Enter Error/Adjustment Resolution \[PSD ERR/ADJ EDIT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option gives designated pharmacy supervisors the ability to enter a resolution comment for each error or adjustment created when using the barcode TRAKKER.

### Print Resolved Errors/Adjustments Log \[PSD ERR/ADJ RESOLVED REPORT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report prints a listing of all resolved errors/adjustments logged by the barcode TRAKKER for a specific Dispensing Site within a given time frame.

## Print Pharmacist ID Labels \[PSD LABEL PHARM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option enables holders of the PSDMGR security key, usually pharmacy supervisors, to print the pharmacists barcoded ID labels.

> These barcode ID labels will identify the Controlled Substances pharmacists using the TRAKKER to perform narcotic vault inventories. The pharmacist is identified by SSN within the barcode but RPh will be displayed on the label for security purposes.

> The following format is used when printing pharmacists ID labels:

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/013.png)

> The recommended labels are Avery \#5160, 1" x 2 5/8". These labels print 3 rows across and 10 columns down for a total of 30 labels per sheet.

## Inspectors Label Print \[PSD LABEL INSP\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows narcotic inspectors and pharmacy supervisors to print the inspectors barcoded ID labels.

> These barcode ID labels will identify the Controlled Substances inspector using the TRAKKER to perform narcotic vault inspections. The narcotic inspector is identified by SSN within the barcode but Ins will be displayed on the label for security purposes.

> The following format is used when printing inspectors ID labels:

> ![](controlled-substances-version-3-supervisor-s-user-manual-updated-psd-3-89/014.png)

> The recommended labels are Avery \#5160, 1" x 2 5/8". These labels print 3 rows across and 10 columns down for a total of 30 labels per sheet.

## Unscheduled Order Report \[PSD EMERGENCY ORDER REPORT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A report to show by drug or by NAOU a list of unscheduled orders.

# Production Reports \[PSD PRODUCTION REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pharmacy uses the production reports to maintain Controlled Substances drug accountability and proper inventory controls. Reports generated in lieu of VA FORM 10-2321 and VA FORM 10-2638 may be generated from this menu.

## Pending CS Orders by Dispensing Site \[PSD PEND VAULT ORDERS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pharmacy uses this option to list all pending Controlled Substances orders or a specific dispensing site.

## Orders Filled Not Delivered \[PSD NOT DELIVERED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates a list of all Controlled Substances orders filled from the pharmacy dispensing site (vault) but not yet delivered to the NAOUs. A summary total sorted by drug is also generated.

## Inspector’s Log for Controlled Substances \[PSD PRINT INSPECTOR LOG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all active Green Sheets by Narcotic Area of Use. The data includes Green Sheet number, drug name, date dispensed, quantity dispensed expiration date (if available), blanks for quantity on hand, and a signature blank for verification.

## Inspector’s Log by Rec’d Date \[PSD INSP LOG BY RECD DATE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all dispensing transactions for Narcotic Area of Use received within a given date range. The data includes dispensing number, drug name, date received, quantity received, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.

## Stock Drug Print (Stock Level and Location) \[PSD STOCK PRINT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report prints an alphabetic listing of all active drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This report lists NAOU, drug name, location, stock levels, all ward (for drug) assignments, and all inventory types.

## Green Sheet Ready for Pickup Log \[PSD PRINT GS PICKUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all Green Sheets ready on the wards to be picked up by pharmacy. This report requires a signature of the pharmacy employee picking up the Green Sheet and a signature of the nurse releasing the Green Sheet. This document will be retained on the ward for nursing’s records.

## GS Picked Up Awaiting Pharmacy Review \[PSD PRT GS PICKED UP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all Green Sheets picked up by pharmacy but still awaiting a pharmacy review.

## Pharmacy Dispensing Report \[PSD PRINT PHARM DISP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists by dispensing site and date range the drug name, pharmacy dispensing number (Green Sheet \#), quantity dispensed, date dispensed, and dispensing pharmacist. Also there’s a summary by drug of total number dispensed. The summary may be generated without the individual dispensing data.

## Daily Activity Log (in lieu of VA FORM 10-2320) \[PSD DAILY LOG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Daily Activity Log lists all transactions for a Controlled Substances dispensing site (vault). It includes a forwarding balance on each transaction. This document may be generated for a single drug, some drugs, <span id="PSD_3_84_DailyActivityLog" class="anchor"></span>all Schedule II drugs (by typing the ^ALL CII DRUGS group name), or ALL drugs within a specified date range.

> Select Production Reports Option: DAILy Activity Log (in lieu of

> VA FORM 10-2320)

> Select Primary Dispensing Site: CONTROL SUBSTANCE VAULT//

> You may select a single drug, several drugs,

> or enter ^ALL to select all drugs.

> You may also enter ^ALL CII DRUGS to select all

> schedule 2 controlled substances.

> Select DRUG: ^ALL CII DRUGS

> Start with Date: T-7 (MAY 16, 2018)

> End with Date: T (MAY 23, 2018)

> This report is designed for a 132 column format.

> You may queue this report to print at a later time.

> DEVICE: 0;;999999999999999999999 HOME (CRT) Right Margin: 80// 132

> Daily Activity Log for CONTROL SUBSTANCE VAULT

> Page: 1

> Date: MAY 16, 2018 to MAY 23, 2018

> DATE/TIME NUMBER TYPE OF ACTIVITY

> QUANTITY BALANCE BY

> -----------------------------------------------------------------------------------------------------------------------------------

> =\> BELLADONNA 16.2MG/OPIUM 30MG SUPP

> 100840

> MAY 23,2018@08:09:32 DISP C WARD

> -12 100828 RW

> END OF REPORT! Press \<RET\> to return to the menu

## Transfer Drugs between Dispensing Sites Report \[PSD PRINT VAULT TRANSFERS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report displays all transactions which transferred Controlled Substances between dispensing sites, for a given period of time. The transactions list within dispensing site, by drug, the date/time transferred, quantity transferred, and pharmacist transferring the drug.

## Green Sheet History \[PSD GS HISTORY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Green Sheet history provides pharmacy with a detailed account of every transaction affecting this VA FORM 10-2638. This history may be displayed to the user’s screen or directed to a printer.

## Expiration Date Report \[PSD EXP REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a Controlled Substances Expiration Date Report for a single NAOU, several NAOUs, or ALL NAOUs. This report may be sorted by DATE/DRUG/NAOU or by DATE/NAOU/DRUG.

## Inventory Sheet Print \[PSD INVEN SHEET PRT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option prints an Inspector’s Sheet which is used to inventory on-hand amounts within a pharmacy dispensing site (vault). This form lists current on-hand amounts and provides a blank space for the inspector to list actual on-hand counts. A signature line is included on each page. This sheet may be generated for one drug, some drugs, or ALL drugs. The drugs are listed alphabetically.

## List On-Hand Amounts \[PSD ON-HAND\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option lists current on-hand amounts for drugs stocked in a pharmacy-dispensing site (vault). The drugs may be selected by one, some, or ALL. The drugs are listed alphabetically to the user’s screen or a selected printer.

## Rx (Prescription) Outpatient Dispensing Report \[PSD RX DISPENSING REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A report sorted by drug, prescription number, or inventory type for a date range of outpatient dispensing.

## OP CS Orders Report \[PSD DIGITALLY SIGNED ORDERS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report includes Controlled Substance (CS) prescriptions that have been entered and digitally signed via CPRS, manually entered via Backdoor Pharmacy (Patient Prescription Processing option \[PSO LM BACKDOOR ORDERS\]) or digitally signed and electronically received via eRx from outside prescribers. Once DEA's regulations are revised and PKI can be fully implemented nationally, sites that choose to activate the PKI functionality can use this option to retrieve all active and pending digitally signed orders for controlled substances. The source of prescription (CPRS, eRx, CPRS+eRx, Written, or All) may be selected.

## OP Released Rx Report \[PSD DIG. SIGNED RELEASED RX\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report includes Controlled Substance (CS) prescriptions that have been entered and digitally signed via CPRS, manually entered via Backdoor Pharmacy (Patient Prescription Processing option \[PSO LM BACKDOOR ORDERS\]) or digitally signed and electronically received via eRx from outside prescribers. Once DEA's regulations are revised and PKI can be fully implemented nationally, sites that choose to activate the PKI functionality can use this option to retrieve all released digitally signed orders for controlled substances. The source of prescription (CPRS, eRx, CPRS+eRx, Written, or All) may be selected.

## Controlled Substance Prescriptions Report \[PSD CS PRESCRIPTIONS REPORT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report includes Controlled Substance (CS) prescriptions that have been entered and digitally signed via CPRS, manually entered via Backdoor Pharmacy (Patient Prescription Processing option \[PSO LM BACKDOOR ORDERS\]) or digitally signed and electronically received via eRx from outside prescribers. This option provides a report of digitally signed orders that have been filled for Schedules I-V controlled substances. The report is for a date range with the option of selecting the source of prescription (CPRS, eRx, CPRS+eRx, Written, or All), and including discontinued and/or expired orders and various sort criteria. For example, list by patient, by provider, by drug, and by schedule, etc.

## DEA DATA – Waived Practitioner Report \[PSD DEA SUBOXONE\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides a list of patients that were prescribed Suboxone drugs. Two views are available, one with details, and another with just the counts of Suboxone patients per prescriber.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Action Prompt There are two action prompts that occur during the pharmacy dispensing process. The action codes
used with these prompts will appear in ( ). The following codes are valid:
> V Verify or Dispense the order (Displayed
> only to the dispensing pharmacist).
> P Process or Fill the order (Displayed only to the
> pharmacy technician or pharmacist
> filling but not dispensing the order).
> DC Cancel the order.
> E Edit the order.
> B Bypass the order.
> S Show the order.
Completion Status A review status is attached to each Controlled Substances Green Sheet returned to pharmacy.
The following are valid:
> NO DISCREPANCY—No discrepancy found.
> TURN IN FOR DESTRUCTION—CS drug turned in to be destroyed.
> RETURNED TO STOCK—CS Drug returned to stock. The dispensing site inventory balance will be updated.
> MATH ERROR—CS drug discrepancy found.
> GREEN SHEET NOT SIGNED BY NURSE—GS missing nurse’s signature.
> OTHER—REFERRED TO PHARMACY SUPERVISOR—CS drug discrepancy referred to supervisor for resolution.
Daily Activity Log The Daily Activity Log lists data, within a selected date range, associated with the VA FORM 2320 for a dispensing site.
Dispensing Number Control number assigned by pharmacy when dispensing a Controlled Substances drug. This number is used to track the Green Sheet and drug. Also referred to as the Disp \#, Green Sheet \#, GS \#, or transaction \# throughout the CS package.
Dispensing/Receiving Report This report can be printed in lieu of VA Form (in lieu of VA Form 10-2321) 2321 and lists all Controlled Substances orders dispensed to an NAOU. The signatures of the dispensing pharmacist and the nurse receiving the drug are required.
Dispensing Site An NAOU set up as a pharmacy vault that dispenses
Controlled Substances drugs.
Dispensing Worksheet This worksheet compiles a list of all pending Controlled Substances request orders for a selected dispensing site. A worksheet number, drug name, quantity ordered, requesting NAOU, ordered by, comments, and blanks for pharmacy dispensing number, manufacturer, lot number, and expiration date are listed on the worksheet.
Drug Address Code A code that represents the location of a drug in the NAOU
(Location Code) For example, if TYLOX is stored in an NAOU on the
> second set of shelves, third shelf from the top, its drug address code could be expressed as S,2,3. The address code can consist of up to three levels separated by a comma. Each level should further define the exact location. The code is associated with an expansion code for clarity.
Drug Address Code Text used to clarify the meaning of a drug address code.
Expansion For example, the code S would be expanded and printed as shelf. (These codes and expansions are locally created terms.)
Green Sheet The CONTROLLED SUBSTANCE ADMINISTRATION
RECORD (VA Form 10-2638) is referred to as a Green Sheet or GS throughout the CS package. Pharmacy dispensing number, drug name, expiration date, quantity dispensed, lot number, ordered by, dispensed by, and ward (NAOU) are printed on the form.
Green Sheet number Control number assigned by pharmacy when dispensing a Controlled Substances drug. This number is used to track the Green Sheet and drug. It is also referred to as the GS \#, dispensing \#, or disp \#, or transaction \# throughout the CS package.
Inpatient Site Inpatient Site must be defined for each NAOU. The Controlled Substances software utilizes this data to distinguish multi-divisional sites.
Inspector’s Log This report lists all active Green Sheets by NAOU. It includes the following information: Green Sheet \#, drug name, date dispensed, quantity dispensed, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.
Interactive Reader The Interactive Reader Language (IRL) is a language Language (IRL) used to write programs on barcode readers that allow the
readers to interact with the user.
Intranet A companywide computer network available via modem that connects users.
Master Vault An NAOU set up as your primary dispensing site.
NAOU - Narcotic Area A Narcotic Area of Use (NAOU) is a place where
of Use commonly stocked Controlled Substances drugs are stored for use by pharmacy, wards, or treatment areas. There are three types of NAOUs: 1) Master Vault, 2) Satellite Vault, and 3) Narcotic Locations.
NAOU Inventory Group An NAOU Inventory Group is defined by pharmacy to represent the Narcotic Areas of Use which are inventoried together as a group. By grouping the commonly inventoried NAOUs under an easy to remember group name, the elements of the inventory are established, and do not have to be redefined every time an inventory is scheduled.
Narcotic Location An NAOU set up for the nursing wards, pharmacy IV room, or a pharmacy working stock area.
Order Status A processing status is attached to each Controlled Substances request order. The following are valid:
> REQUESTED—NOT ORDERED
> Requests created by batch processing but not yet approved.
> ORDERED—NOT PROCESSED
> Ordered by nursing but not processed by pharmacy.
> PROCESSED—NOT DISPENSED Processed (filled) by pharmacy but not yet dispensed.
> FILLED—NOT DELIVERED Dispensed and verified by pharmacy but not delivered to the requesting NAOU.
> DELIVERED—ACTIVELY ON NAOU Drug stored on the NAOU.
> COMPLETED—GREEN SHEET READY FOR PICKUP Nursing has flagged the Green Sheet ready for pharmacy pickup.
> COMPLETED—GREEN SHEET PICKED UP Green Sheet returned to pharmacy but not yet reviewed.
> COMPLETED—REVIEWED Pharmacy has reviewed the Green Sheet .
> COMPLETED—PENDING PROBLEM
> RESOLUTION Pharmacy has reviewed the Green Sheet and a problem exists
> CANCELLED Order cancelled.
> TRANSFERRED TO ANOTHER NAOU Order and drug transferred to another NAOU.
> UNDER REVIEW BY INSPECTOR Order and drug pulled from NAOU by CS Inspector for review.
> LOGGED BY TRAKKER All drug doses from this order have been logged out to patients using the TRAKKER. (Not currently used in Version 2.0.)
PSD ERROR This key should be allocated to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various error and exception conditions generated when entries are filed from the barcode TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER.
PSD NURSE This key should be allocated to nurses, usually LPNs, who may only receive and administer controlled substances but cannot place the order requests.
PSD PARAM This key should be allocated only to the Inpatient Pharmacy Package Coordinator(s). This lock controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site (vault).
PSD TECH Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* \[PSD ON-HAND TECH\], *Transfer Drugs between Dispensing Sites Report* \[PSD PRINT VAULT TRANSFERS TECH\], and the *Daily Activity Log (in lieu of VA FORM 10-2320)* \[PSD DAILY LOG TECH\] options on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\].
PSD TECH ADV Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the *Receipts Into Pharmacy* \[PSD RECEIPTS MENU\], *Dispensing Menu* \[PSD DISPENSING MENU\], *Destructions Menu* \[PSD DESTROY MENU\], *Manufacturer, Lot \#, and Exp. Date - Enter/Edit* \[PSD MFG/LOT/EXP\], *Outpatient Rx's* \[PSD OUTPATIENT\], *Complete Green Sheet* \[PSD COMPLETE GS\], *Destroyed Drugs Report* \[PSD DEST DRUGS REPORT\], *DEA Form 41 Destroyed Drugs Report* \[PSD DESTROY DEA41\], *Destructions Holding Report* \[PSD DESTRUCTION HOLDING\], *Add Existing Green Sheets at Setup* \[PSD EXISTING GS\], *Green Sheet Transfer*
> *  
> Between NAOUs Report* \[PSD GS TRANSFER (NAOU) REPORT\], *NAOUUsage Report* \[PSD NAOU USAGE\], *Transfer Drugs between Dispensing Sites* \[PSD TRANSFER VAULT DRUGS\] options on the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\]. The CS technician may perform all functions of the *Outpatient Rx’s* \[PSD OUTPATIENT\] option except releasing prescriptions.
PSD TRAN This key should be allocated to the Inpatient Pharmacy Coordinator(s). This key controls the access to the *NAOU to NAOU Transfer Stock Entries* \[PSD TRANSFER NAOU\] option. Users can copy stock entries from one NAOU into another NAOU or from an AR/WS AOU into an NAOU.
PSDMGR This key should be allocated to the Inpatient Pharmacy Package Coordinator(s) or his/her designee. This lock controls the editing of CS files for package set up. This key locks the Supervisor’s Menu options \[PSD MGR\].
PSDRPH This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.
PSJ PHARM TECH This key should be allocated to pharmacy technicians handling narcotic orders.
PSJ RNURSE This key should be allocated to nurses who request narcotic orders, receive, and administer controlled substances on the wards.
PSJ RPHARM This key should be given to pharmacists dispensing and receiving narcotic orders.
Satellite Vault An NAOU set up as a secondary dispensing site.
Stock Drug A drug (from the drug file) stored in an NAOU.
Stock Level The quantity of a drug stocked in a specific NAOU.
TRAKKER A barcode collection system utilized by scanning barcode labels or by pressing the key pad on the barcode reader device.
V*<span class="smallcaps">ist</span>*A Veterans Health Information Systems and Technology Architecture
Ward (for Drug) The name of the ward or wards that will use this particular drug. It is important to accurately answer this prompt because this is the link between the Unit Dose package and the Controlled Substances package. The Unit Dose package looks at this field to know if the drug is a Controlled Substances stocked drug.
A
Add Existing Green Sheets at Setup, 30
Add/Delete Ward (for Drug), 19
AMIS, 1
AMIS Report, 28
AOU to NAOU Transfer Entries, 21
Avery \#5160, 1" x 2 5/8", 33, 34
B
Balance Adjustment Report, 29
Balance Adjustments, 29
Breakdown/Dispensing UnitReport, 23
C
Check Stocked Drugs for CS Use, 24
COMPLETED - GREEN SHEET READY FOR PICKUP, 31
COMPLETED - GREEN SHEET READY FOR PICKUP to DELIVERED - ACTIVELY ON NAOU, 31
COMPLETED - REVIEWED to COMPLETED - PENDING PROBLEM RESOLUTION, 32
Completed Green Sheet Discrepancy Report, 27
Controlled Substances Prescriptions Report, 39
Correct Order Status - GS Ready for Pickup, 31
Correction Log Report, 28
Correction Menu, 31
Cost Reports, 28
Create/Edit the Narcotic Area of Use, 14
D
Daily Activity Log (in lieu of VA FORM 10-2320), 37
DEA DATA – Waived Practitioner Report, 39
DEA Form 41 Destroyed Drugs Report, 26
DEA Special Handling List, 22
Delete Green Sheets, 31
DELIVERED - ACTIVELY ON NAOU, 31
Destroy a Controlled Substances Drug, 30
Destroyed Drugs Report, 27
Destructions Holding Report, 25
Destructions Menu, 30
Digitally Signed CS Orders Report, 39
Digitally Signed OP Released Rx Report, 39
DRUG ADDRESS CODE/EXPANSION DIAGRAM, 13
Drug File Stats for CS Drugs, 22
E
Edit/Cancel Verified Orders, 31
Edited Verified Orders Report, 27
Electronic Signature, 3
Enter Error/Adjustment Resolution, 32
Enter/Edit CS Drug Location Codes, 12
Enter/Edit Menu, 11
Error on Completed Green Sheets, 32
Existing Green Sheets Correction, 32
Expiration Date Report, 38
F
File Diagram, 9
G
Green Sheet History, 38
Green Sheet Ready for Pickup Log, 36
Green Sheet Transfer Between NAOUs Report, 27
GS Picked Up Awaiting Pharmacy Review, 36
H
Hidden Actions, 2
Hold a CS Drug (No Inventory Update), 30
I
Inactivate NAOU, 19
Inactivate NAOU Stock Drug, 20
Initial Set Up, 9
Initialize Balance at Setup, 24
Inpatient Site, 11
Inspector’s Log by Rec’d Date, 35
Inspector’s Log for Controlled Substances, 35
Inspectors Label Print, 33
Inventory Group List (80 column), 23
Inventory Sheet Print, 38
Inventory Types - Enter/Edit, 11
L
List CS Drug Location Codes, 22
List On-Hand Amounts, 38
List Pending Errors/Adjustments Logged by TRAKKER, 32
Listing of Green Sheet Log, 28
M
Management Reports, 25
Manufacturer and Narcotic Information Report, 23
Manufacturer, Lot \#, and Exp. Date - Enter/Edit, 18
Mark/Unmark Drugs for Controlled Substances Use, 11
Master Vault, 14
MATH ERROR, GREEN SHEET NOT SIGNED BY NURSE, 27
N
NAOU Inventory Group - Enter/Edit, 18
NAOU to NAOU Transfer Stock Entries, 21
NAOU Usage Report, 28
Narcotic Breakdown Unit/Package Size - Enter/Edit, 18
Narcotic location, 14
Non-VA Drug Placed on Hold for Destruction, 30
O
Orders Filled Not Delivered, 25, 35
OTHER - REFERRED TO SUPERVISOR, 27
P
Pending CS Orders by Dispensing Site, 25, 35
Pharmacy Dispensing Report, 36
PHARMACY NAOU STOCK FILE WORKSHEET, 17
Print CS Set Up Lists, 21
Print Inventory Types, 22
Print Pharmacist ID Labels, 33
Print Resolved Errors/Adjustments Log, 32
Production Reports, 35
PSD PARAM, 11
PSD TECH, 44
PSD TECH ADV, 44
PSD TRAN, 20
PSDMGR, 9, 33
PSDMGR Key, 2
R
reactivate drug, 20
reactivate NAOU, 19
Rx (Prescription) Outpatient Dispensing Report, 39
S
Satellite Vault, 14
Set Up CS (Build Files) Menu, 9
Setting up the Controlled Substances package, 5
Show Narcotic Area of Use, 22
Site Parameters, 11
Sort NAOUs in Inventory Group, 21
Stock CS Drugs - Enter/Edit, 16
Stock Drug List(Inventory Type and Location), 23
Stock Drug Print (Stock Level and Location), 36
Stock Drug Print (StockLevel and Location), 22
Supervisor (CS) Menu, 9
T
Transfer Drugs between Dispensing Sites Report, 38
Transfer Stock Entries, 20
Transferred Green Sheets - Pending NAOU Receipt, 27
U
Under Inspector's Review - Green Sheets, 28
Unscheduled Order Report, 34
V
VA FORM 10-2321, 1, 35
VA FORM 10-2638, 1, 29, 35, 38
VA FORM 10-3638, 29
VAMCs, 1
V*IST*A, 1
W
Ward (for Drug) Transfer, 19
WORKSHEET FOR CREATING, 15


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Controlled Substances Version 3 Supervisor's User Manual (Updated PSD*3*84)

## Digitally Signed CS Orders Report \[PSD DIGITALLY SIGNED ORDERS\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once DEA's regulations are revised and PKI can be fully implemented nationally, sites that choose to activate the PKI functionality can use this option to retrieve all active and pending digitally signed orders for controlled substances.

## Digitally Signed OP Released Rx Report \[PSD DIG. SIGNED RELEASED RX\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once DEA's regulations are revised and PKI can be fully implemented nationally, sites that choose to activate the PKI functionality can use this option to retrieve all released digitally signed orders for controlled substances.
