---
title: RMPR*3*56 Home Oxygen Patient Template Update Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Home Oxygen Patient Template Update
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*56
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 1
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td>Introduction</td> <td><blockquote> <p>The new <strong>Home Oxygen Patient Template Update</strong> [RMPR HO PAT TEMPLATE UPDATE] menu option has been added to the <strong>Home Oxygen Mai"
audience: 
keywords: 
  - strong
  - update
  - oxygen
  - blockquote
  - table
  - colgroup
  - style
  - width
  - tbody
  - home
page_count: 0
word_count: 2274
section_count: 0
table_count: 16
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_56.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_56.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

RMPR\*3\*56 – Release Notes

Home Oxygen Patient Template Update

Patch Description

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The new <strong>Home Oxygen Patient Template Update</strong> [RMPR HO PAT TEMPLATE UPDATE] menu option has been added to the <strong>Home Oxygen Main</strong> <strong>Menu</strong>.</p>
<p>This option will allow users with RMPRSUPERVISOR key to update or change the Home Oxygen Patient template. Under this option, Prosthetics users will be able to update the following:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Vendor</p>
</blockquote></li>
<li><blockquote>
<p>PSAS HCPCS</p>
</blockquote></li>
<li><blockquote>
<p>Fund Control Point (FCP)</p>
</blockquote></li>
<li><blockquote>
<p>Item</p>
</blockquote></li>
<li><blockquote>
<p>Unit Cost.</p>
</blockquote></li>
</ul>
<blockquote>
<p>The purpose of this patch is to allow you to change any of the above options for multiple active Home Oxygen patients (and those that have a future inactivation date) in all patient templates <strong>at one time</strong>. This provides a more efficient method of updating instead of accessing one patient at a time.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Home Oxygen Main Menu screen</td>
<td><blockquote>
<p>Select Prosthetic Official's Menu Option: <strong>Home Oxygen Main Menu</strong></p>
<p>ED Add/Edit Home Oxygen Patient</p>
<p>IN Inactivate/Activate Oxygen Patient</p>
<p>LE Generate Letters</p>
<p>BT Billing Transactions</p>
<p>RE Reports ...</p>
<p>SI Site Parameters Enter/Edit</p>
<p>PB Verify Posted Billing Transactions</p>
<p>SO Purchase Card Sign Off</p>
<p><strong>TU Home Oxygen Patient Template Update</strong></p>
<p>Select Home Oxygen Main Menu Option: Home Oxygen Patient Template Update &lt;<strong>Enter</strong>&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                             |          |
|-------------------------------------------------------------|----------|
| Topic                                                       | See Page |
| Update a Vendor for a Home Oxygen Patient                   | [2](\l)  |
| Update a HCPCS Code for a Home Oxygen Patient               | [4](\l)  |
| Update a Fund Control Point (FCP) for a Home Oxygen Patient | [5](\l)  |
| Update an Item for a Home Oxygen Patient                    | [6](\l)  |
| Update a Unit Cost for an Item for a Home Oxygen Patient    | [7](\l)  |

Update a Vendor for a Home Oxygen Patient

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>You can change a vendor for all active Home Oxygen patients and for patients who have a future inactivation date using the <strong>Update Vendor</strong> option from the <strong>Home Oxygen Patient Template Update</strong> option.</p>
<p><strong>NOTE: If the home oxygen vendor you want is NOT listed and available for selection, you must FIRST add the vendor, from the IFCAP Vendor File, to the <em>Site Parameter Enter/Edit</em> option under the <em>Home Oxygen Main Menu</em>. You can then return to the Home Oxygen Patient Template Update option to now view and select it.</strong></p>
</blockquote></td>
</tr>
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
<p>To update a vendor for a Home Oxygen patient(s), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                              |
| 1    | At the *Site* prompt, press the Spacebar and then press \<Enter\> to select the default site or type a question mark to display a list of selection options and choose one.             |
| 2    | At the *Type of Update* prompt, press \<Enter\> to accept the default for the Update Vendor option.                                                                                     |
| 3    | At the *Enter Existing Vendor to Update* prompt, you can type the name of the vendor to be updated or type a question mark and then press \<Enter\> to display a list and select an option. |
| 4    | At the *OK?* prompt, press \<Enter\> to accept the entry.                                                                                                                                   |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Update Vendor option screen</td>
<td><blockquote>
<p>Select SITE: Hines Development System <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p><strong>1 Update VENDOR</strong></p>
<p>2 Update HCPCS</p>
<p>3 Update FCP</p>
<p>4 Update ITEM</p>
<p>5 Update UNIT COST</p>
<p>Type of Update: Update VENDOR// <strong>&lt;Enter&gt;</strong></p>
<p>Enter Existing Vendor to Update: <strong>? &lt;Enter&gt;</strong></p>
<p>Answer with HOME OXYGEN VENDOR HOME OXYGEN VENDORS</p>
<p>Choose from:</p>
<p>PROSVENDOR,ONE</p>
<p>PROSVENDOR, TWO</p>
<p>Enter Existing Vendor to Update: PROSVENDOR,ONE <strong>&lt;Enter&gt;</strong> PROSVENDOR,ONE</p>
<p>ORD ADD:CORPORATE ORDER ENTRY FMS:</p>
<p>ANY PARK, IL 60064 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
</blockquote></td>
</tr>
</tbody>
</table>

