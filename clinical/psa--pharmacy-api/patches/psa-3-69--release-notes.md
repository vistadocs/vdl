---
title: PSA*3*69 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: PSA
app_name: "Pharmacy: Drug Accountability"
section: CLI
app_status: active
pkg_ns: PSA
patch_ver: 3
patch_id: PSA*3*69
group_key: "PSA:PSA:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - batch
  - class
  - credit
  - return
  - table
  - style
  - width
  - drug
  - contracting
page_count: 0
word_count: 1568
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Drug_Accountability/psa_3_p69_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Drug_Accountability/psa_3_p69_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=87"
---

> ![](psa-3-69-release-notes/001.png)

DRUG ACCOUNTABILITY/ INVENTORY INTERFACE V. 3.0

> RELEASE NOTES

## PSA\*3\*69 May 2009

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Enterprise Development

> *(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [PSA\3\69 May 2009](#psa369-may-2009)
- [Introduction](#introduction)
- [Batch Work List](#batch-work-list)
- [Batch Complete List](#batch-complete-list)
- [View/Update Batch](#viewupdate-batch)
- [Return Drug Credit Report](#return-drug-credit-report)
> PSA\*3\*69 provides a new module enhancement for the Drug Accountability application. From the main menu, *Drug Accountability Menu* \[PSA DRUG ACCOUNTABILITY MENU\] option, *Return Drug Credit Menu* has been added.
> The new module is being added to the Drug Accountability application to address one of the findings in the GAO Report GAO-04-755 dated July 2004 related to implementing better control over return drug credits. The new module, *Return Drug Credit Menu*, contains the following four options.
> These options can be used to document and track drugs that are awaiting return. When the drugs, or items, are returned, the options can be used to document and track the items’ credit from them awaiting credit to estimating the credit that will be received to the actual credit received.
> The *Return Drug Credit Menu* \[PSA RET DRG MENU\] option is accessible for users holding the PSORPH (pharmacist key) security key. Other users must be assigned the PSORET security key before they can access this menu.
> The following information provides descriptions of the four new options within the new module.

# Batch Work List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG BATCH WORKLIST\]

> The *Batch Work List* option allows the user to add, edit, pick up, complete, or cancel a batch in addition to update credits and edit and cancel individual items. Only items with a status of Awaiting Pickup and Picked Up are displayed in this option.

> To complete the process of returning drugs for credit, perform the following steps.

1.  Add a return contractor (first time)
    1.  The user must first have a return contractor defined before they can add a batch with items for return.
    2.  From the “Return Drug Batch List” screen, type CON at the “Select Action” prompt and add the return contractor information.
2.  Add a batch (example follows)
    1.  Each new batch is automatically assigned the status of Awaiting Pickup.
    2.  The user can edit the batch information from the “Return Drug Batch” screen.
3.  Add items (drugs) to the batch (example follows)
    1.  The user can enter the following information about the item being returned.
        - Drug\* • Manufacturer
        - National Drug Code (NDC) • Order Unit\*
        - Dispense Unit • Number of Dispense Unit per Order Unit\*
        - Number of Order Units\* • Number of Dispense Units\*
        - Universal Product Code (UPC)
- Expiration Date
  - Return Reason\* • Update Inventory\*

> \*Required fields

1.  If a user edits an item, the changes to the fields are saved, and the activity log is updated and displays the changes below the drug information on the “Return Drug Item” screen.
4.  Pick up the batch (example follows)
    1.  After all items have been entered into a batch and when the return contractor is ready to physically pick up the drugs, the batch status is changed to Picked Up. At this point, credits can be entered for each item in the batch.
5.  Update credit (example follows)
    1.  On the “Return Drug Batch” screen, the “Total Batch Credit” reflects the total actual credit amount that has been entered for each item in the batch. If only an estimated amount has been entered, the “Total Batch Credit” will still be \$0.00.
6.  Complete the batch (example follows)
    1.  After the batch has been picked up and all credits have been updated, the user can complete the batch. The batch status is changed from Picked Up to Completed. And, the batch has moved from being displayed under the *Batch Work List* option to being displayed under the *Batch Complete List* option. This also finishes the process of returning drugs for credit.
    2.  NOTE: Any item without an actual credit amount is marked DENIED when the batch is being completed and a message appears before the user can continue completing the batch as shown in the following example.

> Example: Adding a Batch

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 31%" />
<col style="width: 8%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>#</p>
</blockquote></th>
<th><blockquote>
<p>BATCH #</p>
</blockquote></th>
<th><blockquote>
<p>CREATED</p>
</blockquote></th>
<th><blockquote>
<p>PICKED UP COMPLETED</p>
<p>AWAITING PICKUP</p>
</blockquote></th>
<th>CREDIT</th>
<th>RETURN CONTRACTOR ITEMS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>0908-001</p>
</blockquote></td>
<td><blockquote>
<p>09/04/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 14</td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>0908-002</p>
</blockquote></td>
<td><blockquote>
<p>09/05/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 1</td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>0908-003</p>
</blockquote></td>
<td><blockquote>
<p>09/06/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>ANWER CONTRACTING CO 2</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>0908-005</p>
</blockquote></td>
<td><blockquote>
<p>09/07/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>JEN MANUFACTURING 1</td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>0908-006</p>
</blockquote></td>
<td><blockquote>
<p>09/08/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 6</td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>0908-007</p>
</blockquote></td>
<td><blockquote>
<p>09/09/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 5</td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>0908-008</p>
</blockquote></td>
<td><blockquote>
<p>09/10/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 10</td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>0908-009</p>
</blockquote></td>
<td><blockquote>
<p>09/11/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 8</td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>0908-010</p>
</blockquote></td>
<td><blockquote>
<p>09/12/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 7</td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>0908-011</p>
</blockquote></td>
<td><blockquote>
<p>09/13/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>0908-012</p>
</blockquote></td>
<td><blockquote>
<p>09/14/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 12</td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>0908-013</p>
</blockquote></td>
<td><blockquote>
<p>09/15/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 5</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>0908-017</p>
</blockquote></td>
<td><blockquote>
<p>09/16/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 4</td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>0908-018</p>
</blockquote></td>
<td><blockquote>
<p>09/17/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>0908-019</p>
</blockquote></td>
<td><blockquote>
<p>09/18/08</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>MORRISON CONTRACTING 0</td>
</tr>
</tbody>
</table>

> Example: Adding Items to a Batch

> Example: Picking up a Batch and Updating Credits

> <span id="_bookmark2" class="anchor"></span>Example: Completing a Batch with One Item Denied

> Return Drug Batch Sep 19, 2008@10:15:06 Page: 1 of 1

> Pharm Location: OUTPATIENTNo Inpatient or Outpat Date Created: 09/19/08@10:08 Batch Number : 0908-020 Status: PICKED UP

> Rtn Contractor: MORRISON CONTRACTING SERVICES Date Picked Up: 09/19/08@10:13 Reference \# : 2242 Total Batch Credit: \$135.00

> ORD ORDER DISP DISP ACTUAL

> \# RETURN DRUG (NDC) QTY UNIT QTY UNIT CREDIT(\$)

1.  BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET 0.00
2.  MEDROXYPROGESTERONE 100MG (00009-0248-02) 15 BOX 15 VIAL 60.00

> 3 MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET 75.00

> Enter ?? for more actions

> ADD New Item CRE Credit Update SEL Select Item

> EDT Edit Batch PKP Pick up Batch

> CAN Cancel Batch COM Complete Batch Select Action: Quit// COM \<Enter\> Complete Batch

> WARNING: The following items will have their CREDIT STATUS set to DENIED because no credit amount has been entered for them:

> RETURN DRUG (NDC) DISP QTY UNIT

> BACLOFEN 10MG TABS (00028-0023-01) 3 TABLET

> Complete Batch? NO// YES \<Enter\>

> Completing Batch...OK

> Note: See *Drug Accountability/Inventory Interface V. 3.0 User Manual* for more details.

# Batch Complete List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG BAT COMPLETE LIST\]

> The *Batch Complete List* option allows the user to view a comprehensive list of the batches with any status: Awaiting Pickup, Picked Up, Cancelled, and Completed. Additional features include editing the contractor/manufacturer and adding/editing/cancelling a batch and an item as done from the *Batch Work List* \[PSA RET DRG BATCH WORKLIST\] option.

# View/Update Batch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG VIEW/UPDATE BATCH\]

> The *View/Update Batch* option allows the user to avoid extra steps and go straight to the batch if the batch number or the contractor reference \# are known. The “Return Drug Batch List” screen is available then allowing the user to add, edit, pick up, complete, or cancel a batch in addition to update credits and edit and cancel items all as done from the *Batch Work List* option.

# Return Drug Credit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSA RET DRG REPORT\]

> The *Return Drug Credit Report* option allows the user to produce reports, either detailed or summarized, on the batches. Use filtering information to include the batches of interest.

> On the summary format report, the “ACTUAL CREDIT\$” column is included on reports that have a STATUS of COMPLETED only. On the detailed format report, the “Total Batch Credit” is included on reports that have a STATUS of COMPLETED only.

> Example: Report – Summary Format

<table style="width:100%;">
<colgroup>
<col style="width: 30%" />
<col style="width: 31%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>Return Drug Credit Report (SUMMARY) Page: 1 PHARM LOCATION: OUTPATIENTNo Inpatient or Outpa STATUS: COMPLETED</p>
<p>Date Range: 09/19/08 THRU 09/19/08 Run Date: 09/19/08@10:16:17</p>
</blockquote></th>
<th rowspan="5"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>DRUG (NDC)</p>
</blockquote></th>
<th><blockquote>
<p>ORD ORDER QTY UNIT</p>
</blockquote></th>
<th><blockquote>
<p>DISP DISP QTY UNIT</p>
</blockquote></th>
<th><blockquote>
<p>UPD INV</p>
</blockquote></th>
<th><blockquote>
<p>ACTUAL CREDIT$</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>Batch #: 0908-020 Date Completed: 09/19/08 - MORRISON CONTRACTING SERVICES BACLOFEN 10MG TABS (00028-0023-01) 3 BOTTLE 3 TABLET NO</p>
<p>MEDROXYPROGESTERONE (00009-0248-02) 15 BOX 15 VIAL NO 60.00</p>
<p>MEPERIDINE 50MG TAB (00555-0381-04) 5 BOTTLE 2500 TABLET NO 75.00</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="5"><p>========</p>
<blockquote>
<p>BATCH ENTRIES: 3 BATCH TOTAL: $135.00</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>CREDIT TOTAL: $135.00</p>
<p>Enter RETURN to continue or '^' to exit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Report – Detailed Format

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 22%" />
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 24%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>Return Drug Credit Report (DETAILED) Page: 1 PHARM LOCATION: OUTPATIENTNo Inpatient or Outpatient Sit BATCH #: 0908-020 CONTRACTOR/MFR: MORRISON CONTRACTING SERVICES STATUS: COMPLETED</p>
<p>Date Range: 09/19/08 THRU 09/19/08 Run Date: 09/19/08@10:16:58 Total Batch Credit: $135.00</p>
</blockquote></th>
<th rowspan="7"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Drug: Manufacturer:</p>
<p>NDC:</p>
<p>Rtrn Ord Qty: Rtrn Disp Qty:</p>
<p>UPC:</p>
</blockquote>
<p>Return Rsn:</p></th>
<th><p>BACLOFEN 10MG TABS TEST MFR</p>
<p>00028-0023-01</p>
<p>3 BOTTLE</p>
<p>3 TABLET</p>
<p>DAMAGED</p></th>
<th></th>
<th><blockquote>
<p>Credit Status: Credit Amount: Exp. Date: Created By: Created On: Upd Inventory:</p>
</blockquote></th>
<th><blockquote>
<p>DENIED</p>
<p>09/15/09</p>
<p>USER,ONE 09/19/08 NO</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Drug: Manufacturer:</p>
<p>NDC:</p>
<p>Rtrn Ord Qty: Rtrn Disp Qty:</p>
<p>UPC:</p>
</blockquote>
<p>Return Rsn:</p></th>
<th><p>MEDROXYPROGESTERONE TEST MFR</p>
<p>00009-0248-02</p>
<p>15 BOX</p>
<p>15 VIAL</p>
<p>DAMAGED</p></th>
<th><blockquote>
<p>100MG</p>
</blockquote></th>
<th><blockquote>
<p>Credit Status: Credit Amount: Exp. Date: Created By: Created On: Upd Inventory:</p>
</blockquote></th>
<th><blockquote>
<p>ACTUAL</p>
<p>$60.00 (ACTUAL) 10/31/09 USER,ONE 09/19/08</p>
<p>NO</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>Press ENTER to Continue or ^ to Exit:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>Return Drug Credit Report (DETAILED) Page: 2 PHARM LOCATION: OUTPATIENTNo Inpatient or Outpatient Sit BATCH #: 0908-020 CONTRACTOR/MFR: MORRISON CONTRACTING SERVICES STATUS: COMPLETED</p>
<p>Date Range: 09/19/08 THRU 09/19/08 Run Date: 09/19/08@10:17:13 Total Batch Credit: $135.00</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Drug: Manufacturer:</p>
<p>NDC:</p>
<p>Rtrn Ord Qty: Rtrn Disp Qty:</p>
<p>UPC:</p>
</blockquote>
<p>Return Rsn:</p></th>
<th><p>MEPERIDINE 50MG TAB TEST MFR</p>
<p>00555-0381-04</p>
<p>5 BOTTLE 2500 TABLET</p>
<p>EXPIRED</p></th>
<th></th>
<th><blockquote>
<p>Credit Status: Credit Amount: Exp. Date: Created By: Created On: Upd Inventory:</p>
</blockquote></th>
<th><blockquote>
<p>ACTUAL</p>
<p>$75.00 (ACTUAL) 07/01/08 USER,ONE 09/19/08</p>
<p>NO</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Enter RETURN to</p>
</blockquote></th>
<th><blockquote>
<p>continue or '^' to</p>
</blockquote></th>
<th><blockquote>
<p>exit:</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>