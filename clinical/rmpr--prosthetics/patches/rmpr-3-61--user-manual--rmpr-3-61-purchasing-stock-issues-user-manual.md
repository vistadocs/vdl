---
title: RMPR*3*61 Purchasing - Stock Issues User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Purchasing - Stock Issues
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*61
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: - [## Stock Issues User Manual](#stock-issues-user-manual) - [Issuing Stock](#issuing-stock) - [Appendix A](#appendix-a) - [Appendix B](#appendix-b) ![](rmpr-3-61-purchasing-stock-issues-user-manual/001.png) PROSTHETICSPURCHASING - STOCK ISSUESUSER MANUALPatch RMPR\3\61 March 2005 VISTA Health Syste
audience: 
keywords: 
  - strong
  - blockquote
  - table
  - colgroup
  - style
  - width
  - tbody
  - stock
  - class
  - issue
page_count: 0
word_count: 6586
section_count: 5
table_count: 24
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: March 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_p61_sium.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_p61_sium.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [## Stock Issues User Manual](#stock-issues-user-manual)
  - [Issuing Stock](#issuing-stock)
  - [Appendix A](#appendix-a)
  - [Appendix B](#appendix-b)
![](rmpr-3-61-purchasing-stock-issues-user-manual/001.png)
PROSTHETICSPURCHASING - STOCK ISSUESUSER MANUALPatch RMPR\*3\*61
March 2005
V*IST*A Health System Design and Development (HSD&D)
Table of Contents
Patch 61 Stock Issues User Manual [1](#stock-issues-user-manual)
Overview [1](#patch-rmpr361-overview)
Issuing Stock [2](#issuing-stock)
Administering a Stock Issue (IS) [2](#administering-a-stock-issue-is)
Edit/Delete Issue from Stock (ED) [8](#editdelete-issue-from-stock-ed)
List Open Stock Issues (PS) [14](#list-open-stock-issues-ps)
Appendix A [15](#appendix-a)
Glossary [15](#glossary)
Appendix B [16](#appendix-b)
Using Prosthetics Help [16](#using-prosthetics-help)

## ## Stock Issues User Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Patch RMPR\*3\*61 Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>The Prosthetics Patch RMPR*3*61 includes enhancements to the <strong>Stock Issues (SI)</strong> <strong>Menu</strong> (accessed from the <strong>Purchasing (PU) Menu</strong>). This option now has the barcode scanning functionality.</p>
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
<td><h5 id="barcode-scanning">Barcode scanning</h5></td>
<td><blockquote>
<p>A benefit of using a barcode scanner is that it takes much less time to scan vs. manually entering data at multiple prompts. Also there is less room for error. <u>The barcode label automatically provides the following information when scanned</u>:</p>
</blockquote>
<ul>
<li><p>Barcode number sequence</p></li>
<li><p>HCPCS Code</p></li>
<li><p>Item Cost</p></li>
<li><p>Date entered</p></li>
<li><p>IFCAP Item name</p></li>
<li><p>PIP Item description</p></li>
<li><p>Vendor</p></li>
<li><p>Location</p></li>
<li><p>Site</p></li>
</ul></td>
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
<td><h5 id="note-to-users">Note to Users</h5></td>
<td><p>Patch RMPR*3*61 is a large patch that involves careful setup PRIOR to installation and data conversion.</p>
<p><strong><u>This is extremely important</u>:</strong> Please review this <strong>Stock Issues User Manual</strong> and the following documents before installation:</p>
<ul>
<li><p>Forum Patch Module description</p></li>
<li><p>Prosthetics Inventory Package (PIP) Implementation Guide</p></li>
<li><p>Prosthetics Inventory Package (PIP) Lessons Learned</p></li>
<li><p>Prosthetics Inventory Package (PIP) User Manual.</p></li>
</ul>
<blockquote>
<p>Additionally, end users should review the manuals and Lessons Learned. Several major changes to the software are being introduced with this patch and the smoothness of adapting to these changes is directly related to end users having and reading these documents.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Issuing Stock

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Administering a Stock Issue (IS)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-1">Introduction</h5></td>
<td><blockquote>
<p>A common Prosthetic purchasing action is the <strong>Issue from Stock (IS)</strong> option. You can access this option from the <strong>Stock Issues (SI)</strong> Menu. The prompts you see when creating an Issue From Stock are recorded on the patient’s 10-2319 record like other purchasing transactions.</p>
<p><strong>Note:</strong> When stock is issued, the action affects the PIP by reducing the Inventory quantity on hand.</p>
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
<td><h5 id="steps">Steps</h5></td>
<td><blockquote>
<p>To access the <strong>Stock Issues Menu</strong>, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                    |
| 1    | From the Prosthetic Official’s Menu, type PU for the Purchasing Menu and press \<Enter.\> |
| 2    | Type SI for the Stock Issues Menu and press \<Enter\>.                                        |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="stock-issues-si-menu">Stock Issues (SI) Menu</h5></td>
<td><p>EN Enter New Request ...</p>
<p><strong>SI Stock Issues ...</strong></p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p>CPC Cancel Purchase Card Transaction</p>
<p>CPO Reconcile/Close Out Purchase Card Transaction</p>
<p>ED2 Edit 2319</p>
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<blockquote>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option<strong>: SI &lt;Enter&gt; Stock Issues</strong></p>
<p><strong>IS Issue From Stock</strong></p>
<p>ED Edit/Delete Issue From Stock</p>
<p>PS List Open Stock Issues</p>
<p>EL Enter Lab Issue from Stock</p>
<p>&gt; Out of order: USE STANDARD ISSUE FROM STOCK</p>
<p>LI Edit Lab Issue from Stock</p>
<p>&gt; Out of order: USE STANDARD ISSUE FROM STOCK</p>
<p>Select Stock Issues Option:</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="site">Site</h5></td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. Enter the site or a question mark to bring up a list of sites to select one.</p>
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
<td><h5 id="steps-continued">Steps (continued)</h5></td>
<td><blockquote>
<p>To issue from stock, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                               |
|------|-------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                        |
| 3    | From the Stock Issues (SI) Menu, select the Issue From Stock (IS) option by typing IS and pressing \<Enter\>. |
| 4    | Select the Site (if more than one Site can be selected).                                                                  |
| 5    | Select a Prosthetic patient.                                                                                                  |
| 6    | To either view the 2319 or continue, press \<Enter\> to continue.                                                         |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="issue-from-stock-is-option">Issue from Stock (IS) option</h5></td>
<td><blockquote>
<p>Select Purchasing Option: <strong>SI &lt;Enter&gt; Stock Issues</strong></p>
<p><strong>IS Issue From Stock</strong></p>
<p>ED Edit/Delete Issue From Stock</p>
<p>PS List Open Stock Issues</p>
<p>EL Enter Lab Issue from Stock</p>
<p>&gt; Out of order: USE STANDARD ISSUE FROM STOCK</p>
<p>LI Edit Lab Issue from Stock</p>
<p>&gt; Out of order: USE STANDARD ISSUE FROM STOCK</p>
<p>Select Stock Issues Option: <strong>IS &lt;Enter&gt;</strong> Issue From Stock</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
</blockquote>
<p>Select PROSTHETIC PATIENT: <strong>PROSpatient,one</strong> &lt;<strong>Enter&gt;</strong> PROSpatient,one 10-4-17 000009999 YES SC VETERAN</p>
<p>Enrollment Priority: GROUP 3 Category: IN PROCESS End Date:</p>
<p>...OK? Yes// &lt;<strong>Enter&gt;</strong> (Yes)</p>
<p>MILWAUKEE, WI</p>
<p>*Comments on file</p>
<p>Current Disability Codes are:</p>
<p>AO/DIS OTHERS ELIG NSC PL-104-262 (ELIG. REFORM</p>
<p>PPROSpatient,one</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: &lt;<strong>Enter&gt;</strong></p>
<blockquote>
<p>Entering a Stock Item!!!</p>
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
<td><h5 id="prosthetic-patient">Prosthetic Patient</h5></td>
<td><blockquote>
<p>Enter the name of the patient in the usual manner, i.e., last name, &lt;comma&gt;, first initial of first name, or first initial of last name plus last 4 numbers of the patient's social security number, or the full social security number without hyphens.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="type-of-transaction">Type of Transaction</h5></td>
<td><blockquote>
<p>Is it a first time issue, a repair of a previous issue, a spare, or are you replacing a previous issue? Choose one of the following at the <strong>Type of Transactions</strong> prompt:</p>
</blockquote>
<ul>
<li><p>INITIAL - I</p></li>
<li><p>REPAIR - X</p></li>
<li><p>SPARE - S</p></li>
</ul>
<ul>
<li><p>REPLACE - R</p></li>
</ul></td>
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
<td><h5 id="steps-1">Steps</h5></td>
<td><blockquote>
<p>To continue to issue from stock, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                |
|------|--------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                         |
| 7    | Select a Type of Transaction.                                                                                              |
| 8    | Select a Patient Category. If you select NSC/OP, then you will need to select a Special Category. (See next page.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-screen">Sample screen</h5></td>
<td><p>Select one of the following:</p>
<p>I INITIAL ISSUE</p>
<p>X REPAIR</p>
<p>R REPLACE</p>
<p>S SPARE</p>
<p>TYPE OF TRANSACTION: <strong>I</strong> &lt;<strong>Enter&gt;</strong>INITIAL ISSUE</p>
<p>PATIENT CATEGORY: <strong>??</strong> &lt;<strong>Enter&gt;</strong></p>
<p>Choose from:</p>
<p>1 SC/OP</p>
<p>2 SC/IP</p>
<p>3 NSC/IP</p>
<p>4 NSC/OP</p>
<p>PATIENT CATEGORY: <strong>4 NSC/OP</strong> &lt;<strong>Enter&gt;</strong></p></td>
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
<td><h5 id="patient-category">Patient Category</h5></td>
<td><blockquote>
<p>Enter the patient's service connection and inpatient or outpatient status at the time the stock was issued. Choose one of the following <strong>Patient Categories</strong>:</p>
</blockquote>
<ul>
<li><p>SC/OP</p></li>
<li><p>SC/IP</p></li>
<li><p>NSC/IP</p></li>
<li><p>NSC/OP</p></li>
</ul></td>
</tr>
</tbody>
</table>

Continued on next page

Administering a Stock Issue (IS), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="special-category">Special Category</h5></td>
<td><blockquote>
<p>If the patient is a <em><strong>NSC/OP</strong></em> patient, then the <strong>Special Category</strong> prompt appears. See sample screen below for the four options available with this prompt.</p>
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
<td><h5 id="steps-2">Steps</h5></td>
<td><blockquote>
<p>To continue to issue from stock, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                           |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                    |
| 9    | If the patient was an NSC/OP, then you must also select a Special Category.                                                                                       |
| 10   | Scan in the barcode label for the item. (You can also manually enter the alpha/numeric sequence under the barcode on the label and press \<Enter\> if necessary.) |
| 11   | If a CPT Modifier is associated with the item, this prompt will appear. Select Left, Right or Both and press \<Enter\>.                                           |
| 12   | The HCPCS, IFCAP Item and PIP Item description displays automatically.                                                                                                    |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-screen-1">Sample screen</h5></td>
<td><p>SPECIAL CATEGORY: <strong>??</strong> &lt;<strong>Enter&gt;</strong></p>
<p>If the patient is NSC/OP, then this field must also be set.</p>
<p>Choose from:</p>
<p><strong>1 SPECIAL LEGISLATION</strong></p>
<p><strong>2 A&amp;A</strong></p>
<p><strong>3 PHC</strong></p>
<p><strong>4 ELIGIBILITY REFORM</strong></p>
<p>SPECIAL CATEGORY: 1 &lt;<strong>Enter&gt;</strong> SPECIAL LEGISLATION</p>
<p>Scan in item bar code: <strong>??</strong></p>
<p>If you have access to a barcode scanner, use it to scan the item barcode now. Don't press the [Enter] key as the scanner should do this automatically.</p>
<p>If the scanner cannot read the barcode, type in the character sequence</p>
<p>immediately below the barcode.</p>
<p>Scan in item barcode: <strong>V2025-3020507120544 &lt;Enter&gt;</strong></p>
<p><mark>HCPCS: E0142 WALKER RIGID WHEELED WITH SE</mark></p>
<p><mark>IFCAP Item: WALKER</mark></p>
<p><mark>PIP Item desc.: WALKER</mark></p></td>
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
<td><h5 id="scan-in-item-barcode">Scan in item barcode</h5></td>
<td><blockquote>
<p>Scan in the item that you issued with the barcode reader at the <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Scan in item barcode</strong> prompt. You can also manually enter the character sequence immediately below the barcode.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New prompt with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="qty">QTY</h5></td>
<td><blockquote>
<p>This is the quantity issued.</p>
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
<td><h5 id="steps-3">Steps</h5></td>
<td><blockquote>
<p>To continue to issue from stock, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                        |
|------|------------------------------------------------------------------------|
| Step | Action                                                                 |
| 13   | Enter the Quantity of the item being issued.                       |
| 14   | Enter the Date of Service that the item was issued to the patient. |
| 15   | Enter the Serial Number (optional) or bypass this prompt.          |
| 16   | Enter the Lot Number (optional) or bypass this prompt.             |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-screen-2">Sample screen</h5></td>
<td><p>QTY: <strong>1</strong> <strong>&lt;Enter&gt;</strong></p>
<p>DATE OF SERVICE: FEB 05, 2003// <strong>??</strong> <strong>&lt;Enter&gt;</strong></p>
<p>This is the date when an item is issued to the patient.</p>
<p>Examples of Valid Dates:</p>
<p>JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057</p>
<p>T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.</p>
<p>T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.</p>
<p>If the year is omitted, the computer uses CURRENT YEAR. Two-digit year</p>
<p>assumes no more than 20 years in the future, or 80 years in the past.</p>
<p>You may omit the precise day, as: JAN, 2002</p>
<p>DATE OF SERVICE: FEB 05, 2003// <strong>T-1</strong> <strong>&lt;Enter&gt;</strong> (FEB 04, 2003)</p>
<p>SERIAL NBR: 12345 <strong>&lt;Enter&gt;</strong></p>
<p>LOT NUMBER: <strong>&lt;Enter&gt;</strong></p></td>
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
<td><h5 id="date-of-service">Date of Service</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Date of Service</strong> prompt defaults to the current date and is the date that the item was given or delivered to the patient. (See sample screen above for examples of valid date entries.)</p>
<p><strong>Note:</strong> If you issued stock last week, and you are entering the SI on a future date, you can change the date to the actual issue date.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New prompt with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="serial-and-lot-numbers-optional">Serial and Lot Numbers (Optional)</h5></td>
<td><blockquote>
<p>The <strong>Serial Number</strong> and the <strong>Lot Number</strong> can help track patients who have received items that have been recalled by either the manufacturer or the FDA.</p>
</blockquote>
<ul>
<li><p>The <strong>Serial</strong> <strong>Number</strong> (1 - 20 characters) is for the issued or repaired appliance.</p></li>
<li><p>The <strong>Lot Number</strong> (1 - 20 characters) stores the manufacturer’s lot number of the item being furnished to the patient.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Continued on next page

Administering a Stock Issue (IS), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="remarks">Remarks</h5></td>
<td><blockquote>
<p>Enter any additional information in the <strong>Remarks</strong> free-text field with a maximum of 61 characters. This should be detailed information about the item or the closeout, which appears on the 2319. This prompt can be bypassed.</p>
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
<td><h5 id="steps-4">Steps</h5></td>
<td><blockquote>
<p>To continue to issue from stock, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                               |
|------|---------------------------------------------------------------|
| Step | Action                                                        |
| 17   | Enter Remarks here (optional), and the Summary displays.  |
| 18   | You can now Post, Edit or Delete the Stock Issue. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="summary-screen">Summary screen</h5></td>
<td><p>REMARKS: {This appears on the 2319 only.} <strong>&lt;Enter&gt;</strong></p>
<p>==============================================================================</p>
<p>*STOCK ISSUE*</p>
<p>PATIENT NAME: PROSpatient,one SSN: 000009999</p>
<p>TYPE OF TRANSACTION: INITIAL ISSUE SOURCE: COMMERCIAL</p>
<p>PATIENT CATEGORY: NSC/OP SPECIAL CATEGORY: SPECIAL LEGISLATION</p>
<p>ITEM: WALKER VENDOR: HINES VA SUPPLY DEPOT</p>
<p>PSAS HCPCS: E0142 WALKER RIGID WHEELED WITH SE</p>
<p>HCPCS/ITEM: 1 E0142-1 C ODJ'S STICK</p>
<p>QUANTITY: 1 UNIT COST: 35.00 TOTAL COST: 35.00</p>
<p>SERIAL NUMBER: LOT NUMBER:</p>
<p>REMARKS: {Appears on the 2319.}</p>
<p>DATE OF SERVICE: JUL 08, 2002 Inventory Location: JLOC ==============================================================================</p>
<p>Would you like to POST/EDIT/DELETE this entry: (P/E/D): P//<strong>&lt;Enter&gt;</strong> OST</p>
<p>Posted to 2319...</p></td>
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
<td><h5 id="postedit-delete-prompt">Post/Edit/ Delete Prompt</h5></td>
<td><blockquote>
<p>At this last prompt, you may post the entry (which completes it), delete it (if it is the wrong patient), or edit/review other records pending for this patient. Accept the default answer of <strong>Post</strong> by pressing <strong>&lt;Enter&gt;</strong> to post to the patient’s 10-2319.</p>
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
<td><h5 id="trans-type">Trans Type</h5></td>
<td><blockquote>
<p>You are returned to the <strong>Transaction Type</strong> prompt to perform another stock issue for the same patient.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Edit/Delete Issue from Stock (ED)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="function-description">Function description</h5></td>
<td><blockquote>
<p>Use the <strong>Edit/Delete Issue from Stock</strong> <strong>(ED)</strong> option to edit the patient's VAF<br />
10-2319 after it has already been posted. You can do the following: edit if you issued the wrong item, correct Issue From Stock errors (edit all fields), and delete the record (if you selected the wrong patient).</p>
<p><strong>Note:</strong> If items are returned to inventory, this option is used, and the issued item can be deleted which returns the item to the PIP.</p>
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
<td><h5 id="ed2-qed2">ED2 &amp; QED2</h5></td>
<td><blockquote>
<p>Patch 61 has made changes in the <strong>Edit 2319 (ED2)</strong> option from the <strong>Purchasing (PU)</strong> Menu and <strong>Quick Edit 2319 Record (QED2)</strong> option from the <strong>NPPD Tools (ND) Menu</strong>. No prompts have been altered in these options. The only change with Patch 61 is that if the <strong>Form Type</strong> is a “<strong>Stock Issue</strong>,” then the <strong>ED2</strong> and <strong>QED2</strong> options cannot be edited as these transactions cannot be selected that were entered through the <strong>Stock Issues (SI) Menu</strong> option.</p>
<p>Editing of Stock Issues should <u>only</u> be done through <strong>Edit/Delete Stock Issue (ED)</strong> option, which in effect updates the PIP. Using this option will update PIP when a stock issue is deleted or if the Quantity or HCPCS code is being changed.</p>
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
<td><h5 id="steps-5">Steps</h5></td>
<td><blockquote>
<p>To edit a stock issue (or delete a stock issue), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                     |
| 1    | At the Select Stock Issues Option prompt, type ED for the Edit/Delete Issue From Stock option. |
| 2    | Select the Site (if more than one Site can be selected).                                               |
| 3    | Select a Prosthetic Patient.                                                                               |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="stock-issues-menu">Stock Issues Menu</h5></td>
<td><blockquote>
<p>Select Purchasing Option: <strong>SI &lt;Enter&gt; Stock Issues</strong></p>
<p>IS Issue From Stock</p>
<p><strong>ED Edit/Delete Issue From Stock</strong></p>
<p>PS List Open Stock Issues</p>
<p>EL Enter Lab Issue from Stock</p>
<p>&gt; Out of order: USE STANDARD ISSUE FROM STOCK</p>
<p>LI Edit Lab Issue from Stock</p>
<p>&gt; Out of order: USE STANDARD ISSUE FROM STOCK</p>
<p>Select Stock Issues Option: <strong>ED</strong> <strong>&lt;Enter&gt;</strong> Edit/Delete Issue From Stock</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select PATIENT: PROSpatient,one <strong>&lt;Enter&gt;</strong> PROSpatient,one 1-1-30 000890765</p>
<p>Enter &lt;RETURN&gt; to continue. HINES, IL</p>
<p>1 PROSpatient,one 5-31-2000 EYEGLASSES $ 5.00</p>
<p>2 PROSpatient,one 7-17-2000 ACCESSORY $ 1.06</p>
<p>3 PROSpatient,one 1-29-2001 OXYGEN DEVICE $ 400.00</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-3: <strong>3 &lt;Enter&gt;</strong> 1-29-2001 OXYGEN DEVICE $ 400.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="site-1">Site</h5></td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations.</p>
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
<td><h5 id="prosthetic-patient-1">Prosthetic Patient</h5></td>
<td><blockquote>
<p>Enter the name of the Prosthetic patient. For instance, enter the last name, &lt;comma&gt;, first initial of first name. You can also enter the first initial of last name plus the last 4 numbers of the patient's social security number, or the full social security number without hyphens.</p>
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
<td><h5 id="summary-review">Summary review</h5></td>
<td><blockquote>
<p>A summary of the stock issue appears so you may verify that this is the record you want. You may choose at this time to either delete the transaction or edit it.</p>
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
<td><h5 id="steps-6">Steps</h5></td>
<td><blockquote>
<p>To continue to edit a stock issue (or delete a stock issue), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                           |
| 4    | The summary displays so you may verify that this is the record you want. You can edit or delete the stock issue. Type “E” to edit it and press \<Enter\>. (You can delete the record by typing “D.”) |
| 5    | Edit the Type of Transaction or press \<Enter\> to accept the current selection.                                                                                                                         |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="summary-screen-1">Summary screen</h5></td>
<td><blockquote>
<p>==============================================================================</p>
<p>*STOCK ISSUE*</p>
<p>PATIENT NAME: PROSpatient,one SSN: 000890765</p>
<p>TYPE OF TRANSACTION: INITIAL ISSUE SOURCE: COMMERCIAL</p>
<p>PATIENT CATEGORY: NSC/OP SPECIAL CATEGORY: SPECIAL LEGISLATION</p>
<p>ITEM: CANE VENDOR: CROWN DRUG COMPANY</p>
<p>PSAS HCPCS: E0100 CANE ADJUST/FIXED WITH TIP</p>
<p>CPT MODIFIER: NU</p>
<p>HCPCS/ITEM: E0100-1 CANE – EXTRA LONG</p>
<p>QUANTITY: 3 UNIT COST: 25.00 TOTAL COST: 75.00</p>
<p>SERIAL NUMBER: 123456 LOT NUMBER:</p>
<p>REMARKS:</p>
<p>DATE OF SERVICE: APR 01, 2003 Inventory Location: HO 1</p>
<p>==============================================================================</p>
<p>Would you like to EDIT/DELETE this Transaction: (E/D): E// <strong>&lt;Enter&gt;</strong> EDIT</p>
<p>TYPE OF TRANSACTION: INITIAL ISSUE// <strong>&lt;Enter&gt;</strong> INITIAL ISSUE</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="type-of-transaction-1">Type of Transaction</h5></td>
<td><p>There are four options in the <strong>Type of Transaction</strong> prompt. Is it a first time issue, a repair of a previous issue, a spare, or are you replacing a previous issue? Change one of the following types of transactions to update the stock issue:</p>
<ul>
<li><blockquote>
<p>INITIAL - I</p>
</blockquote></li>
<li><blockquote>
<p>REPAIR - X</p>
</blockquote></li>
<li><blockquote>
<p>SPARE - S</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>REPLACE - R</p>
</blockquote></li>
</ul></td>
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
<td><h5 id="patient-category-1">Patient Category</h5></td>
<td><blockquote>
<p>Enter the patient's service connection and inpatient or outpatient status at the time the stock was issued. Change one of these <strong>Patient Category</strong> options to update the record:</p>
</blockquote>
<ul>
<li><p>SC/OP</p></li>
<li><p>SC/IP</p></li>
<li><p>NSC/IP</p></li>
<li><p>NSC/OP</p></li>
</ul></td>
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
<td><h5 id="special-category-1">Special Category</h5></td>
<td><blockquote>
<p>If the patient is a <strong>NSC/OP</strong> patient, then this prompt appears. Update one of the following if necessary: Special Legislation, A&amp;A, PHC, or Eligibility Reform.</p>
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
<td><h5 id="steps-7">Steps</h5></td>
<td><blockquote>
<p>To continue to edit a stock issue (or delete a stock issue), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                               |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                        |
| 6    | Edit the Patient Category (if necessary).                                                                                                                                 |
| 7    | Edit the Special Category (if necessary).                                                                                                                                 |
| 8    | At the Scan in item barcode prompt, you can press \<Enter\> to keep the current label information. For a new label, point and click the scanner on the barcode label. |
| 9    | Edit the old/new CPT Modifier field (if necessary).                                                                                                                       |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample">Screen sample</h5></td>
<td><blockquote>
<p>PATIENT CATEGORY: NSC/OP// <strong>&lt;Enter&gt;</strong> NSC/OP</p>
<p>SPECIAL CATEGORY: SPECIAL LEGISLATION// <strong>&lt;Enter&gt;</strong> SPECIAL LEGISLATION</p>
<p>Scan in item barcode: A4254-3011023135714 <strong>&lt;Enter&gt;</strong></p>
</blockquote>
<p>OLD CPT MODIFIER: <strong>NU</strong> <strong>&lt;Enter&gt;</strong></p>
<blockquote>
<p>NEW CPT MODIFIER: <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scan-in-item-barcode-1"><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Scan in item barcode</h5></td>
<td><blockquote>
<p>You can scan in the barcode label or manually enter the number for the item. Press <strong>&lt;Enter&gt;</strong> to keep the same barcode label information without scanning.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New prompt with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="vendor">Vendor</h5></td>
<td><blockquote>
<p>You can select a different <strong>Vendor</strong> for the Item in the Prosthetics Inventory.</p>
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
<td><h5 id="steps-8">Steps</h5></td>
<td><blockquote>
<p>To continue to edit a stock issue (or delete a stock issue), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                           |
|------|---------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                    |
| 10   | The HCPCS, IFCAP Item and PIP Item description automatically displays.                                                    |
| 11   | Edit the Vendor or press \<Enter\> to accept the current Vendor.                                                  |
| 12   | Press \<Enter\> to accept the default Source, or change it by typing either C for Commercial or V for VA. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-1">Screen sample</h5></td>
<td><p><mark>HCPCS: E0100 CANE ADJUST/FIXED WITH TIP</mark></p>
<p><mark>IFCAP Item: CANE</mark></p>
<p><mark>PIP Item desc.: CANE</mark></p>
<p>VENDOR:CROWN DRUG COMPANY// CROWN DRUG COMPANY PH:312 666-0981 NO: 11</p>
<p>ORD ADD:1640 WEST FULTON FMS:</p>
<p>CHICAGO, IL 60612 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<blockquote>
<p>SOURCE: C// <strong>&lt;Enter&gt;</strong> COMMERCIAL</p>
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
<td><h5 id="source">Source</h5></td>
<td><blockquote>
<p>The <strong>Source</strong> prompt is either the VA or Commercial.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="qty-1">Qty</h5></td>
<td><blockquote>
<p>This is the quantity issued.</p>
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
<td><h5 id="date-of-service-1">Date of Service</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Date of Service</strong> is the date the item was issued to a patient. This prompt can be edited if necessary.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>The Date of Service is a new prompt with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-9">Steps</h5></td>
<td><blockquote>
<p>To continue to edit a stock issue (or delete a stock issue), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Step | Action                                                                                         |
| 13   | Press \<Enter\> to accept the current Quantity or edit the amount.                     |
| 14   | Press \<Enter\> to accept the current Date of Service or edit the date (if necessary). |
| 15   | Press \<Enter\> to accept the current Serial Number or edit it.                        |
| 16   | Press \<Enter\> to accept the current Lot Number or edit it.                           |
| 17   | Edit any Remarks (if necessary).                                                           |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-2">Screen sample</h5></td>
<td><blockquote>
<p>QUANTITY: 3// <strong>2</strong> <strong>&lt;Enter&gt;</strong></p>
<p>DATE OF SERVICE: APR 01, 2003// <strong>&lt;Enter&gt;</strong> (APR 01, 2003)</p>
<p>SERIAL NBR: 123456// <strong>&lt;Enter&gt;</strong> 123456</p>
<p>LOT NUMBER: <strong>&lt;Enter&gt;</strong></p>
<p>REMARKS: <em><strong>Entered a different quantity</strong></em> <strong>&lt;Enter&gt;</strong></p>
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
<td><h5 id="serial-nbr">Serial Nbr</h5></td>
<td><blockquote>
<p>This is the <strong>Serial Number</strong> (1 - 20 characters) of the stock item. This prompt can be bypassed.</p>
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
<td><h5 id="lot-number">Lot Number</h5></td>
<td><blockquote>
<p>The <strong>Lot Number</strong> (1-20 characters) stores the manufacturer’s lot number of the item being furnished to the patient.</p>
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
<td><h5 id="remarks-1">Remarks</h5></td>
<td><blockquote>
<p>Enter any additional information here. This should be detailed information about the Item or the closeout. This field has a maximum of 61 characters.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="postedit-delete-prompt-1">Post/Edit/ Delete Prompt</h5></td>
<td><blockquote>
<p>At this point, you may post the entry, delete the entry, or edit it again if you missed a prompt that you need to edit.</p>
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
<td><h5 id="steps-10">Steps</h5></td>
<td><blockquote>
<p>To continue to edit a stock issue (or delete a stock issue), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>18</td>
<td><p>You can now <strong>Post</strong>, <strong>Edit</strong> or <strong>Delete</strong> the Stock Issue. At the <strong>Would you like to Post/Edit/Delete this entry: (P/E/D): P//</strong> prompt, press <strong>&lt;Enter&gt;</strong> to accept the default of <strong>Post</strong> to complete the edits that you have made to the 2319.</p>
<p><strong>Note:</strong> To delete the record at this point, type <strong>D</strong> and press <strong>&lt;Enter&gt;</strong> or type <strong>E</strong> to edit the record again if necessary.</p></td>
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
<td><h5 id="summary-screen-with-editdelete-prompt">Summary screen with Edit/Delete Prompt</h5></td>
<td><p>==============================================================================</p>
<p>*STOCK ISSUE*</p>
<p>PATIENT NAME: PROSpatient,one SSN: 000123456</p>
<p>TYPE OF TRANSACTION: INITIAL ISSUE SOURCE: Commercial</p>
<p>PATIENT CATEGORY: NSC/OP SPECIAL CATEGORY: SPECIAL LEGISLATION</p>
<p>ITEM: CANE VENDOR: CROWN DRUG COMPANY</p>
<p>PSAS HCPCS: E0100 CANE ADJUST/FIXED WITH TIP</p>
<p>CPT MODIFIER: NU</p>
<p>HCPCS/ITEM: E0100-1 CANE EXTRA LONG</p>
<p>QUANTITY: 2 UNIT COST: 25.00 TOTAL COST: 50.00</p>
<p>SERIAL NUMBER: 123456 LOT NUMBER:</p>
<p>REMARKS: Entered a different quantity</p>
<p>DATE OF SERVICE: APR 01, 2003 Inventory Location: HO 1</p>
<p>==============================================================================</p>
<p>Would you like to POST/EDIT/DELETE this entry: (P/E/D): P// <strong>&lt;Enter&gt;</strong> POST</p>
<p>Posting....</p></td>
</tr>
</tbody>
</table>

#### List Open Stock Issues (PS)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="function-description-1">Function description</h5></td>
<td><blockquote>
<p>The <strong>List Open Stock Issues (PS)</strong> option prints Stock Issues that do not have a date in the <em>Delivery Date</em> column of the 2319.</p>
<p><u>Recommendation</u>: Run this report periodically (minimum quarterly) to make sure that Delivery Dates are entered for all Stock Issues. The Delivery Date indicates that the Stock Issue has been posted.</p>
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
<td><h5 id="steps-11">Steps</h5></td>
<td><blockquote>
<p>To display a list of open Stock Issues, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                      |
| 1    | Select the List Open Stock Issues option by typing PS and press \<Enter.\>                                                                                                                      |
| 2    | At the Starting Date prompt, enter the beginning date of the date range you want to view the list of open stock issues. To enter a year date range, you can type T-365 and press \<Enter.\> |
| 3    | At the Ending Date prompt, to enter the end date of a one year range, type T for Today, and press \<Enter.\>                                                                            |
| 4    | At the Device prompt, press \<Enter\> twice and the report displays.                                                                                                                                |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-screen-3">Sample screen</h5></td>
<td><blockquote>
<p>IS Issue From Stock</p>
<p>ED Edit/Delete Issue From Stock</p>
<p><strong>PS List Open Stock Issues</strong></p>
<p>EL Enter Lab Issue from Stock</p>
<p>&gt; Out of order: USE STANDARD ISSUE FROM STOCK</p>
<p>LI Edit Lab Issue from Stock</p>
<p>&gt; Out of order: USE STANDARD ISSUE FROM STOCK</p>
<p>Select Stock Issues Option: <strong>PS</strong> <strong>&lt;Enter&gt;</strong> List Open Stock Issues</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Starting Date: <strong>T-365</strong> <strong>&lt;Enter&gt;</strong> (DEC 30, 2002)</p>
<p>Ending Date: <strong>T</strong> <strong>&lt;Enter&gt;</strong> (DEC 30, 2003)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>FROM: DEC 30, 2002-DEC 30, 2003 OPEN STOCK ISSUES PAGE 1</p>
<p><strong>PATIENT NAME SSN REQUEST DATE VENDOR ITEM ITEM COST</strong></p>
<p>PROSpatient,one 0765 JAN 14, 2003 ABBOTT LABORA WHEELCHAIR - MANUA 300.00</p>
<p>PROSpatient,two 0061 JAN 16, 2003 ABB BEEF-ROUND/TOP/INS 50.00</p>
<p>END OF REPORT</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Glossary

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Term</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><strong>HCPCS</strong></td>
<td>Healthcare Financing Administration Common Procedure Coding System. A code that represents an item or service.</td>
</tr>
<tr class="odd">
<td><strong>Location</strong></td>
<td>A specific area that contains Prosthetic stock.</td>
</tr>
<tr class="even">
<td><strong>Patient Category</strong></td>
<td><p>The patient's service connection and patient status:</p>
<ul>
<li><blockquote>
<p>SC/OP</p>
</blockquote></li>
<li><blockquote>
<p>SC/IP</p>
</blockquote></li>
<li><blockquote>
<p>NSC/IP</p>
</blockquote></li>
<li><blockquote>
<p>NSC/OP</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>PSAS Item</strong></td>
<td><p>An item that can be issued to a patient. There may be multiple PSAS Items associated with one HCPCS:</p>
<blockquote>
<p>1 - Sling, arm extra large</p>
<p>2 - Sling, arm medium</p>
<p>3 - Sling, arm small</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Re-order Level</strong></td>
<td>A level at which time a stock Item should be re-ordered. A mailman message will appear daily indicating the re-order level has been reached.</td>
</tr>
<tr class="odd">
<td><strong>Source</strong></td>
<td>The distribution for the stock, either VA or Commercial.</td>
</tr>
<tr class="even">
<td><strong>Type of Transaction</strong></td>
<td><p>A first time issue, a repair of a previous issue, a spare, or a replacement of a stock item:</p>
<ul>
<li><blockquote>
<p>Initial = I</p>
</blockquote></li>
<li><blockquote>
<p>Repair = X</p>
</blockquote></li>
<li><blockquote>
<p>Spare = S</p>
</blockquote></li>
<li><blockquote>
<p>Replace = R</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Unit of Issue</strong></td>
<td>How the Item is issued, e.g., box, each, bottle, etc.</td>
</tr>
<tr class="even">
<td><strong>Vendor</strong></td>
<td>The company from which the Item is purchased.</td>
</tr>
</tbody>
</table>

## Appendix B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Using Prosthetics Help

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
<p>VAMC 500</p>
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