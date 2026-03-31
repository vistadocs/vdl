---
title: RMPR*3*67 Purchase Card Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Purchase Card
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*67
group_key: "RMPR:RMPR:3"
file_numbers: 
  - 440
security_keys: []
menu_options: 0
description: - [Verify/Repair Purchase Card Numbers (VR)](#verifyrepair-purchase-card-numbers-vr) ![](rmpr-3-67-purchase-card-release-notes/001.png) PROSTHETICS Patch RMPR\3.0\67RELEASE NOTES November 2001 VISTA Health System Design and Development (HSD&D)
audience: 
keywords: 
  - strong
  - card
  - number
  - purchase
  - table
  - colgroup
  - style
  - width
  - tbody
  - blockquote
page_count: 0
word_count: 3131
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_67.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_67.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

    - [Verify/Repair Purchase Card Numbers (VR)](#verifyrepair-purchase-card-numbers-vr)
![](rmpr-3-67-purchase-card-release-notes/001.png)
PROSTHETICS Patch RMPR\*3.0\*67RELEASE NOTES
November 2001
V*IST*A Health System Design and Development (HSD&D)

### Verify/Repair Purchase Card Numbers (VR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Overview of Patch RMPR\*3\*67

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>Recently the Veterans Administration Central Office (VACO) has been issued approximately 17,000 new VISA credit cards from Citibank. These cards were created to replace compromised numbers on old VISA credit cards. These cards are currently being shipped out and distributed to the VA medical centers.</p>
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
<td><h5 id="the-problem">The problem</h5></td>
<td><blockquote>
<p>Because Citibank replaced the OLD credit card numbers with the NEW VISA credit card number, <strong><u>Prosthetics reconciliation now does NOT work</u></strong>. The new VISA cards that are issued to Prosthetics users are not allowing purchase order transactions to reconcile through the Prosthetics options. The Prosthetics options must be used, because in addition to reconciliation, they also close out the patient record.</p>
<p>The Oracle documents (an IFCAP file: Purchase Card Order Reconcile file 440.6) that are sent from Austin have the NEW credit card numbers on them while the order placed in Prosthetics is still attached to the OLD credit card number.</p>
<p>A Prosthetics Purchasing Agent receives notification of a charge from Austin for purchase card transactions, but they are not able to reconcile charges in Prosthetics because the 16-digit Purchase Card Number value (encrypted in Prosthetics) was switched by Citibank to the replacement.</p>
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
<td><h5 id="the-solution">The solution</h5></td>
<td><p><strong>DO</strong> <em><strong><u>NOT</u></strong></em> <strong>RECONCILE THE PROSTHETIC ORDERS USING IFCAP!!! DO NOT MANUALLY FIX ANY FILES!!! THIS WILL PREVENT CLOSURE OF PATIENT RECORDS!!!</strong></p>
<blockquote>
<p>The IFCAP data (NEW credit card number) must be changed back to the OLD credit card number. <u>Patch <strong>RMPR*3*67</strong> will fix this problem and allow you to reconcile these unique orders using the Prosthetics software</u>.</p>
<p>Facility Purchase Card Coordinators are being informed that these orders cannot be reconciled at this time and that these orders <strong>are exempt from the 10-day reconciliation timeframe for a two-month period</strong> while this is being corrected.</p>
<p>With this patch, a change is made from the <strong>NEW credit card number</strong> back to the <strong>OLD number</strong> (in IFCAP) for existing Prosthetics transactions. This allows Prosthetics to perform a reconciliation on those existing Purchase Orders (in Prosthetics).</p>
<p><u>The change <strong>MUST</strong> be done by the credit card holder in Prosthetics</u> using the new <strong>Verify/Repair Purchase Card Number (VR)</strong> option<strong>.</strong></p>
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
<td><h5 id="visa-level-ii">VISA Level II</h5></td>
<td><blockquote>
<p>If a vendor does not use VISA Level II data (level of data capturing and transaction reporting), then <strong>Patch RMPR*3*67 will not work for these vendors</strong>.</p>
<p>The Purchase Order number must be submitted by the vendor to Citibank or orders will <strong>NOT</strong> be reconciled. Purchase order numbers are only included in VISA Level II data. This is why it is important for vendors to be a Level II Vendor!</p>
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
<td><h5 id="understanding-the-purchase-card-technical-process">Understanding the Purchase Card technical process</h5></td>
<td><blockquote>
<p>An order is created using the <strong>Purchase Card Form (PC)</strong> option from the <strong>Enter New Request Menu (EN)</strong> under the <strong>Purchasing Menu (PU)</strong>. When an order has been placed, the Purchase Order number is relayed to the Vendor purchasing the item(s). This Purchase Order number is placed in a VISA Level II Comment field at the time the order is placed.</p>
<p>When the vendor ships the item, they can submit the bill to Citibank. Citibank pays that bill and sends the changed record to an Oracle database in Austin. This Oracle data now includes the NEW credit card number from Citibank.</p>
<p><strong><u>Note for IRM</u>:</strong> This Patch RMPR*3*67 allows the credit card holder to modify the credit card number contained in the Oracle reconciliation document. The NEW Purchase Card data is received from Austin and stored in the IFCAP Purchase Card Order Reconcile File (file #440.6). Users can modify this file with the OLD (original) Purchase Card number that was used with the Prosthetics transaction.</p>
<p><strong><u>This is necessary so that the Prosthetics order can be reconciled and closed</u>.</strong> There is an audit trail for changing the Purchase Card number in the 440.6 file from the NEW Purchase Card number back to the OLD one.</p>
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
<td><h5 id="checks">Checks</h5></td>
<td><blockquote>
<p>There are checks in place in Prosthetics and in IFCAP. The Oracle Document file looks for the Purchase Order number (VISA Level II Vendors only) in the Comment field. VISA Level II provides a free-text Comment field that is submitted to Citibank. The vendor places a Purchase Order number in this Comment field.</p>
<p><strong>Note:</strong> The Purchase Order number does not have to be exact when the Oracle Document file (IFCAP Purchase Card Reconcile file 440.6) is searching for it. It can be buried within a longer string of numbers, but must be in consecutive order.</p>
<p>The next check is to verify the cardholder. If the user is NOT the card holder who placed the original transaction in Prosthetics, the output report will NOT show any data.</p>
<p>A check is also made for the OLD VISA credit card number against the NEW VISA credit card number (that was issued by Citibank).</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Access the VR Option

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-vr-option">New VR Option</h5></td>
<td><blockquote>
<p>The <strong>Verify/Repair Purchase Card Number (VR)</strong> option from the <strong>Prosthetic Official’s Menu</strong> and the <strong>Prosthetic Clerk’s Menu</strong> was created temporarily to be used by sites that have a problem with reconciling Purchase Card orders. This option will be used to change the credit card number assigned to the Oracle document (in IFCAP) from the NEW card number (as distributed by Citibank) to the OLD card number.</p>
<p><strong>Note:</strong> In order for Prosthetics users to reconcile normally through the Prosthetic Purchase Card Reconciliation options, the vendor <strong>MUST</strong> be a VISA Level II vendor.</p>
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
<td><h5 id="access-steps">Access Steps</h5></td>
<td><blockquote>
<p>You must access the <strong>Verify/Repair Purchase Card Number</strong> <strong>(VR)</strong> option from the <strong>Prosthetics Official’s Menu</strong> or the <strong>Prosthetics Clerk’s Menu</strong> by typing <strong>VR</strong> and pressing the <strong>&lt;Enter&gt;</strong> key.</p>
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
<p><strong>VR VERIFY/REPAIR PURCHASE CARD NUMBER</strong></p>
<p>Select Prosthetic Official's Menu Option: <strong>VR</strong> <strong>&lt;Enter&gt;</strong> VERIFY/REPAIR PURCHASE CARD NUMBER</p>
<p>Verify and Repair Purchase Card Number Associated with the</p>
<p>ORACLE Document for Reconciliation</p>
<p>You Must Be the Card Holder of both OLD and NEW Cards!</p>
</blockquote>
<p>SITE: DVAMC (PROSTHETIC SERVICE)// <strong>&lt;Enter&gt;</strong> 630</p>
<p>Starting Date: <strong>T-30</strong> <strong>&lt;Enter&gt;</strong> (OCT 08, 2001)</p>
<p>Ending Date: <strong>T</strong> <strong>&lt;Enter&gt;</strong> (NOV 07, 2001)</p></td>
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
<td><h5 id="site-prompt">Site Prompt</h5></td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if you Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only.) Entering a &lt;?&gt; will bring up a list of sites for which you will need to define the location. Select a site or enter the number(s) for your station.</p>
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
<td><h5 id="starting-ending-date">Starting/ Ending Date</h5></td>
<td><blockquote>
<p>You can enter a start date for the beginning date of a date range and an end date for the last day of the date range. The date will appear after you press the <strong>&lt;Enter&gt;</strong> key.</p>
<p><u>Examples of valid dates</u>:</p>
</blockquote>
<ul>
<li><p>JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057</p></li>
<li><p>T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.</p></li>
<li><p>T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.</p></li>
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
<td><h5 id="enter-old-and-new-purchase-card-number">Enter OLD and NEW Purchase Card Number</h5></td>
<td><blockquote>
<p>You must first enter the OLD Purchase Card number in the <strong>Enter Old Purchase Card Number</strong> prompt. This is a 16-digit number with no dashes or spaces. This is the number used at the time the order was placed. Then enter the NEW Purchase Card number at the next prompt.</p>
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
<td><h5 id="screen-sample-continued">Screen sample (continued)</h5></td>
<td><blockquote>
<p>Enter OLD Purchase Card Number: <strong>?? &lt;Enter&gt;</strong></p>
<p>Enter the 16-Digit Purchase Card #, no dashes or spaces.</p>
<p>Enter OLD Purchase Card Number: 1234567890123456 <strong>&lt;Enter&gt;</strong></p>
<p>Enter NEW Purchase Card Number: 1234567890654321 <strong>&lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> DecServer_ROU Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
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
<td><h5 id="vr-output">VR Output</h5></td>
<td><blockquote>
<p>The <strong>Verify/Repair Purchase Card Number (VR)</strong> option prints a report that shows all the Purchase Orders and the 16-digit credit card number if there is a match. The Prosthetics file looks for the Purchase Order number in the date range specified by the cardholder.</p>
<p><strong>Note:</strong> If the user is not a Credit Card holder or no Purchase Order for the date range is found, a * NO DATA TO PRINT * message will display on the output report.</p>
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
<td><blockquote>
<p>OCT 01, 2001-OCT 23, 2001 Verify PC# <strong>1234567890123456</strong> STA 630 PAGE 1</p>
<p><strong>Order Date Order Number | ORACLE PC # VISA II | Record Status</strong></p>
<p>------------------------------------------------------------------------------</p>
<p>10/23/01 999-R23243 | 1234567890123456 | Okay</p>
<p>10/23/01 999-R23235 |</p>
<p>10/23/01 999-R23197 | 1234567890123456 | Okay</p>
<p>10/23/01 999-R23183 | 1236769000099999 R23183 | Diff Card #</p>
<p>10/23/01 999-R23164 |</p>
<p>10/23/01 999-R23132 | 1234567890123456 | Okay</p>
<p>10/22/01 999-R23002 |</p>
<p>10/22/01 999-R22967 | 1234567890123456 | Okay</p>
<p>10/19/01 999-R22898 |</p>
<p>10/19/01 999-R22896 | 1234567890123456 | Okay</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>OCT 01, 2001-OCT 23, 2001 Verify PC# <strong>1234567890123456</strong> STA 630 PAGE 2</p>
<p>Order Date Order Number | ORACLE PC # VISA II | Record Status</p>
<p>------------------------------------------------------------------------------</p>
<p>10/19/01 999-R22838 | 1234567890654321 630R22838 | Repaired</p>
<p>10/18/01 999-R22787 |</p>
<p>10/16/01 999-R22553 | 1234567890654321 R22553 | Repaired</p>
<p>10/16/01 999-R22552 |</p>
<p>10/16/01 999-R22547 | 1234567890123456 | Okay</p>
<p>10/16/01 999-R22543 |</p>
<p>10/16/01 999-R22542 | 1234567890654321 R22542 | Repaired</p>
<p>10/16/01 999-R22537 |</p>
<p>10/16/01 999-R22536 | 1234567890654321 R22536 | Repaired</p>
<p>10/16/01 999-R22535 | 1234567890654321 R22535 | Repaired</p>
<p>10/16/01 999-R22533 |</p>
<p>10/11/01 999-R21770 |1234567890123456 | Okay</p>
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
<td><h5 id="output-report-and-the-record-status">Output report and the Record Status</h5></td>
<td><blockquote>
<p>If the NEW credit card number is found, the purchase record is fixed and updated automatically. The Record Status will show “<strong>Repaired</strong>” for this Order Number. If the OLD credit card number is found, then the Record Status displays “<strong>Okay.</strong>”</p>
<p>If another Purchase Card number is found, it prints it with a message shown as “<strong>Diff Card #</strong>” in the Record Status and does NOT update the record. With this comment, it alerts the cardholder that the record will need to be manually updated.</p>
<p><strong>Note:</strong> If the Order Number does not have a Record Status and that column is blank, then that means that no Oracle data has been found in IFCAP yet. You will need to continue to run this option every day until all old reconciliations are completed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Audit Features - File 664 (for IRM)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-fields">New fields</h5></td>
<td><blockquote>
<p><strong>Prosthetics, please forward to IRM for Alert:</strong> The audit feature for File 664 has three new fields for auditing created with the release of Prosthetics patch RMPR*3.0*67 including the following:</p>
</blockquote>
<ul>
<li><p>29 - New Purchase Card Number (Free text)</p></li>
<li><p>30 - Audit Repair (Pointer to file)</p></li>
<li><p>31 - Audit Date (Date/Time that the credit card number in file 440.6 was modified.)</p></li>
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
<td><h5 id="screen-sample-1">Screen sample</h5></td>
<td><p>DATE: JAN 19, 2001 PATIENT: PROSPATIENT,ONE</p>
<p>VENDOR: PROSVENDOR,ONE INITIATOR: PROSPROVIDER,ONE</p>
<p>EST. SHIPPING CHARGE: 5 ACT. SHIPPING CHARGE: 5</p>
<p>SHIPPING ENTRY: JAN 19, 2001 STATION NAME: SUPPORT ISC</p>
<p>ITEM: TEST ITEM BRIEF DESCRIPTION: 3-1 COMMODE</p>
<p>UNIT COST: 80 QTY: 1</p>
<p>UNIT OF ISSUE: EA REMARKS: TEST NOIS</p>
<p>TYPE OF TRANSACTION: INITIAL ISSUE PATIENT CATEGORY: SC/OP</p>
<p>SOURCE: COMMERCIAL APPLIANCE/REPAIR: JAN 19, 2001</p>
<p>CONTRACT #: V797P-5894M PSAS HCPCS: E0175</p>
<p>CPT MODIFIER: LT,RT,NU</p>
<p>FORM TYPE: 2421PC DELIVER TO: VETERAN</p>
<p>DATE REQUIRED: JAN 19, 2001 DELIVERY TIME: 0</p>
<p>PURCHASE CARD NUMBER: ef36~%;t10Lh|dG</p>
<p>EST AMOUNT: 85 PURCHASE CARD REFERENCE: 7P0061</p>
<p>IFCAP ORDER: 499-P70090</p>
<p><strong>NEW PURCHASE CARD NUMBER:</strong> 0000000000000000</p>
<p><strong>AUDIT REPAIR:</strong> C4997198P79999</p>
<p><strong>AUDIT DATE:</strong> OCT 27, 2001</p></td>
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
<td><h5 id="help-desk">Help Desk</h5></td>
<td><blockquote>
<p>If you have any questions or problems while implementing this solution, please notify the National VistA Support Help Desk at 1-888-596-4357.</p>
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
<td><h5 id="new-purchase-card-number-field">New Purchase Card Number field</h5></td>
<td><blockquote>
<p>This patch was released to allow users to modify the credit card number contained in the Oracle reconciliation document received from Austin and stored in the IFCAP PURCHASE CARD RECONCILE file (#440.6).</p>
<p>Due to Citibank canceling and re-issuing a number of credit cards, it may be necessary to modify the credit card number in the file #440.6 Oracle document to match the credit card number that is in the original purchase order.</p>
<p><strong>This field stores the new purchase card number that was sent from Citibank in the Oracle transaction from Austin.</strong> This number was originally stored in file 440.6, the IFCAP PURCHASE CARD ORDER RECONCILE file, and has been replaced in file 440.6 by the original purchase card number on the prosthetics transaction.</p>
<p>This is necessary so that the prosthetics order can be reconciled and closed. This field is needed to maintain the audit trail for changing the purchase card number in 440.6 from the new purchase card number back to the original purchase card number.</p>
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
<td><h5 id="audit-repair-field">Audit Repair field</h5></td>
<td><blockquote>
<p>POINTER TO PURCHASE CARD ORDER RECONCILE FILE (#440.6):</p>
<p>Due to Citibank canceling and re-issuing a number of credit cards, it may be necessary to modify the credit card number in the file #440.6 Oracle document to match the credit card number that is in the original purchase order.</p>
<p>This is necessary so that the prosthetics order can be reconciled and closed. <strong>This field is needed to maintain the audit trail for changing the purchase card number in 440.6 from the new purchase card number back to the original purchase card number.</strong></p>
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
<td><h5 id="audit-date-field">Audit Date field</h5></td>
<td><blockquote>
<p>This patch was released to allow users to modify the credit card number contained in the Oracle reconciliation document received from Austin and stored in the IFCAP PURCHASE CARD RECONCILE file (#440.6).</p>
<p><strong>This is the date that the credit card number in file 440.6 was modified.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