*Screen to be continued on next page.*

Continued on next page

Update a Vendor for a Home Oxygen Patient, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Updating a Vendor</td>
<td><blockquote>
<p>When the <strong>Update Vendor</strong> option is used, it changes the vendor for all active Home Oxygen patients and all patients who have a future inactivation date.</p>
</blockquote></td>
</tr>
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
<p>To continue to update a vendor for a Home Oxygen patient(s), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                                 |
| 5    | At the *Enter New Vendor* prompt, you can type the name of the new vendor and press \<Enter\> or type a question mark to display a list and then press \<Enter\> and select a vendor option from the list. |
| 6    | At the *OK?* prompt, press \<Enter\> to accept the entry.                                                                                                                                                      |
| 7    | The system displays the number of records that are updated.                                                                                                                                                            |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Update Vendor option screen</td>
<td><blockquote>
<p>Enter NEW Vendor: <strong>? &lt;Enter&gt;</strong></p>
<p>Answer with HOME OXYGEN VENDOR HOME OXYGEN VENDORS</p>
<p>Choose from:</p>
<p>PROSVENDOR, TWO</p>
<p>Enter NEW Vendor: <strong>PROSVENDOR, TWO</strong> PROSVENDOR, TWO EDIPH:312</p>
<p>ORD ADD:7701 SOUTH St FMS:TEST TEST</p>
<p>CHICAGO, IL 60620 CODE: FAX:</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Updating HO template for vendor PROSVENDOR,ONE to PROSVENDOR, TWO..</p>
<p><strong> 4 Records updated </strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Update a HCPCS Code for a Home Oxygen Patient

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>The <strong>Update HCPCS</strong> option is used to change a HCPCS code to another HCPCS code. You will need to know the HCPCS code when you begin the process to change it in the prosthetics system.</p>
<p>When this option is used, it changes the HCPCS code for all active Home Oxygen patients and all patients who have a future inactivation date.</p>
</blockquote></td>
</tr>
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
<p>To update a HCPCS code for a Home Oxygen patient(s), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                                                                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                                                                                                                                                                     |
| 1    | At the *Site* prompt, press the Spacebar and then press \<Enter\> to select the default site or type a question mark and press \<Enter\> to display a list of selection options and choose one.                                                                                                                                            |
| 2    | At the *Type of Update* prompt, type 2 for the Update HCPCS option and press \<Enter\>.                                                                                                                                                                                                                                                    |
| 3    | At the *Enter Existing HCPCS to Update* prompt, you can type the HCPCS code to be updated and press \<Enter\>. Note: You can also type a question mark and press \<Enter\>. If you do, you will be asked the following: Do you want the entire 2121-Entry PROSTHETIC HCPCS List? If you answer yes, then you can select an option from a list. |
| 4    | At the *Enter New HCPCS* prompt, type the new HCPCS code and press \<Enter\>.                                                                                                                                                                                                                                                                      |
| 5    | The system displays the number of records that are updated.                                                                                                                                                                                                                                                                                                |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Update HCPCS option screen</td>
<td><blockquote>
<p>Select SITE: Hines Development System <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p>1 Update VENDOR</p>
<p><strong>2 Update HCPCS</strong></p>
<p>3 Update FCP</p>
<p>4 Update ITEM</p>
<p>5 Update UNIT COST</p>
<p>Type of Update: Update VENDOR// <strong>2</strong> <strong>&lt;Enter&gt;</strong> Update HCPCS</p>
<p>Enter Existing HCPCS to Update: <strong>E1350</strong> <strong>&lt;Enter&gt;</strong> OXYGEN REPAIR OR SERVICE  inactive HCPCS </p>
<p>Enter NEW HCPCS: <strong>E1383</strong> <strong>&lt;Enter&gt;</strong> OXYGEN CONCENTRAT TO 1708 CU</p>
<p>Updating HO template for HCPCS E1350 to E1383......</p>
<p><strong> 1 Records updated </strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Update a Fund Control Point (FCP) for a Patient

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>The <strong>Update FCP</strong> option can be used to update a Fund Control Point (FCP) to another FCP. You will need to know the FCP or you can enter a question mark to view the available entries for selection. This option changes the FCP for all active Home Oxygen patients and all patients who have a future inactivation date.</p>
<p><strong>NOTE: If the FCP you want is NOT listed and available for selection, you must FIRST add the FCP to the <em>Site Parameter Enter/Edit</em> option under the <em>Home Oxygen Main Menu</em>. You can then return to the Home Oxygen Patient Template Update option to now view and select it.</strong></p>
</blockquote></td>
</tr>
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
<p>To update a Fund Control Point for a Home Oxygen patient(s), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                  |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                           |
| 1    | At the *Site* prompt, press the Spacebar and then press \<Enter\> to select the default site or type a question mark to display a list of selection options and choose one.          |
| 2    | At the *Type of Update* prompt, type 3 for the Update FCP option and press \<Enter\>.                                                                                            |
| 3    | At the *Enter Existing Fund Control Point to Update* prompt, you can type the FCP to be updated or type a question mark and then press \<Enter\> to display a list and select an option. |
| 4    | At the *Enter New Fund Control Point* prompt, type the new FCP and press \<Enter\>. The system displays the number of records that are updated.                                          |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Update FCP option screen</td>
<td><blockquote>
<p>Select SITE: Hines Development System <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p>1 Update VENDOR</p>
<p>2 Update HCPCS</p>
<p><strong>3 Update FCP</strong></p>
<p>4 Update ITEM</p>
<p>5 Update UNIT COST</p>
<p>Type of Update: Update VENDOR// <strong>3</strong> <strong>&lt;Enter&gt;</strong> Update FCP</p>
<p>Enter Existing Fund Control Point to Update: <strong>? &lt;Enter&gt;</strong></p>
<p>Answer with HOME OXYGEN FUND CONTROL POINT</p>
<p>Choose from:</p>
<p>499 887</p>
<p>910 PROSTHETICS</p>
<p>Enter Existing Fund Control Point to Update: <strong>499 887</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Enter NEW Fund Control Point: <strong>910</strong> PROSTHETICS <strong>&lt;Enter&gt;</strong></p>
<p>Updating HO template for FCP 499 887 to 910 PROSTHETICS......</p>
<p><strong> 2 Records updated </strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Update an Item for a Home Oxygen Patient

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>The <strong>Update Item</strong> option allows you to change the item in the template. This would change the record for active Home Oxygen patients and all patients with future inactivation dates.</p>
</blockquote></td>
</tr>
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
<p>To update an item for a Home Oxygen patient(s), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                                                                                                                                        |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                                                                                                                                                 |
| 1    | At the *Site* prompt, press the Spacebar and then press \<Enter\> to select the default site or type a question mark to display a list of selection options and choose one.                                                                                                                                                |
| 2    | At the *Type of Update* prompt, type 4 for the Update Item option and press \<Enter\>.                                                                                                                                                                                                                                 |
| 3    | At the *Enter Existing ITEM to Update* prompt, you can type the item to be updated, and press \<Enter\>. You can also type a question mark and press \<Enter\>. You will then be asked the following: Do you want the entire 11-Entry PROS ITEM MASTER List? If you answer yes, then you can select an option from a list. |
| 4    | At the *Enter NEW ITEM* prompt, type the new item and press \<Enter\>.                                                                                                                                                                                                                                                         |
| 5    | At the *OK?* prompt, press \<Enter\> to accept the item.                                                                                                                                                                                                                                                                       |
| 6    | The system displays the number of records that are updated.                                                                                                                                                                                                                                                                            |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Update Item option screen</td>
<td><blockquote>
<p>Select SITE: Hines Development System <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p>1 Update VENDOR</p>
<p>2 Update HCPCS</p>
<p>3 Update FCP</p>
<p><strong>4 Update ITEM</strong></p>
<p>5 Update UNIT COST</p>
<p>Type of Update: Update VENDOR// <strong>4 &lt;Enter&gt;</strong> Update ITEM</p>
<p>Enter Existing ITEM to Update: oxygen <strong>&lt;Enter&gt;</strong></p>
<p>1 OXYGEN CONCENTRATOR 99 OXYGEN CONCENTRATOR</p>
<p>2 OXYGEN DEVICE 100 OXYGEN DEVICE</p>
<p>CHOOSE 1-2: <strong>1</strong> <strong>&lt;Enter&gt;</strong> 99 OXYGEN CONCENTRATOR</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Enter NEW ITEM: <strong>oxygen device</strong> 100 OXYGEN DEVICE</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Updating HO template for item OXYGEN CONCENTRATOR to OXYGEN DEVICE......</p>
<p><strong> 1 Records updated </strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Update a Unit Cost for an Item for a Home Oxygen Patient

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>If a price for an item is changed, the price can be updated using the <strong>Update Unit Cost</strong> option.</p>
</blockquote></td>
</tr>
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
<p>To update unit cost for an item for a Home Oxygen patient(s), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                         |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                  |
| 1    | At the *Site* prompt, press the Spacebar and then press \<Enter\> to select the default site or type a question mark to display a list of selection options and choose one. |
| 2    | At the *Type of Update* prompt, type 5 for the UpdateUnit Cost option and press \<Enter\>.                                                                         |
| 3    | At the *Enter an ITEM for Unit Cost Update* prompt, you can type the item to be updated or type a question mark, and press \<Enter\> to display a list and select an option.    |
| 4    | At the *OK?* prompt, press \<Enter\>.                                                                                                                                           |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Update Unit Cost option screen</td>
<td><blockquote>
<p>Select SITE: Hines Development System <strong>&lt;Enter&gt;</strong></p>
<p>Select one of the following:</p>
<p>1 Update VENDOR</p>
<p>2 Update HCPCS</p>
<p>3 Update FCP</p>
<p>4 Update ITEM</p>
<p><strong>5 Update UNIT COST</strong></p>
<p>Type of Update: Update VENDOR// <strong>5</strong> Update UNIT COST <strong>&lt;Enter&gt;</strong></p>
<p>Enter an ITEM for UNIT COST Update: <strong>?</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Answer with PROS ITEM MASTER NAME</p>
<p>Choose from:</p>
<p>3 SYRINGE-SUBCUTANEOUS-3IN  THIS ITEM IS INACTIVE </p>
<p>7 BEEF-ROUND/TOP/INSIDE/FRZN</p>
<p>9 PORK-GROUND/FRZN  THIS ITEM IS INACTIVE, USE ITEM NUMBE</p>
<p>40 CATSUP-TOMATO-INDIV</p>
<p>55 WHEELCHAIR-ADULT/HEMI/BLUE-STD FOR ALL PATIENTS</p>
<p>56 WHEELCHAIR-CLASSIC-18X16</p>
<p>59 EYEGLASSES</p>
<p><strong>99 OXYGEN CONCENTRATOR</strong></p>
<p>10000 EYEGLASSES</p>
<p>Enter an ITEM for UNIT COST Update: 99 OXYGEN CONCENTRATOR</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
</blockquote></td>
</tr>
</tbody>
</table>

*Screen to be continued on next page.*

Continued on next page

Update a Unit Cost for an Item for a Home Oxygen Patient, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Unit Cost for an Item</td>
<td><blockquote>
<p>The <strong>Update Unit Cost</strong> option would change the record for active Home Oxygen patients and all Home Oxygen patients with future inactivation dates.</p>
</blockquote></td>
</tr>
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
<p>To update a unit cost for an item for a Home Oxygen patient(s), follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                    |
| 5    | At the *Enter new UNIT COST for item* prompt, type the new cost for the item and press \<Enter\>. |
| 6    | The system displays the number of records that are updated.                                               |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Update Unit Cost option screen</td>
<td><blockquote>
<p>Enter new UNIT COST for item OXYGEN CONCENTRATOR: <strong>? &lt;Enter&gt;</strong></p>
<p>Type a Dollar Amount between 0 and 9999999, 2 Decimal Digits</p>
<p>Enter new UNIT COST for item OXYGEN CONCENTRATOR: <strong>345.00 &lt;Enter&gt;</strong></p>
<p>Updating HO template for unit cost of item OXYGEN CONCENTRATOR to 345.00......</p>
<p><strong> 1 Records updated </strong></p>
</blockquote></td>
</tr>
</tbody>
</table>