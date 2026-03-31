---
title: RMPR*3*61 Prosthetics Inventory Package (PIP) Implementation Guide
doc_type: IG-IMP
doc_label: Implementation Guide
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
menu_options: 24
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h5 id=\\"introduction\\">Introduction</h5></td> <td><blockquote> <p>The purpose of this Prosthetics Inventory Package (PIP) RMPR361 <em><strong>Implementation Guide</strong></em> is to prov"
audience: 
keywords: 
  - strong
  - blockquote
  - table
  - width
  - colgroup
  - style
  - tbody
  - print
  - inventory
  - location
page_count: 0
word_count: 8022
section_count: 4
table_count: 16
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_p61_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_p61_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [## Inventory Package (PIP) Implementation Guide](#inventory-package-pip-implementation-guide)
  - [Information for IRM](#information-for-irm)
  - [More Steps to Implement Patch RMPR\3\61](#more-steps-to-implement-patch-rmpr361)
![](rmpr-3-61-prosthetics-inventory-package-pip-implementation-guide/001.png)
PROSTHETICSINVENTORY PACKAGE (PIP)IMPLEMENTATION GUIDEPatch RMPR\*3\*61
March 2005
V*IST*A Health System Design and Development (HSD&D)
Table of Contents
Inventory Package (PIP) Implementation Guide [1](#inventory-package-pip-implementation-guide)
Overview [1](#overview)
Implementation Checklist [3](#implementation-checklist)
Implementation Steps [4](#implementation-steps)
Information for IRM [8](#information-for-irm)
Introduction [8](#introduction-1)
Scanner/Barcode Printer Configuration [10](#scannerbarcode-printer-configuration)
More Steps to Implement Patch RMPR\*3\*61 [13](#more-steps-to-implement-patch-rmpr361)
Populating the Inventory (into PIP) [13](#populating-the-inventory-into-pip)
Print Current Item Balance by Location (PL) [18](#print-current-item-balance-by-location-pl)
Print All Barcode in a Location (AL) [19](#print-all-barcode-in-a-location-al)
Inventory Implementation Worksheet for New PIP Items [20](#inventory-implementation-worksheet-for-new-pip-items)
Print Stock Work Sheet (WS) [21](#print-stock-work-sheet-ws)
Print PIP/IFCAP Item Report (IP) [22](#print-pipifcap-item-report-ip)

## ## Inventory Package (PIP) Implementation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<p>The purpose of this Prosthetics Inventory Package (PIP) RMPR*3*61 <em><strong>Implementation Guide</strong></em> is to provide instructions for Prosthetics users to implement the use of Patch RMPR*3*61 with the use of the barcode equipment. <u>Before you begin using the PIP software at your site(s), review the checklist in this document</u>. This list provides procedures for you to use the barcode labeling system.</p>
<p>The <strong>Prosthetics Inventory Main Menu</strong> is used to maintain the data in the inventory software and provide reports on that inventory at your location(s).</p>
<p><strong><u>WARNING</u>:</strong> This patch must be loaded <u>after</u> normal working hours. Extensive changes are made to PIP and Stock Issue options; so it should not be used during the install! <strong><u>Mandatory</u></strong>: Make sure that there are no Prosthetic users on the system until after the installation is complete!</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="reports-and-worksheets">Reports and Worksheets</h5></td>
<td><blockquote>
<p>There are reports in the <strong>Inventory Report Menu (RP)</strong> that will help you document your inventory when implementing this patch. There is a blank worksheet at the end of this document to help you capture new Inventory Item data not entered into PIP.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="prosthetics-barcode-scanners">Prosthetics Barcode Scanners</h5></td>
<td><blockquote>
<p>The barcode scanner equipment used by the Prosthetics service can scan only Prosthetics barcode labels. <u>Label Size</u>: Use 1.5 x 3 inch labels with a flat surface, not a glossy or semi-gloss surface.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="notes-to-irm">Notes to IRM</h5></td>
<td><blockquote>
<p>Verify that the printer (Zebra Z4M printer) for use with the barcode scanner was delivered to you with a serial and a TCP/IP port on it. If there is no network card attached to it, you will need to order this separately.</p>
<p>Also after installation, please verify that the option <strong>Inventory Task Balance Check</strong> is scheduled and that the mail group, RMPR INVENTORY is established and has members.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

#### Overview, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="note-to-irm-regarding-documentation">Note to IRM Regarding Documentation</h5></td>
<td><p>Patch RMPR*3*61 is a large patch that involves careful setup PRIOR to installation and data conversion.</p>
<p><strong><u>This is extremely important</u>:</strong> Please review this <em><strong>Implementation Guide</strong></em> and the following documents before installation which are found on the VistA Document Library (VDL):</p>
<ul>
<li><p>Forum Patch Module description</p></li>
<li><p>Prosthetics Inventory Package (PIP) User Manual</p></li>
<li><p>Prosthetics Inventory Package (PIP) Lessons Learned</p></li>
<li><p>Prosthetics Purchasing - Stock Issues User Manual.</p></li>
</ul>
<blockquote>
<p>Additionally, the manuals and Lessons Learned should be provided to end users with the suggestion that they be reviewed. Several major changes to the software are being introduced with this patch and the smoothness of adapting to these changes is directly related to end users having and reading these documents.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Implementation Checklist

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="checklist-summary-and-detailed">Checklist – Summary and Detailed</h5></td>
<td><blockquote>
<p>Below is a summary of the steps to complete before you begin using Patch 61 and the barcode scanner equipment. Following the summary are the details of each step. Please review this checklist in its entirety.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="summary-of-overall-process">Summary of Overall Process</h5></td>
<td><blockquote>
<p><strong>1. Install Patch 61 into your Test account.</strong></p>
<p>Become familiar with new software and equipment.</p>
<p><strong>2. Before installing into your Production</strong> (Live) <strong>account</strong>:</p>
</blockquote>
<ol type="a">
<li><p>Print the <strong>Print Current Item Balance by Location (PL)</strong> report</p></li>
<li><p>Coordinate the install date with your IRM.</p></li>
</ol>
<blockquote>
<p>c. Enter un-posted Stock Issues (if needed).</p>
<p><strong>3. Plan your Physical Inventory Count including:</strong></p>
</blockquote>
<p>a. Plan the date.</p>
<p>b. Select the staff.</p>
<blockquote>
<p>c. Conduct the Physical Inventory Count.</p>
<p>d. Edit any item quantities in PIP (if necessary).</p>
</blockquote>
<p>e. <u>Print</u>: <strong>Print Current Item Balance by Location (PL)</strong> report (after all edits have been made).</p>
<blockquote>
<p><strong>4. Install Patch 61 into your Production (Live account).</strong></p>
<p>a. <u>Print AGAIN</u>: <strong>Print Current Item Balance by Location (PL)</strong> report.</p>
</blockquote>
<ul>
<li><p>Compare it to report printed prior to installation.</p></li>
<li><p>Look for missing Locations, Items, Vendors, etc.</p></li>
<li><p>Log a Remedy ticket if reports are <strong>drastically different</strong>, e.g. missing data (Locations, items, etc.), quantity on hand for one item changed from 3 to 3000, etc.</p></li>
</ul>
<blockquote>
<p>b. <u>Print NEW</u>: Print the <strong>Print PIP/IFCAP Item Report (IP)</strong> to verify that there are no missing IFCAP Items in the report. If there are, then you will need to edit the HCPCS/Item.</p>
</blockquote>
<ol start="5" type="1">
<li><blockquote>
<p><strong>Print Barcode Labels.</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>Print the Print Stock Work Sheet (WS) report monthly and conduct a physical inventory.</strong> If a discrepancy arises, conduct a physical inventory at that time for the most active HCPCS codes.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

#### Implementation Steps

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="step-1-install-in-test-account">Step 1: Install in Test Account</h5></td>
<td><blockquote>
<p>Install Patch 61 into the Test Account. The steps during this phase are shown below:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                                                                              |
| 1    | Coordinate with your IRM to install Patch 61 in the Test Account.                                                                                                                                                                                                   |
| 2    | Practice printing the labels on the barcode printer using the Print All Barcode in a Location (AL) option. If a label needs to be reprinted, use the Reprint Barcode Label (BC) option in your Test Account for a specific site (if a multi-site facility). |
| 3    | Then practice scanning labels you just printed using the Stock Issue(SI) option in your Test Account. (Or manually type in the barcode number.)                                                                                                            |
| 4    | Become familiar with the new/revised features of Inventory. Refer to the *Inventory User Manual* to help you walk through the prompts for each Inventory option in the Test Account.                                                                            |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="step-2-pre-live-installation">Step 2: Pre-Live Installation</h5></td>
<td><blockquote>
<p>Before the installation of Patch 61 into the Production (Live) Account, follow these steps:</p>
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
<td><p>Before you install the patch into your Production (Live) Account, complete the posting of <strong>Stock Issues.</strong> You would also do this prior to conducting a physical count if you have any pending Stock Issues to complete.</p>
<p><strong>Note:</strong> The physical count is optional – see Step 3 Physical Count.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>Print the <strong>Print Current Item Balance by Location (PL)</strong> report. This will display the quantity balances for available items by location.</p>
<p><strong>Note:</strong> You will be printing this report <u>again</u> after the Live installation to do a comparison of item quantities. The purpose of this is to compare item quantities before and after the patch is installed in the Production Account to verify accuracy of the system’s installation.</p></td>
</tr>
<tr class="even">
<td>3</td>
<td><p>Coordinate the selection of the install date with your IRM, because as soon as you complete the physical inventory count, Patch 61 can be installed into your Production Account.</p>
<p><strong>Note:</strong> The physical count is optional – see Step 3 Physical Count.</p></td>
</tr>
</tbody>
</table>

Continued on next page

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="step-3-physical-count-optional-but-highly-recommend">Step 3: Physical Count<br />
<br />
(Optional – But Highly Recommend!!)</h5></td>
<td><blockquote>
<p>You may want to do a physical count of your inventory unless you have completed one very recently (at least within the last month). (Use your discretion based on your activity, size of service, etc. on whether to do another one.) <u>It is advised to start this physical count on a Friday</u>.</p>
<p>The purpose of the physical count is to compare item quantities on the <strong>Print Current Item Balance by Location (PL)</strong> report that you will print before and again after the patch is installed in the Production Account to verify accuracy of the system’s installation.</p>
<p><strong>Note:</strong> If there are discrepancies and no physical count has been done, an accurate verification may NOT be possible.</p>
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
<td>Plan your <u>Inventory Physical Count</u>. A weekend is recommended since there is no stock issue activity. This will make the physical count more accurate. Begin the physical count on a Friday.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Select the staff that will be needed to conduct the physical count of the equipment/supplies.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Print the <strong>Print Current Item Balance by Location (PL)</strong> report to verify the quantity of each item (if you haven’t already printed it before).</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>Make copies of this report for each person conducting the physical count.</p>
<p><strong>Note:</strong> For multi-sites, print to each site’s printer (if possible), and if not, fax it to each assigned staff responsible for the physical count at each site.</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Assign people (if necessary) a selection of HCPCS/items to count using the <strong>Print Current Item Balance by Location (PL)</strong> report.</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Start counting.</td>
</tr>
<tr class="even">
<td>7</td>
<td>After the physical count is complete, make necessary changes (if any) to your PIP. If you do make any changes, you will need to re-print the <strong>Print Current Item Balance by Location (PL)</strong> report.</td>
</tr>
</tbody>
</table>

Continued on next page

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="step-4-irm-installation-live">Step 4: IRM Installation (Live)</h5></td>
<td><blockquote>
<p>Below are the steps to be done when the patch is installed in the Production Account (Live System). Steps are also listed to print the <strong>Print Current Item Balance by Location (PL)</strong> report to compare quantities of items to the report printed prior to installation.</p>
</blockquote>
<p><strong>WARNING:</strong> Stop posting your <strong>Stock Issues</strong> prior to installation of this patch in Production. Once it is installed, you can print the barcode labels and scan that label when posting a Stock Issue.</p></td>
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
<td><p>IRM can install Patch 61 in your Production (Live) Account. Ask to be notified when the installation is complete.</p>
<p><strong>Note:</strong> It may take two hours for sites not running PIP, and 4-8 hours for sites running PIP to install the patch (depending on the size of your inventory in PIP).</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>After the patch has been installed in Production, print the <strong>Print Current Item Balance by Location (PL)</strong> report AGAIN to compare the quantity for each item.</td>
</tr>
<tr class="even">
<td>3</td>
<td><p>Look for missing Locations, Items, Vendors, Reorder Levels, etc. on the report. You are comparing to make sure there are no errors generated by the patch.</p>
<p>If the report is drastically different (e.g., missing data, quantity on hand for one item changed from 3 to 3,000, etc.), log a Remedy ticket.</p>
<p><strong>Note:</strong> You will notice that the format of this report has changed after the installation!!</p>
<p>Because of the format changes, do NOT compare the cost of an item. The <em><strong>Average Cost</strong></em> shown on the old report is not available, and the new report now displays the <em><strong>Actual Cost</strong></em> of an item (unit cost) from a vendor.</p>
<p><u>You will now need to compare the <em><strong>Quantity</strong></em> column of the new format with the <em><strong>Current Balance</strong></em> column of the old report format</u>. They should be equal.</p>
<p>If you find discrepancies and if you’ve recently done a physical count, see which quantity is correct, and perform a reconciliation using the <strong>Reconcile Item Balance (UP)</strong> option. This will make sure that your Inventory is in balance with the <strong>Print Current Item Balance by Location (PL)</strong> report.</p></td>
</tr>
</tbody>
</table>

Continued on next page

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="step-4-contd">Step 4: Cont’d</h5></td>
<td><blockquote>
<p>Installation of Patch 61 into Production (Live) Account steps continued…</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                   |
| 4    | <u>Print NEW</u>: Print the Print PIP/IFCAP Item Report (IP) to verify that there are no missing IFCAP Items in the report. If there are, then you will need to edit the HCPCS/Item. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="step-5-print-barcode-labels">Step 5: Print barcode labels</h5></td>
<td><blockquote>
<p>Print the barcode labels.</p>
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
<td><p>You can begin to use the <strong>Print All Barcode in a Location (AL)</strong> option to print the barcode labels (using the information from your reports and worksheets. (See more detailed instructions in the <em><strong>Inventory User Manual</strong></em> under <strong>New Inventory Reports (Patch RMPR*3*61)</strong> section on how to use this option.)</p>
<p><strong>Warning:</strong> Once patch 61 is installed, the <strong>Issue</strong> <strong>from Stock (IS)</strong> option will only work with a barcode label. Otherwise, you will not be able to issue an item. This means that during this option, a barcode must be scanned, or you can manually enter a barcode sequence number (right below the barcode) in order to issue an item.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>The choice is up to you on how to attach the items with the barcode labels (e.g., label the item or the box or place labels in a binder).</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="step-6-conduct-a-physical-count">Step 6: Conduct a Physical Count</h5></td>
<td><p><strong>(Do Monthly or As Needed)</strong> Access the <strong>Print Stock Work Sheet (WS)</strong> option (under the <strong>Inventory Reports Menu</strong> <strong>(RP)</strong>) and print this report. You can print this worksheet from your Production (Live) Account <strong>(<em><u>only available after Patch 61 has been installed)</u></em></strong>. (See page 21 for more details.)</p>
<p>This worksheet will display the inventory stock by Location, HCPCS, Item description, date, cost, vendor, quantity, and a <u>blank column</u>. Conduct a Physical Count at least monthly during testing or if discrepancies arise, conduct one on the most active HCPCS Codes.</p>
<blockquote>
<p><strong>Note:</strong> You can enter the quantity on this report if there is any discrepancy from the <strong>Print Current Item Balance by Location (PL)</strong> report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Information for IRM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="warning-to-irm">WARNING to IRM</h5></td>
<td><blockquote>
<p>This patch, RMPR*3*61, should NOT be installed if the recommended Zebra printer is not available and operational. <strong>Do NOT install this patch during the first week of the month.</strong> The possibility of PIP roll-up running on the first week of the month can cause problems in the monthly PIP data. Installation of this patch must be coordinated with the prosthetics users.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="conversion">Conversion</h5></td>
<td><blockquote>
<p>Patch RMPR*3*61 will convert all Prosthetics Inventory Programs (PIP) files to new files. The conversion may take 2 hours for sites not running PIP and 4-8 hours for site running PIP to install the patch depending on the size of your inventory (number of items) in PIP.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="nois">NOIS</h5></td>
<td><p>The following are the NOIS associated with this patch:</p>
<ul>
<li><p>STX-1201-72032</p></li>
<li><p>NYH-1001-10380</p></li>
<li><p>ISH-0901-41926</p></li>
<li><p>HUN-0201-21319</p></li>
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
<td><h5 id="test-sites">Test Sites</h5></td>
<td><p>The following are the Test Sites for this patch:</p>
<ul>
<li><p>Atlanta</p></li>
<li><p>Augusta</p></li>
<li><p>Birmingham</p></li>
<li><p>Central Alabama HCS</p></li>
<li><p>Charleston, SC</p></li>
<li><p>Columbia, SC</p></li>
<li><p>Dublin</p></li>
<li><p>Madison, WI</p></li>
<li><p>Milwaukee</p></li>
<li><p>New York HCS</p></li>
<li><p>Tuscaloosa</p></li>
</ul></td>
</tr>
</tbody>
</table>

Continued on next page

#### Introduction, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="overview-of-nois">Overview of NOIS</h5></td>
<td><p>This patch allows queuing of inventory reports to 132 columns printer. NOIS STX-1201-72032 will be fixed by this patch.</p>
<blockquote>
<p>The new file design allows recording of multiple ordering of inventory items, and error messages, during the inventory nightly job, will display a message that an item or items is/are already been ordered. The following NOIS will be fixed: NOIS NYH-1001-10380, ISH-0901-41926 and HUN-0201-21319.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="zebra-printer">Zebra Printer </h5></td>
<td><blockquote>
<p>The Zebra Printer is being used for Patch RMPR*3*61. It is very important to have the Zebra printer configured before the IRM attempts to install Patch RMPR*3*61. See next page for Scanner/Barcode Printer Configuration.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Scanner/Barcode Printer Configuration

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="configurations">Configurations</h5></td>
<td><blockquote>
<p>Before installing this patch, be sure the following steps have been accomplished:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scanner-configuration">1. Scanner Configuration</h5></td>
<td><blockquote>
<p>Any brand of scanner that can read code-128 is recommended. Follow the Scanner User manual instructions on the set-up of the scanner. For the basic configuration, the scanner should be set to:</p>
<p><strong>CODE 128 - ENABLE</strong></p>
<p><strong>CARRIAGE RETURN - ENABLE</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="barcode-printer-configuration">2. Barcode Printer Configuration</h5></td>
<td><blockquote>
<p>Your Zebra barcode printer (Z4M) should come with a default set-up based on the VA network configuration. Below is the basic barcode printer configuration:</p>
<p><strong>Baud rate - 9600</strong></p>
<p><strong>Parity - NONE</strong></p>
<p><strong>Data Bits - 8</strong></p>
<p><strong>Stop bit - 1</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="terminal-type-for-lat-connection">Terminal Type for LAT Connection</h5></td>
<td><blockquote>
<p>Create a Terminal Type and a Device in the Terminal Type and Device file. Below is the example of a Terminal Type and Device:</p>
<p>LAT CONNECTION:</p>
<p>TERMINAL TYPE FOR LAT CONNECTION:</p>
<p>=================================</p>
<p><strong>A. For 300 DPI Zebra printer.</strong></p>
<p>NAME: P-ZEBRA-01 RIGHT MARGIN: 0</p>
<p>FORM FEED: # PAGE LENGTH: 9999</p>
<p>OPEN EXECUTE: S RMPRLRES=12 W $C(2),"^PON^LH0,0",$C(3)</p>
<p>CLOSE EXECUTE: K RMPRLRES S IONOFF=1</p>
<p>DESCRIPTION: Zebra Z4M 300 DPI barcode printer</p>
<p><strong>B. For 203 DPI Zebra printer.</strong></p>
<p>NAME: P-ZEBRA-02 RIGHT MARGIN: 0</p>
<p>FORM FEED: # PAGE LENGTH: 9999</p>
<p>OPEN EXECUTE: S RMPRLRES=8 W $C(2),"^PON^LH0,0",$C(3)</p>
<p>CLOSE EXECUTE: K RMPRLRES S IONOFF=1</p>
<p>DESCRIPTION: Zebra Z4M 203 DPI barcode printer</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="barcode-printer-configuration-1">Barcode Printer Configuration</h5></td>
<td><blockquote>
<p><strong>DEVICE FILE FOR LAT CONNECTION:</strong></p>
<p>===============================</p>
<p>NAME: ZEBRA PROSTHETIC PRINTER $I: _LTA4069:</p>
<p>LOCATION OF TERMINAL: TONY'S DESK LOCAL SYNONYM: ZEBRA</p>
<p>MNEMONIC: ZBP</p>
<p>SUBTYPE: P-ZEBRA-01 TYPE: TERMINAL</p>
<p>LAT SERVER NODE: ISC404 LAT SERVER PORT: 69</p>
<p>LAT PORT SPEED: 96</p>
<p><strong>TELNET CONNECTION:</strong></p>
<p>Enter all necessary data for the telnet printer connection, similar to the LAT printer configuration, and then <strong>ADD</strong> the VMS command below in the TNA_LOAD.COM file.</p>
<p>$ TELNET /CREATE 10.26.141.36 9100 1313 /TIME=(NOIDLE,</p>
<p>RECONNECT=00:00:02)/PROTO=NVT</p>
<p>$ SET PROT=W:RWLP /DEV TNA1313:</p>
<p><strong>TERMINAL TYPE FOR TELNET CONNECTION:</strong></p>
<p>====================================</p>
<p>NAME: P-ZEBRA RIGHT MARGIN: 132</p>
<p>FORM FEED: # PAGE LENGTH: 64</p>
<p>BACK SPACE: $C(8) BARCODE ON: $C(29),"k"</p>
<p><strong>DEVICE FILE FOR TELNET CONNECTION:</strong></p>
<p>==================================</p>
<p>NAME: ZEB1$PRT $I: _TNA1313:</p>
<p>LOCATION OF TERMINAL: Prosthetics Cl KEY OPERATOR: ZEBRA 109</p>
<p>MARGIN WIDTH: 80 PAGE LENGTH: 64</p>
<p>MNEMONIC: Zebra 105se</p>
<p>SUBTYPE: P-ZEBRA TYPE: TERMINAL</p>
<p>LAT SERVER PORT: N/A</p>
<p>PRINT SERVER NAME OR ADDRESS: 10.6.208.21</p>
<p>TELNET PORT: 9100 REMOTE PRINTER NAME: ZEB1$PRT</p>
<p><strong>Note:</strong> Terminal Type should be named with prefix 'P-ZEBRA'. For example; P-ZEBRA-xx, where 'xx' could be a number from '01' to '99'. If the Zebra printer is 203 DPI, variable RMPRLRES should be equal to 8. If the Zebra printer is 300 DPI, variable RMPRLRES should be equal to 12.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## More Steps to Implement Patch RMPR\*3\*61

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Populating the Inventory (into PIP)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="add-inventory-location-or-items-ae-option">Add Inventory LOCATION or ITEMS (AE) option</h5></td>
<td><blockquote>
<p>You must use the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option to populate the Prosthetics Inventory (PIP) to add a new Location or Item to inventory. (This is a one-time procedure.)</p>
<p>The bar coding feature will not work unless the Item(s) has been added to the PIP. <u>You must use the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option before you can issue an Item from the <strong>Stock Issues (SI) Menu</strong></u>. You will not be able to receive stock until an Item has been added.</p>
<p>You can also add a Prosthetic Location for each site where an inventory Item will be stored using the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option.</p>
<p><strong>Note:</strong> All items will need a HCPCS code and Location before creating the barcode label.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="making-corrections-to-the-inventory">Making corrections to the inventory</h5></td>
<td><blockquote>
<p>If you need to make any changes to the inventory data entered through the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option, use the following options.</p>
</blockquote>
<ul>
<li><p>The <strong>Edit Inventory Location (EL)</strong> option is used to make any necessary corrections to a Location name.</p></li>
<li><p>The <strong>Edit Inventory Item (EI)</strong> option is used to make any changes to the PIP Item description, Inventory Location, re-order level, invoice quantities of the Item(s), unit cost, or vendor.</p></li>
</ul>
<blockquote>
<p>If you need to remove a location entered in error, use the <strong>Deactivate Inventory Location (DE)</strong> option.</p>
<p><strong>Note:</strong> If an item is out of stock, and the quantity is shown as zero, the item will no longer appear on the Inventory reports except for the <strong>Print Transaction History (PS)</strong> report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="modified-options">Modified Options</h5></td>
<td><p>Below are the modified options. Please refer to the patch description or the <strong>Inventory (PIP) User Manual</strong> for all the changes in the list of MODIFIED OPTIONS.</p>
<ul>
<li><p>Add Inventory LOCATION or ITEMS [RMPR INV ADD]</p></li>
<li><p>Edit Inventory Items [RMPR INV EDIT]</p></li>
<li><p>Order Item from Supply or Vendor [RMPR INV ORDER]</p></li>
<li><p>Receive Item from Supply, Vendor or Patient [RMPR INV RECEIVE]</p></li>
<li><p>Transfer Stock Between Locations [RMPR INV TRAN]</p></li>
<li><p>Reconcile Item Balance [RMPR INV RECONCILE]</p></li>
<li><p>Item Detail Report [RMPR INV ON HND ITEM]</p></li>
<li><p>HCPCS Summary Report [RMPR INV ON HND HCPCS]</p></li>
<li><p>NPPD Group/Line Report [RMPR INV ON HND GROUP/LINE]</p></li>
<li><p>NPPD Group Summary Report [RMPR INV ON HND SUM]</p></li>
<li><p>Print Current HCPCS Balance by HCPCS [RMPR INV STOCK BY HCPCS]</p></li>
<li><p>Print Current Item Balance by Location [RMPR INV STOCK BY LOCATION]</p></li>
<li><p>Print Transaction History [RMPR INV PRINT/CHECK BAL]</p></li>
<li><p>Issue From Stock [RMPR ADD 2319]</p></li>
<li><p>Edit/Delete Issue From Stock [RMPR EDT 2319]</p></li>
<li><p>Pros Inventory Main [RMPR INV MAIN]</p></li>
<li><p>Inventory Reports [RMPR INV REPORTS]</p></li>
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
<td><h5 id="deleted-options">Deleted options</h5></td>
<td><p>Below are the deleted options:</p>
<ul>
<li><p>Deactivate Inventory Location [RMPR INV DELETE]</p></li>
<li><blockquote>
<p>Remove Item from Inventory [RMPR INV REMOVE]</p>
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
<td><h5 id="new-options-added">New Options Added</h5></td>
<td><p>Below are the new options added:</p>
<ul>
<li><blockquote>
<p>Deactivate Inventory Location [RMPR INV DEACTIVATE]</p>
</blockquote></li>
<li><blockquote>
<p>Edit Inventory Location [RMPR INV EDIT LOCATION]</p>
</blockquote></li>
<li><blockquote>
<p>Print Order/Receive Item [RMPR INV PRINT ORDER/RECEIVE]</p>
</blockquote></li>
<li><blockquote>
<p>Print Item Usage By Location [RMPR INV PRINT ITEM USAGE]</p>
</blockquote></li>
<li><blockquote>
<p>Print Stock Work Sheet [RMPR INV PRINT WORK SHEET]</p>
</blockquote></li>
<li><blockquote>
<p>Reprint Barcode Label [RMPR INV REPRINT BARCODE]</p>
</blockquote></li>
<li><blockquote>
<p>Print Stock On Hand Over Date Range [RMPR INV PRINT OVER DATE]</p>
</blockquote></li>
<li><blockquote>
<p>Print Items Not Issued Within 30-Day [RMPR INV PRINT 30-DAY]</p>
</blockquote></li>
<li><blockquote>
<p>Print All Barcode in a Location [RMPR INV PRINT ALL BARCODE]</p>
</blockquote></li>
<li><blockquote>
<p>Print PIP/IFCAP Item Report [RMPR INV PIP/IFCAP ITEM REPORT]</p>
</blockquote></li>
<li><blockquote>
<p>Remove/Deactivate HCPCS/Item from Inventory [RMPR INV REMOVE HCPCS/ITEM]</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

Continued on next page

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="modified-files-and-data-dictionary">Modified Files and Data Dictionary</h5></td>
<td><p>Below are the modified files and data dictionary:</p>
<p>-----------------------------------</p>
<p>Global: ^RMPR(660,</p>
<p>File Name: RECORD OF PROS APPLIANCE/REPAIR</p>
<p>Description of Change: The following field has been modified:</p>
<p>(#4.6) STOCK ISSUE 1;5 POINTER TO PROSTHETIC INVENTORY</p>
<p>TRANSACTION FILE (#661.6)</p>
<p>(#39) DATE OF SERVICE 1;8 DATE AN ITEM ISSUED TO PATIENT</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="documentation">Documentation</h5></td>
<td><blockquote>
<p>The documentation and KIDS build can be obtained from the ANONYMOUS.SOFTWARE directory at one of the OI Field Offices. The preferred method is to FTP the file from DOWNLOAD.VISTA.MED.VA.GOV, which will transmit the file from the first available server. Alternatively, site may elect to retrieve the file from a specific OI Field Office.</p>
</blockquote>
<p>IO FIELD OFFICE FTP Address DIRECTORY</p>
<p>--------------- ----------- ---------</p>
<p>Hines FTP.FO-HINES.MED.VA.GOV [ANONYMOUS.SOFTWARE]</p>
<p>Albany FTP.FO-ALBANY.MED.VA.GOV [ANONYMOUS.SOFTWARE]</p>
<p>Salt Lake FTP.FO-SLC.MED.VA.GOV [ANONYMOUS.SOFTWARE]</p>
<p>FILE</p>
<p>----</p>
<p>RMPR_3_61.KID</p>
<p>RMPR_3_P61_UM.PDF</p>
<p>RMPR_3_P61_IG.PDF</p>
<p>RMPR_3_P61_SIUM.PDF</p></td>
</tr>
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
<p>If you have further questions on obtaining the files, please contact the CIO National Help Desk at 1-888-596-4357 (HELP), and ask for the Financial Systems Team.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="installation-instructions">Installation Instructions</h5></td>
<td><p>This patch was created with Kernel V8 KIDS and should be installed into your production UCI. It can be installed anytime, but it is recommended that all Prosthetics users should be off the system. Complete installation will take more than 2 hours, depending on the number of items in the Prosthetics Inventory Program (PIP).</p>
<p>1. On the Kids Menu, under the 'Installation' Menu, Load a Distribution. When prompted 'Enter A Host File:' enter RMPR_3_61.KID.</p>
<p>2. Use the option 'Verify Checksum in Transport Global' and verify that all routines have the correct checksums.</p>
<p>3. From the 'Installation' menu of KIDS, use the option 'Install Package(s)'. Select the package 'RMPR*3*61' and proceed with the install.</p>
<p>4. It is recommended that you do not queue this patch for install.</p>
<p>5. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//' (at your discretion).</p>
<p>6. When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//' answer NO.</p>
<p>7. When prompted 'Want to DISABLE Schedule Options, Menu Options and Protocols? YES//', respond YES. When prompted to select the option you would like to place out of order, enter the following:</p>
<blockquote>
<p>RMPR OFFICIAL Prosthetic Official's Menu</p>
<p>RMPR CLERK Prosthetic Clerk's Menu</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="note-for-irm">Note for IRM</h5></td>
<td><p>Once the new files have been created and Prosthetic users start using the package, it is mandatory that the conversion (step 10) should be done!</p>
<p>Make sure no Prosthetic users are on the system when you complete steps 8-11.</p></td>
</tr>
</tbody>
</table>

Continued on next page

#### , Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="installation-steps-continued">Installation steps continued</h5></td>
<td><p>8. If option [RMPR INV TRAN] transfer stock between locations is still out of order, edit and remove the out of order message.</p>
<p>9. Backup globals: ^RMPR(660, ^RMPR(661.2 and ^RMPR(661.3</p>
<p>10. At programmer mode, enter D CONV^RMPRPIUG. Below is an example:</p>
<p>&gt;D CONV^RMPRPIUG</p>
<p>PIP old to new file conversion starting.</p>
<p>Creating locations in file 661.5.</p>
<p>Creating HCPCS items in file 661.11 - 1st pass.</p>
<p>.....</p>
<p>Creating current inventory - file 661.7</p>
<p>Creating patient issue transactions - File 661.6</p>
<p>Creating balancing reconciliations</p>
<p>Creating running balance file 661.9</p>
<p>PIP old to new file conversion complete.</p>
<p>If for some reason the conversion did not finish to completion, check the error or call CIO National Help Desk at 1-888-596-4357 (HELP) and ask for the Financial Systems Team. To restart the conversion, you must do D KILL^RMPRPIXZ to clean up all files created and then do D CONV^RMPRPIUG to restart the conversion again.</p>
<blockquote>
<p>11. You can now let Prosthetic users on the system.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scanner-and-barcode-printer-configuration">Scanner and Barcode Printer Configuration</h5></td>
<td><blockquote>
<p>Return to page 10 for Scanner/Barcode Printer Configuration information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Print Current Item Balance by Location (PL)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-description">Report description</h5></td>
<td><blockquote>
<p>The <strong>Print Current Item Balance by Location (PL)</strong> option is used to print the balances for available items by Location. This option is found under the <strong>Inventory Reports (RP)</strong> menu option on the <strong>PROS Inventory Main (INV) Menu</strong>.</p>
<p><u>This is the option that you want to use immediately before Patch RMPR*3*61 is installed and then again immediately afterwards</u>. You will then be able to compare the reports for each Location and HCPCS to make sure that no errors occurred during the installation of the new patch.</p>
<p><strong>Note:</strong> If there are any discrepancies in the quantity of an Item, you can reconcile an Item in PIP. Also note, that the format of this report changed with the installation of Patch RMPR*3*61. The <em><strong>Quantity</strong></em> column is the same as the <em><strong>Current Balance</strong></em> column of the old format. Zero balances also display on this report!</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="site-prompt">Site prompt</h5></td>
<td><blockquote>
<p>This prompt only appears if your Prosthetics Service covers multiple stations.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="enter-all-prompt">Enter “ALL” prompt</h5></td>
<td><blockquote>
<p><strong>Enter 'ALL' for all Locations or 'RETURN' to select individual Locations:</strong> If you enter ALL at this prompt, every location in your Prosthetics Inventory will be covered by the report. Press the <strong>&lt;Enter&gt;</strong> key to select one or more locations.</p>
</blockquote></td>
</tr>
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
<td><h5 id="sample-report">Sample report</h5></td>
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
<p>A4301-1 WHEELCHAIR-ADULT/HEMI/BL 0 0.00 0.00</p>
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

#### Print All Barcode in a Location (AL)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-2">Introduction</h5></td>
<td><blockquote>
<p>With Patch RMPR*3*61, the <strong>Print All Barcode in a Location (AL)</strong> option is a new Inventory report. This option is available for use in printing all the barcode labels for all items within a Location. This is a helpful option to use after installing this patch into the Production (Live) system.</p>
<p>Insert enough labels in the printer before using this option, since it will print labels for all items in a given station.</p>
<p><strong>Note:</strong> In order to use this option, user must have an RMPRMANAGER key.</p>
</blockquote></td>
</tr>
</tbody>
</table>

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
<p><strong>AL Print All Barcode in a Location</strong></p>
</blockquote></td>
</tr>
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
<p>Select Inventory Reports Option: AL <strong>&lt;Enter&gt;</strong> Print All Barcode in a Location</p>
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
<p>JOKER</p>
<p>MERGER</p>
<p>MERGER (2)</p>
<p>ODJ2</p>
<p>ODJLOC1</p>
<p>Enter Pros Location: <strong>JLOC</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Select Barcode Printer: ZEBRA PROSTHETIC// <strong>&lt;Enter&gt;</strong> ZEBRA PROSTHETIC PRINTER</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Inventory Implementation Worksheet for New PIP Items

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purpose">Purpose</h5></td>
<td><blockquote>
<p>Use this worksheet to enter information for new Inventory Items to be added to PIP for the first time. The columns below are the prompts in PIP. This is the information needed for the <strong>Add Inventory LOCATION or ITEMS (AE)</strong> option.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Prosthetic Location: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

|           |                |                          |         |                     |                 |               |                   |            |
|-----------|----------------|--------------------------|---------|---------------------|-----------------|---------------|-------------------|------------|
| HCPCS | IFCAP Item | PIP Item Description | V/C | Re- order Level | Invoice Qty | Unit Cost | Unit of Issue | Vendor |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |
|           |                |                          |         |                     |                 |               |                   |            |

#### Print Stock Work Sheet (WS)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-3">Introduction</h5>
<h5 id="section-1"></h5>
<h5 id="only-available-after-patch-61-installation">(Only available after Patch 61 Installation)</h5></td>
<td><blockquote>
<p>The <strong>Print Stock Work Sheet (WS)</strong> report prints the inventory stock by Location of a particular station. This option is found under the <strong>Inventory Reports (RP)</strong> menu option on the <strong>Prosthetic Inventory Main (INV) Menu</strong>. This option shows the HCPCS, Item description, Date, Cost, Vendor Quantity, Location and a blank column for the <em>Physical Count</em>. <strong><u>Recommendation</u>:</strong> Conduct a physical count and print this quarterly or as discrepancies arise on an active HCPCS Code.</p>
<p><strong>Tip:</strong> You can also use the blank <em>Physical Count</em> column when conducting a physical inventory for reconciliation purposes.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="select-location-for-report-data">Select location for report data</h5></td>
<td><p>Select Inventory Reports Option: <strong>WS</strong> <strong>&lt;Enter&gt;</strong> Print Stock Work Sheet</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Enter 'ALL' for all Locations or 'RETURN' to select individual Locations: <strong>&lt;Enter&gt;</strong></p>
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
<p>UNIT PHYSICAL</p>
<p>HCPCS ITEM DATE COST VENDOR QTY LOCATION COUNT</p>
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
<p>UNIT PHYSICAL</p>
<p>HCPCS ITEM DATE COST VENDOR QTY LOCATION COUNT</p>
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

#### Print PIP/IFCAP Item Report (IP)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-description-1">Report description</h5></td>
<td><blockquote>
<p>The <strong>Print PIP/IFCAP Item Report (IP)</strong> report prints all PIP Items and the corresponding IFCAP Items. If this report does NOT print an IFCAP Item and this column is blank, then Prosthetics users must edit the HCPCS/Item. When an IFCAP Item is entered, then there is a link to the PIP Item and it displays on this report.</p>
<p><strong>Note:</strong> This report is useful for checking if the IFCAP Item is correctly linked to the PIP Item.</p>
</blockquote></td>
</tr>
</tbody>
</table>

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
<p><strong>IP Print PIP/IFCAP Item Report</strong></p>
<p>Select Inventory Reports Option: <strong>IP &lt;Enter&gt;</strong> Print PIP/IFCAP Item Report</p>
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
<p>HCPCS-ITEM PIP ITEM <strong>IFCAP ITEM</strong></p>
<p>---------- -------- ----------</p>
<p>A4254-1 BATTERY FOR GLUCOSE BEEF-ROUND/TOP/INSIDE/FRZN</p>
<p>A4254-2 BAT FOR GLUCOSE MONI BEEF-ROUND/TOP/INSIDE/FRZN</p>
<p>A4254-3 EYEGLASSES BEEF-ROUND/TOP/INSIDE/FRZN</p>
<p>A4259-1 LANCETS PER BOX/COMM WHEELCHAIR-CLASSIC-18X16</p>
<p>A4301-1 WHEELCHAIR-ADULT/HEM SHOES</p>
<p>A4373-1 WHEELCHAIR - ELECTRI WHEELCHAIR - ELECTRIC</p>
<p>A4373-2 WC MAN WHEELCHAIR - MANUAL</p>
<p>A4402-2 LANCETS PER BOX/COMM OXYGEN DEVICE</p>
<p>A4404-1 OSTOMY RING EACH/COM OXYGEN CONCENTRATOR</p>
<p>A4404-2 OSTOMY RING EACH/COM <em><strong>BLANK!!</strong></em></p>
<p>A4404-3 EYEGLASSES EYEGLASSES</p>
</blockquote></td>
</tr>
</tbody>
</table>