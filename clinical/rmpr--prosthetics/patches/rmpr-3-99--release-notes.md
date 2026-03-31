---
title: RMPR*3*99 Remove IFCAP Item Description from 2319 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Remove IFCAP Item Description from 2319
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*99
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: <span id="_Toc88446104" class="anchor"></span>Remove IFCAP Item Description from 2319 Release Notes
audience: 
keywords: 
  - strong
  - table
  - colgroup
  - style
  - width
  - tbody
  - blockquote
  - description
  - class
  - ifcap
page_count: 0
word_count: 3138
section_count: 0
table_count: 4
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_99rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_99rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

![](rmpr-3-99-remove-ifcap-item-description-from-2319-release-notes/001.png)

ProstheticsRemove IFCAP Item DescriptionFrom 2319Release NotesPatch RMPR\*3\*99

November 2004

V*IST*A Health System Design and Development (HSD&D)

Table of Contents

Remove IFCAP Item Description from 2319 Release Notes [1](#_Toc88446104)

Patch RMPR\*3\*99 Overview [1](#_Toc88446105)

NIF IFCAP Changes in the 2319 (Roll and Scroll) [3](#_Toc88446106)

View Prosthetics Item Transactions (Read Only) [6](#_Toc88446107)

GUI 2319 Button on DOR Menu – Appliance Transactions (Tab 4) [7](#_Toc88446108)

GUI 2319 Button on DOR Menu - Home Oxygen (Tab 8) [9](#_Toc88446109)

Appendix A [11](#_Toc88446110)

Glossary [11](#_Toc88446111)

<span id="_Toc88446104" class="anchor"></span>Remove IFCAP Item Description from 2319 Release Notes

<span id="_Toc88446105" class="anchor"></span>Patch RMPR\*3\*99 Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>Patch <strong>RMPR*3*99 (Remove IFCAP Item Description from 2319)</strong> was developed for Prosthetics to provide an interim solution for the continuation of the National Item File (NIF) data cleansing effort.</p>
<p>On the national level, the IFCAP Item file is pulled from each facility’s database and merged into a VISN database. Then the VISN’s NIF team reviews the Items and edits, deletes and adds descriptions (which are considered to be the “<em>data cleansing</em>” process).</p>
<p>If the IFCAP Item (at the national level) was a Prosthetic Item that was changed, added or deleted, then the Prosthetic Patient Treatment Record (2319) was historically being changed to match the data cleansing changes.</p>
<p>Patch RMPR*3*99 prevents the Prosthetic 2319 from historically being changed when data cleansing happens. This patch protects the <strong>PROSTHETICS ITEM DESCRIPTIONS</strong> in our Prosthetic 2319 from being overridden when the NIF make changes to the <strong>IFCAP DESCRIPTIONS</strong>.</p>
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
<td>Patch RMPR*3*99 changes</td>
<td><blockquote>
<p>Patch RMPR*3*99 affects multiple <strong>Prosthetics Menu</strong> options. All three types of the Prosthetics 2319 have changes including:</p>
<p>1) Roll and Scroll</p>
<p>2) Read Only Roll and Scroll</p>
<p>3) GUI 2319 from the Delayed Order Report (DOR) application.</p>
<p>This patch will change the Prosthetics 2319 <em>Appliance Transactions</em> and <em>Home Oxygen Items</em>, switching the <strong>IFCAP Item Description</strong> to the <strong>HCPCS Description</strong> display.</p>
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
<td>Note to IRM</td>
<td><blockquote>
<p>There is no new .EXE file to install. All the changes are M routines and a new cross reference in File 660. The <strong>IFCAP Item Description</strong> will remain in the database until phase 2 of the NIF implementation.</p>
<p>This is the menu option name that IRM references: <strong>RMPR VIEW 2319 READ ONLY.</strong></p>
<p><strong>Note:</strong> Please read these Release Notes for further information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Patch RMPR\*3\*99 Overview, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>No HCPCS entered prior to 1997</td>
<td><blockquote>
<p>Since HCPCS codes were not used prior to 1997, you will continue to see the <strong>IFCAP Item Description</strong> that was selected at that time. This is considered to be protected data and will not change.</p>
<p>Even though the <strong>Appliance Transaction</strong> <strong>(Screen 4)</strong> column heading displays <strong>HCPCS</strong> (in the Roll and Scroll), the information will continue to display the original <strong>IFCAP Item Description</strong> for those transactions entered prior to 1997.</p>
<p>Even though the GUI version of the <strong>Appliance Transaction (Tab 4)</strong> displays <strong>Item</strong> as the column header, it is actually the <strong>IFCAP Item</strong> for those transactions entered prior to 1997. The column heading was <strong>not</strong> changed to <strong>HCPCS</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc88446106" class="anchor"></span>NIF IFCAP Changes in the 2319 (Roll and Scroll)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>2319 Roll and Scroll changes</td>
<td><blockquote>
<p>Access the <strong>Prosthetics Official’s Menu</strong> option, <strong>Display/Print Patient 2319 (23)</strong> to view the <strong>Appliance Transactions</strong> <strong>(Screen 4)</strong> or <strong>Home Oxygen</strong> <strong>(Screen 8)</strong>. Below are the sample screens for the Roll and Scroll 2319 that were affected by the NIF IFCAP changes.</p>
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
<td>Display/Print Patient 2319 Menu (23)</td>
<td><p>Select Prosthetic Official's Menu Option: <strong>DD &lt;Enter&gt;</strong> Display/Print</p>
<p><strong>23 Display/Print Patient 2319</strong></p>
<p>TI Transaction Inquiry</p>
<p>IP Print All Prosthetic Items</p>
<p>BI Print Prosthetic Billings for MAS</p>
<p>IH Item History</p>
<p>SE Search for Recalled Item</p>
<p>SI Site Parameter Inquiry</p>
<p>VI Vendor Inquiry</p>
<blockquote>
<p>Select Display/Print Option: <strong>23</strong> <strong>&lt;Enter&gt;</strong> Display/Print Patient 2319</p>
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
<td>Select the patient</td>
<td><p>Select PROSTHETIC PATIENT: PROSPATIENT,ONE <strong>&lt;Enter&gt;</strong> LOMA LINDA VAMC 6-10-31</p>
<p>000040707 YES 70% SC VETERAN LL/SD/ MODULE III - GIM PCP:</p>
<p>PROSPROVIDER,ONE CX ADVANCE DIRECTIVE - NO </p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> VIRTUAL CONNECTION Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Current Disability Codes are:</p>
<blockquote>
<p>AO/DIS ALL OTHER S/C S/C</p>
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
<td>Select the Appliance Transactions (Screen 4)</td>
<td><p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p><strong>4 APPLIANCE TRANSACTIONS</strong></p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>4</strong> <strong>&lt;Enter&gt;</strong> APPLIANCE TRANSACTIONS</p>
<blockquote>
<p>HHUU,UXKHUS G SSN: 000-04-0707 DOB: JUN 10,1931 CLAIM# SS</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

NIF IFCAP Changes in the 2319 (Roll and Scroll), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Column</td>
<td><blockquote>
<p>Notice the <strong>HCPCS</strong> column heading below is highlighted. This is the column of data that has been changed with Patch RMPR*3*99 to the <strong>HCPCS Description</strong> from the <strong>IFCAP Item Description</strong> (which was the <strong>Item</strong> column heading).</p>
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
<td><p>New HCPCS Column Title</p>
<p><strong>The <em>Item Description</em> is new!!</strong></p>
<p>=======</p></td>
<td><p><strong><u>Date Qty <mark>HCPCS</mark> Type Vendor Sta Serial Delivery Date Tot Cost</u></strong></p>
<p>1. 05/29/02 1 <strong>AUTO BLOOD</strong> I VENDOR,ONE 605 05/29/02 42.01</p>
<p>2. 07/26/00 1 <strong>VASCULAR G</strong> I VENDOR1,ONE 605 019579 07/26/00 99.19</p>
<p>End of Appliance/Repair records for this veteran!</p>
<p>+=Turned-In *=Historical Data I=Initial X=Repair S=Spare R=Replacement</p>
<p>Enter 1-2 to show full entry, '^' to exit or `return` to continue. <strong>1</strong> <strong>&lt;Enter&gt;</strong></p>
<p>PROSPATIENT,ONE SSN: 000-00-0001 LOMA LINDA VAMC DOB: 99-99 -1931</p>
<p><strong>APPLIANCE/REPAIR LINE ITEM DETAIL</strong> &lt;4-1&gt;</p>
<p>TYPE OF FORM: STOCK ISSUE INITIATOR: PROSPROVIDER,THREE</p>
<p>DATE: MAY 29, 2002</p>
<p>DELIVER TO:</p>
<p>TYPE TRANS: INITIAL ISSUE QTY: 1 SOURCE: COMMERCIAL</p>
<p>VENDOR: PROSVENDOR,ONE</p>
<p>VENDOR PHONE: 800-555-5555</p>
<p>28690 N. Any DRIVE</p>
<p>LAKE FORREST, ILLINOIS 60045</p>
<p>DELIVERY DATE: MAY 29, 2002</p>
<p>TOTAL COST: $42.01 OBL:</p>
<p>REMARKS: <strong><em>[If you type a specific note here,</em> <em>it appears on Screen 4 under the transaction with notes…see below.]</em></strong></p>
<p>DISABILITY SERVED: SC/OP</p>
<p><strong>ITEM DESCRIPTION: BLOOD PRESSURE UNIT DIGITAL</strong></p>
<p>APPLIANCE: BLOOD PRESSURE UNIT DIGITAL</p>
<p>PSAS HCPCS: A4670 AUTO BLOOD PRESSURE MONITOR</p>
<p>ICD-9 Code: 401.9 HYPERTENSION NOS</p>
<p>CPT MODIFIER:</p>
<p>DESCRIPTION: AUTO BLOOD PRESSURE MONITOR</p>
<p>EXTENDED DESCRIPTION:</p>
<p>AUTOMATIC BLOOD PRESSURE MONITOR</p>
<blockquote>
<p>Enter RETURN to continue or '^' to exit:</p>
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
<td>Remarks</td>
<td><blockquote>
<p>If you enter a specific note in the <strong>Remarks</strong> field, it will be easier to locate it to identify it for future Item needs. The note displays on Screen 4 below the transaction.</p>
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
<td>Item Description / Appliance prompt</td>
<td><blockquote>
<p>The <strong>IFCAP</strong> <strong>Item Description</strong> field display above is new. This is the field you should review to determine which <strong>Prosthetic Item</strong> was provided to the patient. You should no longer review the <strong>Appliance</strong> field. When the <strong>Item Description</strong> and the <strong>Appliance</strong> field are identical (as shown above), then the “new note” that is described on the next page will not appear. See next page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

NIF IFCAP Changes in the 2319 (Roll and Scroll), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item Description NEW Note</td>
<td><blockquote>
<p>With Patch RMPR*3*99, whenever an <strong>IFCAP Item Description</strong> has been changed, edited or deleted, you will see a new note under this field as follows:</p>
<p><strong>* See Above for Original Item Description *</strong></p>
<p>Due to the data cleansing, the <strong>Appliance</strong> field (which was the original Item selected) has a new description and the original description is now the <strong>Item Description</strong> field.</p>
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
<td><p>After Patch Install - Item Description with NOTE</p>
<p>=======</p>
<p>=======</p></td>
<td><p>TYPE OF FORM: STOCK ISSUE</p>
<p>INITIATOR: PROSPROVIDER,ONE</p>
<p>DATE: MAY 29, 2002</p>
<p>DELIVER TO:</p>
<p>TYPE TRANS: INITIAL ISSUE QTY: 1 SOURCE: COMMERCIAL</p>
<p>VENDOR: PROSVENDOR,ONE</p>
<p>VENDOR PHONE: 800-555-5555</p>
<p>28690 N. Any DRIVE</p>
<p>LAKE FORREST, ILLINOIS 60045</p>
<p>DELIVERY DATE: MAY 29, 2002</p>
<p>TOTAL COST: $42.01 OBL:</p>
<p>REMARKS:</p>
<p>DISABILITY SERVED: SC/OP</p>
<p><strong>ITEM DESCRIPTION: <em>BLOOD PRESSURE UNIT DIGITAL</em></strong></p>
<p><strong>* See Above For Original Item Description *</strong></p>
<p><strong>APPLIANCE:</strong> <em><strong>BLOOD PRESSURE CUFF DIGITAL</strong></em></p>
<p>PSAS HCPCS: A4670 AUTO BLOOD PRESSURE MONITOR</p>
<p>ICD-9 Code: 401.9 HYPERTENSION NOS</p>
<p>CPT MODIFIER:</p>
<p>DESCRIPTION: AUTO BLOOD PRESSURE MONITOR</p>
<p>EXTENDED DESCRIPTION:</p>
<p>AUTOMATIC BLOOD PRESSURE MONITOR</p>
<blockquote>
<p>Enter RETURN to continue or '^' to exit:</p>
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
<td>Example above</td>
<td><blockquote>
<p>To interpret the example above, the original <strong>Item Description</strong> was “<em>Blood Pressure <strong>Unit</strong> Digital.</em>” Due to data cleansing, the description was changed to “<em>Blood Pressure <strong>Cuff</strong> Digital</em>.”</p>
<p>The <strong>Appliance Field</strong> was changed to the new description: “<em>Blood Pressure <strong>Cuff</strong> Digital</em>” and the original or saved description appears in the new field: <strong>Item Description</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc88446107" class="anchor"></span>View Prosthetics Item Transactions (Read Only)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>“Read Only” patch change</td>
<td><blockquote>
<p>The change with Patch RMPR*3*99 that was previously explained also affects the Roll and Scroll version of Prosthetics and provides the following new (Read only) menu option:</p>
<p><strong>View Prosthetics Item Transactions</strong></p>
<p>Below is a sample screen.</p>
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
<td>View 2319 (Read Only)</td>
<td><p>Select OPTION NAME: <strong>VIEW PROSTHETICS ITEM TRANSACT</strong> <strong>&lt;Enter&gt;</strong> <strong>RMPR VIEW 2319 READ ONLY</strong></p>
<p>View Prosthetics Item Transactions</p>
<p>SITE: SUPPORT ISC// <strong>&lt;Enter&gt;</strong> 578A5</p>
<p>Select PROSTHETIC PATIENT: PROSPATIENT, ONE <strong>&lt;Enter&gt;</strong> SUPPORT ISC 4-5-61 000111111</p>
<p>YES SC VETERAN</p>
<p>PATIENT IS DECEASED. DATE OF DEATH WAS OCT 21,1993@08:00</p>
<p>Would you Like to continue Processing this Patient? NO// YES <strong>&lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p>I ITEM TRANSACTIONS</p>
<p>H HOME OXYGEN ITEMS</p>
<blockquote>
<p>Enter DATA screen to VIEW (Item Transactions or Home Oxygen),'^' to EXIT, or 'return' to continue :</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc88446108" class="anchor"></span>GUI 2319 Button on DOR Menu – Appliance Transactions (Tab 4)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Delayed Order Reports (DOR)</td>
<td><blockquote>
<p>The <strong>GUI 2319 Appliance Transactions</strong> <strong>(Tab 4)</strong> window from the Delayed Order Report (DOR) below shows the heading: <strong>Item</strong> column; however this information is now the <strong>HCPCS Description</strong> with Patch RMPR*3*99.</p>
<p>The column heading <strong>Item</strong> will not be changed to <strong>HCPCS</strong>.</p>
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
<td>Appliance Transactions (Tab 4)</td>
<td><blockquote>
<p>![](rmpr-3-99-remove-ifcap-item-description-from-2319-release-notes/002.png)</p>
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
<td>Next Step</td>
<td><blockquote>
<p>Click the <strong>View Detail</strong> button at the bottom of this window to display the <strong>Appliance Transaction Detail</strong> window and proceed to the next page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

GUI 2319 Button on DOR Menu – Appliance Transactions (Tab 4), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance Field</td>
<td><blockquote>
<p>The <strong>Appliance</strong> field listed in the <strong>Transaction Detail</strong> window below is protected from changes to IFCAP (from the NIF group’s data cleansing).</p>
<p>The example below, “Wheelchair 9000XT 18-inch” in the <strong>Appliance</strong> field will remain the same with Patch RMPR*3*99.</p>
<p><strong>Note:</strong> The <strong>Appliance</strong> field below will always display the originally selected <strong>IFCAP Item Description</strong>. The new “<strong>Item Description</strong>: field in Roll and Scroll and the new note “<em>See Above…</em>” is not necessary in the GUI 2319. This is because the GUI 2319 <strong>IFCAP Item Description</strong> will always be displayed and protected from changes.</p>
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
<td>Transaction Detail window</td>
<td><blockquote>
<p>![](rmpr-3-99-remove-ifcap-item-description-from-2319-release-notes/003.png)</p>
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
<td>Close button</td>
<td><blockquote>
<p>To close the <strong>Transaction Detail</strong> window and return to the <strong>View 2319</strong> window, click the <strong>Close</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc88446109" class="anchor"></span>GUI 2319 Button on DOR Menu - Home Oxygen (Tab 8)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Home Oxygen (Tab 8)</td>
<td><blockquote>
<p>The 2319 in the Delayed Order Report (DOR) shown below of the <strong>Home Oxygen</strong> (Tab 8) window shows the <strong>Item</strong> column which is the <strong>HCPCS Description</strong> with Patch RMPR*3*99.</p>
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
<td>Home Oxygen window</td>
<td><blockquote>
<p>![](rmpr-3-99-remove-ifcap-item-description-from-2319-release-notes/004.png)</p>
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
<td>View Detail button</td>
<td><blockquote>
<p>Click the <strong>View Detail</strong> button at the bottom of this window to display the <strong>Home Oxygen Detail</strong> and proceed to the next page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

GUI 2319 Button on DOR Menu - Home Oxygen (Tab 8), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Home Oxygen (Tab 8) Transaction Detail</td>
<td><blockquote>
<p>Notice the <strong>Appliance</strong> field on the <strong>Transaction Detail</strong> window from the <strong>Home Oxygen (Tab 8)</strong> remains the same, even when changes are made to the NIF IFCAP Item Description.</p>
<p><strong>Note:</strong> The <strong>Appliance</strong> field below will always display the originally selected <strong>IFCAP Item Description</strong>. The new “<strong>Item Description</strong>: field in Roll and Scroll and the new note “<em>See Above…</em>” is not necessary in the GUI 2319. This is because the GUI 2319 <strong>IFCAP Item Description</strong> will always be displayed and protected from changes.</p>
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
<td>Transaction Detail</td>
<td><blockquote>
<p>![](rmpr-3-99-remove-ifcap-item-description-from-2319-release-notes/005.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc88446110" class="anchor"></span>Appendix A

<span id="_Toc88446111" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td>DOR</td>
<td><blockquote>
<p>Delayed Order Report – Prosthetics application.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td>GUI</td>
<td><blockquote>
<p>Graphical User Interface. This is a windows-based application with buttons and tabs instead of prompts in a Roll and Scroll environment for an application. Microsoft Windows is a GUI environment.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HCPCS | Healthcare Common Procedure Coding System – formerly Health Care Financing Administration Common Procedures Coding System - is distributed by Centers for Medicare & Medicaid Services (CMS) and the Health and Human Services (HHS) for all other substances, equipment, supplies, or other items used in Health Care Services. These items include, but are not limited to: medical supplies; orthotic and prosthetic devices; and durable medical equipment. |

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NIF</td>
<td><blockquote>
<p>The National Item File (NIF) database is used to standardize naming practices so that facilities will be able to identify, track and evaluate purchases.</p>
<p>The NIF is also a group that works on this database file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|           |                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VistA | Veterans Health Information Systems and Technology Architecture, formerly known as Decentralized Hospital Computer Program, encompasses the complete information environment at VA medical facilities. It consists of hardware, software packages, and comprehensive support for system-wide and station specific, clinical and administrative automation needs. |