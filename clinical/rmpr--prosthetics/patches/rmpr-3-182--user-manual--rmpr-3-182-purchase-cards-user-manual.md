---
title: RMPR*3*182 Purchase Cards User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Purchase Cards
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*182
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 3
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h5 id=\\"introduction\\">Introduction</h5></td> <td><blockquote> <p>What is a Purchase Card? A Purchase Card is similar to a credit card and has a pre-set monetary limit used to pay for goo"
audience: 
keywords: 
  - strong
  - purchase
  - blockquote
  - card
  - table
  - style
  - width
  - colgroup
  - tbody
  - class
page_count: 0
word_count: 21748
section_count: 8
table_count: 36
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: August 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_182_pc_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_182_pc_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [Purchase Card Process](#purchase-card-process)
  - [Reprints (RP) Menu](#reprints-rp-menu)
  - [Purchase Card Reports](#purchase-card-reports)
  - [Purchase Card Site Parameter (SS)](#purchase-card-site-parameter-ss)
  - [Satellite Broadcast – May, 2001](#satellite-broadcast-may-2001)
  - [Appendix A](#appendix-a)
  - [Appendix B](#appendix-b)
![](rmpr-3-182-purchase-cards-user-manual/001.png)
Prosthetics Purchase CardsUser Manual
August 2002
(Revised August 2017)
V*IST*A System Design and Development
Revision History
<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 35%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2017</td>
<td>RMPR*3.0*182</td>
<td><p>Added the Revision History page &amp; documentation filename was updated to “rmpr_3_182_pc_um”.</p>
<p>In addition this user manual has been updated per patch, RMPR*3.0*182 (pp. <a href="#p23">23</a>, <a href="#p24">24</a>, <a href="#p23">31</a>, <a href="#p24">32</a>, <a href="#p35">35</a>, <a href="#p40">40</a>).</p></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
Table of Contents
Using Prosthetics Purchase Cards [1](#using-prosthetics-purchase-cards)
Overview [1](#overview)
Citibank and VISA [4](#citibank-and-visa)
Purchase Card Process [6](#purchase-card-process)
Overview [6](#overview-1)
Create a Purchase Card Form (PC) [7](#create-a-purchase-card-form-pc)
Edit a Purchase Card Transaction [22](#edit-a-purchase-card-transaction)
Link a Purchase Card Transaction to the Suspense Record [24](#link-a-purchase-card-transaction-to-the-suspense-record)
Cancel Purchase Card Transaction (CPC) [25](#cancel-purchase-card-transaction-cpc)
Reconcile/Close Out Purchase Card Transaction (CPO) [28](#reconcileclose-out-purchase-card-transaction-cpo)
Reprints (RP) Menu [36](#reprints-rp-menu)
Reprint a Purchase Card Form (PCR) [36](#reprint-a-purchase-card-form-pcr)
Purchase Card Reports [39](#purchase-card-reports)
Report List [39](#report-list)
List Open Purchase Card Transactions (LPC) Report [40](#list-open-purchase-card-transactions-lpc-report)
List Open Purchase Card Transactions by Initiator (LPCI) Report [41](#list-open-purchase-card-transactions-by-initiator-lpci-report)
Purchase Card Summary Sheet (LPS) Report [43](#purchase-card-summary-sheet-lps-report)
Purchase Card Site Parameter (SS) [45](#purchase-card-site-parameter-ss)
Satellite Broadcast – May, 2001 [46](#satellite-broadcast-may-2001)
Question and Answer Session [46](#question-and-answer-session)
Appendix A [50](#appendix-a)
Privacy Act [50](#privacy-act)
Patient Notification Letter [51](#patient-notification-letter)
Appendix B [52](#appendix-b)
Glossary [52](#glossary)

#### ### Using Prosthetics Purchase Cards

#### Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>What is a Purchase Card? A Purchase Card is similar to a credit card and has a pre-set monetary limit used to pay for goods or services for official VA use in the Prosthetic Sensory Aids Service (PSAS). The Prosthetics users can use these cards with the Prosthetics package. This is the preferred and recommended procurement method.</p>
<p>The <strong>Purchase Card Form (PC)</strong> option is used to create a transaction. This option is located from the <strong>Enter New Request</strong> <strong>(EN)</strong> <strong>Menu</strong> that is found under the <strong>Purchasing Menu (PU)</strong>.</p>
<p>With the use of the <strong>Purchase Card Form (PC)</strong> option, the Fund Control Point (FCP) is automatically debited. This allows Prosthetics to keep track of the Purchase Card transactions without posting to Fund Control Points. This option will post purchases to the patient’s electronic 10-2319. Once posted, this Purchase Card transaction may only be closed or cancelled.</p>
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
<td><h5 id="purchase-card-numbers">Purchase Card Numbers</h5></td>
<td><blockquote>
<p>The <em><strong>Purchase Card Number</strong></em> is a 16-digit number in IFCAP identifying a specific Purchase Card issued to a Purchasing Agent. This number is critical to accurate record keeping.</p>
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
<td><h5 id="single-purchase-limit">Single Purchase Limit</h5></td>
<td><blockquote>
<p>The single purchase limit is a limitation on the procurement authority delegated to the cardholder by your Contracting Officer. This limit cannot be exceeded unless the Contracting Officer raises the limit. A “single purchase” using the card may include multiple items.</p>
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
<td><h5 id="monthly-purchase-limit">Monthly Purchase Limit</h5></td>
<td><blockquote>
<p>The monthly purchase limit is a budgetary limit that is assigned by the Approving Official. The total dollar value of purchases made for any month may not exceed the monthly cardholder’s limit.</p>
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
<td><h5 id="benefits-of-using-purchase-cards">Benefits of using Purchase Cards</h5></td>
<td><blockquote>
<p>The following benefits have been found when using Purchase Cards:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Vendor is paid promptly.</p>
</blockquote></li>
<li><blockquote>
<p>No invoice to certify which reduces paperwork for Prosthetics and Fiscal Services.</p>
</blockquote></li>
<li><blockquote>
<p>Many vendors give additional discounts for Purchase Card use.</p>
</blockquote></li>
<li><blockquote>
<p>Funds are not obligated until they are actually acquired.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>
Continued on next page
Overview, Continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="prosthetic-services">Prosthetic services</h5></td>
<td><blockquote>
<p>What Prosthetics services can be purchased using your Purchase Card?</p>
</blockquote>
<ul>
<li><blockquote>
<p>All Prosthetic items, services, etc. provided you do not exceed:</p>
</blockquote></li>
<li><blockquote>
<blockquote>
<p>Your single order limitation (warrant authority)</p>
</blockquote>
</blockquote></li>
<li><blockquote>
<blockquote>
<p>Your monthly limitation.</p>
</blockquote>
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
<td><h5 id="visa">VISA</h5></td>
<td><blockquote>
<p>VISA is a form type that is being used by the module to keep track of Purchase Card transactions. The VISA will show up as the form type under the <strong>View Patient 2319</strong> option, <strong>Screen 4</strong>, Extended Screen. This displays when a transaction has been completed by use of a Purchase Card.</p>
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
<td><h5 id="boccc">BOC/CC</h5></td>
<td><blockquote>
<p><strong>Important:</strong> You must have a separate credit card for each <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Budget Object Code/Cost Center (BOC/CC) combination you use when ordering through the Prosthetics package.</p>
<p>The Prosthetics package does not give the option of entering/changing the BOC information on individual patient orders.</p>
<p><strong>Note</strong>: When ordering on the IFCAP side, the BOC/CC can be edited.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>See Glossary – Appendix B for more details.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="prosthetic-staff-responsibility">Prosthetic Staff responsibility</h5></td>
<td><blockquote>
<p>The following are responsibilities of the Prosthetic staff:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Ensuring adequate funds are available for your obligation.</p>
</blockquote></li>
<li><blockquote>
<p>Obligations are reasonable and accurate.</p>
</blockquote></li>
<li><blockquote>
<p>Know what you are buying - participate in regular in-services.</p>
</blockquote></li>
<li><blockquote>
<p>Research and review of product information - determine mandatory sources when available.</p>
</blockquote></li>
<li><blockquote>
<p>Receive feedback from clinical staff and patients regarding products.</p>
</blockquote></li>
<li><blockquote>
<p>Ensure Contractor fulfills the requirements of the contract.</p>
</blockquote></li>
<li><blockquote>
<p>Serve as technical advisor to Contracting Officers - communicate problems/issues with Contracting Officer.</p>
</blockquote></li>
<li><blockquote>
<p>Reconciling transactions in a timely manner.</p>
</blockquote></li>
<li><blockquote>
<p>Follow-up on outstanding transactions.</p>
</blockquote></li>
<li><blockquote>
<p>Monitor activities for quality improvement.</p>
</blockquote></li>
<li><blockquote>
<p>Ensure appropriate BOC and CC are used.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>
Continued on next page
Overview, Continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="access">Access</h5></td>
<td><blockquote>
<p>You can access the Purchase Card feature from the <strong>Purchasing Menu (PU)</strong> as shown below:</p>
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
<td><h5 id="purchasing-menu">Purchasing Menu</h5></td>
<td><blockquote>
<p><strong>PU Purchasing</strong> ...</p>
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
<p>VR VERIFY/REPAIR PURCHASE CARD NUMBER</p>
<p>Select Prosthetic Official's Menu Option: <strong>PU &lt;Enter&gt;</strong> Purchasing</p>
<p><strong>EN Enter New Request ...</strong></p>
<p>SI Stock Issues ...</p>
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
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>EN</strong> <strong>&lt;Enter&gt;</strong> Enter New Request</p>
<p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p><strong>PC Purchase Card Form</strong></p>
<p>SS Purchase Card Site Parameter</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Citibank and VISA

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="who-is-citibank">Who is Citibank?</h5></td>
<td><blockquote>
<p>Citibank is the largest financial institution in the world and a VISA member bank. Citibank is both a credit card issuer and an acquirer. Citibank is a leader in the corporate and government credit card industry.</p>
<p><strong>Note:</strong> Citibank is <strong>ONE</strong> provider and processor of the Veterans Affairs Purchase Cards; there may be others.</p>
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
<td><h5 id="who-is-visa">Who is VISA?</h5></td>
<td><blockquote>
<p>VISA is an international brand of payment cards issued by more than 21,000 member financial institutions around the world including Citibank.</p>
<p><strong>Note:</strong> VISA is <strong>ONE</strong> possible charge company for a bank that the VA uses; there may be others.</p>
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
<td><h5 id="data-capturing">Data Capturing</h5></td>
<td><blockquote>
<p>Enhanced data includes additional information accompanying charge card transactions that is not required for financial transaction settlement. Enhanced data supports multiple accounting and reporting functions.</p>
<p>The merchant sends the data to VISA, and it is then sent to Citibank. The account statement is sent from Citibank to the Purchase Cardholder. Records are passed to Citibank and the VA by way of electronic systems access, data feeds, or paper reports.</p>
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
<td><h5 id="levels-of-data-capturing">Levels of Data Capturing</h5></td>
<td><blockquote>
<p><strong>Level One</strong> is the minimum amount of data required to clear and settle the financial transaction.</p>
<p><strong>Level Two</strong> provides additional summary data for the sale that accompanies Level One data through the clearing and settlement process. <u>This level also provides the ability to provide the Purchase Order Number to Citibank</u>.</p>
<p><strong>Level Three</strong> provides line-item, transaction-related data elements. Level Three data is not attached to Level One financial records; and must be linked to these records using a matching process.</p>
<p><strong>Note:</strong> All vendors are encouraged to have at least <strong>VISA Level II</strong> that supplies the capability to supply the Purchase Order number in the transaction.</p>
</blockquote></td>
</tr>
</tbody>
</table>
Continued on next page
Citibank and VISA, Continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="level-one-data">Level One Data</h5></td>
<td><blockquote>
<p>Level One data includes the following:</p>
</blockquote>
<ul>
<li><p>Merchant name</p></li>
<li><p>Merchant location – city, state, ZIP</p></li>
<li><p>Transaction amount</p></li>
<li><p>Merchant Category Code (MCC)</p></li>
<li><p>Transaction date</p></li>
<li><p>Account number</p></li>
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
<td><h5 id="level-two-data">Level Two Data</h5></td>
<td><blockquote>
<p>Level Two data includes the following:</p>
</blockquote>
<ul>
<li><p>Level One data PLUS:</p></li>
<li><p>Sales tax</p></li>
<li><p>Customer code</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> The Purchase Order number can be entered into a free-text field in Level Two.</p>
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
<td><h5 id="level-three-data">Level Three Data</h5></td>
<td><blockquote>
<p>Level Three data includes the following:</p>
</blockquote>
<ul>
<li><p>Level One and Level Two data PLUS:</p></li>
<li><p>Detailed tax information</p></li>
<li><p>Discount amount</p></li>
<li><p>Freight/ship amount</p></li>
<li><p>Duty amount</p></li>
<li><p>Ship to/from ZIP codes</p></li>
<li><p>Order date</p></li>
<li><p>Account number</p></li>
<li><p>Item commodity code</p></li>
<li><p>Item description</p></li>
<li><p>Quantity</p></li>
<li><p>Unit of measure</p></li>
<li><p>Unit cost</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Purchase Card Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-1">Introduction</h5></td>
<td><blockquote>
<p>Prosthetics uses Purchases Cards that are interfaced with vendor payment from Citibank using a VISA form type to keep track of transactions.</p>
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
<td><h5 id="understanding-the-process">Understanding the process</h5></td>
<td><blockquote>
<p>Below is the cycle of a Purchase Card transaction/order:</p>
</blockquote>
<ul>
<li><p>When the veteran receives the item ordered, the vendor can send a transaction to Citibank to request payment. (If the vendor has the capability to interface with Citibank using VISA with a Level II data, a Purchase Order number is sent to Citibank.)</p></li>
<li><p>Citibank pays that bill and sends the record to the Oracle database in the Financial Service Center (FSC) in Austin (which is IFCAP).</p></li>
<li><p>Citibank notifies the VA FSC in Austin to make the payment.</p></li>
<li><p>Austin populates IFCAP and creates the check.</p></li>
<li><p>Citibank sends the transaction (with the Purchase Order number) to the cardholder for reconciling.</p></li>
<li><p>The cardholder has 10 calendar days to reconcile using the Prosthetics software (using the <strong>Reconcile/Close Out Purchase Card Transaction (CPO)</strong> option).</p></li>
</ul>
<blockquote>
<p><strong>Warning:</strong> If erroneous charges cannot be corrected, <u>then a Dispute must be filed within 30 days</u>. Cardholder must complete 75% of the reconciliations within 10 days, 95% within 17 days, and 100% within 30 days. <strong>All reconciliations must be approved within 14 calendar days by the Approving Officials</strong>.</p>
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
<td><h5 id="in-this-section">In this section</h5></td>
<td><blockquote>
<p>This section covers the following topics:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                         |          |
|---------------------------------------------------------|----------|
| Topic                                                   | See Page |
| Create a Purchase Card Form (PC)                        | 7        |
| Edit a Purchase Card Transaction                        | 22       |
| Link a Purchase Card Transaction to the Suspense Record | 24       |
| Cancel a Purchase Card Transaction (CPC)                | 25       |
| Reconcile/Close Out Purchase Card Transaction (CPO)     | 28       |

#### Create a Purchase Card Form (PC)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="access-1">Access</h5></td>
<td><blockquote>
<p>The <strong>Purchase Card Form (PC)</strong> option is accessed from the <strong>Enter New Request</strong> <strong>(EN)</strong> menu under the <strong>Purchasing Menu (PU)</strong>.</p>
<p><u>You can order one or multiple items on the same order</u>. You will verify eligibility for a patient, and <strong>you will create a Purchase Order (PO)</strong> <strong>number</strong> for the order through this option.</p>
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
<p>To create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                            |
|------|------------------------------------------------------------|
| Step | Action                                                     |
| 1    | Select the Enter New Request menu by typing EN.    |
| 2    | Select the Purchase Card Form option by typing PC. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="enter-new-request-menu-en">Enter New Request Menu (EN)</h5></td>
<td><p><strong>EN Enter New Request ...</strong></p>
<p>SI Stock Issues ...</p>
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
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>EN</strong> <strong>&lt;Enter&gt;</strong> Enter New Request</p>
<p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p><strong>PC Purchase Card Form</strong></p>
<p>SS Purchase Card Site Parameter</p>
<p>Select Enter New Request Option: <strong>PC &lt;Enter&gt;</strong> Purchase Card Form</p></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="site">Site</h5></td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetic Service covers multiple stations. This is a non-editable field (for display purposes only).</p>
<p>Entering a question mark &lt;<strong>?</strong>&gt; will bring up a list of sites. Select a site or enter the number(s) for your station.</p>
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
<td><h5 id="steps-1">Steps</h5></td>
<td><blockquote>
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                           |
| 3    | Select a Site from a list (if at a multi-divisional site) or press \<Enter\> to accept the default site. |
| 4    | Select the Prosthetic Patient.                                                                                   |
| 5    | Disability Codes display (if applicable).                                                                        |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="disability-codes-screen">Disability Codes screen</h5></td>
<td><blockquote>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select PROSTHETIC PATIENT: PROSPATIENT,ONE <strong>&lt;Enter&gt;</strong> HINES, IL 1-1-30 000000001 NO PILL</p>
<p>*Comments on file</p>
<p>Current Disability Codes are:</p>
<p>COS/B EMPLOYEE NSC</p>
<p>AMP/LAE SC VIETNAM S/C</p>
<p>AMP/LAE SC VIETNAM NSC</p>
<p>ORTH/PLS INPATIENT S/C</p>
<p>*More Disability Codes on File, See Screen 1</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="review-screens-1-2-on-the-patient-10-2319">Review Screens 1 &amp; 2 on the Patient 10-2319</h5></td>
<td><blockquote>
<p>You can view any of the 10-2319 patient screens by selecting 1-8 including the following information: 1) Patient Demographics, 2) Clinic Enrollments/ Correspondence, 3) Entitlement Information, 4) Appliance Transactions, 5) Auto Adaptive Information, 6) Critical Comments, 7) Add/Edit Disability Code, and<br />
8) Home Oxygen items.</p>
<p><strong><u>Review Screen 1 and Screen 2 prior to creating a PO to verify Prosthetic eligibility and ensure you are not purchasing a duplicate item</u>.</strong></p>
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
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                             |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                      |
| 6    | At the Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: prompt, type “1” for Patient Demographics to establish eligibility for the patient prior to creating a PO!! |
| 7    | Press \<Enter\> to continue.                                                                                                                                                            |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="patient-demographics">Patient Demographics</h5>
<p>(Screen display)</p></td>
<td><blockquote>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: <strong>1</strong> <strong>&lt;Enter&gt;</strong> PATIENT DEMOGRAPHICS</p>
<p>PROSPATIENT,ONE SSN: 000-00-0001 DOB: JAN 1,1930 CLAIM#</p>
<p>Phone: Phone:</p>
<p>Current Address: Primary Next of Kin Address:</p>
<p>ANY AVE</p>
<p>CHICAG, ILLINOIS 60000</p>
<p>Patient Type: PILL Period of Service: OTHER OR NONE</p>
<p>Primary Eligibility Code: Status: REQUIRED</p>
<p>NSC Eligibility Status:</p>
<p>Receiving A&amp;A Benefits? NO Receiving Housebound Benefits? NO</p>
<p>Receiving Social Security? NO Receiving VA Pension? NO</p>
<p>Receiving Military Retirement? NO Receiving VA Disability? NO</p>
<p>Prosthetic Disability Code(s): COS/B-NSC AMP/LAE-SC AMP/LAE-NSC ORTH/PLS-SC ORTH</p>
<p>/DLF-SC AO/AUTO-SC</p>
<p>Enter RETURN to continue or '^' to exit: <strong>&lt;Enter&gt;</strong></p>
<p>*POW? NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="clinic-enrollments-correspondence">Clinic Enrollments/ Correspondence</h5></td>
<td><blockquote>
<p>The <strong>Clinic Enrollments/Correspondence</strong> option or <strong>Screen 2</strong>, allows you to verify Prosthetic eligibility prior to creating the Purchase Order (PO).</p>
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
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                      |
| 8    | At the Enter return to continue or ‘^’ to exit prompt, press \<Enter\> to continue. The Disability Codes will display again.                                                                        |
| 9    | At the Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: prompt, type “2” (for Clinic Enrollments/ Correspondence) to establish eligibility for the patient prior to creating a PO!! |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-options">10-2319 Screen options</h5></td>
<td><blockquote>
<p>Enter return to continue or `^` to exit: <strong>&lt;Enter&gt;</strong></p>
<p>*Comments on file</p>
<p>Current Disability Codes are:</p>
<p>COS/B EMPLOYEE NSC</p>
<p>AMP/LAE SC VIETNAM S/C</p>
<p>AMP/LAE SC VIETNAM NSC</p>
<p>ORTH/PLS INPATIENT S/C</p>
<p>*More Disability Codes on File, See Screen 1</p>
<p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p><strong>2 CLINIC ENROLLMENTS/CORRESPONDENCE</strong></p>
<p>3 ENTITLEMENT INFORMATION</p>
<p>4 APPLIANCE TRANSACTIONS</p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: <strong>2</strong> <strong>&lt;Enter&gt;</strong> CLINIC ENROLLMENTS/CORRESPONDENCE</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="display-info">Display info</h5></td>
<td><blockquote>
<p>Below is the display for the Last Movement Actions, Clinic Enrollments, and Pending Appointments from the 10-2319 Screen.</p>
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
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                              |
| 10   | At the Enter RETURN to continue or '^' to exit: prompt, press \<Enter\> to continue and view the letters on file.                                           |
| 11   | At the Enter a number prompt, type a number to view a letter or type the caret (^) and press \<Enter\> to bypass viewing the letters on file.               |
| 12   | At the Do you wish to view a letter? No// prompt, press \<Enter\> to bypass and continue. (Type Y for Yes to view letters.)                             |
| 13   | At the Do you wish to create a correspondence letter? No// prompt, press \<Enter\> to bypass and continue. (You can type Y for Yes to create a letter.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="clinic-enrollment-display">Clinic Enrollment display</h5></td>
<td><blockquote>
<p>PROSPATIENT,ONE SSN: 000-00-0001 DOB: JAN 1,1930 CLAIM#</p>
<p>Last Movement Actions</p>
<p>Trans. Type: TRANSFER Trans. Type: ADMISSION</p>
<p>Date: SEP 11,1995@15:04:29 Date: SEP 11,1995@14:59:18</p>
<p>Type of Movement: Type of Movement:</p>
<p>INTERWARD TRANSFER DIRECT</p>
<p>Ward: 1AS Ward: 5NM</p>
<p>Physician: PROSPROVIDER,TWO Physician: PROSPROVIDER,THREE</p>
<p>Diagnosis: SICK Diagnosis: SICK</p>
<p>Clinic Enrollments</p>
<p>Clinic Enrollment Date OPT or AC</p>
<p>MCGILL,TEST MAR 21,2000@13:11 OPT</p>
<p>Pending Appointments</p>
<p>No Pending Appointments for this Patient</p>
<p>Enter RETURN to continue or '^' to exit: <strong>&lt;Enter&gt;</strong></p>
<p>Letters on file:</p>
<p># Patient Type of letter Employee Date of letter</p>
<p>------------------------------------------------------------------------------</p>
<p>1 PROSPATIENT,ONE FOLLOW UP PROSPROVIDER,ONE FEB 08, 2002</p>
<p>2 PROSPATIENT,ONE HO 30 DAY TEST PROSPROVIDER,ONE FEB 08, 2002</p>
<p>3 PROSPATIENT,ONE HO 30 DAY TEST PROSPROVIDER,ONE FEB 08, 2002</p>
<p>4 PROSPATIENT,ONE HO 30 DAY TEST PROSPROVIDER,ONE FEB 08, 2002</p>
<p>5 PROSPATIENT,ONE HO 30 DAY TEST PROSPROVIDER,ONE FEB 08, 2002</p>
<p>Enter '^' to stop or</p>
<p>Enter a number (1-5): <strong>^ &lt;Enter&gt;</strong></p>
<p>Do you wish to view a letter? No// (No) <strong>&lt;Enter&gt;</strong></p>
<p>Do you wish to create a correspondence letter? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>*Comments on file</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="appliance-transaction-screen-4">Appliance Transaction (Screen 4)</h5></td>
<td><blockquote>
<p>You can view the Appliance Transaction history (<strong>Screen 4</strong> from the patient 2319).</p>
<p>(The form type, VISA, displays on the Appliance Transaction Detail screen that has been utilized for purchases as shown on the next page.) <strong><u>Review Screen 4 prior to creating a PO to ensure you are not purchasing a duplicate item</u>.</strong></p>
<p>You can also access this screen from the <strong>Display/Print (DD) Menu</strong> and the <strong>Display/Print Patient 2319 (23)</strong> option.</p>
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
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                       |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                |
| 14   | The Disability codes display first and then the list of 10-2319 selections.                                                                                                           |
| 15   | At the Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: prompt, type “4.” The Appliance Transaction list displays for you to select one and view the details. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="appliance-transaction-list">Appliance Transaction list</h5></td>
<td><blockquote>
<p>Current Disability Codes are:</p>
<p>COS/B EMPLOYEE NSC</p>
<p>AMP/LAE SC VIETNAM S/C</p>
<p>AMP/LAE SC VIETNAM NSC</p>
<p>ORTH/PLS INPATIENT S/C</p>
<p>*More Disability Codes on File, See Screen 1</p>
<p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p><strong>4 APPLIANCE TRANSACTIONS</strong></p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>4</strong> <strong>&lt;Enter&gt;</strong> APPLIANCE TRANSACTIONS</p>
<p>PROSPATIENT,ONE SSN: 000-00-0001 DOB: JAN 1,1930 CLAIM#</p>
<p><u>Date Qty Item Type Vendor Sta Serial Delivery Date Tot Cost</u></p>
<p>1. 11/27/01 1 SHOE COMPO I PROSVENDOR,ONE 499 20.00</p>
<p>follow up</p>
<p>2. 11/20/01 100 SHOE COMPO I PROSVENDOR,ONE 499 1600.00</p>
<p>print on the 2310</p>
<p>3. 11/20/01 1 SHOE COMPO I PROSVENDOR,ONE 499 2.00</p>
<p>4. 10/02/01 1 OXYGEN CON I PROSVENDOR,ONE 499 25.00</p>
<p>5. 10/02/01 1 OXYGEN CON I PROSVENDOR,TWO 499 0.00</p>
<p>6. 10/01/01 PICKUP X PROSVENDOR,ONE 499 5.00</p>
<p>7. 09/28/01 1 EYEGLASSES I PROSVENDOR,TWO 499 5.00</p>
<p>8. 09/28/01 1 OXYGEN CON I PROSVENDOR,TWO 499 0.00</p>
<p>+=Turned-In *=Historical Data I=Initial X=Repair S=Spare R=Replacement</p>
<p>Enter 1-8 to show full entry, '^' to exit or `return` to continue. <strong>1 &lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="line-item-details">Line Item Details</h5></td>
<td><blockquote>
<p>Below are the details (for one patient on one order) that are included in the <strong>Appliance/Repair Line Item Detail</strong> screen.</p>
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
<td><h5 id="type-of-form-field">Type of Form field</h5></td>
<td><blockquote>
<p>Note the <em><strong>Type of Form</strong></em> field below shows that VISA is the form type (vs. 2421, 2914, 2529-3, or stock issue, etc.). This field displays different details depending on the form type.</p>
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
<p>To continue to create a Purchase Card form, follow these steps:</p>
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
<td>16</td>
<td><p>At the <strong>Enter RETURN to continue or “^” to exit:</strong> prompt, you can do the following:</p>
<ul>
<li><p>Press the “<strong>^</strong>” (caret) to exit and you will be taken back to the list of Appliance Transactions where you can select another one to view.</p></li>
<li><p>Disability Codes will display again.</p></li>
<li><p>The prompt, Enter 10-2319 screen to view (1-8), “^” to Exit, or “RETURN” to continue, you can press &lt;Enter&gt; to continue.</p></li>
<li><p>The <strong>Date Required</strong> prompt will display. (See next page.)</p></li>
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
<td><h5 id="appliance-transaction-details">Appliance Transaction details</h5></td>
<td><blockquote>
<p>PROSPATIENT,ONE SSN: 000-00-0001 SUPPORT ISC DOB: 01-01-1930</p>
<p><strong>APPLIANCE/REPAIR LINE ITEM DETAIL</strong> &lt;4-1&gt;</p>
<p><strong>TYPE OF FORM:</strong> <strong>VISA</strong> INITIATOR: PROSPROVIDER,FOUR DATE: NOV 27, 2001</p>
<p>DELIVER TO: PROSTHETICS</p>
<p>TYPE TRANS: INITIAL ISSUE QTY: 1 SOURCE: COMMERCIAL</p>
<p>VENDOR TRACKING: BANK AUTHORIZATION:</p>
<p>VENDOR: PROSVENDOR,ONE</p>
<p>VENDOR PHONE: (555) 555-5555</p>
<p>CORPORATE ORDER ENTRY</p>
<p>ANY PARK, ILLINOIS 60064</p>
<p>DELIVERY DATE:</p>
<p>TOTAL COST: $20.00 OBL: 7P0080</p>
<p>REMARKS: REQUESTED VENDOR SEND ASAP</p>
<p>DISABILITY SERVED: NSC/IP</p>
<p>APPLIANCE: SHOES</p>
<p>PSAS HCPCS: L3201 OXFORD W/SUPINAT/PRONAT INF</p>
<p>CPT MODIFIER:</p>
<p>DESCRIPTION: OXFORD SHOE WITH INSERT</p>
<p>EXTENDED DESCRIPTION:</p>
<p>Enter RETURN to continue or '^' to exit:</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="date-required-field">Date Required field</h5></td>
<td><blockquote>
<p>The <strong>Date Required</strong> field stores the date by which the vendor is required to provide the Item/Service.</p>
<p>If the year is omitted, the computer uses the CURRENT YEAR. You can also enter a precise day.</p>
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
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                |
|------|--------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                         |
| 17   | Press \<Enter\> to accept the current date plus 30 days. (You can also enter a different date by entering T + any number.) |
| 18   | Select the Vendor from a list.                                                                                             |
| 19   | Press \<Enter\> to bypass this prompt, or select a Contract Number/BOA Number (if this is applicable).                     |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchase-card-screen">Purchase Card screen</h5></td>
<td><p>DATE REQUIRED: T+30// <strong>&lt;Enter&gt;</strong> (JAN 11, 2002)</p>
<p>VENDOR: PROSVENDOR,ONE PH:555 555-5555 NO: 3</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ANY PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Select CONTRACT/BOA NUMBER: <strong>&lt;Enter&gt;</strong></p></td>
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
<td><h5 id="contractboa-number">Contract/BOA Number</h5></td>
<td><blockquote>
<p>You can enter two question marks, and press <strong>&lt;Enter&gt;</strong> to display a list and select an option from the <strong>Contract/BOA Number</strong> prompt. You can also bypass this prompt by pressing <strong>&lt;Enter.&gt;</strong> (This is an optional field.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="creating-the-po-number">Creating the PO number</h5></td>
<td><blockquote>
<p><strong>You will generate the Purchase Order number.</strong> The PO number, entered at the <strong>Purchase Order</strong> prompt is an alphanumeric combination as follows:</p>
</blockquote>
<ul>
<li><p>The PO number begins with the <u>Station Identifier</u> (which was selected at the <strong>Site</strong> prompt after first accessing the <strong>Purchase Card Form (PC)</strong> option shown at the beginning of this section).</p></li>
<li><p>After the Station Identifier numbers are <u>two digits</u> (one alpha and then numeric for the <u>fiscal year</u>), and then a <u>four-digit sequential number</u>. <strong><u>Example</u>:<br />
695-U20002.</strong></p></li>
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
<td><h5 id="purchase-card-name-and-number">Purchase Card Name and Number</h5></td>
<td><blockquote>
<p>A Purchase Card number consists of 16-digit numbers identifying a specific Purchase Card issued to a Purchasing Agent. It is encrypted for storage in files. The Purchase Card number will NOT display. This number prints in box 21 of the Purchase Order, unless the 2421 is reprinted by a different Purchasing Agent who does not have the RMPR FCP Manager key.</p>
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
<p>To create a PO number in the Purchase Card form, follow these steps:</p>
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
<td>20</td>
<td>Create a new <strong>Purchase Order Number</strong> <strong>or a Common Numbering Series</strong> by typing the first letter of the Common Numbering series<br />
(i.e., U) and the Fiscal Year (i.e., 2) at the <strong>Purchase Order</strong> prompt, and press <strong>&lt;Enter&gt;</strong>.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>Select a <strong>Purchase Card Name</strong> or press <strong>&lt;Enter&gt;</strong> to accept the default.</td>
</tr>
<tr class="even">
<td>22</td>
<td>Select the <strong>Cost Center</strong> number or enter two question marks to display a list and select one, and press &lt;<strong>Enter</strong>&gt;.</td>
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
<td><h5 id="purchase-card-screen-1">Purchase Card screen</h5></td>
<td><p>ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES</p>
<p>PURCHASE ORDER: <strong>U2</strong> <strong>&lt;Enter&gt;</strong> 695-U2 PC AUTHORIZED BUYER</p>
<p>Are you adding <strong>'695-U25692'</strong> as a new Purchase Order number? <strong>Y &lt;Enter&gt;</strong>(YES)</p>
<p>PURCHASE CARD NAME: FCP #932// <strong>&lt;Enter&gt;</strong> FCP #932</p>
<p>COST CENTER: 8272// <strong>? &lt;Enter&gt;</strong></p>
<p>Enter the Cost Center for this Purchase Order</p>
<p>Answer with COST CENTER</p>
<p>Choose from:</p>
<p><strong>8272 PROSVENDOR,THREE</strong></p>
<p>8273 PROSVENDOR,TWO</p>
<p>COST CENTER: 8272 <strong>&lt;Enter&gt;</strong> PROSVENDOR,THREE</p></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="vendor-tracking-number">Vendor Tracking Number</h5></td>
<td><blockquote>
<p>A <strong>Vendor Tracking Number</strong> is a number used for invoice tracking purposes. A vendor may supply their internal unique tracking number, <u>but it is not required</u>. A tracking number may be anything up to 20 characters long.</p>
<p><strong>Note:</strong> This prompt can be used for reconciliation purposes.</p>
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
<td><h5 id="steps-9">Steps</h5></td>
<td><blockquote>
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                                                                                  |
| 23   | Select a Type of Transaction option from a list.                                                                                                                                                                                                                    |
| 24   | Select a Patient Category option from a list (see options below). If you select the fourth option (NSC/OP), you will be prompted with the Special Category prompt with the following options: 1) Special Legislation, 2) A&A, 3) PHC, or 4) Eligibility Reform. |
| 25   | Select the Item from the Item file. Note: There may be multiple items, and if so, then the Type of Transaction prompt returns for you to begin again. (You should also check eligibility for an item at the Item Level.)                                    |
| 26   | Enter a Vendor Tracking Number (not required), or press \<Enter\> to bypass this prompt.                                                                                                                                                                        |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchase-card-screen-2">Purchase Card screen</h5></td>
<td><p>TYPE OF TRANSACTION: <strong>I</strong> <strong>&lt;Enter&gt;</strong> INITIAL ISSUE</p>
<p>PATIENT CATEGORY:</p>
<p>Enter a code from the list.</p>
<p>Select one of the following:</p>
<p>1 SC/OP</p>
<p>2 SC/IP</p>
<p>3 NSC/IP</p>
<p>4 NSC/OP</p>
<p>PATIENT CATEGORY: <strong>3 &lt;Enter&gt;</strong> NSC/IP</p>
<p>Select ITEM: <strong>SHOES &lt;Enter&gt;</strong></p>
<p>1 SHOES-AMBULATORS-LEATHER 14846 SHOES-AMBULATORS-LEATHER</p>
<p>2 SHOES-CUSTOM MOLDED 12258 SHOES-CUSTOM MOLDED</p>
<p>3 SHOES-CUSTOM-ORTHOPEDIC 12259 SHOES-CUSTOM-ORTHOPEDIC</p>
<p><strong>4 SHOES-EXTRA DEPTH INLAY 12257 SHOES-EXTRA DEPTH INLAY</strong></p>
<p>5 SHOES-ORTHO INLAY 15207 SHOES-ORTHO INLAY</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: <strong>4</strong> <strong>&lt;Enter&gt;</strong> 12257 SHOES-EXTRA DEPTH INLAY</p>
<p>...OK? Yes// (Yes)</p>
<p>VENDOR TRACKING NUMBER: <strong>&lt;Enter&gt;</strong></p></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="description-fields">Description fields</h5></td>
<td><blockquote>
<p>The following are two description prompts as described below:</p>
</blockquote>
<ul>
<li><p>Brief Description (REQUIRED)</p></li>
<li><p>Extended Description</p></li>
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
<td><h5 id="steps-10">Steps</h5></td>
<td><blockquote>
<p>To continue to create a Purchase Card form, follow these steps:</p>
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
<td>27</td>
<td>Select a <strong>PSAS HCPCS</strong> from a list that pertains to the Item. The Item may require a <strong>CPT Modifier</strong> to be selected. If so, you will be prompted with a selection.</td>
</tr>
<tr class="odd">
<td>28</td>
<td><p>Enter a <strong>Brief Description</strong> of 3 to 60 characters (short description of the Item purchased).</p>
<ul>
<li><p>Enter the <strong>MOST IMPORTANT</strong> information here because this appears on the Purchase Order (i.e., catalog number, model number, and a description for one item).</p></li>
<li><p>You should also add delivery instructions here.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>29</td>
<td><p>Enter an <strong>Extended Description</strong> (optional) or press <strong>&lt;Enter&gt;</strong> to bypass this prompt. This is a word processing field and contains many lines for you to type a lengthier description if needed.</p>
<ul>
<li><p>This prompt prints as an attachment. You can enter, “<em><strong>See Attachment</strong></em>” for orders with multiple Items on one transaction.</p></li>
<li><p>You can include the color, size, or confirmation number, etc.</p></li>
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
<td><h5 id="purchase-card-screen-3">Purchase Card screen</h5></td>
<td><p>PSAS HCPCS: <strong>?? &lt;Enter&gt;</strong></p>
<p>Health Care Financing Administration Common Procedure Coding System, (HCPCS). This field should have the HCPCS code for the Item you are selecting. HCPCS is a uniform method to report professional services, procedures and supplies for healthcare providers and medical suppliers.</p>
<p>PSAS HCPCS: <strong>L3250</strong> <strong>&lt;Enter&gt;</strong> CUSTOM MOLD SHOE REMOVE PROST</p>
<p>Enter a CPT MODIFIER for HCPCS L3250: (LT/RT/B): <strong>B</strong> <strong>&lt;Enter&gt;</strong> Both Left and Right</p>
<p>BRIEF DESCRIPTION OF ITEM (for Vendor): <strong>Style #1245, Mens Size 10E</strong> <strong>&lt;Enter&gt;</strong></p>
<p>EXTENDED DESCRIPTION:</p>
<p>No existing text</p>
<blockquote>
<p>Edit? NO// <strong>&lt;Enter&gt;</strong> (NO)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="unit-cost">Unit Cost</h5></td>
<td><blockquote>
<p>The <strong>Unit Cost</strong> is the cost of each unit – or one item being ordered.</p>
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
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                                                                                                                          |
| 30   | Enter a Quantity for the Item(s) being ordered (maximum 300 items).                                                                                                                                                                                                                                         |
| 31   | Enter a Unit Cost.                                                                                                                                                                                                                                                                                          |
| 32   | Select a Unit of Issue (i.e., “EA” for Each).                                                                                                                                                                                                                                                               |
| 33   | Enter identifying information at the Remarks prompt with a maximum of 30 characters in length. (These remarks display on Screen 4 of the 2319.) This prompt is used to quickly identify an Item such as the style or size entered.                                                                      |
| 34   | At the Type of Transaction prompt, you can select another transaction for another Item, or press \<Enter\> to bypass this prompt.                                                                                                                                                                       |
| 35   | Enter the Estimated Shipping Charge or press \<Enter\> to bypass this prompt.                                                                                                                                                                                                                           |
| 36   | Enter the Percent Discount or press \<Enter\> to bypass this prompt. (Estimated Cost and Actual Cost is calculated with the percent discount. This is automatically calculated according to the Vendor that is selected.) Note: If you use this prompt, it will change the Unit Cost automatically. |
| 37   | Enter the Bank Authorization Number or press \<Enter\> to bypass this prompt. (Optional.)                                                                                                                                                                                                               |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchase-card-screen-4">Purchase Card screen</h5></td>
<td><p>QTY: <strong>1 &lt;Enter&gt;</strong></p>
<p>UNIT COST: <strong>102.50 &lt;Enter&gt;</strong></p>
<p>UNIT OF ISSUE: <strong>pr</strong> <strong>&lt;Enter&gt;</strong> PAIR</p>
<p>REMARKS: <strong>Style #1245 Size 10E</strong> <strong>&lt;Enter&gt; <em>{This info will not appear on the<br />
order, only on the 2319 record.}</em></strong></p>
<p>------------------------------</p>
<p>TYPE OF TRANSACTION: <strong>{<em>Enter to bypass or start over for a new item here.}</em></strong></p>
<p>EST. SHIPPING CHARGE: <strong>5.50</strong> <strong>&lt;Enter&gt;</strong></p>
<p>PERCENT DISCOUNT: <strong>&lt;Enter&gt;</strong></p>
<p>BANK AUTHORIZATION NUMBER: <strong>&lt;Enter&gt;</strong></p></td>
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
<td><h5 id="bank-authorization-number-optional">Bank Authorization Number (optional)</h5></td>
<td><blockquote>
<p>The <strong>Bank Authorization Number</strong> (optional information) is a 6-digit number the Vendor obtains from the Purchase Card issuer (i.e., VISA). The Purchasing Agent can request this number from the vendor when an order is placed. If the vendor does not supply it when the order is placed, you can add it later. This number can be used in the reconciliation process of statements at close out.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="deliver-to">Deliver To </h5></td>
<td><blockquote>
<p>You have four delivery choices including the following: 1) the Veteran, 2) VAMC Warehouse, 3) Prosthetics, or 4) Other.</p>
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
<td><h5 id="option-to-edit-or-delete">Option to Edit or Delete</h5></td>
<td><blockquote>
<p>At the <strong>Are you ready to POST to 10-2319 NOW?</strong> prompt, you have the option to edit any prompt for the Item or to delete the transaction. To review the display of your prompts, press <strong>&lt;Enter&gt;</strong> and accept the default of <strong>No</strong>. Otherwise, type <strong>Yes</strong> to post the order.</p>
</blockquote>
<ul>
<li><p>If you press <strong>&lt;Enter&gt;</strong>, you will automatically be taken to the <strong>Edit</strong> screen to change any information before posting.</p></li>
<li><p>If you type, “<strong>^</strong>”, the following prompt will display: <strong>Do you want to delete the Transaction? No</strong>//. You can press <strong>&lt;Enter&gt;</strong> to accept the default of No. Otherwise, type <strong>Yes</strong> to delete the entire transaction.</p></li>
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
<td><h5 id="steps-12">Steps</h5></td>
<td><blockquote>
<p>To continue to create a Purchase Card form, follow these steps:</p>
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
<td>38</td>
<td>Select the location for the delivery of the order in the <strong>Deliver To</strong> prompt.</td>
</tr>
<tr class="odd">
<td>39</td>
<td><p>At the Are you ready to POST to 10-2319 NOW? prompt, type Y for Yes to post it.</p>
<ul>
<li><p>Press <strong>&lt;Enter&gt;</strong> to accept the default of <strong>No</strong> to be automatically routed to the Edit screen to change any prompt before posting the order.</p></li>
<li><p>Type an “^” and press <strong>&lt;Enter&gt;</strong> if you want to delete the transaction.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>40</td>
<td>You can print the Privacy Act Statement (optional). See Appendix A.</td>
</tr>
<tr class="odd">
<td>41</td>
<td>You can print the Notification Letter (optional). See Appendix A.</td>
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
<td><h5 id="purchase-card-screen-5">Purchase Card screen</h5></td>
<td><p>DELIVER TO: <strong>Veteran</strong> <strong>&lt;Enter&gt;</strong> VETERAN</p>
<p>Are you ready to POST to 10-2319 NOW? No// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Would you like to print the Privacy Act Statement? Yes// <strong>N</strong> <strong>&lt;Enter&gt;</strong> (No)</p>
<p>Would you like to print a Patient Notification letter? No// <strong>&lt;Enter&gt;</strong> (No)</p></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="electronic-signature">Electronic Signature</h5></td>
<td><blockquote>
<p>Your Transaction will be REJECTED and DELETED if you do not enter an Electronic Signature. Notify your Application Coordinator if your signature is invalid.</p>
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
<td><h5 id="steps-13">Steps</h5></td>
<td><blockquote>
<p>To continue to create a Purchase Card form, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                     |
| 42   | Enter your Electronic Signature Code (although nothing displays for confidentiality purposes).         |
| 43   | At the Device prompt, press \<Enter\> or enter the Printer name.                                   |
| 44   | The printout displays on your screen (as shown on the next page.)                                          |
| 45   | The Suspense Processing screen displays. You have the option to link the order to the Suspense record. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchase-card-screen-6">Purchase Card screen</h5></td>
<td><p>Your Transaction will be REJECTED and DELETED if you</p>
<p>do not enter an Electronic Signature!</p>
<p>Enter ELECTRONIC SIGNATURE CODE: <em><strong>&lt;Enter electronic signature code here&gt;</strong></em></p>
<p>Thank you.</p>
<p>Cost of this request: <strong>$102.50 &lt;Enter&gt;</strong></p>
<p>Current Control Point Balance: $135,652.86</p>
<p>Posting to Patient 2319 ...</p>
<p>Purchase Card Transaction has been assigned Number: 000-U00000</p>
<p>Updated 10-2319</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>OMB Number 2900-0188 Estimated Burden: 4 minutes</p></td>
</tr>
</tbody>
</table>

Continued on next page

Create a Purchase Card Form (PC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="final-output">Final output</h5></td>
<td><blockquote>
<p>Below is the online screen Purchase Card form. This can also be printed out and faxed or mailed to a vendor. <strong>Required:</strong> Write in the expiration date for the vendor as shown below.</p>
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
<td><h5 id="printout-of-purchase-card-form">Printout of Purchase Card Form</h5></td>
<td><p>*ORIGINAL COPY AND COMMERCIAL INVOICE MUST BE SUBMITTED*</p>
<p><u>TO THE VAMC PROSTHETIC ACTIVITY LISTED BELOW</u></p>
<p><u>Department of Veterans Affairs|Prosthetic Authorization for Items or Services</u></p>
<p>1. Name and Address of Vendor 2. Name and Address of VA Facility</p>
<p>PROSVENDOR,ONE Hines Development System (499/121)</p>
<p>CORPORATE ORDER ENTRY BUILDING #37</p>
<p>PO BOX 1140 HINES, IL 60142</p>
<p>ANY PARK,IL 60064</p>
<p>(555) 555-5555 222</p>
<p>------------------------------------------------------------------------------</p>
<p>3. Veterans Name (Last, First, MI) 4. Date of Authorization</p>
<p>PROSPATIENT,TWO JUN 26, 2002</p>
<p>------------------------------------------------------------------------------</p>
<p>5. Veterans Address 6. Date Required</p>
<p>100 ANY ST JUL 26, 2002</p>
<p>HOLLYWOOD,CALIFORNIA --------------------------------------</p>
<p>9. Authority For Issuance CFR 17.115</p>
<p>CHARGE MEDICAL APPROPRIATION</p>
<p>------------------------------------------------------------------------------</p>
<p>7. Claim Number 101122750P 8. SSN 000-00-0002</p>
<p>------------------------------------------------------------------------------</p>
<p>10. Statistical Data 11. FOB Point 12. Discount 13. Delivery Time</p>
<p>NSC/IP DEST % 30 Days</p>
<p>------------------------------------------------</p>
<p>14. Delivery To: VETERAN</p>
<p>------------------------------------------------------------------------------</p>
<p>15. DESCRIPTION OF ITEMS OR SERVICES AUTHORIZED</p>
<p>------------------------------------------------------------------------------</p>
<p>ITEM NUMBER DESCRIPTION/NOMENCLATURE QUANTITY UNIT UNIT AMOUNT</p>
<p>ORDERED PRICE</p>
<p>------------------------------------------------------------------------------</p>
<p>#1. Shoes Extra Depth Style #1245, Size 10E 1 PR 102.50 102.50</p>
<p>------------------------------------------------------------------------------</p>
<p>16. Contract Number: Subtotal: 102.50</p>
<p>ACCT.#: 17000000 Discount $ 0.00 Shipping: 5.50 Total $ 108.00</p>
<p>------------------------------------------------------------------------------</p>
<p>17. Signature of 18. DATE 19. Signature and Title of 20. Date</p>
<p>Requesting Official Contracting/Accountable Officer</p>
<p>PROSPROVIDER,FOUR PROSPROVIDER,FIVE</p>
<p>------------------------------------------------------------------------------</p>
<p>Order and Receipt Action</p>
<p>------------------------------------------------------------------------------</p>
<p>21. Order Number 22. Date of Order 23. Date Item Received 24. Date Delivered</p>
<p>1234567890123456 JUN 26,2002</p>
<p>------------------------------------------------------------------------------</p>
<p>25. The articles or services listed herein have been received, or rendered</p>
<p>ordered in the quantity and quality specified originally or as shown by</p>
<p>authenticated changes, except as noted.</p>
<p>EXPIRATION DATE: 9/2003 Signature of Veteran or VA Official</p>
<p>------------------------------------------------------------------------------</p>
<p>VOUCHER AUDIT BLOCK (For use by VA Facility only)</p>
<p>------------------------------------------------------------------------------</p>
<p>Bank Authorization Number: Acct. Symbol <strong>000-U00000</strong></p>
<p>------------------------------------------------------------------------------</p>
<blockquote>
<p>ADP Form 10-2421PC APR 1991</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Edit a Purchase Card Transaction

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-2">Introduction</h5></td>
<td><blockquote>
<p>Once you have posted a transaction, you can only edit the <strong>Bank Authorization Number</strong> on a Purchase Card order through the <strong>Edit Purchase Card Transaction (EDPC)</strong> option located under the <strong>Purchasing Menu (PU)</strong> as shown below.</p>
<p><u><em>You should edit a Purchase Card when you reconcile through the</em> <strong>Reconcile/Close Out Purchase Card Transaction (CPO)</strong> option</u>. You can edit a Purchase Card after it has been closed through the <strong>Edit 2319 (ED2)</strong> option. Some fields are not available from the <strong>CPO</strong> option (i.e., <strong>Source</strong> and <strong>CPT Modifier</strong>); then use the <strong>ED2</strong> option.</p>
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
<td><h5 id="purchasing-pu-menu">Purchasing (PU) Menu</h5></td>
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
<p><strong>ED2 Edit 2319</strong></p>
<p><strong>EDPC Edit Purchase Card Transaction</strong></p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>EDPC</strong> <strong>&lt;Enter&gt;</strong> Edit Purchase Card Transaction</p>
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
<td><h5 id="bank-authorization-number">Bank Authorization Number</h5></td>
<td><blockquote>
<p>(Optional prompt.) If you did not add the <strong>Bank Authorization Number</strong> during the entry of the new transaction, it may be added later using the <strong>Edit Purchase Card Transaction (EDPC)</strong> option as shown below.</p>
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
<p>SITE: Hines Development System// 499</p>
<p>Select PATIENT:PROSPATIENT,ONE PROSPATIENT,ONE 1-1-30 000890765 NO PILL</p>
<p>Enter &lt;RETURN&gt; to continue. HINES, IL</p>
<p>1 PROSPATIENT,ONE 8-20-2001 PROSPATIENT,ONE BA: EYEGLASSES</p>
<p>WHEELCHAIR GLOV</p>
<p>2 PROSPATIENT,ONE 9-27-2001 PROSPATIENT,ONE EYEGLASSES</p>
<p>SHOES</p>
<p>3 PROSPATIENT,ONE 11-20-2001 PROSPATIENT,ONE SHOE COMPONENTS</p>
<p>CHOOSE 1-3: <strong>1</strong> <strong>&lt;Enter&gt;</strong> 8-20-2001 PROSPATIENT,ONE BA: EYEGLASSES</p>
<p>WHEELCHAIR GLOV</p>
<p>BANK AUTHORIZATION NUMBER: <strong>?? &lt;Enter&gt;</strong></p>
<p>This six-digit number is the authorization number VISA gives to the vendor for guaranteed payment. This number is used in the reconciliation process.</p>
<p>BANK AUTHORIZATION NUMBER: <strong>123456 &lt;Enter&gt;</strong></p>
<p>Would You like to Edit another Entry (Y/N) ? <strong>NO</strong> <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Edit a Purchase Card Transaction, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="editing-through-the-purchase-card-form-pc">Editing through the Purchase Card Form (PC)…</h5></td>
<td><blockquote>
<p>When you are creating a <strong>Purchase Card Form (PC)</strong>, at the <strong>Are you ready to POST to 10-2319 NOW?</strong> prompt, press <strong>&lt;Enter&gt;</strong> to accept the default of <strong>No</strong> to edit the Purchase Card transaction. (Do not type Yes!!)</p>
<p>A summary of the transaction will display. You can edit any of the prompts available including the Item, the quantity, etc. This feature is available in case an error was made in the entry process.</p>
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
<td><span id="p23" class="anchor"></span><strong>Purchase Card Edited Order</strong></td>
<td><p>Are you ready to POST to 10-2319 NOW? No// <strong>N &lt;Enter&gt;</strong> (No)</p>
<p>000-00-0001 Purchase Card</p>
<p>499-7P0078 1234567890123456</p>
<p>------------------------------------------------------------------------------</p>
<p>ITEM: 925 SHOES AMIS: 21 B</p>
<p>VENDOR TRACKING:</p>
<p>PSAS HCPCS CODE: L3250 CUSTOM MOLD SHOE REMOV PROST</p>
<p>CPT MODIFIER: LT,RT</p>
<p>REMARKS: Style #1245 Mens Size 10#</p>
<p>DESCRIPTION: Style #1245, Mens Size 10E</p>
<p>CONTRACT #:</p>
<p>MODEL:</p>
<p>SERIAL NUMBER:</p>
<p>LOT #:</p>
<p>UNIT COST: 102.50 UNIT OF ISSUE: PR QTY: 1 ITEM COST: 102.50</p>
<p>TYPE: INITIAL CATEGORY: NSC/IP SPECIAL CATEGORY:</p>
<p>SUB TOTAL: $ 102.50</p>
<p>SHIPPING CHARGE: $ 5.50</p>
<p>TOTAL COST: $ 108.00</p>
<p>BANK AUTHORIZATION: 123456</p>
<p><strong>Enter Item to Edit:</strong> SHOE COMPONENTS</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>TYPE OF TRANSACTION: INITIAL ISSUE//</p>
<p>PATIENT CATEGORY: NSC/IP// <strong>&lt;Enter&gt;</strong></p>
<p>ITEM: SHOE COMPONENTS// <strong>&lt;Enter&gt;</strong></p>
<p>VENDOR TRACKING NUMBER: 1122334455// <strong>&lt;Enter&gt;</strong></p>
<p>BRIEF DESCRIPTION: Style #1245, Mens Size 10E Replace <strong>&lt;Enter&gt;</strong></p>
<p>EXTENDED DESCRIPTION:</p>
<p>No existing text</p>
<p>Edit? NO// <strong>&lt;Enter&gt;</strong></p>
<p><strong>QTY:</strong> 1// <strong>2 &lt;Enter&gt; {Edited this prompt}</strong></p>
<p>UNIT COST: 20// <strong>&lt;Enter&gt;</strong></p>
<p>UNIT OF ISSUE: EA// <strong>&lt;Enter&gt;</strong></p>
<p>REMARKS: Style #1245 Mens Size 10# Replace <strong>&lt;Enter&gt;</strong></p>
<p>EST. SHIPPING CHARGE: <strong>&lt;Enter&gt;</strong></p>
<p>PERCENT DISCOUNT: 20// <strong>&lt;Enter&gt;</strong></p>
<p>BANK AUTHORIZATION NUMBER: 123456// <strong>&lt;Enter&gt;</strong></p>
<p>DATE REQUIRED: DEC 20,2002// <strong>&lt;Enter&gt;</strong></p>
<p>DELIVER TO: VETERAN// <strong>&lt;Enter&gt;</strong></p>
<p>Enter Item to Edit:</p></td>
</tr>
</tbody>
</table>

#### Link a Purchase Card Transaction to the Suspense Record

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="description">Description</h5></td>
<td><blockquote>
<p>The <strong>Suspense Processing List Manager</strong> screen displays automatically after creating a Purchase Card transaction. This allows you to link the transaction (item being purchased) to the patient’s suspense entry.</p>
<p><strong>Note:</strong> Refer to the Release Notes for Patch RMPR*3*62 for more information on linking.</p>
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
<td><span id="p24" class="anchor"></span><strong>Suspense Processing List Manager Screen</strong></td>
<td><p>Suspense Processing Nov 20, 2001@13:54:07 Page: 1 of 2__</p>
<p>Open/Pending/Closed Suspense for PROSPATIENT,ONE (000-00-0001) '!' = STAT</p>
<p><u>Date Type Requestor Description Init Act Days Status</u></p>
<p>1 10/09/01 ROUTINE PROVIDER,SIX SHOES EXTRA DEPTH @30 OPEN</p>
<p>2 08/29/01 MANUAL PROVIDER,SIX MANUAL SUSPENSE ENTERE @59 OPEN</p>
<p>3 08/16/00 MANUAL PROVIDER,FOUR DESCRIPTION OF APPLIAN @329 OPEN</p>
<p>4 08/15/00 MANUAL PROVIDER,FOUR EDIT DESCRIPTION. @330 OPEN</p>
<p>5 07/05/00!ROUTINE PROVIDER,SIX DESCRIPTION OF APPLIA 04/26/01 *211 CLOSED</p>
<p>6 05/24/00 MANUAL PROVIDER,FOUR EDITING THE DESCRIPTI 08/02/00 *50 CLOSED</p>
<p>7 05/16/00 MANUAL PROVIDER,SIX This is a test. 07/05/00 *36 CLOSED</p>
<p>8 05/11/00 MANUAL PROVIDER,FOUR Editing free-text fie 05/11/00 0 CLOSED</p>
<p>9 05/05/00 MANUAL PROVIDER,FOUR Adding a manual suspe @402 OPEN</p>
<p>10 03/27/00 MANUAL A;DLKJA;SDLFJA;L @431 OPEN</p>
<p>11 03/27/00 ROUTINE 08/03/00 *93 CLOSED</p>
<p><u>12 03/22/00 MANUAL PROVIDER,FOUR ADDING A PATIENT SUSPE @434 OPEN_</u></p>
<p><u>+ Enter ?? for more actions___________________________________________</u></p>
<p>23 Display 2319 PI Post Initial Action CD CPRS Display</p>
<p>VR View Request OT Post Other CR Cancel Request</p>
<p>IA View Initial Action PC Post Complete FW Forward Consult</p>
<p>VO View Other Action AD Add Manual PR Print Consult</p>
<p>CO View Complete ED Edit Manual</p>
<p>Select Item(s): Next Screen// <strong>PC &lt;Enter&gt;</strong> Post Complete</p>
<p>Enter a list or range of numbers (1-14): <strong>1 &lt;Enter&gt;</strong></p>
<p>List of 2319 Records:</p>
<p><strong>1. 11/20/01 SHOE EXTRA DEPTH PROSVENDOR,ONE</strong></p>
<p>Enter 2319 Record to be LINKED : (1-1): <strong>1</strong> <strong>&lt;Enter&gt;</strong></p>
<p>COMPLETE NOTE:</p>
<p><strong>PO to PROSVENDOR,ONE</strong></p>
<p>Edit? NO//</p></td>
</tr>
</tbody>
</table>

#### Cancel Purchase Card Transaction (CPC)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchasing-option">Purchasing option</h5></td>
<td><blockquote>
<p>The <strong>Cancel Purchase Card Transaction (CPC)</strong> option will cancel the Purchase Card transaction and remove the purchase from the Patient's 10-2319 Record.</p>
<p>This option allows you to select the patient’s name, Purchase Card number or Bank Authorization number, but you must have an electronic signature code on file. If you do not, contact your IRM.</p>
<p>When you have completed the cancellation process, the <strong>Suspense</strong> <strong>(SU) Menu</strong> displays allowing you to process orders (including viewing notes, entering notes, and completing orders) for a patient. When the transaction is cancelled, the control point is automatically updated.</p>
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
<td><h5 id="steps-14">Steps</h5></td>
<td><blockquote>
<p>To cancel a Purchase Card transaction, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Step | Action                                                                                              |
| 1    | Select the Purchasing (PU) Menu, and then select the Cancel Purchase Card Transaction (CPC) option. |
| 2    | Select a Site from a list or press \<Enter\> to accept the default site.                    |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchasing-menu-1">Purchasing Menu</h5></td>
<td><blockquote>
<p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p><strong>CPC Cancel Purchase Card Transaction</strong></p>
<p>CPO Reconcile/Close Out Purchase Card Transaction</p>
<p>ED2 Edit 2319</p>
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>CPC</strong> <strong>&lt;Enter&gt;</strong> Cancel Purchase Card Transaction</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>You may also make a selection by Purchase Card Transaction</p>
<p>(Example, PC number), or Bank Authorization Number (6 digit number).</p>
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
<td><h5 id="site-1">Site</h5></td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetic Service covers multiple stations. This is a non-editable field (for display purposes only). Entering a question mark &lt;<strong>?</strong>&gt; will bring up a list of sites for which you will need to define the locations. Select a site or enter the number(s) for your station.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Cancel Purchase Card Transaction (CPC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="confirmation-prompt">Confirmation prompt</h5></td>
<td><blockquote>
<p>At the confirmation prompt, <strong>Do you really want to CANCEL this Transaction?</strong>, you can answer <strong>Yes</strong> or <strong>No</strong> or you may enter an '<strong>^</strong>' to Quit.</p>
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
<td><h5 id="steps-15">Steps</h5></td>
<td><blockquote>
<p>To continue to cancel a Purchase Card transaction, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                    |
|------|--------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                             |
| 3    | Select a Prosthetic Patient.                                                                                       |
| 4    | At the Do you really want to CANCEL this Transaction? prompt, type Y for Yes to continue the cancellation. |
| 5    | At the Effective Date prompt, press \<Enter\> to accept the default of the current date.                   |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><span id="p35" class="anchor"></span><strong>Cancel Purchase Card Transaction screen</strong></td>
<td><p>Select PATIENT: PROSPATIENT,THREE <strong>&lt;Enter&gt;</strong> PROSPATIENT,THREE 12-27-50 000122750 YES SC VETERAN</p>
<p>STENT-MULTI-LIN</p>
<p>000-00-0003 Purchase Card</p>
<p>695-Y02699 1234567890123456</p>
<p>------------------------------------------------------------------------------</p>
<p>ITEM: 46346 STENT-MULTI-LINK-3.0-13MM AMIS: 20</p>
<p>VENDOR TRACKING: 2344</p>
<p>PSAS HCPCS CODE: SI523 STENT, CORONARY</p>
<p>CPT MODIFIER: GX</p>
<p>DESCRIPTION: STENT-TRISTAR-3.0X13</p>
<p>CONTRACT #:</p>
<p>MODEL:</p>
<p>SERIAL NUMBER:</p>
<p>LOT #:</p>
<p>UNIT COST: 1425.00 UNIT OF ISSUE: EA QTY: 1 ITEM COST: 1425.00</p>
<p>TYPE: INITIAL CATEGORY: NSC/IP SPECIAL CATEGORY:</p>
<p>SUB TOTAL: $1425.00</p>
<p>SHIPPING CHARGE: $ 0.00</p>
<p>TOTAL COST: $1425.00</p>
<p>BANK AUTHORIZATION:</p>
<p>Do you really want to CANCEL this Transaction? <strong>Y &lt;Enter&gt;</strong> (Yes)</p>
<p>Amendment Number: 1</p>
<p>...copying Purchase Order into work file...</p>
<p>...SORRY, HOLD ON...</p>
<p>EFFECTIVE DATE: JUL 8,1998// &lt;<strong>Enter</strong>&gt; (JUL 08, 1998)</p></td>
</tr>
</tbody>
</table>

Continued on next page

Cancel Purchase Card Transaction (CPC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="type-comments">Type Comments</h5></td>
<td><blockquote>
<p>The <strong>Type Comments</strong> prompt (optional) provides a free-text response of comments about the type amendment. You can type 3 to 150 characters here. You can press <strong>&lt;Enter&gt;</strong> and bypass this field.</p>
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
<td><h5 id="confirmation-prompt-1">Confirmation Prompt</h5></td>
<td><blockquote>
<p>At the confirmation prompt, <strong>Sure You Want to Cancel this Order?,</strong> you must enter a <strong>Yes</strong> or a <strong>No</strong>, or you may enter an '<strong>^</strong>' to Quit.</p>
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
<td><h5 id="approve-amendment-number">Approve Amendment Number &lt;#&gt;</h5></td>
<td><blockquote>
<p>Every time you make an amendment to a transaction, that information is sent to IFCAP. IFCAP then sends back the next Amendment number when requesting to cancel a transaction. The prompt is shown below: <strong>Approve Amendment Number &lt;#&gt; ?</strong>.</p>
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
<td><h5 id="cancel-purchase-card-transaction-screen">Cancel Purchase Card Transaction Screen</h5></td>
<td><blockquote>
<p>TYPE COMMENTS: <strong>Canceling this transaction. &lt;Enter&gt;</strong></p>
<p>SURE YOU WANT TO CANCEL THIS ORDER ? <strong>Y</strong> &lt;<strong>Enter</strong>&gt; (YES)</p>
<p><strong>Approve Amendment number 1: ? YES//</strong> &lt;<strong>Enter</strong>&gt; (YES)</p>
<p>Enter ELECTRONIC SIGNATURE CODE: <strong>Enter signature code here.</strong> <strong>&lt;Enter&gt;</strong> Thank you.</p>
<p>...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...</p>
<p>...copying amendment information back to Purchase Order file...</p>
<p>...EXCUSE ME, JUST A MOMENT PLEASE...</p>
<p>...now creating entry in File 410 for the amendment....</p>
<p>CANCELLATION REMARKS: <strong>Incorrect vendor.</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>Transaction Canceled and Deleted...</p>
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
<td><h5 id="electronic-signature-code">Electronic Signature Code</h5></td>
<td><blockquote>
<p>Enter your electronic signature code, and press <strong>&lt;Enter&gt;</strong> to continue the cancellation of the transaction.</p>
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
<td><h5 id="cancellation-remarks-required-entry">Cancellation Remarks (Required Entry)</h5></td>
<td><blockquote>
<p>The <strong>Cancellation Remarks,</strong> a <u>required</u> entry, can consist of any remarks the Purchasing Agent or Prosthetic Clerk would like to state in the mail message. The reply must consist of a minimum of 3 characters and a maximum of 60 characters in length.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Reconcile/Close Out Purchase Card Transaction (CPO)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-3">Introduction</h5></td>
<td><blockquote>
<p>The <strong>Reconcile/Close Out Purchase Card Transaction (CPO)</strong> option is used to close out purchasing transactions that used the Purchase Card. The reconciliation must be processed using the Prosthetics system, not IFCAP. <strong>If you only close out in IFCAP, it does not automatically close in Prosthetics.</strong></p>
<p>To close out a transaction, you can select the patient’s name, date, Purchase Card transaction number (example, Purchase Order (PO) number), or Bank Authorization number (6-digit number). You can also compare prices to make sure they are correct using this option.</p>
<p><strong>NOTE:</strong> You must be the cardholder or an Approving Official (alternate) to reconcile the order. If you are not, contact your IRM.</p>
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
<td><h5 id="editing-a-po">Editing a PO</h5></td>
<td><blockquote>
<p>You can use this <strong>Reconcile/Close Out Purchase Card Transaction</strong> <strong>(CPO)</strong> option to make edits to the PO without closing the Purchase Card transaction.</p>
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
<td><h5 id="closing-a-po">Closing a PO</h5></td>
<td><blockquote>
<p>If you created a PO in IFCAP, you would close it there. If you create it in Prosthetics, then you would close it in Prosthetics.</p>
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
<td><h5 id="reconciliation-scenarios">Reconciliation Scenarios</h5></td>
<td><blockquote>
<p>There are several scenarios that can occur when reconciling Purchase Card transactions. Here are just some of the scenarios that can happen with Purchase Card transactions and will require different methods to resolve.</p>
</blockquote>
<ul>
<li><p>Filing a dispute when reconciling a Purchase Card transaction regarding a Vendor.</p></li>
<li><p>Reconciling a partial order on a Purchase Card transaction.</p></li>
<li><p>Vendor has double charged the Purchase Card.</p></li>
<li><p>Vendor bills the wrong Purchase Card.</p></li>
<li><p>Vendor sends the wrong item, which needs to be returned with a credit given and then re-charged for the correct item received.</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> Some screen samples and/or instructions for some of these scenarios are shown at the end of this topic.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reconcile/Close Out Purchase Card Transaction (CPO), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="reconciliation-checkpoints">Reconciliation checkpoints</h5></td>
<td><blockquote>
<p>The cardholder must complete 75% of the reconciliations within 10 days, 95% within 17 days, and 100% within 30 days. The Approving Officials must approve all reconciliations within 14 calendar days.</p>
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
<td><h5 id="steps-16">Steps</h5></td>
<td><blockquote>
<p>To begin the process of reconciling/closing out a Purchase Card transaction using this option, follow the steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                               |
| 1    | Select the Reconcile/Close Out Purchase Card Transaction (CPO) option from the Purchasing (PU) Menu. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchasing-menu-pu">Purchasing Menu (PU)</h5></td>
<td><blockquote>
<p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p>CPC Cancel Purchase Card Transaction</p>
<p><strong>CPO Reconcile/Close Out Purchase Card Transaction</strong></p>
<p>ED2 Edit 2319</p>
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>CPO</strong> <strong>&lt;Enter&gt;</strong> Reconcile/Close Out Purchase Card Transaction</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reconcile/Close Out Purchase Card Transaction (CPO), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="patient-order-data">Patient order data</h5></td>
<td><blockquote>
<p>When you select the patient or the Purchase Card number, data will display for the Purchase Card transaction including the following:</p>
</blockquote>
<ul>
<li><p>Item</p></li>
<li><p>Vendor</p></li>
<li><p>PSAS HCPCS Code</p></li>
<li><p>CPT Modifier</p></li>
<li><p>Deliver to (location)</p></li>
<li><p>Description</p></li>
<li><p>Serial number</p></li>
<li><p>Unit cost</p></li>
<li><p>Type</p></li>
<li><p>Category</p></li>
<li><p>Subtotal</p></li>
<li><p>Shipping charges</p></li>
<li><p>Total cost of the order.</p></li>
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
<td><h5 id="steps-17">Steps</h5></td>
<td><blockquote>
<p>To continue to reconcile/close out a Purchase Card transaction, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Step | Action                                                                               |
| 2    | Select the Site (if a multi-site facility).                                      |
| 3    | Select the Prosthetic Patient or enter the PO number, and the data will display. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><span id="p40" class="anchor"></span><strong>Screen display</strong></td>
<td><p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>You may also make a selection by Purchase Card Transaction</p>
<p>(Example, PO number), or Bank Authorization Number (6 digit number).</p>
<p>Select PATIENT: 1-19-2001 PROSPATIENT,ONE BA: CANE</p>
<p>000-00-0001 Purchase Card</p>
<p>695-U256925 encrypted</p>
<p>------------------------------------------------------------------------------</p>
<p>ITEM: 903 CANE/WOODEN AMIS: 05 D</p>
<p>VENDOR TRACKING:</p>
<p>PSAS HCPCS CODE: E0100 CANE ADJUST/FIXED WITH TIP</p>
<p>CPT MODIFIER: NU</p>
<p>DELIVER TO:</p>
<p>DESCRIPTION: CANE</p>
<p>CONTRACT #:</p>
<p>MODEL:</p>
<p>SERIAL NUMBER:</p>
<p>LOT #:</p>
<p>UNIT COST: 24 UNIT OF ISSUE: EA QTY: 1 ITEM COST: 24.00</p>
<p>TYPE: INITIAL CATEGORY: SC/OP SPECIAL CATEGORY:</p>
<p>SUB TOTAL: $ 24.00</p>
<p>SHIPPING CHARGE: $ 3.00</p>
<p>TOTAL COST: $ 27.00</p>
<p>BANK AUTHORIZATION:</p></td>
</tr>
</tbody>
</table>

Continued on next page

Reconcile/Close Out Purchase Card Transaction (CPO), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="confirmation-prompt-2">Confirmation prompt</h5></td>
<td><blockquote>
<p>At the <strong>Ready to Reconcile and Close-Out Transaction? NO//?</strong> prompt, you can reconcile and post the transaction. If there is an incorrect amount, it can be changed at this prompt by responding with a <strong>NO</strong>. You will then be taken through all the prompts that allow you to change a part of the order. Then answer <strong>YES</strong> when this prompt appears again to continue the reconciliation process.</p>
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
<td><h5 id="ifcap-order-fcp">IFCAP Order FCP</h5></td>
<td><blockquote>
<p>The <strong>IFCAP Order FCP</strong> prompt is the interface between Prosthetics and IFCAP. If you only close out in IFCAP, it does NOT automatically close in Prosthetics.</p>
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
<td><h5 id="steps-18">Steps</h5></td>
<td><blockquote>
<p>To continue to reconcile/close out a Purchase Card transaction, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                      |
| 4    | At the Ready to Reconcile and Close-Out Transaction prompt, type Yes to continue. If you need to correct any prompt, type No, or press \<Enter\> to be taken through all the prompts again. |
| 5    | At the Close-Out Remarks prompt, enter free text (i.e., Invoice number). Press \<Enter\>.                                                                                                           |
| 6    | At the IFCAP Order FCP prompt, you are routed into IFCAP to reconcile the purchase order.                                                                                                               |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-1">Screen sample</h5></td>
<td><p><strong>Ready to Reconcile and Close-Out Transaction?</strong> NO// <strong>YES</strong> <strong>&lt;Enter&gt;</strong></p>
<p>...now posting to file 660...</p>
<p><strong>CLOSE-OUT REMARKS:</strong> CLOSE OUT// <strong>&lt;Enter&gt;</strong></p>
<p>You are reconciling this PURCHASE CARD ORDER:</p>
<p><strong>IFCAP Order FCP:</strong> 910 PROSTHETICS Purchase Date: JAN 19, 2001</p>
<p>Vendor Name: PROSVENDOR,ONE P.O.#: <strong>000-U00000</strong></p>
<p>STATUS: $Amount: 27.00</p>
<p>Total Reconciled Charges: 27.00</p>
<p>------------------------------------------------------------------------------</p>
<p>The system is attempting to locate credit card charge...</p>
<p>Matching Card XXXX3456, Vendor's Purchase Order #:</p>
<p>Listing All Credit Card Charges with Matched Card XXXX1234:</p>
<p>01-19-01 $30.00</p>
<p>...Ok for 7P0065 PROSVENDOR,ONE? YES// <strong>&lt;Enter&gt;</strong></p></td>
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
<td><h5 id="to-exit-before-closing">To Exit before closing</h5></td>
<td><blockquote>
<p>You can exit before you reconcile or close out a transaction by entering an “<strong>^</strong>” to exit the <strong>Reconcile/Close Out Purchase Card Transaction (CPO)</strong> option. You can then proceed to reconcile or close out at a later time.</p>
<p><strong>Note:</strong> If you exit before closing or reconciling and you have made any edits, those fields will not be changed and will remain unedited.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reconcile/Close Out Purchase Card Transaction (CPO), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="action-code">Action Code</h5></td>
<td><blockquote>
<p>At the end of the reconciliation process, you can select any of the actions (IFCAP actions) displayed below including:</p>
</blockquote>
<ul>
<li><p>RC – Reconcile</p></li>
<li><p>DO – Display Order</p></li>
<li><p>RS – Reselect Charges</p></li>
<li><p>RD – Redisplay Data</p></li>
<li><p>DC – Display Charges</p></li>
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
<td><h5 id="steps-19">Steps</h5></td>
<td><blockquote>
<p>To continue to reconcile/close out a Purchase Card transaction, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Step | Action                                                                           |
| 7    | Type RC at the Action prompt to reconcile the Purchase Card form.        |
| 8    | At the Complete Order Received prompt, type Y for Yes.                   |
| 9    | At the Final Charge prompt, type Y for Yes if appropriate.               |
| 10   | At the Edit? prompt, press \<Enter\> to bypass the editing of the order. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-2">Screen sample</h5>
<p>Action Code</p></td>
<td><p>You are reconciling this PURCHASE CARD ORDER:</p>
<p>IFCAP Order FCP: 910 PROSTHETICS Purchase Date: JAN 19, 2001</p>
<p>Vendor Name: PROSVENDOR,ONE P.O.#: 000-U00000</p>
<p>STATUS: $Amount: 51.00</p>
<p>Total Reconciled Charges: 27.00</p>
<p>------------------------------------------------------------------------------</p>
<p>to this credit card CHARGE:</p>
<p>Reconcile Doc: C49910197P0065 Purchase Date: JAN 19, 2001</p>
<p>Vendor Name: P.O.#:</p>
<blockquote>
<p>TXN REF: $Amount: 27.00</p>
</blockquote>
<p>You are reconciling this PURCHASE CARD ORDER:</p>
<p>IFCAP Order FCP: 910 PROSTHETICS Purchase Date: JAN 19, 2001</p>
<p>Vendor Name: PROSVENDOR,ONE P.O.#: 000-U00000</p>
<p>STATUS: $Amount: 27.00</p>
<p>Total Reconciled Charges: 27.00</p>
<p>------------------------------------------------------------------------------</p>
<p>to this credit card CHARGE:</p>
<p>Reconcile Doc: C99999197P0065 Purchase Date: JAN 19, 2001</p>
<p>Vendor Name: P.O.#:</p>
<p>TXN REF: $Amount: 27.00</p>
<p>------------------------------------------------------------------------------</p>
<p>WARNING: The CC-charge amount and purchase card order amount are different.</p>
<p>______________________________________________________________________________</p>
<p>Action Code: <strong>RC: Reconcile</strong> DO: Display Order RS: Reselect Charges</p>
<p>RD: Redisplay Data DC: Display Charges</p>
<p><strong>Action:</strong> <strong>RC &lt;Enter&gt;</strong></p>
<p>COMPLETE ORDER RECEIVED: NO// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> YES</p>
<p>WARNING: If a credit or additional charge is expected against this order number, do NOT respond YES.</p>
<p>FINAL CHARGE: NO// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> YES</p>
<p>COMMENTS:</p>
<p>No existing text</p>
<p>Edit? NO// <strong>&lt;Enter&gt;</strong></p>
<p>Generating ET-document to FMS...</p>
<p>Enter Next Transaction to Close-out, or &lt;RETURN&gt; to continue.</p></td>
</tr>
</tbody>
</table>

Continued on next page

Reconcile/Close Out Purchase Card Transaction (CPO), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="filing-a-dispute">Filing a dispute</h5></td>
<td><blockquote>
<p>You can file a dispute when reconciling a Purchase Card transaction. Notice a partial screen print is shown below. This scenario shows that you would like to file a dispute.</p>
<p>You would then fill out the Department of Veterans Affairs Cardholder Dispute Form and forward it to the banking agency.</p>
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
<td><h5 id="screen-sample-with-dispute-prompt">Screen sample with Dispute prompt</h5></td>
<td><p>You are reconciling this PURCHASE CARD ORDER:</p>
<p>IFCAP Order FCP: 913 PROSTHETIC APPLIANCES Purchase Date: MAY 28, 2002</p>
<p>Vendor Name: PROSVENDOR,FOUR P.O.#: 000-U00000</p>
<p>STATUS: Partial Payment (Complete Rec) $Amount: 47.00</p>
<p>Total Reconciled Charges: 47.00</p>
<p>to this credit card CHARGE:-------------------------------</p>
<p>Reconcile Doc: C69521709008003 Purchase Date: JUN 18, 2002</p>
<p>Vendor Name: PROSVENDOR,FOUR P.O.#: 1234</p>
<p>TXN REF: 24435232169980839957234 $Amount: 47.00</p>
<p>------------------------------------------------------------------------------</p>
<p>______________________________________________________________________________</p>
<p>Action Code: <strong>RC: Reconcile</strong> DO: Display Order RS: Reselect Charges</p>
<p>RD: Redisplay Data DC: Display Charges</p>
<p>Action: <strong>RC &lt;Enter&gt;</strong></p>
<p>COMPLETE ORDER RECEIVED: YES// <strong>&lt;Enter&gt;</strong></p>
<p>WARNING: If a credit or additional charge is expected against this order number do NOT respond YES.</p>
<p>FINAL CHARGE: NO// <strong>&lt;Enter&gt;</strong></p>
<p><strong>Are you going to dispute this charge amount?: NO//YES &lt;Enter&gt;</strong></p>
<p>COMMENTS:</p>
<p>1&gt;<strong>VENDOR CHARGED INCORRECTLY AGAINST VA RECORDS &lt;Enter&gt;</strong></p>
<blockquote>
<p>EDIT Option:</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reconcile/Close Out Purchase Card Transaction (CPO), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scenario-when-a-vendor-double-charges">Scenario: When a Vendor Double Charges</h5></td>
<td><blockquote>
<p>When a vendor double charges the VA for an item for a patient, you can <u>remove</u> the item through IFCAP using the <strong>Edit/Remove Reconciliation</strong> option. You can route to the option by entering: <strong>“^PC”</strong> at the “<strong>Select Purchasing Option</strong>” prompt in Prosthetics. See the sample below for more IFCAP prompt-level details:</p>
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
<td><h5 id="sample-ifcap-screen">Sample IFCAP screen</h5>
<p>Duplicate charge</p></td>
<td><p>Select Purchasing Option: <strong>^PC</strong></p>
<p>1 Purchase Card Form [RMPR4 PC] (PC)</p>
<p>2 Print Closed Suspense Records [RMPR SUSPENSE PRINT CLOSED] (PC)</p>
<p>3 Print Closed Home/Liaison Visits [RMPR H/L PRINT CLOSED] (PC)</p>
<p><strong>4 Purchase Card Menu [PRCH PURCHASE CARD MENU] (PC)</strong></p>
<p>Type '^' to stop, or choose a number from 1 to 4 :<strong>4</strong> PC Purchase Card Menu</p>
<p>You have 131 charge(s) to be reconciled for statement (06/27/02 - 07/08/02).</p>
<p>Purchase Card Reports Menu ...</p>
<p>Approving Official Menu ...</p>
<p>Process Purchase Card Menu ...</p>
<p>Purchase Card Display/Print Menu ...</p>
<p>Purchase Card Order Reconcile - Oracle Data</p>
<p><strong>Reconciliation Menu</strong> ...</p>
<p>Select Purchase Card Menu Option: <strong>REC</strong>onciliation Menu</p>
<p>Reconciliation</p>
<p><strong>Edit/Remove Reconciliation</strong></p>
<p>ET-FMS Document Display</p>
<p>Daily Purchase Card Charges Statement</p>
<p>Select Reconciliation Menu Option: <strong>ED</strong>it/Remove Reconciliation</p>
<p>Select Reconciled/Disputed C-Document/Purchase Card Order: 1U1234 05-28-02</p>
<p>PC Partial Payment (Complete Rec)</p>
<p>FCP: 913 $ 47.00</p>
<p><strong>1 123-2U8694</strong></p>
<p><strong>C12345678901234 06-18-02 $47.00 PROSVENDOR,FOUR</strong></p>
<p>2 123-2U8694</p>
<p>C12345678901234 06-18-02 $47.00 PROSVENDOR,FOUR</p>
<p>CHOOSE 1-2: <strong>1</strong> <strong>&lt;Enter&gt;</strong> C12345678901234 06-18-02 $47.00 PROSVENDOR,FOUR</p>
<p> WARNING </p>
<p>This charge is reconciled. If you 'Edit' it, another approval will be needed.</p>
<p>If you 'Remove' the reconciliation, you must reconcile the charge and your</p>
<p>Approving Official will have to approve it again.</p>
<p>Use the action code DD (Display Document) if no change is desired.</p>
<p>Do you want to continue? NO// <strong>YES &lt;Enter&gt;</strong></p>
<p>______________________________________________________________________________</p>
<p>Action Code: <strong>ED: Edit</strong> DO: Display Order ND: Next Document</p>
<p><strong>RM: Remove</strong> DD: Display Document</p>
<p>Action: <strong>RM &lt;Enter&gt;</strong></p>
<p>COMMENTS:</p>
<p>1&gt;<strong>VENDOR DOUBLE CHARGED &lt;Enter&gt;</strong></p>
<p>EDIT Option: <strong>&lt;Enter&gt;</strong></p>
<blockquote>
<p>AFTER Removing Change P.O. Status to: Partial Payment (Complete Rec)// 48</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reconcile/Close Out Purchase Card Transaction (CPO), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scenario-partial-reconciliation">Scenario: Partial Reconciliation</h5></td>
<td><blockquote>
<p>You can reconcile a partial Purchase Card transaction. If there are multiple items on a Purchase Card transaction and only part of the order has been fulfilled, you can reconcile a partial order so that a partial payment can be made.</p>
<p>At the <strong>Complete Order Received</strong> prompt, you would type “No” when reconciling the partial order. At the <strong>Final Charge</strong> prompt, you would also type “No.” Then when the order has been completely fulfilled, you would use the <strong>Reconcile/Close Out Purchase Card Transaction (CPO)</strong> option again, and type, “Yes” to these two prompts.</p>
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
<td><h5 id="scenario-vendor-bills-the-wrong-purchase-card">Scenario: Vendor bills the wrong Purchase Card</h5></td>
<td><blockquote>
<p>If a vendor bills the wrong Purchase Card, you can correct this error. This is another common scenario. You would follow these IFCAP steps to resolve it:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>In IFCAP, you would select the <strong>Purchase Card Menu</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Select the <strong>Process Purchase Card Menu</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Select the <strong>New Detailed Purchase Card Order</strong> option.</p>
</blockquote></li>
<li><blockquote>
<p>Enter a NEW Purchase Order number.</p>
</blockquote></li>
<li><blockquote>
<p>Enter the Purchase Card Name.</p>
</blockquote></li>
<li><blockquote>
<p>Bypass through all prompts until you select the vendor.</p>
</blockquote></li>
<li><blockquote>
<p>At the <strong>FCP</strong> prompt, you can change the Fund Control Point to replace it with the correct one.</p>
</blockquote></li>
<li><blockquote>
<p>Again, continue to either answer or bypass prompts (as necessary) and exit at the <strong>Enter a New Purchase Order Number or a Common Numbering Series Purchase Order</strong> prompt.</p>
</blockquote></li>
<li><blockquote>
<p>In Prosthetics, access the <strong>Reconciliation Menu</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Select the <strong>Reconciliation</strong> option.</p>
</blockquote></li>
<li><blockquote>
<p>Select the <strong>Reconcile by Purchase Card Order #</strong> option.</p>
</blockquote></li>
<li><blockquote>
<p>Enter the Purchase Card Order number.</p>
</blockquote></li>
<li><blockquote>
<p>At the <strong>Action</strong> prompt, enter <strong>RC</strong> to reconcile.</p>
</blockquote></li>
<li><blockquote>
<p>At the <strong>Complete Order Received</strong> prompt, type Yes.</p>
</blockquote></li>
<li><blockquote>
<p>At the <strong>Final Charge</strong> prompt, type No.</p>
</blockquote></li>
<li><blockquote>
<p>At the <strong>Comments</strong> prompt, type “<em>Vendor billed wrong card</em>.”</p>
</blockquote></li>
</ol>
<blockquote>
<p>At a later time, after the financial institution received the correct Purchase Card information from the vendor, you can perform a reconciliation and answer “Yes” at the <strong>Final Charge</strong> prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Reprints (RP) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Reprint a Purchase Card Form (PCR)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-4">Introduction</h5></td>
<td><blockquote>
<p>The <strong>Reprint a Purchase Card Form (PCR)</strong> option reprints the Purchase Card transaction. You can access this option from the <strong>Reprints Menu (RP)</strong> which is under the <strong>Purchasing Menu (PU)</strong>.</p>
<p><strong>Note:</strong> If you reprint a Purchase Order that you did not create, then the Purchase Card number is encrypted for security purposes.</p>
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
<td><h5 id="purchasing-pu-menu-1">Purchasing (PU) Menu</h5></td>
<td><blockquote>
<p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p><strong>RP Reprints ...</strong></p>
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
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>RP &lt;Enter&gt;</strong> Reprints</p>
<p>24 Reprint a 2421 Form</p>
<p>PSC Reprint a 10-55 Form</p>
<p><strong>PCR Reprint a Purchase Card Form</strong></p>
<p>Select Reprints Option: <strong>PCR</strong> <strong>&lt;Enter&gt;</strong> Reprint a Purchase Card Form</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reprint a Purchase Card Form (PCR), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="select-transaction-or-patient-name">Select Transaction or Patient Name</h5></td>
<td><blockquote>
<p>The form to reprint is selected at the <strong>Select Transaction or Patient Name</strong> prompt. In response to this prompt, you may enter any of the following to search for the Purchase Card form and reprint it:</p>
</blockquote>
<ul>
<li><p>Prosthetics date</p></li>
<li><p>Patient name</p></li>
<li><p>Reference number</p></li>
<li><p>Purchase Card number</p></li>
<li><p>Bank Authorization number</p></li>
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
<td><h5 id="screen-sample-3">Screen sample</h5></td>
<td><p>Select Transaction or Patient Name:<strong>PROSPATIENT,ONE</strong> <strong>&lt;Enter&gt;</strong> PROSPATIENT,ONE 1-1-30 000000001 NO PILL</p>
<p>Enrollment Priority: Category: IN PROCESS End Date:</p>
<p>* Patient Requires a Means Test *</p>
<p>Primary Means Test Required from FEB 13,2002</p>
<p>Enter &lt;RETURN&gt; to continue. HINES, IL</p>
<p>1 PROSPATIENT,ONE 9-27-2001 PROSPATIENT,ONE EYEGLASSES</p>
<p>SHOES</p>
<p>2 PROSPATIENT,ONE 11-20-2001 PROSPATIENT,ONE SHOE COMPONENTS</p>
<p>3 PROSPATIENT,ONE 11-20-2001 PROSPATIENT,ONE CANE</p>
<p>4 PROSPATIENT,ONE 11-27-2001 PROSPATIENT,ONE WHEELCHAIR</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-4: <strong>1 &lt;Enter&gt;</strong> 9-27-2001 PROSPATIENT,ONE EYEGLASSES</p>
<blockquote>
<p>SHOES</p>
<p>Would you like to print the Privacy Act Statement? Yes// <strong>N &lt;Enter&gt;</strong> (No)</p>
<p>Would you like to print a Patient Notification letter? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
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
<td><h5 id="options">Options</h5></td>
<td><blockquote>
<p>This option will also ask if you wish to reprint the <strong>Privacy Act Statement</strong> and the <strong>Patient Notification Letter</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reprint a Purchase Card Form (PCR), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="pcr-option">PCR option</h5></td>
<td><blockquote>
<p>Below is a sample of a <strong>Reprint a Purchase Card Form</strong>:</p>
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
<td><h5 id="screen-sample-4">Screen sample</h5></td>
<td><p>*ORIGINAL COPY AND COMMERCIAL INVOICE MUST BE SUBMITTED*</p>
<p>TO THE VAMC PROSTHETIC ACTIVITY LISTED BELOW</p>
<p>______________________________________________________________________________Department of Veterans Affairs|Prosthetic Authorization for Items or Services</p>
<p>------------------------------------------------------------------------------</p>
<p>1. Name and Address of Vendor 2. Name and Address of VA Facility</p>
<p>PROSVENDOR,ONE Hines Development System (499/121)</p>
<p>CORPORATE ORDER ENTRY BUILDING #37</p>
<p>PO BOX 1140 HINES, IL 60142</p>
<p>ANY PARK,IL 60064</p>
<p>(800) 255-5162 222</p>
<p>------------------------------------------------------------------------------</p>
<p>3. Veterans Name (Last, First, MI) 4. Date of Authorization</p>
<p>PROSPATIENT,ONE JUN 26, 2002</p>
<p>------------------------------------------------------------------------------</p>
<p>5. Veterans Address 6. Date Required</p>
<p>ANY ST. JUL 26, 2002</p>
<p>CHICAGO,ILLINOIS 60000 --------------------------------------</p>
<p>9. Authority For Issuance CFR 17.115</p>
<p>CHARGE MEDICAL APPROPRIATION</p>
<p>------------------------------------------------------------------------------</p>
<p>7. Claim Number 8. SSN 000-00-0001</p>
<p>------------------------------------------------------------------------------</p>
<p>10. Statistical Data 11. FOB Point 12. Discount 13. Delivery Time</p>
<p>SC/OP ORIGIN % 1 30 Days</p>
<p>------------------------------------------------</p>
<p>14. Delivery To: VETERAN</p>
<p>------------------------------------------------------------------------------</p>
<p>15. DESCRIPTION OF ITEMS OR SERVICES AUTHORIZED</p>
<p>------------------------------------------------------------------------------</p>
<p>ITEM NUMBER DESCRIPTION/NOMENCLATURE QUANTITY UNIT UNIT AMOUNT</p>
<p>ORDERED PRICE</p>
<p>------------------------------------------------------------------------------</p>
<p>#1. EYEGLASSES 1 EA 1.00 1.00</p>
<p>#2. SHOES 1 PR 20.00 20.00</p>
<p>------------------------------------------------------------------------------</p>
<p>16. Contract Number: Subtotal: 21.00</p>
<p>ACCT.#: 17000000 Discount $ 0.21 Shipping: 10.00 Total $ 30.79</p>
<p>------------------------------------------------------------------------------</p>
<p>17. Signature of 18. DATE 19. Signature and Title of 20. Date</p>
<p>Requesting Official Contracting/Accountable Officer</p>
<p>PROVIDER,SIX PROSPROVIDER,FIVE</p>
<p>------------------------------------------------------------------------------</p>
<p>Order and Receipt Action</p>
<p>------------------------------------------------------------------------------</p>
<p>21. Order Number 22. Date of Order 23. Date Item Received 24. Date Delivered</p>
<p>encrypted JUN 26, 2002</p>
<p>------------------------------------------------------------------------------</p>
<p>25. The articles or services listed herein have been received, or rendered</p>
<p>ordered in the quantity and quality specified originally or as shown by</p>
<p>authenticated changes, except as noted.</p>
<p>EXPIRATION DATE: 9/2003 Signature of Veteran or VA Official</p>
<p>------------------------------------------------------------------------------</p>
<p>VOUCHER AUDIT BLOCK (For use by VA Facility only)</p>
<p>------------------------------------------------------------------------------</p>
<p>Bank Authorization Number: Acct. Symbol 695-U25693</p>
<p>------------------------------------------------------------------------------</p>
<blockquote>
<p>ADP Form 10-2421PC APR 1991</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Purchase Card Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Report List

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-5">Introduction</h5></td>
<td><blockquote>
<p>Below is a list of available reports from the <strong>Purchasing (PU)</strong> <strong>Menu</strong> regarding Purchase Cards:</p>
</blockquote>
<ul>
<li><p>List Open Purchase Card Transactions (LPC)</p></li>
<li><p>List Open Purchase Card Transactions by Initiator (LPCI)</p></li>
<li><p>Purchase Card Summary Sheet (LPS)</p></li>
</ul>
<blockquote>
<p>These reports are good tools for managers to monitor the number of outstanding open orders. They are also good tools to follow up with vendors on open orders.</p>
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
<td><h5 id="list-open-purchase-card-transactions-lpc">List Open Purchase Card Transactions (LPC)</h5></td>
<td><blockquote>
<p>The <strong>List Open Purchase Card Transactions (LPC)</strong> Report will list all open Purchase Card Transactions. The Purchase Card number will be encrypted. Only the creator (the purchase cardholder) and the Supervisor can view this number.</p>
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
<td><h5 id="list-open-purchase-card-transactions-by-initiator-lpci">List Open Purchase Card Transactions by Initiator (LPCI)</h5></td>
<td><blockquote>
<p>The <strong>List Open Purchase Card Transactions By Initiator</strong> <strong>(LPCI)</strong> option will display a list of the open Purchase Card transactions by the employee that initiated the transaction.</p>
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
<td><h5 id="purchase-card-summary-sheet-lps">Purchase Card Summary Sheet (LPS)</h5></td>
<td><blockquote>
<p>The <strong>Purchase Card Summary Sheet (LPS)</strong> Report displays the Purchase Card Summary by Card Number. It will list the open and closed obligations.</p>
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
<td><h5 id="in-this-section-1">In this section</h5></td>
<td><blockquote>
<p>This section covers the following topics:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                                 |          |
|-----------------------------------------------------------------|----------|
| Topic                                                           | See Page |
| List Open Purchase Card Transactions (LPC) Report               | 40       |
| List Open Purchase Card Transactions by Initiator (LPCI) Report | 41       |
| Purchase Card Summary Sheet (LPS) Report                        | 43       |

#### List Open Purchase Card Transactions (LPC) Report

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-6">Introduction</h5></td>
<td><blockquote>
<p>The <strong>List Open Purchase Card Transactions (LPC)</strong> Report will list all open Purchase Card transactions. The Purchase Card number will be encrypted, except for the creator (the Purchase Card cardholder) and the Supervisor.</p>
<p>You will be prompted to enter starting and ending dates. This list will show patients’ names, social security numbers, Purchase Card numbers, dates, vendors, items, and costs in order by Purchase Card number.</p>
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
<td><h5 id="purchasing-menu-pu-1">Purchasing Menu (PU)</h5></td>
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
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p><strong>LPC List Open Purchase Card Transactions</strong></p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>LPC</strong> <strong>&lt;Enter&gt;</strong> List Open Purchase Card Transactions</p>
<p>This report lists Open Purchase Card Transactions created in the</p>
<p>Prosthetics Package.</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Starting Date: <strong>T-90</strong> <strong>&lt;Enter&gt;</strong> (AUG 08, 2001)</p>
<p>Ending Date: <strong>T</strong> <strong>&lt;Enter&gt;</strong> (NOV 06, 2001)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>...HMMM, HOLD ON...</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-output">Report output</h5></td>
<td><blockquote>
<p>AUG 08, 2001-NOV 06, 2001 Open 2421PC Transactions STA 499 PAGE 1</p>
<p><strong>Patient SSN Purchase Card Date PC # Vendor Item Item Cost</strong></p>
</blockquote>
<p>PATIENT,FOUR 0004 9999999999999999 01/23 U28633 VENDOR,FIVE PUMP-ALPHA 30.00</p>
<p>PATIENT,FOUR 0004 9999999999999999 01/23 U28648 VENDOR,FIVE ZONE 10-DM 90.00</p>
<p>PATIENT,FIVE 0005 9999999999999999 02/08 U29889 VENDOR,FIVE BED-ELECTR 85.50</p>
<p>PATIENT,SIX 0006 9999999999999999 01/29 U29063 VENDOR,SIX GARMENT-JO 9.00</p>
<p>PATIENT,SEVEN 0007 9999999999999999 02/07 U29851 VENDOR,SEVEM WHEELCHAIR 78.00</p>
<p>PATIENT,EIGHT 0008 9999999999999999 02/15 2U0534 VENDOR,EIGHT WHEELCHAIR 5.31</p>
<p>PATIENT,NINE 0009 9999999999999999 02/22 2U1013 VENDOR,NINE WHEELCHAIR 140.69</p>
<p>WHEELCHAIR 298.27</p>
<p>PATIENT,TEN 0010 9999999999999999 03/01 2U1621 VENDOR,TEN PROSTHESIS 0.00</p>
<p>PROSTHESIS 118.50</p>
<blockquote>
<p>=========</p>
<p>Total 9319.77</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### List Open Purchase Card Transactions by Initiator (LPCI) Report

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-7">Introduction</h5></td>
<td><blockquote>
<p>The <strong>List Open Purchase Card Transactions By Initiator</strong> <strong>(LPCI)</strong> option is located under the <strong>Purchasing Menu (PU)</strong>. This option will list the open Purchase Card transactions by the Prosthetic employee that initiated the transaction. It provides the dollar value for each employee by the Purchase Card number.</p>
<p>If the creator requests a report for another employee, the Purchase Card number will be encrypted (except for the Purchase Card cardholder’s number) for security purposes.</p>
<p>The list will be sorted by transaction date and initiator. You will be prompted to enter a starting date and an ending date. This option will show patients’ names, social security numbers, obligation numbers, request dates, vendors, items, and costs.</p>
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
<td><h5 id="purchasing-menu-pu-2">Purchasing Menu (PU)</h5></td>
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
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p><strong>LPCI List Open Purchase Card Transactions By Initiator</strong></p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>LPCI &lt;Enter&gt;</strong> List Open Purchase Card Transactions By Initiator</p>
<p>This report lists Open Purchase Card Transactions created in the</p>
<p>Prosthetics Package.</p>
<p>This report is sorted by Transaction Date and Initiator.</p>
<p>The PC # column is the abbreviated Purchase Card Transaction Number,</p>
<p>Example: 644-PC546, would display as 546.</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Starting Date: <strong>T-90</strong> <strong>&lt;Enter&gt;</strong> (AUG 08, 2001)</p>
<p>Ending Date: <strong>T</strong> <strong>&lt;Enter&gt;</strong> (NOV 06, 2001)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>...HMMM, HOLD ON...</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

List Open Purchase Card Transactions by Initiator (LPCI) Report, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="effective-date-field">Effective Date field</h5></td>
<td><blockquote>
<p><u>Examples of Valid Dates</u>:</p>
</blockquote>
<ul>
<li><p>JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057</p></li>
<li><p>T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.</p></li>
<li><p>T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.</p></li>
</ul>
<blockquote>
<p>If the year is omitted, the computer uses the CURRENT YEAR. A two-digit year assumes no more than 20 years in the future, or 80 years in the past.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-output-1">Report output</h5></td>
<td><blockquote>
<p>AUG 08, 2001-NOV 06, 2001 Open 2421PC Transactions STA 499 PAGE 1</p>
<p>Initiator: PROVIDER,SIX</p>
<p><strong>Patient SSN Purchase Card Date PC # Vendor Item Item Cost</strong></p>
<p>------------------------------------------------------------------------------</p>
</blockquote>
<p>PATIENT1,ONE 0011 9999999999999999 02/27 W20150 VENDOR1,ONE PACEMAKER 7590.00</p>
<p>LEADWIRE 900.00</p>
<p>LEADWIRE 900.00</p>
<p>PATIENT1,TWO 0012 9999999999999999 02/27 W20152 VENDOR1,TWO BONE-SCREW 115.00</p>
<p>BONE-SCREW 115.00</p>
<p>ACETABULA 1081.00</p>
<p>SHEEL-POR 1466.00</p>
<p>FEMORAL-S 3252.38</p>
<p>FEMORAL-HE 405.75</p>
<p>=======</p>
<p>Total 15825.13</p>
<blockquote>
<p>AUG 08, 2001-NOV 06, 2001 Open 2421PC Transactions STA 499 PAGE 2</p>
<p>Initiator: PROSPROVIDER,FOUR</p>
<p><strong>Patient SSN Purchase Card Date PC # Vendor Item Item Cost</strong></p>
<p>------------------------------------------------------------------------------</p>
<p>PATIENT1,THREE 0013 1234567890123456 08/21 7P0074 VENDOR, ONEWALKER</p>
<p>PATIENT1,THREE 0013 1234567890123456 10/16 7P0075 VENDOR,ONE SHOE COMPO 220.00</p>
<p>=========</p>
<p>Total 220.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Purchase Card Summary Sheet (LPS) Report

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-8">Introduction</h5></td>
<td><blockquote>
<p>The <strong>Purchase Card Summary (LPS)</strong> Report displays the Purchase Card Summary by card number. It will list the open and closed obligations over a date range. This report tracks the amount spent on a per transaction basis.</p>
<p>This option also keeps track of the total cumulative amount authorized, the total amount liquidated, and the total non-liquidated amount obligated for a Purchase Card.</p>
<p><u>This report identifies the following</u>:</p>
</blockquote>
<ul>
<li><p>Patient</p></li>
<li><p>Last four numbers of the Social Security Number</p></li>
<li><p>Date of the transaction</p></li>
<li><p>Purchase Card number</p></li>
<li><p>Authorized amount</p></li>
<li><p>Adjusted amount</p></li>
<li><p>Liquidated amount</p></li>
<li><p>Cumulative amount</p></li>
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
<td><h5 id="purchasing-menu-pu-3">Purchasing Menu (PU)</h5></td>
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
<p>EDPC Edit Purchase Card Transaction</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p><strong>LPS Purchase Card Summary Sheet</strong></p>
<p>Select Purchasing Option: <strong>LPS &lt;Enter&gt;</strong> Purchase Card Summary Sheet</p>
<p>Prosthetics Purchase Card Summary Sheet</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Starting Date: <strong>T-90</strong> <strong>&lt;Enter&gt;</strong> (AUG 08, 2001)</p>
<p>Ending Date: <strong>T</strong> <strong>&lt;Enter&gt;</strong> (NOV 06, 2001)</p>
<p>Enter PURCHASE CARD NUMBER: 1234567890123456 <strong>&lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>...HMMM, I'M WORKING AS FAST AS I CAN...</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Purchase Card Summary Sheet (LPS) Report, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="amount-column-descriptions">Amount Column descriptions</h5></td>
<td><blockquote>
<p>Below are the descriptions for the amount columns in this report:</p>
</blockquote>
<ul>
<li><p>The <strong>Authorized Amount</strong> column indicates the amount of the original transaction.</p></li>
<li><p>The <strong>Adjusted Amount</strong> column reflects any changes in price or shipping charges (and can be a negative number as shown below).</p></li>
<li><p>The <strong>Liquidated Amount</strong> column is the amount that is paid to the vendor for the transaction.</p></li>
<li><p>The <strong>Cumulative Amount</strong> column shows the cumulative total spent by the Purchasing Agent on a specific Purchase Card.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-output-2">Report output</h5></td>
<td><blockquote>
<p>AUG 08, 2001-NOV 06, 2001 1234567890123456 Summary STA 499 PAGE 1</p>
<p><strong>Patient SSN Date PC # Auth Amt Adj Amt Liq Amt Cum Amt</strong></p>
<p>------------------------------------------------------------------------------</p>
</blockquote>
<p>PATIENT1,FOUR 0014 01/02 U29999 38.25 0.00 38.25 38.25</p>
<p>PATIENT1,FIVE 0015 01/02 U29999 138.00 -1.00 137.00 175.25</p>
<p>PATIENT1,SIX 0016 01/02 U29999 22.50 0.00 22.50 197.75</p>
<p>PATIENT1,SEVEN 0017 01/02 U29999 85.50 0.00 85.50 283.25</p>
<p>PATIENT1,EIGHT 0018 01/02 U29999 85.50 0.00 85.50 368.75</p>
<p>PATIENT1,NINE 0019 01/02 U29999 22.50 0.00 22.50 391.25</p>
<p>PATIENT1,TEN 0110 01/02 U29999 36.15 0.00 36.15 427.40</p>
<p>PATIENT2,ONE 0021 01/02 U29999 36.15 0.00 36.15 463.55</p>
<p>PATIENT2,TW0 0022 01/02 U29999 36.15 6.50 42.65 506.20</p>
<p>PATIENT2,THREE 0023 01/02 U29999 25.65 4.35 30.00 536.20</p>
<p>PATIENT2,FOUR 0024 01/02 U29999 36.15 -10.50 25.65 561.85</p>
<p>PATIENT2,FIVE 0025 01/02 U29999 78.15 9.50 87.65 649.50</p>
<p>PATIENT2,SIX 0026 01/02 U29999 36.15 10.50 46.65 696.15</p>
<p>PATIENT2,SEVEN 0027 01/02 U29999 36.15 0.00 36.15 732.30</p>
<p>PATIENT2,EIGHT 0028 01/02 U29999 59.15 0.10 59.25 791.55</p>
<blockquote>
<p>------------------------------------------------------------------------------</p>
<p>TOTALS 772.10 19.45 791.55 6819.20</p>
<p>Total liquidated 791.55</p>
<p>Total non-liquidated 267.00</p>
<p>Total Cumulative Authorized 6819.20</p>
<p>Total Open Orders/Transactions 2</p>
<p>Total Closed Orders/Transactions 0</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Purchase Card Site Parameter (SS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-9">Introduction</h5></td>
<td><blockquote>
<p>The <strong>Purchase Card Site Parameter (SS)</strong> will be used to enter the site parameter for the Purchase Card. This option is located from the <strong>Enter New Request Menu (EN)</strong>. It will set the IFCAP site to be used on all Purchase Card transactions.</p>
<p><strong>Note:</strong> <u>This is a one-time setup process for a Prosthetics site</u>. This form will update the patient’s electronic 10-2319.</p>
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
<td><h5 id="screen-sample-5">Screen sample</h5></td>
<td><p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p>PC Purchase Card Form</p>
<p><strong>SS Purchase Card Site Parameter</strong></p>
<p>Select Enter New Request Option: <strong>SS</strong> <strong>&lt;Enter&gt;</strong> Purchase Card Site Parameter</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p><strong>Enter the IFCAP Site used with the Purchase Card Module</strong></p>
<p><strong>The following site you select will be used on all your</strong></p>
<p><strong>Purchase Card Transactions in IFCAP only.</strong></p>
<p>Select STATION NUMBER ('^' TO EXIT): 499//<strong>&lt;Enter&gt;</strong> 499 SUPPORT ISC</p>
<p>Select FISCAL YEAR ('^' to EXIT): 02//<strong>&lt;Enter&gt;</strong></p></td>
</tr>
</tbody>
</table>

## Satellite Broadcast – May, 2001

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Question and Answer Session

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="satellite-objectives">Satellite Objectives</h5></td>
<td><blockquote>
<p>Below are the questions and answers from the Satellite Broadcast training from May, 2001. These are the satellite objectives regarding the Purchase Card Reconciliation process:</p>
</blockquote>
<ul>
<li><p>Ability to explain vendor Level II Purchase Card status</p></li>
<li><p>Explain the difference between a monthly credit card limit and a single purchase limit, and how to request higher limits</p></li>
<li><p>Ability to correctly reconcile a Prosthetic Purchase Card transaction</p></li>
<li><p>Ability, as the Approving Official, to correctly approve a Prosthetic Purchase Card transaction</p></li>
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
<td><h5 id="purchase-limits">Purchase Limits</h5></td>
<td><blockquote>
<p>Who do I ask to have the purchasing agents’ monthly or single purchase limit amount increased?</p>
<p><strong>ANSWER: You should request this in writing to your Purchase Card Coordinator.</strong></p>
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
<td><h5 id="reconciling">Reconciling</h5></td>
<td><blockquote>
<p>How many days do I have to reconcile an order?</p>
<p><strong>ANSWER: Based on VHA Handbook 1730.1 (Use and Management of the Government Purchase Card Program) the cardholder must complete 75% of the reconciliations within 10 days, 95% within 17 days and 100% within 30 days to reconcile a purchase order. Unreconciled purchases increase the possibility of fraud and abuse. Incorrect billing not found promptly and protested with the card company may preclude recovery or credit.</strong></p>
<p>Why does Prosthetics reconcile using the Prosthetics software instead of the IFCAP software like everyone else?</p>
</blockquote>
<p>ANSWER: Prosthetics reconciles using the Prosthetics software because Prosthetics is required to close the order on the veteran’s Prosthetic record. There is an interface between the Prosthetics software and IFCAP. So when you reconcile in Prosthetics, the order in IFCAP is also closed.</p>
<blockquote>
<p>I receive the message on my screen that says I have 35 purchase card orders to reconcile. How do I know what those orders are? Can I get a report?</p>
<p><strong>ANSWER: Yes, you can get a list of the orders ready to be reconciled. In the Purchase Card Menu option in IFCAP, select the <em>Reconciliation Menu</em>, then the <em>Manual Charge Selection</em> option and enter the FCP. This will generate a listing for you. Actually, it expedites the reconciliation process if you automatically print this report whenever you have reconciliations. You can then match your paperwork to the listing, and the reconciliations will go quicker.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Question and Answer Session, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="approving-an-order">Approving an order</h5></td>
<td><blockquote>
<p>As the Approving Official, how many days do I have to approve an order?</p>
<p><strong>ANSWER: Based on the same VHA Handbook, the Approving Official has fourteen (14) calendar days to approve reconciliations.</strong></p>
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
<td><h5 id="fiscal">Fiscal</h5></td>
<td><blockquote>
<p>Is it required that after I reconcile a purchase order, I send to Fiscal a copy of the invoice and purchase order?</p>
<p><strong>ANSWER: This is not a national policy, but local Fiscal officers may require these documents as part of receipt record maintenance.</strong></p>
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
<td><h5 id="open-orders">Open Orders</h5></td>
<td><blockquote>
<p>Should I be monitoring my open purchase card orders? If so, how often and how should I do it?</p>
<p><strong>ANSWER: Yes, it is important to monitor open purchase card orders. You should contact (either in writing or by phone) the vendors who have not submitted their transaction to Citibank at least once every ten days. You then document the order that the vendor has been contacted.</strong></p>
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
<td><h5 id="outstanding-pos">Outstanding PO’s</h5></td>
<td><blockquote>
<p>If an employee resigns, who is responsible to reconcile their outstanding purchase orders?</p>
<p><strong>ANSWER: The Approving Official is responsible. They have been given special menu options to do this reconciliation. The Approving Official may designate a surrogate to do this job.</strong></p>
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
<td><h5 id="dispute-process">Dispute process</h5></td>
<td><blockquote>
<p>Could you explain the "Dispute" process? Is there a time limit to file a dispute?</p>
<p><strong>ANSWER: The dispute process is the method used for correction of erroneous charges that appear on a cardholder's account. A written dispute should be filed as soon as you are aware of the error but no later than 30 days. You may obtain the Government Dispute Form from your Purchase Card Coordinator.</strong></p>
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
<td><h5 id="amendment">Amendment</h5></td>
<td><blockquote>
<p>Why and when is an amendment created to a purchase card order?</p>
<p><strong>ANSWER: An amendment is created whenever you make a change to an existing order. This change could reflect a cost difference, quantity difference, additional shipping charges, etc. The purpose of the amendment is to capture the changes and correct the FCP balance when there is a cost change.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Question and Answer Session, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="detailed-vs.-simplified-purchase-card-order">Detailed vs. Simplified Purchase Card order</h5></td>
<td><blockquote>
<p>Other purchase card users at my facility are required to do a Detailed purchase card order. The Prosthetics software automatically generates a Simplified Purchase Card order. What's the difference and is there any way I can change our order to Detailed?</p>
<p><strong>ANSWER: Originally all Purchase Card users created Simplified Purchase Card orders in IFCAP. Only recently have Purchase Card users been instructed to use the Detailed order. The reason for the change to Detailed is because a Simplified order in IFCAP does not have an Item prompt, therefore you cannot get any type of Item History report.</strong></p>
<p><strong>With the Prosthetics software, since we have an Item prompt, we are able to get both an Item History as well as a HCPCS History. Therefore, there is no need to change our order to the Detailed.</strong></p>
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
<td><h5 id="purchase-order-numbers">Purchase Order Numbers</h5></td>
<td><blockquote>
<p>How can I get a vendor to include the purchase order number on their transaction to Citibank?</p>
<p><strong>ANSWER: The vendor must have Level II charge capabilities that allows them to enter the Purchase Order Number in the free text field.</strong> <strong>Without the Level II, the vendor is not able to include the PO number.</strong></p>
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
<td><h5 id="vendor-bill">Vendor bill</h5></td>
<td><blockquote>
<p>Is it true that a vendor should not bill Citibank until the item has been shipped?</p>
<p><strong>ANSWER: This is true. The vendor is not to bill Citibank until they have shipped the item. This would be in violation of their credit card agreements and federal procurement law. Any vendor who violates the process must be notified that they have prematurely charged the VA and they should process a credit for the full amount until the item can be shipped and properly charged. If vendors refuse to cooperate by issuing credits, Prosthetics may dispute the premature charges due to non-delivery.</strong></p>
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
<td><h5 id="unauthorized-charges">Unauthorized charges</h5></td>
<td><blockquote>
<p>What should I do if unauthorized charges are appearing?</p>
<p><strong>ANSWER: You should contact your supervisor if you believe someone is using your purchase card for unauthorized purchases. This is especially critical, as the cardholder is responsible for insuring that the card is utilized for official government business only.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Question and Answer Session, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="erroneous-charge">Erroneous charge</h5></td>
<td><blockquote>
<p>How do I get a charge off my account that was erroneously posted by Citibank?</p>
<p><strong>ANSWER: You should employ the "Dispute" process.</strong></p>
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
<td><h5 id="partial-shipment">Partial shipment</h5></td>
<td><blockquote>
<p>Do I close out a purchase order that has a partial shipment or wait until it has been shipped complete?</p>
<p><strong>ANSWER: You should close it out as Partial. Once the vendor ships the remaining items, they will again bill Citibank. The order will appear again to reconcile and at that time you can post it as a complete order.</strong></p>
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
<td><h5 id="record-keeping">Record-keeping</h5></td>
<td><blockquote>
<p>How long are we required to keep the reconciled purchase card orders?</p>
<p><strong>ANSWER: We are required to keep the documents for six (6) years.</strong></p>
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
<td><h5 id="processing-credits">Processing Credits</h5></td>
<td><blockquote>
<p>Could you define a credit and how should we process the credits?</p>
<p><strong>ANSWER: An example of a credit is when the item you purchased is defective and you are returning it. The company will then issue a credit against your purchase card for the returned item. Once the vendor has reshipped the item, they will recharge your credit card using the original purchase card order number.</strong></p>
<p><strong>In order to process the credit transaction, you select the <em>Purchase Card</em> <em>Menu</em> option in IFCAP, then the <em>Reconciliation Menu</em>, then select the <em>Edit/Remove Reconciliation</em> option. This will allow you to open the closed purchase card order</strong> <strong>in IFCAP and process the credit.</strong></p>
<p><strong>Once, the vendor has recharged your credit card for the reshipped item, you will need to use this same menu option to reconcile the purchase order a second time.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Privacy Act

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-10">Introduction</h5></td>
<td><blockquote>
<p>Below is a copy of the <strong>Privacy Act</strong> that can be printed optionally during the creation of a Purchase Card transaction.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-1"></h5></td>
<td><blockquote>
<p>52.224-2 PRIVACY ACT (APR 1984)</p>
<p>(a) The Contractor agrees to---</p>
<p>(1) Comply with the Privacy Act of 1974 (the Act) and the agency rules and</p>
<p>regulations issued under the Act in the design, development, or operation</p>
<p>of any system of records on individuals to accomplish an agency function when</p>
<p>the contract specifically identifies---</p>
<p>(i) The systems of records: and</p>
<p>(ii) The design, development, or operation work that the contractor is to</p>
<p>perform;</p>
<p>(2) Include the Privacy Act notification contained in this contract in every</p>
<p>solicitation and resulting subcontract and in every subcontract awarded without</p>
<p>a solicitation, when the work statement in the proposed subcontract required the</p>
<p>redesign, development, or operation of a system of records on individuals that</p>
<p>is subject to the Act; and</p>
<p>(3) Include this clause, including this subparagraph (3), in all subcontracts</p>
<p>awarded under this contract which requires the design, development, or operation of such a system of records.</p>
<p>(b) In the event of violations of the Act, a civil action may be brought against the agency involved when the violation concerns the design, development or</p>
<p>operation of a system of records on individuals to accomplish an agency function,</p>
<p>and criminal penalties may be imposed upon the officers or employees of the agency when the violation concerns the operation of a system of records on individuals to accomplish an agency function. For purposes of the Act, when the con-</p>
<p>tract is for the operation of a system of records on individuals to accomplish</p>
<p>an agency function, the Contractor is considered to be an employee of the agency.</p>
<p>(c) (1) "Operation of a system of records," as used in this clause, means per-</p>
<p>formance of any of the activities associated with maintaining the system of records, including the collection, use, and dissemination of records.</p>
<p>(2) "Record," as used in this clause, means any item, collection, or grouping</p>
<p>of information about an individual that is maintained by an agency, including,</p>
<p>but not limited to, education, financial transactions, medical history, and</p>
<p>criminal or employment history and that contains the person's name, or the iden-</p>
<p>tifying number, symbol, or other identifying particular assigned to the individual, such as a fingerprint or voiceprint or a photograph.</p>
<p>(3) "System of records on individuals" as used in this clause, means a</p>
<p>group of any records under the control of any agency from which information is</p>
<p>retrieved by the name of the individual or by some identifying number, symbol, or other identifying particular assigned to the individual.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Patient Notification Letter

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-11">Introduction</h5></td>
<td><blockquote>
<p>A <strong>Patient Notification</strong> <strong>Letter</strong> can be generated and sent to the patient optionally during the creation of a Purchase Card transaction.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Department of Veterans Affairs</p>
<p>Hines Development System</p>
<p>TEST 2</p>
<p>HINES, IL 60142</p>
<p>Nov 20, 2001</p>
<p>MR. PROSPATIENT,ONE In reply refer to: 499/121</p>
<p>STREET ADDRESS Accounting Symbol 7P0079</p>
<p>CHICAG, ILLINOIS 60000 Veteran: PROSPATIENT,ONE</p>
<p>SSN: 000-00-0001</p>
<p>Dear Mr. PROSPATIENT,ONE</p>
<p>This is to notify you that the items listed below were ordered</p>
<p>for you on Nov 20, 2001. Delivery of this equipment is expected</p>
<p>on or about Dec 20, 2001.</p>
<p>If you do not receive it within 5 days of the expected date,</p>
<p>please contact (Purchasing Agent), of my staff, at 555-555-5555.</p>
<p>Sincerely,</p>
<p>Name of Chief</p>
<p>CHIEF</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Glossary

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="boc">BOC</h5></td>
<td><blockquote>
<p><strong>Budget Objective Code</strong> – Object classification codes are used to report VA’s personal services, supplies or services.</p>
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
<td><h5 id="boccc-combination">BOC/CC Combination</h5></td>
<td><blockquote>
<p>Prosthetics must have a separate credit card for each Budget Object Code/Cost Center (BOC/CC) combination used when ordering through the Prosthetic package.</p>
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
<td><h5 id="cc">CC</h5></td>
<td><blockquote>
<p><strong>Cost Center</strong> – Series of specific numerical digits assigned to a function or organization. The purpose is to classify and accumulate costs applicable to the function or organization.</p>
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
<td><h5 id="fcp">FCP</h5></td>
<td><blockquote>
<p><strong>Fund Control Point</strong> – Division of monies from an appropriation to a specified service, activity or purpose. Each facility distributes their budget allocation into an FCP for Prosthetics.</p>
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
<td><h5 id="hcpc">HCPC</h5></td>
<td><blockquote>
<p><strong>Health Care Procedural Code</strong> – A universal cost coding system created by Medicare. This has been adopted by the VHA as a national mechanism of common identification. The codes are assigned to appliances, devices, medical equipment, supplies and services provided to patients. Each code corresponds to the <strong>Health Care</strong> <strong>Financing Administration</strong> (HCFA) designated 5-digit identifier or the VA-unique 5-digit VA Unique codes</p>
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
<td><h5 id="ifcap">IFCAP</h5></td>
<td><blockquote>
<p><strong>Integrated Funds Distribution, Control Point Activity, Accounting and Procurement</strong>. IFCAP is a system used to report, record, and amend purchase card transactions as well as automation of other activities in Fiscal, AMMS, and other departments.</p>
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
<td><h5 id="nppd">NPPD</h5></td>
<td><blockquote>
<p><strong>National Prosthetic Patient Database</strong> – A compilation of statistical data extracted from each VA medical center’s entries to the Prosthetic package, reflecting both fiscal obligations and completed patient transactions.</p>
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
<td><h5 id="purchase-order">Purchase Order</h5></td>
<td><blockquote>
<p>A government document authorizing the purchase of goods or services within the terms indicated.</p>
</blockquote></td>
</tr>
</tbody>
</table>
Continued on next page
Glossary, Continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchasing-agents">Purchasing Agents</h5></td>
<td><blockquote>
<p>An employee legally empowered to purchase goods and services from commercial vendors.</p>
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
<td><h5 id="transaction">Transaction</h5></td>
<td><blockquote>
<p>Any action with permanent numbering that affects a bill or an account that identifies a request. All transactions are numbered sequentially and may be examined individually. It consists of the Station number, Fiscal Year, Quarter, and Control Point Sequence number.</p>
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
<td><h5 id="type-of-transaction">Type of Transaction</h5></td>
<td><blockquote>
<p>The Type of Transaction prompt includes the following: a first-time issue, a repair of a previous issue, a spare, or a replacement of a stock item:</p>
</blockquote>
<ul>
<li><blockquote>
<blockquote>
<p>Initial = I</p>
</blockquote>
</blockquote></li>
<li><blockquote>
<blockquote>
<p>Repair = X</p>
</blockquote>
</blockquote></li>
<li><blockquote>
<blockquote>
<p>Spare = S</p>
</blockquote>
</blockquote></li>
<li><blockquote>
<blockquote>
<p>Replace = R</p>
</blockquote>
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
<td><h5 id="va-form-10-2319">VA Form<br />
10-2319</h5></td>
<td><blockquote>
<p>Each time a patient receives medical equipment, supplies or services from the Prosthetics Service, the item purchased is recorded on this VA Form 10-2319 (Record of Prosthetics Appliance/Repair). This is an overall list of all appliances/repairs purchased for a veteran.</p>
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
<td><h5 id="vendor">Vendor</h5></td>
<td><blockquote>
<p>The company from which the item is purchased.</p>
</blockquote></td>
</tr>
</tbody>
</table>
