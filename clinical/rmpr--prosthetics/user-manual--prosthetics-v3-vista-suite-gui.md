---
title: Prosthetics Version 3 VistA Suite (GUI) User Manual (Updated RMPR*3*136)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: VistA Suite (GUI)  (Updated RMPR*3*136)
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
menu_options: 0
description: ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/001.png)
audience: 
keywords: 
  - strong
  - blockquote
  - style
  - width
  - table
  - colgroup
  - tbody
  - class
  - window
  - prosthetics
page_count: 0
word_count: 47792
section_count: 0
table_count: 93
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: March 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_136um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_136um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/001.png)

Prosthetics VistA SuiteUser ManualVersion 3.0 (GUI Version)March 2005

for Patch RMPR\*3.0\*136

Health System Design and Development

Provider Systems

Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>GUI User Manual</td>
<td><blockquote>
<p>Below are the development phases and dates of this <strong>Prosthetics VistA Suite User Manual.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Section</strong></th>
<th><strong>Date</strong></th>
<th><strong>Patch</strong></th>
<th><strong>Page/Author</strong></th>
<th><strong>Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NPPD Detail Display User Manual</td>
<td>1/03</td>
<td>RMPR*3.0*71</td>
<td><p>Section 2</p>
<p>Page 65</p></td>
<td>New GUI feature</td>
</tr>
<tr class="even">
<td>Automated Delayed Order Report</td>
<td>6/03</td>
<td>RMPR*3.0*59</td>
<td><p>Section 3</p>
<p>Page 83</p></td>
<td>New GUI feature</td>
</tr>
<tr class="odd">
<td>View Prosthetic Billing Information</td>
<td>1/05</td>
<td>RMPR*3.0*96</td>
<td><p>Section 4</p>
<p>Page 111</p></td>
<td>New GUI feature</td>
</tr>
<tr class="even">
<td>Purchase Card Purchasing</td>
<td>4/05</td>
<td>RMPR*3.0*90</td>
<td><p>Section 1</p>
<p>Page 2</p></td>
<td>New GUI feature</td>
</tr>
<tr class="odd">
<td>NPPD Detail Display User Manual</td>
<td>4/05</td>
<td>RMPR*3.0*109</td>
<td><p>Section 2</p>
<p>Page 69</p></td>
<td>Added a new “Display Custom Data field” feature</td>
</tr>
<tr class="even">
<td></td>
<td>9/1/05</td>
<td>RMPR*3.0*90</td>
<td><mark>REDACTED</mark></td>
<td>Minor fixes per EVS</td>
</tr>
<tr class="odd">
<td>Throughout</td>
<td>1/13/06</td>
<td>RMPR*3.0*90</td>
<td><mark>REDACTED</mark></td>
<td>Updated GUI screens</td>
</tr>
<tr class="even">
<td>Section 5: Creating a Lab Work Order</td>
<td>2/22/06</td>
<td>RMPR*3.0*75</td>
<td><mark>REDACTED</mark></td>
<td>Added OWL creation section</td>
</tr>
<tr class="odd">
<td>Section 6: Orthotic Lab &amp; Work Order</td>
<td>8/11/06</td>
<td>RMPR*3.0*75</td>
<td><mark>REDACTED</mark></td>
<td>Added OWL Lab section</td>
</tr>
<tr class="even">
<td>Sections 5 &amp; 6</td>
<td>3/2007</td>
<td>RMPR*3.0*75</td>
<td><mark>REDACTED</mark></td>
<td>Fixes per EVS and release of patch 75</td>
</tr>
<tr class="odd">
<td>Sections 5 &amp; 6</td>
<td>4/2007</td>
<td>RMPR*3.0*75</td>
<td><mark>REDACTED</mark></td>
<td>Fixes per EVS</td>
</tr>
<tr class="even">
<td>RMPR*3.0*75 released</td>
<td>5/2007</td>
<td>RMPR*3.0*75</td>
<td><mark>REDACTED</mark></td>
<td></td>
</tr>
<tr class="odd">
<td>RMPR*3.0*136</td>
<td>11/2007</td>
<td>RMPR*3.0*136</td>
<td><mark>REDACTED</mark></td>
<td>Updated GUI for Excel report save</td>
</tr>
</tbody>
</table>

Table of Contents

