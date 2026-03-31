---
title: RMPR*3*70 HCPCS Update and Read Only 2319 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: HCPCS Update and Read Only 2319
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*70
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h5 id=\\"introduction\\">Introduction</h5></td> <td><blockquote> <p>The purpose of this patch is to update a list of HCPCS in Prosthetics HCPCS file (#661.1) and to transport two Prosthetic"
audience: 
keywords: 
  - strong
  - table
  - rmpr
  - colgroup
  - style
  - width
  - tbody
  - blockquote
  - vendor
  - transactions
page_count: 0
word_count: 1667
section_count: 3
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_70.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_70.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [## HCPCS Update and Read Only 2319](#hcpcs-update-and-read-only-2319)
  - [Patch RMPR\3\70 Release Notes](#patch-rmpr370-release-notes)
![](rmpr-3-70-hcpcs-update-and-read-only-2319-release-notes/001.png)
Prosthetics Patch RMPR\*3\*70Release NotesHCPCS Update and Read Only 2319
September 2002
V*IST*A System Design and Development

## ## HCPCS Update and Read Only 2319

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch RMPR\*3\*70 Release Notes

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
<p>The purpose of this patch is to update a list of HCPCS in Prosthetics HCPCS file (#661.1) and to transport two Prosthetics options as follows:</p>
</blockquote>
<ul>
<li><p>RMPR View 2319 Read Only (User option)</p></li>
<li><p>RMPR Auto Fix (IRM option)</p></li>
</ul>
<blockquote>
<p>This HCPCS correction will take place during the post-init. Due to CPU intensive processing, it is recommended to schedule the RMPR AUTO FIX option to run on the weekend, once a week.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="rmpr-view-2319-read-only">RMPR View 2319 Read Only</h5></td>
<td><blockquote>
<p>The option, View Prosthetics Item Transactions (RMPR VIEW 2319 READ ONLY) can be added to a menu for use mainly by non-Prosthetics users. It can be given to any user who has the need to see the Prosthetics patient’s transactions or items issued.</p>
<p>This option allows you to view or print the patient’s Item Transactions and Home Oxygen Items issued to a particular patient.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="rmpr-auto-fix">RMPR Auto Fix</h5></td>
<td><blockquote>
<p>The option, NPPD Auto Fix (RMPR AUTO FIX) is a taskman option for checking the RECORD OF PROS APPLIANCE/REPAIR file (#660), and switch Transaction Type Initial Issue (New) to Repair or Repair to Initial Issue (New).</p>
<p>This option will send a mailman message to the RMPR INVENTORY mail group for all patient’s transactions that have been switched. It is recommended to task this option on the weekend, once a week.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="contents">Contents</h5></td>
<td>This document contains the following topics:</td>
</tr>
</tbody>
</table>

|                                         |          |
|-----------------------------------------|----------|
| Topic                                   | See Page |
| RMPR View 2319 Only - Item Transactions | 3        |
| RMPR View 2319 Only - Home Oxygen Items | 4        |
| For IRM: RMPR Auto Fix                  | 5        |

#### RMPR View 2319 Read Only – Item Transactions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="item-transactions">Item Transactions</h5></td>
<td><blockquote>
<p>Below is a sample of the prompts that display when accessing the <strong>RMPR View 2319 Read Only</strong> option and selecting <strong>Item Transactions</strong>.</p>
</blockquote></td>
</tr>
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
<td><p>Select OPTION NAME: <strong>RMPR VIEW</strong> <strong>2319 READ ONLY</strong> <strong>&lt;Enter&gt;</strong> View Prosthetics Item Transactions</p>
<p>SITE: HINESTEST <strong>&lt;Enter&gt;</strong> 999</p>
<p>Select PROSTHETIC PATIENT: PROSPATIENT,ONE <strong>&lt;Enter&gt;</strong> PROSPROVIDER,ONE 1-1-30 000000001 NO PILL</p>
<p>Enter &lt;RETURN&gt; to continue.</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>HINES, IL</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p><strong>I ITEM TRANSACTIONS</strong></p>
<p>H HOME OXYGEN ITEMS</p>
<p>Enter DATA screen to VIEW (Item Transactions or Home Oxygen),'^' to EXIT, or 'return' to continue <strong>: ITEM TRANSACTIONS &lt;Enter&gt;</strong></p>
<p>PROSPATIENT,ONE SSN: 000-00-0001 DOB: JAN 1,1930 CLAIM#</p>
<p>Date Qty Item Type Vendor Sta Serial Delivery Date Tot Cost</p>
<p>1. 08/19/02 1 EYEGLASSES I VENDOR,ONE 499 23.00</p>
<p>2. 08/19/02 SHIPPING X VENDOR,ONE 499 2.00</p>
<p>3. 07/09/02 1 SYRINGE- I VENDOR,ONE 499 1.00</p>
<p>4. 07/08/02 1 EYEGLASSES X VENDOR,ONE 499 07/08/02 35.00</p>
<p>This appears on the 2319</p>
<p>5. 07/08/02 1 EYEGLASSES I VENDOR,ONE 499 07/08/02 35.00</p>
<p>6. 07/05/02 2 SHOE COMPO X VENDOR,ONE 499 07/05/02 40.00</p>
<p>1SDFSD</p>
<p>7. 07/05/02 1 EYEGLASSES X VENDOR,ONE 499 07/05/02 50.00</p>
<p>8. 07/03/02 1 EYEGLASSES I VENDOR,ONE 499 07/03/02 35.00</p>
<p>9. 07/03/02 1 SHOES I VENDOR,ONE 499 DSF S 07/03/02 15.00</p>
<p>10. 06/26/02 1 SHOES I VENDOR,ONE 499 102.50</p>
<p>Diabetic Shoes, L/R Close Out Dia.Shoes</p>
<p>+=Turned-In *=Historical Data I=Initial X=Repair S=Spare R=Replacement</p>
<p>Enter 1-10 to show full entry, '^' to exit or `return` to continue. <strong>1 &lt;Enter&gt;</strong></p>
<p>PROSPATIENT,ONE SSN: 000-89-0765 SUPPORT ISC DOB: 01-01-1930</p>
<p>APPLIANCE/REPAIR LINE ITEM DETAIL &lt;4-1&gt;</p>
<p>TYPE OF FORM: 2421 INITIATOR: PROSPROVIDER,TWO DATE: AUG 19, 2002</p>
<p>DELIVER TO: VETERAN</p>
<p>TYPE TRANS: INITIAL ISSUE QTY: 1 SOURCE: COMMERCIAL</p>
<p>VENDOR: VENDOR,ONE</p>
<p>CORPORATE ORDER ENTRY</p>
<p>VENDOR PARK, ILLINOIS 60064</p>
<p>DELIVERY DATE:</p>
<p>TOTAL COST: $23.00</p>
<p>REMARKS:</p>
<p>DISABILITY SERVED: SC/OP</p>
<p>APPLIANCE: EYEGLASSES</p>
<p>PSAS HCPCS: V2025 EYEGLASSES DELUX FRAMES</p>
<p>ICD-9 Code:</p>
<p>CPT MODIFIER: LT,RT,GY</p>
<p>DESCRIPTION: TESTING</p>
<p>EXTENDED DESCRIPTION:</p>
<p>Enter RETURN to continue or '^' to exit:</p></td>
</tr>
</tbody>
</table>

#### RMPR View 2319 Read Only – Home Oxygen Items

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="home-oxygen-items">Home Oxygen Items</h5></td>
<td><blockquote>
<p>Below is a sample of the prompts that display when accessing the <strong>RMPR View 2319 Read Only</strong> option and selecting <strong>Home Oxygen Items</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-1">Screen Sample</h5></td>
<td><p>Select one of the following:</p>
<p>I ITEM TRANSACTIONS</p>
<p><strong>H HOME OXYGEN ITEMS</strong></p>
<p>Enter DATA screen to VIEW (Item Transactions or Home Oxygen),'^' to EXIT, or 'return' to continue : <strong>HOME OXYGEN ITEMS</strong> <strong>&lt;ENTER&gt;</strong></p>
<p>PATIENT,TWO 000-00-0002P</p>
<p>Current Prescription (#4)</p>
<p>Active Date: JUL 23,2001 Expiration Date: JUL 23,2001</p>
<p>Enter RETURN to continue or '^' to exit: <strong>&lt;ENTER&gt;</strong></p>
<p>PATIENT,TWO SSN: 000-00-0002P DOB: DEC 27,1950 CLAIM# 101122750P</p>
<p>Date Qty Item Type Vendor Sta Serial Delivery Date Tot Cost</p>
<p><strong>1.</strong> <strong>09/25/00 1 OXYGEN LIQ I INLANDER B 500 09/25/00 23.00</strong></p>
<p>2. 03/24/00 1 OXYGEN TAN I GENERAL SE ST. NUM. 578 03/24/00 1.00</p>
<p>End of Home Oxygen records for this veteran!</p>
<p>+=Turned-In *=Historical Data I=Initial X=Repair S=Spare R=Replacement</p>
<p>Enter 1-2 to show full entry, '^' to exit or `return` to continue. <strong>1</strong> <strong>&lt;ENTER&gt;</strong></p>
<p>PROSPATIENT,TWO SSN: 000-00-0002P CORKWELL DOB: 12-27-1950</p>
<p>APPLIANCE/REPAIR LINE ITEM DETAIL &lt;4-1&gt;</p>
<p>TYPE OF FORM: OTHER INITIATOR: PROSPROVIDER,TWO DATE: SEP 25, 2000@11:56</p>
<p>DELIVER TO:</p>
<p>TYPE TRANS: INITIAL ISSUE QTY: 1 SOURCE: COMMERCIAL</p>
<p>VENDOR: PROSVENDOR,TWO</p>
<p>7701 SOUTH CLAREMONT</p>
<p>CHICAGO, ILLINOIS 60620</p>
<p>DELIVERY DATE: SEP 25, 2000@12:25:15</p>
<p>TOTAL COST: $23.00</p>
<p>REMARKS:</p>
<p>DISABILITY SERVED: SC/OP</p>
<p>APPLIANCE: OXYGEN LIQUID</p>
<p>PSAS HCPCS: E0431 PORTABLE OXYGEN</p>
<p>ICD-9 Code:</p>
<p>CPT MODIFIER: GX</p>
<p>DESCRIPTION:</p>
<p>EXTENDED DESCRIPTION:</p>
<p>Enter RETURN to continue or '^' to exit:</p></td>
</tr>
</tbody>
</table>

#### For IRM: RMPR Auto Fix

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="taskman-option-for-irm">Taskman Option for IRM</h5></td>
<td><blockquote>
<p>The option, NPPD Auto Fix (RMPR AUTO FIX) is a taskman option for checking the RECORD OF PROS APPLIANCE/REPAIR file (#660), and switch Transaction Type Initial Issue (New) to Repair or Repair to Initial Issue (New).</p>
<p>To schedule this taskman option, follow these screen prompts below for the NPPD Auto Fix. Due to CPU intensive processing, it is recommended to schedule this option to run on the weekend, once a week.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-2">Screen sample</h5></td>
<td><p>Select OPTION NAME: <strong>TASKMAN MANAGEMENT</strong> <strong>&lt;Enter&gt;</strong></p>
<p><strong>Schedule/Unschedule Options</strong></p>
<p>One-time Option Queue</p>
<p>Taskman Management Utilities ...</p>
<p>List Tasks</p>
<p>Dequeue Tasks</p>
<p>Requeue Tasks</p>
<p>Delete Tasks</p>
<p>Print Options that are Scheduled to run</p>
<p>Cleanup Task List</p>
<p>Print Options Recommended for Queuing</p>
<p>Select Taskman Management Option: <strong>SCHEDULE/UNSCHEDULE OPTIONS</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Select OPTION to schedule or reschedule: <strong>RMPR AUTO FIX</strong> <strong>&lt;Enter&gt;</strong> NPPD Auto Fix</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Option Name: RMPR AUTO FIX</p>
<p>Menu Text: NPPD Auto Fix TASK ID: 376101</p>
<p>__________________________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: SEP 14,2002@05:00</p>
<p>DEVICE FOR QUEUED JOB OUTPUT:</p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 7D</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>______________________________________________________________________________</p>
<p>Exit Save Next Page Refresh</p>
<p>Command: Exit <strong>&lt;Enter&gt;</strong></p>
<p>Save changes before leaving form (Y/N)? <strong>Yes</strong> <strong>&lt;Enter&gt;</strong></p>
<blockquote>
<p>Select OPTION to schedule or reschedule:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="mailman-message">Mailman Message</h5></td>
<td><blockquote>
<p>This option will send a mailman message to RMPR INVENTORY mail group for all patients’ transactions that have been switched.</p>
</blockquote></td>
</tr>
</tbody>
</table>