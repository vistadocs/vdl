---
title: Prosthetics Version 3 Basic User Manual (Updated RMPR*3*178)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Basic  (Updated RMPR*3*178)
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 3
description: "<table style=\\"width:100%;\\"> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 11%\\" /> <col style=\\"width: 70%\\" /> <col style=\\"width: 0%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td>Audience</td> <td colspan=\\"3\\"><blockquote> <p>The <em><strong>Prosthetics Basics User Manual</strong></em> is for"
audience: 
keywords: 
  - strong
  - table
  - style
  - width
  - class
  - colgroup
  - tbody
  - blockquote
  - patient
  - colspan
page_count: 0
word_count: 33176
section_count: 14
table_count: 16
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/prostheticsbasicsusermanual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/prostheticsbasicsusermanual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

Prosthetics (RMPR)

Basic User Manual

![](prosthetics-version-3-basic-user-manual-updated-rmpr-3-178/001.png)

October 2024Department of Veterans Affairs (VA)Office of Information and Technology (OIT)Enterprise Program Management Office (EPMO)  
Revision History

When updates occur, the Title Page lists the new revised date and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/2024</td>
<td>RMPR*3.0*216</td>
<td><p>Removed the following options from the <a href="#utilities-menu-ut">Utilities Menu</a>:</p>
<p>PGE <a href="#PurgeObsoleteData">Purge Obsolete Data</a></p>
<p>&gt; Out of order: (per patch RMPR*3.0*216)</p>
<p>PCL <a href="#PurgeClosedPurchasingTransactions">Purge Closed Purchasing Transactions</a></p>
<p>&gt; Out of order: (per patch RMPR*3.0*216)</p>
<p>PCX <a href="#PurgeCancelledTransactions">Purge Cancelled Transactions</a></p>
<p>&gt; Out of order: (per patch RMPR*3.0*216)</p>
<p>PSU <a href="#PurgeSuspenseRecords">Purge Suspense Records</a></p>
<p>&gt; Out of order: (per patch RMPR*3.0*216)</p>
<p>The <a href="#PurgeObsoleteData">Purge Obsolete Data</a> [RMPR PURGE MENU] Main Menu will be placed "OUT OF ORDER" and the <a href="#PurgeAgedPurchasingTransactions">Purge Aged Purchasing Transactions [RMPR PURGE AGED]</a> will remain as a standalone option under the Utilities <a href="#utilities-menu-ut">[RMPR UTLITIES]</a> menu.</p></td>
</tr>
<tr class="even">
<td>10/2016</td>
<td>RMPR*3.0*178</td>
<td>Added new option RMPR GIP STOCK to Purchasing Menu (p. <a href="\l">9</a>)</td>
</tr>
<tr class="odd">
<td>08/2014</td>
<td>RMPR*3.0*168</td>
<td><p>Updates for ICD-10</p>
<p>Updated title page</p>
<p>New ICD-10 screen capture (p.47)</p></td>
</tr>
<tr class="even">
<td>08/2011</td>
<td>RMPR*3*167</td>
<td>Modify text when referencing Form 1358. See page 88.</td>
</tr>
<tr class="odd">
<td>3/01/2010</td>
<td>RMPR*3*150</td>
<td>Added new option EDIT 2319 (Vendor, QTY, Cost)</td>
</tr>
<tr class="even">
<td>5/19/2004</td>
<td></td>
<td>Initial Version 3.0</td>
</tr>
</tbody>
</table>