Introduction to Prosthetics Application Suite User Manual [1](#_Toc172537284)

User Manual Overview [1](#_Toc172537285)

Section 1 [3](#_Toc172537286)

GUI Purchase Card Purchasing [3](#_Toc172537287)

Overview [3](#_Toc172537288)

Chapter 1 – Roll and Scroll Features [7](#_Toc172537289)

Patch RMPR\*3\*90 Overview [7](#_Toc172537290)

Utilities Menu – Site Parameters File [8](#_Toc172537291)

Utilities Menu – Display Prosthetic PO Information (WD) [11](#_Toc172537292)

Purchasing Menu – Enter Waiver or Excluded Notice (EW) [12](#_Toc172537293)

Purchasing Menu – Enter/Edit Contract \# (EC) [14](#_Toc172537294)

Display/Print Patient 2319 (23) – Excluded and Waiver [15](#_Toc172537295)

Chapter 2 – Access/Sign-on Instructions to GUI [17](#_Toc172537296)

Sign-On Properties (Optional) [23](#_Toc24938076)

Chapter 3 – Purchase Ordering [27](#_Toc172537298)

The Purchase Order Control Window [27](#_Toc172537299)

Select a Site and Status [28](#_Toc172537300)

Select an SSN Range [29](#_Toc172537301)

Change Data Display [31](#_Toc89754782)

View Column Descriptions [32](#_Toc89754783)

Chapter 4 - Display the 2319 [33](#_Toc172537304)

2319 Button [33](#_Toc172537305)

View 2319 – Patient Demographics (Tab 1) [35](#_Toc172537306)

View 2319 – Clinic Enrollments/Correspondence (Tab 2) [36](#_Toc172537307)

View 2319 – Entitlement Info (Tab 3) [37](#_Toc172537308)

View 2319 – Appliance Transactions (Tab 4) [38](#_Toc172537309)

View 2319 – Auto Adaptive Info (Tab 5) [40](#_Toc172537310)

View 2319 – Critical Comments (Tab 6) [41](#_Toc172537311)

View 2319 – HISA Information (Tab 7) [42](#_Toc172537312)

View 2319 – Home Oxygen (Tab 8) [44](#_Toc172537313)

Chapter 5 - View a CPRS Record [47](#_Toc172537314)

CPRS Button [47](#_Toc172537315)

Chapter 6 - View a Request [49](#_Toc172537316)

Request Button [49](#_Toc172537317)

Chapter 7 - Purchase Order Creation [51](#_Toc172537318)

Create a P.O. [51](#_Toc172537319)

Select a Due Date [54](#_Toc172537320)

Select a Site [56](#_Toc172537321)

Select a Purchase Card [57](#_Toc172537322)

Cost Center [58](#_Toc172537323)

Select a Vendor [59](#_Toc172537324)

Select the Delivery Method [61](#_Toc172537325)

Chapter 8 - Add Item(s) to the Purchase Order [63](#_Toc172537326)

Add Items Button [63](#_Toc172537327)

Return to P.O. Button [70](#_Toc172537328)

Add Additional Items [71](#_Toc172537329)

Edit/Delete an Item [72](#_Toc172537330)

Chapter 9 - Purchase Order Creation Continued [75](#_Toc172537331)

Enter Discount/Shipping [75](#_Toc172537332)

Enter Your Electronic Signature [76](#_Toc172537333)

Post CPRS Note [78](#_Toc172537334)

Chapter 10 - Closing and Exiting [81](#_Toc89754795)

Exit the Purchase Order Control Window [81](#_Toc89754796)

Sample Printout [82](#_Toc172537337)

Section 2 [85](#_Toc24938072)

NPPD Detail Display [85](#_Toc172537339)

Overview [85](#_Toc24938073)

Enter a Date Range [86](#_Toc24938077)

Display the Data [88](#_Toc24938078)

Select Custom Data [89](#_Toc172537343)

Print the NPPD Detail [101](#_Toc172537344)

Save as an Excel File [103](#_Toc172537345)

Exiting the NPPD Detail Display Window [106](#_Toc172537346)

Section 3 [109](#_Toc172537347)

Automated Delayed Order Report (DOR) [109](#_Toc172537348)

Overview [109](#_Toc44299367)

Display the DOR Data [111](#_Toc44299368)

Introduction [111](#_Toc44299369)

Select a Site(s) [112](#_Toc44299370)

Select a Starting Date [113](#_Toc44299371)

Select a Status [114](#_Toc44299372)

Select the SSN Range [115](#_Toc44299373)

Display the Data [116](#_Toc44299374)

View DOR Calculation Detail [118](#_Toc44299375)

View Pending Calculations [122](#_Toc44299376)

View 2319 Information [125](#_Toc24185572)

View 2319 – Patient Demographics [125](#_Toc24185573)

View 2319 - Clinic Enrollments/Correspondence [127](#_Toc24185574)

View 2319 - Entitlement Infor mation [128](#_Toc24185575)

View 2319 – Appliance Transactions [129](#_Toc24185576)

View 2319 – Auto Adaptive Info [131](#_Toc24185577)

View 2319 - Critical Comments [132](#_Toc24185578)

View 2319 – View HISA Information [133](#_Toc24185579)

View 2319 – Home Oxygen [134](#_Toc24185580)

View and Manage the DOR [136](#_Toc44299386)

View CPRS [136](#_Toc44299387)

View Request [137](#_Toc44299388)

Save as an Excel File [138](#SaveExcel)

Print the DOR [141](#_Toc44299390)

Exiting the DOR Window [142](#_Toc172537373)

Section 4 [145](#_Toc172537374)

View Prosthetics Billing Information [145](#_Toc172537375)

Overview [145](#_Toc89754773)

Chapter 1 - For Billing Users [147](#_Toc89754774)

Billing Main Menu Window [147](#_Toc89754775)

Chapter 2 – For Prosthetics Users [149](#_Toc89754776)

Prosthetics Main Menu Window [149](#_Toc89754777)

Chapter 3 – View Billing Information Package [151](#_Toc89754778)

View Billing Information Window [151](#_Toc89754779)

Enter a Date Range [152](#_Toc89754780)

Display the Prosthetics Data [154](#_Toc89754781)

Change Data Display [155](#_Toc172537385)

View Column Descriptions - Site, Dates and Patient Data [156](#_Toc172537386)

View Column Description - Insurance Information [157](#_Toc89754784)

View Column Descriptions - Coding Errors [158](#_Toc89754785)

View Column Descriptions - Item Information [159](#_Toc89754786)

View Column Descriptions - Quantity and Total Cost Data [160](#_Toc89754787)

View Column Descriptions - HCPCS and HCPCS Description Data [161](#_Toc89754788)

View Column Descriptions - ICD9 and ICD9 Description [162](#_Toc89754789)

View Column Descriptions - Disability Information [163](#_Toc89754790)

Chapter 4 - Printing [165](#_Toc89754791)

Print the View Prosthetics Billing Information Window [165](#_Toc89754792)

Chapter 5 – Saving [167](#_Toc89754793)

Save as an Excel File [167](#_Toc172537397)

AutoFilter [170](#_Toc172537398)

Chapter 6 - Closing and Exiting [171](#_Toc172537399)

Exiting the View Prosthetic Billing Information Window [171](#_Toc172537400)

Section 5 [173](#_Toc172537401)

Creating a Lab Work Order [173](#_Toc172537402)

Overview [173](#_Toc172537403)

Selecting a Lab Type [175](#_Toc172537404)

Selecting Stations [176](#_Toc172537405)

Patient Category and Type of Transaction [177](#_Toc172537406)

Primary Item Information [178](#_Toc172537407)

Changing the Date Required [180](#_Toc172537408)

Changing the Print Location [181](#_Toc172537409)

Viewing Additional Information [184](#_Toc172537410)

Submitting the Lab Work Order [185](#_Toc172537411)

Section 6 [187](#_Toc172537412)

Orthotic Lab & Work Order [187](#_Toc172537413)

Overview [187](#_Toc172537414)

Orthotic Lab & Work Order Window Areas [189](#_Toc172537415)

Title Bar [189](#_Toc172537416)

Menu Bar [190](#_Toc172537417)

Work Orders Listview [192](#_Toc172537418)

HCPCS Area [193](#_Toc172537419)

Command Buttons Area [194](#_Toc172537420)

HCPCS Materials Area [196](#_Toc172537421)

HCPCS Labor Area [196](#_Toc172537422)

Workflows [197](#_Toc172537423)

Filtering Lab Work Orders [197](#_Toc172537424)

Managing Lab Technicians [198](#_Toc172537425)

Managing HCPCS Items [200](#_Toc172537426)

HCPCS Materials [204](#_Toc172537427)

HCPCS Labor [207](#_Toc172537428)

Printing the OWL [210](#_Toc172537429)

Completing the OWL [211](#_Toc172537430)

Cancelling the OWL [212](#_Toc172537431)

Closing the OWL [213](#_Toc172537432)

Appendix A [215](#_Toc172537433)

Getting Help [215](#_Toc89754798)

Appendix B [217](#_Toc44299392)

Using the Menus [217](#_Toc172537436)

Appendix C [219](#_Toc172537437)

Activate Section 508 Assistance [219](#_Toc89754800)

<span id="_Toc172537284" class="anchor"></span>Introduction to Prosthetics Application Suite User Manual

<span id="_Toc172537285" class="anchor"></span>User Manual Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>This <strong>Prosthetics Application Suite User Manual</strong> encompasses past GUI (graphical user interface) patches that provided new and enhanced GUI features for Prosthetics. This user manual will be the main user manual for all future GUI updates.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>In this manual</td>
<td><blockquote>
<p>This user manual contains the following topics and their corresponding sections:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                 |           |
|---------------------------------|-----------|
| Topic                           | Section   |
| Purchase Card Purchasing        | Section 1 |
| NPPD Detail Display             | Section 2 |
| Delayed Order Report            | Section 3 |
| View Billing Information        | Section 4 |
| Creating a Lab Work Order (OWL) | Section 5 |
| Orthotic Lab & Work Order       | Section 6 |

<span id="_Toc172537286" class="anchor"></span>Section 1

<span id="_Toc172537287" class="anchor"></span>GUI Purchase Card Purchasing

<span id="_Toc172537288" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction to GUI Purchasing</td>
<td><blockquote>
<p>Patch RMPR*3*90 is a large Prosthetics patch affecting the Purchase Card Purchasing features. There is a whole new module using GUI (graphical user interface) windows features to create a Purchase Card purchase order. You will no longer be able to use the roll and scroll <strong>Purchase Card Menu</strong> option.</p>
<p><strong>IMPORTANT:</strong> A new feature in GUI Purchasing is that a purchase order cannot be created if the consult (or manual entry in Suspense) is not in an <strong>Open</strong> or <strong>Pending</strong> status.</p>
<p><strong>Note:</strong> Reconciling a 1358 purchase order continues as a roll and scroll selection.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>PSAS Menu options</td>
<td><blockquote>
<p>There are several <strong>PSAS Menu</strong> options addressed with Patch 90. Here are the current roll and scroll <strong>VistA Prosthetics</strong> menu options that have been enhanced:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Purchasing – <strong>Purchase Cards Menu</strong> Option</p>
</blockquote></li>
<li><blockquote>
<p>Utilities Menu – <strong>Site Parameters</strong> option</p>
</blockquote></li>
<li><blockquote>
<p>Display/Print Menu – <strong>Display/Print Patient 2319 (23)</strong> option (Appliance Transactions – Screen 4)</p>
</blockquote></li>
</ul>
<blockquote>
<p>Three new roll and scroll menu options include:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Purchasing Menu – <strong>Enter Waiver or Excluded Notice (EW)</strong></p>
</blockquote></li>
<li><blockquote>
<p>Purchasing Menu – <strong>Enter Contract Number (EC)</strong></p>
</blockquote></li>
<li><blockquote>
<p>Utilities Menu – <strong>Display Pros PO Information (WD)</strong></p>
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
<td>Transaction Type</td>
<td><p>In this GUI Purchase Card Purchasing module with Patch RMPR*3*90, there are no longer four <strong>Transaction Types</strong> as they have been consolidated into two Types: The four Types were: S – Spare, X – Repair, I – Initial Issue, and R – Replace. This change has consolidated many steps into fewer keystrokes for users.</p>
<p>The two (2) consolidated Transaction Types are:</p>
<ul>
<li><p>I – New/Replace</p></li>
<li><p>X – Service/Repair</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> The Inventory, Home Oxygen and Lab modules still have four (4) Transaction Types.</p>
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
<td>SC and NSC Patient Categories</td>
<td><blockquote>
<p>Also, there used to be four <strong>Patient Category</strong> options, and this has been consolidated into two options with this patch. The four options were:</p>
<p>1) Service Connected/In-Patient</p>
<p>2) Service Connected/Outpatient</p>
<p>3) Non-Service Connected/In-patient</p>
<p>4) Non-Service Connected/Outpatient</p>
<p><strong>The two NEW Patient Categories are:</strong></p>
<p><strong>1) Service Connected</strong></p>
<p><strong>2) Non-Service Connected</strong></p>
<p><strong>Note:</strong> With this consolidation, there is no need for a <strong>Special Category</strong> which had four options for you to choose when you selected the <strong>Patient Category</strong> of <strong>Non-Service Connected/Outpatient</strong> option.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Printed Purchase Order</td>
<td><blockquote>
<p>The full social security number is not displayed on the printed purchase order; only the last four numbers on Form 2421. The purchase order number now appears on the top of this form. Also, the Lot number, Serial number, Make and Model appear on the purchase order (as appropriate).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>The Purchase Order Control Window</td>
<td><blockquote>
<p>The <strong>Purchase Order Control</strong> window shown below displays consults from the Suspense module that have been entered through CPRS or entered manually. <strong>Open</strong> and <strong>Pending</strong> consults display here for one site or <strong>“All Sites</strong>” as well as a Purchasing Agent’s responsible SSN range for patients.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/002.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537289" class="anchor"></span>Chapter 1 – Roll and Scroll Features

<span id="_Toc172537290" class="anchor"></span>Patch RMPR\*3\*90 Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>New and deleted features</td>
<td><blockquote>
<p>There are new Roll and Scroll features with Patch RMPR*3*96 as well as updated features and features no longer needed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchasing Menu - Purchase Cards</td>
<td><blockquote>
<p>The <strong>Purchase Cards</strong> option (under the <strong>Purchasing Menu (PU)</strong> and the <strong>Enter New Request (EN)</strong> option) are no longer needed in roll and scroll and cannot be used any longer.</p>
<p>The new GUI Purchase Order process is outlined in this user manual and has been developed to replace the roll and scroll process. There have been many features added within this process as well.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchasing Menu</td>
<td><blockquote>
<p>The new menu options in the <strong>Purchasing Menu</strong> include:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Enter Waiver or Excluded Notice (EW)</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>Enter/Edit Contract Number (EC)</strong></p>
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
<td>Utilities Menu</td>
<td><blockquote>
<p>The <strong>Site Parameters</strong> file has been updated in the <strong>Utilities Menu</strong> with several new features and prompts. The enhanced option is the <strong>Enter/Edit Site Parameters (SP)</strong> option. You will then select the <strong>Enter/Edit Station Site Parameters (SS)</strong> option.</p>
<p>Also there is a new menu option, <strong>Display Pros PO Information (WD)</strong> for display purposes only.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display/Print 2319</td>
<td><blockquote>
<p>There are two new display fields on the <strong>Display/Print Patient 2319</strong> (in the Appliance Transaction – Screen 4) as follows:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Contract Number</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>Excluded Waiver</strong></p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc172537291" class="anchor"></span>Utilities Menu – Site Parameters File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site Parameters file</td>
<td><blockquote>
<p>You must first set up the Site Parameters file to set up your Purchasing Agent information including their name and SSN range of responsibilities before they can begin to use the GUI Purchase Order feature. This is also where the Common Numbering Series (number that is created for the PO process) and the new <strong>Manager Comment</strong> is updated.</p>
<p>To access this file, select the <strong>Utilities Menu (UT)</strong> and the <strong>Enter/Edit Site Parameters (SP)</strong> option.</p>
<p><strong>Note:</strong> This file can be updated when a Purchasing Agent is on vacation, sick or for any temporary purposes to transfer the SSN range of responsibilities to another Purchasing Agent.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetic Official’s Menu</td>
<td><blockquote>
<p>PU Purchasing ...</p>
<p>DD Display/Print ...</p>
<p><strong>UT Utilities .</strong>..</p>
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
<p>Select Prosthetic Official's Menu Option: <strong>UT</strong> Utilities</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Utilities Menu</td>
<td><blockquote>
<p>AP Add/Edit Patient to Prosthetics</p>
<p>DIS Enter Prosthetic Disability Code to 2319</p>
<p>REM Delete Prosthetic Disability Code from 2319</p>
<p>EN Enter/Edit Prosthetic Item Master</p>
<p>IF IFCAP Utilities ...</p>
<p>PGE Purge Obsolete Data ...</p>
<p>RC Flag Item as Returned/Condemned</p>
<p>RE Edit Returned/Condemned Item</p>
<p><strong>SP Enter/Edit Site Parameters ..</strong>.</p>
<p>WD Display Prosthetic PO Information</p>
<p>Select Utilities Option: SP <strong>&lt;Enter&gt;</strong> Enter/Edit Site Parameters</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Utilities Menu – Site Parameters File, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Next step</td>
<td><blockquote>
<p>Select the <strong>Enter/Edit Station Site Parameters (SS)</strong> option as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Enter/Edit Site Parameters option</td>
<td><blockquote>
<p><strong>SS Enter/Edit Station Site Parameters</strong></p>
<p>RF Set CPT Modifier Rental Flag</p>
<p>Select Enter/Edit Site Parameters Option: <strong>SS</strong> <strong>&lt;Enter&gt;</strong> Enter/Edit Station Site Parameters</p>
<p>Select PROSTHETICS SITE PARAMETER SITE NAME:</p>
<p>ATLANTA VAMC 508</p>
<p>CORKWELL VAMC 500</p>
<p>HINESTEST 999</p>
<p>Hines Development System2 ST. NUM. 578</p>
<p>SAN ANTONIO VAMC 671</p>
<p>ZZOJ VAMC VAMC 991</p>
<p>Answer with INSTITUTION NAME, or STATUS, or STATION NUMBER, or OFFICIAL VA NAME, or CURRENT LOCATION, or CODING SYSTEM/ID PAIR, or NAME (CHANGED FROM), or CODING SYSTEM</p>
<p>Do you want the entire INSTITUTION List? <strong>Y</strong> <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Choose from:</p>
<p>ALBANY, NY 500</p>
<p>ALBUQUERQUE, NM 501</p>
<p>ALBUQUERQUE-RO NM 340</p>
<p>ALEXANDRIA, LA 502</p>
<p>ALLEN PARK, MI MI 553</p>
<p>ALTOONA, PA 503</p>
<p>^</p>
<p>Select PROSTHETICS SITE PARAMETER SITE NAME: <strong>500</strong> <strong>&lt;Enter&gt;</strong> ALBANY, NY</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Printer</td>
<td><blockquote>
<p>You also need to know the name of your printer to set it up in the Site Parameters file. This must be defined and cannot be entered as “null” as it must be a Prosthetic printer.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Utilities Menu – Site Parameters File, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Manager Comment (NEW FEATURE)</td>
<td><blockquote>
<p>Notice the new <strong>Manager Comment</strong> prompt below. You can enter a free-text comment that will display on the GUI <strong>Purchase Order Control</strong> window at the bottom of the display. This can be used by Supervisors to make announcements or specific messages to their responsible groups.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Site Parameters file</p>
<p><strong>NEW Prompt</strong></p></td>
<td><blockquote>
<p>VAMC 500 COR</p>
<p>KWELL VAMC</p>
<p>SITE NAME: CORKWELL VAMC//</p>
<p>VISN: 17//</p>
<p>PHONE NUMBER:</p>
<p>STREET ADD1: //</p>
<p>CITY: SAN ANTONIO//</p>
<p>STATE: TEXAS//</p>
<p>ZIP CODE: 78249//</p>
<p><strong>MANAGER COMMENT:</strong> <strong>"Please enter your time today." &lt;Enter&gt;</strong></p>
<p>CHIEF SIG BLOCK: PROSmanager,one,ACTING CHIEF,PROSTHETICS SERVICE</p>
<p>Replace <strong>Y &lt;Enter&gt;</strong> ?? Replace</p>
<p>Select PURCHASING AGENT: PROSpurchagent,one //</p>
<p>PURCHASING AGENT: PROSpurchagent,one//</p>
<p>START RANGE: 0//</p>
<p>STOP RANGE: 99//</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537292" class="anchor"></span>Utilities Menu – Display Prosthetic PO Information (WD)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display PO Information (WD)</td>
<td><blockquote>
<p>With Patch RMPR*3*90, you can display purchase order information with the new option from the <strong>Utilities Menu</strong> called <strong>Display Prosthetic PO Information (WD)</strong>. This will display purchase order information that does not contain patient name or sensitive information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display Prosthetic PO Information (WD)</td>
<td><blockquote>
<p>PU Purchasing ...</p>
<p>DD Display/Print ...</p>
<p><strong>UT Utilities .</strong>..</p>
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
<p>Select Prosthetic Official's Menu Option: <strong>UT</strong> <strong>&lt;Enter&gt;</strong> Utilities</p>
<p>AP Add/Edit Patient to Prosthetics</p>
<p>DIS Enter Prosthetic Disability Code to 2319</p>
<p>REM Delete Prosthetic Disability Code from 2319</p>
<p>EN Enter/Edit Prosthetic Item Master</p>
<p>IF IFCAP Utilities ...</p>
<p>PGE Purge Obsolete Data ...</p>
<p>RC Flag Item as Returned/Condemned</p>
<p>RE Edit Returned/Condemned Item</p>
<p>SP Enter/Edit Site Parameters ...</p>
<p><strong>WD Display Prosthetic PO Information</strong></p>
<p>Select Utilities Option: <strong>WD</strong> <strong>&lt;Enter&gt;</strong> Display Prosthetic PO Information</p>
<p>Select PROSTHETICS 1358 DATE: 2-15-2005 EYEGLASSES-PRES</p>
<p>DEVICE: <strong>&lt;Enter&gt;</strong> INCOMING TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Prosthetics Display MAR 10,2005 09:18 PAGE 1</p>
<p>------------------------------------------------------------------------------</p>
<p>Deliver To: OTHER LOCATION AT THIS SITE IFCAP Order: 516-0U7820</p>
<p>Vendor: INVACARE</p>
<p>Initiator: PROSDEVELOPER,ONE</p>
<p>Station Name: BAY PINES VAMC</p>
<p>Item: EYEGLASSES-PRESCRIPTION</p>
<p>Brief Description: EYEGLASSES</p>
<p>Unit Cost: 25.00 Qty: 1 Unit of Issue: EA</p>
<p>Eyeglasses, Prescription</p>
<p>Select PROSTHETICS 1358 DATE:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537293" class="anchor"></span>Purchasing Menu – Enter Waiver or Excluded Notice (EW)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definitions</td>
<td><blockquote>
<p>The <strong>Enter Waiver or Excluded Notice (EW)</strong> option is from the <strong>Purchasing (PU)</strong> Menu. You can use this menu option if you forget to enter this information during the creation of the purchase order.</p>
<p>A <strong>Waiver</strong> is a device/vendor that is not on a National Prosthetics Mandatory BPA/Contract and is prescribed because it meets the needs of an individual patient. (The prescribing physician requests in writing to the Chief of Staff and if approved, a copy is forwarded to the VPR.) <strong>Excluded</strong> means that an Item (HCPCS) issued is not covered by a National Prosthetics Mandatory BPA/Contract.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetic Official’s Menu</td>
<td><p><strong>PU Purchasing</strong> ...</p>
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
<p>Select Prosthetic Official's Menu Option: <strong>PU</strong> <strong>&lt;Enter&gt;</strong> Purchasing</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchasing Menu</td>
<td><p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p>EC Enter Contract # and FPDS</p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p>CPC Cancel Purchase Card Transaction</p>
<p>CPO Reconcile/Close Out Purchase Card Transaction</p>
<p>ED2 Edit 2319</p>
<p>EDPC Edit Purchase Card Transaction</p>
<p>ER Enter Product Information for Recall</p>
<p><strong>EW Enter Waiver or Excluded Notice</strong></p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<blockquote>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>EW &lt;Enter&gt;</strong> Enter Waiver or Excluded Notice</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Purchasing Menu – Enter Waiver or Excluded Notice (EW), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>The 2319</td>
<td><blockquote>
<p>The Waiver or Excluded information appears on the 2319.</p>
<p><strong>Note:</strong> This new feature works for any Inventory/Stock Issues items as well.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Enter Waiver or Excluded Notice</td>
<td><p>Enter Patient Name or PO Number 1-27-2005 ITEM DES</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Patient Name: PROSpatient,one <strong>&lt;Enter&gt;</strong></p>
<p>Form: VISA</p>
<p>Transaction #: 0U7748</p>
<p>Brief Desc: ITEM DES</p>
<p>PSAS HCPCS: E2100</p>
<p>Item: WHEELCHAIR-H2000-18IN-ELEV</p>
<p>Vendor: SUN BRAND</p>
<p>Initiator: PROSdeveloper,one</p>
<p><strong>EXCLUDE/WAIVER:</strong> <strong>?</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>E EXCLUDED</p>
<p>W WAIVER</p>
<p><strong>EXCLUDE/WAIVER:</strong> <strong>E</strong> <strong>&lt;Enter&gt;</strong> EXCLUDED</p>
<blockquote>
<p>Enter Patient Name or PO Number <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537294" class="anchor"></span>Purchasing Menu – Enter/Edit Contract \# (EC)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Enter/Edit Contract Number</td>
<td><blockquote>
<p>The <strong>Enter/Edit Contract Number (EC)</strong> option allows you to enter a new Contract number on the 2319 or edit an existing one. This menu option is a free-text field and you can enter any free-text.</p>
<p><strong>Note:</strong> The <strong>Contract #</strong> has a maximum of 30 characters allowed in this prompt.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchasing Menu</td>
<td><p>EN Enter New Request ...</p>
<p>SI Stock Issues ...</p>
<p>RP Reprints ...</p>
<p>RE Record 2237 Purchase to 2319</p>
<p>ED Edit/Delete 2237 from 10-2319</p>
<p><strong>EC Enter/Edit Contract #</strong></p>
<p>CA Cancel a Transaction</p>
<p>CO Close Out</p>
<p>CPC Cancel Purchase Card Transaction</p>
<p>CPO Reconcile/Close Out Purchase Card Transaction</p>
<p>ED2 Edit 2319</p>
<p>EDPC Edit Purchase Card Transaction</p>
<p>ER Enter Product Information for Recall</p>
<p>EW Enter Wavier or Excluded Notice</p>
<p>HI Add Historical Data</p>
<p>HID Delete Historical Data Entry</p>
<p>LI List Open 1358 Prosthetic Transactions</p>
<p>LII List Open 1358 Transactions By Initiator</p>
<p>LPC List Open Purchase Card Transactions</p>
<p>LPCI List Open Purchase Card Transactions By Initiator</p>
<p>LPS Purchase Card Summary Sheet</p>
<p>Select Purchasing Option: <strong>EC</strong> <strong>&lt;Enter&gt;</strong> Enter/Edit Contract # on 2319</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Enter Contract #</td>
<td><p>Enter Patient Name or PO Number 1-27-2005 ITEM DES</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>Patient Name: <strong>PROSpatient,one</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Form: VISA</p>
<p>Transaction #: 0U7748</p>
<p>Brief Desc: ITEM DES</p>
<p>PSAS HCPCS: E2100</p>
<p>Item: WHEELCHAIR-H2000-18IN-ELEV</p>
<p>Vendor: SUN BRAND</p>
<p>Initiator: PROSdeveloper,one</p>
<p><strong>CONTRACT #:</strong> <strong>?</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Answer must be 1-30 characters in length.</p>
<p><strong>CONTRACT #:</strong> 123ABC <strong>&lt;Enter&gt;</strong></p>
<p>Enter Patient Name or PO Number</p></td>
</tr>
</tbody>
</table>

<span id="_Toc172537295" class="anchor"></span>Display/Print Patient 2319 (23) – Excluded and Waiver

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Excluded and Waiver prompts</td>
<td><blockquote>
<p>With Patch RMPR*3*90, there are two new prompts on the 2319: Excluded and Waiver. You can display and print the 2319 from the <strong>Display/Print (DD) Menu</strong> (accessed from the <strong>Prosthetics Official’s Menu</strong>) to update the Excluded or Waiver prompts on the 2319. Follow the sequence of prompts below to display or print the 2319.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display/Print Patient 2319</td>
<td><p>Select Display/Print Option: <strong>23</strong> <strong>&lt;Enter&gt;</strong> Display/Print Patient 2319</p>
<p>SITE: DVAMC BAY PINES 516/121// <strong>&lt;Enter&gt;</strong> 516</p>
<p>Select PROSTHETIC PATIENT: PROSpatient,one <strong>&lt;Enter&gt;</strong> 5-28-</p>
<p>25 000277955 NO NSC VETERAN B B PC NORTH PINELLAS</p>
<p>Enrollment Priority: GROUP 8c Category: IN PROCESS End Date:</p>
<p>BAY PINES VAMC</p>
<p>DEVICE: HOME//<strong>&lt;Enter&gt;</strong> INCOMING TELNET Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>Current Disability Codes are:</p>
<p>AO/DIS OTHERS ELIG NSC PL-104-262 (ELIG. REFORM</p>
<blockquote>
<p>AO/ELAS OTHERS ELIG NSC PL-104-262 (ELIG. REFORM</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance Transactions (Screen 4)</td>
<td><p>Select one of the following:</p>
<p>1 PATIENT DEMOGRAPHICS</p>
<p>2 CLINIC ENROLLMENTS/CORRESPONDENCE</p>
<p>3 ENTITLEMENT INFORMATION</p>
<p><strong>4 APPLIANCE TRANSACTIONS</strong></p>
<p>5 AUTO ADAPTIVE INFORMATION</p>
<p>6 CRITICAL COMMENTS</p>
<p>7 ADD/EDIT DISABILITY CODE</p>
<p>8 HOME OXYGEN ITEMS</p>
<blockquote>
<p>Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue : <strong>4</strong> <strong>&lt;Enter&gt;</strong> APPLIANCE TRANSACTIONS</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Display/Print Patient 2319 (23) – Excluded and Waiver, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>New Display fields</td>
<td><blockquote>
<p>Below you can see the two new display fields on the <strong>Display/Print Patient 2319</strong>:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Contract Number</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>Excluded Waiver</strong></p>
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
<td><p>Appliance/ Repair Record for a Veteran</p>
<p>New display fields here:</p></td>
<td><p>PROSpatient,one SSN: 000-27-7955 DOB: MAY 28,1925 CLAIM#</p>
<p>Date Qty HCPCS Type Vendor Sta Serial Delivery Date Tot Cost</p>
<p>1. 01/27/05 2 BLOOD GLUC R SUN BRAND 516 24.00</p>
<p>2. 01/24/05 2 PLNR BACK I INVACARE 516 20.00</p>
<p>REMARK</p>
<p>3. 02/06/04 1 WHO, WRIST I EBI MEDICA 516 2022-14 02/06/04 7.73</p>
<p>RIGHT MEDIUM ISSUED 12-16-04</p>
<p>4. 02/06/04 1 WHO, WRIST I EBI MEDICA 516 2022-24 02/06/04 7.73</p>
<p>LEFT MEDIUM ISSUED 12-16-04</p>
<p>5. 03/10/03 2 ELASTIC SU I SURGICAL A 516 8868LG 03/10/03 19.78</p>
<p>ISS 2-21-03 1PR TRUFORM AK 8868 LG</p>
<p>6. 02/19/03 1 AUTO BLOOD I MEDICAL PL 516 02/19/03 29.70</p>
<p>MAILED BP KIT</p>
<p>End of Appliance/Repair records for this veteran!</p>
<p>+=Turned-In *=Historical Data I=Initial X=Repair S=Spare R=Replacement</p>
<p>Enter 1-6 to show full entry, '^' to exit or `return` to continue. <strong>1 &lt;Enter&gt;</strong></p>
<p>PROSpatient,one SSN: 000-27-7955 BAY PINES VAMC DOB: 05-28-1925</p>
<p>APPLIANCE/REPAIR LINE ITEM DETAIL &lt;4-1&gt;</p>
<p>TYPE OF FORM: VISA INITIATOR: PROSdeveloper,one DATE: JAN 27, 2005</p>
<p>DELIVER TO: VETERAN</p>
<p>TYPE TRANS: REPAIR QTY: 2 SOURCE: COMMERCIAL</p>
<p>VENDOR TRACKING: BANK AUTHORIZATION:</p>
<p>VENDOR: SUN BRAND</p>
<p>VENDOR PHONE: 404-455-0664</p>
<p>3900 GREEN INDUSTRIAL WAY</p>
<p>ATLANTA, GEORGIA 30341</p>
<p>DELIVERY DATE:</p>
<p>TOTAL COST: $24.00 OBL: 0U7748</p>
<p>REMARKS:</p>
<p>DISABILITY SERVED: NSC</p>
<p>ITEM DESCRIPTION: WHEELCHAIR-H2000-18IN-ELEV</p>
<p>APPLIANCE: WHEELCHAIR-H2000-18IN-ELEV</p>
<p><strong>CONTRACT #: 123ABC</strong></p>
<p><strong>EXCLUDED/WAIVER: EXCLUDED</strong></p>
<p>PSAS HCPCS: E2100 BLOOD GLUCOSE MONITOR W VOICE</p>
<p>ICD-9 Code:</p>
<p>CPT MODIFIER:</p>
<p>DESCRIPTION: ITEM DES</p>
<p>EXTENDED DESCRIPTION:</p>
<blockquote>
<p>Enter RETURN to continue or '^' to exit: <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537296" class="anchor"></span>Chapter 2 – Access/Sign-on Instructions to GUI

Open the Prosthetics Main Menu

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Introduction</strong></td>
<td><p>Introducing the <strong>Prosthetics Main Menu</strong> window, as shown below. This feature was first included in Patch RMPR*3*90. It will grow as more features are developed in the GUI suite of Prosthetics programs as part of an entire VistA suite of Prosthetics programs. It will remain the main point of access for future Prosthetics applications. This window allows you to access the current GUI features including the following:</p>
<ul>
<li><p>VistA Sign-On</p></li>
<li><p>Processing (formerly Purchasing)</p></li>
<li><p>View Prosthetic Billing Information</p></li>
<li><p>Delayed Order Report</p></li>
<li><p>NPPD Detail Display Report</p></li>
<li><p>Orthotic Lab &amp; Work Order (OWL)</p></li>
<li><p>Help</p></li>
<li><p>About (provides the version number of the application)</p></li>
</ul></td>
</tr>
</tbody>
</table>

|                           |                                                                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Prosthetics Main Menu | ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/003.png) |

  
Display/Print Patient 2319 (23) – Excluded and Waiver, Continued

|           |                                                                                  |
|-----------|----------------------------------------------------------------------------------|
| Steps | To sign on to VistA and access the Prosthetics applications, follow these steps: |

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Step</strong></td>
<td><strong>Action</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td><p><u>For Prosthetics users</u>: Double-click the <strong>Prosthetics Vista Suite</strong> which is the <em>medicine bag</em> icon on your desktop.</p>
<p><u>(For Billing Users</u>: Double-click the <strong>Prosthetics View Billing Menu</strong> which is the <em>green dollar sign</em> icon on your desktop.)</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>Click the <strong>VISTA Sign-On</strong> button.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;S&gt;</strong> key.</p>
<p>A confirmation window displays to alert you that opening this application may expose you to individually-identifiable information which must be kept confidential.</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>Click <strong>Yes</strong> if you agree to follow appropriate security and privacy policies. The <strong>Connect To</strong> dialog displays.</td>
</tr>
</tbody>
</table>

|                    |                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Confirm window | ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/004.png) |

|                            |                                                                                                                                                |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Help and About Buttons | If you require online help, you can click the Help button WITHOUT signing on. You can also access the About option WITHOUT signing on. |

Display/Print Patient 2319 (23) – Excluded and Waiver, Continued

|                                                    |                                                                                                                    |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| About window (Version number may be different) | ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/005.png) |

|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single Sign-on | The Prosthetics Main Menu window is a location for a single sign-on to all the Prosthetics GUI applications. Using this main menu requires you to sign-on using the VISTA Sign-on button. Then you can decide if you want the Purchasing option, the View Prosthetic Billing Information option, the Delayed Order Report option, or the NPPD Detail Display Report option (until future applications are available). |

|               |                                                                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title Bar | After you sign on, all Prosthetics programs will display the server information that you are logged into in the Title bar of the application window. |

|                           |                                                                                                                                                                                                                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multiple Windows Open | After you log on, you can access multiple applications, and you can switch between open applications without having to relog on and without losing displayed data. <u>If you change servers that you are logged into, then you will lose the data displayed in all open windows</u>. |

|                            |                                                                                                                                                                                                                                                                                                                                    |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exit the V*ist*A Suite | You can logoff the Prosthetics Main Menu window by clicking the Close button. This exits you out of the V*ist*A suite of Prosthetics applications. If you have any open Prosthetics applications when you exit, you will lose data in these open applications. A confirmation message will display as shown below. |

|                          |                                                                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Confirmation message | ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/006.png) |

Connect to the System (Only necessary for multiple sites)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Prosthetics Main Menu window</strong></td>
<td><p>After you click the <strong>VISTA Sign-on</strong> button and click <strong>Yes</strong> at the Confirm window (as described above), the <strong>Connect To</strong> dialog box displays as shown below <u>ONLY if you are connected to multiple sites/systems</u>.</p>
<p>Workstations are typically configured to sign-on to a single system. However, if your workstation is configured to sign-on to more than one system (see example below), you will see the <strong>Connect To</strong> window whenever you try to establish a connection.</p></td>
</tr>
</tbody>
</table>

|                       |                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------|
| Connect To window | ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/007.png) |

|           |                                                             |
|-----------|-------------------------------------------------------------|
| Steps | To continue to access the VistA system, follow these steps: |

|          |                                                                                                                                                      |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                           |
| 1        | Click the drop-down arrow in the Connect To dialog box to display the list of systems or press \<Enter\> for the default system (displayed). |
| 2        | In that list, click the connection you need.                                                                                                         |
| 3        | Then click OK or press \<Enter\> to sign-on to that system.                                                                                  |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Cancel Button</strong></td>
<td><p>You can click the <strong>Cancel</strong> button to exit the <strong>Connect To</strong> dialog box.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;C&gt;</strong> key to cancel.</p></td>
</tr>
</tbody>
</table>

|                 |                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Help Button | The Help button displays online help regarding the dialog box that is currently displayed. You can also press the \<F1\> key to display online help. |

Sign-On to VistA

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Introduction</strong></td>
<td><p>The <strong>VISTA Sign-on</strong> window is the main sign-on window for all VistA GUI applications. It displays the current system introductory messages, and lets you sign on to the system using your Access and Verify codes.</p>
<p><strong><u>Note</u>:</strong> This is the first window if you have only one system to sign-on to; otherwise, see the previous page.</p></td>
</tr>
</tbody>
</table>

|                   |                                                                 |
|-------------------|-----------------------------------------------------------------|
| VISTA Sign-on | To continue to sign on to the VistA system, follow these steps: |

|          |                                                                                     |
|----------|-------------------------------------------------------------------------------------|
| Step | Action                                                                          |
| 1        | In the Access Code box on the VISTA Sign-on window, enter your access code. |
| 2        | Press the \<Tab\> key to jump to the Verify Code box.                       |
| 3        | In the Verify Code box, enter your verify code.                                 |
| 4        | Press \<Enter\> or click OK to sign on.                                     |

|                          |                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| VistA Sign-on window | ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/008.png) |

|                     |                                                                                                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Time-saving Tip | Alternatively, in the access code box you can enter your access code, a semicolon, and your verify code all at once. Then press \<Enter\> or click OK to sign on. |

  
Display/Print Patient 2319 (23) – Excluded and Waiver, Continued

|                 |                                                                                                                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Menu Button | Once you have accessed the DOR window, the NPPD Detail Display window, or the View Prosthetic Billing Information window, you can return to the Prosthetics Main Menu by clicking the Menu button. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Multiple Windows Open</strong></td>
<td><p>After you log on, you can access multiple applications, and you can switch between open applications without having to re-log on and without losing displayed data.</p>
<p>You can keep a window open (any Prosthetics GUI application) by clicking the <strong>Menu</strong> button, returning to the <strong>Prosthetics Main Menu</strong> window and opening another application. Once you have multiple programs open, you can switch back and forth between them and not lose any data.</p>
<p><strong>Warning:</strong> If you change servers that you are logged into, then you will lose the data displayed in all open windows.</p></td>
</tr>
</tbody>
</table>

Logging Off

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Log Off</td>
<td><blockquote>
<p>You can also sign off the <strong>Prosthetics VistA Suite</strong> screen by clicking the <strong>Close</strong> Menu. The following message displays for you to click <strong>OK</strong> to continue or <strong>Cancel</strong> to cancel the log off procedure.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Confirmation Message</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/009.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24938076" class="anchor"></span>Sign-On Properties (Optional)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sign-on Properties</td>
<td><blockquote>
<p>From the <strong>Sign-on</strong> window, you can also set <strong>Sign-on Properties</strong> as shown below.</p>
<p><strong><u>Recommendation</u>:</strong> Do not change the settings. Use this option only if necessary.</p>
</blockquote></td>
</tr>
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
<p>To set sign-on properties, follow these steps:</p>
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
<td>From the <strong>VistA</strong> <strong>Sign-on</strong> window, click the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/010.png) icon at the top left corner (to the left of the window title name).</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>From the <strong>VistA Sign-on</strong> window menu, choose the <strong>Properties</strong> option.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/011.png)</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>Set any individual properties you want to change on the <strong>Sign-on Properties</strong> dialog box, and click <strong>OK</strong> to save those changes.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>To return the properties to their default values, click the <strong>Defaults</strong> button, and then click <strong>OK</strong> to save that change.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sign-on Properties window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/012.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Sign-on properties that you save will be used for subsequent sign-ons using this workstation.</p>
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
<td>Window Position</td>
<td><blockquote>
<p>Below are the window positions as they appear on your desktop.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                      |                                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Part                 | Function                                                                                                                   |
| Center (default) | The window will always appear in the center of the screen.                                                                 |
| Current          | The current position of the window will be saved and used in the future.                                                   |
| Remember         | Each time the window is used and closed, it will record its position and open in that same place the next time it is used. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Window Size</td>
<td><blockquote>
<p>Below are the window sizes as they appear on your desktop.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Part                 | Function                                                                                                               |
| Normal (default) | The size of the window as it was designed. Typically, this is 500 pixels wide by 300 pixels high.                      |
| Current          | The current size of the window will be saved and used in the future.                                                   |
| Remember         | Each time the window is used and closed, it will record its size and open with the same size the next time it is used. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Color and Font</td>
<td><blockquote>
<p>Below are the text background colors and fonts.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                      |                                                                          |
|----------------------|--------------------------------------------------------------------------|
| Part                 | Function                                                                 |
| Background Color | You can set the background color to Cream or White.                      |
| Font             | You can choose any font on your system to use for the Introductory Text. |

<span id="_Toc172537298" class="anchor"></span>Chapter 3 – Purchase Ordering

<span id="_Toc172537299" class="anchor"></span>The Purchase Order Control Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display data</td>
<td><blockquote>
<p>The <strong>Purchase Order Control</strong> window shown below will display consults from the Suspense module that have been entered through CPRS or entered manually. <strong>Open</strong> and <strong>Pending</strong> consults display here for one site or <strong>“All Sites</strong>” as well as a Purchasing Agent’s responsible SSN range for patients.</p>
<p>To access the Purchase Order Control window, click the <strong>Processing</strong> button on the Main Menu.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order Control window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/013.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Manager Notes</td>
<td><blockquote>
<p>The new feature, <strong>Manager Notes</strong> window, displays text-entered notes from a manager that can be displayed to all Purchasing Agents in their group.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Create P.O.</td>
<td><blockquote>
<p>You will create a PO from this window for a specific patient.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537300" class="anchor"></span>Select a Site and Status

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site field</td>
<td><blockquote>
<p>The first step to view purchasing transactions is to select a Site. There is a drop down list to select a specific site or you can select the <strong>All Sites</strong> checkbox (which is the default setting). The <strong>Site</strong> drop-down arrow may display a list of multiple sites for you to select one. When you click the drop down arrow, the checkmark from the <strong>All Sites</strong> checkbox disappears automatically.</p>
<p><strong>Recommendation:</strong> It is strongly recommended that you <u>always</u> select <strong>All Sites</strong> so a consult does not get overlooked.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order Control window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/014.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CBOC data</td>
<td><blockquote>
<p>If you want to view all available suspense entries/electronic consult orders including Community Based Outpatient Clinics (CBOC) data, click the <strong>All Sites</strong> checkbox instead of selecting your specific site from the <strong>Site</strong> drop-down list box. This ensures that the display will include all sites. For example, the Kenosha, Wisconsin CBOC will not display when the Milwaukee site is selected only. These records display when the <strong>All Sites</strong> checkbox is selected.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Status options</td>
<td><blockquote>
<p>The status selections are <strong>Open</strong> transactions and <strong>Pending</strong> transactions. They are both checked by default, but you can deselect one by clicking on it.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537301" class="anchor"></span>Select an SSN Range

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SSN Range</td>
<td><blockquote>
<p>This is a range of patient Social Security Numbers by the last two digits entered in the Starting SSN field and the Ending SSN field. When you enter a range, it will display electronic consults or manual suspense entries within that range.</p>
<p>A Purchasing Agent has two choices when entering SSN ranges:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Enter a specific SSN range within your responsible range by entering the Starting SSN and Ending SSN, or</p>
</blockquote></li>
<li><blockquote>
<p>Keep the “Or…your assigned SSN range” checkbox checked (which is the default setting).</p>
</blockquote></li>
</ol>
<blockquote>
<p>The SSN range has been entered in the Site Parameters file by employee name. (See Chapter 1: Utilities Menu - Site Parameters File for more information.)</p>
<p>If your workload is categorized by the SSN for a specific Purchasing Agent, then you can display entries that are assigned by one Purchasing Agent at a time.</p>
<p><strong>Note:</strong> Enter a range of 00 to 99 to view all Purchasing Agents’ SSNs for all patients.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SSN Range or Assigned SSN Range checkboxes</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/015.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display button</td>
<td><blockquote>
<p>Click the <strong>Display/Refresh</strong> button once you have selected a Site(s), Status and an SSN range. The transactions displayed depend upon what site was selected, whether you have selected <strong>Open</strong> or <strong>Pending</strong> or both statuses as well as the SSN range for the Purchasing Agent.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Data</td>
<td><blockquote>
<p>The data that is displayed includes the following:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Done</p>
</blockquote></li>
<li><blockquote>
<p>Type (Routine, Eyeglass, Manual, Contact Lens and Clone)</p>
</blockquote></li>
<li><blockquote>
<p>Station</p>
</blockquote></li>
<li><blockquote>
<p>Date (Create date of Suspense entry)</p>
</blockquote></li>
<li><blockquote>
<p>Days (Number of days the transaction has remained in Open or Pending status)</p>
</blockquote></li>
<li><blockquote>
<p>Patient</p>
</blockquote></li>
<li><blockquote>
<p>SSN</p>
</blockquote></li>
<li><blockquote>
<p>Description (of the transaction)</p>
</blockquote></li>
<li><blockquote>
<p>Status (Open or Pending)</p>
</blockquote></li>
<li><blockquote>
<p>IEN 668</p>
</blockquote></li>
<li><blockquote>
<p>Pt IEN</p>
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
<td>Purchase Order Control list</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/016.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754782" class="anchor"></span>Change Data Display

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sizing columns</td>
<td><blockquote>
<p>Columns are sizable on this window, but not movable. To resize a column, you can place the cursor on the column header borderline until you can view the double-headed arrow. Then click and drag the column until it is the size you want.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column sorting</td>
<td><blockquote>
<p>You can manipulate the layout of the view in the <strong>Purchase Order Control</strong> window for display purposes. The following can be done for column sorting features:</p>
</blockquote>
<ul>
<li><p>To enlarge a column, click and drag a cell border.</p></li>
</ul>
<ul>
<li><p>To sort on any column, click on the header to sort it in <u>ascending order</u>.</p></li>
</ul>
<ul>
<li><p>If you click on the same column again, it will sort it in <u>descending order</u>.</p></li>
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
<td>Refresh data</td>
<td><blockquote>
<p>You can click the <strong>Display/Refresh</strong> button to update your window with any new transactions that may have been added into Suspense.</p>
<p>If you have changed the sort order, you can refresh your data by clicking the <strong>Display/Refresh</strong> button again.</p>
<p><strong><u>Note</u>:</strong> Refresh does not reset any column resizing that has been done.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Clear button</td>
<td><blockquote>
<p>You can use the <strong>Clear</strong> button to blank out the window and start over with new display criteria.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu button</td>
<td><blockquote>
<p>The <strong>Menu</strong> button returns you to the <strong>Prosthetics Main Menu</strong> window where you can open additional applications at the same time.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>2319 button</td>
<td><blockquote>
<p>You can display all eight tabs of 2319 data for a patient from this button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CPRS button</td>
<td><blockquote>
<p>You can view a CPRS record for a patient from this button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Request button</td>
<td><blockquote>
<p>You can view a Request (if information is available for that patient) from this button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754783" class="anchor"></span>View Column Descriptions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Done</td>
<td><blockquote>
<p>The Done column displays a <strong>Yes</strong> after you have created a purchase order with one or more items on it.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Type</td>
<td><blockquote>
<p>The <strong>Type</strong> column displays one of the following record types for the Purchase Order transaction: Manual Suspense entry or Routine Consult (electronic orders via CPRS including Eyeglass, Contact Lens and Home Oxygen orders). Clone is also a type of record that may display.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Station</td>
<td><blockquote>
<p>The Station column displays the Station Number of the selected Purchasing Agent.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td><blockquote>
<p>The <strong>Date</strong> column displays the date the consult was entered into Suspense or the manual entry was created in Suspense.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Days</td>
<td><blockquote>
<p>The <strong>Days</strong> column displays the number of days the transaction has remained in Open or Pending status.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Patient</td>
<td><blockquote>
<p>The <strong>Patient</strong> column contains the veteran’s name, last name first. All patient transactions for the requested date range appear for Non-Service Connected (NSC) veterans.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SSN</td>
<td><blockquote>
<p>The <strong>SSN</strong> column displays the patient’s Social Security Number (SSN).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>The <strong>Description</strong> column displays the prescription that was entered on the consult or during the manual suspense entry.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Status</td>
<td><blockquote>
<p>The status displays either <strong>Open</strong> or <strong>Pending</strong>. Records with an <strong>Open</strong> status are shown in blue. Pending status transactions are shown in red.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537304" class="anchor"></span>Chapter 4 - Display the 2319

<span id="_Toc172537305" class="anchor"></span>2319 Button

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>2319 Button</td>
<td><blockquote>
<p>You can click the <strong>2319</strong> button on the <strong>Purchase Order Control</strong> window to display the View 2319 window with the following eight tabs:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Patient Demographics</p>
</blockquote></li>
<li><blockquote>
<p>Clinic Enrollments/Correspondence</p>
</blockquote></li>
<li><blockquote>
<p>Entitlement Info (not available)</p>
</blockquote></li>
<li><blockquote>
<p>Appliance Transaction</p>
</blockquote></li>
<li><blockquote>
<p>Auto Adaptive Info (not available)</p>
</blockquote></li>
<li><blockquote>
<p>Critical Comments</p>
</blockquote></li>
<li><blockquote>
<p>HISA Information</p>
</blockquote></li>
<li><blockquote>
<p>Home Oxygen</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>2319 button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/017.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View 2319 window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/018.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/019.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537306" class="anchor"></span>View 2319 – Patient Demographics (Tab 1)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Tab 1</td>
<td><blockquote>
<p>You can view the <strong>Patient Demographics</strong> tab that includes a patient’s benefits, eligibility, next of kin, emergency contact info (if available), and disabilities.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Patient Demographics tab</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/020.png)</p>
</blockquote></td>
</tr>
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
<p>To close this window and return to the main <strong>Purchase Order Control</strong> window, click the <strong>Close</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Demographics data</td>
<td><blockquote>
<p>You can view the patient demographics for the veteran.</p>
<p>This includes: Name (in red if deceased, with Date of Death listed above the Date of Birth and a blank age field), address, next of kin, emergency contact information, veteran benefits and eligibility (former Prisoner of War (highlighted in blue if “Yes”), Aid &amp; Attendance, service connected, non-service connected, etc.).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537307" class="anchor"></span>View 2319 – Clinic Enrollments/Correspondence (Tab 2)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Tab 2</td>
<td><blockquote>
<p>You can view the <strong>Clinic Enrollments/Correspondence</strong> tab that includes last movement actions, clinic enrollments, pending appointments, and letters on file</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Clinic Enrollments/ Correspondence</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/021.png)</p>
</blockquote></td>
</tr>
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
<p>To close this window and return to the main <strong>Purchase Order Control</strong> window, click the <strong>Close</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>This second tab details clinic enrollments and correspondence for the veteran. This includes the following: the last movement actions (i.e., hospital admissions and discharges), clinic enrollments, pending appointments and correspondence letters.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537308" class="anchor"></span>View 2319 – Entitlement Info (Tab 3)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Tab 3</td>
<td><blockquote>
<p>The <strong>Entitlement Info</strong> tab is not available in this version of the Prosthetics application. This tab details entitlement and loan information for the veteran. This includes the following: PSC Issue Card, clothing allowance, items on loan, and items returned.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Entitlement Info</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/022.png)</p>
</blockquote></td>
</tr>
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
<p>To close this window and return to the main <strong>Purchase Order Control</strong> window, click the <strong>Close</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537309" class="anchor"></span>View 2319 – Appliance Transactions (Tab 4)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Tab 4</td>
<td><blockquote>
<p>The <strong>Appliance Transactions</strong> tab displays the following information:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Date (this is the date of the PO)</p>
</blockquote></li>
<li><blockquote>
<p>Quantity</p>
</blockquote></li>
<li><blockquote>
<p>HCPC Item</p>
</blockquote></li>
<li><blockquote>
<p>Type</p>
</blockquote></li>
<li><blockquote>
<p>Vendor</p>
</blockquote></li>
<li><blockquote>
<p>Station</p>
</blockquote></li>
<li><blockquote>
<p>Serial</p>
</blockquote></li>
<li><blockquote>
<p>HCPC</p>
</blockquote></li>
<li><blockquote>
<p>Total Cost</p>
</blockquote></li>
<li><blockquote>
<p>IEN 660</p>
</blockquote></li>
</ul>
<blockquote>
<p>The total number of records found displays at the bottom.</p>
<p>You can click the <strong>View Detail</strong> button to display the <strong>Appliance Transaction Detail</strong> window, which includes Appliance Item detail, IFCAP vendor, costs, lab info, historical data, and an extended description. (See the next page for more info about this window.)</p>
<p><strong>Note:</strong> Columns are resizable on this window (not movable).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance Transactions</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/023.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

View 2319 – Appliance Transactions (Tab 4), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Detail</td>
<td><blockquote>
<p>When you select a record and click the <strong>View Detail</strong> button, the <strong>Appliance Transaction Detail</strong> window displays as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance Transaction Detail</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/024.png)</p>
</blockquote></td>
</tr>
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
<p>To close this window and return to the main <strong>Purchase Order Control</strong> window, click the <strong>Close</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537310" class="anchor"></span>View 2319 – Auto Adaptive Info (Tab 5)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Tab 5</td>
<td><blockquote>
<p>The <strong>Auto Adaptive Info</strong> tab is not available in this version of the Prosthetics application.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Auto Adaptive Info</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/025.png)</p>
</blockquote></td>
</tr>
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
<p>To close this window and return to the main <strong>Purchase Order Control</strong> window, click the <strong>Close</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537311" class="anchor"></span>View 2319 – Critical Comments (Tab 6)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Tab 6</td>
<td><blockquote>
<p>You can view comments in the <strong>Critical Comments</strong> tab as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Critical Comments window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/026.png)</p>
</blockquote></td>
</tr>
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
<p>Click the <strong>Close</strong> button to exit the <strong>Critical Comments</strong> window return to the main <strong>Purchase Order Control</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537312" class="anchor"></span>View 2319 – HISA Information (Tab 7)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Tab 7</td>
<td><blockquote>
<p>On the <strong>HISA Information</strong> tab, if there is no data for a specific patient, it will state “NOTHING TO REPORT.”</p>
<p>This tab details the HISA (Home Improvement Structural Alteration) information including the date, quantity, HCPC item, type, vendor, station number, serial, HCPCS Code, total cost of the item ordered, and IEN 660.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HISA Information</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/027.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

View 2319 – HISA Information (Tab 7), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Detail</td>
<td><blockquote>
<p>When you select a record and click the <strong>View Detail</strong> button, the <strong>Appliance Transaction Detail</strong> window displays as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance Transaction Detail</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/028.png)</p>
</blockquote></td>
</tr>
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
<p>To close this window and return to the main <strong>Purchase Order Control</strong> window, click the <strong>Close</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537313" class="anchor"></span>View 2319 – Home Oxygen (Tab 8)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Tab 8</td>
<td><blockquote>
<p>The <strong>Home Oxygen</strong> tab displays the following information:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Date</p>
</blockquote></li>
<li><blockquote>
<p>Quantity</p>
</blockquote></li>
<li><blockquote>
<p>HCPC Item</p>
</blockquote></li>
<li><blockquote>
<p>Type</p>
</blockquote></li>
<li><blockquote>
<p>Vendor</p>
</blockquote></li>
<li><blockquote>
<p>Station</p>
</blockquote></li>
<li><blockquote>
<p>Serial</p>
</blockquote></li>
<li><blockquote>
<p>HCPC</p>
</blockquote></li>
<li><blockquote>
<p>Total Cost</p>
</blockquote></li>
<li><blockquote>
<p>IEN 660</p>
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
<td>Home Oxygen</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/029.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

View 2319 – Home Oxygen (Tab 8), Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Detail</td>
<td><blockquote>
<p>When you select a record and click the <strong>View Detail</strong> button, the <strong>Appliance Transaction Detail</strong> window displays as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance Transaction Detail</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/030.png)</p>
</blockquote></td>
</tr>
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
<p>To close this window and return to the main <strong>Purchase Order Control</strong> window, click the <strong>Close</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537314" class="anchor"></span>Chapter 5 - View a CPRS Record

<span id="_Toc172537315" class="anchor"></span>CPRS Button

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CPRS</td>
<td><blockquote>
<p>Click the <strong>CPRS</strong> button on the main <strong>Purchase Order Control</strong> window to display the <strong>View CPRS</strong> window if information is available.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CPRS button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/031.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CPRS Record</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/032.png)</p>
</blockquote></td>
</tr>
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
<p>To exit the <strong>View CPRS</strong> window, click the <strong>Close</strong> button to return to the <strong>Purchase Order Control</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537316" class="anchor"></span>Chapter 6 - View a Request

<span id="_Toc172537317" class="anchor"></span>Request Button

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Request button</td>
<td><blockquote>
<p>Click the <strong>Request</strong> button on the main <strong>Purchase Order Control</strong> window to display the <strong>View Request</strong> window (if information is available) including a description of the item/services, Order/Suspense date, Initial Action and/or Completion date if applicable, and Initial Action or Completion note if available.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Request button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/033.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Request window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/034.png)</p>
</blockquote></td>
</tr>
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
<p>To exit the <strong>View Request</strong> window, click the <strong>Close</strong> button to return to the <strong>Purchase Order Control</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537318" class="anchor"></span>Chapter 7 - Purchase Order Creation

<span id="_Toc172537319" class="anchor"></span>Create a P.O.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>First step</td>
<td><blockquote>
<p>Select a patient from the <strong>Purchase Order Control</strong> window. Check Eligibility for the patient on the 2319 <strong>Patient Demographics</strong> tab, and check to see if there are any duplicate orders on the 2319 <strong>Appliance Transactions</strong> tab. Then proceed to click the <strong>Create P.O.</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Create P.O. button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/035.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order window</td>
<td><blockquote>
<p>The <strong>Purchase Order</strong> window displays a two-panel window as shown below. It contains the patient name and SSN in the title bar.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The <u>left-side</u> panel is the <strong>Policy Panel</strong>. This panel has buttons that display pop-up windows for you to enter and display additional purchase order information.</p>
</blockquote></li>
<li><blockquote>
<p>The <u>right-side</u> is the <strong>Purchase Order</strong> window. Its information fields display data as you complete the information in the Policy Panel pop-up windows.</p>
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
<td><p>Two-panel Purchase Order window</p>
<p><strong>Policy Panel</strong></p></td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/036.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Create a P.O., Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CPRS and Request</td>
<td><blockquote>
<p>You can also review the CPRS and the Request buttons for a patient before creating a PO to update yourself on the patient.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>More about the Policy Panel</td>
<td><blockquote>
<p>You begin the PO process by clicking each button on the <strong>Policy Panel</strong> in order. If a button has green text, it is not required to click it (i.e., <strong>Due Date</strong> button and possibly the <strong>Site</strong> button) but you can click it to change the default data. If a button has red text, then it is a required button, and you must click it or you will not be able to proceed to the next button on the list in the <strong>Policy Panel</strong>.</p>
<p><strong>Note:</strong> The <strong>Site</strong> button already has a check in the checkbox in this example because a <strong>Site</strong> was selected before displaying transactions on the previous window. You can change the default <strong>Site</strong> by clicking the button. The <strong>Due Date</strong> does not have a checkbox and has a default setting of 30 days from the current date. You only need to check it if you want to change the <strong>Due Date</strong> setting.</p>
<p>As you click each button on the <strong>Policy Panel</strong> and fill in information in the pop-up window that displays, the fields in the <strong>Purchase Order</strong> window will automatically populate with the data you entered in the corresponding pop-up window.</p>
<p>Once you select a button on the <strong>Policy Panel</strong>, notice the checkbox in the <strong>Policy Panel</strong> next to a button is automatically checked. This tracks which buttons you have completed in the PO creation process.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchasing Order window fields</td>
<td><blockquote>
<p>The fields within the <strong>Purchase Order</strong> window are populated in the order of the buttons on the Policy Panel. As you click each button, a pop-up window displays allowing you to enter data that will automatically fill in the fields on the <strong>Purchase Order</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537320" class="anchor"></span>Select a Due Date

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>First Step on Policy Panel</td>
<td><blockquote>
<p>Click the <strong>Due Date</strong> button on the <strong>Policy Panel if you want to change the default of 30 days from the current date. You do not need to click this button if you want to keep the 30 day default</strong>. If you click the <strong>Due Date</strong> button, a four-month calendar displays for you to select a due date.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Selecting a due date</td>
<td><blockquote>
<p>The calendars display with the current date circled in red and the due date marked with a blue ellipse. You can accept the current date by clicking <strong>OK</strong>. You can also change the date by the following methods:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|             |                                                                                                                                                                                                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change the… | Description                                                                                                                                                                                     |
| Day     | Click on the actual day of the week in the calendar. You must select the current date or a date in the future.                                                                                  |
| Month   | Click on the month at the top of the calendar to display a list of all months and select one from there. You can decrease or increase one month at a time by clicking the left or right arrows. |
| Year    | Click on the year and an up and down arrow button displays for you to increase or decrease the year.                                                                                            |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Calendars</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/037.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537321" class="anchor"></span>Select a Site

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select a Site</td>
<td><blockquote>
<p>Click the <strong>Site</strong> button on the <strong>Policy Panel</strong>. You can click the drop-down arrow to select a site. Click <strong>OK</strong> to display the data on the <strong>Purchase Order</strong> <strong>Control</strong> window. Notice that a green checkmark displays next to the <strong>Site</strong> button once you have selected an option.</p>
<p><strong>Note:</strong> The number in the <strong>Common Numbering Series</strong> field comes from the Site Parameters file and automatically displays when you select a Site. You can now select a different numbering series, if that is how your site is organized.</p>
</blockquote></td>
</tr>
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
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/038.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site ID and Common Numbering Series fields</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/039.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Checkmarks</td>
<td><blockquote>
<p>Checkmarks display next to the buttons on the Policy Panel to track which steps you have completed in the PO creation process.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Add/Edit Patient option</td>
<td><blockquote>
<p>If you select a patient that is not in the Prosthetics Patient File, a message displays to inform you that you are unable to continue. Click <strong>OK</strong> to clear the message. Please use the <strong>Add/Edit Patient (AP)</strong> option to add the patient to Prosthetics.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/040.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537322" class="anchor"></span>Select a Purchase Card

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Card button</td>
<td><blockquote>
<p>Select a purchase card by clicking the <strong>Purchase Card</strong> button on the <strong>Policy Panel</strong>.</p>
<p>The <strong>Please Select a Purchase Card</strong> pop-up window displays. Click the dropdown arrow to display a list and select one.</p>
<p>To select a different <strong>Common Numbering Series</strong>, click the dropdown arrow.</p>
<p>Click <strong>Ok.</strong> The window disappears and the data displays in the <strong>Purchase Order</strong> <strong>Control</strong> window based on your selection for the Purchase Card number, Fund Control Point and Cost Center.</p>
<p><strong>Note:</strong> Notice that a checkmark displays next to the <strong>Purchase Card</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select a Purchase Card</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/041.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cost Center button</td>
<td><blockquote>
<p>The Cost Center is already populated for you when you select a Purchase Card.</p>
<p>Cost Center is not editable.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>P Card Name / Cost Center / Fund Control Point</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/042.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537323" class="anchor"></span>Cost Center

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cost Center button</td>
<td><blockquote>
<p>The Cost Center is already populated for you when you select a Site.</p>
<p>Cost Center is not editable.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537324" class="anchor"></span>Select a Vendor

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Vendor field</td>
<td><blockquote>
<p>Click the <strong>Vendor</strong> button on the <strong>Policy Panel</strong>. Enter a partial spelling (minimum of three characters) of a Vendor and click the drop-down arrow to select one beginning with the criteria that you entered. Click <strong>OK</strong> to accept it. After the vendor is selected the following fields cannot be changed: Site, Purchase Card and Vendor.</p>
<p><strong>Note:</strong> If you do not enter at least three characters of a vendor before you click the dropdown arrow, the list will be empty.</p>
<p><strong>Warning Message:</strong> If you enter a partial spelling search that is not descriptive enough, a warning message dialog box will display.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Partial Spelling Search</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/043.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Vendor list</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/044.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Vendor field</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/045.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537325" class="anchor"></span>Select the Delivery Method

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Delivery locations</td>
<td><blockquote>
<p>Click the <strong>Delivery</strong> button on the <strong>Policy Panel</strong>. There are three delivery location options including: <strong>Prosthetics</strong>, <strong>Veteran</strong>, and an <strong>Other Location - At This Site</strong> option, which is a new option with Patch RMPR*3*90.</p>
<p><strong>Note:</strong> If you choose the <strong>Other Location- At This Site</strong> option, another pop-up window displays as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select a Delivery Location</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/046.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Other Location</td>
<td><blockquote>
<p>You can enter a free-text description in the blank field (with a maximum of 50 characters) on the <strong>Other Location – At This Site</strong> pop-up window which is a new feature with this patch. This helps warehouse employees to determine a delivery location.</p>
<p><strong>Note:</strong> This information does not print on a hard copy printout.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Other Location</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/047.png)</p>
</blockquote></td>
</tr>
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
<p>Click <strong>OK</strong> to return to the <strong>Purchase Order Control</strong> window and select the next button on the <strong>Policy Panel</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537326" class="anchor"></span>Chapter 8 - Add Item(s) to the Purchase Order

<span id="_Toc172537327" class="anchor"></span>Add Items Button

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order Items</td>
<td><blockquote>
<p>When you click the <strong>Add Items</strong> button on the <strong>Policy Panel</strong>, the <strong>Purchase Order</strong> window displays as shown below. The Purchase Order number, patient’s name and SSN display at the top. This window provides multiple steps to add information when adding one or multiple items to the Purchase Order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Add Items button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/048.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Add Items Button, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>First Step</td>
<td><blockquote>
<p>On the Purchase Order window, you MUST select a <strong>Type of Transaction</strong> as either <strong>New/Replace</strong>, <strong>Service/Repair</strong> or <strong>Rental Item.</strong></p>
<p><strong>Note:</strong> These three transactions types have been consolidated from four types with this patch.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Second Step</td>
<td><blockquote>
<p>The <strong>Patient Category</strong> (<strong>SC</strong> or <strong>NSC</strong>) radio buttons are displayed. This is an enhanced feature with this patch that has been consolidated into two options. You MUST select either: <strong>SC</strong> (Service Connected) or <strong>NSC</strong> (Non Service Connected).</p>
<p><strong>Note:</strong> If there is a SC Disability, it will display in the box at the top. There is no longer any additional selection of eligibility for the Special Category.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/049.png)</p>
<p><strong>Note:</strong> You can use the <strong>Tab</strong> key to tab from one field to the next on this window. You can also use the spacebar to check a checkbox.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Add Items Button, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing Item</td>
<td><blockquote>
<p>You can select the <strong>Billing Item</strong> by entering partial spelling search criteria <u>with a minimum of three characters</u>. You MUST enter a partial spelling to begin your search. Once you type the initial search value, you can click on the drop-down arrow and a list will display. From this list, you can scroll to select an option.</p>
<p><strong>Note:</strong> This billing information does not display on the 2319 nor does it print on the Purchase Order. It is only for billing purposes.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/050.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Criteria Search</td>
<td><blockquote>
<p>You MUST enter a partial spelling of the <strong>HCPCS</strong> Description (or HCPCS code or synonym) to begin your search. Once you type an initial search value, you can then click on the drop-down arrow and a list will display. From this list, you can scroll to select an option. If you know the code, you can enter the entire HCPCS code.</p>
<p><strong>Note:</strong> The search criteria must be for a valid HCPCS code.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Number of Bids</td>
<td><blockquote>
<p>Click <strong>Number of Bids</strong> to enter a bid on this item. The maximum number of bids on an item is 3. For certain HCPCS (e.g., HISAS, HISAN), this window will automatically open for your selection. It should be used whenever you receive a bid for a prosthetic item.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Contract</td>
<td><blockquote>
<p>You can select the <strong>Contract</strong> information by clicking the drop down arrow to begin your search. Once you type an initial search value, you can then click on the drop-down arrow and a list will display. From this list, you can scroll to select an option.</p>
<p><strong>Note:</strong> The Contract information is tied to the Vendor in the <strong>Vendor</strong> file and will display according to the Vendor that was selected.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Add Items Button, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Brief Description</td>
<td><blockquote>
<p>You can enter a <strong>Brief Description</strong> in the free-text field (with a maximum of 60 characters) which prints on the purchase order. You can also (optionally) add free-text Remarks. If you would like to enter an extended description, click the <strong>Extended Description</strong> button. See below for more information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Extended Description</td>
<td><blockquote>
<p>Notice as the <strong>Extended Description</strong> window shows below that you can type in a free-text extended description (of unlimited maximum number of characters). This information appears on the printed PO.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Extended Description</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/051.png)</p>
</blockquote></td>
</tr>
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
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/052.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Add Items Button, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Remarks</td>
<td><blockquote>
<p>You can enter free-text information up to a maximum of 30 characters in the Remarks field.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Extended and Waiver</td>
<td><blockquote>
<p>There are two NEW prompts shown below. You can click the checkboxes if the item is considered excluded or has a waiver. (You can also use the spacebar to select one of the checkboxes after using the <strong>Tab</strong> key.)</p>
<p>If you forget to select the <strong>Excluded</strong> or <strong>Waiver</strong> checkboxes in the creation of the PO, you can go into the Roll and Scroll <strong>Enter Waiver or Excluded Notice (EW)</strong> option and enter the information afterwards.</p>
</blockquote></td>
</tr>
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
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/053.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Optional fields</td>
<td><blockquote>
<p>The following fields are optional:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Manufacturer (with a maximum of 30 characters)</p>
</blockquote></li>
<li><blockquote>
<p>Model (with a maximum of 30 characters)</p>
</blockquote></li>
<li><blockquote>
<p>Serial # (with a maximum of 15 characters)</p>
</blockquote></li>
<li><blockquote>
<p>Lot # (with a maximum of 30 characters)</p>
</blockquote></li>
</ul>
<blockquote>
<p>This information prints on the Purchase Order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Add Items Button, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Unit of Issue</td>
<td><blockquote>
<p>You can select a <strong>Unit of Issue</strong> from a drop-down selection list. Enter a partial spelling search of one character minimum.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Qty and Cost</td>
<td><blockquote>
<p>You can enter the <strong>Quantity</strong> and <strong>Unit Cost</strong> of the item you are adding to the Purchase Order. Notice that the <strong>Total Cost</strong> will be calculated automatically for you when you click in that field. You can also use the <strong>Tab</strong> key to view the Total Cost.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Add Item to PO button – REQUIRED!!</td>
<td><blockquote>
<p><strong>REQUIRED:</strong> Once you have entered all the correct information for the Item, you <strong>MUST</strong> click the <strong>Add Item to P.O.</strong> button. This button will appear double lined or highlighted to remind you to click it.</p>
<p>The information disappears from this <strong>Purchase Order</strong> window to allow you to add more items if necessary.</p>
<p><strong>WARNING:</strong> If you click the <strong>Return to P.O.</strong> button before you click the <strong>Add Item to P.O.</strong> button, you will LOSE all the data that you have entered for that specific item.</p>
</blockquote></td>
</tr>
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
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/054.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537328" class="anchor"></span>Return to P.O. Button

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Return to P.O. button</td>
<td><blockquote>
<p>After you click the <strong>Add Item to P.O.</strong> button for all the items you want to add to this Purchase Order, then click the <strong>Return to P.O.</strong> button. The <strong>Purchase Order Control</strong> window displays where you can verify that the item(s) has been added to the Purchase Order.</p>
<p><strong>Warning:</strong> Do NOT click the <strong>Return to P.O.</strong> button before the <strong>Add Item to P.O.</strong> button as the data will disappear and you will have to re-enter it.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Return to P.O. button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/055.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537329" class="anchor"></span>Add Additional Items

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item List</td>
<td><blockquote>
<p>Notice below the list with the item added in the display. It carries over the information that you selected from the <strong>Purchase Order</strong> window.</p>
<p>You can add more items by clicking the <strong>Add Items</strong> button as many times as necessary.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Add Items button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/056.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537330" class="anchor"></span>Edit/Delete an Item

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item List</td>
<td><blockquote>
<p>You can edit a line item or delete a line item by clicking on it and clicking the <strong>Edit / Delete Item</strong> button. You are returned to the <strong>Purchase Order</strong> window to make your edit or deletion.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Edit / Delete Item</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/057.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Edit/Delete an Item, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Delete or Edit an Item</td>
<td><blockquote>
<p>Once you have made edits to the Item that you are adding, click the <strong>Update Item</strong> button.</p>
</blockquote>
<ul>
<li><blockquote>
<p>OR –</p>
</blockquote></li>
</ul>
<blockquote>
<p>Once you have verified the item you want to delete, click the <strong>Delete This Item</strong> button.</p>
</blockquote>
<ul>
<li><blockquote>
<p>THEN –</p>
</blockquote></li>
</ul>
<blockquote>
<p>Click the <strong>Return to PO</strong> button. This will save the edits that you have made as well as the deletion.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/058.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537331" class="anchor"></span>Chapter 9 - Purchase Order Creation Continued

<span id="_Toc172537332" class="anchor"></span>Enter Discount/Shipping

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Discount/ Shipping (Optional)</td>
<td><blockquote>
<p>Click the <strong>Discount/Shipping</strong> button on the <strong>Policy Panel</strong>. Enter the Discount percentage for the item you are ordering and the Shipping amount (if applicable).</p>
<p>Click the <strong>OK</strong> button to add the Discount and the Shipping to the order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Add Discount and Shipping Charge</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/059.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Discount and Shipping amounts shown</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/060.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537333" class="anchor"></span>Enter Your Electronic Signature

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print PO</td>
<td><blockquote>
<p>The PO will print automatically once you submit the PO. The PO can print on both Windows printers and VistA printers. You can select a different printer by either clicking <strong>Windows Printer</strong> or selecting a <strong>VistA Printer</strong> from the dropdown list.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Signature</td>
<td><blockquote>
<p>Click the <strong>Submit Order</strong> button on the <strong>Policy Panel</strong>. Enter your Electronic Signature and click the <strong>Send PO</strong> button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Enter Your Electronic Signature</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/061.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Complete order</td>
<td><blockquote>
<p>Click the <strong>OK</strong> button on the <strong>Confirmation</strong> window as shown below. This window displays the current status of the PO as either Pending or Complete.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Confirmation Window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/062.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Insufficient Funds</td>
<td><blockquote>
<p>If your purchase card does not have adequate funds to cover the purchase order, you will get the message below. You can get more funds allocated to the purchase card and continue the process.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Insufficient Funds Window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/063.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537334" class="anchor"></span>Post CPRS Note

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Close the order</td>
<td><blockquote>
<p>Click the <strong>Post CPRS Note</strong> button on the <strong>Policy Panel</strong> when you have entered all the necessary information for the item you are ordering. The <strong>Post Note to CPRS</strong> pop-up window displays as shown below.</p>
<p><strong>NOTE:</strong> By posting your note in this new method, you have automatically linked your transaction to the consult and created your patient care encounter. No further linking is necessary!</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Post Note to CPRS</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/064.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Post Complete</td>
<td><blockquote>
<p>You have three checkboxes to choose a selection for your note-to-be: 1) Post Complete, 2) Post Initial and 3) Post Other. Last, click the <strong>Post Note</strong> button.</p>
<p>Click the <strong>Post Complete</strong> checkbox (if applicable), and enter a note in the free-text box area (optional) which has unlimited amount of space to enter a note. This checkbox places the transaction from a PENDING status to a CLOSED status.</p>
<p>Click the <strong>OK</strong> button to process the completion. Continue to the next page.</p>
<p><strong>NOTE:</strong> When you select Post Complete an encounter is created.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Post Initial and Post Other</td>
<td><blockquote>
<p>If you select the <strong>Post Initial</strong> checkbox, this places the transaction from an OPEN status to a PENDING status. The <strong>Post Other</strong> checkbox will put the transaction in a PENDING status if it is in an OPEN status or will keep it at PENDING if that is the current status.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Post CPRS Note, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Complete order</td>
<td><blockquote>
<p>When you have completed the process to posting the CPRS note, you will receive the following two pop-up messages. If you selected the <strong>Post Complete</strong> checkbox, the first pop-up displays as shown with the Closed status for the suspense entry.</p>
<p>Click the <strong>OK</strong> button to finalize the order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Closed Suspense</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/065.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Post Initial</td>
<td><blockquote>
<p>When you click the <strong>Post Initial</strong> checkbox, the status of the suspense entry changes from Open to Pending status. The popup window will display as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Post Initial Popup window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/066.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Post CPRS Note, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Done column</td>
<td><blockquote>
<p>The <strong>Purchase Order Control</strong> window returns after you have completed the purchase order creation process. Notice that the <strong>Done</strong> column displays “<strong>Yes</strong>” in it.</p>
<p>The status of the transaction will be updated from Open to Pending or from Pending to Closed.</p>
<p><strong>WARNING:</strong> If you click the <strong>Refresh</strong> Button, the <strong>Done</strong> column will refresh and the transactions that you have completed will disappear from the list as they now have a CLOSED status.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase Order Control window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/067.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754795" class="anchor"></span>

Chapter 10 - Closing and Exiting

<span id="_Toc89754796" class="anchor"></span>Exit the Purchase Order Control Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit the Application</td>
<td><blockquote>
<p>You can exit the application by first clicking the <strong>Menu</strong> button on the <strong>Purchase Order Control</strong> window. Then click the <strong>Close</strong> button on the <strong>Main Prosthetics</strong> window: When the <strong>Confirmation</strong> window displays, click the <strong>OK</strong> button to exit.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Confirmation window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/068.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cancel button</td>
<td><blockquote>
<p>If you click the <strong>Cancel</strong> button, you will remain in the application and can continue to work.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537337" class="anchor"></span>Sample Printout

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Reprint PO</td>
<td><blockquote>
<p>Below is a reprint of the PO number: 0U7820.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purchase order reprint option</td>
<td><p>Select Transaction or Patient Name: <strong>0U7820</strong> 2-15-2005PROSpatient,one Y EYEGLASSES-PRES</p>
<p>Would you like to print the Privacy Act Statement? Yes// (Yes)</p>
<p>Would you like to print a Patient Notification letter? No// (No)</p>
<p>DEVICE: HOME// INCOMING TELNET Right Margin: 80//</p>
<blockquote>
<p>OMB Number 2900-0188 PO#: 0U7820</p>
</blockquote></td>
</tr>
</tbody>
</table>

\*\*\*ORIGINAL COPY AND COMMERCIAL INVOICE MUST BE SUBMITTED\*\*\*

TO THE VAMC PROSTHETIC ACTIVITY LISTED BELOW

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Department of Veterans Affairs\|Prosthetic Authorization for Items or Services

-------------------------------------------------------------------------------

1\. Name and Address of Vendor 2. Name and Address of VA Facility

INVACARE DVAMC BAY PINES 516/121 (516/121)

899 CLEVELAND ST PROSTHETIC & SENSORY AIDS SERVICE

P O BOX 4028 BAY PINES, FL 33744

ELYRIA,OH 44036

800-642-8262 727-398-9345

-------------------------------------------------------------------------------

3\. Veterans Name (Last, First, MI) 4. Date of Authorization

PROSpatient,one FEB 15, 2005

-------------------------------------------------------------------------------

5\. Veterans Address 6. Date Required

9 E ORANGE ST MAR 17, 2005

SERIA LEONE,LOUISIANA 12345 ----------------------------------------

9\. Authority For Issuance CFR 17.115

304-288-3401 CHARGE MEDICAL APPROPRIATION

-------------------------------------------------------------------------------

7\. Claim Number SS 8. ID \#: 4800 (Used to be full SSN.)

-------------------------------------------------------------------------------

10\. Statistical Data 11. FOB Point 12. Discount 13. Delivery Time

SC/IP ORIGIN % 12 30 Days

--------------------------------------------------

14\. Delivery To: OTHER LOCATION AT THIS SITE

-------------------------------------------------------------------------------

15\. DESCRIPTION OF ITEMS OR SERVICES AUTHORIZED

-------------------------------------------------------------------------------

ITEM NUMBER DESCRIPTION QUANTITY UNIT UNIT AMOUNT

ORDERED PRICE

-------------------------------------------------------------------------------

\#1. EYEGLASSES 1 EA 25.00 25.00

Serial Number: 48DJ47DK39 Lot \#: 12

Model: 2A Make: INVACARE

-------------------------------------------------------------------------------

16\. Contract Number: GS-00F-8355A(MAS) Subtotal: 25.00

ACCT.#: 95150 Discount \$ 3.00 Shipping: 24.00 Total \$ 46.00

-------------------------------------------------------------------------------

17\. Signature of 18. DATE 19. Signature and Title of 20. Date

Requesting Official Contracting/Accountable Officer

PROSuser,one PROSuser,one

-------------------------------------------------------------------------------

Order and Receipt Action

-------------------------------------------------------------------------------

21. Order Number 22. Exp Date 23. Date Item Received 24. Date Delivered

4716360100064653 (Purchase Order Number and <span class="mark">Expiration Date</span> added.)

-------------------------------------------------------------------------------

25\. The articles or services listed herein have been received, or rendered

ordered in the quantity and quality specified originally or as shown by

authenticated changes, except as noted.

Signature of Veteran or VA Official

-------------------------------------------------------------------------------

Acct. Symbol 516-0U7820

-------------------------------------------------------------------------------

ADP Form 10-2421PC APR 1991

CONTINUATION OF PURCHASE CARD ORDER NUMBER: 0U7820 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Department of Veterans Affairs\|Prosthetic Authorization for Items or Services

-------------------------------------------------------------------------------

1\. Name and Address of Vendor 2. Name and Address of VA Facility

INVACARE DVAMC BAY PINES 516/121 (516/121)

899 CLEVELAND ST PROSTHETIC & SENSORY AIDS SERVICE

P O BOX 4028 BAY PINES, FL 33744

ELYRIA,OH 44036

800-642-8262 727-398-9345

-------------------------------------------------------------------------------

3\. Veterans Name (Last, First, MI) 4. Date of Authorization

LXYF,ZLUQDY A FEB 15, 2005

-------------------------------------------------------------------------------

15\. DESCRIPTION OF ITEMS OR SERVICES AUTHORIZED

-------------------------------------------------------------------------------

ITEM NUMBER DESCRIPTION QUANTITY UNIT UNIT AMOUNT

ORDERED PRICE

-------------------------------------------------------------------------------

Eyeglasses, Prescription

<span id="_Toc24938072" class="anchor"></span>

Section 2

<span id="_Toc172537339" class="anchor"></span>NPPD Detail Display

<span id="_Toc24938073" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>This section covers the <strong>National Prosthetic Patient Database (NPPD) Detail Display</strong> feature.</p>
<p>Prosthetics users will be able to do the following with this patch:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Search for data and display data by a range of dates.</p>
</blockquote></li>
<li><blockquote>
<p>Sort and rearrange the view; display data in a custom view.</p>
</blockquote></li>
<li><blockquote>
<p>Print the display.</p>
</blockquote></li>
<li><blockquote>
<p>Convert the display into a Microsoft Excel file (for more complex sorting capabilities).</p>
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
<td>Data displayed</td>
<td><blockquote>
<p>The data that is displayed on this window includes the following:</p>
</blockquote>
<ul>
<li><p>Site</p></li>
<li><p>Date (Suspense entry date)</p></li>
<li><p>Type of transaction (I=Initial/New and X=Repair)</p></li>
<li><p>Form type (Stock Issue, Purchase Card, 2237, Other)</p></li>
<li><p>Patient name</p></li>
<li><p>Social Security Number</p></li>
<li><p>IEN</p></li>
<li><p>Brief description</p></li>
<li><p>HCPCS code and description</p></li>
<li><p>NPPD code</p></li>
<li><p>Initiator name</p></li>
<li><p>Suspense Initial Action date</p></li>
<li><p>Cost</p></li>
<li><p>Quantity</p></li>
<li><p>VA or Commercial</p></li>
<li><p>Vendor name</p></li>
<li><p>Grouper number (from AMIS)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc24938077" class="anchor"></span>Enter a Date Range

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date/Calendars</td>
<td><blockquote>
<p>After you have successfully signed on to VistA and the <strong>NPPD Detail Display</strong> window appears, you must select the date range that you want to view.</p>
<p>Enter a <strong>Beginning Date</strong> and an <strong>Ending Date</strong> by clicking on the drop-down list boxes next to the respective fields. A calendar displays as shown below.</p>
<p>You can also click the <strong>File</strong> menu and the <strong>Select</strong> <strong>Beginning Date</strong> or <strong>Select</strong> <strong>Ending Date</strong> option.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/069.png)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Ctrl&gt;</strong> key <strong>+ &lt;B&gt;</strong> key for the Beginning Date and the<br />
<strong>&lt;Ctrl&gt;</strong> key + <strong>&lt;E&gt;</strong> key for the Ending Date to display the respective calendars.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Calendar for date range selection</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/070.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued\]

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Selecting a date range</td>
<td><blockquote>
<p>The calendars display with the current date circled in red shown at the bottom of the calendar. You can accept the current date by clicking on it. You can also change the date by the following methods:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|             |                                                                                                                                                                                                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change the… | Description                                                                                                                                                                                     |
| Day     | Click on the actual day of the week in the calendar.                                                                                                                                            |
| Month   | Click on the month at the top of the calendar to display a list of all months and select one from there. You can decrease or increase one month at a time by clicking the left or right arrows. |
| Year    | Click on the year and an up and down arrow button displays for you to increase or decrease the year.                                                                                            |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Number of Day Restrictions</td>
<td><blockquote>
<p>You are restricted to a date range of less than 100 days. If you select a date range outside of this 100 day parameter, the following dialog message box displays:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date Range Message box</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/071.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Start Date before End Date</td>
<td><blockquote>
<p>If you accidentally entered an incorrect date range, you will receive a warning message. For instance, if you enter a start date that is after the end date, the message below will display. Click the <strong>OK</strong> button and reselect your date range.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Start/End Date Message</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/072.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24938078" class="anchor"></span>Display the Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display the data</td>
<td><blockquote>
<p>Once you have selected the date ranges, click the <strong><u>D</u>isplay</strong> button to reveal the data within that date range. (You can also click the <strong>File</strong> Menu and the <strong>Display</strong> option.)</p>
<p><strong>Shortcut:</strong> Press the <strong>&lt;Ctrl&gt;</strong> key + <strong>&lt;D&gt;</strong> key.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Changing the display of the data…</td>
<td><blockquote>
<p>You can manipulate the layout of the view in the <strong>NPPD Detail Display</strong> window for both viewing as well as printing purposes.</p>
<p><u>You can manipulate the view of the data as follows</u>:</p>
</blockquote>
<ul>
<li><p>To move a column, click and drag on a column header to another location.</p></li>
<li><p>To enlarge a column, click and drag a cell border.</p></li>
<li><p>To sort on any column, click on the header to sort it in <u>ascending order</u>.</p></li>
<li><p>If you click on the same column again, it will sort it in <u>descending order</u>.</p></li>
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
<td>NPPD Detail Display</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/073.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Patient confidentiality</td>
<td><blockquote>
<p>The <strong>Patient</strong> column and the <strong>SSN</strong> column have been shortened due to patient name and SSN confidentiality issues in documentation.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537343" class="anchor"></span>Select Custom Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Custom Data</td>
<td><blockquote>
<p>The <strong>Select custom data?</strong> drop-down lists allow you to select new columns to display. They also would convert into a Microsoft Excel file. These are optional prompts as you are not required to select any options. This is the main file for prosthetic purchasing transactions. This file is also the permanent record for the patient VAF 10-2319 of items issued to the veteran.</p>
<p>This list gives you the option to add information that was entered during the purchase order creation process to your NPPD Detail Report. For instance, if you added a Waiver or Excluded, you can view that data here.</p>
</blockquote>
<p><strong>Note:</strong> Custom data will display in the column to the right and you will have to scroll to the right to view it. If you do not see the new column, click the <strong>Display</strong> button.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Custom Data</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/074.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>MS Excel</td>
<td><blockquote>
<p>If you selected custom data and convert it to an MS Excel file (using the <strong>Excel</strong> button), you will view the custom data on the Excel spreadsheet as you scroll to the right.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Select Custom Data, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Data fields</td>
<td><blockquote>
<p>Below is a list of the Custom Data fields and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>

01 ENTRY DATE

This is the date that the transaction was entered into the system. It may or may not be the same as the request date.

02 PATIENT NAME

This is the name of the patient that this transaction is for. The name is a pointer to the PROSTHETIC PATIENT file which has the same internal entry number as the main patient database.

1 DATE ITEM ADDED TO PO AFTER CREATION

This field is the date the appliance issue or repair was requested by the patient. It may or may not be the same as the entry date or the delivery date. This depends on how quickly the transactions take place.

2 TYPE OF TRANSACTION

This set of codes will tell what kind of transaction this request is. The possibilities all fall under the VAF 10-7306a listings except for the repair.

4 ITEM

This field is a pointer to the master item list of possible appliances. The master list is set up so that appliances fall into groups which are the types of appliances.

4.1 HCPCS

Health Care Financing Administration Common Procedure Coding System (HCPCS).

This field should have the HCPCS code for the Item you are selecting. HCPCS is a uniform method for healthcare providers and medical suppliers to report professional services, procedures and supplies.

4.2 VENDOR TRACKING NUMBER

This field is the Vendor's internal unique tracking number. Some of the small vendors are not automated with VISA, and this tracking number is used to reference this transaction. This tracking number is based on the item, and can be as simple as the vendors item number, or elaborate as the vendors transaction number. This data will be used in the reconciliation process.

4.3 BANK AUTHORIZATION NUMBER

This six digit number is the authorization number VISA gives to the vendor for guaranteed payment. This number is used in the reconciliation process.

4.4 ICD9 CODE

Repository for CPRS diagnosis. From the message protocol in Consult Tracking. Standardized Prosthetics HCPCS.

4.6 STOCK ISSUE

This is a pointer to file \#661.2.

Continued on next page

Select Custom Data, Continued

4.7 CPT MODIFIER

CPT Modifiers in a comma delimited format, consistent with the HCFA published manuals.

4.8 DATE CPT MODIFIER EXTRACTED

This is the date the patient record extracted for billing. This date is also being used to trigger a mail message to billing if the PSAS HCPCS is edited and changed after the extraction has been ran.

4.9 HCPCS-ICD9 CODING FLAG

This field is used to determine the current code set versioning of a transaction.

4.91 CODING FLAG DATE

This is the date associated with field number 4.9. The date the coding flag was set.

5 QTY

This is the number of units that was issued or repaired for this transaction.

6 SHIP/DEL

This is the charge associated with shipping.

6.5 PICKUP/DEL

This field is a set of codes to identify pickup/delivery charges on VAF 10-2319.

7 VENDOR

The vendor is a pointer to IFCAP's VENDOR file and is the name of the company from which this appliance was or is to be purchased. The vendor may or may not be the same as the manufacturer. Therefore, manufacturers should also be listed in this file as vendors if you are going to be purchasing directly from the manufacturer.

8 STATION

The station is the Veterans Affairs site where this transaction is to come to completion. It is the station that is ultimately responsible for the issue and payment for the prosthetic device. This is the station reporting the workload.

8.1 SUSPENSE DATE

This is suspense date (.01 field).

8.11 SUSPENSE STATION

This refers to the consulting station.

8.12 PCE

This field is pointer to (Patient Encounter). When an entry is created in PCE a pointer is being set.

8.13 DATE SENT TO PCE

This is the date last sent or edited in PCE. If PCE is deleted this field should be deleted.

Continued on next page

Select Custom Data, Continued

8.14 SUSPENSE STATUS

This is the suspense status of the patient 2319 record. If the status is complete, a suspense link was established. If the status is incomplete, there is no suspense link to the patient 2319 record.

8.2 DATE RX WRITTEN

This is the date the prescription was written.

8.3 INITIAL ACTION DATE

This field is the date when an initial action was entered in suspense.

8.4 COMPLETION DATE

This is the date the suspense was completed.

8.5 TYPE OF REQUEST

This field could either be ROUTINE PROSTHETICS, EYEGLASS, CONTACT LENS, OXYGEN, MANUAL NONCPRS or CLOTHING ALLOWANCE.

8.6 SUSPENSE REQUESTOR

This is a pointer to file \#200, the person requesting the suspense as it appears in file \#668.

8.61 CONSULT REQUEST SERVICE 4

A service/section of a suspense requestor that initiated a consult for Prosthetics item. This free text entry is a service/section name of SERVICE/SECTION.

8.7 PROVISIONAL DIAGNOSIS

This is a free text diagnosis as it appears in suspense file.

8.8 SUSPENSE ICD9

This is the code at the time suspense was created.

8.9 CONSULT

This is a pointer to Consult file.

9 SERIAL NBR

This is the serial number of the issued or repaired appliance. If the serial number is longer than 20 characters, use the FIRST 20 characters.

9.1 PRODUCT DESCRIPTION

The manufacture product description to be used for recalls.

9.2 PRODUCT MODEL

The manufacture product model number to be used for recalls.

Continued on next page

Select Custom Data, Continued

10 DELIVERY DATE

This is the date that the appliance was delivered and accepted by the patient. This date, under certain circumstances, may be a date that the appliance was mailed to the patient. It may or may not be the same as the transaction date and/or the request date.

11 FORM REQUESTED ON

The FORM REQUESTED ON is based on current VA regulations. The system makes no checks to be sure that the form entered from the set of codes is within these regulations.

'1' FOR PSC

'2' FOR 2421

'3' FOR 2237

'4' FOR 2529-3

'5' FOR 2529-7

'6' FOR 2474

'7' FOR 2431

'8' FOR 2914

'9' FOR OTHER

'10' FOR 2520

'11' FOR STOCK ISSUE

'12' FOR INVENTORY ISSUE

'13' FOR HISTORICAL DATA

'14' FOR VISA

'15' FOR LAB ISSUE-3

12 SOURCE

This set of codes denotes which two possible sources were used for the acquisition of the appliance. The sources are grouped into either VA sources or commercial sources.

13 ACTION

The action taken on this transaction is noted here. The set of codes is self explanatory; however, the inactive action is used to indicate that the appliance is no longer being followed by VA.

QTY:

'1' FOR LOAN

'2' FOR CONDEMNED

'3' FOR RETURNED

'4' FOR INACTIVE

'5' FOR LOST

14 TOTAL COST

This field contains the total cost of the transaction.

Continued on next page

Select Custom Data, Continued

15 HISTORICAL DATA

If this field contains an asterisk (\*), then this transaction has been counted by the AMIS option, or is considered to be a historical transaction.

16 REMARKS

A free-text field used to indicate any additional information that is needed for this entry. For Purchasing Transactions this field will contain the remarks for the individual item, and the close-out remarks added together.

17 RETURNED STATUS

The status of the appliance upon return to the veteran. This notes what action was taken by the repair depot or station upon the completion of repairs.

'1' FOR RETURNED

'2' FOR CONDEMNED

'3' FOR CANCELLED

'4' FOR TURNED-IN

'5' FOR LOST

'6' FOR BROKEN

17.5 RETURN STATUS DATE

This is the date upon which the return status was determined and carried out if the item was returned to the veteran.

18 \*STATUS FLAG

The status of the patient is entered here so the service can determine if the patient is being followed, dropped, transferred, or canceled by this station.

21 LOT NUMBER

This field stores the lot number of the item being furnished to the patient. Enter the manufacturer's lot number, if known.

22 \*PRODUCT LINE

Set of codes that contain information for Hearing Aid transactions.

'1' FOR HEARING AIDS

'2' FOR BATTERIES

'3' FOR OTHER

23 TRANSACTION

This is the IFCAP transaction number from VAF 4-1358 or VAF 2237. A temporary Transaction number for a VAF 10-2529-3 may also be entered.

24 DESCRIPTION

This is a detailed description of the item/service supplied.

Continued on next page

Select Custom Data, Continued

25 DELIVER TO

Delivery location that will print on VAF 10-2421 to show the vendor where the item will be delivered.

27 INITIATOR

This is the person who created the transaction.

28 EXTENDED DESCRIPTION

This is the extended information from purchasing and also from posting of VAF 2237s.

29 INVENTORY POINT

This is the inventory point for this transaction and is a pointer to the GENERIC INVENTORY.

31 BILL DATE

This is the DATE/TIME the bill is created.

32 BILL STATUS

This is the status of a bill in relation to Integrated Billing.

'1' FOR ENTERED/NOT REVIEWED

'2 ' FOR REVIEWED

'3' FOR AUTHORIZED

'4' FOR PRINTED

'5' FOR TRANSMITTED

'7' FOR CANCELLED

'0' FOR CLOSED

33 BILL IEN

This is the bill IEN in file \#399.

35 USER WHO EDIT

User who edited the 2319 record using option ED2. This field will only be populated when the Total Cost field has been changed.

36 DATE EDITED

This is the date the Total Cost field has been changed using option ED2.

37 HCPCS/ITEM

This is the PIP HCPCS unique item.

38 HCPCS/ITEM DESCRIPTION

This is the description of an Item or Appliance kept by local site.

This field is updated during the STOCK ISSUE options.

Continued on next page

Select Custom Data, Continued

38.1 EXCLUDE/WAIVER

This field determines if the item is EXCLUDED or Waiver off of a National Contract.

'E' FOR EXCLUDED

'W' FOR WAIVER

38.7 CONTRACT \#

This field stores the Contract Number.

40 REQUESTING STATION

This is the station requesting services or appliances.

45 TOTAL LABOR HOURS

This is the number of hours spent on the job. This field is only populated via routines.

46 TOTAL LABOR COST

The total cost of the labor to perform this job.

47 TOTAL MATERIAL COST

The total cost of all the materials to perform the job.

48 TOTAL LAB COST

The Prosthetic Laboratory Total Cost calculated by AMIS.

50 COMPLETION DATE

The date the job was completed.

51 LAB REMARKS

A free-text field used to indicate any additional Laboratory information that is needed for this entry. Since the field is only 40 characters in length, use meaningful abbreviations where possible.

52 AMIS NEW CODE

This field is set when AMIS is generated. It is the New Worksheet AMIS code.

60 AMIS DATE

The date AMIS was run and the item was picked up and counted.

62 PATIENT CATEGORY

This is the Prosthetic Patient Category used for counting AMIS.

'1' FOR SC/OP

'2' FOR SC

'3' FOR NSC

'4' FOR NSC/OP

Continued on next page

Select Custom Data, Continued

63 SPECIAL CATEGORY

If the patient is NSC/OP, then this field must also be set. SPECIAL CATEGORY is also used in counting AMIS.

'1' FOR SPECIAL LEGISLATION

'2' FOR A&A

'3' FOR PHC

'4' FOR ELIGIBILITY REFORM

64 ADMIN REPAIR AMIS CODE AM

This field will be set when AMIS is generated for the Repair Worksheets.

68 AMIS GROUPER

This is used in AMIS calculations. This field should never be changed through FileMan!

69 SOURCE OF PROCUREMENT LB

The source from which the Purchasing Agent is ordering the needed equipment. The sources one may choose from are limited.

'O' FOR ORTHOTIC LAB

'R' FOR RESTORATION LAB

'S' FOR SHOE LAST CLINIC

'W' FOR WHEELCHAIR REPAIR SHOP

'N' FOR NATIONAL FOOT CENTER

'D' FOR DENVER DISTRIBUTION CENTER

70 RECEIVING STATION

This field contains the institution that will receive the VAF 10-2529-3 request for processing.

71 WORK ORDER NUMBER

Work Order Number (STA-FY-QTR-TYPE OF LAB-NUMBER) for items processed in the Prosthetic Laboratory.

72 2529-3

VAF 10-2529-3 information will be displayed if the VAF 10-2319 item is associated with a Denver Distribution Center, National Foot Center, or Prosthetics Lab request.

73 LAB AMIS DATE

Last date the Lab AMIS was run.

74 ORTHOTICS LAB CODE

Contains the Orthotic Lab New Code.

75 ORTHOTICS LAB REPAIR CODE LBA

Contains the Orthotic Lab Repair Code.

Continued on next page

Select Custom Data, Continued

76 RESTORATION LAB CODE LBA

Contains the Restoration Lab New Code.

77 RESTORATIONS LAB REPAIR CODE LBA

Contains the Restoration Lab Repair Code.

78 UNIT OF ISSUE

This is the unit by which items/services are issued (e.g., each, pair, box, case, etc.).

79 AMIS FLAG

Contains the status if the Item will not count on the Administrative AMIS.

80 WORK FOR OTHER STATION LB

Contains the Status if the Job Performed will display as work performed for another station.

'1' FOR YES

81 NO ADMIN COUNT

This field will be set if the Item will not count on the Administrative AMIS or the Orthotic Laboratory AMIS.

'1' FOR NO COUNT

82 NO LAB COUNT

Field will be set if there is no AMIS Count for AMIS.

'1' FOR NO COUNT

83 BACKLOG DATE

This field will contain the date that the entry was created. This entry will be a backlog entry until it has been completed. All backlog data must show up on the Laboratory or Restoration AMIS Count.

89 HISTORICAL ITEM

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

90 HISTORICAL STATION

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

91 HISTORICAL VENDOR

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

92 HISTORICAL VENDOR PHONE HSTV

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

Continued on next page

Select Custom Data, Continued

93 HISTORICAL STREET ADD

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

94 HISTORICAL CITY

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

95 HISTORICAL STATE

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

96 HISTORICAL ZIP

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

97 HISTORICAL RECORD

This field is used for the consolidation sites, will contain the data that has been merged from a legacy system. This field is populated by the RMPRJ routine that is not exported.

<span id="_Toc172537344" class="anchor"></span>Print the NPPD Detail

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print the data</td>
<td><blockquote>
<p>You can print the <strong>NPPD Detail Display</strong> data. Click the <strong><u>P</u>rint</strong> button to send this data to your local printer, and click <strong>OK</strong> on the <strong>Print</strong> dialog box. (You can also click the <strong>File</strong> Menu and the <strong>Print</strong> option.)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Ctrl&gt;</strong> key + <strong>&lt;P&gt;</strong> key.</p>
<p>The layout of the print will be the same as the display.</p>
<p><strong>Note:</strong> You can select a printer to print the NPPD detail.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Change to Landscape</td>
<td><blockquote>
<p><strong><u>Recommendation</u>:</strong> You should change the format of the printout from <em>Portrait</em> to <em>Landscape</em> to print all the columns on the same page.</p>
</blockquote></td>
</tr>
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
<p>To change the print format, follow these steps:</p>
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
<td>Click the <strong><u>P</u>rint</strong> button on the <strong>NPPD Detail Display</strong> window.</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>Click the <strong><u>P</u>roperties</strong> button (to the right of the <strong>Name</strong> field) on the <strong>Print</strong> dialog box.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;P&gt;</strong> key.</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>Continue to the next page.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print dialog box</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/075.png)</p>
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
<td>Layout Tab</td>
<td><blockquote>
<p>You can change the format of the printout from the standard <em>Portrait</em> format to <em>Landscape</em> on the <strong>Layout</strong> tab.</p>
</blockquote></td>
</tr>
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
<p>To continue to change to the Landscape format, follow these steps:</p>
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
<td>4</td>
<td>Click the <strong>Layout</strong> tab on the <strong>Properties</strong> dialog box (usually shown as a default view).</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Click the <strong><u>L</u>andscape</strong> radio button to change the format.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;L&gt;</strong> key.</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>Click <strong>OK</strong> or press <strong>&lt;Enter.&gt;</strong></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Landscape Radio button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/076.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Last step</td>
<td><blockquote>
<p>When you return to the <strong>Print</strong> dialog box, click <strong>OK</strong> again, and it will print your output. You can print multiple copies if necessary.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537345" class="anchor"></span>Save as an Excel File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Excel Button</td>
<td><blockquote>
<p>Click the <strong><u>E</u>xcel</strong> button on the <strong>NPPD Detail Display</strong> window to launch Excel and display the current data. (You can also click the <strong>File</strong> menu and select the <strong>Excel</strong> option.)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key to launch MS Excel.</p>
<p><strong>Note:</strong> This feature creates a temporary Excel .CSV file in the folder selected. The default folder is C:\NPPDDownload (which is automatically created). The file name is based on the date range.</p>
<p><strong><u>Example</u>:</strong> Jul 02, 2006_Aug 10, 2006.csv</p>
</blockquote>
<p>Prior to the display, you are notified that the information about to be exported may contain Patient Identifiable Information.</p></td>
</tr>
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
<p>To export data to Excel:</p>
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
<td><p>Click the <strong><u>E</u>xcel</strong> button on the <strong>NPPD Detail Display</strong> window.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Click the <strong><u>O</u>K</strong> button on the security reminder.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Continue to the <strong>Select Directory</strong> window.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Security Reminder</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/077.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                              |
| 4    | Navigate to the desired directory and select <u>O</u>K .(Click Cancel to exit or <u>H</u>elp to view the help pages associated with this functionality) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Directory</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/078.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                   |
| 5    | Navigate to a secure location where the temporary Excel (.csv) file will be stored and then select <u>O</u>K . Excel will open and display the data. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>MS Excel data</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/079.png)</p>
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
<td>6</td>
<td><p>This is only a temporary file so if you wish to save the data you must select <strong><u>F</u>ile,</strong> then <strong>Save <u>A</u>s,</strong> then change the name of the file.</p>
<p><strong>Note:</strong> To save the file, you <strong>must</strong> change the filename from the default. If you accept the default file name, it will be deleted when you close the NPPD window.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Temp file location</td>
<td><blockquote>
<p>Should you wish to check the location of the temp file, it displays on the NPPD Detail Display window right above the Excel button.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/080.png)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>You will be unable to export another report to Excel or navigate away from the NPPD Detail Display window until the current Excel (.csv) file is closed. Attempting to do so without first closing the file will result in one of the following errors depending on what action has taken place. If you do save a file with Patient Identifiable Info in it, don’t forget to delete it when you no longer need it.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attempting to Open another report with temp file still open</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/081.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attempting to navigate away from the NPPD Detail Display window with temp file still open</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/082.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537346" class="anchor"></span>Exiting the NPPD Detail Display Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit the Window</td>
<td><blockquote>
<p>You can exit the application by first clicking the <strong>Menu</strong> button on the <strong>NPPD Detail Display</strong> window. This closes the NPPD Detail Display window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NPPD Detail Display “Menu” button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/083.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit the Application</td>
<td><blockquote>
<p>Then click the <strong>Close</strong> button on the <strong>Prosthetics</strong> <strong>Main Menu</strong> window:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|     |     |
|-----|-----|
|     |     |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Main Menu “Close” button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/084.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Confirmation window</td>
<td><blockquote>
<p>Click OK on the confirmation window to close the Prosthetics VistA Suite.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/085.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cancel button</td>
<td><blockquote>
<p>If you click the <strong>Cancel</strong> button, you will remain in the application and can continue to work.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537347" class="anchor"></span>Section 3

<span id="_Toc172537348" class="anchor"></span>Automated Delayed Order Report (DOR)

<span id="_Toc44299367" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>Delayed Order Report (DOR)</strong> <strong>User Manual</strong> corresponds to Patch RMPR*3*59. This patch provides Prosthetics GUI (graphical user interface) windows for the <strong>Delayed Order Report</strong> <strong>(DOR)</strong> feature.</p>
<p><strong>Note:</strong> <em><strong>Using this feature requires basic MS Windows skills.</strong></em></p>
<p>Prosthetics users can do the following with this patch:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Search for and display manual suspense entries/electronic consult (CPRS order) data by one or all sites</p>
</blockquote></li>
<li><blockquote>
<p>Display data using one or multiple statuses (Open, Pending, Cancelled or Closed)</p>
</blockquote></li>
<li><blockquote>
<p>Use a starting date for Closed and Cancelled records to display data</p>
</blockquote></li>
<li><blockquote>
<p>Sort and rearrange the view; display data in a custom view</p>
</blockquote></li>
<li><blockquote>
<p>Print the display</p>
</blockquote></li>
<li><blockquote>
<p>Convert the display into a Microsoft Excel file (for more sorting capabilities)</p>
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
<td>Working Days</td>
<td><blockquote>
<p>A delayed order is counted in Working days not Calendar days<strong>. This does NOT include Saturdays and Sundays or Holidays!!!</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Record Status</td>
<td><p>The <em><strong>Status</strong></em> column shows the following status types:</p>
<ol type="1">
<li><p>Open</p></li>
<li><p>Pending</p></li>
<li><p>Closed</p></li>
<li><p>Cancelled</p></li>
</ol></td>
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
<td>Status cycle</td>
<td><blockquote>
<p>The <em><strong>Initial Action Date</strong></em> displays the date of the first action taken on the suspense entry/electronic consult (CPRS order) record. This changes the status from OPEN to PENDING. An order remains in PENDING status until it is fulfilled and then changes to a CLOSED status.</p>
<p><strong>Note:</strong> The status can change from OPEN to CLOSED if the order has been fulfilled upon the initial action.</p>
<p>Keep in mind that when creating the first action note, the status changes from OPEN to PENDING and when creating the second or additional action note(s), the status remains PENDING. Only when a record is completed does the status change to CLOSED.</p>
<p>When a complete note is posted, all action has taken place for a requested Prosthetic item or service. When you post the complete note, the status on the record changes from PENDING (if action has previously taken place on the request) or OPEN to a CLOSED status.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Work Days, not Calendar Days</td>
<td><blockquote>
<p>The <strong>Delayed Order Report</strong> displays the number of “Work“ days (<strong>not</strong> Calendar days) from the original date the order was entered as an electronic consult or a suspense entry to the day it is completed. A “Work” day is defined as Monday through Friday.</p>
<p><strong>Note:</strong> The calculation subtracts Saturdays and Sundays and Holidays from the number of days the order was entered, even if a CPRS order was written over a weekend. <strong><u>Holidays are NOT counted</u>.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299368" class="anchor"></span>Display the DOR Data

<span id="_Toc44299369" class="anchor"></span>Introduction

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>General steps to view DOR Data</td>
<td><blockquote>
<p>To utilize the <strong>Delayed Order Report (DOR)</strong> data, here is a general set of steps to display DOR data as follows:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Select ALL sites by checking the “<em><strong>Or…All Sites</strong></em>” checkbox (or you can select a specific site from the drop down list).</p>
</blockquote></li>
<li><blockquote>
<p>Enter a Starting Date (defaults to the current date).</p>
</blockquote></li>
<li><blockquote>
<p>Select a Status if you want to change the default statuses. The default statuses are set to <strong>Open</strong>, <strong>Pending</strong>, and <strong>Closed</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Enter the SSN range of the patient display (mandatory).</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Display</strong> button.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>The <em><strong>Description</strong></em> is a free-text field that is manually entered with approximately 15 characters in length. If you can’t view the entire description, you can expand the column by clicking and dragging the borderline to a wider position.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Data displayed</td>
<td><blockquote>
<p>The data that is displayed with this GUI feature includes the following:</p>
<p><u>Grid Columns</u>:</p>
</blockquote>
<ul>
<li><p>Site</p></li>
<li><p>Delayed column (Yes or No)</p></li>
<li><p>Status of the order</p></li>
<li><p>Type of Order – Manual Suspense or Routine (electronic orders via CPRS including Eyeglass, Contact Lens and Home Oxygen orders)</p></li>
<li><p>Station number</p></li>
<li><p>Create Date (Suspense entry date)</p></li>
<li><p>First Action Date – Date that the order was put into PENDING status</p></li>
<li><p>Number of Days that the order has been delayed including columns for: 0-5, 6-9, 10-29, 30-90, and 90+ columns</p></li>
<li><p>Link information – linked message(s) to the order record</p></li>
<li><p>Brief description</p></li>
<li><p>Patient name</p></li>
<li><p>Social Security Number</p></li>
</ul>
<blockquote>
<p><u>Fields</u>:</p>
<p>Selection Result Totals (near bottom of window) include:</p>
</blockquote>
<ul>
<li><p>Total records found</p></li>
<li><p>Total delayed records by calculation</p></li>
<li><p>Percent delayed records by calculation</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc44299370" class="anchor"></span>Select a Site(s)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Site</td>
<td><blockquote>
<p>The first thing you must do to view the DOR is to select a site for the records that you want to display. If you are a multi-site facility, you will be able to select the specific site you want to view via the drop down box. <strong><u>Recommendation</u>:</strong> It is highly recommended that you select the “<em><strong>Or…All Sites</strong></em>” checkbox.</p>
</blockquote></td>
</tr>
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
<p>To begin the process to display the DOR data, follow this first step:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                          |
|------|--------------------------------------------------------------------------|
| Step | Action                                                                   |
| 1    | Click the “*Or…All Sites*” checkbox to view ALL sites and CBOC data. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>DOR window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/086.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select “ALL Sites”</td>
<td><blockquote>
<p>If you want to view all available suspense entries/electronic consult orders including Community Based Outpatient Clinics (CBOC) data, click the <strong>All Sites</strong> checkbox instead of selecting your specific site from the <strong>Site</strong> drop-down list box. This ensures that the display will include all sites. For example, the Kenosha, Wisconsin CBOC will not display when the Milwaukee site is selected only. These records display when the <strong>All Sites</strong> checkbox is selected.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299371" class="anchor"></span>Select a Starting Date

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date/Calendar</td>
<td><blockquote>
<p>Note the <em><strong>Starting Date</strong></em> defaults to the current date. You can change this date. Enter a <em><strong>Starting Date</strong></em> by clicking on the drop-down list box. A calendar displays with the current date circled in red and shown at the bottom of the calendar. You can accept the current date by clicking on it.</p>
</blockquote></td>
</tr>
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
<p>To continue to display the DOR data, follow this step:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                       |
|------|-------------------------------------------------------|
| Step | Action                                                |
| 2    | Enter a Starting Date (defaults to the current date). |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td><blockquote>
<p>You can change the date by the following methods:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|             |                                                                                                                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change the… | Description                                                                                                                                                                             |
| Day     | Click on the actual day of the week in the calendar.                                                                                                                                    |
| Month   | Click on the month at the top of the calendar to display a list of all months and select one. Or you can decrease or increase one month at a time by clicking the left or right arrows. |
| Year    | Click on the year and an up and down arrow button displays for you to increase or decrease the year.                                                                                    |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Starting date calendar</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/087.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299372" class="anchor"></span>Select a Status

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Status</td>
<td><blockquote>
<p>You can view <strong>Open</strong>, <strong>Pending</strong>, <strong>Closed</strong> or <strong>Canceled</strong> records by clicking the checkbox for one or all of these options. The default statuses that are already checked are: <strong>Open</strong>, <strong>Pending</strong> and <strong>Closed</strong>. You can click in these boxes to uncheck any status.</p>
</blockquote></td>
</tr>
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
<p>To continue to display the DOR data, follow this step:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                             |
|------|-------------------------------------------------------------|
| Step | Action                                                      |
| 3    | Select a Status if you want to change the default statuses. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Status Scenarios</td>
<td><blockquote>
<p>There are a number of combinations that you can choose including the following status scenarios:</p>
<p><strong><u>Scenario 1</u>:</strong> If you select the <strong>Open</strong> and <strong>Pending</strong> statuses, you will view all suspense records/electronic consult records (CPRS orders) available with a status of <strong>Open</strong> and <strong>Pending</strong>.</p>
<p><strong><u>Scenario 2</u>:</strong> The <em><strong>Starting Date</strong></em> field works with the <strong>Closed</strong> and <strong>Canceled</strong> statuses. If you check either one of these statuses, you can then select the <em><strong>Starting Date</strong></em> to display these records. (The <em><strong>Starting Date</strong></em> field that you select plus <strong>Closed</strong> Delayed records for that period does NOT affect the <strong>Open</strong> and <strong>Pending</strong> status record display.)</p>
<p><strong><u>Scenario 3</u>:</strong> If you select all four statuses, you will view ALL <strong>Open</strong> and <strong>Pending</strong> records. You will also view the <strong>Closed</strong> and <strong>Canceled</strong> records beginning with the <em><strong>Starting Date</strong></em> you select ONLY.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299373" class="anchor"></span>Select the SSN Range

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SSN fields</td>
<td><blockquote>
<p>You must have an SSN range to view DOR data. There is a <strong>Starting SSN</strong> and an <strong>Ending SSN</strong> field box. This is a range of patient Social Security Numbers by the last two digits. When you enter a range, it will display electronic consults or manual suspense entries within that range.</p>
<p>If your workload is categorized by the SSN for a specific Purchasing Agent, then you can display entries that are assigned by one Purchasing Agent at a time.</p>
<p><strong>Note:</strong> Enter a range of 00 to 99 to view all Purchasing Agents’ SSNs for all patients.</p>
</blockquote></td>
</tr>
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
<p>To continue to display the DOR data, follow this step:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                         |
|------|---------------------------------------------------------|
| Step | Action                                                  |
| 4    | Enter the SSN range of the patient display (mandatory). |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SSN range</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/088.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299374" class="anchor"></span>Display the Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Data display</td>
<td><blockquote>
<p>The data displayed are manual suspense and all other consult entries. You’ll notice columns with a breakdown of days of 0-5, 6-9, 10-29, 30-89 and 90+ columns.</p>
<p><u>These columns display the total number of days old by category within the breakdown of the columns. It does NOT display the total number of instances of records (manual suspense entries or electronic consults via CPRS orders)</u>.</p>
</blockquote></td>
</tr>
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
<p>To continue to display the DOR data, follow this step:</p>
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
<td><p>Once you have the desired criteria, click the <strong>Display</strong> button. (You can also double click a record to view the <strong>Request</strong> window.)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;D&gt;</strong> key.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sizing and Sorting columns</td>
<td><blockquote>
<p>Columns are sizable on this window, but not movable. To resize a column, you can place the cursor on the column header borderline until you can view the double-headed arrow. Then click and drag the column until it is the size you want.</p>
<p>To sort the columns, click the column header and the data will redisplay in ascending or descending order. <strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Delayed Order Report window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/089.png)</p>
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
<td>Menu, Refresh and Clear buttons</td>
<td><blockquote>
<p>The <strong>Menu</strong> button returns you to the <strong>Prosthetics Main Menu</strong> window where you can open additional applications at the same time. The <strong>Refresh</strong> button resets (recalls) the data if you had made some column sizing changes. It is the same as clicking the <strong>Display</strong> button again. You can use the <strong>Clear</strong> button to blank out the window and start over with new display criteria.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column titles</td>
<td><blockquote>
<p>Below are the header titles of each column and a description of each.</p>
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
<td>Column</td>
<td>Description</td>
</tr>
<tr class="even">
<td><strong>Dlyd</strong></td>
<td>The <strong>Delayed</strong> column will display either a Yes or No as to whether the record is delayed or not. You can sort on this column by all “Yes” records or all “No” records by clicking on the column.</td>
</tr>
<tr class="odd">
<td><strong>Status</strong></td>
<td>The <strong>Status</strong> of the record is either Open, Pending, Closed or Cancelled. Records with an Open status are shown in blue.</td>
</tr>
<tr class="even">
<td><strong>Type</strong></td>
<td>This is the <strong>Type</strong> of record - Manual Suspense entry or Routine Consult (electronic orders via CPRS including Eyeglass, Contact Lens and Home Oxygen orders).</td>
</tr>
<tr class="odd">
<td><strong>Station</strong></td>
<td>This is the <strong>Station Identifying number</strong>.</td>
</tr>
<tr class="even">
<td><strong>Create</strong></td>
<td>The <strong>Create date</strong> is the date that the record was created.</td>
</tr>
<tr class="odd">
<td><strong>1<sup>st</sup> Action</strong></td>
<td>The <strong>First Action date</strong> is the date that initial action was taken on the request and the status changed from Open to Pending.</td>
</tr>
<tr class="even">
<td><strong>0-5</strong></td>
<td>The number of days (0-5) that an order record is <strong>not</strong> delayed.</td>
</tr>
<tr class="odd">
<td><strong>6-9; 10-29; 30-89; 90+</strong></td>
<td><p>These columns of number ranges designate the number of Workdays within these ranges that a request has been delayed. <strong>This does NOT include Saturdays and Sundays nor Holidays.</strong> This also designates that the record is in a Pending status. Any record over 5 days is highlighted in red with yellow numbers.</p>
<p><strong>Note:</strong> The numbers listed in each row for a record designate the <u>number of days NOT the number of record instances</u>.</p></td>
</tr>
<tr class="even">
<td><strong>Lnk</strong></td>
<td><p>The <strong>Link</strong> column designates how many items that were linked to that record. It could be a zero or a number.</p>
<p>Note that if the status is <strong>Closed</strong>, and there is a zero in the Link column, then those records were never linked.</p></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td>This is the <strong>description</strong> of the request.</td>
</tr>
<tr class="even">
<td><strong>Patient</strong></td>
<td>The <strong>patient name</strong> is displayed.</td>
</tr>
<tr class="odd">
<td><strong>SSN</strong></td>
<td>The <strong>Social Security Number</strong> for the patient is displayed.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Yellow and Red fields</td>
<td><blockquote>
<p>Records that have a delayed date beyond 5 days will have the number of days in yellow and the block will be highlighted in red.</p>
<p>Records with 0-5 days will have the number shown in bold print.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299375" class="anchor"></span>View DOR Calculation Detail

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>DOR Detail button</td>
<td><blockquote>
<p>You can view the DOR calculation detail for the range of consults and manual suspense entries that you displayed. When you select the <strong>DOR Detail</strong> button, it doesn’t matter what status is checked because the calculation looks at all the <strong>Open</strong>, <strong>Pending</strong> and <strong>Closed</strong> records from the starting date you selected.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Number of MANUALS</td>
<td><blockquote>
<p>You can view the total number of <em>Manual</em> suspense entries that are in <strong>Open</strong>, <strong>Pending</strong> or <strong>Closed</strong> status. Those in the 6-9 or higher columns show the ones that are Delayed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Number of CONSULTS</td>
<td><blockquote>
<p>You can view the total number of electronic Consults (that were not entered manually) that are in <strong>Open,</strong> <strong>Pending</strong> or <strong>Closed</strong> status and have not had any action taken on them. Those in the 6-9 or higher columns show the ones that are Delayed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SUB TOTAL</td>
<td><blockquote>
<p>The <strong>SUB TOTAL</strong> row totals the number of <em>Manual</em> suspense entries + the total number of all other consults.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>DOR Calculation Detail window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/090.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Minus PENDING</td>
<td><blockquote>
<p>This row displays the number of consults that have had an initial action taken on it (starting with the date you selected in the calendar for the starting date which is shown here by 1/1/2003) and put into a <strong>Pending</strong> status.</p>
<p>This number is subtracted from the subtotal for the <strong>Total Delayed</strong> row below that.</p>
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
<td>TOTAL DELAYED</td>
<td><blockquote>
<p>The <strong>TOTAL DELAYED</strong> is calculation that adds the total number of <em>Manual</em> Suspense records + the total number of all other consults and subtracts the number of consults in a <strong>Pending</strong> status (Pending from before the Start Date selected).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>DOR Calculation Detail window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/091.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Total of Sub Total</td>
<td><blockquote>
<p>The <strong>Total of the Sub Total</strong> field includes: 1) the total from the <strong>Sub Total</strong> above (third row), 2) all totals of <em>Manual</em> Suspense entries and 3) all other electronic consults.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Minus Total Pending</td>
<td><blockquote>
<p>The next row shows the calculation for the Total consults minus the <strong>Pending</strong> consults from the starting date that you selected.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>TOTAL DELAYED</td>
<td><p>The <strong>TOTAL DELAYED</strong> field is shown.</p>
<p>This displays the Total Delayed from the grid above (any greater than 5 days delayed) divided by (the result of the total Sub Total minus Total Pending as of 1/1/03) and multiplied by 100. This is the percentage delayed.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Percent Delayed</td>
<td><blockquote>
<p>The final calculations above, this equals the <strong>Percent Delayed</strong> (shown as 95.37%).</p>
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
<td>Scenarios below</td>
<td><blockquote>
<p>The scenarios below describe different timelines when orders are received at different times of the month and if they are delayed. Then it will explain which month’s Calculation Report where the data will appear.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Scenario 1</td>
<td><blockquote>
<p>An order is received on Tuesday, June 3rd and is changed to <strong>Pending</strong> or <strong>Closed</strong> status on Friday, 6/6. This is <u>not</u> a delayed order and would appear in the June Calculation Report as an order received.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Scenario 2</td>
<td><blockquote>
<p>An order is received on Tuesday, 6/3 and is changed to <strong>Pending</strong> or <strong>Closed</strong> on Wednesday, 6/20. This is a delayed order and would be included in the June Calculation Report as a delayed order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Scenario 3</td>
<td><blockquote>
<p>An order is received on Thursday, 6/26 and is changed to <strong>Pending</strong> or <strong>Closed</strong> on Tuesday, 7/15. This was <u>not</u> a delayed order in June; however the order is included in the June Calculation Report, because it was received in June. Since it took greater than 5 days to change it to <strong>Pending</strong> or <strong>Closed</strong>, it would also be included in the July report as a delayed order and would be included in the calculations.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Scenario 4</td>
<td><blockquote>
<p>An order is received on Thursday, 6/26 and changed to <strong>Pending</strong> or <strong>Closed</strong> on Monday, August 4<sup>th</sup>. This is <u>not</u> a delayed order in June; however, the order is included in the June Calculation Report, because it was received in June. Since it took greater than 5 days to change it to <strong>Pending</strong> or <strong>Closed</strong>, it would be included in both the July and August report as a delayed order and would also be included in the calculations.</p>
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
<td>Print button</td>
<td><blockquote>
<p>You can print the <strong>DOR Calculation Detail</strong> data by clicking the <strong>Print</strong> button. A <strong>Print Preview</strong> pane will display that allows you to zoom in, scroll forward/ backward, print, save the data, or open/load a new report.</p>
<p>Click the <strong>Close</strong> button to return to the <strong>DOR Calculation Detail</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print Preview</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/092.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299376" class="anchor"></span>View Pending Calculations

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Pending Calc Button</td>
<td><blockquote>
<p>Click on the <strong>Pending Calc</strong> button on the <strong>DOR</strong> window and the window displays based on the selection criteria of this window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Pending status consults</td>
<td><blockquote>
<p>The <strong>Pending Calculations</strong> window displays the total number of Workdays with the total number of <strong>Pending</strong> records since an initial action was taken on it. These records are categorized into columns by the number of Workdays it has remained in a <strong>Pending</strong> status.</p>
<p>The calculation used to display these <strong>Pending</strong> status records is from the <u>First Action date</u> (not from Creation Date) to the <u>current date</u>. This is a tool to help managers monitor their consults and manual suspense entries that have been <strong>Pending</strong> for an extended period of time.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Pending Calculations</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/093.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print button</td>
<td><blockquote>
<p>The <strong>Print</strong> button allows you to print the Pending Action Calculations and will display the <strong>Print</strong> dialog box.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Excel button</td>
<td><blockquote>
<p>You can send this data to MS Excel by clicking the <strong>Excel</strong> button. It will launch the application and display the data at the same time. (You can also click the <strong>File</strong> menu, click <strong>Excel,</strong> then select the <strong>Send - Request Grid</strong> option.)</p>
<p>For more information on saving data as an Excel file, see “Save as an Excel File,” later in this chapter.</p>
</blockquote></td>
</tr>
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
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/094.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24185572" class="anchor"></span>

View 2319 Information

<span id="_Toc24185573" class="anchor"></span>View 2319 – Patient Demographics

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>The <strong>View 2319</strong> button displays the 10-2319 Prosthetic patient records. The title bar displays the patient name and SSN. Here are the windows of information that you can view from the patient’s 2319:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Patient Demographics</p>
</blockquote></li>
<li><blockquote>
<p>Clinic Enrollments/Correspondence</p>
</blockquote></li>
<li><blockquote>
<p>Entitlement Info</p>
</blockquote></li>
<li><blockquote>
<p>Appliance Transactions</p>
</blockquote></li>
<li><blockquote>
<p>Auto Adaptive Info</p>
</blockquote></li>
<li><blockquote>
<p>Critical Comments</p>
</blockquote></li>
<li><blockquote>
<p>HISA Information</p>
</blockquote></li>
<li><blockquote>
<p>Home Oxygen Items</p>
</blockquote></li>
</ol>
<blockquote>
<p><strong>Note:</strong> Use the <strong>&lt;Alt&gt;</strong> key and the number to toggle to different tabs.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Demographics data</td>
<td><blockquote>
<p>You can view the patient demographics for the veteran. This includes: Name (in red if deceased with Date of Death listed above the Date of Birth and the age field will not display), address, next of kin, emergency contact information, veteran benefits and eligibility (former Prisoner of War (highlighted in blue if “Yes”), Aid &amp; Attendance, service connected, non-service connected, etc.).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><u>1</u>. Patient Demographics window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/095.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24185574" class="anchor"></span>View 2319 - Clinic Enrollments/Correspondence

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Window description</td>
<td><blockquote>
<p>This second tab details clinic enrollments and correspondence for the veteran. This includes the following: the last movement actions (i.e., hospital admissions and discharges), clinic enrollments, pending appointments and correspondence letters.</p>
<p><strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><u>2</u>. Clinic Enrollments/ Correspondence</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/096.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/097.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24185575" class="anchor"></span>View 2319 - Entitlement Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Window description</td>
<td><blockquote>
<p>The third tab details entitlement and loan information for the veteran. This includes the following: PSC Issue Card, clothing allowance, items on loan, and items returned.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><u>3</u>. Entitlement Info</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/098.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/099.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24185576" class="anchor"></span>View 2319 – Appliance Transactions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance Transactions</td>
<td><blockquote>
<p>The <strong>Appliance Transactions</strong> tab of the <strong>View 2319</strong> window displays all transaction history for a veteran. The <em><strong>Date</strong></em> column is the date of the PO. Columns are re-sizable on this window (not movable). The total records found displays at the bottom.</p>
<p><strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
</blockquote></td>
</tr>
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
<p>To view the Appliance Transactions detail, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                        |
|------|----------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                 |
| 1    | Select a transaction by clicking on it to highlight it.                                                                                |
| 2    | Click the ViewDetail button below to display the appliance details. (You can also double click a record to view the details.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><u>4</u>. Appliance Transactions</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/100.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/101.png) button in the top right-hand corner.</p>
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
<td>Steps</td>
<td><blockquote>
<p>To continue to view the Appliance Transactions detail, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                           |
|------|---------------------------------------------------------------------------|
| Step | Action                                                                    |
| 3    | The Transaction Detail window is shown below.                         |
| 4    | Click the Close button to return to the Appliance Transaction window. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Appliance Transaction Detail</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/102.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/103.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24185577" class="anchor"></span>View 2319 – Auto Adaptive Info

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Window description</td>
<td><blockquote>
<p>The fifth tab details the Auto Adaptive information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><u>5</u>. Auto Adaptive Info</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/104.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/105.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24185578" class="anchor"></span>View 2319 - Critical Comments

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Window description</td>
<td><blockquote>
<p>The sixth tab details any critical comments recorded for the veteran.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><u>6</u>. Critical Comments</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/106.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/107.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24185579" class="anchor"></span>View 2319 – View HISA Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Window description</td>
<td><blockquote>
<p>The seventh tab details the HISA (Home Improvement Structural Alteration) information including the date, quantity, item, type, vendor, station number, serial, HCPCS Code and cost of the item ordered.</p>
<p><strong>Note:</strong> “<em>HISA Information</em>” is the new name for this window; it used to be “<em>Add/Edit Disability Codes</em>.”</p>
<p><strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                               |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                        |
| 1    | Select a transaction by clicking on it to highlight it.                                                                                       |
| 2    | Click the ViewDetail button below to display the HISA information details. (You can also double click a record to view the details.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><u>7</u>. HISA Information</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/108.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/109.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24185580" class="anchor"></span>View 2319 – Home Oxygen

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Window description</td>
<td><blockquote>
<p>The eighth tab details the <strong>Home Oxygen</strong> information including the date, quantity, item, type, vendor, station, serial, HCPCS Code, and total cost of the item(s).</p>
<p><strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                      |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                               |
| 1    | Select a transaction by clicking on it to highlight it.                                                                                              |
| 2    | Click the ViewDetail button below to display the Home Oxygen information details. (You can also double click a record to view the details.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><u>8</u>. Home Oxygen</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/110.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit</td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/111.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Detail</td>
<td><blockquote>
<p>When you select a record and click the <strong>View Detail</strong> button, the following window displays as shown on the next page</p>
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
<td>View Detail button</td>
<td><blockquote>
<p>After clicking the <strong>View Detail</strong> button on the <strong>Home Oxygen</strong> window, the following window displays for the patient.</p>
</blockquote></td>
</tr>
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
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/112.png)</p>
</blockquote></td>
</tr>
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
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/113.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299386" class="anchor"></span>View and Manage the DOR

<span id="_Toc44299387" class="anchor"></span>View CPRS

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>The <strong>View CPRS</strong> button from the <strong>DOR</strong> window allows you to view all the consult data on the <strong>View CPRS</strong> window as shown below. This is the same data as in the electronic Consult - <strong>Suspense (SU) Menu</strong> feature where you can enter CD for the CPRS Display.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View CPRS window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/114.png)</p>
</blockquote></td>
</tr>
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
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/115.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299388" class="anchor"></span>View Request

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Function description</td>
<td><blockquote>
<p>When you click the <strong>View Request</strong> button on the <strong>DOR</strong> window, the <strong>View Request</strong> window displays as shown below. This provides the display of the manual suspense entry for the patient.</p>
<p><strong>Note:</strong> You can also double click on a record in the <strong>DOR</strong> window grid to display this <strong>View Request</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Request window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/116.png)</p>
</blockquote></td>
</tr>
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
<p>To exit, click the <strong>Close</strong> button or the ![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/117.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="SaveExcel" class="anchor"></span>Save as an Excel File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Excel Button</td>
<td><blockquote>
<p>Click the <strong><u>E</u>xcel</strong> button on the <strong>Delayed Order Report</strong> window to launch Excel and display the current data. (You can also click the <strong>File</strong> menu, click <strong>Excel,</strong> then select the <strong>Send - Request Grid</strong> option.)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key to launch MS Excel.</p>
<p><strong>Note:</strong> This feature creates a temporary Excel .CSV file in the folder selected. The default folder is C:\NPPDDownload (which is automatically created). The file name is based on the number of selected sites and the SSN range.</p>
<p><strong><u>Examples</u>:</strong> DOR_1_00_33.csv means 1 site was selected for SSN range 00-33.</p>
<p>DOR_ALL_34_99.csv means All Sites were selected for SSN range 34-99.</p>
</blockquote>
<p>Prior to the display, you are notified that the information about to be exported may contain Patient Identifiable Information.</p></td>
</tr>
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
<p>To export data to Excel:</p>
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
<td><p>Click the <strong><u>E</u>xcel</strong> button on the <strong>Delayed Order Report</strong> window.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Click the <strong><u>O</u>K</strong> button on the security reminder.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Continue to the <strong>Select Directory</strong> window.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Security Reminder</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/118.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                              |
| 4    | Navigate to the desired directory and select <u>OK</u> .(Click Cancel to exit or <u>H</u>elp to view the help pages associated with this functionality) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Directory</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/119.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                   |
| 5    | Navigate to a secure location where the temporary Excel (.csv) file will be stored and then select <u>O</u>K . Excel will open and display the data. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>MS Excel data</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/120.png)</p>
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
<td>6</td>
<td><p>This is only a temporary file so if you wish to save the data you must select <strong><u>F</u>ile,</strong> then <strong>Save <u>A</u>s,</strong> then change the name of the file.</p>
<p><strong>Note:</strong> To save the file, you <strong>must</strong> change the filename from the default. If you accept the default file name, it will be deleted when you close the DOR window.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Temp file location</td>
<td><blockquote>
<p>Should you wish to check the location of the temp file, it displays on the DOR window right below the Print button.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/121.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>You will be unable to export another report to Excel or navigate away from the DOR window until the current Excel (.csv) file is closed. Attempting to do so without first closing the file will result in one of the following errors depending on what action has taken place. If you do save a file with Patient Identifiable Info in it, don’t forget to delete it when you no longer need it.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attempting to Open another report with temp file still open</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/122.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attempting to navigate away from the DOR window with temp file still open</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/123.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299390" class="anchor"></span>Print the DOR

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print the DOR data</td>
<td><blockquote>
<p>You can print the <strong>DOR</strong> data using the <strong>Print</strong> button to send this data to your local printer. You can also click the <strong>File</strong> Menu and the <strong>Print-Request Grid</strong> option, and the <strong>Print</strong> dialog box displays. The layout of the print will be the same as the display.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;P&gt;</strong> key.</p>
<p><strong>Note:</strong> You can select a different printer that you have setup to print the detail.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Landscape default</td>
<td><blockquote>
<p>When printing grids, the default is set to print in the <strong>Landscape</strong> format and then returns the printer to the prior state.</p>
</blockquote></td>
</tr>
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
<p>To print the DOR, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                         |
| 1    | Click the <u>P</u>rint button on the DOR window.                                                                                                                       |
| 2    | The Print dialog box displays.                                                                                                                                             |
| 3    | Click the <u>P</u>roperties button (to the right of the Name field) on the Print dialog box if you want to change the page orientation of the printout. (Optional) |
| 4    | Click the OK button.                                                                                                                                                       |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print dialog box</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/124.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

  
<span id="_Toc172537373" class="anchor"></span>Exiting the DOR Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit the Window</td>
<td><blockquote>
<p>You can exit the application by first clicking the <strong>Menu</strong> button on the <strong>Delayed Order Report</strong> window. This closes the DOR window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>DOR “Menu” button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/125.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit the Application</td>
<td><blockquote>
<p>Then click the <strong>Close</strong> button on the <strong>Prosthetics</strong> <strong>Main Menu</strong> window:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|     |     |
|-----|-----|
|     |     |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Main Menu “Close” button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/126.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Confirmation window</td>
<td><blockquote>
<p>Click OK on the confirmation window to close the Prosthetics VistA Suite.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/127.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cancel button</td>
<td><blockquote>
<p>If you click the <strong>Cancel</strong> button, you will remain in the application and can continue to work.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537374" class="anchor"></span>Section 4

<span id="_Toc172537375" class="anchor"></span>View Prosthetics Billing Information

<span id="_Toc89754773" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>This <strong>View Prosthetics Billing Information</strong> <strong>User Manual</strong> is for Patch RMPR*3*96. This patch provides Prosthetics GUI (graphical user interface) windows for the <strong>View Prosthetics</strong> <strong>Billing Information</strong> feature.</p>
<p>The Prosthetics and Billing users will be able to do the following with this patch:</p>
</blockquote>
<ul>
<li><p>Search for data and display data by a range of dates.</p></li>
<li><p>Sort and rearrange the view; display data in a custom view.</p></li>
<li><p>Print the display.</p></li>
<li><blockquote>
<p>Convert the display into a MS Excel file (for complex sorting features).</p>
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
<td>Audience</td>
<td><blockquote>
<p>These Release Notes are geared towards two audiences. The <strong>VistA Sign-on</strong> window will appear with different functions according to which type of user is accessing the Billing information. The two audiences for this document and the <strong>VistA Sign-on</strong> window include:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Billing users – Section 1</p>
</blockquote></li>
<li><blockquote>
<p>Prosthetics users – Section 2</p>
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
<td>Data displayed</td>
<td><blockquote>
<p>The data that is displayed on the <strong>View Prosthetics Billing Information</strong> window includes the following:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Site</p>
</blockquote></li>
<li><blockquote>
<p>Create Date</p>
</blockquote></li>
<li><blockquote>
<p>Delivery Date</p>
</blockquote></li>
<li><blockquote>
<p>Patient name</p>
</blockquote></li>
<li><blockquote>
<p>Social Security Number</p>
</blockquote></li>
<li><blockquote>
<p>Insurance</p>
</blockquote></li>
<li><blockquote>
<p>Coding Errors</p>
</blockquote></li>
<li><blockquote>
<p>Item Description</p>
</blockquote></li>
<li><blockquote>
<p>Quantity</p>
</blockquote></li>
<li><blockquote>
<p>Total Cost</p>
</blockquote></li>
<li><blockquote>
<p>HCPCS</p>
</blockquote></li>
<li><blockquote>
<p>HCPCS Description</p>
</blockquote></li>
<li><blockquote>
<p>ICD9</p>
</blockquote></li>
<li><blockquote>
<p>ICD9 Description</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc89754774" class="anchor"></span>

Chapter 1 - For Billing Users

<span id="_Toc89754775" class="anchor"></span>Billing Main Menu Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing Main windows</td>
<td><blockquote>
<p>Below is the <strong>Prosthetics Main Menu</strong> window where Billing users can first sign-on to VistA (using the <strong>VistA Sign-On</strong> button) and then access the <strong>View Prosthetics Billing Information</strong> window. The Billing users will see a “<em>green dollar sign</em>” icon on the desktop to select the Prosthetics feature.</p>
<p><strong>Note:</strong> Please see the <strong>Prosthetics Main Menu User Manual</strong> for more detail information regarding VistA Sign-On instructions.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetics Main Menu</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/128.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing button</td>
<td><blockquote>
<p>Click the <strong>View Prosthetics Billing Information</strong> button and proceed to Chapter 3.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754776" class="anchor"></span>

Chapter 2 – For Prosthetics Users

<span id="_Toc89754777" class="anchor"></span>Prosthetics Main Menu Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetics Main Menu Window</td>
<td><blockquote>
<p>The <strong>Prosthetics Main Menu</strong> window is also where Prosthetics users can sign-on to VistA and then access the <strong>View Prosthetics Billing Information</strong> window. These users also have access to other Prosthetics features.</p>
<p><strong>Note:</strong> To access this application, you will double click on the <strong>Prosthetics VistA Suite</strong> (<em>medicine bag)</em> icon on desktop. Please see the <strong>Prosthetics Main Menu User Manual</strong> for more detailed VistA Sign-on instructions.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing button</td>
<td><blockquote>
<p>Click the <strong>View Prosthetics Billing Information</strong> button and proceed to the next page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754778" class="anchor"></span>

Chapter 3 – View Billing Information Package

<span id="_Toc89754779" class="anchor"></span>View Billing Information Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purpose</td>
<td><blockquote>
<p>You can view Prosthetics billing information, insurance information and disability information for specific veteran using the <strong>View Prosthetics Billing Information</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Prosthetics Billing Information main window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/129.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu button</td>
<td><blockquote>
<p>The <strong>Menu</strong> button will close the <strong>View Prosthetic Billing Information</strong> window and return you to the <strong>Prosthetics Main Menu</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754780" class="anchor"></span>Enter a Date Range

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date/Calendars</td>
<td><blockquote>
<p>After you have successfully signed on to VistA, and the <strong>View Prosthetic Billing Information</strong> window appears, you must select the date range that you want to view.</p>
<p>Enter a <strong>Beginning Date</strong> and an <strong>Ending Date</strong> by clicking on the drop-down list boxes next to the respective fields. A calendar displays as shown below.</p>
<p><strong>Note:</strong> The software will sort by the <strong>Create Date</strong> field of the Prosthetics Purchase Order or Stock Issue. It does <strong>not</strong> sort by the <strong>Delivery Date</strong> field (the date paid).</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/130.png)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Ctrl&gt;</strong> key <strong>+ &lt;B&gt;</strong> key for the Beginning Date and the<br />
<strong>&lt;Ctrl&gt;</strong> key + <strong>&lt;E&gt;</strong> key for the Ending Date to display the respective calendars. You can also click the <strong>File</strong> Menu and the <strong>Select</strong> <strong>Beginning Date</strong> or <strong>Select</strong> <strong>Ending Date</strong> option from the list.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Calendar for date range selection</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/131.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Enter a Date Range, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Selecting a date range</td>
<td><blockquote>
<p>The calendars display with the current date circled in red shown at the bottom of the calendar. You can accept the current date by clicking on it. You can also change the date by the following methods:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|             |                                                                                                                                                                                                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change the… | Description                                                                                                                                                                                     |
| Day     | Click on the actual day of the week in the calendar.                                                                                                                                            |
| Month   | Click on the month at the top of the calendar to display a list of all months and select one from there. You can decrease or increase one month at a time by clicking the left or right arrows. |
| Year    | Click on the year and an up and down arrow button displays for you to increase or decrease the year.                                                                                            |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Number of Day Restrictions</td>
<td><blockquote>
<p>You are restricted to a date range of less than 100 days. If you select a date range outside of this 100 day parameter, the following dialog message box displays:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date Range Message box</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/132.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Start Date before End Date</td>
<td><blockquote>
<p>If you accidentally entered an incorrect date range, you will receive a warning message. For instance, if you enter a start date that is after the end date, the message below will display. Click the <strong>OK</strong> button and reselect your date range.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Start/End Date Message</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/133.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754781" class="anchor"></span>Display the Prosthetics Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Display the data</td>
<td><blockquote>
<p>Once you have selected the date ranges, click the <strong>Display</strong> button to reveal the data within that date range. (You can also click the <strong>File Menu</strong> and the <strong>Display</strong> option.)</p>
<p>A progress bar activates, and the button name changes to “<em>Searching</em>” while the system is retrieving records. (A long date range may result in a long search time.)</p>
<p><strong>Recommendation:</strong> The larger the date range selected, the greater time it will take to search, sort, and display the data. We recommend that you sort by a short date range (5-10 days) and perform the sort early in the morning or later in the day when your VistA system is less active.</p>
<p><strong>Shortcut:</strong> Press the &lt;<strong>Ctrl</strong>&gt; key + &lt;<strong>D</strong>&gt; key.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Prosthetics Billing Information</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/134.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537385" class="anchor"></span>Change Data Display

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Changing the display of the data…</td>
<td><blockquote>
<p>You can manipulate the layout of the view in the <strong>View Prosthetics Billing Information</strong> window for both viewing as well as printing purposes as follows:.</p>
</blockquote>
<ul>
<li><p>To enlarge a column, click and drag a cell border.</p></li>
<li><p>To sort on any column, click on the header to sort it in <u>ascending order</u>.</p></li>
<li><p>If you click on the same column again, it will sort it in <u>descending order</u>.</p></li>
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
<td>Refresh data</td>
<td><blockquote>
<p>If you have changed the sort order, you can refresh your data by clicking the <strong><u>D</u>isplay</strong> button again.</p>
<p><strong><u>Note</u>:</strong> Refresh does not reset any column resizing that has been done.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537386" class="anchor"></span>View Column Descriptions - Site, Dates and Patient Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> column displays the VA facility where the veteran was treated and where the Prosthetics transaction was created.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Create Date</td>
<td><blockquote>
<p>The <strong>Create Date</strong> is the date the transaction (Purchase Order or Stock Issue) was created and posted to the Prosthetic veteran’s record (2319).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Delivery Date</td>
<td><blockquote>
<p>If the <strong>Delivery Date</strong> field is blank, this indicates that Prosthetics has <strong>NOT</strong> paid the item; therefore an assumption is made that the veteran may not have received the item.</p>
<p>The <strong>Delivery Date</strong> is <strong>not</strong> the date the veteran received the item; it is technically the date the Purchase Order was closed or the date the Stock Issue transaction was posted to the 2319.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Patient</td>
<td><blockquote>
<p>The <strong>Patient</strong> column contains the veteran’s last name and first name. Only Non-Service Connected transactions display for the requested date range.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SSN</td>
<td><blockquote>
<p>The <strong>SSN</strong> column displays the patient’s Social Security Number (SSN).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column Headers</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/135.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754784" class="anchor"></span>View Column Description - Insurance Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Insurance for a patient</td>
<td><blockquote>
<p>The <strong>Insurance</strong> column displays health insurance information from the patient’s VistA record.</p>
<p>If there is no health insurance information in the patient’s VistA record, it displays “<em>Nothing Found</em>” in the <strong>Insurance</strong> column.</p>
<p>If health insurance displays, then the <u>most recent</u> insurance entered into the patient’s VistA record will display.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Insurance column</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/136.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Asterisk</td>
<td><blockquote>
<p>If there is an asterisk (*) in the <strong>Insurance</strong> column, this indicates that there is more than one insurance listed for the patient. If there is no asterisk (*), then there is only ONE insurance listed for the patient in the VistA record.</p>
<p>Click on that line item to display the insurance information in the box below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sorting Tip</td>
<td><blockquote>
<p>You can sort on the column headers within the <strong>Insurance Information</strong> box to group items together for easier review. For instance, you can click on the <strong>Effective date</strong> column or <strong>Expires date</strong> column headers, and this will group items for reviewing the most recent insurance.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Effective date column sorted</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/137.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754785" class="anchor"></span>View Column Descriptions - Coding Errors

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Coding Errors</td>
<td><blockquote>
<p>The <strong>Coding Errors</strong> column is to alert Billing users of a <em>possible</em> error. Errors could be any of the following:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Inactive HCPCS</p>
</blockquote></li>
<li><blockquote>
<p>Inactive ICD-9 codes</p>
</blockquote></li>
<li><blockquote>
<p>Use of VA unique HCPCS codes.</p>
</blockquote></li>
</ul>
<blockquote>
<p>The <strong>Coding</strong> <strong>Errors</strong> column checks the HCPCS code to see if it was valid at the time of service, and if not, then the word “HCPCS” is shown in red as well as the “HCPCS Description” is shown in red. This also applies to the inactive ICD9 Codes.</p>
<p><strong><u>Example</u>:</strong> If there is a red HCPCS displayed in the <strong>HCPCS</strong> column, then the <strong>Coding Errors</strong> column will display “<strong>Alert HCPCS</strong>” for Prosthetics or Billing users. This will provide a mechanism to alert users to review this billing information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Coding Column</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/138.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sorting Tip</td>
<td><blockquote>
<p>You can sort on the <strong>Coding Errors</strong> column by clicking the column header to group items for review.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754786" class="anchor"></span>View Column Descriptions - Item Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item definition</td>
<td><blockquote>
<p>The <strong>Item</strong> column displays an Item or appliance kept in the Pros Master Item file. This column displays the IFCAP Item description of the Item issued to the Veteran.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>~R~ in the Item column</td>
<td><blockquote>
<p>An “<strong>~R~</strong>” displayed in the <strong>Item</strong> column represents a <strong>Repair</strong> item. The <strong>HCPCS Description</strong> column should explain what was being repaired.</p>
<p>The <strong>Item</strong> column is the “<em>Brief Description</em>” entry that is printed on the purchase order transaction and appears on the 2319 record. The <em>Brief Description</em> is entered to define the item.</p>
<p><strong>Tip:</strong> You can sort on the Item column by clicking the column header to group items to review all Repair items together.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item column sorted – Repair items grouped together</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/139.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754787" class="anchor"></span>View Column Descriptions - Quantity and Total Cost Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Qty column</td>
<td><blockquote>
<p>The <strong>Quantity</strong> column provides the number issued of that Item to the veteran. This is the quantity based on purchasing (not units).</p>
<p><strong>Note:</strong> For Home Oxygen, it is a payment unit not a billing unit.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column headers</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/140.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Total Cost column</td>
<td><blockquote>
<p>The <strong>Total Cost</strong> column represents the cost of the issue.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754788" class="anchor"></span>View Column Descriptions - HCPCS and HCPCS Description Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS definition</td>
<td><blockquote>
<p>The HCPCS acronym stands for Healthcare Financing Administration Common Procedure Coding System. The HCPCS code represents an item or service. The Prosthetics staff selects the HCPCS code when the transaction was created.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Red HCPCS</td>
<td><p>If the HCPC Code and HCPCS Description in the <strong>HCPCS</strong> and <strong>HPCPS Description</strong> columns are red, that represents a HCPCS Code that has a coding error as defined by an Inactive HCPCS.</p>
<blockquote>
<p>This provides an alert to Prosthetics and Billing users as this will affect billing information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column headers</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/141.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Asterisk in HCPCS column and Calculation Flag</td>
<td><blockquote>
<p>If there is an asterisk in the <strong>HCPCS</strong> column, this indicates that there is a calculation flag.</p>
</blockquote>
<p>A calculation flag determines whether or not a HCPCS is used as a Main Component to display the entire cost of a purchase, when multiple items within the purchase make up a whole (e.g., when purchasing a limb or surgical implants).</p></td>
</tr>
</tbody>
</table>

<span id="_Toc89754789" class="anchor"></span>View Column Descriptions - ICD9 and ICD9 Description

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ICD9 definition</td>
<td><blockquote>
<p>International Classification of Diseases (Ninth Revision) <strong>-</strong>A coding system designed by WHO, (World Health Organization). ICD-9-CM is the official system of assigning codes to diagnoses and procedures associated with hospital utilization in the United States.</p>
<p>The ICD –9 is used to code and classify mortality data from death certificates. VOLUMES 1-2 contain diagnosis and procedures. VOLUME 3 is used for statistical, research and re-imbursement purposes.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column headers</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/142.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ICD9 Code Selection</td>
<td><blockquote>
<p>This code is selected by the prescribing clinician when the Prosthetic consult is created.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754790" class="anchor"></span>View Column Descriptions - Disability Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Disability Information</td>
<td><blockquote>
<p>If the patient has disability information, it will automatically be displayed in the <strong>Disability Information</strong> box in the bottom of the window.</p>
<p>If a patient is selected without any disability information, the <strong>Disability Information</strong> box at the bottom of the window will display “<em>Nothing Found</em>.”</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Disability sample</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/143.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754791" class="anchor"></span>

Chapter 4 - Printing

<span id="_Toc89754792" class="anchor"></span>Print the View Prosthetics Billing Information Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print the data</td>
<td><blockquote>
<p>You can print the <strong>View Prosthetics</strong> <strong>Billing Information</strong> data after you have finished your sort by column heading. Click the <strong><u>P</u>rint</strong> button to send this information to your local printer, and click <strong>OK</strong> on the <strong>Print</strong> dialog box. (You can also click the <strong>File</strong> Menu and the <strong>Print</strong> option.)</p>
<p><strong>Note:</strong> The layout of the print will be the same as the display. You can select a specific printer to print the <strong>View Prosthetics Billing</strong> <strong>Information</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Change to Landscape</td>
<td><blockquote>
<p><strong><u>Recommendation</u>:</strong> You should change the format of the printout from <em>Portrait</em> to <em>Landscape</em> to print all the columns on the same page.</p>
</blockquote></td>
</tr>
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
<p>To change the print format, follow these steps:</p>
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
<td>Click the <strong><u>P</u>rint</strong> button on the <strong>View Prosthetics</strong> <strong>Billing Information</strong> window.</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>Click the <strong><u>P</u>roperties</strong> button (to the right of the <strong>Name</strong> field) on the <strong>Print</strong> dialog box. Continue to the next page.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;P&gt;</strong> key.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print dialog box</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/144.png)</p>
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
<td>Layout Tab</td>
<td><blockquote>
<p>You can change the format of the printout from the standard <em>Portrait</em> format to <em>Landscape</em> on the <strong>Layout</strong> tab.</p>
</blockquote></td>
</tr>
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
<p>To continue to change to the Landscape format, follow these steps:</p>
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
<td>Click the <strong>Layout</strong> tab on the <strong>Properties</strong> dialog box (usually shown as a default view).</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>Click the <strong><u>L</u>andscape</strong> radio button to change the format.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;L&gt;</strong> key.</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Click <strong>OK</strong> or press <strong>&lt;Enter.&gt;</strong></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Landscape Radio button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/145.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Last step</td>
<td><blockquote>
<p>When you return to the <strong>Print</strong> dialog box, click <strong>OK</strong> again, and it will print your output. You can print multiple copies if necessary.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc89754793" class="anchor"></span>

Chapter 5 – Saving

<span id="_Toc172537397" class="anchor"></span>Save as an Excel File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Excel Button</td>
<td><blockquote>
<p>Click the <strong><u>E</u>xcel</strong> button on the <strong>View Prosthetics Billing Information</strong> window to launch Excel and display the current data. (You can also click the <strong>File</strong> menu and select the <strong>Excel</strong> option.)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key to launch MS Excel.</p>
<p><strong>Note:</strong> This feature creates a temporary Excel .CSV file in the folder selected. The default folder is C:\ViewBillingDownload (which is automatically created). The file name is based on the date range.</p>
<p><strong><u>Example</u>:</strong> Jul 02, 2006_Aug 10, 2006.csv</p>
</blockquote>
<p>Prior to the display, you are notified that the information about to be exported may contain Patient Identifiable Information.</p></td>
</tr>
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
<p>To export data to Excel:</p>
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
<td><p>Click the <strong><u>E</u>xcel</strong> button on the <strong>View Prosthetics Billing Information</strong> window.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Click the <strong><u>O</u>K</strong> button on the security reminder.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Continue to the <strong>Select Directory</strong> window.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Security Reminder</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/146.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                              |
| 4    | Navigate to the desired directory and select <u>O</u>K .(Click Cancel to exit or <u>H</u>elp to view the help pages associated with this functionality) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Directory</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/147.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                   |
| 5    | Navigate to a secure location where the temporary Excel (.csv) file will be stored and then select <u>O</u>K . Excel will open and display the data. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>MS Excel data</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/148.png)</p>
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
<td>6</td>
<td><p>This is only a temporary file so if you wish to save the data you must select <strong><u>F</u>ile,</strong> then <strong>Save <u>A</u>s,</strong> then change the name of the file.</p>
<p><strong>Note:</strong> To save the file, you <strong>must</strong> change the filename from the default. If you accept the default file name, it will be deleted when you close the NPPD window.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Temp file location</td>
<td><blockquote>
<p>Should you wish to check the location of the temp file, it displays on the View Prosthetic Billing window right above the Excel button.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/149.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>You will be unable to export another report to Excel or navigate away from the View Prosthetic Billing Information window until the current Excel (.csv) file is closed. Attempting to do so without first closing the file will result in one of the following errors depending on what action has taken place. If you do save a file with Patient Identifiable Info in it, don’t forget to delete it when you no longer need it.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attempting to Open another report with temp file still open</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/150.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attempting to navigate away from the View Prosthetic Billing Information window with temp file still open</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/151.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537398" class="anchor"></span>AutoFilter

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>AutoFilter</td>
<td><blockquote>
<p>The <strong>AutoFilter</strong> feature can limit what is displayed for your view which can be printed for reports. Filtering is a quick and easy way to find and work with a subset of data in a list. A filtered list displays only the rows that meet the criteria you specify for a column.</p>
<p><strong>Steps:</strong> On the <strong>Data</strong> menu, point to <strong>Filter</strong>, and then click <strong>AutoFilter</strong>.</p>
<p>When you use the <strong>AutoFilter</strong> command, arrows appear to the right of the column labels in the filtered list.</p>
<p><strong>Note:</strong> Unlike sorting, filtering does not rearrange a list. Filtering temporarily hides rows you do not want displayed. When Excel filters rows, you can edit, format, chart, and print your list subset without rearranging or moving it.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537399" class="anchor"></span>Chapter 6 - Closing and Exiting

<span id="_Toc172537400" class="anchor"></span>Exiting the View Prosthetic Billing Information Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit the Window</td>
<td><blockquote>
<p>You can exit the application by first clicking the <strong>Menu</strong> button on the <strong>View Prosthetic Billing Information</strong> window. This closes the View Prosthetic Billing Information window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Prosthetic Billing Information “Menu” button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/152.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit the Application</td>
<td><blockquote>
<p>Then click the <strong>Close</strong> button on the <strong>Prosthetics</strong> <strong>Main Menu</strong> window:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|     |     |
|-----|-----|
|     |     |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Main Menu “Close” button</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/153.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Confirmation window</td>
<td><blockquote>
<p>Click OK on the confirmation window to close the Prosthetics VistA Suite.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/154.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cancel button</td>
<td><blockquote>
<p>If you click the <strong>Cancel</strong> button, you will remain in the application and can continue to work.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537401" class="anchor"></span>Section 5

<span id="_Toc172537402" class="anchor"></span>Creating a Lab Work Order

<span id="_Toc172537403" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>The Create application allows you to create an Orthotics Lab Work order (OWL). You may now Complete and Cancel a work order from the Graphical User Interface (GUI). The Create application also allows you view information associated with the current work order, such as 2319 information, CPRS data, and the initial Request.</p>
<p>The Create application is accessed from the Purchase Order Control window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Accessing the Create Lab Work Order window</td>
<td><blockquote>
<p>To access the Create Lab Work Order window from the Purchase Order Control window, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight a work order in the Purchase Order Control listview.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Note 1:</strong> The patient must be defined in the PROSTHETICS PATIENT FILE. If you select a patient who is not already defined, a popup message alerts you to this fact. (Click <strong>OK</strong> to clear the popup window.) Use the <strong>AP – Add/Edit Patient to Prosthetics</strong> option to correct this issue.</p>
</blockquote>
<blockquote>
<p><strong>Note 2:</strong> A work order that displays LAB in the Type column has already been used to create a lab order and may not be reused for that purpose.</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Click the <strong>Create OWL</strong> button. The Create Lab Work Order window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/155.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Create Lab Work Order window</td>
<td><blockquote>
<p>The <strong>Create Lab Work Order</strong> window shown below displays the name and SSN of the patient that was highlighted on the Purchase Control window when you clicked the Create OWL button.</p>
<p>The name and SSN display in blue letters in the upper-left corner of the screen. The Create Date displays in a yellow field in the upper-right corner.</p>
<p>You will create a Lab Work Order from this window for a specific patient.</p>
<p><strong>Note:</strong> On this screen, a field with a yellow background cannot be directly edited. The field value defaults in, sometimes as a result of another selection you’ve made.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Create Lab Order window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/156.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Quitting Work</td>
<td><blockquote>
<p>If you need to stop working at any point during the workflow, click the <strong>Quit Work</strong> button in the lower-right corner of the window. You will return to the Purchase Order Control window.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/157.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537404" class="anchor"></span>Selecting a Lab Type

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Lab Type</td>
<td><blockquote>
<p>The first step to creating a Lab Order is to select a Lab Type. Below the patient SSN there are four radio buttons that correspond to the following lab types:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Orthotics/Prosthetics</p>
</blockquote></li>
<li><blockquote>
<p>Optical</p>
</blockquote></li>
<li><blockquote>
<p>Restoration</p>
</blockquote></li>
<li><blockquote>
<p>Wheelchair</p>
</blockquote></li>
</ul>
<blockquote>
<p>Click one of the <strong>Lab Type</strong> radio buttons, then mouse click or press <strong>&lt;Tab&gt;</strong> to go to the next field.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Lab Type radio buttons</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/158.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537405" class="anchor"></span>Selecting Stations

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NPPD Station</td>
<td><blockquote>
<p>The National Prosthetic Patient Database (NPPD) is a dynamic, comprehensive national database used to collect information on the disabled population’s use of prosthetic, orthotic, and sensory aids. This information allows for statistical analysis and oversight of the VA Prosthetic Service. The NPPD compiles prosthetic data recorded at each VHA facility, or station.</p>
<p>Click the <strong>NPPD Station</strong> drop-down arrow to display a list of stations for you to select one. A shortcut is to enter a partial spelling of the <strong>NPPD Station</strong> and click the drop-down arrow (or press the &lt;TAB&gt; key) to select one beginning with the criteria that you entered.</p>
<p>Once a station has been selected, the station name displays next to the NPPD Station label and the site number displays in the yellow field to the right.</p>
<p><strong>Note:</strong> For a user at a station which does its own OWL, the NPPD Station, Receiving Station, and Requesting Station will all be the same.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NPPD Station drop-down list</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/159.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Receiving Station</td>
<td><blockquote>
<p>Enter a partial spelling of the <strong>Receiving Station</strong> and click the drop-down arrow (or press the &lt;TAB&gt; key) to select an item beginning with the characters you entered. The Receiving Station is the institution that will receive the VAF 10-2529-3 request for processing.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Requesting Station</td>
<td><blockquote>
<p>Enter a partial spelling of the <strong>Requesting Station</strong> and click the drop-down arrow (or press the &lt;TAB&gt; key) to select an item beginning with the characters you entered. The Requesting Station is the station requesting the services or appliances.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537406" class="anchor"></span>Patient Category and Type of Transaction

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Patient Category</td>
<td><blockquote>
<p>The next step is to select a Patient Category. To the right of the patient SSN there are two radio buttons that correspond to the following patient categories:</p>
</blockquote>
<ul>
<li><blockquote>
<p>SC (service connected)</p>
</blockquote></li>
<li><blockquote>
<p>NSC (non-service connected)</p>
</blockquote></li>
</ul>
<blockquote>
<p>Click one of the <strong>Patient Category</strong> radio buttons.</p>
<p><strong>Shortcut:</strong> Press the <strong>&lt;Tab&gt;</strong> key to move focus to the Patient Category area, then use the arrow keys to select a Patient Category.</p>
<p>For your reference, a listview to the right of the Patient Category area displays disabilities on record for the current patient. This listview displays the following three columns:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Disability</p>
</blockquote></li>
<li><blockquote>
<p>% (percentage of disability)</p>
</blockquote></li>
<li><blockquote>
<p>SC (service connected – yes or no)</p>
</blockquote></li>
</ul>
<p>The SC column displays YES if the disability is service connected and NO if otherwise.</p>
<blockquote>
<p>You may sort this display by clicking any one of the column headings.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Patient Category area</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/160.png)</p>
</blockquote></td>
</tr>
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
<p>Below the Patient Category area there are two radio buttons that correspond to the following transaction types:</p>
</blockquote>
<ul>
<li><blockquote>
<p>New / Replace</p>
</blockquote></li>
<li><blockquote>
<p>Repair / Service</p>
</blockquote></li>
</ul>
<blockquote>
<p>Click one of the <strong>Type of Transaction</strong> radio buttons.</p>
<p><strong>Shortcut:</strong> Press the <strong>&lt;Tab&gt;</strong> key to move focus to the Type of Transaction area, then use the arrow keys to select a Type of Transaction.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537407" class="anchor"></span>Primary Item Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing Item</td>
<td><blockquote>
<p>Enter a partial spelling of the <strong>Billing Item</strong> and click the drop-down arrow (or press the &lt;Tab&gt; key) to select an item beginning with the characters you entered.</p>
</blockquote></td>
</tr>
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
<p>Enter a partial spelling of the <strong>HCPCS</strong> code or description and click the drop-down arrow (or press the &lt;Tab&gt; key) to select a code containing the characters that you entered.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CPT Modifier</td>
<td><blockquote>
<p>Below the HCPCS field there are four radio buttons that correspond to the following CPT Modifiers:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Left</p>
</blockquote></li>
<li><blockquote>
<p>Right</p>
</blockquote></li>
<li><blockquote>
<p>Both</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
</ul>
<blockquote>
<p>Click the applicable <strong>CPT Modifier</strong> radio button.</p>
<p><strong>Shortcut:</strong> Press the <strong>&lt;Tab&gt;</strong> key to move focus to the CPT Modifier area, then use the arrow keys to select a CPT Modifier.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Extended Description</td>
<td><blockquote>
<p>To enter a longer description of the item, click the <strong>Extended Desc.</strong> button. The OWL Extended Description window shown below displays. You can type a free-text extended description of an unlimited maximum number of characters. Click the <strong>OK</strong> button to close the window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Extended Description window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/161.png)</p>
</blockquote></td>
</tr>
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
<p>The Unit of Issue is 1 by default and cannot be changed.</p>
<p><strong>Note:</strong> Any field on this screen with a yellow background is for display only and cannot be modified.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Quantity</td>
<td><blockquote>
<p>The quantity defaults to 1 and cannot be changed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537408" class="anchor"></span>Changing the Date Required

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Change Date Required</td>
<td><blockquote>
<p>Today’s date defaults into the Date Required field. To select a different date, click the <strong>Change Date Required</strong> button.</p>
<p><strong>Note:</strong> You may only select today’s date or a future date.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Please select a new Date Required</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/162.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537409" class="anchor"></span>Changing the Print Location

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Request Receipt</td>
<td><blockquote>
<p>Once you submit the lab work order, a request receipt will print automatically to the printer specified in the Print Location field.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print Location area</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/163.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Change Print Location</td>
<td><blockquote>
<p>To change the printer, click the <strong>Change Print Location</strong> button, located near the lower-left corner of the window.</p>
<p>The Please Select a Printer window displays.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Please Select a Printer window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/164.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Printer Type</td>
<td><blockquote>
<p>You may select one of the following three printer types:</p>
</blockquote>
<ul>
<li><blockquote>
<p>A Window Printer</p>
</blockquote></li>
<li><blockquote>
<p>A VistA Printer of your choice</p>
</blockquote></li>
<li><blockquote>
<p>The Default VistA Printer</p>
</blockquote></li>
</ul>
<blockquote>
<blockquote>
<p><strong>Note:</strong> The default VistA printer is defined in file 669.9 PROSTHETICS SITE PARAMETER.</p>
</blockquote>
<blockquote>
<p>Depending on the Lab Type you chose when the OWL was created, the VistA printer is defined in the following field:</p>
</blockquote>
</blockquote>
<ul>
<li><blockquote>
<p>Optical - 26 - EYE CLINIC LAB DEVICE</p>
</blockquote></li>
<li><blockquote>
<p>Orthotics/Prosthetics - 27 - ORTHOTIC LAB DEVICE</p>
</blockquote></li>
<li><blockquote>
<p>Restoration - 28 - RESTORATION CLINIC DEVICE</p>
</blockquote></li>
<li><blockquote>
<p>Wheelchair - 30 - WHEELCHAIR REPAIR SHOP DEVICE</p>
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
<td>Windows Printer</td>
<td><blockquote>
<p>To select a Windows printer, click the <strong>Windows Printer</strong> button in the Change Print Location area. The Windows Print dialog displays.</p>
<p>Select the desired printer from the <strong>Name</strong> dropdown, then click <strong>OK</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows Printer selection window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/165.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Default VistA Printer</td>
<td><blockquote>
<p>To print to the Default VistA Printer, click the <strong>Default VistA Printer</strong> button, then click <strong>OK</strong>.</p>
<p><strong>Notes:</strong> The Default VistA Printer is the default print location, so you don’t have to do anything unless you’ve already changed the printer before. The default VistA printer is defined in file 669.9 PROSTHETICS SITE PARAMETER.</p>
<p>Depending on the Lab Type you chose when the OWL was created, the VistA printer is defined in the following field:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Optical - 26 - EYE CLINIC LAB DEVICE</p>
</blockquote></li>
<li><blockquote>
<p>Orthotics/Prosthetics - 27 - ORTHOTIC LAB DEVICE</p>
</blockquote></li>
<li><blockquote>
<p>Restoration - 28 - RESTORATION CLINIC DEVICE</p>
</blockquote></li>
<li><blockquote>
<p>Wheelchair - 30 - WHEELCHAIR REPAIR SHOP DEVICE</p>
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
<td>Choose a VistA Printer</td>
<td><blockquote>
<p>To select a particular VistA Printer, choose a from the <strong>VistA Printer</strong> dropdown list, then click <strong>OK</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VistA Printer dropdown list</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/166.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Selected Printer</td>
<td><blockquote>
<p>After you click OK, the name of the selected printer displays in the Print Location field.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Print Location area</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/167.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537410" class="anchor"></span>Viewing Additional Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>The lower-left corner of the Create Lab Work Order screen contains the following three buttons:</p>
</blockquote>
<ul>
<li><blockquote>
<p>2319</p>
</blockquote></li>
<li><blockquote>
<p>CPRS</p>
</blockquote></li>
<li><blockquote>
<p>Request</p>
</blockquote></li>
</ul>
<blockquote>
<p>These buttons, described briefly below, function just as they do on the Purchase Order Control window. For more information, see Section 1 of this manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>2319 button</td>
<td><blockquote>
<p>To view all eight tabs of 2319 data for a patient, click the <strong>2319</strong> button.</p>
<p>For more information, see Chapter 4 in Section 1 of this manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CPRS button</td>
<td><blockquote>
<p>To view the CPRS record for a patient, click the <strong>CPRS</strong> button.</p>
<p>For more information, see Chapter 5 in Section 1 of this manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Request button</td>
<td><blockquote>
<p>To view the request (if information is available for this patient), click the <strong>Request</strong> button.</p>
<p>For more information, see Chapter 6 of Section 1 of this manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537411" class="anchor"></span>Submitting the Lab Work Order

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Create Lab Work Order button</td>
<td><blockquote>
<p>To submit the Lab Work Order, click the <strong>Create Lab Work Order</strong> button, in the lower-right corner of the Create Lab Work Order window.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/168.png)</p>
<p>The request receipt will print to the printer specified in the Print Location area.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537412" class="anchor"></span>Section 6

<span id="_Toc172537413" class="anchor"></span>Orthotic Lab & Work Order

<span id="_Toc172537414" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Accessing the Orthotics Work Order and Lab window</td>
<td><blockquote>
<p>The OWL window is accessible from two different locations:</p>
<p><strong>Method 1 – Accessing OWL from the Prosthetics Main Menu</strong></p>
<p>At the Prosthetics Main Menu, click the <strong>Orthotic Lab &amp; Work Order</strong> button. The OWL window displays.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/169.png)</p>
<p><strong>Method 2 – Accessing OWL from the Purchase Control window</strong></p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/170.png)</p>
<p>At the Purchase Order Control window, click the <strong>OWL.</strong> button. The OWL window displays.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Orthotics Work Order and Lab window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/171.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Quitting Work</td>
<td><blockquote>
<p>If you need to stop working at any point during the workflow, click the <strong>Close</strong> button in the lower-right corner of the window. You will return to the Main Menu.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/172.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537415" class="anchor"></span>Orthotic Lab & Work Order Window Areas

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Seven Major window areas</td>
<td><blockquote>
<p>The OWL window contains seven major areas where you can view information or enter data. These areas are described below.</p>
</blockquote>
<ul>
<li><blockquote>
<p>Title bar</p>
</blockquote></li>
<li><blockquote>
<p>Menu bar</p>
</blockquote></li>
<li><blockquote>
<p>Work Orders listview</p>
</blockquote></li>
<li><blockquote>
<p>HCPCS area</p>
</blockquote></li>
<li><blockquote>
<p>Command Buttons</p>
</blockquote></li>
<li><blockquote>
<p>HCPCS Materials area</p>
</blockquote></li>
<li><blockquote>
<p>HCPCS Labor area</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc172537416" class="anchor"></span>Title Bar

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Title Bar</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/173.png)</p>
<p>The title bar runs along the top edge of the OWL window. Its default color is blue and it contains the name of the application.</p>
<p>The three buttons at the far right of the title bar allow you to minimize, maximize/restore, and close the window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537417" class="anchor"></span>Menu Bar

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu Bar</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/174.png)</p>
<p>The menu bar lies below the title bar. The OWL title bar contains eight options: File, Select &amp; Display, View, Work Order, HCPCS, Materials, Labor, and Help. Click an option on the menu bar to list all the operations you can perform from within that menu. Click the desired option to execute a specific function.</p>
<p>Each menu option and its corresponding suboptions display as listed below:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File menu</td>
<td><blockquote>
<p>The following options are available from the File menu:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Print OWL:</strong> Print the selected lab work order.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Exit:</strong> Save current data and close the OWL window.</p>
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
<td>Select &amp; Display menu</td>
<td><blockquote>
<p>The following options are available from the Select &amp; Display menu:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Pending Assignment:</strong> Toggle Pending Assignment box checked/unchecked. Check box to display lab work orders not assigned to a tech.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Assigned:</strong> Toggle Assigned box checked/unchecked. Check box to display lab work orders assigned to a tech.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Completed:</strong> Toggle Completed box checked/unchecked. Check box to display lab work orders with a Completed status.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Cancelled:</strong> Toggle Cancelled box checked/unchecked. Check box to display lab work orders with a Cancelled status.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Display/Refresh:</strong> Refresh the Work Orders Listview display.</p>
</blockquote></li>
</ul>
<blockquote>
<p>For more information on using the Work Orders listview, see “Filtering the Work Orders Listview,” Filtering_the_Work_Orders_Listvlater in this chapter.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View menu</td>
<td><blockquote>
<p>The following options are available from the View menu:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>View 2319:</strong> Display 2319 information for the selected lab work order.</p>
</blockquote></li>
<li><blockquote>
<p><strong>View CPRS:</strong> Display CPRS information for the selected lab work order.</p>
</blockquote></li>
<li><blockquote>
<p><strong>View Request:</strong> Display request information for the selected lab work order.</p>
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
<td>Work Order menu</td>
<td><blockquote>
<p>The following options are available from the Work Order menu:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>OWL Detail:</strong> Display lab work order detail.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Assign Tech:</strong> Assign a technician to the selected lab work order.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Complete OWL:</strong> Complete the selected work order.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Cancel OWL:</strong> Cancel the selected work order.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Print OWL:</strong> Display the Print Lab Work Order dialog.</p>
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
<td>HCPCS menu</td>
<td><blockquote>
<p>The following options are available from the HCPCS menu:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Detail / Edit:</strong> Display OWL Material dialog.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Add HCPCS:</strong> Add secondary HCPCS items.</p>
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
<td>Materials menu</td>
<td><blockquote>
<p>The following options are available from the Materials menu:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Detail / Edit:</strong> View/edit the selected HCPCS materials.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Add Material:</strong> Add secondary HCPCS materials.</p>
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
<td>Labor menu</td>
<td><blockquote>
<p>The following options are available from the Labor menu:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Detail / Edit:</strong> View/edit the selected HCPCS labor.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Add Labor:</strong> Add labor hours for HCPCS item.</p>
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
<td>Help menu</td>
<td><blockquote>
<p>The following options are available from the Help menu:</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Contents:</strong> Display this online Help file.</p>
</blockquote></li>
<li><blockquote>
<p><strong>About:</strong> Display Prosthetics VistA Suite version # and compilation date.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc172537418" class="anchor"></span>Work Orders Listview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Work Orders Listview</td>
<td><blockquote>
<p>Use this area of the screen to view, filter, and sort work orders. It contains four checkboxes, a command button, a sortable listview, and a display of the total number of work orders.</p>
<p>For more information, see the “Filtering Lab Work Orders” section on page 181 of this manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Work Orders Listview</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/175.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537419" class="anchor"></span>HCPCS Area

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Overview</td>
<td><blockquote>
<p>Use this area of the screen to add, edit, and delete HCPCS items. It contains a sortable listview and two buttons.</p>
<p>The total number of HCPCS items and the total cost of HCPCS for the selected work order display below the listview.</p>
<p>For more information, see the “Managing HCPCS Items” section on page 184 of this manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Area</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/176.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Listview</td>
<td><blockquote>
<p>The following list provides an overview of some of the main features of the HCPCS listview:</p>
</blockquote>
<ul>
<li><blockquote>
<p>The number following the <strong>HCPCS for Work Order</strong> label matches the Lab Work Order (LWO) Number of the row highlighted above in the Work Orders listview.</p>
</blockquote></li>
<li><blockquote>
<p>The primary HCPCS item is indicated by a YES in the <strong>Pri</strong> column of the HCPCS listview. This HCPCS code matches the code selected when the work order was created.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Detail/Edit</strong> button to view or edit the item highlighted in the HCPCS listview. The OWL HCPCS window displays. You can edit all fields on t he OWL HCPCS window except Qty, Unit of Issue, and Total Cost. (See Editing a HCPCS Item.)</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Add HCPCS</strong> to add secondary HCPCS items to the work order. (See “Adding a HCPCS Item.”)</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc172537420" class="anchor"></span>Command Buttons Area

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Command buttons area</td>
<td><blockquote>
<p>A command button is a large button which, when clicked, executes a command. The Command Buttons area contains the following eight buttons:</p>
</blockquote>
<ul>
<li><blockquote>
<p>OWL Detail</p>
</blockquote></li>
<li><blockquote>
<p>2319</p>
</blockquote></li>
<li><blockquote>
<p>CPRS</p>
</blockquote></li>
<li><blockquote>
<p>Request</p>
</blockquote></li>
<li><blockquote>
<p>Assign Tech</p>
</blockquote></li>
<li><blockquote>
<p>Complete OWL</p>
</blockquote></li>
<li><blockquote>
<p>Cancel OWL</p>
</blockquote></li>
<li><blockquote>
<p>Print OWL</p>
</blockquote></li>
</ul>
<blockquote>
<p>Their functions are described in the Workflows section starting on page 181 of this manual.. For more information, see the following sections:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Managing Lab Technicians (page 182)</p>
</blockquote></li>
<li><blockquote>
<p>Printing the OWL (page 193)</p>
</blockquote></li>
<li><blockquote>
<p>Completing the OWL (page 194)</p>
</blockquote></li>
<li><blockquote>
<p>Cancelling the OWL (page 195)</p>
</blockquote></li>
<li><blockquote>
<p>Closing the OWL (page 196)</p>
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
<td>Command buttons</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/177.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>OWL Detail button</td>
<td><blockquote>
<p>Click the OWL Detail button to display information about the work order currently highlighted in the Work Order listview.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>OWL Detail</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/178.png)</p>
<p>The information on this screen is for display only and cannot be modified from this screen.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537421" class="anchor"></span>HCPCS Materials Area

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Materials Area</td>
<td><blockquote>
<p>Use this area of the screen to add, edit, and delete materials related to HCPCS items. It contains a sortable listview and two buttons.</p>
<p>The total number of Material Entries and the total cost of materials for the selected HCPCS item display below the listview.</p>
<p>For more information, see the “HCPCS Materials” section on page 187 of this manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Materials Area</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/179.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537422" class="anchor"></span>HCPCS Labor Area

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Labor Area</td>
<td><blockquote>
<p>Use this area of the screen to add, edit, and delete labor related to HCPCS items. It contains a sortable listview and two buttons.</p>
<p>The total number of Labor Entries and the total cost of labor for the selected HCPCS item display below the listview.</p>
<p>For more information, see the section “HCPCS Labor.”</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS Labor Area</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/180.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537423" class="anchor"></span>Workflows

<span id="_Toc172537424" class="anchor"></span>Filtering Lab Work Orders

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Work Orders listview checkboxes</td>
<td><blockquote>
<p>Four checkboxes allow you to filter the Work Orders listview. The Pending Assignment and Assigned checkboxes are checked by default.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Work Orders listview</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/181.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Workflow</td>
<td><blockquote>
<p>To filter the Work Orders listview, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Check the desired boxes:</p>
</blockquote></li>
</ol>
<ul>
<li><blockquote>
<p><strong>Pending Assignment:</strong> Display work orders with a Status of PENDING ASSIGNMENT (i.e., work orders with no Assigned Tech).</p>
</blockquote></li>
<li><blockquote>
<p><strong>Assigned:</strong> Display work orders with a Status of ASSIGNED TO TECHNICIAN.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Completed:</strong> Display work orders with a Status of COMPLETED.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Cancelled:</strong> Display work orders with a Status of CANCELLED.</p>
</blockquote></li>
</ul>
<blockquote>
<blockquote>
<p>The four checkboxes work in various combinations. Checking more than one checkbox displays the selected results connected by the Boolean operator OR. For example, if you check the boxes Assigned and Cancelled, then click Display/Refresh, the listview displays work orders with a Status of ASSIGNED TO TECHNICIAN <strong>or</strong> CANCELLED.</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Click <strong>Display/Refresh.</strong></p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/182.png)</p>
</blockquote>
<p><strong>Notes:</strong> This listview only displays completed and cancelled work orders that were created in GUI OWL.<br />
<strong>Work orders created in roll &amp; scroll will not display here.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537425" class="anchor"></span>Managing Lab Technicians

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Assigning a Tech</td>
<td><blockquote>
<p>To assign a technician to a work order that is pending assignment, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight a work order with a status of <strong>Pending Assignment</strong>, then click the <strong>Assign Tech</strong> command button. The Assign Technician window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/183.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Type a few <strong>characters</strong> of the tech’s name, then press <strong>&lt;Tab&gt;</strong> or click the down arrow button to display names drop-down list. Select a <strong>name</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Assign.</strong> The Assign Technician window closes and the Work Orders listview displays the chosen tech’s name in the Assigned Tech column.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Note:</strong> Because the listview automatically refreshes after you click Assign, the Assigned box must be checked for you to see the work order with the newly-assigned tech. If the Assigned box is not checked, the work order disappears from the listview. To see it, check the <strong>Assigned</strong> box, then click <strong>Display/Refresh</strong>.</p>
</blockquote>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Editing a Tech</td>
<td><blockquote>
<p>To change the technician on a work order that already has an assigned tech, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight the work order with an Assigned Tech, then click the <strong>Assign Tech</strong> command button. A popup window displays the following confirmation message: “This Work Order has already been assigned. Do you wish to change the assignment?”</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Yes</strong> to close the popup. The Assign Technician window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/184.png)</p>
</blockquote>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>Type a few <strong>characters</strong> of the tech’s name, then press <strong>&lt;Tab&gt;</strong> or click the down arrow button to display names drop-down list. Select a new <strong>name</strong> from the drop-down list.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Assign</strong>. The Assign Technician window closes and the Work Orders listview displays the chosen tech’s name in the Assigned Tech column.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<span id="_Toc172537426" class="anchor"></span>Managing HCPCS Items

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Adding a HCPCS Item</td>
<td><blockquote>
<p>To add a secondary HCPCS item, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Click the <strong>Add HCPCS</strong> button to add an additional HCPCS item. The OWL HCPCS Add On Item window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/185.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Type a few characters in the <strong>Billing Item</strong> dropdown list, then press <strong>&lt;Tab&gt;</strong> to select a Billing Item from the dropdown list.</p>
</blockquote></li>
<li><blockquote>
<p>Type a few characters in the <strong>HCPCS</strong> dropdown list, then press <strong>&lt;Tab&gt;</strong> to select a HCPCS code.</p>
</blockquote></li>
<li><blockquote>
<p>Optionally check the <strong>Hi-Tech Item</strong> checkbox.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Note:</strong> Hi-Tech items are HCPCS that are flagged by the user to be using high technology. The list of Hi-Tech items is provided by VACO and DVG. To obtain the latest list of approved Hi-Tech items, contact the Prosthetics and Clinical Logistics Office (10FP).</p>
</blockquote>
</blockquote>
<ol start="5" type="1">
<li><blockquote>
<p>Select the appropriate <strong>CPT Modifier</strong> radio button. This is required.</p>
</blockquote></li>
<li><blockquote>
<p>Optionally enter a brief description in the <strong>Brief Desc</strong> field.</p>
</blockquote></li>
<li><blockquote>
<p>The <strong>Qty</strong> field defaults to 1 and cannot be modified.</p>
</blockquote></li>
<li><blockquote>
<p>The <strong>Unit of Issue</strong> defaults to EA (each) and cannot be edited.</p>
</blockquote></li>
<li><blockquote>
<p>The <strong>Total cost</strong> defaults and cannot be edited.</p>
</blockquote></li>
<li><blockquote>
<p>Optionally enter a <strong>Serial Number</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Optionally type or paste text into the <strong>Extended Description</strong> field.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Quit</strong> button to close the Add On Item window without saving changes, or click <strong>Add</strong>. After you click Add, the Add On Item window closes and the HCPCS item is added to the HCPCS listview.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Editing a HCPCS Item</td>
<td><blockquote>
<p>To edit a HCPCS item, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight the row of the HCPCS item to be edited, then click <strong>Detail/Edit</strong>. The OWL HCPCS window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/186.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>You can edit the data in all fields except for the following three:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Qty</p>
</blockquote></li>
<li><blockquote>
<p>Unit of Issue</p>
</blockquote></li>
<li><blockquote>
<p>Total Cost</p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>To finish the workflow, click one of the following buttons:</p>
</blockquote></li>
</ol>
<ul>
<li><blockquote>
<p>Click <strong>Update</strong> to save all changes and close the OWL HCPCS window.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Quit</strong> to discard changes and close the OWL HCPCS window.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Delete</strong> to remove this HCPCS item from the work order.</p>
</blockquote></li>
</ul>
<blockquote>
<blockquote>
<p><em><strong>Note:</strong></em> The <strong>Delete</strong> button is disabled for the Primary HCPCS item, which can be edited but not deleted.</p>
</blockquote>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Deleting a HCPCS Item</td>
<td><blockquote>
<p>To delete a HCPCS item from the work order, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight the HCPCS item in the HCPCS listview on the OWL window, then click <strong>Detail/Edit.</strong> The Add On Item window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Note:</strong> The Delete button is disabled for Primary HCPCS items. You may only delete Add-On HCPCS items this way.</p>
</blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/187.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Click <strong>Delete.</strong> A popup window asked you to confirm the deletion.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Yes.</strong> The HCPCS item is removed from the HCPCS listview.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<span id="_Toc172537427" class="anchor"></span>HCPCS Materials

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Adding Materials for a HCPCS Item</td>
<td><blockquote>
<p>To add materials for a HCPCS item, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight an item in the HCPCS listview.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Add Material</strong> button. The OWL Material window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/188.png)</p>
</blockquote>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>Type a few letters in the <strong>Material</strong> field, then press <strong>&lt;Tab&gt;</strong> and select a material from the drop-down list. Examples: Velcro, plaster, rivets, leather.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Note:</strong> The material must be loaded in the local item file or it won’t display in the drop-down list.</p>
</blockquote>
</blockquote>
<ol start="4" type="1">
<li><blockquote>
<p>Enter a quantity in the <strong>Qty</strong> field.</p>
</blockquote></li>
<li><blockquote>
<p>Specify a <strong>Unit of Issue</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Enter a <strong>Cost.</strong></p>
</blockquote></li>
<li><blockquote>
<p>Optionally enter a <strong>Serial Number</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Optionally select a <strong>Vendor.</strong></p>
</blockquote></li>
<li><blockquote>
<p>Optionally enter <strong>Remarks.</strong></p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Add</strong>. The OWL Materials window closes and the material is added to the Materials listview. Any cost is added to the Cost field.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Updating Materials for a HCPCS Item</td>
<td><blockquote>
<p>To edit materials for a HCPCS item, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight a row in the Materials listview, then click <strong>Detail/Edit.</strong> The OWL Material window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/189.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>You can edit the data in any field on this window.</p>
</blockquote></li>
<li><blockquote>
<p>To finish the workflow, click one of the following buttons:</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Update</strong> to save all changes and close the OWL Material window.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Quit</strong> to discard changes and return to the OWL window.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Delete</strong> to remove this material from the HCPCS item.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Deleting Materials for a HCPCS Item</td>
<td><blockquote>
<p>To delete material from a HCPCS item, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight a row in the Materials listview, then click <strong>Detail/Edit.</strong> The OWL Material window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/190.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Click <strong>Delete</strong>. A confirmation pop-up window displays.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Yes</strong> to delete the material. The OWL Material window closes and the material is removed from the listview.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<span id="_Toc172537428" class="anchor"></span>HCPCS Labor

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Adding labor</td>
<td><blockquote>
<p>To add labor costs to a HCPCS item, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight an item from the HCPCS listview, then click <strong>Add Labor.</strong> The OWL Labor window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/191.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Type the first few letters of a tech’s last name, press <strong>&lt;Tab&gt;</strong>, then select a technician from the drop-down list.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Note:</strong> If only one tech name matches the letters you entered, that name is selected as soon as you press &lt;Tab&gt;, and your cursor focus moves to the Date field.</p>
</blockquote>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>Optionally change the <strong>Date</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Enter the number of <strong>Hours.</strong></p>
</blockquote></li>
<li><blockquote>
<p>Enter the hourly <strong>Rate.</strong></p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Add.</strong> The labor displays in the Labor for HCPCS listview and the labor cost is added to the Cost field.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Editing Labor</td>
<td><blockquote>
<p>To edit labor costs for a HCPCS item, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight a row in the Labor listview, then click <strong>Detail/Edit</strong>. The OWL Labor window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/192.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Edit the information as desired.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Note:</strong> Once a technician has been added, you cannot change the tech the next time you return to edit HCPCS labor. To change the technician on HCPCS labor, you must delete the labor and add it back with the correct tech.</p>
</blockquote>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>Click <strong>Update.</strong> The OWL Labor window closes and changes are saved.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Deleting Labor</td>
<td><blockquote>
<p>To delete labor costs for a HCPCS item, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight a row in the Labor listview, then click <strong>Detail/Edit</strong>. The OWL Labor window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/193.png)</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Click <strong>Delete</strong>. A confirmation pop-up window displays.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Yes</strong> to delete the labor. The OWL Labor window closes and the labor is removed from the listview.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<span id="_Toc172537429" class="anchor"></span>Printing the OWL

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Printing a Request Receipt</td>
<td><blockquote>
<p>To print a lab work order, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight the desired <strong>lab work order</strong> in the Work Orders listview.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Print OWL</strong> button. The OWL Print Lab Work Order window displays.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/194.png)</p>
</blockquote>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>The OWL will print on the printer listed in the Current Print Location field. To print to the default printer, skip to step 5. To change printers, continue with step 4.</p>
</blockquote></li>
<li><blockquote>
<p>This window provides three printer options:</p>
</blockquote>
<ul>
<li><blockquote>
<p>To select a Windows Printer, click the <strong>Windows Printer</strong> button. Select a printer from the <strong>Name</strong> drop-down list, then click <strong>OK</strong>. Proceed to step 5.</p>
</blockquote></li>
<li><blockquote>
<p>To select a VistA Printer other than the default, select a printer from the <strong>VistA Printer</strong> drop-down list. Proceed to step 5.</p>
</blockquote></li>
<li><blockquote>
<p>To select the default VistA Printer, click the <strong>Default VistA Printer</strong> button. Proceed to step 5.<br />
<strong>Note:</strong> The default VistA printer is defined in file 669.9 PROSTHETICS SITE PARAMETER.</p>
</blockquote></li>
</ul></li>
</ol>
<blockquote>
<blockquote>
<p>Depending on the Lab Type you chose when the OWL was created, the VistA printer is defined in the following field:</p>
</blockquote>
</blockquote>
<ul>
<li><blockquote>
<blockquote>
<p>Optical - 26 - EYE CLINIC LAB DEVICE</p>
</blockquote>
</blockquote></li>
<li><blockquote>
<blockquote>
<p>Orthotics/Prosthetics - 27 - ORTHOTIC LAB DEVICE</p>
</blockquote>
</blockquote></li>
<li><blockquote>
<blockquote>
<p>Restoration - 28 - RESTORATION CLINIC DEVICE</p>
</blockquote>
</blockquote></li>
<li><blockquote>
<blockquote>
<p>Wheelchair - 30 - WHEELCHAIR REPAIR SHOP DEVICE</p>
</blockquote>
</blockquote></li>
</ul>
<ol start="5" type="1">
<li><blockquote>
<p>Click <strong>Print Lab Work Order</strong>. The work order prints and the OWL Print Lab Work Order window closes.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<span id="_Toc172537430" class="anchor"></span>Completing the OWL

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Completing the OWL</td>
<td><blockquote>
<p>To complete the OWL, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight the desired <strong>lab work order</strong> in the Work Orders listview.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Complete OWL</strong> button. The OWL Complete window displays. This window displays the lab work order number, patient name, and patient SSN. It also informs you of the following three things:</p>
</blockquote>
<ul>
<li><blockquote>
<p>You are about to COMPLETE this work order.</p>
</blockquote></li>
<li><blockquote>
<p>You are about to CLOSE the original consult.</p>
</blockquote></li>
<li><blockquote>
<p>This will prevent any further OWL activities or purchasing for this work order.</p>
</blockquote></li>
</ul></li>
</ol>
<blockquote>
<blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/195.png)</p>
</blockquote>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>Optionally enter text in the <strong>Post note to CPRS</strong> field.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Complete</strong> button to complete the work order and close the original consult. A Confirm window displays.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Yes</strong> to complete this work order. A Prosthetics VistA Suite window pops up to display the following information:</p>
</blockquote></li>
</ol>
<ul>
<li><blockquote>
<p>Completed Suspense Action.</p>
</blockquote></li>
<li><blockquote>
<p>Posted note to CPRS Consult.</p>
</blockquote></li>
<li><blockquote>
<p>Suspense status has been updated to CLOSED.</p>
</blockquote></li>
</ul>
<ol start="6" type="1">
<li><blockquote>
<p>Click <strong>OK</strong> to close the Prosthetics VistA Suite window.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<span id="_Toc172537431" class="anchor"></span>Cancelling the OWL

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cancelling the OWL</td>
<td><blockquote>
<p>To cancel an OWL lab work order, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Highlight the desired <strong>lab work order</strong> in the Work Orders listview.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Cancel OWL</strong> button. The OWL Cancel window displays. (See image at the top of the next page.) This window displays the lab work order number, patient name, and patient SSN. It also informs you of the following three things:</p>
</blockquote>
<ul>
<li><blockquote>
<p>You are about to CANCEL this work order.</p>
</blockquote></li>
<li><blockquote>
<p>You are about to CLOSE the original consult.</p>
</blockquote></li>
<li><blockquote>
<p>This will prevent any further OWL activities or purchasing for this work order.</p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>Optionally enter text in the <strong>Please enter a CPRS note about this cancellation</strong> field (such as a reason for the cancellation).</p>
</blockquote></li>
<li><blockquote>
<p>To create a clone of this consult, check the box following the question <strong>Do you wish to create a CLONE of this consult for future use?</strong><br />
<strong>Note:</strong> You may wish to clone a consult in the event that you need to make another purchase on the closed consult.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Cancel Work Order</strong> button. A confirmation window pops up to display the question Are you sure you wish to CANCEL this Work Order?</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Yes</strong> to cancel the work order. A Prosthetics VistA Suite window pops up to display the following information:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Complete Suspense Action.</p>
</blockquote></li>
<li><blockquote>
<p>Posted note to CPRS Consult.</p>
</blockquote></li>
<li><blockquote>
<p>Suspense status has been updated to CANCELLED.</p>
</blockquote></li>
</ul></li>
</ol>
<ol start="7" type="1">
<li><blockquote>
<p>Click <strong>OK</strong> to close the Prosthetics VistA Suite window.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>OWL Cancel window</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/196.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537432" class="anchor"></span>Closing the OWL

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Closing the OWL</td>
<td><blockquote>
<p>To exit the OWL window, click the <strong>Close</strong> button in the lower-right corner of the window. The OWL window closes and you return to the Prosthetics Main Menu.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/197.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537433" class="anchor"></span>Appendix A

<span id="_Toc89754798" class="anchor"></span>Getting Help

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>F1 Key</td>
<td><blockquote>
<p>Online Help can be accessed in three methods:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Click the <strong>Help</strong> Menu (located in the upper left corner of the menu bar) and the <strong>Contents</strong> option.</p>
</blockquote></li>
<li><blockquote>
<p>Press the <strong>&lt;F1&gt;</strong> key.</p>
</blockquote></li>
<li><blockquote>
<p>Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;H&gt;</strong> key. (This activates the <strong>Help</strong> Menu, not the Billing contents.)</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Help Menu</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/198.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc44299392" class="anchor"></span>

Appendix B

<span id="_Toc172537436" class="anchor"></span>Using the Menus

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menus</td>
<td><blockquote>
<p>Below are the different menus and menu options that are available to be used instead of the corresponding buttons. You can use these menu options alternatively.</p>
<p>The <strong>Help</strong> Menu is the only menu that does not have a corresponding button. This menu leads you to online help through the <strong>Contents</strong> option. The <strong>Section 508</strong> option is described more in Appendix B.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File Menu</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/199.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select and Display Menu</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/200.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Menu</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/201.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Help Menu</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/202.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537437" class="anchor"></span>Appendix C

<span id="_Toc89754800" class="anchor"></span>Activate Section 508 Assistance

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>You can change the colors of the screen to black/white, which is required for Section 508 requirements to be read by visually and hearing impaired veterans.</p>
<p>This feature can be updated from the <strong>Help</strong> Menu. It provides a toggle to go back and forth between using the colors or the black/white screens depending on your needs.</p>
</blockquote></td>
</tr>
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
<p>To activate the Section 508 assistance, follow these steps:</p>
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
<td><p>Click the <strong>Help</strong> Menu, and click the <strong>Section 508</strong> option.</p>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/203.png)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Ctrl&gt;</strong> key + <strong>&lt;S&gt;</strong> key.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Click <strong>OK</strong> on the confirmation message dialog box as shown below.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Click <strong>OK</strong> again to exit out of the system and restart to activate the changes.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Confirmation message</td>
<td><blockquote>
<p>![](prosthetics-version-3-vista-suite-gui-user-manual-updated-rmpr-3-136/204.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>