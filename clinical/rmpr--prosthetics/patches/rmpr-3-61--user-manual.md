---
title: RMPR*3*61 Prosthetics Inventory Package (PIP) User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Prosthetics Inventory Package (PIP)
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
menu_options: 3
description: <span id="_Toc461510747" class="anchor"></span>Prosthetics Inventory Package (PIP)
audience: 
keywords: 
  - strong
  - table
  - colgroup
  - width
  - tbody
  - style
  - blockquote
  - class
  - hcpcs
  - report
page_count: 0
word_count: 39810
section_count: 0
table_count: 74
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: March 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_p61_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_p61_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

![](rmpr-3-61-prosthetics-inventory-package-pip-user-manual/001.png)

PROSTHETICSINVENTORY PACKAGE (PIP)USER MANUALPatch RMPR\*3\*61

March 2005

VistA Health System Design and Development (HSD&D)

######## Table of Contents

Prosthetics Inventory Package (PIP) [1](#_Toc461510747)

Overview [1](#_Toc461510748)

Accessing the Inventory Main Menu [3](#_Toc99425770)

Inventory Option Descriptions [4](#_Toc99425771)

Inventory Reports (RP) Menu Option Descriptions [6](#_Toc99425772)

Email Notifications [9](#_Hlt509035655)

Overview [9](#_Toc99425774)

Managing/Viewing Inventory Data [10](#_Toc461510757)

Overview of Prosthetic Inventory Main Menu [10](#_Toc99425776)

Add Inventory LOCATION or ITEMS (AE) [11](#_Toc99425777)

Edit Inventory Items (EI) [18](#_Toc99425778)

Edit Inventory Location (EL) [22](#_Toc99425779)

Deactivate Inventory Location (DE) [24](#_Toc99425780)

Order Item from Supply or Vendor (OI) [26](#_Toc99425781)

Receive Item from Supply, Vendor or Patient (RC) [29](#_Hlt509029087)

Transfer Stock Between Locations (TR) [33](#_Toc99425783)

Reconcile Item Balance (UP) [35](#_Toc99425784)

Remove/Deactivate HCPCS/Item from Inventory (RE) [37](#_Toc440693904)

Inventory Reports Menu … [38](#_Hlt509029118)

Overview [38](#_Hlt509197346)

New Inventory Reports (Patch RMPR\*3\*61) [39](#_Toc99425788)

Overview [39](#_Toc99425789)

Print Order/Receive Item (PO) [41](#_Toc99425790)

Print Item Usage by Location (IU) [43](#_Toc99425791)

Print Stock Work Sheet (WS) [46](#_Toc99425792)

Reprint Barcode Label (BC) [47](#_Toc99425793)

Print Items Not Issued Within 30-Day (P3) [49](#_Toc99425794)

Print Stock on Hand Over Date Range (OD) [50](#_Toc99425795)

Print All Barcode in a Location (AL) [52](#_Toc99425796)

Print PIP/IFCAP Item Report (IP) [53](#_Toc99425797)

Prosthetic Inventory Reports (Patch RMPR\*3\*51) [54](#_Toc99425798)

Overview [54](#_Toc99425799)

Access the Inventory Reports Menu [55](#_Toc501807359)

Field/Column Descriptions [56](#_Toc501807360)

Viewing/Printing Reports [58](#_Hlt501531386)

Item Detail Report (SI) [59](#_Hlt500262678)

Overview [59](#_Toc501807363)

Item Detail Report – Choosing “All HCPCS” [60](#_Toc501807364)

Item Detail Report – Choosing “All HCPCS for NPPD Group” [62](#_Toc501807365)

Item Detail Report – Choosing “All HCPCS for NPPD Line” [65](#_Toc501807366)

Item Detail Report – Choosing “Select Individual HCPCS” [68](#_Toc501807367)

HCPCS Summary Report (SH) [70](#_Hlt500262683)

Overview [70](#_Toc501807369)

HCPCS Summary Report – Choosing “All HCPCS” [71](#_Toc501807370)

HCPCS Summary Report – Choosing “All HCPCS for NPPD Group” [74](#_Toc501807371)

HCPCS Summary Report – Choosing “All HCPCS for NPPD Line” [76](#_Toc501807372)

HCPCS Summary Report – Choosing “Select Individual HCPCS” [79](#_Toc501807373)

NPPD Group/Line Report (SG) [82](#_Hlt500262688)

Overview [82](#_Toc501807375)

NPPD Group/Line Report - Select a Single NPPD Group [83](#_Toc501807376)

NPPD Group/Line Report - Select Multiple NPPD Groups [85](#_Toc501807377)

NPPD Group Summary Report (SS) [87](#_Hlt500262696)

Overview [87](#_Toc501807379)

Viewing the NPPD Group Summary Report [88](#_Toc501807380)

Other Useful Inventory Reports [89](#_Hlt509035833)

Overview [89](#_Toc99425823)

Print Transaction History (PS) [90](#_Toc99425824)

Print Current Item Balance by Location (PL) [92](#_Hlt509035835)

Print Current HCPCS Balance by HCPCS (PI) [93](#_Hlt509035837)

Appendix A [94](#_Toc461510772)

Glossary [94](#_Toc99425828)

Appendix B [95](#_Toc99425829)

Using Prosthetics Help [95](#_Toc99425830)

<span id="_Toc461510747" class="anchor"></span>Prosthetics Inventory Package (PIP)

<span id="_Toc461510748" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Software description</td>
<td><blockquote>
<p>The Prosthetics inventory software (also known as the Prosthetics Inventory Package or “PIP”) tracks quantities of prosthetic items located in the Prosthetics Sensory and AIDS Service (PSAS) inventory of each facility.</p>
<p>The PIP system using bar coding provides the means to do the following:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Manages the inventory data using barcode scanner equipment</p>
</blockquote></li>
<li><blockquote>
<p>Provides for faster data entry with scanning information of labels</p>
</blockquote></li>
<li><blockquote>
<p>More accurate data entry with scanning of HCPCS Codes</p>
</blockquote></li>
<li><blockquote>
<p>Sends a mail message when stock is low</p>
</blockquote></li>
<li><blockquote>
<p>Automatically calculates stock quantities when stock is ordered or issued.</p>
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
<td>Patch RMPR*3*61</td>
<td><blockquote>
<p>Introducing <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Patch RMPR*3*61 which provides a new <strong>Prosthetics</strong> <strong>Inventory Main Menu</strong> and new <strong>Inventory Reports Menu</strong> options. This patch also provides barcode printing and reader functionality.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Introduction to Patch RMPR*3*61 with new functionality.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="warning">WARNING</h5></td>
<td><blockquote>
<p><strong>WARNING:</strong> <u>Do <strong>NOT</strong> install this patch</u> (or any patch) <u>during the first week of the month</u> as this will affect the Prosthetic Inventory Package statistics.</p>
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
<td><h5 id="installation-of-patch-rmpr361">Installation of Patch RMPR*3*61</h5></td>
<td><blockquote>
<p>Patch RMPR*3*61 is a large patch that involves careful setup PRIOR to installation and data conversion.</p>
<p><strong><u>This is extremely important</u>:</strong> Please review this <strong>Prosthetics</strong> <strong>Inventory Package (PIP) User Manual</strong> and all other documents relating to Patch RMPR*3*61 before proceeding with the installation including the following:</p>
</blockquote>
<ul>
<li><p>Forum Patch Module description</p></li>
<li><p>Prosthetics Inventory Package (PIP) Implementation Guide</p></li>
<li><p>Prosthetics Inventory Package (PIP) Lessons Learned</p></li>
<li><p>Prosthetics Purchasing - Stock Issues User Manual.</p></li>
</ul>
<blockquote>
<p>Additionally, the documents: <strong>Inventory User Manual, Stock Issues User Manual</strong> and <strong>Lessons Learned</strong> should be provided to end users with the suggestion that they be reviewed. Several major changes to the software are being introduced with this patch and the smoothness of adapting to these changes is directly related to end users having and reading these documents.</p>
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
<td><h5 id="ordering-receiving-inventory">Ordering/ Receiving Inventory</h5></td>
<td><blockquote>
<p>This patch is NOT for ordering or receiving inventory.</p>
<p>The intention of this patch is to disperse inventory to the 2319. You cannot order an item from IFCAP using the Prosthetics Inventory Package (PIP) using the <strong>Order Item from Supply or Vendor (OI)</strong> option since it is not part of IFCAP. You must use GIP or IFCAP.</p>
<p>The <strong>Order Item from Supply or Vendor</strong> <strong>(OI)</strong> is an option to record an Item that has been ordered. Whenever you place an order, use this option to update the quantity of the stock ordered. This option works in conjunction with the <strong>Receive Item from Supply, Vendor or Patient</strong> <strong>(RC)</strong> option.</p>
<p><strong>Note:</strong> The <strong>Order Item from Supply or Vendor</strong> <strong>(OI)</strong> option is not associated with IFCAP. This option will not automatically order an item from Supply or Vendor.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425770" class="anchor"></span>Accessing the Inventory Main Menu

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu description</td>
<td><blockquote>
<p>The <strong>Pros Inventory Main</strong> <strong>Menu</strong> is found under the <strong>Prosthetic Official's</strong> <strong>Menu</strong> and the <strong>Prosthetic Clerk's</strong> <strong>Menu</strong>. The Prosthetics Inventory software also provides reports on the status of the inventory.</p>
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
<td><h5 id="prosthetics-officials-menu">Prosthetics Official’s Menu</h5></td>
<td><p>PU Purchasing ...</p>
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
<p><strong>INV Pros Inventory Main ...</strong></p>
<p>ND NPPD Tools ...</p>
<p>VR VERIFY/REPAIR PURCHASE CARD NUMBER</p>
<p>Select Prosthetic Official's Menu Option: <strong>INV</strong> Pros Inventory Main</p></td>
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
<td>Pros Inventory Main Menu screen</td>
<td><p>AE Add Inventory LOCATION or ITEMS</p>
<p>EI Edit Inventory Items</p>
<p>EL Edit Inventory Location</p>
<p>DE Deactivate Inventory Location</p>
<p>OI Order Item from Supply or Vendor</p>
<p>RC Receive Item from Supply, Vendor or Patient</p>
<p>TR Transfer Stock Between Locations</p>
<p>UP Reconcile Item Balance</p>
<p>RP Inventory Reports ...</p>
<p>RE Remove/Deactivate HCPCS/Item from Inventory</p>
<p>Select Pros Inventory Main Option:</p></td>
</tr>
</tbody>
</table>

<span id="_Toc99425771" class="anchor"></span>Inventory Option Descriptions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Add Inventory LOCATION or ITEMS (AE)</td>
<td><blockquote>
<p>The <strong>Add Inventory LOCATION or ITEMS</strong> <strong>(AE)</strong> option is used to set-up and maintain Prosthetic locations and inventory items used by the inventory software. All <em><strong><u>new</u></strong></em> locations and inventory items are entered using this option.</p>
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
<td>Edit Inventory Items (EI)</td>
<td><blockquote>
<p>Any changes you need to make to a Prosthetic inventory Item must be made through the <strong>Edit Inventory Items (EI)</strong> option. You can only edit an Item that has already been set-up (entered through the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option).</p>
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
<td>Edit Inventory Location (EL)</td>
<td><blockquote>
<p>Any changes you need to make to the Prosthetic Locations must be made through the <strong>Edit Inventory Location (EL)</strong> option. You can only edit a Location that has already been set-up. You can also edit an existing HCPCS.</p>
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
<td>Deactivate Inventory Location (DE)</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Deactivate</strong> <strong>Inventory Location (DE)</strong> option allows you to deactivate an inventory Location. Deactivating a Location also deactivates <strong><u>all</u></strong> the HCPCS associated with that Location. This option requires the user to own the RMPRMANAGER key.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Option renamed from <strong>Delete Inventory Location</strong> to <strong>Deactivate Inventory Location</strong> with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Order Item from Supply or Vendor (OI)</td>
<td><blockquote>
<p>The <strong>Order Item from Supply or Vendor</strong> <strong>(OI)</strong> is an option to record an Item that has been ordered. Whenever you place an order, use this option to update the quantity of the stock ordered. This option works in conjunction with the <strong>Receive Item from Supply, Vendor or Patient</strong> <strong>(RC)</strong> option.</p>
<p><strong>Note:</strong> This option is not associated with IFCAP. This option will not automatically order an item from Supply or Vendor.</p>
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
<td>Receive Item from Supply, Vendor or Patient (RC)</td>
<td><blockquote>
<p>Whenever you receive ordered items, use the <strong>Receive Item from Supply, Vendor or Patient</strong> <strong>(RC)</strong> option to record and update the quantity of the stock received.</p>
<p>Receiving an item in Supply through the IFCAP package does not update the Prosthetics Inventory module. This option has to be done separately for an item to be received and recorded in the Prosthetics module.</p>
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
<td>Transfer Stock Between Locations (TR)</td>
<td><blockquote>
<p>If you have a quantity of stock in one location that you would like to show (transfer) as being in another location, use the <strong>Transfer Stock Between Locations</strong> <strong>(TR)</strong> option. You can transfer all quantities or certain quantities.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Inventory Option Descriptions, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Reconcile Item Balance (UP)</td>
<td><p>Use the <strong>Reconcile Item Balance</strong> <strong>(UP)</strong> option to reconcile any differences determined in balances between a physical count and the quantity on-hand shown by the system. This option should only be used for existing items and is only used to record quantities.</p>
<blockquote>
<p>Balances can be checked by using the report options:</p>
</blockquote>
<ul>
<li><p>Print Current HCPCS Balance by HCPCS (PI) – or -</p></li>
<li><p>Print Current Item Balance by Location (PL)</p></li>
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
<td><h5 id="remove-deactivate-hcpcsitem-from-inventory-re">Remove/ Deactivate HCPCS/Item from Inventory (RE)</h5></td>
<td><blockquote>
<p>The <strong>Remove/Deactivate HCPCS/Item from Inventory (RE)</strong> option removes/ deactivates inventory item(s) from Prosthetics Inventory Package. Once an item has been removed/deactivated, that item is not accessible.</p>
<p><strong>Note:</strong> Only users with RMPRMANAGER key can access this option.</p>
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
<td>Inventory Reports (RP) Menu</td>
<td><blockquote>
<p>The <strong>Inventory Reports</strong> <strong>(RP)</strong> <strong>Menu</strong> contains reports showing item balances and statistics. The first four usage reports are available for the sites and for PSAS Headquarters personnel to use. Use these reports to assess and manage your inventory.</p>
<p>The <strong>Inventory Reports</strong> <strong>(RP)</strong> <strong>Menu</strong> includes the following report options:</p>
</blockquote>
<ul>
<li><p>Item Detail Report</p></li>
<li><p>HCPCS Summary Report</p></li>
<li><p>NPPD Group/Line Report</p></li>
<li><p>NPPD Group Summary Report</p></li>
<li><p>Print Employee Lab Issue Statistics</p></li>
<li><p>Print Current HCPCS Balance by HCPCS</p></li>
<li><p>Print Current Item Balance by Location</p></li>
<li><p>Print Order/Receive Item</p></li>
<li><p>Print Transaction History</p></li>
<li><p>Print Item Usage By Location</p></li>
<li><p>Print Stock Work Sheet</p></li>
<li><p>Reprint Barcode Label</p></li>
<li><p>Print Item Not Issued Within 30-Day</p></li>
<li><p>Print Stock On Hand Over Date Range</p></li>
<li><p>Print All Barcode in a Location</p></li>
<li><p>Print PIP/IFCAP Item Report</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc99425772" class="anchor"></span>Inventory Reports (RP) Menu Option Descriptions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Inventory Reports</strong> <strong>(RP)</strong> Main Menu has 15 report options as described below.</p>
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
<td>Inventory Reports Menu screen</td>
<td><blockquote>
<p>Select Pros Inventory Main Option: <strong>RP Inventory Reports</strong></p>
<p>SI Item Detail Report</p>
<p>SH HCPCS Summary Report</p>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PE Print Employee Lab Issue Statistics</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>P3 Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
<p>Select Inventory Reports Option:</p>
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
<td>Item Detail Report (SI)</td>
<td><blockquote>
<p>The <strong>Item Detail Report (SI)</strong> is the most detailed report at the facility level. This report displays the stock on hand for a date range and sorted by item at the facility level. Since this report is in the NPPD Report format, all HCPCS in that group are shown on the report, even if there was no activity during the reporting timeframe. For example, K004-1 and K004-3 is shown, but also K004-2 is shown. HCPCS are always grouped under their respective NPPD Line and Group headings.</p>
<p>There are also separate summary lines for USED and NEW Total Values. At the end of the report is a Grand Total New and Used for inventory on-hand as well as items issued.</p>
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
<td>HCPCS Summary Report (SH)</td>
<td><blockquote>
<p>The <strong>HCPCS Summary Report (SH)</strong> is for both local as well as headquarters use. This report provides a quick overview of the total dollars on-hand in Inventory. It displays the stock on-hand for a specified date range, and it is sorted by HCPCS. This report provides a description field in the second column. There is a Grand Total USED and NEW for items issued as well as stock on-hand on this report.</p>
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
<td>NPPD Group/Line Report (SG)</td>
<td><blockquote>
<p>The <strong>NPPD Group/Line Report (SG)</strong> is for local use. This report displays the same information as the <strong>Item Detail Report</strong> but at the NPPD Line level. It displays the stock on hand for a date range and sorted by NPPD Group and NPPD Line. There is a Grand Total USED and NEW for items issued as well as stock on hand on this report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Inventory Reports (RP) Menu Option Descriptions, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NPPD Group Summary Report (SS)</td>
<td><blockquote>
<p>The <strong>NPPD Group Summary Report (SS)</strong> is for local use. This report provides high-level summary information based on the NPPD Group selected. It is the summary of the entire Prosthetics inventory for a certain date range sorted by NPPD Group.</p>
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
<td>Print Current HCPCS Balance by HCPCS (PI)</td>
<td><blockquote>
<p>The <strong>Print Current HCPCS Balance by HCPCS</strong> <strong>(PI)</strong> is a report of the number of items available in current inventory by location for selected HCPCS. It includes other information about the items, including the following:</p>
</blockquote>
<ul>
<li><p>Source (VA or Commercial)</p></li>
<li><p>Vendor</p></li>
<li><p>Unit of issue</p></li>
<li><p>Re-order level</p></li>
<li><p>Average cost.</p></li>
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
<td>Print Current Item Balance by Location (PL)</td>
<td><blockquote>
<p>The <strong>Print Current Item Balance by Location</strong> <strong>(PL)</strong> is a report of item balances by one, more than one, or all prosthetic Locations for a site.</p>
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
<td>Print Transaction History (PS)</td>
<td><blockquote>
<p>The <strong>Print Transaction History</strong> <strong>(PS)</strong> option to print daily Item statistics of all or particular HCPCS and Items that are in Prosthetics Inventory. This option prints the VA form 10-1210. The report shows all the statistics of a particular HCPCS Code, Item, and dollar amount for a certain date range.</p>
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
<td>Print Order/Receive Item (PO)</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Order/Receive Item (PO)</strong> option prints the Open, Received Item(s), or Cancelled Items in the PIP. You will be asked for the number of days back an item was open, received, or cancelled.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print Item Usage by Location (IU)</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Item Usage by Location (IU)</strong> option provides a report of an item usage and quantity for a specified date range. This report is sorted by Location.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

Continued on next page

Inventory Reports (RP) Menu Option Descriptions, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print Stock Work Sheet (WS)</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Stock Work Sheet (WS)</strong> option prints the inventory stock by Location of a particular station. It shows the HCPCS, Item description, date, cost, vendor, quantity, location, and a blank column for the physical count.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Reprint Barcode Label (BC)</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Reprint Barcode Label (BC)</strong> option allows inventory users to print barcode labels. Only HCPCS in PIP can be printed using this option.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-items-not-issued-within-30-day-p3">Print Items Not Issued Within 30-Day (P3)</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Items Not Issued Within 30-Day (P3)</strong> report option prints Items not issued within a 30-day period. Items that have been issued within 30 days will NOT be printed on this report.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print Stock on Hand Over Date Range (OD)</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Stock on Hand Over Date Range (OD)</strong> report prints all Items in a particular Location, where the number of days on-hand is greater than the number of days in the date range selected. Sort criteria are based on Locations and new or old Items.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-all-barcode-in-a-location-al">Print All Barcode in a Location (AL)</h5></td>
<td><blockquote>
<p>With Patch RMPR*3*61, the <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print All Barcode in a Location</strong> <strong>(AL)</strong> option is an option available for use in printing all the barcode labels for all items within a Location.</p>
<p><strong>Note:</strong> This is a helpful option to use after installing this patch into the Production (Live) system to implement this patch.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-pipifcap-item-report-ip">Print PIP/IFCAP Item Report (IP)</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print PIP/IFCAP Item (IP)</strong> report prints all PIP Items and the corresponding IFCAP Items. Prosthetics users must edit the HCPCS/Item that has a blank IFCAP Item. This report is useful for checking if the IFCAP Item is correctly linked to the PIP Item.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<span id="_Hlt509035655" class="anchor"></span>Email Notifications

<span id="_Toc99425774" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>Email notifications are sent when your items have been reduced to the Re-order Level you entered for the item. If you have re-ordered items, and your PIP reflects your Re-order Number, you will still receive an email notification.</p>
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
<td>Task Job (Inventory Task Balance Check)</td>
<td><blockquote>
<p>After installation of the Prosthetic Inventory module, IRM will schedule the <em>Inventory Task Balance Check</em> to run every night.</p>
<p>This option will check all items in each Prosthetics Location and send a Prosthetics Inventory message if the balance is below the Re-order Level for an item.</p>
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
<td>Mail Group (RMPR INVENTORY)</td>
<td><blockquote>
<p>The RMPR INVENTORY mail group receives the <em>Inventory Task Balance Check</em> message whenever the balance for an item is below the re-order level. There must be at least one member, either the Prosthetics Chief or a designated person responsible for the Prosthetics Inventory module.</p>
<p><strong>Note:</strong> Make sure that IRM has a list of the people who should be in this mail group.</p>
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
<td><h5 id="sample-mail-message">Sample mail message</h5></td>
<td><p>Subj: PROSTHETICS INVENTORY MESSAGE [#79931] 12/28/02@06:00 14 lines</p>
<p>From: POSTMASTER In 'IN' basket. Page 1 *New*</p>
<p>------------------------------------------------------------------------------</p>
<p>Run Date: DEC 28, 2002</p>
<p>This is a notification from the Prosthetics Department........</p>
<p>The current balance for the following item(s) is/are below the reorder level:</p>
<p>[Site] [Location] [Item] [HCPCS] [Reorder Lvl] [Bal]</p>
<p>SUPPOR HO 1 EYEGLASSES A4254-3 4 1</p>
<p>SUPPOR HNC ULTRALIGHTWEIGHT WHEELCHAIR K0005-2 5 3</p>
<p> Quantity = 10 has been ordered for item..ULTRALIGHTWEIGHT WHEELCHAIR G</p>
<p>RN on DEC 18, 2002</p>
<blockquote>
<p>ROOM 3 TAIL CLOSURES/COMMERCIAL A4369-1 2 1</p>
<p>Thank You!!!</p>
<p>PROSTHETICS DEPARTMENT</p>
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
<td>Privacy Act</td>
<td><blockquote>
<p>The Privacy Act covers personal data within this package. Access to the software should be restricted to those personnel whose normal duties require viewing and editing such patient-related data as found in the Prosthetics Inventory Package.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc461510757" class="anchor"></span>Managing/Viewing Inventory Data

<span id="_Toc99425776" class="anchor"></span>Overview of Prosthetic Inventory Main Menu

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Pros Inventory Main</strong> <strong>Menu</strong> options are used to manage the Prosthetics Inventory that contains information about Items including the following:</p>
</blockquote>
<ul>
<li><p>Prosthetics Location</p></li>
<li><p>HCPCS Code</p></li>
<li><p>Quantity</p></li>
<li><p>Cost</p></li>
<li><p>Unit of issue</p></li>
<li><p>Vendor</p></li>
<li><p>Re-order level</p></li>
<li><p>Source (VA or Commercial)</p></li>
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
<td>Pros Inventory Main Menu</td>
<td><p>AE Add Inventory LOCATION or ITEMS</p>
<p>EI Edit Inventory Items</p>
<p>EL Edit Inventory Location</p>
<p>DE Deactivate Inventory Location</p>
<p>OI Order Item from Supply or Vendor</p>
<p>RC Receive Item from Supply, Vendor or Patient</p>
<p>TR Transfer Stock Between Locations</p>
<p>UP Reconcile Item Balance</p>
<p>RP Inventory Reports ...</p>
<p>RE Remove/Deactivate HCPCS/Item from Inventory</p>
<p>Select Pros Inventory Main Option:</p></td>
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
<td>Inventory Reports Menu</td>
<td><blockquote>
<p>The reports under the <strong>Inventory Reports</strong> Menu provide statistics and document the status of the inventory. The <strong>Inventory Reports</strong> Menu contains the following options:</p>
</blockquote>
<ul>
<li><p>Item Detail Report</p></li>
<li><p>HCPCS Summary Report</p></li>
<li><p>NPPD Group/Line Report</p></li>
<li><p>NPPD Group Summary Report</p></li>
<li><p>Print Employee Lab Issue Statistics</p></li>
<li><p>Print Current HCPCS Balance by HCPCS</p></li>
<li><p>Print Current Item Balance by Location</p></li>
<li><p>Print Order/Receive Item</p></li>
<li><p>Print Transaction History</p></li>
<li><p>Print Item Usage by Location</p></li>
<li><p>Print Stock Work Sheet</p></li>
<li><p>Reprint Barcode Label</p></li>
<li><p>Print Items Not Issued Within 30-Day</p></li>
<li><p>Print Stock on Hand Over Date Range</p></li>
<li><p>Print All Barcode in a Location</p></li>
<li><p>Print PIP/IFCAP Item Report</p></li>
</ul></td>
</tr>
</tbody>
</table>

  
<span id="_Toc99425777" class="anchor"></span>Add Inventory LOCATION or ITEMS (AE)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You must use the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option to populate the Prosthetics Inventory (PIP) to add a new Location or Item to inventory. (This is a one-time procedure.) You can also add a Prosthetic Location for each site where an inventory Item will be located.</p>
<p><u>You must use this option before you can issue an Item from the <strong>Stock Issues (SI) Menu</strong> if it has not been previously added</u>. You will not be able to receive stock until an Item has been added. The barcode scanner equipment will not work unless the Item(s) has been added to the PIP.</p>
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
<p>To add a PIP Location and/or an IFCAP Item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                   |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                            |
| 1    | Select the Site (if more than one Site can be selected).                                                                                                                                      |
| 2    | Enter a Prosthetics Location and press \<Enter\>. (You can type one or two question marks \<??\> to display a list and select one <u>or add a new one</u> as shown on the next page.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only). Entering a question mark &lt;?&gt; will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
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
<td>Enter Pros Location</td>
<td><blockquote>
<p>The <strong>Enter Pros Location</strong> prompt provides a list of Locations by typing a question mark. You can view the entire <strong>PROS ITEM LOCATION</strong> list to select one or add a new one if you wish.</p>
<p>When entering a new Location, there is a free-text field of 3 - 30 characters in length.</p>
<p>This is a location of an item or stock being tracked for inventory. This might be a room number, warehouse, etc.</p>
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
<td>Sample screen</td>
<td><p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong></p>
<p>Enter Pros Location: <strong>?? &lt;Enter&gt;</strong></p>
<p>Answer with PROS ITEM LOCATION</p>
<p>Choose from:</p>
<p>RADIOLOGY</p>
<p>RMC26</p>
<p>You may enter a new PROS ITEM LOCATION, if you wish</p>
<p>This is a location of an item or stock being tracked for inventory.</p>
<p>Enter Pros Location: <strong>ROOM 19</strong>... <strong>&lt;Enter&gt;</strong></p>
<p>Are you adding 'ROOM 19' as a new PROS ITEM LOCATION? N// <strong>Y &lt;Enter&gt;</strong> (Yes)</p></td>
</tr>
</tbody>
</table>

Continued on next page

Add Inventory LOCATION or ITEMS (AE), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item Location Address</td>
<td><blockquote>
<p>The <strong>Prosthetic Item Location Address</strong> prompt provides an entry for a more detailed description of the Prosthetics Location that you are adding to PIP.</p>
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
<td>Select HCPCS</td>
<td><blockquote>
<p>The <strong>Select HCPCS</strong> prompt allows you to select a HCPCS Code from the current Prosthetic HCPCS list. Entering <strong>&lt;??&gt;</strong> at this prompt brings up the entire list. Select the current HCPCS associated with the item(s) you will be adding.</p>
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
<p>To continue to add a PIP Location and/or an IFCAP Item, follow these steps:</p>
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
<td>3</td>
<td>Enter the <strong>Prosthetic Item Location Address</strong>, and press &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>At the <strong>Select HCPCS</strong> prompt, you can enter the HCPCS Code or type two question marks <strong>&lt;??&gt;</strong> and press <strong>&lt;Enter&gt;</strong>.</p>
<ul>
<li><p>A prompt displays asking if you want the entire 3035-Entry Prosthetics HCPCS list to be viewed with a Y/N prompt.</p></li>
<li><p>You can then select one by entering a HCPCS Code, Short Name, CPT, Synonym or Description.</p></li>
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
<td>Sample Screen</td>
<td><p>PROS ITEM LOCATION ADDRESS<strong>: Basement Floor - West Wing &lt;Enter&gt;</strong></p>
<p>Select HCPCS: <strong>?? &lt;Enter&gt;</strong></p>
<p>Answer with PROSTHETIC HCPCS, or SHORT NAME, or CPT, or SYNONYM, or DESCRIPTION</p>
<p>Do you want the entire 3035-Entry PROSTHETIC HCPCS List? <strong>Y</strong> <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Choose from:</p>
<p>A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p>A4255 GLUCOSE MONITOR PLATFORMS</p>
<p>E0100 CANE ADJUST/FIXED WITH TIP</p>
<p>E0113 CRUTCH UNDERARM EACH WOOD</p>
<p>E1260 WHEELCHAIR LIGHTWT FOOT REST</p>
<p><strong>^ &lt;Enter&gt;</strong></p>
<p>Select HCPCS: <strong>E1260</strong> <strong>&lt;Enter&gt;</strong> WHEELCHAIR LIGHTWT FOOT REST</p></td>
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
<td><h5 id="hcpcs-code">HCPCS Code</h5></td>
<td><blockquote>
<p>For each HCPCS Code, you may enter multiple IFCAP Items and PIP Item Descriptions that is more descriptive for your facility. (See next page for sample PIP Item Descriptions.)</p>
<p><strong>Note</strong>: The list of HCPCS shown above is a portion of the entire list for your Prosthetics Service.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Add Inventory LOCATION or ITEMS (AE), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>IFCAP Item</td>
<td><blockquote>
<p>The <strong>IFCAP Item</strong> prompt allows you to associate or link the IFCAP Item to the local PIP Item Description you are about to add.</p>
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
<td>2 Levels of Item Descriptions</td>
<td><blockquote>
<p>Below are two different Item prompts with different levels of detail:</p>
<p><strong>1. IFCAP Item –</strong> This prompt provides a description from the main list of IFCAP Items in the Prosthetic file (which cannot be changed in Prosthetics):</p>
<p><em><u>Example</u></em>: Diabetic Shoe</p>
<p><strong>2. Inventory Item Description</strong> – Local “PIP” or Inventory Item specific description (which can be changed/replaced in Prosthetics): <em><u>Example</u></em>: Diabetic Shoe – Size 8</p>
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
<p>To continue to add a PIP Location and/or an IFCAP Item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                           |
| 5    | At the IFCAP Item prompt, you may enter a new Item and press \<Enter\>. This is an Item or appliance in the PSAS HCPCS list kept by a local file in PIP. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample screen</td>
<td><blockquote>
<p>IFCAP ITEM: <strong>? &lt;Enter&gt;</strong></p>
<p>Answer with PROS ITEM MASTER NAME</p>
<p>Do you want the entire 18-Entry PROS ITEM MASTER List? <strong>Y</strong> <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Choose from:</p>
<p>3 SYRINGE-SUBCUTANEOUS-3IN  THIS ITEM IS INACTIVE </p>
<p>55 WHEELCHAIR-ADULT/HEMI/BLUE-STD FOR ALL PATIENTS</p>
<p>56 WHEELCHAIR-CLASSIC-18X16</p>
<p>59 EYEGLASSES</p>
<p>99 OXYGEN CONCENTRATOR</p>
<p>100 OXYGEN DEVICE</p>
<p>912 WHEELCHAIR GLOVES</p>
<p>913 SHOE COMPONENTS</p>
<p>921 WHEELCHAIR - ELECTRIC</p>
<p>IFCAP ITEM: <strong>921</strong> &lt;<strong>Enter&gt;</strong> WHEELCHAIR - ELECTRIC</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Inventory Item Description: WHEELCHAIR - ELECTRIC Replace <strong>&lt;Enter&gt;</strong></p>
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
<td>Inventory Item Description</td>
<td><blockquote>
<p>The <strong>Inventory Item Description</strong> is a free-text field of 3 - 50 characters in length. This description for the item is used locally by your Prosthetic service. You may specify size, volume, etc. You can change the description at this prompt and replace it with a new one. For example, the HCPCS Code, A4565 may have the following PIP Item Descriptions:</p>
<p>1 - Sling, arm large</p>
<p>2 - Sling, arm small</p>
<p><strong>Note:</strong> For each HCPCS Code, you may enter multiple IFCAP Items and PIP Item descriptions. Several IFCAP Items may be associated with one HCPCS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Add Inventory LOCATION or ITEMS (AE), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Source</td>
<td><blockquote>
<p>The <strong>Source</strong> prompt is defined as the source for the Item you are defining. Enter either (V)A (for <strong>used</strong> items) or (C)ommercial (for <strong>new</strong> items) at this prompt. Note that new and used Items are tracked separately to maintain inventory records for each Source.</p>
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
<p>To continue to add a PIP Location and/or an IFCAP Item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>Select <strong>V</strong> (VA) or <strong>C</strong> (Commercial) at the <strong>Source</strong> prompt and press <strong>&lt;Enter&gt;</strong>.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Enter a <strong>Re-order Level</strong> number (optional) or exit at this prompt.</td>
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
<td>Screen sample</td>
<td><blockquote>
<p>SOURCE: C// <strong>?? &lt;Enter&gt;</strong></p>
<p>This is the source of an item:</p>
<p>'V' stands for VA or USED items and</p>
<p>'C' for COMMERCIAL or NEW items.</p>
<p>NEW and USED items are tracked separately so that separate inventory records should be maintained for each source.</p>
<p>Choose from:</p>
<p>V VA</p>
<p>C COMMERCIAL</p>
<p>If the item is USED, type in 'V' for VA.</p>
<p>If the item is NEW, type in 'C' for COMMERCIAL.</p>
<p>SOURCE: C// COMMERCIAL <strong>&lt;Enter&gt;</strong></p>
<p>RE-ORDER LEVEL: <strong>5 &lt;Enter&gt;</strong></p>
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
<td><p>Re-Order Level</p>
<p>(Optional)</p></td>
<td><blockquote>
<p>The <strong>Re-Order Level</strong> (optional prompt) is a number that signifies when an Item should be re-ordered. The system uses this number to check against the quantity on-hand and will alert specified users through an email if the quantity on-hand is too low. Items are still accessible through PIP even if you do not enter a Re-order level for an Item.</p>
<p><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong><u>You can also exit at this prompt</u>!</strong> The Item entry process is actually complete, even though no quantity has been assigned. This is because there may not be any Items available in stock at this point.</p>
<p><strong>Note:</strong> If the quantity is below the Re-order level for the Item, a message is sent to alert members of the RMPR INVENTORY mail group. Contact your IRM to be entered as a member of that mail group if you need a notification.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Functionality change with Patch RMPR*3*61 to exit the entry process of an item before entering quantity.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

Continued on next page

Add Inventory LOCATION or ITEMS (AE), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Invoice Quantity</td>
<td><blockquote>
<p>The <strong>Invoice Quantity</strong> prompt provides the entry of the quantity of the IFCAP Item that you are adding at a specific Location for a specific vendor. (This is not the same as the quantity on-hand for an Item.)</p>
<p><strong>Note:</strong> To enter a receipt of an existing IFCAP Item, use the <strong>Receive Item from Supply, Vendor or Patient (RC)</strong> option. To update/correct the quantities on-hand for an IFCAP Item, use the <strong>Reconcile Item Balance (UP)</strong> option.</p>
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
<p>To continue to add a PIP Location and/or an IFCAP Item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                         |
|------|-----------------------------------------------------------------------------------------|
| Step | Action                                                                                  |
| 8    | Enter the Invoice Quantity and press \<Enter\>.                                 |
| 9    | Enter the Unit Cost or type a zero and press \<Enter\>.                         |
| 10   | The Total Cost of Quantity prompt displays with the total automatically calculated. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample screen</td>
<td><blockquote>
<p>INVOICE QUANTITY: <strong>?? &lt;Enter&gt;</strong></p>
<p>Type the item quantity you are receiving into stock. This quantity should match that on the paper record of the receipt such as an invoice or delivery note. It is not the same as the quantity on hand. To correct on hand quantities, you should use the Reconciliation option.</p>
<p>Please make sure you create separate receipts if you are receiving the same item from different vendors or at different costs.</p>
<p>INVOICE QUANTITY: <strong>10 &lt;Enter&gt;</strong></p>
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
<td>Unit Cost</td>
<td><blockquote>
<p>The <strong>Unit Cost</strong> prompt is the cost of each unit being added. If you do not have the information to enter in this prompt, you can enter a Zero (0).</p>
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
<td>Sample screen</td>
<td><blockquote>
<p>UNIT COST: <strong>?? &lt;Enter&gt;</strong></p>
<p>Type in the dollar cost per item.</p>
<p>If you would prefer to enter the total dollar value for the item quantity you have just typed in, then type in 0 here.</p>
<p>UNIT COST: <strong>75 &lt;Enter&gt;</strong></p>
<p>TOTAL COST OF QUANTITY: 750.00</p>
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
<td>Total Cost of Quantity</td>
<td><blockquote>
<p>The <strong>Total Cost of Quantity</strong> prompt automatically displays the total dollar value for the item you are requesting to order. (This is the Invoice Quantity multiplied by the Unit Cost.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Add Inventory LOCATION or ITEMS (AE), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Vendor</td>
<td><blockquote>
<p>The <strong>Vendor</strong> prompt specifies the vendor from whom the Item is procured. You can also select a vendor for the IFCAP Item from a list.</p>
<p>This list includes the Vendor name, phone number, FMS (Financial Management System) Vendor Code or Dun &amp; Bradstreet Synonym as well as other details (i.e., city, state, ZIP code and fax number if applicable).</p>
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
<td><h5 id="unit-of-issue">Unit of Issue</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Unit of Issue</strong> prompt provides a list by entering a question mark. This list is from IFCAP. This defines the Item and how it is received as a pair, in a box, etc.</p>
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
<td>Steps (continued)</td>
<td><blockquote>
<p>To continue to add a PIP Location and/or an IFCAP Item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                             |
|------|-----------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                      |
| 11   | Select a Vendor and press \<Enter\>. You can type a question mark \<?\> to display a list and select one.       |
| 12   | Enter a Unit of Issue and press \<Enter\>. You can type a question mark \<?\> to display a list and select one. |
| 13   | A confirmation prompt displays stating that inventory has been updated.                                                     |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample screen</td>
<td><blockquote>
<p>VENDOR: <strong>?</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Answer with VENDOR NUMBER, or NAME, or DUN &amp; BRADSTREET #, or</p>
<p>FMS VENDOR CODE, or SYNONYM</p>
<p>Do you want the entire VENDOR List? <strong>N</strong> <strong>&lt;Enter&gt;</strong> (No)</p>
<p>VENDOR: <strong>ABBOTT</strong> <strong>&lt;Enter&gt;</strong> LABORATORIES ABBOTT LABORATORIES PH:800 255-5162 NO: 3</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ABBOTT PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Unit of Issue: each <strong>&lt;Enter&gt;</strong> EA EACH</p>
<p> Inventory updated.</p>
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
<td>Confirmation note</td>
<td><blockquote>
<p>When you complete the entry process, a confirmation appears that Inventory has been updated.</p>
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
<td>Number of Labels to Print</td>
<td><blockquote>
<p>A default number will display for you to print at the <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Number of Labels to Print</strong> prompt. You can press <strong>&lt;Enter&gt;</strong> to select the default number or enter a number that is less than the default.</p>
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
<td>Steps (continued)</td>
<td><blockquote>
<p>To continue to add a PIP Location and/or an IFCAP Item, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                              |
| 14   | Press \<Enter\> at the Number of Labels to print or enter a number less than the default number shown.                                      |
| 15   | Press \<Enter\> at the Select Barcode Printer if it is set to the default for your barcode scanner equipment.                               |
| 16   | You can press \<Enter\> at the Do you want your output QUEUED? to accept the default of No, and the barcode label will print automatically. |
| 17   | You can then select another HCPCS to add another Location or Item, if necessary and continue the same process again.                                |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-prompts">New Prompts:</h5></td>
<td><blockquote>
<p>Number of Labels to print: 10// <strong>&lt;Enter&gt;</strong></p>
<p>Select Barcode Printer: ZEBRA PROSTHETIC// <strong>&lt;Enter&gt;</strong> ZEBRA PROSTHETIC PRINTER</p>
<p>Do you want your output QUEUED? No// <strong>&lt;Enter&gt;</strong></p>
<p>Select HCPCS: <strong>&lt;Enter&gt;</strong></p>
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
<td><h5 id="select-barcode-printer">Select Barcode Printer</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Select Barcode Printer</strong> prompt will display a default printer for the barcode scanner equipment.</p>
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
<td><h5 id="do-you-want-your-output-queued"><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Do you want your output QUEUED?</h5></td>
<td><blockquote>
<p>If you want your barcode label to print automatically, you would <strong>NOT</strong> want to QUEUE your output to the printer. It may take awhile for it to be printed depending on other print jobs sent to the printer before your label request.</p>
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

<span id="_Toc99425778" class="anchor"></span>Edit Inventory Items (EI)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>The <strong>Edit Inventory Item (EI)</strong> option is used to make any changes to the PIP Item description, inventory location, re-order level, invoice quantities of the Item(s), unit cost, or vendor. You can edit an Item when there are multiple Items for a HCPCS Code.</p>
<p>If you edit the PIP Item description, you will be prompted to associate a current stock record to the Item. The PIP Item(s) was entered through the <strong>Receive Item from Supply, Vendor or Patient (RC)</strong> option.</p>
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
<p>To edit inventory Item information, follow these steps:</p>
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
<td>1</td>
<td>Select the <strong>Site</strong> (if more than one site can be selected).</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Select the <strong>HCPCS Code</strong> of the PIP Item you want to edit. You can type two question marks <strong>&lt;??&gt;</strong> to display a list and select one.</td>
</tr>
<tr class="even">
<td>3</td>
<td><p>You can now edit any of the prompts that display from the HCPCS Code to the Vendor.</p>
<p><strong>Note:</strong> If you edit the <strong>PIP Item Description</strong>, then you will need to select a current stock record. (See next page.)</p></td>
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
<td>Sample screen</td>
<td><blockquote>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Editing Inventory Items.....</p>
<p>Select HCPCS: <strong>A4254</strong> <strong>&lt;Enter&gt;</strong> BATTERY FOR GLUCOSE MONITOR</p>
<p>is associated with more than 1 item, please select one...</p>
<p>IFCAP Item: BATTERY DEVICE</p>
<p>1 A4254-1 C BATTERY FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>IFCAP Item: BATTERY DEVICE</p>
<p>2 A4254-2 C BAT FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>IFCAP Item: BATTERY DEVICE</p>
<p>3 A4254-3 C BAT FOR GLU MON/COMM</p>
<p>Choose 1 - 3 : <strong>1 &lt;Enter&gt;</strong></p>
<p>HCPCS: A4254 BATTERY FOR GLUCOSE MONITOR <strong>&lt;Enter&gt;</strong></p>
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
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only). Entering a question mark <strong>&lt;?&gt;</strong> will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
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
<td>Select HCPCS</td>
<td><blockquote>
<p>This is the HCPCS from the Prosthetic HCPCS list for this Location. Entering two question marks<strong>&lt;??&gt;</strong> at this prompt displays the entire list. Select a HCPCS to edit.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Edit Inventory Items (EI), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>IFCAP Item</td>
<td><blockquote>
<p>The <strong>IFCAP Item</strong> must be associated with the HCPCS that you entered. Entering two question marks <strong>&lt;??&gt;</strong> at this prompt displays the entire list.</p>
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
<td>PIP Item Description</td>
<td><blockquote>
<p>The <strong>PIP Item Description</strong> prompt is a prompt that is used at your local facility. (This is a free-text entry.)</p>
<p>One example of a PIP Item Description change is “Wheelchair Gloves” can be changed to “W/C Gloves.” You can also specify size and volume in the description.</p>
<p><strong>Note:</strong> When you make a change, notice that you are then prompted to select a current stock record. This will associate or link the item with the information that was entered through the <strong>Receive Item from Supply, Vendor or Patient (RC)</strong> option. A list of stock record(s) may display, and you can select one from the list.</p>
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
<p>To continue to edit inventory Item information, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                            |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                     |
| 4    | Enter the IFCAP Item and press \<Enter\>.                                                                                                                          |
| 5    | You can change the PIP Item Description and press \<Enter\>.                                                                                                       |
| 6    | If there is more than one stock record to associate, you will be presented with a list to select one. The linking is done at the Select a current stock record prompt. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Sample screen</p>
<p>Linking done here</p></td>
<td><blockquote>
<p>IFCAP ITEM: BATTERY DEVICE// <strong>&lt;Enter&gt;</strong> 15171 BATTERY DEVICE</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>PIP Item Description: BATTERY MONITOR DEVICE // <strong>?? &lt;Enter&gt;</strong></p>
<p>Enter a description for this item that will be used locally by your Prosthetics Service. You may want to use a description with additional text specifying things like size, volume, etc.</p>
<p>PIP Item Description: BATTERY MONITOR DEVICE // <strong>BAT MON DEV &lt;Enter&gt;</strong></p>
<p>Are you sure you want to change this Item's Description? N// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> YES</p>
<p>Select a current stock record...</p>
<p>Date Quantity Value Vendor Location</p>
<p>1 SEP 04, 2001 20 500.00 ABBOTT LABORATORIES Room 18</p>
<p>2 SEP 04, 2001 15 375.00 ABBOTT LABORATORIES Room 18</p>
<p>Choose 1 - 2: <strong>1</strong> <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Edit Inventory Items (EI), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Enter Pros Location</td>
<td><blockquote>
<p>You can modify the existing Prosthetic Location name at the <strong>Enter Pros Location</strong> prompt. This is a free-text field of 3 – 30 characters. (You can press &lt;<strong>Enter</strong>&gt; to bypass the prompt.) This is a Location of an Item or stock being tracked for inventory. It can be a room number, warehouse, etc.</p>
<p><strong>Note:</strong> You cannot add a new Location through this option. You must use the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option for a new Location.</p>
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
<td>Re-Order Level</td>
<td><blockquote>
<p>The <strong>Re-Order Level</strong> is the number that signifies when to re-order an item.</p>
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
<td>Invoice Quantity</td>
<td><blockquote>
<p>The <strong>Invoice Quantity</strong> is the amount of the Item associated with the transaction that you have on hand for a Location. You can edit this prompt.</p>
<p><strong>Note:</strong> You can change the quantity amount of an invoice/stock worksheet/packing slip, etc. at this prompt; you are <strong>not</strong> entering Items received. Use the <strong>Receive Item from Supply, Vendor or Patient (RC)</strong> option to enter Items received into Inventory.</p>
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
<td>Unit Cost</td>
<td><blockquote>
<p>The <strong>Unit Cost</strong> prompt is the cost of one Item. The <strong>Total Cost of Quantity</strong> prompt automatically displays the Invoice Quantity multiplied by the Unit Cost.</p>
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
<p>To continue to edit inventory Item information, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                    |
|------|--------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                             |
| 7    | You can edit the Prosthetic Location at the Enter Pros Location prompt or press \<Enter\> to bypass it.    |
| 8    | You can edit the Reorder Level number.                                                                         |
| 9    | You can edit the Invoice Quantity and/or the Unit Cost. (This will change the Total Cost of Quantity.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample screen</td>
<td><blockquote>
<p>Enter Pros Location: Room 18// <strong>&lt;Enter&gt;</strong></p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> YES</p>
<p>RE-ORDER LEVEL<strong>:</strong> 2// <strong>4</strong> <strong>&lt;Enter&gt;</strong></p>
<p>INVOICE QUANTITY: 10// <strong>20</strong> <strong>&lt;Enter&gt;</strong></p>
<p>UNIT COST: 25// <strong>&lt;Enter&gt;</strong></p>
<p>TOTAL COST OF QUANTITY: 500.00</p>
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
<td>Vendor</td>
<td><blockquote>
<p>This is the specific <strong>Vendor(s)</strong> from whom the Item was procured. You can also select a vendor for the Item from a list.</p>
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
<td><h5 id="unit-of-issue-1">Unit of Issue</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Unit of Issue</strong> prompt provides a list by entering a question mark. This list is from IFCAP. This defines the Item and how it is received as a pair, in a box, etc.</p>
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
<td>Steps</td>
<td><blockquote>
<p>To continue to edit inventory Item information, follow these steps:</p>
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
<td>10</td>
<td>You can edit the <strong>Vendor</strong>.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>You can edit the <strong>Unit of Issue</strong>. You can type a question mark <strong>&lt;?&gt;</strong> to display a list and select one.</td>
</tr>
<tr class="even">
<td>12</td>
<td><p>A confirmation displays.</p>
<p><strong>Note:</strong> The Invoice Quantity amount increased as shown in parenthesis before the Location in the sample screen below. (See arrow.)</p></td>
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
<td><h5 id="sample-screen">Sample screen</h5></td>
<td><blockquote>
<p>VENDOR: ABBOTT LABORATORIES// <strong>&lt;Enter&gt;</strong> ABBOTT LABORATORIES PH:800 255-5162 NO: 3</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ABBOTT PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>UNIT OF ISSUE: Ea <strong>&lt;Enter&gt;</strong> EACH</p>
<p> Item A4254-1 was Edited by PROSUSER,one: <strong>(+10)</strong> @ Location Room 18</p>
<p>Editing Inventory Items.....</p>
<p>Select HCPCS: A4254// <strong>^ &lt;Enter&gt;</strong></p>
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
<td>Confirmation</td>
<td><blockquote>
<p>A confirmation note includes the HCPCS Code for the Item that was edited, the name of the person who performed the edit, and the Location.</p>
<p>You can then select another Item to be edited using the same HCPCS or a new HCPCS. You can also exit the system at the <strong>Select HCPCS</strong> prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425779" class="anchor"></span>Edit Inventory Location (EL)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><p>The <strong>Edit Inventory Location (EL)</strong> option is used to make any necessary corrections to a Location name.</p>
<blockquote>
<p><strong>Note:</strong> You cannot add a new Location through this option. You must use the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option for new Locations.</p>
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
<p>To edit an inventory Location, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                       |
|------|-----------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                |
| 1    | Select the Site (if more than one site can be selected).                                                          |
| 2    | Enter a Prosthetics Location. You can type one or two question marks \<??\> to display a list and select one. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample screen</td>
<td><p>Select Pros Inventory Main Option: <strong>EL</strong> <strong>&lt;Enter&gt;</strong> Edit Inventory Location</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Editing an Inventory Location.....</p>
<p>Enter Pros Location: <strong>? &lt;Enter&gt;</strong></p>
<p>Answer with PROS ITEM LOCATION</p>
<p>Do you want the entire PROS ITEM LOCATION List? <strong>Y</strong> <strong>&lt;Enter&gt;</strong> YES</p>
<p>1 HO 1</p>
<p>2 A LOC</p>
<p>3 GENERIC</p>
<p>4 HNC</p>
<p>5 HO 1</p>
<p>6 JLOC</p>
<p><strong>7 Room 18</strong></p>
<p>CHOOSE 1-7: <strong>7 &lt;Enter&gt;</strong> Room 18</p></td>
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
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only). Entering a question mark &lt;?&gt; will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
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
<td>Enter Pros Location</td>
<td><blockquote>
<p>The <strong>Enter Pros Location</strong> prompt is a free-text field of 3 - 30 characters. Enter the name of an existing Prosthetics Location you want to edit. This might be a room number, warehouse, etc. You can type a question mark &lt;?&gt; to view a list and select one.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Edit Inventory Location (EL), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Location</td>
<td><blockquote>
<p>You will now have an opportunity to modify the Location name at the <strong>Location</strong> prompt. (If you do not need to do so, press &lt;<strong>Enter&gt;</strong> to bypass the prompt.)</p>
<p>This is a Location of an item or stock being tracked for inventory. If you do modify the Location name, a verification prompt appears to confirm your response.</p>
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
<p>To continue to edit an inventory Location, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                   |
| 3    | At the Location prompt, you can change the name of the Location and press \<Enter\> or press \<Enter\> to bypass the change. |
| 4    | A confirmation prompt displays asking if you are sure you want to change the name of the Location.                                       |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Screen sample</td>
<td><p>LOCATION: Room 18// <strong>Room 19</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Are you sure you want to change the name of this location? N// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> YES</p>
<p>Location has been edited from 'Room 18' to 'Room 19' !!!</p></td>
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
<td>Confirmation</td>
<td><blockquote>
<p>A confirmation note includes the name of the Location before it was edited and the name of the new Location.</p>
</blockquote></td>
</tr>
</tbody>
</table>

  
<span id="_Toc99425780" class="anchor"></span>Deactivate Inventory Location (DE)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>The <strong>Deactivate Inventory Location (DE)</strong> option prevents you from issuing an item from a Location that is no longer to be used.</p>
<p><strong>WARNING:</strong> <strong>Deactivating a Location deactivates <u>ALL the HCPCS</u> associated with that Location!!!</strong> Deactivating a Location is recommended when you enter a Location in error or the Location is not in use.</p>
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
<p>To deactivate an inventory Location, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                       |
| 1    | Select the Site (if more than one site can be selected).                                                                                                                                                 |
| 2    | Select the Location you want to deactivate at the Enter Pros Location prompt. You can also enter a single question mark \<?\> at this prompt to get a list of all possible Locations and select one. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Screen sample</td>
<td><blockquote>
<p>Select Pros Inventory Main Option: <strong>DE</strong> <strong>&lt;Enter&gt;</strong> Deactivate Inventory Location</p>
<p>SITE: VAMC// <strong>&lt;Enter&gt;</strong> 500</p>
<p>Deactivate an Inventory Location.....</p>
<p>This option now requires the electronic signatures of 2 users holding the RMPRMANAGER key to be entered before a location will be deactivated.</p>
<p>Enter Pros Location: <strong>? &lt;Enter&gt;</strong></p>
<p>Answer with PROS ITEM LOCATION</p>
<p>Do you want the entire PROS ITEM LOCATION List? <strong>Y</strong> <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Choose from:</p>
<p>LEFT WING; BACK HALL</p>
<p>RD TEST</p>
<p>ROOM 3</p>
<p>Enter Pros Location: <strong>Room 3</strong> <strong>&lt;Enter&gt;</strong></p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>The above location contains 1 types of items, with a total quantity of 1 and cost of $50.</p>
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
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only). Entering a question mark <strong>&lt;?&gt;</strong> will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
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
<td>Enter Pros Location</td>
<td><blockquote>
<p>The <strong>Enter Pros Location</strong> prompt is a free-text field of 3 - 30 characters. Enter the name of an existing Prosthetics Location you want to edit. This might be a room number, warehouse, etc. You can type a question mark <strong>&lt;?&gt;</strong> to view a list and select one.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Deactivate Inventory Location (DE), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>2 Electronic Signatures!!!</td>
<td><blockquote>
<p><strong>This option is only given to the holder of the RMPRMANAGER key.</strong> This option requires the electronic signatures of <u>two (2) users</u> holding the RMPRMANAGER key to be entered before a Location will be deactivated.</p>
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
<p>To continue to deactivate an inventory Location, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                    |
|------|--------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                             |
| 3    | The 2<sup>nd</sup> manager (encrypted) must enter their user name for the signature code, and press \<Enter\>. |
| 4    | Enter your Current Signature Code (encrypted) and press \<Enter\>.                                         |
| 5    | Type Y for Yes at the confirmation prompt to finalize the deactivation.                                        |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Screen sample</td>
<td><blockquote>
<p>Please ask another user with the RMPRMANAGER key to enter their user name and electronic signature.</p>
<p>Enter user name of 2nd manager: <strong>xxxxxxxxxxxxx</strong> <strong>&lt;Enter</strong>&gt;</p>
<p>Enter your Current Signature Code: <strong>xxxxxxxxxxx</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Are you sure you want to DEACTIVATE this LOCATION (Y/N) ? N// <strong>Y &lt;Enter&gt;</strong> YES</p>
<p>Location is deactivated</p>
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
<td>Signature Code</td>
<td><blockquote>
<p>The <strong>Enter your Current Signature Code</strong> prompt…allows you to enter an encrypted electronic signature and press the <strong>&lt;Enter&gt;</strong> key.</p>
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
<td>Second manager name</td>
<td><blockquote>
<p>The <strong>Enter user name of 2<sup>nd</sup> Manager</strong> prompt…allows you to enter a second encrypted electronic signature of a manager, and press the <strong>&lt;Enter&gt;</strong> key.</p>
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
<td><h5 id="confirmation">Confirmation</h5></td>
<td><blockquote>
<p>A confirmation prompt displays allowing you to cancel at this point or continue the deactivation of the Location.</p>
</blockquote></td>
</tr>
</tbody>
</table>

  
<span id="_Toc99425781" class="anchor"></span>Order Item from Supply or Vendor (OI)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>Whenever you order supplies, you should update the inventory by using the <strong>Order Item from Supply or Vendor (OI)</strong> option to show the quantity ordered. This function <u>tracks</u> purchase orders that are complete. <u>It does not actually place an order</u>. This option shows the items on order (from phone orders, faxed orders, etc.).</p>
<p>During the background job at night, if items are low (lower than the assigned Re-order level), you will receive an email notice of the stock on hand.</p>
<p><strong>Note:</strong> You can view the Items on a report from the <strong>Print Order/Receive Item (PO)</strong> Report.</p>
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
<td><h5 id="status-of-an-ordertracking-status">Status of an order/Tracking status</h5></td>
<td><blockquote>
<p>The following are the statuses when tracking an order:</p>
</blockquote>
<ul>
<li><p>Open - The order stays open until all quantity ordered has been received.</p></li>
<li><p>Received – The purchase order is complete.</p></li>
<li><p>Canceled</p></li>
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
<td>Steps</td>
<td><blockquote>
<p>To track an Item from Supply or Vendor, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                              |
|------|--------------------------------------------------------------|
| Step | Action                                                       |
| 1    | Select the Site (if more than one site can be selected). |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample screen</td>
<td><blockquote>
<p>Select Pros Inventory Main Option: <strong>OI</strong> <strong>&lt;Enter&gt;</strong> Order Item from Supply or Vendor</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Ordering ITEM from Supply or Vendor....</p>
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
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only). Entering a question mark &lt;?&gt; will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Order Item from Supply or Vendor (OI), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select HCPCS to Order</td>
<td><blockquote>
<p>This is the HCPCS Code that you ordered – a HCPCS that currently exists. Notice that the HCPCS list also shows the PIP Item Description and a more detailed HCPCS/Item number as shown below.</p>
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
<td>Enter Vendor</td>
<td><blockquote>
<p>Select a vendor that you used for this order. You can also select a vendor for the Item from a list. This list includes the Vendor name, phone number, FMS (Financial Management System) Vendor Code or Dun &amp; Bradstreet Synonym as well as other details (i.e., city, state, ZIP code and fax number if applicable).</p>
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
<p>To continue to track an Item from Supply or Vendor, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                           |
|------|---------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                    |
| 2    | Select the HCPCS to Order. Enter a single question mark \<?\> at this prompt to get a list of all possible HCPCS. |
| 3    | Select a Vendor from a list by typing two question marks \<??\>.                                                  |
| 4    | Enter a number in the Quantity to Order prompt.                                                                       |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample screen</td>
<td><blockquote>
<p>Select HCPCS to ORDER: <strong>? &lt;Enter&gt;</strong></p>
<p>Answer with PROSTHETICS HCPCS ITEM MASTER FILE, or NUMBER, or</p>
<p>DESCRIPTION, or STATION, or PSAS ITEM</p>
<p>Do you want the entire PROSTHETICS HCPCS ITEM MASTER FILE List? <strong>Y &lt;Enter&gt;</strong> (Yes)</p>
<p>Choose from:</p>
<p>1 A5506 A5506-1 DIABETIC SHOE - SZ 8</p>
<p>2 A5506 A5506-2 DIABETIC SHOE - SZ 9</p>
<p>3 K0001 K0001-1 WHEELCHAIR – MANUAL</p>
<p>Select HCPCS to ORDER: <strong>1</strong> <strong>&lt;Enter&gt;</strong> (1 YES) A5506 A5506-1 DIABETIC SHOE - SZ 8</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Enter Vendor: <strong>Abbott</strong> <strong>&lt;Enter&gt;</strong> LABORATORIES ABBOTT LABORATORIES PH:800 255-5162NO: 3 ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ABBOTT PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Quantity to Order: <strong>10 &lt;Enter&gt;</strong></p>
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
<td>Quantity to Order</td>
<td><blockquote>
<p>This is the amount (a number between 0 and 99999) that signifies the quantity you are ordering.</p>
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
<td>Enter Comment</td>
<td><blockquote>
<p>The <strong>Enter Comment</strong> prompt provides a free-text field that can be used for comments or any description of an item being ordered. Enter a short comment between 3-50 characters in length, if you need one.</p>
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
<p>To continue to track an Item from Supply or Vendor, follow these steps:</p>
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
<td>5</td>
<td>Type a comment in the <strong>Enter Comment</strong> prompt and press <strong>&lt;Enter&gt;</strong>.</td>
</tr>
<tr class="odd">
<td>6</td>
<td><p>A confirmation prompt displays that the item was ordered.</p>
<p><strong>Note:</strong> This function does not actually place the order; it is a tracking mechanism only.</p></td>
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
<p>Enter Comment: Ordered items from Vendor, Abbott &lt;Enter&gt;</p>
<p>* Item was ordered....</p>
<p>Select HCPCS to ORDER<strong>:^ &lt;Enter&gt;</strong></p>
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
<td>Confirmation Prompt</td>
<td><blockquote>
<p>A confirmation prompt displays stating the following: * <strong>Item was ordered…</strong>.</p>
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
<td><h5 id="select-hcpcs-to-order">Select HCPCS to Order</h5></td>
<td><blockquote>
<p>The <strong>Select HCPCS to Order</strong> prompt displays for you to enter another HCPCS or exit at this prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Hlt509029087" class="anchor"></span>Receive Item from Supply, Vendor or Patient (RC)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function descriptions</td>
<td><blockquote>
<p>Whenever you receive supplies, you should update the inventory using the <strong>Receive Item from Supply, Vendor or Patient (RC)</strong> option to show the quantity received. You can receive supplies from a different supply area, from a vendor, or Items returned from a patient. Barcode scanner equipment is used with this option.</p>
<p><strong>Note</strong>: All Items will need a HCPCS code and location before creating the barcode label. The barcode scanner will not work unless the Items are in PIP.</p>
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
<p>To receive an Item from Supply, Vendor or Patient, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                              |
|------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                       |
| 1    | Select the Site (if more than one site can be selected).                                                                                 |
| 2    | The Select HCPCS prompt is provided to receive the Item(s). (If there is more than one Item, a list will display for you to select one.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample screen</td>
<td><p>Select Pros Inventory Main Option: <strong>RC &lt;Enter&gt;</strong> Receive Item from Supply, Vendor or Patient</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Receive an Item from Supply, Vendor or Veteran.</p>
<p>Select HCPCS:<strong>A4254</strong> <strong>&lt;Enter&gt;</strong> BATTERY FOR GLUCOSE MONITOR</p>
<p>HCPCS: A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p><strong>is associated with more than 1 item, please select one...</strong></p></td>
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
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only).</p>
<p>Entering a question mark &lt;?&gt; will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
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
<td>Select HCPCS</td>
<td><blockquote>
<p>This is the HCPCS of the item(s) received. There may be multiple Items for a HCPCS Code that you enter. If so, a list will display for you to select one.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Receive Item from Supply, Vendor or Patient (RC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>IFCAP Item</td>
<td><blockquote>
<p>Choose an Item from the <strong>IFCAP Item</strong> list. When you do, the following displays:</p>
</blockquote>
<ul>
<li><p>HCPCS</p></li>
<li><p>IFCAP Item</p></li>
<li><p>PIP Item Description.</p></li>
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
<td>Invoice Quantity</td>
<td><blockquote>
<p>The <strong>Invoice Quantity</strong> prompt is the amount (a number between 0 and 99999) received.</p>
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
<p>To continue to receive an Item from Supply, Vendor or Patient, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Step | Action                                                                                            |
| 3    | Select the IFCAP Item that was received. If more than one displays, select one from the list. |
| 4    | Enter the Invoice Quantity to be received.                                                    |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Sample Screen</p>
<p>The following displays:</p></td>
<td><p>IFCAP Item: BATTERY DEVICE</p>
<p>1 A4254-1 C BATTERY FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>IFCAP Item: BATTERY DEVICE</p>
<p>2 A4254-2 C BAT FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>IFCAP Item: BATTERY DEVICE</p>
<p>3 A4254-3 C BAT FOR GLU MON/COMM</p>
<p>Choose 1 - 3 : 1 &lt;Enter&gt;</p>
<p>HCPCS: A4254 BATTERY FOR GLUCOSE MONITOR <strong>&lt;Enter&gt;</strong></p>
<p>HCPCS: A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p>IFCAP Item: BATTERY</p>
<p>PIP Item Description: BATTERY-Glucometer-6 Volt</p>
<p>INVOICE QUANTITY: <strong>29</strong> <strong>&lt;Enter&gt;</strong></p>
<p>UNIT COST: <strong>45 &lt;Enter&gt;</strong></p></td>
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
<td>Unit Cost</td>
<td><blockquote>
<p>The <strong>Unit Cost</strong> prompt is the cost of one unit (a number between 0 and 99999) of the quantity received.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Receive Item from Supply, Vendor or Patient (RC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="total-cost">Total Cost</h5></td>
<td><blockquote>
<p>The <strong>Total Cost of the Quantity</strong> is calculated and displays automatically.</p>
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
<p>This is the <strong>Vendor</strong> that is supplying the stock. If the vendor is not the same as on the original order (shown on the packing slip), you can change the vendor.</p>
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
<p>To continue to receive an Item from Supply, Vendor or Patient, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                        |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                 |
| 5    | Enter the Unit Cost of an Item. You can also press \<Enter\> to bypass this prompt.                                                                                            |
| 6    | The Total Cost of the Item displays. You can press \<Enter\> to accept the default cost. If you bypassed the Unit Cost prompt, you can enter the total dollar amount here. |
| 7    | Enter the Vendor. (You can change the Vendor from the original order at this prompt if necessary.)                                                                                 |
| 8    | Enter the Unit of Issue and press \<Enter\>.                                                                                                                                   |
| 9    | Enter the Prosthetic Location and the item has been received.                                                                                                                      |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Screen sample</td>
<td><p>TOTAL COST OF QUANTITY: 1305.00 <strong>&lt;Enter&gt;</strong></p>
<p>VENDOR: <strong>Abbott Laboratories</strong> <strong>&lt;Enter&gt;</strong> ABBOTT LABORATORIES PH:800 255-5162 NO: 3</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ABBOTT PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>The entered Vendor is not the same as on the original order</p>
<p>Do you want to change the Vendor on the order? <strong>Y &lt;Enter&gt;</strong> YES</p>
<p>UNIT OF ISSUE: ea <strong>&lt;Enter&gt;</strong> EACH</p>
<p>Enter Pros Location: <strong>C-26</strong> <strong>&lt;Enter&gt;</strong></p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> YES</p>
<p> Item has been received and inventory updated. If you are using barcoding you should now print labels for the items received.</p></td>
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
<td><h5 id="unit-of-issue-2"><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Unit of Issue</h5></td>
<td><blockquote>
<p>This is the way an item is packaged or set up with a separate cost.</p>
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
<td>Enter Pros Location</td>
<td><blockquote>
<p>At the <strong>Enter Pros Location</strong> prompt, select the Location where the inventory is received. (If you cannot find the Location you want, and you are a multi-site facility, you may have selected the wrong site.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Receive Item from Supply, Vendor or Patient (RC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Number of Labels to print</td>
<td><blockquote>
<p>The <strong>Number of Labels to print</strong> prompt displays. It is recommended that you should print the barcode labels <strong>NOW</strong>. This prompt assumes you want to print the number of the invoice quantity received. <u>You can print fewer labels but not more than the default setting</u>. The default number of labels appears according to the number you entered into the <strong>Invoice Quantity</strong> prompt.</p>
<p>The following information prints on the barcode label: HCPCS Item, the unit cost, the date when received into inventory, the local description of the item and the vendor.</p>
<p><strong>Note:</strong> There is a backup option that allows you to print a single barcode label at a later time using the <strong>Print Barcode Label (PB)</strong> option. <u>Use for backup purposes</u>.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New functionality with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To continue to receive an Item from Supply, Vendor or Patient, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                              |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                                       |
| 10   | At the Number of Labels to print prompt, you can press \<Enter\> to accept the default setting. Or type in the number (less than the default) of barcode labels you want to print for the Item selected.             |
| 12   | At the Select Barcode Printer prompt, press \<Enter\> to accept the default setting.                                                                                                                                 |
| 13   | Press \<Enter\> at the Do you want your output QUEUED? to accept the default of No, and the barcode label will print automatically. <u>If you answer Yes, you will then enter a Start Time</u>. (See below.) |
| 14   | Press \<Enter\> to accept the default Start Time for the current day/time.                                                                                                                                               |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample Screen</td>
<td><blockquote>
<p>Number of Labels to print: 29// &lt;<strong>Enter</strong>&gt;</p>
<p>Select Barcode Printer: ZEBRA PROSTHETIC// <strong>&lt;Enter</strong>&gt;</p>
</blockquote>
<p>Do you want your output QUEUED? No// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> YES</p>
<p>Requested Start Time: NOW// <strong>&lt;Enter&gt;</strong> (MAY 14, 2002@11:37:26)</p>
<p>REQUEST QUEUED!</p>
<p>Receive an Item from Supply, Vendor or Veteran.</p>
<p>Select HCPCS: <strong>^ &lt;Enter&gt;</strong></p></td>
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
<td>Select Barcode Printer</td>
<td><blockquote>
<p>You can press <strong>&lt;Enter&gt;</strong> to accept the default setting or select your Barcode Printer device from a list by typing two question marks <strong>&lt;??&gt;</strong> and pressing <strong>&lt;Enter&gt;</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

  
<span id="_Toc99425783" class="anchor"></span>Transfer Stock Between Locations (TR)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>If you transfer stock from one Location to another, you can update the inventory using the <strong>Transfer Stock Between Locations (TR)</strong> option. This option allows you to transfer stock from one Location to another without deactivating and re-adding PIP Items.</p>
<p><strong>Note:</strong> To <em><u>deactivate</u></em> items in a location, use the <strong>Deactivate Inventory Location (DE)</strong> option. This option does not remove an Item from a Location if all quantities have been transferred.</p>
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
<p>To transfer an Item from a Location, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                               |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                        |
| 1    | Select the Site (if more than one site can be selected).                                                                                  |
| 2    | The Select HCPCS prompt is provided to transfer the Item(s). (If there is more than one Item, a list will display for you to select one.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample Screen</td>
<td><blockquote>
<p>Select Pros Inventory Main Option: <strong>TR</strong> &lt;<strong>Enter&gt;</strong> Transfer Stock Between Locations</p>
<p>SITE: Hines Development System// &lt;<strong>Enter&gt;</strong> 499</p>
<p>Transfer item quantity to another location.</p>
<p>Select HCPCS: BA158 &lt;<strong>Enter&gt;</strong> EYE DROP GUIDE</p>
<p>HCPCS: BA158 EYE DROP GUIDE</p>
<p>IFCAP Item: EYEGLASSES</p>
<p>PIP Item Description: EYEGLASSES FRAME DELUXE</p>
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
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only).</p>
<p>Entering a question mark &lt;?&gt; will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
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
<td>Select HCPCS</td>
<td><blockquote>
<p>This is the HCPCS Code of the Item that was transferred. After you select one, the HCPCS, IFCAP Item and PIP Item Description displays (as shown in the shaded area above).</p>
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
<td>Select a Current Stock Record</td>
<td><blockquote>
<p>The <strong>Select a current stock record</strong> prompt allows you to identify the HCPCS you are transferring.</p>
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
<td>Enter Quantity to Transfer</td>
<td><blockquote>
<p>This is the amount (a number between 0 and 99999) of the Item that was transferred.</p>
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
<p>To continue to transfer an Item from a Location, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                                                 |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                                                          |
| 3    | At the Select a current stock record prompt, a list of order dates will display with the quantity, Unit Cost, Value, Vendor and Location. Select one and press \<Enter\> to link the Item to transfer with the Location of the Item(s). |
| 4    | Enter the Quantity to transfer of the Item in the specific Location.                                                                                                                                                                            |
| 5    | Enter the Receiving Location of the Item(s) you are transferring.                                                                                                                                                                               |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-1">Screen sample</h5></td>
<td><blockquote>
<p>Select a current stock record...</p>
<p>Date Qty Unit Cost Value Vendor Location</p>
<p>1 05/01/02 20 50.00 1000.00 ABBOTT LABORATORIES C-26</p>
<p>2 05/01/02 5 50.00 250.00 ABBOTT LABORATORIES C-26</p>
<p>Choose 1 - 2 : <strong>1</strong> &lt;<strong>Enter&gt;</strong></p>
<p>Enter Quantity to transfer: <strong>2</strong> &lt;<strong>Enter&gt;</strong></p>
<p>Enter Receiving Location: <strong>D-14</strong> &lt;<strong>Enter&gt;</strong></p>
<p>...OK? Yes// &lt;<strong>Enter&gt;</strong> YES</p>
<p>QTY 2 transferred from C-26 to D-14</p>
<p>Transfer item quantity to another location.</p>
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
<td>Enter Receiving Location</td>
<td><blockquote>
<p>This is the Location where the stock has been transferred. If you cannot enter the Location at this prompt, check to see if the Location receiving the stock has that stock Item assigned to it.</p>
<p><strong>Note:</strong> If you enter the receiving Location and it is the same as the forwarding Location, you will see the following note:</p>
<p>* Forwarding and Receiving Location is the same!!!!</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425784" class="anchor"></span>Reconcile Item Balance (UP)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>Use the <strong>Reconcile Item Balance</strong> <strong>(UP)</strong> option when your reports (<strong>Print Current Balance by Location</strong> or <strong>Print Current HCPCS Balance by HCPCS</strong>) show an item balance different from the actual physical count for a Location.</p>
<p>This option also allows you to update other Item-specific information. <strong>To use this <u>option, you must own the RMPRMANAGER key</u>.</strong></p>
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
<p>To reconcile an item balance, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Step | Action                                                                                   |
| 1    | Select the Site (if more than one Site can be selected).                             |
| 2    | At the Select HCPCS prompt, select the HCPCS Code that needs to be balanced/updated. |
| 3    | Select an IFCAP Item if a HCPCS is associated with more than one item.                   |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Screen sample</td>
<td><p>Select Pros Inventory Main Option: <strong>UP</strong> <strong>&lt;Enter&gt;</strong> Reconcile Item Balance</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Reconcile Inventory item quantities on hand...</p>
<p>Select HCPCS: <strong>A4254</strong> <strong>&lt;Enter&gt;</strong> Battery for glucose monitor A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p>HCPCS: A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p>is associated with more than 1 item, please select one<strong>... &lt;Enter&gt;</strong></p>
<p>IFCAP Item: BATTERY DEVICE</p>
<p>1 A4254-1 C BATTERY FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>IFCAP Item: BATTERY DEVICE</p>
<p>2 A4254-2 C BAT FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>IFCAP Item: BATTERY DEVICE</p>
<p>3 A4254-3 C BAT FOR GLU MON/COMM</p>
<p>Choose 1 - 3 : 1 &lt;Enter&gt;</p></td>
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
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only). Entering a question mark &lt;?&gt; will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
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
<td>Select HCPCS</td>
<td><blockquote>
<p>This is the <strong>HCPCS Code</strong> that needs to be balanced/updated.</p>
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
<td>IFCAP Item</td>
<td><blockquote>
<p>Select an Item from the <strong>IFCAP Item</strong> list if a HCPCS is associated with more than one item. This is the Item that needs to be balanced/updated.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reconcile Item Balance (UP), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Enter Pros Location</td>
<td><p>Select a <strong>Location</strong> from the list of Locations for the site.</p>
<blockquote>
<p><strong>Note:</strong> If you cannot find the Location you want, and you are a multi-site facility, you may have selected the wrong site.</p>
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
<p>To continue to reconcile an item balance, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                      |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                               |
| 4    | At the Enter Pros Location prompt, enter the Location of the item you want to reconcile or enter two question marks \<??\> to display a list and select one. |
| 5    | Select a Vendor for the Item that you are reconciling.                                                                                                           |
| 6    | Enter the amount of the Invoice Quantity that you are reconciling for the Item.                                                                                  |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Sample Screen</p>
<p>Reconciles at the <strong>Invoice Quantity</strong> prompt:</p></td>
<td><p><mark>HCPCS: A4254 BATTERY FOR GLUCOSE MONITOR</mark></p>
<p><mark>IFCAP Item: BATTERY</mark></p>
<p><mark>PIP Item desc.: BATTERY FOR GLUCOSE MONITOR/COMMERCIAL</mark></p>
<p>Enter Pros Location: <strong>JLOC</strong> <strong>&lt;Enter&gt;</strong> &lt;Enter&gt;</p>
<p>VENDOR: <strong>ABBOTT</strong> <strong>&lt;Enter&gt;</strong> LABORATORIES ABBOTT LABORATORIES PH:800 255-5162 NO: 3 ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ABBOTT PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>INVOICE QUANTITY: 20// <strong>25</strong> <strong>&lt;Enter&gt;</strong></p>
<p>* Item was reconciled...</p>
<p>Reconcile Inventory item quantities on hand...</p>
<p>Select HCPCS: <strong>^ &lt;Enter&gt;</strong></p></td>
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
<p>This is the Vendor associated with the Item that you are reconciling.</p>
<p><strong>WARNING:</strong> If you have a situation where more than one Vendor supplies the same Item(s), you should perform a separate reconcile count for each Vendor!</p>
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
<td>Invoice Quantity</td>
<td><blockquote>
<p>Enter the correct quantity, a number between 0 and 99999, for the Item that you are reconciling. When the level of stock for an Item reaches zero quantity on hand, the Item is removed automatically. To remove an Item, you can enter a ZERO, which removes the Item from the PIP inventory.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc440693904" class="anchor"></span>Remove/Deactivate HCPCS/Item from Inventory (RE)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can remove or deactivate an inventory Item from PIP through the <strong>Remove/ Deactivate HCPCS/Item from Inventory (RE)</strong>. Once an Item has been removed/deactivated, that Item is no longer accessible.</p>
<p><strong>Note:</strong> Only users with the RMPRMANAGER key can access this option.</p>
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
<p>To remove an Item from PIP, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                               |
|------|-------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                        |
| 1    | Select the Site (if more than one site can be selected).                                                                  |
| 2    | Select the HCPCS that you want to remove. You can type one or two question marks \<??\> to display a list and select one. |
| 3    | At the prompt, Do you want to Remove/Deactivate ALL Items for this HCPCS? N//, type Y for Yes.                        |
| 4    | At the prompt, Are you sure you want to Remove/Deactivate ALL ITEMs for HCPCS XXXXX? N//, type Y for Yes.             |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-screen-1">Sample screen</h5></td>
<td><blockquote>
<p>AE Add Inventory LOCATION or ITEMS</p>
<p>EI Edit Inventory Items</p>
<p>EL Edit Inventory Location</p>
<p>DE Deactivate Inventory Location</p>
<p>OI Order Item from Supply or Vendor</p>
<p>RC Receive Item from Supply, Vendor or Patient</p>
<p>TR Transfer Stock Between Locations</p>
<p>UP Reconcile Item Balance</p>
<p>RP Inventory Reports ...</p>
<p>RE Remove/Deactivate HCPCS/Item from Inventory</p>
<p>Select Pros Inventory Main Option: <strong>RE</strong> <strong>&lt;Enter&gt;</strong> Remove/Deactivate HCPCS/Item from Inventory</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>* Removing/Deactivating HCPCS......</p>
<p>Select HCPCS: <strong>BA150</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Do you want to Remove/Deactivate ALL Items for this HCPCS? N// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> YES</p>
<p>Are you sure you want to Remove/Deactivate ALL ITEMs for HCPCS BA150? N// <strong>Y</strong> <strong>&lt;Enter&gt;</strong> YES</p>
<p>* HCPCS/ITEM BA150-1 has been Removed/Deactivated from PIP...</p>
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
<td><h5 id="confirmation-1">Confirmation</h5></td>
<td><blockquote>
<p>You have two confirmation prompts where you can continue the removal/ deactivation or cancel the process and exit the option.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Hlt509029118" class="anchor"></span>Inventory Reports Menu …<span id="_Hlt509197346" class="anchor"></span>

Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>Use the <strong>Inventory Reports</strong> Menu options to help you to review what you have in your Prosthetics Inventory. The next few sections are as follows:</p>
<p><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><u>New Inventory Reports</u> (from Patch RMPR*3*61)</p>
</blockquote>
<ul>
<li><p>Print Order/Receive Item</p></li>
<li><p>Print Item Usage by Location</p></li>
<li><p>Print Stock Work Sheet</p></li>
<li><p>Reprint Barcode Label</p></li>
<li><p>Print Items Not Issued Within 30-Day</p></li>
<li><p>Print Stock on Hand Over Date Range</p></li>
<li><p>Print All Barcode in a Location</p></li>
<li><p>Print PIP/IFCAP Item Report</p></li>
</ul>
<blockquote>
<p><u>Prosthetic Inventory Reports</u> (from a previous patch, Patch RMPR*3*51):</p>
</blockquote>
<ul>
<li><p>Item Detail Report</p></li>
<li><p>HCPCS Summary Report</p></li>
<li><p>NPPD Group/Line Report</p></li>
<li><p>NPPD Group Summary Report</p></li>
</ul>
<blockquote>
<p>Other Useful Inventory Reports:</p>
</blockquote>
<ul>
<li><p>Print Current HCPCS Balance by HCPCS (format revised)</p></li>
<li><p>Print Current Item Balance by Location (format revised)</p></li>
<li><p>Print Transaction History</p></li>
</ul></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Inventory Reports with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<span id="_Toc99425788" class="anchor"></span>[^1]New Inventory Reports (Patch RMPR\*3\*61)

<span id="_Toc99425789" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>There are eight new <strong>Inventory Report Menu</strong> options with Patch RMPR*3*61 as follows:</p>
</blockquote>
<ul>
<li><p>Print Order/Receive Item (PO)</p></li>
<li><p>Print Item Usage by Location (IU)</p></li>
<li><p>Print Stock Work Sheet (WS)</p></li>
<li><p>Reprint Barcode Label (BC)</p></li>
<li><p>Print Items Not Issued Within 30-Day (P3)</p></li>
<li><p>Print Stock on Hand Over Date Range (OD)</p></li>
<li><p>Print All Barcode in a Location (AL)</p></li>
<li><p>Print PIP/IFCAP Item Report (IP)</p></li>
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
<td>Reports Menu</td>
<td><blockquote>
<p>SI Item Detail Report</p>
<p>SH HCPCS Summary Report</p>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>P3 Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
<p>Select Inventory Reports Option:</p>
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
<td>Print Order/Receive Item (PO)</td>
<td><blockquote>
<p>The <strong>Print Order/Receive Item (PO)</strong> report is a new report with Patch RMPR*3*61. This option prints Open, Received item(s) or Cancelled in the Prosthetics Inventory Package (PIP). You will be asked for the number of days back an item was ordered, received or cancelled for this report.</p>
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
<td>Print Item Usage by Location (IU)</td>
<td><blockquote>
<p>The <strong>Print Item Usage by Location (IU)</strong> report provides an item usage and quantity on-hand report for a specified date range and sorted by location.</p>
</blockquote></td>
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
<td>Print Stock Worksheet (WS)</td>
<td><blockquote>
<p>This report prints the inventory stock by Location of a particular station. It shows the HCPCS, Item description, date, cost, vendor, quantity, Location and a blank column for the physical count.</p>
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
<td>Reprint Barcode Label (BC)</td>
<td><blockquote>
<p>This option allows inventory users to print barcode labels. Only HCPCS in PIP can be printed using this option.</p>
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
<td><h5 id="print-items-not-issued-within-30-day-p3-1">Print Items Not Issued Within 30-Day (P3)</h5></td>
<td><blockquote>
<p>The <strong>Print Items Not Issued Within 30-Day (P3)</strong> report option prints Items not issued within a 30-day period. Items have been issued within 30 days will NOT be printed on this report.</p>
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
<td>Print Stock on Hand Over Date Range (OD)</td>
<td><blockquote>
<p>This report prints all Items in a particular Location, where the number of days on-hand is greater than the number of days in the date range selected. Sort criteria are based on Locations and new or old Items.</p>
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
<td><h5 id="print-all-barcode-in-a-location-al-1">Print All Barcode in a Location (AL)</h5></td>
<td><blockquote>
<p>With Patch RMPR*3*61, the <strong>Print All Barcode in a Location</strong> <strong>(AL)</strong> option is an option available for use in printing all the barcode labels for all items within a Location. This is a helpful option to use after installing this patch into the Production (Live) system during the implementation of this patch.</p>
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
<td><h5 id="print-pipifcap-item-report-ip-1">Print PIP/IFCAP Item Report (IP)</h5></td>
<td><blockquote>
<p>The <strong>Print PIP/IFCAP Item (IP)</strong> report prints all PIP Items and the corresponding IFCAP Items. Prosthetics users must edit the HCPCS/Item that has a blank IFCAP Item. This report is useful for checking if the IFCAP Item is correctly linked to the PIP Item.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425790" class="anchor"></span>Print Order/Receive Item (PO)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Order/Receive Item (PO)</strong> Report is a new report with Patch RMPR*3*61. This option prints Open, Received Item(s), or Canceled in the Prosthetics Inventory Package (PIP). You will be asked for the number of days back an Item was open, received, or canceled for this report.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select number of days old</td>
<td><blockquote>
<p>You can select the number of days tracking backwards that you want the report to print data in timeframes as follows:</p>
</blockquote>
<ul>
<li><p>30 Days Old</p></li>
<li><p>60 Days Old</p></li>
<li><p>90 Days Old</p></li>
<li><p>Over 90 Days Old</p></li>
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
<td>Sample screen</td>
<td><p>Select Inventory Reports Option: <strong>PO</strong> <strong>&lt;Enter&gt;</strong> Print Order/Receive Item</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select one of the following:</p>
<p><strong>1 30 Days Old</strong></p>
<p>2 60 Days Old</p>
<p>3 90 Days Old</p>
<p>4 Over 90 Days Old</p>
<p>Select number of days old: 30 Days Old// <strong>1 &lt;Enter&gt;</strong> 30 Days Old</p>
<p>Select one of the following:</p>
<p><strong>O OPEN</strong></p>
<p>R RECIEVED</p>
<p>C CANCEL</p>
<p>Select Category of report: OPEN// <strong>O</strong> <strong>&lt;Enter&gt;</strong> OPEN</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Processing report.....</p></td>
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
<td>Category of Report</td>
<td><blockquote>
<p>You can select the report to print one of the following categories:</p>
</blockquote>
<ul>
<li><p>Open</p></li>
<li><p>Received</p></li>
<li><p>Canceled</p></li>
</ul></td>
</tr>
</tbody>
</table>

Continued on next page

Print Order/Receive Item (PO), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report for Ordered Items</td>
<td><p>* PIP ORDER AND RECEIVE ITEM REPORT * for 30 days old, <strong>OPEN order</strong></p>
<p>Station: SUPPORT ISC Run Date: JUN 28, 2001 PAGE: 1</p>
<p>------------------------------------------------------------------------------</p>
<p><strong>DATE</strong> DATE <strong>QTY</strong> QTY</p>
<p>HCPCS ITEM VENDOR <strong>ORDERED</strong> RECIEVED <strong>ORDERED</strong> RECIEVED</p>
<p>----- ---- ------ ------- -------- ------- --------</p>
<p>A4367-1 Ostomy belt holder ABBOTT LABO 06/28/01 15</p>
<p>Comment: Entered a new item for HCPCS Code A4367</p>
<p>A4404-1 OSTOMY RING EACH/COM ABBOTT LABO 06/21/01 1</p>
<p>BA100-1 READING MACHINE/COMM INLANDER 06/25/01 4</p>
<p>E0142-1 WALKER RIGID WHEELED INLANDER BR 06/25/01 5</p>
<p>Comment: 6/22/01 ordered</p>
<p>E0601-1 CONT AIRWAY PRESSURE ABBOTT LABO 06/21/01 1</p>
<p>K0082-1 22 NF BATTERY CASE ABBOTT LABO 06/25/01 25</p>
<p>Comment: ORDERING BATTERY CASES AT HINES</p>
<p>L5050-4 123 ABBOTT LABO 06/21/01 10</p>
<p>------------------------------------------------------------------------------</p>
<p>&lt;End of Report&gt;</p></td>
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
<td>Received Data</td>
<td><blockquote>
<p>Below is the report with Received as the selection criteria. Above is a report with Open as the selection criteria (indicated by the <strong>Date Ordered</strong> column).</p>
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
<td>Select Received Category</td>
<td><p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select one of the following:</p>
<p>1 30 Days Old or Less</p>
<p>2 60 Days Old or Less</p>
<p>3 90 Days Old or Less</p>
<p><strong>4 Over 90 Days Old or Less</strong></p>
<p>Select number of days old: 30 Days Old or Less// <strong>4 &lt;Enter&gt;</strong> Over 90 Days Old or Less</p>
<p>Select one of the following:</p>
<p>O OPEN</p>
<p><strong>R RECIEVED</strong></p>
<p>C CANCEL</p>
<p>Select Category of report: OPEN// <strong>R &lt;Enter&gt;</strong> RECEIVED</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p></td>
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
<td>Report for Received Items</td>
<td><p>* PIP ORDER AND RECEIVE ITEM REPORT * for OVER 90 days old or Less, <strong>RECIEVED</strong> <strong>order</strong></p>
<p>Station: SUPPORT ISC Run Date: JAN 31, 2002 PAGE: 1</p>
<p>------------------------------------------------------------------------------</p>
<p>DATE <strong>DATE</strong> QTY <strong>QTY</strong></p>
<p>HCPCS ITEM VENDOR ORDERED <strong>RECIEVED</strong> ORDERED <strong>RECIEVED</strong></p>
<p>----- ---- ------ ------- -------- ------- --------</p>
<p>A4254-1 BATTERY FOR GLUCOSE ABB 10/23/01 29</p>
<p>A4565-18 WHEELCHAIR - ELECTRI ABBOTT LABO 01/30/02 10</p>
<p>A4565-18 WHEELCHAIR - ELECTRI ABBOTT LABO 01/30/02 20</p>
<p>E0196-1 GEL PRESSURE MATTRES ABBOTT LABO 10/02/01 20</p>
<p>K0004-4 W/C LW - ALUMINUM SUNRISE MED 09/19/01 6</p>
<p>K0005-1 ULTRALIGHTWEIGHT WHE SUNRISE MED 09/18/01 6</p>
<p>K0005-2 ULTRALIGHTWEIGHT WHE SUNRISE MED 09/18/01 6</p>
<p>------------------------------------------------------------------------------</p>
<p>&lt;End of Report&gt;</p></td>
</tr>
</tbody>
</table>

<span id="_Toc99425791" class="anchor"></span>Print Item Usage by Location (IU)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Item Usage by Location (IU)</strong> report provides an item usage and quantity on hand report for a specified date range sorted by Location.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Locations</td>
<td><blockquote>
<p>You can enter a specific Location or “<strong>ALL</strong>” Locations to print the data in the report.</p>
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
<td>Source Criteria</td>
<td><blockquote>
<p>You can enter one of the two Source Criteria items as follows:</p>
</blockquote>
<ul>
<li><p>Old Items (V)A</p></li>
<li><p>New Items (C)ommercial</p></li>
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
<td>Sample screen</td>
<td><p>Select Inventory Reports Option: <strong>IS</strong> <strong>&lt;Enter&gt;</strong> Print Item Usage By Location</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Enter 'ALL' for all Locations or 'RETURN' to select individual Locations: <strong>ALL &lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p><strong>V OLD Items</strong></p>
<p>C NEW Items</p>
<p>Enter a SOURCE Criteria: NEW Items// <strong>V</strong> <strong>&lt;Enter&gt;</strong> OLD Items</p>
<p>Beginning Date: T-30//<strong>T-90</strong> <strong>&lt;Enter&gt;</strong> (MAR 30, 2001)</p>
<p>Ending Date: TODAY//<strong>T</strong> <strong>&lt;Enter&gt;</strong> (JUN 28, 2001)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Processing report.....</p></td>
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
<td>Date Ranges</td>
<td><blockquote>
<p>You can enter a Beginning Date and an Ending Date range for your report. The default date range for the report is 30 days, but you can change the range to any specific date or date range.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Print Item Usage by Location (IU), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report parameters</td>
<td><blockquote>
<p>Below is a sample <strong>Print Item Usage by Location (IU)</strong> report selecting <strong>V</strong> for VA for Old Items (or USED items) to display.</p>
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
<td>Sample Report – Old Items (V)</td>
<td><p>* DETAIL ITEM USAGE BY LOCATION * <strong>for USED Items</strong></p>
<p>Station: MILWAUKEE, WI Run Date: JUL 2,2001@13:21:53 PAGE: 1</p>
<p>APR 03, 2001 to JUL 02, 2001 [ 91 calendar days ]</p>
<p>------------------------------------------------------------------------------</p>
<p>Location: B-5</p>
<p>QTY $ DAYS AVE <strong>DAYS</strong> STOCK TOTAL $</p>
<p>HCPCS ITEM ISSUE VALUE USAGE RATE <strong>ON-HAND</strong> ON-HAND VAL ON-HND</p>
<p>----- ---- ----- ----- ---------- ------- ------- ----------</p>
<p>A4670-4 VAS-DIGITAL B 0.00 0.000 21 0.00</p>
<p>B9004-2 VAS INFUSION 1 750.00 0.011 455.0 5 3,750.00</p>
<p>DL101-3 VAS DRESSING 0.00 0.000 3 5.40</p>
<p>DL103-4 VAS REACHER 1 6.20 0.011 182.0 2 12.40</p>
<p>DL104-4 VAS SHOE HORN 0.00 0.000 28 83.44</p>
<p>DL105-7 VAS-SHOELACES 0.00 0.000 54 51.30</p>
<p>DL106-2 VAS-SOCK AID 0.00 0.000 29 289.42</p>
<p>DL151-3 VAS BATH SPON 0.00 0.000 30 30.00</p>
<p>E0135-4 VAS-WALKER 0.00 0.000 11 0.00</p>
<p>E0142-2 VAS-WALKER SP 0.00 0.000 24 0.00</p>
<p>E0143-3 VAS WALKER W/ 0.00 0.000 17 552.50</p>
<p>E0155-3 VAS-WALKER WH 0.00 0.000 17 0.00</p>
<p>E0176-6 VAS AIR CUSHI 0.00 0.000 3 324.81</p>
<p>E0178-4 VAS GEL CUSHI 1 101.22 0.011 91.0 1 101.22</p>
<p>E0245-8 VAS-TUB BENCH 0.00 0.000 9 338.22</p>
<p>L8500-2 SERVOX-SPEECH 0.00 0.000 6 2,902.50</p>
<p>UNKNOWN-21VAS-SKI'S 0.00 0.000 17 0.00</p>
<p>------------------------------------------------------------------------------</p>
<p>Location: SAVANT</p>
<p>QTY $ DAYS AVE DAYS STOCK TOTAL $</p>
<p>HCPCS ITEM ISSUE VALUE USAGE RATE ON-HAND ON-HAND VAL ON-HND</p>
<p>----- ---- ----- ----- ---------- ------- ------- ----------</p>
<p>E0184-1 VAS MATTRESS 1 45.00 0.011 637.0 7 315.00</p>
<p>E0266-4 VAS BED ELECT 1 292.86 0.011 182.0 2 585.72</p>
<p>-----------------------------------------------------------------------------</p>
<p>Location: C-26</p>
<p>QTY $ DAYS AVE <strong>DAYS</strong> STOCK TOTAL $</p>
<p>HCPCS ITEM ISSUE VALUE USAGE RATE <strong>ON-HAND</strong> ON-HAND VAL ON-HND</p>
<p>----- ---- ----- ----- ---------- ------- ------- ----------</p>
<p>DL175-4 VAS-GLOVES-WH 0.00 0.000 24 0.00</p>
<p>E0100-6 VAS-CANE 0.00 0.000 10 0.00</p>
<p>E0191-9 VAS-CHEESE BO 0.00 0.000 23 0.00</p>
<p>E0776-3 VAS-IV POLE 0.00 0.000 21 157.50</p>
<p>K0001-4 VAS STANDARD/ 0.00 0.000 12 691.44</p>
<p>L1845-2 VAS KNEE BRAC 1 9.56 0.011 455.0 5 47.80</p>
<p>UNKNOWN-22VAS-BOOT-ROOK 0.00 0.000 12 0.00</p>
<p>------------------------------------------------------------------------------</p>
<p>&lt;End of Report&gt;</p></td>
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
<td><h5 id="days-on-hand">Days On-Hand</h5></td>
<td><blockquote>
<p>See <em><strong>Field/Column Descriptions</strong></em> in this section for a detailed explanation of the “Days On Hand” column of this report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Print Item Usage by Location (IU), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report parameters</td>
<td><blockquote>
<p>Below is a sample <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Item Usage by Location (IU)</strong> report selecting (C)ommercial (New Items) to display.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample Report – New Items (C)</td>
<td><p>* DETAIL ITEM USAGE BY LOCATION * <strong>for NEW Items</strong></p>
<p>Station: MILWAUKEE, WI Run Date: JUL 2,2001@13:27:06 PAGE: 1</p>
<p>APR 03, 2001 to JUL 02, 2001 [ 91 calendar days ]</p>
<p>------------------------------------------------------------------------------</p>
<p>Location: B-5</p>
<p>QTY $ DAYS AVE <strong>DAYS</strong> STOCK TOTAL $</p>
<p>HCPCS ITEM ISSUE VALUE USAGE RATE <strong>ON-HAND</strong> ON-HAND VAL ON-HND</p>
<p>----- ---- ----- ----- ---------- ------- ------- ----------</p>
<p>BA110-2 RAZOR-CORDLES 0.00 0.000 2 99.98</p>
<p>BA118-1 CASSETTE PLAY 0.00 0.000 4 91.80</p>
<p>BA158-2 GUIDE-EYEDROP 0.00 0.000 5 24.75</p>
<p>BA159-2 PILL BOX REMI 0.00 0.000 10 54.50</p>
<p>BA159-3 PILL REMINDER 11 11.66 0.121 165.5 20 21.20</p>
<p>BA183-3 SUNGLASSES NO 1 25.00 0.011 182.0 2 50.00</p>
<p>BA183-2 SUNGLASSES NO 0.00 0.000 4 100.00</p>
<p>BA184-2 CLOCK-TALK-AL 0.00 0.000 5 64.75</p>
<p>BA185-3 WATCH LOW VIS 0.00 0.000 4 45.16</p>
<p>BA185-4 WATCH LOW VIS 0.00 0.000 3 33.87</p>
<p>BA185-5 WATCH LOW VIS 0.00 0.000 4 45.16</p>
<p>BA185-6 WATCH TALKING 3 81.00 0.033 0.0 0.00</p>
<p>BA185-2 WATCH-BRAILLE 0.00 0.000 4 236.00</p>
<p>DL100-2 BUTTON HOOK-G 3 10.68 0.033 333.7 11 39.16</p>
<p>DL101-2 STICK-DRESSIN 13 62.27 0.143 14.0 2 9.58</p>
<p>DL103-1 REACHER-REGUL 3 20.55 0.033 60.7 2 13.70</p>
<p>DL104-1 SHOE HORN/COM 12 71.40 0.132 310.9 41 243.95</p>
<p>DL105-2 SHOELACES-ELA 3 4.50 0.033 576.3 19 28.50</p>
<p><strong>DL105-3 SHOELACES-ELA 2 3.00 0.022 &gt;999 22 33.00</strong></p>
<p>DL105-4 SHOELACES-ELA 7 10.50 0.077 208.0 16 24.00</p>
<p>------------------------------------------------------------------------------</p>
<p>&lt;End of Report&gt;</p></td>
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
<td>&gt;999 Value</td>
<td><blockquote>
<p>When the <strong>Days On Hand</strong> column displays a &gt;999 value, this means that the item is overstocked according to the calculation of the Stock on Hand.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425792" class="anchor"></span>Print Stock Work Sheet (WS)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Stock Work Sheet (WS)</strong> report prints the inventory stock by Location of a particular station. It shows the HCPCS, Item description, date, unit cost, vendor quantity, Location and a blank column for the physical count.</p>
<p><strong>Tip:</strong> You can use the blank column when conducting a physical inventory for reconciliation purposes.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select location for report data</td>
<td><p>Select Inventory Reports Option: <strong>WS</strong> <strong>&lt;Enter&gt;</strong> Print Stock Work Sheet</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Enter 'ALL' for all Locations or 'RETURN' to select individual Locations:</p>
<p><strong>&lt;Enter&gt;</strong></p>
<p>Select Location 1: <strong>JLOC &lt;Enter&gt;</strong></p>
<p>1 JLOC SUPPORT ISC</p>
<p>2 JLOC22 SUPPORT ISC</p>
<p>3 JLOC3 SUPPORT ISC</p>
<p>CHOOSE 1-3: <strong>1</strong> <strong>&lt;Enter&gt;</strong> JLOC SUPPORT ISC</p>
<p>Select Location 2: <strong>JLOC3</strong> <strong>&lt;Enter&gt;</strong> SUPPORT ISC</p>
<p>Select Location 3: <strong>&lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Processing report.....</p></td>
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
<td><h5 id="stock-reconciliation-work-sheet">Stock Reconciliation Work Sheet</h5></td>
<td><p>* PROSTHETICS STOCK RECONCILIATION WORK SHEET * PAGE: 1</p>
<p>Run Date: DEC 04, 2002 station: SUPPORT ISC</p>
<p>------------------------------------------------------------------------------</p>
<p><strong>Location: JLOC</strong></p>
<p>UNIT <strong>PHYSICAL</strong></p>
<p>HCPCS ITEM DATE COST VENDOR QTY LOCATION <strong>COUNT</strong></p>
<p>----- ---- ---- ---- ------ --- -------- -----</p>
<p>A4254-1 BATTERY FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>12/02/02 42.16 ABBOTT LA 25 JLOC ________</p>
<p>A4254-3 EYEGLASSES</p>
<p>05/07/02 45.00 ABBOTT LA 29 JLOC ________</p>
<p>A4373-1 WHEELCHAIR - ELECTRIC</p>
<p>02/05/02 200.00 ABBOTT LA 20 JLOC ________</p>
<p>BA185-2 WATCH BRAILLE</p>
<p>09/05/01 32.38 HINES VA 4 JLOC ________</p>
<p><strong>Location: JLOC3</strong></p>
<p>UNIT <strong>PHYSICAL</strong></p>
<p>HCPCS ITEM DATE COST VENDOR QTY LOCATION <strong>COUNT</strong></p>
<p>----- ---- ---- ---- ------ --- -------- -----</p>
<p>A4254-1 BATTERY FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>02/11/02 23.50 ABBOTT LA 37 JLOC3 ________</p>
<p>K0096-1 WHEELCHAIR - ELECTRIC</p>
<p>10/25/01 800.00 ABBOTT LA 10 JLOC3 ________</p>
<p>L5000-1 SHO INSERT W ARCH TOE FILL/COMMERCIAL</p>
<p>09/05/01 5.00 ABBOTT LA 192 JLOC3 ________</p>
<p>L5000-2 SHO INSERT W ARCH TOE/VA</p>
<p>09/05/01 3.00 ABBOTT LA 100 JLOC3 ________</p>
<p>&lt;End of Report&gt;</p></td>
</tr>
</tbody>
</table>

<span id="_Toc99425793" class="anchor"></span>Reprint Barcode Label (BC)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Reprint Barcode Label (BC)</strong> option allows inventory users to print barcode labels if you did not use the <strong>Receive Item from Supply, Vendor or Patient (RC)</strong> option. It will print labels for current inventory only. The HCPCS code for a stock item must exist in PIP before it can be printed on a barcode.</p>
<p>This option prints the following on a Barcode label:</p>
</blockquote>
<ul>
<li><p>HCPCS Code</p></li>
<li><p>HCPCS description</p></li>
<li><p>Unit Cost</p></li>
<li><p>Date received into inventory</p></li>
<li><p>Item description (local description of the item)</p></li>
<li><p>Vendor</p></li>
</ul></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report criteria</td>
<td><p>Select Inventory Reports Option: <strong>BC</strong> <strong>&lt;Enter&gt;</strong> Reprint Barcode Label</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Print Barcode Labels for current inventory...</p>
<p>Select HCPCS: <strong>?? &lt;Enter&gt;</strong></p>
<p>1 A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p>2 A4259 LANCETS PER BOX</p>
<p>3 A4402 LUBRICANT PER OUNCE</p>
<p>4 A4404 OSTOMY RING EACH</p>
<p>5 A4565 SLINGS</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, or</p>
<p>Choose 1 - 5 : <strong>1</strong> <strong>&lt;Enter&gt;</strong></p>
<p>HCPCS: A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p>is associated with more than 1 item, please select one...</p></td>
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
<td><h5 id="select-hcpcs">Select HCPCS</h5></td>
<td><blockquote>
<p>You can enter two question marks at the <strong>Select HCPCS</strong> prompt to display a list and select one. If it is associated with more than one item, it will list the IFCAP Items associated with it, and you can select one from the list. (See next page.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Reprint Barcode Label (BC), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Number of labels to print</td>
<td><blockquote>
<p>The <strong>Number of Labels to print</strong> prompt will have a default number set for the maximum number of labels that you can print. It will not allow you to print more than the default number; however, you can print less than the default number displayed.</p>
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
<td>Report sample</td>
<td><p>IFCAP ITEM: BATTERY</p>
<p>1 A4254-1 C BATTERY FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>IFCAP ITEM: BATTERY</p>
<p>4 A4254-1 C BATTERY FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>IFCAP ITEM: BATTERY</p>
<p>10 A4254-3 C BAT</p>
<p>Choose 1 - 10 : <strong>1 &lt;Enter&gt;</strong></p>
<p>HCPCS: A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p>IFCAP Item: BATTERY</p>
<p>PIP Item desc.: BATTERY FOR GLUCOSE MONITO/COMMERCIAL</p>
<p>Select a current stock record...</p>
<p>Date Qty Unit Cost Value Vendor Location</p>
<p>1 10/23/01 29 45.00 1305.00 ABB HO 1</p>
<p>2 01/08/02 1 155.00 155.00 M AND M MARS JLOC3</p>
<p>Choose 1 - 2 : <strong>1 &lt;Emter&gt;</strong></p>
<p>Number of Labels to print: 29//<strong>25</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Select Barcode Printer: ZEBRA PROSTHETIC// <strong>&lt;Enter&gt;</strong> ZEBRA PROSTHETIC PRINTER TONY'S DESK</p>
<p>Do you want your output QUEUED? NO// <strong>&lt;Enter&gt;</strong> (NO)</p>
<p>Print Barcode Labels for current inventory...</p>
<p>Select HCPCS: A4254// <strong>^ &lt;Enter&gt;</strong></p></td>
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
<td>To exit</td>
<td><blockquote>
<p>To exit the <strong>Reprint Barcode Label</strong> option, you can enter an “up caret” (^) at the <strong>Select HCPCS</strong> prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425794" class="anchor"></span>Print Items Not Issued Within 30-Day (P3)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-description">Report description</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Items Not Issued Within 30-Day (P3)</strong> report option prints Items not issued within a 30-day period. Items that have been issued within 30 days will <strong>NOT</strong> display on this report.</p>
<p><strong>Note:</strong> You can select “<strong>All</strong>” or specific Locations to display.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-criteria">Report criteria</h5></td>
<td><blockquote>
<p>Select Inventory Reports Option: P3<strong>&lt;Enter&gt;</strong>Print Items Not Issued Within 30-Day</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Enter 'ALL' for all Locations or 'RETURN' to select individual Locations: <strong>&lt;Enter&gt;</strong></p>
<p>Select <strong>Location 1</strong>: JLOC</p>
<p>1 JLOC SUPPORT ISC</p>
<p>2 JLOC22 SUPPORT ISC</p>
<p>3 JLOC22 (2) SUPPORT ISC</p>
<p>4 JLOC3 SUPPORT ISC</p>
<p>5 JLOC3 (2) SUPPORT ISC</p>
<p>CHOOSE 1-5: <strong>1</strong> <strong>&lt;Enter&gt;</strong> JLOC SUPPORT ISC</p>
<p>Select Location 2: JLOC3 &lt;Enter&gt;</p>
<p>1 JLOC3 SUPPORT ISC</p>
<p>2 JLOC3 (2) SUPPORT ISC</p>
<p>CHOOSE 1-2: <strong>1</strong> <strong>&lt;Enter&gt;</strong> JLOC3 SUPPORT ISC</p>
<p>Select Location 3: &lt;Enter&gt;</p>
<p>DEVICE: HOME// TELNET <strong>&lt;Enter&gt;</strong> Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Processing report.....</p>
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
<td><h5 id="print-items-not-issued-within-30-day-report">Print Items Not Issued Within 30-Day Report</h5></td>
<td><blockquote>
<p>* PROSTHETICS ITEMS NOT ISSUED WITHIN 30-DAY * PAGE: 1</p>
<p>Run Date: NOV 25, 2002 station: SUPPORT ISC</p>
<p>------------------------------------------------------------------------------</p>
<p>Location: JLOC</p>
<p>DATE UNIT TOTAL</p>
<p>HCPCS ITEM SRC VENDOR ENTERED QTY COST VALUE</p>
<p>----- ---- --- ------ ------- --- ---- ------</p>
<p>A4254-3 EYEGLASSES C ABBOTT 05/07/02 29 45.00 1,305.00</p>
<p>A4373-1 WHEELCHAIR - ELECTRIC V ABBOTT 02/05/02 20 200.00 4,000.00</p>
<p>BA185-2 WATCH BRAILLE C HINES V 09/05/01 4 32.38 129.52</p>
<p>BA185-3 WATCH LOW VISION BLACK C HINES V 09/05/01 46 2.82 129.72</p>
<p>E0111-2 CRUTCH FOREARM/VA V HINES V 09/05/01 3 2.00 6.00</p>
<p>V2025-1 EYEGLASSES C ABBOTT 05/07/02 16 35.07 561.10</p>
<p>V2025-1 EYEGLASSES C ABB 07/09/02 4 50.00 200.00</p>
<p>------------------------------------------------------------------------------</p>
<p>Location: JLOC3</p>
<p>DATE UNIT TOTAL</p>
<p>HCPCS ITEM SRC VENDOR ENTERED QTY COST VALUE</p>
<p>----- ---- --- ------ ------- --- ---- ------</p>
<p>A4254-1 BATTERY FOR GLUCOSE MONI C 01/08/02 1 155.00 155.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425795" class="anchor"></span>Print Stock on Hand Over Date Range (OD)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Stock on Hand Over Date Range (OD)</strong> report prints all Items in a particular Location, where the number of days on-hand is greater than the number of the days in the date range selected.</p>
<p><strong>Note:</strong> Sort criteria are based on Locations and <em><strong>new</strong></em> or <em><strong>old</strong></em> Items.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report sample</td>
<td><p>Select Inventory Reports Option: <strong>OD</strong> <strong>&lt;Enter&gt;</strong> Print Stock On Hand Over Date Range</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Enter 'ALL' for all Locations or 'RETURN' to select individual Locations: <strong>&lt;Enter&gt;</strong></p>
<p>Select Location 1: <strong>JLOC</strong> <strong>&lt;Enter&gt;</strong></p>
<p>1 JLOC SUPPORT ISC</p>
<p>2 JLOC22 SUPPORT ISC</p>
<p>3 JLOC3 SUPPORT ISC</p>
<p>CHOOSE 1-3: <strong>1</strong> &lt;<strong>Enter&gt;</strong> JLOC SUPPORT ISC</p>
<p>Select Location 2: <strong>JLOC3 &lt;Enter&gt;</strong> SUPPORT ISC</p>
<p>Select Location 3: <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p>V OLD Items</p>
<p>C NEW Items</p>
<p>Enter a SOURCE Criteria: NEW Items// <strong>V</strong> &lt;<strong>Enter&gt;</strong> OLD Items</p>
<p>Beginning Date: T-30//T-90 &lt;<strong>Enter&gt;</strong> (NOV 02, 2001)</p>
<p>Ending Date: TODAY// &lt;<strong>Enter&gt;</strong> (JAN 31, 2002)</p>
<p>DEVICE: HOME// &lt;<strong>Enter&gt;</strong> TELNET Right Margin: 80// &lt;<strong>Enter&gt;</strong></p>
<p>Processing report.....</p></td>
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
<td>Stock on Hand Over Date Range – for Used Items</td>
<td><p>* STOCK ON HAND OVER DATE RANGE * <strong>for USED Items</strong></p>
<p>Station: SUPPORT ISC Run Date: JAN 31,2002@10:17:48 PAGE: 1</p>
<p>NOV 02, 2001 to JAN 31, 2002 [ 91 calendar days ]</p>
<p>------------------------------------------------------------------------------</p>
<p><strong>Location: JLOC3</strong></p>
<p>QTY $ DAYS AVE DAYS STOCK TOTAL $</p>
<p>HCPCS ITEM ISSUE VALUE USAGE RATE ON-HAND ON-HAND VAL ON-HND</p>
<p>----- ---- ----- ----- ---------- ------- ------- ----------</p>
<p>L5000-2 SHO INSERT W 0.00 0.000 &gt;91 200 600.00</p>
<p>-----------------------------------------------------------------------------</p>
<p><strong>Location: JLOC</strong></p>
<p>QTY $ DAYS AVE DAYS STOCK TOTAL $</p>
<p>HCPCS ITEM ISSUE VALUE USAGE RATE ON-HAND ON-HAND VAL ON-HND</p>
<p>----- ---- ----- ----- ---------- ------- ------- ----------</p>
<p>E0111-2 CRUTCH FOREAR 0.00 0.000 &gt;91 3 6.00</p>
<p>------------------------------------------------------------------------------</p>
<p>&lt;End of Report&gt;</p></td>
</tr>
</tbody>
</table>

Continued on next page

Print Stock on Hand Over Date Range (OD), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample report</td>
<td><blockquote>
<p>Below is the <strong>Stock On Hand Over Date Range</strong> report for <strong>NEW</strong> Items.</p>
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
<td>Stock On Hand Over Date Range for New Items</td>
<td><blockquote>
<p>* STOCK ON HAND OVER DATE RANGE * <strong>for NEW Items</strong></p>
<p>Station: MILWAUKEE Run Date: DEC 18,2001@12:54:31 PAGE: 1</p>
<p>NOV 18, 2001 to DEC 18, 2001 <strong>[ 31 calendar days ]</strong></p>
<p>------------------------------------------------------------------------------</p>
<p>Location: RMB5</p>
<p>QTY $ DAYS AVE <strong>DAYS</strong> STOCK TOTAL $</p>
<p>HCPCS ITEM ISSUE VALUE USAGE RATE <strong>ON-HAND</strong> ON-HAND VAL ON-HND</p>
<p>----- ---- ----- ----- ---------- ------- ------- ----------</p>
<p>BA110-2 RAZOR-CORDLES 0.00 0.000 &gt;31 2 99.98</p>
<p>BA118-1 CASSETTE PLAY 0.00 0.000 &gt;31 4 91.80</p>
<p>BA158-2 GUIDE-EYEDROP 0.00 0.000 &gt;31 5 24.75</p>
<p>BA159-2 PILL BOX REMI 3 16.35 0.097 72.3 7 38.15</p>
<p>BA159-3 PILL REMINDER 0.00 0.000 &gt;31 20 21.20</p>
<p>BA183-3 SUNGLASSES NO 0.00 0.000 &gt;31 2 50.00</p>
<p>BA183-2 SUNGLASSES NO 0.00 0.000 &gt;31 4 100.00</p>
<p>BA184-2 CLOCK-TALK-AL 0.00 0.000 &gt;31 5 64.75</p>
<p>BA185-3 WATCH LOW VIS 0.00 0.000 &gt;31 4 45.16</p>
<p>BA185-4 WATCH LOW VIS 0.00 0.000 &gt;31 3 33.87</p>
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
<td><h5 id="days-on-hand-1">Days on Hand</h5></td>
<td><blockquote>
<p>Note that there is one line item that shows 72.3 in the <strong>Days On-Hand</strong> column in the report shown above. This means that the Stock On Hand is shown for 72.3 days over the date range selected of 31 calendar days (72.3 Days On-Hand + 31 calendar days).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425796" class="anchor"></span>Print All Barcode in a Location (AL)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>With Patch RMPR*3*61, the <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print All Barcode in a Location</strong> <strong>(AL)</strong> option is available for use in printing all the barcode labels for all Items within a Location. (<u>This is a helpful option to use after <strong>first</strong> installing this patch into the Production (Live) system</u>.)</p>
<p>In order to use this option, you must have an RMPRMANAGER key. Insert enough labels in the printer before using this option, since it will print labels for all Items in a given station.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="inventory-reports-menu">Inventory Reports Menu</h5></td>
<td><blockquote>
<p>SI Item Detail Report</p>
<p>SH HCPCS Summary Report</p>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>P3 Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
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
<td><h5 id="sample-screen-2">Sample screen</h5></td>
<td><blockquote>
<p>Select Inventory Reports Option: <strong>AL</strong> <strong>&lt;Enter&gt;</strong> Print All Barcode in a Location</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Enter Pros Location: <strong>??</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>HO 1</p>
<p>A LOC</p>
<p>HNC</p>
<p>HO 1</p>
<p>JLOC</p>
<p>JLOC22</p>
<p>JLOC22 (2)</p>
<p>JLOC3</p>
<p>JLOC3 (2)</p>
<p>MERGER</p>
<p>MERGER (2)</p>
<p>ODJ2</p>
<p>ODJLOC1</p>
<p>Enter Pros Location: JLOC <strong>&lt;Enter&gt;</strong></p>
<p>Select Barcode Printer: ZEBRA PROSTHETIC// <strong>&lt;Enter&gt;</strong> ZEBRA PROSTHETIC PRINTER</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425797" class="anchor"></span>Print PIP/IFCAP Item Report (IP)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-description-1">Report description</h5></td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print PIP/IFCAP Items Report (IP)</strong> prints all PIP Items and the corresponding IFCAP Items. If this report does NOT print an IFCAP Item, and this column is blank, then Prosthetics users must edit the HCPCS/Item. When an IFCAP Item is entered, then there is a link to the PIP Item. This report is useful for checking if the IFCAP Item is correctly linked to the PIP Item.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>New Report Menu Option with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="inventory-reports-menu-1">Inventory Reports Menu</h5></td>
<td><blockquote>
<p>SI Item Detail Report</p>
<p>SH HCPCS Summary Report</p>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>P3 Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
<p>Select Inventory Reports Option: <strong>IP</strong> <strong>&lt;Enter&gt;</strong> Print PIP/IFCAP Item Report</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Processing report.....</p>
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
<td><h5 id="print-pipifcap-items-report">Print PIP/IFCAP Items Report</h5></td>
<td><blockquote>
<p>* PROSTHETICS PIP/IFCAP ITEMS REPORT* PAGE: 1</p>
<p>Run Date: DEC 12, 2002 Station: SUPPORT ISC</p>
<p>------------------------------------------------------------------------------</p>
<p>HCPCS-ITEM PIP ITEM IFCAP ITEM</p>
<p>---------- -------- ----------</p>
<p>A4254-1 BATTERY FOR GLUCOSE BEEF-ROUND/TOP/INSIDE/FRZN</p>
<p>A4254-2 BAT FOR GLUCOSE MONI BEEF-ROUND/TOP/INSIDE/FRZN</p>
<p>A4254-3 EYEGLASSES BEEF-ROUND/TOP/INSIDE/FRZN</p>
<p>A4259-1 LANCETS PER BOX/COMM WHEELCHAIR-CLASSIC-18X16</p>
<p>A4301-1 WHEELCHAIR-ADULT/HEM SHOES</p>
<p>A4373-1 WHEELCHAIR - ELECTRI WHEELCHAIR - ELECTRIC</p>
<p>A4373-2 WC MAN WHEELCHAIR - MANUAL</p>
<p>A4402-1 LUBRICANT PER OUNCE/ PORK-GROUND/FRZN</p>
<p>A4402-2 LANCETS PER BOX/COMM OXYGEN DEVICE</p>
<p>A4404-1 OSTOMY RING EACH/COM OXYGEN CONCENTRATOR</p>
<p>A4404-2 OSTOMY RING EACH/COM EYEGLASSES</p>
<p>A4404-3 EYEGLASSES EYEGLASSES</p>
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
<td><h5 id="ifcap-item">IFCAP Item</h5></td>
<td><blockquote>
<p>If there is a blank in the IFCAP Item column on this report, then you will need to edit this Item through the <strong>Edit Inventory Items (EI)</strong> option and add an item description at the <em><strong>IFCAP/Item</strong></em> prompt from the list of options.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425798" class="anchor"></span>Prosthetic Inventory Reports (Patch RMPR\*3\*51)

<span id="_Toc99425799" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>There are four Inventory Reports from Patch RMPR*3*51 in the <strong>Inventory Reports</strong> Menu. These usage reports are available for the sites and for PSAS Headquarters personnel to use.</p>
<p>The four types of reports and the options that display them are:</p>
</blockquote>
<ul>
<li><p>Item Detail Report (SI)</p></li>
<li><p>HCPCS Summary Report (SH)</p></li>
<li><p>NPPD Group/Lines Report (SG)</p></li>
<li><p>NPPD Group Report (SS)</p></li>
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
<td>Headquarter Roll-up Data</td>
<td><blockquote>
<p>Headquarters personnel can request all reports through a server process. They can request a roll-up for station inventory data for a certain date range through a server. The roll-up data is loaded in an Excel document and can be used for other reporting purposes.</p>
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
<td>Purpose</td>
<td><blockquote>
<p>Usage reports are developed for the site level that will show stock usage over a selected date range. Each report is sorted first by site and by a date range.</p>
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
<td>USED and NEW Inventory</td>
<td><blockquote>
<p>There are values for USED and NEW inventory shown separately on the usage reports. These values are never added together.</p>
<p><strong>Note:</strong> If the same item (with the same HCPCS code) has both NEW and USED quantities entered against it, then the report will print NEW and USED figures on separate lines.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc501807359" class="anchor"></span>Access the Inventory Reports Menu

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetic Official’s Menu</td>
<td><p>PU Purchasing ...</p>
<p>DD Display/Print ...</p>
<p>UT Utilities ...</p>
<p>AM AMIS ...</p>
<p>SU Suspense ...</p>
<p>CO Correspondence ...</p>
<p>SC Scheduled Meetings and Home/Liaison Visits ...</p>
<p>PS Process Form 2529-3 ...</p>
<p>EL Eligibility Inquiry</p>
<p>ET PSC/Entitlement Records ...</p>
<p>HO Home Oxygen Main Menu <strong>...</strong></p>
<p><strong>INV Pros Inventory Main ...</strong></p>
<p>ND NPPD Tools ...</p>
<p>VR Verify/Repair Purchase Card Number</p>
<p>Select Prosthetic Official's Menu Option: <strong>INV</strong> Pros Inventory Main</p></td>
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
<p>To access the <strong>Prosthetic Inventory Reports</strong> Menu, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                   |
| 1    | At the Prosthetic Official’s Menu, type INV for the Prosthetic Inventory Main Menu, and press \<Enter\>. |
| 2    | Type RP for Inventory Reports Menu, and press \<Enter\>.                                                     |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetic Inventory Main Menu</td>
<td><p>AE Add Inventory LOCATION or ITEMS</p>
<p>EI Edit Inventory Items</p>
<p>EL Edit Inventory Location</p>
<p>DE Deactivate Inventory Location</p>
<p>RI Remove Item from Inventory</p>
<p>OI Order Item from Supply or Vendor</p>
<p>RC Receive Item from Supply, Vendor or Patient</p>
<p>TR Transfer Stock Between Locations</p>
<p>UP Reconcile Item Balance</p>
<p><strong>RP Inventory Reports ...</strong></p>
<p>RE Remove/Deactivate HCPCS/Item from Inventory</p>
<p>Select Pros Inventory Main Option: <strong>RP</strong> Inventory Reports</p></td>
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
<td>Inventory Reports Menu</td>
<td><blockquote>
<p>SI Item Detail Report</p>
<p>SH HCPCS Summary Report</p>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>P3 Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print ALL Barcode in a Location</p>
</blockquote>
<p>IP Print PIP/IFCAP Item Report</p></td>
</tr>
</tbody>
</table>

<span id="_Toc501807360" class="anchor"></span>Field/Column Descriptions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Fields and columns</td>
<td><blockquote>
<p>Below are the field and column descriptions within the inventory reports.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 30%" />
<col style="width: 27%" />
<col style="width: 36%" />
<col style="width: 5%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Field/Column</td>
<td colspan="3">Description</td>
</tr>
<tr class="even">
<td><strong>Run Date</strong></td>
<td colspan="3">The date and time the report is run shown on the first line of a report.</td>
</tr>
<tr class="odd">
<td><strong>Station</strong></td>
<td colspan="3">The system location that you select or it may be a default. If you have only one site, this prompt is not available.</td>
</tr>
<tr class="even">
<td><strong>Number of Calendar Days</strong></td>
<td colspan="3">Total number of calendar days for the date range selected will be shown on the second line of a report.</td>
</tr>
<tr class="odd">
<td><strong>HCPCS</strong></td>
<td colspan="3">HCPCS code.</td>
</tr>
<tr class="even">
<td><p><strong>PSAS/Item</strong></p>
<p><strong>Description</strong></p></td>
<td colspan="3"><p>Free-text description of the item from the name entered into the “Add an Item” option. This is shown only on the <strong>Item Detail Report</strong>.</p>
<p>On the <strong>HCPCS Summary Report</strong>, the <em>Description</em> field replaces the <em>PSAS Item</em> field and provides a description of the HCPCS code.</p></td>
</tr>
<tr class="odd">
<td><strong>VA (Used)</strong></td>
<td>Number issued and dollar value for USED inventory.</td>
<td rowspan="3"><p><strong>CAUTION: These dollar values may not equal the dollar values on the 2319. (See Appendix A for a more detailed explanation.)</strong></p>
<p><strong>These are the values for the date range selected. In the examples to follow, it would be the numbers issued for September 2000.</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>COM (New)</strong></td>
<td>Number issued and dollar value for NEW inventory.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Total Issue</strong></td>
<td>Total number issued for the VA (Used) and Commercial (New) on different lines.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Days Ave Usage Rate</strong></td>
<td colspan="3"><p>Average rate of use per day. This is the total issued (both USED or NEW) divided by the total calendar days for the date range selected.</p>
<p><strong><u>Note</u>:</strong> Value will be expressed in decimal format if usage rate is less than one unit per day.</p>
<p><strong><u>Example</u>:</strong> If an item was issued ten times during a 20 day period, the average usage rate over the period would be 0.5.</p></td>
</tr>
<tr class="odd">
<td><strong>Stock On-Hand</strong></td>
<td colspan="3"><p>Number of USED and number of NEW stock on-hand items remaining in inventory.</p>
<p><strong><u>Note</u>:</strong> These quantities refer to the date the report was run and not necessarily the date range entered.</p></td>
</tr>
</tbody>
</table>

Continued on next page

Field/Column Descriptions, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Fields and columns (continued)</td>
<td><blockquote>
<p>Below are the descriptions of the each of the columns and fields within the usage reports.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Field/Column</td>
<td>Description</td>
</tr>
<tr class="even">
<td><strong>Days On-Hand</strong></td>
<td><p>Number of days of quantity on-hand remaining in inventory. This is the Total Stock on Hand divided by the Days Average Usage Rate.</p>
<p><strong><u>Example</u>:</strong> To refer to the previous example where 10 items were issued during a 20-day period, if we had 10 items left in the inventory, the Days On Hand Value would be 20. The quantity on hand refers to the date the report was run and not necessarily the date range entered.</p>
<p><strong><u>Note</u>:</strong> If you see &gt;nn, where nn equals the number of calendar days, then it means no items were issued during those calendar days. If you see &gt;999, this means that the inventory on hand exceeds 999 days.</p></td>
</tr>
<tr class="odd">
<td><strong>Total Dollar Value On-Hand</strong></td>
<td><p>Total value of USED and total value of NEW on-hand.</p>
<p><strong><u>Note</u>:</strong> This is not the total of the average cost. This is the total cost to purchase the items on hand.</p></td>
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
<td>Grand totals</td>
<td><blockquote>
<p>At the bottom of the reports, the following grand totals are shown:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                             |                                              |
|---------------------------------------------|----------------------------------------------|
| Field/Column                                | Description                                  |
| Grand Total Dollar Value Issued (Used)  | Total dollar value of USED inventory issued. |
| Grand Total Dollar Value Issued (New)   | Total dollar value of NEW inventory issued.  |
| Grand Total Dollar Value on Hand (Used) | Total cost of USED stock on hand.            |
| Grand Total Dollar Value on Hand (New)  | Total cost of NEW stock on hand.             |

<span id="_Hlt501531386" class="anchor"></span>Viewing/Printing Reports

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column Size</td>
<td><blockquote>
<p>Contact your IRM department to change the column size from 80 to 132-column width size to print the Inventory Reports and view them on your screen.</p>
<p><strong>See instructions below if</strong> you use a terminal emulation software on a PC to view a report on your screen or print it out. You must change the column size that is viewable from 80 characters wide to 132 characters. Otherwise, you will <strong><u>not</u></strong> be able to view the entire contents of a report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                           |
| 1    | Click the Options Menu.                                                                                      |
| 2    | Click the Display option. The Display dialog box displays as shown below. Click the VT Specific tab. |
| 3    | Click the down arrow in the Columns field and select 132.                                                    |
| 4    | Click the Ok button.                                                                                         |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display Option</td>
<td><blockquote>
<p>![](rmpr-3-61-prosthetics-inventory-package-pip-user-manual/002.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Hlt500262678" class="anchor"></span>Item Detail Report (SI)

<span id="_Toc501807363" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Item Detail Report</strong> option provides a detailed report that displays the stock on hand sorted by HCPCS/Item at the facility level. (This is the report that provides the greatest amount of detail vs. the <strong>HCPCS Summary Report</strong> that only provides high-level summary information.) The following are the sort criteria options:</p>
</blockquote>
<ul>
<li><p>All HCPCS (default setting)</p></li>
<li><p>All HCPCS for an NPPD Group</p></li>
<li><p>All HCPCS for an NPPD Line (or related HCPCS)</p></li>
<li><p>Select Individual HCPCS (more than one HCPCS can be selected)</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> Each option above has the same report format (i.e., HCPCS always grouped under respective NPPD Line and Group headings.)</p>
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
<p>To select the <strong>Item Detail Report</strong>, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                 |
|------|---------------------------------------------------------------------------------|
| Step | Action                                                                          |
| 1    | Type SI for the ItemDetail Report option, and press \<Enter\>. |
| 2    | At the Site prompt, press \<Enter\> to select the default site entry.   |
| 3    | At the Beginning Date prompt, type the beginning date of the date range.    |
| 4    | At the Ending Date prompt, type the end date, and press \<Enter\>.      |
| 5    | The four options to view or print the Item Detail Report displays.          |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Inventory Reports Menu</td>
<td><blockquote>
<p>SI Item Detail Report</p>
<p>SH HCPCS Summary Report</p>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>PC Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
</blockquote>
<p>Select Inventory Reports Option: <strong>SI</strong> &lt;<strong>Enter</strong>&gt; <strong>Item Detail Report</strong></p>
<p>SITE: Hines Development System// &lt;<strong>Enter</strong>&gt; ST. NUM. 499</p>
<p>Beginning Date: <strong>9/1/00</strong> (SEP 01, 2000) &lt;<strong>Enter</strong>&gt;</p>
<p>Ending Date: <strong>9/30/00</strong> (SEP 30, 2000) &lt;<strong>Enter</strong>&gt;</p>
<p>Select one of the following:</p>
<p><strong>A ALL HCPCS</strong></p>
<p>G ALL HCPCS for NPPD group</p>
<p>L ALL HCPCS for NPPD line</p>
<p>S Select individual HCPCS</p></td>
</tr>
</tbody>
</table>

<span id="_Toc501807364" class="anchor"></span>Item Detail Report – Choosing “All HCPCS”

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>You can select to view or print the <strong>Item Detail Report</strong> using the <strong>All HCPCS</strong>. This is the default setting, and you can press &lt;<strong>Enter</strong>&gt; instead of typing <strong>A</strong> and pressing <strong>&lt;Enter&gt;</strong>.</p>
<p>All HCPCS/Item in a group will be shown on the report even if there was no activity during the reporting date range.</p>
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
<p>To select the <strong>All HCPCS</strong> option for the <strong>Item Detail Report</strong>, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                   |
| 1    | At the Choose HCPCS Selection prompt, type A for the All HCPCS option, and press \<Enter\>.                              |
| 2    | At the Device: Home// prompt, press \<Enter\>                                                                                    |
| 3    | To view or print the report, type 132 at the Right Margin: 80// prompt to extend the margins for the report to display and/or print. |
| 4    | Then press \<Enter\>.                                                                                                                |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item Detail Report Options</td>
<td><p>Select one of the following:</p>
<p><strong>A ALL HCPCS</strong></p>
<p>G ALL HCPCS for NPPD group</p>
<p>L ALL HCPCS for NPPD line</p>
<p>S Select individual HCPCS</p>
<p>Choose HCPCS selection option: <strong>A//</strong> &lt;<strong>Enter</strong>&gt; <strong>ALL HCPCS</strong></p>
<p>DEVICE: HOME// &lt;<strong>Enter</strong>&gt; TELNET Right Margin: 80// <strong>132</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>Processing report.......</p></td>
</tr>
</tbody>
</table>

Continued on next page

Item Detail Report – Choosing “All HCPCS”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>All HCPCS</td>
<td><blockquote>
<p>Below is the <strong>Prosthetic</strong> <strong>Inventory Item Detail Report</strong> using the <strong>All HCPCS</strong> option. Also, you can run a report for a one-day range to see beginning inventory balances.</p>
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
<td><p>PROSTHETIC INVENTORY ITEM DETAIL REPORT Run Date: DEC 14,2000@10:00:04 Page: 1</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>100 B MANUAL CUSTOM [WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>K0004-1 HIGH STRENGTH L | 0 0.00 | 0 | 0.00 | 2 | &gt;30| 758.78</p>
<p>K0004-2 WHEELCHAIR 9000 | 10 3.00 | 10 | 0.33 | 3 | 9| 1,098.03</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 10 3,294.09 | 10 | 0.33 | 5 | | 1,856.81</p>
<p>100 C STANDARD [WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>K0001-2 WHEELCHAIR INVA | 5 576.25 | 5 | 0.17 | 3 | 18| 387.30</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 5 576.25 | 5 | 0.17 | 3 | | 387.30</p>
<p>100 D ACCESSORIES [WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>DL175-2 GLOVES-WHEELCHA | 8 56.00 | 8 | 0.27 | 13 | 49| 91.00</p>
<p>DL175-3 GLOVES-WHEELCHA | 8 56.00 | 8 | 0.27 | 28 | 105| 196.00</p>
<p>DL177-1 COVER-MATTRESS- | 0 0.00 | 0 | 0.00 | 5 | &gt;30| 281.85</p>
<p>DL177-2 COVER-ROHO-1R88 | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 252.00</p>
<p>DL177-3 COVER-ROHO-1R89 | 0 0.00 | 0 | 0.00 | 8 | &gt;30| 181.44</p>
<p>E0978-1 WHEELCHAIR BELT | 0 0.00 | 0 | 0.00 | 5 | &gt;30| 154.25</p>
<p>K0019-1 ARM PAD EACH/CO | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 30.00</p>
<p>K0020-1 FIXED ADJUST AR | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 19.80</p>
<p>K0045-1 FOOTREST COMPLE | 0 0.00 | 0 | 0.00 | 8 | &gt;30| 80.00</p>
<p>K0098-1 DRIVE BELT POWE | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 86.40</p>
<p>===============================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 24 | | 0.00</p>
<p>(New) | 16 112.00 | 16 | 0.53 | 91 | | 1,372.74</p>
<p>100 E CUSHION FOAM [WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>E0963-2 CUSHION-FOAM-16 | 1 7.35 | 1 | 0.03 | 2 | 60| 14.70</p>
<p>E0963-3 CUSHION-FOAM-18 | 1 8.40 | 1 | 0.03 | 2 | 60| 16.80</p>
<p>E0964-2 CUSHION-FOAM-18 | 9 82.71 | 9 | 0.30 | 9 | 30| 82.71</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 11 98.46 | 11 | 0.37 | 13 | | 114.21</p>
<p>100 F CUSHION SPEC [WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>E0176-2 CUSHION-DONUT-V | 0 0.00 | 0 | 0.00 | 7 | &gt;30| 11.27:</p>
<p>E0176-3 CUSHION-ROHO-1R | 4 654.69 | 4 | 0.13 | 7 | 53| 1,527.61</p>
<p>E0176-4 CUSHION-ROHO-1R | 1 216.54 | 1 | 0.03 | 4 | 120| 866.16</p>
<p>E0176-5 CUSHION-ROHO-1R | 1 216.54 | 1 | 0.03 | 4 | 120| 866.16</p>
<p>E0178-2 CUSHION-JAY 2 | 3 607.38 | 3 | 0.10 | 6 | 60| 1,214.76</p>
<p>E0178-3 CUSHION-JAY-ACT | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 799.56</p>
<p>===============================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 9 1,695.15 | 9 | 0.30 | 32 | | 5,285.52</p>
<p>GRAND TOTAL $ VALUE ISSUED (Used) = $ 483.75 GRAND TOTAL $ VALUE ON-HAND (Used) = $ 2,276.54</p>
<p>GRAND TOTAL $ VALUE ISSUED (New) = $ 26,150.77 GRAND TOTAL $ VALUE ON-HAND (New) = $ 97,658.36</p>
<blockquote>
<p>&lt;End of Report&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc501807365" class="anchor"></span>Item Detail Report – Choosing “All HCPCS for NPPD Group”

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>You can select to view or print the <strong>Item Detail Report</strong> using the <strong>All HCPCS for NPPD Group</strong> criteria. This criteria option provides a list of NPPD Groups. You will be able to select a single NPPD Group or multiple NPPD Groups.</p>
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
<p>To view or print the <strong>Item Detail Report</strong> for <strong>All HCPCS for NPPD Group</strong>, follow these steps:</p>
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
<td>1</td>
<td>At the <strong>Choose HCPCS Selection</strong> prompt, type <strong>G</strong> for the <strong>All HCPCS for NPPD Group</strong> option, and press &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>A list of NPPD Groups displays. Type a number of the NPPD Group you want to select, and press &lt;<strong>Enter</strong>&gt;.</p>
<p><strong>Note:</strong> You can select multiple NPPD Groups, by typing a list or range of numbers (e.g., 1,3,5 or 2-4,8).</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>At the <strong>Device: Home//</strong> prompt, press &lt;<strong>Enter</strong>&gt;</td>
</tr>
<tr class="odd">
<td>4</td>
<td>To view or print the report, type “<strong>;132;”</strong> at the <strong>Right Margin: 80//</strong> prompt to extend the margins for the report to display and/or print, and press &lt;<strong>Enter</strong>&gt;.</td>
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
<td>All HCPCS for NPPD Group option</td>
<td><p>Select one of the following:</p>
<p>A ALL HCPCS</p>
<p><strong>G ALL HCPCS for NPPD group</strong></p>
<p>L ALL HCPCS for NPPD line</p>
<p>S Select individual HCPCS</p>
<p>Choose HCPCS selection option: A// <strong>G &lt;Enter&gt; ALL HCPCS for NPPD group</strong></p>
<p>1. WHEELCHAIRS AND ACCESSORIES</p>
<p>2. ARTIFICIAL LEGS</p>
<p>3. ARTIFICIAL ARMS AND TERMINAL DEVICES</p>
<p><strong>4. BRACES AND ORTHOTICS</strong></p>
<p>5. SHOES/ORTHOTICS</p>
<p>6. NEUROSENSORY AIDS</p>
<p>7. RESTORATIONS</p>
<p>8. OXYGEN AND RESPIRATORY</p>
<p>9. MEDICAL EQUIPMENT</p>
<p>10. ALL OTHER SUPPLIES AND EQUIPMENT</p>
<p>11. HOME DIALYSIS PROGRAM</p>
<p>12. ADAPTIVE EQUIPMENT</p>
<p>13. HISA</p>
<p>14. SURGICAL IMPLANTS</p>
<p>15. MISC</p>
<p>Select NPPD Group : (1-15): <strong>4</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>DEVICE: HOME// <strong>;132;</strong> <strong>&lt;Enter&gt;</strong> TELNET VIRTUAL Processing report.......</p></td>
</tr>
</tbody>
</table>

Continued on next page

Item Detail Report – Choosing “All HCPCS for NPPD Group”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report sample</td>
<td><blockquote>
<p>Below is the Prosthetic <strong>Inventory Item Detail Report</strong> with the <strong>All HCPCS for NPPD Group</strong> criteria selected.</p>
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
<td><p>PROSTHETIC INVENTORY ITEM DETAIL REPORT Run Date: DEC 14,2000@10:03:24 Page: 1</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>400 A BRACE ANKLE [BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L1902-1 AFO ANKLE GAUNT | 5 17.80 | 5 | 0.17 | 2 | 12| 7.12</p>
<p>L1902-2 BRACE ANKLE LAC | 0 0.00 | 0 | 0.00 | 3 | &gt;30| 42.00</p>
<p>L1902-3 BRACE ANKLE LAC | 0 0.00 | 0 | 0.00 | 2 | &gt;30| 28.00</p>
<p>L1902-4 BRACE ANKLE LAC | 0 0.00 | 0 | 0.00 | 12 | &gt;30| 168.00</p>
<p>L1902-5 BRACE ANKLE LAC | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 56.00</p>
<p>L1930-1 AFO PLASTIC/COM | 0 0.00 | 0 | 0.00 | 1 | &gt;30| 19.87</p>
<p>L1930-2 BRACE AFO LEFT | 2 39.92 | 2 | 0.07 | 2 | 30| 39.92</p>
<p>L1930-3 BRACE AFO PLAST | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 79.48</p>
<p>L1930-4 BRACE AFO PLAST | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 119.22</p>
<p>L1930-5 BRACE AFO PLAST | 0 0.00 | 0 | 0.00 | 5 | &gt;30| 99.35</p>
<p>L1930-6 BRACE AFO PLAST | 1 19.87 | 1 | 0.03 | 4 | 120| 79.48</p>
<p>L1930-7 BRACE AFO PLAST | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 119.22</p>
<p>L1930-8 BRACE AFO PLAST | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 119.22</p>
<p>L4392-2 SOLE-WALKING | 1 4.50 | 1 | 0.03 | 8 | 240| 36.00</p>
<p>L4392-3 LINER-REPLACEME | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 94.50</p>
<p>L4392-4 LINER-REPLACEME | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 94.50</p>
<p>L4396-2 BRACE-MULTIPODU | 0 0.00 | 0 | 0.00 | 40 | &gt;30| 1,800.00</p>
<p>L4396-3 BRACE-MULTIPODU | 3 135.00 | 3 | 0.10 | 10 | 100| 450.00</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 12 217.09 | 12 | 0.40 | 127 | | 3,451.88</p>
<p>400 D BRACE AL/OTH [BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L0120-1 COLLAR-CERVICAL | 0 0.00 | 0 | 0.00 | 11 | &gt;30| 48.40</p>
<p>L0120-5 COLLAR-CERVICAL | 3 8.55 | 3 | 0.10 | 9 | 90| 25.65</p>
<p>L0120-6 COLLAR-CERVICAL | 1 3.70 | 1 | 0.03 | 3 | 90| 11.10</p>
<p>L0120-7 COLLAR-CERVICAL | 0 0.00 | 0 | 0.00 | 12 | &gt;30| 44.40</p>
<p>L0120-8 COLLAR-CERVICAL | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 28.50</p>
<p>L2270-1 VARUS/VALGUS ST | 0 0.00 | 0 | 0.00 | 3 | &gt;30| 43.92</p>
<p>L3670-2 SLING ARM BLUE | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 28.02</p>
<p>L3700-1 ELBOW ORTHOSES | 4 39.80 | 4 | 0.13 | 8 | 60| 79.60</p>
<p>L3907-2 BRACE WRIST SPI | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 157.50</p>
<p>L3907-3 BRACE WRIST SPI | 1 15.75 | 1 | 0.03 | 9 | 270| 141.75</p>
<p>L3908-2 BRACE-WRIST-LAR | 7 27.09 | 7 | 0.23 | 19 | 81| 73.53</p>
<p>L3908-3 BRACE-WRIST-LAR | 5 19.35 | 5 | 0.17 | 5 | 30| 19.35</p>
<p>L3908-4 BRACE-WRIST-MED | 2 7.74 | 2 | 0.07 | 13 | 195| 50.31</p>
<p>L3908-5 BRACE-WRIST-MED | 1 3.87 | 1 | 0.03 | 23 | 690| 89.01</p>
<p>L3908-6 BRACE-WRIST-SMA | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 15.48</p>
<p>L3908-7 BRACE-WRIST-SMA | 1 3.87 | 1 | 0.03 | 5 | 150| 19.35</p>
<p>L3908-8 BRACE-WRIST-XLA | 7 30.96 | 7 | 0.23 | 7 | 30| 27.09</p>
<p>L3908-9 BRACE-WRIST-XLA | 7 50.31 | 7 | 0.23 | 16 | 69| 123.84</p>
<p>L3908-10 BRACE-WRIST-RIG | 1 3.87 | 1 | 0.03 | 11 | 330| 42.57</p>
<p>L4350-1 PNEUMATIC ANKLE | 2 49.00 | 2 | 0.07 | 1 | 15| 24.50</p>
<p>L4360-2 CAMWALKER-LARGE | 7 315.00 | 7 | 0.23 | 2 | 9| 90.00</p>
<p>L4360-3 CAMWALKER-MEDIU | 8 640.00 | 8 | 0.27 | 9 | 34| 405.00</p>
<p>L4360-4 CAMWALKER-SHORT | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 450.00</p>
<p>L4360-6 CAMWALKER-SHORT | 0 0.00 | 0 | 0.00 | 12 | &gt;30| 540.00</p>
<p>L4360-7 CAMWALKER-SMALL | 0 0.00 | 0 | 0.00 | 11 | &gt;30| 495.00</p>
<p>L4360-10 CAMWALKER-SHORT | 0 0.00 | 0 | 0.00 | 12 | &gt;30| 540.00</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 57 1,218.86 | 57 | 1.90 | 242 | | 3,613.87</p></td>
</tr>
</tbody>
</table>

(Screen print sample continued on next page…)

Continued on next page

Item Detail Report – Choosing “All HCPCS for NPPD Group”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report sample (continued)</td>
<td><blockquote>
<p>Below is the continued <strong>Prosthetic Inventory Item Detail Report</strong> with the <strong>All HCPCS for NPPD Group</strong> criteria selected.</p>
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
<td><p>400 E ELAS HOSE, EA [BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L8100-1 ELAS SUPRT STOC | 0 0.00 | 0 | 0.00 | 22 | &gt;30| 304.32</p>
<p>L8100-2 STOCKING VENOSA | 2 19.38 | 2 | 0.07 | | 0|</p>
<p>L8100-6 FAST FIT 114 20 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-7 FAST FIT 114 21 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-8 FAST FIT 114 21 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-9 FAST FIT 114 21 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-10 FAST FIT 114 22 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-11 FAST FIT 114 22 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-12 FAST FIT 114 23 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-13 FAST FIT 114 23 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-14 FAST FIT 114 23 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-15 FAST FIT 114 24 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-16 FAST FIT 114 24 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-17 FAST FIT 114 24 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-18 FAST FIT 114 24 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-19 FAST FIT 114 25 | 2 49.76 | 2 | 0.07 | 4 | 60| 99.52</p>
<p>L8100-20 FAST FIT 114 26 | 2 49.76 | 2 | 0.07 | 5 | 75| 124.40</p>
<p>L8100-21 ULTIMATE STOCKI | 0 0.00 | 0 | 0.00 | 2 | &gt;30| 35.00</p>
<p>L8100-22 ULTIMATE STOCKI | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 105.00</p>
<p>L8100-23 ULTIMATE STOCKI | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 105.00</p>
<p>L8100-24 STOCKING-VENOSA | 4 38.76 | 4 | 0.13 | 20 | 150| 193.80</p>
<p>L8100-25 STOCKING-VENOSA | 31 300.39 | 31 | 1.03 | 6 | 6| 58.14</p>
<p>L8100-26 STOCKING-VENOSA | 26 251.94 | 26 | 0.87 | 11 | 13| 106.59</p>
<p>L8100-30 STOCKING-CAROLO | 1 6.80 | 1 | 0.03 | 23 | 690| 156.40</p>
<p>L8100-31 STOCKING-CAROLO | 2 13.60 | 2 | 0.07 | 22 | 330| 149.60</p>
<p>L8100-32 STOCKING-CAROLO | 0 0.00 | 0 | 0.00 | 24 | &gt;30| 163.20</p>
<p>L8100-33 ULTIMATE JOBST | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8100-34 ULTIMATE JOBST | 0 00.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8100-35 ULTIMATE JOBST | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8100-36 ULTIMATE THIGH | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8100-37 ULTIMATE THIGH | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8110-1 ELASTIC SUPP ST | 0 0.00 | 0 | 0.00 | 2 | &gt;30| 18.00</p>
<p>L8110-8 STOCKING-VENOSA | 0 0.00 | 0 | 0.00 | 24 | &gt;30| 232.56</p>
<p>L8110-9 STOCKING-VENOSA | 0 0.00 | 0 | 0.00 | 22 | &gt;30| 213.18</p>
<p>L8110-10 STOCKING-VENOSA | 2 19.38 | 2 | 0.07 | 20 | 300| 193.80</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 72 749.77 | 72 | 2.40 | 347 | | 5,446.65</p>
<p>400 F BRACES, KNEE [BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L1800-2 BRACE KNEE SPIR | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 60.40</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>---------------------------------------------------------------------------------------------------</p>
<p>PROSTHETIC INVENTORY ITEM DETAIL REPORT Run Date: DEC 15,2000@08:04:<strong>41 Page: 17 <em>(A few pages were skipped here.)</em></strong></p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L8310-13 GUARD RUPTURE R | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 82.40</p>
<p>L8330-1 SCROTAL SUPPORT | 0 0.00 | 0 | 0.00 | 11 | &gt;30| 58.74</p>
<p>L8330-2 SCROTAL SUPPORT | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 53.40</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 1 8.25 | 1 | 0.03 | 479 | | 8,932.79</p>
<p>GRAND TOTAL $ VALUE ISSUED (Used) = $ 0.00 GRAND TOTAL $ VALUE ON-HAND (Used) = $ 0.00</p>
<p>GRAND TOTAL $ VALUE ISSUED (New) = $ 2,349.02 GRAND TOTAL $ VALUE ON-HAND (New) = $ 23,012.04</p>
<p>&lt;End of Report&gt;</p></td>
</tr>
</tbody>
</table>

<span id="_Toc501807366" class="anchor"></span>Item Detail Report – Choosing “All HCPCS for NPPD Line”

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>You can select to view or print the <strong>Item Detail Report</strong> using the <strong>All HCPCS for NPPD Line</strong> criteria.</p>
<p>If you select the <strong>All HCPCS for NPPD Line</strong> criteria, a list of NPPD Groups displays. Then the NPPD Lines within the NPPD Group display unless multiple NPPD Groups were selected. You will be able to select one NPPD Line or multiple NPPD Lines for one NPPD Group.</p>
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
<p>To view or print the <strong>Item Detail Report</strong> using the <strong>All HCPCS for an NPPD Line</strong> criteria, follow these steps:</p>
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
<td>1</td>
<td>At the <strong>Choose HCPCS Selection</strong> prompt, type <strong>L</strong> for the <strong>All HCPCS for NPPD Line</strong> option, and press &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>A list of NPPD Groups displays. Type a number(s) of the NPPD Group you want to select, and press &lt;<strong>Enter</strong>&gt;.</p>
<p><strong><u>Note</u>:</strong> For multiple NPPD Groups, you can enter a list or range of numbers (e.g., 1,3,5 or 2-4,8).</p></td>
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
<td>NPPD Groups</td>
<td><p>Select one of the following:</p>
<p>A ALL HCPCS</p>
<p>G ALL HCPCS for NPPD group</p>
<p><strong>L ALL HCPCS for NPPD line</strong></p>
<p>S Select individual HCPCS</p>
<p>Choose HCPCS selection option: A// <strong>L &lt;Enter&gt;</strong> ALL HCPCS for NPPD line</p>
<p>1. WHEELCHAIRS AND ACCESSORIES</p>
<p>2. ARTIFICIAL LEGS</p>
<p>3. ARTIFICIAL ARMS AND TERMINAL DEVICES</p>
<p><strong>4. BRACES AND ORTHOTICS</strong></p>
<p>5. SHOES/ORTHOTICS</p>
<p>6. NEUROSENSORY AIDS</p>
<p>7. RESTORATIONS</p>
<p>8. OXYGEN AND RESPIRATORY</p>
<p>9. MEDICAL EQUIPMENT</p>
<p>10. ALL OTHER SUPPLIES AND EQUIPMENT</p>
<p>11. HOME DIALYSIS PROGRAM</p>
<p>12. ADAPTIVE EQUIPMENT</p>
<p>13. HISA</p>
<p>14. SURGICAL IMPLANTS</p>
<p>15. MISC</p>
<p>Select NPPD Group : (1-15): <strong>4 &lt;Enter&gt;</strong></p>
<p>NPPD Lines for Group: 400 - BRACES AND ORTHOTICS</p></td>
</tr>
</tbody>
</table>

Continued on next page

Item Detail Report – Choosing “All HCPCS for NPPD Line”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Selecting Multiple NPPD Groups</td>
<td><blockquote>
<p>If <u>one</u> NPPD Group is selected, you will be able to select multiple NPPD Lines.</p>
<p>If you select <u>multiple</u> NPPD Groups, you will <strong>NOT</strong> be able to select an NPPD Line. You will automatically be taken to the Device prompt.</p>
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
<p>To view or print the <strong>Item Detail Report</strong> using the <strong>All HCPCS for NPPD Line</strong> criteria, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                         |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                  |
| 3    | A list of NPPD Lines displays. Type one or multiple NPPD Lines, and press \<Enter\>. To enter multiple NPPD Lines, you must type a list or range of numbers (e.g., 1,3,5 or 2-4,8). |
| 4    | At the Device: Home// prompt, press \<Enter\>                                                                                                                                   |
| 5    | To view or print the report, type “;132;” at the Right Margin: 80// prompt to extend the margins for the report to display and/or print, and press \<Enter\>.               |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NPPD Lines</td>
<td><p>1. 400 A BRACE ANKLE</p>
<p>2. 400 B BRACE LEG AK</p>
<p>3. 400 C BRACE, SPINAL</p>
<p>4. 400 D BRACE AL/OTH</p>
<p>5. 400 E ELAS HOSE, EA</p>
<p>6. 400 F BRACES, KNEE</p>
<p>7. 400 G CORSET/BELT</p>
<p>Select NPPD line(s) within the above group: (1-7): <strong>5 &lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>;132;</strong> <strong>&lt;Enter&gt;</strong> TELNET VIRTUAL</p>
<p>Processing report.......</p></td>
</tr>
</tbody>
</table>

Continued on next page

Item Detail Report – Choosing “All HCPCS for NPPD Line”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report sample</td>
<td><blockquote>
<p>Below is an <strong>Item Detail Report</strong> using the <em>All HCPCS for NPPD Line</em> criteria.</p>
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
<td><p>PROSTHETIC INVENTORY ITEM DETAIL REPORT Run Date: DEC 14,2000@10:06:40 Page: 1</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>400 E ELAS HOSE, EA [BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L8100-1 ELAS SUPRT STOC | 0 0.00 | 0 | 0.00 | 22 | &gt;30| 304.32</p>
<p>L8100-2 STOCKING VENOSA | 2 19.38 | 2 | 0.07 | | 0|</p>
<p>L8100-6 FAST FIT 114 20 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-7 FAST FIT 114 21 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-8 FAST FIT 114 21 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-9 FAST FIT 114 21 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-10 FAST FIT 114 22 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-11 FAST FIT 114 22 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-12 FAST FIT 114 23 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>PROSTHETIC INVENTORY ITEM DETAIL REPORT Run Date: DEC 14,2000@10:06:40 Page: 2</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L8100-13 FAST FIT 114 23 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-14 FAST FIT 114 23 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-15 FAST FIT 114 24 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-16 FAST FIT 114 24 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-17 FAST FIT 114 24 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-18 FAST FIT 114 24 | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 149.28</p>
<p>L8100-19 FAST FIT 114 25 | 2 49.76 | 2 | 0.07 | 4 | 60| 99.52</p>
<p>L8100-20 FAST FIT 114 26 | 2 49.76 | 2 | 0.07 | 5 | 75| 124.40</p>
<p>L8100-21 ULTIMATE STOCKI | 0 0.00 | 0 | 0.00 | 2 | &gt;30| 35.00</p>
<p>L8100-22 ULTIMATE STOCKI | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 105.00</p>
<p>L8100-23 ULTIMATE STOCKI | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 105.00</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>PROSTHETIC INVENTORY ITEM DETAIL REPORT Run Date: DEC 14,2000@10:06:40 Page: 3</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L8100-24 STOCKING-VENOSA | 4 38.76 | 4 | 0.13 | 20 | 150| 193.80</p>
<p>L8100-25 STOCKING-VENOSA | 31 300.39 | 31 | 1.03 | 6 | 6| 58.14</p>
<p>L8100-26 STOCKING-VENOSA | 26 251.94 | 26 | 0.87 | 11 | 13| 106.59</p>
<p>L8100-30 STOCKING-CAROLO | 1 6.80 | 1 | 0.03 | 23 | 690| 156.40</p>
<p>L8100-31 STOCKING-CAROLO | 2 13.60 | 2 | 0.07 | 22 | 330| 149.60</p>
<p>L8100-32 STOCKING-CAROLO | 0 0.00 | 0 | 0.00 | 24 | &gt;30| 163.20</p>
<p>L8100-33 ULTIMATE JOBST | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8100-34 ULTIMATE JOBST | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8100-35 ULTIMATE JOBST | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8100-36 ULTIMATE THIGH | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>L8100-37 ULTIMATE THIGH | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 249.50</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>PROSTHETIC INVENTORY ITEM DETAIL REPORT Run Date: DEC 14,2000@10:06:40 Page: 4</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS PSAS/ITEM V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L8110-1 ELASTIC SUPP ST | 0 0.00 | 0 | 0.00 | 2 | &gt;30| 18.00</p>
<p>L8110-8 STOCKING-VENOSA | 0 0.00 | 0 | 0.00 | 24 | &gt;30| 232.56</p>
<p>L8110-9 STOCKING-VENOSA | 0 0.00 | 0 | 0.00 | 22 | &gt;30| 213.18</p>
<p>L8110-10 STOCKING-VENOSA | 2 19.38 | 2 | 0.07 | 20 | 300| 193.80</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 72 749.77 | 72 | 2.40 | 347 | | 5,446.65</p>
<p>GRAND TOTAL $ VALUE ISSUED (Used) = $ 0.00 GRAND TOTAL $ VALUE ON-HAND (Used) = $ 0.00</p>
<p>GRAND TOTAL $ VALUE ISSUED (New) = $ 749.77 GRAND TOTAL $ VALUE ON-HAND (New) = $ 5,446.65</p>
<p>&lt;End of Report&gt;</p></td>
</tr>
</tbody>
</table>

<span id="_Toc501807367" class="anchor"></span>Item Detail Report – Choosing “Select Individual HCPCS”

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>You can select to view or print the <strong>Item Detail Report</strong> using the <strong>Select</strong> <strong>Individual HCPCS</strong> criteria. This report provides the following cost information:</p>
</blockquote>
<ul>
<li><p>Grand totals for Dollar Value Issued for both USED and NEW items</p></li>
<li><p>Dollar value on hand for both USED and NEW items.</p></li>
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
<td>Steps</td>
<td><blockquote>
<p>To view or print the <strong>Item Detail Report</strong> by selecting an individual HCPCS, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                             |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                      |
| 1    | At the Choose HCPCS Selection option prompt, type S for the Select Individual HCPCS option, and press \<Enter\>.                                            |
| 2    | At the Select HCPCS 1: prompt, enter the HCPCS if you know it or enter two question marks to display a list of HCPCS and select one if you do not know the exact HCPCS. |
| 3    | More HCPCS prompts will display until you press \<Enter\> to bypass it.                                                                                                 |
| 4    | At the Device: Home// prompt, press \<Enter\>.                                                                                                                      |
| 5    | To view or print the report, type “;132;” at the Right Margin: 80// prompt to extend the margins for the report to display and/or print, and press \<Enter\>.   |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Individual HCPCS</td>
<td><p>A ALL HCPCS</p>
<p>G ALL HCPCS for NPPD group</p>
<p>L ALL HCPCS for NPPD line</p>
<p>S Select individual HCPCS</p>
<p>Choose HCPCS selection option: A// <strong>S</strong> <strong>&lt;Enter&gt;</strong> Select individual HCPCS</p>
<p>Select HCPCS 1: <strong>L0120</strong> <strong>&lt;Enter&gt;</strong> CERV FLEXIBLE NON-ADJUSTABLE</p>
<p>Select HCPCS 2: <strong>&lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>;132;</strong> <strong>&lt;Enter&gt;</strong> TELNET VIRTUAL</p>
<p>Processing report.......</p></td>
</tr>
</tbody>
</table>

Continued on next page

Item Detail Report – Choosing “Select Individual HCPCS”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Individual HCPCS</td>
<td><blockquote>
<p>Remember to change the report width size from the default standard of 80 to 132 at the <strong>Right Margin: 80//</strong> prompt. (Contact your IRM if you need instructions on how to make this change.)</p>
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
<td><p>PROSTHETIC INVENTORY ITEM DETAIL REPORT Run Date: DEC 14,2000@10:08:38 Page: 1</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>400 D BRACE AL/OTH [BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS <strong><mark>PSAS/ITEM</mark></strong> V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L0120-1 COLLAR-CERVICAL | 0 0.00 | 0 | 0.00 | 11 | &gt;30| 48.40</p>
<p>L0120-5 COLLAR-CERVICAL | 3 8.55 | 3 | 0.10 | 9 | 90| 25.65</p>
<p>L0120-6 COLLAR-CERVICAL | 1 3.70 | 1 | 0.03 | 3 | 90| 11.10</p>
<p>L0120-7 COLLAR-CERVICAL | 0 0.00 | 0 | 0.00 | 12 | &gt;30| 44.40</p>
<p>L0120-8 COLLAR-CERVICAL | 0 0.00 | 0 | 0.00 | 10 | &gt;30| 28.50</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 4 12.25 | 4 | 0.13 | 45 | | 158.05</p>
<p>GRAND TOTAL $ VALUE ISSUED (Used) = $ 0.00 GRAND TOTAL $ VALUE ON-HAND (Used) = $ 0.00</p>
<p>GRAND TOTAL $ VALUE ISSUED (New) = $ 12.25 GRAND TOTAL $ VALUE ON-HAND (New) = $ 158.05</p>
<p>&lt;End of Report&gt;</p></td>
</tr>
</tbody>
</table>

<span id="_Hlt500262683" class="anchor"></span>HCPCS Summary Report (SH)

<span id="_Toc501807369" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <strong>HCPCS Summary Report</strong> provides a quick overview of the total dollars on hand in Inventory. This report displays the stock on hand for a specified date range, and it is sorted by HCPCS. The HCPCS options for you to select when viewing or printing a report includes the following:</p>
</blockquote>
<ul>
<li><p>All HCPCS (default setting)</p></li>
<li><p>All HCPCS for an NPPD Group</p></li>
<li><p>All HCPCS for an NPPD Line (or related HCPCS)</p></li>
<li><p>Select Individual HCPCS (more than one HCPCS can be selected).</p></li>
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
<td>Steps</td>
<td><blockquote>
<p>To select the <strong>HCPCS Summary Report</strong>, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                           |
| 1    | Type SH for the HCPCS Summary Report option from the Inventory Report Menu, and press \<Enter\>. |
| 2    | At the Site prompt, press \<Enter\> to select the default site entry.                                    |
| 3    | At the Beginning Date prompt, type the beginning date of the date range, and press \<Enter\>.            |
| 4    | At the Ending Date prompt, type the end date, and press \<Enter\>.                                       |
| 5    | The options for the HCPCS Summary Report displays.                                                           |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Inventory Reports Menu</td>
<td><p>SI Item Detail Report</p>
<p><strong>SH HCPCS Summary Report</strong></p>
<blockquote>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>PC Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
</blockquote>
<p>Select Inventory Reports Option: <strong>SH</strong> &lt;<strong>Enter</strong>&gt; Stock On Hand HCPCS</p>
<p>SITE: Hines Development System// &lt;<strong>Enter</strong>&gt; 499</p>
<p>Beginning Date: <strong>9/1/00</strong> (SEP 01, 2000) &lt;<strong>Enter</strong>&gt;</p>
<p>Ending Date: <strong>9/30/00</strong> (SEP 30, 2000) &lt;<strong>Enter</strong>&gt;</p>
<p>Select one of the following:</p>
<p>A ALL HCPCS</p>
<p>G ALL HCPCS for NPPD group</p>
<p>L ALL HCPCS for NPPD line</p>
<p>S Select individual HCPCS</p></td>
</tr>
</tbody>
</table>

<span id="_Toc501807370" class="anchor"></span>HCPCS Summary Report – Choosing “All HCPCS”

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report right margins</td>
<td><blockquote>
<p>The <strong>All HCPCS</strong> option on the <strong>HCPCS Summary Report</strong> must be printed using an extended right margin format of 132-width size instead of the standard 80-width default size. (See your IRM department for detailed instructions.)</p>
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
<p>To select the <strong>All HCPCS</strong> option of the <strong>HCPCS Summary Report</strong>, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                   |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                            |
| 1    | At the Choose HCPCS Selection option prompt, type A for the All HCPCS option, and press \<Enter\>.                                                |
| 2    | At the Device: Home// prompt, press \<Enter\>.                                                                                                            |
| 3    | To print the report, type “;132;” at the Right Margin: 80// prompt to extend the margins for the report to display and/or print, and press \<Enter\>. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Summary Report Options</td>
<td><p>Select one of the following:</p>
<p><strong>A ALL HCPCS</strong></p>
<p>G ALL HCPCS for NPPD group</p>
<p>L ALL HCPCS for NPPD line</p>
<p>S Select individual HCPCS</p>
<p>Choose HCPCS selection option: A// &lt;<strong>Enter</strong>&gt; ALL HCPCS</p>
<p>DEVICE: HOME// <strong>;132;</strong> &lt;<strong>Enter</strong>&gt; TELNET VIRTUAL</p>
<blockquote>
<p>Processing report.......</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

HCPCS Summary Report – Choosing “All HCPCS”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Description field</td>
<td><blockquote>
<p>Notice that this <strong>HCPCS Summary Report</strong> provides a <strong>DESCRIPTION</strong> field in the second column instead of a <strong>PSAS/Item</strong> field as in the <strong>Item Detail Report</strong>.</p>
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
<td><p>PROSTHETIC INVENTORY HCPCS SUMMARY REPORT Run Date: DEC 14,2000@10:10:16 Page: 1</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>100 B MANUAL CUSTOM [ WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS <strong><mark>DESCRIPTION</mark></strong> V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>K0004 HIGH STREN(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>K0004 HIGH STREN(New) | 10 3,294.09 | 10 | 0.33 | 5 | 15| 1,856.81</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 10 3,294.09 | 10 | 0.33 | 5 | | 1,856.81</p>
<p>100 C STANDARD [ WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS DESCRIPTION V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>K0001 STANDARD W(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>K0001 STANDARD W(New) | 5 576.25 | 5 | 0.17 | 3 | 18| 387.30</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 5 576.25 | 5 | 0.17 | 3 | | 387.30</p>
<p>100 D ACCESSORIES [ WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS DESCRIPTION V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>DL175 GLOVES, WH(Used) 0 0.00| | 0 | 0.00 | 24 | &gt;30| 0.00</p>
<p>DL175 GLOVES, WH(New) | 16 112.00 | 16 | 0.53 | 41 | 77| 287.00</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>PROSTHETIC INVENTORY HCPCS SUMMARY REPORT Run Date: DEC 14,2000@10:10:16 Page: 3</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS DESCRIPTION V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>DL177 COVERS(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>DL177 COVERS(New) | 0 0.00 | 0 | 0.00 | 23 | &gt;30| 715.29</p>
<p>E0978 WHEELCHAIR(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>E0978 WHEELCHAIR(New) | 0 0.00 | 0 | 0.00 | 5 | &gt;30| 154.25</p>
<p>K0019 ARM PAD EA(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>K0019 ARM PAD EA(New) | 0 0.00 | 0 | 0.00 | 6 | &gt;30| 30.00</p>
<p>K0020 FIXED ADJU(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>K0020 FIXED ADJU(New) | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 19.80</p>
<p>K0045 FOOTREST C(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>K0045 FOOTREST C(New) | 0 0.00 | 0 | 0.00 | 8 | &gt;30| 80.00</p>
<p>K0098 DRIVE BELT(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>K0098 DRIVE BELT(New) | 0 0.00 | 0 | 0.00 | 4 | &gt;30| 86.40</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 24 | | 0.00</p>
<p>(New) | 16 112.00 | 16 | 0.53 | 91 | | 1,372.74</p>
<p>100 E CUSHION FOAM [ WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS DESCRIPTION V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>E0963 WHEELCHAIR(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>E0963 WHEELCHAIR(New) | 2 15.75 | 2 | 0.07 | 4 | 60| 31.50</p>
<p>E0964 WHEELCHAIR(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>E0964 WHEELCHAIR(New) | 9 82.71 | 9 | 0.30 | 9 | 30| 82.71</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 11 98.46 | 11 | 0.37 | 13 | | 114.21</p></td>
</tr>
</tbody>
</table>

(Report screen sample continued on next page)

Continued on next page

HCPCS Summary Report – Choosing “All HCPCS”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sample Screen (continued)</td>
<td><blockquote>
<p>The <strong>HCPCS Summary Report</strong> using the “All HCPCS” option continues as follows:</p>
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
<td><p>100 F CUSHION SPEC [ WHEELCHAIRS AND ACCESSORIES ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS <mark>DESCRIPTION</mark> V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>E0176 AIR PRESSR(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>E0176 AIR PRESSR(New) | 6 1,087.77 | 6 | 0.20 | 23 | 115| 3,487.74</p>
<p>E0178 GEL PRESSR(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>E0178 GEL PRESSR(New) | 3 607.38 | 3 | 0.10 | 10 | 100| 2,014.32</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 9 1,695.15 | 9 | 0.30 | 33 | | 5,502.06</p>
<p>400 A BRACE ANKLE [ BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS DESCRIPTION V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L1902 AFO ANKLE (Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>L1902 AFO ANKLE (New) | 5 17.80 | 5 | 0.17 | 23 | 138| 301.12</p>
<p>L1930 AFO PLASTI(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>L1930 AFO PLASTI(New) | 3 59.79 | 3 | 0.10 | 34 | 340| 675.76</p>
<p>L4392 REPLACE AN(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>L4392 REPLACE AN(New) | 1 4.50 | 1 | 0.03 | 20 | 600| 225.00</p>
<p>L4396 ANKLE CONT(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>L4396 ANKLE CONT(New) | 3 135.00 | 3 | 0.10 | 50 | 500| 2,250.00</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 12 217.09 | 12 | 0.40 | 127 | | 3,451.88</p>
<p>400 D BRACE AL/OTH [ BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS DESCRIPTION V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>E1810 ADJUST KNE(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>E1810 ADJUST KNE(New) | 0 0.00 | 0 | 0.00 | 1 | &gt;30| 0.00</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>GRAND TOTAL $ VALUE ISSUED (Used) = $ 483.75 GRAND TOTAL $ VALUE ON-HAND (Used) = $ 2,276.54</p>
<p>GRAND TOTAL $ VALUE ISSUED (New) = $ 26,150.77 GRAND TOTAL $ VALUE ON-HAND (New) = $ 97,626.06</p></td>
</tr>
</tbody>
</table>

<span id="_Toc501807371" class="anchor"></span>HCPCS Summary Report – Choosing “All HCPCS for NPPD Group”

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <strong>All HCPCS for NPPD Group</strong> option on the <strong>HCPCS Summary Report</strong> displays all the HCPCS usage for an NPPD Group. This report must be printed using an extended right margin format of 132-width size instead of the standard 80-width default size.</p>
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
<p>To view or print the <strong>HCPCS Summary Report</strong> for using the <strong>All HCPCS for NPPD Group</strong> option, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                   |
| 1    | At the Choose HCPCS Selection prompt, type G for the All HCPCS for NPPD Group option, and press \<Enter\>.                                                                               |
| 2    | A list of NPPD Groups displays. Type a number of the NPPD Group you want to select, and press \<Enter\>. Note: You can select multiple groups, by typing a list or range (e.g., 1,3,5 or 2-4,8). |
| 3    | At the Device: Home// prompt, press \<Enter\>                                                                                                                                                    |
| 4    | To display or print the report, type “;132;” at the Right Margin: 80// prompt to extend the margins for the report to display and/or print, and press \<Enter\>.                             |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>All HCPCS for NPPD Group</td>
<td><p>Select one of the following:</p>
<p>A ALL HCPCS</p>
<p><strong>G ALL HCPCS for NPPD group</strong></p>
<p>L ALL HCPCS for NPPD line</p>
<p>S Select individual HCPCS</p>
<p>Choose HCPCS selection option: A// <strong>G</strong> &lt;<strong>Enter</strong>&gt; ALL HCPCS for NPPD group</p>
<p>1. WHEELCHAIRS AND ACCESSORIES</p>
<p>2. ARTIFICIAL LEGS</p>
<p>3. ARTIFICIAL ARMS AND TERMINAL DEVICES</p>
<p><strong>4. BRACES AND ORTHOTICS</strong></p>
<p>5. SHOES/ORTHOTICS</p>
<p>6. NEUROSENSORY AIDS</p>
<p>7. RESTORATIONS</p>
<p>8. OXYGEN AND RESPIRATORY</p>
<p>9. MEDICAL EQUIPMENT</p>
<p>10. ALL OTHER SUPPLIES AND EQUIPMENT</p>
<p>11. HOME DIALYSIS PROGRAM</p>
<p>12. ADAPTIVE EQUIPMENT</p>
<p>13. HISA</p>
<p>14. SURGICAL IMPLANTS</p>
<p>15. MISC</p>
<p>Select NPPD Group : (1-15): <strong>4 &lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>;132;</strong> &lt;<strong>Enter</strong>&gt; TELNET VIRTUAL</p>
<p>Processing report.......</p></td>
</tr>
</tbody>
</table>

Continued on next page

HCPCS Summary Report – Choosing “All HCPCS for NPPD Group”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Description field</td>
<td><blockquote>
<p>Again, notice that this <strong>HCPCS Summary Report</strong> provides a <strong>DESCRIPTION</strong> field in the second column instead of a <strong>PSAS/Item</strong> field as in the <strong>Item Detail Report</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

PROSTHETIC INVENTORY HCPCS SUMMARY REPORT Run Date: DEC 14,2000@10:15:30 Page: 1

STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 \[ 30 calendar days \]

400 A BRACE ANKLE \[ BRACES AND ORTHOTICS \]

---------------------------------------------------------------------------------------------------------------------------------HCPCS DESCRIPTION V.A.(Used) Total\| COM. (New) Total\| Total \|Days Ave \| Stock On-Hand\| Days \|Total \$ Value On-HandIssue \$ Value\| Issue \$ Value\| Issue \|Usage Rate\| Used New \| On-Hand\| Used New---------------------------------------------------------------------------------------------------------------------------------

L1902 AFO ANKLE (Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L1902 AFO ANKLE (New) \| 5 17.80 \| 5 \| 0.17 \| 23 \| 138\| 301.12

L1930 AFO PLASTI(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L1930 AFO PLASTI(New) \| 3 59.79 \| 3 \| 0.10 \| 34 \| 340\| 675.76

L4392 REPLACE AN(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L4392 REPLACE AN(New) \| 1 4.50 \| 1 \| 0.03 \| 20 \| 600\| 225.00

L4396 ANKLE CONT(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L4396 ANKLE CONT(New) \| 3 135.00 \| 3 \| 0.10 \| 50 \| 500\| 2,250.00

================================================================================================================================

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 12 217.09 \| 12 \| 0.40 \| 127 \| \| 3,451.88

400 D BRACE AL/OTH \[ BRACES AND ORTHOTICS \]

--------------------------------------------------------------------------------------------------------------------------------

HCPCS DESCRIPTION V.A.(Used) Total\| COM. (New) Total\| Total \|Days Ave \| Stock On-Hand\| Days \|Total \$ Value On-Hand

Issue \$ Value\| Issue \$ Value\| Issue \|Usage Rate\| Used New \| On-Hand\| Used New

--------------------------------------------------------------------------------------------------------------------------------

E1810 ADJUST KNE(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

E1810 ADJUST KNE(New) \| 0 0.00 \| 0 \| 0.00 \| 1 \| \>30\| 0.00

L0120 CERV FLEXI(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L0120 CERV FLEXI(New) \| 4 12.25 \| 4 \| 0.13 \| 45 \| 338\| 158.05

L2270 VARUS/VALG(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L2270 VARUS/VALG(New) \| 0 0.00 \| 0 \| 0.00 \| 3 \| \>30\| 43.92

L3670 ACROMIO/CL(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L3670 ACROMIO/CL(New) \| 0 0.00 \| 0 \| 0.00 \| 6 \| \>30\| 28.02

L3700 ELBOW ORTH(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L3700 ELBOW ORTH(New) \| 4 39.80 \| 4 \| 0.13 \| 8 \| 60\| 79.60

L3907 WHFO WRST (Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L3907 WHFO WRST (New) \| 1 15.75 \| 1 \| 0.03 \| 19 \| 570\| 299.25

L3908 WRIST COCK(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L3908 WRIST COCK(New) \| 31 147.06 \| 31 \| 1.03 \| 103 \| 100\| 460.53

L4350 PNEUMATIC (Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L4350 PNEUMATIC (New) \| 2 49.00 \| 2 \| 0.07 \| 1 \| 15\| 24.50

L4360 PNEUMATIC (Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L4360 PNEUMATIC (New) \| 15 955.00 \| 15 \| 0.50 \| 56 \| 112\| 2,520.00

================================================================================================================================

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 57 1,218.86 \| 57 \| 1.90 \| 242 \| \| 3,613.87

400 E ELAS HOSE, EA \[ BRACES AND ORTHOTICS \]

-------------------------------------------------------------------------------------------------------------------------------

HCPCS DESCRIPTION V.A.(Used) Total\| COM. (New) Total\| Total \|Days Ave \| Stock On-Hand\| Days \|Total \$ Value On-Hand

Issue \$ Value\| Issue \$ Value\| Issue \|Usage Rate\| Used New \| On-Hand\| Used New

--------------------------------------------------------------------------------------------------------------------------------

L8100 ELAS SUPRT(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L8100 ELAS SUPRT(New) \| 70 730.39 \| 70 \| 2.33 \| 279 \| 120\| 4,789.11

L8110 ELASTIC SU(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L8110 ELASTIC SU(New) \| 2 19.38 \| 2 \| 0.07 \| 68 \| \>999\| 657.54

================================================================================================================================

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 72 749.77 \| 72 \| 2.40 \| 347 \| \| 5,446.65

400 F BRACES, KNEE \[ BRACES AND ORTHOTICS \]

--------------------------------------------------------------------------------------------------------------------------------

HCPCS DESCRIPTION V.A.(Used) Total\| COM. (New) Total\| Total \|Days Ave \| Stock On-Hand\| Days \|Total \$ Value On-Hand

Issue \$ Value\| Issue \$ Value\| Issue \|Usage Rate\| Used New \| On-Hand\| Used New

--------------------------------------------------------------------------------------------------------------------------------

L1800 KNEE ORTHO(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L1800 KNEE ORTHO(New) \| 0 0.00 \| 0 \| 0.00 \| 27 \| \>30\| 414.60

---------------------------------------------------------------------------------------

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 1 8.25 \| 1 \| 0.03 \| 479 \| \| 8,932.79

GRAND TOTAL \$ VALUE ISSUED (Used) = \$ 0.00 GRAND TOTAL \$ VALUE ON-HAND (Used) = \$ 0.00

GRAND TOTAL \$ VALUE ISSUED (New) = \$ 2,349.02 GRAND TOTAL \$ VALUE ON-HAND (New) = \$ 23,012.04

<span id="_Toc501807372" class="anchor"></span>HCPCS Summary Report – Choosing “All HCPCS for NPPD Line”

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>You can select to view or print the <strong>HCPCS Summary Report</strong> using the <strong>All HCPCS for NPPD Line</strong> criteria.</p>
<p>If you select the <strong>All HCPCS for NPPD Line</strong> criteria, you will first select an NPPD Group, and then select a Line(s) within the Group unless <u>multiple</u> NPPD Groups were selected. You will be able to select one NPPD Line or multiple NPPD Lines for one NPPD Group.</p>
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
<p>To view or print the <strong>HCPCS Summary Report</strong> for <strong>All HCPCS for an NPPD Line</strong>, follow these steps:</p>
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
<td>1</td>
<td>At the <strong>Choose HCPCS Selection</strong> prompt, type <strong>L</strong> for the <strong>All HCPCS for NPPD Line</strong> option, and press &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>A list of NPPD Groups displays. Type a number(s) of the NPPD Group you want to select, and press &lt;<strong>Enter</strong>&gt;.</p>
<p><strong><u>Note</u>:</strong> For <u>multiple</u> NPPD Groups, you can enter a list or range of numbers (e.g., 1,3,5 or 2-4,8).</p></td>
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
<td>All HCPCS for NPPD Line</td>
<td><p>Select one of the following:</p>
<p>A ALL HCPCS</p>
<p>G ALL HCPCS for NPPD group</p>
<p><strong>L ALL HCPCS for NPPD line</strong></p>
<p>S Select individual HCPCS</p>
<p>Choose HCPCS selection option: A// <strong>L</strong> &lt;<strong>Enter</strong>&gt; ALL HCPCS for NPPD line</p>
<p>1. WHEELCHAIRS AND ACCESSORIES</p>
<p>2. ARTIFICIAL LEGS</p>
<p>3. ARTIFICIAL ARMS AND TERMINAL DEVICES</p>
<p><strong>4. BRACES AND ORTHOTICS</strong></p>
<p>5. SHOES/ORTHOTICS</p>
<p>6. NEUROSENSORY AIDS</p>
<p>7. RESTORATIONS</p>
<p>8. OXYGEN AND RESPIRATORY</p>
<p>9. MEDICAL EQUIPMENT</p>
<p>10. ALL OTHER SUPPLIES AND EQUIPMENT</p>
<p>11. HOME DIALYSIS PROGRAM</p>
<p>12. ADAPTIVE EQUIPMENT</p>
<p>13. HISA</p>
<p>14. SURGICAL IMPLANTS</p>
<p>15. MISC</p>
<p>Select NPPD Group: (1-15): <strong>4</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>NPPD Lines for Group: 100 - WHEELCHAIRS AND ACCESSORIES</p></td>
</tr>
</tbody>
</table>

Continued on next page

HCPCS Summary Report – Choosing “All HCPCS for NPPD Line”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Selecting Multiple NPPD Groups</td>
<td><blockquote>
<p>If <u>one</u> NPPD Group is selected, you will be able to select multiple NPPD Lines. If you select <u>multiple</u> NPPD Groups, you will <strong>NOT</strong> be able to select an NPPD Line. You will be automatically taken to the Device prompt.</p>
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
<p>To view or print the <strong>HCPCS Summary Report</strong> using the <strong>All HCPCS for NPPD Line</strong> option, follow these steps:</p>
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
<td>3</td>
<td><p>A list of NPPD Lines displays. Type one or multiple NPPD Lines, and press &lt;<strong>Enter</strong>&gt;.</p>
<p><strong><u>Note</u>:</strong> To enter multiple NPPD Lines, you must type a list or range of numbers (e.g., 1,3,5 or 2-4,8).</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>At the <strong>Device: Home//</strong> prompt, press &lt;<strong>Enter</strong>&gt;</td>
</tr>
<tr class="even">
<td>5</td>
<td>To view or print the report, type <strong>“;132;”</strong> at the <strong>Right Margin: 80//</strong> prompt to extend the margins for the report to display and/or print, and press &lt;<strong>Enter</strong>&gt;.</td>
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
<td>NPPD Lines</td>
<td><p>1. 400 A BRACE ANKLE</p>
<p>2. 400 B BRACE LEG AK</p>
<p>3. 400 C BRACE, SPINAL</p>
<p>4. 400 D BRACE AL/OTH</p>
<p><strong>5. 400 E ELAS HOSE, EA</strong></p>
<p>6. 400 F BRACES, KNEE</p>
<p>7. 400 G CORSET/BELT</p>
<p>Select NPPD line(s) within the above group: (1-7): <strong>5 &lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>;132;</strong> <strong>&lt;Enter&gt;</strong> TELNET VIRTUAL</p>
<p>Processing report.......</p></td>
</tr>
</tbody>
</table>

Continued on next page

HCPCS Summary Report – Choosing “All HCPCS for NPPD Line”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report sample</td>
<td><blockquote>
<p>Below is a sample Prosthetic Inventory HCPCS Summary Report.</p>
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
<td><p>PROSTHETIC INVENTORY HCPCS SUMMARY REPORT Run Date: DEC 14,2000@10:16:59 Page: 1</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p>400 E ELAS HOSE, EA [ BRACES AND ORTHOTICS ]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>HCPCS DESCRIPTION V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>L8100 ELAS SUPRT(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>L8100 ELAS SUPRT(New) | 70 730.39 | 70 | 2.33 | 279 | 120| 4,789.11</p>
<p>L8110 ELASTIC SU(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>L8110 ELASTIC SU(New) | 2 19.38 | 2 | 0.07 | 68 | &gt;999| 657.54</p>
<p>================================================================================================================================</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 72 749.77 | 72 | 2.40 | 347 | | 5,446.65</p>
<p>GRAND TOTAL $ VALUE ISSUED (Used) = $ 0.00 GRAND TOTAL $ VALUE ON-HAND (Used) = $ 0.00</p>
<p>GRAND TOTAL $ VALUE ISSUED (New) = $ 749.77 GRAND TOTAL $ VALUE ON-HAND (New) = $ 5,446.65</p>
<p>&lt;End of Report&gt;</p>
<p>-----------------------------------------------------------------------------------------</p></td>
</tr>
</tbody>
</table>

<span id="_Toc501807373" class="anchor"></span>HCPCS Summary Report – Choosing “Select Individual HCPCS”

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>You can choose the <strong>Select Individual HCPCS</strong> criteria option to produce the <strong>HCPCS Summary Report</strong>. You can select one or multiple HCPCS to be displayed on this report.</p>
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
<p>To view or print the <strong>HCPCS Summary Report</strong> by selecting an Individual HCPCS, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                   |
|------|-------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                            |
| 1    | Type SH for the HCPCS Summary Report option from the Inventory Reports Menu, and press \<Enter\>. |
| 2    | At the Site prompt, press \<Enter\> to select the default site entry.                                     |
| 3    | At the Beginning Date prompt, type the beginning date of the date range, and press \<Enter\>.             |
| 4    | At the Ending Date prompt, type the end date, and press \<Enter\>.                                        |
| 5    | The four criteria options to view or print the HCPCS Summary Report displays.                                 |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Stock On Hand HCPCS Option</td>
<td><p>SI Item Detail Report</p>
<p><strong>SH HCPCS Summary Report</strong></p>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<blockquote>
<p>PC Print Items Not Issued Within 30-Day</p>
</blockquote>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
<p>Select Inventory Reports Option: <strong>SH</strong> &lt;<strong>Enter</strong>&gt; HCPCS Summary Report</p>
<p>SITE: Hines Development System// &lt;<strong>Enter</strong>&gt; 499</p>
<p>Beginning Date: 9/1/00 &lt;<strong>Enter</strong>&gt; (SEP 01, 2000)</p>
<p>Ending Date: 9/30/00 &lt;<strong>Enter</strong>&gt; (SEP 30, 2000)</p>
<p>Select one of the following:</p>
<p>A ALL HCPCS</p>
<p>G ALL HCPCS for NPPD group</p>
<p>L ALL HCPCS for NPPD line</p>
<p>S Select individual HCPCS</p></td>
</tr>
</tbody>
</table>

Continued on next page

HCPCS Summary Report – Choosing “Select Individual HCPCS”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Individual HCPCS</td>
<td><blockquote>
<p>The <strong>HCPCS Summary Report</strong> works exactly like the <strong>Item Detail Report</strong> with the only exception that the display will report usage by HCPCS instead of an Item.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                           |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                    |
| 1    | At the Choose HCPCS Selection option prompt, type S for the Select Individual HCPCS criteria option, and press \<Enter\>.                                 |
| 2    | At the Select HCPCS 1: prompt, enter two question marks to display a list of HCPCS and select one if you do not know the exact HCPCS.                                 |
| 3    | More HCPCS prompts will display until you press \<Enter\> to bypass it.                                                                                               |
| 4    | At the Device: Home// prompt, press \<Enter\>.                                                                                                                    |
| 5    | To view or print the report, type “;132;” at the Right Margin: 80// prompt to extend the margins for the report to display and/or print, and press \<Enter\>. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Selection List</td>
<td><p>Choose HCPCS selection option: A// <strong>S</strong> &lt;<strong>Enter</strong>&gt; <strong>Select Individual HCPCS</strong></p>
<p>Select HCPCS 1: <strong>??</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>Choose from:</p>
<p>A4254 BATTERY FOR GLUCOSE MONITOR</p>
<p>A4259 LANCETS PER BOX</p>
<p>A4402 LUBRICANT PER OUNCE</p>
<p>A4404 OSTOMY RING EACH</p>
<p>A4565 SLINGS</p>
<p>DL175 GLOVES, WHEELCHAIR</p>
<p>E0100 CANE ADJUST/FIXED WITH TIP</p>
<p>E0142 WALKER RIGID WHEELED WITH SE</p>
<p>E0143 WALKER FOLDING WHEELED W/O S</p>
<p>E1399 DURABLE MEDICAL EQUIPMENT MI</p>
<p>K0001 STANDARD WHEELCHAIR</p>
<p><strong>L0120 CERV FLEXIBLE NON-ADJUSTABLE</strong></p>
<p>L5000 SHO INSERT W ARCH TOE FILLER</p>
<p>L5020 TIBIAL TUBERCLE HGT W/ TOE F</p>
<p>L5050 ANK SYMES MOLD SCKT SACH FT</p>
<p>L5060 SYMES MET FR LEATH SOCKET AR</p>
<p>L7499 UPPER EXTREMITY PROSTH, NOS  inactive HCPCS </p>
<p>L7499 UPPER EXTREMITY PROSTH, NOS</p>
<p>UNKNOWN UNKNOWN HCPCS</p>
<p>Select HCPCS 1: <strong>L0120</strong> <strong>&lt;Enter&gt;</strong> CERV FLEXIBLE NON-ADJUSTABLE</p>
<p>Select HCPCS 2: <strong>&lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>;132;</strong> <strong>&lt;Enter&gt;</strong> TELNET VIRTUAL</p>
<p>Processing report.......</p></td>
</tr>
</tbody>
</table>

Continued on next page

HCPCS Summary Report – Choosing “Select Individual HCPCS”, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report Sample</td>
<td><blockquote>
<p>Below is the <strong>Prosthetics Inventory</strong> <strong>HCPCS Summary Report</strong> using the <strong>Select Individual HCPCS</strong> criteria. Usage is reported by HCPCS code on this report. Note the first column: HCPCS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

PROSTHETIC INVENTORY HCPCS SUMMARY REPORT Run Date: DEC 14,2000@10:18:07 Page: 1

STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 \[ 30 calendar days \]

400 D BRACE AL/OTH \[ BRACES AND ORTHOTICS \]

---------------------------------------------------------------------------------------------------------------------------------HCPCS DESCRIPTION V.A.(Used) Total\| COM. (New) Total\| Total \|Days Ave \| Stock On-Hand\| Days \|Total \$ Value On-HandIssue \$ Value\| Issue \$ Value\| Issue \|Usage Rate\| Used New \| On-Hand\| Used New---------------------------------------------------------------------------------------------------------------------------------

L0120 CERV FLEXI(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

L0120 CERV FLEXI(New) \| 4 12.25 \| 4 \| 0.13 \| 45 \| 338\| 158.05

================================================================================================================================

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 4 12.25 \| 4 \| 0.13 \| 45 \| \| 158.05

GRAND TOTAL \$ VALUE ISSUED (Used) = \$ 0.00 GRAND TOTAL \$ VALUE ON-HAND (Used) = \$ 0.00

GRAND TOTAL \$ VALUE ISSUED (New) = \$ 12.25 GRAND TOTAL \$ VALUE ON-HAND (New) = \$ 158.05

\<End of Report\>

<span id="_Hlt500262688" class="anchor"></span>NPPD Group/Line Report (SG)

<span id="_Toc501807375" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>NPPD Group/Line</strong> <strong>Report</strong> option will display the same information as the <strong>Item Detail Report</strong> and the <strong>HCPCS Summary Report</strong> options but at the NPPD Line level. It displays the stock on hand for a date range and sorted by NPPD Group and NPPD Line.</p>
<p>You will select a site and a date range. You will be able to select one or multiple NPPD Groups. Then an NPPD Line selection must be made <strong><u>ONLY</u></strong> if one NPPD Group is selected.</p>
<p>A couple of conditions exist depending on which prompt you choose as follows:</p>
</blockquote>
<ul>
<li><p>If you choose <u>one</u> NPPD Group, you will be able to select multiple NPPD Lines.</p></li>
<li><p>If you choose <u>more</u> than one NPPD Group, an NPPD Line cannot be selected.</p></li>
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
<td>Steps</td>
<td><blockquote>
<p>To select the <strong>NPPD Group/Line Report</strong>, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                |
| 1    | Type SG for the NPPD Group/LineReport, and press \<Enter\>.                          |
| 2    | At the Site prompt, press \<Enter\> to select the default site entry.                         |
| 3    | At the Beginning Date prompt, type the beginning date of the date range, and press \<Enter\>. |
| 4    | At the Ending Date prompt, type the end date, and press \<Enter\>.                            |
| 5    | The NPPD Groups display.                                                                          |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Inventory Reports Menu</td>
<td><p>SI Item Detail Report</p>
<p>SH HCPCS Summary Report</p>
<p><strong>SG NPPD Group/Line Report</strong></p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>PC Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
<p>Select Inventory Reports Option: <strong>SG</strong> NPPD Group/Line Report</p>
<p>SITE: Hines Development System// &lt;<strong>Enter</strong>&gt; 499</p>
<p>Beginning Date: 9/1/00 (SEP 01, 2000) &lt;<strong>Enter</strong>&gt;</p>
<p>Ending Date: 9/30/00 (SEP 30, 2000) &lt;<strong>Enter</strong>&gt;</p></td>
</tr>
</tbody>
</table>

<span id="_Toc501807376" class="anchor"></span>NPPD Group/Line Report - Select a Single NPPD Group

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Single NPPD Group</td>
<td><blockquote>
<p>You can select a single NPPD Group. When the NPPD Lines display, you will have the option of selecting <u>one</u> or <u>multiple</u> NPPD Lines.</p>
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
<td>1</td>
<td>After the NPPD Groups display, a <strong>Select NPPD Group</strong> prompt displays.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Type the number of the NPPD Group you want to select.</td>
</tr>
<tr class="even">
<td>3</td>
<td><p>A list of NPPD Lines displays for the Group you selected. You can select a single or multiple NPPD Lines.</p>
<p><strong><u>Note</u>:</strong> To enter multiple NPPD Lines, you must type a single number or range of numbers (e.g., 1,3,5 or 2-4,8).</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>At the <strong>Device: Home//</strong> prompt, press &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="even">
<td>5</td>
<td>To view or print the report, type <strong>“;132;”</strong> at the <strong>Right Margin: 80//</strong> prompt to extend the margins for the report to display and/or print, and press &lt;<strong>Enter</strong>&gt;.</td>
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
<td>NPPD Groups and NPPD Lines Selection screen</td>
<td><p>1. WHEELCHAIRS AND ACCESSORIES</p>
<p>2. ARTIFICIAL LEGS</p>
<p>3. ARTIFICIAL ARMS AND TERMINAL DEVICES</p>
<p>4. BRACES AND ORTHOTICS</p>
<p>5. SHOES/ORTHOTICS</p>
<p>6. NEUROSENSORY AIDS</p>
<p>7. RESTORATIONS</p>
<p>8. OXYGEN AND RESPIRATORY</p>
<p>9. MEDICAL EQUIPMENT</p>
<p>10. ALL OTHER SUPPLIES AND EQUIPMENT</p>
<p>11. HOME DIALYSIS PROGRAM</p>
<p>12. ADAPTIVE EQUIPMENT</p>
<p>13. HISA</p>
<p>14. SURGICAL IMPLANTS</p>
<p>15. MISC</p>
<p>Select NPPD Group: (1-15): <strong>4 &lt;Enter&gt;</strong></p>
<p>NPPD Lines for Group: 400 - BRACES AND ORTHOTICS <strong>&lt;Enter&gt;</strong></p>
<p>1. 400 A BRACE ANKLE</p>
<p>2. 400 B BRACE LEG AK</p>
<p>3. 400 C BRACE, SPINAL</p>
<p>4. 400 D BRACE AL/OTH</p>
<p>5. 400 E ELAS HOSE, EA</p>
<p>6. 400 F BRACES, KNEE</p>
<p>7. 400 G CORSET/BELT</p>
<p>Select NPPD line(s) within the above group: (1-7): <strong>5</strong> &lt;<strong>Enter</strong>&gt;</p>
<p>DEVICE: HOME// <strong>;132;</strong> &lt;<strong>Enter</strong>&gt; TELNET VIRTUAL</p>
<p>Processing report.......</p></td>
</tr>
</tbody>
</table>

Continued on next page

NPPD Group/Line Report - Select a Single NPPD Group, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report Sample</td>
<td><blockquote>
<p>Below is the <strong>NPPD Group/Line Report</strong>. This report was obtained by selecting a <u>single</u> NPPD Group.</p>
</blockquote></td>
</tr>
</tbody>
</table>

PROSTHETIC INVENTORY NPPD GROUP/LINE REPORT Run Date: DEC 14,2000@10:19:38 Page: 1

STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 \[ 30 calendar days \]

BRACES AND ORTHOTICS

---------------------------------------------------------------------------------------------------------------------------------

NPPD LINE V.A.(Used) Total\| COM. (New) Total\| Total \|Days Ave \| Stock On-Hand\| Days \|Total \$ Value On-Hand

Issue \$ Value\| Issue \$ Value\| Issue \|Usage Rate\| Used New \| On-Hand\| Used New

--------------------------------------------------------------------------------------------------------------------------------

400 E ELAS HOSE, EA

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 72 749.77 \| 72 \| 2.40 \| 347 \| 145\| 5,446.65

================================================================================================================================

0 0.00\| 72 749.77 \| 72 \| \| 0 347 \| \| 0.00 5,446.65

GRAND TOTAL \$ VALUE ISSUED (Used) = \$ 0.00 GRAND TOTAL \$ VALUE ON-HAND (Used) = \$ 0.00

GRAND TOTAL \$ VALUE ISSUED (New) = \$ 749.77 GRAND TOTAL \$ VALUE ON-HAND (New) = \$ 5,446.65

\<End of Report\>

<span id="_Toc501807377" class="anchor"></span>NPPD Group/Line Report - Select Multiple NPPD Groups

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Single NPPD Group</td>
<td><blockquote>
<p>You can select a <em><strong>single</strong></em> NPPD Group to display on the <strong>NPPD Group/Line Report</strong>. When the NPPD Lines display, you will have the option of selecting <u>one</u> or <u>multiple</u> NPPD Lines.</p>
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
<td>1</td>
<td>After the NPPD Groups display, a Select NPPD Group prompt displays.</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>Type the number of the NPPD Groups you want to select. You can select <u>multiple</u> NPPD Groups.</p>
<p><strong><u>Note</u>:</strong> To enter multiple NPPD Groups, you must type a list or range of numbers (e.g., 1,3,5 or 2-4,8).</p></td>
</tr>
<tr class="even">
<td>3</td>
<td><p>A list of NPPD Lines displays. You can select a <u>single</u> NPPD Line or <u>multiple</u> NPPD Lines.</p>
<p><strong><u>Note</u>:</strong> To enter multiple NPPD Lines, you must type a list or range of numbers (e.g., 1,3,5 or 2-4,8).</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>At the <strong>Device: Home//</strong> prompt, press &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="even">
<td>5</td>
<td>To view or print the report, type <strong>“;132;”</strong> at the <strong>Right Margin: 80//</strong> prompt to extend the margins for the report to display and/or print, and press &lt;<strong>Enter</strong>&gt;.</td>
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
<td>NPPD Groups and NPPD Lines selection screen</td>
<td><blockquote>
<p>1. WHEELCHAIRS AND ACCESSORIES</p>
<p>2. ARTIFICIAL LEGS</p>
<p>3. ARTIFICIAL ARMS AND TERMINAL DEVICES</p>
<p>4. BRACES AND ORTHOTICS</p>
<p>5. SHOES/ORTHOTICS</p>
<p>6. NEUROSENSORY AIDS</p>
<p>7. RESTORATIONS</p>
<p>8. OXYGEN AND RESPIRATORY</p>
<p>9. MEDICAL EQUIPMENT</p>
<p>10. ALL OTHER SUPPLIES AND EQUIPMENT</p>
<p>11. HOME DIALYSIS PROGRAM</p>
<p>12. ADAPTIVE EQUIPMENT</p>
<p>13. HISA</p>
<p>14. SURGICAL IMPLANTS</p>
<p>15. MISC</p>
<p>Select NPPD Group: (1-15): <strong>4,9 &lt;Enter&gt;</strong></p>
<p>DEVICE: HOME// <strong>;132;</strong> <strong>&lt;Enter&gt;</strong> TELNET VIRTUAL</p>
<p>Processing report.......</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

NPPD Group/Line Report - Select Multiple NPPD Groups, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report sample</td>
<td><blockquote>
<p>Below is the <strong>NPPD Group/Line Report</strong>. This report was obtained by selecting <em><strong>multiple</strong></em> NPPD Groups (as shown under the two shaded headings).</p>
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
<td><p>PROSTHETIC INVENTORY NPPD GROUP/LINE REPORT Run Date: DEC 15,2000@15:21:22 Page: 1</p>
<p>STATION: Milwaukee VAMC NOV 01, 2000 - NOV 30, 2000 [ 30 calendar days ]</p>
<p><strong><mark>BRACES AND ORTHOTICS</mark></strong></p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>NPPD LINE V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>400 A BRACE ANKLE</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 12 217.09 | 12 | 0.40 | 127 | 318| 3,451.88</p>
<p>400 D BRACE AL/OTH</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 57 1,218.86 | 57 | 1.90 | 242 | 127| 3,613.87</p>
<p>400 E ELAS HOSE, EA</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 72 749.77 | 72 | 2.40 | 344 | 143| 5,417.58</p>
<p>400 F BRACES, KNEE</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 16 155.05 | 16 | 0.53 | 131 | 246| 1,595.92</p>
<p>400 G CORSET/BELT</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 1 8.25 | 1 | 0.03 | 479 | &gt;999| 8,932.79</p>
<p>================================================================================================================================</p>
<p>0 0.00| 158 2,349.02 | 158 | | 0 1323 | | 0.00 23,012.04</p>
<p><strong><mark>MEDICAL EQUIPMENT</mark></strong></p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>NPPD LINE V.A.(Used) Total| COM. (New) Total| Total |Days Ave | Stock On-Hand| Days |Total $ Value On-Hand</p>
<p>Issue $ Value| Issue $ Value| Issue |Usage Rate| Used New | On-Hand| Used New</p>
<p>--------------------------------------------------------------------------------------------------------------------------------</p>
<p>900 A WALKING AIDS</p>
<p>(Used) 1 0.00| | 1 | 0.03 | 62 | &gt;999| 0.00</p>
<p>(New) | 108 1,923.07 | 108 | 3.60 | 349 | 97| 2,651.81</p>
<p>900 D BED HOSP SPEC</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 6 0.00 | 6 | 0.20 | 9 | 45| 5,432.54</p>
<p>900 E MATTRESS STAN</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 6 -460.00 | 6 | 0.20 | 9 | 45| 1,035.00</p>
<p>900 F MATTRESS SPEC</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 8 | &gt;30| 360.00</p>
<p>(New) | 2 338.62 | 2 | 0.07 | 15 | 225| 887.86</p>
<p>900 G BED, ACCESSORIES</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 6 397.80 | 6 | 0.20 | 35 | 175| 2,327.55</p>
<p>900 I SPEC HOME EQP (SAFETY)</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 20 | &gt;30| 0.00</p>
<p>(New) | 89 3,143.96 | 89 | 2.97 | 122 | 41| 3,009.69</p>
<p>900 J TENS UNIT</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 0 | | 0.00</p>
<p>(New) | 8 1,000.00 | 8 | 0.27 | 4 | 15| 500.00</p>
<p>900 K MED EQP AL/OTH</p>
<p>(Used) 0 0.00| | 0 | 0.00 | 42 | &gt;30| 0.00</p>
<p>(New) | 242 5,296.04 | 242 | 8.07 | 382 | 47| 5,731.05</p>
<p>================================================================================================================================</p>
<p>1 0.00| 467 11,639.49 | 468 | | 132 925 | | 360.00 21,575.50</p>
<p>GRAND TOTAL $ VALUE ISSUED (Used) = $ 0.00 GRAND TOTAL $ VALUE ON-HAND (Used) = $ 360.00</p>
<p>GRAND TOTAL $ VALUE ISSUED (New) = $ 13,988.51 GRAND TOTAL $ VALUE ON-HAND (New) = $ 44,587.54</p>
<p>&lt;End of Report&gt;</p></td>
</tr>
</tbody>
</table>

<span id="_Hlt500262696" class="anchor"></span>NPPD Group Summary Report (SS)

<span id="_Toc501807379" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <strong>NPPD Group Summary Report</strong> is based on the NPPD Group selected. It is the summary of the entire Prosthetics inventory for a certain date range sorted by NPPD Group.</p>
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
<p>To select the <strong>NPPD Group Summary Report</strong>, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                  |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                           |
| 1    | Type SS for the NPPD GroupSummary Report option from the Inventory Reports Menu, and press \<Enter\>.                       |
| 2    | At the Site prompt, press \<Enter\> to select the default site entry.                                                                    |
| 3    | At the Beginning Date prompt, type the beginning date of the date range, and press \<Enter\>.                                            |
| 4    | At the Ending Date prompt, type the end date, and press \<Enter\>.                                                                       |
| 5    | At the Device: HOME// prompt, press \<Enter\>.                                                                                           |
| 6    | To view or print the report, type “;132;” at the Right Margin: 80// prompt to extend the margins for the report to display and/or print. |
| 7    | Press \<Enter\>.                                                                                                                             |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NPPD Group Summary Report</td>
<td><blockquote>
<p>SI Item Detail Report</p>
<p>SH HCPCS Summary Report</p>
<p>SG NPPD Group/Line Report</p>
<p>SS NPPD Group Summary Report</p>
<p>PI Print Current HCPCS Balance by HCPCS</p>
<p>PL Print Current Item Balance by Location</p>
<p>PO Print Order/Receive Item</p>
<p>PS Print Transaction History</p>
<p>IU Print Item Usage By Location</p>
<p>WS Print Stock Work Sheet</p>
<p>BC Reprint Barcode Label</p>
<p>PC Print Items Not Issued Within 30-Day</p>
<p>OD Print Stock On Hand Over Date Range</p>
<p>AL Print All Barcode in a Location</p>
<p>IP Print PIP/IFCAP Item Report</p>
<p>Select Inventory Reports Option: <strong>SS</strong> &lt;<strong>Enter</strong>&gt; NPPD Group Summary Report</p>
<p>SITE: Hines Development System// &lt;<strong>Enter</strong>&gt; 499</p>
<p>Beginning Date: 9/1 (SEP 01, 2000) &lt;<strong>Enter</strong>&gt;</p>
<p>Ending Date: 9/30 (SEP 30, 2000) &lt;<strong>Enter</strong>&gt;</p>
<p>DEVICE: HOME// TELNET VIRTUAL</p>
<p>You need at least 132 columns for this report.</p>
<p>Please use a device capable of this requirement.</p>
<p>DEVICE: HOME// <strong>;132;</strong> &lt;<strong>Enter</strong>&gt; TELNET VIRTUAL</p>
<p>Processing report.......</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc501807380" class="anchor"></span>Viewing the NPPD Group Summary Report

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NPPD Group Report</td>
<td><blockquote>
<p>Below is the <strong>Prosthetic Inventory</strong> <strong>NPPD Group Summary Report</strong> that displays an entire summary of NPPD Groups for the selected date range.</p>
</blockquote></td>
</tr>
</tbody>
</table>

PROSTHETIC INVENTORY NPPD GROUP SUMMARY REPORT Run Date: NOV 2,2000@14:16:17 Page: 1STATION: Hines Development Sy SEP 01, 2000 - SEP 30, 2000 \[ 30 calendar days \]ENTIRE SUMMARY---------------------------------------------------------------------------------------------------------------------------------NPPD GROUP V.A.(Used) Total\| COM. (New) Total\| Total \|Days Ave \| Stock On-Hand\| Days \|Total \$ Value On-HandIssue \$ Value\| Issue \$ Value\| Issue \|Usage Rate\| Used New \| On-Hand\| Used New---------------------------------------------------------------------------------------------------------------------------------

100 WHEELCHAIRS AND ACCESSORIES

(Used) 0 0.00\| \| 0 \| 0.00 \| 24 \| \>30\| 0.00

(New) \| 51 5,775.95 \| 51 \| 1.70 \| 145 \| 85\| 9,233.12

-----------------------------------------------------------------------------------------------------------------------

400 BRACES AND ORTHOTICS

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 158 2,349.02 \| 158 \| 5.27 \| 1327 \| 252\| 23,041.11

----------------------------------------------------------------------------------------------------------------------

500 SHOES/ORTHOTICS

(Used) 6 0.00\| \| 6 \| 0.20 \| 163 \| 815\| 949.04

(New) \| 35 751.44 \| 35 \| 1.17 \| 211 \| 181\| 4,429.94

600 NEUROSENSORY AIDS

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 54 473.58 \| 54 \| 1.80 \| 180 \| 100\| 1,764.57

---------------------------------------------------------------------------------------------------------------------

800 OXYGEN AND RESPIRATORY

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 103 1,853.57 \| 103 \| 3.43 \| 70 \| 20\| 11,173.04

----------------------------------------------------------------------------------------------------------------------

900 MEDICAL EQUIPMENT

(Used) 1 0.00\| \| 1 \| 0.03 \| 132 \| \>999\| 360.00

(New) \| 467 11,639.49 \| 467 \| 15.57 \| 930 \| 60\| 21,644.27

910 ALL OTHER SUPPLIES AND EQUIPMENT

(Used) 0 0.00\| \| 0 \| 0.00 \| 0 \| \| 0.00

(New) \| 8 49.52 \| 8 \| 0.27 \| 25 \| 94\| 359.56

-----------------------------------------------------------------------------------------------------------------------

999 MISC

(Used) 1 483.75\| \| 1 \| 0.03 \| 54 \| \>999\| 967.50

(New) \| 109 3,258.20 \| 109 \| 3.63 \| 1568 \| 432\| 26,714.93

======================================================================================================================

GRAND TOTAL \$ VALUE ISSUED (Used) = \$ 483.75 GRAND TOTAL \$ VALUE ON-HAND (Used) = \$ 2,276.54

GRAND TOTAL \$ VALUE ISSUED (New) = \$ 26,150.77 GRAND TOTAL \$ VALUE ON-HAND (New) = \$ 98,360.54

\<End of Report\>

<span id="_Hlt509035833" class="anchor"></span>Other Useful Inventory Reports

<span id="_Toc99425823" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>There are other useful Inventory Reports including the following:</p>
</blockquote>
<ul>
<li><p>Print Transaction History (PS)</p></li>
<li><p>Print Current Item Balance by Location (PL)</p></li>
<li><p>Print Current HCPCS Balance by HCPCS (PI)</p></li>
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
<td>Print Transaction History (PS)</td>
<td><blockquote>
<p>This option is used to <strong>Print Transaction History</strong> <strong>(PS)</strong> covering a selected time period. It prints a record of stock movement or transaction history (number issued, ordered, received) for all or selected HCPCS and items that are in Prosthetics Inventory over a specified date range.</p>
<p>The report includes patients receiving the items, notes on updates to the HCPCS Items, returns, cancellations, deactivations, etc., plus dollar amounts for HCPCS/Items issued.</p>
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
<td>Print Current Item Balance by Location (PL)</td>
<td><blockquote>
<p>The <strong>Print Current Item Balance by Location (PL)</strong> option is used to print the balances for available items by location. This report is also helpful when conducting a physical count and provides the Unit Cost as well as the quantity of an Item in each Location.</p>
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
<td>Print Current HCPCS Balance by HCPCS (PI)</td>
<td><blockquote>
<p>The <strong>Print Current HCPCS Balance by HCPCS</strong> <strong>(PI)</strong> option prints a report of the number of items available in each location for selected HCPCS. It includes other information about the items, including source (VA or Commercial), vendor, and unit of issue, re-order level and average cost. You may select individual HCPCS or all HCPCS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc99425824" class="anchor"></span>Print Transaction History (PS)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>This option is used to <strong>Print Transaction History</strong> <strong>(PS)</strong> covering a selected time period. It prints a record of stock movement or transaction history (number issued, ordered, received) for all or selected HCPCS and items that are in Prosthetics Inventory over a specified date range.</p>
<p>The report includes patients receiving the items, notes on updates to the HCPCS items, returns, cancellations, deactivations, etc., plus dollar amounts for HCPCS/items issued.</p>
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
<p>To select the <strong>NPPD Group Summary Report</strong>, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                  |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                           |
| 1    | Type PS for the Print Transaction History option from the Inventory Reports Menu, and press \<Enter\>.                           |
| 2    | At the Site prompt, press \<Enter\> to select the default site entry.                                                                    |
| 3    | At the Beginning Date prompt, type the beginning date of the date range, and press \<Enter\>.                                            |
| 4    | At the Ending Date prompt, type the end date, and press \<Enter\>.                                                                       |
| 5    | At the Device: HOME// prompt, press \<Enter\>.                                                                                           |
| 6    | To view or print the report, type “;132;” at the Right Margin: 80// prompt to extend the margins for the report to display and/or print. |
| 7    | Press \<Enter\>.                                                                                                                             |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> prompt only appears if your Prosthetics Service covers multiple stations. This is a non-editable field (for display purposes only). Entering a question mark &lt;?&gt; will bring up a list of sites for which you will need to define the Locations. Select a site or enter the number(s) for your station.</p>
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
<td><h5 id="sample-report-criteria">Sample Report criteria</h5></td>
<td><p>Select Inventory Reports Option: <strong>PS</strong> <strong>&lt;Enter&gt;</strong> Print Transaction History</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong></p>
<p>Select HCPCS 1: <strong>A4402-3</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Select HCPCS 2: <strong>&lt;Enter&gt;</strong></p>
<p>Beginning Date: T-30// <strong>&lt;Enter&gt;</strong> (NOV 16, 2003)</p>
<p>Ending Date: TODAY// <strong>&lt;Enter&gt;</strong> (DEC 16, 2003)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<blockquote>
<p>Processing report......</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Print Transaction History (PS), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS</td>
<td><blockquote>
<p>Enter each HCPCS you want covered in the report. The "Select HCPCS" prompt will continue to appear until you press the <strong>&lt;Enter&gt;</strong> key to bypass the prompt.</p>
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
<td>Beginning Date</td>
<td><blockquote>
<p>This is the earliest date for the report. Enter a specific date for the period of interest or you may accept the default displayed.</p>
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
<td>Ending Date</td>
<td><blockquote>
<p>This is the last day of the reporting period. Enter a specific date for the period of interest or you may accept the default of TODAY.</p>
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
<td>Device</td>
<td><blockquote>
<p>Press the &lt;<strong>Enter</strong>&gt; key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.</p>
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
<td><h5 id="sample-report">Sample report</h5></td>
<td><p>* ISSUE and STOCK CONTROL RECORD - PROSTHETICS STOCK ITEMS * Page: 1</p>
<p>station: SUPPORT ISC</p>
<p>JAN 04, 2003 to JUL 23, 2003</p>
<p>------------------------------------------------------------------------------</p>
<p>QTY QTY QTY DOLLAR</p>
<p>DATE PATIENT SSN USER ISSUE ORDER REC VALUE</p>
<p>---- ------- --- ---- ----- ----- --- ------</p>
<p>HCPCS: A4402-3 Item: LUBRICANT GEL</p>
<p>03/12/03 Note: RECEIPT PROSdv,one 5 25.00</p>
<p>03/12/03 Note: ORDER PROSdv,two 3 0.00</p>
<p>03/12/03 Note: RECEIPT PROSdv,three 2 110.00</p>
<p>03/12/03 Note: RECEIPT PROSdv,four 3 165.00</p>
<p>03/12/03 Note: RECEIPT PROSdv,five 1 55.00</p>
<p>03/12/03 Note: PATIENT ISSUE PROSdv,six 2 110.00</p>
<p>03/12/03 Note: RETURN IN PROSdv,seven 2 110.00</p>
<p>03/12/03 Note: RECONCILE PROSdv,eight 9 495.00</p>
<p>03/12/03 Note: RECONCILE PROSdv,nine -2 -110.00</p>
<p>03/12/03 Note: RECONCILE PROSdv,ten 0 0.00</p>
<p>03/13/03 Note: RECONCILE PROSdv,eleven -1 -19.29</p>
<p>03/28/03 Note: TRANSFER PROSdv,twelve -2 -2.86</p>
<p>03/28/03 Note: TRANSFER PROSdv,thirteen 2 2.86</p>
<p>03/28/03 PROSpatient, one 0765 PROSdv,fourteen 1 1.43</p>
<p>04/21/03 Note: ORDER PROSdv,fifteen 5 0.00</p>
<p>04/21/03 Note: RECEIPT PROSdv,sixteen 5 250.00</p>
<p>04/25/03 PROSpatient, two 0765 PROSdv,seventeen 1 1.42</p>
<p>04/25/03 PROSpatient, thr 0765 PROSdv,eighteen 1 1.43</p>
<p>05/07/03 PROSpatient, fou 0765 PROSdv,nineteen 1 50.00</p>
<p>* Dollar Value of Item Issued = 54.28</p>
<p>* Dollar Value of HCPCS Issued = 54.28</p>
<blockquote>
<p>&lt;End of Report&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Hlt509035835" class="anchor"></span>Print Current Item Balance by Location (PL)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Current Item Balance by Location (PL)</strong> option is used to print the balances for available items by location. <u>The format has been revised with Patch RMPR*3*61, and zero balances are now shown on this report</u>.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Report format has been revised with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site</td>
<td><blockquote>
<p>This prompt only appears if your Prosthetics Service covers multiple stations. Enter the site and press &lt;<strong>Enter</strong>&gt;.</p>
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
<td>Enter “ALL”</td>
<td><blockquote>
<p><strong>Enter 'ALL' for all Locations or 'RETURN' to select individual Locations</strong>: If you enter ALL at this prompt, every location in your Prosthetics Inventory will be covered by the report. Press the &lt;<strong>Enter</strong>&gt; key to select one or more specific locations.</p>
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
<td><h5 id="date-received-column">Date Received column</h5></td>
<td><blockquote>
<p>To help the users manage there inventory, this report was modified to print the <em><strong>Date Received</strong></em> column. Users can reference this report with the information below the barcode to double check if a particular barcode has any inventory on stock.</p>
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
<td><h5 id="device">Device</h5></td>
<td><blockquote>
<p>Press the <strong>&lt;Enter&gt;</strong> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.</p>
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
<td><h5 id="sample-report-1">Sample report</h5></td>
<td><p>* PROSTHETICS INVENTORY BALANCE BY LOCATION * PAGE: 1</p>
<p>Run Date: DEC 04, 2002 station: SUPPORT ISC</p>
<p>------------------------------------------------------------------------------</p>
<p><strong>Location: JLOC</strong></p>
<p>UNIT</p>
<p>DATE OF UNIT TOTAL</p>
<p>HCPCS ITEM SRC VENDOR RECVD ISSUE QTY COST VALUE</p>
<p>----- ---- --- ------ ----- ----- --- ---- ------</p>
<p>A4254-1 BATTERY FOR GLUCOSE MONI C ABBOTT 12/02/02 25 42.16 1,054.03</p>
<p>A4254-3 EYEGLASSES C ABBOTT 05/07/02 29 45.00 1,305.00</p>
<p><strong>A4301-1 WHEELCHAIR-ADULT/HEMI/BL 0 0.00 0.00</strong></p>
<p>A4373-1 WHEELCHAIR - ELECTRIC V ABBOTT 02/05/02 20 200.00 4,000.00</p>
<p>BA185-2 WATCH BRAILLE C HINES 09/05/01 4 32.38 129.52</p>
<p>BA185-3 WATCH LOW VISION BLACK C HINES 09/05/01 46 2.82 129.72</p>
<p>E0111-2 CRUTCH FOREARM/VA V HINES 09/05/01 3 2.00 6.00</p>
<p>------------------------------------------------------------------------------</p>
<p><strong>Location: JLOC3</strong></p>
<p>UNIT</p>
<p>DATE OF UNIT TOTAL</p>
<p>HCPCS ITEM SRC VENDOR RECVD ISSUE QTY COST VALUE</p>
<p>----- ---- --- ------ ----- ----- --- ---- ------</p>
<p>A4254-1 BATTERY FOR GLUCOSE MONI C ABBOTT 02/11/02 37 23.50 869.50</p>
<p>K0096-1 WHEELCHAIR - ELECTRIC C ABBOTT 10/25/01 10 800.00 8,000.00</p>
<p>L5000-1 SHO INSERT W ARCH TOE FI C ABBOTT 09/05/01 192 5.00 960.00</p>
<p>L5000-2 SHO INSERT W ARCH TOE/VA V ABBOTT 09/05/01 100 3.00 300.00</p></td>
</tr>
</tbody>
</table>

<span id="_Hlt509035837" class="anchor"></span>Print Current HCPCS Balance by HCPCS (PI)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Report description</td>
<td><blockquote>
<p>The <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Print Current HCPCS Balance by HCPCS</strong> <strong>(PI)</strong> option prints a report of the number of items available in each location for selected HCPCS. It includes other information about the items, including source (VA or Commercial), vendor, <strong>unit of issue</strong> (new column with Patch RMPR*3*61), re-order level and average cost. You may select individual HCPCS or all HCPCS.</p>
<p><strong>Note:</strong> Items with zero dollar amounts now display on this report with Patch 61.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Report format has been revised with Patch RMPR*3*61.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site</td>
<td><blockquote>
<p>This prompt only appears if your Prosthetics Service covers multiple stations. Enter the site.</p>
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
<td>Enter “ALL”</td>
<td><blockquote>
<p><strong>Enter 'ALL' for all HCPCS or 'RETURN' to select individual HCPCS</strong>: If you enter ALL at this prompt, every HCPCS Item in your PIP will be covered by the report. Press the &lt;<strong>Enter</strong>&gt; key to select one or more specific HCPCS items.</p>
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
<td>Device</td>
<td><blockquote>
<p>Press the &lt;<strong>Enter</strong>&gt; key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.</p>
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
<td>Sample report</td>
<td><p>* PROSTHETICS INVENTORY BALANCE BY HCPCS * PAGE: 2</p>
<p>Run Date: DEC 12, 2002 station: SUPPORT ISC</p>
<p>------------------------------------------------------------------------------</p>
<p>RE- <strong>UNIT</strong></p>
<p>ORDER <strong>OF</strong> UNIT TOTAL</p>
<p>HCPCS ITEM SRC LOCATION VENDOR LEVEL <strong>ISSUE</strong> QTY COST VALUE</p>
<p>----- ---- --- -------- ------ ----- ----- --- ---- ------</p>
<p>A4254-1 BATTERY FOR GLUCO C HO 1 ABB 1 EA 29 45.00 1,305.00</p>
<p>A4254-1 BATTERY FOR GLUCO C JLOC3 20 1 155.00 155.00</p>
<p>A4254-1 BATTERY FOR GLUCO C JLOC3 ABBOTT 20 37 23.50 869.50</p>
<p>A4254-1 BATTERY FOR GLUCO C HELEN PORTION 0 PR 3 1.00 3.00</p>
<p>A4254-1 BATTERY FOR GLUCO C J-Room ABBOTT 0 EA 29 45.00 1,305.00</p>
<p>A4254-1 BATTERY FOR GLUCO C JLOC ABBOTT 0 25 42.16 1,054.03</p>
<p>A4254-3 EYEGLASSES C HO 1 ABB 4 17 49.83 847.10</p>
<p>A4254-3 EYEGLASSES C HO 1 ABB 4 25 55.00 1,375.00</p>
<p>A4254-3 EYEGLASSES C JLOC ABBOTT 0 29 45.00 1,305.00</p>
<p>=======================</p>
<p>Totals for A4254 = 195 8,218.63</p>
<p>A4259-1 LANCETS PER BOX/C C HNC ABBOTT 0 EA 2 21.50 43.00</p>
<p>A4259-1 LANCETS PER BOX/C C TRAN INLANDE 1 BX 2 21.20 42.40</p>
<p>=======================</p>
<p>Totals for A4259 = 27 584.50</p>
<p>------------------------------------------------------------------------------</p>
<p><strong>A4301-1 WHEELCHAIR-ADULT/ 0 0.00 0.00</strong></p>
<p>=======================</p>
<p><strong>Totals for A4301 = 0 0.00</strong></p></td>
</tr>
</tbody>
</table>

<span id="_Toc461510772" class="anchor"></span>

Appendix A

<span id="_Toc99425828" class="anchor"></span>Glossary

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

<span id="_Toc99425829" class="anchor"></span>Appendix B

<span id="_Toc99425830" class="anchor"></span>Using Prosthetics Help

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
<p>Entering a single question mark at a prompt provides you with a single line of standard help.</p>
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
<p>Two question marks entered at a prompt provide you with a list of choices appropriate to the prompt where you entered the question marks.</p>
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
<p>You can enter three question marks to view Menu option descriptions.</p>
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

[^1]: New reports with Patch RMPR\*3\*61.