#### Table of Contents

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
  - [Prosthetics Basics User Manual](#prosthetics-basics-user-manual)
  - [<u>Section 1</u>: Understanding Main Menu Features](#usection-1u-understanding-main-menu-features)
    - [Overview](#overview)
    - [Purchasing Menu (PU)](#purchasing-menu-pu)
    - [Purchasing Menu (PU), continued](#purchasing-menu-pu-continued)
    - [Display/Print Menu (DD)](#displayprint-menu-dd)
    - [Utilities Menu (UT)](#utilities-menu-ut)
    - [Suspense Menu (SU)](#suspense-menu-su)
    - [Correspondence Menu (CO)](#correspondence-menu-co)
    - [Scheduled Meetings and Home/Liaison Visits Menu (SC)](#scheduled-meetings-and-homeliaison-visits-menu-sc)
    - [Process Form 2529-3 (PS)](#process-form-2529-3-ps)
    - [Eligibility Inquiry (EL) Menu](#eligibility-inquiry-el-menu)
    - [PSC/Entitlement Records (ET) Menu](#pscentitlement-records-et-menu)
    - [Home Oxygen Main Menu (HO)](#home-oxygen-main-menu-ho)
    - [Pros Inventory Main (INV)](#pros-inventory-main-inv)
    - [NPPD Tools Menu (ND)](#nppd-tools-menu-nd)
  - [<u>Section 2</u>: Display/Print Menu](#usection-2u-displayprint-menu)
    - [Overview](#overview-1)
    - [Display/Print Menu Option Descriptions](#displayprint-menu-option-descriptions)
    - [Display/Print Patient 2319 (23)](#displayprint-patient-2319-23)
    - [View and Print the Patient 2319](#view-and-print-the-patient-2319)
    - [View Patient Demographics](#view-patient-demographics)
    - [View Clinic Enrollments/Correspondence](#view-clinic-enrollmentscorrespondence)
    - [View Letters/Correspondence on File](#view-letterscorrespondence-on-file)
    - [View Entitlement Information](#view-entitlement-information)
    - [View Appliance Transactions](#view-appliance-transactions)
    - [View Auto Adaptive Information](#view-auto-adaptive-information)
    - [View Critical Comments](#view-critical-comments)
    - [Add/Edit Disability Codes](#addedit-disability-codes)
    - [View Home Oxygen Items](#view-home-oxygen-items)
  - [Transaction Inquiry (TI)](#transaction-inquiry-ti)
    - [View a Transaction](#view-a-transaction)
  - [Print All Prosthetic Items (IP)](#print-all-prosthetic-items-ip)
    - [Overview](#overview-2)
    - [View the Prosthetic Item Master List](#view-the-prosthetic-item-master-list)
  - [Print Prosthetic Billings for MAS (BI)](#print-prosthetic-billings-for-mas-bi)
    - [Overview](#overview-3)
    - [View Prosthetic Billing Information](#view-prosthetic-billing-information)
    - [View Item History](#view-item-history)
    - [View Item History Within a Date Range](#view-item-history-within-a-date-range)
  - [Search for Recalled Item (SE)](#search-for-recalled-item-se)
    - [Overview](#overview-4)
    - [Search by Serial Number or Lot Number](#search-by-serial-number-or-lot-number)
    - [Search by Item Number](#search-by-item-number)
  - [Site Parameter Inquiry (SI)](#site-parameter-inquiry-si)
    - [Overview](#overview-5)
  - [Vendor Inquiry (VI)](#vendor-inquiry-vi)
    - [Overview](#overview-6)
    - [Vendor Inquiry Screen Output](#vendor-inquiry-screen-output)
  - [<u>Section 3</u>: Purchasing Menu (PU)](#usection-3u-purchasing-menu-pu)
    - [Overview](#overview-7)
    - [List Open 1358 Prosthetic Transactions (LI)](#list-open-1358-prosthetic-transactions-li)
    - [Close Out (CO)](#close-out-co)
  - [Enter New Request (EN)](#enter-new-request-en)
    - [Overview](#overview-8)
    - [Enter a 2421 Form (24)](#enter-a-2421-form-24)
    - [Enter a 2520 Transaction without Printing 10-55 (25)](#enter-a-2520-transaction-without-printing-10-55-25)
    - [10-55 PSC Form (10)](#10-55-psc-form-10)
    - [Eyeglass Record (29)](#eyeglass-record-29)
  - [Appendix A – Online Help](#appendix-a-online-help)
  - [Appendix B - Glossary](#appendix-b-glossary)

## Prosthetics Basics User Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## <u>Section 1</u>: Understanding Main Menu Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Audience</td>
<td colspan="3"><blockquote>
<p>The <em><strong>Prosthetics Basics User Manual</strong></em> is for new Prosthetics users of the Prosthetics Sensory Aids Service (PSAS) system including Purchasing Agents and any other new end user on the system.</p>
<p>This manual will provide a general overview of the entire system as well as step-by-step instructions of the more frequently used menus and options.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Main Menu</td>
<td colspan="3"><blockquote>
<p>The main menu for Prosthetics is the following - the <strong>Prosthetic’s Officials</strong> Menu:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><em><strong>Prosthetic’s Officials Menu</strong></em></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">PU</td>
<td>Purchasing</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">DD</td>
<td>Display/Print</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">UT</td>
<td>Utilities</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">AM</td>
<td>AMIS</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">SU</td>
<td>Suspense</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">CO</td>
<td>Correspondence</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">SC</td>
<td>Scheduled Meetings &amp; Home/Liaison Visits</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">PS</td>
<td>Process Form 2529-3</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">EL</td>
<td>Eligibility Inquiry</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">ET</td>
<td>PSC/Entitlement Records</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HO</td>
<td>Home Oxygen Main Menu</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">INV</td>
<td>Pros Inventory Main</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">ND</td>
<td>NPPD Tools</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">VR</td>
<td>Verify/Repair Purchase Card Form</td>
<td></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 66%" />
<col style="width: 15%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td>In this manual</td>
<td colspan="3"><blockquote>
<p>The following are the sections in this manual.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2">Topic</td>
<td>See Page</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Section 1: Understanding Main Menu Features</td>
<td>1</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Section 2: Display/Print Menu (DD)</td>
<td>24</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Section 3: Purchasing Menu (PU)</td>
<td>58</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Appendix A – Online Help</td>
<td>82</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Appendix B - Glossary</td>
<td>83</td>
<td></td>
</tr>
</tbody>
</table>
Overview, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Options</td>
<td><blockquote>
<p>Below are the <strong>Prosthetic Official’s Main</strong> <strong>Menu</strong> options, the option name for each, the synonym, and a description of each. To display this information, type three question marks at the following prompt:</p>
<p>Select Prosthetic Official's Menu Option: <strong>??? &lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>Menu Option</th>
<th>Synonym</th>
<th><p>Option</p>
<p>Name</p></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Purchasing</td>
<td>PU</td>
<td>RMPR PURCHAS-ING MENU</td>
<td>Purchasing menu, sub-menu of Prosthetic Clerk/Official master menus.</td>
</tr>
<tr class="even">
<td>Display/Print</td>
<td>DD</td>
<td>RMPR DISPLAY/PRINT</td>
<td>Display/Print menu for Prosthetic Clerks and Officials. This is a sub-menu of Prosthetic Clerks and Official’s master menus.</td>
</tr>
<tr class="odd">
<td>Utilities</td>
<td>UT</td>
<td>RMPR UTILITIES</td>
<td>This is the Prosthetic’s Utility Menu.</td>
</tr>
<tr class="even">
<td>AMIS</td>
<td>AM</td>
<td>RMPR MGMT REPORTS</td>
<td>AMIS data is generated from this menu option.</td>
</tr>
<tr class="odd">
<td>Suspense</td>
<td>SU</td>
<td>RMPR SUSPENSE MENU</td>
<td>This is the menu for Suspense Options.</td>
</tr>
<tr class="even">
<td>Correspondence</td>
<td>CO</td>
<td>RMPR CORR MAIN</td>
<td>This is the main menu for Correspondence.</td>
</tr>
<tr class="odd">
<td>Scheduled Meetings &amp; Home/Liaison Visits</td>
<td>SC</td>
<td>RMPR SCHED-H/L VISITS</td>
<td>This is the main menu for Scheduled Meetings and Home Liaison Visits.</td>
</tr>
<tr class="even">
<td>Eligibility Inquiry</td>
<td>EL</td>
<td>RMPR ELG INQ</td>
<td>This option is an eligibility inquiry into the MAS PATIENT file (#2).</td>
</tr>
<tr class="odd">
<td><p>PSC/</p>
<p>Entitlement Records</p></td>
<td>ET</td>
<td>RMPR ENTITLE-MENT/PSC</td>
<td>This is the menu for Prosthetic Service Card and Entitlement Records.</td>
</tr>
<tr class="even">
<td>Home Oxygen Main Menu</td>
<td>HO</td>
<td>RMPO-MENU-MAIN</td>
<td>This menu helps you manage your home oxygen program. It tracks costs of services, helps you manage billings, and alerts you when it is time to send letters to patients (e.g., prescription expiration).</td>
</tr>
<tr class="odd">
<td>NPPD Tools</td>
<td>ND</td>
<td>RMPR NPPD TOOLS</td>
<td>This option contains all tools associated with the National Prosthetic Patient Database.</td>
</tr>
</tbody>
</table>
Overview, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Options (continued)</td>
<td><blockquote>
<p>Below are the <strong>Prosthetic Official’s Main</strong> <strong>Menu</strong> options, the option name for each, the synonym, and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 32%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Process Form 2529-3</td>
<td>PS</td>
<td>RMPR 2529-3 MAIN</td>
<td>Main Menu for Prosthetics Lab Module</td>
</tr>
<tr class="odd">
<td>Pros Inventory Main</td>
<td>INV</td>
<td>RMPR INV MAIN</td>
<td>Prosthetic generic inventory system.</td>
</tr>
<tr class="even">
<td>NPPD Tools</td>
<td>ND</td>
<td>RMPR NPPD TOOLS</td>
<td>Tools for the National Prosthetics Patient Database</td>
</tr>
<tr class="odd">
<td>Verify/Repair Purchase Card Form</td>
<td>VR</td>
<td>RMPR Verify/ Repair PC Number</td>
<td>Temporary option used to fix reconciliations of Purchase Card orders.</td>
</tr>
</tbody>
</table>

### Purchasing Menu (PU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Purchasing Menu</strong> <strong>(PU)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Menu Option</th>
<th>Synonym</th>
<th><p>Option</p>
<p>Name</p></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enter New Request</td>
<td>EN</td>
<td>RMPR ENT REQUESTS</td>
<td>This is the sub-menu for entering prosthetic purchasing requests that link with IFCAP.</td>
</tr>
<tr class="even">
<td>Stock Issues</td>
<td>SI</td>
<td>RMPR STOCK ISS</td>
<td>This is the Stock Issue Menu Options.</td>
</tr>
<tr class="odd">
<td>Reprints</td>
<td>RP</td>
<td>RMPR REPRINTS</td>
<td>This is the Reprint Menu for Prosthetic Purchasing Forms.</td>
</tr>
<tr class="even">
<td>Record 2237 Purchase to 10-2319</td>
<td>RE</td>
<td>RMPR ENT 2237</td>
<td>This option will record the information from a VAF 2237 to a patient’s VAF<br />
10-219 record.</td>
</tr>
<tr class="odd">
<td>Edit/Delete 2237 from 10-2319</td>
<td>ED</td>
<td>RMPR 2319 EDT</td>
<td>This option will edit or delete information posted from a VAF 2237 record to a patient’s VAF 10-2319.</td>
</tr>
<tr class="even">
<td>Cancel a Transaction</td>
<td>CA</td>
<td>RMPR CANCEL</td>
<td>This option will cancel purchasing transactions that have not been closed out.</td>
</tr>
<tr class="odd">
<td>Close Out</td>
<td>CO</td>
<td>RMPR CLOSE-OUT</td>
<td>This is locked with RMPRSUPERVISOR. This option is used to close out transactions when invoices are received from the vendor. This will update the actual VAF 1358 account balance.</td>
</tr>
<tr class="even">
<td>Cancel Purchase Card Transaction</td>
<td>CPC</td>
<td>RMPR4 PCC</td>
<td>This option will cancel the Purchase Card Transaction and remove the purchase from the Patient’s 10-2319 Record.</td>
</tr>
<tr class="odd">
<td>Reconcile/Close Out Purchase Card Transaction</td>
<td>CPO</td>
<td>RMPR4 CLOSE OUT</td>
<td>This option is used to close out purchasing transactions that used the Purchase Card. This option will <u>not</u> post to IFCAP 1358.</td>
</tr>
<tr class="even">
<td>Generic Inventory Stock Issues</td>
<td>GIP</td>
<td>RMPR GIP STOCK</td>
<td>This option allows sites to issue prosthetics stock that is maintained by the IFCAP Generic Inventory Package (GIP) rather than the prosthetics inventory Package (PIP).*</td>
</tr>
</tbody>
</table>
> \*Patch RMPR\*3.0\*178 configures VistA to allow the Prosthetics Department to use GIP instead of PIP. It automatically updates inventory in IFCAP GIP. However, when items issued are from an INVENTORY POINT linked to a Point of Use (POU) supply cabinet, option does not update the inventory, since special cabinets automatically update GIP inventory balances, via HL7 messaging, when stock is removed. This option also checks the DynaMed System Parameter flag to determine if the site is running DynaMed, and if so this option will abort. Sites using DynaMed should continue to use PIP until a solution is implemented for DynaMed and GIP.
Purchasing Menu (PU), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions (continued)</td>
<td><blockquote>
<p>Below are the <strong>Purchasing</strong> <strong>Menu</strong> <strong>(PU)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Menu Option</th>
<th>Synonym</th>
<th><p>Option</p>
<p>Name</p></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Edit 2319</td>
<td>ED2</td>
<td>RMPR EDIT 2319</td>
<td>This option will allow limited editing of purchasing and stock issue transactions recorded on a patient’s VAF 10-2319.</td>
</tr>
<tr class="even">
<td>EDIT 2319 (Vendor, QTY, Cost)</td>
<td>ED2C</td>
<td>RMPR EDIT 2319 VENDOR/QTY/COST</td>
<td>This option will allow users with the RMPRSUPERVISOR key to edit Vendor, Qty &amp; cost.</td>
</tr>
<tr class="odd">
<td>Edit Purchase Card Transaction</td>
<td>EDPC</td>
<td>RMPR4 EDPC</td>
<td>This option will edit the 2421PC form once it has been created.</td>
</tr>
<tr class="even">
<td>Add Historical Data</td>
<td>HI</td>
<td>RMPR HIS DATA</td>
<td>This option will allow posting an item to the patient’s VAF 10-2319 without counting on AMIS.</td>
</tr>
<tr class="odd">
<td>Delete Historical Data</td>
<td>HID</td>
<td>RMPR HIS DEL</td>
<td>This option deletes historical data.</td>
</tr>
<tr class="even">
<td>List Open 1358 Prosthetic Transactions</td>
<td>LI</td>
<td>RMPR PRINT OPEN TRANS</td>
<td>This option lists VAF 1358 transactions that have not been closed out.</td>
</tr>
<tr class="odd">
<td>List Open 1358 Transactions by Initiator</td>
<td>LII</td>
<td>RMPR PRINT OPEN TRANS INIT</td>
<td>This option will print open 1358 transactions in the Prosthetics package, sorted by initiator.</td>
</tr>
<tr class="even">
<td>List Open Purchase Card Transactions</td>
<td>LPC</td>
<td>RMPR4 LIST OPN</td>
<td>This menu will print all open Purchase Card Transactions. The Purchase Card Number will be encrypted, except for the creator and supervisor.</td>
</tr>
<tr class="odd">
<td>List Open Purchase Card Transactions by Initiator</td>
<td>LPCI</td>
<td>RMPR4 LIST OPEN BY INIT</td>
<td>This option will print the open Purchase Card Transactions by Initiator, sorted by transaction date.</td>
</tr>
</tbody>
</table>

### Purchasing Menu (PU), continued

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Purchasing Menu</strong> <strong>(PU)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Purchase Card Summary Sheet</td>
<td>LPS</td>
<td>RMPR4 PC SUM</td>
<td>This option displays the Purchase Card Summary by Card Number. It will list the open and closed obligations.</td>
</tr>
</tbody>
</table>

### Display/Print Menu (DD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Display/Print</strong> <strong>Menu</strong> <strong>(DD)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Display/Print Patient 2319</td>
<td>23</td>
<td>RMPR PRINT 2319</td>
<td>Display/print a patient's VAF 10-2319.</td>
</tr>
<tr class="odd">
<td>Transaction Inquiry</td>
<td>TI</td>
<td>RMPR 1358 INQ</td>
<td>Inquiry to single purchasing transaction.</td>
</tr>
<tr class="even">
<td>Print All Prosthetic Items</td>
<td>IP</td>
<td>RMPR PRINT ALL ITEMS</td>
<td>This option prints all Prosthetic Item Master records along with their new and repair AMIS codes. Lab AMIS codes are not printed with this version of Prosthetics.</td>
</tr>
<tr class="odd">
<td>Print Prosthetic Billings for MAS</td>
<td>BI</td>
<td>RMPR PRINT BILL</td>
<td>Prints all NSC (non-service connected) items issued to patients for billing purposes.</td>
</tr>
<tr class="even">
<td>Item History</td>
<td>IH</td>
<td>RMPR ITEM HISTORY</td>
<td>Prints an item history of all purchases made for this item.</td>
</tr>
<tr class="odd">
<td>Search for Recalled Item</td>
<td>SE</td>
<td>RMPR PRINT RECALL</td>
<td>Searches the RECORD OF PROS APPLIANCE/ REPAIR file (#660) for recalled item.</td>
</tr>
<tr class="even">
<td>Site Parameter Inquiry</td>
<td>SI</td>
<td>RMPR SITE INQ</td>
<td>This menu option should be used to review your local site information.</td>
</tr>
<tr class="odd">
<td>Vendor Inquiry</td>
<td>VI</td>
<td>RMPR INQ VEND</td>
<td>This option is an inquiry to the IFCAP VENDOR file (#440).</td>
</tr>
</tbody>
</table>

### Utilities Menu (UT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Utilities</strong> <strong>Menu</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Menu Option</th>
<th>Synonym</th>
<th><p>Option</p>
<p>Name</p></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Add/Edit Patient to Prosthetics</td>
<td>AP</td>
<td>RMPR ADD PATIENT</td>
<td>This option will add a new patient to the PROSTHETICS PATIENT file (#665). You may also edit existing patient data using this option.</td>
</tr>
<tr class="even">
<td>Enter Prosthetic Disability Code to 2319</td>
<td>DIS</td>
<td>RMPR DIS ENTRY</td>
<td>This will add or delete Disability Codes to be counted on AMIS.</td>
</tr>
<tr class="odd">
<td>Delete Prosthetic Disability Code from 2319</td>
<td>REM</td>
<td>RMPR DEL CODE</td>
<td>Mark Disability Code from patient's VAF 10-2319 as deactivated.</td>
</tr>
<tr class="even">
<td>Enter/Edit Prosthetic Item Master</td>
<td>EN</td>
<td>RMPR ADD ITEM MASTER</td>
<td>This option adds a new Item Record to File 661, PROS ITEM MASTER.</td>
</tr>
<tr class="odd">
<td>IFCAP Utilities</td>
<td>IF</td>
<td>RMPR VEN/ITEM</td>
<td>Menu for IFCAP Vendor and Item Edit options.</td>
</tr>
<tr class="even">
<td>Purge Obsolete Data<span id="PurgeObsoleteData" class="anchor"></span></td>
<td>PGE</td>
<td>RMPR PURGE MENU</td>
<td><p>Prosthetic Purging Options</p>
<p>Placed ‘Out of Order’ per patch RMPR*3.0*216.</p></td>
</tr>
<tr class="odd">
<td>Purged Aged Purchasing Transactions</td>
<td>PAG</td>
<td>RMPR PURGE AGED</td>
<td>Prosthetics Purge Aged Purchasing Transactions RMPR*3.0*216 moved the option to be under the Utilities Menu as a standalone option.</td>
</tr>
<tr class="even">
<td>Purge Closed<span id="PurgeClosedPurchasingTransactions" class="anchor"></span> Purchasing Transactions</td>
<td>PCL</td>
<td>RMPR PURGE CLOSED</td>
<td><p>Purges Prosthetics 1358 File (#664) closed transaction.</p>
<p>RMPR*3.0*216 placed the option ‘Out of Order’.</p></td>
</tr>
<tr class="odd">
<td>Purge Cancelled Transactions<span id="PurgeCancelledTransactions" class="anchor"></span></td>
<td>PCX</td>
<td>RMPR PURGE CANCELLED</td>
<td><p>Purges cancelled transactions.</p>
<p>RMPR*3.0*216 placed the option ‘Out of Order’.</p></td>
</tr>
<tr class="even">
<td>Purge Suspense Records<span id="PurgeSuspenseRecords" class="anchor"></span></td>
<td>PSU</td>
<td>RMPR PURGE SUS</td>
<td><p>Purges suspense records.</p>
<p>RMPR*3.0*216 placed the option ‘Out of Order’.</p></td>
</tr>
<tr class="odd">
<td>Flag Item as Returned/Condemned</td>
<td>RC</td>
<td>RMPR RETURN</td>
<td>This will place items as returned, condemned, turned-in, lost or broken. To review this data once entered, review the patient's VAF 10-2319 record on the third screen.</td>
</tr>
<tr class="even">
<td>Edit Returned/ Condemned Item</td>
<td>RE</td>
<td>RMPR RETURNED EDIT</td>
<td>This option will allow users to edit or delete items that have been flagged as returned or condemned.</td>
</tr>
<tr class="odd">
<td>RMPR file cleansing for field lengths</td>
<td>FCLN</td>
<td>RMPR FILE CLEANSING</td>
<td>This option was created temporarily to be used by sites that the VistA data dictionary for FileMan.</td>
</tr>
<tr class="even">
<td>Enter/Edit Site Parameters</td>
<td>SP</td>
<td>RMPR SITE MENU</td>
<td>To enter/edit station Prosthetics site parameters.</td>
</tr>
<tr class="odd">
<td>Display Prosthetic PO Information</td>
<td>WD</td>
<td>RMPR WH DISPLAY</td>
<td>This option will display purchase order information that does not contain patient name or sensitive information.</td>
</tr>
<tr class="even">
<td>Purge Aged Purchasing Transactions<span id="PurgeAgedPurchasingTransactions" class="anchor"></span></td>
<td>PAG</td>
<td>RMPR PURGE AGED</td>
<td>Purge Prosthetics 1358 File (#664) Orders, of aged transactions based on the same order purged from the Procurement &amp; Accounting Transactions File (#442).</td>
</tr>
</tbody>
</table>
Annual purging of the Prosthetics 1358 File \#664 where an order will be deleted if previously purged from the IFCAP Procurement & Accounting Transactions File \#442. The purge criteria will be guided by the same purge criteria used for IFCAP Annual Purging where the order information is kept for the previous 8 years. The Purge Aged Purchasing Process is used for the Annual purge.
For further guidelines, please visit [<u>PROSTHETIC & SENSORY AIDS SERVICE (10P4RK) - Business Practice Guidelines (BPGs) and Standard Operating Procedures (SOPs) - All Documents (sharepoint.com)</u>](https://dvagov.sharepoint.com/sites/VHAProsthetics/Business%20Practice%20Guidelines/Forms/AllItems.aspx)

### Suspense Menu (SU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>A Suspense Request (through the <strong>Suspense Menu</strong>) is a request for service or an item that is tracked by a five-day Delayed Order Report. The five workday policy refers to the process or time it takes from receiving the order in Prosthetics to the time an initial action on a request or the time the request is fulfilled has been taken.</p>
<p>If this process takes more than five workdays, it is flagged on the report for monitoring and reporting purposes. It is also denoted in the Suspense list by an asterisk.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Suspense Menu</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Add Suspense Record</td>
<td>AS</td>
<td>RMPR ADD SUSPENSE</td>
<td>Adds a new Suspense Record to the PROSTHETIC SUSPENSE file (#668). The patient need not be in the PROSTHETICS PATIENT file (#665).</td>
</tr>
<tr class="odd">
<td>Close Suspense Record</td>
<td>CS</td>
<td>RMPR CLOSE SUSPENSE</td>
<td>This will close out the suspense record, and flag it as completed.</td>
</tr>
<tr class="even">
<td>Edit Suspense Record</td>
<td>ES</td>
<td>RMPR SUSPENSE EDIT</td>
<td>This option will edit a suspense record for a patient.</td>
</tr>
<tr class="odd">
<td>Inquire to Individual Suspense Record</td>
<td>IS</td>
<td>RMPR INQ SUSPENSE</td>
<td>This option will display the complete Suspense Record for a veteran.</td>
</tr>
<tr class="even">
<td>Print Closed Suspense Records</td>
<td>PC</td>
<td>RMPR SUSPENSE PRINT CLOSED</td>
<td>This will print the closed suspense records for a date range.</td>
</tr>
<tr class="odd">
<td>Print Open Suspense Records</td>
<td>PO</td>
<td>RMPR SUSPENSE PRINT</td>
<td>This option will list all open suspense records.</td>
</tr>
</tbody>
</table>
Suspense Menu (SU), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions (continued)</td>
<td><blockquote>
<p>Below are the <strong>Suspense Menu</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Print 5 Day Old Suspense Report</td>
<td>PR</td>
<td>RMPR SUSPENSE PRINT 5 DAY OLD</td>
<td>This option prints all suspense records over 5 working days old.</td>
</tr>
<tr class="odd">
<td>Print Suspense Statistics</td>
<td>ST</td>
<td>RMPR SUSPENSE STAT</td>
<td>Prints statistics from the PROSTHETICS SUSPENSE file (#668).</td>
</tr>
<tr class="even">
<td>Suspense Processing</td>
<td>SP</td>
<td>RMPR SUSP MENU</td>
<td>This is the List Manager version of Suspense Processing, to be used with Consult Tracking.</td>
</tr>
</tbody>
</table>

### Correspondence Menu (CO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Correspondence Menu</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Create a Letter</td>
<td>CR</td>
<td>RMPR CORR CREATE</td>
<td>Creates new letter for Prosthetics.</td>
</tr>
<tr class="odd">
<td>Delete Patient Correspondence Letter</td>
<td>DE</td>
<td>RMPR CORR DELETE</td>
<td>Deletes correspondence letter from the PROS LETTER TRANSACTION file (#665.4).</td>
</tr>
<tr class="even">
<td>Add/Edit Correspondence Skeleton Letter</td>
<td>ED</td>
<td>RMPR CORR EDIT</td>
<td>This option allows Prosthetics managers to edit the basic skeleton letters (FORM LETTER TYPE).</td>
</tr>
<tr class="odd">
<td>Print/Display Patient Correspondence Letter</td>
<td>PR</td>
<td>RMPR CORR VIEW</td>
<td>View correspondence letter.</td>
</tr>
<tr class="even">
<td>Print Correspondence Skeleton Letter</td>
<td>PS</td>
<td>RMPR CORR PRINT</td>
<td>Allows printing of a correspondence letter.</td>
</tr>
</tbody>
</table>

### Scheduled Meetings and Home/Liaison Visits Menu (SC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Scheduled Meetings and Home/Liaison Visits (SC)</strong> Menu options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Pull over Scheduled Clinic Visits</td>
<td>PL</td>
<td>RMPR PULL SCHED</td>
<td>This option will allow scheduling clinic visits to be pulled over to VAF 10-2527.</td>
</tr>
<tr class="odd">
<td>Edit Form 10-2527 Information</td>
<td>25</td>
<td>RMPR EDIT 2527</td>
<td>Enter referral and action information to patient's clinic visits.</td>
</tr>
<tr class="even">
<td>Delete Scheduled Prosthetic Clinic Visits</td>
<td>DL</td>
<td>RMPR SCHED DEL</td>
<td>This option will allow the user to delete Prosthetics clinic visits that have been pulled over to the VAF 10-2527.</td>
</tr>
<tr class="odd">
<td>Enter/Edit Closed Time for Clinic Visits</td>
<td>CA</td>
<td>RMPR CLOSE APP</td>
<td>Clinic team member may enter or change time that a scheduled clinic appointment was completed.</td>
</tr>
<tr class="even">
<td>Appointment Roster and Action Sheet</td>
<td>AP</td>
<td>RMPR PRT 2527</td>
<td>Prints VAF 10-2527 for single clinic after information has been pulled over from MAS scheduled clinic visits.</td>
</tr>
<tr class="odd">
<td>Open Home/Liaison Visits</td>
<td>OP</td>
<td>RMPR H/L OPEN</td>
<td>Open home or liaison visits for Prosthetics.</td>
</tr>
<tr class="even">
<td>Close Home/Liaison Visits</td>
<td>CO</td>
<td>RMPR H/L CLOSE</td>
<td>Close open home or liaison visits by entering the date closed and the total hours of the visit.</td>
</tr>
<tr class="odd">
<td>Edit/Delete Home/Liaison Visits</td>
<td>ED</td>
<td>RMPR H/L EDIT</td>
<td>Edit/delete home or liaison visits.</td>
</tr>
<tr class="even">
<td>Print Closed Home/Liaison Visits</td>
<td>PC</td>
<td>RMPR H/L PRINT CLOSED</td>
<td>Print closed home/liaison visits.</td>
</tr>
<tr class="odd">
<td>Print Open Home/Liaison Visits</td>
<td>PO</td>
<td>RMPR H/L PRINT OPEN</td>
<td>Print open home or liaison visits.</td>
</tr>
</tbody>
</table>

### Process Form 2529-3 (PS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Process Form 2529-3</strong> Menu options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>2529-3 Request Menu</td>
<td>RQ</td>
<td>RMPR 2529-3</td>
<td>This menu will be used by the Prosthetics administrative personnel to enter, edit, print, and close out VAF 10-2529-3 requests.</td>
</tr>
<tr class="odd">
<td>Prosthetic Lab Menu</td>
<td>LB</td>
<td>RMPR LAB MENU</td>
<td>This is the main menu for Prosthetic Laboratory Technicians.</td>
</tr>
</tbody>
</table>

### Eligibility Inquiry (EL) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>The <strong>Eligibility Inquiry</strong> is an option and does not have submenu options. The following is an example of this option</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="screen-sample">Screen sample</h5></td>
<td><blockquote>
<p>PU Purchasing ...</p>
<p>DD Display/Print ...</p>
<p>UT Utilities ...</p>
<p>AM AMIS ...</p>
<p>SU Suspense ...</p>
<p>CO Correspondence ...</p>
<p>SC Scheduled Meetings and Home/Liaison Visits ...</p>
<p>PS Process Form 2529-3 ...</p>
<p>EL Eligibility Inquiry</p>
<p>ET PSC/Entitlement Records ...</p>
<p>HO Home Oxygen Main Menu ...</p>
<p>INV Pros Inventory Main ...</p>
<p>ND NPPD Tools ...</p>
<p>OC CoreFLS Order Control</p>
<p>VR VERIFY/REPAIR PURCHASE CARD NUMBER</p>
<p>Select Prosthetic Official's Menu Option<strong>: EL &lt;Enter&gt;</strong> Eligibility Inquiry</p>
<p>SITE: Hines Development System//</p>
<p>Select PATIENT NAME: PROSPATIENT,ONE 1-1-30 000000001 NO PILL</p>
<p>Enrollment Priority: Category: IN PROCESS End Date:</p>
<p>* Patient Requires a Means Test *</p>
<p>Primary Means Test Required from FEB 13,2002</p>
<p>Enter &lt;RETURN&gt; to continue. <strong>&lt;Enter&gt;</strong></p>
<p>PROSPATIENT,ONE SSN:000-00-0001 DOB: JAN 1,1930 CLAIM#</p>
<p>Phone: PHONE Phone:</p>
<p>Current Address: Primary Next of Kin Address:</p>
<p>1ST LINE OF STREET ADDRESS</p>
<p>SECOND LINE OF STREET ADDRESS</p>
<p>Patient Type: PILL Period of Service: OTHER OR NONE</p>
<p>Primary Eligibility Code: Status: REQUIRED</p>
<p>NSC Eligibility Status:</p>
<p>Receiving A&amp;A Benefits? NO Receiving Housebound Benefits? NO</p>
<p>Receiving Social Security? NO Receiving VA Pension? NO</p>
<p>Receiving Military Retirement? NO Receiving VA Disability? NO</p>
<p>Patient Name: PROSPATIENT,ONE SSN: 000-00-0001</p>
<p>MAS Disability Code(s):</p>
<p>*POW? NO</p>
<p>Enter `^`to exit, or `return` to continue: <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
Eligibility Inquiry (EL) Menu, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Example (continued)</td>
<td><blockquote>
<p>The Eligibility Inquiry also provides Last Movement Actions, Pending Appointments, and letters on file. You can select a Letter on File to be viewed. Enter the number of the letter to display and press <strong>&lt;Enter&gt;</strong> at the <strong>Device</strong> prompts.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="screen-sample-continued">Screen sample (continued)</h5></td>
<td><blockquote>
<p>PROSPATIENT,ONE SSN: 000-00-0001 DOB: JAN 1,1930 CLAIM#</p>
<p>Last Movement Actions</p>
<p>Trans. Type: TRANSFER Trans. Type: ADMISSION</p>
<p>Date: SEP 11,1995@15:04:29 Date: SEP 11,1995@14:59:18</p>
<p>Type of Movement: Type of Movement:</p>
<p>INTERWARD TRANSFER DIRECT</p>
<p>Ward: 1AS Ward: 5NM</p>
<p>Physician: PROSPROVIDER,ONE Physician: PROSPROVIDER,TWO</p>
<p>Diagnosis: SICK Diagnosis: SICK</p>
<p>Clinic Enrollments</p>
<p>Clinic Enrollment Date OPT or AC</p>
<p>MCGILL,TEST MAR 21,2000@13:11 OPT</p>
<p>Pending Appointments</p>
<p>Appt. Date Clinic Status Type</p>
<p>MAR 1,2004@09:15 PROSTHETICS INPATIENT APPOINTMENTREGULAR</p>
<p>SITE: Hines Development System//</p>
<p>Letters on file:</p>
<p># Patient Type of letter Employee Date of letter</p>
<p>------------------------------------------------------------------------------</p>
<p>1 PROSPATIENT,ONE TEST PROSPROVIDER,THREE JUN 03, 2003</p>
<p>2 PROSPATIENT,ONE ADP FL 10-90 PROSPROVIDER,THREE JUN 02, 2003</p>
<p>3 PROSPATIENT,ONE TEST PROSPROVIDER,THREE FEB 08, 2002</p>
<p>4 PROSPATIENT,ONE HO 30 DAY TEST PROSPROVIDER,THREE FEB 08, 2002</p>
<p>5 PROSPATIENT,ONE HO 30 DAY TEST PROSPROVIDER,THREE FEB 08, 2002</p>
<p>Enter '^' to stop or</p>
<p>Enter a number (1-5): 2 <strong>&lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80//<strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
Eligibility Inquiry (EL) Menu, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="letter-on-file">Letter on File</h5></td>
<td><blockquote>
<p>Below is the Letter on File that you selected to view for the specific patient displayed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="screen-sample-continued-1">Screen sample (continued)</h5></td>
<td><blockquote>
<p>REQUEST FOR QUOTATION</p>
<p>Date: Feb 12, 2004</p>
<p>TO: FROM: PROSVENDOR,ONE</p>
<p>Hines Development System</p>
<p>TEST 2</p>
<p>HINES, IL 60142</p>
<p>Vendor Phone #: Veteran: PROSPATIENT,ONE</p>
<p>SSN: 000000001</p>
<p>Your firm is being considered for the following:</p>
<p>An estimate on the above-listed item(s) is requested. YOUR QUOTATION</p>
<p>DOES NOT CONSTITUTE A PURCHASE ORDER. Upon completion of the esti-</p>
<p>mate, return the original to the Veterans Affairs facility indicated</p>
<p>above and retain a copy for your files.</p>
<p>If approved, a purchase order will be prepared and forwarded to you.</p>
<p>Sincerely,</p>
<p>PROSPROVIDER,FOUR</p>
<p>CHIEF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><h5 id="screen-sample-continued-2">Screen sample (continued)</h5></td>
<td><blockquote>
<p>VENDOR'S ESTIMATE</p>
<p>(To be completed by Vendor)</p>
<p>----------------------------------------------------------------------</p>
<p>| Article or Service |Quantity| Unit |Unit Cost|Total Cost|</p>
<p>----------------------------------------------------------------------</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>----------------------------------------------------------------------</p>
<p>| Vendor: Contract number (if applicable) |</p>
<p>| Address: |</p>
<p>| City: |</p>
<p>| State: Zip: |</p>
<p>| Telephone: |</p>
<p>| Date: Signature &amp; Title of Company Official|</p>
<p>| Note:List Terms/Discounts if Applicable |</p>
<p>----------------------------------------------------------------------</p>
<p>FL 10-90 ADP</p>
<p>Would you like to see more letters? No// (No)</p>
<p>Do you wish to create a correspondence letter? No// (No)</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PSC/Entitlement Records (ET) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>PSC/Entitlement Records (ET)</strong> Menu options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Add/Edit Clothing Allowance</td>
<td>AC</td>
<td>RMPR CLOTHING</td>
<td>Adds a Clothing Allowance for a patient.</td>
</tr>
<tr class="odd">
<td>Add/Edit Prosthetic Service Card</td>
<td>PS</td>
<td>RMPR ADD PSC</td>
<td>This option will add a Prosthetic Service Card to the patient’s VAF 10-2319 record.</td>
</tr>
<tr class="even">
<td>Enter/Edit Auto Adaptive Info</td>
<td>AU</td>
<td>RMPR AUTO</td>
<td><p>This option is the main menu to enter/edit auto-adaptive equipment purchased for the patient.</p>
<p>This allows adding a new Vehicle of Record, adding van modifications, new items, and editing of items and repairs.</p></td>
</tr>
<tr class="odd">
<td>Record Other Patient Information</td>
<td>RO</td>
<td>RMPR ADD OD</td>
<td><p>This option allows a free-text word processing area for storage of other information needed by service on the patient's VAF 10-2319 record.</p>
<p>Information such as eye color, hair color, patient's station, etc. is included.</p></td>
</tr>
</tbody>
</table>

### Home Oxygen Main Menu (HO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Home Oxygen Main Menu (HO)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Add/Edit Home Oxygen Patient</td>
<td>ED</td>
<td>RMPO ADD/EDIT PAT</td>
<td><blockquote>
<p>This option allows the user to add patients to the Prosthetics Patient file, edit demographics (e.g., therapy activation date and eligibility for home oxygen services), and document prescription and billing equipment data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Billing Transactions</td>
<td>BT</td>
<td>RMPO BILLING TRANSACTIONS</td>
<td>This option allows you to edit bills for a specific month, accept those transactions, and post them.</td>
</tr>
<tr class="even">
<td>Generate Letters</td>
<td>LE</td>
<td>RMPO LIST/PRINT MANAGER</td>
<td>This option creates a list of patients who are due to receive letters and prints the letters.</td>
</tr>
<tr class="odd">
<td>Home Oxygen Patient Template Update</td>
<td>TU</td>
<td>RMPO HO PAT TEMPLATE UPDA</td>
<td><p>This is a utility for updating vendor, HCPCS, FCP, item, and unit cost of all Home Oxygen patients in a particular station at once.</p>
<p>Only the patient template is changed, not the monthly billing. If the monthly billing is already been created for a certain month, changes on the template will not affect the billing cycle.</p></td>
</tr>
</tbody>
</table>
Home Oxygen Main Menu (HO), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Home Oxygen Main Menu (HO)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Inactivate/Activate Oxygen Patient</td>
<td>IN</td>
<td>RMPO INACT/ACT</td>
<td>This is an option to deactivate and activate/reactivate home oxygen patients.</td>
</tr>
<tr class="odd">
<td>Purchase Card Sign Off</td>
<td>SO</td>
<td>RMPO PO SIGN OFF</td>
<td>Once a billing is accepted and posted, this option can be used to sign off on the billing.</td>
</tr>
<tr class="even">
<td>Reports</td>
<td>RE</td>
<td>RMPO-RPT-MAINMENU</td>
<td>This menu contains reports on active and inactive home oxygen patients, addresses, prescription reports, billing discrepancies, etc.</td>
</tr>
<tr class="odd">
<td>Site Parameters Enter/Edit</td>
<td>SI</td>
<td>RMPO SITE EE</td>
<td>This option is used to define those parameters specific to the site such as: letters that should be generated and default prescription expiration dates.</td>
</tr>
<tr class="even">
<td>Verify Posted Billing Transactions</td>
<td>PB</td>
<td>RMPO POST 2319</td>
<td>This option posts all Home Oxygen billing transactions for a selected month for bills posted in IFCAP but not in Patient 2319 records. It will loop through all the records for the MONTH and VENDOR entered.</td>
</tr>
</tbody>
</table>

### Pros Inventory Main (INV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Pros Inventory Main (INV)</strong> Menu options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Add Inventory LOCATION or ITEMS</td>
<td>AE</td>
<td>RMPR INV ADD</td>
<td>This is an option to add a Location, HCPCS or ITEMS for inventory. Users can edit item fields under this option.</td>
</tr>
<tr class="odd">
<td>Deactivate Inventory Location</td>
<td>DE</td>
<td>RMPR INV DEACTIVATE</td>
<td>This option is only given to the holder of RMPRMANGAER key. It requires the electronic signatures of 2 users holding this key to be entered before a location can be deactivated.</td>
</tr>
<tr class="even">
<td>Edit Inventory Items</td>
<td>EI</td>
<td>RMPR INV EDIT</td>
<td>This option is for editing an Inventory Location or Items. You can only edit an Item or Location that has already been set-up.</td>
</tr>
<tr class="odd">
<td>Edit Inventory Location</td>
<td>EL</td>
<td>RMPR INV EDIT LOCATION</td>
<td>This option is for editing an existing inventory location.</td>
</tr>
<tr class="even">
<td>Inventory Reports</td>
<td>RP</td>
<td>RMPR INV REPORTS</td>
<td>Various Inventory reports are available through this option.</td>
</tr>
<tr class="odd">
<td>Order Item from Supply or Vendor</td>
<td>OI</td>
<td>RMPR INV ORDER</td>
<td>This is an option to record that an Item has been ordered. This option will not automatically order an item from Supply or Vendor.</td>
</tr>
</tbody>
</table>
Pros Inventory Main (INV), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu options continued</td>
<td><blockquote>
<p>Below are the <strong>Pros Inventory Main (INV)</strong> Menu options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Receive Item from Supply, Vendor or Patient</td>
<td>RC</td>
<td>RMPR INV RECEIVE</td>
<td>This is an option to record that an Item has been received and entered the Prosthetics Inventory. Receiving an Item in Supply through the IFCAP package does not update the Prosthetics Inventory module. This option must be done separately for an Item to be received and recorded in the Prosthetics module.</td>
</tr>
<tr class="odd">
<td>Reconcile Item Balance</td>
<td>UP</td>
<td>RMPR INV RECON-CILE</td>
<td>This is an option to reconcile or update Items in Prosthetics Inventory. Users can update the Quantity, Total Cost, Vendor, Unit of Issue, Re-order Level and Description.</td>
</tr>
<tr class="even">
<td>Remove/Deactivate HCPCS/Item from Inventory</td>
<td>RE</td>
<td>RMPR INV REMOVE HCPCS/ ITEM</td>
<td>This option removes/ deactivates inventory item(s) from the Prosthetics Inventory Program. Once an item has been removed/ deactivated, that item is not accessible. Only users with RMPRMANAGER key can access this option.</td>
</tr>
<tr class="odd">
<td>Transfer Stock Between Locations</td>
<td>TR</td>
<td>RMPR INV TRAN</td>
<td>This is an option to transfer an Item to a different Location. In order to transfer an Item, it must be set-up to both Locations. User can transfer all Quantities or certain Quantities. This option does not remove an item from a location if all quantities have been transferred.</td>
</tr>
</tbody>
</table>

### NPPD Tools Menu (ND)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>NPPD Tools Menu (ND)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Add/Edit HCPCS Synonyms</td>
<td>AE</td>
<td>RMPR ADD/EDIT HCPCS SYNONYM</td>
<td>This option will only edit the DESCRIPTION and SYNONYM in the Prosthetics HCPCS file.</td>
</tr>
<tr class="odd">
<td>DSS HCPCS History</td>
<td>HH</td>
<td>RMPR HCPCS HISTORY</td>
<td>This menu will display all HCPCS issued on a Patient's 2319 records for a date range.</td>
</tr>
<tr class="even">
<td>HCPCS Inquiry</td>
<td>INQ</td>
<td>RMPR NPPD INQ</td>
<td>You can look up one HCPCS at a time with this option.</td>
</tr>
<tr class="odd">
<td>NPPD Detail Display</td>
<td></td>
<td>RMPR NPPD GUI</td>
<td><blockquote>
<p>For users to be able to use the NPPD Detail Display GUI front-end, this option must be on either their primary or secondary menu options. This option has also been placed on RMPR NPPD TOOLS to give users who have access to the current NPPD options, access to NPPD GUI Detail Display. Note: 'B' type option for use after installation of RMPR*3*71. 'B' type options are not visible to roll &amp; scroll users.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Print 2529-3 Single Line</td>
<td>LSL</td>
<td>RMPR NPPDL<br />
PRL L</td>
<td>This option will print a single line, either New or Repair in Detail format for the form type 2529-3 only. This is the Lab.</td>
</tr>
</tbody>
</table>
NPPD Tools Menu (ND), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>NPPD Tools Menu (ND)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Print 2529-3 Worksheets</td>
<td>LPRT</td>
<td>RMPR NPPDL PRT</td>
<td><p>This option provides both Summary and Detail worksheets. They are divided into the following two basic parts with a station summary of each:</p>
<p>* New Activities</p>
<p>* Repair Activities</p>
<p>The above are further broken down by each mapped NPPD Group with a summary of each. Within each NPPD Group, there is an NPPD Line with a summary. The Detail display adds an itemized listing for each NPPD Line within the NPPD Group, so every transaction for the date range selected is displayed.</p>
<p>It is recommended to send this report to a device that will print a 132-right margin. This will not only ensure that you get the entire report, it will also expand the length of some of the data (e.g., Item and HCPCS DESCRIPTION on the Detail Worksheet) to make it more legible.</p></td>
</tr>
<tr class="odd">
<td>Print NPPD Single Line Detail</td>
<td>SL</td>
<td><p>RMPR NPPD</p>
<p>PRL L</p></td>
<td>This option will print a single line, either New or Repair in Detail format.</td>
</tr>
</tbody>
</table>
NPPD Tools Menu (ND), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu option descriptions</td>
<td><blockquote>
<p>Below are the <strong>NPPD Tools Menu (ND)</strong> options, the synonym, option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Print NPPD Worksheets</td>
<td>PRT</td>
<td>RMPR NPPD PRT</td>
<td>Printing functionality.</td>
</tr>
<tr class="odd">
<td>Print PSAS HCPCS List</td>
<td>MAP</td>
<td>RMPR NPPD LIST</td>
<td>Printing functionality.</td>
</tr>
<tr class="even">
<td>PSAS HCPCS History</td>
<td>PH</td>
<td>RMPR PSAS HCPCS HISTORY</td>
<td>View history of PSAS HCPCS.</td>
</tr>
<tr class="odd">
<td>Quick Edit 2319 Record</td>
<td>QED2</td>
<td>RMPR NPPD QUICK EDIT</td>
<td>This menu is a quick edit of the 2319 Record. This will allow you to select a record by the number displayed on the detail NPPD report for quick corrections.</td>
</tr>
</tbody>
</table>

## <u>Section 2</u>: Display/Print Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Display/Print</strong> <strong>(DD)</strong> menu is a sub-menu of <strong>Prosthetic Clerks and Official’s</strong> master menus. The internal option name is: RMPR DISPLAY/ PRINT, and the synonym is: DD.</p>
<p>The audience for this feature is Prosthetics Clerks as well as Officials.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Menu Option</td>
<td><blockquote>
<p>Below is the Prosthetic Official’s Menu.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 65%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Synonym</td>
<td>Menu Option</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">PU</td>
<td>Purchasing…</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">DD</td>
<td>Display/Print…</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">UT</td>
<td>Utilities…</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">AM</td>
<td>AMIS…</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">SU</td>
<td>Suspense …</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">CO</td>
<td>Correspondence…</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">SC</td>
<td>Scheduled Meeting and Home/Liaison Visits …</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">PS</td>
<td>Process Form 2529-3…</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">EL</td>
<td>Eligibility Inquiry</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">ET</td>
<td>PSC/Entitlement Records …</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HO</td>
<td>Home Oxygen Main Menu…</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">INV</td>
<td>Pros Inventory Main …</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">ND</td>
<td>NPPD Tool …</td>
<td></td>
</tr>
<tr class="odd">
<td>In this section</td>
<td colspan="3"><blockquote>
<p>The following chapters are in this section:</p>
</blockquote></td>
</tr>
</tbody>
</table>
|                                         |          |
|-----------------------------------------|----------|
| Topic                                   | See Page |
| Display/Print Menu Option Descriptions  | 25       |
| Display/Print Patient 2319 (23)         | 26       |
| Transaction Inquiry (TI)                | 42       |
| Print All Prosthetic Items (IP)         | 44       |
| Print Prosthetics Billings for MAS (BI) | 46       |
| Item History (IH)                       | 49       |
| Search for Recalled Item (SE)           | 51       |
| Site Parameter Inquiry (SI)             | 55       |

### Display/Print Menu Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option descriptions</td>
<td><blockquote>
<p>Below are the <strong>Display/Print</strong> Menu options with the option name and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>
|                        |                                        |
|------------------------|----------------------------------------|
| Display/Print Menu |                                        |
| 23                     | Display/Print Patient 2319             |
| TI                     | Transaction Inquiry                    |
| IP                     | Print All Prosthetic Items             |
| BI                     | Print Prosthetic Billings for MAS      |
| IH                     | Item History                           |
| SE                     | Search for Recall by Lot/Serial Number |
| SI                     | Site Parameter Inquiry                 |
| VI                     | Vendor Inquiry                         |
<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Option</td>
<td>Synonym</td>
<td><p>Option</p>
<p>Name</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>Display/Print Patient 2319</td>
<td>23</td>
<td>RMPR PRINT 2319</td>
<td>Display/print a patient’s VAF 10-2319 (Note the 2319 contains more than eligibility)</td>
</tr>
<tr class="odd">
<td>Transaction Inquiry</td>
<td>TI</td>
<td>RMPR 1358 INQ</td>
<td>Inquiry to single purchasing transaction.</td>
</tr>
<tr class="even">
<td>Print All Prosthetic Items</td>
<td>IP</td>
<td>RMPR PRINT ALL ITEMS</td>
<td>This option prints all Prosthetic Item Master records along with their new and repair AMIS codes. Lab AMIS codes are not printed with this version of Prosthetics.</td>
</tr>
<tr class="odd">
<td>Print Prosthetic Billings for MAS</td>
<td>BI</td>
<td>RMPR PRINT BILL</td>
<td>Prints all NSC (non-service connected) items issued to patients for billing purposes.</td>
</tr>
<tr class="even">
<td>Item History</td>
<td>IH</td>
<td>RMPR ITEM HISTORY</td>
<td>Prints an item history of all purchases made for this item.</td>
</tr>
<tr class="odd">
<td>Search for Recalled Item</td>
<td>SE</td>
<td>RMPR PRINT RECALL</td>
<td>Searches the RECORD OF PROS APPLIANCE/REPAIR file (#660) for recalled item.</td>
</tr>
<tr class="even">
<td>Site Parameter Inquiry</td>
<td>SI</td>
<td>RMPR SITE INQ</td>
<td>This menu option should be used to review your local site information.</td>
</tr>
<tr class="odd">
<td>Vendor Inquiry</td>
<td>VI</td>
<td>RMPR INQ VEN</td>
<td>This option is an inquiry to the IFCAP VENDOR file (#440).</td>
</tr>
</tbody>
</table>

### Display/Print Patient 2319 (23)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>You can view or print the 10-2319 Prosthetics Veteran patient information from the <strong>Display/Print Patient 2319</strong> <strong>(23)</strong> option. You will be prompted to select a patient.</p>
<p>You will also be prompted for a device to print the Patient 10-2319. You have the choice to send the report to a printer by entering a printer at the Device prompt or view selected portions of the 2319 on your terminal screen.</p>
<p><strong><u>Note</u>:</strong> Output to a printer will produce a different display than when it is sent to a terminal screen as you have a choice of which eligibility screens to view versus the printout will print the entire Patient 2319.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Options</td>
<td><blockquote>
<p>Here are the screens that you can view from the patient’s 2319:</p>
</blockquote>
<p>Patient Demographics</p>
<p>Clinic Enrollments/Correspondence</p>
<p>Entitlement Information</p>
<p>Appliance Transactions</p>
<p>Auto Adaptive Information</p>
<p>Critical Comments</p>
<p>Add/Edit Disability Code</p>
<p>Home Oxygen Items</p></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 66%" />
<col style="width: 14%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td>In this chapter</td>
<td colspan="2"><blockquote>
<p>The following topics are in this chapter:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Topic</td>
<td colspan="2">See Page</td>
</tr>
<tr class="odd">
<td colspan="2">View and Print the Patient 2319</td>
<td colspan="2">27</td>
</tr>
<tr class="even">
<td colspan="2">View/Print Patient Demographics</td>
<td colspan="2">29</td>
</tr>
<tr class="odd">
<td colspan="2">View Clinic Enrollments/Correspondence</td>
<td colspan="2">30</td>
</tr>
<tr class="even">
<td colspan="2">View Letters/Correspondence on File</td>
<td colspan="2">31</td>
</tr>
<tr class="odd">
<td colspan="2">View Entitlement Information</td>
<td colspan="2">33</td>
</tr>
<tr class="even">
<td colspan="2">View Appliance Transactions</td>
<td colspan="2">34</td>
</tr>
<tr class="odd">
<td colspan="2">View Auto Adaptive Information</td>
<td colspan="2">36</td>
</tr>
<tr class="even">
<td colspan="2">View Critical Comments</td>
<td colspan="2">37</td>
</tr>
<tr class="odd">
<td colspan="2">Add/Edit Disability Codes</td>
<td colspan="2">38</td>
</tr>
<tr class="even">
<td colspan="2">View Home Oxygen Items</td>
<td colspan="2">41</td>
</tr>
</tbody>
</table>

### View and Print the Patient 2319

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display the 2319</td>
<td><blockquote>
<p>You can display the 10-2319 Prosthetics Veteran record using the <strong>Display/Print Patient 2319 (23)</strong> Menu option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Steps</td>
<td><blockquote>
<p>To display or print the 10-2319 Prosthetics Veteran record, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>At the Select Display/Print Option prompt, type 23 to access the Display/Print Patient 2319 (23) option.</td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the <strong>Site:</strong> prompt, press <strong>&lt;Enter&gt;</strong> to accept the default setting or type a “<strong>?</strong>” to display a list and select a site from the list.</td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>At the <strong>Select Prosthetic Patient</strong> prompt, enter a Prosthetic patient name with the “LAST NAME,FIRST NAME” format.</td>
</tr>
<tr class="odd">
<td colspan="2">4</td>
<td>Press &lt;<strong>Enter</strong>&gt; to continue.</td>
</tr>
<tr class="even">
<td colspan="2">5</td>
<td>Patient identification information displays. : <strong>At the …OK? Yes// prompt, press &lt;Enter&gt; to continue</strong>.</td>
</tr>
<tr class="odd">
<td>2319 Screen</td>
<td colspan="2"><p><strong>23 Display/Print Patient 2319</strong></p>
<p>TI Transaction Inquiry</p>
<p>IP Print All Prosthetic Items</p>
<p>BI Print Prosthetic Billings for MAS</p>
<p>IH Item History</p>
<p>SE Search for Recalled Item</p>
<p>SI Site Parameter Inquiry</p>
<p>VI Vendor Inquiry</p>
<p>Select Display/Print Option: <strong>23</strong> <strong>&lt;Enter&gt;</strong> Display/Print Patient 2319</p>
<p>SITE: SUPPORT ISC// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select PROSTHETIC PATIENT: <strong>PROSPATIENT,ONE</strong> <strong>&lt;Enter&gt;</strong> PROSPATIENT,ONE 1-1-30 000000001</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>HINES, IL</p></td>
</tr>
</tbody>
</table>
View and Print the Patient 2319, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Printing vs. Displaying the 2319</td>
<td><blockquote>
<p>Printing is different than viewing the 2319 on your terminal! If you elect to print the 2319 information by entering <strong>SLAVE or another printer device</strong>, the <u>entire</u> Record of Appliances and Repairs prints out.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Steps (continued)</td>
<td><blockquote>
<p>To display or print the 10-2319 Prosthetics Veteran record, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">6</td>
<td><p>The system displays the <strong>Device: Home//</strong> prompt. Press &lt;<strong>Enter</strong>&gt; twice to display information to your terminal screen or type <strong>SLAVE</strong> to print the information to your personal printer.</p>
<p>You can print the information to another printer by typing the printer ID.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">7</td>
<td>The system displays: <strong>Right Margin: 80//</strong> (unless you requested to print to a printer using the SLAVE entry). Press &lt;<strong>Enter</strong>&gt; to continue.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">8</td>
<td>The Disability Codes display for the selected patient and you are given a choice of information to view, edit or print from the patient’s 2319.</td>
<td></td>
</tr>
<tr class="odd">
<td>2319 Screen (continued)</td>
<td colspan="3"><p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>*Comments on File.</p>
<p>Current Disability Codes are:</p>
<p>COS/B EMPLOYEE NSC</p>
<p>AMP/LAE SC VIETNAM S/C</p>
<p>Select one of the following</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<blockquote>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue :</p>
</blockquote></td>
</tr>
</tbody>
</table>

### View Patient Demographics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can view the patient’s demographics by entering 1 at the <strong>“Enter 10-2319 screen to VIEW...”</strong> This includes the patient’s name, social security number, date of birth, address and phone, eligibility and benefits, and claim number, which is shown at the top of the 2319 form.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To view patient demographics, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Type “<strong>1</strong>” to select the <strong>Patient Demographics</strong> screen at the prompt, and press &lt;<strong>Enter</strong>&gt;.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>The patient demographics display as shown below.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>Press &lt;<strong>Enter</strong>&gt; to continue. If there is no entry for POW?, you may enter it at this time or press the <strong>&lt;Enter&gt;</strong> key to accept a default of NO.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">4</td>
<td>The current Disability Codes display if available.</td>
<td></td>
</tr>
<tr class="even">
<td><p>Patient Demographics Screen</p>
<p>Output</p>
<p>Disability Codes</p></td>
<td colspan="3"><p>Select one of the following:</p>
<p><strong>1 PATIENT DEMOGRAPHICS</strong></p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>1</strong> <strong>&lt;Enter&gt;</strong> PATIENT DEMOGRAPHICS</p>
<p>PROSPATIENT,ONE SSN: 000000001 DOB: JAN 1,1930 CLAIM#</p>
<p>Phone: Phone:</p>
<p>Current Address: Primary Next of Kin Address:</p>
<p>ABC STREET</p>
<p>CHICAGO, ILLINOIS 60000</p>
<p>Patient Type: PILL Period of Service: OTHER OR NONE</p>
<p>Primary Eligibility Code: Status: REQUIRED</p>
<p>NSC Eligibility Status:</p>
<p>Receiving A&amp;A Benefits? NO Receiving Housebound Benefits? NO</p>
<p>Receiving Social Security? NO Receiving VA Pension? NO</p>
<p>Receiving Military Retirement? NO Receiving VA Disability? NO</p>
<p>Prosthetic Disability Code(s): COS/B-NSC AMP/LAE-SC</p>
<p>Enter RETURN to continue or '^' to exit: <strong>&lt;Enter&gt;</strong></p>
<p>*POW? NO</p>
<p>Enter return to continue or `^` to exit: <strong>&lt;Enter&gt;</strong></p>
<p>Current Disability Codes are:</p>
<p>COS/B EMPLOYEE NSC</p>
<p>AMP/LAE SC VIETNAM S/C</p>
<p>ORTH/PLS INPATIENT S/C</p></td>
</tr>
</tbody>
</table>

### View Clinic Enrollments/Correspondence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can view the clinic enrollments and correspondence for the patient by selecting to view screen 2.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To view clinic enrollments and correspondence for a veteran, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Type 2 at the prompt: “Enter 10-2319 screen to VIEW (1-8)…” to select the Clinic Enrollments/Correspondence (2) screen.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>The following information displays: Last Movement Actions, Clinic Enrollments, and Pending Appointments.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td><p>Press &lt;<strong>Enter</strong>&gt; at the <strong>Would you like to see more clinics? No//</strong> prompt to accept the default setting or <strong>Y</strong> for <strong>Yes</strong>.</p>
<p>Note: This prompt may not appear if there aren’t many clinics.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">4</td>
<td>Press &lt;<strong>Enter</strong>&gt; to continue.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">5</td>
<td>To view correspondence, see next page, “<strong>View Letters on File</strong>.”</td>
<td></td>
</tr>
<tr class="odd">
<td>Clinic Enrollment/ Correspondence Screen</td>
<td colspan="3"><p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p><strong>2 CLINIC ENROLLMENTS/CORRESPONDENCE</strong></p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>2 &lt;Enter&gt;</strong> CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>PROSPATIENT,TWO SSN: 000-00-0002 DOB: FEB 28,1949 CLAIM#</p>
<p>Last Movement Actions</p>
<p>Trans. Type: DISCHARGE Trans. Type: ADMISSION</p>
<p>Date: JAN 12,1997@08:00 Date: JUN 5,1996@12:47:34</p>
<p>Type of Movement: Type of Movement:</p>
<p>REGULAR OPT-SC</p>
<p>Ward: 2AS Ward: 2AS</p>
<p>Physician: PROSPROVIDER,FIVE Physician: PROSPROVIDER,FIVE</p>
<p>Diagnosis: SOB Diagnosis: SOB</p>
<p>Clinic Enrollments</p>
<p>Clinic Enrollment Date OPT or AC</p>
<p>HOUSE/A MAY 17,1994 OPT</p>
<p>TEST1 NOV 1,1994@11:10 OPT</p>
<p>Would you like to see more clinics? No// n (No<strong>) &lt;Enter&gt;</strong></p>
<p>Pending Appointments</p>
<p>No Pending Appointments for this Patient</p>
<p>Enter RETURN to continue or '^' to exit: <strong>&lt;ENTER&gt;</strong></p></td>
</tr>
</tbody>
</table>

### View Letters/Correspondence on File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Clinic Enrollments</td>
<td><blockquote>
<p>You can also view the letters on file for the patient using <strong>Clinic Enrollments/Correspondence (2)</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps (continued)</td>
<td><blockquote>
<p>To view letters on file for a patient, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">6</td>
<td>The letter listings on file display for a patient if available.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">7</td>
<td>The <strong>Enter a number</strong> prompt displays to view a letter. Type the number of the letter you want to view or print and press &lt;<strong>Enter</strong>.&gt;</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">8</td>
<td>The <strong>DEVICE: HOME//</strong> prompt displays. Press &lt;<strong>Enter</strong>&gt; to continue to view the letter or enter a printer device. This example shows you how to view the letter.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">9</td>
<td>Press &lt;<strong>Enter</strong>&gt; again after the <strong>Right Margin: 80//</strong> prompt.</td>
<td></td>
</tr>
<tr class="even">
<td>Letters on File</td>
<td colspan="3"><p>Letters on file:</p>
<p># Patient Type of letter Employee Date of letter</p>
<p>------------------------------------------------------------------------------</p>
<p>1 PROSPATIENT,ONE ADP FL 10-90 PROSPROVIDER,THREE DEC 16, 1999</p>
<p>2 PROSPATIENT,ONE HO 30 DAY TEST PROSPROVIDER,THREE FEB 08, 2002</p>
<p>3 PROSPATIENT,ONE HO 30 DAY TEST PROSPROVIDER,THREE FEB 08, 2002</p>
<p>Enter '^' to stop or Enter a number (1-3):<strong>1 &lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>REQUEST FOR QUOTATION</p>
<p>Date: Mar 13, 2000</p>
<p>TO: VENDOR NAME FROM: PROSVENDOR,ONE</p>
<p>7000 SOUTH ST SUPPORT ISC</p>
<p>CHICAGO, ILLINOIS 60620</p>
<p>CHICAGO, IL 60619</p>
<p>Vendor Phone #: (555)</p>
<p>Veteran: PROSPATIENT,ONE</p>
<p>SSN: 000000001</p>
<p>Your firm is being considered for the following:</p>
<p>PROSTHETIC LEG</p>
<p>An estimate on the above-listed item(s) is requested. YOUR QUOTATION</p>
<p>DOES NOT CONSTITUTE A PURCHASE ORDER. Upon completion of the esti-</p>
<p>mate, return the original to the Veterans Affairs facility indicated</p>
<p>above and retain a copy for your files.</p>
<p>If approved, a purchase order will be prepared and forwarded to you.</p>
<p>Sincerely,</p>
<p>PROSPROVIDER,SIX, ACTING CHIEF, PROSTHETICS SERVICE CHIEF</p></td>
</tr>
</tbody>
</table>
View Letters/Correspondence on File, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Output</td>
<td><blockquote>
<p>A letter on file sample is shown below for a patient’s Vendor Estimate.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Steps (continued)</td>
<td><blockquote>
<p>To view letters on file, continue to follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">10</td>
<td>The letter(s) displays if available for a patient.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">11</td>
<td>At the <strong>Would you like to see more letters? No//</strong> prompt, press &lt;<strong>Enter</strong>&gt; to accept the default of <strong>No</strong>. If you want to view more letters that are on file, type <strong>Y</strong> for <strong>Yes</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">12</td>
<td>At the <strong>Do You wish to create a correspondence letter? No//</strong> prompt, press &lt;<strong>Enter</strong>&gt; to accept the default setting or type <strong>Y</strong> for <strong>Yes</strong>. (See the <strong>Correspondence</strong> section for instructions.)</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">13</td>
<td>The <strong>Suspense</strong> Menu may display for you to enter a request for a Prosthetic item or service (depending on the settings at your site).</td>
<td></td>
</tr>
<tr class="even">
<td>Sample Letter Screen</td>
<td colspan="3"><p>VENDOR'S ESTIMATE</p>
<p>(To be completed by Vendor)</p>
<p>----------------------------------------------------------------------</p>
<p>| Article or Service |Quantity| Unit |Unit Cost|Total Cost|</p>
<p>----------------------------------------------------------------------</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>| | | | | |</p>
<p>----------------------------------------------------------------------</p>
<p>| Vendor: Contract number (if applicable) |</p>
<p>| Address: |</p>
<p>| City: |</p>
<p>| State: Zip: |</p>
<p>| Telephone: |</p>
<p>| Date: Signature &amp; Title of Company Official|</p>
<p>| Note:List Terms/Discounts if Applicable |</p>
<p>----------------------------------------------------------------------</p>
<p>FL 10-90 ADP</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>Would you like to see more letters? No// <strong>&lt;ENTER&gt;</strong></p>
<p>Do you wish to create a correspondence letter? No// <strong>&lt;ENTER&gt;</strong></p></td>
</tr>
</tbody>
</table>

### View Entitlement Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can view the patient’s entitlement information by typing <strong>(3)</strong> at the “<strong>Enter 10-2319 screen to VIEW</strong>...” prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To view entitlement information, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Select the <strong>Entitlement Information</strong> screen by typing <strong>3.</strong></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>The patient name, social security number, date of birth, and claim number displays as well as any entitlements. This includes a clothing allowance if applicable, automobile information, and items returned.</td>
<td></td>
</tr>
<tr class="even">
<td>Entitlement Screen</td>
<td colspan="3"><p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p><strong>3 ENTITLEMENT INFORMATION</strong></p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>3 &lt;Enter&gt;</strong> ENTITLEMENT INFORMATION</p>
<p>PROSPATIENT,ONE SSN: 000-00-0001 DOB: JAN 1,1930 CLAIM#</p>
<p>PSC Issue Card: Appliance Ht 68 Wt 192 Eyes BR Hair GY Serial Number</p>
<p>JAN 31, 2000 TEST ITEM</p>
<p>Clothing Allowance: Date: 04-01-01 ELIGIBLE STATIC</p>
<p>Date of Exam: JUL 11, 2000</p>
<p>Examiner: PROSPROVIDER,EIGHT</p>
<p>Desc:</p>
<p>Date: 03-15-02 NOT-ELIGIBLE NON-STATIC</p>
<p>Date of Exam: MAR 10, 2002 Examiner: PROSPROVIDER,NINE</p>
<p>Desc:</p>
<p>Date: 05-08-02 ELIGIBLE STATIC</p>
<p>Date of Exam: MAY 08, 2002 Examiner: PROSPROVIDER,SEVEN</p>
<p>Desc: TESTING</p>
<p>Items Returned: Date Item Serial Status</p>
<blockquote>
<p>Enter RETURN to continue or '^' to exit:</p>
</blockquote></td>
</tr>
</tbody>
</table>

### View Appliance Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can view appliance transactions for the patient by typing <strong>4</strong> at the <strong>“Enter 10-2319 screen to VIEW...”</strong> prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To view entitlement information, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Select the <strong>Appliance Transactions</strong> screen by typing <strong>4</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>If you want to view the complete entry for a transaction, type the number of the transaction at the “<strong>Enter 1-n to show full entry...</strong>” prompt.</td>
<td></td>
</tr>
<tr class="even">
<td>Appliance Transactions Screen</td>
<td colspan="3"><blockquote>
<p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>4</strong> <strong>&lt;Enter&gt;</strong> APPLIANCE TRANSACTIONS</p>
<p>PROSPATIENT,TWO SSN: 000-00-0002 DOB: FEB 28,1949 CLAIM#</p>
<p>Date Qty Item Type Vendor Sta Serial Delivery Date Tot Cost</p>
<p>1. 02/16/00 1 TEST ITEM I VENDOR,TWO 499 9.00</p>
<p>2. 02/16/00 2 TEST ITEM I VENDOR,TWO 499 5.00</p>
<p>3. 02/16/00 1 EYEGLASSES I VENDOR,TWO 499 0.00</p>
<p>4. 05/07/03 1 WHEELCHAIR I VENDOR,THREE 05/07/03 300.00 +=Turned-In *=Historical Data I=Initial X=Repair S=Spare R=Replacement</p>
<p>Enter 1-19 to show full entry, '^' to exit or `return` to continue. <strong>4 &lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
View Appliance Transactions, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Continued…</td>
<td><blockquote>
<p>Below is the complete entry for the transaction selected previously.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance/ Repair Line Item Detail</td>
<td><p>PROSTHETICS,PATIENTONE SSN: 000-12-3456 DOB: 01-01-1000</p>
<p>APPLIANCE/REPAIR LINE ITEM DETAIL &lt;4-1&gt;</p>
<p>TYPE OF FORM: INITIATOR: DATE: OCT 01, 2013</p>
<p>DELIVER TO:</p>
<p>TYPE TRANS: INITIAL ISSUE QTY: SOURCE: COMMERCIAL</p>
<p>VENDOR:</p>
<p>DELIVERY DATE:</p>
<p>TOTAL COST: OBL:</p>
<p>REMARKS:</p>
<p>DISABILITY SERVED: NSC/OP</p>
<p>ITEM DESCRIPTION: COOKIE</p>
<p>APPLIANCE: COOKIE</p>
<p>CONTRACT #:</p>
<p>EXCLUDED/WAIVER:</p>
<p>PSAS HCPCS: A4364 ADHESIVE</p>
<p>ICD10 Code: A00.0 CHOLERA DUE TO VIBRIO CHOLERAE 01, BIOVAR CHOLERAE</p>
<p>CPT MODIFIER:</p>
<p>DESCRIPTION:</p>
<p>EXTENDED DESCRIPTION:</p>
<blockquote>
<p>Enter RETURN to continue or '^' to exit:</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Screen output</td>
<td><blockquote>
<p>Below is the continued screen output from the <strong>Appliance Transaction</strong> information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### View Auto Adaptive Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can view the patient’s auto adaptive information by typing <strong>5</strong> at <strong>the “Enter 10-2319 screen to VIEW...”</strong> prompt.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Auto Adaptive Screen</td>
<td><blockquote>
<p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>5</strong> AUTO ADAPTIVE INFORMATION</p>
<p>NAME: PTROSPATIENT,TWO SSN: 000000002 CLAIM NO.</p>
<p>VEHICLE ID# YEAR PURCHASE DATE MAKE MODEL PAGE 1</p>
<p>PROCESS DATE ITEM QTY COST AMIS TYPE</p>
<p>'*' Denotes Inactive Vehicle of Record</p>
<p>---------------------------------------------------------------------</p>
<p>VAN-123 199 MAR 13, 2000 FORD VAN 4502: MAR 13, 2000</p>
<p>MAR 13, 2000 AIR-CONDITIONING 1 $500.00 ADAP EQP INITIAL</p>
<p>MAR 13, 2000 CB RADIO 1 $100.00 VAN MOD INITIAL</p>
<p>Total/Date: $600.00</p>
<p>Enter RETURN to continue or '^' to exit:</p>
</blockquote></td>
</tr>
</tbody>
</table>

### View Critical Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can view, add, or edit any critical comments for the patient by typing 6 at the “<strong>Enter 10-2319 screen to VIEW</strong>...” prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To add or edit critical comments, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Select the <strong>Critical Comments</strong> option by typing <strong>6</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the Would you like to Add/Edit Patient Critical Comments? No// prompt, type Y for Yes, and press &lt;Enter&gt;.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>At the <strong>Edit? No//</strong> prompt, type <strong>Y</strong> for <strong>Yes</strong>, and press &lt;<strong>Enter</strong>&gt;.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">4</td>
<td>The word processing text editor displays for you to type your note.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">5</td>
<td>Press the <strong>Num Lock</strong> key and the <strong>E</strong> key together to exit and save the information.</td>
<td></td>
</tr>
<tr class="odd">
<td>Critical Comments Screen</td>
<td colspan="3"><blockquote>
<p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
</blockquote>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>6</strong> CRITICAL COMMENTS</p>
<p>PATIENT:PROSPATIENT,ONE CRITICAL COMMENTS</p>
<p>No Patient Critical Comments Recorded for this patient!</p>
<p>Would you like to Add/Edit Patient Critical Comments? No// <strong>Y</strong> (Yes)</p>
<p>CRITICAL COMMENTS:</p>
<p>No existing text</p>
<p>Edit? NO// <strong>YES</strong></p>
<p>==[ WRAP ]==[ INSERT ]======&lt; CRITICAL COMMENTS &gt;=====[ &lt;PF1&gt;H=Help]=</p>
<p><strong>Editing Critical Comments.</strong></p>
<p>&lt;======T======T======T======T======T======T======T======T======T&gt;====</p>
<p>PATIENT: PROSPATIENT,ONE CRITICAL COMMENTS</p>
<p>Editing Critical Comments.</p>
<p>Would you like to Add/Edit Patient Critical Comments? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>*Comments on file</p></td>
</tr>
</tbody>
</table>

### Add/Edit Disability Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can add to or edit the patient’s disability codes by typing <strong>7</strong> at the <strong>“Enter 10-2319 screen to VIEW...”</strong> prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To add or edit a Disability Code, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Select the <strong>Add/Edit Disability Code</strong> option by typing <strong>7</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the Would you like to Add/Edit a Disability Code to the Patient’s 2319? Yes// prompt, press &lt;Enter.&gt;</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>At the <strong>Select Prosthetic Disability Code</strong> prompt, type a Disability Code, and press <strong>&lt;Enter.&gt;</strong> (You can also type two question marks to view a list and select one.)</td>
<td></td>
</tr>
<tr class="odd">
<td>Add/Edit Disability Code Screen</td>
<td colspan="3"><blockquote>
<p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
</blockquote>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>7</strong> <strong>&lt;Enter&gt;</strong> ADD/EDIT DISABILITY CODE</p>
<p>Would you like to ADD/EDIT a Disability Code to the Patient's 2319? YES// &lt;<strong>Enter</strong>&gt;</p>
<p>Select PROSTHETIC DISABILITY CODE: <strong>?? &lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>AMP/LAE SC SC VIETNAM</p>
<p>COS/B NSC EMPLOYEE</p>
<p>You may enter a new PROSTHETIC DISABILITY CODE, if you wish</p>
<p>This is a pointer to the Prosthetic Disability Code file (662).</p>
<p>Choose from:</p>
<p>1 AMP/LAE</p>
<p>2 AMP/LAK</p>
<p>3 AMP/LBE</p>
<p>Select PROSTHETIC DISABILITY CODE: <strong>1</strong> <strong>&lt;Enter&gt;</strong> AMP/LAE</p>
<p>...OK? Yes// &lt;<strong>Enter&gt;</strong> (Yes)</p>
<p>SC SC VIETNAM</p>
<p>Select one of the following:</p>
<p>E EDIT DISABILITY CODE</p>
<p>A ADD DUPLICATE DISABILITY CODE</p>
<p>Enter response: EDIT// <strong>A</strong> <strong>&lt;Enter&gt;</strong> <strong>ADD DUPLICATE DISABILITY CODE</strong></p>
<p>PROSTHETIC DISABILITY CODE: AMP/LAE// <strong>&lt;Enter&gt;</strong></p></td>
</tr>
</tbody>
</table>
Add/Edit Disability Codes, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Add a Code</td>
<td><blockquote>
<p>To continue to add a Disability Code, see the sample screen below. At the <strong>Would you like to Mark a Disability Code as Deleted? NO//</strong> prompt, press &lt;<strong>Enter</strong>&gt; to accept the default setting.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To add or edit a Disability Code, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Select the <strong>Add/Edit Disability Code</strong> option by typing <strong>7</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><h5 id="addedit-disability-code-screen-continued">Add/Edit Disability Code Screen (continued)</h5></td>
<td colspan="3"><p>SERVICE/NON-SERVICE: <strong>??</strong></p>
<p>Enter `1` for Service Connected or `2` for Non-Service Connected.</p>
<p>Choose from:</p>
<p>1 SERVICE CONNECTED</p>
<p>2 NON-SERVICE CONNECTED</p>
<p>SERVICE/NON-SERVICE: <strong>2</strong> NON-SERVICE CONNECTED</p>
<p>ELIGIBILITY CATEGORY: <strong>??</strong></p>
<p>This field stores the Eligibility Category for the Patient.</p>
<p>Choose from:</p>
<p>1 SC VIETNAM</p>
<p>2 ALL OTHER SERVICE-CONNECTED</p>
<p>3 NSC A&amp;A</p>
<p>4 OTHERS ELIGIBLE</p>
<p>5 V.I.S.T.</p>
<p>6 VOC REHAB</p>
<p>7 PHC</p>
<p>8 INPATIENT</p>
<p>9 EMPLOYEE</p>
<p>10 PRIMA FACIA</p>
<p>ELIGIBILITY CATEGORY: <strong>1</strong> SC VIETNAM</p>
<p>Select PROSTHETIC DISABILITY CODE: <strong>&lt;Enter&gt;</strong></p>
<p>PROSPATIENT,ONE HAS THE FOLLOWING DISABILITY CODES:</p>
<p>COS/B NSC EMPLOYEE</p>
<p>AMP/LAE SC SC VIETNAM</p>
<p>AMP/LAE NSC SC VIETNAM</p>
<p>Would you like to Mark a Disability Code as Deleted? NO// <strong>&lt;Enter&gt;</strong></p>
<blockquote>
<p>*Comments on file</p>
</blockquote></td>
</tr>
</tbody>
</table>
Add/Edit Disability Codes, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>To Edit a Code</td>
<td><blockquote>
<p>You can edit and delete a Disability Code using this screen. To edit a disability code, type <strong>E</strong> for <strong>Edit Disability Code</strong> at the Enter Response prompt. Press <strong>&lt;Enter&gt;</strong> at the additional prompts to accept the default settings.</p>
<p>You delete a Disability Code for a patient by entering YES at the <strong>Would you like to Mark a Disability Code as Deleted? No//</strong> prompt.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Add/Edit Disability Code Screen</td>
<td><p>Select one of the following:</p>
<p>E EDIT DISABILITY CODE</p>
<p>A ADD DUPLICATE DISABILITY CODE</p>
<p>Enter response: <strong>EDIT// &lt;Enter&gt; DISABILITY CODE</strong></p>
<p>PROSTHETIC DISABILITY CODE: AO/AUTO// <strong>&lt;Enter&gt;</strong></p>
<p>SERVICE/NON-SERVICE: SERVICE CONNECTED// <strong>&lt;Enter&gt;</strong></p>
<p>ELIGIBILITY CATEGORY: SC VIETNAM// <strong>&lt;Enter&gt;</strong></p>
<p>Select PROSTHETIC DISABILITY CODE: <strong>&lt;Enter&gt;</strong></p>
<p>PROSPATIENT,ONE HAS THE FOLLOWING DISABILITY CODES:</p>
<p>COS/B NSC EMPLOYEE</p>
<p>AMP/LAE SC SC VIETNAM</p>
<p>AMP/LAE NSC SC VIETNAM</p>
<p>ORTH/PLS SC INPATIENT</p>
<p>ORTH/DLF SC SC VIETNAM</p>
<p>AO/AUTO SC SC VIETNAM</p>
<p>Would you like to Mark a Disability Code as Deleted? NO// <strong>&lt;Enter&gt;</strong></p>
<p>*Comments on file</p></td>
</tr>
</tbody>
</table>

### View Home Oxygen Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can view the patient’s home oxygen information by typing <strong>8</strong> at the <strong>“Enter 10-2319....”</strong> prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample output</td>
<td><blockquote>
<p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: <strong>8</strong> <strong>&lt;Enter&gt;</strong> HOME OXYGEN ITEMS</p>
<p>PROSPATIENT,THREE 000-00-0003</p>
<p>Current Prescription (#5)</p>
<p>Active Date: OCT 16,2003 Expiration Date: OCT 15,2004</p>
<p>CONCENTRATOR 02 @ 28% VIA COOL AEROSOL TRACH MASK, BUNN COMPRESSOR, M TANK</p>
<p>10 E TANKS, 4 TRACH MASKS, 6 1000 ML PREFILLED AND 4 500 ML AEROSOL BTLS</p>
<p>PER MO.</p>
<p>NEBULIZER .5 CC ALBUTEROL &amp; 2.5 CC IPRATROPRIUM,</p>
<p>2 #6 SHILEY TRACH TUBES CUFFED, UNFENESTRATED EVERY 6 MONTHS WITH NON-</p>
<p>DISPOSABLE INNER CANNULAS</p>
<p>Enter RETURN to continue or '^' to exit: <strong>&lt;Enter&gt;</strong></p>
<p>PROSPATIENT,THREE SSN: 000-00-0003 DOB: OCT 12,1954 CLAIM# 391580866</p>
<p>Date Qty Item Type Vendor Sta Serial Delivery Date Tot Cost</p>
<p>1. 01/27/04 4 HUMIDIFIER X FIRST COMM 695 02/11/04 26.60</p>
<p>4111</p>
<p>2. 01/27/04 1 OXYGEN-REN X FIRST COMM 695 02/11/04 90.25</p>
<p>4111</p>
<p>3. 01/27/04 1 OX-COMPRES X FIRST COMM 695 02/11/04 42.75</p>
<p>4111</p>
<p>4. 12/17/03 12 NEBULIZER I FIRST COMM 695 12/22/03 14.76</p>
<p>4111</p>
<p>5. 12/17/03 1 OXYGEN-REN X FIRST COMM 695 12/22/03 90.25</p>
<p>4111</p>
<p>6. 12/17/03 8 OXYGEN-REF X FIRST COMM 695 12/22/03 72.24</p>
<p>4111</p>
<p>7. 12/17/03 1 OX-COMPRES X FIRST COMM 695 12/22/03 42.75</p>
<p>4111</p>
<p>8. 11/24/03 4 HUMIDIFIER X FIRST COMM 695 12/05/03 26.60</p>
<p>4111</p>
<p>9. 11/24/03 4 NEBULIZER I FIRST COMM 695 12/05/03 4.92</p>
<p>4111</p>
<p>10. 11/24/03 1 OXYGEN-REN X FIRST COMM 695 12/05/03 90.25</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Transaction Inquiry (TI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### View a Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can view a single purchasing transaction through the <strong>Transaction Inquiry (TI)</strong> option from the <strong>Display/Print</strong> Menu. (This option displays purchasing information for a specific transaction from the Prosthetics 1358 file (#664.))</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To perform a transaction inquiry, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Type <strong>TI</strong> for the <strong>Transaction Inquiry</strong> option from the <strong>Display/Print</strong> Menu.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the Select Patient Name or Transaction Number prompt, type a patient name or transaction number, and press &lt;<strong>Enter</strong>&gt;.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>Select the transaction you want to view from the list of transactions displayed.</td>
<td></td>
</tr>
<tr class="odd">
<td>Transaction Inquiry Screen</td>
<td colspan="3"><p>23 Display/Print Patient 2319</p>
<p><strong>TI Transaction Inquiry</strong></p>
<p>IP Print All Prosthetic Items</p>
<p>BI Print Prosthetic Billings for MAS</p>
<p>IH Item History</p>
<p>SE Search for Recalled Item</p>
<p>SI Site Parameter Inquiry</p>
<p>VI Vendor Inquiry</p>
<p>Select Display/Print Option: <strong>TI</strong> <strong>&lt;Enter&gt;</strong> Transaction Inquiry</p>
<p>Select Patient Name or Transaction Number: <strong>PROVIDER1,TWO</strong> <strong>&lt;Enter&gt;</strong> PROSPATIENT,ONE 1-1-30</p>
<p>453890765 NO PILL HINES, IL</p>
<p>1 PATIENT,ONE 1-31-2000 PATIENT,ONEClosed REF: 0002 EYEGLASSES</p>
<p>2 PATIENT,ONE 1-31-2000 PATIENT,ONEClosed REF: 0003 TEST ITEM</p>
<p>3 PATIENT,ONE 1-31-2000 PATIENT,ONE REF: 0004 TEST ITEM</p>
<p>4 PATIENT,ONE 1-31-2000 PATIENT,ONE TEST ITEM</p>
<p>5 PATIENT,ONE 1-31-2000 PATIENT,ONE REF: 0003 PICKUP/DELIVERY</p>
<blockquote>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR CHOOSE 1-5: <strong>1 &lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
View a Transaction, continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print a transaction</td>
<td><blockquote>
<p>You can also print a transaction as well as view one.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps (continued)</td>
<td><blockquote>
<p>To perform a transaction inquiry, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td colspan="2">Action</td>
</tr>
<tr class="even">
<td colspan="2">4</td>
<td colspan="2">The Device prompt appears.</td>
</tr>
<tr class="odd">
<td colspan="2">5</td>
<td colspan="2">At the Device prompt, press &lt;<strong>Enter</strong>&gt; twice to display information to your terminal screen. (You can also type <strong>SLAVE</strong> to send the information to your printer, and press &lt;<strong>Enter</strong>&gt;.)</td>
</tr>
<tr class="even">
<td colspan="2">6</td>
<td colspan="2">The transaction information displays for the requested patient.</td>
</tr>
<tr class="odd">
<td>Transaction Inquiry Screen</td>
<td colspan="2"><p>1-31-2000 PROSPATIENT,ONE Closed REF: 0002 EYEGLASSES</p>
<p>DEVICE: &lt;<strong>Enter</strong>&gt; TELNET Right Margin: 80// &lt;<strong>Enter</strong>&gt;</p>
<p>PROSTHETICS 1358 LIST SEP 27,2000 09:46 PAGE 1</p>
<p>---------------------------------------------------------------------</p>
<p>DATE: JAN 31, 2000 PATIENT: PROSPATIENT,ONE</p>
<p>OBLIGATION NUMBER: 499-C45004 VENDOR: VENDOR PRODUCTION</p>
<p>C.P.: 499-94-2-055-0047 REFERENCE: 499-C45004-0002</p>
<p>CLOSE OUT DATE: JAN 31, 2000@13:05:53 INITIATOR: PROVIDER,THREE</p>
<p>EST. SHIPPING CHARGE: 1 SHIPPING ENTRY: JAN 31, 2000</p>
<p>STATION NAME: SUPPORT ISC</p>
<p>ITEM: EYEGLASSES BRIEF DESCRIPTION: ITEM 1</p>
<p>UNIT COST: 1 QTY: 1</p>
<p>UNIT OF ISSUE: EA TYPE OF TRANSACTION: INITIAL ISSUE</p>
<p>PATIENT CATEGORY: SC/OP SOURCE: COMMERCIAL</p>
<p>APPLIANCE/REPAIR: JAN 31, 2000 PSAS HCPCS: A4500</p>
<p>CLOSE-OUT REMARKS: CLOSE FORM TYPE: 2421</p>
<p>CLOSED BY: PROVIDER,THREE DELIVER TO: VETERAN</p>
<p>DATE REQUIRED: MAR 01, 2000 DELIVERY TIME: 30</p>
<p>Select Patient Name or Transaction Number: <strong>&lt;Enter&gt; to exit the screen.</strong></p></td>
<td></td>
</tr>
</tbody>
</table>

## Print All Prosthetic Items (IP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Print All Prosthetic Items (IP)</strong> option prints all Prosthetic Item Master records along with their new and repair AMIS codes. This listing is useful for Purchasing Agents as a catalog of all current Prosthetic items available for issue, and for Prosthetics Supervisors to validate correctness of Prosthetics AMIS codes.</p>
<p><u>Note</u>: Lab AMIS codes are not printed with this version of Prosthetics.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To print all Prosthetic items, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Type IP for the Print All Prosthetic Items option from the Display/Print Menu.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the Device prompt, press &lt;<strong>Enter</strong>&gt;. The following displays: Right Margin: 80//.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>Press &lt;<strong>Enter</strong>&gt;.</td>
<td></td>
</tr>
<tr class="odd">
<td>Print All Prosthetic Items Screen</td>
<td colspan="3"><p>23 Display/Print Patient 2319</p>
<p>TI Transaction Inquiry</p>
<p><strong>IP Print All Prosthetic Items</strong></p>
<p>BI Print Prosthetic Billings for MAS</p>
<p>IH Item History</p>
<p>SE Search for Recalled Item</p>
<p>SI Site Parameter Inquiry</p>
<p>VI Vendor Inquiry</p>
<p>Select Display/Print Option: <strong>IP</strong> <strong>&lt;Enter&gt;</strong> Print All Prosthetic Items</p>
<p>DEVICE: <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Recommendation</td>
<td><blockquote>
<p>It is recommended that you run this option quarterly to verify the AMIS codes that have been assigned. This will assure that you will receive proper calculations in your AMIS Worksheets.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### View the Prosthetic Item Master List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetic Item Master List</td>
<td><blockquote>
<p>You can view the Prosthetic Item Master List from the <strong>Print All Prosthetic Items (IP)</strong> option. Notice that the Item Master List below has three pages displayed with the Item Number, short description, and extended description.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print All Prosthetic Items Screen (continued)</td>
<td><p>PROS ITEM MASTER LIST SEP 27,2000 09:47 <strong>PAGE 1</strong></p>
<p>ITEM</p>
<p>NUMBER SHORT DESCRIPTION DESCRIPTION</p>
<p>------------------------------------------------------------------------------</p>
<p>3 SYRINGE-SUBCUTANEOUS-3I 3 IN SUBCUTANEOUS SYRINGE (3)</p>
<p>ANC: 05 A ARC: R01 ONC: 10 ORC: R15 A RNC: RRC:</p>
<p>ANC: 01 A ARC: R15 ONC: ORC: RNC: RRC:</p>
<p>ANC: 04 A ARC: R03 B ONC: 03 ORC: R15 A RNC: RRC:</p>
<p>59 EYEGLASSES EYEGLASSES</p>
<p>ANC: 11 ARC: R06 ONC: 10 ORC: R15 A RNC: 04 RRC: R13</p>
<p>10000 EYEGLASSES EYEGLASSES</p>
<p>ANC: 11 ARC: R06 ONC: ORC: RNC: RRC:</p>
<p>PROS ITEM MASTER LIST SEP 27,2000 09:47 <strong>PAGE 2</strong></p>
<p>ITEM</p>
<p>NUMBER SHORT DESCRIPTION DESCRIPTION</p>
<p>------------------------------------------------------------------------------</p>
<p>ANC: 04 A ARC: ONC: ORC: RNC: RRC:</p>
<p>903 TEST ITEM TEST</p>
<p>ANC: 05 D ARC: R15 ONC: ORC: R15 B RNC: RRC:</p>
<p>55 WHEELCHAIR-ADULT/HEMI/BLU STANDARD ADULT ROLLS 2000 HEMI WHEELCHAIR</p>
<p>WITH ELEVATING LEG REST AND ANTI TIPPER,</p>
<p>BLUE (55)</p>
<p>ANC: R14 ARC: R15 ONC: 10 ORC: R15 A RNC: 10 RRC: R12</p>
<p>56 WHEELCHAIR-CLASSIC-18X16 PREMIER CLASSIC STANDARD WIDTH AND DEPTH,</p>
<p>18X16, SEAT HEIGHT (19 3/4) BACK HEIGHT</p>
<p>STYLE 16 1/2IN, FIXED DETACHABLE DESK</p>
<p>LENGTH ARMS, REAR WHEEL SIZE 24X11IN,</p>
<p>BLACK MOLDED WITH SOLID SNAP ON TIRES,</p>
<p>CHROME PLATED STEEL HANDRIMS, PUSH TO LOCK</p>
<p>WHEEL LOCKS, 8X1 CASTERS, BLACK MOLDED</p>
<p>PROS ITEM MASTER LIST SEP 27,2000 09:47 <strong>PAGE 3</strong></p>
<p>ITEM</p>
<p>NUMBER SHORT DESCRIPTION DESCRIPTION</p>
<p>------------------------------------------------------------------------------</p>
<p>WITH SOLID TIRES, REGAL BLUE LEATHERETTE</p>
<p>UPHOLSTERY, CHROME FRAME FINISH (56)</p>
<p>ANC: 17 A ARC: R15 ONC: 12 ORC: R15 D RNC: 09 RRC:</p></td>
</tr>
</tbody>
</table>

## Print Prosthetic Billings for MAS (BI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Print Prosthetic Billings for MAS (BI)</strong> option prints all NSC (non-service connected) items issued to patients for billing purposes. MAS stands for Medical Administrative Services.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To view Prosthetic Billings for MAS, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Type BI for the Print Prosthetic Billings for MAS option from the Display/Print Menu.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the Site prompt, enter the name of the site and press <strong>&lt;Enter&gt;</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>At the <strong>Start With Delivery Date</strong> prompt, enter the beginning date of the date range. (For instance if the report should cover one year from the current date, enter T-365 which stands for “Today minus 365 days from today”).</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">4</td>
<td>At the <strong>End With Delivery Date</strong> prompt, type a <strong>T</strong> for <strong>Today</strong> if you want to enter the end of the date range with the current date.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">5</td>
<td>At the <strong>Device</strong> prompt, enter a printer or press &lt;<strong>Enter</strong>&gt;. The following displays: <strong>Right Margin: 80//</strong>. Press &lt;<strong>Enter</strong>&gt; again.</td>
<td></td>
</tr>
<tr class="odd">
<td>Print Prosthetic Billings for MAS Screen</td>
<td colspan="3"><p>23 Display/Print Patient 2319</p>
<p>TI Transaction Inquiry</p>
<p>IP Print All Prosthetic Items</p>
<p><strong>BI Print Prosthetic Billings for MAS</strong></p>
<p>IH Item History</p>
<p>SE Search for Recalled Item</p>
<p>SI Site Parameter Inquiry</p>
<p>VI Vendor Inquiry</p>
<p>Select Display/Print Option<strong>: BI</strong> Print Prosthetic Billings for MAS</p>
<p>SITE: Hines Development System// 499</p>
<p>Start With Delivery Date: <strong>T-365</strong> (SEP 28, 1999)</p>
<p>End With Delivery Date: <strong>T</strong> (SEP 27, 2000)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>...EXCUSE ME, JUST A MOMENT PLEASE...</p>
<p>...PREPARING TO PRINT PROSTHETIC BILLING...</p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchasing Menu</td>
<td><blockquote>
<p>Each transaction done through the <strong>Purchasing</strong> Menu requires the Prosthetic Purchasing Agent to enter the correct patient category for each item issued. Any item issued to a veteran who is NSC/OP and has insurance recorded in the MAS Patient file, will appear on this listing for billing purposes in MAS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### View Prosthetic Billing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing Information</td>
<td><blockquote>
<p>Below are the first two pages of the Prosthetic billing information for this sample.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Print Prosthetic Billings for MAS Screen (continued)</td>
<td><p>PATIENT NAME SSN SEP 28, 1999-SEP 27, 2000STA 499 <strong>PAGE 1</strong></p>
<p>------------------------------------------------------------------------------</p>
<p>TEST,A 5465</p>
<p>Insurance COB Subscriber ID Group Holder Effective Expires</p>
<p>===========================================================================</p>
<p>BLUE CROSS 9432 111 SELF 03/01/70</p>
<p>06/21/00 06/21/00 TEST ITEM QTY: 1 TOTAL COST: 1.00</p>
<p>PROSPATIENT,TWO 0002</p>
<p>Insurance COB Subscriber ID Group Holder Effective Expires</p>
<p>===========================================================================</p>
<p>AETNA 72727272 1633 SELF 01/01/90 01/01/99</p>
<p>BLUE CROSS p 088888888 3333 SELF 01/01/93</p>
<p>12/13/99 12/20/99* EYEGLASSES QTY: 1 TOTAL COST: 50.00</p>
<p>PATIENT NAME SSN SEP 28, 1999-SEP 27, 2000STA 499 PAGE 2</p>
<p>------------------------------------------------------------------------------</p>
<p>PROSPATIENT,TWO 0002</p>
<p>Insurance COB Subscriber ID Group Holder Effective Expires</p>
<p>===========================================================================</p>
<p>AETNA 72727272 1633 SELF 01/01/90 01/01/99</p>
<p>BLUE CROSS p 088888888 3333 SELF 01/01/93</p>
<p>12/13/99 12/13/99 EYEGLASSES QTY: 1 TOTAL COST: 5.00</p>
<p>12/13/99 12/13/99 WHEELCHAIR-ADULT/HEMI/BLUE-STD QTY: 1 TOTAL COST: 5.00</p>
<p>Enter RETURN to continue or '^' to exit: &lt;<strong>Enter</strong>&gt;</p></td>
</tr>
</tbody>
</table>
View Prosthetic Billing Information, continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing information</td>
<td><blockquote>
<p>Below are pages 3 and 4 of the Prosthetic billing information of this report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Print Prosthetic Billings for MAS Screen (continued)</td>
<td><p>PATIENT NAME SSN SEP 28, 1999-SEP 27, 2000STA 499 <strong>PAGE 3</strong></p>
<p>------------------------------------------------------------------------------</p>
<p>PROSPATIENT,TWO 0002</p>
<p>Insurance COB Subscriber ID Group Holder Effective Expires</p>
<p>===========================================================================</p>
<p>AETNA 72727272 1633 SELF 01/01/90 01/01/99</p>
<p>BLUE CROSS p 088888888 3333 SELF 01/01/93</p>
<p>12/13/99 12/13/99 EYEGLASSES QTY: 1 TOTAL COST: 50.00</p>
<p>12/13/99 12/13/99 EYEGLASSES QTY: 1 TOTAL COST: 50.00</p>
<p>12/13/99 12/13/99 EYEGLASSES QTY: 1 TOTAL COST: 50.00</p>
<p>12/13/99 12/13/99 EYEGLASSES QTY: 1 TOTAL COST: 50.00</p>
<p>12/13/99 12/13/99 EYEGLASSES QTY: 1 TOTAL COST: 5.00</p>
<p>12/13/99 12/13/99 WHEELCHAIR-ADULT/HEMI/BLUE-STD QTY: 1 TOTAL COST: 5.00</p>
<p>12/20/99 12/20/99 EYEGLASSES QTY: 1 TOTAL COST: 50.00</p>
<p>Enter RETURN to continue or '^' to exit: &lt;<strong>Enter</strong>&gt;</p>
<p>PATIENT NAME SSN SEP 28, 1999-SEP 27, 2000STA 499 <strong>PAGE 4</strong></p>
<p>------------------------------------------------------------------------------</p>
<p>PROSPATIENT,TWO 0002</p>
<p>Insurance COB Subscriber ID Group Holder Effective Expires</p>
<p>===========================================================================</p>
<p>AETNA 72727272 1633 SELF 01/01/90 01/01/99</p>
<p>BLUE CROSS p 088888888 3333 SELF 01/01/93</p>
<p>12/20/99 12/20/99 EYEGLASSES QTY: 1 TOTAL COST: 5.00</p>
<p>12/20/99 12/20/99 WHEELCHAIR-ADULT/HEMI/BLUE-STD QTY: 1 TOTAL COST: 5.00</p>
<p>12/20/99 12/20/99 EYEGLASSES QTY: 1 TOTAL COST: 50.00</p>
<p>12/20/99 12/20/99 EYEGLASSES QTY: 1 TOTAL COST: 5.00</p>
<p>12/20/99 12/20/99 WHEELCHAIR-ADULT/HEMI/BLUE-ST QTY: 1 TOTAL COST: 5.00</p>
<p>01/07/00 01/07/00 EYEGLASSES QTY: 1 TOTAL COST: 5.00</p>
<blockquote>
<p>01/07/00 01/07/00 EYEGLASSES QTY: 1 TOTAL COST: 5.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

### View Item History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Item History (IH)</strong> option from the <strong>Display/Print</strong> Menu prints the history of all purchases made for an item you select. It allows you to review the history of all items issued during any date range you may choose. You can view the request date, patient name, SSN, Vendor, Serial Number, quantity, total cost, and Initiator.</p>
<p>There are four types of transactions including: 1) Initial Issue, 2) Replacement,<br />
3) Repair, and 4) Spare. You can select multiple items to view at one time. This includes who received the item, cost of the item, quantity, purchased or issued, etc.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To view item history, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
|      |                                                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                         |
| 1    | Type IH for the Item History option from the Display/Print Menu.                                                                   |
| 2    | At the Site prompt, press \<Enter\> to accept the default Site or type two question marks to display and list and select a different site. |
| 3    | Once you have selected a site, an OK? Yes// prompt displays.                                                                               |
| 4    | Press \<Enter\> and another Select Item prompt displays.                                                                                   |
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item History Screen</td>
<td><p>23 Display/Print Patient 2319</p>
<p>TI Transaction Inquiry</p>
<p>IP Print All Prosthetic Items</p>
<p>BI Print Prosthetic Billings for MAS</p>
<p><strong>IH Item History</strong></p>
<p>SE Search for Recalled Item</p>
<p>SI Site Parameter Inquiry</p>
<p>VI Vendor Inquiry</p>
<p>Select Display/Print Option: <strong>IH</strong> &lt;<strong>Enter</strong>&gt; Item History</p>
<p>SITE: Hines Development System2// ST. NUM. 578</p>
<p>Select ITEM 1: <strong>??</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>Choose from:</p>
<p>3  THIS ITEM IS INACTIVE </p>
<p>7</p>
<p>9  THIS ITEM IS INACTIVE, USE ITEM NUMBER 11 </p>
<p>40</p>
<p>55</p>
<p>Select ITEM 1: <strong>3</strong></p>
<p>1 3  THIS ITEM IS INACTIVE </p>
<p>2 345-1234 55</p>
<p>CHOOSE 1-2: <strong>2</strong> &lt;<strong>Enter</strong>&gt; 55</p>
<p>...OK? Yes// (Yes) &lt;<strong>Enter</strong>&gt;</p>
<p>Select ITEM 2: <strong>&lt;Enter&gt;</strong> or enter another item.</p></td>
</tr>
</tbody>
</table>

### View Item History Within a Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item Master file</td>
<td><blockquote>
<p>Please note that the item number and the item name must correspond with what is contained in the Prosthetics Item Master file when you are requesting to view items in the <strong>Item History</strong> option.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps (continued)</td>
<td><blockquote>
<p>To view item history, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">5</td>
<td>At the <strong>Beginning Date: T-30//</strong> prompt, press &lt;<strong>Enter</strong>&gt; to accept this default setting. You can also enter a different entry for a beginning date.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">6</td>
<td>At the <strong>Ending Date: TODAY//</strong> prompt, press &lt;<strong>Enter</strong>&gt; to accept this default setting. You can also enter a different entry for an ending date.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">7</td>
<td>At the <strong>Device</strong> prompt, press &lt;<strong>Enter</strong>&gt;. The following displays: <strong>Right Margin: 80//</strong>. Press &lt;<strong>Enter</strong>&gt; again.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">8</td>
<td>The Item History displays.</td>
<td></td>
</tr>
<tr class="even">
<td>Item History Screen (continued)</td>
<td colspan="3"><p>Beginning Date: T-30// &lt;<strong>Enter</strong>&gt; (AUG 29, 2000)</p>
<p>Ending Date: TODAY// &lt;<strong>Enter</strong>&gt; (SEP 28, 2000)</p>
<p>DEVICE: HOME// &lt;<strong>Enter</strong>&gt; TELNET Right Margin: 80// &lt;<strong>Enter</strong>&gt;</p>
<p>...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...</p>
<p>ITEM HISTORY: WHEELCHAIR-ADULT/HEMI/BLUE-STD FOR ALL STA ST. NUM. 578P</p>
<p>AGE 1</p>
<p>REQUEST DATE PATIENT NAME SSN VENDOR AUG 29, 2000-SEP 28, 2000</p>
<p>SEP 25, 2000@11:56 PATIENT,FOUR 2750 Vendor SERIAL NBR: QTY: 1 TOTAL COST: 23.00 INITIAL ISSUE</p>
<p>INITIATOR: PROSPROVIDER,THREE</p>
<p>TOTAL DOLLARS SPENT ON THIS ITEM: $ 23.00 TOTAL QUANTITY ISSUED: 1</p></td>
</tr>
</tbody>
</table>

## Search for Recalled Item (SE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Search for Recalled Item (SE)</strong> option from the <strong>Display/Print</strong> Menu searches the RECORD OF PROS APPLIANCE/REPAIR file (#660) for a recalled item.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To search for a recalled item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Type SE for the Search for Recalled Item (SE) option from the Display/Print Menu.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the <strong>Site</strong> prompt, press &lt;<strong>Enter</strong>&gt; to accept the default Site or type two question marks to display a list and select a different site.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>At the <strong>Beginning Date</strong> prompt, enter a date for the beginning of the date range of the data you want to view, and press &lt;<strong>Enter</strong>&gt;. (For instance, if you want a range of a year of data, enter <strong>T-365</strong> for “Today minus 365 days from the current date.”)</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">4</td>
<td>At the <strong>Ending Date</strong> prompt, enter the end date of the date range of the data you want to view, and press &lt;<strong>Enter</strong>&gt;. (For instance, you can enter <strong>T</strong> for <strong>Today</strong> for the current date.)</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">5</td>
<td>At the <strong>Select one of the following</strong> prompts, a list of options display including: 1) <strong>Search by Serial Number or Lot Number</strong> or 2) <strong>Search by Item</strong>. Type the option that you want and press &lt;<strong>Enter</strong>&gt;.</td>
<td></td>
</tr>
<tr class="odd">
<td>Search for Recalled Item Screen</td>
<td colspan="3"><p>23 Display/Print Patient 2319</p>
<p>TI Transaction Inquiry</p>
<p>IP Print All Prosthetic Items</p>
<p>BI Print Prosthetic Billings for MAS</p>
<p>IH Item History</p>
<p><strong>SE Search for Recalled Item</strong></p>
<p>SI Site Parameter Inquiry</p>
<p>VI Vendor Inquiry</p>
<p>Select Display/Print Option<strong>: SE</strong> Search for Recalled Item</p>
<p>SITE: A 3456789012345678901234567890 LONG NAME// 499</p>
<p>Beginning Date: <strong>T-365</strong> (SEP 28, 1999)</p>
<p>Ending Date: <strong>T</strong> (SEP 27, 2000)</p>
<p>Select one of the following:</p>
<p>1 Search by Serial Number or Lot Number</p>
<p>2 Search by Item</p>
<p>Enter response: <strong>&lt;Enter&gt;</strong></p></td>
</tr>
</tbody>
</table>

### Search by Serial Number or Lot Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Search patterns</td>
<td><blockquote>
<p>Items issued through the Prosthetics stock program can be traced to an individual patient if either the item’s lot or serial number was recorded at the time of the issue. To use the <strong>Search by Serial Number or Lot Number</strong> option, some unique pattern in either the lot or serial number must be known.</p>
<p>For example, to find all issues to patients receiving an item with the Serial Number (or in the Lot Number) of <strong>90-222-98</strong>, enter <strong>90-</strong> at the “<strong>Enter Serial Number or Lot Number:</strong>” prompt. A search of the database will begin and the results may be sent to the screen or printer. Multiple results may display.</p>
<p>For this example, entering <strong>90-222</strong> or <strong>222</strong> would have given the same results. Entering 222-90 would NOT have found these transactions since 222-90 is NOT a pattern in either transaction’s Serial Number or Lot Number.</p>
<p><strong><u>Note</u>:</strong> You may also search by item name.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To search for a recalled item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Enter 1 for the Search by Serial Number or Lot Number.</td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the Enter Serial Number or Lot Number prompt, you can enter partial information to begin the search.</td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>At the Device prompt, press &lt;<strong>Enter</strong>&gt;. The following displays: Right Margin: 80//. Press &lt;<strong>Enter</strong>&gt; again.</td>
</tr>
<tr class="odd">
<td>Search by Serial Number or Lot Number Screen</td>
<td colspan="2"><blockquote>
<p>Select one of the following:</p>
<p>1 Search by Serial Number or Lot Number</p>
<p>2 Search by Item</p>
<p>Enter response: <strong>1</strong> Search by Serial Number or Lot Number</p>
<p>Enter Serial Number or Lot Number: <strong>9</strong></p>
<p>DEVICE: <strong>&lt;Enter&gt;</strong> HOME// TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>...HMMM, I'M WORKING AS FAST AS I CAN..</p>
<p>RECALLED ITEM REPORT</p>
<p>JUN 20, 1997-OCT 02, 2000 STA ST. NUM. 578 PAGE 1</p>
<p>REQUEST DATE PATIENT NAME SSN ITEM VENDOR</p>
<p>JUN 01, 2000 TEST,H 5612 TEST ITEM PROSVENDOR,THREE</p>
<p>LOT NBR: SERIAL NBR: K0429</p>
<p>END OF REPORT</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Search by Item Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <strong>Recalled Item Report</strong> displays the request date, patient name, SSN, item, and vendor.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To search for a recalled item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">6</td>
<td>At the <strong>Select ITEM</strong> prompt, type either an item number or two question marks to display a list and then select one.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">7</td>
<td>At the <strong>Device: HOME//</strong> prompt, press &lt;<strong>Enter</strong>&gt; twice to display the information to your terminal screen (or type <strong>SLAVE</strong> to print it).</td>
<td></td>
</tr>
<tr class="even">
<td>Search for Recalled Item Screen (continued)</td>
<td colspan="3"><p>Select one of the following:</p>
<p>1 Search by Serial Number or Lot Number</p>
<p>2 Search by Item</p>
<p>Enter response: 2 Search by Item Select ITEM: <strong>??</strong></p>
<p>Choose from:</p>
<p>3  THIS ITEM IS INACTIVE </p>
<p>7</p>
<p>9  THIS ITEM IS INACTIVE, USE ITEM NUMBER 11 </p>
<p>40</p>
<p>55</p>
<p>56</p>
<p>Select ITEM: <strong>3</strong></p>
<p>1 3  THIS ITEM IS INACTIVE </p>
<p>2 345-1234 55</p>
<p>CHOOSE 1-2: <strong>1</strong> &lt;<strong>Enter</strong>&gt; 3  THIS ITEM IS INACTIVE </p>
<p>...OK? Yes// &lt;<strong>Enter</strong>&gt; (Yes)</p>
<p>DEVICE: HOME// &lt;<strong>Enter</strong>&gt; TELNET Right Margin: 80// &lt;<strong>Enter</strong>&gt;</p>
<p>RECALLED ITEM REPORT SEP 28, 1999-SEP 27, 2000 STA 499 <strong>PAGE 1</strong></p>
<p>REQUEST DATE PATIENT NAME SSN ITEM VENDOR</p>
<p>MAY 19, 2000 PATIENT,TWO 8888 SYRINGE-SUBCUTA PROSVENDOR,THREE</p>
<p>LOT NBR: SERIAL NBR:</p>
<p>MAY 22, 2000 PATIENT,TWO 8888 SYRINGE-SUBCUTA PROSVENDOR,FIVE</p>
<p>LOT NBR: SERIAL NBR:</p>
<p>MAY 23, 2000 PATIENT,TWO 8888 SYRINGE-SUBCUTA PROSVENDOR,FIVE</p>
<p>LOT NBR: SERIAL NBR:</p>
<p>END OF REPORT</p></td>
</tr>
</tbody>
</table>
Search by Item Number, continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Example</td>
<td><blockquote>
<p>The following is an example of the usefulness of the <strong>Search for Recalled Item</strong> option:</p>
<p>A vendor calls the Prosthetic office to look for a patient’s name and/or purchase order number but all they have is the item that was purchased and the date of the purchase.</p>
<p>By using this option, you can locate the patient’s name and the item at the prompt that asks for the beginning and ending date.</p>
</blockquote>
<p>You would then access the patient’s 2319 which is located under the <strong>Display/Print</strong> option.</p>
<p>Select the Appliance Transactions option.</p>
<p>Select the date given to you by the vendor and enter the number that matches the date.</p>
<p>The number will show full entry, and you will be able to locate the purchase order number.</p></td>
</tr>
</tbody>
</table>

## Site Parameter Inquiry (SI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Site Parameter Inquiry</strong> <strong>(SI)</strong> option from the <strong>Display/Print</strong> Menu should be used to review your local site information.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To inquire on a site parameter, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td>Type ST for the Search for Recalled Item (ST) option from the Display/Print Menu.</td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td>At the <strong>Site</strong> prompt, type two question marks to display a list and select a site.</td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td>At the <strong>Device: HOME//</strong> prompt, press &lt;<strong>Enter</strong>&gt; twice to display the information to your terminal screen (or type <strong>SLAVE</strong> to print it).</td>
</tr>
<tr class="odd">
<td>Site Parameter Inquiry Screen</td>
<td colspan="2"><p>23 Display/Print Patient 2319</p>
<p>TI Transaction Inquiry</p>
<p>IP Print All Prosthetic Items</p>
<p>BI Print Prosthetic Billings for MAS</p>
<p>IH Item History</p>
<p>SE Search for Recalled Item</p>
<p><strong>SI Site Parameter Inquiry</strong></p>
<p>VI Vendor Inquiry</p>
<p>Select Display/Print Option: <strong>SI &lt;Enter&gt;</strong> Site Parameter Inquiry</p>
<p>Select PROSTHETICS SITE PARAMETERS SITE NAME: <strong>??</strong></p>
<p>Choose from:</p>
<p>Hines Development System</p>
<p>Hines Development System2</p>
<p>CORKWELL VAMC</p>
<p>HINESTEST</p>
<p>SAN ANTONIO VAMC</p>
<p>ZZOJ VAMC VAMC</p>
<p>Select PROSTHETICS SITE PARAMETERS SITE NAME: <strong>H &lt;Enter&gt;</strong></p>
<p>1 Hines System Development</p>
<p>2 Hines System Development2</p>
<p>CHOOSE 1-2: <strong>1</strong> <strong>&lt;Enter&gt;</strong> Hines System Development</p>
<p>DEVICE: <strong>1</strong> &lt;<strong>Enter</strong>&gt; P-SLAVE-CERA10 173C</p></td>
</tr>
</tbody>
</table>

## Vendor Inquiry (VI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Vendor Inquiry</strong> (VI) option from the <strong>Display/Print</strong> Menu provides a display of all information contained in IFCAP’s Vendor file. Enter the vendor’s name and the information is displayed. You can type two question marks to display a list of vendors to select one.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Display/Print Menu Screen</td>
<td><blockquote>
<p>23 Display/Print Patient 2319</p>
<p>TI Transaction Inquiry</p>
<p>IP Print All Prosthetic Items</p>
<p>BI Print Prosthetic Billings for MAS</p>
<p>IH Item History</p>
<p>SE Search for Recalled Item</p>
<p>SI Site Parameter Inquiry</p>
<p>VI Vendor Inquiry</p>
<p>Select Display/Print Option: <strong>VI &lt;Enter&gt;</strong> Vendor Inquiry</p>
<p>Select VENDOR NAME: <strong>?? &lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>1 PROSVENDOR,FOUR NO: 1</p>
<p>ORD ADD:M AND M AVENUE FMS:</p>
<p>HACKETTSTOWN, NJ 07840 CODE: FAX:555 555-1212</p>
<p>THIS VENDOR IS INACTIVE, NO REPLACEMENT VENDOR *</p>
<p>PLEASE CHOOSE ANOTHER VENDOR</p>
<p>2 PROSVENDOR,FIVE PH:555 555-5555 NO: 2</p>
<p>ORD ADD:1ST AVE NO 22ND FMS:</p>
<p>HINES, IL 60141 CODE: FAX:</p>
<p>3 PROSVENDOR,THREE PH:555-555-5555 NO: 3</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ANY PARK, IL 60064 CODE: FAX:</p>
<p>4 PROSVENDOR,SIX EDI PH:555 555-5555 NO: 4</p>
<p>ORD ADD:7701 SOUTH ST FMS:TEST TEST</p>
<p>CHICAGO, IL 60620 CODE: FAX:</p>
<p>5 PROSVENDOR,SEVEN PH:555 555-5555 NO: 5</p>
<p>ORD ADD:7501 S PULASKI FMS:</p>
<p>CHICAGO, IL 60652 CODE:FED000000 FAX:</p>
<p>^</p>
<p>Select VENDOR NAME: PROSVENDOR,SIX <strong>&lt;Enter&gt;</strong> PROSVENDOR,SIX EDIPH:555 555-5555NO:</p>
<p>4</p>
<p>ORD ADD:7701 SOUTH ST FMS:TEST TEST</p>
<p>CHICAGO, IL 60620 CODE: FAX:</p>
<p>...OK? Yes// (Yes) <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Vendor Inquiry Screen Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Vendor Report</td>
<td><blockquote>
<p>The Vendor report displays for the vendor selected. You can press &lt;<strong>Enter</strong>&gt; at the <strong>Device</strong> prompt, to display the information to your terminal or type <strong>SLAVE</strong> to send it to your printer for a hard copy.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Vendor Inquiry Screen</td>
<td colspan="2"><blockquote>
<p>DEVICE: <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>VENDOR LIST OCT 3,2000 15:13 PAGE 1</p>
<p>------------------------------------------------------------------------------</p>
<p>NUMBER: 4 NAME: PROSVENDOR,SIX</p>
<p>ORDERING ADDRESS1: 7701 SOUTH CLAREMONT</p>
<p>ORDERING CITY: CHICAGO ORDERING STATE: ILLINOIS</p>
<p>ORDERING ZIP CODE: 60620 PROCUREMENT CONTACT PERSON: PROVIDER,TEN</p>
<p>VENDOR PHONE NUMBER: (555) 555-5555 BILLING ADDRESS1: BILLING ADDRESS 1</p>
<p>BILLING ADDRESS2: BILLING ADDRESS 2 BILLING CITY: CHICAGO</p>
<p>BILLING STATE: ILLINOIS BILLING ZIP CODE: 60620</p>
<p>BILLING PHONE NUMBER: 555-5555</p>
<p>TYPE OF OWNERSHIP (FY88): V VIETNAM VETERAN - OWNED</p>
<p>SOCIOECONOMIC GROUP (FPDS): Q VIETNAM VET-OWNED SM</p>
<p>SOCIOECONOMIC GROUP (FPDS): S VETERAN-OWNED SM BUSINESS</p>
<p>BUSINESS TYPE (FPDS): SMALL LABOR SURPLUS AREA?: YES</p>
<p>BUSINESS TYPE (FPDS-88): SMALL IS A SF129 ON FILE?: YES</p>
<p>DATE OF SF129: OCT 23, 1992 GUARANTEED DELIVERY VENDOR?: NO</p>
<p>SPECIAL FACTORS: FAX#555-2509/FOB D EDI VENDOR?: YES</p>
<p>VENDOR ID NUMBER: 77778</p>
</blockquote></td>
</tr>
</tbody>
</table>

## <u>Section 3</u>: Purchasing Menu (PU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>Creating the Prosthetics purchase order is an involved process and includes the following:</p>
</blockquote>
<p>It combines patient information, vendor, item, obligation, and cost information on a single purchasing document.</p>
<p>It is integrated with six other VISTA applications including: PSAS, IFCAP, Consult Tracking, CPRS, Patient Care Encounters, DSS and Billing. They are integrated by exchange of data between applications.</p>
<p>It is also different because of the structure of the National Prosthetics Patient Database (NPPD) and the NPPD requirements.</p>
<p>Creating the PSAS purchasing document using IFCAP interface is a seamless process.</p>
<p>PSAS data (patient name, SSN, address, and phone number) are automatically printed on PSAS obligation document.</p></td>
</tr>
<tr class="even">
<td><h5 id="background">Background</h5></td>
<td><blockquote>
<p>PSAS has developed a customized <strong>Purchasing Menu</strong> in the prosthetics software package in VISTA, which calls into IFCAP, to alleviate the need to switch to and from various packages in VISTA or various screens. This reduced processing time of procuring devices/appliances and services for direct patient care.</p>
<p>The <strong>National Prosthetic Patient Database (NPPD)</strong> requires various fields, which are patient specific, to ensure we are adhering to eligibility criteria, and maintaining prescription, diagnosis, ordering, vendor, item, and accounting data is captured on the patients record. The need for one point of entry and seamless entry/order processing has proven effective in reducing delays and fast effective processing of orders.</p>
<p>PSAS is held to a five-day time limit in processing an order (again since it is for direct patient care), and VISN Directors performance standards state such.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="prosthetics-system">Prosthetics System</h5></td>
<td><blockquote>
<p>The Purchasing Menu (PU) is accessed from the Prosthetic Official’s Menu.</p>
</blockquote></td>
</tr>
</tbody>
</table>
Overview, continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="va-forms">VA Forms</h5></td>
<td colspan="2"><blockquote>
<p>Purchasing interfaces with IFCAP into the IFCAP 1358 module. Forms printed include the following:</p>
</blockquote>
<p>VAF 10-2421, Prosthetics Authorization and Invoice</p>
<p>Form Letter 10-55, Authority to Exceed Amount on Service Card.</p>
<blockquote>
<p>For tracking transactions associated with purchasing, Prosthetics will accommodate:</p>
</blockquote>
<p>VAF 10-2520, Prosthetic Service Card Invoice</p>
<p>VAF 10-2914, Prescription and Authorization for Eyeglasses - Computer entry of eyeglass prescriptions has been automated.</p>
<p>No-Form, Pickup/Delivery Charges</p>
<p>Request for Estimate (FL 10-55)</p>
<p>Patient Notification Letter.</p>
<blockquote>
<p>Listed below are all the menus and sub-menus that you will use for purchasing purposes. If the system does not allow you to access an option, contact your Fiscal Service and inform them that you need access to fund control points.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><h5 id="purchasing-menu-pu-1">Purchasing Menu (PU)</h5></td>
<td><blockquote>
<p>Select Prosthetic Official's Menu Option: PU Purchasing</p>
<p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p>CPC Cancel Purchase Card Transaction</p>
<p>CPO Reconcile/Close Out Purchase Card Transaction</p>
<p>ED2 Edit 2319</p>
<p>ED2C Edit 2319 (Vendor,QTY,Cost)</p>
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><h5 id="in-this-manual">In this manual</h5></td>
<td><blockquote>
<p>The following topics are covered under the Purchasing Menu:</p>
</blockquote></td>
</tr>
</tbody>
</table>
|                                             |          |
|---------------------------------------------|----------|
| Topic                                       | See Page |
| List Open 1358 Prosthetic Transactions (LI) | 61       |
| Close Out (CO)                              | 63       |
| Enter a New Request (EN)                    | 64       |
Overview, continued
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="stock-issues">Stock Issues</h5></td>
<td><blockquote>
<p>There is a separate <strong>Stock Issues User Manual</strong> that was developed with Patch RMPR*3*61 the Inventory/Bar Coding enhancement. Therefore, this menu and the menu options will not be explained in this basic manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchase-cards">Purchase Cards</h5></td>
<td><blockquote>
<p>There is also a <strong>Purchase Cards User Manual</strong> that is available from the Vista Document Library for you to download and therefore will not be explained in this basic manual.</p>
<p>The <strong>Purchase Cards User Manual</strong> also documents the following Purchasing options:</p>
</blockquote>
<p>Purchase Card Form (PC) – from the <strong>Enter New Request (EN) Menu</strong></p>
<p>CPC - Cancel Purchase Card Transaction</p>
<p>CPO - Reconcile/Close Out Purchase Card Transaction</p>
<p>LPC - List Open Purchase Card Transactions</p>
<p>LPCI - List Open Purchase Card Transactions By Initiator</p>
<p>LPS - Purchase Card Summary Sheet</p>
<p>Reprint a Purchase Card Form (PCR) – from the <strong>Reprints (RP) Menu</strong></p></td>
</tr>
</tbody>
</table>

### List Open 1358 Prosthetic Transactions (LI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-1">Introduction</h5></td>
<td><blockquote>
<p>The <strong>List Open 1358 Prosthetic Transactions (LI)</strong> option produces a report that will print the open 1358 transactions in the Prosthetics Package, sorted by initiator. However, it will not include manual transactions that were created in the IFCAP 1358 module. Once the transaction has been closed out, it will not appear on this report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="purchasing-pu-menu">Purchasing (PU) Menu</h5></td>
<td><p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p>CPC Cancel Purchase Card Transaction</p>
<p>CPO Reconcile/Close Out Purchase Card Transaction</p>
<p>ED2 Edit 2319</p>
<p>ED2C Edit 2319 (Vendor,QTY,Cost)</p>
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p><strong>LI List Open 1358 Prosthetic Transactions</strong></p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>LI &lt;Enter&gt; List Open 1358 Prosthetic Transactions</strong></p>
<p>This report lists open purchasing transactions created in the</p>
<p>Prosthetic Package. It will not include manual transactions done</p>
<p>in the IFCAP 1358 module.</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Starting Date: <strong>T-300</strong> <strong>&lt;Enter&gt;</strong> (JAN 31, 2001)</p>
<p>Ending Date: <strong>T</strong> <strong>&lt;Enter&gt;</strong> (NOV 27, 2001)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<blockquote>
<p>…Hmmm, I’m working as fast as I can</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><h5 id="section"></h5></td>
<td></td>
</tr>
<tr class="even">
<td><h5 id="site">Site</h5></td>
<td><blockquote>
<p>Multiple division sites are available</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="date-prompts">Date prompts</h5></td>
<td><blockquote>
<p>The date prompts determine the range of dates for which the report will be produced.</p>
</blockquote></td>
</tr>
</tbody>
</table>
List Open 1358 Prosthetic Transactions (LI), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="output">Output</h5></td>
<td><blockquote>
<p>Here’s the output:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-output">Screen output</h5></td>
<td><p>FROM: JAN 31, 2001-NOV 27, 2001 OPEN 1358 TRANSACTIONS STA 499 PAGE 1</p>
<p>PATIENT NAME SSN OBLIGATION REQUEST DATE VENDOR ITEM ITEM COST</p>
<p>PATIENT,FIVE 0005 A20012-0132 FEB 02, 2001 VENDOR,EIGHT TEST ITEM 0.01</p>
<p>PATIENT,FOUR 0004 A20012-0133 FEB 05, 2001 VENDOR,THREE TEST ITEM 0.01</p>
<p>PATIENT,FIVE 0005 A20012-0134 FEB 06, 2001 VENDOR,THREE TEST ITEM 0.01</p>
<p>PATIENT,FIVE 0005 A20012-0135 FEB 06, 2001 VENDOR,THREE EYEGLASSES 0.01</p>
<p>PATIENT,FOUR 0004 A20012-0140 MAY 22, 2001 VENDOR,NINE *SHIPPING 1.00</p>
<p>OXYGEN DEV 1.00</p>
<p>PATIENT,FOUR 0004 A20012-0141 JUL 10, 2001 VENDOR,TEN OXYGEN DEV 1.00</p>
<p>PATIENT,FOUR 0004 A20012-0142 JUL 16, 2001 VENDOR,THREE *DELIVERY 1.00</p>
<p>PATIENT,F0UR 0004 A20012-0143 JUL 19, 2001 VENDOR,THRE TEST ITEM 2.00</p>
<p>PATIENT,FOUR 0004 A20012-0144 JUL 19, 2001 VENDOR,TEN DELIVERY</p></td>
</tr>
</tbody>
</table>

### Close Out (CO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="menu-description">Menu description</h5></td>
<td><blockquote>
<p>The <strong>Close Out (CO)</strong> option is used to close out transactions when invoices are received from the vendor. This will update the actual VAF 1358 account balance.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="screen-sample-1">Screen sample</h5></td>
<td><blockquote>
<p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p>CPC Cancel Purchase Card Transaction</p>
<p>CPO Reconcile/Close Out Purchase Card Transaction</p>
<p>ED2 Edit 2319</p>
</blockquote>
<p>ED2C Edit 2319 (Vendor,QTY,Cost)</p>
<blockquote>
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>CO</strong> &lt;<strong>Enter</strong>&gt; Close Out</p>
<p>SITE: Hines Development System// &lt;<strong>Enter</strong>&gt; 499</p>
<p>Select OBLIGATION NUMBER: 499-A20012 07-01-97 1358 Obligated - 1358</p>
<p>FCP: 910 $ 2000.00</p>
<p>1358 Balance is $ 2911.23</p>
<p>Select PATIENT: 8-16-2001 PROSPATIENT,FOUR REF: 0167 SHOE COMPONENTS</p>
<p>PROSPATIENT,FOUR 000-00-0004 499-A20012</p>
<p>------------------------------------------------------------------------------</p>
<p>ITEM: 913 SHOE COMPONENTS AMIS: 20</p>
<p>PSAS HCPCS CODE: L3455 SHOE HEEL NEW LEATHER STANDA</p>
<p>CPT MODIFIER: LT,RT</p>
<p>REMARKS: TESTING</p>
<p>DESCRIPTION: TESTING</p>
<p>SERIAL NUMBER:</p>
<p>UNIT COST: 20 UNIT OF ISSUE: EA QTY: 1 ITEM COST: 20.00</p>
<p>TYPE: INITIAL CATEGORY: SC/OP SPECIAL CATEGORY:</p>
<p>SUB TOTAL: $ 20.00</p>
<p>% DISCOUNT: 5 $ 1.00</p>
<p>SHIPPING CHARGE: $ 2.00</p>
<p>TOTAL COST: $ 21.00</p>
<p>Ready to Close-Out Transaction? No// <strong>Y</strong> &lt;<strong>Enter</strong>&gt; (Yes)</p>
<p>CLOSE-OUT REMARKS: TESTING &lt;<strong>Enter</strong>&gt;</p>
<p>Updated 1 10-2319 record for this Veteran</p>
<p>Closed out Transaction</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Enter New Request (EN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="menu-description-1">Menu description</h5></td>
<td><blockquote>
<p><strong>Enter New Request (EN)</strong> option or to enter a new transaction, you must choose one of the menu options (purchasing forms) below. All the options listed under this menu are similar in several ways. Each form type will, upon posting, update the patient’s electronic 10-2319, and record the transaction to the 1358 obligation that you choose.</p>
<p>Once posted, these requests may only be closed out or cancelled. After you begin input into the computer, these forms must be completed to the point of posting to the 1358 obligation and patient's 10-2319 record. If the form is not completed, exiting the program during input of one of these forms will cause the transaction to be deleted. (This is unlike IFCAP where a transaction may be started and later edited.)</p>
<p><strong>Note:</strong> Prosthetics purchasing forms are not saved in the computer for editing later.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="enter-new-request-menu-en">Enter New Request Menu (EN)</h5></td>
<td><blockquote>
<p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p>CPC Cancel Purchase Card Transaction</p>
<p>CPO Reconcile/Close Out Purchase Card Transaction</p>
<p>ED2 Edit 2319</p>
</blockquote>
<p>ED2C Edit 2319 (Vendor,QTY,Cost)</p>
<blockquote>
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>EN</strong> &lt;<strong>Enter</strong>&gt; Enter New Request</p>
<p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p>PC Purchase Card Form</p>
<p>SS Purchase Card Site Parameter</p>
</blockquote></td>
</tr>
</tbody>
</table>
|                                         |          |
|-----------------------------------------|----------|
| Topic                                   | See Page |
| 2421 Form (24)                          | 65       |
| 2520 Transaction without printing 10-55 | 75       |
| 10-55 PSC Form (10)                     | 77       |
| 2914 Eyeglass Record (29)               | 80       |

### Enter a 2421 Form (24)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-2">Introduction</h5></td>
<td><blockquote>
<p>With the <strong>2421 Form (24)</strong> option, the user will create a 2421 Form for a selected patient. This form will update the patient’s electronic 10-2319, and record the transaction to the 1358 obligation that you choose. Once posted, this request may only be closed out or cancelled.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="when-do-you-use-this-option">When do you use this option?</h5></td>
<td><blockquote>
<p>You must use the <strong>2421 Form (24)</strong> option when a vendor does NOT accept the government purchase card. (This is another form of a Prosthetics Purchase Order using a 1358.)</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="what-is-the-process">What is the process?</h5></td>
<td><blockquote>
<p>After you access the <strong>2421 Form</strong> <strong>(24)</strong> option, this form must be completed to the point of posting to the 1358 obligation and patient's 10-2319 record. If it is not completed, exiting the program during input will cause the transaction to be deleted.</p>
<p>You will be prompted to enter the site, substation, obligation number, patient, and disability code(s) if none exists. If the patient already has disability codes, they will display.</p>
<p>You may view any of the 10-2319 patient screens (patient demographics, clinic enrollments/correspondence, entitlement information, appliance transactions, auto adaptive information, critical comments, add/edit disability code).</p>
</blockquote></td>
</tr>
</tbody>
</table>
Enter a 2421 Form (24), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="obligation-number">Obligation Number</h5></td>
<td><blockquote>
<p>This is the 1358 Number. This prompt will display: <strong>This will Create a 10-2421 Do you wish to Continue? Yes//</strong>. By pressing <strong>&lt;Enter&gt;</strong>, you accept the default answer of YES and are asked to select the Prosthetics 1358 patient.</p>
<p>The Obligation Number is also considered all the following: Procurement &amp; Accounting Transactions Purchase Order Number, or method of processing, or Depot Voucher No., or Supply Status, or Supply Status Order, or FCP or vendor, or Purchase Card holder, or Requisition No.(Supply), or Issue Voucher No.(Supply), or Issue Voucher No.(Fiscal), or Inventory/Distribution Point, or ISMS Order No.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps">Steps</h5></td>
<td colspan="4"><blockquote>
<p>To enter a <strong>2421 Form (24),</strong> follow these steps:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">1</td>
<td>Select the Form Type (i.e., 2421 Form (24)).</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">2</td>
<td>Enter the <strong>Site</strong> (if a multi-site facility).</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">3</td>
<td>Enter the 1358 Obligation Number.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><h5 id="form-screen">2421 Form screen</h5></td>
<td colspan="3"><blockquote>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select OBLIGATION NUMBER: <strong>?? &lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>499-A20003 11-24-95 1358 Cancelled Order</p>
<p>FCP: 910 $ 0.00</p>
<p>499-A20010 01-04-00 1358 Order Not Completely Prepared</p>
<p>FCP: 910 $ 0.00</p>
<p>499-A20012 07-01-97 1358 Obligated - 1358</p>
<p>FCP: 910 $ 2000.00</p>
<p>Select OBLIGATION NUMBER: 499-a20012 07-01-97 1358 Obligated - 1358</p>
<p>FCP: 910 $ 2000.00</p>
<p>1358 Balance is $ 2984.97</p>
<p>This will Create a 10-2421 Do you wish to Continue? Yes// <strong>Y &lt;Enter&gt;</strong> (Yes)</p>
</blockquote></td>
</tr>
</tbody>
</table>
Enter a 2421 Form (24), continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="prosthetic-patient">Prosthetic patient</h5></td>
<td><blockquote>
<p>The patient selected must be in both the MAS patient file and the Prosthetic Patient file. If the patient is not in the Prosthetic Patient file, but is in the MAS Patient file, you may enter the patient into the Prosthetic Patient file at this time.</p>
<p>The current Disability codes will be displayed for the selected patient. If there is no Prosthetic Disability Code entered for the patient, you must do so prior to continuing.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-1">Steps</h5></td>
<td><blockquote>
<p>To continue to enter a <strong>2421 Form (24),</strong> follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">4</td>
<td>Enter the <strong>Prosthetic Patient</strong>. The Disability Codes will display.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">5</td>
<td>Enter the <strong>Date</strong> or press <strong>&lt;Enter&gt;</strong> to accept the default setting.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">6</td>
<td>Select a <strong>Vendor</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><h5 id="screen-sample-2">Screen Sample</h5></td>
<td colspan="3"><blockquote>
<p>Select PROSTHETIC PATIENT: PATIENT,FOUR <strong>&lt;Enter&gt;</strong> PATIENT,FOUR 12-27-50 000654321 YES SC VETERAN</p>
<p>Enrollment Priority: GROUP 2 Category: IN PROCESS End Date:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>SUPPORT ISC</p>
<p>Current Disability Codes are:</p>
<p>AMP/LS INPATIENT S/C</p>
<p>BLD/TRE EMPLOYEE NSC</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue:</p>
<p>DATE REQUIRED: T+30// <strong>&lt;Enter&gt;</strong> (AUG 18, 2001)</p>
<p>VENDOR:<strong>??</strong></p>
<p>Enter the Vendor the item is being purchased from.</p>
<p>VENDOR: VENDOR,THREE <strong>&lt;Enter&gt;</strong> VENDOR,THREE PH:555 555-5555 NO: 3</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="date-required">Date Required</h5></td>
<td><blockquote>
<p>Press <strong>&lt;Enter&gt;</strong> at the <strong>Date Required</strong> prompt to accept the default response, which is today’s date plus 30 days. If another date is necessary (i.e., item is needed in one week), enter that date.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="vendor">Vendor</h5></td>
<td><blockquote>
<p>Select the Vendor for the item you are purchasing. If the computer does not recognize the vendor you select, you must first enter the vendor into the IFCAP file.</p>
<p>You may enter an <strong>^</strong> to exit the program at this time if you need to enter data into either of these files.</p>
</blockquote></td>
</tr>
</tbody>
</table>
Enter a 2421 Form (24), continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="contractboa-number">Contract/BOA Number</h5></td>
<td><blockquote>
<p>If the item you are purchasing is on contract with the vendor, enter the Contract Number at the prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="type-of-transaction">Type of Transaction</h5></td>
<td><blockquote>
<p>Enter a question mark (?) to view the choices for the <strong>Type of Transaction</strong> prompt. They are the following:</p>
</blockquote>
<p>I Initial Issue</p>
<p>R Replace</p>
<p>S Spare</p>
<p>X Repair</p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-2">Steps</h5></td>
<td><blockquote>
<p>To continue to enter a <strong>2421 Form (24),</strong> follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 0%" />
<col style="width: 27%" />
<col style="width: 0%" />
<col style="width: 71%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">7</td>
<td>Select a Contract/BOA Number.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">8</td>
<td>Select a Type of Transaction.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><h5 id="form-screen-continued">2421 Form Screen (continued)</h5></td>
<td colspan="3"><blockquote>
<p>Select CONTRACT/BOA NUMBER: <strong>?? &lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>V797P-5640M -- EXP. DATE: 12-31-95 MOL$100000 CONTRACT</p>
<p>V797P-5894M 02-09-00 EXP. DATE: 05-04-01 MIN$1000/MOL$15000</p>
<p>CONTRACT</p>
<p>Select CONTRACT/BOA NUMBER: <strong>v797p-5640M</strong> <strong>&lt;Enter&gt;</strong> -- EXP. DATE: 12-31-95 MOL $100000 CONTRACT</p>
<p>TYPE OF TRANSACTION: <strong>I</strong> &lt;<strong>Enter</strong>&gt; INITIAL ISSUE</p>
</blockquote></td>
</tr>
</tbody>
</table>
Enter a 2421 Form (24), continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="patient-category">Patient Category</h5></td>
<td><blockquote>
<p>The <strong>Patient Category</strong> includes the following:</p>
</blockquote>
<p>SC/OP (Service connected/Outpatient)</p>
<p>SC/IP (Service connected/Inpatient)</p>
<p>NSC/IP (Non-service connected/Inpatient)</p>
<p>NSC/OP (Non-service connected/Outpatient)</p>
<blockquote>
<p><strong>Note:</strong> If you select the NSC/OP option, a prompt for Special Category appears requiring you to select from one of four options (i.e., Special Legislation, AA, etc.)</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="item">Item</h5></td>
<td><blockquote>
<p>This is the item entered into the Prosthetic Item master list. You can search for an item using the question mark processing feature.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="psas-hcpcs">PSAS HCPCS</h5></td>
<td><blockquote>
<p>Enter the appropriate HCPCS (Health Care Financing Administration Common Procedure Coding System) code. Try the HCPCS, E1399 if unknown. This field should have the HCPCS code for the Item you are selecting. HCPCS is a uniform method to report professional services, procedures and supplies for healthcare providers and medical suppliers.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue to enter a <strong>2421 Form (24),</strong> follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Step | Action                                                                                      |
| 9    | Enter the Patient Category. (If the veteran is NSC/OP, then select a Special Category.) |
| 10   | Select the Item to be Issued or Repaired.                                               |
| 11   | Select the PSAS HCPCS and if necessary a CPT Modifier.                              |
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>2421 Form screen (continued)</td>
<td><blockquote>
<p>PATIENT CATEGORY: <strong>??</strong></p>
<p>Enter a code from the list.</p>
<p>Select one of the following:</p>
<p>1 SC/OP</p>
<p>2 SC/IP</p>
<p>3 NSC/IP</p>
</blockquote>
<ol start="4" type="1">
<li><blockquote>
<p>NSC/OP</p>
</blockquote></li>
</ol>
<blockquote>
<p>PATIENT CATEGORY: NSC/IP <strong>&lt;Enter&gt;</strong></p>
<p>Select ITEM: 913 SHOE COMPONENTS</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>PSAS HCPCS: L3455 <strong>&lt;Enter&gt;</strong> SHOE HEEL NEW LEATHER STANDA</p>
<p>Enter a CPT MODIFIER for HCPCS L3455: (LT/RT/B): Both Left and Right</p>
</blockquote></td>
</tr>
</tbody>
</table>
Enter a 2421 Form (24), continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="briefextended-description-of-item">Brief/Extended Description of Item</h5></td>
<td><blockquote>
<p>You can type a brief description of the item for that specific vendor. This description will print on the 10-2421 form for use by the vendor to determine what item is to be provided to the veteran.</p>
<p>At the Extended Description, you can further describe the item for the vendor in a text editor at the <strong>Edit?</strong> prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued-1">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue to enter a <strong>2421 Form (24),</strong> follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td colspan="2">12</td>
<td>Enter a brief and an extended description of the item (for the vendor).</td>
</tr>
<tr class="odd">
<td colspan="2">13</td>
<td>Enter the <strong>Quantity</strong> to be Purchased.</td>
</tr>
<tr class="even">
<td colspan="2">14</td>
<td>Enter Unit Cost.</td>
</tr>
<tr class="odd">
<td colspan="2">15</td>
<td>Enter Unit of Issue.</td>
</tr>
<tr class="even">
<td colspan="2">16</td>
<td>Enter <strong>Remarks</strong> (2310 and 1358).</td>
</tr>
<tr class="odd">
<td colspan="2">17</td>
<td>Establish a <strong>Shipping Charge</strong> (optional).</td>
</tr>
<tr class="even">
<td><h5 id="form-screen-continued-1">2421 Form screen (continued)</h5></td>
<td colspan="2"><blockquote>
<p>BRIEF DESCRIPTION OF ITEM (for Vendor): SHOE HEEL</p>
<p>EXTENDED DESCRIPTION:</p>
<p>No existing text</p>
<p>Edit? NO//</p>
<p>QTY: <strong>1</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>UNIT COST: <strong>2500</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>UNIT OF ISSUE: <strong>ea</strong> &lt;<strong>Enter</strong>&gt; EACH</p>
<p>REMARKS (2319 and 1358):</p>
<p>----------------------------------</p>
<p>EST. SHIPPING CHARGE:</p>
</blockquote></td>
</tr>
</tbody>
</table>
|                      |                                                                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------------------------------|
| Prompt               | Description                                                                                                               |
| Quantity             | Enter the number of the item you want to order – total amount of units issued for this item.                              |
| Unit Cost            | Enter the cost of one item to be purchased.                                                                               |
| Unit of Issue        | This field uses data from the IFCAP system (i.e., ea for Each).                                                           |
| Remarks              | Any Remarks you would like printed on the 1358 Obligation form and the 10-2319 should be entered here.                    |
| Est. Shipping Charge | The estimated shipping charge when the transaction is created. This field only holds the estimate, not the actual charge. |
Enter a 2421 Form (24), continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="percent-discount">Percent Discount</h5></td>
<td><blockquote>
<p>Contains the percent discount for the purchase. Estimated Cost and Actual Cost are calculated with the percent Discount.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="deliver-to">Deliver To</h5></td>
<td><blockquote>
<p>You have four selections of delivery locations to choose one.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued-2">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue to enter a <strong>2421 Form (24),</strong> follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td colspan="2">18</td>
<td>Enter a <strong>Percent Discount</strong> (if applicable).</td>
</tr>
<tr class="odd">
<td colspan="2">19</td>
<td><p>Select one of the following to <strong>Deliver To</strong>:</p>
<p>Veteran</p>
<p>VAMC Warehouse</p>
<p>Prosthetics</p>
<p>Other</p></td>
</tr>
<tr class="even">
<td colspan="2">20</td>
<td>Answer Yes or No at the following prompt: Are you ready to POST to IFCAP and 10-2319 NOW? No//</td>
</tr>
<tr class="odd">
<td>2421 Form screen (continued)</td>
<td colspan="2"><blockquote>
<p>PERCENT DISCOUNT: <strong>&lt;Enter&gt;</strong></p>
<p>DELIVER TO: <strong>?? &lt;Enter&gt;</strong></p>
<p>Enter a code from the list.</p>
<p>Select one of the following:</p>
<p>1 VETERAN</p>
<p>2 VAMC WAREHOUSE</p>
<p>3 PROSTHETICS</p>
<p>OTHER</p>
<p>DELIVER TO: PROSTHETICS <strong>&lt;Enter&gt;</strong></p>
<p>Are you ready to POST to IFCAP and 10-2319 NOW? No// <strong>NO &lt;Enter&gt;</strong> (No)</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="are-you-ready-to-post">Are you ready to Post?</h5></td>
<td><blockquote>
<p>The prompt, <strong>Are you ready to Post to IFCAP and the 2319 now?//No</strong> displays. The default answer for posting will always be <strong>NO</strong>. Accept the default answer by pressing the <strong>&lt;Enter&gt;</strong> key, so you may verify that the information entered on the request is correct. <u>The data entered displays for your review</u>.</p>
<p>If information is not correct, you have the option to edit the transaction as shown in the example on the next page.</p>
</blockquote></td>
</tr>
</tbody>
</table>
Enter a 2421 Form (24), continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display Entry</td>
<td><blockquote>
<p>The data entered displays below for your review if you accepted the default of <strong>NO</strong> at the <strong>Are you ready to Post to IFCAP and 10-2319 NOW?</strong> prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="form-screen-continued-2">2421 Form screen (continued)</h5></td>
<td><blockquote>
<p>PROSPATIENT,FOUR 000-00-0004 499-A20012</p>
<p>-----------------------------------------------------------------------------</p>
<p>ITEM: 903 TEST ITEM AMIS: 05 D</p>
<p>PSAS HCPCS CODE: VENDOR,FOUR HEART PACEMAKER, PERMANENT</p>
<p>CPT MODIFIER: GX</p>
<p>DELIVER TO: PROSTHETICS</p>
<p>DESCRIPTION: Heart Pacemaker, Permanent</p>
<p>SERIAL NUMBER:</p>
<p>UNIT COST: 2500 UNIT OF ISSUE: EA QTY: 1 ITEM COST: 2500.00</p>
<p>TYPE: INITIAL CATEGORY: NSC/IP SPECIAL CATEGORY:</p>
<p>SUB TOTAL: $2500.00</p>
<p>% DISCOUNT:</p>
<p>SHIPPING CHARGE: $ 0.00</p>
<p>TOTAL COST: $2500.00</p>
<p>Enter Item to Edit: 903 TEST ITEM</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
</blockquote></td>
</tr>
</tbody>
</table>
Enter a 2421 Form (24), continued
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="edit-the-form">Edit the form</h5></td>
<td><blockquote>
<p>You can now edit the prompts if you need to change anything on the order. Press <strong>&lt;Enter&gt;</strong> to view each prompt and accept the default entry shown.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued-3">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue to enter a <strong>2421 Form (24),</strong> follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Step</td>
<td colspan="2">Action</td>
</tr>
<tr class="even">
<td colspan="2">21</td>
<td colspan="2">Press <strong>&lt;Enter&gt;</strong> for each prompt that you do not want to edit.</td>
</tr>
<tr class="odd">
<td colspan="2">22</td>
<td colspan="2">None of the fields have been edited in the example below because the information is correct. When you are asked again <strong>Are you Ready to POST to IFCAP and 10-2319 NOW? NO//</strong> you can answer YES.</td>
</tr>
<tr class="even">
<td colspan="2">23</td>
<td colspan="2"><blockquote>
<p>A YES response at the <strong>Would you like to print the Privacy Act Statement?</strong> will print an additional page to the 10-2319.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2">24</td>
<td colspan="2">At the prompt, <strong>Would you like to print a Patient Notification letter?</strong> A YES response will print the Patient Notification letter on the purchasing printer defined in the Site Parameter File. You may also print the Patient Notification letter from the <strong>Reprint 2421 Form (24)</strong> option from the <strong>Reprints (RP)</strong> <strong>Menu</strong>.</td>
</tr>
<tr class="even">
<td><h5 id="form-screen-continued-3">2421 Form screen (continued)</h5></td>
<td colspan="3"><blockquote>
<p>TYPE OF TRANSACTION: INITIAL ISSUE// &lt;<strong>Enter</strong>&gt;</p>
<p>PATIENT CATEGORY: NSC/IP// &lt;<strong>Enter</strong>&gt;</p>
<p>ITEM: TEST ITEM// &lt;<strong>Enter</strong>&gt;</p>
<p>PSAS HCPCS: SI501// &lt;<strong>Enter</strong>&gt;</p>
<p>BRIEF DESCRIPTION: Heart Pacemaker, Permanent Replace &lt;Enter&gt;</p>
<p>EXTENDED DESCRIPTION: &lt;<strong>Enter</strong>&gt;</p>
<p>No existing text</p>
<p>Edit? NO// &lt;<strong>Enter</strong>&gt;</p>
<p>QTY: 1// &lt;<strong>Enter</strong>&gt;</p>
<p>UNIT COST: 2500// <strong>2</strong> &lt;<strong>Enter</strong>&gt;</p>
<p> Total for Previous Item(s) is $2500</p>
<p> Total With This Amount is $2</p>
<p>UNIT OF ISSUE: EA// &lt;<strong>Enter</strong>&gt;</p>
<p>REMARKS: &lt;<strong>Enter</strong>&gt;</p>
<p>EST. SHIPPING CHARGE: &lt;<strong>Enter</strong>&gt;</p>
<p>PERCENT DISCOUNT: &lt;<strong>Enter</strong>&gt;</p>
<p>DATE REQUIRED: AUG 18,2001// &lt;<strong>Enter</strong>&gt;</p>
<p>DELIVER TO: PROSTHETICS// &lt;<strong>Enter</strong>&gt;</p>
<p>Enter Item to Edit:</p>
<p>Are you ready to POST to IFCAP and 10-2319 NOW? No// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Would you like to print the Privacy Act Statement? Yes// Y <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Would you like to print a Patient Notification letter? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>Posting Now ...</p>
<p>1358 Transaction has been assigned Number: 499-A20012-0143</p>
<p>Updated 10-2319</p>
<p>DEVICE: HOME// &lt;<strong>Enter</strong>&gt; TELNET Right Margin: 80// &lt;<strong>Enter</strong>&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><h5 id="final-output">Final Output</h5></td>
<td colspan="3"><blockquote>
<p>Below is the output of the data from the 2421 Form (24) option. Then the Suspense Processing (SU) screen displays and allows you to perform an action on a Suspense item and link it to the item(s) you just ordered through the Stock Issues (SI) Menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="form-24-screen-final-output">2421 Form (24) Screen – Final Output</h5></td>
<td colspan="2"><blockquote>
<p>OMB Number 2900-0188 Estimated Burden: 4 minutes</p>
<p>*ORIGINAL COPY AND COMMERCIAL INVOICE MUST BE SUBMITTED*</p>
<p>TO THE VAMC PROSTHETIC ACTIVITY LISTED BELOW</p>
<p>______________________________________________________________________________</p>
<p>Department of Veterans Affairs|Prosthetics Authorization for Items or Services</p>
<p>------------------------------------------------------------------------------</p>
<p>1. Name and Address of Vendor 2. Name and Address of VA Facility</p>
<p>PROSVENDOR,THREE Hines Development System (499/121)</p>
<p>CORPORATE ORDER ENTRY TEST 2</p>
<p>PO BOX 1140 HINES, IL 60142</p>
<p>ANY PARK,IL 60064</p>
<p>(800) 255-5162 222</p>
<p>------------------------------------------------------------------------------</p>
<p>3. Veterans Name (Last, First, MI) 4. Date of Authorization</p>
<p>PROSPATIENT,FOUR JUL 19, 2001</p>
<p>------------------------------------------------------------------------------</p>
<p>5. Veterans Address 6. Date Required</p>
<p>100 HOLLYWOOD AUG 18, 2001</p>
<p>HOLLYWOOD,CALIFORNIA --------------------------------------</p>
<p>9. Authority For Issuance CFR 17.115</p>
<p>CHARGE MEDICAL APPROPRIATION</p>
<p>------------------------------------------------------------------------------</p>
<p>7. Claim Number 000654322P 8. SSN 000-00-0004</p>
<p>------------------------------------------------------------------------------</p>
<p>10. Statistical Data 11. FOB Point 12. Discount 13. Delivery Time</p>
<p>NSC/IP DEST % 30 Days</p>
<p>------------------------------------------------</p>
<p>14. Delivery To: PROSTHETICS</p>
<p>------------------------------------------------------------------------------</p>
<p>15. DESCRIPTION OF ITEMS OR SERVICES AUTHORIZED</p>
<p>------------------------------------------------------------------------------</p>
<p>ITEM NUMBER DESCRIPTION/NOMENCLATURE QUANTITY UNIT UNIT AMOUNT</p>
<p>ORDERED PRICE</p>
<p>------------------------------------------------------------------------------</p>
<p>#1. Heart Pacemaker, Permanent 1 EA 2.00 2.00</p>
<p>------------------------------------------------------------------------------</p>
<p>16. Contract Number: Subtotal: 2.00</p>
<p>ACCT.#: 17000000 Discount $ 0.00 Shipping: 0.00 Total $ 2.00</p>
<p>------------------------------------------------------------------------------</p>
<p>17. Signature and Title of 18. DATE 19. Signature and Title of 20. Date</p>
<p>Requesting Official Contracting/Accountable Officer</p>
<p>PROSPROVIDER1,ONE PROSPROVIDER,FOUR</p>
<p>------------------------------------------------------------------------------</p>
<p>Order and Receipt Action</p>
<p>------------------------------------------------------------------------------</p>
<p>21. Order Number 22. Date of Order 23. Date Item Received 24. Date Delivered</p>
<p>499-A20012-0143 JUL 19, 2001</p>
<p>------------------------------------------------------------------------------</p>
<p>25. The articles or services listed herein have been received, or rendered</p>
<p>ordered in the quantity and quality specified originally or as shown by</p>
<p>authenticated changes, except as noted.</p>
<p>Signature of Veteran or VA Official</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### Enter a 2520 Transaction without Printing 10-55 (25)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="description">Description</h5></td>
<td><blockquote>
<p>From the <strong>Purchasing (PU) Menu</strong> and the <strong>Enter New Request (EN) Menu</strong>, you can access the <strong>2520 Transaction without Printing (25)</strong> option. This is used for VAF 10-2520 PSC transactions that are under $300.00 and do not have an FL 10-55. It will then post to the VAF 1358 and patient's VAF 10-2319 record.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-3">Screen sample</h5></td>
<td><blockquote>
<p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p>PC Purchase Card Form</p>
<p>SS Purchase Card Site Parameter</p>
<p>Select Enter New Request Option: 25 &lt;Enter&gt; 2520 Transaction without printing 10-55</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select OBLIGATION NUMBER: 499-A20012 07-01-97 1358 Obligated - 1358</p>
<p>FCP: 910 $ 2000.00</p>
<p>1358 Balance is $ 2570.23</p>
<p>This will Create ALL OTHER Do you wish to Continue? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Select PROSTHETIC PATIENT: PATIENT,FOUR <strong>&lt;Enter&gt;</strong> SUPPORT ISC 12-27-50 00012275</p>
<p>0P YES SC VETERAN</p>
<p>Current Disability Codes are:</p>
<p>AMP/LS INPATIENT S/C</p>
<p>BLD/TRE EMPLOYEE NSC</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue:</p>
<p>Enter 'W' for WHEELCHAIR, 'O' for BRACE, 'B' for BLIND AIDS, 'A' for ART. LIMBS</p>
<p>Select PSC ITEM CATEGORY: <strong>?? &lt;Enter&gt;</strong></p>
<p>CHOOSE FROM:</p>
<p>W WHEELCHAIR</p>
<p>O BRACE</p>
<p>B BLIND AID</p>
<p>A ARTIFICIAL LIMB</p>
<p>Enter 'W' for WHEELCHAIR, 'O' for BRACE, 'B' for BLIND AIDS, 'A' for ART. LIMBS</p>
<p>Select PSC ITEM CATEGORY: W</p>
<p>You will not be able to exceed an item repair cost of more than $100.00.</p>
<p>Add/Edit/View Patient PSC? No// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Select PSC ISSUE CARD: <strong>?? &lt;Enter&gt;</strong></p>
<p>1 MAY 22, 2000 TEST 345-678</p>
<p>You may enter a new PSC ISSUE CARD, if you wish</p>
<p>This is the date the PSC card was issued.</p>
<p>Select PSC ISSUE CARD: 1 5-22-2000 TEST 345-678</p>
<p>PSC ISSUE CARD DATE: MAY 22,2000// <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
Enter a 2520 Transaction without Printing 10-55 (25), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-continued-3">Screen sample (continued)</h5></td>
<td><blockquote>
<p>ITEM: EYEGLASSES// <strong>??</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>This is the PSC item issued to the patient.</p>
<p>Choose from:</p>
<p>3 SYRINGE-SUBCUTANEOUS-3IN  THIS ITEM IS INACTIVE </p>
<p>55 WHEELCHAIR-ADULT/HEMI/BLUE-STD FOR ALL PATIENTS</p>
<p>56 WHEELCHAIR-CLASSIC-18X16</p>
<p>59 EYEGLASSES</p>
<p>99 OXYGEN CONCENTRATOR</p>
<p>100 OXYGEN DEVICE</p>
<p>903 TEST ITEM</p>
<p>912 WHEELCHAIR GLOVES</p>
<p>913 SHOE COMPONENTS</p>
<p>921 WHEELCHAIR - ELECTRIC</p>
<p>922 WHEELCHAIR - MANUAL</p>
<p>925 SHOES</p>
<p>10000 EYEGLASSES</p>
<p>ITEM: EYEGLASSES// &lt;<strong>Enter</strong>&gt;</p>
<p>DETAILED DESCRIPTION: TEST// &lt;<strong>Enter</strong>&gt;</p>
<p>SERIAL NUMBER: 345-678// &lt;<strong>Enter</strong>&gt;</p>
<p>Select PSC ISSUE CARD: <strong>??</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>1 MAY 22, 2000 TEST 345-678</p>
<p>You may enter a new PSC ISSUE CARD, if you wish</p>
<p>This is the date the PSC card was issued.</p>
<p>Select PSC ISSUE CARD: <strong>1</strong> &lt;<strong>Enter</strong>&gt; 5-22-2000 TEST 345-678</p>
<p>PSC ISSUE CARD DATE: MAY 22,2000// &lt;<strong>Enter</strong>&gt;</p>
<p>ITEM: EYEGLASSES// &lt;<strong>Enter</strong>&gt;</p>
<p>DETAILED DESCRIPTION: TEST// &lt;<strong>Enter</strong>&gt;</p>
<p>SERIAL NUMBER: 345-678// &lt;<strong>Enter</strong>&gt;</p>
<p>Select PSC ISSUE CARD: <strong>1</strong> &lt;<strong>Enter</strong>&gt; 5-22-2000 TEST 345-678</p>
<p>PSC ISSUE CARD DATE: MAY 22,2000// &lt;<strong>Enter</strong>&gt;</p>
<p>ITEM: EYEGLASSES// &lt;<strong>Enter</strong>&gt;</p>
<p>DETAILED DESCRIPTION: TEST// &lt;<strong>Enter</strong>&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

### 10-55 PSC Form (10)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="description-1">Description</h5></td>
<td><blockquote>
<p>From the <strong>Purchasing (PU) Menu</strong> and the <strong>Enter New Request (EN) Menu</strong>, you can access the <strong>10-55 PSC Form (10)</strong>. This will create a new FL 10-55 form and post purchasing data to patient's VAF 10-2319 record and update the Service's VAF 1358 obligation.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-10-55-psc-form-10">Sample 10-55 PSC Form (10)</h5></td>
<td><blockquote>
<p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p>PC Purchase Card Form</p>
<p>SS Purchase Card Site Parameter</p>
<p>Select Enter New Request Option: 10 10-55 PSC Form</p>
<p>SITE: Hines Development System//</p>
<p>Select STATION NUMBER: 499 SUPPORT ISC</p>
<p>Select OBLIGATION NUMBER: ??</p>
<p>Choose from:</p>
<p>499-A20003 11-24-95 1358 Cancelled Order</p>
<p>FCP: 910 $ 0.00</p>
<p>499-A20010 01-04-00 1358 Order Not Completely Prepared</p>
<p>FCP: 910 $ 0.00</p>
<p>499-A20012 07-01-97 1358 Obligated - 1358</p>
<p>FCP: 910 $ 2000.00</p>
<p>Select OBLIGATION NUMBER: <strong>499-A20012 &lt;Enter&gt;</strong> 07-01-97 1358 Obligated - 1358</p>
<p>FCP: 910 $ 2000.00</p>
<p>1358 Balance is $ 259.79</p>
<p>This will Create a PSC 10-55 Do you wish to Continue? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Select PROSTHETIC PATIENT: PROSPATIENT,ONE <strong>&lt;Enter&gt; PROSPATIENT,ONE</strong> 1-1-30 453890765</p>
<p>NO PILL</p>
<p>Enrollment Priority: Category: IN PROCESS End Date:</p>
<p>* Patient Requires a Means Test *</p>
<p>Primary Means Test Required from FEB 13,2002</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>HINES, IL</p>
</blockquote></td>
</tr>
</tbody>
</table>
10-55 PSC Form (10), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-continued">Screen (continued)</h5></td>
<td><blockquote>
<p>*Comments on file</p>
<p>Current Disability Codes are:</p>
<p>COS/B EMPLOYEE NSC</p>
<p>AMP/LAE SC VIETNAM S/C</p>
<p>AMP/LAE SC VIETNAM NSC Deleted...</p>
<p>ORTH/PLS INPATIENT S/C</p>
<p>*More Disability Codes on File, See Screen 1</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue:</p>
<p>Add/Edit/View Patient PSC? No// y (Yes)</p>
<p>Select PSC ISSUE CARD:</p>
<p>NAME SERIAL NUMBER</p>
<p>1. TEST ITEM</p>
<p>SELECT NUMBER: <strong>1 &lt;Enter&gt;</strong></p>
<p>VENDOR: PROSVENDOR,THREE PH:555 555-5555 NO: 3</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ANY PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>TYPE OF TRANSACTION: I <strong>&lt;Enter&gt;</strong> INITIAL ISSUE</p>
<p>PATIENT CATEGORY: 4 <strong>&lt;Enter&gt;</strong> NSC/OP</p>
<p>SPECIAL CATEGORY: 4 <strong>&lt;Enter&gt;</strong> ELIGIBILITY REFORM</p>
<p>PSAS HCPCS: A4254 <strong>&lt;Enter&gt;</strong> BATTERY FOR GLUCOSE MONITOR</p>
<p>DESCRIPTION OF ITEM (For Vendor): Battery</p>
<p>EXTENDED DESCRIPTION:</p>
<p>No existing text</p>
<p>Edit? NO//</p>
<p>QTY: 1// <strong>&lt;Enter&gt;</strong></p>
<p>UNIT COST: 20 <strong>&lt;Enter&gt;</strong></p>
<p>UNIT OF ISSUE: JB// <strong>&lt;Enter&gt;</strong> JOB</p>
<p>REMARKS (2319 and 1358): battery <strong>&lt;Enter&gt;</strong></p>
<p>EST. SHIPPING CHARGE: 2 <strong>&lt;Enter&gt;</strong></p>
<p>Are you ready to POST to IFCAP and 10-2319 NOW? No// y <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Would you like to print the Privacy Act Statement? Yes// n <strong>&lt;Enter&gt;</strong> (No)</p>
<p>Posting Now ...</p>
<p>1358 Transaction has been assigned Number: 499-A20012-0226</p>
<p>Updated 10-2319</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
10-55 PSC Form (10), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="letter-on-file-1">Letter on file</h5></td>
<td><blockquote>
<p>Below is the letter on file for the 10-55 PSC Form (10).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="sample-letter">Sample Letter</h5></td>
<td><blockquote>
<p>DEPARTMENT OF VETERANS AFFAIRS</p>
<p>Hines Development System</p>
<p>TEST 2</p>
<p>HINES, IL 60142</p>
<p>PROSVENDOR,THREE In Reply Refer to: -121</p>
<p>CORPORATE ORDER ENTRY PROSPATIENT,ONE</p>
<p>ANY PARK, IL 60064 000-00-0001</p>
<p>499-A20012-0226</p>
<p>PROSVENDOR,THREE</p>
<p>With reference to your request of 02/18/04, authority is granted to repair the appliance described below for the above-named veteran.</p>
<p>..........................................................................</p>
<p>DESCRIPTION OF APPLIANCE OR REPAIR</p>
<p>Unit Total</p>
<p>Item Name Serial Number Qty Price Cost</p>
<p>..........................................................................</p>
<p>903 TEST ITEM 1 $20.00</p>
<p>Battery</p>
<p>Shipping Charge: $2.00</p>
<p>The total cost, not including mailing cost, will not exceed $20.00</p>
<p>When repairs are completed, please attach the original of this letter to</p>
<p>the original copy of your invoice covering repair charges. Your invoice,</p>
<p>in original and one copy should then be forwarded to this office for</p>
<p>payment.</p>
<p>Please retain the duplicate copy of this letter for your files.</p>
<p>Sincerely,</p>
<p>PROVIDER,FOUR, Chief</p>
<p>CHIEF</p>
<p>Initiator: PROSPROVIDER1,ONE REF: 578 ADP FORM 10-55</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Eyeglass Record (29)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="description-2">Description</h5></td>
<td><blockquote>
<p>From the <strong>Purchasing (PU) Menu</strong> and the <strong>Enter New Request (EN) Menu</strong>, you can access the <strong>2914 Eyeglass Record (29)</strong>. This will create a VAF 10-2914 eyeglass record and post to the patient's VAF 10-2319 and VAF 1358 obligation.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="enter-new-request-menu">Enter New Request Menu</h5></td>
<td><blockquote>
<p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p>PC Purchase Card Form</p>
<p>SS Purchase Card Site Parameter</p>
<p>Select Enter New Request Option: <strong>29</strong> <strong>&lt;Enter&gt;</strong> <strong>2914 Eyeglass Record</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="eyeglass-record-screen-sample">2914 Eyeglass Record Screen sample</h5></td>
<td><blockquote>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong></p>
<p>Select STATION NUMBER: <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select OBLIGATION NUMBER: 499-A20012 07-01-97 1358 Obligated - 1358</p>
<p>FCP: 910 $ 2000.00 <strong>&lt;Enter&gt;</strong></p>
<p>1358 Balance is $ 237.79</p>
<p>This will Create an EYEGLASS 10-2914 Do you wish to Continue? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Select PROSTHETIC PATIENT: PROSPATIENT,ONE HINES, IL 1-1-30 000890765</p>
<p>NO PILL</p>
<p>*Comments on file</p>
<p>Current Disability Codes are:</p>
<p>COS/B EMPLOYEE NSC</p>
<p>AMP/LAE SC VIETNAM S/C</p>
<p>AMP/LAE SC VIETNAM NSC Deleted...</p>
<p>ORTH/PLS INPATIENT S/C</p>
<p>*More Disability Codes on File, See Screen 1</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
2914 Eyeglass Record (29), continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-continued-4">Screen sample (continued)</h5></td>
<td><blockquote>
<p>Enter a screen number (1-8) OR '^' TO EXIT.</p>
<p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: <strong>&lt;Enter&gt;</strong></p>
<p>VENDOR: PROSVENDOR,THREE PH:555 555-5555 NO: 3</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ANY PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>ITEM (for AMIS): ?? <strong>&lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>59 EYEGLASSES</p>
<p>10000 EYEGLASSES</p>
<p>ITEM (for AMIS): 59 <strong>&lt;Enter&gt;</strong> EYEGLASSES</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>TYPE OF TRANSACTION: I <strong>&lt;Enter&gt;</strong> INITIAL ISSUE</p>
<p>PATIENT CATEGORY: NSC OP <strong>&lt;Enter&gt;</strong></p>
<p>PSAS HCPCS: A4254 <strong>&lt;Enter&gt;</strong> Eyeglass</p>
<p>BRIEF DESCRIPTION: Eyeglass for a stigmatism <strong>&lt;Enter&gt;</strong></p>
<p>QTY: 1// <strong>&lt;Enter&gt;</strong></p>
<p>UNIT COST: 29.99 <strong>&lt;Enter&gt;</strong></p>
<p>UNIT OF ISSUE: ea <strong>&lt;Enter&gt;</strong> EACH</p>
<p>REMARKS (2319 and 1358): Ordered eyeglasses <strong>&lt;Enter&gt;</strong></p>
<p>EST. SHIPPING CHARGE: 3.50 <strong>&lt;Enter&gt;</strong></p>
<p>Are you ready to POST to IFCAP and 10-2319 NOW? No// y <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Posting Now ...</p>
<p>1358 Transaction has been assigned Number: 499-A20012-0227</p>
<p>Updated 10-2319</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix A – Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Question Mark Help</strong></td>
<td><blockquote>
<p>You can view online descriptive help for menus, options, and prompts. You can enter one, two, or three question marks to get extended online help in Prosthetics.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>? (Single question mark)</strong></td>
<td><blockquote>
<p>Entering a <strong>single question mark</strong> at a prompt provides you with a single line of standard help.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>?? (Double question mark)</strong></td>
<td><blockquote>
<p><strong>Two question marks</strong> entered at a prompt provide you with a list of choices appropriate to the prompt where you entered the question marks.</p>
<p>SITE: Hines Development System// <strong>?? &lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>ATLANTA VAMC 508</p>
<p>CORKWELL VAMC 500</p>
<p>HINESTEST 998</p>
<p>Hines Development System 499</p>
<p>SAN ANTONIO VAMC 671</p>
<p>ZZOJ VAMC VAMC 991</p>
<p>SITE: Hines Development System//</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Menu Options</strong></td>
<td><blockquote>
<p>You can enter <strong>three question marks</strong> to view Menu option descriptions.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>??? (Triple question mark)</strong></td>
<td><blockquote>
<p>Entering three question marks provides you with a brief description and a synonym:</p>
<p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p>PC Purchase Card Form</p>
<p>SS Purchase Card Site Parameter</p>
<p>Select Enter New Request Option: <strong>??? &lt;Enter&gt;</strong></p>
<p>'10-55 PSC Form' Option name: RMPR 10-55 Synonym: 10</p>
<p>This will create a new FL 10-55 form and post purchasing data to patient's VAF 10-2319 record and update the Service's VAF 1358 obligation.</p>
<p>'2421 Form' Option name: RMPR 2421 Synonym: 24</p>
<p>This option will create a new VAF 10-2421 form, post to the patient's</p>
<p>VAF 10-2319, and update the VAF 1358 obligation.</p>
<p>'2520 Transaction without printing 10-55' Option name: RMPR 2520 Synonym: 25</p>
<p>For VAF 10-2520 PSC transactions that are under $300.00 and do not have and FL 10-55. It will then post to the VAF 1358 and patient's VAF 10-2319 record.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix B - Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|        |                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------|
| Ad Hoc | An Ad-hoc has a specific purpose. Example: MS Access ad hoc query done to obtain specific data. |
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>AMIS</td>
<td><blockquote>
<p>Automated Management Information System.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Authorization</td>
<td><blockquote>
<p>An estimated payment that will be applied to the 1358.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Control Point</td>
<td><blockquote>
<p>The division of monies to a specified service, activity, or purpose from an appropriation. This is a financial element, existing only in IFCAP, that corresponds to the ACCS number in FMS.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cost Center</td>
<td><blockquote>
<p>Subsections of Fund Control Points. Cost centers allow fiscal staff to create total expense reports for a section or service, and requestors to assign requests to that section or service.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>DCT</td>
<td><blockquote>
<p>Document Confirmation Transactions</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Default</td>
<td><blockquote>
<p>A normal or suggested response to a prompt that is provided by the system.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Detailed Inventory ID</td>
<td><blockquote>
<p>A description of the item and/or where it can be found within a location.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>DSS</td>
<td><blockquote>
<p>Decision Support System</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>FMS</td>
<td><blockquote>
<p>Financial Management System (FMS), which has replaced CALM as the primary accounting system for administration appropriations.</p>
<p>FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security.</p>
<p>FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>FPDS</td>
<td><blockquote>
<p>Federal Procurement Data System.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Fund Control Point</td>
<td><blockquote>
<p>CALM accounting element that is not used by FMS.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Funds Distribution</td>
<td><blockquote>
<p>A group of fiscal options that allow the budget analyst to distribute funds to control points and track budget distribution reports information.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>GIP</td>
<td><blockquote>
<p>Generic Inventory package.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Grouper Counter</td>
<td><blockquote>
<p>The grouper counter is used to associate multiple entries in file 660, Record of Appliance/Repair, to a single patient. A post-init routine initially sets the counter for you at 99999999, then counts backwards. Do not edit this number.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS</td>
<td><blockquote>
<p>Healthcare Financing Administration Common Procedure Coding System. A code that represents an item or service.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>IFCAP</td>
<td><blockquote>
<p>Integrated Funds Distribution, Control Point Activity, Accounting and Procurement.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item File</td>
<td><blockquote>
<p>A listing of items specified by A&amp;MM as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers, and a procurement history.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item History</td>
<td><blockquote>
<p>Procurement information stored in the ITEM file. A history is kept by fund control point at the time of request.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item Master Number</td>
<td><blockquote>
<p>A computer-generated number used to identify an item in the ITEM file.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Location</td>
<td><blockquote>
<p>A specific area that contains prosthetic stock.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>MCCR</td>
<td><blockquote>
<p>Medical Care Cost Recovery</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>No-Form Daily Record</td>
<td><blockquote>
<p>The no-form type of purchasing transaction is used to record purchases from local Durable Medical Equipment (DME) contracts. Not all VAMCs use this type of contract. Items such as hospital beds, bath transfer equipment, etc. are examples of types of equipment purchased from a DME on this form.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NPPD</td>
<td><blockquote>
<p>National Prosthetics Patient Database</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Obligation</td>
<td><blockquote>
<p>The commitment of funds. The process that Fiscal Service completes to set aside monies to cover the cost of a purchase order.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Obligation Number</td>
<td><blockquote>
<p>The C prefix number that Fiscal Service assigns to the 1358.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Patient Category</td>
<td><blockquote>
<p>The patient’s service connection and patient status:</p>
<p>SC/OP</p>
<p>SC/IP</p>
<p>NSC/IP</p>
<p>NSC/OP</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Pickup and Delivery Charges Form</td>
<td><blockquote>
<p>Pickup and delivery charges must be included in AMIS information. This computer form records pickup and delivery charges when a local vendor is required by contract to pickup/deliver prosthetic items at a veteran’s home.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>PSAS Item</td>
<td><blockquote>
<p>Prosthetic Sensory Aids Service (PSAS) item that can be issued to a patient. There may be multiple PSAS items associated with one HCPCS:</p>
<p>Sling, arm extra large</p>
<p>Sling, arm medium</p>
<p>Sling, arm small</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>PSC</td>
<td><blockquote>
<p>Prosthetic Service Card</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order</td>
<td><blockquote>
<p>A government document authorizing the purchase of goods or services within the terms indicated.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchasing Agents</td>
<td><blockquote>
<p>A&amp;MM employees legally empowered to purchase goods and services from commercial vendors.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Reference Number</td>
<td><blockquote>
<p>Also known as the transaction number. The computer-generated number that identifies a request. It is comprised of the station number, fiscal year, quarter, control point, four-digit sequence number.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Re-order Level</td>
<td><blockquote>
<p>A level at which time a stock item should be re-ordered. A mailman message will appear daily indicating the re-order level has been reached.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Short Description</td>
<td><blockquote>
<p>The nomenclature that identifies the item in the ITEM MASTER file. It is restricted to three-to-sixty characters and consists of what the item is, what kind of item, and the size of the item (e.g., glove-surgical medium).</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site Parameters</td>
<td><blockquote>
<p>Information such as station number, cashier address, billing address, etc., that is unique to your station.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Source</td>
<td><blockquote>
<p>The distribution for the stock, either VA or Commercial.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Transaction</td>
<td><blockquote>
<p>Any action that affects a bill or an account. All transactions are numbered sequentially and may be examined individually.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Transaction Number</td>
<td><blockquote>
<p>The number of the transaction that funded a control point. It consists of the station, fiscal year, quarter, control point sequence number.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Type of Transaction</td>
<td><blockquote>
<p>A first-time issue, a repair of a previous issue, a spare, or a replacement of a stock item:</p>
<p>Initial = I</p>
<p>Repair = X</p>
<p>Spare = S</p>
<p>Replace = R</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Unit of Issue</td>
<td><blockquote>
<p>How the item is issued, e.g., box, each, bottle, etc.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA</td>
<td><blockquote>
<p>The Department of Veterans Affairs, formerly called the Veterans Administration.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form<br />
4-1358</td>
<td><blockquote>
<p>This VA form is used to record estimated obligations or changes in estimated obligations.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form<br />
10-2319</td>
<td><blockquote>
<p>Each time a patient receives medical equipment, supplier or services from Prosthetics Service, the item purchased is recorded on this form (Record of Appliance/Repair). This is an overall list of all appliances/repairs purchased for a veteran.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form<br />
10-2421</td>
<td><blockquote>
<p>This is the main purchasing authorization and invoice form for items or services issued by Prosthetics Service.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form<br />
10-2520</td>
<td><blockquote>
<p>This form is used to authorize repairs for prosthetic items/appliances prior to the item being sent to a vendor for repair.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form 10-2527</td>
<td><blockquote>
<p>Appointment roster and action sheet for clinics.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form<br />
10-2914</td>
<td><blockquote>
<p>Eyeglasses are authorized for purchase on this form.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form<br />
10-55</td>
<td><blockquote>
<p>This repair authorization form letter is used by Prosthetics Service to authorize repairs of prosthetic items/appliances sent directly to the vendor by the veteran, without prior Prosthetic Service approval on VA Form 10-2520.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form<br />
10-7306d (AMIS)</td>
<td><blockquote>
<p>This form tracks cumulative active prosthetics disability codes for AMIS calculations.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form 2237</td>
<td><blockquote>
<p>This form is used to request goods and services by a service/section, through A&amp;MM.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VA Form 2421PC</td>
<td><blockquote>
<p>This form keeps track of purchases that are used with a purchase card. Form 1358 is no longer available when a purchase card is used.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Vendor</td>
<td><blockquote>
<p>The company from which the item is purchased.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Vendor File</td>
<td><blockquote>
<p>An IFCAP file (440) of vendors that the facility conducts business. This file contains ordering and billing addresses, contract information, FPDS information, and telephone numbers.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>V<em>IST</em>A</td>
<td><blockquote>
<p>Veterans Health Information Systems and Technology Architecture, formerly Decentralized Hospital Computer Program of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA).</p>
<p>V<em>IST</em>A software, developed by the VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M and, via the Kernel, runs on all major M implementations regardless of vendor.</p>
<p>V<em>IST</em>A is composed of packages that undergo a verification process to ensure conformity with name spacing and other V<em>IST</em>A standards and conventions.</p>
</blockquote></td>
</tr>
</tbody>
</table>
