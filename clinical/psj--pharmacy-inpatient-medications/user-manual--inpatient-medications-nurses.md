---
consolidated_title: "inpatient medications nurse's user manual"
app_code: PSJ
doc_type: UM
master_source: "Inpatient Medications Nurse's User Manual (PSJ*5*423)"
master_pub_date: December 1997
consolidated_from: 4 versions
prior_versions:
  - "Inpatient Medications Nurse's User Manual (PSJ*5*447)"
  - "Inpatient Medications Nurse's User Manual (updated PSJ*5*364)"
  - "Inpatient Medications Nurse's User Manual (updated PSJ*5*399)"
---

![](inpatient-medications-nurse-s-user-manual-psj-5-423/001.png)

INPATIENT MEDICATIONS

####### NURSE’S USER MANUAL

December 1997

(Revised May 2025)

Enterprise Program Management Office  
*(This page included for two-sided copying.)*

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Orientation](#orientation)
- [List Manager](#list-manager)
  - [Using List Manager](#using-list-manager)
  - [Hidden Actions](#hidden-actions)
- [Order Options](#order-options)
  - [Order Entry](#order-entry)
  - [Non-Verified/Pending Orders](#non-verifiedpending-orders)
    - [Display of Discontinued or Edited IV Orders](#display-of-discontinued-or-edited-iv-orders)
  - [Inpatient Order Entry](#inpatient-order-entry)
  - [PADE Main Menu Option](#pade-main-menu-option)
  - [Patient Actions](#patient-actions)
    - [Patient Record Update](#patient-record-update)
    - [New Order Entry](#new-order-entry)
    - [Detailed Allergy/ADR List](#detailed-allergyadr-list)
    - [View Profile](#view-profile)
    - [Patient Information](#patient-information)
    - [Select Order](#select-order)
  - [Order Actions](#order-actions)
    - [Discontinue](#discontinue)
    - [Edit](#edit)
    - [IV Bag/Label Parameters](#iv-baglabel-parameters)
    - [Verify](#verify)
    - [Hold](#hold)
    - [Renew](#renew)
    - [Activity Log](#activity-log)
    - [Finish](#finish)
    - [Flag](#flag)
    - [Speed Actions](#speed-actions)
  - [Discontinue All of a Patient’s Orders](#discontinue-all-of-a-patients-orders)
  - [Hold All of a Patient’s Orders](#hold-all-of-a-patients-orders)
  - [Inpatient Profile](#inpatient-profile)
  - [Order Checks](#order-checks)
    - [Clinic Orders](#clinic-orders)
    - [Order Validation Checks](#order-validation-checks)
    - [Display of Provider Overrides and Pharmacist Interventions](#display-of-provider-overrides-and-pharmacist-interventions)
    - [Dosing Order Checks](#dosing-order-checks)
  - [Check Drug Interactions](#check-drug-interactions)
  - [Pharmacy - Edit Clinic Med Orders Start Date/Time](#pharmacy-edit-clinic-med-orders-start-datetime)
    - [Search Med Orders Date Entry](#search-med-orders-date-entry)
    - [Search by Clinic, Clinic Group or Patient](#search-by-clinic-clinic-group-or-patient)
    - [Select Patient from Clinic](#select-patient-from-clinic)
    - [View Patient Clinic Order Entry Profile](#view-patient-clinic-order-entry-profile)
    - [Entering a New Start Date/Time](#entering-a-new-start-datetime)
    - [Order Entry View with New Start Date](#order-entry-view-with-new-start-date)
    - [New Start Date Update Confirmation](#new-start-date-update-confirmation)
    - [Conditional Messages Displaying after New Start Date](#conditional-messages-displaying-after-new-start-date)
    - [Conditional Messages Displaying after Selection of Orders](#conditional-messages-displaying-after-selection-of-orders)
- [Maintenance Options](#maintenance-options)
  - [Edit Inpatient User Parameters](#edit-inpatient-user-parameters)
  - [Edit Patient’s Default Stop Date](#edit-patients-default-stop-date)
- [Output Options](#output-options)
  - [PAtient Profile (Unit Dose)](#patient-profile-unit-dose)
  - [Reports Menu](#reports-menu)
    - [Hour MAR](#hour-mar)
    - [Day MAR](#day-mar)
    - [Day MAR](#day-mar-1)
    - [Action Profile \#1](#action-profile-1)
    - [Action Profile \#2](#action-profile-2)
    - [AUthorized Absence/Discharge Summary](#authorized-absencedischarge-summary)
    - [Extra Units Dispensed Report](#extra-units-dispensed-report)
    - [Free Text Dosage Report](#free-text-dosage-report)
    - [INpatient Stop Order Notices](#inpatient-stop-order-notices)
    - [Medications Due Worksheet](#medications-due-worksheet)
    - [OTP Medication Dispense Report](#otp-medication-dispense-report)
    - [Patient Profile (Extended)](#patient-profile-extended)
  - [Align Labels (Unit Dose)](#align-labels-unit-dose)
  - [Label Print/Reprint](#label-printreprint)
- [Inquiries Options](#inquiries-options)
  - [Dispense Drug Look-Up](#dispense-drug-look-up)
  - [Standard Schedules](#standard-schedules)
- [CPRS Order Checks: How They Work](#cprs-order-checks-how-they-work)
  - [CPRS Order Checks Introduction](#cprs-order-checks-introduction)
  - [Order Check Data Caching](#order-check-data-caching)
- [Error Messages](#error-messages)
  - [Error Information](#error-information)
- [Glossary](#glossary)
- [Index](#index)
- [14 Day MAR Report, 171, 172](#14-day-mar-report-171-172)
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch Number</th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>05/2025</td>
<td>Title, 201, 202</td>
<td>PSJ*5*423</td>
<td><ul>
<li><p>Updated <u>Error Information</u> section with new <u>Drug</u> and <u>System</u> error messages</p></li>
</ul></td>
</tr>
<tr class="even">
<td>03/2025</td>
<td><a href="#OTP_1">xi</a>, <a href="#OTP_Med_report">157</a>, <a href="#otp-medication-dispense-report">191</a></td>
<td>PSJ*5*445</td>
<td><ul>
<li><p>Added OTP Medication Dispense Report to the <a href="#OTP_1">Menu Tree</a>, Reports Menu <a href="#OTP_Med_report">options</a> and <a href="#otp-medication-dispense-report">descriptions</a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>06/2023</td>
<td>Title, <a href="#p42_NewPersonFile">42</a></td>
<td>PSJ*5*372</td>
<td><ul>
<li><p>Added <u>NEW PERSON file (#200)</u> Order Entry Provider DEA check to <strong>“PROVIDER:”</strong> (Regular and Abbreviated) section</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, Index, and Footers</p></li>
</ul></td>
</tr>
<tr class="even">
<td>03/2023</td>
<td>Title, i, 25, 204</td>
<td>PSJ*5*407</td>
<td><ul>
<li><p>Added Coverage Times <strong><u>Note</u></strong> in the Inpatient Order Entry section</p></li>
<li><p>Added Coverage Times <strong><u>Note</u></strong> in the Glossary section</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, Index, and Footers</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>09/2022</td>
<td>Title, <a href="#Indication_field_New_ord_entry">40</a>, <a href="#Indication_New_Order_Entry_Note">43</a>, <a href="#indication_New_Order_Entry">44</a>, <a href="#Indication_field_New_ord_IV">51</a>-<a href="#BCMAPATIENT_EIGHTEEN">52</a>, <a href="#Indication_Example_New_Ord_entry_note">55</a>, <a href="#Indication_Example_New_Ord_entry">57</a></td>
<td>PSJ*5*399</td>
<td><p>Added a definition of the <a href="#Indication_field_New_ord_entry">Indication field under Unit Dose New Order Entry</a>.</p>
<p>Updated the following for the Unit Dose New Order Entry screenshot:</p>
<ul>
<li><p>Added a <a href="#Indication_New_Order_Entry_Note">note</a> that explains why the Indication field displays differently.</p></li>
<li><p>Added the <a href="#Indication_New_Order_Entry">Indication</a> field.</p></li>
</ul>
<p><a href="#Indication_field_New_ord_IV">Added a definition for the Indication field for IV New Order Entry</a>. Changed the name of a patient from BCMA,EIGHTEEN-PATIENT to <a href="#BCMAPATIENT_EIGHTEEN">BCMAPATIENT,EIGHTEEN</a> on all screenshots in the “Indication” section.</p>
<p>Updated the following for the IV New Order Entry screenshot:</p>
<ul>
<li><p>Added a <a href="#Indication_Example_New_Ord_entry_note">note</a> that explains why the Indication field displays differently.</p></li>
<li><p>Added the <a href="#Indication_Example_New_Ord_entry">Indication</a> field.</p></li>
</ul>
<p>Updated dates on Title page and footer</p></td>
</tr>
<tr class="even">
<td>07/2021</td>
<td><p>41-44</p>
<p>72-73</p>
<p>79-80</p></td>
<td>PSJ*5*364</td>
<td><p>Updated 4.5.2 <a href="#New_Order_Entry4">New Order Entry</a> example with hazardous medication warning message.</p>
<p>Updated 4.6.2 <a href="#P73_EditanOrder1">Edit example</a> with hazardous medication warning message</p>
<p>Updated 4.6.3 <a href="#Page_75A">Verify example</a> with hazardous medication warning message.</p>
<p>Updated footer</p></td>
</tr>
<tr class="odd">
<td>09/2020</td>
<td><p><a href="#P5">5</a>, <a href="#P10">10</a>, <a href="#P15">15</a>, <a href="#P21">21 –</a> <a href="#P23">23</a>, <a href="#P55">55</a> – <a href="#P62">62</a>, <a href="#P64">64</a>-<a href="#Revision_History">66</a>, <a href="\l">72</a>, <a href="#P82">81</a>, <a href="#P89">89</a>, <a href="#P99">99</a>, <a href="#P102">102</a>, <a href="#P107">107</a>, <a href="#P110">110</a>, <a href="#P113">113</a>, <a href="#P119">119</a>, <a href="#P124">124</a></p>
<p><a href="#Enter_CM_Clinic_Order">33</a></p>
<p><a href="#P61">61</a></p>
<p><a href="#P127">127</a></p>
<p><a href="#CM_New_Clinic_Medication_Entry">195</a></p></td>
<td>PSJ*5*319</td>
<td><p>Added CM to all applicable screen captures.</p>
<p>Added a description for <a href="#Enter_CM_Clinic_Order">Entering a new CM Clinic Medication order</a>, revised the menu items, and put them into traditional VistA format.</p>
<p>Removed the duplicate CM New Clinic Medication Entry from the <a href="#Example_Profile_View">Example: Profile View</a>.</p>
<p><a href="#clinic-orders">Clinic Orders</a>: Removed the statement about backdoor inpatient medications, added a description of PSJ_5_319 and updated the example of a CM New Clinic Medication Entry.</p>
<p>Added <a href="#CM_New_Clinic_Medication_Entry">CM New Clinic Medication Entry</a> to Glossary/Patient Order Action Prompts.</p>
<p>Global: removed all instances of “New clinic orders cannot be created.” Updated title page and footers for month and year.</p>
<p>(J. Morrison, Dev; R. Payne, SQA; C. Bernier, J. Callahan, TWs)</p></td>
</tr>
<tr class="even">
<td>8/2020</td>
<td><p><a href="#Rules_for_StopDateTime_Calc">40</a>, <a href="#Stop_Date_Time">51</a></p>
<p>Global</p></td>
<td>PSJ*5*388</td>
<td><p>Updated <a href="#Rules_for_StopDateTime_Calc">Stop Date/Time text</a> and added a reference to the Technical Manual for more detail of the rules for Stop Date/Time calculation.</p>
<p>Revised dates on Title page and in footers</p>
<p>(S.Suiters, VA PM; J. Niksich, PM; C. Bernier, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>07/2019</td>
<td><p><a href="#Revision_History"><span>iv</span>-<span>x</span></a><br />
<a href="#P30">30</a></p>
<p><a href="#Index">208</a></p></td>
<td>PSJ*5*327</td>
<td><p>Updated Revision History and Table of Contents</p>
<p>Deleted note on special order checks for clozapine.</p>
<p>Updated Index.</p>
<p>(L. Behuniak; C. Mobley, J.Gulick Tech Writer)</p></td>
</tr>
<tr class="even">
<td>12/2018</td>
<td><a href="#p33">33</a>, <a href="#p40">40</a>, <a href="#p47">47</a></td>
<td>PSJ*5*366</td>
<td><p>Updated Medication Route default prompt to check defined routes for Orderable Items. Added new checks for Providers when writing medications.</p>
<p>(D. Connolly, PM, F. Perez, TW)</p></td>
</tr>
<tr class="odd">
<td>10/2018</td>
<td><a href="\l">Title</a>, <a href="#list-manager">5</a>, <a href="#Page_14">13</a>, <a href="#p019">20-21</a>, <a href="#Page_26">26-27</a>,<a href="#p040">40-42</a>,<a href="#Page_52">52-69</a>,<a href="#Page_75">75-84</a>, <a href="#p79">87-91</a>, <a href="#Page_96">96</a>, <a href="#Page_99">99</a>, <a href="\l">103-113</a>, <a href="#p122">122-125</a></td>
<td>PSJ*5*353</td>
<td><p>Updated Inpatient Order Displays</p>
<p>(G. Pickwoad, PM,E. Cook, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>09/2018</td>
<td><p>Title Page, i, vii</p>
<p>18, 20, 27, 37, 46-48, 52, 53, 55-60, 62, 63, 68-70, 72, 75, 76, 79, 80, 82, 84, 90, 93-100, 111, 113, 124-126, 135, 164, 169 and 170</p>
<p>34, 43</p>
<p>35, 43</p>
<p>18, 20, 53, 76, 90, and 135</p>
<p>20, 47, 52, 53, 57, 59, 76, 84, 90, 95, 97, 100, 111, 125, 135, 157, 167, and 169</p>
<p>70 and 131</p></td>
<td>PSJ*5*373</td>
<td><p>Updated Title Page, Revision History, and Table of Contents</p>
<p>Corrected date so year is displayed with four digits in the following options:</p>
<p>PSJI ORDER - Order Entry (IV)</p>
<p>PSJI PROFILE REPORT - Patient Profile Report (IV)</p>
<p>PSJ OE - Inpatient Order Entry</p>
<p>PSJU NE - Order Entry</p>
<p>PSJU PR - Patient Profile (Unit Dose)</p>
<p>PSJ EXTP - Patient Profile (Extended)</p>
<p>PSJ PR - Inpatient Profile</p>
<p>Added warning when entered Start Date/Time exceeds 7 days from the order’s Login Date.</p>
<p>Added warning that an entry of a stop date greater than 367 days from the start of the date of the order is not allowed.</p>
<p>Corrected alignment so Give info and Renewed info are on the same line.</p>
<p>Corrected Out-of-Aligned items in Active, Non-Active, Pending, and Renewed columns so they line up with Start/Stop status column.</p>
<p>Made formatting change (Orphan paragraph title and missing bullet).</p></td>
</tr>
<tr class="odd">
<td>02/2018</td>
<td><p>Title</p>
<p>5</p>
<p>6</p>
<p>14, 19-20, 22, 26-27, 40, 52, 54-59, 63, 69, 84, 96, 99, 138, 148, 170, 172, 174, 176, 180, 183</p>
<p>75-76</p>
<p>80</p>
<p>87-89</p>
<p>132</p>
<p>191</p></td>
<td>PSJ*5*256</td>
<td><p>Updated month/year of revision</p>
<p>Updated Inpatient List Manager Diagram</p>
<p>Updated Hidden Area information</p>
<p>Updated Patient Information Screen Displays</p>
<p>Updated Verification Action for Old Schedule Name</p>
<p>Updated Renew Action for Old Schedule Name</p>
<p>Updated Finish Action for Old Schedule Name</p>
<p>Updated Dosing Order Check section 4.10.4</p>
<p>Updated Error Message Table – added System Level Error</p></td>
</tr>
<tr class="even">
<td>02/2017</td>
<td>i-x, 23-24</td>
<td>PSJ*5*325</td>
<td><p>Updated Revision History and Table of Contents.</p>
<p>Added Section 4.2.1. Display of Discontinued or Edited IV Orders.</p>
<p>(L. Behuniak, PM; B. Thomas, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>10/2016</td>
<td><p>9</p>
<p>10</p>
<p>25</p>
<p>51</p>
<p>61</p></td>
<td>PSJ*5*317</td>
<td><p>Updated Revision History and Table of Contents</p>
<p>Added Hidden action  - ‘PD’ action.      </p>
<p>Added Drug IEN and PADE Stock Item Indicator    </p>
<p>Added section 4.1.9 PADE Main Menu Option.</p>
<p>Added PADE Stock and Ward Stock Items</p>
<p>Added Inpatient Order Entry profile -‘PD’ flag.                    </p>
<p>(S. Soldan PM; R.Walters, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>08/2016</td>
<td><p><span id="rhistory" class="anchor"></span>i-v</p>
<p>24</p>
<p>128</p></td>
<td>PSJ*5*315</td>
<td><p>Updated Revision History and Table of Contents</p>
<p>Added text for new Duration of Administration prompt to <em>Inpatient Order Entry</em> option</p>
<p>Added text for requesting additional user activity for entering specific information in the new Duration of Administration prompt</p>
<p>(D. Connolly, PM; E. Phelps, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>06/2016</td>
<td><p>i.</p>
<p>88-89</p></td>
<td>PSJ*5*313</td>
<td><p>Update Revision History and Table of Contents</p>
<p>Added language to Section 4.5.7 re changes to IV Additive and Orderable Item. Added example: Multiple items for an Orderable Item. Added Example: Multiple IV Additives for same order with multiple items attached to the Orderable Item.</p>
<p>Updated Revision History and TOC</p>
<ol type="A">
<li><p>Zak, Analyst, L. Ramos, Tech Writer)</p></li>
</ol></td>
</tr>
<tr class="even">
<td>04/2016</td>
<td><p>i,v-vi</p>
<p>19, 20,</p>
<p>28, 47,</p>
<p>56, 65,</p>
<p>66, 67</p>
<p>93, 94,</p>
<p>95, 96,</p>
<p>97, 98,</p>
<p>99, 100,</p>
<p>101, 102,</p>
<p>103, 104,</p>
<p>105, 106,</p>
<p>107, 108,</p>
<p>109, 110,</p>
<p>111, 112,</p>
<p>113, 114,</p>
<p>115, 116,</p>
<p>117, 118,</p>
<p>119, 120,</p>
<p>121, 122, 123</p>
<p>185,186</p>
<p>188, 195,</p>
<p>197</p></td>
<td>PSJ*5*281</td>
<td><p>Update Revision History</p>
<p>Update Table of Contents</p>
<p>Update screen captures</p>
<p>Add OI &amp; DD Enh Order Check</p>
<p>Moved content from sections 4.10.1 - 4.10.4 to section 4.9</p>
<p>Add Allergy Order Check</p>
<p>Add Clinical Reminders</p>
<p>Update Glossary</p>
<p>Update Index</p>
<p>(H. Cross, PM; S. Heiress, M.Danneeru,Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>05/2015</td>
<td>69</td>
<td>PSJ*5*259</td>
<td><p>Added verbiage to section 4.5.3 Verify</p>
<p>(A. Sessler, PM; G. Werner, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>03/2014</td>
<td><p>All</p>
<p>i-iv, v-vi</p>
<p>1</p>
<p>40-41</p>
<p>47</p>
<p>50, 80</p>
<p>107</p>
<p>98, 102, 163‑164</p>
<p>173, 174</p>
<p>179-181</p>
<p>100</p>
<p>85-86</p></td>
<td><p>PSJ*5*252</p>
<p>PSJ*5*297</p>
<p>Remedy Ticket #844215</p></td>
<td><p>Renumbered all pages &amp; format heading alignment</p>
<p>Update Revision History and Table of Contents</p>
<p>Added to the Related Manuals</p>
<p>Added Bottle</p>
<p>Update screen</p>
<p>Added reference to Order Checks</p>
<p>Added 4.10.4. Dosing Order Checks</p>
<p>Update or delete content</p>
<p>Update Glossary</p>
<p>Update Index</p>
<p>Updated the last paragraph</p>
<p>Added text for placing orders for CPRS Inpatient Medications</p>
<p>(C. Powell, PM; S. Heiress, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>12/2013</td>
<td>i-iv, 29, 29a-29b, 48, 48a-48d, 74m, 74x, 127, 127a-127b, 139-142</td>
<td>PSJ*5*279</td>
<td><p>Added IV Bag Logic, Infusion Rate T@0, Pre-Exchange Report, and Missing Dose Request Printer functionalities.</p>
<p>Updated Glossary and Index.</p>
<p>(R. Santos, PM; B. Thomas, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>04/2013</td>
<td>i-x, 11, 12, 13-14, 14a, 16d-16f, 74m-74x, 77, 98, 100-101, 140-141</td>
<td>PSJ*5*275</td>
<td><p>Added Clinic Orders functionality</p>
<p>(R. Singer, PM; B. Thomas, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>01/2013</td>
<td><p>i</p>
<p>v</p>
<p>5</p>
<p>vii, 9, 11</p>
<p>10, 20, 140</p>
<p>16, 16a, 16c, 26, 40, 40a, 40c, 41-42, 52, 57, 67, 71, 74a, 74c, 74d, 77, 99, 104, 106, 107, 111, 114</p>
<p>73a-73d</p>
<p>74f-74f1</p>
<p>74f2</p>
<p>124</p>
<p>125-138</p>
<p>139-142</p></td>
<td><p>PSJ*5*260,</p>
<p>PSJ*5*268</p></td>
<td><p>Updated Revision History</p>
<p>Updated Table of Contents</p>
<p>Fix text wrapping (Page 1 of 1) in screen</p>
<p>Added new option Check Drug Interaction &amp; Display Drug Allergies</p>
<p>Change label for OCI</p>
<p>Added Creatinine Clearance (CrCl) and Body Surface Area (BSA)</p>
<p>Added new section for Check Drug Interactions function</p>
<p>Added Clinic Orders information</p>
<p>Drug allergy update</p>
<p>Added Hidden Action Check Interactions &amp; Display Drug Allergies, and update OCI</p>
<p>Updated Glossary<br />
Updated Index</p>
<p>(D.McCance, PM; S. Heiress, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>09/2012</td>
<td><p>i-iii, 12, 12a-12b,<br />
14, 14a-14b, 16d-16f,<br />
24b-24d, 26-27, 27a-27b, 30, 30a-30b, 59, 59a-59b</p>
<p>131</p></td>
<td>PSJ*5*267</td>
<td><p>Added No Allergy Assessment logic</p>
<p>Updated Special Instructions/Other Print Info</p>
<p>(R. Singer, PM; B. Thomas, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>01/2012</td>
<td><p>i-iv</p>
<p>v-vi</p>
<p>10</p>
<p>20</p>
<p>23</p>
<p>35</p>
<p>47, 53, 60</p>
<p>74d</p>
<p>74f-74g</p>
<p>74k</p>
<p>74l</p>
<p>124, 127, 131, 133, 134</p>
<p>137-140</p></td>
<td>PSJ*5*254</td>
<td><p>Updated Table of Contents</p>
<p>Added Order Checks/Interventions (OCI) to “Hidden Actions” section</p>
<p>Defined OCI Indicator</p>
<p>Updated Schedule Type text</p>
<p>Updated text under Interventions Menu</p>
<p>Updated Pharmacy Interventions for Edit, Renew, and Finish orders</p>
<p>Added note to Drug-Drug Interactions</p>
<p>Added note to Drug-Allergy Interactions</p>
<p>Added “Display Pharmacist Intervention” section</p>
<p>Defined Historical Overrides/Interventions</p>
<p>Updated Glossary</p>
<p>Updated Index</p>
<p>(R. Singer, PM; C. Bernier, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>09/2011</td>
<td>65</td>
<td>PSJ*5*235</td>
<td><p>Updated ‘Note’ section regarding Expected First Dose</p>
<p>Scott PM, G. Werner Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>07/2011</td>
<td><p>Cover Page</p>
<p>i, 16</p>
<p>140</p></td>
<td>PSJ*5*243</td>
<td><p>Removed the acronym PD on Cover page</p>
<p>Update Revision History</p>
<p>Update Index</p>
<p>Revised the existing display in the <em>Non-Verified/Pending Orders</em> [PSJU VBW] option from a pure alphabetic listing of patient names, to a categorized listing by priority. Added “priority” to Index.</p>
<p>(N. Goyal, PM; E. Phelps/John Owczarzak, Tech Writers)</p></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td><p>i</p>
<p>v-vi</p>
<p>12</p>
<p>13</p>
<p>15-16d</p>
<p>18</p>
<p>20</p>
<p>26-27</p>
<p>33-34b</p>
<p>35-39</p>
<p>40-40d</p>
<p>46</p>
<p>67</p>
<p>71</p>
<p>72-73</p>
<p>74</p>
<p>74a-74c</p>
<p>74d-74f</p>
<p>74f-74g</p>
<p>105</p>
<p>119-120</p>
<p>121-122</p>
<p>123-136</p>
<p>137-140</p></td>
<td>PSJ*5*181</td>
<td><p>Updated Revision History</p>
<p>Updated Table of Contents</p>
<p>New Example: Patient Information Screen</p>
<p>New Example: Non-Verified/Pending Orders</p>
<p>Updated: Example: Short Profile, HOURS OF RECENTLY DC/EXPIRED field (#7) and INPATIENT WARD PARAMETERS file (#59.6) information, and Example: Profile.</p>
<p>Updated “Select DRUG:”</p>
<p>New Example: Dispense Drug with Possible Dosages and New Example: Dispense Drug with Local Possible Dosages</p>
<p>New Example: New Order Entry</p>
<p>New Example: New Order Entry (Clinic Location)</p>
<p>New Examples of all the New Interventions</p>
<p>Updated the View Profile and New Example: Profile View</p>
<p>New Medication Profile Discontinue Type Codes</p>
<p>New Example: Flagged Order</p>
<p>New Example: Inpatient Profile</p>
<p>Updated Order Checks</p>
<p>New Example: Local Outpatient Order Display and New Example: Remote Outpatient Order Display</p>
<p>Duplicate Therapy</p>
<p>Drug-Drug Interaction</p>
<p>CPRS Order Checks</p>
<p>Updated Example: Authorized Absence/Discharge Summary (continued)</p>
<p>CPRS Order checks: How they work</p>
<p>Error Messages</p>
<p>Glossary - fix page numbering</p>
<p>Index - new entries and fix page numbering</p>
<p>(C.Flegel, S. Heiress, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>06/2010</td>
<td><p>i-vi, 22-23, 23a-23b, 24, 24a-24b, 74a-74b, 74e-74f, 133, 136-137</p>
<p>77, 100, 103, 108-110, 112, 114</p></td>
<td>PSJ*5*113</td>
<td><p>Added new Order Validation Requirements.</p>
<p>Removed Duplicate Order Check Enhancement functionality, PSJ*5*175 (removed in a prior patch).</p>
<p>Miscellaneous corrections.</p>
<p>(R. Singer, DM, B. Thomas, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>12/2009</td>
<td><p>60a, 60b</p>
<p>vi</p></td>
<td>PSJ*5*222</td>
<td><p>Added description of warning displayed when finishing a Complex Unit Dose Order with overlapping admin times. Corrected page numbers in Table of Contents.</p>
<p>(E. Wright, PM; R. Sutton, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>07/2009</td>
<td>48</td>
<td>PSJ*5*215</td>
<td><p>When Dispense Drug is edited for an active Unit Dose, an entry is added to the activity log.</p>
<p>(G. Tucker, PM; S. B. Scudder, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>02/2009</td>
<td>125</td>
<td>PSJ*5*196</td>
<td><p>Update to IV Duration</p>
<p>(A. Scott, PM; G. Werner, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>08/2008</td>
<td>19-37, 58-59, 65, 134</td>
<td>PSJ*5*134</td>
<td><p>Inpatient Medication Route changes added, plus details on IV type changes for infusion orders from CPRS, pending renewal functions, and expected first dose changes.</p>
<p>(S. Templeton, PM; G. O’Connor, Tech Writer)</p></td>
</tr>
<tr class="even">
<td>10/2007</td>
<td><p>iv, 74a-74d</p>
<p>5, 12,<br />
16- 17, 26, 34-38,<br />
41-42,<br />
72-73</p></td>
<td><p>PSJ*5*175</p>
<p>PSJ*5*160</p></td>
<td><p>Modified outpatient header text for display of duplicate orders.</p>
<p>Added new functionality to Duplicate Drug and Duplicate Class definitions.</p>
<p>Modifications for remote allergies, to ensure all allergies are included when doing order checks using VA Drug Class; Analgesic order checks match against specific class only; check for remote data interoperability performed when entering patient’s chart; and list of remote allergies added to Patient Information screen.</p>
<p>(R. Singer, PM; E. Phelps/C. Varney, Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>07/2007</td>
<td>79a-79b,<br />
86a-86b, 92a-92b</td>
<td>PSJ*5*145</td>
<td><p>On 24-Hour, 7-Day, and 14-Day MAR Reports, added prompt to include Clinic Orders when printing by Ward or Ward Group. Also added prompt to include Ward Orders when printing by Clinic or Clinic Group.</p>
<p>(R. Singer, PM; E. Phelps, Tech. Writer)</p></td>
</tr>
<tr class="even">
<td>05/2007</td>
<td>24</td>
<td>PSJ*5*120</td>
<td><p>Modified Inpatient Medications V. 5.0 to consider the duration the same way as all other stop date parameters, rather than as an override.</p>
<p>(R. Singer, PM; E. Phelps, Tech. Writer)</p></td>
</tr>
<tr class="odd">
<td>12/2005</td>
<td><p>1,</p>
<p>73-74b</p></td>
<td>PSJ*5*146</td>
<td><p>Remote Data Interoperability (RDI) Project: Removed document revision dates in Section 1. Introduction. Updated Section 4.9. Order Checks, to include new functionality for remote order checking.</p>
<p>(E. Williamson, PM; M. Newman, Tech. Writer)</p></td>
</tr>
<tr class="even">
<td>01/2005</td>
<td>All</td>
<td>PSJ*5*111</td>
<td><p>Reissued entire document to include updates for Inpatient Medications Orders for Outpatients and Non-Standard Schedules.</p>
<p>(S. Templeton, PM, R. Singer, PM, M. Newman, Tech. Writer)</p></td>
</tr>
</tbody>
</table>
<span id="pTOC" class="anchor"></span>Table of Contents
Since the documentation is arranged in a topic oriented format and the screen options are not, a menu tree is provided below for the newer users who may need help finding the explanations to the options.Menu Tree Topic-Oriented Section
Align Labels (Unit Dose) Output Options
Discontinue All of a Patient's Orders Order Options
EUP Edit Inpatient User Parameters Maintenance Options
Hold All of a Patient's Orders Order Options
IOE Inpatient Order Entry Order Options
IPF Inpatient Profile Order Options
Check Drug Interaction Order Options
INQuiries Menu… Inquiries Option
Dispense Drug Look-Up Inquiries Option
Standard Schedules Inquiries Option
Label Print/Reprint Output Options
Non-Verified/Pending Orders Order Options
Order Entry Order Options
PAtient Profile (Unit Dose) Output Options
Reports Menu… Output Options
24 Hour MAR Output Options
7 Day MAR Output Options
14 Day MAR Output Options
Action Profile \#1 Output Options
Action Profile \#2 Output Options
AUthorized Absence/Discharge Output Options
Summary
Extra Units Dispensed Report Output Options
Free Text Dosage Report Output Options
INpatient Stop Order Notices Output Options
Medications Due Worksheet Output Options
<span id="OTP_1" class="anchor"></span>OTP Medication Dispense Report Output Options
Patient Profile (Extended) Output Options
*(This page included for two-sided copying.)*

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications package provides a method of management, dispensing, and administration of inpatient drugs within the hospital. Inpatient Medications combines clinical and patient information that allows each medical center to enter orders for patients, dispense medications by means of Pick Lists, print labels, create Medication Administration Records (MARs), and create Management Reports. Inpatient Medications also interacts with the Computerized Patient Record System (CPRS) and the Bar Code Medication Administration (BCMA) packages to provide more comprehensive patient care.

This user manual is written for the Nursing Staff, the Automated Data Processing Application Coordinator (ADPAC), and other healthcare staff for managing, dispensing, and administering medications to the patients within the hospital. The main text of the manual outlines patients’ ordering options for new and existing orders, editing options, output options, and inquiry options.

The Inpatient Medications documentation is comprised of several manuals. These manuals are written as modular components and can be distributed independently and are listed below.

Nurse’s User Manual V. 5.0

Pharmacist’s User Manual V. 5.0

Supervisor’s User Manual V. 5.0

Technical Manual/Security Guide V. 5.0

Pharmacy Ordering Enhancements (POE) Phase 2 Release Notes V. 1.0

Pharmacy Ordering Enhancements (POE) Phase 2 Installation Guide V. 1.0

Dosing Order Check User Manual

VistA to MOCHA Interface Document

*(This page included for two-sided copying.)*

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

> Example: *Inpatient Order Entry* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them.

> Example: “Select DRUG:” indicates a screen prompt.

- Responses in bold face indicate what the user is to type in.

> Example: Printing a MAR report by group (G), by ward (W), clinic (C), or patient (P).

- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.  
  Example: Press \<Tab\> to move the cursor to the next field.

> Press \<Enter\> to select the default.

- Text depicted with a black background, displayed in a screen capture, designates reverse video or blinking text on the screen.  
  Example:

> \(9\) Admin Times: 01-09-15-20

> \*(10) Provider: PSJPHARMACIST,ONE

- ![](inpatient-medications-nurse-s-user-manual-psj-5-423/002.png)Note: Indicates especially important or helpful information.
- ![](inpatient-medications-nurse-s-user-manual-psj-5-423/003.png) Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.

> Example: ![](inpatient-medications-nurse-s-user-manual-psj-5-423/004.png)When the nurse holds the PSJ RNURSE key, it will be possible to take any available actions on selected Unit Dose or IV orders and verify non-verified orders.

- Some of the menu options have several letters that are capitalized. By entering in the letters and pressing \<Enter\>, the user can go directly to that menu option (the letters do not have to be entered as capital letters).

Example: From the *Unit Dose Medications* option: the user can enter INQ and proceed directly into the *INQuiries Menu* option.

- ?, ??, ??? One, two, or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.
- ^ Caret (up arrow or a circumflex) and pressing \<Enter\> can be used to exit the current option.

# List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new screen, which was designed using List Manager, has dramatically changed from the previous version.

This new screen will give the user:

- More pertinent information
- Easier accessibility to vital reports and areas of a patient’s chart the user may

> wish to see.

Please take the time to read over the explanation of the screen and the actions that can now be executed at the touch of a button. This type of preparation before using List Manager is effective in saving time and effort.

Inpatient List Manager

![](inpatient-medications-nurse-s-user-manual-psj-5-423/005.png)

<span id="P5" class="anchor"></span>

\* Crises, Warnings, Allergies, and Directives (CWAD)  
Screen Title: The screen title changes according to what type of information List Manager is displaying (e.g., Patient Information, Non-Verified Order, Inpatient Order Entry, etc.).

CWAD Indicator: This indicator will display when the crises, warnings, allergies, and directives information has been entered for the patient. (This information is entered via the Text Integration Utilities (TIU) package.) When the patient has Allergy/Adverse Drug Reaction (ADR) data defined, an “\<A\>” is displayed to the right of the ward location to alert the user of the existence of this information.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/006.png)Note: This data may be displayed using the Detailed Allergy/ADR List action). Crises, warnings, and directives are displayed respectively, “\<C\>”,“\<W\>”,“\<D\>”. This data may be displayed using the CWAD hidden action. Any combination of the four indicators can display.

Header Area: The header area is a “fixed” (non-scrollable) area that displays the patient’s demographic information. This also includes information about the patient’s current admission. The status and type of order are displayed in the top left corner of the heading, and will include the priority (if defined) for pending orders. The most recent height and weight for the patient and the date it was taken is displayed. The most recent information added is an estimated Creatinine Clearance (CrCL), the most recent serum Creatinine and date taken along with a calculated Body Surface Area (BSA) if height and weight are available.

List Area: (scrolling region): This is the section that will scroll (like the previous version) and display the information that an action can be taken on. The Allergies/Reactions line includes non-verified and verified Allergy/ADR information as defined in the Allergy package. The allergy data is sorted by type (DRUG, OTHER, FOOD). If no data is found for a category, the heading is displayed as “Allergies/Reactions: No Allergy Assessment”. The Inpatient and Outpatient Narrative lines may be used by the inpatient pharmacy staff to display information specific to the current admission for the patient.

Message Window: This section displays a plus sign (+), if the list is longer than one screen, and informational text (i.e., Enter ?? for more actions). If the plus sign is entered at the action prompt, List Manager will “jump” forward to the next screen. The plus sign is only a valid action if it is displayed in the message window.

Action Area: The list of valid actions available to the user display in this area of the screen. If a double question mark (??) is entered at the “Select Action:” prompt, a “hidden” list of additional actions that are available will be displayed.

## Using List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List Manager is a tool designed so that a list of items can be presented to the user for an action.

- For Inpatient Medications, the List Manager gives the user the following:
- Capability to browse through a list of orders.
- Capability to take action(s) against those items.
- Capability to print MARs, labels, and profiles from within the *Inpatient Order Entry* option.
- Capability to select a different option than the option being displayed.

## Hidden Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A double question mark (??) can be entered at the “Select Action:” prompt for a list of all actions available. Typing the name(s) or synonym(s) at the “Select Action:” prompt enters the actions.

The following is a list of generic List Manager actions with a brief description. The synonym for each action is shown, followed by the action name and description.

| <u>Synonym</u> | <u>Action</u>         | <u>Description</u>                                                      |
|----------------|-----------------------|-------------------------------------------------------------------------|
| \+             | Next Screen           | Moves to the next screen                                                |
| \-             | Previous Screen       | Moves to the previous screen                                            |
|                |                       |                                                                         |
| UP             | Up a Line             | Moves up one line                                                       |
| DN             | Down a line           | Moves down one line                                                     |
|                |                       |                                                                         |
| FS             | First Screen          | Moves to the first screen                                               |
| LS             | Last Screen           | Moves to the last screen                                                |
| GO             | Go to Page            | Moves to any selected page in the list                                  |
| RD             | Re Display Screen     | Redisplays the current screen                                           |
| PS             | Print Screen          | Prints the header and the portion of the list currently displayed       |
|                |                       |                                                                         |
| PT             | Print List            | Prints the list of entries currently displayed                          |
| SL             | Search List           | Finds selected text in list of entries                                  |
| Q              | Quit                  | Exits the screen                                                        |
| ADPL           | Auto Display (On/Off) | Toggles the menu of actions to be displayed/not displayed automatically |
| \>             | Shift View to Right   | Shifts the view on the screen to the right                              |
| \<             | Shift View to Left    | Shifts the view on the screen to the left                               |

The following is a list of Inpatient Medications specific hidden actions with a brief description. The synonym for each action is shown followed by the action name and description.

| <u>Synonym</u> | <u>Action</u>                 | <u>Description</u>                                                                                                        |
|----------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| MAR            | MAR Menu                      | Displays the *MAR Menu*                                                                                                   |
| 24             | 24 Hour MAR                   | Shows the 24 Hour MAR                                                                                                     |
| 7              | 7 Day MAR                     | Shows the 7 Day MAR                                                                                                       |
| 14             | 14 Day MAR                    | Shows the 14 Day MAR                                                                                                      |
| MD             | Medications Due Worksheet     | Shows the Worksheet                                                                                                       |
|                |                               |                                                                                                                           |
| LBL            | Label Print/Reprint           | Displays the *Label Print/Reprint Menu*                                                                                   |
| ALUD           | Align Labels (Unit Dose)      | Aligns the MAR label stock on a printer                                                                                   |
| LPUD           | Label Print/Reprint           | Allows print or reprint of a MAR label                                                                                    |
| ALIV           | Align Labels (IV)             | Aligns the IV bag label stock on a printer                                                                                |
| ILIV           | Individual Labels (IV)        | Allows print or reprint of an IV bag label                                                                                |
| SLIV           | Scheduled Labels (IV)         | Allows print of the scheduled IV bag label                                                                                |
| RSIV           | Reprint Scheduled Labels (IV) | Allows reprint of scheduled IV bag labels                                                                                 |
|                |                               |                                                                                                                           |
| OTH            | Other Pharmacy Options        | Displays more pharmacy options                                                                                            |
| PIC            | Pick List Menu                | Displays the *Pick List Menu*                                                                                             |
| EN             | Enter Units Dispensed         | Allows entry of the units actually dispensed for a Unit Dose order                                                        |
| EX             | Extra Units Dispensed         | Allows entry of extra units dispensed for a Unit Dose order                                                               |
| PL             | Pick List                     | Creates the Pick List report                                                                                              |
| RRS            | Report Returns                | Allows the entry of units returned for a Unit Dose order                                                                  |
|                |                               |                                                                                                                           |
| RPL            | Reprint Pick List             | Allows reprint of a pick list                                                                                             |
| SND            | Send Pick list to ATC         | Allows a pick list to be sent to the ATC (Automated Tablet Counter)                                                       |
| UP             | Update Pick List              | Allows an update to a pick list                                                                                           |
|                |                               |                                                                                                                           |
| RET            | Returns/Destroyed Menu        | Displays the Returns/Destroyed options                                                                                    |
| RR             | Report Returns                | Allows entry of units returned for a Unit Dose order                                                                      |
| RD             | Returns/Destroyed Entry (IV)  | Allows entry of units returned or destroyed for an order                                                                  |
|                |                               |                                                                                                                           |
| PRO            | Patient Profiles              | Displays the *Patient Profile Menu*                                                                                       |
| IP             | Inpatient Medications Profile | Generates an Inpatient Profile for a patient                                                                              |
| IV             | IV Medications Profile        | Generates an IV Profile for a patient                                                                                     |
| UD             | Unit Dose Medications Profile | Generates a Unit Dose Profile for a patient                                                                               |
| OP             | Outpatient Prescriptions      | Generates an Outpatient Profile for a patient                                                                             |
| AP1            | Action Profile \#1            | Generates an Action Profile \#1                                                                                           |
| AP2            | Action Profile \#2            | Generates an Action Profile \#2                                                                                           |
| EX             | Patient Profile (Extended     | Generates an Extended Patient Profile                                                                                     |
| CWAD           | CWAD Information              | Displays the crises, warnings, allergies, and directives information on a patient                                         |
| DA             | Display Drug Allergies        | Displays signs/symptoms of an allergy associated to a med order                                                           |
| CK             | Check Interaction             | Allows a user to perform order checks against the patient’s active medication profile with or without a prospective drug. |

The following actions are available while in the Unit Dose Order Entry Profile.

| <u>Synonym</u> | <u>Action</u>     | <u>Description</u>                                                                                                           |
|----------------|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| DC             | Speed Discontinue | Speed discontinue one or more orders (This is also available in the *Inpatient Order Entry* and *Order Entry (IV) options.*) |
| RN             | Speed Renew       | Speed renewal of one or more orders                                                                                          |
| SF             | Speed Finish      | Speed finish one or more orders                                                                                              |
| SV             | Speed Verify      | Speed verify one or more orders                                                                                              |

The following actions are available while viewing an order.

| <u>Synonym</u> | <u>Action</u>                          | <u>Description</u>                                                                                                                                                                                                                      |
|----------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CO             | Copy an order                          | Allows the user to copy an active, discontinued, or expired Unit Dose order                                                                                                                                                             |
| DIN            | Drug Restriction/Guideline Information | Displays the Drug Restriction/Guideline Information for both the Orderable Item and Dispense Drug                                                                                                                                       |
| I              | Mark Incomplete                        | Allows the user to mark a Non-Verified Pending order incomplete                                                                                                                                                                         |
| JP             | Jump to a Patient                      | Allows the user to begin processing another patient                                                                                                                                                                                     |
| N              | Mark Not to be Given                   | Allows the user to mark a discontinued or expired order as not to be given                                                                                                                                                              |
| OCI            | Overrides/Interventions                | Indicates there are associated CPRS Overrides and/or Pharmacist Interventions. When the OCI displays on the Order Detail screen, the user can type “OCI” to display associated CPRS Provider Overrides and/or Pharmacist Interventions. |

From the Inpatient Order Entry screen, the user can access PADE Activity via the PD action, which displays all of the PADE transactions.

Example: Hidden Action (PD PADE Activity) Inpatient Order Entry screen display

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

3 CAPTOPRIL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 75MG PO TID

4 LEVOTHYROXINE TAB ? \*\*\*\*\* \*\*\*\*\* P WS

Give: 0.025MG BY MOUTH \*Q8H

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

<span id="P10" class="anchor"></span>CM New Clinic Medication Entry

Enter RETURN to continue or '^' to exit:

The following actions are also available:

\+ Next Screen PS Print Screen OTH Other Pharmacy Options

\- Previous Screen PT Print List DC Speed Discontinue

UP Up a Line SL Search List RN Speed Renew

DN Down a Line Q Quit SF Speed Finish

FS First Screen ADPL Auto Display(On/Off) SV Speed Verify

LS Last Screen MAR MAR Menu CWAD CWAD Information

GO Go to Page LBL Label Print/Reprint CK Check Interactions

RD Re Display Screen JP Jump to a Patient IN Intervention Menu

PD PADE Activity

Enter RETURN to continue or '^' to exit:

Drug IEN and PADE Stock Item Indicator

From Hidden Actions, and from the VistA Pick List, the user can view the drug name from the drug Internal Entry Number (IEN) field.

Also, if the medication listed is a PADE stock item, the word “PADE” will be added to the VistA Pick List report.

Example: Pick List with Drug IEN and PADE stock item indicator

(106)                          PICK LIST REPORT                03/18/15  11:19

Ward group: BCMA                                                       Page: 12

                  For 03/19/15  15:01 through 03/20/15  15:00

Team: \*\* N/F \*\*

Room-Bed       Patient                                             Units  Units

         Medication                             ST            U/D Needed  Disp'd

--------------------------------------------------------------------------------

================================== WARD: BCMA ==================================

422-1       IAPATIENT,ONE  (1234):

    

ASCORBIC ACID 250MG TAB (1353) C PADE ATC 1 1 1

Give: 250MG PO DAILY

10

Start: 03/13/15 14:02 Stop: 04/12/15 14:00

--------------------------------------------------------------------------

HEPARIN 5000 UNITS/ML INJ 1ML (154) C PADE  ATC 1 WS \_\_\_\_

Give: 5000UNIT/1ML SC Q8H

06-14-22

Start: 03/13/15 14:01 Stop: 04/12/15 14:00

          

LEVOTHYROXINE 0.025MG (989)                   C   ATC 1      1   \_\_\_\_

          Give: 0.025MG BY MOUTH DAILY

                                                             0900

       Start: 03/18/15  10:25        Stop: 06/26/15  24:00

      --------------------------------------------------------------------------

MORPHINE SULFATE 10MG SYRINGE (322) P   PADE        1      2   \_\_\_\_

          Give: 10MG/1ML IV BID PRN

       Start: 03/18/15  10:26        Stop: 06/26/15  24:00

*(This page included for two-sided copying.)*

# Order Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Unit Dose Medications* option is used to access the order entry, patient profiles, and various reports, and is the main starting point for the Unit Dose system.

Example: Unit Dose Menu

Select Unit Dose Medications Option: ?

Align Labels (Unit Dose)

Discontinue All of a Patient's Orders

ECO Edit Clinic Med Orders Start Date/Time

EUP Edit Inpatient User Parameters

ESD Edit Patient's Default Stop Date

Hold All of a Patient's Orders

IOE Inpatient Order Entry

IPF Inpatient Profile

RO Act On Existing Orders

Check Drug Interaction

INQuiries Menu ...

Label Print/Reprint

Non-Verified/Pending Orders

Order Entry

PAtient Profile (Unit Dose)

PIck List Menu ...

Reports Menu ...

Within the Inpatient Medications package there are three different paths the nurse can take to enter a new order or take action on an existing order. They are (1) *Order Entry*, (2) *Non-Verified/Pending Orders* and (3) *Inpatient Order Entry*. Each of these paths differs by the prompts that are presented. Once the nurse has reached the point of entering a new order or selecting an existing order, the process becomes the same for each path.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/007.png)Note: When the selected order type (non-verified or pending) does not exist (for that patient) while the user is in the *Non-Verified/Pending Orders* option, the user cannot enter a new order or take action on an existing order for that patient.

Patient locks and order locks are incorporated within the Inpatient Medications package. When a user (User 1) selects a patient through any of the three paths, *Order Entry*, *Non-Verified/Pending Orders,* or *Inpatient Order Entry*, and this patient has already been selected by another user (User 2), the user (User 1) will see a message that another user (User 2) is processing orders for this patient. This will be a lock at the patient level within the Pharmacy packages. When the other user (User 2) is entering a new order for the patient, the user (User 1) will not be able to access the patient due to a patient lock within the VistA packages. A lock at the order level is issued when an order is selected through Inpatient Medications for any action other than new order entry. Any users attempting to access this patient’s order will receive a message that another user is working on this order. This order-level lock is within the VistA packages.

The three different paths for entering a new order or taking an action on an existing order are summarized in the following sections.

## Order Entry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU NE\]

The *Order Entry* option allows the nurse to create, edit, renew, hold, and discontinue Unit Dose orders while remaining in the Unit Dose Medications module. The *Order Entry* option functions almost identically to the *Inpatient Order Entry* option, but does not include IV orders on the profile and only Unit Dose orders may be entered or processed.

The *Order Entry* \[PSJU NE\] option also allows for processing of clinic orders. Clinic orders are displayed separately from non-clinic orders.

After selecting the *Order Entry* option from the *Unit Dose Medications* option, the nurse will be prompted to select the patient. At the “Select PATIENT:” prompt, the user can enter the patient’s name or enter the first letter of the patient’s last name and the last four digits of the patient’s social security number (e.g., P0001).

Before the Patient Information screen displays, if the patient selected has no allergy assessment on file, the following prompt displays to the pharmacist/user:

"NO ALLERGY ASSESSMENT exists for this patient! Would you like to enter one now?"

- If the pharmacist/user enters 'YES,' he/she is prompted to enter the allergy information.
- If the pharmacist/user enters 'NO,' a pharmacist intervention is created, with a type of 'NO ALLERGY ASSESSMENT.' The pharmacist/user is then prompted for Provider and Recommendation information.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/008.png)Note: If the selected patient is Sensitive, Discharged, both Sensitive and Discharged, or Deceased, there are variations in the Order Entry process and in the prompts that display to the pharmacist/user.

<span id="Page_14" class="anchor"></span>

Example: Pharmacist Answers ‘Yes’ and Enters Allergy Information

Select PATIENT: PSJPATIENT1, ONE

NO ALLERGY ASSESSMENT exists for this patient!

Would you like to enter one now? No// YES (Yes)

Does this patient have any known allergies or adverse reactions? : Yes

This patient has no allergy/adverse reaction data.

Enter Causative Agent: LATEX

Checking existing PATIENT ALLERGIES (#120.8) file for matches...

Now checking GMR ALLERGIES (#120.82) file for matches...

Now checking the National Drug File - Generic Names (#50.6)

Now checking the National Drug File - Trade Names (#50.67)

Now checking the INGREDIENTS (#50.416) file for matches...

...OK? Yes// Y (Yes)

LATEX OK? Yes// (Yes)

Example: Pharmacist Answers ‘No’ and Intervention is Created

Select PATIENT: PSJPATIENT1, ONE

NO ALLERGY ASSESSMENT exists for this patient!

Would you like to enter one now? No// N (No)

Now creating Pharmacy Intervention

PROVIDER:

Select one of the following:

1 UNABLE TO ASSESS

2 OTHER

RECOMMENDATION: ^

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

The Patient Information Screen is displayed:

Example: Patient Information Screen

Patient Information Feb 10, 2011@10:44:55 Page: 1 of 1

TESTYPATNM,TEST Ward: GEN MED A

PID: 666-00-0423 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 01/01/50 (61) Att: Psj,Test Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE TrSp: Medical Observati Admitted: 02/13/07

Dx: OBSERVATION Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies - Verified: PENICILLIN, ASPIRIN

Non-Verified:

Adverse Reactions:

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile <span id="P15" class="anchor"></span>CM New Clinic Medication Entry

Select Action: View Profile//

The nurse can now enter a Patient Action at the “Select Action: View Profile//” prompt in the Action Area of the screen.

## Non-Verified/Pending Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU VBW\]

The *Non-Verified/Pending Orders* option allows easy identification and processing of non-verified and/or pending orders. This option will also show pending and pending renewal orders, which are orders from CPRS that have not been finished by Pharmacy Service. Unit Dose and IV orders are displayed using this option.

The *Non-Verified/Pending Orders* \[PSJU VBW\] option also allows for processing of clinic orders. Clinic orders are displayed separately from non-clinic orders.

If this is the first time into this option, the first prompt will be: Select IV ROOM NAME. If not, then the first prompt is “Display an Order Summary? NO// ”. A YES answer will allow the nurse to view an Order Summary of Pending/Non-Verified Order Totals by Ward Group, Clinic Group, and Clinic. The Pending IV, Pending Unit Dose, Non-Verified IV, and Non-Verified Unit Dose totals are then listed by Ward Group, Clinic Group, and Clinic. The nurse can then specify whether to display Non-Verified Orders, Pending Orders or both.

A ward group indicates inpatient nursing units (wards) that have been defined as a group within Inpatient Medications to facilitate processing of orders. A clinic group is a combination of outpatient clinics that have been defined as a group within Inpatient Medications to facilitate processing of orders.

Example: Non-Verified/Pending Orders

Non-Verified/Pending Orders

Select IV ROOM NAME: TST ISC ROOM

You are signed on under the TST ISC ROOM IV ROOM

Enter IV LABEL device: HOME// COMPUTER ROOM

Enter IV REPORT device: HOME// COMPUTER ROOM

Display an Order Summary? NO// YES

Searching for Pending and Non-Verified orders...................................

Pending/Non-Verified Order Totals by Ward Group/Clinic Location

Pending Non-Verified

Ward Group/Clinic Location IV UD IV UD

Ward Groups

GEN MED 5 5 0 3

TST 1 Group 1 3 0 0

TST 3 0 2 0 0

^OTHER 5 27 1 5

Clinics

45 CLINIC PATTERN 5 0 0 0

1\) Non-Verified Orders

2\) Pending Orders

Select Order Type(s) (1-2):

![](inpatient-medications-nurse-s-user-manual-psj-5-423/009.png)Note: The Ward Group of ^OTHER includes all orders from wards that do not belong to a ward group. Use the *Ward Group Sort* option to select ^OTHER.

Next, the nurse can select which packages to display: Unit Dose Orders, IV Orders, or both, provided this user holds the PSJ RNFINISH and the PSJI RNFINISH keys. If the user holds only one of the RNFINISH keys, then either Unit Dose or IV orders will be displayed.

The next prompt allows the nurse to select non-verified and/or pending orders for a group (G), ward (W), clinic (C), patient (P), or priority (PR). When group is selected, a prompt to select by ward group (W) or clinic group (C) displays.

If ward or ward groups is selected, patients will be listed by wards, then by priority, then by teams, and then by patient name. Patients that have one or more STAT pending orders will be listed first, followed by patients with one or more ASAP pending orders, and then all other patients that have only ROUTINE pending orders. Within each priority, the patient listing is sorted alphabetically by team and then by patient name.

When priority is selected, only patients with the selected priority will display, listed by team and then by patient name.

Before the Patient Information screen displays, if the patient selected has no allergy assessment on file, the following prompt displays to the pharmacist/user:

"NO ALLERGY ASSESSMENT exists for this patient! Would you like to enter one now?"

- If the pharmacist/user enters 'YES,' he/she is prompted to enter the allergy information.
- If the pharmacist/user enters 'NO,' a pharmacist intervention is created, with a type of 'NO ALLERGY ASSESSMENT.' The pharmacist/user is then prompted for Provider and Recommendation information.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/010.png)Note: If the selected patient is Sensitive, Discharged, both Sensitive and Discharged, or Deceased, there are variations in the process and in the prompts that display to the pharmacist/user.

Example: Pharmacist Answers ‘Yes’ and Enters Allergy Information

Select PATIENT: PSJPATIENT1, ONE

NO ALLERGY ASSESSMENT exists for this patient!

Would you like to enter one now? No// YES (Yes)

Does this patient have any known allergies or adverse reactions? : Yes

This patient has no allergy/adverse reaction data.

Enter Causative Agent: LATEX

Checking existing PATIENT ALLERGIES (#120.8) file for matches...

Now checking GMR ALLERGIES (#120.82) file for matches...

Now checking the National Drug File - Generic Names (#50.6)

Now checking the National Drug File - Trade Names (#50.67)

Now checking the INGREDIENTS (#50.416) file for matches...

...OK? Yes// Y (Yes)

LATEX OK? Yes// (Yes)

Example: Pharmacist Answers ‘No’ and Intervention is Created

Select PATIENT: PSJPATIENT1, ONE

NO ALLERGY ASSESSMENT exists for this patient!

Would you like to enter one now? No// N (No)

Now creating Pharmacy Intervention

PROVIDER:

Select one of the following:

1 UNABLE TO ASSESS

2 OTHER

RECOMMENDATION: ^

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

1\) Unit Dose Orders

2\) IV Orders

Select Package(s) (1-2): 1-2

Select by GROUP (G), WARD (W), CLINIC (C), PATIENT (P), or PRIORITY (PR): PATIENT \<Enter\>

Select by WARD GROUP (W) or CLINIC GROUP (C): WARD \<Enter\>

Select PATIENT: PSJPATIENT1,ONE 000-00-0001 08/18/20 B-12 1 EAST

 

Select PATIENT: \<Enter\>

A profile prompt is displayed asking the nurse to choose a profile for the patient. The nurse can choose a short, long, or no profile. If NO profile is chosen, the orders for the patient selected will be displayed, for finishing or verification, by login date with the earliest date showing first. When a pending Unit Dose order has a STAT priority, this order will always be displayed first in the profile view and will be displayed in blinking reverse video. If a profile is chosen, the orders will be selected from this list for processing (any order may be selected). The following example displays a short profile.

Example: Short Profile

Select Unit Dose Medications Option: Non-Verified/Pending Orders

Display an Order Summary? NO// y YES

Searching for Pending and Non-Verified orders...................................

.......................................................

Pending/Non-Verified Order Totals by Ward Group/Clinic Location

Pending Non-Verified

Ward Group/Clinic Location IV UD IV UD

Ward Groups

BCMA 56 75 10 30

GEN MED 5 5 0 0

TEST AGAIN 1 18 2 4

TST 1 GROUP 1 4 0 0

TST 2 GROUP 0 10 0 0

TST 3 0 2 0 0

^OTHER 6 32 0 4

Clinics

45 CLINIC PATTERN 5 0 0 0

BARBARA'S CLINIC 1 0 0 0

BECKY'S CLINIC 1 0 0 0

1\) Non-Verified Orders

2\) Pending Orders

Select Order Type(s) (1-2): 1

1\) Unit Dose Orders

2\) IV Orders

Select Package(s) (1-2): 1

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): gROUP

Select by WARD GROUP (W) or CLINIC GROUP (C): wARD

Select WARD GROUP: bcma

PHARMACY

...a few moments, please......................................

ORDERS NOT VERIFIED BY A PHARMACIST - BCMA

No. TEAM PATIENT

--------------------------------------------------------------------------------

1 Not Found BCMA,EIGHTY-PATIENT (0080)

2 Not Found BCMA,EIGHTYEIGHT-PATIENT (0088)

3 Not Found BCMA,EIGHTYFIVE-PATIENT (0085)

4 Not Found BCMA,EIGHTYSIX-PATIENT (0086)

5 Not Found BCMA,EIGHTYTHREE-PATIENT (0083)

6 Not Found BCMA,EIGHT (0008)

7 Not Found BCMA,FIFTEEN-PATIENT (0015)

8 Not Found BCMA,FIFTYTHREE-PATIENT (0053)

9 Not Found BCMA,FIFTYTWO-PATIENT (0052)

10 Not Found BCMA,FORTYTWO-PATIENT (0042)

11 Not Found BCMA,FOUR-PATIENT (0004)

12 Not Found BCMA,FOURTEEN-PATIENT (0014)

13 Not Found BCMA,NINETY-PATIENT (0090)

14 Not Found BCMA,NINETYTWO-PATIENT (0092)

15 Not Found BCMA,ONE HUNDRED-PATIENT (0100)

16 Not Found BCMA,SEVENTYSEVEN-PATIENT (0077)

17 Not Found BCMA,SIXTEEN-PATIENT (0016)

18 Not Found BCMA,TEN-PATIENT (0010)

Select 1 - 18: 1

Do you want to print a profile for the patient? NO// y YES

SHORT, LONG, or NO Profile? SHORT// SHORT

Select PRINT DEVICE: home;80;9999 COMPUTER ROOM

I N P A T I E N T M E D I C A T I O N S 03/16/2011 10:32

VAMC: ZZ ALBANY-PRRTP (500PA)

\- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

BCMA,EIGHTY-PATIENT Ward: BCMA

PID: 666-33-0080 Room-Bed: 12-B Ht(cm): 167.64 (03/30/2009)

DOB: 04/07/1935 (75) Wt(kg): 90.00 (03/30/2009)

Sex: FEMALE Admitted: 02/07/2002

Dx: HIGH FEVER

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.05

Allergies: CODEINE, ASPIRIN, CAFFEINE, STRAWBERRIES

ADR:

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

1 ENOXAPARIN 30MG/0.3ML/SYR INJ ? \*\*\*\*\* \*\*\*\*\* N

Give: XXX SC XXX@09-13

2 MULTIVITAMINS/MINERALS TAB ? \*\*\*\*\* \*\*\*\*\* N

Give: ONE TABLET PO QAM

3 PREDNISONE TAB ? \*\*\*\*\* \*\*\*\*\* N

Give: 2000MG PO NOW

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

4 DOCUSATE NA CAP,ORAL ? \*\*\*\*\* \*\*\*\*\* P

Give: 100MG PO QAM

5 ACETAMINOPHEN TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 325MG PO Q6H

6 in CISPLATIN 250MG IN 0.9% NACL 250 ML ? \*\*\*\*\* \*\*\*\*\* P

7 in CISPLATIN 250MG IN 0.9% NACL 250 ML 10? \*\*\*\*\* \*\*\*\*\* P

8 in CISPLATIN 250MG IN 0.9% NACL 250 ML 10? \*\*\*\*\* \*\*\*\*\* P

9 in DOPAMINE 400MG/D5W 1600MCG/ML 250 ML ? \*\*\*\*\* \*\*\*\*\* P

10 in DOPAMINE IN 200ML D5W 200 ML 50MCG/KG/? \*\*\*\*\* \*\*\*\*\* P

11 HEPARIN/SODIUM CHLORIDE INJ,SOLN ? \*\*\*\*\* \*\*\*\*\* P

Give: IV CONTINUOUS DRIP

View ORDERS (1-11): 1

----------------------------------------------------------------------

Patient: BCMA,EIGHTY-PATIENT Status: NON-VERIFIED

Orderable Item: ENOXAPARIN 30MG/0.3ML/SYR INJ

Instructions:

Dosage Ordered: XXX

Duration: Start: 04/05/2010 13:00

Med Route: SUBCUTANEOUS (SC)

Stop: 07/14/2010 24:00

Schedule Type: NOT FOUND

Schedule: XXX@09-13

(No Admin Times)

Provider: PHARMACIST,ONE \[w\]

Units Units Inactive

Dispense Drugs U/D Disp'd Ret'd Date

--------------------------------------------------------------------------------

ENOXAPARIN 30MG/0.3ML INJ SYRINGE 0.3ML 1 0 0

ORDER NOT VERIFIED

Self Med: NO

Entry By: PHARMACIST,ONE Entry Date: 04/05/10 14:36

Enter RETURN to continue or '^' to exit:

Select profile type for order processing.

SHORT, LONG, or NO Profile? SHORT// SHORT

Non-Verified/Pending Orders Mar 16, 2011@10:33:08 Page: 1 of 2

BCMA,EIGHTY-PATIENT Ward: BCMA A

PID: 666-33-0080 Room-Bed: 12-B Ht(cm): 167.64 (03/30/2009)

DOB: 04/07/35 (75) Wt(kg): 90.00 (03/30/2009)

Sex: FEMALE Admitted: 02/07/2002

Dx: HIGH FEVER Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.05

--------------------------------------------------------------------------------

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

1 ENOXAPARIN 30MG/0.3ML/SYR INJ C 04/05/2010 07/14/2010 N

Give: XXX SC XXX@09-13

2 MULTIVITAMINS/MINERALS TAB C 09/21/2010 12/20/2010 N

Give: ONE TABLET PO QAM

3 PREDNISONE TAB O 09/21/2010 10/21/2010 N

Give: 2000MG PO NOW

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

4 DOCUSATE NA CAP,ORAL ? \*\*\*\*\* \*\*\*\*\* P

Give: 100MG PO QAM

5 ACETAMINOPHEN TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 325MG PO Q6H

+---------Enter ?? for more actions---------------------------------------------

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P21" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen//

The orders on the profile are sorted first by status (ACTIVE, NON-VERIFIED, NON-VERIFIED COMPLEX, PENDING RENEWALS, PENDING COMPLEX, PENDING, RECENTLY DISCONTINUED/EXPIRED), then alphabetically by SCHEDULE TYPE. Pending orders with a priority of STAT are listed first and are displayed in a bold and blinking text for easy identification. After SCHEDULE TYPE, orders are sorted alphabetically by DRUG (the drug name listed on the profile), and then in descending order by START DATE.

Example: Short Profile

Inpatient Order Entry Jun 12, 2006@23:12:54 Page: 1 of 1

PSJPATIENT11, ONE Ward: 2ASM

PID: 000-55-3421 Room-Bed: 102-1 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 12/02/23 (82) Wt(kg): 100.00 (06/24/03)

Sex: MALE Admitted: 12/11/01

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_

Dx: HE IS A PAIN. Last transferred: 12/11/01

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 CEFAZOLIN 1 GM C 06/12/2006 06/22/2006 H

in 5% DEXTROSE 50 ML Q8H

2 CIMETIDINE TAB C 06/12/2006 07/12/2006 A

Give: 300MG PO BID

3 FUROSEMIDE TAB C 06/01/2006 06/15/2006 HP

Give: 40MG PO QAM

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

4 CAPTOPRIL TAB C 06/14/2006 06/28/2006 N

Give: 25MG PO BID

\- - - - - - - - - - - - P E N D I N G R E N E W A L S - - - - - - - - - - - -

5 HALOPERIDOL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 5MG PO BID Renewed 06/14/2006

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

6 HEPARIN/DEXTROSE INJ,SOLN ? \*\*\*\*\* \*\*\*\*\* P

Give: IV

7 LACTULOSE SYRUP ? \*\*\*\*\* \*\*\*\*\* P NF

Give: 10GM/15ML PO BID PRN

<span id="p019" class="anchor"></span>- - - - - - - - - - - RECENTLY DISCONTINUED/EXPIRED (LAST X HOURS) - - - - - - - - - -

8 FOLIC ACID TAB C 06/14/2006 06/16/2006 D

Give: 1MG PO QAM

9 GENTAMICIN 80 MG C 06/12/2006 06/12/2006 D

in 5% DEXTROSE 100 ML Q8H

10 ISONIAZID TAB C 04/03/2006 04/17/2006 DF

Give: 300MG PO QD

11 POTASSIUM CHLORIDE 10MEQ C 06/12/2006 06/12/2006 DA

in 5% DEXTROSE 1000 ML Q8H

12 POTASSIUM CHLORIDE 40 MEQ C 06/12/2006 06/12/2006 DD

in 5% DEXTROSE 250 ML 120 ml/hr

13 PROPRANOLOL TAB C 06/15/2006 06/20/2006 DP

Give: 40MG PO Q6H

14 THIAMINE TAB C 04/03/2006 04/17/2006 E

Give: 100MG PO BID

X – Represents the value set in either the ward or system parameter

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

The HOURS OF RECENTLY DC/EXPIRED field (#7) has been created in the INPATIENT WARD PARAMETERS file (#59.6). The Inpatient Medications profiles will display the recently discontinued/expired orders that fall within the number of hours specified in this field. The value defined in this field will take precedence over the Inpatient System parameter. The inpatient ward parameter allows for a minimum value of one (1) hour and a maximum value of one hundred twenty (120) hours. The Inpatient Ward Parameters Edit \[PSJ IWP EDIT\] option allows the user to edit this new ward parameter. If this parameter is not set the software will use the value in the HOURS OF RECENTLY DC/EXPIRED field (#26.8) in the PHARMACY SYSTEM file (#59.7). If neither parameter is set the software will default to twenty-four (24) hours.

The HOURS OF RECENTLY DC/EXPIRED field (#26.8) has been created in the PHARMACY SYSTEM file (#59.7). The Inpatient Medications profiles will display the recently discontinued/expired orders that fall within the number of hours specified in this field. This parameter allows for a minimum value of one (1) hour and a maximum value of one hundred twenty (120) hours. The Systems Parameters Edit \[PSJ SYS EDIT\] option includes the ability for a user to edit this inpatient site parameter. If neither parameter is set the software will default to twenty-four (24) hours.

On the medication profile in the status column the codes and the action they represent are as follows.

Order Status: The current status of the order. These statuses include:

- A Active
- N Non-Verified
- O On Call (IV orders only)
- I Incomplete
- HP Placed on hold by provider through CPRS
- H Placed on hold via backdoor Pharmacy
- E Expired
- DP Discontinued by provider through CPRS
- DE Discontinued due to edit via backdoor Pharmacy (Unit Dose orders only)
- D Discontinued via backdoor Pharmacy (IV & UD); discontinued due to edit via backdoor Pharmacy (IV)

The Status column will also display some additional discontinue type actions performed on the order. The codes and the action they represent are as follows:

- DF Discontinued due to edit by a provider through CPRS
- DD Auto discontinued due to death
- DA Auto discontinued due to patient movements

Example: Profile

Inpatient Order Entry Jun 12, 2006@23:12:54 Page: 1 of 1

PSJPATIENT11, ONE Ward: 2ASM

PID: 000-55-3421 Room-Bed: 102-1 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 12/02/23 (82) Wt(kg): 100.00 (06/24/03)

Sex: MALE Admitted: 12/11/01

Dx: HE IS A PAIN. Last transferred: 12/11/01

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 CEFAZOLIN 1 GM C 06/12/2006 06/22/2006 H

in 5% DEXTROSE 50 ML Q8H

2 CIMETIDINE TAB C 06/12/2006 07/12/2006 A

Give: 300MG PO BID

3 FUROSEMIDE TAB C 06/01/2006 06/15/2006 HP

Give: 40MG PO QAM

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

4 CAPTOPRIL TAB C 06/14/2006 06/28/2006 N

Give: 25MG PO BID

\- - - - - - - - - - - - P E N D I N G R E N E W A L S - - - - - - - - - - - -

5 HALOPERIDOL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 5MG PO BID Renewed: 06/14/2006

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

6 HEPARIN/DEXTROSE INJ,SOLN ? \*\*\*\*\* \*\*\*\*\* P

Give: IV

7 LACTULOSE SYRUP ? \*\*\*\*\* \*\*\*\*\* P NF

Give: 10GM/15ML PO BID PRN

\- - - - - - - - - - - RECENTLY DISCONTINUED/EXPIRED (LAST 24 HOURS) - - - - - -

8 FOLIC ACID TAB C 06/14/2006 06/16/2006 D

Give: 1MG PO QAM

9 GENTAMICIN 80 MG C 06/12/2006 06/12/2006 D

in 5% DEXTROSE 100 ML Q8H

10 ISONIAZID TAB C 04/03/2006 04/17/2006 DF

Give: 300MG PO QD

11 POTASSIUM CHLORIDE 10MEQ C 06/12/2006 06/12/2006 DA

in 5% DEXTROSE 1000 ML Q8H

12 POTASSIUM CHLORIDE 40 MEQ C 06/12/2006 06/12/2006 DD

in 5% DEXTROSE 250 ML 120 ml/hr

13 PROPRANOLOL TAB C 06/15/2006 06/20/2006 DP

Give: 40MG PO Q6H

14 THIAMINE TAB C 04/03/2006 04/17/2006 E

Give: 100MG PO BID

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P23" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

The nurse can enter a Patient Action at the “Select Action: Quit//” prompt in the Action Area of the screen or choose a specific order or orders.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/011.png)When the nurse holds the PSJ RNURSE key, it will be possible to take any available actions on selected Unit Dose or IV orders and verify non-verified orders.

The following keys may be assigned if the user already holds the PSJ RNURSE key:

![](inpatient-medications-nurse-s-user-manual-psj-5-423/012.png) PSJ RNFINISH key will allow the nurse to finish Unit Dose orders.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/013.png) PSJI RNFINISH key will allow the nurse to finish IV orders.

### Display of Discontinued or Edited IV Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Non-Verified/Pending Orders* \[PSJU VBW\] option allows discontinued or edited IV orders from CPRS to display to the user prior to taking action to finish or edit the pending order.

This allows the user to pull IVs that are discontinued and prevent them from being sent to the patient ward and potentially be given in error. It also allows the user to perform a drug-drug interaction check, since recently discontinued medications can still cause a drug interaction.

The discontinued and edited records which are viewed are temporary and are stored in the IV MEDICATION ORDERS DC'D (#52.75) file. These records are only intended to help identify discontinued IV orders for a particular ward or a ward group and will not include any clinics or clinic groups. The records act as alerts, and taking action on these records does not impact the actual order.

The user can delete the discontinued IV orders from the IV MEDICATION ORDERS DC'D (#52.75) file when appropriate.

The following actions are available for records being viewed in this option: (P)rint, (R)efresh, (D)elete, or (I)gnore:

- The (Print) action allows the viewed orders to be printed to a device. Optionally, those records can be deleted, once printed. Any report queued to a device will only contain discontinued orders that were logged at the time of queuing.
- The (Refresh) action re-displays the records.
- The (Delete) action removes the currently viewed records from the file so they will no longer be displayed.
- The (Ignore) action continues with the usual next prompt and take no action on the records.

In addition to helping prevent medication errors, this modification also allows labels to be pulled for IVs that are not yet prepared. This saves resources, including the drug (especially helpful when drug shortages occur), and time spent managing pharmacy orders. For IVs that are already prepared, the user may reuse the prepared bag on another patient while it is still within the expiration date.

Example: Non-Verified/Pending Orders

> Select OPTION NAME: PSJU VBW Non-Verified/Pending Orders

> Select IV ROOM NAME: CHEYENNE RM#272

> Display an Order Summary? NO// \<enter\>

> 1\) Non-Verified Orders

> 2\) Pending Orders

> Select Order Type(s) (1-2): 1-2

> 1\) Unit Dose Orders

> 2\) IV Orders

> Select Package(s) (1-2): 1-2

> Select by GROUP (G), WARD (W), CLINIC (C), PATIENT (P) or PRIORITY (PR): GROUP

> Select by WARD GROUP (W) or CLINIC GROUP (C): WARD

> Select WARD GROUP: C WARD EAST WINGS

Example: Output

IV ORDER D/Cs and EDITS Thru CPRS Since 6/1/2016@14:21 (past 840 hrs)

IV ROOM: CHEYENNE RM#272 GROUP: C WARD EAST WINGS

WARD - ROOM/BED DRUG PATIENT PID DT/TM

-------------------------------------------------------------------------

C MEDICIN 9999 ABCIXIMAB AAADTSXY,QLYJH 4507 06/06/2016

Edited Give: IV 30 ml/hr @1:15 pm

C MEDICIN 9999 ABCIXIMAB AAADTSXY,QLYJH 4507 06/07/2016

Edited Give: IV 30 ml/hr @1:56 pm

(P)rint, (R)efresh, (D)elete, or (I)gnore?: (P/R/D/I): I// gnore

## Inpatient Order Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSJ OE\]

The *Inpatient Order Entry* \[PSJ OE\] option, if assigned, allows the nurse to create, edit, renew, hold, and discontinue Unit Dose and IV orders, as well as put existing IV orders on call for any patient, while remaining in the Unit Dose Medications module.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/014.png)Note: If all coverage times are not populated for the user selected IV Room, then IV order entry may be blocked and this warning message will be displayed, “The \[name of file 59.5 entry\] IV ROOM can be updated using option 'Site Parameters (IV)' by a holder of the PSJI MGR VistA Security Key. Contact the Pharmacy Informaticist to update the IV Room parameters.”

The *InpatientOrder Entry* \[PSJ OE\] option also allows for processing of clinic orders. Clinic orders are displayed separately from non-clinic orders.

When the user accesses the *Inpatient Order Entry* option from the Unit Dose Medications module for the first time within a session, a prompt is displayed to select the IV room in which to enter orders. When only one active IV room exists, the system will automatically select that IV room. The user is then given the label and report devices defined for the IV room chosen. If no devices have been defined, the user will be given the opportunity to choose them. If this option is exited and then re-entered within the same session, the current label and report devices are shown. The following example shows the option re-entered during the same session.

Example: Inpatient Order Entry

Select Unit Dose Medications Option: IOE Inpatient Order Entry

You are signed on under the BIRMINGHAM ISC IV ROOM

Current IV LABEL device is: NT TELNET TERMINAL

Current IV REPORT device is: NT TELNET TERMINAL

Select PATIENT: PSJPATIENT1

At the “Select PATIENT:” prompt, the user can enter the patient’s name or enter the first letter of the patient’s last name and the last four digits of the patient’s social security number (e.g., P0001).

Before the Patient Information screen displays, if the patient selected has no allergy assessment on file, the following prompt displays to the pharmacist/user:

"NO ALLERGY ASSESSMENT exists for this patient! Would you like to enter one now?"

- If the pharmacist/user enters 'YES,' he/she is prompted to enter the allergy information.
- If the pharmacist/user enters 'NO,' a pharmacist intervention is created, with a type of 'NO ALLERGY ASSESSMENT.' The pharmacist/user is then prompted for Provider and Recommendation information.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/015.png)Note: If the selected patient is Sensitive, Discharged, both Sensitive and Discharged, or Deceased, there are variations in the Order Entry process and in the prompts that display to the pharmacist/user.

Example: Pharmacist Answers ‘Yes’ and Enters Allergy Information

Select PATIENT: PSJPATIENT1, ONE

NO ALLERGY ASSESSMENT exists for this patient!

Would you like to enter one now? No// YES (Yes)

Does this patient have any known allergies or adverse reactions? : Yes

This patient has no allergy/adverse reaction data.

Enter Causative Agent: LATEX

Checking existing PATIENT ALLERGIES (#120.8) file for matches...

Now checking GMR ALLERGIES (#120.82) file for matches...

Now checking the National Drug File - Generic Names (#50.6)

Now checking the National Drug File - Trade Names (#50.67)

Now checking the INGREDIENTS (#50.416) file for matches...

...OK? Yes// Y (Yes)

LATEX OK? Yes// (Yes)

Example: Pharmacist Answers ‘No’ and Intervention is Created

Select PATIENT: PSJPATIENT1, ONE

NO ALLERGY ASSESSMENT exists for this patient!

Would you like to enter one now? No// N (No)

Now creating Pharmacy Intervention

PROVIDER:

Select one of the following:

1 UNABLE TO ASSESS

2 OTHER

RECOMMENDATION: ^

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

<span id="Page_26" class="anchor"></span>The Patient Information Screen is displayed:

Example: Patient Information Screen

Patient Information Sep 12, 2000 10:36:38 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/00

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: No Allergy Assessment

Remote:

Adverse Reactions:

Inpatient Narrative: INP NARR...

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile//

The nurse can now enter a Patient Action at the “Select Action: View Profile//” prompt in the Action Area of the screen.

The DURATION OF ADMINISTRATION prompt in the *Inpatient Order Entry* \[PSJ OE\] option calculates the appropriate removal times for medications requiring removal and displays them for verification by the Pharmacist.

Example: Explanation of Duration of Administration Prompt

The Duration of Administration is the period of time the medication remains on the patient before removal. If this medication order requires a drug-free period prior to the next administration, enter a Duration of Administration here.

If this medication order does not require a drug-free period prior to the next administration, this field should be left blank.

Enter the number of hours the medication will remain on the patient in the Duration of Administration field. The BCMA user will be prompted to remove the medication after the Duration of Administration period.

The Duration of Administration cannot match or exceed the order frequency (the period of time between two Admin Times), except for BID, TID and QID schedules.

## PADE Main Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new menu option, the Pharmacy Automated Dispensing Equipment (PADE) Main Menu, has been added to Unit Dose Medications. The PADE menu option allows the user to transmit inpatient medication orders to PADE so that the user has the most current information necessary to manage and dispense medications.

This menu has the following four options:

   SA     PADE Send Area Setup

   SS     PADE System Setup

   IN     PADE Inbound Inventory Setup

   SC     PADE Send Surgery Cases

## Patient Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Actions are the actions available in the Action Area of the List Manager Screen. These actions pertain to the patient information and include editing, viewing, and new order entry.

### Patient Record Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Record Update action allows editing of the Inpatient Narrative and the Patient’s Default Stop Date and Time for Unit Dose Order entry.

Example: Patient Record Update

Patient Information Sep 12, 2000 14:39:07 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/00

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: No Allergy Assessment

Remote:

Adverse Reactions:

Inpatient Narrative: INP NARR …

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Order Entry

Select Action: View Profile// PU

INPATIENT NARRATIVE: INP NARR...// Narrative for Patient PSJPATIENT1

UD DEFAULT STOP DATE/TIME: SEP 21,2000@24:00//

The “INPATIENT NARRATIVE: INP NARR...//” prompt allows the nurse to enter information in a free text format, up to 250 characters.

The “UD DEFAULT STOP DATE/TIME:” prompt is the date and time entry to be used as the default value for the STOP DATE/TIME of the Unit Dose orders during order entry and renewal processes. This value is used only if the corresponding ward parameter is enabled. The order entry and renewal processes will sometimes change this date and time.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/016.png)Note: If the Unit Dose order, being finished by the nurse, is received from CPRS and has a duration assigned, the UD DEFAULT STOP DATE/TIME is displayed as the Calc Stop Date/Time.

When the SAME STOP DATE ON ALL ORDERS parameter is set to Yes, the module will assign the same default stop date for each patient. This date is initially set when the first order is entered for the patient, and can change when an order for the patient is renewed. This date is shown as the default value for the stop date of each of the orders entered for the patient.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/017.png)Note: If this parameter is not enabled, the user can still edit a patient’s default stop date. Unless the parameter is enabled, the default stop date will not be seen or used by the module.

Examples of Valid Dates and Times:

- JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057
- T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.
- T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.
- If the year is omitted, the computer uses CURRENT YEAR. Two-digit year assumes no more than 20 years in the future, or 80 years in the past.
- If only the time is entered, the current date is assumed.
- Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc.
- The nurse may enter a time, such as NOON, MIDNIGHT, or NOW.
- The nurse may enter NOW+3' (for current date and time plus 3 minutes--the apostrophe following the number indicates minutes).
- <u>Time is REQUIRED in this response.</u>

### New Order Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Unit Dose</u>

The New Order Entry action allows the nurse to enter new Unit Dose and IV orders for the patient depending upon the order option selected (*Order Entry*, *Non-Verified Pending Orders*, or *Inpatient Order Entry*). Only one user is able to enter new orders on a selected patient due to the patient lock within the VistA applications. This minimizes the chance of duplicate orders.

For Unit Dose order entry, a response must be entered at the “Select DRUG:” prompt. The nurse can select a particular drug or enter a pre-defined order set.

Depending on the entry in the “Order Entry Process:” prompt in the *Inpatient User Parameters Edit* option, the nurse will enter a regular or abbreviated order entry process. The abbreviated order entry process requires entry into fewer fields than regular order entry. Beside each of the prompts listed below, in parentheses, will be the word regular, for regular order entry and/or abbreviated, for abbreviated order entry.

- <span id="P30" class="anchor"></span>“Select DRUG:” (Regular and Abbreviated)

Nurses select Unit Dose medications directly from the DRUG file. The Orderable Item for the selected drug will automatically be added to the order, and all Dispense Drugs entered for the order must be linked to that Orderable Item. If the Orderable Item is edited, data in the DOSAGE ORDERED field and the DISPENSE DRUG field will be deleted. If multiple Dispense Drugs are needed in an order, they may be entered by selecting the DISPENSE DRUG field from the edit list before accepting the new order. After each Dispense Drug is selected, it will be checked against the patient’s current medications for duplicate therapy, drug-drug/drug-allergy interactions, dangerous meds for patient \>64, Aminoglycoside ordered, and Glucophage lab results order checks. (See Section 4.9 Order Checks for more information.)

The nurse can enter an order set at this prompt. An order set is a group of pre-written orders. The maximum number of orders is unlimited. Order sets are created and edited using the *Order Set Enter/Edit* option found under the *Supervisor’s Menu*.

Order sets are used to expedite order entry for drugs that are dispensed to all patients in certain medical practices or for certain procedures. Order sets are designed to be used when a recognized pattern for the administration of drugs can be identified. For example:

- A pre-operative series of drugs administered to all patients undergoing a certain surgical procedure.
- A certain series of drugs to be dispensed to all patients prior to undergoing a particular radiographic procedure.
- A certain group of drugs, prescribed by a provider for all patients, that is used for treatment on a certain medical ailment or emergency.

Order sets allow rapid entering of this repetitive information, expediting the whole order entry process. Experienced users might want to set up most of their common orders as order sets.

Order set entry begins like other types of order entry. At the “Select DRUG:” prompt, S.NAME should be entered. The NAME represents the name of a predefined order set. The characters S. tell the software that this will not be a single new order entry for a single drug, but a set of orders for multiple drugs. The S. is a required prefix to the name of the order set. When the user types the characters S.?, a list of the names of the order sets that are currently available will be displayed. If S. (\<Spacebar\> and \<Enter\>) is typed, the previous order set is entered.

After the entry of the order set, the software will prompt for the Provider’s name and Nature of Order. After entry of this information, the first order of the set will automatically be entered. The options available are different depending on the type of order entry process that is enabled–regular, abbreviated, or ward. If regular or abbreviated order entry is enabled, the user will be shown one order at a time, all fields for each order of the order set and then the “Select Item(s): Next Screen //” prompt. The user can then choose to take an action on the order. Once an action is taken or bypassed, the next order of the order set will be entered automatically. After entry of all the orders in the order set, the software will prompt for more orders for the patient. At this point the user can proceed exactly as in new order entry, and respond accordingly.

When a drug is chosen, if an active drug text entry for the Dispense Drug and/or Orderable Item linked to this drug exists, then the prompt, “Restriction/Guideline(s) exist. Display?:” will be displayed along with the corresponding defaults. The drug text indicator will be \<DIN\> and will be displayed on the right hand corner on the same line as the Orderable Item. This indicator will be highlighted.

If the Dispense Drug or Orderable Item has a non-formulary status, this status will be displayed on the screen as “\*N/F\*” beside the Dispense Drug or Orderable Item.

Overrides/Interventions (OCI):

When the OCI displays on the Order Detail screen, it indicates there are associated CPRS Provider Overrides and/or Pharmacist Interventions for this order. The Overrides/Interventions \<OCI\> will display on the same line as the Orderable Item field, to the left of the drug text indicator \<DIN\> (if it exists).

\*(1)Orderable Item: METRONIDAZOLE TAB \<OCI\>\<DIN\>

Instructions: 250MG

\*(2)Dosage Ordered: 250MG

Duration: (3)Start: 07/11/2011 15:33

\*(4) Med Route: ORAL REQUESTED START: 07/11/2011 16:00

\(5\) Stop: 07/25/2011 15:33

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q36H

\(9\) Admin Times:

\*(10) Provider: PSJPROVIDER,ONE\[es\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

METRONIDAZOLE 250MG TAB 1

\+ Enter ?? for more actions

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

If the OCI displays on the Order Detail screen, the user can type “OCI” to display the CPRS Provider Overrides and/or Pharmacist Interventions associated with the order, as well as any historical overrides and interventions, if applicable.

- “DOSAGE ORDERED:” (Regular and Abbreviated)

To allow pharmacy greater control over the order display shown for Unit Dose orders on profiles, labels, MARs, etc., the DOSAGE ORDERED field is not required if only one Dispense Drug exists in the order. If more than one Dispense Drug exists for the order, then this field is required.

When a Dispense Drug is selected, the selection list/default will be displayed based on the Possible Dosages and Local Possible Dosages.

Example: Dispense Drug with Possible Dosages

Select DRUG: BACLOFEN

Lookup: GENERIC NAME

BACLOFEN 10 MG TAB MS200

...OK? Yes// (Yes)

Now doing allergy checks.Please wait...

Now processing Clinical Reminder Order Checks.Please wait ...

Now Processing Enhanced Order Checks!Please wait...

Press Return to continue......

Available Dosage(s)

1\. 5MG

2\. 10MG

3\. 15MG

4\. 20MG

5\. 30MG

6\. 40MG

Select from list of Available Dosages or Enter Free Text Dose:

All Local Possible Dosages will be displayed within the selection list/default.

Example: Dispense Drug with Local Possible Dosages

Select DRUG: GENTAMICIN SULFATE 0.1% CREAM DE101 DERM CLINIC ONLY

...OK? Yes// (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue......

Available Dosage(s)

1\.

2\. SMALL AMOUNT

3\. THIN FILM

4\. MODERATE AMOUNT

5\. LIBERAL AMOUNT

Select from list of Available Dosages or Enter Free Text Dose:

![](inpatient-medications-nurse-s-user-manual-psj-5-423/018.png)Note: If an order contains multiple Dispense Drugs, Dosage Ordered should contain the total dosage of the medication to be administered.

The user has the flexibility of how to display the order view on the screen. When the user has chosen the drug and when no Dosage Ordered is defined for an order, the order will be displayed as:

Example: Order View Information when Dosage Ordered is not Defined

DISPENSE DRUG NAME

Give: UNITS PER DOSE MEDICATION ROUTE SCHEDULE

When the user has chosen the drug and Dosage Ordered is defined for the order, it will be displayed as:

Example: Order View Information when Dosage Ordered is Defined

ORDERABLE ITEM NAME DOSE FORM

Give: DOSAGE ORDERED MEDICATION ROUTE SCHEDULE

The DOSAGE ORDERED and the UNITS PER DOSE fields are modified to perform the following functionality:

- Entering a new backdoor order:
1.  If the Dosage Ordered entered is selected from the Possible Dosages or the Local Possible Dosages, the user will not be prompted for the Units Per Dose. Either the BCMA Units Per Dose or the Dispense Units Per Dose, defined under the Dispense Drug, will be used as the default for the Units Per Dose.
2.  If a free text dose is entered for the Dosage Order, the user will be prompted for the Units Per Dose. A warning message will display when the entered Units Per Dose does not seem to be compatible with the Dosage Ordered. The user will continue with the next prompt
- <span id="Enter_CM_Clinic_Order" class="anchor"></span>Entering a new CM Clinic Medication order:
1.  The action, CM New Clinic Medication Entry,allows users to enter Clinic Medication orders. The following menu options can be used to enter a clinic order:
    1.  *Inpatient Order Entry* \[PSJ OE\] option
    2.  *Order Entry (IV)* \[PSJI ORDER\] option
    3.  *Order Entry* \[PSJU NE\] option
- Finishing pending orders:
1.  If the Dosage Ordered entered is selected from the Possible Dosages or the Local Possible Dosages, the user will not be prompted for the Units Per Dose. Either the BCMA Units Per Dose or the Dispense Units Per Dose, defined under the Dispense Drug, will be used as the default for the Units Per Dose.
2.  If a free text dose was entered for the pending order, the UNITS PER DOSE field will default to 1. A warning message will display when the Units Per Dose does not seem to be compatible with the Dosage Ordered when the user is finishing/verifying the order.
- Editing order:
1.  Any time the DOSAGE ORDERED or the UNITS PER DOSE field is edited, a check will be performed and a warning message will display when the Units Per Dose does not seem to be compatible with the Dosage Ordered. Neither field will be automatically updated.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/019.png)Note: There will be no Dosage Ordered check against the Units Per Dose if a Local Possible Dosage is selected.

- “UNITS PER DOSE:” (Regular)

This is the number of units (tablets, capsules, etc.) of the selected Dispense Drug to be given when the order is administered.

When a selection is made from the dosage list provided at the “DOSAGE ORDERED:” prompt, then this “UNITS PER DOSE:” prompt will not be displayed unless the selection list/default contains Local Possible Dosages. If a numeric dosage is entered at the “DOSAGE ORDERED:” prompt, but not from the selection list, then the default for “UNITS PER DOSE:” will be calculated as follows: DOSAGE ORDERED/STRENGTH = UNITS PER DOSE and will not be displayed.

If free text or no value is entered at the “DOSAGE ORDERED:” prompt, the “UNITS PER DOSE:” prompt will be displayed. When the user presses \<Enter\> past the “UNITS PER DOSE:” prompt, without entering a value, a “1” will be stored. A warning message will be generated when free text is entered at the “DOSAGE ORDERED:” prompt and no value or an incorrect value is entered at the “UNITS PER DOSE:” prompt.

- “MED ROUTE:” (Regular and Abbreviated)

Inpatient Medications uses the medication route provided by CPRS as the default when finishing an IV order, and transmits any updates to an order’s medication route to CPRS.

Inpatient Medications determines the default medication route for a new order entered through Inpatient Medications, and sends the full Medication Route name for display on the BCMA VDL.

This is the administration route to be used for the order. If a Medication Route is identified for the selected Orderable Item, it will be used as the default for the order. Inpatient Medications applies the Medication Route provided by CPRS as the default when finishing an IV order.

- If no medication route is specified, Inpatient Medications will use the Medication Route provided by CPRS as the default when finishing an IV order.
- If updates are made to the medication route, Inpatient Medications will transmit any updates to an order’s Medication Route to CPRS.
- Inpatient Medications determines the default Medication Route for a new order.
- Inpatient Medications sends the full Medication Route name for display on the BCMA VDL.

<span id="p33" class="anchor"></span>PSJ\*5\*366 added a medication route “short list” and “long list” for selection of a medication route during the order finishing and order entry process. The short list includes only the routes associated with the dosage form for the selected medication in the PHARMACY ORDERABLE ITEM file (#50.7). When entering an order, entering “?” at the Medication Route prompt will display the short list of routes. Entering “??” at the Medication Route prompt will display the long list of routes. The system will allow either partial matches for routes that are found in the short list, or exact full-text matches or abbreviation matches for other routes in the MEDICATION ROUTES file (#51.2).

Prior to PSJ\*5\*366 if no default med route was defined, the system set the med route to PO or ORAL. This patch removes that automatic PO or ORAL default.

If a route entered does not match any of the defined medication routes, then “??” displays.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/020.png)In the short list you can either select by entering the leading character or by selecting the number from the displayed list.

- Sequence of Schedule Type and Schedule Prompts:

Prior to PSJ\*5\*113, the order of the prompts in Inpatient Medications order entry was Schedule Type followed by Schedule. The sequence of the prompts was changed so that the Schedule prompt falls before the Schedule Type prompt.

- Schedule Validation Requirement One

> When a schedule is selected at the Schedule Field, the system shall default the Schedule Type for the schedule entered from the Administration Schedule File into the order.

- Schedule Validation Requirement Two

> If the user changes the schedule, a warning message will be generated stating that the administration times and the schedule type for the order will be changed to reflect the defaults for the new schedule selected. The warning message: “This change in schedule also changes the ADMIN TIMES and SCHEDULE TYPE of this order” shall appear.

- Schedule Validation Check Three

> If the schedule type is changed from Continuous to PRN during an edit, the system shall automatically remove any administration times that were associated with the schedule so that the order will not include administration times.

- “SCHEDULE:” (Regular and Abbreviated)

This defines the frequency the order is to be administered. Schedules must be selected from the ADMINISTRATION SCHEDULE file, with the following exceptions:

- Schedule containing PRN: (Ex. TID PC PRN). If the schedule contains PRN, the base schedule must be in the ADMINISTRATION SCHEDULE file.
- Day of week schedules (Ex. MO-FR or MO-FR@0900)
- Admin time only schedules (Ex. 09-13)

While entering a new order, if a Schedule is defined for the selected Orderable Item, that Schedule is displayed as the default for the order.

- “SCHEDULE TYPE:” (Regular)

This defines the type of schedule to be used when administering the order. If the Schedule Type entered is one-time, the ward parameter, DAYS UNTIL STOP FOR ONE-TIME, is accessed to determine the stop date. When the ward parameter is not available, the system parameter, DAYS UNTIL STOP FOR ONE-TIME, will be used to determine the stop date. When neither parameter has been set, one-time orders will use the ward parameter, DAYS UNTIL STOP DATE/TIME, to determine the stop date instead of the start and stop date being equal.

When a new order is entered or an order entered through CPRS is finished by pharmacy, the default Schedule Type is determined as described below:

- If no Schedule Type has been found and a Schedule Type is defined for the selected Orderable Item, that Schedule Type is used for the order.
- If no Schedule Type has been found and the schedule contains PRN, the Schedule Type is PRN.
- If no Schedule Type has been found and the schedule is “ON CALL”, “ON-CALL” or “ONCALL”, the Schedule Type is ON CALL.
- Schedules meant to cause orders to display as ON CALL in BCMA must be defined in the ADMINISTRATION SCHEDULE (#51.1) file with a schedule type equal to “ON CALL.”
- For all others, the Schedule Type is CONTINUOUS.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/021.png)Note: During backdoor order entry, the Schedule Type entered is used unless the schedule is considered a ONE-TIME schedule. In that case, the Schedule Type is changed to ONE TIME.

- ADMINISTRATION TIME:” (Regular)

This defines the time(s) of day the order is to be given. Administration times must be entered in a two or four digit format. If you need to enter multiple administration times, they must be separated by a dash (e.g., 09-13 or 0900-1300). If the schedule for the order contains “PRN”, all Administration Times for the order will be ignored. In new order entry, the default Administration Times are determined as described below:

- If Administration Times are defined for the selected Orderable Item, they will be shown as the default for the order.
- If Administration Times are defined in the INPATIENT WARD PARAMETERS file for the patient’s ward and the order’s schedule, they will be shown as the default for the order.
- If Administration Times are defined for the Schedule, they will be shown as the default for the order.
- Order Validation Checks:

The following order validation checks will apply to Unit Dose orders and to intermittent IV orders.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/022.png)Note: IV orders do not have Schedule Type.

- Order Validation Check One

For intermittent IV orders, references to an order’s Schedule Type will refer to either the TYPE OF SCHEDULE from the Administration Schedule file (#51.1), or PRN for schedule names in PRN format, or CONTINUOUS for schedule names in Day of Week format.

- Order Validation Check Two

The system shall use the schedule type of the schedule from the Administration Schedule file independent of the schedule name when processing an order to determine if administration times are required for a particular order.

- Order Validation Check Three

If an order has the Schedule Type of Continuous, the Schedule entered is NOT in Day of Week (Ex. MO-FR) or PRN (Ex. TID PC PRN) format, and the frequency associated with the schedule is one day (1440 minutes) or less, the system will not allow the number of administration times associated with the order to be greater than the number of administration times calculated for that frequency. The system will allow for the number

of administration times to be LESS than the calculated administration times for that frequency but not less than one administration time. (For example, an order with a schedule of BID is associated with a frequency of 720 minutes. The frequency is divided into 1440 minutes (24 hours) and the resulting calculated administration time is two. For this order, the number of administration times allowed may be no greater than two, but no less than one. Similarly, a schedule frequency of 360 minutes must have at least one administration time but cannot exceed four administration times.)

If an order has the Schedule Type of Continuous, the Schedule entered is NOT in Day of Week (Ex. MO-FR) or PRN (Ex. TID PC PRN) format, and the frequency associated with the schedule is greater than one day (1440 minutes) and evenly divisible by 1440, only one administration time is permitted. (For example, an order with a schedule frequency of 2880 minutes must have ONLY one administration time. If the frequency is greater than 1440 minutes and not evenly divisible by 1440, no administration times will be permitted.)

The system shall present warning/error messages to the user if the number of administration times is less than or greater than the maximum admin times calculated for the schedule or if no administration times are entered. If the number of administration times entered is less than the maximum admin times calculated for the schedule, the warning message: “The number of admin times entered is fewer than indicated by the schedule.” shall appear. In this case, the user will be allowed to continue after the warning. If the number of administration times entered is greater than the maximum admin times calculated for the schedule, the error message: “The number of admin times entered is greater than indicated by the schedule.” shall appear. In this case, the user will not be allowed to continue after the warning. If no admin times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

- Order Validation Check Four

If an order has a Schedule Type of Continuous and is an Odd Schedule {a schedule whose frequency is not evenly divisible by or into 1440 minutes (1 day)}, the system shall prevent the entry of administration times. For example, Q5H, Q17H – these are not evenly divisible by 1440. In these cases, the system shall prevent access to the administration times field. No warning message is presented.

- Order Validation Check Five

If an order has a Schedule Type of Continuous with a non-odd frequency of greater than one day, (1440 minutes) the system shall prevent more than one administration time, for example, schedules of Q72H, Q3Day, and Q5Day.

If the number of administration times entered exceeds one, the error message: “This order requires one admin time” shall appear. If no administration times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

- Order Validation Check Six

If an order has a Schedule Type of One Time, or if an order is entered with a schedule that is defined in the schedule file as One Time, the system shall prevent the user from entering more than one administration time.

If more than one administration time is entered, the error message: “This is a One Time Order - only one administration time is permitted.” shall appear. No administration times are required.

- Order Validation Check Seven

For an order with a Schedule Type of Continuous where no doses/administration times are scheduled between the order’s Start Date/Time and the Stop Date/Time, the system shall present a warning message to the user and not allow the order to be accepted or verified until the Start/Stop Date Times, schedule, and/or administration times are adjusted so that at least one dose is scheduled to be given.

If the stop time will result in no administration time between the start time and stop time, the error message: “There must be an admin time that falls between the Start Date/Time and Stop Date/Time.” shall appear.

- “SPECIAL INSTRUCTIONS:” (Regular and Abbreviated)

These are the Special Instructions (using abbreviations whenever possible) needed for the administration of this order. This field allows unlimited characters. For new order entry, when Special Instructions are added, the nurse is prompted whether to flag this field for display in a BCMA message box. When finishing orders placed through CPRS, where the Provider Comments are not too long to be placed in this field, the nurse is given the option to copy the comments into this field. Should the nurse choose to copy and flag these comments for display in a BCMA message box on the Virtual Due List (VDL), an exclamation mark “!” will appear in the order next to this field.

The following menu choices regarding copying of provider comments are available:

- Y Yes (copy) – This will copy Provider Comments into the Special Instructions field
- N No (don’t copy) – This will bypass copying Provider Comments
- ! Copy and flag for display in a BCMA Message Box – This will copy Provider Comments into the Special Instructions field and flag for display in a BCMA Message Box
- E Copy and Edit – This will copy Provider Comments into the Special Instructions field and open in a word processing window for editing

Example: Special Instructions

PROVIDER COMMENTS:

This text is Provider Comments.

Select one of the following:

Y Yes (copy)

N No (don't copy)

! Copy and flag for display in a BCMA Message Box

E Copy and Edit

Copy the Provider Comments into Special Instructions (Yes/No/!/E): e Copy and Edit

SPECIAL INSTRUCTIONS:

This text is Provider Comments.

EDIT? NO// y YES

==\[ WRAP \]==\[ INSERT \]========\< SPECIAL INSTRUCTIONS \>=======\[ \<PF1\>H=Help \]====

For Low Magnesium\*\*\*Magnesium \<2.4 give 11gm; Mag \<2.2 give 2 gm: mag \< 2

give 3 gm; Mag \< 1.8 give 2 x 2gm\*\* Then Recheck Magnesium

=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Would you like to flag the Special Instructions field for display in a BCMA

Message box?

     Select one of the following:

          Y         Yes

          N         No

Flag the Special Instructions (Yes/No):

![](inpatient-medications-nurse-s-user-manual-psj-5-423/023.png)Note: For “DONE” Orders (CPRS Med Order) <u>only</u>, the Provider Comments are automatically placed in the SPECIAL INSTRUCTIONS field. If the Provider Comments are greater than 180 characters, Special Instructions will display “REFERENCE PROVIDER COMMENTS IN CPRS FOR INSTRUCTIONS.”

![](inpatient-medications-nurse-s-user-manual-psj-5-423/024.png)Note: The up arrow character “^” is not allowed in Special Instructions. If detected, the following prompts appear:

Example: Prompts when “^” is detected in Special Instructions

SPECIAL INSTRUCTIONS:

No existing text

Edit? NO// Yes YES

==\[ WRAP \]==\[ INSERT \]========\< SPECIAL INSTRUCTIONS \>=======\[ \<PF1\>H=Help \]====

for low magnesium \*\*\* \<2.4 give 1 gm; Mag \<2.2gm; Mag \<2 give 3gm; Mag

\<1.8 give 2 x 2gm\*\*. Then recheck magnesium^ Y Yes (copy)

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

SPECIAL INSTRUCTIONS must not contain embedded uparrow "^".

Press Return to continue editing SPECIAL INSTRUCTIONS...

- “<span id="Indication_field_New_ord_entry" class="anchor"></span>INDICATION:”

With patch PSJ\*5\*399, the user will be prompted for Indication. The list of indications is retrieved from the Pharmacy Orderable item file (#50.7) field \#14 MOST COMMON INDICATION FOR USE and field \#13 INDICATION FOR USE subfile (#50.713). Indication is not a required field in backdoor but is a required field in CPRS.

Example: Non-Verified Unit Dose Order with Indication

NON-VERIFIED UNIT DOSE Feb 11, 2022@15:21:18 Page: 1 of 2

CPRSPATIENT,ONE Ward: 3 NORTH SURG A

PID: 666-06-1001 Room-Bed: AS-6 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/15/53 (68) Att: CPRSPROVIDER,ONE Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: INSULIN REGULAR 500 UNT/ML INJ

Instructions:

\*(2)Dosage Ordered: 10MG

Duration: (3)Start: 02/11/2022 15:20

\*(4) Med Route: INTRAMUSCULAR

\(5\) Stop: 02/25/2022 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QAM

\(9\) Admin Times: 09

\*(10) Provider: CPRSPROVIDER,FIFTY \[w\]

\(11\) Special Instructions:

\(14\) Indication: FOR BLOOD SUGAR

\(12\) Dispense Drug U/D Inactive Date

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen//

Example: Active Unit Dose Order with Indication

ACTIVE UNIT DOSE Feb 11, 2022@15:21:53 Page: 1 of 2

CPRSPATIENT,ONE Ward: 3 NORTH SURG A

PID: 666-06-1001 Room-Bed: AS-6 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/15/53 (68) Att: CPRSPROVIDER,ONE Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: INSULIN REGULAR 500 UNT/ML INJ

Instructions:

\*(2)Dosage Ordered: 10MG

Duration: \*(3)Start: 02/11/2022 15:20

\*(4) Med Route: INTRAMUSCULAR

\*(5) Stop: 02/25/2022 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QAM

\(9\) Admin Times: 09

\*(10) Provider: CPRSPROVIDER,FIFTY \[w\]

\(11\) Special Instructions:

\(14\) Indication: FOR BLOOD SUGAR

\(12\) Dispense Drug U/D Inactive Date

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen//

Example: Pending Unit Dose Order with Indication

PENDING UNIT DOSE (ROUTINE) Feb 11, 2022@15:43:25 Page: 1 of 2

BCMAPATIENT,EIGHTEEN Ward: BCMA CAD

PID: 666-33-1018 Room-Bed: 4-B Ht(cm): 254.00 (07/06/18)

DOB: 04/07/35 (86) Att: CPRSPROVIDER,ONE Wt(kg): 68.04 (04/29/21)

\*(1)Orderable Item: INSULIN INJ

Instructions: 10MG

\*(2)Dosage Ordered: 10MG

Duration: (3)Start: 02/11/2022 15:36

\*(4) Med Route: INTRAMUSCULAR REQUESTED START: 02/11/2022 17:00

\(5\) Stop: 05/22/2022 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q6H

\(9\) Admin Times: 0500-1100-1700-2300

\*(10) Provider: CPRSPROVIDER,FIFTY \[w\]

\(11\) Special Instructions:

\(14\) Indication: TO CONTROL BLOOD SUGAR

\(12\) Dispense Drug U/D Inactive Date

\+ INVALID DISPENSE DRUG

BY Bypass FL Flag

DC Discontinue FN Finish

Select Item(s): Next Screen//

- “START DATE/TIME:” (Regular and Abbreviated)

This is the date and time the order is to begin. For Inpatient Medications orders, the Start Date/Time is initially assigned to the CLOSEST ADMINISTRATION TIME, NEXT ADMINISTRATION TIME or NOW (which is the login date/time of the order), depending on the value of the DEFAULT START DATE CALCULATION field in the INPATIENT WARD PARAMETERS file. Start Date/Time may not be entered prior to 7 days from the order’s Login Date. When a start date is being entered or edited, there will be a warning given if the start date is more than seven days in the future.

- “EXPECTED FIRST DOSE:” (Regular and Abbreviated)

Inpatient Medications no longer displays an expected first dose for orders containing a schedule with a schedule type of One-time. The system also no longer displays an expected first dose for orders containing a schedule with a schedule type of On-call. The Inpatient Medications application performs the following actions.

- Modifies order entry to allow entry of a Day-of-Week schedule in the following format: days@schedule name. For example, MO-WE-FR@BID or TU@Q6H.
- Translates the schedule into the appropriate administration times. For example, MO-WE-FR@BID is translated to MO-WE-FR@10-22.
- Modifies the expected first dose calculation to accept the new format of schedules. For example, MO-WE-FR@BID or MO@Q6H.
- Accepts the new formatted schedules from CPRS. For example, MO-WE-FR@BID or TU@Q6H.

Translates a schedule received in the new format from CPRS into the appropriate schedule and administration times.

<span id="Rules_for_StopDateTime_Calc" class="anchor"></span>

- “STOP DATE/TIME:” (Regular)

This is the date and time the order will automatically expire. The system calculates the default Stop Date/Time for order administration based on the STOP TIME FOR ORDER site parameter. For IV orders, the default date shown is the least of (1) the \<IV TYPE\> GOOD FOR HOW MANY DAYS site parameter (where \<IV TYPE\> is LVPs, PBs, etc.), (2) the NUMBER OF DAYS FOR IV ORDER field (found in the IV Additives file) for all additives in this order, (3) the DAY (nD) or DOSE (nL) LIMIT field (found in the PHARMACY ORDERABLE ITEM file) for the orderable item associated with this order or (4) the duration received from CPRS (if applicable). The Site Manager or Application Coordinator can change any fields.

Note that an entry of a stop date greater than 367 days from the start of the date of the order is not allowed.

For the rules for calculating Unit Dose order Stop Date/Time calculation, refer to [Section 18.5.2 Stop Date/Time Calculation](file:///C:/Users/VHAISPBERNIC/Downloads/psj_5_388_tm.docx) in the Inpatient Medications Technical Manual/Security Guide.

- “PROVIDER:” (Regular and Abbreviated)This identifies the provider who authorized the order. Only users who meet all these conditions may be selected at this prompt: holds the Provider security key, is Authorized to Write Med Orders, does not have an Inactivation Date or an Inactivation Date that has passed, does not have a Termination Date or a Termination Date that has passed, and who is not DISUSER’ed.

  <span id="p40" class="anchor"></span>For Controlled Substance medications, the provider must also have a valid DEA number in the NEW DEA \#'S multiple of their <span id="p42_NewPersonFile" class="anchor"></span>NEW PERSON file (#200). In order for the DEA number to be valid for a medication, the DEA number must not be expired, and must be authorized for medication's drug schedule.

  Note: Patch PSJ\*5\*366 added the criteria to check for DISUSER.

  Note: Patch PSJ\*5\*372 added the criteria to check for DEA number.
- “SELF MED:” (Regular and Abbreviated)Identifies the order as one whose medication is to be given for administration by the patient. This prompt is only shown if the ‘SELF MED’ IN ORDER ENTRY field of the INPATIENT WARD PARAMETERS file is set to On.
- “NATURE OF ORDER:” (Regular and Abbreviated)  
  This is the method the provider used to communicate the order to the user who entered or took action on the order. Nature of Order is defined in CPRS. Written will be the default for new orders entered. When a new order is created due to an edit, the default will be Service Correction. The following table shows some Nature of Order examples.

| Nature of Order    | Description                                                                                            | Prompted for Signature in CPRS | Chart Copy Printed? |
|--------------------|--------------------------------------------------------------------------------------------------------|--------------------------------|---------------------|
| Written            | The source of the order is a written doctor’s order                                                    | No                             | No                  |
| Verbal             | A doctor verbally requested the order                                                                  | Yes                            | Yes                 |
| Telephoned         | A doctor telephoned the service to request the order                                                   | Yes                            | Yes                 |
| Service Correction | The service is discontinuing or adding new orders to carry out the intent of an order already received | No                             | No                  |
| Duplicate          | This applies to orders that are discontinued because they are a duplicate of another order             | No                             | Yes                 |
| Policy             | These are orders that are created as a matter of hospital policy                                       | No                             | Yes                 |

The Nature of Order abbreviation will display on the order next to the Provider’s Name. The abbreviations will be in lowercase and enclosed in brackets. Written will display as \[w\], telephoned as \[p\], verbal as \[v\], policy as \[i\], electronically entered as \[e\], and service correction as \[s\]. If the order is electronically signed through the CPRS package <u>AND</u> the CPRS patch OR\*3\*141 is installed on the user’s system, then \[es\] will appear next to the Provider’s Name instead of the Nature of Order abbreviation.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/025.png) <span id="Indication_New_Order_Entry_Note" class="anchor"></span>Note: In the example below, the available selections for the Indications field will display because Indication was pre-defined for the orderable item. However, when there is no pre-defined Indication for an orderable item, available selections will not display and the Indications field will look like this:  
  
Flag the Other Print Info (Yes/No): No  
INDICATION:  
START DATE/TIME: JUL 12,2022@07:40// (JUL 12, 2022@07:40)

Example: <span id="New_Order_Entry4" class="anchor"></span>New Order Entry

> <u>Patient Information Apr 28, 2021@10:01:38 Page: 1 of 1</u>

> PSJPATIENT1,ONE Ward: GENERAL A

> PID: 000-00-0202 Room-Bed: GENMED-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> DOB: 05/16/70 (50) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> Sex: FEMALE Admitted: 04/23/21

> Dx: LUNG CANCER Last transferred: \*\*\*\*\*\*\*\*

> CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

> Allergies - Verified: LATEX

> Non-Verified:

> Adverse Reactions:

> Inpatient Narrative:

> Outpatient Narrative:

> Enter ?? for more actions

> PU Patient Record Update NO New Order Entry

> DA Detailed Allergy/ADR List IN Intervention Menu

> VP (View Profile) CM New Clinic Medication Entry

> Select Action: Quit// NO New Order Entry

> Select DRUG: FLUOROURACIL 50MG

> Lookup: VA PRODUCT NAME

> FLUOROURACIL 50MG/ML INJ FLUOROURACIL 500MG/10ML INJ AN300

> ...OK? Yes// (Yes)

> --------------------------------------------------------------------------------

> \*\*\*\*\* WARNING \*\*\*\*\*

> FLUOROURACIL is hazardous to handle and dispose. Please take the

> appropriate handling and disposal precautions.

> --------------------------------------------------------------------------------

> Press Return to continue:

> Now doing allergy checks. Please wait...

> Now processing Clinical Reminder Order Checks. Please wait ...

> Now Processing Enhanced Order Checks! Please wait...

> Available Dosage(s)

> 1\. 50MG/1ML

> 2\. 100MG/2ML

> Select from list of Available Dosages or Enter Free Text Dose: 1 50MG/1ML

> You entered 50MG/1ML is this correct? Yes// YES

> MED ROUTE: // SQ SUBCUTANEOUS SQ

> SCHEDULE: TID

> 1 TID 09-13-17

> 2 TID 01-02-03-04

> CHOOSE 1-2: 1 TID 09-13-17

> SCHEDULE TYPE: CONTINUOUS// CONTINUOUS

> ADMIN TIMES: 09-13-17//

> SPECIAL INSTRUCTIONS:

> Edit? NO// YES

> ==\[ WRAP \]==\[INSERT \]=========\< SPECIAL INSTRUCTIONS \[Press \<PF1\>H for help\]====

> BELOW.

> ADDING SPECIAL INSTRUCTIONS.

> \<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

> Would you like to flag the Special Instructions field for display in a BCMA

> Message box?

> Select one of the following:

> Y Yes

> N No

> Flag the Special Instructions (Yes/No): YES Yes  
> <span id="indication_New_Order_Entry" class="anchor"></span>INDICATION:

> 1 FOR CHEMOTHERAPY

> 99 Free Text entry

> Select INDICATION from the list: ?

> This field contains the Indication For Use and must be 3-40 characters

> in length.

> 1 FOR CHEMOTHERAPY

> 99 Free Text entry

> Select INDICATION from the list: 1 FOR CHEMOTHERAPY

> START DATE/TIME: APR 28,2021@10:08// APR 28,2021@10:08

> STOP DATE/TIME: MAY 12,2021@24:00// MAY 12,2021@24:00

> Expected First Dose: APR 28,2021@13:00

> PROVIDER: McCOY, BONES //

> <u>ACTIVE UNIT DOSE Apr 28, 2021@10:08:18 Page: 1 of 2</u>

> PSJPATIENT1,ONE Ward: GENERAL A

> PID: 000-00-0202 Room-Bed: GENMED-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> DOB: 05/16/70 (50) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> (1)Orderable Item: FLUOROURACIL INJ,SOLN

> Instructions:

> (2)Dosage Ordered: 50MG/1ML

> Duration: (3)Start: 04/28/2021 10:08

> \(4\) Med Route: SUBCUTANEOUS

> \(5\) Stop: 05/12/2021 24:00

> \(6\) Schedule Type: CONTINUOUS

> \(8\) Schedule: TID

> \(9\) Admin Times: 09-13-17

> \(10\) Provider: McCOY, BONES

> \(11\) Special Instructions!: (see below)

> BELOW.

> ADDING SPECIAL INSTRUCTIONS.

> \+ Enter ?? for more actions

> ED Edit AC ACCEPT

> Select Item(s): Next Screen// AC ACCEPT

> NATURE OF ORDER: WRITTEN// W

> ...transcribing this non-verified order....

> <u>NON-VERIFIED UNIT DOSE Apr 28, 2021@10:57:27 Page: 1 of 2</u>

> PSJPATIENT1,ONE Ward: GENERAL A

> PID: 000-00-0202 Room-Bed: GENMED-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> DOB: 05/16/70 (50) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> \*(1)Orderable Item: FLUOROURACIL INJ,SOLN

> Instructions:

> \*(2)Dosage Ordered: 50MG/1ML

> Duration: (3)Start: 04/28/2021 13:00

> \*(4) Med Route: SUBCUTANEOUS

> \(5\) Stop: 05/03/2021 22:00

> \(6\) Schedule Type: CONTINUOUS

> \*(8) Schedule: TID

> \(9\) Admin Times: 09-13-17

> \*(10) Provider: McCOY, BONES \[w\]

> \(11\) Special Instructions!: (see below)

> Adding Special Instructions.

> <u>(12) Dispense Drug U/D Inactive Date</u>

> \+ Enter ?? for more actions

> DC Discontinue ED Edit AL Activity Logs

> HD (Hold) RN (Renew)

> FL Flag VF Verify

> Select Item(s): Next Screen// VF Verify

> ...a few moments, please.....

> Pre-Exchange DOSES:

> ORDER VERIFIED.

> Type \<Enter\> to continue or '^' to exit:

<u>IV</u>

For IV order entry, the nurse must bypass the “Select DRUG:” prompt (by pressing \<Enter\>) and then choosing the IV Type at the “Select IV TYPE:” prompt. The following are the prompts that the nurse can expect to encounter while entering a new IV order for the patient.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/026.png) This option is only available to those nurses who have Inpatient Order Entry access.

- “Select IV TYPE:”

IV types are admixture, piggyback, hyperal, syringe, and chemotherapy. An admixture is a Large Volume Parenteral (LVP) solution intended for continuous parenteral infusion. A piggyback is a small volume parenteral solution used for intermittent infusion. Hyperalimentation (hyperal) is long-term feeding of a protein-carbohydrate solution. A syringe IV type order uses a syringe rather than a bottle or a bag. Chemotherapy is the treatment and prevention of cancer with chemical agents.

When an order is received from CPRS, Inpatient Medications will accept and send updates to IV Types from CPRS. When an IV type of Continuous is received, Inpatient Medications defaults to an IV type of Admixture. However, when an IV type of Intermittent is received, Inpatient Medications defaults to an IV type of piggyback.

- “Select ADDITIVE:”

There can be any number of additives for an order, including zero. An additive or additive synonym can be entered. If the Information Resources Management Service (IRMS) Chief/Site Manager or Application Coordinator has defined it in the IV Additives file, the nurse may enter a quick code for an additive. The quick code allows the user to pre-define certain fields, thus speeding up the order entry process. The <u>entire</u> quick code name must be entered to receive all pre-defined fields in the order.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/027.png)Note: Drug inquiry is allowed during order entry by entering two question marks (??) at the strength prompt for information on an additive or solution.

When an additive is chosen, if an active drug text entry for the Dispense Drug and/or Orderable Item linked to this additive exists, then the prompt, “Restriction/Guideline(s) exist. Display?:” will be displayed along with the corresponding defaults. The drug text indicator will be \<DIN\> and will be displayed on the right side of the IV Type on the same line. This indicator will be highlighted.

If the Dispense Drug tied to the Additive or the Orderable Item has a non-formulary status, this status will be displayed on the screen as “\*N/F\*” beside the Additive or Orderable Item.

<span id="p040" class="anchor"></span>

- “BOTTLE:”

The bottle number is used to specify in which the additive will be included for the IV order.  If this field is blank, it means that the additive will be included in all bottles.

A pending order from CPRS can have an additive bottle value such as “1” (1 Bag/Day), blank (All bags), or “See Comments” (which bottle number(s) to place the additive in, is entered in the Provider Comments). During the finishing process, the user can enter/edit a specific value for the bottle number(s). If the bottle number for an additive contains “See Comments”, the user must replace it with either the specific bottle number(s) or enter an “@” to remove the “See Comments” to indicate that the additive will be included in all bottles.

- “Select SOLUTION:”

There can be any number of solutions in an order, depending on the type. It is even possible to require zero solutions when an additive is pre-mixed with a solution. If no solutions are chosen, the system will display a warning message, in case it is an oversight, and gives the opportunity to add one. The nurse may enter an IV solution or IV solution synonym.

When a solution is chosen, if an active drug text entry for the Dispense Drug and/or Orderable Item linked to this solution exists, then the prompt, “Restriction/Guideline(s) exist. Display?:” will be displayed along with the corresponding defaults. The drug text indicator will be \<DIN\> and will be displayed on the right side of the IV Type on the same line. This indicator will be highlighted.

If the Dispense Drug tied to the Solution or the Orderable Item has a non-formulary status, this status will be displayed on the screen as “\*N/F\*” beside the Solution or Orderable Item.

- “INFUSION RATE:”

The infusion rate is the rate at which the IV is to be administered. This value, in conjunction with the total volume of the hyperal or the admixture type, is used to determine the time covered by one bag; hence, the system can predict the bags needed during a specified time of coverage. This field is free text for piggybacks. For admixtures, a number that will represent the infusion rate must be entered. The nurse can also specify the \# of bags per day that will be needed. This will automatically populate the NUMBER OF LABELS PER DAY (NLPD) field.

Example: 125 = 125 ml/hr (IV system will calculate bags needed per day), 125@2 = 125 ml/hr with 2 labels per day, Titrate@1 = Titrate with 1 label per day. The format of this field is either a number only or free text only, or \[FREE TEXT@NUMBER OF LABELS PER DAY.\]

Intermittent IV Orders

The schedule and administration times for intermittent orders are used to determine the number of daily scheduled labels. The use of the @ symbol for intermittent IV orders is not allowed.

Continuous IV Orders

A 2-digit numeric field is added to the NON-VERIFIED ORDERS file (#53.1) and to the IV (#100) multiple of the PHARMACY PATIENT file (#55).

- Printed IV labels do not display the NLPD field regardless of value.
- The NLPD field, if populated, determines the number of labels that will print when the *Scheduled Labels (IV)* \[PSJI LBLS\] option is run for continuous IV orders.
- The NLPD field is not sent to BCMA.
- When an Infusion Rate is received from CPRS in the format Rate@Labels, the “@” symbol is used to separate the Infusion Rate into its respective INFUSION RATE and NLPD component fields.
- The number of labels per day is always shown next to the infusion rate, when the infusion rate is free text or the number of labels has been entered by the user, or when the number of labels has been received from CPRS. The INFUSION RATE field must be selected when editing. There is no field number reference for NLPD.
- Edits to the NLPD field never create a new order.
- The NLPD field is not populated when the number of labels is system calculated based on a numeric infusion rate.
- The following rules apply to the use of the “@” symbol in the Infusion Rate: The number entered after the “@” symbol populates the NLPD field. Anything entered before the “@” symbol displays in the INFUSION RATE field. The “@” symbol will not be visible in the display of the Infusion Rate.

Example:

INFUSION RATE: 50 ml/hr// Titrate@0

NUMBER OF LABELS PER DAY: 0//

When the infusion rate is entered as free text, a minimum of two characters is required for the order level validation for Infusion rate for Inpatient Medications or CPRS orders.

Example:

INFUSION RATE: 50 ml/hr// INFUSE SLOWLY

When the infusion rate is numeric, the NLPD is optional. When entering free text in THE INFUSION RATE field, the NLPD is required with no default. Numeric entry of 0-99 is allowed; all other entries are invalid.

- A new order is not created when a change is made to the NLPD field.

When the INFUSION RATE field is selected, an NLPD prompt displays.

Example:

NUMBER OF LABELS PER DAY: //

An abbreviation entered in the INFUSION RATE field is replaced with expanded text, if the abbreviation has been defined in the INFUSION INSTRUCTIONS file (#53.47.)

Example:

INFUSION RATE: 50 ml/hr// T … Now Expanding Text

Input expanded to Titrate

Press Return to Continue

A minimum of 2 characters and a maximum of 30 characters may be entered into the INFUSION RATE field. The special character “^” is not allowed. A warning message displays if the free text entry contains less than the minimum requirement of 2 characters or more than the maximum requirement of 30 characters.

Example: Warning Message

INFUSION RATE: 50 ml/hr// P

Free text entries must contain a minimum of 2 characters and a maximum of 30 characters.

INFUSION RATE: 50 ml/hr//

The INFUSION INSTRUCTIONS file (#53.47) allows the user to add to or edit the abbreviations or expanded text by storing the infusion rate abbreviations, up to 9 characters, and the associated expanded text, a minimum of 2 characters and a maximum of 30 characters.

Help Text is provided for the infusion rate when ? or ?? is entered.

When an order is received from CPRS, Inpatient Medications accepts infusion rates in both ml/hr and as “infuse over time.” In the Order View screen, for orders with an IV Type considered Intermittent, the infusion rate will display as “infuse over” followed by the time. For example, infuse over 30 minutes.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/028.png)Note: If an administration time(s) is defined, the number of labels will reflect the administration time(s) for the intermittent IVPB type orders.

- “MED ROUTE:” (Regular and Abbreviated)

Inpatient Medications uses the medication route provided by CPRS as the default when finishing an IV order, and transmits any updates to an order’s medication route to CPRS.

Inpatient Medications determines the default medication route for a new order entered through Inpatient Medications, and sends the full Medication Route name for display on the BCMA VDL.

This is the administration route to be used for the order. If a Medication Route is identified for the selected Orderable Item, it will be used as the default for the order. Inpatient Medications applies the Medication Route provided by CPRS as the default when finishing an IV order.

- If no medication route is specified, Inpatient Medications will use the Medication Route provided by CPRS as the default when finishing an IV order.
- If updates are made to the medication route, Inpatient Medications will transmit any updates to an order’s Medication Route to CPRS.
- Inpatient Medications determines the default Medication Route for a new order.
- Inpatient Medications sends the full Medication Route name for display on the BCMA VDL.

PSJ\*5\*366 added a medication route “short list” and “long list” for selection of a medication route during the order finishing and order entry process. The short list includes only the routes associated with the dosage form for the selected medication in the PHARMACY ORDERABLE ITEM file (#50.7). When entering an order, entering “?” at the Medication Route prompt will display the short list of routes. Entering “??” at the Medication Route prompt will display the long list of routes. The system will allow either partial matches for routes that are found in the short list, or exact full-text matches or abbreviation matches for other routes in the MEDICATION ROUTES file (#51.2).

<span id="p47" class="anchor"></span>Prior to PSJ\*5\*366 if no default med route was defined, the system set the med route to PO or ORAL. This patch removes that automatic PO or ORAL default.

If a route entered does not match any of the defined medication routes, then “??” displays.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/029.png)In the short list you can either select by entering the leading character or by selecting the number from the displayed list.

- “SCHEDULE:”

This prompt occurs on piggyback and intermittent syringe orders. Schedules must be selected from the ADMINISTRATION SCHEDULE file, with the following exceptions:

- Schedule containing PRN: (Ex. TID PC PRN). If the schedule contains PRN, the base schedule must be in the ADMINISTRATION SCHEDULE file.
- Day of week schedules (Ex. MO-FR or MO-FR@0900)
- Admin time only schedules (Ex. 09-13)
- “ADMINISTRATION TIME:”

This is free text. The pharmacist might want to enter the times of dose administration using military time such as 03-09-15-21. Administration times must be entered in a two or four digit format. If multiple administration times are needed, they must be separated by a dash (e.g., 09-13 or 0900-1300). This field must be left blank for odd schedules, (e.g., Q16H).

- “OTHER PRINT INFO:”

The system allows a word processing entry of unlimited free text. For new order entry, when Other Print Info is added, the nurse is prompted whether to flag this field for display in a BCMA message box. When finishing orders placed through CPRS, where the Provider Comments are not too long to be placed in this field, the nurse is given the option to copy the comments into this field. Should the nurse choose to copy and flag these comments for display in a BCMA message box on the VDL, an exclamation mark “!” will appear in the order next to this field.

The following menu choices regarding copying of provider comments are available:

- Y Yes (copy) – This will copy Provider Comments into the Other Print Info field.
- N No (don’t copy) – This will bypass copying Provider Comments.
- ! Copy and flag for display in a BCMA Message Box – This will copy Provider Comments into the Other Print Info field and flag for display in a BCMA Message Box.
- E Copy and Edit – This will copy Provider Comments into the Other Print Info field and open in a word processing window for editing.

The system enables the nurse to review the provider comments received from CPRS during the finishing of an IV order. A maximum of 60 characters of text is printed on the IV label from Other Print Info. When Other Print Info exceeds 60 characters, the message: “Instructions too long. See Order View or BCMA for full text.” appears on the IV label.

Before the nurse enters Other Print Info information, the message: “WARNING, IF OTHER PRINT INFO exceeds one line of 60 characters, ‘Instructions too long. See Order View or BCMA for full text.’ prints on the IV label instead of the full text.”

After the nurse enters Other Print Info information, if the entry exceeds one line of 60 characters, the message: “WARNING OTHER PRINT INFO exceeds one line of 60 characters, ‘Instructions too long. See Order View or BCMA for full text.’ prints on the IV label instead of the full text.”

Example: Other Print Info

OTHER PRINT INFO

This text is Other Print Info

Would you like to flag the Other Print Info field for display in a BCMA

Message box?

Select one of the following:

Y Yes

N No

Flag the Other Print Info (Yes/No): y Yes

![](inpatient-medications-nurse-s-user-manual-psj-5-423/030.png)Note: For “DONE” Orders (CPRS Med Order) <u>only</u>, the Provider Comments are automatically placed in the OTHER PRINT INFO field. If the Provider Comments are greater than 60 characters, Other Print Info will display “REFERENCE PROVIDER COMMENTS IN CPRS FOR INSTRUCTIONS.”

- “<span id="Indication_field_New_ord_IV" class="anchor"></span>INDICATION:”

With patch PSJ\*5\*399, the user will be prompted for Indication. The list of indications is retrieved from the Pharmacy Orderable item file (#50.7) field \#14 MOST COMMON INDICATION FOR USE and field \#13 INDICATION FOR USE subfile (#50.713). Indication is not a required field in backdoor but is a required field in CPRS.

Example: Non-Verified IV Order with Indication

NON-VERIFIED IV Feb 11, 2022@15:24:45 Page: 1 of 2

CPRSPATIENT,ONE Ward: 3 NORTH SURG A

PID: 666-06-1001 Room-Bed: AS-6 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/15/53 (68) Att: CPRSPROVIDER,ONE Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1) Additives: Type: ADMIXTURE

MULTIVITAMIN INJ 10 ML (1)

\*(2) Solutions:

SODIUM CHLORIDE 0.45% 1000 ML

Duration: (4) Start: 02/11/2022 15:00

\*(3) Infusion Rate: 10 ml/hr (4 labels per

day)

\*(5) Med Route: IV (6) Stop: 02/14/2022 23:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: CPRSPROVIDER,FIFTY \[w\] Cum. Doses:

\(10\) Other Print:

\(14\) Indication: TO FILL NUTRITIONAL GAPS

\+ Enter ?? for more actions

DC Discontinue RN (Renew) VF Verify

HD (Hold) OC (On Call) FL Flag

ED Edit AL Activity Logs

Select Item(s): Next Screen//

Example: Active IV Order with Indication

ACTIVE IV Feb 11, 2022@15:25:25 Page: 1 of 2

CPRSPATIENT,ONE Ward: 3 NORTH SURG A

PID: 666-06-1001 Room-Bed: AS-6 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/15/53 (68) Att: CPRSPROVIDER,ONE Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1) Additives: Order number: 23 Type: ADMIXTURE

MULTIVITAMIN INJ 10 ML (1)

\*(2) Solutions:

SODIUM CHLORIDE 0.45% 1000 ML

Duration: \*(4) Start: 02/11/2022 15:00

\*(3) Infusion Rate: 10 ml/hr (4 labels per

day)

\*(5) Med Route: IV \*(6) Stop: 02/14/2022 23:59

\*(7) Schedule: Last Fill: 02/11/2022 15:25

\(8\) Admin Times: Quantity: 4

\*(9) Provider: CPRSPROVIDER,FIFTY \[w\] Cum. Doses: 4

\(10\) Other Print:

\(14\) Indication: TO FILL NUTRITIONAL GAPS

\+ Enter ?? for more actions

DC Discontinue RN Renew VF (Verify)

HD Hold OC On Call FL Flag

ED Edit AL Activity Logs

Select Item(s): Next Screen//

Example: Pending IV Order with Indication

PENDING IV (ROUTINE) Feb 11, 2022@15:37:42 Page: 1 of 3

<span id="BCMAPATIENT_EIGHTEEN" class="anchor"></span>BCMAPATIENT,EIGHTEEN Ward: BCMA CAD

PID: 666/33/0018 Room-Bed: 4-B Ht(cm): 254.00 (07/06/18)

DOB: 04/07/35 (86) Att: CPRSPROVIDER,ONE Wt(kg): 68.04 (04/29/21)

\*(1) Additives: Type: ADMIXTURE

MULTIVITAMIN INJ 10 ML (1)

\*(2) Solutions:

SODIUM CHLORIDE 3% 500 ML

Duration: (4) Start: 02/11/2022 15:36

\*(3) Infusion Rate: 10 ml/hr

\*(5) Med Route: IV (6) Stop: 02/14/2022 23:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: CPRSOROVIDER,FIFTY \[w\] Cum. Doses:

\(10\) Other Print:

\(14\) Indication: TO FILL NUTRITIONAL GAPS

\(11\) Remarks :

IV Room: ALBANY IV ROOM

\+ Enter ?? for more actions

DC Discontinue FL Flag

ED Edit FN Finish

Select Item(s): Next Screen//

- “START DATE / TIME:”

The system calculates the default Start Date/Time for order administration based on the DEFAULT START DATE CALCULATION field in the INPATIENT WARD PARAMETERS file. This field allows the site to use the NEXT or CLOSEST administration or delivery time, or NOW, which is the order’s login date/time as the default Start Date. When NOW is selected for this parameter, it will <u>always</u> be the default Start Date/Time for IVs. This may be overridden by entering the desired date/time at the prompt.

When NEXT or CLOSEST is used in this parameter and the IV is a continuous-type IV order, the default answer for this prompt is based on the delivery times for the IV room specified for that order entry session. For intermittent type IV orders, if the order has administration times, the start date/time will be the NEXT or CLOSEST administration time depending on the parameter. If the intermittent type IV order does not have administration times, the start date/time will round up or down to the closest hour. The Site Manager or Application Coordinator can change this field.

The Pharmacy User is warned if they attempt to enter a start date more than 7 days in the future. When a start date is being entered or edited, there will be a warning given if the start date is more than seven days in the future.

- “EXPECTED FIRST DOSE:” (Regular and Abbreviated)

Inpatient Medications no longer displays an expected first dose for orders containing a schedule with a schedule type of One-time. The system also no longer display an expected first dose for orders containing a schedule with a schedule type of On-call. The Inpatient Medications application performs the following actions.

- Modifies order entry to allow entry of a Day-of-Week schedule in the following format: days@schedule name. For example, MO-WE-FR@BID or TU@Q6H.
- Translates the schedule into the appropriate administration times. For example, MO-WE-FR@BID is translated to MO-WE-FR@10-22.
- Modifies the expected first dose calculation to accept the new format of schedules. For example, MO-WE-FR@BID or MO@Q6H.
- Accepts the new formatted schedules from CPRS. For example, MO-WE-FR@BID or TU@Q6H.
- Translates a schedule received in the new format from CPRS into the appropriate schedule and administration times.
- “<span id="Stop_Date_Time" class="anchor"></span>STOP DATE / TIME:”

The system calculates the default Stop Date/Time for order administration based on the STOP TIME FOR ORDER site parameter. For IV orders, the default date shown is the least of (1) the \<IV TYPE\> GOOD FOR HOW MANY DAYS site parameter (where \<IV TYPE\> is LVPs, PBs, etc.), (2) the NUMBER OF DAYS FOR IV ORDER field (found in the IV Additives file) for all additives in this order, (3) the DAY (nD) or DOSE (nL) LIMIT field (found in the PHARMACY ORDERABLE ITEM file) for the orderable item associated with this order or (4) the duration received from CPRS (if applicable). The Site Manager or Application Coordinator can change these fields.

Note that an entry of a stop date greater than 367 days from the start of the date of the order is not allowed.

For the rules for calculating Unit Dose order Stop Date/Time calculation, refer to [Section 18.5.2 Stop Date/Time Calculation](file:///C:/Users/VHAISPBERNIC/Downloads/psj_5_388_tm.docx) in the Inpatient Medications Technical Manual/Security Guide.

- “NATURE OF ORDER:”

This is the method the provider used to communicate the order to the user who entered or took action on the order. Nature of Order is defined in CPRS. “Written” will be the default for new orders entered. When a new order is created due to an edit, the default will be Service Correction. The following table shows some Nature of Order examples.

| Nature of Order    | Description                                                                                            | Prompted for Signature in CPRS? | Chart Copy Printed? |
|--------------------|--------------------------------------------------------------------------------------------------------|---------------------------------|---------------------|
| Written            | The source of the order is a written doctor’s order                                                    | No                              | No                  |
| Verbal             | A doctor verbally requested the order                                                                  | Yes                             | Yes                 |
| Telephoned         | A doctor telephoned the service to request the order                                                   | Yes                             | Yes                 |
| Service Correction | The service is discontinuing or adding new orders to carry out the intent of an order already received | No                              | No                  |
| Duplicate          | This applies to orders that are discontinued because they are a duplicate of another order             | No                              | Yes                 |
| Policy             | These are orders that are created as a matter of hospital policy                                       | No                              | Yes                 |

The Nature of Order abbreviation will display on the order next to the Provider’s Name. The abbreviations will be in lowercase and enclosed in brackets. Written will display as \[w\], telephoned as \[p\], verbal as \[v\], policy as \[i\], electronically entered as \[e\], and service correction as \[s\]. If the order is electronically signed through the CPRS package <u>AND</u> the CPRS patch OR\*3\*141 is installed on the user’s system, then \[es\] will appear next to the Provider’s Name instead of the Nature of Order abbreviation.

- “Select CLINIC LOCATION:”

This prompt is only displayed for Outpatient IV orders entered through the Inpatient Medications package. The user will enter the hospital location name when prompted.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/031.png)Note: While entering an order, the nurse can quickly delete the order by typing a caret (^) at any one of the prompts listed above except at the “Stop Date/Time:” prompt. Once the user has passed this prompt, if the order still needs to be deleted, a caret (^) can be entered at the “Is this O.K.:” prompt.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/032.png)<span id="Indication_Example_New_Ord_entry_note" class="anchor"></span>Note: In the example below, the available selections for the Indications field will display because Indication was pre-defined for the orderable item. However, when there is no pre-defined Indication for an orderable item, available selections will not display and the Indications field will look like this:

Flag the Other Print Info (Yes/No): No  
INDICATION:  
START DATE/TIME: JUL 12,2022@07:40// (JUL 12, 2022@07:40)

Example: New Order Entry

Select ADDITIVE: MULT

1 MULTIVITAMIN INJ

2 MULTIVITAMINS

CHOOSE 1-2: 2 MULTIVITAMINS

(The units of strength for this additive are in ML)

Strength: 2 2 ML

Select ADDITIVE:

Select SOLUTION: 0.9

1 0.9% SODIUM CHLORIDE 100 ML

BCMA

2 0.9% SODIUM CHLORIDE 50 ML

BCMA

CHOOSE 1-2: 1 0.9% SODIUM CHLORIDE 100 ML

BCMA

Now doing allergy checks.Please wait...

Now processing Clinical Reminder Order Checks.Please wait ...

Now Processing Enhanced Order Checks!Please wait...

======================================================================================

This patient is receiving the following orders(s) that have a SIGNIFICANT Drug

Interaction with MULTIVITAMINS 2 ML:

WARFARIN INJ C 02/22 03/01 N

Give: 5MG/1VIAL PO 3ID

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS.

======================================================================================

Display Professional Interaction Monograph(s)? NO// YES

DEVICE: HOME// COMPUTER ROOM

Professional Monograph

Drug Interaction with WARFARIN and MULTIVITAMINS

This information is generalized and not intended as specific medical

advice. Consult your healthcare professional before taking or

discontinuing any drug or commencing any course of treatment.

MONOGRAPH TITLE: Selected Anticoagulants/Alpha Tocopheryl

SEVERITY LEVEL: 2-Severe Interaction: Action is required to reduce the

risk of severe adverse interaction.

MECHANISM OF ACTION: Unknown.

CLINICAL EFFECTS: Vitamin E may increase the pharmacologic effects of

anticoagulants.

PREDISPOSING FACTORS: None determined.

PATIENT MANAGEMENT: Coadministration of vitamin E and anticoagulants

Press Return to continue...

should be avoided. If both drugs are administered, monitor

hypoprothrombinemic response to warfarin and adjust the dose of the

anticoagulants as indicated. The time of highest risk for a coumarin-type

drug interaction is when the precipitant drug is initiated or

discontinued. Contact the prescriber before initiating, altering the

dose or discontinuing either drug.

DISCUSSION: Vitamin E doses of 800 International Units/day and more

have been reported to increase the hypoprothrombinemic effect of

warfarin: while doses of 42 International units/day of vitamin E for 30

days have increased the hypoprothrombinemic effect of dicumarol.

Agenerase brand of amprenavir capsules and oral solution contain a

significant amount of vitamin E. Each 150 mg capsule contains 109

International Units vitamin E, with a total of 1744 International Units

of vitamin E in the recommended daily adult dose. Each mL of oral

solution contains 46 International Units of vitamin E.

REFERENCES:

1.Corrigan JJ Jr, Marcus FI. Coagulopathy associated with vitamin E

ingestion. JAMA 1974 Dec 2:230(9):1300-1.

Press Return to continue...

2.Schrogie JJ. Letter: Coagulopathy and fat-soluble vitamins. JAMA 1976

Apr 7:232(1):19.

3.Corrigan JJ Jr, Ulfers LL. Effect of vitamin E on prothrombin levels

in warfarin-induced vitamin K deficiency. Am J Clin Nutr 1981 Sep:

34(9):1701-5.

4.Anonymous. Vitamin K, vitamin E and the coumarin drugs. Nutr Rev 1982

Jun: 40(6):180-2.

5.Agenerase (amprenavir) Capsules US prescribing information.

GlaxoSmithKline February, 2004.

Copyright 2010 First DataBank, Inc.

Do you want to Intervene with MULTIVITAMINS 2 ML? NO//

INFUSION RATE: 125 INFUSE OF 125 MINUTES

MED ROUTE: IV//

SCHEDULE: QID

ADMINISTRATION TIMES: 09-13-17-21//

REMARKS:

OTHER PRINT INFO:  
<span id="Indication_Example_New_Ord_entry" class="anchor"></span>INDICATION:

1 TO FILL NUTRITIONAL GAPS

99 Free Text entry

Select INDICATION from the list: ?

This field contains the Indication For Use and must be 3-40 characters

in length.

1 TO FILL NUTRITIONAL GAPS

99 Free Text entry

Select INDICATION from the list:

START DATE/TIME: 02/26/2010@18:51// (FEB 26, 2010@18:51)

STOP DATE/TIME: 03/27/2010@23:59

PROVIDER: PROVIDER,ONE

1 PROVIDER,ONE NEW YORK OP 10BA1/ADP Scholar Extra

ordinaire

2 PROVIDER,ONEHUNDRED TZB 10BA1/ADP Scholar Extraord

ordinaire

3 PROVIDER,ONEHUNDREDFIVE 10BA1/ADP Scholar Extraor

dordinaire

4 PROVIDER,ONEHUNDREDNINETYONE BM 10BA1/ADP Schol

ar Extraordinaire

5 PROVIDER,ONEHUNDREDSIXTYSEVEN 10BA1/ADP Scholar E

xtraordinaire

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 PROVIDER,ONE NEW YORK OP 10BA1/ADP Scholar E

xtraordinaire

Orderable Item: MULTIVITAMINS INJ

Give: IV QID

100716

\[1\]0808 7A GEN MED 02/25/10

EIGHT,INPATIENT 726-B

MULTIVITAMINS 2 ML

0.9% SODIUM CHLORIDE 100 ML

INFUSE OVER 125 MINUTES

QID

09-13-17-21

1\[1\]

Start date; 02/25/2010 18:51 Stop date: 03/27/2010 23:59

Expected First Dose: FEB 25,2010@21:00

Is this O.K.: YES// YES

NATURE OF ORDER: WRITTEN// W

...transcribing this non-verified order....

NON-VERIFIED IV Feb 25, 2010@18:54:08 Page: 1 of 2

EIGHT,INPATIENT Ward: 7A GEN

PID: 666-00-0808 Room-Bed: 726-B Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 01/01/50 (61) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

--------------------------------------------------------------------------------

\*(1) Additives: Type: PIGGYBACK

MULTIVITAMINS 2 ML

\(2\) Solutions:

0.9% SODIUM CHLORIDE 100 ML

Duration: (4) Start: 02/26/2010 18:51

\(3\) Infusion Rate: INFUSE OVER 125 MINUTES

\*(5) Med Route: IV (6) Stop: 03/27/2010 23:59

\*(7) Schedule: QID Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 09-13-17-21 Quantify: 0

\*(9) Provider: PROVIDER,ONE \[w\] Cum. Doses:

\*(10)Orderable item: MULTIVITAMINS INJ

Instructions:

\(11\) Other Print:

+---------Enter ?? for more actions---------------------------------------------

DC Discontinue RN (Renew) VF Verify

HD (Hold) OC (On Call) FL Flag

ED Edit AL Activity Logs

Select Item(s): Next Screen//

After entering the data for the order, the system will prompt the nurse to confirm that the order is correct. The IV module contains an integrity checker to ensure the necessary fields are answered for each type of order. The nurse must edit the order to make corrections if all of these fields are not answered correctly. If the order contains no errors, but has a warning, the user will be allowed to proceed.

PADE Stock and Ward Stock Items

The VistA Pharmacy Inpatient Order Entry Patient Profile screen contains information on whether or not a drug is a PADE stock item.

New display functions include the following:

- PD = PADE stock item (Medication in the PADE inventory file)
- WP = Ward Stock and PADE stock item

<span id="Page_52" class="anchor"></span>Example: Patient Profile Inpatient Order Entry screen display

<u>Inpatient Order Entry Mar 03, 2015@13:38:02 Page: 1 of 1</u>

BCMAPATIENT,FOUR Ward: 7A GEN A

PID: 000-00-0001 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 12/25/66 (48) Attn: Psj,Test Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: FEMALE TrSp: Medical Observat Admitted: 01/12/09

Dx: COUGH Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 ALPRAZOLAM TAB C 03/02 03/09 A PD

Give: 0.25MG PO BID

2 AMPICILLIN CAP,ORAL C 03/03 03/09 A WP

Give: 250MG BY MOUTH TID

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

3 CAPTOPRIL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 75MG PO TID

4 LEVOTHYROXINE TAB ? \*\*\*\*\* \*\*\*\*\* P WS

Give: 0.025MG BY MOUTH \*Q8H

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P55" class="anchor"></span>CM New Clinic Order Entry

SO Select Order

Select Action: Quit//

### Detailed Allergy/ADR List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Detailed Allergy/ADR List action displays a detailed listing of the selected item from the patient’s Allergy/ADR List. Entry to the *Edit Allergy/ADR Data* option is provided with this list also.

- Enter/Edit Allergy/ADR Data  
  Provides access to the Adverse Reaction Tracking (ART) package to allow entry and/or edit of allergy adverse reaction data for the patient. See the Allergy package documentation for more information on Allergy/ADR processing.
- Select Allergy  
  Allows the user to view a specific allergy. Intervention Menu

![](inpatient-medications-nurse-s-user-manual-psj-5-423/033.png) This option is only available to those users who hold the PSJ RPHARM key.

The Intervention Menu action allows entry of new interventions and existing interventions to be edited, deleted, viewed, or printed. Each kind of intervention will be discussed and an example will follow.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/034.png)Note: Interventions can also be dynamically created in response to Order Checks for critical drug-drug interactions and allergy/ADRs. Refer to [Section 4.9 Order Checks](#p123).

If a change is made to an intervention associated to an inpatient order made in response to critical drug-drug and/or allergy/ADR, the changes are reflected and displayed whenever interventions display.

New interventions entered via the Intervention Menu are at the patient level and are not associated with a particular order. Consequently, new entries made through this menu are not reflected in the OCI listing, the BCMA Display Order detail report, and do not cause highlighting in BCMA.

- New: This option is used to add an entry into the APSP INTERVENTION file.

Example: New Intervention

Patient Information Feb 11, 2011@11:17:44 Page: 1 of 1

BCMAPATIENT,FIVE Ward: 3 NORTH

PID: 000-00-5555 Room-Bed: 1-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 09/16/45 (65) Att: Psj,Test Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE TrSp: Medical Observati Admitted: 12/05/08

Dx: FLUID IN LUNGS Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: NKA

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI Delete Pharmacy Intervention PO Print Pharmacy Intervention

ED Edit Pharmacy Intervention VP View Pharmacy Intervention

NE Enter Pharmacy Intervention

Select Item(s): NE Enter Pharmacy Intervention

Select APSP INTERVENTION INTERVENTION DATE: T FEB 11, 2011

Are you adding 'FEB 11, 2011' as a new APSP INTERVENTION (the 526TH)? No// Y

(Yes)

APSP INTERVENTION PATIENT: PRETST,PATTHREE 8-1-61 000009677

NO NSC VETERAN

Combat Vet Status: ELIGIBLE End Date: 02/12/2015

APSP INTERVENTION DRUG: CIMETIDINE 200MG TAB GA301

PROVIDER: PHARMACIST,LINDA J LP

INSTITUTED BY: PHARMACY// PHARMACY

INTERVENTION: ?

Answer with APSP INTERVENTION TYPE, or NUMBER

Do you want the entire 22-Entry APSP INTERVENTION TYPE List? N (No)

INTERVENTION: ALLERGY

RECOMMENDATION: NO CHANGE

WAS PROVIDER CONTACTED: NO NO

RECOMMENDATION ACCEPTED: Y YES

FINANCIAL COST:

REASON FOR INTERVENTION:

No existing text

Edit? NO//

ACTION TAKEN:

No existing text

Edit? NO//

CLINICAL IMPACT:

No existing text

Edit? NO//

FINANCIAL IMPACT:

No existing text

Edit? NO//

Select APSP INTERVENTION INTERVENTION DATE:

- Edit: This option is used to edit an existing entry in the APSP INTERVENTION file.

Example: Edit an Intervention

Patient Information Feb 11, 2011@11:52:02 Page: 1 of 1

PRETST,PATTHREE Ward:

PID: 000-00-9677 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/01/61 (49) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted:

Dx: Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: NKA

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI   Delete Pharmacy Intervention       PO   Print Pharmacy Intervention

ED   Edit Pharmacy Intervention         VP   View Pharmacy Intervention

NE   Enter Pharmacy Intervention

Select Item(s): ED   Edit Pharmacy Intervention 

Select INTERVENTION:T SEP 22, 2000 PRETST,PATTHREE WARFARIN 10MG

INTERVENTION DATE: SEP 22,2000// \<Enter\>

PATIENT: PRETST,PATTHREE// \<Enter\>

PROVIDER: PSJPROVIDER,ONE // \<Enter\>

PHARMACIST: PSJNURSE,ONE // \<Enter\>

DRUG: WARFARIN 10MG// \<Enter\>

INSTITUTED BY: PHARMACY// \<Enter\>

INTERVENTION: ALLERGY// \<Enter\>

OTHER FOR INTERVENTION:

1\>

RECOMMENDATION: NO CHANGE// \<Enter\>

OTHER FOR RECOMMENDATION:

1\>

WAS PROVIDER CONTACTED: NO// \<Enter\>

PROVIDER CONTACTED:

RECOMMENDATION ACCEPTED: YES// \<Enter\>

AGREE WITH PROVIDER: \<Enter\>

FINANCIAL COST:

REASON FOR INTERVENTION:

No existing text

Edit? NO//

ACTION TAKEN:

No existing text

Edit? NO//

CLINICAL IMPACT:

No existing text

Edit? NO//

FINANCIAL IMPACT:

No existing text

Edit? NO//

- Delete: This option is used to delete an entry from the APSP INTERVENTION file. The nurse may only delete an entry that was entered on the same day.

Example: Delete an Intervention

Patient Information Feb 11, 2011@11:52:02 Page: 1 of 1

PRETST,PATTHREE Ward:

PID: 000-00-9677 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/01/61 (49) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted:

Dx: Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: NKA

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI Delete Pharmacy Intervention PO Print Pharmacy Intervention

ED Edit Pharmacy Intervention VP View Pharmacy Intervention

NE Enter Pharmacy Intervention

Select Item(s): de Delete Pharmacy Intervention

You may only delete entries entered on the current day.

Select APSP INTERVENTION INTERVENTION DATE: t FEB 11, 2011

1 2-11-2011 PRETST,PATTHREE CIMETIDINE 200MG TAB

2 2-11-2011 PRETST,PATTHREE CIMETIDINE 200MG TAB

CHOOSE 1-2: 1 2-11-2011 PRETST,PATTHREE CIMETIDINE 200MG TAB

SURE YOU WANT TO DELETE THE ENTIRE ENTRY? y YES

Select APSP INTERVENTION INTERVENTION DATE:

- View: This option is used to display Pharmacy Interventions in a captioned format.

Example: View an Intervention

Patient Information Feb 11, 2011@11:52:02 Page: 1 of 1

PRETST,PATTHREE Ward:

PID: 000-00-9677 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/01/61 (49) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted:

Dx: Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: NKA

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI Delete Pharmacy Intervention PO Print Pharmacy Intervention

ED Edit Pharmacy Intervention VP View Pharmacy Intervention

NE Enter Pharmacy Intervention

Select Item(s): VP View Pharmacy Intervention

Select APSP INTERVENTION INTERVENTION DATE: T FEB 11, 2011 PRETST,PATTHR

EE CIMETIDINE 200MG TAB

ANOTHER ONE:

INTERVENTION DATE: FEB 11, 2011 PATIENT: PRETST,PATTHREE

PROVIDER: PROVIDER,LINDA J PHARMACIST: PHARMACIST,CHRIS

DRUG: CIMETIDINE 200MG TAB INSTITUTED BY: PHARMACY

INTERVENTION: ALLERGY RECOMMENDATION: NO CHANGE

WAS PROVIDER CONTACTED: NO RECOMMENDATION ACCEPTED: YES

Select APSP INTERVENTION INTERVENTION DATE:

- Print: This option is used to obtain a captioned printout of Pharmacy Interventions for a certain date range. It will print out on normal width paper and can be queued to print at a later time.

Example: Print an Intervention

Select Unit Dose Medications Option: Inpatient Order Entry

Select PATIENT: BCMA,EIGHTEEN-PATIENT 666-33-0018 04/07/35 7A GEN MED

Patient Information Mar 16, 2011@12:37:20 Page: 1 of 1

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

CrCL: 0.8(est.) (CREAT: 122mg/dL 8/26/96) BSA (m2): 2.15

--------------------------------------------------------------------------------

Allergies - Verified: AMPICILLIN, PENICILLIN, STRAWBERRIES

Non-Verified:

Adverse Reactions:

Inpatient Narrative:

Outpatient Narrative:

----------Enter ?? for more actions---------------------------------------------

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI Delete Pharmacy Intervention PO Print Pharmacy Intervention

ED Edit Pharmacy Intervention VP View Pharmacy Intervention

NE Enter Pharmacy Intervention

Select Item(s): PO Print Pharmacy Intervention

\* Previous selection: INTERVENTION DATE from Jun 1,2010

START WITH INTERVENTION DATE: Jun 1,2010// T-1 (MAR 15, 2011)

GO TO INTERVENTION DATE: LAST// T (MAR 16, 2011)

DEVICE: home;80;9999 COMPUTER ROOM

PHARMACY INTERVENTION LISTING MAR 16,2011 12:37 PAGE 1

--------------------------------------------------------------------------------

INTERVENTION: CRITICAL DRUG INTERACTION

INTERVENTION DATE: MAR 16,2011 PATIENT: BCMA,EIGHTEEN-PATIENT

PROVIDER: PROVIDER,ONE PHARMACIST: PHARMACIST,TWO

DRUG: INDINAVIR SULFATE 400MG CAP INSTITUTED BY: PHARMACY

RECOMMENDATION: NO CHANGE

WAS PROVIDER CONTACTED: RECOMMENDATION ACCEPTED:

PROVIDER CONTACTED:

INTERVENTION DATE: MAR 16,2011 PATIENT: BCMA,EIGHTEEN-PATIENT

PROVIDER: PROVIDER,ONE PHARMACIST: PHARMACIST,TWO

DRUG: SIMVASTATIN 20MG TAB INSTITUTED BY: PHARMACY

RECOMMENDATION: NO CHANGE

WAS PROVIDER CONTACTED: RECOMMENDATION ACCEPTED:

PROVIDER CONTACTED:

----------------------------

SUBTOTAL 0

SUBCOUNT 2

----------------------------

TOTAL 0

COUNT 2

Patient Information Mar 16, 2011@12:37:57 Page: 1 of 1

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

CrCL: 0.8(est.) (CREAT: 122mg/dL 8/26/96) BSA (m2): 2.15

--------------------------------------------------------------------------------

Allergies - Verified: AMPICILLIN, PENICILLIN, STRAWBERRIES

Non-Verified:

Adverse Reactions:

Inpatient Narrative:

Outpatient Narrative:

----------Enter ?? for more actions---------------------------------------------

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile//

### View Profile 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Profile action allows selection of a Long, Short, or NO profile for the patient. The profile displayed in the *Inpatient Order Entry* and *Non-Verified/Pending Orders* options will include IV and Unit Dose orders. The long profile shows all orders, including discontinued and expired orders. The short profile displays recently discontinued or expired orders based on parameter values found in the System parameter and inpatient ward parameter files.

<span id="Example_Profile_View" class="anchor"></span>Example: Profile View

Inpatient Order Entry         Oct 19, 2010@16:41:35          Page:    1 of    3

PSJPATIENT,ELEVEN                 Ward: 7AS   

   PID: 666-00-2921           Room-Bed:               Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

   DOB: 08/09/54 (56)                                 Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

   Sex: MALE                                     Admitted: 06/09/10

    Dx: RESPIRATORY DISTRESS             Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found BSA (m2): \_\_\_\_\_\_\_\_\_\_\_

                                                                                

 - - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

   1  -\>AMIODARONE TAB                           C  10/19/2010  11/18/2010 A   

          Give: 400MG PO TID                                                    

   2    CIMETIDINE TAB                           C  10/19/2010  11/18/2010 R   

          Give: 300MG PO QHS                                                   
 - - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

   3    LOVASTATIN TAB                           C  10/19/2010  11/18/2010 N  NF

          Give: 20MG PO QPM                                                    
 - - - - - - - - - -  N O N - V E R I F I E D  C O M P L E X - - - - - - - - - -

   4    HALOPERIDOL TAB                          C  10/19/2010  11/18/2010 N   

          Give: 10MG PO BID                                                    

        HALOPERIDOL TAB                          C  10/19/2010  11/18/2010 N   

         Give: 15MG PO QHS                                                    
 - - - - - - - - - - - - P E N D I N G   R E N E W A L S - - - - - - - - - - - -

   5    CIMETIDINE TAB                           ?  \*\*\*\*\*  \*\*\*\*\* P  

          Give: 300MG PO QHS   Renewed 10/19/2010                                                  
 - - - - - - - - - - - - - P E N D I N G  C O M P L E X - - - - - - - - - - - -

   6    PREDNISONE TAB                           ?  \*\*\*\*\*  \*\*\*\*\* P             

          Give: 20MG PO QAM                                                     

        PREDNISONE TAB                           ?  \*\*\*\*\*  \*\*\*\*\* P             

          Give: 10MG PO QOD                                                    

        PREDNISONE TAB                           ?  \*\*\*\*\*  \*\*\*\*\* P             

          Give: 5MG PO QD                                                      
 - - - - - - - - - - - - - - - -  P E N D I N G - - - - - - - - - - - - - - - -

7    ACETAMINOPHEN TAB                        ?  \*\*\*\*\*  \*\*\*\*\* P             

          Give: 650MG PO Q4H PRN                                               
 - - - - - - - -  RECENTLY DISCONTINUED/EXPIRED (LAST 120 HOURS) - - - - - - - -

   8    ASPIRIN TAB,EC                           C  10/19/2010  10/19/2010 D   

          Give: 325MG PO QHS                                                   

   9  -\>NAPROXEN TAB                             C  10/19/2010  10/19/2010 D   

          Give: 250MG PO BID                                                   

\+ Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P61" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen//

The orders on the profile are sorted first by status (ACTIVE, NON-VERIFIED, NON-VERIFIED COMPLEX, PENDING RENEWALS, PENDING COMPLEX, PENDING, RECENTLY DISCONTINUED/EXPIRED), then alphabetically by SCHEDULE TYPE. Pending orders with a priority of STAT are listed first and are displayed in a bold and blinking text for easy identification. After SCHEDULE TYPE, orders are sorted alphabetically by DRUG (the drug name listed on the profile), and then in descending order by START DATE.

Example: Short Profile

Inpatient Order Entry Jun 12, 2006@23:12:54 Page: 1 of 1

PSJPATIENT11, ONE Ward: 2ASM

PID: 000-55-3421 Room-Bed: 102-1 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 12/02/23 (82) Att: Psj,Test Wt(kg): 100.00 (06/24/03)

Sex: MALE TrSp: Medical Observati Admitted: 12/11/01

Dx: HE IS A PAIN. Last transferred: 12/11/01

CrCL: \<Not Found\> (CREAT: Not Found BSA (m2): \_\_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 CEFAZOLIN 1 GM C 06/12 06/22 H

in 5% DEXTROSE 50 ML Q8H

2 CIMETIDINE TAB C 06/12 07/12 A

Give: 300MG PO BID

3 FUROSEMIDE TAB C 06/01 06/15 HP

Give: 40MG PO QAM

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

4 CAPTOPRIL TAB C 06/14 06/28 N

Give: 25MG PO BID

\- - - - - - - - - - - - P E N D I N G R E N E W A L S - - - - - - - - - - - -

5 HALOPERIDOL TAB ? \*\*\*\*\* \*\*\*\*\* P 06/14

Give: 5MG PO BID

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

6 HEPARIN/DEXTROSE INJ,SOLN ? \*\*\*\*\* \*\*\*\*\* P

Give: IV

7 LACTULOSE SYRUP ? \*\*\*\*\* \*\*\*\*\* P NF

Give: 10GM/15ML PO BID PRN

- - - - - - - - - - - RECENTLY DISCONTINUED/EXPIRED (LAST X HOURS) - - - - - - - - - -

8 FOLIC ACID TAB C 06/14 06/16 D

Give: 1MG PO QAM

9 GENTAMICIN 80 MG C 06/12 06/12 D

in 5% DEXTROSE 100 ML Q8H

10 ISONIAZID TAB C 04/03 04/17 DF

Give: 300MG PO QD

11 POTASSIUM CHLORIDE 10MEQ C 06/12 06/12 DA

in 5% DEXTROSE 1000 ML Q8H

12 POTASSIUM CHLORIDE 40 MEQ C 06/12 06/12 DD

in 5% DEXTROSE 250 ML 120 ml/hr

13 PROPRANOLOL TAB C 06/15 06/20 DP

Give: 40MG PO Q6H

14 THIAMINE TAB C 04/03 04/17 E

Give: 100MG PO BID

X – Represents the value set in either the ward or system parameter

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P62" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Sets of Complex Orders with a status of “Pending” or “Non-Verified” will be grouped together in the Profile View. They appear as one numbered list item, as shown in the following examples. Once these orders are made active, they will appear individually in the Profile View, with a status of “Active”.

If an order has been verified by pharmacy but has not been verified by nursing, it will be listed under the ACTIVE heading with an arrow (-\>) to the right of its number. A CPRS Med Order will have a “DONE” priority and will display a “d” to the right of the number on the long profiles. These orders will display under the Non-Active header.

Orders may be selected by choosing the Select Order action, or directly from the profile using the number displayed to the left of the order. Multiple orders may be chosen by entering the numbers of each order to be included separated by commas (e.g., 1,2,3), or a range of numbers using the dash (e.g., 1-3).

The HOURS OF RECENTLY DC/EXPIRED field (#7) has been created in the INPATIENT WARD PARAMETERS file (#59.6). The Inpatient Medications profiles will display the recently discontinued/expired orders that fall within the number of hours specified in this field. The value defined in this field will take precedence over the Inpatient System parameter. The inpatient ward parameter allows for a minimum value of one (1) hour and a maximum value of one hundred twenty (120) hours. The Inpatient *Ward Parameters Edit* \[PSJ IWP EDIT\] option allows the user to edit this new ward parameter. If this parameter is not set the software will use the value in the HOURS OF RECENTLY DC/EXPIRED field (#26.8) in the PHARMACY SYSTEM file (#59.7). If neither parameter is set the software will default to twenty-four (24) hours.

The HOURS OF RECENTLY DC/EXPIRED field (#26.8) has been created in the PHARMACY SYSTEM file (#59.7). The Inpatient Medications profiles will display the recently discontinued/expired orders that fall within the number of hours specified in this field. This parameter allows for a minimum value of one (1) hour and a maximum value of one hundred twenty (120) hours. The *Systems Parameters Edit* \[PSJ SYS EDIT\] option includes the ability for a user to edit this inpatient site parameter. If neither parameter is set the software will default to twenty-four (24) hours.

On the medication profile in the status column the codes and the action they represent are as follows.

Order Status: The current status of the order. These statuses include:

- A Active
- N Non-Verified
- O On Call (IV orders only)
- I Incomplete
- HP Placed on hold by provider through CPRS
- H Placed on hold via backdoor Pharmacy
- E Expired
- DP Discontinued by provider through CPRS
- DE Discontinued due to edit via backdoor Pharmacy (Unit Dose orders only)
- D Discontinued via backdoor Pharmacy (IV & UD); discontinued due to edit via backdoor Pharmacy (IV)

The Status column will also display some additional discontinue type actions performed on the order. The codes and the action they represent are as follows:

- DF Discontinued due to edit by a provider through CPRS
- DD Auto discontinued due to death
- DA Auto discontinued due to patient movements

![](inpatient-medications-nurse-s-user-manual-psj-5-423/035.png)Note: The START DATE and DRUG sort may be reversed using the INPATIENT PROFILE ORDER SORT prompt in the *Edit Inpatient User Parameters* option.

Example: Pending Complex Order in Profile View

Inpatient Order Entry Mar 07, 2004@13:03:55 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 03/03/04

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): \_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - P E N D I N G C O M P L E X - - - - - - - - - - - - - - - -

1 CAPTOPRIL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 25MG PO QDAILY

CAPTOPRIL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 50MG PO BID

CAPTOPRIL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 100MG PO TID

 

 

 

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P64" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen//

Example: Non-Verified Complex Order in Profile View

Inpatient Order Entry Mar 07, 2004@13:03:55 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 03/03/04

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): \_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - N O N - V E R I F I E D C O M P L E X - - - - - - - - - - - -

1 CAPTOPRIL TAB C 03/26/2004 03/27/2004 N

Give: 25MG PO QDAILY

CAPTOPRIL TAB C 03/28/2004 03/29/2004 N

Give: 50MG PO BID

CAPTOPRIL TAB C 03/30/2004 03/31/2004 N

Give: 100MG PO TID

 

 

 

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen//

Example: Active Complex Order in Profile View

Inpatient Order Entry Mar 07, 2004@15:00:05 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 03/03/04

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - -

1 CAPTOPRIL TAB C 03/26/2004 03/27/2004 A

Give: 25MG PO QDAILY

2 CAPTOPRIL TAB C 03/28/2004 03/29/2004 A

Give: 50MG PO BID

3 CAPTOPRIL TAB C 03/30/2004 03/31/2004 A

Give: 100MG PO TID

 

 

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen//

Orders that are dispensed via Pharmacy Automated Dispensing Equipment (PADE) will display a ‘PD’ flag to the right of the order status. If an order is dispensed via PADE and is also a Ward Stock item, the ‘WP’ flag will display.

Example: PD and WP Flags for PADE / Ward Stock Items

<u>Inpatient Order Entry         Dec 16, 2015@16:51:41          Page:    1 of   10</u>

MONPATNM,MARILYN                  Ward: GENERAL                    CAD

   PID: 666-00-0195           Room-Bed: GENSUR-2      Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

   DOB: 07/07/67 (48)                                 Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

   Sex: FEMALE                                   Admitted: 08/29/11

Dx: CHEST PAIN Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2):­­­­­­­­­­­\_\_\_\_\_\_\_\_ <u>                                                                              </u>

 - - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

   1    ACETAMINOPHEN 160MG/5ML LIQUID,ORAL      C  12/02/2015  12/16/2015 A   

          Give: 650MG=20.3ML(1 UD CUP) PO Q12H                                 

   2    FAMCICLOVIR TAB                          C  12/03/2015  12/17/2015 A  PD

          Give: 250MG PO Q12H                                                  

   3    HALOPERIDOL TAB                          C  10/28/2015  12/21/2015 A  WP

          Give: 20.25MG PO Q24H                                                

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen// 

### Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Information screen is displayed for the selected patient. The header contains the patient’s demographic data, while the list area contains Allergy/Adverse Reaction data, including remote data and Pharmacy Narratives. If an outpatient is selected, all future appointments in clinics that allow Inpatient Medications orders will display in the list area, too.

Example: Patient Information

Patient Information Sep 13, 2000 15:04:31 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/00

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: No Allergy Assessment

Remote:

Adverse Reactions:

Inpatient Narrative: Narrative for Patient PSJPATIENT1

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile//

Example: Patient Information Screen for Outpatient Receiving Inpatient Medications

Patient Information May 12, 2003 14:27:13 Page: 1 of 1

PSJPATIENT3,THREE     Last Ward: 1 West  
   PID: 000-00-0003     Last Room-Bed:             Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)  
   DOB: 02/01/55 (48)                              Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)  
   Sex: FEMALE                              Last Admitted: 01/13/98

Dx: TESTING                                Discharged: 01/13/98

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

     

Allergies/Reactions: No Allergy Assessment

Remote:

Adverse Reactions: 

Inpatient Narrative:                                                            
Outpatient Narrative:                                                          

 

Clinic:                  Date/Time of Appointment:

Clinic A                 May 23, 2003/9:00 am

Flu Time Clinic          June 6, 2003/10:00 am

Enter ?? for more actions

PU Patient Record Update                NO New Order Entry  
DA Detailed Allergy/ADR List            IN Intervention Menu  
VP View Profile CM New Clinic Medication Entry  
Select Action: View Profile//

### Select Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Select Order action is used to take action on a previously entered order by selecting it from the profile, after the patient is selected and length of profile is chosen (i.e., short or long).

Example: Selecting an Order

Inpatient Order Entry Mar 07, 2002@13:01:56 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/00

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 in 0.9% SODIUM CHLORIDE 1000 ML 125 ml/hrC 03/07/2002 03/07/2002 E

2 in 5% DEXTROSE 50 ML 125 ml/hr C 03/06/2002 03/06/2002 E

3 CEPHAPIRIN 1 GM C 03/04/2002 03/09/2002 A

in DEXTROSE 5% IN N. SALINE 100 ML QID

4 ASPIRIN CAP,ORAL O 03/07/2002 03/07/2002 E

Give: 650MG PO NOW

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

5 in DEXTROSE 10% 1000 ML 125 ml/hr ? \*\*\*\*\* \*\*\*\*\* P

 

 

 

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="Revision_History" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Quit// 1

ACTIVE UNIT DOSE Mar 07, 2002@13:10:46 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: ASPIRIN CAP,ORAL \<DIN\>

Instructions:

\*(2)Dosage Ordered: 325MG

Duration: \*(3)Start: 03/07/2002 13:10

\*(4) Med Route: ORAL

BCMA ORDER LAST ACTION: 03/07/02 13:09 Given\* \*(5) Stop: 03/08/2002 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QID

\(9\) Admin Times: 09-13-17-21

\*(10) Provider: PSJPROVIDER,ONE \[es\]

\(11\) Special Instructions:

 

\(12\) Dispense Drug U/D Inactive Date

ASPIRIN BUFFERED 325MG TAB 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL (Flag) VF (Verify)

Select Item(s): Next Screen//

The list area displays detailed order information and allows actions to be taken on the selected order. A number displayed to the left of the field name identifies fields that may be edited. If a field, marked with an asterisk (\*) next to its number, is edited, it will cause this order to be discontinued and a new one created. If a pending order is selected, the system will determine any default values for fields not entered through CPRS and display them along with the data entered by the provider.

The BCMA ORDER LAST ACTION field will only display when an action has been performed through BCMA on this order. This information includes the date and time of the action and the BCMA action status. If an asterisk (\*) appears after the BCMA status, this indicates an action was taken on the prior order that is linked to this order.

Actions, displayed in the Action Area, enclosed in parenthesis are not available to the user. In the example above, the action Verify is not available to the user since it was previously verified.

In the order display for an outpatient with inpatient orders, the clinic location and the appointment date and time will display in the screen header area in the same location that the ward and room-bed information displays for an admitted patient.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/036.png) Only users with the appropriate keys will be allowed to take any available actions on the Unit Dose or IV order.

Example: Order View For An Outpatient With Inpatient Orders

ACTIVE UNIT DOSE Nov 28, 2003@10:55:47 Page: 1 of 2

PSJPATIENT3,THREE       Clinic: CLINIC (PAT)

PID: 000-00-0003 Clinic Date: 10/31/03 08:00 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 02/01/55 (48) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: CAPTOPRIL TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 25MG

\*(3)Start: 10/31/2003 08:00

\*(4) Med Route: ORAL (BY MOUTH)

\*(5) Stop: 11/29/2003 12:56

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: BID

\(9\) Admin Times: 08-20

\*(10) Provider: PSJPROVIDER,ONE \[s\] DURATION:

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

CAPTOPRIL 25MG TABS 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen//

## Order Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Order Actions are the actions available in the Action Area of the List Manager Screen. These actions pertain to the patient’s orders and include editing, discontinuing, verifying, etc.

### Discontinue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an order is discontinued, the order’s Stop Date/Time is changed to the date/time the action is taken. An entry is placed in the order’s Activity Log recording who discontinued the order and when the action was taken. Pending and Non-verified orders are deleted when discontinued and will no longer appear on the patient’s profile.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/037.png)Note: Any orders placed through the Med Order Button cannot be discontinued.

Example: Discontinue an Order

ACTIVE IV Mar 20, 2001@16:37:49 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1) Additives: Order number: 65 Type: ADMIXTURE \<DIN\>

POTASSIUM CHLORIDE 40 MEQ

\*(2) Solutions:

0.9% SODIUM CHLORIDE 1000 ML

Duration: \*(4) Start: 03/19/2001 11:30

\*(3) Infusion Rate: 100 ml/hr

\*(5) Med Route: IV \*(6) Stop: 03/26/2001 24:00

\*(7) Schedule: Last Fill: 03/19/2001 14:57

\(8\) Admin Times: Quantity: 2

\*(9) Provider: PSJPROVIDER,ONE \[w\] Cum. Doses: 43

\(10\) Other Print:

\(11\) Remarks :

Entry By: PSJPROVIDER,ONE Entry Date: 03/19/01 11:30

Enter ?? for more actions

DC Discontinue RN Renew FL Flag

ED Edit OC On Call

HD Hold AL Activity Logs

Select Item(s): Quit// DC Discontinue

NATURE OF ORDER: WRITTEN// \<Enter\> W

Requesting PROVIDER: PSJPROVIDER,ONE // \<Enter\> PROV

REASON FOR ACTIVITY: TESTING

DISCONTINUED IV Mar 20, 2001@16:38:28 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1) Additives: Order number: 65 Type: ADMIXTURE \<DIN\>

POTASSIUM CHLORIDE 40 MEQ

\*(2) Solutions:

0.9% SODIUM CHLORIDE 1000 ML

Duration: \*(4) Start: 03/19/2001 11:30

\*(3) Infusion Rate: 100 ml/hr

\*(5) Med Route: IV \*(6) Stop: 03/20/2001 16:38

\*(7) Schedule: Last Fill: 03/19/2001 14:57

\(8\) Admin Times: Quantity: 2

\*(9) Provider: PSJPROVIDER,ONE \[w\] Cum. Doses: 43

\(10\) Other Print:

\(11\) Remarks :

Entry By: PSJPROVIDER,ONE Entry Date: 03/19/01 11:30

Enter ?? for more actions

DC (Discontinue) RN (Renew) FL Flag

ED (Edit) OC (On Call)

HD (Hold) AL Activity Logs

Select Item(s): Quit// \<Enter\> QUIT

When an action of DC (Discontinue) is taken on one child order that is part of a Complex Order, a message will display informing the user that the order is part of a Complex Order, and the user is prompted to confirm that the action will be taken on all of the associated child orders.

Example: Discontinue a Complex Order

ACTIVE UNIT DOSE Feb 25, 2004@21:25:50 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: ASPIRIN TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 650MG

Duration: \*(3)Start: 03/26/2001 14:40

\*(4) Med Route: ORAL

\*(5) Stop: 03/28/2001 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QDAILY

\(9\) Admin Times: 1440

\*(10) Provider: PSJPROVIDER,ONE \[es\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ASPIRIN BUFFERED 325MG TAB 2

\+ Enter ?? for more actions

DC Discontinue ED (Edit) AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// \<Enter\>

Select Item(s): Next Screen// DC Discontinue

This order is part of a complex order. If you discontinue this order the

following orders will be discontinued too (unless the stop date has already

been reached).

Press Return to continue... \<Enter\>

CAPTOPRIL TAB C 03/26 03/27 N

Give: 25MG PO QDAILY

CAPTOPRIL TAB C 03/26 03/29 N

Give: 100MG PO TID

Press Return to continue... \<Enter\>

Do you want to discontinue this series of complex orders? Yes//

### Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows modification of any field shown on the order view that is preceded by a number in parenthesis (#).

Example: Edit an Order

ACTIVE UNIT DOSE Sep 13, 2000 15:20:42 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: AMPICILLIN CAP

Instructions:

\*(2)Dosage Ordered: 500MG

Duration: \*(3)Start: 09/07/2000 15:00

\*(4) Med Route: ORAL

\*(5) Stop: 09/21/2000 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QID

\(9\) Admin Times: 01-09-15-20

\*(10) Provider: PSJPROVIDER,ONE \[es\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

AMPICILLIN 500MG CAP 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL (Flag) VF Verify

Select Item(s): Next Screen//

If a field marked with an asterisk (\*) to the left of the number is changed, the original order will be discontinued, and a new order containing the edited data will be created. The Stop Date/Time of the original order will be changed to the date/time the new edit order is accepted. The old and new orders are linked and may be viewed using the History Log function. When the screen is refreshed, the field(s) that was changed will now be shown in blinking reverse video and “This change will cause a new order to be created” will be displayed in the message window.

If the Dispense Drug or Orderable Item has a non-formulary status, this status will be displayed on the screen as “\*N/F\*” beside the Dispense Drug or Orderable Item.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/038.png)Note: The first time a field marked with an asterisk (\*) is selected for editing, if CPRS Provider Overrides and/or Pharmacist Interventions exist for the order, entering Y (Yes) at the prompt: “Order Check Overrides/Interventions exist for this order. Display? (Y/N)? Y//” displays the following:

Heading information first, followed by a summary of the Current CPRS Order Checks overridden by the Provider, as well as the Overriding Provider, plus title, Override Entered By, plus title, Date/Time Entered, and the Override Reason.

Example: Edit an Order with Provider Overrides/Interventions

============================================================================

\*\* Current Provider Overrides for this order \*\*

============================================================================

Overriding Provider: PSJPROVIDER,ONE (PROVIDER)

Override Entered By: PSJPROVIDER,ONE (PROVIDER)

Date/Time Entered: 07/11/11 09:45

Override Reason: testing functionality of PO & PI

CRITICAL drug-drug interaction: TAMOXIFEN CITRATE 10MG TAB and WARFARIN NA

(GOLDEN STATE) 1MG TAB \[ACTIVE\] - The concurrent use of tamoxifen or

toremifene may increase the effects of anticoagulants. - Monograph Available

SIGNIFICANT drug-drug interaction: TAMOXIFEN CITRATE 10MG TAB and

THIORIDAZINE HCL 10MG TAB \[UNRELEASED\] - Concurrent use of inhibitors of CYP

P-450-2D6 may decrease the effectiveness of tamoxifen in preventing breast

cancer recurrence. Concurrent use of amiodarone or thioridazine may increase

the risk of potentially life-threatening cardiac arrhythmias, including

torsades de pointes. - Monograph Available

Press RETURN to Continue or '^' to Exit :

============================================================================

\*\* Current Pharmacist Interventions for this order \*\*

============================================================================

Intervention Date/Time: 07/11/11 09:50

Pharmacist: PSJPHARMACIST,ONE Drug: TAMOXIFEN CITRATE 10MG TAB

Instituted By: PHARMACY

Intervention: CRITICAL DRUG INTERACTION

Originating Package: INPATIENT

Once a Complex Order is made active, the following fields may <u>not</u> be edited:

- ADMINISTRATION TIME
- Any field where an edit would cause a new order to be created. These fields are denoted with an asterisk in the Detailed View of a Complex Order.

If a change to one of these fields is necessary, the Complex Order must be discontinued and a new Complex Order must be created.

Example: Edit an Order (continued)

NON-VERIFIED UNIT DOSE Sep 13, 2000 15:26:46 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: AMPICILLIN CAP

Instructions:

\*(2)Dosage Ordered: 500MG

Duration: \*(3)Start: 09/13/2000 20:

\*(4) Med Route: ORAL

\*(5)Stop: 09/27/2000 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QID

\(9\) Admin Times: 01-09-15-20

\*(10) Provider: PSJPROVIDER,ONE

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

AMPICILLIN 500MG CAP 1

\+ This change will cause a new order to be created.

ED Edit AC ACCEPT

Select Item(s): Next Screen//

If the ORDERABLE ITEM or DOSAGE ORDERED fields are edited, the Dispense Drug data will not be transferred to the new order. If the Orderable Item is changed, data in the DOSAGE ORDERED field will not be transferred. New Start Date/Time, Stop Date/Time, Login Date/Time, and Entry Code will be determined for the new order. Changes to other fields (those without the asterisk) will be recorded in the order’s activity log.

If the DISPENSE DRUG is edited, an entry in the order’s activity log is made to record the change.

If an Orderable Item or Dispense Drug are edited, Enhanced Order Checks are performed.

<span id="P73_EditanOrder1" class="anchor"></span>Example: Edit an Order (continued)

<u>Inpatient Order Entry Apr 28, 2021@12:54:03 Page: 1 of 2</u>

FROPATNM,MISTER Ward: GEN MED A

PID: 123-33-4444 Room-Bed: A-5 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 12/11/78 (42) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 04/23/21

Dx: THIS IS ADMITTING DIAGNOSIS Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 NAPROXEN TAB C 04/28/2021 05/12/2021 A

Give: 250MG PO BID

2 WARFARIN TAB C 04/28/2021 05/12/2021 A

Give: 2MG PO BID

3 HALOPERIDOL TAB O 04/27/2021 05/11/2021 A

Give: 1MG PO NOW

4 AMIKACIN INJ,SOLN P 04/28/2021 05/12/2021 A

Give: 500MG/2ML IV BID2 PRN

\- - - - - - - - RECENTLY DISCONTINUED/EXPIRED (LAST 72 HOURS) - - - - - - - -

5 AMIKACIN INJ,SOLN C 04/28/2021 04/28/2021 D

\+ Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen// SO Select Order

Select ORDERS (1-5): 2

<u>ACTIVE UNIT DOSE Apr 28, 2021@13:02:03 Page: 1 of 2</u>

FROPATNM,MISTER Ward: GEN MED A

PID: 123-33-4444 Room-Bed: A-5 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 12/11/78 (42) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: WARFARIN TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 2MG

Duration: \*(3)Start: 04/28/2021 12:53

\*(4) Med Route: ORAL (BY MOUTH)

\*(5) Stop: 05/12/2021 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: BID

\(9\) Admin Times: 09-17

\*(10) Provider: PROVIDER,INPAT \[w\]

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

WARFARIN 2MG TABS 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// ED Edit

Select FIELDS TO EDIT: 2

Available Dosage(s)

1\. 2MG

2\. 4MG

Select from list of Available Dosages or Enter Free Text Dose: 2MG// 2 4MG

You entered 4MG is this correct? Yes// YES

<u>NON-VERIFIED UNIT DOSE Apr 28, 2021@13:04:56 Page: 1 of 2</u>

FROPATNM,MISTER Ward: GEN MED A

PID: 123-33-4444 Room-Bed: A-5 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 12/11/78 (42) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: WARFARIN TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 4MG

Duration: \*(3)Start: 04/28/2021 13:05

\*(4) Med Route: ORAL (BY MOUTH)

\*(5) Stop: 05/12/2021 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: BID

\(9\) Admin Times: 09-17

\*(10) Provider: PROVIDER,INPAT \[w\]

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

WARFARIN 2MG TABS 1

\+ This change will cause a new order to be created.

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

--------------------------------------------------------------------------------\*\*\*\*\* WARNING \*\*\*\*\*WARFARIN is hazardous to handle and dispose. Please take theappropriate handling and disposal precautions.--------------------------------------------------------------------------------

Press Return to continue:

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

NATURE OF ORDER: SERVICE CORRECTION// S

...discontinuing original order...

...creating new order...(you will now work on this new order).

![](inpatient-medications-nurse-s-user-manual-psj-5-423/039.png)Note: Bolded warning text above may appear after the Accept command (AC) is entered for medications that are marked as Hazardous to Handle and/or Hazardous to Dispose in the National Drug files.

### IV Bag/Label Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes IV Parameters in Bar Code Medication Administration (BCMA).

The BCMA IV bag/label parameters determine the status of an order’s IV labels after an IV order is edited. The BCMA IV parameters are used to determine if an order’s previously printed IV labels are valid (or invalid) after an edit occurs.

BCMA IV parameters are defined primarily by division, and may also be defined by ward location. If no parameters have been defined for a given ward, orders associated with that ward will use the IV parameters for the division associated with the ward.

The following fields are available in the BCMA IV parameters on the IV Order Entry screen:

- Additive
- Strength
- Bottle
- Solution
- Volume
- Infusion Rate
- Med Route
- Schedule
- Admin Time
- Remarks
- Other Print Info
- Provider
- Start Date/Time
- Stop Date/Time
- Provider Comments.

Each field offers a selection of Warning, Non-Verify, and Invalid Bag.

- If a field is set to Warning, and an order is changed, the IV bags from the old order are carried to the new order and are available on the BCMA VDL. When a nurse scans the bar code on an IV bag, a Warning message alerts them about fields that have changed.
- If a field is set to Non-Verify, and an order is changed, the IV bags from the old order are carried to the new order and are available on the BCMA VDL. When a nurse scans the bar code on an IV bag, NO warning message displays.
- If a field is set to Invalid Bag, and an order is changed, the IV bags from the old order do not carry to the new order or display on the BCMA VDL.

#### Editing Orders when an Invalid IV Bag Event Occurs

The pharmacist is provided a list of invalidated IV bags when an Invalid Bag event has occurred.

An Invalid Bag event occurs when both of the following conditions are met:

- A change is made to any IV order field that matches a BCMA IV Bag site parameter field that is set to “Invalid Bag.”
- IV labels were available for the order prior to the change.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/040.png)Note: Order changes may originate in Inpatient Medications or CPRS.

If an Invalid Bag event occurs, the following is displayed after the edited order’s status is changed to ACTIVE:

- The edited field that triggered the IV bags to be invalidated
- The Date and time of each invalidated IV label
- The label ID of each invalidated IV bag
- The status of each invalidated IV bag
- The Count status of each invalidated IV bag.
- The BCMA Action – Date/Time of each invalidated IV bag

Example: Invalid Labels Cannot be Reprinted or Scanned

Is this O.K.: Y// y YES

NATURE OF ORDER: SERVICE CORRECTION// sERVICE CORRECTION S

\*\* Edit to PROVIDER has caused the following IV labels to be invalidated \*\*

(Invalid IV labels cannot be reprinted or marked as Infusing in BCMA)

Label Date/Time Unique ID Status Count BCMA Action-Date/Time

--------------- -------- --------- ----- -----------------------

09/14/12 16:06 91V149 YES

09/14/12 16:06 91V150 YES

09/14/12 16:06 91V151 YES

A pause occurs before the display scrolls to the top of the screen.

After the user enters “YES,” a prompt to print a list of Invalidated IV labels to a device or RETURN to continue displays.

Example: Prompt to Print

Enter 'P' to print list of Invalidated Labels or RETURN to continue: p  PRINT

DEVICE: HOME// 

When P is entered at the “Enter P” prompt, the following is displayed in the report:

- Location (current Ward or Clinic)
- Patient Name
- Medication (IV Additive, IV Solution, or Orderable Item)
- Date/time
- V# of the IV bag
- Status
- Count
- BCMA Action-Date/time

Example: List of Invalidated Labels Report

Enter 'P' to print list of Invalidated Labels or RETURN to continue: p

PRINT DEVICE

DEVICE: HOME// SSH VIRTUAL TERMINAL Right Margin: 80//

\* Invalidated IV Labels \*

Patient: BANPATNM,JAMES E Location: BECKY'S CLINIC

Additive(s): CEFAMANDOLE 20 GM

Solution(s): DEXTROSE 10% 1000 ML

Label Date/Time Unique ID Status Count BCMA Action-Date/Time

--------------- -------- --------- ----- -----------------

09/14/12 16:06 91V149 YES

09/14/12 16:06 91V150 YES

09/14/12 16:06 91V151 YES

When the screen is full, a pause for the report output occurs, if the user selects the device option to print to the screen.

When an invalid bag event occurs, all IV labels associated with the edited order that have not already been invalidated are invalidated. IV labels that were previously invalidated as a result of prior edits are not displayed.

Following the “REASON FOR ACTIVITY:” prompt, the “Print new replacement labels? NO// Y” prompt displays to allow the pharmacist to print replacement labels when the following conditions occur:

- A non-starred field is changed.
- The IV parameter is set to Invalid Bag for an edited field.

Example: Print New Replacement IV Labels

REASON FOR ACTIVITY: test

Print new replacement labels? NO// YES

8 Labels needed for doses due at ...

IV labels printed prior to an order edit are displayed as available when edits are made to fields set to Warning or Non-Verify in the BCMA IV Parameters.

Example: IV Labels Available and Print New Replacement Labels

The following IV labels are available: 

 

Label Date/Time   Unique ID             Status   

08/02/12 09:57    8157V178                 

08/02/12 09:57    8157V179                  

08/02/12 09:57    8157V180                  

08/02/12 09:57    8157V181                 

08/02/12 09:57    8157V182  

Print new replacement labels? N// Y                 

The BCMA availability of IV bags may be viewed using the Label Log action. All IV labels that have been invalidated are displayed in the label log file with “NO” in the “Available in BCMA” column.

The label log file displays the status of the IV label as either available or not available in BCMA.

Example: Label Log Display

(A)ctivity (L)abel (H)istory (I)nstructions History: Label Log

LABEL LOG:

\# DATE/TIME ACTION USER \#LABELS TRACK COUNT

================================================================================

1 FEB 26,2013@16:69:53

DISPENSED HARRIS,JAMES 3 ORDER ACTION YES

Enter RETURN to continue or '^' to exit:

Unique IDs for this order:

Available

Label Date/Time Unique ID in BCMA Status Count BCMA Action-Date/Time

02/25/13 15:36 197V6411 NO YES

02/25/13 15:36 197V6410 NO YES

02/25/13 15:36 197V6409 NO YES

(A)ctivity (L)abel (H)istory (I)nstructions History:

Labels will not be available in BCMA under the following conditions:

- When the status is Reprint, Recycled, Destroyed or Cancelled.
- When the action is Given, Infusing, Stopped or Completed.
- When an Invalid Bag Event has occurred.

After the above information is displayed in the label log, the below prompt displays for associated linked orders, if they exist. The default is “Y//.”

Example: Associated Linked Orders Prompt

Do you wish to see labels from linked (edited) orders? Y//

The clinic location’s abbreviation, or the full clinic name if no abbreviation exists, prints on the IV label when the CLINIC field (#126) is populated. The ward location name is printed when the CLINIC field is null. The name “OPT. IV.” is printed if neither the clinic location name nor the ward location name is populated.

### Verify

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Orders must be accepted and verified before they can become active and are included on the pick list, BCMA VDL, etc. If AUTO-VERIFY is enabled for the nurse, new orders immediately become active after entry or finish (pending orders entered through CPRS). Orders verified by nursing prior to pharmacy verification are displayed on the profile under the active header marked with an arrow (-\>) to the right of the order number. When verify is selected and when the order has not been verified by the pharmacist, the nurse must enter any missing data and correct any invalid data before the verification is accepted.

When an action of VF (Verify) is taken on one child order that is part of a Complex Order, a message will display informing the user that the order is part of a Complex Order, and the user is prompted to confirm that the action will be taken on all of the associated child orders.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/041.png)Note: Orders that have been accepted by the pharmacist will appear on the BCMA VDL if verified by a nurse.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/042.png)Note: The ALLOW AUTO-VERIFY FOR USER field in the INPATIENT USER PARAMETERS file controls AUTO-VERIFY.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/043.png)Note: The user will not be allowed to finish an order that contains a schedule that is considered to be non-standard. Schedules must be selected from the ADMINISTRATION SCHEDULE file, with the following exceptions:

- Schedule containing PRN: (Ex. TID PC PRN). If the schedule contains PRN, the base schedule must be in the ADMINISTRATION SCHEDULE file.
- Day of week schedules (Ex. MO-FR or MO-FR@0900)
- Admin time only schedules (Ex. 09-13)

![](inpatient-medications-nurse-s-user-manual-psj-5-423/044.png)Note: When verifying a unit dose order that contains an Old Schedule Name, the user will have to edit the schedule to the New Schedule Name before they will be able to verify the unit dose order. This does not apply to Old Schedule Names for Day of the Week Schedules.

<span id="Page_75" class="anchor"></span>Verifying Unit Dose Order with Old Schedule Name

<u>NON-VERIFIED UNIT DOSE Apr 25, 2017@11:54:58 Page: 1 of 3</u>

PSJPATIENT,ONE Ward: 7A GEN

PID: 666-09-4321 Room-Bed: 722-C Ht(cm): 165.10 (04/19/17)

DOB: 04/05/44 (73) Att: Psj,Test Wt(kg): 77.11 (04/19/17)

Sex: FEMALE TrSp: Medical Observati Admitted: 04/19/17

Dx: CHEST PAIN Last transferred: \*\*\*\*\*\*\*\*

CrCL: 33.2(est.) (CREAT: 1.5mg/dL 4/19/17) BSA (m2): 1.85

\*(1)Orderable Item: EPOETIN ALFA,RECOMBINANT INJ,SOLN

Instructions: 10000UNIT/1ML

\*(2)Dosage Ordered: 10000UNIT/1ML

Duration: (3)Start: 04/25/17 11:14

\*(4) Med Route: SUBCUTANEOUS REQUESTED START: 04/28/17 09:00

\(5\) Stop: 04/26/17 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q72H

\(9\) Admin Times: 0900

\*(10) Provider: PROVIDER,ONE \[es\]

\(11\) Special Instructions:

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// VF Verify

The schedule Q72H has been replaced with Q3D by the system administrator

after this order was entered.

Please correct the schedule before verifying this order.

Press Return to continue...

*\<User will be taken back to the patient’s profile\>*

If the Dispense Drug or Orderable Item has a non-formulary status, this status will be displayed on the screen as “\*N/F\*” beside the Dispense Drug or Orderable Item.

<span id="Page_75A" class="anchor"></span>Example: Verify an Order

> <u>NON-VERIFIED UNIT DOSE Apr 28, 2021@11:55:58 Page: 1 of 2</u>

> PSJPATIENT1,ONE Ward: GENERAL A

> PID: 000-00-0202 Room-Bed: GENMED-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> DOB: 05/16/70 (50) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> \*(1)Orderable Item: FLUOROURACIL INJ,SOLN

> Instructions:

> \*(2)Dosage Ordered: 50MG/1ML

> Duration: (3)Start: 04/28/2021 13:00

> \*(4) Med Route: SUBCUTANEOUS

> \(5\) Stop: 05/03/2021 22:00

> \(6\) Schedule Type: CONTINUOUS

> \*(8) Schedule: TID

> \(9\) Admin Times: 09-13-17

> \*(10) Provider: McCOY, BONES \[w\]

> \(11\) Special Instructions!: (see below)

> Adding Special Instructions.

> <u>(12) Dispense Drug U/D Inactive Date</u>

> \+ Enter ?? for more actions

> DC Discontinue ED Edit AL Activity Logs

> HD (Hold) RN (Renew)

> FL Flag VF Verify

> Select Item(s): Next Screen// VF Verify

> --------------------------------------------------------------------------------

> \*\*\*\*\* WARNING \*\*\*\*\*

> FLUOROURACIL is hazardous to handle and dispose. Please take the

> appropriate handling and disposal precautions.

> --------------------------------------------------------------------------------

> Press Return to continue:

> Now doing allergy checks. Please wait...

> Now processing Clinical Reminder Order Checks. Please wait ...

> Now Processing Enhanced Order Checks! Please wait...

> Press Return to continue...

> ...a few moments, please.....

> Pre-Exchange DOSES:

> ORDER VERIFIED.

> Type \<Enter\> to continue or '^' to exit:

![](inpatient-medications-nurse-s-user-manual-psj-5-423/045.png)Note: Bolded warning text above may appear, after the Verify command (VF) is entered for medications that are marked as Hazardous to Handle and/or Hazardous to Dispose in the National Drug files.

### Hold

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only active orders may be placed on hold. Orders placed on hold will continue to show under the ACTIVE heading on the profiles until removed from hold. Any orders placed on hold through the pharmacy options cannot be released from hold using any of the CPRS options. An entry is placed in the order’s Activity Log recording the user who placed/removed the order from hold and when the action was taken.

If the Dispense Drug or Orderable Item has a non-formulary status, this status will be displayed on the screen as “\*N/F\*” beside the Dispense Drug or Orderable Item.

Example: Place an Order on Hold

ACTIVE UNIT DOSE Feb 25, 2001@21:25:50 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Att: Psj,Test Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: ASPIRIN TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 650MG

Duration: \*(3)Start: 02/26/01 14:

\*(4) Med Route: ORAL

\*(5) Stop: 02/28/01 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QDAILY

\(9\) Admin Times: 1440

\*(10) Provider: PSJPROVIDER,ONE \[es\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ASPIRIN BUFFERED 325MG TAB 2

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// HD Hold

Do you wish to place this order 'ON HOLD'? Yes// \<Enter\> (Yes)

NATURE OF ORDER: WRITTEN// \<Enter\> W...

COMMENTS:

1\>TESTING

2\>

EDIT Option: . \<Enter\>

Enter RETURN to continue or '^' to exit: \<Enter\>

> -----------------------------------------report continues--------------------------------

Notice that the order shows a status of “H” for hold in the right side of the Aspirin Tablet order below.

Example: Place an Order on Hold (continued)

HOLD UNIT DOSE Feb 25, 2001@21:27:57 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Att: Psj,Test Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: ASPIRIN TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 650MG

Duration: \*(3)Start: 02/26/01 14:40

\*(4) Med Route: ORAL

\*(5) Stop: 02/28/01 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QDAILY

\(9\) Admin Times: 1440

\*(10) Provider: PSJPROVIDER,ONE \[es\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ASPIRIN BUFFERED 325MG TAB 2

\+ Enter ?? for more actions

DC Discontinue ED (Edit) AL Activity Logs

HD Hold RN (Renew)

FL Flag VF (Verify)

Select Item(s): Next Screen// \<Enter\>

HOLD UNIT DOSE Feb 25, 2001@21:28:20 Page: 2 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Att: Psj,Test Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\+

(7)Self Med: NO

Entry By: PSJPROVIDER,ONE Entry Date: 02/25/01 21:25

\(13\) Comments:

TESTING

Enter ?? for more actions

DC Discontinue ED (Edit) AL Activity Logs

HD Hold RN (Renew)

FL Flag VF (Verify)

Select Item(s): Quit// \<Enter\>

Unit Dose Order Entry Feb 25, 2001@21:30:15 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Att: Psj,Test Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE TrSp: Medical Observati Admitted: 05/03/00

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 ASPIRIN TAB C 02/26 02/28 H

Give: 650MG ORAL QDAILY

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P82" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Quit//

### Renew

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Medication orders (referred to in this section as orders) that may be renewed include the following:

- All non-complex active Unit Dose and IV orders.
- Orders that have been discontinued due to ward transfer or treating specialty change.
- Expired orders containing an administration schedule (Unit Dose and scheduled IV orders) that have not had a scheduled administration time since the last BCMA action was taken.
- Expired orders not containing an administration schedule (continuous IV orders) that have had an expired status less than the time limit defined in the EXPIRED IV TIME LIMIT field in the PHARMACY SYSTEM file.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/046.png) Note: Complex Orders may only be renewed if all associated child orders are renewable.

#### Renewing Orders with CPRS Overrides/Pharmacist Interventions

When renewing an order, if CPRS Provider Overrides and/or Pharmacy Interventions exist for the order, entering Y (Yes) at the prompt: “Order Check Overrides/Interventions exist for this order. Display? (Y/N)? Y//” displays the heading information first, followed by a summary of the Current CPRS Order Checks overridden by the Provider.

If current Pharmacist Interventions exist, they will display with the following fields (if populated), Heading, Intervention Date/Time, Provider, Pharmacist, Drug, Instituted By, Intervention, Recommendation, and Originating Package.

Example: Renew an Order with Provider Overrides/Interventions

============================================================================

\*\* Current Provider Overrides for this order \*\*

============================================================================

Overriding Provider: PSJPROVIDER,ONE (PROVIDER)

Override Entered By: PSJPROVIDER,ONE (PROVIDER)

Date/Time Entered: 07/11/11 09:45

Override Reason: testing functionality of PO & PI

CRITICAL drug-drug interaction: TAMOXIFEN CITRATE 10MG TAB and WARFARIN NA

(GOLDEN STATE) 1MG TAB \[ACTIVE\] - The concurrent use of tamoxifen or

toremifene may increase the effects of anticoagulants. - Monograph Available

SIGNIFICANT drug-drug interaction: TAMOXIFEN CITRATE 10MG TAB and

THIORIDAZINE HCL 10MG TAB \[UNRELEASED\] - Concurrent use of inhibitors of CYP

P-450-2D6 may decrease the effectiveness of tamoxifen in preventing breast

cancer recurrence. Concurrent use of amiodarone or thioridazine may increase

the risk of potentially life-threatening cardiac arrhythmias, including

torsades de pointes. - Monograph Available

Press RETURN to Continue or '^' to Exit :

============================================================================

\*\* Current Pharmacist Interventions for this order \*\*

============================================================================

Intervention Date/Time: 07/11/11 09:50

Pharmacist: PSJPHARMACIST,ONE Drug: TAMOXIFEN CITRATE 10MG TAB

Instituted By: PHARMACY

Intervention: CRITICAL DRUG INTERACTION

Originating Package: INPATIENT

![](inpatient-medications-nurse-s-user-manual-psj-5-423/047.png)Note: When Renewing an Order in Inpatient Medications, if Current CPRS Provider Overrides do not exist and Pharmacist Interventions do exist for the order, the following displays:

============================================================================

\*\* Current Provider Overrides for this order \*\*

============================================================================

No Provider Overrides to display

============================================================================

\*\* Current Pharmacist Interventions for this order \*\*

============================================================================

Intervention Date: 07/11/11 14:55

Provider: PSJPROVIDER,ONE Pharmacist: PSJPHARMACIST,ONE

Drug: WARFARIN NA (GOLDEN STATE) 1MG TAB

Instituted By: PHARMACY

Intervention: CRITICAL DRUG INTERACTION

Recommendation: OTHER Originating Package: INPATIENT

Other For Recommendation:

TEST INTERVENTION FOR CRITICAL DRUG-DRUG

![](inpatient-medications-nurse-s-user-manual-psj-5-423/048.png)Note: When renewing a Unit Dose order that contains an Old Schedule Name, the user will be notified of the schedule change and the New Schedule Name. The user will be informed that a renewed order cannot be edited and a new order must be entered. This does not apply to Old Schedule Names for Day of the Week Schedules.

Renewing a Unit Dose Order with Old Schedule Name

<u>ACTIVE UNIT DOSE Apr 25, 2017@14:38:03 Page: 1 of 3</u>

PSJPATIENT,ONE Ward: 7A GEN

PID: 666-09-4321 Room-Bed: 722-C Ht(cm): 165.10 (04/19/17)

DOB: 04/05/44 (73) Att: Psj,Test Wt(kg): 77.11 (04/19/17)

Sex: FEMALE Admitted: 04/19/17

Dx: CHEST PAIN Last transferred: \*\*\*\*\*\*\*\*

CrCL: 33.2(est.) (CREAT: 1.5mg/dL 4/19/17) BSA (m2): 1.85

\*(1)Orderable Item: EPOETIN ALFA,RECOMBINANT INJ,SOLN

Instructions:

\*(2)Dosage Ordered: 3000UNIT/1ML

Duration: \*(3)Start: 04/25/17 14:23

\*(4) Med Route: SUBCUTANEOUS

\*(5) Stop: 07/24/17 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q72H

\(9\) Admin Times: 0900

\*(10) Provider: INPATIENT-MEDS,PROVIDER \[w\]

\(11\) Special Instructions:

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// rn Renew

The schedule Q72H has been replaced with Q3D by the system administrator

after this order was renewed.

WARNING - Renewed RXs cannot be edited. Please enter new order.

Press Return to continue...

*\<User will be taken to the patient’s profile\>*Renewing Active Orders

The following applies when the RN (Renew) action is taken on any order with a status of “Active”:

- A new Default Stop Date/Time is calculated for the order using the same calculation applied to new orders. The starting point of the Default Stop Date/Time calculation is the date and time that the order was signed in CPRS or the date and time that the RN (Renew) action was taken in Inpatient Medications.
- The RN (Renew) action does not create a new order.
- The Start Date/Time is not available for editing when an order is renewed.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/049.png)Note: Orders having a schedule type of One-Time or On Call must have a status of “Active” in order to be renewed.

Renewing Discontinued Orders

IV and Unit Dose orders that have been discontinued, either through the (DC) Discontinue action or discontinued due to edit, cannot be renewed.

IV and Unit Dose medication orders that have been discontinued due to ward transfer or treating specialty change will allow the (RN) Renew action.

Renewing Expired Unit Dose Orders

The following applies to expired Unit Dose orders having a schedule type of Continuous or PRN.

1.  The RN (Renew) action will not be available on an order with a status of “Expired” if either of the following two conditions exist:
    1.  If the difference between the current system date and time and the last scheduled administration time is greater than the frequency of the schedule. This logic will be used for schedules with standard intervals (for example, Q7H).
    2.  If the current system date and time is greater than the time that the next dose is due. This logic is used for schedules with non-standard intervals (for example, Q6H – 0600-1200-1800-2400).
2.  A new Default Stop Date/Time is calculated for the order using the same calculation applied to new orders. The starting point of the Default Stop Date/Time calculation is the date and time that the order was signed in CPRS or the date and time that the RN (Renew) action was taken in Inpatient Medications.
3.  The (RN) Renew action does not create a new order.
4.  The Start Date/Time is not available for editing when an order is renewed.
5.  The renewed order has a status of “Active.”

Renewing Expired Scheduled IV Orders

The following applies to only IV orders that have a scheduled administration time.

1.  The RN (Renew) action is not available on a scheduled IV order with a status of “Expired” if either of the following two conditions exist:
1.  If the difference between the current system date and time and the last scheduled administration time is greater than the frequency of the schedule. This logic is used for schedules with standard intervals (for example, Q7H).
2.  If the current system date and time is greater than the time that the next dose is due. This logic is used for schedules with non-standard intervals (for example, Q6H – 0600-1200-1800).
6.  A new Default Stop Date/Time is calculated for the order using the same calculation applied to new orders. The starting point of the Default Stop Date/Time calculation is the date and time that the order was signed in CPRS or the date and time that the RN (Renew) action was taken in Inpatient Medications.
7.  The RN (Renew) action does not create a new order.
8.  The Start Date/Time is not available for editing when an order is renewed.
9.  The renewed order has a status of “Active.”

Renewing Expired Continuous IV Orders

The following applies to IV orders that do not have a scheduled administration time.

1.  For Continuous IV orders having a status of “Expired,” the “Expired IV Time Limit” system parameter controls whether or not the RN (Renew) action is available. If the number of hours between the expiration date/time and the current system date and time is less than this parameter, the RN (Renew) action is allowed. This parameter has a range of 0 to 24 hours, and may be changed using the PARameters Edit Menu option.
10. If the RN (Renew) action is taken on a renewable continuous IV order, a new Default Stop Date/Time is calculated using existing Default Stop Date/Time calculations. The starting point of the Default Stop Date/Time calculation is the date and time that the order was signed in CPRS or the date and time that the RN (Renew) action was taken in Inpatient Medications.
11. The RN (Renew) action does not create a new order.
12. The Start Date/Time is not available for editing when an order is renewed.
13. The renewed order has a status of “Active.”

Renewing Complex Orders

When an action of RN (Renew) is taken on one child order that is part of a Complex Order, a message will display informing the user that the order is part of a Complex Order, and the user is prompted to confirm that the action will be taken on all of the associated child orders.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/050.png)Notes:

> Only Complex Orders created with the conjunction AND will be available for renewal.

> Orders created by checking the “Give additional dose now” box in CPRS, when ordered in conjunction with a Complex Order, will not be available for renewal.

Example: Renew a Complex Order

ACTIVE UNIT DOSE Feb 25, 2004@21:25:50 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: ASPIRIN TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 650MG

Duration: \*(3)Start: 03/26/2001 14:40

\*(4) Med Route: ORAL

\*(5) Stop: 03/28/2001 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QDAILY

\(9\) Admin Times: 1440

\*(10) Provider: PSJPROVIDER,ONE \[es\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ASPIRIN BUFFERED 325MG TAB 2

\+ Enter ?? for more actions

DC Discontinue ED (Edit) AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// RN Renew

This order is part of a complex order. If you RENEW this order the

following orders will be RENEWED too.

Press Return to continue... \<Enter\>

DIGOXIN TAB C 03/26 03/29 A

Give: 200MG PO BID

DIGOXIN TAB C 03/26 03/28 A

Give: 100MG PO TID

Press Return to continue... \<Enter\>

RENEW THIS COMPLEX ORDER SERIES? YES//

Viewing Renewed Orders

The following outlines what the user may expect following the renewal process:

1.  The patient profile will contain the most recent renewal date in the Renewed field.
3.  The patient detail will contain the most recent renewal date and time in the Renewed field.
4.  The Activity Log will display the following:
- ORDER EDITED activity, including the previous Stop Date/Time and the previous Provider (if a new Provider is entered at the time the order is renewed).
- ORDER RENEWED BY PHARMACIST activity, including the pharmacist that renewed the order and the date and time that the RN (Renew) action was taken.

Example: Renewed Order in Profile View

Inpatient Order Entry Feb 25, 2004@21:25:50 Page: 1 of 1

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (83) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/00

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 ASPIRIN TAB 650 C 03/26/2004 03/28/2004 A

Give: 650MG PO QDAILY Renewed: 03/27/2004

 

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Quit// 1

Example: Renewed Order in Detailed Order View

ACTIVE UNIT DOSE Feb 25, 2004@21:25:50 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: ASPIRIN TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 650MG

Duration: \*(3)Start: 03/26/2004 14:40

\*(4) Med Route: ORAL Renewed: 03/27/2004 11:00

\*(5) Stop: 03/28/2004 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QDAILY

\(9\) Admin Times: 1440

\*(10) Provider: PSJPROVIDER,ONE \[es\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ASPIRIN BUFFERED 325MG TAB 2

\+ Enter ?? for more actions

DC Discontinue ED (Edit) AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen//

ACTIVE UNIT DOSE Feb 25, 2004@21:28:20 Page: 2 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\+

(7)Self Med: NO

Entry By: PSJPROVIDER,ONE Entry Date: 03/25/04 21:25

Renewed By: PSJPROVIDER,ONE

\(13\) Comments:

TESTING

Enter ?? for more actions

DC Discontinue ED (Edit) AL Activity Logs

HD Hold RN (Renew)

FL (Flag) VF (Verify)

Select Item(s): Quit// \<Enter\>Discontinuing a Pending Renewal

When a pharmacist attempts to discontinue a pending renewal, the following message displays.

This order is in a pending status. If this pending order is discontinued, the original order will still be active.

If this occurs, a pharmacist may discontinue a pending order, both orders, or exit the discontinue function. When a pending renewal is discontinued, the order will return to its previous status.

Orders That Change Status During Process of Renew

Orders that are active during the renewal process but become expired during the pharmacy finishing process follow the logic described in Renewing Expired Unit Dose Orders, Renewing Expired Scheduled IV Orders, and Renewing Expired Continuous IV Orders.

### Activity Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows viewing of a long or short activity log, dispense log, history log, or instructions history of the order. A short activity log only shows actions taken on orders and does not include field changes. The long activity log shows actions taken on orders and does include the requested Start and Stop Date/Time values. If a history log is selected, it will find the first order, linked to the order where the history log was invoked. Then the log will display an order view of each order associated with it, in the order that they were created. If an instructions history log is selected, it will find the first order linked to the order where the history log was invoked from, then show each incremental change to the instructions in the order they were created. When a dispense log is selected, it shows the dispensing information for the order.

Example: Activity Log

ACTIVE UNIT DOSE Sep 21, 2000 12:44:25 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: AMPICILLIN CAP

Instructions:

\*(2)Dosage Ordered: 500MG

Duration: \*(3)Start: 09/07/2000 15:00

\*(4) Med Route: ORAL

\*(5) Stop: 09/21/2000 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QID

\(9\) Admin Times: 01-09-15-20

\*(10) Provider: PSJPROVIDER,ONE \[es\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

AMPICILLIN 500MG CAP 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF Verify

Select Item(s): Next Screen// AL Activity Logs

1 - Short Activity Log

2 - Long Activity Log

3 - Dispense Log

4 - History Log

5 – Instructions History

Select LOG to display: 2 Long Activity Log

Date: 09/07/00 14:07 User: PSJPHARMACIST,ONE

Activity: ORDER VERIFIED BY PHARMACIST

Date: 09/07/00 14:07 User: PSJPHARMACIST,ONE

Activity: ORDER VERIFIED

Field: Requested Start Date

Old Data: 09/07/00 09:00

Date: 09/07/00 14:07 User: PSJPHARMACIST,ONE

Activity: ORDER VERIFIED

Field: Requested Stop Date

Old Data: 09/07/00 24:00

Enter RETURN to continue or '^' to exit:

### Finish

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-nurse-s-user-manual-psj-5-423/051.png) Nurses who hold the PSJ RNFINISH key will have the ability to finish and verify Unit Dose orders placed through CPRS.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/052.png) Nurses who hold the PSJI RNFINISH key will have the ability to finish and verify IV orders placed through CPRS.

When an order is placed or renewed by a provider through CPRS, the nurse or pharmacist needs to finish and/or verify this order. The same procedures are followed to finish the renewed order as to finish a new order with the following exceptions:

> The PENDING RENEWAL orders may be speed finished from within the Unit Dose *Order Entry* option. The user may enter an SF, for speed finish, at the “Select ACTION:” prompt and then select the pending renewals to be finished. A prompt is issued for the Stop Date/Time. This value is used as the Stop Date/Time for the pending renewals selected. All other fields will retain the values from the renewed order.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/053.png)Note: Order Checks happen during the finish process.

When an action of FN (Finish) is taken on one child order that is part of a Complex Order, a message will display informing the user that the order is part of a Complex Order, and the user is prompted to confirm that the action will be taken on all of the associated child orders.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/054.png)Note: Complex orders cannot be speed finished because it may not be appropriate to assign the same stop date to all components of a complex order.

Example: Complex Unit Dose Orders with Overlapping Administration Times

When finishing (FN) a complex unit dose drug order with overlapping admin times, after you select the order, a warning message is displayed with the warning and the overlapping admin times.

\*\*WARNING\*\*

The highlighted admin times for these portions of this complex order overlap.

Part 1 has a schedule of BID and admin time(s) of 10-22.

AND

Part 2 has a schedule of QDAY and admin time(s) of 10.

Please ensure the schedules and administration times are appropriate.

Press Return to continue...

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P89" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen//

To finish the order, you must correct the order so that there are no overlapping admin times.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/055.png)Note: When finishing a unit dose order that contains an Old Schedule Name, the software will replace it with the New Schedule Name. This does not apply to Old Schedule Names for Day of the Week Schedules.

<span id="p79" class="anchor"></span>Finishing Unit Dose Order with Old Schedule Name

<u>PENDING UNIT DOSE (ROUTINE) Apr 20, 2017@11:15:51 Page: 1 of 3</u>

PSJPATIENT,ONE Ward: 7A GEN

PID: 666-09-4321 Room-Bed: 722-C Ht(cm): 165.10 (04/19/17)

DOB: 04/05/44 (73) Att: Psj,Test Wt(kg): 77.11 (04/19/17)

\*(1)Orderable Item: EPOETIN ALFA,RECOMBINANT INJ,SOLN

Instructions: 20000UNIT/2ML

\*(2)Dosage Ordered: 20000UNIT/2ML

Duration: (3)Start: 04/20/17 11:14

\*(4) Med Route: SUBCUTANEOUS REQUESTED START: 04/23/17 09:00

\(5\) Stop: 04/26/17 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q72H

\(9\) Admin Times: 0900

\*(10) Provider: PROVIDER,ONE \[es\]

\(11\) Special Instructions: <u>(12) Dispense Drug U/D Inactive Date</u>

EPOETIN ALPHA, RECOMB 2000 UNT/ML INJ 1

\+ Enter ?? for more actions

BY Bypass FL (Flag)

DC Discontinue FN Finish

Select Item(s): Next Screen// FN Finish

The schedule Q72H has been replaced with Q3D by the system administrator

after this order was entered.

Do you wish to continue with the current order? YES//

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

<u>NON-VERIFIED UNIT DOSE Apr 20, 2017@11:20 Page: 1 of 3</u>

PSJPATIENT,ONE Ward: 7A GEN

PID: 666-09-4321 Room-Bed: 722-C Ht(cm): 165.10 (04/19/17)

DOB: 04/05/44 (73) Att: Psj,Test Wt(kg): 77.11 (04/19/17)

\*(1)Orderable Item: EPOETIN ALFA,RECOMBINANT INJ,SOLN

Instructions: 20000UNIT/2ML

\*(2)Dosage Ordered: 20000UNIT/2ML

Duration: (3)Start: 04/20/17 11:14

\*(4) Med Route: SUBCUTANEOUS REQUESTED START: 04/23/17 09:00

\(5\) Stop: 04/26/17 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q3D

\(9\) Admin Times: 0900

\*(10) Provider: PROVIDER,ONE \[es\]

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

EPOETIN ALFA,RECOMBINANT 10000UNT/ML INJ 2

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen//AC

When finishing the order which contains an Old Schedule Name, the user will be notified that the schedule within the order has been replaced with a new name and asked if they wish to continue with the current order. If the user chooses to continue, the software will replace the old schedule name with the new schedule name in the order. If the user chooses not to continue, the software will return them to the pending unit dose order screen .

![](inpatient-medications-nurse-s-user-manual-psj-5-423/056.png)Note: When finishing a pending renewal for a Unit Dose order that contains an Old Schedule Name, the user will be notified of the schedule change and the New Schedule Name. The user will be informed that a renewed order cannot be edited and a new order must be entered. This does not apply to Old Schedule Names for Day of the Week Schedules.

Pending Renewal for Unit Dose Order with Old Schedule Name

<u>PENDING UNIT DOSE (ROUTINE) Apr 25, 2017@14:44:47 Page: 1 of 3</u>

PSJPATIENT,ONE Ward: 7A GEN

PID: 666-09-4321 Room-Bed: 722-C Ht(cm): 165.10 (04/19/17)

DOB: 04/05/44 (73) Wt(kg): 77.11 (04/19/17)

\*(1)Orderable Item: EPOETIN ALFA,RECOMBINANT INJ,SOLN

Instructions: 2000UNIT/1ML

\*(2)Dosage Ordered: 2000UNIT/1ML

Duration: (3)Start: 04/25/2017 14:10

\*(4) Med Route: SUBCUTANEOUS Renewed: 04/25/2017 14:19

\(5\) Stop: 05/02/2017 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q72H

\(9\) Admin Times: 0900

\*(10) Provider: PROVIDER,ONE \[es\]

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

EPOETIN ALPHA, RECOMB 2000 UNT/ML INJ 1

\+ Enter ?? for more actions

BY Bypass FL (Flag)

DC Discontinue FN Finish

Select Item(s): Next Screen// FN Finish

The schedule Q72H has been replaced with Q3D by the system administrator

after this order was renewed.

WARNING - Renewed RXs cannot be edited. Please enter new order.

Press Return to continue...

*\<User will be taken back to the detailed order screen\>*

![](inpatient-medications-nurse-s-user-manual-psj-5-423/057.png)Note: When finishing an order, if CPRS Order Checks/Provider Overrides and Pharmacist Interventions exist, they will display during the finish process. Heading information displays first, followed by a summary of the Current CPRS Order Checks overridden by the Provider, as well as the Overriding Provider, plus title, Override Entered By, plus title, Date/Time Entered, and the Override Reason.

Example: Finish an Order with Provider Overrides/Interventions

============================================================================

\*\* Current Provider Overrides for this order \*\*

============================================================================

Overriding Provider: PSJPROVIDER,ONE (PROVIDER)

Override Entered By: PSJPROVIDER,ONE (PROVIDER)

Date/Time Entered: 07/11/11 17:40

Override Reason: Provider gave permission to administer

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN NA

(GOLDEN STATE) 1MG TAB \[ACTIVE\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

![](inpatient-medications-nurse-s-user-manual-psj-5-423/058.png)Note: If no Current CPRS Provider Overrides were entered at the time the order was created in CPRS, they will NOT display during finishing, and no heading or messages will display when finishing the Pending order in Inpatient Medications.

Example: Finish an Order Without a Duration

PENDING IV (ROUTINE) Sep 07, 2000 16:11:42 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\(1\) Additives: Type:

\(2\) Solutions:

Duration: (4) Start: \*\*\*\*\*\*\*\*

\(3\) Infusion Rate:

REQUESTED START: 09/07/2000 09:00

\*(5) Med Route: IVPB (6) Stop: \*\*\*\*\*\*\*\*

\*(7) Schedule: QID Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 01-09-15-20 Quantity: 0

\*(9) Provider: PSJPROVIDER,ONE \[es\] Cum. Doses:

\*(10)Orderable Item: AMPICILLIN INJ

Instructions:

\(11\) Other Print:

Provider Comments: THIS IS AN INPATIENT IV EXAMPLE.

\+ Enter ?? for more actions

DC Discontinue FL (Flag)

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

COMPLETE THIS ORDER AS IV OR UNIT DOSE? IV// IV

Copy the Provider Comments into Other Print Info? Yes// YES

IV TYPE: PB

CHOOSE FROM:

A ADMIXTURE

C CHEMOTHERAPY

H HYPERAL

P PIGGYBACK

S SYRINGE

Enter a code from the list above.

Select one of the following:

A ADMIXTURE

C CHEMOTHERAPY

H HYPERAL

P PIGGYBACK

S SYRINGEIV TYPE: PIGGYBACK

\*\*AUTO STOP 7D\*\*

This patient is already receiving an order for the following drug in the same

class as AMPICILLIN INJ 2GM:

AMPICILLIN CAP C 09/07 09/21 A

Give: 500MG PO QID

Do you wish to continue entering this order? NO// Y

Select ADDITIVE: AMPICILLIN// \<Enter\>

ADDITIVE: AMPICILLIN// \<Enter\>

Restriction/Guideline(s) exist. Display? : (N/D): No// D

Dispense Drug Text:

Refer to PBM/MAP PUD treatment guidelines

RESTRICTED TO NEUROLOGY

(The units of strength for this additive are in GM)

Strength: 1 GM

Select ADDITIVE: \<Enter\>

Select SOLUTION: 0.9

1 0.9% NACL 500 ML

2 0.9% NACL 100 ML

3 0.9% NACL 50 ML

4 0.9% NaCl 250 ML

BT

CHOOSE 1-4: 2 0.9% NACL 100 ML

INFUSION RATE: \<Enter\>

> -----------------------------------------report continues-------------------------------

![](inpatient-medications-nurse-s-user-manual-psj-5-423/059.png)Note: When the CPRS patch, OR\*3\*141, is installed on the user’s system <u>AND</u> the order is electronically signed through the CPRS package, the electronically signed abbreviation, \[es\], will appear next to the Provider’s Name on the order.

Example: Finish an Order Without a Duration (continued)

PENDING IV (ROUTINE) Sep 07, 2000 16:23:46 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\(1\) Additives: Type: PIGGYBACK \<DIN\>

AMPICILLIN 1 GM

\(2\) Solutions:

0.9% NACL 100 ML

Duration: (4) Start: 09/07/2000 15:00

\(3\) Infusion Rate:

REQUESTED START: 09/07/2000 09:00

\*(5) Med Route: IVPB (6) Stop: 09/14/2000 16:54

\*(7) Schedule: QID Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 01-09-15-20 Quantity: 0

\*(9) Provider: PSJPROVIDER,ONE \[es\] Cum. Doses:

\*(10)Orderable Item: AMPICILLIN INJ

Instructions:

\(11\) Other Print: THIS IS AN INPATIENT IV EXAMPLE.

\+ Enter ?? for more actions

AC Accept ED Edit

Select Item(s): Next Screen// AC

Orderable Item: AMPICILLIN INJ

Give: IVPB QID

0001 1 EAST 09/07/00

PSJPATIENT1,ONE B-12

AMPICILLIN 1 GM

0.9% NACL 100 ML

Dose due at: \_\_\_\_\_\_\_\_

THIS IS AN INPATIENT IV EXAMPLE

QID

01-09-15-20

M2\*\*\*

Fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

Start date: SEP 7,2000 15:00 Stop date: SEP 14,2000 16:54

Is this O.K.? YES// \<Enter\>

The Requested Start date/time value is added to the order view to indicate the date/time requested by the provider to start the order. This date/time is the CPRS expected first dose when no duration is received from CPRS.

Example: Finish an Order With a Duration

PENDING IV (ROUTINE) Sep 07, 2000 16:11:42 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\(1\) Additives: Type:

\(2\) Solutions:

Duration: 10 DAYS (4) Start: \*\*\*\*\*\*\*\*

\(3\) Infusion Rate:

\*(5) Med Route: IVPB (6) Stop: \*\*\*\*\*\*\*\*

\*(7) Schedule: QID Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 01-09-15-20 Quantity: 0

\*(9) Provider: PSJPROVIDER,ONE \[es\] Cum. Doses:

\*(10)Orderable Item: AMPICILLIN INJ

Instructions:

\(11\) Other Print:

Provider Comments: THIS IS AN INPATIENT IV EXAMPLE.

\+ Enter ?? for more actions

DC Discontinue FL (Flag)

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

COMPLETE THIS ORDER AS IV OR UNIT DOSE? IV// IV

Copy the Provider Comments into Other Print Info? Yes// YES

IV TYPE: PB

CHOOSE FROM:

A ADMIXTURE

C CHEMOTHERAPY

H HYPERAL

P PIGGYBACK

S SYRINGE

Enter a code from the list above.

Select one of the following:

A ADMIXTURE

C CHEMOTHERAPY

H HYPERAL

P PIGGYBACK

S SYRINGE

IV TYPE: PIGGYBACK

\*\*AUTO STOP 7D\*\*

This patient is already receiving an order for the following drug in the same

class as AMPICILLIN INJ 2GM:

AMPICILLIN CAP C 09/07 09/21 A

Give: 500MG PO QID

Do you wish to continue entering this order? NO// Y

Select ADDITIVE: AMPICILLIN// \<Enter\>

ADDITIVE: AMPICILLIN// \<Enter\>

Restriction/Guideline(s) exist. Display? : (N/D): No// D

Dispense Drug Text:

Refer to PBM/MAP PUD treatment guidelines

RESTRICTED TO NEUROLOGY

(The units of strength for this additive are in GM)

Strength: 1 GM

Select ADDITIVE: \<Enter\>

Select SOLUTION: 0.9

1 0.9% NACL 500 ML

2 0.9% NACL 100 ML

3 0.9% NACL 50 ML

4 0.9% NaCl 250 ML

BT

CHOOSE 1-4: 2 0.9% NACL 100 ML

INFUSION RATE: \<Enter\>

PENDING IV (ROUTINE) Sep 07, 2000 16:23:46 Page: 1 of 2

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\(1\) Additives: Type: PIGGYBACK \<DIN\>

AMPICILLIN 1 GM

\(2\) Solutions:

0.9% NACL 100 ML

Duration: 10 DAYS (4) Start: 09/07/2000 09:00

\(3\) Infusion Rate: Calc Start: 09/07/2000 08:13

\*(5) Med Route: IVPB (6) Stop: 09/17/2000 09:00

Calc Stop: 09/22/2000 24:00

\*(7) Schedule: QID Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 01-09-15-20 Quantity: 0

\*(9) Provider: PSJPROVIDER,ONE \[es\] Cum. Doses:

\*(10)Orderable Item: AMPICILLIN INJ

Instructions:

\(11\) Other Print: THIS IS AN INPATIENT IV EXAMPLE.

\+ Enter ?? for more actions

AC Accept ED Edit

Select Item(s): Next Screen// AC

> -----------------------------------------report continues--------------------------------

![](inpatient-medications-nurse-s-user-manual-psj-5-423/060.png)Note: When the CPRS patch, OR\*3\*141, is installed on the user’s system <u>AND</u> the order is electronically signed through the CPRS package, the electronically signed abbreviation, \[es\], will appear next to the Provider’s Name on the order.

Example: Finish an Order With a Duration (continued)

Orderable Item: AMPICILLIN INJ

Give: IVPB QID

0001 1 EAST 09/07/00

PSJPATIENT1,ONE B-12

AMPICILLIN 1 GM

0.9% NACL 100 ML

Dose due at: \_\_\_\_\_\_\_\_

THIS IS AN INPATIENT IV EXAMPLE

QID

01-09-15-20

M2\*\*\*

Fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

Start date: 09/07/2000 09:00 Stop date: 09/17/2000 09:00

Is this O.K.? YES// \<Enter\>

The calculated Start Date/Time (Calc Start) and the Stop Date/Time (Calc Stop) will display according to how the following Inpatient Ward Parameters settings are configured:

- DAYS UNTIL STOP DATE/TIME:
- DAYS UNTIL STOP FOR ONE-TIME:
- SAME STOP DATE ON ALL ORDERS:
- TIME OF DAY THAT ORDERS STOP:
- DEFAULT START DATE CALCULATION:

The CPRS Expected First Dose will display as the default Start Date/Time when a duration is received from CPRS.

The default Stop Date/Time is derived from the CPRS Expected First Dose and the duration, when the duration is available from CPRS.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/061.png)Note: When an order is placed through CPRS prior to the next administration time for today, the <u>Expected First Dose</u> will be today at the next administration time. However, if the order is placed after the <u>last</u> administration time of the schedule for today, the Expected First Dose will be at the next administration time. The Expected First Dose displayed in CPRS displays as Requested Start Date/Time on the order view if no duration is received from CPRS. The Expected First Dose displays as the default Start Date/Time on the order view when a duration is received. Expected First Dose does not display for On-call or One-time orders.

If the Dispense Drug or Orderable Item has a non-formulary status, this status will be displayed on the screen as “\*N/F\*” beside the Dispense Drug or Orderable Item.

The user, when finishing an order that contains an IV Additive and there is more than one dispense drug matched to the selected Orderable Item, they must select the correct item for the order from the displayed list. If there are multiple additives contained on the single order, the Pharmacist must select each of the correct additives for the order. (See example below) The lists of additive will be displayed as follows:

Print Name Additive Strength: Strength

When there are Multiple IV Additive Orderable Items, each IV additive must be selected from the displayed list.

Example: Multiple items for an Orderable Item

DC Discontinue FL (Flag)ED Edit FN FinishSelect Item(s): Next Screen// FN FinishIV TYPE: PIGGYBACK//More than one dispense IV Additives are available for:Orderable Item: PIPERACILLIN/TAZOBACTAM INJ  Ordered Dose: 5 GMPlease select the correct dispense IV Additive below for this order:1  PIPERACILLIN/TAZOBACTAM                Additive Strength: 3.375 GM  2  PIPERACILLIN/TAZOBACTAM                Additive Strength: 2.25 GM 3  PIPERACILLIN/TAZOBACTAM                Additive Strength: 4.5 GMSelect (1 - 3): 3 PIPERACILLIN/TAZOBACTAM         Additive Strength: 4.5 GM

Example: Multiple IV Additives for same order with multiple items attached to the Orderable Item

More than one dispense IV Additives are available for:Orderable Item: PIPERACILLIN/TAZOBACTAM  Ordered Dose: 5 GMPlease select the correct dispense IV Additive below for this order:1  PIPERACILLIN/TAZOBACTAM                Additive Strength: 3.375  2  PIPERACILLIN/TAZOBACTAM                Additive Strength: 2.25   3  PIPERACILLIN/TAZOBACTAM                Additive Strength: 4.5Select (1 - 3): 2More than one dispense IV Additives are available for:Orderable Item: CIPROFLOXACIN  Ordered Dose: 2 MGPlease select the correct dispense IV Additive below for this order:  1  CIPROFLOXACIN 200MG                    Additive Strength: N/A  2  CIPROFLOXACIN 400MG                    Additive Strength: N/ASelect (1 - 2): 2More than one dispense IV Additives are available for:Orderable Item: CEFAZOLIN  Ordered Dose: 2 GMPlease select the correct dispense IV Additive below for this order:  1  CEFAZOLIN                         Additive Strength: N/A  2  CEFAZ2                                 Additive Strength: N/A  3  CEFAZ3                                 Additive Strength: N/ASelect (1 - 3): 1

A prompt is added to the finishing process, “COMPLETE THIS ORDER AS IV OR UNIT DOSE?” to determine if the user should complete the order as either an IV or Unit Dose order. The prompt will be displayed only if the user selected the *Inpatient Order Entry* option to finish the order and the order was placed in CPRS using the Inpatient Meds dialog. Also, the prompt will appear only if the correct combination of the entry in the IV FLAG in the MEDICATION ROUTES file and the entry in the APPLICATION PACKAGES’ USE field in the DRUG file for the order’s Dispense Drug are found.

The following table will help explain the different scenarios for orders placed in CPRS using the Inpatient Meds dialog:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 25%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>IV FLAG in the MEDICATION ROUTES file</th>
<th>Dispense Drug’s Application Use</th>
<th>Which Order View screen will be displayed to the user</th>
<th>Special Processing</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IV</td>
<td>IV</td>
<td>IV</td>
<td>None</td>
</tr>
<tr class="even">
<td>IV</td>
<td>Unit Dose</td>
<td>Unit Dose</td>
<td>Prompt user to finish order as IV or Unit Dose</td>
</tr>
<tr class="odd">
<td>IV</td>
<td><p>IV and</p>
<p>Unit Dose</p></td>
<td>IV</td>
<td>Prompt user to finish order as IV or Unit Dose</td>
</tr>
<tr class="even">
<td>Non-IV</td>
<td>IV</td>
<td>IV</td>
<td>Prompt user to finish order as IV or Unit Dose</td>
</tr>
<tr class="odd">
<td>Non-IV</td>
<td>Unit Dose</td>
<td>Unit Dose</td>
<td>None</td>
</tr>
<tr class="even">
<td>Non-IV</td>
<td><p>IV and</p>
<p>Unit Dose</p></td>
<td>Unit Dose</td>
<td>Prompt user to finish order as IV or Unit Dose</td>
</tr>
</tbody>
</table>

### Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-nurse-s-user-manual-psj-5-423/062.png) This option is only available to those users who hold the PSJ RPHARM key.

The flag action is available to alert the users that the order is incomplete or needs clarification. Flagging is applied to any orders that need more information or corrections from the clinician. When the user flags the order, an alert is sent to the specified user defining the information that is needed to process the medication order. The specified user can send a return alert with the needed information. The Activity Log will record the flagging activities including acknowledgement that the alert was viewed. The flag action can be performed in either CPRS or in Inpatient Medications.

When a flagged order appears on the order view, the order number on the right hand side will be highlighted using reverse video. The nurse, or any user without the PSJ RPHARM key, does not have the ability to flag or un-flag orders; however, they can view the flagged or un-flagged comments via the Activity Log.

Example: Flagged Order

<span id="Page_96" class="anchor"></span>Inpatient Order Entry Feb 11, 2011@13:05:49 Page: 1 of 1

--------------------------------------------------------------------------------

ZZZRETFIVEEIGHTYSIX,PATIENT Ward: ALB-PRR A

PID: 000-00-1234 Room-Bed: Ht(cm): 187.96 (05/03/10)

DOB: 04/07/70 (40) Att: Psj,Test Wt(kg): 74.00 (05/03/10)

Sex: MALE TrSp: Medical Observati Admitted: 07/02/97

Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.97

--------------------------------------------------------------------------------

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

1 ACETAZOLAMIDE INJ ? \*\*\*\*\* \*\*\*\*\* P

Give: 500MG/1VIAL IV NOW

2 ACETAZOLAMIDE INJ ? \*\*\*\*\* \*\*\*\*\* P

Give: 500MG/1VIAL IV Q12H

3 VINCRISTINE INJ ? \*\*\*\*\* \*\*\*\*\* P

Give: 3MG/3ML IVP BID

----------Enter ?? for more actions---------------------------------------------

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P99" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Quit// SO Select Order

### Speed Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the list of orders in the patient’s profile, the nurse can select one or more of the orders on which to take action. The nurse can quickly discontinue this patient’s orders by selecting Speed Discontinue, or quickly renewing an order by selecting Speed Renew. Other “quick” selections include Speed Finish and Speed Verify.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/063.png)Note: Any orders placed through the Med Order Button cannot be Speed Discontinued.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/064.png)Note: Complex orders cannot be speed finished because it may not be appropriate to assign the same stop date to all components of a complex order.

## Discontinue All of a Patient’s Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSJU CA\]

The *Discontinue All of a Patient’s Orders* option allows a nurse to discontinue all of a patient’s orders. Also, it allows a ward clerk to mark all of a patient’s orders for discontinuation. If the ALLOW USER TO D/C ORDERS parameter is turned on to take action on active orders, then the ward clerk will also be able to discontinue orders. This ALLOW USER TO D/C ORDERS parameter is set using the *Inpatient User Parameter’s Edit* option under the *PARameter’s Edit Menu* option, which is under the *Supervisor’s Menu* option.

This option is then used to discontinue the selected orders. If a non-verified or pending order is discontinued, it is deleted completely from the system.

## Hold All of a Patient’s Orders 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU HOLD ALL\]

The *Hold All of a Patient’s Orders* option allows a nurse to place all of a patient’s active orders on hold in order to temporarily stop the medication from being dispensed, or take all of the patient’s orders off of hold to restart the dispensing of the medication.

The option will take no action on individual orders that it finds already on hold. When this option is used to put all orders on hold, the system will print labels for each medication order newly put on hold, indicating on the label that the medication is on hold. Also, the profile will notify the user that the patient’s orders have been placed on hold; the letter H will be placed in the Status/Info column on the profile for each formerly active order.

When the option is used to take all orders off of hold, the system will reprint labels for the medication orders that were taken off hold and indicate on the label that the medication is off hold. Again, this option will take no action on individual orders that it finds were not on hold. The profile will display to the user that the patient’s orders have been taken off hold.

Example 1: Hold All of a Patient’s Orders

Select Unit Dose Medications Option: Hold All of a Patient's Orders

Select PATIENT: PSJPATIENT2,TWO 000-00-0002 02/22/42 A-6

DO YOU WANT TO PLACE THIS PATIENT'S ORDERS ON HOLD? Yes// \<Enter\> (Yes)

HOLD REASON: SURGERY SCHEDULED FOR 9:00AM

...a few moments, please....................DONE!

To take the orders <u>off of hold</u>, choose this same option and the following will be displayed:

Example 2: Take All of a Patient’s Orders Off of Hold

Select Unit Dose Medications Option: HOld All of a Patient's Orders

Select PATIENT: PSJPATIENT2,TWO 000-00-0002 02/22/42 A-6

THIS PATIENT'S ORDERS ARE ON HOLD.

DO YOU WANT TO TAKE THIS PATIENT'S ORDERS OFF OF HOLD? Yes// \<Enter\> (Yes)............

.....DONE!

.....DONE!

![](inpatient-medications-nurse-s-user-manual-psj-5-423/065.png)Note: Individual orders can be placed on hold or taken off of hold through the *Order Entry* and *Non–Verified/Pending Orders* options.

## Inpatient Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ PR\]

The *Inpatient Profile* option allows the user to view the Unit Dose and IV orders of a patient simultaneously. The user can conduct the Inpatient Profile search by ward group, ward, or patient. If the selection to sort is by ward, the administration teams may be specified. The default for the administration team is ALL and multiple teams may be entered. If selecting by ward or ward group, the profile may be sorted by patient name or room-bed. To print Outpatients, the user should select the ward group ^OTHER or print by Patient.

When the user accesses this option from the Unit Dose Medications module for the first time within a session, a prompt is displayed to select the IV room. When only one active IV room exists, it will be selected automatically. The user is then given the label and report devices defined for the IV room chosen. If no devices have been defined, the user will be given the opportunity to choose them. If this option is exited and then re-entered within the same session, the current label and report devices are shown.

In the following description, viewing a profile by patient is discussed; however, ward and ward group are handled similarly.

After the user selects the patient for whom a profile view is needed, the length of profile is chosen. The user can choose to view a long or short profile or, if the user decides not to view a profile for the chosen patient, “NO Profile” can be selected. When NO Profile is chosen, the system will return to the “Select PATIENT:” prompt and the user may choose a new patient.

Once the length of profile is chosen, the user can print the patient profile (by accepting the default or typing P at the “Show PROFILE only, EXPANDED VIEWS only, or BOTH: Profile//” prompt), an expanded view of the patient profile (by typing E), or both (by typing B). The expanded view lists the details of each order for the patient. The activity logs of the orders can also be printed when the expanded view or both, the expanded view and profile, are chosen.

The advantage of this option is that by viewing the combined Unit Dose/IV profile of a patient, the user can quickly determine if any corrections or modifications need to be made for existing or future orders based on Unit Dose or IV medications already being received by the patient. Sometimes the nurse must revise a prospective order for a patient based on the Unit Dose or IV medications already prescribed for the patient.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/066.png)Note: For Unit Dose orders, the long activity log shows all activities of an order, while the short activity log excludes the field changes, and shows only the major activities. For IV orders, the short and long activity logs give the user the same results.

Example: Inpatient Profile

Select Unit Dose Medications Option: IPF Inpatient Profile

Select by WARD GROUP (G), WARD (W), or PATIENT (P): Patient \<Enter\>

Select PATIENT: PSJPATIENT11,ONE 000-55-3421 08/18/20 1 EAST

Select another PATIENT: \<Enter\>

SHORT, LONG, or NO Profile? SHORT// \<Enter\> SHORT

Show PROFILE only, EXPANDED VIEWS only, or BOTH: PROFILE// BOTH

Show SHORT, LONG, or NO activity log? NO// SHORT

Select PRINT DEVICE: 0;80 NT/Cache virtual TELNET terminal

Inpatient Order Entry Jun 12, 2006@23:12:54 Page: 1 of 1

<span id="Page_99" class="anchor"></span>PSJPATIENT11, ONE Ward: 2ASM

PID: 000-55-3421 Room-Bed: 102-1 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 12/02/23 (82) Wt(kg): 100.00 (06/24/03)

Sex: MALE Admitted: 12/11/01

Dx: Breathing Difficulty Last transferred: 12/11/01

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 CEFAZOLIN 1 GM C 06/12/2006 06/22/2006 H

in 5% DEXTROSE 50 ML Q8H

2 CIMETIDINE TAB C 06/12/2006 07/12/2006 A

Give: 300MG PO BID

3 FUROSEMIDE TAB C 06/01/2006 06/15/2006 HP

Give: 40MG PO QAM

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

4 CAPTOPRIL TAB C 06/14/2006 06/28/2006 N

Give: 25MG PO BID

\- - - - - - - - - - - - P E N D I N G R E N E W A L S - - - - - - - - - - - -

5 HALOPERIDOL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 5MG PO BID Renewed 06/14/2006

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

6 HEPARIN/DEXTROSE INJ,SOLN ? \*\*\*\*\* \*\*\*\*\* P

Give: IV

7 LACTULOSE SYRUP ? \*\*\*\*\* \*\*\*\*\* P NF

Give: 10GM/15ML PO BID PRN

\- - - - - - - - - - - RECENTLY DISCONTINUED/EXPIRED (LAST 24 HOURS) - - - - - -

8 FOLIC ACID TAB C 06/14 06/16 D

Give: 1MG PO QAM

9 GENTAMICIN 80 MG C 06/12/2006 06/12/2006 D

in 5% DEXTROSE 100 ML Q8H

10 ISONIAZID TAB C 04/03/2006 04/17/2006 DF

Give: 300MG PO QD

11 POTASSIUM CHLORIDE 10MEQ C 06/12/2006 06/12/2006 DA

in 5% DEXTROSE 1000 ML Q8H

12 POTASSIUM CHLORIDE 40 MEQ C 06/12/2006 06/12/2006 DD

in 5% DEXTROSE 250 ML 120 ml/hr

13 PROPRANOLOL TAB C 06/15/2006 06/20/2006 DP

Give: 40MG PO Q6H

14 THIAMINE TAB C 04/03/2006 04/17/2006 E

Give: 100MG PO BID

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P102" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Entry Date: 09/19/00 09:55

## Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Order checks (allergy/adverse drug reactions, drug-drug interactions, duplicate therapy, dangerous medications for patient over 64 years of age, Glucophage lab results, and Aminoglycosides ordered) are performed when a new medication order is placed through Inpatient Medications or when various actions are taken on medication orders through the Inpatient Medications application. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error due to the omission of an order check when a non-active medication order is acted upon.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/067.png)Note: The check for remote data availability is performed when entering a patient’s chart, rather than on each order.

The following actions will initiate an order check:

- Action taken through Inpatient Medications to enter a medication order will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through Inpatient Medications to finish a medication order placed through CPRS will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through IV Menu to finish a medication order placed through CPRS will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through Inpatient Medications to renew a medication order will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through IV Menu to renew a medication order will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through IV Menu to copy a medication order, thereby creating a new order.

The following are the different items used for the order checks:

- Checks each Dispense Drug within the Unit Dose order for allergy/adverse drug reactions.
- Checks each Dispense Drug within the Unit Dose order against existing orders for drug-drug interaction, and duplicate therapy.
- Checks each additive within an IV order for drug-drug interaction, and duplicate therapy against solutions or other additives within the order.
- Checks each IV order solution for allergy/adverse reactions.
- Checks each IV order solution for drug-drug interaction against other solutions or additives within the order if they are defined as a PreMix.
- Checks each IV order additive for allergy/adverse reaction.
- Checks each IV order additive for drug-drug interaction, and duplicate therapy against existing orders for the patient.
- Checks each IV order solution for drug-drug interaction against existing orders for the patient.

Override capabilities are provided based on the severity of the order check, if appropriate.

Order Checks will be displayed/processed in the following order:

- System Errors
- Allergy/ADR (local & remote)
- CPRS checks generated backdoor (3 new checks)
- Drug Level Errors
- Inpatient Critical Drug Interaction
- Local & Remote Outpatient Critical Drug Interactions
- Inpatient Significant Drug Interactions
- Local & Remote Outpatient Significant Drug Interactions
- Order Level Error Messages – Drug Interactions
- Duplicate Therapy –Inpatient, Local & Remote Outpatient
- Order Level Error Messages – Duplicate Therapy

These checks will be performed at the Dispense Drug level. Order checks for IV orders will use Dispense Drugs linked to each additive/solution in the IV order. All pending, non-verified, active and renewed Inpatient orders, active Outpatient orders, and active Non-Veterans Affairs (VA) Meds documented in CPRS will be included in the check. In addition, with the release of OR\*3\*238, order checks will be available using data from the Health Data Repository Historical (HDR-Hx) and the Health Data Repository Interim Messaging Solution (HDR-IMS). This will contain both Outpatient orders from other VAMCs as well as from Department of Defense (DoD) facilities, if available. Any remote Outpatient order that has been expired for 30 days or less will be included in the list of medications to be checked.

There is a slight difference in the display of local Outpatient orders compared with remote Outpatient orders. Below are examples of the two displays:

Example: Local Outpatient Order Display

Duplicate Drug in Local Rx:

Rx \#: 2608

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

Example: Remote Outpatient Order Display

Duplicate Drug in Remote Rx:

LOCATION NAME: \<NAME OF FACILITY\>

Rx \#: 2608

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Days Supply: 30

In the Remote Outpatient Order Display example above, notice the name of the remote location has been added. In addition, the number of refills is not available.

If the order is entered by the Orderable Item only, these checks will be performed at the time the Dispense Drug(s) is specified. The checks performed include:

Duplicate Therapy - Each First Databank duplicate therapy class is assigned a duplication allowance value. The duplication allowance value indicates how many duplications are considered appropriate before a warning is generated. If the number of duplicate therapy matches (number of drug pairs) exceeds the duplication allowance value, a warning will be displayed.

In the example below, the patient is already receiving orders containing a Dispense Drug in the same therapy class as one of the Dispense Drugs in the new order. The duplication allowance for the Antihyperlipidemics HMGCo-A Reductase Inhibitors (Statins) therapy class is zero. The new order for Simvastatin 20mg tab and the existing outpatient pharmacy order for Simvastatin 10mg tab are both in the same therapy class resulting in one duplication match. Since one duplication match is greater than zero, a duplicate therapy warning is displayed.

Inpatient duplicate orders of this kind are displayed in a numbered list. The user is first asked whether or not to continue the current order. If the user selects to continue the order then the user is prompted with which, if any, numbered Inpatient duplicate orders to discontinue. The user may enter a range of numbers from the numbered list of duplicate orders or bypass the prompt by selecting \<Enter\> and continue with the order. Entry of orders with duplicate drugs of the same class will be allowed.

Inpatient Order Entry         Mar 16, 2011@12:10:42          Page:    1 of    2

BCMA,EIGHTEEN-PATIENT             Ward: 7A GEN                         A

   PID: 666-33-0018           Room-Bed:               Ht(cm): 175.26 (12/15/08)

   DOB: 04/07/35 (75)         Att: Psj,Test          Wt(kg): 100.00 (12/15/08)

   Sex: FEMALE                TrSp: Medical Observati      Admitted: 01/31/02

    Dx: UPSET                            Last transferred: 06/04/10

CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): 2.21

--------------------------------------------------------------------------------

\- - - - - - - - - -  N O N - V E R I F I E D  C O M P L E X - - - - - - - - - -

   1    LITHIUM TAB,SA                           C  10/13  10/15 N             

          Give: 450MG PO QID                                                   

        LITHIUM TAB,SA                           C  10/13  10/15 N             

          Give: 10000MG PO Q4H                                                 

   2    RILUZOLE TAB                             C  10/13  10/15 N             

          Give: 50MG PO BID                                                    

+---------Enter ?? for more actions---------------------------------------------

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen// no New Order Entry

Select DRUG: simv

Lookup: DRUG GENERIC NAME

1 SIMVASTATIN 10MG TAB CV350

2 SIMVASTATIN 20MG TAB CV350

3 SIMVASTATIN 40MG TAB CV350

4 SIMVASTATIN 80MG TAB CV350

CHOOSE 1-4: 2 SIMVASTATIN 20MG TAB CV350 N/F

Restriction/Guideline(s) exist. Display? : (N/O): No// NO

Enter RETURN to continue or '^' to exit:

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

================================================================================

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es) as SIMVASTATIN 20MG

TAB:

Local Rx \#501820A (ACTIVE) for SIMVASTATIN 10MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

Processing Status: Not released locally (Window)

Class(es) Involved in Therapeutic Duplication(s): Antihyperlipidemics

HMGCo-A Reductase Inhibitors (Statins) ================================================================================

Press Return to continue...

Available Dosage(s)

1\. 20MG

2\. 40MG

3\. 60MG

Select from list of Available Dosages or Enter Free Text Dose: 2 40MG

You entered 40MG is this correct? Yes// YES

MED ROUTE: ORAL (BY MOUTH)// PO

SCHEDULE: QPM// 2100

SCHEDULE TYPE: CONTINUOUS// CONTINUOUS

ADMIN TIMES: 2100//

SPECIAL INSTRUCTIONS:

START DATE/TIME: MAR 16,2011@12:10// MAR 16,2011@12:10

STOP DATE/TIME: MAR 18,2011@24:00// MAR 18,2011@24:00

Expected First Dose: MAR 16,2011@21:00

PROVIDER: PHARMACIST,SEVENTEEN//

NON-VERIFIED UNIT DOSE Mar 16, 2011@12:10:15 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Att: Psj,Test Wt(kg): 100.00 (12/15/08)

--------------------------------------------------------------------------------

(1)Orderable Item: SIMVASTATIN TAB

Instructions:

(2)Dosage Ordered: 40MG

Duration: (3)Start: 03/16/11 12:10

\(4\) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 03/18/11 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: QPM

\(9\) Admin Times: 2100

\(10\) Provider: PHARMACIST,SEVENTEEN

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

SIMVASTATIN 20MG TAB 2

+---------Enter ?? for more actions---------------------------------------------

ED Edit AC ACCEPT

Select Item(s): Next Screen// ac ACCEPT

NATURE OF ORDER: WRITTEN// W

...transcribing this non-verified order....

NON-VERIFIED UNIT DOSE Mar 16, 2011@12:10:24 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Att: Psj,Test Wt(kg): 100.00 (12/15/08)

--------------------------------------------------------------------------------

\*(1)Orderable Item: SIMVASTATIN TAB

Instructions:

\*(2)Dosage Ordered: 40MG

Duration: (3)Start: 03/16/11 12:10

\*(4) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 03/18/11 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QPM

\(9\) Admin Times: 2100

SIMVASTATIN 20MG TAB 2

+---------Enter ?? for more actions---------------------------------------------

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// vf Verify

...a few moments, please.....

Pre-Exchange DOSES:

ORDER VERIFIED.

Enter RETURN to continue or '^' to exit:

- Drug-Drug Interactions - Drug-drug interactions warnings will be displayed for critical or significant drug-drug interactions. If the Dispense Drug selected is identified as having an interaction of this level with one of the drugs the patient is already receiving, details of the order the new drug interacts with will be displayed.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/068.png)Note: For a Significant Interaction, the entry of an intervention is optional. For a Critical Interaction, the user <u>must</u> enter an intervention before continuing.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/069.png)Note: If the user, is prompted for an intervention and enters 9, which is OTHER, “Other For Recommendation” displays. This allows the user to enter unlimited free text as a response to the order check(s).

Example: Drug-Drug Interactions Display

Inpatient Order Entry Mar 16, 2011@12:04:33 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): 2.21

--------------------------------------------------------------------------------

\- - - - - - - - - - N O N - V E R I F I E D C O M P L E X - - - - - - - - - -

1 LITHIUM TAB,SA C 10/13/2011 10/15/2011 N

Give: 450MG PO QID

LITHIUM TAB,SA C 10/13/2011 10/15/2011 N

Give: 10000MG PO Q4H

2 RILUZOLE TAB C 10/13/2011 10/15/2011 N

Give: 50MG PO BID

RILUZOLE TAB C 10/15/2011 10/16/2011 N

Give: 10000MG PO Q4H

\- - - - - - - - - - - - - P E N D I N G C O M P L E X - - - - - - - - - - - -

3 HALOPERIDOL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 40MG PO BID

----------Enter ?? for more actions---------------------------------------------

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P107" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Quit// no New Order Entry

Select DRUG: indinavi

Lookup: DRUG GENERIC NAME

INDINAVIR SULFATE 400MG CAP AM800

...OK? Yes// (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

================================================================================

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with INDINAVIR SULFATE 400MG CAP:

Local Rx \#501820A (ACTIVE) for SIMVASTATIN 10MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

Processing Status: Not released locally (Window)

Concurrent administration may result in elevated HMG levels, which may

increase the risk of myopathy, including rhabdomyolysis. (1-16)

================================================================================

Display Professional Interaction Monograph(s)? NO//

Do you want to Continue with INDINAVIR SULFATE 400MG CAP? NO// y YES

Now creating Pharmacy Intervention

For INDINAVIR SULFATE 400MG CAP

PROVIDER: PSJPROVIDER,ONE TP

RECOMMENDATION: ?

Answer with APSP INTERVENTION RECOMMENDATION, or NUMBER

Choose from:

1 CHANGE DRUG

2 CHANGE FORM OR ROUTE OF ADMINISTRATION

3 ORDER LAB TEST

4 ORDER SERUM DRUG LEVEL

5 CHANGE DOSE

6 START OR DISCONTINUE A DRUG

7 CHANGE DOSING INTERVAL

8 NO CHANGE

9 OTHER

RECOMMENDATION: 9  OTHER

OTHER FOR RECOMMENDATION:

  No existing text

  Edit? NO//

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention? N// O

Available Dosage(s)

1\. 400MG

2\. 800MG

Select from list of Available Dosages or Enter Free Text Dose: 1 400MG

You entered 400MG is this correct? Yes// YES

MED ROUTE: ORAL (BY MOUTH)// PO

SCHEDULE: QDAY//

1 QDAY 0900

2 QDAY-DIG 1300

3 QDAY-WARF 1300

CHOOSE 1-3: 1 0900

SCHEDULE TYPE: CONTINUOUS// CONTINUOUS

ADMIN TIMES: 0900//

SPECIAL INSTRUCTIONS:

START DATE/TIME: 03/16/2011@12:08// 03/16/2011@12:08

STOP DATE/TIME: 03/17/2011@24:00// 03/17/2011@24:00

Expected First Dose: 03/17/2011@09:00

PROVIDER: PHARMACIST,SEVENTEEN// 145

NON-VERIFIED UNIT DOSE Mar 16, 2011@12:07:46 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

--------------------------------------------------------------------------------

(1)Orderable Item: INDINAVIR CAP,ORAL

Instructions:

(2)Dosage Ordered: 400MG

Duration: (3)Start: 03/16/2011 12:08

\(4\) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 03/17/2011 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: QDAY

\(9\) Admin Times: 0900

\(10\) Provider: PHARMACIST,SEVENTEEN

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR SULFATE 400MG CAP 1

+---------Enter ?? for more actions---------------------------------------------

ED Edit AC ACCEPT

Select Item(s): Next Screen// ac ACCEPT

Press Return to continue...

NATURE OF ORDER: WRITTEN// W

...transcribing this non-verified order....

NON-VERIFIED UNIT DOSE Mar 16, 2011@12:08:04 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

--------------------------------------------------------------------------------

\*(1)Orderable Item: INDINAVIR CAP,ORAL

Instructions:

\*(2)Dosage Ordered: 400MG

Duration: (3)Start: 03/16/2011 12:08

\*(4) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 03/17/2011 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QDAY

\(9\) Admin Times: 0900

\*(10) Provider: PHARMACIST,SEVENTEEN \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR SULFATE 400MG CAP 1

+---------Enter ?? for more actions---------------------------------------------

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// NEXT SCREEN

- Allergy Order Checks – This section describes the Allergy Order Checks functionality. Allergy Order Checks appear prior to Clinical Reminder Order Checks.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/070.png)Note: Severity for an allergy can ONLY be entered for (O)bserved and NOT (H)istorical Allergy/Adverse Reactions and the user MUST HOLD the GMRA-ALLERGY VERIFY key to enter MECHANISM and SEVERITY for Observed types of Allergy/Adverse Reactions.

Inpatient Order Entry Mar 16, 2011@12:04:33 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): 2.21

Allergies - Verified: ACETAMINOPHEN, CODEINE, PROPOFOL

Non-Verified: AMLODIPINE/BENAZEPRIL, LEVOTHYROXINE, SULFA DRUGS

Remote: ACETAMINOPHEN, CODEINE, DIPRIVAN, GUAIFENESIN, PROPOFOL

Adverse Reactions:

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile

Select Action: View Profile// View Profile

SHORT, LONG, or NO Profile? SHORT// SHORT

Inpatient Order Entry Mar 16, 2011@12:04:33 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): 2.21

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 ACETAMINOPHEN TAB C 05/22/2011 06/19/2011 A

Give: 325MG PO Q6H

2 AMLODIPINE/BENAZEPRIL CAP,ORAL C 05/06/2011 06/03/2011 A

Give: 5mg PO AM

3 LEVOTHYROXINE SODIUM TAB C 05/08/2011 06/05/2011 A

Give: 0.025MG PO QAM

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

4 SULFADIAZINE TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 500MG PO AM & AFTERNOON

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

<span id="P110" class="anchor"></span>CM New Clinic Medication Entry

Select Action: Quit// SO Select Order

Select ORDERS (1-4): 1

ACTIVE UNIT DOSE Mar 16, 2011@12:04:33 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

\*(1)Orderable Item: ACETAMINOPHEN TAB

Instructions:

\*(2)Dosage Ordered: 325MG

Duration: \*(3)Start: 05/22/2014 12:03

\*(4) Med Route: ORAL

\*(5) Stop: 06/19/2014 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q6H

\(9\) Admin Times: 0600-1200-1800-2359

\*(10) Provider: CLERKPEARSON,HOLLY \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ACETAMINOPHEN 325MG TAB UNIT DOSE 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// CO CO

NON-VERIFIED UNIT DOSE May 27, 2014@18:10:16 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

(1)Orderable Item: ACETAMINOPHEN TAB

Instructions:

(2)Dosage Ordered: 325MG

Duration: (3)Start: 05/27/2014 18:10

\(4\) Med Route: ORAL

\(5\) Stop: 06/24/2014 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: Q6H

\(9\) Admin Times: 0600-1200-1800-2359

\(10\) Provider: CLERKPEARSON,HOLLY \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ACETAMINOPHEN 325MG TAB UNIT DOSE 1

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

A Drug-Allergy Reaction exists for this medication and/or class!

Prospective Drug: ACETAMINOPHEN 325MG TAB UNIT DOSE

Causative Agent: ACETAMINOPHEN (CLE13 TEST LAB - 05/07/14)

Historical/Observed: OBSERVED

Severity: SEVERE

Ingredients: ACETAMINOPHEN

Signs/Symptoms: NAUSEA AND VOMITING

Provider Override Reason: N/A - Order Entered Through VistA

Press Return to continue:

A Drug-Allergy Reaction exists for this medication and/or class!

Prospective Drug: ACETAMINOPHEN 325MG TAB UNIT DOSE

Causative Agent: ACETAMINOPHEN (MARTINSBURG VAMC - 05/13/14)

Historical/Observed: HISTORICAL

Severity: Not Entered

Ingredients: ACETAMINOPHEN

Signs/Symptoms: DIARRHEA

Provider Override Reason: N/A - Order Entered Through VistA

Do you want to Intervene? YES// Y

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for ACETAMINOPHEN 325MG TAB UNIT DOSE

PROVIDER: DOCTOR, TEST DT 192 4567891 BAY PINES TEST LAB

RECOMMENDATION: 9 OTHER

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

NATURE OF ORDER: WRITTEN// W

...transcribing this non-verified order....

NON-VERIFIED UNIT DOSE May 27, 2014@18:14:45 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

\*(1)Orderable Item: ACETAMINOPHEN TAB

Instructions:

\*(2)Dosage Ordered: 325MG

Duration: (3)Start: 05/27/2014 18:14

\*(4) Med Route: ORAL

\(5\) Stop: 06/24/2014 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q6H

\(9\) Admin Times: 0600-1200-1800-2359

\*(10) Provider: CLERKPEARSON,HOLLY \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ACETAMINOPHEN 325MG TAB UNIT DOSE 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// VF Verify

...a few moments, please.....

Pre-Exchange DOSES: 2

...updating dispense drug(s)...

...ACETAMINOPHEN 325MG TAB UNIT DOSE U/D: 1...

ORDER VERIFIED.

Enter RETURN to continue or '^' to exit:

You are finished with the new order.

The following ACTION prompt is for the original order.

Enter RETURN to continue or '^' to exit:

ACTIVE UNIT DOSE May 27, 2014@18:16:09 Page: 2 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

(7)Self Med: NO

Entry By: PEARSON,HOLLY Entry Date: 05/22/14 12:04

\(13\) Comments:

Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Quit// QUIT

Inpatient Order Entry May 27, 2014@18:16:10 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): 2.21

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 ACETAMINOPHEN TAB C 05/22/2011 06/19/2011 A

Give: 325MG PO Q6H

2 ACETAMINOPHEN TAB C 05/27/2011 06/24/2011 A

Give: 325MG PO Q6H

3 AMLODIPINE/BENAZEPRIL CAP,ORAL C 05/06/2011 06/03/2011 A

Give: 5mg PO AM

4 LEVOTHYROXINE SODIUM TAB C 05/08/2011 06/05/2011 A

Give: 0.025MG PO QAM

\- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -

5 SULFADIAZINE TAB ? \*\*\*\*\* \*\*\*\*\* P

\+ Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P113" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen//

The following changes have been made to the existing allergy order checks:

1.  In Backdoor Pharmacy, the system will require the pharmacist to complete an Intervention if the severity value equals ‘Severe’ before allowing the pharmacist to continue with the order.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/071.png)Note: The intervention functionality will be similar to the Critical Drug-Drug Interactions in backdoor pharmacy today.

2.  For Allergies/Adverse Reactions with Severity of Mild, Moderate, or Not Entered, the system will continue the same as it does today with the option that allows the pharmacist to enter an intervention at their discretion.
3.  All allergies are captured and stored with the order, regardless of whether or not an intervention was entered.
4.  Remote/HDR allergy Signs/Symptoms are now displayed when doing Allergy/ADR Order Checks.
5.  Modified Allergy/ADR Order Check to display actual Station Name in lieu of Local or Remote terminology.
6.  For a Severe Allergy the user is required to enter their electronic signature and intervention.

    ![](inpatient-medications-nurse-s-user-manual-psj-5-423/072.png)Note: In order to enter the Severity for an allergy in the Allergy Package it must be entered as (O)bserved  and not (H)istorical Allery/Adverse Reaction.

> <u>Mild:</u>

> Now doing allergy checks. Please wait...

> A Drug-Allergy Reaction exists for this medication and/or class!

> Prospective Drug: ASPIRIN 81MG EC TAB

> Causative Agent: ASPIRIN (ALBANY - 07/09/15)

> Historical/Observed: OBSERVED

> Severity: MILD

> Ingredients: ASPIRIN

> Signs/Symptoms: ANXIETY, HIVES

>           Drug Class: CN103 NON-OPIOID ANALGESICS

> Provider Override Reason: N/A - Order Check Not Evaluated by Provider

> Do you want to Intervene? YES// NO

> <u>Moderate:</u>

> Now doing allergy checks. Please wait...

> A Drug-Allergy Reaction exists for this medication and/or class!

> Prospective Drug: MINOXIDIL 2.5MG S.T.

> Causative Agent: MINOXIDIL (ALBANY - 07/29/15)

> Historical/Observed: OBSERVED

> Severity: MODERATE

> Ingredients: MINOXIDIL

> Signs/Symptoms: ANXIETY, ITCHING,WATERING EYES

> Drug Class: CV490 ANTIHYPERTENSIVES,OTHER

> Provider Override Reason: N/A - Order Check Not Evaluated by Provider

> Do you want to Intervene? YES// NO

> <u>Not Entered:</u>

> Now doing allergy checks. Please wait...

> A Drug-Allergy Reaction exists for this medication and/or class!

> Prospective Drug: AMIODARONE

> Causative Agent: AMIODARONE (ALBANY - 07/29/15)

> Historical/Observed: OBSERVED

> Severity: Not Entered

> Ingredients: AMIODARONE, IODINE

> Signs/Symptoms: ANXIETY

> Drug Class: CV300 ANTIARRHYTHMICS

> Provider Override Reason: N/A - Order Check Not Evaluated by Provider

> Do you want to Intervene? YES// NO

> <u>Severe without Intervention:</u>

> Now doing allergy checks. Please wait...

> A Drug-Allergy Reaction exists for this medication and/or class!

> Prospective Drug: PENICILLIN

> Causative Agent: PENICILLIN (ALBANY - 07/29/15)

> Historical/Observed: OBSERVED

> Severity: SEVERE

> Ingredients: PENICILLIN

> Signs/Symptoms: DIARRHEA, HIVES

>           Drug Class: AM110 PENICILLIN-G RELATED PENICILLINS

> Provider Override Reason: N/A - Order Check Not Evaluated by Provider

> Do you want to Intervene? YES// NO

> With a SEVERE reaction, an intervention is required!

> <u>Severe with Intervention:</u>

> Now doing allergy checks. Please wait...

> A Drug-Allergy Reaction exists for this medication and/or class!

> Prospective Drug: PENICILLIN

> Causative Agent: PENICILLIN (ALBANY - 07/29/15)

> Historical/Observed: OBSERVED

> Severity: SEVERE

> Ingredients: PENICILLIN

> Signs/Symptoms: DIARRHEA, HIVES

>           Drug Class: AM110 PENICILLIN-G RELATED PENICILLINS

> Provider Override Reason: N/A - Order Check Not Evaluated by Provider

> Do you want to Intervene? YES//

> Enter your Current Signature Code: SIGNATURE VERIFIED

> Now creating Pharmacy Intervention

> For PENICILLIN VK 250MG TAB

> PROVIDER: INPATIENT-MEDS,PROVIDER PROV

> RECOMMENDATION: 1 CHANGE DRUG

> See 'Pharmacy Intervention Menu' if you want to delete this

> intervention or for more options.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/073.png)Note: “With a severe reaction, an intervention is required”

> <u>Historical</u>:

> Now doing allergy checks.  Please wait...   

> A Drug-Allergy Reaction exists for this medication and/or class! 

>     Prospective Drug: AMPICILLIN 250MG   
>      Causative Agent: AMPICILLIN (ALBANY - 01/14/16)   
>  Historical/Observed: HISTORICAL   
>             Severity: Not Entered   
>          Ingredients: AMPICILLIN   
>       Signs/Symptoms: DRY MOUTH, HIVES   
>           Drug Class: AM111 PENICILLINS,AMINO DERIVATIVES 

>    Provider Override Reason: N/A - Order Check Not Evaluated by Provider 

> Do you want to Intervene? YES// NO

Example: CPRS Allergy Order Entry Process

From the Order tab, enter a new allergy using the Allergies Dialog:

![](inpatient-medications-nurse-s-user-manual-psj-5-423/074.png)

<u>Example of Historical Allergy</u>:

![](inpatient-medications-nurse-s-user-manual-psj-5-423/075.png)

<u>Example of Observed Allergy</u>:

![](inpatient-medications-nurse-s-user-manual-psj-5-423/076.png)

Example: Inpatient Allergy Order Entry Process

<u>Example of Observed Allergy</u>:

<u>Patient Information Jan 15, 2016@09:50:42 Page: 1 of 1</u>

DEF,PATIENT Ward: GEN MED A

PID: 666-66-6661 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 01/01/62 (54) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 04/15/15

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies - Verified: AMIODARONE, AMIODARONE 200MG (PAR), HEPARIN, INDINAVIR,

MINOXIDIL, MORPHINE, PENICILLIN, VANCOMYCIN, ASPIRIN

Non-Verified:

Remote:

Adverse Reactions:

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile <span id="P119" class="anchor"></span>CM New Clinic Medication Entry

Select Action: View Profile// DA

<u>Detailed ADR List Jan 15, 2016@09:51:07 Page: 1 of 2</u>

DEF,PATIENT Ward: GEN MED A

PID: 666-66-6661 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 01/01/62 (54) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 04/15/15

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Verified

Drug:

1 AMIODARONE

2 AMIODARONE 200MG (PAR)

3 HEPARIN

4 INDINAVIR

5 MINOXIDIL

6 MORPHINE

7 PENICILLIN

8 VANCOMYCIN

Drug/Food:

9 ASPIRIN

\+ Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data SA Select Allergy

Select Action: Next Screen// EA

Enter Causative Agent: LIDOC

Checking existing PATIENT ALLERGIES (#120.8) file for matches...

Now checking GMR ALLERGIES (#120.82) file for matches...

Now checking the National Drug File - Generic Names (#50.6)

1 LIDOCAINE

2 LIDOCAINE/MENTHOL

3 LIDOCAINE/MENTHOL/METHYL SALICYLATE

4 LIDOCAINE/NEOMYCIN/POLYMYXIN

5 LIDOCAINE/POVIDONE IODINE

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1

CHOOSE 1-5: 1 LIDOCAINE

LIDOCAINE OK? Yes// (Yes)

(O)bserved or (H)istorical Allergy/Adverse Reaction: O OBSERVED

Select date reaction was OBSERVED (Time Optional): T (JAN 15, 2016) JAN 15,

2016 (JAN 15, 2016)

Are you adding 'JAN 15, 2016' as

a new ADVERSE REACTION REPORTING? No// Y (Yes)

No signs/symptoms have been specified. Please add some now.

The following are the top ten most common signs/symptoms:

1\. ANXIETY 7. HIVES

2\. ITCHING,WATERING EYES 8. DRY MOUTH

3\. ANOREXIA 9. DRY NOSE

4\. DROWSINESS 10. RASH

5\. NAUSEA,VOMITING 11. OTHER SIGN/SYMPTOM

6\. DIARRHEA

Enter from the list above : 7,10

Date(Time Optional) of appearance of Sign/Symptom(s): Jan 15, 2016// (JAN 15, 2

016\)

The following is the list of reported signs/symptoms for this reaction:

Signs/Symptoms Date Observed

---------------------------------------------------------------------------

1 HIVES Jan 15, 2016

2 RASH Jan 15, 2016

Select Action (A)DD, (D)ELETE OR \<RET\>:

Choose one of the following:

A - ALLERGY

P - PHARMACOLOGICAL

U - UNKNOWN

MECHANISM: UNKNOWN// A ALLERGY

COMMENTS:

No existing text

Edit? NO//

Complete the observed reaction report? Yes// (Yes)

DATE/TIME OF EVENT: JAN 15,2016//

OBSERVER: VO,MAI// BIRMINHGAM ALABAMA MV SYSTEMS ANALYST

SEVERITY: SE SEVERE

DATE MD NOTIFIED: Jan 15,2016// (JAN 15, 2016)

Complete the FDA data? Yes// N (No)

Currently you have verifier access.

Would you like to verify this Causative Agent now? Yes// (Yes)

CAUSATIVE AGENT: LIDOCAINE

TYPE: DRUG

INGREDIENTS: LIDOCAINE

VA DRUG CLASSES: CN204 - LOCAL ANESTHETICS,INJECTION

CV300 - ANTIARRHYTHMICS

DE700 - LOCAL ANESTHETICS,TOPICAL

GU900 - GENITO-URINARY AGENTS,OTHER

NT300 - ANESTHETICS,MUCOSAL

OP700 - ANESTHETICS,TOPICAL OPHTHALMIC

PH000 - PHARMACEUTICAL AIDS/REAGENTS

OBS/HIST: OBSERVED

SIGNS/SYMPTOMS: HIVES (Jan 15, 2016)

RASH (Jan 15, 2016)

MECHANISM: ALLERGY

Would you like to edit any of this data? N (No)

PATIENT: DEF,PATIENT CAUSATIVE AGENT: LIDOCAINE

INGREDIENTS: LIDOCAINE VA DRUG CLASSES: ANTIARRHYTHMICS

LOCAL ANESTHETICS,INJ

LOCAL ANESTHETICS,TOP

ANESTHETICS,MUCOSAL

Enter RETURN to continue or '^' to exit:

ANESTHETICS,TOPICAL O

PHARMACEUTICAL AIDS/R

GENITO-URINARY AGENTS

ORIGINATOR: VO,MAI ORIGINATED: Jan 15, 2016@09:52

SIGN OFF: NO OBS/HIST: OBSERVED

SEVERITY: SEVERE OBS D/T: Jan 15, 2016

ID BAND MARKED: CHART MARKED:

SIGNS/SYMPTOMS: HIVES (Jan 15, 2016)

RASH (Jan 15, 2016)

Change status of this allergy/adverse reaction to verified? Y

Opening Adverse React/Allergy record for review...

<u>Browse Document Jan 15, 2016@09:54:33 Page: 1 of 1</u>

Adverse React/Allergy

DEF,P 666-66-6661 GEN MED Adm: 04/15/2015 Dis:

DATE OF NOTE: JAN 15, 2016@09:54:33 ENTRY DATE: JAN 15, 2016@09:54:33

AUTHOR: VO,MAI EXP COSIGNER:

URGENCY: STATUS: UNSIGNED

This patient has had an allergy to LIDOCAINE

verified on Jan 15, 2016@09:54:33.

\+ Next Screen - Prev Screen ?? More actions

Find Sign/Cosign Link ...

Print Copy Encounter Edit

Edit Identify Signers Interdiscipl'ry Note

Make Addendum Delete Quit

Select Action: Quit//

<u>Example of Historical Allergy</u>:

<u>Detailed ADR List Jan 15, 2016@09:51:07 Page: 1 of 2</u>

DEF,PATIENT Ward: GEN MED A

PID: 666-66-6661 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 01/01/62 (54) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 04/15/15

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Verified

Drug:

1 AMIODARONE

2 AMIODARONE 200MG (PAR)

3 HEPARIN

4 INDINAVIR

5 MINOXIDIL

6 MORPHINE

7 PENICILLIN

8 VANCOMYCIN

Drug/Food:

9 ASPIRIN

\+ Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data SA Select Allergy

Select Action: Next Screen// EA

Enter Causative Agent: LIDO

Checking existing PATIENT ALLERGIES (#120.8) file for matches...

,PATIENT DEF,PATIENT 1-1-62 666666661 YES ACTIVE DUTY INP

ATIENT-MEDS,PROVIDER LIDOCAINE

LIDOCAINE OK? Yes// N (No)

Now checking GMR ALLERGIES (#120.82) file for matches...

Now checking the National Drug File - Generic Names (#50.6)

1 LIDOCAINE

2 LIDOCAINE/MENTHOL

3 LIDOCAINE/MENTHOL/METHYL SALICYLATE

4 LIDOCAINE/NEOMYCIN/POLYMYXIN

OBS/

REACTANT VER. MECH. HIST TYPE

-------- ---- ------- ---- ----

AMIODARONE AUTO ALLERGY OBS DRUG

(IODINE)

Reactions: ANXIETY

AMIODARONE 200MG (PAR) YES ALLERGY HIST DRUG

(AMIODARONE, IODINE)

Reactions: ANXIETY

HEPARIN AUTO ALLERGY OBS DRUG

Reactions: DRY MOUTH, DRY NOSE

INDINAVIR AUTO ALLERGY OBS DRUG

(INDINAVIR SULFATE)

Reactions: ITCHING,WATERING EYES, ANOREXIA,

NAUSEA,VOMITING, ANXIETY, DROWSINESS

LIDOCAINE YES ALLERGY OBS DRUG

Reactions: HIVES, RASH

5 LIDOCAINE/POVIDONE IODINE

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 3 LIDOCAINE/MENTHOL/METHYL SALICYLATE

LIDOCAINE/MENTHOL/METHYL SALICYLATE OK? Yes// (Yes)

(O)bserved or (H)istorical Allergy/Adverse Reaction: H HISTORICAL

No signs/symptoms have been specified. Please add some now.

The following are the top ten most common signs/symptoms:

1\. ANXIETY 7. HIVES

2\. ITCHING,WATERING EYES 8. DRY MOUTH

3\. ANOREXIA 9. DRY NOSE

4\. DROWSINESS 10. RASH

5\. NAUSEA,VOMITING 11. OTHER SIGN/SYMPTOM

6\. DIARRHEA

Enter from the list above : 7

Date(Time Optional) of appearance of Sign/Symptom(s):

The following is the list of reported signs/symptoms for this reaction:

Signs/Symptoms Date Observed

---------------------------------------------------------------------------

1 HIVES

Select Action (A)DD, (D)ELETE OR \<RET\>:

Choose one of the following:

A - ALLERGY

P - PHARMACOLOGICAL

U - UNKNOWN

MECHANISM: UNKNOWN// A ALLERGY

COMMENTS:

No existing text

Edit? NO//

Currently you have verifier access.

Would you like to verify this Causative Agent now? Yes// Y (Yes)

CAUSATIVE AGENT: LIDOCAINE/MENTHOL/METHYL SALICYLATE

TYPE: DRUG

INGREDIENTS: LIDOCAINE

MENTHOL

METHYL SALICYLATE

VA DRUG CLASSES: DE900 - DERMATOLOGICALS,TOPICAL OTHER

OBS/HIST: HISTORICAL

SIGNS/SYMPTOMS: HIVES

MECHANISM: ALLERGY

Would you like to edit any of this data? N (No)

PATIENT: DEF,PATIENT CAUSATIVE AGENT: LIDOCAINE/MENTHOL/MET

INGREDIENTS: LIDOCAINE VA DRUG CLASSES: DERMATOLOGICALS,TOPIC

MENTHOL

METHYL SALICYLATE

ORIGINATOR: VO,MAI ORIGINATED: Jan 15, 2016@09:55

SIGN OFF: NO OBS/HIST: HISTORICAL

ID BAND MARKED: CHART MARKED:

Enter RETURN to continue or '^' to exit:

<u>Jan 15, 2016@09:56:46</u>

SIGNS/SYMPTOMS: HIVES

Change status of this allergy/adverse reaction to verified? Y (Yes)

Opening Adverse React/Allergy record for review...

<u>Browse Document Jan 15, 2016@09:56:46 Page: 1 of 1</u>

Adverse React/Allergy

DEF,P 666-66-6661 GEN MED Adm: 04/15/2015 Dis:

DATE OF NOTE: JAN 15, 2016@09:56:45 ENTRY DATE: JAN 15, 2016@09:56:45

AUTHOR: VO,MAI EXP COSIGNER:

URGENCY: STATUS: UNSIGNED

This patient has had an allergy to LIDOCAINE/MENTHOL/METHYL SALICYLATE

verified on Jan 15, 2016@09:56:45.

\+ Next Screen - Prev Screen ?? More actions

Find Sign/Cosign Link ...

Print Copy Encounter Edit

Edit Identify Signers Interdiscipl'ry Note

Make Addendum Delete Quit

Select Action: Quit//

- Clinical Reminder Order Checks - This section describes the Clinical Reminder Order Checks functionality (PSJ\*5\*281).

Order Checks now includes the ability to view Clinical Reminders (prior to the display of Enhanced Drug-Drug interactions). Reminders are used to aid physicians in performing tasks to fulfill Clinical Practice Guidelines and periodic procedures or education as needed for veteran patients

> <span id="p122" class="anchor"></span>Example: Drug-Drug Interactions Display

Inpatient Order Entry Mar 16, 2011@12:04:33 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

> CrCL: 78.1(est.) (CREAT:1.0mg/dL 4/19/12) BSA (m2): 2.21

--------------------------------------------------------------------------------

\- - - - - - - - - - N O N - V E R I F I E D C O M P L E X - - - - - - - - - -

1 LITHIUM TAB,SA C 10/13/2011 10/15/2011 N

Give: 450MG PO QID

LITHIUM TAB,SA C 10/13/2011 10/15/2011 N

Give: 10000MG PO Q4H

2 RILUZOLE TAB C 10/13/2011 10/15/2011 N

Give: 50MG PO BID

RILUZOLE TAB C 10/15/2011 10/16/2011 N

Give: 10000MG PO Q4H

\- - - - - - - - - - - - - P E N D I N G C O M P L E X - - - - - - - - - - - -

3 HALOPERIDOL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 40MG PO BID

----------Enter ?? for more actions---------------------------------------------

PI Patient Information NO New Order Entry

PU Patient Record Update <span id="P124" class="anchor"></span>CM New Clinic Medication Entry

SO Select Order

Select Action: Quit// no New Order Entry

Select DRUG: indinavi

Lookup: DRUG GENERIC NAME

INDINAVIR SULFATE 400MG CAP AM800

...OK? Yes// (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

============================================================================

\*\*\* Clinical Reminder Order Check \| Severity: HIGH \*\*\*

CR3286 CROC - GENTAMICIN OI SEVERITY HIGH (RULE DISPLAY NAME)

CR3286 CROC - GENTAMICIN OI SEVERITY HIGH (RULE ORDER CHECK TEXT)

----------------------------------------------------------------------------

\*\*\* Clinical Reminder Order Check \| Severity: MEDIUM \*\*\*

Potentially Teratogenic Medication (FDA Category D or C)

Concern has been raised about use of this medication during pregnancy.

1\) Pregnancy status should be determined. Discuss use of this medication on the

context of risks to the mother and child of untreated disease. Potential

benefits may warrant use of the drug in pregnant women despite risks.

2\) The patient must be provided contraceptive counseling on potential risk vs.

benefit of taking this medication if she were to become pregnant.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The 'Teratogenic Medications' Order Check will display for female patients

between the ages of 12 and 50, except those with a known exclusion criterion

(e.g., hysterectomy), or those with a documented IUD placement that is more

recent than a documented IUD removal.

----------------------------------------------------------------------------

\*\*\* Clinical Reminder Order Check \| Severity: LOW \*\*\*

CR3286 CROC - GENTAMICIN DRUG SEVERITY LOW (RULE DISPLAY NAME)

CR3286 CROC - GENTAMICIN DRUG SEVERITY LOW (RULE ORDER CHECK TEXT 01) CR3286

CROC - GENTAMICIN DRUG SEVERITY LOW (RULE ORDER CHECK TEXT 02) CR3286 CROC -

GENTAMICIN DRUG SEVERITY LOW (RULE ORDER CHECK TEXT 03) CR3286 CROC -

GENTAMICIN DRUG SEVERITY LOW (RULE ORDER CHECK TEXT 04)

----------------------------------------------------------------------------

> Do you want to Continue? Y// ES

> Enter your Current Signature Code: SIGNATURE VERIFIED

> Now creating Pharmacy Intervention

> For GENTAMICIN 4MG/2ML INTRATHECAL

> PROVIDER: DOCTOR, TEST DT

> RECOMMENDATION: 9 OTHER

> OTHER FOR RECOMMENDATION:

> No existing text

> Edit? NO//

> See 'Pharmacy Intervention Menu' if you want to delete this

> intervention or for more options.

> Press Return to continue...

> Would you like to edit this intervention? N// O

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

================================================================================

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with INDINAVIR SULFATE 400MG CAP:

Local Rx \#501820A (ACTIVE) for SIMVASTATIN 10MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

Processing Status: Not released locally (Window)

Concurrent administration may result in elevated HMG levels, which may

increase the risk of myopathy, including rhabdomyolysis. (1-16)

================================================================================

Display Professional Interaction Monograph(s)? NO//

Do you want to Continue with INDINAVIR SULFATE 400MG CAP? NO// y YES

Now creating Pharmacy Intervention

For INDINAVIR SULFATE 400MG CAP

PROVIDER: PSJPROVIDER,ONE TP

RECOMMENDATION: ?

Answer with APSP INTERVENTION RECOMMENDATION, or NUMBER

Choose from:

1 CHANGE DRUG

2 CHANGE FORM OR ROUTE OF ADMINISTRATION

3 ORDER LAB TEST

4 ORDER SERUM DRUG LEVEL

5 CHANGE DOSE

6 START OR DISCONTINUE A DRUG

7 CHANGE DOSING INTERVAL

8 NO CHANGE

9 OTHER

RECOMMENDATION: 8 NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention? N// O

Available Dosage(s)

1\. 400MG

2\. 800MG

Select from list of Available Dosages or Enter Free Text Dose: 1 400MG

You entered 400MG is this correct? Yes// YES

MED ROUTE: ORAL (BY MOUTH)// PO

SCHEDULE: QDAY//

1 QDAY 0900

2 QDAY-DIG 1300

3 QDAY-WARF 1300

CHOOSE 1-3: 1 0900

SCHEDULE TYPE: CONTINUOUS// CONTINUOUS

ADMIN TIMES: 0900//

SPECIAL INSTRUCTIONS:

START DATE/TIME: MAR 16,2011@12:08// MAR 16,2011@12:08

STOP DATE/TIME: MAR 17,2011@24:00// MAR 17,2011@24:00

Expected First Dose: MAR 17,2011@09:00

PROVIDER: PHARMACIST,SEVENTEEN// 145

NON-VERIFIED UNIT DOSE Mar 16, 2011@12:07:46 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

--------------------------------------------------------------------------------

(1)Orderable Item: INDINAVIR CAP,ORAL

Instructions:

(2)Dosage Ordered: 400MG

Duration: (3)Start: 03/16/2011 12:08

\(4\) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 03/17/2011 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: QDAY

\(9\) Admin Times: 0900

\(10\) Provider: PHARMACIST,SEVENTEEN

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR SULFATE 400MG CAP 1

+---------Enter ?? for more actions---------------------------------------------

ED Edit AC ACCEPT

Select Item(s): Next Screen// ac ACCEPT

Press Return to continue...

NATURE OF ORDER: WRITTEN// W

...transcribing this non-verified order....

NON-VERIFIED UNIT DOSE Mar 16, 2011@12:08:04 Page: 1 of 2

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

--------------------------------------------------------------------------------

\*(1)Orderable Item: INDINAVIR CAP,ORAL

Instructions:

\*(2)Dosage Ordered: 400MG

Duration: (3)Start: 03/16/2011 12:08

\*(4) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 03/17/2011 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QDAY

\(9\) Admin Times: 0900

\*(10) Provider: PHARMACIST,SEVENTEEN \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR SULFATE 400MG CAP 1

+---------Enter ?? for more actions---------------------------------------------

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// NEXT SCREEN

### Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinic orders are created via CPRS generally using the Meds Inpatient tab or the IV Fluids tab. Drug orders that have a clinic and an appointment date and time are considered clinic orders. The clinic must be defined with ‘ADMINISTER INPATIENT MEDS?’ prompt answered YES under the SETUP A CLINIC \[SDBUILD\] option in the Scheduling package. Defining the clinic in this manner ensures that an appointment date and time are defined.<span id="P127" class="anchor"></span>

Patch PSJ\*5\*319 added functionality to allow users to create clinic orders in backdoor. Users can select the action, CM New Clinic Medication Entry, available on the ListMan Inpatient

order entry screen to create a new clinic order.

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen// CM New Clinic Medication Entry

Visit Location: GENERAL MEDICINE

Date/Time of Visit: NOW// (AUG 10, 2020@13:57)

Select DRUG:

MOCHA v1.0 Enhancements 1 adds drug interaction and therapeutic duplication order checks for clinic orders to Outpatient Pharmacy. Previously Inpatient Medications package performed order checks on active, pending and non-verified clinic orders. With the MOCHA v1.0 Enhancements 1, Inpatient medications will perform enhanced order checks for recently discontinued and expired inpatient medications clinic orders.

For both packages, the system will display clinic orders in a standard format to differentiate them from Inpatient Medications and Outpatient Pharmacy order checks.

Based on the number of days defined in the IMO DC/EXPIRED DAY LIMIT field (#6) in CLINIC DEFINITION file (#53.46), the enhanced order checks process will only include discontinued and expired drug interactions and/or duplicate therapy orders with a stop date that falls within the range defined. The following are the scenarios that drive which dates will be displayed for the clinic order:

- If there are start/stop dates defined, they are displayed.
- If there are no stop/start dates defined, the ‘requested start/stop dates’ will be displayed with the word “Requested” prior to the start/stop date header.
- If there are no requested start/stop dates defined, the order date will be displayed and the start/stop date headers will be displayed with “\*\*\*\*\*\*\*\*” for the date.
- If there is either a requested start date or a requested stop date, the available date will be displayed and “\*\*\*\*\*\*\*\*” will be displayed for the undefined date.

Unit Dose Clinic Order Check example:

Now Processing Enhanced Order Checks!  Please wait...

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with CIMETIDINE 300 MG:

      Clinic Order: PHENYTOIN 100MG CAP (DISCONTINUED)

          Schedule: Q8H

           Dosage: 100MG

        Start Date: 02/27/2012@13:00

         Stop Date: 02/28/2012@15:22:27

Concurrent use of cimetidine or ranitidine may result in elevated levels

of and toxicity from the hydantoin.Neutropenia and thrombocytopenia have

been reported with concurrent cimetidine and phenytoin. 

IV Clinic Order Check example:

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with WARFARIN 2MG TAB:

      Clinic Order: POTASSIUM CHLORIDE 20 MEQ (ACTIVE)

Other Additive(s): MAGNESIUM SULFATE 1 GM (1), CALCIUM GLUCONATE 1 GM (2),

                    HEPARIN 1000 UNITS, CIMETIDINE 300 MG

       Solution(s): DEXTROSE 20% 500 ML 125 ml/hr

                    AMINO ACID SOLUTION 8.5% 500 ML 125 ml/hr

        Start Date: 04/05/2012@15:00

         Stop Date: 04/27/2012@24:00

The pharmacologic effects of warfarin may be increased resulting in severe

bleeding.

Therapeutic Duplication - IV and Unit Dose clinic order therapeutic duplications display in the same format as drug interactions.

Unit Dose Clinic Order Check example:

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

POTASSIUM CHLORIDE 30 MEQ

Clinic Order: POTASSIUM CHLORIDE 10MEQ TAB (PENDING)

Schedule: BID

Dosage: 20MEQ

Requested Start Date: 11/20/2012@17:00

Stop Date: \*\*\*\*\*\*\*\*

Class(es) Involved in Therapeutic Duplication(s): Potassium

IV Order Check example:

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

CEFAZOLIN 1 GM

Clinic Order: CEFAZOLIN 2 GM (PENDING)

Solution(s): 5% DEXTROSE 50 ML

Order Date: 11/20/12@11:01

Start Date: \*\*\*\*\*\*\*\*

Stop Date: \*\*\*\*\*\*\*\*

Clinic Order: CEFAZOLIN SOD 1GM INJ (EXPIRED)

Solution(s): 5% DEXTROSE 50 ML

Start Date: 10/24/2012@16:44

Stop Date: 10/25/2012@24:00

Class(es) Involved in Therapeutic Duplication(s): Beta-Lactams,

Cephalosporins, Cephalosporins - 1st Generation

- Drug-Allergy Interactions – Drug allergy interactions will be either critical or significant. If the Dispense Drug selected is identified as having an interaction with one of the patient’s allergies, the allergy the drug interacts with will be displayed.
- CPRS Order Check: Aminoglycoside Ordered

> Trigger: Ordering session completion.

> Mechanism: For each medication order placed during this ordering session, the CPRS Expert System requests the pharmacy package to determine if the medication belongs to the VA Drug Class ‘Aminoglycosides’. If so, the patient’s most recent BUN results are used to calculate the creatinine clearance then OERR is notified and the warning message is displayed.

> \[Note: The creatinine clearance value displayed in some order check messages is an estimate based on adjusted body weight if patient height is \> 60 inches. Approved by the CPRS Clinical Workgroup 8/11/04, it is based on a modified Cockcroft-Gault formula and was installed with patch OR\*3\*221.

> For more information: <http://www.ascp.com/public/pubs/tcp/1999/jan/cockcroft.shtml>

> CrCl (male) = (140 - age) x (adj body weight\* in kg)

> --------------------------------------

> (serum creatinine) x 72

> \* If patient height is not greater than 60 inches, actual body weight is used.

> CrCl (female) = 0.85 x CrCl (male)

> To calculate adjusted body weight, the following equations are used:

> Ideal body weight (IBW) = 50 kg x (for men) or 45 kg x (for women) + 2.3 x (height in inches - 60)

> Adjusted body weight (Adj. BW) if the ratio of actual BW/IBW \> 1.3 = (0.3 x (Actual BW - IBW)) + IBW

> Adjusted body weight if the ratio of actual BW/IBW is not \> 1.3 = IBW or Actual BW (whichever is less)\]

> Message: Aminoglycoside - est. CrCl: \<value calculated from most recent serum creatinine\>. (CREAT: \<result\> BUN: \<result\>).

> Danger Lvl: This order check is exported with a High clinical danger level.

- CPRS Order Check: Dangerous Meds for Patients \>64

> DANGEROUS MEDS FOR PT \> 64 – Yes

> This is based on the BEERS list. This order check only checks for three drugs: Amitriptyline, Chlorpropamide and Dipyridamole. The workgroup felt that the list of drugs should be expanded. A request can be sent to CPRS for this.

> Trigger: Acceptance of pharmacy orderable items amitriptyline, chlorpropamide or dipyridamole.

> Mechanism: The CPRS Expert System determines if the patient is greater than 64 years old. It then checks the orderable item of the medication ordered to determine if it is mapped as a local term to the national term DANGEROUS MEDS FOR PTS \> 64.

> Message: If the orderable item text contains AMITRIPTYLINE this message is displayed:

> Patient is \<age\>. Amitriptyline can cause cognitive impairment and loss of balance in older patients. Consider other antidepressant medications on formulary.

> If the orderable item text contains CHLORPROPAMIDE this message is displayed:

> Patient is \<age\>. Older patients may experience hypoglycemia with Chlorpropamide due do its long duration and variable renal secretion. They may also be at increased risk for Chlorpropamide-induced SIADH.

> If the orderable item text contains DIPYRIDAMOLE this message is displayed:

> Patient is \<age\>. Older patients can experience adverse reactions at high doses of Dipyridamole (e.g., headache, dizziness, syncope, GI intolerance.) There is also questionable efficacy at lower doses.

> Danger Lvl: This order check is exported with a High clinical danger level.

- CPRS Order Check: Glucophage Lab Results

> Glucophage-Lab Results Interactions

> Trigger: Selection of a Pharmacy orderable item.

> Mechanism: The CPRS Expert System checks the pharmacy orderable item’s local text (from the Dispense Drug file \[#50\]) to determine if it contains “glucophage” or “metformin”. The expert system next searches for a serum creatinine result within the past x number of days as determined by parameter ORK GLUCOPHAGE CREATININE. If the patient’s creatinine result was greater than 1.5 or does not exist, OE/RR is notified and the warning message is displayed.

> Message: Metformin– no serum creatinine within past \<x\> days. else:

> Metformin – Creatinine results: \<creatinine greater than 1.5 w/in past \<x\> days\>

> Danger Lvl: This order check is exported with a High clinical danger level.

### Order Validation Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following order validation checks will apply to Unit Dose orders and to intermittent IV orders.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/077.png)Note: IV orders do not have Schedule Type.

- Order Validation Check One

For intermittent IV orders, references to an order’s Schedule Type will refer to either the TYPE OF SCHEDULE from the Administration Schedule file (#51.1), or PRN for schedule names in PRN format, or CONTINUOUS for schedule names in Day of Week format.

- Order Validation Check Two

The system shall use the schedule type of the schedule from the Administration Schedule file independent of the schedule name when processing an order to determine if administration times are required for a particular order.

- Order Validation Check Three

If an order has the Schedule Type of Continuous, the Schedule entered is NOT in Day of Week (Ex. MO-FR) or PRN (Ex. TID PC PRN) format, and the frequency associated with the schedule is one day (1440 minutes) or less, the system will not allow the number of administration times associated with the order to be greater than the number of administration times calculated for that frequency. The system will allow for the number of administration times to be LESS than the calculated administration times for that frequency but not less than one administration time. (For example, an order with a schedule of BID is associated with a frequency of 720 minutes. The frequency is divided into 1440 minutes (24 hours) and the resulting calculated administration time is two. For this order, the number of administration times allowed may be no greater than two, but no less than one. Similarly, a schedule frequency of 360 minutes must have at least one administration time but cannot exceed four administration times.)

If an order has the Schedule Type of Continuous, the Schedule entered is NOT in Day of Week (Ex. MO-FR) or PRN (Ex. TID PC PRN) format, and the frequency associated with the schedule is greater than one day (1440 minutes) and evenly divisible by 1440, only one administration time is permitted. (For example, an order with a schedule frequency of 2880 minutes must have ONLY one administration time. If the frequency is greater than 1440 minutes and not evenly divisible by 1440, no administration times will be permitted.)

The system shall present warning/error messages to the user if the number of administration times is less than or greater than the maximum admin times calculated for the schedule or if no administration times are entered. If the number of administration times entered is less than the maximum admin times calculated for the schedule, the warning message: “The number of admin times entered is fewer than indicated by the schedule.” shall appear. In this case, the user will be allowed to continue after the warning. If the number of administration times entered is greater than the maximum admin times calculated for the schedule, the error message: “The number of admin times entered is greater than indicated by the schedule.” shall appear. In this case, the user will not be allowed to continue after the warning. If no admin times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

- Order Validation Check Four

If an order has a Schedule Type of Continuous and is an Odd Schedule {a schedule whose frequency is not evenly divisible by or into 1440 minutes (1 day)}, the system shall prevent the entry of administration times. For example, Q5H, Q17H – these are not evenly divisible by 1440. In these cases, the system shall prevent access to the administration times field. No warning message is presented.

- Order Validation Check Five

If an order has a Schedule Type of Continuous with a non-odd frequency of greater than one day, (1440 minutes) the system shall prevent more than one administration time, for example, schedules of Q72H, Q3Day, and Q5Day.

If the number of administration times entered exceeds one, the error message: “This order requires one admin time” shall appear. If no administration times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

- Order Validation Check Six

If an order has a Schedule Type of One Time, or if an order is entered with a schedule that is defined in the schedule file as One Time, the system shall prevent the user from entering more than one administration time.

If more than one administration time is entered, the error message: “This is a One Time Order - only one administration time is permitted.” shall appear. No administration times are required.

- Order Validation Check Seven

For an order with a Schedule Type of Continuous where no doses/administration times are scheduled between the order’s Start Date/Time and the Stop Date/Time, the system shall present a warning message to the user and not allow the order to be accepted or verified until the Start/Stop Date Times, schedule, and/or administration times are adjusted so that at least one dose is scheduled to be given.

If the stop time will result in no administration time between the start time and stop time, the error message: “There must be an admin time that falls between the Start Date/Time and Stop Date/Time.” shall appear.

### Display of Provider Overrides and Pharmacist Interventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Inpatient Medications, the first time a field preceded by an asterisk (\*) is selected for editing and when renewing an order, if Current Pharmacist Interventions exist for the order, entering Y (Yes) at the prompt, “Order Check Overrides/Interventions exist for this order. Display? (Y/N)? Y//,” will display the following information when the fields are populated with data:

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Heading: Current Pharmacist Interventions for this order</p></li>
</ul></th>
<th><ul>
<li><blockquote>
<p>Recommendation Accepted</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Intervention Date/Time</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Agree With Provider</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Provider</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Rx #</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Pharmacist</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Division</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Drug,</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Financial Cost</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Instituted By</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Other For Intervention</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Intervention</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Reason For Intervention</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Other For Recommendation</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Action Taken</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Originating Package</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Clinical Impact</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>Was Provider Contacted</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Financial Impact</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>Provider Contacted</p>
</blockquote></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

============================================================================

\*\* Current Provider Overrides for this order \*\*

============================================================================

Overriding Provider: PSJPROVIDER,ONE (PROVIDER)

Override Entered By: PSJPROVIDER,ONE (PROVIDER)

Date/Time Entered: 7/12/11 09:13

Override Reason: Testing 9 OTHER

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN NA

(GOLDEN STATE) 2MG TAB \[ACTIVE\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN(GOLDEN

ST) 0.5MG(1/2X1MG) TAB \[UNRELEASED\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

Press RETURN to Continue or '^' to Exit :

============================================================================

\*\* Current Pharmacist Interventions for this order \*\*

============================================================================

Intervention Date: 7/12/11 09:14

Provider: PSJPROVIDER,ONE Pharmacist: PSJPHARMACIST,ONE

Drug: METRONIDAZOLE 250MG TAB Instituted By: PHARMACY

Intervention: CRITICAL DRUG INTERACTION

Recommendation: OTHER Originating Package: INPATIENT

Other For Recommendation:

INTERVENTION FOR CRITICAL DRUG-DRUG

Press RETURN to Continue or '^' to Exit :

Intervention TIME displays to the right of the date (e.g., 01/18/11 09:04)

If Historical Overrides/Interventions exist for an order, entering Y (Yes) at the prompt: “View Historical Overrides/Interventions for this order (Y/N)? Y//,” displays the Historical Pharmacist Intervention information:

============================================================================

\*\* Historical Pharmacist Interventions for this order \*\*

============================================================================

Intervention Date: 07/12/11 09:14

Provider: PSJPROVIDER,ONE Pharmacist: PSJPHARMACIST,ONE

Drug: METRONIDAZOLE 250MG TAB Instituted By: PHARMACY

Intervention: CRITICAL DRUG INTERACTION

Recommendation: OTHER Originating Package: INPATIENT

Other For Recommendation:

Testing 9 OTHER

Press RETURN to Continue or '^' to Exit :

============================================================================

\*\* Historical Provider Overrides for this order \*\*

============================================================================

Overriding Provider: PSJPROVIDER,ONE (PROVIDER)

Override Entered By: PSJPROVIDER,ONE (PROVIDER)

Date/Time Entered: 07/12/11 09:13

Override Reason: Testing 9 OTHER

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN NA

(GOLDEN STATE) 2MG TAB \[ACTIVE\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN(GOLDEN

ST) 0.5MG(1/2X1MG) TAB \[UNRELEASED\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

Intervention TIME displays to the right of the date (e.g., 01/18/11 09:04. Current Pharmacist Intervention fields and labels also display, when the fields are populated.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/078.png)<span id="p123" class="anchor"></span>Note: In Inpatient Medications, if no Current Pharmacist Interventions exist when editing a field preceded by an asterisk (\*),the following displays:

============================================================================

\*\* Current Pharmacist Interventions for this order \*\*

============================================================================

No Pharmacist Interventions to display

### Dosing Order Checks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v2.0 implements the first increment of dosage checks and introduces the Maximum Single Dose Check for simple and complex orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.1b implements the second increment of dosage checks and introduces the Max Daily Dose Check for simple orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.0 and MOCHA v2.1b use the same interface to First Databank (FDB) as MOCHA v1.0.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/079.png)Note: Please refer to the Dosing Order Checks User Manual for a detailed description of dosing order checks.

## Check Drug Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ CHECK DRUG INTERACTION\]

The Check Drug Interaction option allows a user to check for a drug interaction and Therapeutic Duplications between two or more drugs. This option shall be placed on the Unit Dose Medications \[PSJU MGR\] Menu, and the IV \[PSJI MGR\] Menu.

Example: Checking for drug interactions

Select IV Menu Option: Check Drug Interaction

Drug 1: CIMETIDINE 300MG TAB GA301

...OK? Yes// (Yes)

Drug 2: WARFARIN 5MG TAB

Lookup: GENERIC NAME

WARFARIN 5MG TAB BL110

...OK? Yes// (Yes)

Drug 3:

Now Processing Enhanced Order Checks! Please wait...

\*\*\* DRUG INTERACTION(S) \*\*\*

============================================================

\*\*\*Critical\*\*\* with WARFARIN 5MG TAB and

CIMETIDINE 300MG TAB

CLINICAL EFFECTS: The pharmacologic effects of warfarin may be

increased resulting in severe bleeding.

============================================================

Press Return to Continue...:

Display Professional Interaction monograph? N// YES

DEVICE: HOME// SSH VIRTUAL TERMINAL Right Margin: 80//

------------------------------------------------------------

Professional Monograph

Drug Interaction with WARFARIN 5MG TAB and CIMETIDINE 300MG TAB

This information is generalized and not intended as specific medical

advice. Consult your healthcare professional before taking or

discontinuing any drug or commencing any course of treatment.

MONOGRAPH TITLE: Anticoagulants/Cimetidine

SEVERITY LEVEL: 2-Severe Interaction: Action is required to reduce

the risk of severe adverse interaction.

MECHANISM OF ACTION: Inhibition of warfarin hepatic metabolism. The

effect appears to be greater on the less active R-warfarin than on the

S-warfarin.

CLINICAL EFFECTS: The pharmacologic effects of warfarin may be

increased resulting in severe bleeding.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with WARFARIN 5MG TAB and CIMETIDINE 300MG TAB

PREDISPOSING FACTORS: None determined.

PATIENT MANAGEMENT: Coadministration of cimetidine and warfarin

should be avoided. If they are administered concurrently, monitor

anticoagulant activity and adjust the dose of warfarin indicated. The

H-2 antagonists famotidine and nizatidine are unlikely to interact

with warfarin.The time of highest risk for a coumarin-type drug

interaction is when the precipitant drug is initiated or discontinued.

Contact the prescriber before initiating, altering the dose or

discontinuing either drug.

DISCUSSION: The majority of drug interaction reports involving H-2

antagonists and warfarin have occurred with cimetidine. Reports of a

possibly significant interaction between ranitidine and warfarin have

been equivocal. Famotidine and nizatidine do not appear to affect

prothrombin time.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with WARFARIN 5MG TAB and CIMETIDINE 300MG TAB

REFERENCES:

1.Silver BA, Bell WR. Cimetidine potentiation of the

hypoprothrombinemic effect of warfarin. Ann Intern Med 1979

Mar;90(3):348-9.

2.Wallin BA, Jacknowitz A, Raich PC. Cimetidine and effect of

warfarin. Ann Intern Med 1979 Jun;90(6):993.

3.Serlin MJ, Sibeon RG, Breckenridge AM. Lack of effect of ranitidine

on warfarin action. Br J Clin Pharmacol 1981 Dec;12(6):791-4.

4.Kerley B, Ali M. Cimetidine potentiation of warfarin action. Can Med

Assoc J 1982 Jan 15;126(2):116.

5.Desmond PV, Mashford ML, Harman PJ, Morphett BJ, Breen KJ, Wang YM.

Decreased oral warfarin clearance after ranitidine and cimetidine.

Clin Pharmacol Ther 1984 Mar;35(3):338-41.

6.Toon S, Hopkins KJ, Garstang FM, Rowland M. Comparative effects of

ranitidine and cimetidine on the pharmacokinetics and pharmacodynamics

of warfarin in man. Eur J Clin Pharmacol 1987;32(2):165-72.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with WARFARIN 5MG TAB and CIMETIDINE 300MG TAB

7.Cournot A, Berlin I, Sallord JC, Singlas E. Lack of interaction

between nizatidine and warfarin during chronic administration. J Clin

Pharmacol 1988 Dec;28(12):1120-2.

8.Hussey EK, Dukes GE. Do all histamine2-antagonists cause a warfarin

drug interaction?. DICP 1989 Sep;23(9):675-9.

9.Hunt BA, Sax MJ, Chretien SD, Gray DR, Frank WO, Lalonde RL.

Stereoselective alterations in the pharmacokinetics of warfarin

enantiomers with two cimetidine dose regimens. Pharmacotherapy 1989;

9(3):184.

10.Baciewicz AM, Morgan PJ. Ranitidine-warfarin interaction. Ann

Intern Med 1990 Jan 1;112(1):76-7.

Copyright 2012 First DataBank, Inc.

------------------------------------------------------------

Enter RETURN to continue or '^' to exit:

Display Professional Interaction monograph? N// O

## Pharmacy - Edit Clinic Med Orders Start Date/Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ ECO\]

The *Edit Clinic Med Orders Start Date/Time* \[PSJ ECO\] option allows the user to change the selected date/range of all active or non-verified clinic orders (Unit Dose, IV, IVP/IVPB) to a new single START DATE/TIME for a patient(s) within a selected clinic. This option provides:

- An action that allows the user to edit the Start Date/Time of a patient order.
- Patient selection by medication order start date and by Clinic Group, Clinic, or Patient.
- The Pharmacy User is warned if they attempt to enter a start date more than 7 days in the future.
- A patient profile display of active or non-verified Clinic medication orders for date/time range selected.
- Automatic retrieval, one patient at a time, based on the type of patient selection, when editing a medication Start Date/Time for one or multiple patient Clinic medication orders. Date/Time edits are confirmed for each patient.
- Actions to view the patient’s full order entry profile, details of specific clinic and non-clinic orders.
- Various warnings and message prompts to the user when certain profile or order conditions occur, allowing the user to view, exit, or proceed with the edit process.
- The *Edit Clinic Med Orders Start Date/Time* \[PSJ ECO\] option has changes to reflect the new fields related to medications requiring removal. The user will be directed to go to the [Inpatient Order Entry \[PSJ OE\]](\l) option to modify the orders that contain medications requiring removal.

### Search Med Orders Date Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A search med orders date entry prompt is the first prompt from the *Edit Clinic Med Orders Start Date/Time* \[PSJ ECO\] menu option:

- The Begin Search Date defaults to “ TODAY//” (current date).
- The End Search Date defaults to the entered Begin Search Date. The End Search Date shall not precede the Begin Search Date.

Example: Prompt that End Search Date Shall Not Precede Begin Search Date

Begin Search Date: TODAY//06/01  (JUN 01, 2012)

End Search Date: Jun 01, 2012// 05/15  (MAY 15, 2012)

Response must not precede 6/1/2012.

End Search Date: Jun 01, 2012//

- Time entry with the date is optional.
- The search results include all active or non-verified clinic orders within the selected date range, not just those with a start date within the range. Current business rules apply for date/time validation entry.

Example: Prompt to Search Begin and End Dates

Search for Active and Non-Verified CLINIC Medication Orders

that fall within the date range selected below:

Begin Search Date: TODAY// (default to current date)

End Search Date: (default to the entered Begin Search Date:)

### Search by Clinic, Clinic Group or Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The entry prompt “Search by CLINIC (C), CLINIC GROUP (G), or PATIENT (P):” allows the user to search by clinic, clinic group or patient, with no default, from the *Edit Clinic Med Orders Start Date/Time* \[PSJ ECO\] menu option.

Example: Prompt to Select Clinic, Clinic Group or Patient

Search by CLINIC (C), CLINIC GROUP (G) or PATIENT (P):

The appropriate entry prompt “C,” “G,” or “P” is provided and allows the user to enter a Clinic, Clinic Group or Patient name. Current business rules apply to the entry of clinic name, clinic group or patient name.

Table: Prompt Entry for Clinic, Clinic Group or Patient

| Entry Result | System Prompt     | User Entry                                                                     |
|------------------|-----------------------|------------------------------------------------------------------------------------|
| C                | “SELECT CLINIC:”      | Clinic name – case inclusive (display clinics that are marked allow clinic orders) |
| G                | “SELECT CLINIC GROUP” | Clinic group name                                                                  |
| P                | “SELECT PATIENT:”     | Patient name                                                                       |

The entry prompt, “SELECT CLINIC:” or “SELECT PATIENT:” is repeated allowing the user to select multiple clinics or multiple patients by entering individual names for the search. A blank return stops the search, and the process continues.

### Select Patient from Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user selects “Clinic,” the numbered list of active patients’ full names displays in alphabetical order by last name for all active or non-verified clinic orders (Unit Dose, IV, IVP, IVPB) from the med orders date/time range entered.

Example: Display Patient List

CLINIC ORDERS - PATIENT CLINIC

No.    PATIENT

--------------------------------------------------------------------------------

   1    CPRSPATIENT, ONE (0091)

   2    CPRSPATIENT, TWO (5555)

   3    CPRSPATIENT, THREE (0038)

Select 1 - 3:

If the user selects “Clinic,” an entry prompt of “Select N – N:” displays. N – N represents the begin/end number of displayed patients. The user may select one or multiple patients. Current business rules apply to numbered entry list selection.

Example: Prompt to Select Patient

Select 1 – 1:

### View Patient Clinic Order Entry Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Clinic Order Entry Patient profile view of active followed by non-verified orders, is provided based on the filter selection choices previously made.

Example: Display Clinic Order Entry Patient Profile

Clinic Order Entry May 06, 2011@09:46:50 Page: 1 of 2

CPRSPATIENT,ONE Ward: 3 North

PID: 666-01-0123 Room-Bed: 123-A Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 10/10/58 (52) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Last Admitted: 03/28/11

Dx: SICK Discharged: 03/28/11

CLINIC ORDERS: May 10, 2013 to May 12, 2013@24:00

\- - - - - - - - - - - - - - - - PATIENT CLINIC - - - - - - - - - - - - - - - -

1 FLUOROURACIL INJ,SOLN C 05/12/2013 05/17/2013 A

Give: IV ONCE

2 ABACAVIR/LAMIVUDINE TAB C 05/10/2013 05/17/2013 N

Give: 1 TABLET PO BID

\+ Enter ?? for more actions

ES Edit Start Date VP View Profile

VD View Order Detail CD Change Date Range

Select Action:Quit//

![](inpatient-medications-nurse-s-user-manual-psj-5-423/080.png)Note: If the user selects “by Patient” orders for all clinics for that patient are displayed rather than orders from a single clinic. This is the alternate path re-entry point when selecting by patient.

The following user actions are provided in the Clinic Order Entry Patient profile:

- ES Edit Start Date
- VD View Order Detail
- VP View Profile
- CD Change Date Range
- Quit

#### ES Edit Start Date

The “ES” (Edit Start Date) action allows the user to select medication orders to edit. The system provides an entry prompt “Select Orders: (N-N):” when ES is entered. (N - N) represents the begin/end number from the displayed number list in the Clinic Order Entry profile. The system proceeds to entry prompt “NEW START DATE/TIME:”

#### VD View Order Detail

The “VD” (View Order Detail) action allows the user to select the medication orders to view. The following attributes are provided:

- View Only
- No Patient Demographics
- Order Details Only
- Allowed Action of QUIT

Example: Display VD View Order Detail

Patient: CPRSPATIENT, THREE Status: ACTIVE

\*(1) Additives: Order number: 1 Type: ADMIXTURE

5-FLUOURACIL 11 MG

\*(2) Solutions:

DEXTROSE 20% DEXTROSE TEST 500 ML

Duration: \*(4) Start: 04/12/2012 09:39

\*(3) Infusion Rate: 11 ml/hr

\*(5) Med Route: IM \*(6) Stop: 04/13/2012 24:00

\*(7) Schedule: Last Fill: 04/12/2012 09:44

\(8\) Admin Times: Quantity: 1

\*(9) Provider: MACOY, BONES \[es\] Cum. Doses: 1

\(10\) Other Print: (11) Remarks :

IV Room: TST ISC ROOM

Entry By: PROVIDER, ONE Entry Date: 04/12/12 09:44

Enter RETURN to continue or '^' to exit: Select Action: Quit// Quit

#### VP View Profile

The “VP” (View Profile) action allows the user to view the order profile for all medication orders. The following attributes are provided:

- Entire Patient Profile Non-Clinic and Clinic medication orders are displayed.
- This is a display only action.
- The Quit action is allowed.

Medication orders display in the following sequence:

1.  Non-clinic inpatient medication orders display in the usual manner.
2.  Clinic medication orders display by clinic name in alphabetical order as follows:
- Pending
- Non-verified
- Active
- Discontinued/expired
3.  Non-active, non-clinic medication orders display at the bottom of the profile list.

Example: Display VP View Profile

                                I N P A T I E N T   M E D I C A T I O N S       03/06/13  10:17

                              VAMC:  ALBANY (500)

\- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

TESTPATNM,PATIENT                   Ward: IP WARD

    PID: 666-00-0195      Room-Bed: \* NF \*           Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

    DOB: 07/07/67  (45)                              Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

    Sex: FEMALE                                    Admitted: 10/31/94

     Dx: SICK                              Last transferred: 05/07/03

   CrCL: \<Not Found\> (CREAT: Not Found)            BSA (m2): \_\_\_\_\_\_\_\_\_

Allergies: CEFAZOLIN, PENICILLIN, VALIUM, WARFARIN, ASPIRIN,

            BISMUTH SUBSALICYLATE, EGGS, LACTOSE, MILK, BACON ( FREE TEXT ),

            ICE CREAM, STRAWBERRIES

NV Aller.: CIMETIDINE

       ADR: AMPICILLIN

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

   1     BACLOFEN TAB                             R  03/04/2013  03/15/2013  A

           Give: 10MG PO Q4H

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

   2     CEFAMANDOLE INJ                          C  02/13/2013  03/17/2013  N

           Give: 10 GM IVP Q3D@0900                    

   3     5-FLUOURACIL 100 MG                      C  02/15/2013  03/17/2013  N

         in DEXTROSE 10% 1000 ML  200 ml/hr

\- - - - - - - - - - - - - - - -  P E N D I N G - - - - - - - - - - - - - - - -

   4     BACLOFEN TAB                             C  \*\*\*\*\*  \*\*\*\*\*  P

           Give: 20MG PO BID

   5     CAPTOPRIL TAB                            C  \*\*\*\*\*  \*\*\*\*\*  P

           Give: 25MG PO BID

   6     FLUOROURACIL INJ,SOLN                    C  \*\*\*\*\*  \*\*\*\*\*  P

           Give: 100MG/2ML IV BID

\- - - - - - - - - - - - - - - - - CLINIC NAME - - - - - - - - - - - - - - - -

   7     BACLOFEN TAB                             C  02/25/2013  03/27/2013  A

           Give: 10MG ORALSL Q4H

           Instructions too long. See Order View or BCMA for full

           text.

View ORDERS (1-7):

#### CD Change Date Range

The “CD” (Change Date Range) action in the Clinic Order Entry view allows the user to change the search date range for the current patient’s clinic orders. The user may begin a new search by entering a new Begin Search Date and End Search Date for the current patient and continue with the ECO process. The original date range entry remains unchanged for other patients after completing the CD action for the current patient. To assist the user in selecting clinics and patients, clinics are displayed alphabetically along with the associated patients, within the selected date range and clinic group. The Clinic Order Entry profile displays after the completion of the patient selection for all the selected clinics.

Example: Clinic and Patient Display

Search by CLINIC (C), CLINIC GROUP (G), or PATIENT (P) : gROUP

Select CLINIC GROUP: gROUP ONE

CLINIC ORDERS - BECKY'S CLINIC

No. PATIENT

--------------------------------------------------------------------------------

1 CPRSPATIENT, ONE (0091)

2 CPRSPATIENT, TWO (5555)

3 CPRSPATIENT, THREE (0038)

4 CPRSPATIENT, FOUR (0237)

Select 1 - 4: 3

CLINIC ORDERS - CLINIC (45)

No. PATIENT

--------------------------------------------------------------------------------

1 CPRSPATIENT, TWO (5555)

2 CPRSPATIENT, THREE (0038)

Select 1 - 2: 1

If the user selects by “Patient,” and no active/non-verified orders exist within the entered date range, the below message displays.

Example: No Active/Non-Verified Clinic Orders by Patient Message

No ACTIVE AND/OR NON-VERIFIED Clinic Orders found for this patient

If the user selects by “Clinic,” and no active/non-verified orders exist within the entered date range, the below message displays.

Example: No Active/Non-Verified Clinic Orders by Clinic Message

NO ACTIVE AND/OR NON-VERIFIED ORDERS FOR SELECTED CLINIC

#### Quit

The entry prompt “Select Action: Quit//” displays on the Clinic Order Entry Patient profile after the Inpatient Medications profile display for the selected patient(s). The number entered forces the use of the VD action with a “Enter RETURN to continue or ‘^’ to exit” prompt.

Example: Entering a Number Response to “Select Action: Quit//” Prompt

Select Action: Quit// 1

 \<    ----------------------------------------------------------------------

Patient: BCMAPATIENT,EIGHT                     Status: ACTIVE

Orderable Item: ATENOLOL TAB

  Instructions:

Dosage Ordered: 100MG

      Duration:                               Start: 06/18/2012  11:00

     Med Route: ORAL (PO)

                                               Stop: 06/22/2012  11:00

Schedule Type: CONTINUOUS

      Schedule: BID

   Admin Times: 09-17

      Provider: PROVIDER, ONE \[s\]

                                                Units   Units   Inactive

Dispense Drugs                            U/D  Disp'd  Ret'd   Date

-----------------------------------------------------------------------------

ATENOLOL 100MG TAB                        1    0       0

Self Med: NO

Entry By: MCCOY, BONES                              Entry Date: 05/31/12  12:28\>

Enter RETURN to continue or '^' to exit:

### Entering a New Start Date/Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The entry prompt “NEW START DATE/TIME:” displays allowing the user to enter a new Start Date/Time. After the user enters a new Start Date/Time, a prompt displays giving the user the ability to change the calculated Stop Date/Time.

Example: Prompt Entry for New Start Date/Time

NEW START DATE/TIME: 05/16/2011@1100

### Order Entry View with New Start Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinic Order Entry view, based on Begin search date and the NEW end date, if greater than the original entered end date of the search, re-displays after the user enters “YES” to the “CHANGE ALL START DATES/TIME TO” prompt.

Example: Display Clinic Order Entry with New Start Date

Clinic Order Entry Apr 13, 2012@14:21:31 Page: 1 of 1

BCMAPATIENT,FIVE Last Ward: 3 NORTH

PID: 000-00-5555 Last Room-Bed: 1-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 09/16/60 (51) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Last Admitted: 12/05/08

Dx: FLUID IN LUNGS Discharged: 04/10/12

CLINIC ORDERS: Apr 20, 2013 to Apr 21, 2013@24:00

--------------------------------------------------------------------------------

\- - - - - - - - - - - - - - - - BECKY'S CLINIC - - - - - - - - - - - - - - - -

1 DIPHENHYDRAMINE INJ,SOLN C 04/21/2012 04/26/2012 N

Give: 10MG IM WEEKLY

2 ACETAMINOPHEN TAB R 04/20/2012 04/25/2012 N

Give: 10 MG PO Q4H

\- - - - - - - - - - - - - - - - - CLINIC (45) - - - - - - - - - - - - - - - - -

3 RANITIDINE TAB C 04/20/2012 04/23/2012 N

Give: 300 MG PO BID-AM

\- - - - - - - - - - - - - - - CLINIC PATTERN 45 - - - - - - - - - - - - - - -

4 HEPARIN 11 ML (1) ? 04/20/2012 04/21/2012 N

in 5% DEXTROSE 50 ML 100 ml/hr

----------Enter ?? for more actions---------------------------------------------

ES Edit Start Date VD View Order Detail VP View Profile

Select Action:Quit//

### New Start Date Update Confirmation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the user answers “YES” to the “Are you sure?” confirmation of the new Start Date/Time change, the prompt “NATURE OF ORDER: SERVICE CORRECTION//” displays for an ACTIVE Clinic Order, with a default of SERVICE CORRECTION.

Example: Nature of Order Prompt

NATURE OF ORDER: SERVICE CORRECTION//

The selected record(s), along with the applicable message for each order, is updated, using current business functionality.

Example: Update Message

Now working on order:

BACLOFEN 07/01/12 11:11

Give: 10 MG PO QID

NATURE OF ORDER: SERVICE CORRECTION// S

...discontinuing original order...

...creating new order.....

Pre-Exchange DOSES:

----------------------------------------------------------------------

Now working on order:

CEFAMANDOLE 05/22/12 08:00

Give: 44 GM IV

...updating order.......

...updating OE/RR...

----------------------------------------------------------------------

Now working on order:

DAPSONE 04/23/12 12:00

Give: 50 MG PO QAM

...updating order.......

...updating OE/RR...

----------------------------------------------------------------------

Now working on order:

FLUOROURACIL 05/20/12 12:00

Give: 11 MG IM

...updating order.......

...updating OE/RR...

After the user enters “QUIT” or when editing by clinic with multiple patients, the system mimics the *Non-Verified/Pending Orders* \[PSJU VBW\] option when cycling through the remaining selected patient(s).

![](inpatient-medications-nurse-s-user-manual-psj-5-423/081.png)Note: The Nature of Order prompt does not display for edits made to orders that are not active, e.g., orders with a status of non-verified.

### Conditional Messages Displaying after New Start Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Individual message prompts may or may not be presented after the new start date/time is entered for the patient. These depend on various validations that are being checked which the user may need to review or act upon. None, one, or more messages may display depending upon the entry.

#### New Start Date No Earlier than Now

A change to a new start date, earlier than “NOW” is not allowed. If the new start date entered is earlier than “NOW” the following prompt displays: “Start Date/Time earlier than NOW is not allowed. Re-enter start date. Enter new Start Date/Time:”.

#### New Start Date beyond 365 Days

A change to a new Start DATE beyond 365 days is not allowed.

Example: Message Start Date Beyond 365 Days

Start Date cannot be more than 365 days from today. Re-enter Start Date.

Enter new Start Date/Time:

![](inpatient-medications-nurse-s-user-manual-psj-5-423/082.png)Note: The system cycles back to the enter new start/date prompt entry until the new start/date time is less than 365 days.

#### Other Orders Exist

The message below displays when orders exist for the date entered at the “new Start Date/Time:” prompt. The existing active orders also display.

Example: Message Other Orders Exist

\* This patient has active order(s) on Jun 04, 2012. \*

PROCHLORPERAZINE 06/01/12 11:11

Give: 5 MG/1 ML IV WEEKLY

Do you want to view the profile?

- If the user answers “YES,” a Profile View for the selected orders for the Start Date/Time edit for the new date displays followed by the prompt to continue.

> Example: Display View Profile for Selected Order

> \<begin profile display\>

> VP view

>      \<end profile display\>  

> The following orders have been selected for Start Date/Time edit:

> \<selected orders listed\>

> The Start Date/Time for the selected orders will be changed to \<05/16/2012@11:00\>. Do you want to continue? //

- If the user answers “NO,” the “new Start Date/Time:” prompt to re-enter a new Start Date/Time displays.

#### New Start Date After One or More Stop Dates

The message below and prompt display, with no default, when the new start date is after one or more stop date(s).

Example: Display Start Date After Stop Date

\* The new start date is after one or more stop date(s). \*

The stop date(s) will be automatically changed to reflect the new start date.

Do you want to view the profile?

- If the user answers “YES,” the process continues.
- If the user answers “NO,” the “new Start Date/Time:” prompt to re-enter a new Start Date/Time displays.

> The selected changed med orders display followed by the message: “The Start Date/Time for the selected orders will now be changed to mm/dd/yy hh:mm (user entered Start Date/Time.) Are you sure?”

> Example: Prompt to Confirm Changed Start Date

> Selected Orders: Current Start Date/Time

> ------------------------------------------------------------------------------

> \< TRIHEXYPHENIDYL 04/09/12 07:53

> Give: 10MG PO SU-MO-TU-WE-TH-FR-SA

> BACLOFEN 04/19/2012 11:11

> Give: 20 MG PO Q2H \>

> ------------------------------------------------------------------------------

> The Start Date/Time for the selected orders will

> now be changed to \<6/1/12 11:00\>

> Are you sure ?

The process returns to the “Enter a new Start Date/Time:” prompt. The existing business rule for a new order is used to calculate the med order stop date from the med start date.

### Conditional Messages Displaying after Selection of Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following individual message prompts may or may not be presented after the ES selection when selecting  the clinic med order(s). These depend on various validations that are being checked which the user may need to review or act upon. None, one, or more messages may display depending upon the entry.

#### ON CALL Orders

ON CALL (OC) status can only be set for IV orders. If the user selects a Clinic IV order with an ON CALL status, the message: “Orders with ON CALL Status cannot be edited…..” displays. ES action changes to orders with ON CALL status are not allowed.

Example: Selecting ON CALL Orders

Select Action:Next Screen// es  Edit Start Date   
Select Orders:  (1-5): 2

Orders with ON CALL Status cannot be edited - no changes will be applied

to any of the following orders with ON CALL status:

ON CALL Status orders: Current Start / Stop Dates

---------------------------------------------------------------------------

\< GENTAMICIN 07/18/12 07/23/12

in INFUSE OVER 5 MINUTES\>

Press Return to continue...

#### ON HOLD Orders

If the user selects ON HOLD orders, the message: “ON HOLD orders cannot be edited….”displays. ES action changes to orders ON HOLD are not allowed.

Example: Selecting ON HOLD Orders

Select Action:Next Screen// es  Edit Start Date   
Select Orders: (1-3): 1-2

ON HOLD orders cannot be edited - no changes will be applied

to any of the following ON HOLD orders:

ON HOLD orders: Current Start / Stop Dates

---------------------------------------------------------------------------

\<ACETAMINOPHEN 07/21/12 07/26/12

Give: 10 MG PO Q4H\>

Press Return to continue...

#### Complex Orders

If the user selects complex orders, the message: “Complex Orders cannot be edited – no changes will be applied to any of the following Complex order components:…….” displays. ES action changes to complex orders are not allowed.

Example: Selecting Complex Orders

Select Action:Next Screen// es  Edit Start Date   
Select Orders:  (1-5): 2

Complex Orders cannot be edited - no changes will be applied  
  to any of the following Complex order components:  
Complex Component (Child) Orders:            Current Start Date/Time  
---------------------------------------------------------------------------  
    \<LANOLIN                                    06/01/2012  17:00  
        Give: 25 MG TOP 5XD\>  
Press Return to continue...

#### Orders for More than One Clinic

If the user selects orders for more than one clinic, the message: “You have selected orders from different clinics do you want to continue?” displays:

- If the user answers “NO,” the Clinic Order Entry profile view of order(s) for the selected patient(s) re-displays.
- If the user answers “YES,” the process continues.

#### Orders with different Start Date/Times

If the user selects orders for more than one Start Date/Time, the message: “You have selected orders with different Start Date/Time, do you want to proceed?” displays:

- If the user answers “NO,” the Clinic Order Entry profile view of order(s) for the selected patient(s) re-displays.
- If the user answers “YES,” the process continues.

#### Orders for More than one Clinic with Different Start Date/Times

If the user selects orders for more than one clinic with different Start Date/Times, the message below displays:

Example: Orders for More than One Clinic with Different Start Date/Times

You have selected orders from different clinics

and with different Start Date/Times.

Do you want to continue?

- If the user answers “NO,” the Clinic Order Entry profile view of order(s) for the selected patient(s) re-displays.
- If the user answers “YES,” the process continues.

#### System Auto Adjusts the Start Time to the Current Time

The system will auto adjust the start date/time to “NOW” for <u>pending</u> CPRS clinic orders with a start/date time in the past.

For example, when the order was created in CPRS, the current ‘NOW’ Start Time was 13:02, but when the pending order is selected in Inpatient Medications, the current ‘NOW’ Start Time is 13:12.

# Maintenance Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of these maintenance options are located on the *Unit Dose Medications* menu.

## Edit Inpatient User Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ UEUP\]

The *Edit Inpatient User Parameters* option allows users to edit various Inpatient User parameters. The prompts that will be encountered are as follows:

- “PRINT PROFILE IN ORDER ENTRY:”

> Enter YES for the opportunity to print a profile after entering Unit Dose orders for a patient.

- “INPATIENT PROFILE ORDER SORT:”

This is the sort order in which the Inpatient Profile will show inpatient orders. The options will be sorted either by medication or by start date of order. Entering the words “Medication Name” (or the number 0) will show the orders within schedule type (continuous, one-time, and then PRN) and then alphabetically by drug name. Entering the words “Start Date of Order” (or the number 1) will show the order chronologically by start date, with the most recent dates showing first and then by schedule type (continuous, one-time, and then PRN).

![](inpatient-medications-nurse-s-user-manual-psj-5-423/083.png)Note: The Profile first shows orders by status (active, non-verified, and then non-active).

- “LABEL PRINTER:”

Enter the device on which labels are to be printed.

- “USE WARD LABEL SETTINGS:”

> Enter YES to have the labels print on the printer designated for the <u>ward</u> instead of the printer designated for the <u>pharmacy</u>.

## Edit Patient’s Default Stop Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU CPDD\]

![](inpatient-medications-nurse-s-user-manual-psj-5-423/084.png) This option is locked with the PSJU PL key.

The “UD DEFAULT STOP DATE/TIME:” prompt accepts the date and time entry to be used as the default value for the STOP DATE/TIME of the Unit Dose orders during order entry and renewal processes. This value is used only if the corresponding ward parameter is enabled. The order entry and renewal processes will sometimes change this date and time.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/085.png)Note: If the Unit Dose order, being finished by the user, is received from CPRS and has a duration assigned, the UD DEFAULT STOP DATE/TIME is displayed as the Calc Stop date/time.

When the SAME STOP DATE ON ALL ORDERS parameter is set to yes, the module will assign a default stop date for each patient. This date is initially set when the first order is entered for the patient, and can change when an order for the patient is renewed. This date is shown as the default value for the stop date of each order entered for the patient. However, if a day or dose limit exists for the selected Orderable Item, and the limit is less than the default stop date, the earlier stop date and time will be displayed.

# Output Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most of the Output Options are located under the *Reports Menu* option on the *Unit DoseMedications* menu. The other reports are located directly on the *Unit Dose Medications* menu.

## PAtient Profile (Unit Dose)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU PR\]

The *PAtient Profile (Unit Dose*) \[PSJU PR\] option allows a user to print a profile (list) of a patient’s orders for the patient’s current or last (if patient has been discharged) admission, by group (G), ward (W), clinic (C), or patient (P). When group is selected, a prompt to select by ward group (W) or clinic group (C) displays. If the user’s terminal is selected as the printing device, this option will allow the user to select any of the printed orders to be shown in complete detail, including the activity logs, if any.

The *PAtient Profile (Unit Dose)* \[PSJU PR\] option also allows for viewing a list of clinic orders. Clinic orders are displayed separately from non-clinic orders.

Example: Patient Profile

Select Unit Dose Medications Option: PAtient Profile (Unit Dose)

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): P Patient \<Enter\>

Select PATIENT: PSJPATIENT1,ONE 000-00-0001 08/18/20 1 EAST

Select another PATIENT: \<Enter\>

SHORT, LONG, or NO Profile? SHORT// \<Enter\> SHORT

Show PROFILE only, EXPANDED VIEWS only, or BOTH: PROFILE// \<Enter\>

Select PRINT DEVICE: \<Enter\> NT/Cache virtual TELNET terminal

U N I T D O S E P R O F I L E 09/13/00 16:20

SAMPLE HEALTHCARE SYSTEM

\- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/00

Dx: TESTING

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_

Allergies: No Allergy Assessment

ADR:

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 -\> AMPICILLIN CAP C 09/07/2000 09/21/2000 A NF

Give: 500MG PO QID

2 -\> HYDROCORTISONE CREAM,TOP C 09/07/2000 09/21/2000 A NF

Give: 1% TOP QDAILY

3 -\> PROPRANOLOL 10MG U/D C 09/07/2000 09/21/2000 A NF

Give: PO QDAILY

View ORDERS (1-3): 1

> -----------------------------------------report continues--------------------------------

Example: Patient Profile (continued)

----------------------------------------------------------------------

Patient: PSJPATIENT1,ONE Status: ACTIVE

Orderable Item: AMPICILLIN CAP

Instructions:

Dosage Ordered: 500MG

Duration: Start: 09/07/2000 15:00

Med Route: ORAL (PO) Stop: 09/21/2000 24:00

Schedule Type: CONTINUOUS

Schedule: QID

Admin Times: 01-09-15-20

Provider: PSJPROVIDER,ONE \[w\]

Units Units Inactive

Dispense Drugs U/D Disp'd Ret'd Date

--------------------------------------------------------------------------------

AMPICILLIN 500MG CAP 1 0 0

ORDER NOT VERIFIED

Self Med: NO

Entry By: PSJPROVIDER,ONE Entry Date: 09/07/00 13:37

## Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU REPORTS\]

The *Reports Menu* option contains various reports generated by the Unit Dose package.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/086.png)Note: All of these reports are <u>QUEUABLE</u>, and it is <u>strongly suggested</u> that these reports be queued when run.

Example: Reports Menu

Select Reports Menu Option: ?

7 7 Day MAR

14 14 Day MAR

24 24 Hour MAR

AP1 Action Profile \#1

AP2 Action Profile \#2

AUthorized Absence/Discharge Summary

Extra Units Dispensed Report

Free Text Dosage Report

INpatient Stop Order Notices

Medications Due Worksheet

<span id="OTP_Med_report" class="anchor"></span>OTP Medication Dispense Report

Patient Profile (Extended)

### Hour MAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU 24H MAR\]

The *24 Hour MAR* option creates a report that can be used to track the administration of a patient’s medications over a 24-hour period. The 24 Hour MAR report includes:

- Date/time range covered by the MAR using a four-digit year format
- Institution Name
- Ward/Clinic\*
- Patient demographic data
- Time line
- Information about each order

\*For Outpatients receiving Inpatient Medication orders in an appropriate clinic.

The order information consists of:

- Order date
- Start date
- Stop date
- Schedule type (a letter code next to the administration times)
- Administration times (will be blank if an IV order does not have a schedule)
- Drug name
- Strength (if different from that indicated in drug name)
- Medication route abbreviation
- Schedule
- Verifying pharmacist’s and nurse’s initials

The MAR is printed by group (G), ward (W) , clinic (C) , or patient (P). When group is selected, a prompt to select by ward group (W) or clinic group (C) displays. If the user chooses to print by patient, the opportunity to select more than one patient will be given. The system will keep prompting, “Select another PATIENT:”. If a caret (^) is entered, the user will return to the report menu. When all patients are entered, press \<Enter\> at this prompt to continue.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/087.png)Note: If the user chooses to select by ward, administration teams may be specified and the MAR may be sorted by administration team, and then by room-bed or patient name. The default for the administration team is ALL and multiple administration teams may be entered. If selecting by ward group, the MAR may be sorted by room-bed or patient name. When the report is printed by clinic or clinic group, and the order is for an outpatient, the report leaves Room/Bed blank.

When selecting by Ward, Ward Group, Clinic, or Clinic Group, the following prompts are included. All orders for a patient are grouped together by the patient’s name, regardless of location.

#### Select by Ward:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): WARD

Include Clinic Orders?

Entering YES for Clinic Orders prints both ward and clinic orders for patients on a ward.

Entering NO for Clinic Orders prints only the ward orders.

#### Select by Ward Group:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): GROUP

Select by WARD GROUP (W) or CLINIC GROUP (C): WARD

Include Clinic Orders?

Entering YES for Clinic Orders prints both ward and clinic orders for patients in a Ward Group.

Entering NO for Clinic Orders prints only the ward orders for patients in a Ward Group.

#### Select by Clinic:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): CLINIC

Include Ward Orders?

Entering YES for Ward Orders prints both clinic and ward orders for patients in a clinic.

Entering NO for Ward Orders prints only the clinic orders.

#### Select by Clinic Group:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): GROUP

Select by WARD GROUP (W) or CLINIC GROUP (C): CLINIC

Include Ward Orders?

Entering YES for Ward Orders prints both clinic and ward orders for patients in a Clinic Group.

Entering NO for Ward Orders prints only the clinic orders for patients in a Clinic Group.

There are six medication choices. The user may select multiple choices of medications to be printed on the 24 Hour MAR. Since the first choice is ALL Medications, the user will not be allowed to combine this with any other choices. The default choice is “Non-IV Medications only” if:

1.  The MAR ORDER SELECTION DEFAULT parameter was not defined.
2.  Selection by Ward group.
3.  Selected by patients and patients are from different wards.

The MAR is separated into two sheets. The first sheet is for continuous medications and the second sheet is for one-time and PRN medications. When the 24 Hour MAR with orders is run, both sheets will print for each patient, even though the patient might only have one type of order. The user can also print blank MARs and designate which sheets to print. The user can print continuous medication sheets only, PRN sheets only, or both. The blank MARs contain patient demographics, but no order data. Order information can be added manually or with labels.

Each sheet of the 24 Hour MAR consists of three parts:

1.  The top part of each sheet contains the patient demographics.
2.  The main body of the MAR contains the order information and an area to record the medication administration.
1.  The order information prints on the left side of the main body, and is printed in the same format as on labels. Labels can be used to add new orders to this area of the MAR (Labels should <u>never</u> be placed over order information already on the MAR). Renewal dates can be recorded on the top line of each order.
2.  The right side of the main body is where the actual administration is to be recorded. It is marked in one-hour increments for simplicity.
3.  The bottom of the form allows space for signatures/titles, initials for injections, allergies, injection sites, omitted doses, reason for omitted doses, and initials for omitted doses.

At the “Enter START DATE/TIME for 24 Hour MAR:” prompt, indicate the date and the time of day, in military time, the 24 Hour MAR is to start, including leading and trailing zeros. The time that is entered into this field will print on the 24 Hour MAR as the earliest time on the time line. If the time is not entered at this prompt, the time will default to the time specified in the ward parameter, “START TIME OF DAY FOR 24 HOUR MAR:”. If the ward parameter is blank, then the time will default to 0:01 a.m. system time.

Please keep in mind that the MAR is designed to print on stock 8 ½” by 11” paper at 16 pitch (6 lines per inch).

![](inpatient-medications-nurse-s-user-manual-psj-5-423/088.png)Note: It is strongly recommended that this report be queued to print at a later time.

Example: 24 Hour MAR

Select Reports Menu Option: 24 24 Hour MAR

Select the MAR forms: 3// ?

Select one of the following:

1 Print Blank MARs only

2 Print Non-Blank MARs only

3 Print both Blank and Non-Blank MARs

Select the MAR forms: 3// \<Enter\> Print both Blank and Non-Blank MARs

Enter START DATE/TIME for 24 hour MAR: 090700@1200 (09/07/00@12:00)

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): PATIENT \<Enter\>

Select PATIENT: PSJPATIENT1,ONE 000-00-0001 08/18/20 1 EAST

Select another PATIENT: \<Enter\>

Enter medication type(s): 2,3,6// ?

1\. All medications

2\. Non-IV medications only

3\. IVPB (Includes IV syringe orders with a med route of IV or IVPB.

All other IV syringe orders are included with non-IV medications).

4\. LVPs

5\. TPNs

6\. Chemotherapy medications (IV)

A combination of choices can be entered here except for option 1.

e.g. Enter 1 or 2-4,5 or 2.

Enter medication type(s): 2,3,6// 1

Select PRINT DEVICE: 0;132 NT/Cache virtual TELNET terminal

> -----------------------------------------report continues--------------------------------

Example: 24 Hour MAR (continued)

CONTINUOUS SHEET 24 HOUR MAR 09/07/2000 12:00 through 09/08/00 11:59

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/00 16:15

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Ward: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Admin

Order Start Stop Times 12 13 14 15 16 17 18 19 20 21 22 23 24 01 02 03 04 05 06 07 08 09 10 11

---------------------------------------------------------------------------------------------------------------

\| \|

---------------------------------------------------------------------------------------------------------

\| \|

---------------------------------------------------------------------------------------------------------

\| \|

---------------------------------------------------------------------------------------------------------

\| \|

---------------------------------------------------------------------------------------------------------

\| \|

---------------------------------------------------------------------------------------------------------

\| \|

---------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| ALLERGIES \| INJECTION SITES \| MED/DOSE OMITTED \| REASON \| INIT \|

\|--------------------------\|------\|--------------\|-------------------\|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\| Indicate RIGHT (R)\|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\| or LEFT (L) \|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\| 1. DELTOID \|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\| 2. ABDOMEN \|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\| 3. ILIAC CREST \|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\| 4. GLUTEAL \|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\| 5. THIGH \|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\|PRN:E=Effective \|--------------------\|------------\|------\|

\|--------------------------\|------\|--------------\| N=Not Effective\|--------------------\|------------\|------\|

---------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 VA FORM 10-2970

> -----------------------------------------report continues-------------------------------

Example: 24 Hour MAR (continued)

ONE-TIME/PRN SHEET 24 HOUR MAR 09/07/2000 12:00 through 09/08/00 11:59

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/00 16:15

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Ward: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Admin

Order Start Stop Times 12 13 14 15 16 17 18 19 20 21 22 23 24 01 02 03 04 05 06 07 08 09 10 11

---------------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

---------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| ALLERGIES \| INJECTION SITES \| MED/DOSE OMITTED \| REASON \| INIT \|

\|-------------------------\|------\|--------------\|--------------------\|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\| Indicate RIGHT (R) \|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\| or LEFT (L) \|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\| 1. DELTOID \|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\| 2. ABDOMEN \|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\| 3. ILIAC CREST \|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\| 4. GLUTEAL \|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\| 5. THIGH \|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\|PRN: E=Effective \|--------------------\|------------\|------\|

\|-------------------------\|------\|--------------\| N=Not Effective\|--------------------\|------------\|------\|

---------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 VA FORM 10-5568d

> -----------------------------------------report continues--------------------------------

Example: 24 Hour MAR (continued)

CONTINUOUS SHEET 24 HOUR MAR 09/07/2000 12:00 through 09/08/00 11:59

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/00 16:15

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Ward: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Admin

Order Start Stop Times 12 13 14 15 16 17 18 19 20 21 22 23 24 01 02 03 04 05 06 07 08 09 10 11

--------------------------------------------------------------------------------------------------------------------------

\| \| \|01 \|

09/07 \|09/07 15:00\|09/21/00 24:00(A9111) \|09 \|

AMPICILLIN CAP C\|15 \| 15 20 01 09

Give: 500MG PO QID \|20 \|

\| \|

RPH: PI RN: \_\_\_\_\_\| \|

---------------------------------------------------------------------------------------------------------------------

\| \| \|01 \|

09/07 \|09/07 15:00 \|09/14/00 16:54(A9111) \|09 \|

AMPICILLIN 1 GM C\|15 \| 15 20 01 09

in 0.9% NACL 100 ML \|20 \|

IVPB QID \| \|

See next label for continuation \| \|

---------------------------------------------------------------------------------------------------------------------

THIS IS AN INPATIENT IV EXAMPLE \| \|

\| \|

\| \|

\| \|

\| \|

RPH: PI RN: \_\_\_\_\_ \| \|

---------------------------------------------------------------------------------------------------------------------

\| \| \| \|

09/07 \|09/07 17:00 \|09/07/00 12:00(A9111) \| \|

HYDROCORTISONE CREAM,TOP C\|17 \|

Give: 1% TOP QDAILY \| \|

\| \|

RPH: PI RN: \_\_\_\_\_\| \|

---------------------------------------------------------------------------------------------------------------------

\| \| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

09/07 \|09/07 17:00 \|09/07/00 12:50 (A9111) \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

METHYLPREDNISOLNE INJ C\|09 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

Give: 500MG IV Q12H \|21 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

THIS IS AN INPATIENT IV EXAMPLE \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: MLV RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------------------------------------------

\| \| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

09/07 \|09/07 17:00 \|09/07/00 12:50 (A9111) \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

METHYLPREDNISOLNE INJ C\|17 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

Give: 1000MG IV QDAILY \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

THIS IS AN INPATIENT IV EXAMPLE \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: MLV RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

----------------------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| ALLERGIES \| INJECTION SITES \| MED/DOSE OMITTED \| REASON \| INIT \|

\|------------------------------\|------\|--------------\|--------------------\|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\| Indicate RIGHT (R) \|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\| or LEFT (L) \|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\| 1. DELTOID \|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\| 2. ABDOMEN \|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\| 3. ILIAC CREST \|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\| 4. GLUTEAL \|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\| 5. THIGH \|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\|PRN: E=Effective \|------------------------\|----------------\|------\|

\|------------------------------\|------\|--------------\| N=Not Effective\|------------------------\|----------------\|------\|

----------------------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 PAGE: 1 VA FORM 10-2970

> -----------------------------------------report continues--------------------------------

Example: 24 Hour MAR (continued)

ONE-TIME/PRN SHEET 24 HOUR MAR 09/07/2000 12:00 through 09/08/00 11:59

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/00 16:15

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Ward: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Admin

Order Start Stop Times 12 13 14 15 16 17 18 19 20 21 22 23 24 01 02 03 04 05 06 07 08 09 10 11

---------------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

--------------------------------------------------------------------------------------------------------

\| \|

---------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| ALLERGIES \| INJECTION SITES \| MED/DOSE OMITTED \| REASON \| INIT \|

\|--------------------------\|------\|-------------\|--------------------\|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\| Indicate RIGHT (R) \|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\| or LEFT (L) \|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\| 1. DELTOID \|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\| 2. ABDOMEN \|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\| 3. ILIAC CREST \|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\| 4. GLUTEAL \|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\| 5. THIGH \|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\|PRN: E=Effective \|--------------------\|------------\|------\|

\|--------------------------\|------\|-------------\| N=Not Effective\|--------------------\|------------\|------\|

---------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 LAST PAGE: 2 VA FORM 10-5568d

### Day MAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU 7D MAR\]

The *7 Day MAR* option creates a report form that can be used to track the administration of patients’ medications.

The 7 Day MAR report includes:

- Date/time range covered by the MAR using a four-digit year format
- Institution Name
- Ward/Clinic\*
- Patient demographic data
- Time line
- Information about each order

\*For Outpatients receiving Inpatient Medication orders in an appropriate clinic.

The order information consists of:

- Order date
- Start date
- Stop date
- Schedule type (a letter code next to the administration times)
- Administration times (will be blank if an IV order does not have a schedule)
- Drug name
- Strength (if different from that indicated in drug name)
- Medication route abbreviation
- Schedule
- Verifying pharmacist’s and nurse’s initials

The MAR is printed by group (G), ward (W), clinic (C) , or patient (P). When group is selected, a prompt to select by ward group (W) or clinic group (C) displays. If the user chooses to print by patient, the opportunity to select more than one patient will be given. The system will keep prompting, “Select another PATIENT:”. If a caret (^) is entered, the user will return to the report menu. When all patients are entered, press \<Enter\> at this prompt to continue.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/089.png)Note: If the user chooses to select by ward, administration teams may be specified and the MAR may be sorted by administration team, and then by room-bed or patient name. The default for the administration team is ALL and multiple administration teams may be entered. If selecting by ward group, the MAR may be sorted by room-bed or patient name. When the report is printed by clinic or clinic group, and the order is for an outpatient, the report leaves Room/Bed blank.

When selecting by Ward, Ward Group, Clinic, or Clinic Group, the following prompts are included. All orders for a patient are grouped together by the patient’s name, regardless of location.

#### Select by Ward:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): WARD

Include Clinic Orders?

Entering YES for Clinic Orders prints both ward and clinic orders for patients on a ward.

Entering NO for Clinic Orders prints only the ward orders.

#### Select by Ward Group:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): GROUP

Select by WARD GROUP (W) or CLINIC GROUP (C): WARD

Include Clinic Orders?

Entering YES for Clinic Orders prints both ward and clinic orders for patients in a Ward Group.

Entering NO for Clinic Orders prints only the ward orders for patients in a Ward Group.

#### Select by Clinic:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): CLINIC

Include Ward Orders?

Entering YES for Ward Orders prints both clinic and ward orders for patients in a clinic.

Entering NO for Ward Orders prints only the clinic orders.

#### Select by Clinic Group:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): GROUP

Select by WARD GROUP (W) or CLINIC GROUP (C): CLINIC

Include Ward Orders?

Entering YES for Ward Orders prints both clinic and ward orders for patients in a Clinic Group.

Entering NO for Ward Orders prints only the clinic orders for patients in a Clinic Group.

There are six medication choices. The user may select multiple choices of medications to be printed on the 7 Day MAR. Since the first choice is ALL Medications, the user will not be allowed to combine this with any other choices. The default choice is “Non-IV Medications only” if:

1.  The MAR ORDER SELECTION DEFAULT parameter was not defined.
2.  Selection by Ward group.
3.  Selected by patients and patients are from different wards.

The *7 Day MAR* option also allows the nurse to choose whether to print one of the two sheets, continuous, PRN, or both. The MAR is separated into two sheets. The first sheet is for continuous medications and the second sheet is for one-time and PRN medications. When the 7 Day MAR with orders is run, both sheets will print for each patient, even though the patient might only have one type of order. The user can also print blank MARs and designate which sheets to print. The user can print continuous medication sheets only, PRN sheets only, or both. The blank MARs contain patient demographics, but no order data. Order information can be added manually or with labels.

Each sheet of the 7 Day MAR consists of three parts:

1.  The top part of each sheet contains the patient demographics.
2.  The main body of the MAR contains the order information and an area to record the medication administration.
1.  The order information prints on the left side of the main body, printed in the same format as on labels. Labels can be used to add new orders to this area of the MAR (Labels should <u>never</u> be placed over order information already on the MAR). Renewal dates can be recorded on the top line of each order.
2.  The right side of the main body is where the actual administration is to be recorded. On the continuous medication sheet, the right side will be divided into seven columns, one for each day of the range of the MAR. Asterisks will print at the bottom of the columns corresponding to the days on which the medication is not to be given (e.g., Orders with a schedule of Q3D would only be given every three days, so asterisks would appear on days the medication should not be given).
3.  The bottom of the form is designed to duplicate the bottom of the current CMR (VA FORM 10-2970), the back of the current PRN and ONE TIME MED RECORD CMR (VA FORM 10-5568d). The MAR is provided to record other information about the patient and his or her medication(s). It is similar to the bottom of the 24 Hour MAR, but lists more injection sites and does not allow space to list allergies.

For IV orders that have no schedule, \*\*\*\*\*\*\* will print on the bottom of the column corresponding to the day the order is to expire. On the continuous medication sheet only, there might be additional information about each order under the column marked notes. On the first line, SM will print if the order has been marked as a self-med order. The letters HSM will print if the order is marked as a hospital supplied self-med. On the second line, WS will print if the order is found to be a ward stock item, CS will print if the item is a Controlled Substance and/or NF will print if the order is a non-formulary. If the order is printed in more than one block, the RPH and RN initial line will print on the last block.

The answer to the prompt, “Enter START DATE/TIME for 7 Day MAR:” determines the date range covered by the 7 Day MAR. The stop date is automatically calculated. Entry of <u>time</u> is not required, but if a time is entered with the date, only those orders that expire after the date and time selected will print. If no time is entered, all orders that expire on or after the date selected will print.

Please keep in mind that the MAR is designed to print on stock 8 ½” by 11” paper at 16 pitch (6 lines per inch).

![](inpatient-medications-nurse-s-user-manual-psj-5-423/090.png)Note: It is strongly recommended that this report be queued to print at a later time.

Example: 7 Day MAR

Select Reports Menu Option: 7 7 Day MAR

Select the MAR forms: 3// \<Enter\> Print both Blank and Non-Blank MARs

Select TYPE OF SHEETS TO PRINT: BOTH// \<Enter\>

Enter START DATE/TIME for 7 day MAR: 090700@1200 (09/07/00@12:00:00)

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): PATIENT \<Enter\>

Select PATIENT: PSJPATIENT1,ONE 000-00-0001 08/18/20 1 EAST

Select another PATIENT: \<Enter\>

Enter medication type(s): 2,3,6// 1

Select PRINT DEVICE: 0;132 NT/Cache virtual TELNET terminal

CONTINUOUS SHEET 7 DAY MAR 09/07/00 through 09/13/00

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/2000 16:14

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Loc: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Admin

Order Start Stop Times 09/07 09/08 09/09 09/10 09/11 09/12 09/13 notes

---------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

---------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

---------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

---------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

---------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

---------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| INJECTION SITES \| MED/DOSE OMITTED \| REASON \| INIT \|

\|-------------------------\|------\|-----------------------------------\|--------------------\|------------\|------\|

\|-------------------------\|------\| Indicate RIGHT (R) or LEFT (L) \|--------------------\|------------\|------\|

\|-------------------------\|------\| \|--------------------\|------------\|------\|

\|-------------------------\|------\| (IM) (SUB Q) \|--------------------\|------------\|------\|

\|-------------------------\|------\|1.DELTOID 6. UPPER ARM \|--------------------\|------------\|------\|

\|-------------------------\|------\|2.VENTRAL GLUTEAL 7. ABDOMEN \|--------------------\|------------\|------\|

\|-------------------------\|------\|3.GLUTEUS MEDIUS 8. THIGH \|--------------------\|------------\|------\|

\|-------------------------\|------\|4.MID(ANTERIOR) THIGH 9. BUTTOCK \|--------------------\|------------\|------\|

\|-------------------------\|------\|5.VASTUS LATERALIS 10. UPPER BACK\|--------------------\|------------\|------\|

\|-------------------------\|------\|PRN: E=Effective N=Not Effective \|--------------------\|------------\|------\|

---------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 VA FORM 10-2970

> -----------------------------------------report continues--------------------------------

Example: 7 Day MAR (continued)

ONE-TIME/PRN SHEET 7 DAY MAR 09/07/00 through 09/13/00

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/00 16:14

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Loc: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Order Start Stop Order Start Stop

---------------------------------------------------------------------------------------------------------------

\| \| \| \| \| \|

\| \|

\| \|

\| \|

\| \|

\| \|

---------------------------------------------------------------------------------------------------------------

\| \| \| \| \| \|

\| \|

\| \|

\| \|

\| \|

\| \|

---------------------------------------------------------------------------------------------------------------

\| DATE \| TIME \| MEDICATION/DOSE/ROUTE \| INIT \| REASON \| RESULTS \| TIME \| INIT \|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

\|--------\|--------\|----------------------------\|------\|-------------------\|-------------------\|--------\|------\|

---------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| INJECTION SITES \| SIGNATURE/TITLE \| INIT \|

\|---------------------------\|------\|------------------------------------\|------------------------------\|------\|

\|---------------------------\|------\| Indicate RIGHT (R) or LEFT (L) \|------------------------------\|------\|

\|---------------------------\|------\| \|------------------------------\|------\|

\|---------------------------\|------\| (IM) (SUB Q) \|------------------------------\|------\|

\|---------------------------\|------\|1. DELTOID 6. UPPER ARM \|------------------------------\|------\|

\|---------------------------\|------\|2. VENTRAL GLUTEAL 7. ABDOMEN \|------------------------------\|------\|

\|---------------------------\|------\|3. GLUTEUS MEDIUS 8. THIGH \|------------------------------\|------\|

\|---------------------------\|------\|4. MID(ANTERIOR) THIGH 9. BUTTOCK \|------------------------------\|------\|

\|---------------------------\|------\|5. VASTUS LATERALIS 10. UPPER BACK\|------------------------------\|------\|

\|---------------------------\|------\| PRN: E=Effective N=Not Effective \|------------------------------\|------\|

---------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 VA FORM 10-5568d

> -----------------------------------------report continues--------------------------------

Example: 7 Day MAR (continued)

CONTINUOUS SHEET 7 DAY MAR 09/07/00 through 09/13/00

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/2000 16:14

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Loc: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Admin

Order Start Stop Times 09/07 09/08 09/09 09/10 09/11 09/12 09/13 notes

----------------------------------------------------------------------------------------------------------------------------------

\| \| \|01 \|\*\*\*\*\*\*\*\*\*\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|

09/07 \|09/07 15:00 \|09/21/00 24:00(A9111) \|09 \|\*\*\*\*\*\*\*\*\*\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|

AMPICILLIN CAP C\|15 \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|

Give: 500MG PO QID \|20 \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|

\| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|

RPH: PI RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \|

----------------------------------------------------------------------------------------------------------------------------

\| \| \|01 \|\*\*\*\*\*\*\*\*\*\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

09/07 \|09/07 15:00 \|09/14/00 16:54(A9111) \|09 \|\*\*\*\*\*\*\*\*\*\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

AMPICILLIN 1 GM C\|15 \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

in 0.9% NACL 100 ML \|20 \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

IVPB QID \| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

See next label for continuation \| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

THIS IS AN INPATIENT IV EXAMPLE \| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

RPH: PI RN: \_\_\_\_\_ \| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

\| \| \| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

09/07 \|09/07 17:00 \|09/07/00 12:34(A9111) \| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

HYDROCORTISONE CREAM,TOP C\|17 \|\*\*\*\*\*\*\*\*\*\|\*\*\*\*\*\*\*\*\*\|\*\*\*\*\*\*\*\*\*\|\*\*\*\*\*\*\*\*\*\|\*\*\*\*\*\*\*\*\*\|\*\*\*\*\*\*\*\*\*\|\*\*\*\*\*\*\*\*\|

Give: 1% 0 QDAILY \| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

\| \|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|

RPH: MLV RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

\| \| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

09/07 \|09/07 17:00 \|09/07/00 12:50 (A9111) \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

METHYLPREDNISOLNE INJ C\|09 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

Give: 500MG IV Q12H \|21 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

THIS IS AN INPATIENT IV EXAMPLE \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: MLV RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

\| \| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

09/07 \|09/07 17:00 \|09/07/00 12:50 (A9111) \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

METHYLPREDNISOLNE INJ C\|17 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

Give: 1000MG IV QDAILY \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

THIS IS AN INPATIENT IV EXAMPLE \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: MLV RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

----------------------------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| INJECTION SITES \| MED/DOSE OMITTED \| REASON \| INIT \|

\|------------------------------\|--------\|------------------------------------\|------------------------\|----------------\|---------\|

\|------------------------------\|--------\| Indicate RIGHT (R) or LEFT (L) \|------------------------\|----------------\|---------\|

\|------------------------------\|--------\| \|------------------------\|----------------\|---------\|

\|------------------------------\|--------\| (IM) (SUB Q) \|------------------------\|----------------\|---------\|

\|------------------------------\|--------\|1. DELTOID 6. UPPER ARM \|------------------------\|----------------\|---------\|

\|------------------------------\|--------\|2. VENTRAL GLUTEAL 7. ABDOMEN \|------------------------\|----------------\|---------\|

\|------------------------------\|--------\|3. GLUTEUS MEDIUS 8. THIGH \|------------------------\|----------------\|---------\|

\|------------------------------\|--------\|4. MID(ANTERIOR) THIGH 9. BUTTOCK \|------------------------\|----------------\|---------\|

\|------------------------------\|--------\|5. VASTUS LATERALIS 10. UPPER BACK\|------------------------\|----------------\|---------\|

\|------------------------------\|--------\| PRN: E=Effective N=Not Effective \|------------------------\|----------------\|---------\|

----------------------------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 LAST PAGE: 1 VA FORM 10-2970

### Day MAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU 14D MAR\]

The *14 Day MAR* option creates a report form that can be used to track the administration of patients’ medications.

- Date/time range covered by the MAR using a four-digit year format
- Institution Name
- Ward/Clinic\*
- Patient demographic data
- Time line
- Information about each order

\*For Outpatients receiving Inpatient Medication orders in an appropriate clinic.

The order information consists of:

- Order date
- Start date
- Stop date
- Schedule type (a letter code next to the administration times)
- Administration times (will be blank if an IV order does not have a schedule)
- Drug name
- Strength (if different from that indicated in drug name)
- Medication route abbreviation
- Schedule
- Verifying pharmacist’s and nurse’s initials

The MAR is printed by group (G), ward (W), clinic (C) , or patient (P). When group is selected, a prompt to select by ward group (W) or clinic group (C) displays. If the user chooses to print by patient, the opportunity to select more than one patient will be given. The system will keep prompting, “Select another PATIENT:”. If a caret (^) is entered, the user will return to the report menu. When all patients are entered, press \<Enter\> at this prompt to continue.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/091.png)Note: If the user chooses to select by ward, administration teams may be specified and the MAR may be sorted by administration team, and then by room-bed or patient name. The default for the administration team is ALL and multiple administration teams may be entered. If selecting by ward group, the MAR may be sorted by room-bed or patient name. When the report is printed by clinic or clinic group, and the order is for an outpatient, the report leaves Room/Bed blank.

When selecting by Ward, Ward Group, Clinic, or Clinic Group, the following prompts are included. All orders for a patient are grouped together by the patient’s name, regardless of location.

#### Select by Ward:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): WARD

Include Clinic Orders?

Entering YES for Clinic Orders prints both ward and clinic orders for patients on a ward.

Entering NO for Clinic Orders prints only the ward orders.

#### Select by Ward Group:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): GROUP

Select by WARD GROUP (W) or CLINIC GROUP (C): WARD

Include Clinic Orders?

Entering YES for Clinic Orders prints both ward and clinic orders for patients in a Ward Group.

Entering NO for Clinic Orders prints only the ward orders for patients in a Ward Group.

#### Select by Clinic:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): CLINIC

Include Ward Orders?

Entering YES for Ward Orders prints both clinic and ward orders for patients in a clinic.

Entering NO for Ward Orders prints only the clinic orders.

#### Select by Clinic Group:

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): GROUP

Select by WARD GROUP (W) or CLINIC GROUP (C): CLINIC

Include Ward Orders?

Entering YES for Ward Orders prints both clinic and ward orders for patients in a Clinic Group.

Entering NO for Ward Orders prints only the clinic orders for patients in a Clinic Group.

There are six medication choices. The user may select multiple choices of medications to be printed on the 14 Day MAR. Since the first choice is ALL Medications, the user will not be allowed to combine this with any other choices. The default choice is “Non-IV Medications only” if:

1.  The MAR ORDER SELECTION DEFAULT parameter was not defined.
2.  Selection by Ward group.
3.  Selected by patients and patients are from different wards.

The *14 Day MAR* option allows the nurse to choose whether to print continuous, PRN, or both. The MAR is separated into two sheets. The first sheet is for continuous medications and the second sheet is for one-time and PRN medications. When the 14 Day MAR with orders is run, both sheets will print for each patient, even though the patient might only have one type of order.

The user can also print blank MARs and designate which sheets to print. The user can print continuous medication sheets only, PRN sheets only, or both. The blank MARs contain patient demographics, but no order data. Order information can be added manually or with labels.

Each sheet of the MAR consists of three parts:

1.  The top part of each sheet contains the patient demographics.
2.  The main body of the MAR contains the order information and an area to record the medication administration.
1.  The order information prints on the left side of the main body, printed in the same format as on labels. Labels can be used to add new orders to this area of the MAR (Labels should <u>never</u> be placed over order information already on the MAR). Renewal dates can be recorded on the top line of each order.
2.  The right side of the main body is where the actual administration is to be recorded. On the continuous medication sheet, the right side will be divided into 14 columns, one for each day of the range of the MAR. Asterisks will print at the bottom of the columns corresponding to the days on which the medication is not to be given (e.g., Orders with a schedule of Q3D would only be given every three days, so asterisks would appear on two days out of three).
3.  The bottom of the MAR is provided to record other information about the patient and his or her medication(s). It is similar to the bottom of the 24-hour MAR, but lists more injection sites.

For IV orders that have no schedule, \*\*\*\* will print on the bottom of the column corresponding to the day the order is to expire. On the continuous medication sheet only, there might be additional information about each order under the column marked notes. On the first line, SM will print if the order has been marked as a self-med order. The letters HSM will print if the order is marked as a hospital supplied self-med. On the second line, WS will print if the order is found to be a ward stock item, CS will print if the item is a Controlled Substance and/or NF will print if the order is a non-formulary. If the order is printed in more than one block, the RPH and RN initial line will print on the last block.

The answer to the prompt, “Enter START DATE/TIME for 14 Day MAR:” determines the date range covered by the 14 Day MAR. The stop date is automatically calculated. Entry of time is not required, but if a time is entered with the date, only those orders that expire after the date and time selected will print. If no time is entered, all orders that will expire on or after the date selected will print.

Please keep in mind that the MAR is designed to print on stock 8 ½” by 11” paper at 16 pitch (6 lines per inch).

![](inpatient-medications-nurse-s-user-manual-psj-5-423/092.png)Note: It is strongly recommended that this report be queued to print at a later time.

Example: 14 Day MAR

Select Reports Menu Option: 14 Day MAR

Select the MAR forms: 3// \<Enter\> Print both Blank and Non-Blank MARs

Select TYPE OF SHEETS TO PRINT: BOTH// \<Enter\>

Enter START DATE/TIME for 14 day MAR: 090700@1200 (SEP 07, 2000@12:00:00)

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): PATIENT \<Enter\>

Select PATIENT: PSJPATIENT1,ONE 000-00-0001 08/18/20 1 EAST

Select another PATIENT: \<Enter\>

Enter medication type(s): 2,3,6// 1

Select PRINT DEVICE: 0;132 NT/Cache virtual TELNET terminal

> -----------------------------------------report continues--------------------------------

Example: 14 Day MAR Report (continued)

CONTINUOUS SHEET 14 DAY MAR 09/07/2000 through 09/20/2000

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/2000 16:11

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Loc: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Admin SEP

Order Start Stop Times 07 08 09 10 11 12 13 14 15 16 17 18 19 20 notes

----------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

----------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

----------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

----------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

----------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

----------------------------------------------------------------------------------------------------------------

\| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

----------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| INJECTION SITES \| MED/DOSE OMITTED \| REASON \| INIT \|

\|-------------------------\|------\|------------------------------------\|--------------------\|------------\|------\|

\|-------------------------\|------\| Indicate RIGHT (R) or LEFT (L) \|--------------------\|------------\|------\|

\|-------------------------\|------\| \|--------------------\|------------\|------\|

\|-------------------------\|------\| (IM) (SUB Q) \|--------------------\|------------\|------\|

\|-------------------------\|------\|1. DELTOID 6. UPPER ARM \|--------------------\|------------\|------\|

\|-------------------------\|------\|2. VENTRAL GLUTEAL 7. ABDOMEN \|--------------------\|------------\|------\|

\|-------------------------\|------\|3. GLUTEUS MEDIUS 8. THIGH \|--------------------\|------------\|------\|

\|-------------------------\|------\|4. MID(ANTERIOR) THIGH 9. BUTTOCK \|--------------------\|------------\|------\|

\|-------------------------\|------\|5. VASTUS LATERALIS 10. UPPER BACK\|--------------------\|------------\|------\|

\|-------------------------\|------\| PRN: E=Effective N=Not Effective \|--------------------\|------------\|------\|

----------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 VA FORM 10-2970

> -----------------------------------------report continues--------------------------------

Example: 14 Day MAR (continued)

ONE-TIME/PRN SHEET 14 DAY MAR 09/07/2000 through 09/20/2000

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/2000 16:11

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Ward: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Order Start Stop Order Start Stop

---------------------------------------------------------------------------------------------------------------

\| \| \| \| \| \|

\| \|

\| \|

\| \|

\| \|

---------------------------------------------------------------------------------------------------------------

\| \| \| \| \| \|

\| \|

\| \|

\| \|

\| \|

---------------------------------------------------------------------------------------------------------------

\| DATE \| TIME \| MEDICATION/DOSE/ROUTE \| INIT \| REASON \| RESULTS \| TIME \| INIT \|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

\|--------\|--------\|-------------------------------\|------\|------------------\|-----------------\|--------\|------\|

---------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| INJECTION SITES \| SIGNATURE/TITLE \| INIT \|

\|----------------------------\|------\|------------------------------------\|-----------------------------\|------\|

\|----------------------------\|------\| Indicate RIGHT (R) or LEFT (L) \|-----------------------------\|------\|

\|----------------------------\|------\| \|-----------------------------\|------\|

\|----------------------------\|------\| (IM) (SUB Q) \|-----------------------------\|------\|

\|----------------------------\|------\|1. DELTOID 6. UPPER ARM \|-----------------------------\|------\|

\|----------------------------\|------\|2. VENTRAL GLUTEAL 7. ABDOMEN \|-----------------------------\|------\|

\|----------------------------\|------\|3. GLUTEUS MEDIUS 8. THIGH \|-----------------------------\|------\|

\|----------------------------\|------\|4. MID(ANTERIOR) THIGH 9. BUTTOCK \|-----------------------------\|------\|

\|----------------------------\|------\|5. VASTUS LATERALIS 10. UPPER BACK\|-----------------------------\|------\|

\|----------------------------\|------\| PRN: E=Effective N=Not Effective \|-----------------------------\|------\|

---------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 VA FORM 10-5568d

> -----------------------------------------report continues--------------------------------

Example: 14 Day MAR (continued)

CONTINUOUS SHEET 14 DAY MAR 09/07/2000 through 09/20/2000

SAMPLE HEALTHCARE SYSTEM Printed on 09/20/2000 16:11

Name: PSJPATIENT1,ONE Weight (kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Ward: 1 EAST

PID: 000-00-0001 DOB: 08/18/1920 (80) Height (cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_) Room-Bed: B-12

Sex: MALE Dx: TESTING Admitted: 05/03/2000 13:29

Allergies: No Allergy Assessment ADR:

Admin SEP

Order Start Stop Times 07 08 09 10 11 12 13 14 15 16 17 18 19 20 notes

----------------------------------------------------------------------------------------------------------------------------------

\| \| \|01 \|\*\*\*\*\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

09/07 \|09/07 15:00 \|09/21/00 24:00 (A9111) \|09 \|\*\*\*\*\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

AMPICILLIN CAP C\|15 \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

Give: 500MG PO QID \|20 \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: PI RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

\| \| \|01 \|\*\*\*\*\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

09/07 \|09/07 15:00 \|09/14/00 16:54 (A9111) \|09 \|\*\*\*\*\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

AMPICILLIN 1 GM C\|15 \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

in 0.9% NACL 100 ML \|20 \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

IVPB QID \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

See next label for continuation \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

THIS IS AN INPATIENT IV EXAMPLE \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: PI RN: \_\_\_\_\_ \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

\| \| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

09/07 \|09/07 17:00 \|09/07/00 12:34 (A9111) \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

HYDROCORTISONE CREAM,TOP C\|17 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

Give: 1% 0 QDAILY \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

\| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: MLV RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

\| \| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

09/07 \|09/07 17:00 \|09/07/00 12:50 (A9111) \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

METHYLPREDNISOLNE INJ C\|09 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

Give: 500MG IV Q12H \|21 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

THIS IS AN INPATIENT IV EXAMPLE \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: MLV RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

---------------------------------------------------------------------------------------------------------------------------

\| \| \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

09/07 \|09/07 17:00 \|09/07/00 12:50 (A9111) \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

METHYLPREDNISOLNE INJ C\|17 \|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|\*\*\*\*\|

Give: 1000MG IV QDAILY \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

THIS IS AN INPATIENT IV EXAMPLE \| \|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|\_\_\_\_\|

RPH: MLV RN: \_\_\_\_\_\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|

----------------------------------------------------------------------------------------------------------------------------------

\| SIGNATURE/TITLE \| INIT \| INJECTION SITES \| MED/DOSE OMITTED \| REASON \| INIT \|

\|---------------------------------\|------\|------------------------------------\|------------------------\|----------------\|--------\|

\|---------------------------------\|------\| Indicate RIGHT (R) or LEFT (L) \|------------------------\|----------------\|--------\|

\|---------------------------------\|------\| \|------------------------\|----------------\|--------\|

\|---------------------------------\|------\| (IM) (SUB Q) \|------------------------\|----------------\|--------\|

\|---------------------------------\|------\|1. DELTOID 6. UPPER ARM \|------------------------\|----------------\|--------\|

\|---------------------------------\|------\|2. VENTRAL GLUTEAL 7. ABDOMEN \|------------------------\|----------------\|--------\|

\|---------------------------------\|------\|3. GLUTEUS MEDIUS 8. THIGH \|------------------------\|----------------\|--------\|

\|---------------------------------\|------\|4. MID(ANTERIOR) THIGH 9. BUTTOCK \|------------------------\|----------------\|--------\|

\|---------------------------------\|------\|5. VASTUS LATERALIS 10. UPPER BACK\|------------------------\|----------------\|--------\|

\|---------------------------------\|------\| PRN: E=Effective N=Not Effective \|------------------------\|----------------\|--------\|

----------------------------------------------------------------------------------------------------------------------------------

PSJPATIENT1,ONE 000-00-0001 Room-Bed: B-12 LAST PAGE: 1 VA FORM 10-2970

### Action Profile \#1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU AP-1\]

The *Action Profile \#1* \[PSJU AP-1\]option creates a report form that contains all of the active inpatient medication orders for one or more patients. These patients may be selected by ward group (G), ward (W) , or patient (P). If selection by ward is chosen, the administration teams may be specified. The default for the administration team is ALL and multiple administration teams may be entered. If selecting by ward or ward group, the profile may be sorted by patient name or room-bed. Entering a Ward Group of ^OTHER will automatically sort by patient and print a report for Outpatients that are receiving Inpatient Medications and that meet the report parameters. If the user chooses to run this option by patient, the opportunity is given to select as many patients as needed, but only those that have <u>active</u> orders will print.

The *Action Profile \#1* \[PSJU AP-1\] option also allows for viewing a list of clinic orders. Clinic orders are displayed separately from non-clinic orders.

Start and stop dates will be prompted next. If the user chooses to enter a start and stop date, only patients with active orders occurring between those dates will print. The start and stop dates must be in the future (NOW is acceptable). Time is required only if the current date of TODAY or T is entered.

There are six medication choices. The user may select multiple choices of medications to be printed on the Action Profile \#1 report. Since the first choice is ALL Medications, the user will not be allowed to combine this with any other choices. The default choice is “Non-IV Medications only” if:

1.  The MAR ORDER SELECTION DEFAULT parameter was not defined.
2.  Selection by Ward group.
3.  Selected by patients and patients are from different wards.

The form is printed so the attending provider will have a method of periodically reviewing these active medication orders. If the user chooses to run this option by patient, the opportunity is given to select as many patients as needed, but only those that have <u>active</u> orders will print.

Also on this profile, the provider can renew, discontinue, or not take any action regarding the active orders for each patient. A new order will be required for any new medication prescribed or for any changes in the dosage or directions of an existing order. If no action is taken, a new order is not required.

If the user chooses to enter a start and stop date, only patients with active orders occurring between those dates will print (for the ward or wards chosen). The start and stop dates must be in the future (NOW is acceptable). Time is required only if the current date of TODAY or T is entered.

It is recommended that the action profiles be printed on two-part paper, if possible. Using two-part paper allows a copy to stay on the ward and the other copy to be sent to the pharmacy.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/093.png)Note: This report uses a four-digit year format.

Example: Action Profile \#1

Select Reports Menu Option: AP1 Action Profile \#1

Select by WARD GROUP (G), WARD (W), or PATIENT (P): Patient \<Enter\>

Select PATIENT: PSJPATIENT1,ONE 000-00-0001 08/18/20 1 EAST

Select another PATIENT: \<Enter\>

Enter medication type(s): 2,3,6// 1

...this may take a few minutes...(you should QUEUE this report)...

Select PRINT DEVICE: \<Enter\> NT/Cache virtual TELNET terminal

Enter RETURN to continue or '^' to exit: \<Enter\>

UNIT DOSE ACTION PROFILE \#1 09/11/2000 11:01

SAMPLE HEALTHCARE SYSTEM

(Continuation of VA FORM 10-1158) Page: 1

--------------------------------------------------------------------------------

This form is to be used to REVIEW/RENEW/CANCEL existing active medication

orders for inpatients. Review the active orders listed and beside each order

circle one of the following:

R - to RENEW the order

D - to DISCONTINUE the order

N - to take NO ACTION (the order will remain

active until the stop date indicated)

A new order must be written for any new medication or to make any changes

in dosage or directions on an existing order.

--------------------------------------------------------------------------------

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/1920 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/2000

Dx: TESTING

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_

Allergies: No Allergy Assessment

ADR:

--------------------------------------------------------------------------------

No. Action Drug ST Start Stop Status/Info

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 R D N AMPICILLIN 1 GM C 09/07 09/14 A

in 0.9% NACL 100 ML QID

Special Instructions: THIS IS AN INPATIENT IV EXAMPLE

2 R D N AMPICILLIN CAP C 09/07 09/21 A

Give: 500MG PO QID

3 R D N HYDROCORTISONE CREAM,TOP C 09/07 09/21 A

Give: 1% TOP QDAILY

4 R D N MULTIVITAMINS 5 ML C 09/07 09/12 A

in 0.9% NACL 1000 ML 20 ml/hr

5 R D N PROPRANOLOL 10MG U/D C 09/07 09/21 A

Give: PO QDAILY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date AND Time PHYSICIAN’S SIGNATURE

MULTIDISCIPLINARY REVIEW

(WHEN APPROPRIATE) \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PHARMACIST'S SIGNATURE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NURSE'S SIGNATURE

ADDITIONAL MEDICATION ORDERS:

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date AND Time PHYSICIAN’S SIGNATURE

PSJPATIENT1,ONE 000-00-0001 08/18/1920

### Action Profile \#2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU AP-2\]

The *Action Profile \#2* \[PSJU AP-2\] option is similar to the *Action Profile \#1* option (see previous report) with the added feature that the nurse can show only expiring orders, giving in effect, stop order notices (see *INpatient Stop Order Notices*).

The *Action Profile \#2* \[PSJU AP-2\] option also allows for viewing a list of clinic orders. Clinic orders are displayed separately from non-clinic orders.

The user can run the *Action Profile \#2* \[PSJU AP-2\] option by group (G), ward (W), clinic (C), or patient (P). When group is selected, a prompt to select by ward group (W) or clinic group (C) displays. If this option is run by patient, the opportunity to select as many patients as desired is given, but the user will not get a report if the patient has no <u>active</u> orders.

If the option for a ward or a ward group is chosen, a prompt to choose the ward or ward group for which the user wants to run the option is displayed. The user will then be asked to sort (print) Action Profiles by team (T) or treating provider (P). If Ward Group of ^OTHER is entered, the user will not be given a sort (print) option; it will automatically sort by treating provider and print a report of Outpatients that are receiving Inpatient Medications and that meet the report parameters.

At the “Print (A)ll active orders, or (E)xpiring orders only? A//” prompt, the user can choose to print all active orders for the patient(s) selected, or print only orders that will expire within the date range selected for the patient(s) selected.

There are six medication choices. The user may select multiple choices of medications to be printed on the Action Profile \#2 report. Since the first choice is ALL Medications, the user will not be allowed to combine this with any other choices.

It is recommended that the action profiles be printed on two-part paper, if possible. Using two-part paper allows a copy to stay on the ward and the other copy to be sent to the pharmacy.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/094.png)Note: This report uses a four-digit year format.

Example: Action Profile \#2

Select Reports Menu Option: AP2 Action Profile \#2

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): PATIENT \<Enter\>

Select PATIENT: PSJPATIENT1,ONE 000-00-0001 08/18/20 1 EAST

Select another PATIENT: \<Enter\>

Enter START date/time: NOW// \<Enter\> (09/11/00@11:02)

Enter STOP date/time: 09/11/2000@11:02// T+7 (09/18/2000)

Print (A)ll active orders, or (E)xpiring orders only? A// \<Enter\> (ALL)

Enter medication type(s): 2,3,6// 1

Select PRINT DEVICE: \<Enter\> NT/Cache virtual TELNET terminal

...this may take a few minutes...(you really should QUEUE this report)...

Enter RETURN to continue or '^' to exit: \<Enter\>

UNIT DOSE ACTION PROFILE \#2 09/11/2000 11:03

SAMPLE HEALTHCARE SYSTEM

(Continuation of VA FORM 10-1158) Page: 1

--------------------------------------------------------------------------------

A new order must be written for any new medication or to make any changes

in dosage or directions on an existing order.

--------------------------------------------------------------------------------

Team: NOT FOUND

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/1920 (80) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/2000

Dx: TESTING

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies: No Allergy Assessment

ADR:

--------------------------------------------------------------------------------

No. Action Drug ST Start Stop Status/Info

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 AMPICILLIN 1 GM C 09/07 09/14 A

in 0.9% NACL 100 ML QID

Special Instructions: THIS IS AN INPATIENT IV EXAMPLE

\_\_TAKE NO ACTION \_\_DISCONTINUE \_\_RENEW COST/DOSE: 1.32

------------------------------------------------------------------------

2 AMPICILLIN CAP C 09/07 09/21 A

Give: 500MG PO QID

\_\_TAKE NO ACTION \_\_DISCONTINUE \_\_RENEW COST/DOSE: 0.731

------------------------------------------------------------------------

3 HYDROCORTISONE CREAM,TOP C 09/07 09/21 A

Give: 1% TOP QDAILY

\_\_TAKE NO ACTION \_\_DISCONTINUE \_\_RENEW COST/DOSE: 0.86

------------------------------------------------------------------------

4 MULTIVITAMINS 5 ML C 09/07 09/12 A

in 0.9% NACL 1000 ML 20 ml/hr

\_\_TAKE NO ACTION \_\_DISCONTINUE \_\_RENEW COST/DOSE: 468.795

------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date AND Time PHYSICIAN’S SIGNATURE

MULTIDISCIPLINARY REVIEW

(WHEN APPROPRIATE) \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PHARMACIST'S SIGNATURE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NURSE'S SIGNATURE

ADDITIONAL MEDICATION ORDERS:

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date AND Time PHYSICIAN’S SIGNATURE

PSJPATIENT1,ONE 000-00-0001 08/18/1920

### AUthorized Absence/Discharge Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU DS\]

The *AUthorized Absence/Discharge Summary* option creates a report to allow the user to determine what action to take on a patient’s Unit Dose orders if the patient is discharged from the hospital or will leave the hospital for a designated period of time (authorized absence). The form is printed so that the provider can place the active orders of a patient on hold, not take any action on the order, or continue the order upon discharge or absence. If the provider wishes to continue the order upon discharge, then he or she can identify the number of refills, the quantity, and the number of days for the order to remain active. If no action is taken on the order, it will expire or be discontinued.

The user can run the Authorized Absence Discharge Summary by ward group, ward, or by patient. If the user chooses to run this report by patient, the opportunity is given to select as many patients as desired, but only patients with <u>active</u> orders will print.

If the option by ward or ward groups is chosen, the user will be prompted for start and stop date. Entry of these dates is not required, but if a start and stop date is entered, a discharge summary will print only for those patients that have at least one order that will be active between those dates. If the user does not enter a start date, all patients with active orders will print (for the ward or ward group chosen). If a clinic visit has been scheduled, the date will print. If more than one has been scheduled, only the first one will print. It is recommended that this report be queued to print when user demand for the system is low.

For co-payment purposes, information related to the patient’s service connection is shown on the first page of the form (for each patient). If the patient is a service-connected less than 50% veteran, the provider is given the opportunity to mark each non-supply item order as either SERVICE CONNECTED (SC) or NON-SERVICE CONNECTED (NSC).

![](inpatient-medications-nurse-s-user-manual-psj-5-423/095.png)Note: This report uses a four-digit year format.

Example: Authorized Absence/Discharge Summary

Select Reports Menu Option: AUthorized Absence/Discharge Summary

Print BLANK Authorized Absence/Discharge Summary forms? NO// \<Enter\>

Select by WARD GROUP (G), WARD (W), or PATIENT (P): Patient \<Enter\>

Select PATIENT: PSJPATIENT2,TWO 000-00-0002 02/22/42 1 West

Select another PATIENT: \<Enter\>

...this may take a few minutes...(you should QUEUE this report)...

Select PRINT DEVICE: \<Enter\> TELNET

AUTHORIZED ABSENCE/DISCHARGE ORDERS 09/19/2000 12:43

VAMC: REGION 5 (660)

VA FORM: 10-7978M

Effective Date: Page: 1

================================================================================

Instructions to the physician:

A. A prescription blank (VA FORM 10-2577F) must be used for:

1\. all class II narcotics

2\. any medications marked as 'nonrenewable'

3\. any new medications in addition to those entered on this form.

B. If a medication is not to be continued, mark "TAKE NO ACTION".
C. To continue a medication, you MUST:

1\. enter directions, quantity, and refills

2\. sign the order, enter your DEA number, and enter the date AND time.

================================================================================

PSJPATIENT2,TWO Ward: 1 West

PID: 000-00-0002 Room-Bed: A-6 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 02/22/1942 (58) Team: \* NF \* Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Last Admitted: 06/24/1998

Dx: KDJF Discharged: 12/11/12

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_

Allergies: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE, CHOCOLATE,

NUTS, STRAWBERRIES, DUST

NV Aller.: AMOXICILLIN, AMPICILLIN, TAPE, FISH, FLUPHENAZINE DECANOATE

ADR:

================================================================================

\*\*\* THIS PATIENT HAS NON-VERIFIED ORDERS. \*\*\*

\_\_\_ AUTHORIZED ABSENCE \<96 HOURS \_\_\_ AUTHORIZED ABSENCE \>96 HOURS

NUMBER OF DAYS: \_\_\_\_\_ (NO REFILLS allowed on AA/PASS meds)

\_\_\_ REGULAR DISCHARGE \_\_\_ OPT NSC \_\_\_ SC

Service Connected:

Disabilities: NONE STATED

Next scheduled clinic visit:

================================================================================

Schedule Cost per

No. Medication Type Dose

--------------------------------------------------------------------------------

1 ACETAMINOPHEN 650 MG SUPP CONTINUOUS 0.088

Inpt Dose: 650MG RECTALLY QDAILY

\_\_\_ TAKE NO ACTION (PATIENT WILL NOT RECEIVE MEDICATION)

Outpatient Directions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Qty: \_\_\_\_\_ Refills: 0 1 2 3 4 5 6 7 8 9 10 11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician’s Signature DEA \# Date AND Time

Enter RETURN to continue or '^' to exit:

AUTHORIZED ABSENCE/DISCHARGE ORDERS Page: 2

VAMC: REGION 5 (660)

VA FORM: 10-7978M

PSJPATIENT2,TWO 000-00-0002 02/22/1942

--------------------------------------------------------------------------------

Schedule Cost per

No. Medication Type Dose

--------------------------------------------------------------------------------

2 BENZOYL PEROXIDE 10% GEL (2OZ) CONTINUOUS 3.78

Inpt Dose: APPLY SMALL AMOUNT TOP QDAILY

Special Instructions: TEST

\_\_\_ TAKE NO ACTION (PATIENT WILL NOT RECEIVE MEDICATION)

Outpatient Directions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Qty: \_\_\_\_\_ Refills: 0 1 2 3 4 5 6 7 8 9 10 11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician’s Signature DEA \# Date AND Time

--------------------------------------------------------------------------------

3 RANITIDINE 150MG CONTINUOUS 0.5

Inpt Dose: 150MG PO BID

\_\_\_ TAKE NO ACTION (PATIENT WILL NOT RECEIVE MEDICATION)

Outpatient Directions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Qty: \_\_\_\_\_ Refills: 0 1 2 3 4 5 6 7 8 9 10 11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician’s Signature DEA \# Date AND Time

--------------------------------------------------------------------------------

4 THEO-24 200MG CONTINUOUS 0.086

Inpt Dose: 400MG PO QID

Special Instructions: TESTING DO

\_\_\_ TAKE NO ACTION (PATIENT WILL NOT RECEIVE MEDICATION)

Outpatient Directions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Qty: \_\_\_\_\_ Refills: 0 1 2 3 4 5 6 7 8 9 10 11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician’s Signature DEA \# Date AND Time

================================================================================

OTHER MEDICATIONS:

5 Medication: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Outpatient Directions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Qty: \_\_\_\_\_ Refills: 0 1 2 3 4 5 6 7 8 9 10 11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician’s Signature DEA \# Date AND Time

--------------------------------------------------------------------------------

6 Medication: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Outpatient Directions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Qty: \_\_\_\_\_ Refills: 0 1 2 3 4 5 6 7 8 9 10 11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician’s Signature DEA \# Date AND Time

Enter RETURN to continue or '^' to exit: \<Enter\>

AUTHORIZED ABSENCE/DISCHARGE INSTRUCTIONS 09/19/2000 12:43

VAMC: REGION 5 (660)

VA FORM: 10-7978M

Effective Date:

================================================================================

PSJPATIENT2,TWO Ward: 1 West

PID: 000-00-0002 Room-Bed: A-6 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 02/22/1942 (58) Team: \* NF \* Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Last Admitted: 06/24/1998

Dx: KDJF Discharged: 12/11/12

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_

Allergies: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE, CHOCOLATE,

NUTS, STRAWBERRIES, DUST

NV Aller.: AMOXICILLIN, AMPICILLIN, TAPE, FISH, FLUPHENAZINE DECANOATE

ADR:

================================================================================

Next scheduled clinic visit:

================================================================================

DIETARY INSTRUCTIONS: (Check One)

\_\_ NO RESTRICTIONS \_\_ RESTRICTIONS (Specify) \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

================================================================================

PHYSICAL ACTIVITY LIMITATIONS: (Check One)

\_\_ NO RESTRICTIONS \_\_ RESTRICTIONS (Specify) \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

================================================================================

SPECIAL INSTRUCTIONS: (list print information, handouts, or other

instructions pertinent to patient's condition)\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

================================================================================

DIAGNOSES: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter RETURN to continue or '^' to exit: \<Enter\>

AUTHORIZED ABSENCE/DISCHARGE INSTRUCTIONS 09/19/2000 12:43

VAMC: REGION 5 (660)

VA FORM: 10-7978M

Effective Date:

================================================================================

PSJPATIENT2,TWO Ward: 1 West

PID: 000-00-0002 Room-Bed: A-6 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 02/22/1942 (58) Team: \* NF \* Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Last Admitted: 06/24/1998

Dx: KDJF Discharged: 12/11/12

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_

Allergies: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE, CHOCOLATE,

NUTS, STRAWBERRIES, DUST

NV Aller.: AMOXICILLIN, AMPICILLIN, TAPE, FISH, FLUPHENAZINE DECANOATE

ADR:

================================================================================

Next scheduled clinic visit:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Nurse's Signature Date AND Time

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician’s Signature Date AND Time

==========================================

\>\>\>\>\> I HAVE RECEIVED AND UNDERSTAND \<\<\<\<\<

\>\>\>\>\> MY DISCHARGE INSTRUCTIONS \<\<\<\<\<

==========================================

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Patient's Signature Date And Time

PSJPATIENT2,TWO 000-00-0002 02/22/1942

### Extra Units Dispensed Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU EUDD\]

The *Extra Units Dispensed Report* option allows the user to print a report showing the amounts, date dispensed, and the initials of the person who entered the dispensed drug. This can be printed by ward group, ward, or by patient. If the user chooses to select by ward, the administration teams may be specified. The default for the administration team is ALL and multiple administration teams may be entered. If selecting by ward or ward group, the profile may be sorted by patient name or room-bed.

Example: Extra Units Dispensed Report

Select Reports Menu Option: EXtra Units Dispensed Report

Enter Start Date and Time: T@1000 (09/19/2000@10:00)

Enter Ending Date and Time: T@2400 (09/19/2000@24:00)

Select by WARD GROUP (G), WARD (W), or PATIENT (P): Patient \<Enter\>

Select PATIENT: PSJPATIENT2,TWO 2-22-42 000000002 YES ACTIVE DUTY

Select another PATIENT: \<Enter\>

Select output device: 0;80 TELNET

this may take a while...(you should QUEUE the Extra Units Dispensed report)

EXTRA UNITS DISPENSED REPORT PAGE: 1

REPORT FROM: 09/19/2000 10:00 TO: 09/19/2000 24:00

PSJPATIENT2,TWO Room_Bed: A-6

000-00-0002 Ward: 1 West

DRUG NAME UNIT DATE DISP.

DISPENSED BY

ACETAMINOPHEN 650 MG SUPP 3 09/19/00 12:54 MV

5 09/19/00 12:54 MV

.......................................... 8

BENZOYL PEROXIDE 10% GEL (2OZ) 2 09/19/00 12:58 PM

.......................................... 2

RANITIDINE 150MG 3 09/19/00 12:54 MV

3 09/19/00 12:58 PM

.......................................... 6

TOTAL FOR PSJPATIENT2,TWO................... 16

Press Return to continue...

### Free Text Dosage Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU DOSAGE REPORT\]

The *Free Text Dosage Report* option creates a report to track commonly ordered free text dosages over a date range. This report evaluates Unit Dose orders that were active during the specified dates against the DISPENSE DRUG file. If the applicable Possible Dosages or Local Possible Dosages do not match the Dosage Ordered, then this is considered a Free Text Dosage Entry and is contained in this report. This report includes the:

- Dispense Drug
- Free Text Dosage Entry
- Total number of occurrences of each Free Text Dosage Entry
- Number of occurrences by the Provider Name

Each entry in the Free Text Dosage Report consists of at least two lines of display. The first line shows the Dispense Drug name, followed by the drug internal entry number in parentheses. The first line continues with the Free Text Dosage Entry and the total number of occurrences of this entry. The second line shows the name of the Providers that used this Free Text Dosage Entry during the requested date range, and the number of times Providers used this free text dosage. Since all Providers are listed, multiple lines will be displayed.

Unit Dose orders that were active during the specified date range and have free text dosages are included in this report. The user is prompted to enter the “Beginning Date:” and an “Ending Date:” for the report to print. If no value is entered in either of the two prompts, the report will not print. The date range will be listed in the “Period:” section of the report header with the beginning date appearing as the first date and the ending date appearing as the second date.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/096.png)Note: It is strongly recommended that this report be queued to print at a later time.

Example: Free Text Dosage Report

Select Reports Menu Option: FREE Text Dosage Report

Beginning Date: T-100 (SEP 29, 2001)

Ending Date: T (JAN 07, 2002)

DEVICE: HOME// 0;80 NT/Cache virtual TELNET terminal

Working - please wait...........................

Page 1

Inpatient Free Text Dosage Entry Report

Period: Sep 29, 2001 to Jan 07, 2002

Drug Free Text Entry Count

Provider:Count

-------------------------------------------------------------------------------

A-METHYL-PARA-TYROSINE CAPS,25 (5098) 100MG 1

PSJPROVIDER,ONE:1

ACETAMINOPHEN 325MG C.T. (263) 1000MG 1

PSJPROVIDER,TWO:1

100MG 2

PSJPROVIDER,THREE:1 PSJPROVIDER,FOUR:1

100mg 1

PSJPROVIDER,FOUR:1

300MG 1

PSJPROVIDER,TWO:1

325MG 7

PSJPROVIDER,ONE:1 PSJPROVIDER,TWO:4

PSJPROVIDER,FIVE:2

Press Return to Continue or ^ to Exit:

### INpatient Stop Order Notices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ EXP\]

The *INpatient Stop Order Notices* option produces a list of patients’ medication orders that are about to expire. Action must be taken (using VA FORM 10-1158) if these medications are to be re-ordered. This option will list both Unit Dose orders and IV orders. The user may choose to print All, which is the default, or either the Unit Dose or IV orders.

The next prompt allows the user to select by group (G), ward (W), clinic (C), or patient (P). When group is selected, a prompt to select by ward group (W) or clinic group (C) displays.

Start and stop dates will be prompted next.

Special Instructions for Unit Dose orders and Other Print Information for IV orders are listed on the report. IV orders are sorted by the Orderable Item of the first additive or solution in the order. The Orderable Item with each additive and solution is displayed along with the strength/volume specified. The schedule type for all IV orders is assumed to be continuous.

If the user chooses to print by ward, the selection to sort by administration teams is displayed. ALL teams, which is the default, multiple teams, or one administration team may be chosen.

Example: Inpatient Stop Order Notices

Select Reports Menu Option: INpatient Stop Order Notices

Select by GROUP (G), WARD (W), CLINIC (C), or PATIENT (P): PATIENT \<Enter\>

Select PATIENT: PSJPATIENT2,TWO 000-00-0002 02/22/42 1 West

Enter start date: T (09/19/2000)

Enter stop date: T+7 (09/26/2000)

List IV orders, Unit Dose orders, or All orders: ALL// \<Enter\>

Select PRINT DEVICE: 0;80 TELNET

...this may take a few minutes...

...you really should QUEUE this report, if possible...

Enter RETURN to continue or '^' to exit: \<Enter\>

AS OF: 09/19/00 13:14 Page: 1

THE FOLLOWING MEDICATIONS WILL EXPIRE

FROM 09/19/00 00:01 THROUGH 09/26/00 24:00

TO CONTINUE MEDICATIONS, PLEASE REORDER ON VA FORM 10-1158.

PSJPATIENT2,TWO Ward: 1 West

PID: 000-00-0002 Room-Bed: A-6 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 02/22/1942 (58) Team: \* NF \* Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Last Admitted: 06/24/98

Dx: KDJF Discharged: 12/11/12

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_

Allergies: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE, CHOCOLATE,

NUTS, STRAWBERRIES, DUST

NV Aller.: AMOXICILLIN, AMPICILLIN, TAPE, FISH, FLUPHENAZINE DECANOATE

ADR:

Medication ST Start Stop Status/Info

Dosage Provider

--------------------------------------------------------------------------------

AMPICILLIN 1 GM C 09/19 09/22/00 18:00 A

in 0.45% NACL 100 ML QID PSJPROVIDER,ONE

IV

PENTAMIDINE ISETHIONATE 1 MG C 09/19 09/22/00 18:00 A

in 0.45% NACL 1000 ML 8 MG/HR PSJPROVIDER,ONE

IV 8 MG/HR@1

ACETAMINOPHEN 300/CODEINE 30 TAB C 09/16 09/22/00 22:00 A

Give: 2TABS PO QDAILY PSJPROVIDER,ONE

BENZOYL PEROXIDE GEL,TOP C 09/19 09/22/00 22:00 A

Give: APPLY SMALL AMOUNT TOP QDAILY PSJPROVIDER,ONE

Special Instructions: TEST

RANITIDINE TAB C 09/18 09/22/00 22:00 A

Give: 150MG PO BID PSJPROVIDER,ONE

THEOPHYLLINE CAP,SA C 09/18 09/22/00 22:00 A

Give: 400MG PO QID PSJPROVIDER,ONE

Special Instructions: TESTING

PSJPATIENT2,TWO 000-00-0002 1 West A-6

### Medications Due Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ MDWS\]

The *Medications Due Worksheet* option creates a report that lists active medications (Unit Dose and IV) that are due within a selected 24-hour period. The user will be able to select by ward group, ward, or individual patients. If the user chooses to select by ward, the administration teams may be specified. The default for the administration team is ALL and multiple administration teams may be entered. If selecting by ward or ward group, the Medications Due Worksheet may be sorted by administration time, patient name, or room-bed. However, if the user chooses to select by patient, multiple patients can be entered.

![](inpatient-medications-nurse-s-user-manual-psj-5-423/097.png)Note: If you specify ^OTHER as the ward group, it will select orders for outpatients in clinics that allow inpatient medication orders.

For IV orders that have no schedule, the projected administration times will be calculated based on the order’s volume, flow rate, and start time. An asterisk (\*) will be printed for the administration times instead of the projected administration times.

If the MAR ORDER SELECTION DEFAULT prompt for the ward parameter is defined, the default will be displayed at the “Enter medication type(s):” prompt.

The default choice is 2 or Non-IV Medications only if:

1.  The MAR ORDER SELECTION DEFAULT parameter was not defined.
2.  Selection by Ward group.
3.  Selected by patients and patients are from different wards.

The PRN medication orders will be printed if the user enters YES at the “Would you like to include PRN Medications (Y/N)? NO//” prompt. PRN orders will be listed after all continuous and one-time orders are printed.

Example: Medications Due Worksheet

Select Reports Menu Option: MEDications Due Worksheet

Would you like to include PRN Medications (Y/N)? NO// YES

Enter Start Date and Time: T@1000 (09/19/00@10:00)

Enter Ending Date and Time: T@2400 (09/19/00@24:00)

Select by WARD GROUP (G), WARD (W), or PATIENT (P): Patient \<Enter\>

Select PATIENT: PSJPATIENT2,TWO 2-22-42 000000002 YES ACTIVE DUTY

Select another PATIENT: \<Enter\>

Enter medication type(s): 2// 1

Select output device: 0;80 TELNET

MEDICATIONS DUE WORKSHEET For: PSJPATIENT2,TWO Page: 1

Report from: 09/19/00 10:00 to: 09/19/00 24:00 Report Date: 09/19/00

Continuous/One time Orders for: ALL MEDS

For date: 09/19/00

PSJPATIENT2,TWO A-6 12:00 09/18 \| 09/18 12:00 \| 09/22/00 22:00

000-00-0002 RANITIDINE TAB

1 West Give: 150MG PO BID

RN/LPN Init: \_\_\_\_\_\_\_\_

09/18 \| 09/18 12:00 \| 09/22/00 22:00

THEOPHYLLINE CAP,SA

Give: 400MG PO QID

TESTING

RN/LPN Init: \_\_\_\_\_\_\_\_

\* 09/19 \| 09/19 12:00 \| 09/22/00 18:00

AMPICILLIN 1 GM

in

0.45% NACL 1000 ML QID

IV QID

RN/LPN Init: \_\_\_\_\_\_\_\_

15:00 09/18 \| 09/18 12:00 \| 09/22/00 22:00

RANITIDINE TAB

Give: 150MG PO BID

RN/LPN Init: \_\_\_\_\_\_\_\_

09/18 \| 09/18 12:00 \| 09/22/00 22:00

THEOPHYLLINE CAP,SA

Give: 400MG PO QID

TESTING

RN/LPN Init: \_\_\_\_\_\_\_\_

20:00 09/18 \| 09/18 12:00 \| 09/22/00 22:00

RANITIDINE TAB

Give: 150MG PO BID

RN/LPN Init: \_\_\_\_\_\_\_\_

09/18 \| 09/18 12:00 \| 09/22/00 22:00

THEOPHYLLINE CAP,SA

Give: 400MG PO QID

TESTING

RN/LPN Init: \_\_\_\_\_\_\_\_

\* Projected admin. times based on order's volume, flow rate, and start time.

Enter RETURN to continue or '^' to exit:

### OTP Medication Dispense Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU OTP\]

The OTP Medication Dispense Report allows the user to print an OTP (Opioid Treatment Program) Medication Dispense Report by patient for a date range. The report shows whether a patient received medication in clinic or as a take-home dose within the date range selected. The report will also display the medication dispensed, the dose amount, the individual that dispensed the dose, and the time of the dispensed dose.

Example: OTP Medication Dispense Report

Enter START Date: T-7// T-30 (OCT 19, 2024)

Enter END Date: T// T (NOV 18, 2024)

Select output device: TELNET PORT

OTP MEDICATION DISPENSE REPORT for Oct 19, 2024 to Nov 18, 2024@23:59

Run Date: NOV 18, 2024@09:47

Page: 1

================================================================================

-------------------------- MEDICATION TO BE TAKEN ON: -------------------------

\| \| \| \| \| \| \| \|

\|10/19/2024\|10/20/2024\|10/21/2024\|10/22/2024\|10/23/2024\|10/24/2024\|10/25/2024 \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

\|Take Home \|Take Home \|Take Home \|In Clinic \|Take Home \|Take Home \|In Clinic \|

\| \| \| \|12:41 PO \| \| \|12:42 PO \|

\| \| \| \|Meth LIQ \| \| \|Meth LIQ \|

\| \| \| \|60 MG \| \| \|60 MG \|

-------------------------------------------------------------------------------

-------------------------- MEDICATION TO BE TAKEN ON: -------------------------

\| \| \| \| \| \| \| \|

\|10/26/2024\|10/27/2024\|10/28/2024\|10/29/2024\|10/30/2024\|10/31/2024\|11/01/2024 \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

\|Take Home \|Take Home \|Take Home \|In Clinic \|Take Home \|Take Home \|In Clinic \|

\| \| \| \|12:41 PO \| \| \|12:43 PO \|

\| \| \| \|Meth LIQ \| \| \|Meth LIQ \|

\| \| \| \|60 MG \| \| \|60 MG \|

-------------------------------------------------------------------------------

-------------------------- MEDICATION TO BE TAKEN ON: -------------------------

\| \| \| \| \| \| \| \|

\|11/02/2024\|11/03/2024\|11/04/2024\| \| \| \| \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

\|Take Home \|Take Home \|Take Home

\| \| \|

\| \| \|

\| \| \|

-------------------------------------------------------------------------------

\*\* LEGEND \*\*

================================================================================

Initial - Name Legend

PO – PROVIDER ONE

BLANK SPACE - shows that no dispense information was received via the interface.

This can indicate the patient was a no-show for their appointment, no medication

was prescribed/dispensed, or that the interface failed to send the data.

\*\* - Asterisks indicate that Dispense Amount may have changed within the week.

================================================================================

### Patient Profile (Extended)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ EXTP\]

The *Patient Profile (Extended)* option creates a report to allow the viewing of all the orders on file for a patient. The user can view all of the orders that have not been purged or enter a date to start searching from.

Select Reports Menu Option: PATient Profile (Extended)

Select PATIENT: PSJPATIENT1,ONE 000-00-0001 08/18/20 1 EAST

Date to start searching from (optional): 083101

Select another PATIENT: \<Enter\>

Show PROFILE only, EXPANDED VIEWS only, or BOTH: PROFILE// BOTH

Show SHORT, LONG, or NO activity log? NO// SHORT

Select PRINT DEVICE: \<Enter\> DECSERVER

I N P A T I E N T M E D I C A T I O N S 02/28/02 14:12

VAMC: ALBANY, NY (500)

\- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

PSJPATIENT1,ONE Ward: 1 EAST

PID: 000-00-0001 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 05/03/00

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_

Allergies: No Allergy Assessment

ADR:

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 MULTIVITAMINS 5 ML C 02/28/2002 03/30/2002 A

in 0.9% SODIUM CHLORIDE 1000 ML Q8H

2 BACLOFEN TAB C 02/20/2002 03/06/2002 A

Give: 10MG PO QDAILY

PATIENT SPITS OUT MEDICINE

3 PREDNISONE TAB C 02/25/2002 03/11/2002 A

Give: 5MG PO TU-TH-SA@09

4 RESERPINE TAB C 02/20/2002 03/06/2002 A

Give: 1MG PO QDAILY

5 PANCREATIN CAP,ORAL O 02/21/2002 03/23/2002 A

Give: 1 CAPSULE PO ONCE

\- - - - - - - - - - - - - - - N O N - A C T I V E - - - - - - - - - - - - - - -

6 CEFTAZIDIME INJ ? \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* N

Give: 1 GM IV QDAILY

7 TRACE ELEMENTS INJ ? \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* N

Give: 1 ML IV QDAILY

\- - - - - - - - - - - - - - - N O N - A C T I V E - - - - - - - - - - - - - - -

8 in DEXTROSE 5% 1000 ML 1 ml/hr ? \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* P

9 CEFAZOLIN INJ ? \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* P

Give: 1GM/1VIAL IVPB ONE TIME

10 PENICILLIN INJ,SUSP ? \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* P

Give: 600000UNT/1ML IM BID

11 PENICILLIN INJ,SUSP ? \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* P

Give: 600000UNT/1ML IM QDAILY

\- - - - - - - - - - - - - - - N O N - A C T I V E - - - - - - - - - - - - - - -

12 CEFAZOLIN 1 GM C 11/02/2001 12/07/2001 E

in 5% DEXTROSE 1000 ML QID

13 zC2TESTDRUG 1 LITER C 12/14/2001 12/21/2001 E

in 5% DEXTROSE 1000 ML QDAILY

Enter RETURN to continue or '^' to exit: \<Enter\>

Patient: PSJPATIENT1,ONE Status: ACTIVE

\*(1) Additives: Order number: 29 Type: PIGGYBACK

MULTIVITAMINS 5 ML

\(2\) Solutions:

0.9% SODIUM CHLORIDE 1000 ML

Duration: \*(4) Start: 02/28/2002 13:56

\(3\) Infusion Rate: INFUSE OVER 8 HOURS.

\*(5) Med Route: IV \*(6) Stop: 03/30/2002 24:00

\*(7) Schedule: QDAILY Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 09-13-17-21 Quantity: 0

\*(9) Provider: PSJPROVIDER,ONE \[w\] Cum. Doses:

\*(10)Orderable Item: MULTIVITAMINS INJ

Instructions:

\(11\) Other Print:

\(12\) Remarks :

Entry By: PSJPROVIDER,ONE Entry Date: 02/28/02 13:56

ACTIVITY LOG:

\# DATE TIME REASON USER

===============================================================================

1 FEB 28,2002 13:58:30 VERIFY PSJPHARMACIST,ONE

Comment: ORDER VERIFIED BY PHARMACIST

----------------------------------------------------------------------

Patient: PSJPATIENT1,ONE Status: ACTIVE

Orderable Item: BACLOFEN TAB

Instructions:

Dosage Ordered: 10MG

Duration: Start: 02/20/2002 15:20

Med Route: ORAL (PO) Stop: 03/06/2002 24:00

Schedule Type: CONTINUOUS

Schedule: QDAILY

Admin Times: 1440

Provider: PSJPROVIDER,ONE \[w\]

Special Instructions: PATIENT SPITS OUT MEDICINE

Units Units Inactive

Dispense Drugs U/D Disp'd Ret'd Date

--------------------------------------------------------------------------------

BACLOFEN 10MG TABS 1 0 0

Entry By: PSJPROVIDER,ONE Entry Date: 02/20/02 15:20

ACTIVITY LOG:

\# DATE TIME REASON USER

===============================================================================

(THE ORDERABLE ITEM IS CURRENTLY LISTED AS INACTIVE.)

Date: 02/20/02 15:20 User: PSJPHARMACIST,ONE

Activity: ORDER ENTERED AS ACTIVE BY PHARMACIST

----------------------------------------------------------------------

Patient: PSJPATIENT1,ONE Status: ACTIVE

Orderable Item: PREDNISONE TAB

Instructions:

Dosage Ordered: 5MG

Duration: Start: 02/25/2002 10:58

Med Route: ORAL (PO) Stop: 03/11/2002 24:00

Schedule Type: CONTINUOUS

Schedule: TU-TH-SA@09

Admin Times: 09

Provider: PSJPROVIDER,ONE \[w\]

Units Units Inactive

Dispense Drugs U/D Disp'd Ret'd Date

--------------------------------------------------------------------------------

PREDNISONE 5MG TAB 1 0 0

Self Med: NO

Entry By: PSJPROVIDER,ONE Entry Date: 02/25/02 10:58

ACTIVITY LOG:

\# DATE TIME REASON USER

===============================================================================

Date: 02/25/02 10:58 User: PSJPHARMACIST,ONE

Activity: ORDER VERIFIED BY PHARMACIST

## Align Labels (Unit Dose)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU AL\]

The *Align Labels (Unit Dose)* option allows the user to align the label stock on a printer so that Unit Dose order information will print within the physical boundaries of the label.

Example: Align Labels (Unit Dose)

Select Unit Dose Medications Option: ALIGn Labels (Unit Dose)

Select LABEL PRINTER: \<Enter\> TELNET

\\------------ FIRST LINE OF LABEL ------------/

\< \>

\<------------- LABEL BOUNDARIES ---------------\>

\< \>

/--------------LAST LINE OF LABEL--------------\\

XX/XX \| XX/XX \| XX/XX/XX XX:XX (PXXXX) \| A T PATIENT NAME

ROOM-BED

DRUG NAME SCHEDULE TYPE\| D I XXX-XX-XXXX DOB (AGE)

TEAM

DOSAGE ORDERED MED ROUTE SCHEDULE \| M M SEX DIAGNOSIS

SPECIAL INSTRUCTIONS \| I E ACTIVITY DATE/TIME ACTIVITY

WS HSM NF RPH:\_\_\_\_\_ RN:\_\_\_\_\_\| N S WARD GROUP

WARD

Are the labels aligned correctly? Yes// Y (Yes)

## Label Print/Reprint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU LABEL\]

The *Label Print/Reprint* option allows the user to print new unprinted labels and/or reprint the latest label for any order containing a label record. When entering this option, the nurse will be informed if there are any unprinted new labels from auto-cancelled orders (i.e., due to ward or service transfers). The nurse will be shown a list of wards to choose from if these labels are to be printed at this time. The nurse can delete these auto-cancel labels; however, deletion will be for <u>all</u> of the labels.

Next, the nurse will be instructed if there are any unprinted new labels. The nurse can then decide whether to print them now or later.

The nurse can choose to print the labels for a group (G), ward (W), clinic (C), or patient (P). When group is selected, a prompt to select by ward group (W) or clinic group (C) displays. If ward, ward group, clinic, or clinic group is chosen, the label start date will be entered and the labels will print on the specified printer device. When the option to print by individual patient is chosen, an Inpatient Profile will be displayed and the nurse can then choose the labels from the displayed Unit Dose and IV orders to be printed on a specified printer.

# Inquiries Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the Inquiries Options are located under the *INQuiries Menu* option on the *Unit DoseMedications* menu.

INQuiries Menu\[PSJU INQMGR\]

The *INQuiries Menu* option allows the user to view information concerning standard schedules and drugs. No information in this option can be edited, so there is no danger of disrupting the Unit Dose Medications module’s operation. The *INQuiries Menu* contains the following sub-options:

Example: Inquiries Menu

Select Unit Dose Medications Option: INQuiries Menu

Select INQuiries Menu Option: ?

Dispense Drug Look-Up

Standard Schedules

## Dispense Drug Look-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSJU INQ DRUG\]

The *Dispense Drug Look-Up* option allows the user to see what drugs are in the DRUG file and any Unit Dose information pertaining to them.

At the “Select DRUG:” prompt, the nurse can answer with drug number, quick code, or VA drug class code (for IV, solution print name, or additive print name). Information about the selected drug will be displayed.

Example: Dispense Drug Look-Up

Select Unit Dose Medications Option: INQuiries Menu

Select INQuiries Menu Option: DIspense Drug Look-Up

Select DRUG: ASP

1 ASPIRIN 10 GRAIN SUPPOSITORIES CN103 02-18-98 INPATIENT

2 ASPIRIN 325MG CN103 N/F \*90-DAY FILL\*

3 ASPIRIN 325MG E.C. CN103 \*90-DAY FILL\*

4 ASPIRIN 325MG E.C. U/D CN103 N/F TAB

5 ASPIRIN 325MG U/D CN103

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 5 ASPIRIN 325MG U/D CN103

FORMULARY ITEM

A UNIT DOSE DRUG

DAY (nD) or DOSE (nL) LIMIT:

UNIT DOSE MED ROUTE:

UNIT DOSE SCHEDULE TYPE:

UNIT DOSE SCHEDULE:

CORRESPONDING OUTPATIENT DRUG:

ATC MNEMONIC:

ATC CANISTER: WEST WING 12

SOUTH WING 12

JUNK ONE 12

TESSS 12

11;PS(57.5, 12

13;PS(57.5, 12

14;PS(57.5, 12

15;PS(57.5, 12

16;PS(57.5, 12

17;PS(57.5, 12

18;PS(57.5, 12

21;PS(57.5, 12

22;PS(57.5, 12

Select DRUG:

## Standard Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU INQ STD SCHD\]

It is extremely important for all users to know the method of schedule input. When the user enters a standard schedule, the system will echo back the corresponding Administration times.

At the “Select STANDARD SCHEDULE:” prompt, enter an administration schedule abbreviation to view information pertaining to that schedule. An explanation of the selected schedule will be displayed. To view a list of the available administration schedule abbreviations, enter a question mark (?) at the prompt “Select STANDARD SCHEDULE:”.

Example: Standard Schedules

Select INQuiries Menu Option: STandard Schedules

Select STANDARD SCHEDULE: q4H 01-05-09-13-17-21

Schedule: Q4H Type: CONTINUOUS

Standard Admin Times: 01-05-09-13-17-21

Select STANDARD SCHEDULE:

# CPRS Order Checks: How They Work

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CPRS Order Checks Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In CPRS, Order Checks occur by evaluating a requested order against existing patient data. Most order checks are processed via the CPRS Expert System. A few are processed within the Pharmacy, Allergy Tracking System, and Order Entry packages. Order Checks are a real-time process that occurs during the ordering session and is driven by responses entered by the ordering provider. Order Check messages are displayed interactively in the ordering session.

Order Checks review existing data and current events to produce a relevant message, which is presented to patient caregivers. Order Checks use the CPRS Expert System (OCX namespace), to define logical expressions for this evaluation and message creation. In addition to the expert system Order Checks have some hard-coded algorithms. For example, the drug-drug interaction order check is made via an entry point in the pharmacy package whereas Renal Functions for Patients Over 65 is defined as a rule in the CPRS Expert System.

## Order Check Data Caching

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data caching was recently added to improve the speed of order checks. Before data caching, order checks could be slow because each order check retrieved data from the other VISTA packages—even if the order checks used the same data. With data caching, the first order check in an ordering session retrieves data from other VISTA packages, uses the data to evaluate whether it should display a warning, and then stores the retrieved data in the ^XTMP(“OCXCACHE” global for five minutes. The order checks that occur in the next five minutes can use the cached data, if it is the appropriate data, instead of retrieving data from the other packages. After five minutes, the cached data expires, and order checks must retrieve new data from the VISTA packages.

For example, before data caching was implemented, if an order check took 3 seconds to retrieve data from other VISTA packages, and there were 12 order checks, clinicians might wait 36 seconds to sign orders. With data caching, the first order check might take 3 seconds to retrieve the data, but subsequent order checks could use the cache and might take only .03 seconds each. That would be 3.33 seconds compared to 36 seconds. The numbers in this example are for illustration only and do not reflect real system speed. However, data caching should speed up order checks.

To avoid using all available disk space for storing data from order checks, there are several ways to clear the ^XTMP(“OCXCACHE” global. ORMTIME removes data from the global when it runs. The suggested frequency for running ORMTIME is every 30 minutes, but not every site runs it that frequently. Kernel clean up utilities also remove data from the cache when they run, which is usually every 24 hours. If needed, users that have access to the programmer’s prompt can manually clear the cache from that prompt by using PURGE^OCXCACHE.

(*This page included for two-sided copying.)*

# Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Error Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The text in the error message and reason column will be displayed to the user. The type of error is displayed in Column 1.

There are three levels of error messages:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>System</th>
<th>When such an error occurs, Drug Interaction, Duplicate Therapy, or Dosing order checks will be performed. Other order checks that do not use the COTS database (FDB) will still be performed such as allergy/ADRs, duplicate drug (for outpatient only) and new CPRS order checks, etc.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Drug</td>
<td><p>The second error level is for the drug and no Drug Interaction, Duplicate Therapy, or Dosing order checks will be performed for a specific drug. Drug level errors can occur for the prospective drug (drug being processed) or the profile drug. If a drug level error occurs on the prospective drug, no profile drug errors will be displayed. The only exception to this is when you are processing an IV order with multiple prospective drugs (i.e. multiple IV Additives). Profile drug level errors will only be shown once per patient session.</p>
<p>There are two reasons that a drug level error is generated; the drug is not matched to NDF or the drug is matched to NDF, but the VA Product to which it is matched does not have a GCNSEQNO assigned or the GCNSEQNO assigned does not match up to the GCNSEQNO in the COTS database. The latter (GCNSENO mismatch) is rare.</p></td>
</tr>
<tr class="even">
<td>Order</td>
<td>The third error level is for the order. Order level errors will only occur with dosing order checks. Please see the <a href="http://vaww.oed.portal.va.gov/projects/pre/PRE_TW/MOCHA%20v2x%20PDFs/Assignments%20and%20Schedule/Kiley&#39;s%20Assignments/Dosing%20Order%20Check%20User%20Manual.doc"><em>Dosing Order Check User Manual</em></a> for more information.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 26%" />
<col style="width: 20%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Level</strong></th>
<th><strong>Error Message</strong></th>
<th><strong>Reason</strong></th>
<th><strong>Why message is being displayed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>System</td>
<td>No Enhanced Order Checks can be performed.</td>
<td>Vendor Database cannot be reached.</td>
<td>The connectivity to the vendor database has gone down. A MailMan message is sent to the G. PSS ORDER CHECKS mail group when the link goes down and when it comes back up.</td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed.</td>
<td>The connection to the vendor database has been disabled.</td>
<td>A user has executed the Enable/Disable Vendor Database Link [PSS ENABLE/DISABLE DB LINK] option and disabled the interface.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>No Enhanced Order Checks can be performed</td>
<td>Vendor database updates are being processed</td>
<td>The vendor database (custom and standard data) is being updated using the DATUP (Data Update) process.</td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed</td>
<td>An unexpected error has occurred</td>
<td>There is a system network problem and the vendor database cannot be reached or a software interface issue.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>No Dosing Order Checks can be performed</td>
<td>Dosing Order Checks are disabled</td>
<td>A user has executed the <em>Enable/Disable Dosing Order Checks</em> [PSS Dosing Order Checks] option.</td>
</tr>
<tr class="even">
<td>System</td>
<td>Recommended frequency of &lt;DRUG NAME&gt;: Unable to convert units: &lt;DOSE UNIT&gt; to &lt;DOSE UNIT&gt;. A frequency check was not performed because the ordered dose of &lt;DOSE UNIT&gt; is not convertible to the dose screening unit of measure of &lt;DOSE UNIT&gt;.</td>
<td></td>
<td>VA customization may exist in which the Dose Units were customized but the patient age is not within bounds of the customized age bands. VA NDF team to refer to PECS to introduce and/or update VA customizations for the patient ages.</td>
</tr>
<tr class="odd">
<td>Drug</td>
<td>Enhanced Order Checks cannot be performed for Local or Local Outpatient Drug: &lt;DRUG NAME&gt;</td>
<td>Drug not matched to NDF</td>
<td>The local drug being ordered/ or on profile has not been matched to NDF. Matching the drug to a VA Product will eliminate this message.</td>
</tr>
<tr class="even">
<td>Drug</td>
<td><p>Order Checks could not be done for Remote Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions and Duplicate Therapy.</p>
<p>Remote order indicator</p></td>
<td></td>
<td>If this error message is displayed, it means that the VA product that the local or remote drug being ordered/or on the local or remote profile does not have a GCNSEQNO or in rare cases, the GCNSEQNO assigned to the VA Product does not match up with a GCNSEQNO in the vendor database.</td>
</tr>
<tr class="odd">
<td>Drug</td>
<td>Enhanced Order Checks cannot be performed for Orderable Item: &lt;OI NAME&gt;</td>
<td>No active Dispense Drug found</td>
<td>Highly unlikely that this error would be seen. At the time the order check was being performed the orderable item did not have an active dispense drug associated.</td>
</tr>
<tr class="even">
<td>Drug</td>
<td>&lt;DRUG NAME&gt; is contraindicated for this patient. Do NOT prescribe/administer this drug by the CONTRAINDICATED &lt;DRUG ROUTE&gt;.</td>
<td>Contraindication</td>
<td>The chosen route is contraindicated and should not be selected.</td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action Prompts</strong></th>
<th>There are three types of Inpatient Medications “Action” prompts that occur during order entry: ListMan, Patient/Order, and Hidden action prompts.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong><u>ListMan Action Prompts</u></strong></p>
</blockquote></td>
<td><p>+ Next Screen</p>
<p>- Previous Screen</p>
<p>UP Up a Line</p>
<p>DN Down a Line</p>
<p>&gt; Shift View to Right</p>
<p>&lt; Shift View to Left</p>
<p>FS First screen</p>
<p>LS Last Screen</p>
<p>GO Go to Page</p>
<p>RD Re Display Screen</p>
<p>PS Print Screen</p>
<p>PT Print List</p>
<p>SL Search List</p>
<p>Q Quit</p>
<p>ADPL Auto Display (on/off)</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong><u>Patient/Order Action Prompts</u></strong></p>
</blockquote></td>
<td><p>PU Patient Record Updates</p>
<p>DA Detailed Allergy/ADR List</p>
<p>VP View Profile</p>
<p>NO New Orders Entry</p>
<p><span id="CM_New_Clinic_Medication_Entry" class="anchor"></span>CM New Clinic Medication Entry</p>
<p>IN Intervention Menu</p>
<p>PI Patient Information</p>
<p>SO Select Order</p>
<p>DC Discontinue</p>
<p>ED Edit</p>
<p>FL Flag</p>
<p>VF Verify</p>
<p>HD Hold</p>
<p>RN Renew</p>
<p>AL Activity Logs</p>
<p>OC On Call</p>
<p>NL Print New IV Labels</p>
<p>RL Reprint IV Labels</p>
<p>RC Recycled IV</p>
<p>DT Destroyed IV</p>
<p>CA Cancelled IV</p></td>
</tr>
<tr class="odd">
<td><strong><u>Hidden Action Prompts</u></strong></td>
<td><p>LBL Label Patient/Report</p>
<p>JP Jump to a Patient</p>
<p>OTH Other Pharmacy Options</p>
<p>MAR MAR Menu</p>
<p>DC Speed Discontinue</p>
<p>RN Speed Renew</p>
<p>SF Speed Finish</p>
<p>SV Speed Verify</p>
<p>CO Copy</p>
<p>N Mark Not to be Given</p>
<p>I Mark Incomplete</p>
<p>DIN Drug Restr/Guide</p>
<p>DA Display Drug Allergies</p>
<p>OCI Overrides/Interventions</p>
<p>CK Check Interactions</p></td>
</tr>
<tr class="even">
<td><strong>Active Order</strong></td>
<td>Any order which has not expired or been discontinued. Active orders also include any orders that are on hold or on call.</td>
</tr>
<tr class="odd">
<td><strong>Activity Reason Log</strong></td>
<td>The complete list of all activity related to a patient order. The log contains the action taken, the date of the action, and the user who took the action.</td>
</tr>
<tr class="even">
<td><strong>Activity Ruler</strong></td>
<td>The activity ruler provides a visual representation of the relationship between manufacturing times, doses due, and order start times. The intent is to provide the on-the-floor user with a means of tracking activity in the IV room and determining when to call for doses before the normal delivery. The activity ruler can be enabled or disabled under the <em>SIte Parameters (IV)</em> option.</td>
</tr>
<tr class="odd">
<td><strong>Additive</strong></td>
<td>A drug that is added to an IV solution for the purpose of parenteral administration. An additive can be an electrolyte, a vitamin or other nutrient, or an antibiotic. Only an electrolyte or multivitamin type additives can be entered as IV fluid additives in CPRS.</td>
</tr>
<tr class="even">
<td><strong>ADMINISTRATION SCHEDULE File</strong></td>
<td>File #51.1. This file contains administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule type (e.g., QID, Q4H, PRN). The administration time entered is in military time, with each time separated from the next by a dash, and times listed in ascending order.</td>
</tr>
<tr class="odd">
<td><strong>Administering Teams</strong></td>
<td>Nursing teams used in the administration of medication to the patients. There can be a number of teams assigned to take care of one ward, with specific rooms and beds assigned to each team.</td>
</tr>
<tr class="even">
<td><p><strong>Admixture</strong></p>
<p><strong>Allergy/ADR Order Check</strong></p></td>
<td><p>An admixture is a type of intravenously administered medication comprised of any number of additives (including zero) in one solution. It is given at a specified flow rate; when one bottle or bag is empty, another is hung.</p>
<p>The screening of a patient’s documented allergies or adverse reactions against a medication ordered by a provider.</p></td>
</tr>
<tr class="odd">
<td><strong>APSP INTERVENTION File</strong></td>
<td>File #9009032.4. This file is used to enter pharmacy interventions. Interventions in this file are records of occurrences where the pharmacist had to take some sort of action involving a particular prescription or order. A record would record the provider involved, why an intervention was necessary, what action was taken by the pharmacists, etc.</td>
</tr>
<tr class="even">
<td><strong>Average Unit Drug Cost</strong></td>
<td>The total drug cost divided by the total number of units of measurement.</td>
</tr>
<tr class="odd">
<td><strong>BSA</strong></td>
<td><p>Body Surface Area. The Dubois formula is used to calculate the Body Surface Area using the following formula:</p>
<p>BSA (m²) = 0.20247 x Height (m)<sup>0.725</sup> x Weight (kg)<sup>0.425</sup></p>
<p>The equation is performed using the most recent patient height and weight values that are entered into the vitals package.</p>
<p>The calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="even">
<td><strong>BCMA</strong></td>
<td>A VistA computer software package named Bar Code Medication Administration. This package validates medications against active orders prior to being administered to the patient.</td>
</tr>
<tr class="odd">
<td><strong>Calc Start Date</strong></td>
<td>Calculated Start Date. This is the date that would have been the default Start Date/Time for an order if no duration was received from CPRS. Due to the existence of a duration, the default Start Date/Time of the order becomes the <u>expected first dose</u>.</td>
</tr>
<tr class="even">
<td><strong>Calc Stop Date</strong></td>
<td>Calculated Stop Date. This is the date that would have been the default Stop Date/Time for an order if no duration was received from CPRS. Due to the existence of a duration, the default Stop Date/Time of the order becomes the expected first dose plus the duration.</td>
</tr>
<tr class="odd">
<td><strong>Chemotherapy</strong></td>
<td>Chemotherapy is the treatment or prevention of cancer with chemical agents. The chemotherapy IV type administration can be a syringe, admixture, or a piggyback. Once the subtype (syringe, piggyback, etc.) is selected, the order entry follows the same procedure as the type that corresponds to the selected subtype (e.g., piggyback type of chemotherapy follows the same entry procedure as regular piggyback IV).</td>
</tr>
<tr class="even">
<td><strong>Chemotherapy: “Admixture”</strong>;</td>
<td>The Chemotherapy “Admixture” IV type follows the same order entry procedure as the regular admixture IV type. This type is in use when the level of toxicity of the chemotherapy drug is high and is to be administered continuously over an extended period of time (e.g., hours or days).</td>
</tr>
<tr class="odd">
<td><strong>Chemotherapy “Piggyback”</strong></td>
<td>The Chemotherapy “Piggyback” IV type follows the same order entry procedure as the regular piggyback IV type. This type of chemotherapy is in use when the chemotherapy drug does not have time constraints on how fast it must be infused into the patient. These types are normally administered over a 30 - 60 minute interval.</td>
</tr>
<tr class="even">
<td><strong>Chemotherapy “Syringe”</strong></td>
<td>The Chemotherapy “Syringe” IV type follows the same order entry procedure as the regular syringe IV type. Its administration may be continuous or intermittent. The pharmacist selects this type when the level of toxicity of the chemotherapy drug is low and needs to be infused directly into the patient within a short time interval (usually 1-2 minutes).</td>
</tr>
<tr class="odd">
<td><strong>Child Orders</strong></td>
<td>One or more Inpatient Medication Orders that are associated within a Complex order and are linked together using the conjunctions AND and OR to create combinations of dosages, medication routes, administration schedules, and order durations.</td>
</tr>
<tr class="even">
<td><strong>CLINIC DEFINITION file</strong></td>
<td>File #53.46. This file is used in conjunction with Inpatient Medications for Outpatients (IMO) to give the user the ability to define, by clinic, default stop dates, whether to auto-dc IMO orders, and whether to send IMO orders to BCMA. User’s may also define a Missing Dose Request printer and a Pre-Exchange Report printer.</td>
</tr>
<tr class="odd">
<td><strong>Clinic Group</strong></td>
<td>A clinic group is a combination of outpatient clinics that have been defined as a group within Inpatient Medications to facilitate processing of orders.</td>
</tr>
<tr class="even">
<td><strong>Clinical Reminder Order Checks (CROC)</strong></td>
<td>CPRS Order Checks that use Clinical Reminder functionality, both reminder terms and reminder definitions, to perform checks for groups of orderable items.</td>
</tr>
<tr class="odd">
<td><strong>Complex Order</strong></td>
<td>An order that is created from CPRS using the Complex order dialog and consists of one or more associated Inpatient Medication orders, known as “child” orders.</td>
</tr>
<tr class="even">
<td><strong>Continuous IV Order</strong></td>
<td>Inpatient Medications IV order not having an administration schedule. This includes the following IV types: Hyperals, Admixtures, Non-Intermittent Syringe, and Non-Intermittent Syringe or Admixture Chemotherapy.</td>
</tr>
<tr class="odd">
<td><strong>Continuous Syringe</strong></td>
<td>A syringe type of IV that is administered continuously to the patient, similar to a hyperal IV type. This type of syringe is commonly used on outpatients and administered automatically by an infusion pump.</td>
</tr>
<tr class="even">
<td><strong>Coverage Times</strong></td>
<td><p>The start and end of coverage period designates administration times covered by a manufacturing run. There must be a coverage period for all IV types: admixtures and primaries, piggybacks, hyperals, syringes, and chemotherapy. For one type, admixtures for example, the user might define two coverage periods; one from 1200 to 0259 and another from 0300 to 1159 (this would mean that the user has two manufacturing times for admixtures).</p>
<p><strong>Note:</strong> If any of the five Coverage Times are not present in file 59.5 (IV Room) the following warning message will be displayed, “The [name of file 59.5 entry] IV ROOM can be updated using option 'Site Parameters (IV)' by a holder of the PSJI MGR VistA Security Key. Contact the Pharmacy Informaticist to update the IV Room parameters.”</p></td>
</tr>
<tr class="odd">
<td><strong>CPRS</strong></td>
<td>A VistA computer software package called Computerized Patient Record Systems. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application. All pending orders that appear in the Unit Dose and IV modules are initially entered through the CPRS package.</td>
</tr>
<tr class="even">
<td><strong>CrCL</strong></td>
<td><p>Creatinine Clearance. The CrCL value which displays in the pharmacy header is identical to the CrCL value calculated in CPRS. The formula approved by the CPRS Clinical Workgroup is the following:</p>
<p>Modified Cockcroft-Gault equation using<br />
Adjusted Body Weight in kg (if ht &gt; 60in)</p>
<p>This calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="odd">
<td><strong>Critical Drug-Drug Interaction</strong></td>
<td>One of two types of drug-drug interactions identified by order checks. The other type is a “significant” drug-drug interaction</td>
</tr>
<tr class="even">
<td><strong>Cumulative Doses</strong></td>
<td>The number of IV doses actually administered, which equals the total number of bags dispensed less any recycled, destroyed, or cancelled bags.</td>
</tr>
<tr class="odd">
<td><strong>DATUP</strong></td>
<td>Data Update (DATUP). Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out VA custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the production and pre-production centralized MOCHA databases at Austin and Philadelphia.</td>
</tr>
<tr class="even">
<td><strong>Default Answer</strong></td>
<td>The most common answer, predefined by the system to save time and keystrokes for the user. The default answer appears before the two slash marks (//) and can be selected by the user by pressing &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="odd">
<td><strong>Dispense Drug</strong></td>
<td>The Dispense Drug is pulled from the DRUG file (#50) and usually has the strength attached to it (e.g., Acetaminophen 325 mg). Usually, the name alone without a strength attached is the Orderable Item name.</td>
</tr>
<tr class="even">
<td><strong>Delivery Times</strong></td>
<td>The time(s) when IV orders are delivered to the wards.</td>
</tr>
<tr class="odd">
<td><strong>Dosage Ordered</strong></td>
<td>After the user has selected the drug during order entry, the dosage ordered prompt is displayed.</td>
</tr>
<tr class="even">
<td><strong>DRUG ELECTROLYTES file</strong></td>
<td>File #50.4. This file contains the names of anions/cations, and their concentration units.</td>
</tr>
<tr class="odd">
<td><strong>DRUG file</strong></td>
<td>File #50. This file holds the information related to each drug that can be used to fill a prescription.</td>
</tr>
<tr class="even">
<td><strong>Duration</strong></td>
<td>The length of time between the Start Date/Time and Stop Date/Time for an Inpatient Medications order. The default duration for the order can be specified by an ordering clinician in CPRS by using the Complex Dose tab in the Inpatient Medications ordering dialog.</td>
</tr>
<tr class="odd">
<td><p><strong>Electrolyte</strong></p>
<p><strong>Enhanced Order Checks</strong></p></td>
<td><p>An additive that disassociates into ions (charged particles) when placed in solution.</p>
<p>Drug–Drug Interaction, Duplicate Therapy, and Dosing order checks that are executed utilizing FDB’s MedKnowledge Framework APIs and database.</p></td>
</tr>
<tr class="even">
<td><strong>Entry By</strong></td>
<td>The name of the user who entered the Unit Dose or IV order into the computer.</td>
</tr>
<tr class="odd">
<td><strong>Hospital Supplied Self Med</strong></td>
<td>Self medication, which is to be supplied by the Medical Center’s pharmacy. Hospital supplied self med is only prompted for if the user answers Yes to the SELF MED: prompt during order entry.</td>
</tr>
<tr class="even">
<td><strong>Hyperalimentation (Hyperal)</strong></td>
<td>Long term feeding of a protein-carbohydrate solution. Electrolytes, fats, trace elements, and vitamins can be added. Since this solution generally provides all necessary nutrients, it is commonly referred to as Total Parenteral Nutrition (TPN). A hyperal is composed of many additives in two or more solutions. When the labels print, they show the individual electrolytes in the hyperal order.</td>
</tr>
<tr class="odd">
<td><strong>Infusion Rate</strong></td>
<td>The designated rate of flow of IV fluids into the patient.</td>
</tr>
<tr class="even">
<td><strong>INPATIENT USER PARAMETERS file</strong></td>
<td>File #53.45. This file is used to tailor various aspects of the Inpatient Medications package with regards to specific users. This file also contains fields that are used as temporary storage of data during order entry/edit.</td>
</tr>
<tr class="odd">
<td><strong>INPATIENT WARD PARAMETERS file</strong></td>
<td>File #59.6. This file is used to tailor various aspects of the Inpatient Medications package with regards to specific wards.</td>
</tr>
<tr class="even">
<td><strong>Intermittent Syringe</strong></td>
<td>A syringe type of IV that is administered periodically to the patient according to an administration schedule.</td>
</tr>
<tr class="odd">
<td><strong>Internal Order Number</strong></td>
<td>The number on the top left corner of the label of an IV bag in brackets ([ ]). This number can be used to speed up the entry of returns and destroyed IV bags.</td>
</tr>
<tr class="even">
<td><strong>IV ADDITIVES file</strong></td>
<td>File #52.6. This file contains drugs that are used as additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.</td>
</tr>
<tr class="odd">
<td><strong>IV CATEGORY file</strong></td>
<td>File #50.2. This file allows the user to create categories of drugs in order to run “tailor-made” IV cost reports for specific user-defined categories of drugs. The user can group drugs into categories.</td>
</tr>
<tr class="even">
<td><strong>IV Duration</strong></td>
<td>The duration of an order may be entered in CPRS at the IV DURATION OR TOTAL VOLUME field in the IV Fluids order dialog. The duration may be specified in terms of volume (liters or milliliters), or time (hours or days). Inpatient Medications uses this value to calculate a default stop date/time for the order at the time the order is finished.</td>
</tr>
<tr class="odd">
<td><strong>IV Label Action</strong></td>
<td><p>A prompt, requesting action on an IV label, in the form of “Action ( )”, where the valid codes are shown in the parentheses. The following codes are valid:</p>
<p>P – Print a specified number of labels now.</p>
<p>B – Bypass any more actions.</p>
<p>S – Suspend a specified number of labels for the IV room to print on demand.</p></td>
</tr>
<tr class="even">
<td><strong>IV Room Name</strong></td>
<td>The name identifying an IV distribution area.</td>
</tr>
<tr class="odd">
<td><strong>IV SOLUTIONS file</strong></td>
<td>File #52.7. This file contains drugs that are used as primary solutions in the IV room. The solution must already exist in the Drug file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.</td>
</tr>
<tr class="even">
<td><strong>IV STATS file</strong></td>
<td>File #50.8. This file contains information concerning the IV workload of the pharmacy. This file is updated each time the <em>COmpile IV Statistics</em> option is run and the data stored is used as the basis for the AMIS (IV) report.</td>
</tr>
<tr class="odd">
<td><strong>Label Device</strong></td>
<td>The device, identified by the user, on which computer-generated labels will be printed.</td>
</tr>
<tr class="even">
<td><strong>Local Possible Dosages</strong></td>
<td>Free text dosages that are associated with drugs that do not meet all of the criteria for Possible Dosages.</td>
</tr>
<tr class="odd">
<td><strong>LVP</strong></td>
<td>Large Volume Parenteral (LVP) — Admixture. A solution intended for continuous parenteral infusion, administered as a vehicle for additive(s) or for the pharmacological effect of the solution itself. It is comprised of any number of additives, including zero, in one solution. An LVP runs continuously, with another bag hung when one bottle or bag is empty.</td>
</tr>
<tr class="even">
<td><strong>Manufacturing Times</strong></td>
<td>The time(s) that designate(s) the general time when the manufacturing list will be run and IV orders prepared. This field in the <em>SIte Parameters (IV)</em> option (IV Room file (#59.5)) is for documentation only and does not affect IV processing.</td>
</tr>
<tr class="odd">
<td><strong>MEDICATION ADMINISTERING TEAM file</strong></td>
<td>File #57.7. This file contains wards, the teams used in the administration of medication to that ward, and the rooms/beds assigned to that team.</td>
</tr>
<tr class="even">
<td><strong>MEDICATION INSTRUCTION file</strong></td>
<td>File #51. This file is used by Outpatient Pharmacy and Unit Dose Special Instructions. (Not used by IV Other Print Info.) It contains the medication instruction name, expansion, and intended use.</td>
</tr>
<tr class="odd">
<td><strong>MEDICATION ROUTES file</strong></td>
<td>File #51.2. This file contains medication route names. The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.</td>
</tr>
<tr class="even">
<td><strong>Medication Routes/Abbreviations</strong></td>
<td>Route by which medication is administered (e.g., oral). The Medication Routes file (#51.2) contains the routes and abbreviations, which are selected by each VAMC. The abbreviation cannot be longer than five characters to fit on labels and the MAR. The user can add new routes and abbreviations as appropriate.</td>
</tr>
<tr class="odd">
<td><strong>Non-Formulary Drugs</strong></td>
<td>The medications that are defined as commercially available drug products not included in the VA National Formulary.</td>
</tr>
<tr class="even">
<td><strong>Non-VA Meds</strong></td>
<td>Term that encompasses any Over-the-Counter (OTC) medications, Herbal supplements, Veterans Health Administration (VHA) prescribed medications but purchased by the patient at an outside pharmacy, and medications prescribed by providers outside VHA. All Non-VA Meds must be documented in patients’ medical records.</td>
</tr>
<tr class="odd">
<td><strong>Non-Verified Orders</strong></td>
<td>Any order that has been entered in the Unit Dose or IV module that has not been verified (made active) by a nurse and/or pharmacist. Ward staff may not verify a non-verified order.</td>
</tr>
<tr class="even">
<td><strong>Orderable Item</strong></td>
<td>An Orderable Item name has no strength attached to it (e.g., Acetaminophen). The name with a strength attached to it is the Dispense Drug name (e.g., Acetaminophen 325mg).</td>
</tr>
<tr class="odd">
<td><strong>Order Check</strong></td>
<td>Order checks (drug-allergy/ADR interactions, drug-drug interactions, duplicate drug, and duplicate drug class) are performed when a new medication order is placed through either the CPRS or Inpatient Medications applications. They are also performed when medication orders are renewed, when Orderable Items are edited, or during the finishing process in Inpatient Medications. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error.</td>
</tr>
<tr class="even">
<td><strong>Order Sets</strong></td>
<td>An Order Set is a set of N pre-written orders. (N indicates the number of orders in an Order Set is variable.) Order Sets are used to expedite order entry for drugs that are dispensed to all patients in certain medical practices and procedures.</td>
</tr>
<tr class="odd">
<td><strong>Order View</strong></td>
<td>Computer option that allows the user to view detailed information related to one specific order of a patient. The order view provides basic patient information and identification of the order variables.</td>
</tr>
<tr class="even">
<td><strong>Parenteral</strong></td>
<td>Introduced by means other than the digestive track.</td>
</tr>
<tr class="odd">
<td><strong>Patient Profile</strong></td>
<td>A listing of a patient’s active and non-active Unit Dose and IV orders. The patient profile also includes basic patient information, including the patient’s name, social security number, date of birth, diagnosis, ward location, date of admission, reactions, and any pertinent remarks.</td>
</tr>
<tr class="even">
<td><strong>PECS</strong></td>
<td>Pharmacy Enterprise Customization System. A Graphical User Interface (GUI) web-based application used to research, update, maintain, and report VA customizations of the commercial-off-the-shelf (COTS) vendor database used to perform Pharmacy order checks such as drug-drug interactions, duplicate therapy, and dosing.</td>
</tr>
<tr class="odd">
<td><strong>Pending Order</strong></td>
<td>A pending order is one that has been entered by a provider through CPRS without Pharmacy or Nursing finishing the order. Once Pharmacy or Nursing has finished and verified the order, it will become active.</td>
</tr>
<tr class="even">
<td><strong>PEPS</strong></td>
<td>Pharmacy Enterprise Product System. A re-engineering of pharmacy data and its management practices developed to use a commercial off-the-shelf (COTS) drug database, currently First DataBank (FDB) MedKnowledge, to provide the latest identification and safety information on medications.</td>
</tr>
<tr class="odd">
<td><strong>Pharmacist Intervention</strong></td>
<td>A recommendation provided by a pharmacist through the Inpatient Medications system’s Intervention process acknowledging the existence of a critical drug-drug interaction and/or allergy/ADR interaction, and providing justification for its existence. There are two ways an intervention can be created, either via the Intervention Menu, or in response to Order Checks.</td>
</tr>
<tr class="even">
<td><strong>PHARMACY SYSTEM file</strong></td>
<td>File #59.7. This file contains data that pertains to the entire Pharmacy system of a medical center, and not to any one site or division.</td>
</tr>
<tr class="odd">
<td><strong>Piggyback</strong></td>
<td>Small volume parenteral solution for intermittent infusion. A piggyback is comprised of any number of additives, including zero, and one solution; the mixture is made in a small bag. The piggyback is given on a schedule (e.g., Q6H). Once the medication flows in, the piggyback is removed; another is not hung until the administration schedule calls for it.</td>
</tr>
<tr class="even">
<td><strong>Possible Dosages</strong></td>
<td>Dosages that have a numeric dosage and numeric dispense units per dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to the VA PRODUCT file (#50.68). The VA PRODUCT file (#50.68) entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.</td>
</tr>
<tr class="odd">
<td><strong>Pre-Exchange Units</strong></td>
<td>The number of actual units required for this order until the next cart exchange.</td>
</tr>
<tr class="even">
<td><strong>Primary Solution</strong></td>
<td>A solution, usually an LVP, administered as a vehicle for additive(s) or for the pharmacological effect of the solution itself. Infusion is generally continuous. An LVP or piggyback has only one solution (primary solution). A hyperal can have one or more solutions.</td>
</tr>
<tr class="odd">
<td><strong>Print Name</strong></td>
<td>Drug generic name as it is to appear on pertinent IV output, such as labels and reports. Volume or Strength is not part of the print name.</td>
</tr>
<tr class="even">
<td><strong>Print Name{2}</strong></td>
<td>Field used to record the additives contained in a commercially purchased premixed solution.</td>
</tr>
<tr class="odd">
<td><strong>Profile</strong></td>
<td>The patient profile shows a patient’s orders. The Long profile includes all the patient’s orders, sorted by status: active, non-verified, pending, and non-active. The Short profile will exclude the patient’s discontinued and expired orders.</td>
</tr>
<tr class="even">
<td><strong>Prompt</strong></td>
<td>A point at which the system questions the user and waits for a response.</td>
</tr>
<tr class="odd">
<td><strong>Provider</strong></td>
<td>Another term for the physician/clinician involved in the prescription of an IV or Unit Dose order for a patient.</td>
</tr>
<tr class="even">
<td><strong>Provider Override Reason</strong></td>
<td>A reason supplied by a provider through the CPRS system, acknowledging a critical drug-drug interaction and/or allergy/ADR interaction and providing justification for its existence.</td>
</tr>
<tr class="odd">
<td><strong>PSJI MGR</strong></td>
<td>The name of the <em>key</em> that allows access to the supervisor functions necessary to run the IV medications software. Usually given to the Inpatient Medications package coordinator.</td>
</tr>
<tr class="even">
<td><strong>PSJI PHARM TECH</strong></td>
<td>The name of the <em>key</em> that must be assigned to pharmacy technicians using the IV module. This key allows the technician to finish IV orders, but not verify them.</td>
</tr>
<tr class="odd">
<td><strong>PSJI PURGE</strong></td>
<td>The <em>key</em> that must be assigned to individuals allowed to purge expired IV orders. This person will most likely be the IV application coordinator.</td>
</tr>
<tr class="even">
<td><strong>PSJI RNFINISH</strong></td>
<td>The name of the <em>key</em> that is given to a user to allow the finishing of IV orders. This user must also be a holder of the PSJ RNURSE key.</td>
</tr>
<tr class="odd">
<td><strong>PSJI USR1</strong></td>
<td>The <em>primary menu option</em> that may be assigned to nurses.</td>
</tr>
<tr class="even">
<td><strong>PSJI USR2</strong></td>
<td>The <em>primary menu option</em> that may be assigned to technicians.</td>
</tr>
<tr class="odd">
<td><strong>PSJU MGR</strong></td>
<td>The name of the <em>primary menu</em> and of the <em>key</em> that must be assigned to the pharmacy package coordinators and supervisors using the Unit Dose Medications module.</td>
</tr>
<tr class="even">
<td><strong>PSJU PL</strong></td>
<td>The name of the <em>key</em> that must be assigned to anyone using the Pick List options.</td>
</tr>
<tr class="odd">
<td><strong>PSJ PHARM TECH</strong></td>
<td>The name of the <em>key</em> that must be assigned to pharmacy technicians using the Unit Dose Medications module.</td>
</tr>
<tr class="even">
<td><strong>PSJ RNFINISH</strong></td>
<td>The name of the <em>key</em> that is given to a user to allow the finishing of a Unit Dose order. This user must also be a holder of the PSJ RNURSE key.</td>
</tr>
<tr class="odd">
<td><strong>PSJ RNURSE</strong></td>
<td>The name of the <em>key</em> that must be assigned to nurses using the Unit Dose Medications module.</td>
</tr>
<tr class="even">
<td><strong>PSJ RPHARM</strong></td>
<td>The name of the <em>key</em> that must be assigned to a pharmacist to use the Unit Dose Medications module. If the package coordinator is also a pharmacist he/she must also be given this key.</td>
</tr>
<tr class="odd">
<td><strong>Quick Code</strong></td>
<td>An abbreviated form of the drug generic name (from one to ten characters) for IV orders. One of the three drug fields on which lookup is done to locate a drug. Print name and synonym are the other two. Use of quick codes will speed up order entry, etc.</td>
</tr>
<tr class="even">
<td><strong>Report Device</strong></td>
<td>The device, identified by the user, on which computer-generated reports selected by the user will be printed.</td>
</tr>
<tr class="odd">
<td><strong>Schedule</strong></td>
<td>The frequency of administration of a medication (e.g., QID, QDAILY, QAM, STAT, Q4H).</td>
</tr>
<tr class="even">
<td><strong>Schedule Type</strong></td>
<td>Codes include: <strong>O</strong> - one time (i.e., STAT - only once), <strong>P</strong> - PRN (as needed; no set administration times). <strong>C</strong>- continuous (given continuously for the life of the order; usually with set administration times). <strong>R</strong> - fill on request (used for items that are not automatically put in the cart - but are filled on the nurse’s request. These can be multidose items (e.g., eye wash, kept for use by one patient and is filled on request when the supply is exhausted)). And <strong>OC</strong> - on call (one time with no specific time to be given, i.e., 1/2 hour before surgery).</td>
</tr>
<tr class="odd">
<td><strong>Scheduled IV Order</strong></td>
<td>Inpatient Medications IV order having an administration schedule. This includes the following IV Types: IV Piggyback, Intermittent Syringe, IV Piggyback Chemotherapy, and Intermittent Syringe Chemotherapy.</td>
</tr>
<tr class="even">
<td><strong>Self Med</strong></td>
<td>Medication that is to be administered by the patient to himself.</td>
</tr>
<tr class="odd">
<td><strong>Standard Schedule</strong></td>
<td>Standard medication administration schedules stored in the Administration Schedule file (#51.1).</td>
</tr>
<tr class="even">
<td><strong>Start Date/Time</strong></td>
<td>The date and time an order is to begin.</td>
</tr>
<tr class="odd">
<td><strong>Status</strong></td>
<td><strong>A</strong> - active, <strong>E</strong> - expired, <strong>R</strong> - renewed (or reinstated), <strong>D</strong> - discontinued, <strong>H</strong> - on hold, <strong>I</strong> - incomplete, or <strong>N</strong> - non-verified, <strong>U</strong> – unreleased, <strong>P</strong> – pending, <strong>O</strong> – on call, , DP- discontinued by provider through CPRS, DE- discontinued due to edit via backdoor pharmacy (unit Dose orders only), DF- discontinued due to edit by provider through CPRS, DD- auto discontinued due to death, DA- auto discontinued due to patient movements, HP- placed on hold due to provider CPRS, <strong>DE</strong> – discontinued edit, <strong>RE</strong> – reinstated, <strong>DR</strong> – discontinued renewal.</td>
</tr>
<tr class="even">
<td><strong>Stop Date/Time</strong></td>
<td>The date and time an order is to expire.</td>
</tr>
<tr class="odd">
<td><strong>Stop Order Notices</strong></td>
<td>A list of patient medications that are about to expire and may require action.</td>
</tr>
<tr class="even">
<td><strong>Syringe</strong></td>
<td>Type of IV that uses a syringe rather than a bottle or bag. The method of infusion for a syringe-type IV may be continuous or intermittent.</td>
</tr>
<tr class="odd">
<td><strong>Syringe Size</strong></td>
<td>The syringe size is the capacity or volume of a particular syringe. The size of a syringe is usually measured in number of cubic centimeters (ccs).</td>
</tr>
<tr class="even">
<td><strong>TPN</strong></td>
<td>Total Parenteral Nutrition. The intravenous administration of the total nutrient requirements of the patient. The term TPN is also used to mean the solution compounded to provide those requirements.</td>
</tr>
<tr class="odd">
<td><strong>Units per Dose</strong></td>
<td>The number of Units (tablets, capsules, etc.) to be dispensed as a Dose for an order. Fractional numbers will be accepted.</td>
</tr>
<tr class="even">
<td><strong>VA Drug Class Code</strong></td>
<td>A drug classification system used by VA that separates drugs into different categories based upon their characteristics. IV cost reports can be run for VA Drug Class Codes.</td>
</tr>
<tr class="odd">
<td><strong>VDL</strong></td>
<td>Virtual Due List. This is a Graphical User Interface (GUI) application used by the nurses when administering medications.</td>
</tr>
<tr class="even">
<td><strong>Ward Group</strong></td>
<td>A ward group indicates inpatient nursing units (wards) that have been defined as a group within Inpatient Medications to facilitate processing of orders.</td>
</tr>
<tr class="odd">
<td><strong>WARD GROUP file</strong></td>
<td>File #57.5. This file contains the name of the ward group, and the wards included in that group. The grouping is necessary for the pick list to be run for specific carts and ward groups.</td>
</tr>
<tr class="even">
<td><strong>Ward Group Name</strong></td>
<td>A field in the WARD GROUP file (#57.5) used to assign an arbitrary name to a group of wards for the pick list and medication cart.</td>
</tr>
<tr class="odd">
<td><strong>WARD LOCATION file</strong></td>
<td>File #42. This file contains all of the facility ward locations and their related data, i.e., Operating beds, Bed section, etc. The wards are created/edited using the <em>Ward Definition</em> option of the ADT module.</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 14 Day MAR Report, 171, 172

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

14 Day MAR Report Example, 174

2

24 Hour MAR Report, 157, 159, 160, 167

24 Hour MAR Report Example, 160

7

7 Day MAR Report, 165, 166, 167

7 Day MAR Report Example, 168

A

Abbreviated Order Entry, 30, 31

Action Area, 6, 15, 23, 27, 28, 71, 72

Action Profile \#1 Report, 177

Action Profile \#1 Report Example, 178

Action Profile \#2 Report Example, 180

Activity Log, 72, 76, 84, 92, 103, 106

Activity Log Example, 93

Additive, 46, 47, 108, 194, 201, 205, 206, 209

Administration Schedule, 50, 82, 201

Administration Team, 158, 165, 171, 177

Administration Time, 100

Administration Times, 50, 75, 101, 158, 165, 171

Admixture, 46, 47, 201, 202, 203, 204, 206

Adverse Reaction Tracking (ART) Package, 59

Align Labels (Unit Dose), 192

Align Labels (Unit Dose) Example, 192

Asterisk, 71, 74, 76

Auto-Verify, 81

B

BCMA, 1, 50, 71

BCMA Virtual Due List (VDL), 81

C

Check Drug Interactions, 139

Chemotherapy, 46, 202, 203

Clinic, 16, 17, 158, 165, 171, 193

Clinic Group, 16, 17, 158, 165, 171, 193

Clinic Location, 55

Clinic Orders, 132

Clinical Reminder Order Checks, 129

Complex Orders, 90

Active Complex Order, 68

Non-Verified Complex Order, 68

Pending Complex Order, 67

CPRS, 1, 16, 43, 50, 54, 71, 82, 84, 93, 101, 103, 107, 108, 201, 204, 208

CPRS Med Order, 51

CPRS Order Checks Introduction, 196

CPRS Order Checks: How They Work, 196

CPRS Provider Overrides, 31

Critical Drug-Drug Interaction, 204

critical drug-drug interactions, 60

CWAD Indicator, 6

D

Default Start Date Calculation

Default Start Date Calculation = NOW, 177

Default Stop Date, 29, 54, 143, 154, 155

Default Stop Date/Time, 54

Detailed Allergy/ADR List, 59, 200

Discontinue All of a Patient’s Orders, 104

Discontinue an Order, 72

Discontinue an Order Example, 72

Discontinuing a Pending Renewal, 92

Dispense Drug, 30, 31, 32, 46, 47, 74, 75, 83, 84, 101, 102, 108, 204, 207

Dispense Drug Look-Up, 194

Dispense Drug Look-Up Example, 194

Dispense Log, 92

DONE Order, 51

Dosage Ordered, 30, 31, 32, 33, 75, 205

Dosing Order Checks, 139

Drug File, 30, 102, 194

Drug Prompt, 30

Drug Text Indicator, 31, 46, 47

E

Edit an Order, 73

Edit an Order Example, 74, 75

Edit Inpatient User Parameters, 67, 154

Edit Patient’s Default Stop Date, 154

Enter/Edit Allergy/ADR Data, 59

Error Information, 198

Error Messages, 198

Expected First Dose, 101

F

Finish an Order, 93

Finish an Order With a Duration Example, 99

Finish an Order Without a Duration Example, 97

Flag an Order, 103

Flag an Order Example, 103

Free Text Dosage, 186

G

Glossary, 200

H

Header Area, 6

Hidden Actions, 4, 7

History Log, 74, 92

Hold, 3, 14, 25, 59, 84, 85, 104, 105, 201

Hold All of a Patient’s Orders, 104

Hold All of a Patient’s Orders Example, 105

Hold an Order, 84

Hold an Order Example, 84

Take All of a Patient’s Orders Off of Hold Example, 105

Hyperal, 46, 47, 203, 205, 209

I

Infusion Rate, 47, 49

Inpatient Medication Orders for Outpatients, 54, 165, 171, 177

Inpatient Narrative, 28

Inpatient Order Entry, 3, 6, 7, 13, 14, 25, 29, 46, 64, 102

Inpatient Order Entry Example, 25

Inpatient Profile, 105, 193

Inpatient Profile Example, 106

Inpatient Stop Order Notices Example, 187

Inpatient User Parameters File, 67, 82

Inpatient Ward Parameters, 42, 53

Inquiries Menu, 194

Inquiries Menu Example, 194

Inquiries Options, 194

Intermittent Syringe, 50

Intervention, 60, 202

Intervention Menu, 59, 60, 200

Delete an Intervention Example, 62

Edit an Intervention Example, 61

New Intervention Example, 60

Print an Intervention Example, 63

View an Intervention Example, 62

Introduction, 1

IRMS, 46

IV Additives, 54, 205

IV Duration, 206

IV Flag, 102

IV Room, 25, 53, 105, 201, 205, 206

IV Solution, 47, 201

IV Type, 46, 47, 54

L

Label Print/Reprint, 193

Large Volume Parenteral (LVP), 46, 206

List Area, 6

List Manager, 5, 6, 7, 28, 72

Local Possible Dosages, 32, 206

Local Possible Dosages Example, 32

M

Maintenance Options, 154

Medication Administration Records (MARs), 1

Medication Routes, 49, 102, 207

Menu Option, 3

Menu Tree, xi

Message Window, 6, 74

N

Nature of Order, 31, 42, 54

<u>New Order Entry</u>, 29

New IV Order Entry Example, 55

Non-Formulary Status, 31, 47, 74, 83, 84, 101

Non-Verified Order, 6

Non-Verified/Pending Orders, 13, 15, 16, 24, 29, 64

Non-Verified/Pending Orders Example, 16

O

OCI, 9

OCXCACHE, 196

Order Actions, 72

Order check

data caching, 196

OCXCACHE, 196

XTMP, 196

Order Check, 30, 107, 108, 207

Drug-Allergy Interactions, 30, 107, 108

Drug-Drug Interactions, 30, 107, 108

Duplicate Class, 30, 107, 108

Duplicate Drug, 107, 108

Order Check Data Caching, 196

Order Check/Interventions, 9

Order Checks/Interventions (OCI) indicator, 31

Order Entry, 9, 13, 14, 29, 30, 105

Order Locks, 13

Order Options, 13

Order Set, 30, 31

Order Validation Checks, 135

Orderable Item, 30, 31, 46, 47, 49, 74, 75, 83, 84, 101, 155, 204, 207

Orientation, 3

Other Print Info, 50, 51

Output Options, 156

P

Parenteral, 46, 201, 206, 208

Patient Action, 15, 23, 27, 28

Patient Actions, 28

Patient Information, 6, 15, 27, 48, 69, 200

Patient Information Example, 69

Patient Information Screen Example, 15, 27

Patient Lock, 13, 29

Patient Record Update, 28

Patient Record Update Example, 28

Pharmacist Intervention, 208

Pick List, 1, 81, 210, 211

Pick List Menu Example, 143

Piggyback, 46, 47, 50, 202, 203, 208, 209

Possible Dosages, 32, 206, 209

Possible Dosages Example, 32

Priority, 6, 17, 18, 21, 65

Provider, 31, 42

Provider Comments, 51

PSJ RNFINISH Key, 17, 24, 93, 103

PSJ RNURSE Key, 3, 23, 210

PSJ RPHARM Key, 59

PSJI RNFINISH Key, 17, 24, 93

PSJU PL Key, 154

Q

Quick Code, 46, 194, 206

R

Regular Order Entry, 30

Renew an Order, 86

Active Orders, 88

Complex Orders, 90

Discontinued Orders, 88

Expired Continuous IV Orders, 89

Expired Scheduled IV Orders, 89

Expired Unit Dose Orders, 88

Viewing Renewed Orders, 91

Renewing Orders

with CPRS Overrides/Pharmacist Interventions, 86

Requested Start Date/Time, 99, 101

Requested Stop Date/Time, 99

Revision History, i

S

Schedule, 50, 167, 173, 195, 205, 206, 208

Screen Prompts, 3

Screen Title, 6

Select Action, 6, 7, 15, 23, 27

Select Allergy, 59

Select Order, 66, 70, 200

Select Order Example, 70

Self Med, 42

Short Profile Example, 18

Solution, 46, 47, 108, 194, 201, 205, 206, 208, 209, 211

Speed Actions, 104

Speed Discontinue, 201

Speed Finish, 201

Speed Renew, 201

Speed Verify, 201

Speed Discontinue, 104

Speed Finish, 94, 104

Speed Renew, 104

Speed Verify, 104

Standard Schedules, 195

Standard Schedules Example, 195

Start Date/Time, 53, 72, 75, 211

Stop Date/Time, 42, 54, 55, 72, 74, 75, 92, 94, 211

Syringe, 46, 202, 203, 205, 211

T

Table of Contents, ix

Topic Oriented Section, xi

U

Unit Dose Medications, 3, 13, 14, 154, 194

Unit Dose Order Entry Profile, 9

Units Per Dose, 33

V

VA Drug Class Code, 194

VA FORM 10-1158, 178, 180

VA FORM 10-2970, 167

VA FORM 10-5568d, 167

VDL, 51, 81, 211

Verify an Order, 81

Verify an Order Example, 84

View Profile, 15, 27, 64, 200

View Profile Example, 64

VistA, 29, 204

Volume, 46

W

Ward, 17, 105, 158, 177, 193

Ward Group, 16, 17, 105, 158, 165, 171, 177, 193, 211

Ward Group Sort

^OTHER, 17, 177

Ward Stock, 167, 173

X

XTMP, 196

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Inpatient Medications Nurse's User Manual (PSJ*5*447)

### Intervention Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-nurse-s-user-manual-psj-5-447/033.png) This option is only available to those users who hold the PSJ RPHARM key.

The Intervention Menu action allows entry of new interventions and existing interventions to be edited, deleted, viewed, or printed. Each kind of intervention will be discussed and an example will follow.

![](inpatient-medications-nurse-s-user-manual-psj-5-447/034.png)Note: Interventions can also be dynamically created in response to Order Checks for critical drug-drug interactions, allergy/ADRs, high pharmacogenomic and dosing order checks.. Refer to [Section 4.9 Order Checks](#p123).

If a change is made to an intervention associated to an inpatient order made in response to critical drug-drug and/or allergy/ADR, the changes are reflected and displayed whenever interventions display.

New interventions entered via the Intervention Menu are at the patient level and are not associated with a particular order. Consequently, new entries made through this menu are not reflected in the OCI listing, the BCMA Display Order detail report, and do not cause highlighting in BCMA.

New: This option is used to add an entry into the APSP INTERVENTION file.

Figure 44: Example: New Intervention

Patient Information Feb 11, 2011@11:17:44 Page: 1 of 1

BCMAPATIENT,FIVE Ward: 3 NORTH

PID: 000-00-5555 Room-Bed: 1-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 09/16/45 (65) Att: Psj,Test Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE TrSp: Medical Observati Admitted: 12/05/08

Dx: FLUID IN LUNGS Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: NKA

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI Delete Pharmacy Intervention PO Print Pharmacy Intervention

ED Edit Pharmacy Intervention VP View Pharmacy Intervention

NE Enter Pharmacy Intervention

Select Item(s): NE Enter Pharmacy Intervention

Select APSP INTERVENTION INTERVENTION DATE: T FEB 11, 2011

Are you adding 'FEB 11, 2011' as a new APSP INTERVENTION (the 526TH)? No// Y

(Yes)

APSP INTERVENTION PATIENT: PRETST,PATTHREE 8-1-61 000009677

NO NSC VETERAN

Combat Vet Status: ELIGIBLE End Date: 02/12/2015

APSP INTERVENTION DRUG: CIMETIDINE 200MG TAB GA301

PROVIDER: PHARMACIST,LINDA J LP

INSTITUTED BY: PHARMACY// PHARMACY

INTERVENTION: ?

Answer with APSP INTERVENTION TYPE, or NUMBER

Do you want the entire 22-Entry APSP INTERVENTION TYPE List? N (No)

INTERVENTION: ALLERGY

RECOMMENDATION: NO CHANGE

WAS PROVIDER CONTACTED: NO NO

RECOMMENDATION ACCEPTED: Y YES

FINANCIAL COST:

REASON FOR INTERVENTION:

No existing text

Edit? NO//

ACTION TAKEN:

No existing text

Edit? NO//

CLINICAL IMPACT:

No existing text

Edit? NO//

FINANCIAL IMPACT:

No existing text

Edit? NO//

Select APSP INTERVENTION INTERVENTION DATE:

Edit: This option is used to edit an existing entry in the APSP INTERVENTION file.

Figure 45: Example: Edit an Intervention

Patient Information Feb 11, 2011@11:52:02 Page: 1 of 1

PRETST,PATTHREE Ward:

PID: 000-00-9677 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/01/61 (49) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted:

Dx: Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: NKA

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI   Delete Pharmacy Intervention       PO   Print Pharmacy Intervention

ED   Edit Pharmacy Intervention         VP   View Pharmacy Intervention

NE   Enter Pharmacy Intervention

Select Item(s): ED   Edit Pharmacy Intervention 

Select INTERVENTION:T SEP 22, 2000 PRETST,PATTHREE WARFARIN 10MG

INTERVENTION DATE: SEP 22,2000// \<Enter\>

PATIENT: PRETST,PATTHREE// \<Enter\>

PROVIDER: PSJPROVIDER,ONE // \<Enter\>

PHARMACIST: PSJNURSE,ONE // \<Enter\>

DRUG: WARFARIN 10MG// \<Enter\>

INSTITUTED BY: PHARMACY// \<Enter\>

INTERVENTION: ALLERGY// \<Enter\>

OTHER FOR INTERVENTION:

1\>

RECOMMENDATION: NO CHANGE// \<Enter\>

OTHER FOR RECOMMENDATION:

1\>

WAS PROVIDER CONTACTED: NO// \<Enter\>

PROVIDER CONTACTED:

RECOMMENDATION ACCEPTED: YES// \<Enter\>

AGREE WITH PROVIDER: \<Enter\>

FINANCIAL COST:

REASON FOR INTERVENTION:

No existing text

Edit? NO//

ACTION TAKEN:

No existing text

Edit? NO//

CLINICAL IMPACT:

No existing text

Edit? NO//

FINANCIAL IMPACT:

No existing text

Edit? NO//

Delete: This option is used to delete an entry from the APSP INTERVENTION file. The nurse may only delete an entry that was entered on the same day.

> Figure 46: Example: Delete an Intervention

Patient Information Feb 11, 2011@11:52:02 Page: 1 of 1

PRETST,PATTHREE Ward:

PID: 000-00-9677 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/01/61 (49) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted:

Dx: Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: NKA

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI Delete Pharmacy Intervention PO Print Pharmacy Intervention

ED Edit Pharmacy Intervention VP View Pharmacy Intervention

NE Enter Pharmacy Intervention

Select Item(s): de Delete Pharmacy Intervention

You may only delete entries entered on the current day.

Select APSP INTERVENTION INTERVENTION DATE: t FEB 11, 2011

1 2-11-2011 PRETST,PATTHREE CIMETIDINE 200MG TAB

2 2-11-2011 PRETST,PATTHREE CIMETIDINE 200MG TAB

CHOOSE 1-2: 1 2-11-2011 PRETST,PATTHREE CIMETIDINE 200MG TAB

SURE YOU WANT TO DELETE THE ENTIRE ENTRY? y YES

Select APSP INTERVENTION INTERVENTION DATE:

View: This option is used to display Pharmacy Interventions in a captioned format.

Figure 47: Example: View an Intervention

Patient Information Feb 11, 2011@11:52:02 Page: 1 of 1

PRETST,PATTHREE Ward:

PID: 000-00-9677 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/01/61 (49) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted:

Dx: Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

Allergies/Reactions: NKA

Inpatient Narrative:

Outpatient Narrative:

Enter ?? for more actions

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI Delete Pharmacy Intervention PO Print Pharmacy Intervention

ED Edit Pharmacy Intervention VP View Pharmacy Intervention

NE Enter Pharmacy Intervention

Select Item(s): VP View Pharmacy Intervention

Select APSP INTERVENTION INTERVENTION DATE: T FEB 11, 2011 PRETST,PATTHR

EE CIMETIDINE 200MG TAB

ANOTHER ONE:

INTERVENTION DATE: FEB 11, 2011 PATIENT: PRETST,PATTHREE

PROVIDER: PROVIDER,LINDA J PHARMACIST: PHARMACIST,CHRIS

DRUG: CIMETIDINE 200MG TAB INSTITUTED BY: PHARMACY

INTERVENTION: ALLERGY RECOMMENDATION: NO CHANGE

WAS PROVIDER CONTACTED: NO RECOMMENDATION ACCEPTED: YES

Select APSP INTERVENTION INTERVENTION DATE:

- Print: This option is used to obtain a captioned printout of Pharmacy Interventions for a certain date range. It will print out on normal width paper and can be queued to print at a later time.

Figure 48: Example: Print an Intervention

Select Unit Dose Medications Option: Inpatient Order Entry

Select PATIENT: BCMA,EIGHTEEN-PATIENT 666-33-0018 04/07/35 7A GEN MED

Patient Information Mar 16, 2011@12:37:20 Page: 1 of 1

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

CrCL: 0.8(est.) (CREAT: 122mg/dL 8/26/96) BSA (m2): 2.15

--------------------------------------------------------------------------------

Allergies - Verified: AMPICILLIN, PENICILLIN, STRAWBERRIES

Non-Verified:

Adverse Reactions:

Inpatient Narrative:

Outpatient Narrative:

----------Enter ?? for more actions---------------------------------------------

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile// IN Intervention Menu

--- Intervention Menu ---

DI Delete Pharmacy Intervention PO Print Pharmacy Intervention

ED Edit Pharmacy Intervention VP View Pharmacy Intervention

NE Enter Pharmacy Intervention

Select Item(s): PO Print Pharmacy Intervention

\* Previous selection: INTERVENTION DATE from Jun 1,2010

START WITH INTERVENTION DATE: Jun 1,2010// T-1 (MAR 15, 2011)

GO TO INTERVENTION DATE: LAST// T (MAR 16, 2011)

DEVICE: home;80;9999 COMPUTER ROOM

PHARMACY INTERVENTION LISTING MAR 16,2011 12:37 PAGE 1

--------------------------------------------------------------------------------

INTERVENTION: CRITICAL DRUG INTERACTION

INTERVENTION DATE: MAR 16,2011 PATIENT: BCMA,EIGHTEEN-PATIENT

PROVIDER: PROVIDER,ONE PHARMACIST: PHARMACIST,TWO

DRUG: INDINAVIR SULFATE 400MG CAP INSTITUTED BY: PHARMACY

RECOMMENDATION: NO CHANGE

WAS PROVIDER CONTACTED: RECOMMENDATION ACCEPTED:

PROVIDER CONTACTED:

INTERVENTION DATE: MAR 16,2011 PATIENT: BCMA,EIGHTEEN-PATIENT

PROVIDER: PROVIDER,ONE PHARMACIST: PHARMACIST,TWO

DRUG: SIMVASTATIN 20MG TAB INSTITUTED BY: PHARMACY

RECOMMENDATION: NO CHANGE

WAS PROVIDER CONTACTED: RECOMMENDATION ACCEPTED:

PROVIDER CONTACTED:

----------------------------

SUBTOTAL 0

SUBCOUNT 2

----------------------------

TOTAL 0

COUNT 2

Patient Information Mar 16, 2011@12:37:57 Page: 1 of 1

BCMA,EIGHTEEN-PATIENT Ward: 7A GEN A

PID: 666-33-0018 Room-Bed: Ht(cm): 175.26 (12/15/08)

DOB: 04/07/35 (75) Wt(kg): 100.00 (12/15/08)

Sex: FEMALE Admitted: 01/31/02

Dx: UPSET Last transferred: 06/04/10

CrCL: 0.8(est.) (CREAT: 122mg/dL 8/26/96) BSA (m2): 2.15

--------------------------------------------------------------------------------

Allergies - Verified: AMPICILLIN, PENICILLIN, STRAWBERRIES

Non-Verified:

Adverse Reactions:

Inpatient Narrative:

Outpatient Narrative:

----------Enter ?? for more actions---------------------------------------------

PU Patient Record Update NO New Order Entry

DA Detailed Allergy/ADR List IN Intervention Menu

VP View Profile CM New Clinic Medication Entry

Select Action: View Profile//

### Allergy Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Medications (Unit Dose and IV) order entry process with check for adverse allergy/ADR reactions (conditions by which the user will get new order checks).

Drug allergy interactions will be either critical or significant. If the Dispense Drug selected is identified as having an interaction with one of the patient’s allergies, the allergy the drug interacts with will be displayed.

Please see Appendix A or the Adverse Reaction Tracking UserManual or Adverse Reaction Tracking Technical Manual for more information.

### CPRS Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In CPRS, Order Checks occur by evaluating a requested order against existing patient data. Most order checks are processed via the CPRS Expert System. A few are processed within the Pharmacy, Allergy Tracking System, and Order Entry packages. Order Checks are a real-time process that occurs during the ordering session and is driven by responses entered by the ordering provider. Order Check messages are displayed interactively in the ordering session.

Order Checks review existing data and current events to produce a relevant message, which is presented to patient caregivers. Order Checks use the CPRS Expert System (OCX namespace), to define logical expressions for this evaluation and message creation. In addition to the expert system Order Checks have some hard-coded algorithms. For example, the drug-drug interaction order check is made via an entry point in the pharmacy package whereas Renal Functions for Patients Over 65 is defined as a rule in the CPRS Expert System.

<span id="_Toc206054211" class="anchor"></span>Figure 86: CPRS Order Check: Aminoglycoside Ordered

> Trigger: Ordering session completion.

> Mechanism: For each medication order placed during this ordering session, the CPRS Expert System requests the pharmacy package to determine if the medication belongs to the VA Drug Class ‘Aminoglycosides’. If so, the patient’s most recent BUN results are used to calculate the creatinine clearance then OERR is notified and the warning message is displayed.

> \[Note: The creatinine clearance value displayed in some order check messages is an estimate based on adjusted body weight if patient height is \> 60 inches. Approved by the CPRS Clinical Workgroup 8/11/04, it is based on a modified Cockcroft-Gault formula and was installed with patch OR\*3\*221.

> For more information: <http://www.ascp.com/public/pubs/tcp/1999/jan/cockcroft.shtml>

> CrCl (male) = (140 - age) x (adj body weight\* in kg)

> --------------------------------------

> (serum creatinine) x 72

> \* If patient height is not greater than 60 inches, actual body weight is used.

> CrCl (female) = 0.85 x CrCl (male)

> To calculate adjusted body weight, the following equations are used:

> Ideal body weight (IBW) = 50 kg x (for men) or 45 kg x (for women) + 2.3 x (height in inches - 60)

> Adjusted body weight (Adj. BW) if the ratio of actual BW/IBW \> 1.3 = (0.3 x (Actual BW - IBW)) + IBW

> Adjusted body weight if the ratio of actual BW/IBW is not \> 1.3 = IBW or Actual BW (whichever is less)\]

> Message: Aminoglycoside - est. CrCl: \<value calculated from most recent serum creatinine\>. (CREAT: \<result\> BUN: \<result\>).

> Danger Lvl: This order check is exported with a High clinical danger level.

<span id="_Toc206054212" class="anchor"></span>Figure 87: CPRS Order Check: Dangerous Meds for Patients \>64

> DANGEROUS MEDS FOR PT \> 64 – Yes

> This is based on the BEERS list. This order check only checks for three drugs: Amitriptyline, Chlorpropamide and Dipyridamole. The workgroup felt that the list of drugs should be expanded. A request can be sent to CPRS for this.

> Trigger: Acceptance of pharmacy orderable items amitriptyline, chlorpropamide or dipyridamole.

> Mechanism: The CPRS Expert System determines if the patient is greater than 64 years old. It then checks the orderable item of the medication ordered to determine if it is mapped as a local term to the national term DANGEROUS MEDS FOR PTS \> 64.

> Message: If the orderable item text contains AMITRIPTYLINE this message is displayed:

> Patient is \<age\>. Amitriptyline can cause cognitive impairment and loss of balance in older patients. Consider other antidepressant medications on formulary.

> If the orderable item text contains CHLORPROPAMIDE this message is displayed:

> Patient is \<age\>. Older patients may experience hypoglycemia with Chlorpropamide due do its long duration and variable renal secretion. They may also be at increased risk for Chlorpropamide-induced SIADH.

> If the orderable item text contains DIPYRIDAMOLE this message is displayed:

> Patient is \<age\>. Older patients can experience adverse reactions at high doses of Dipyridamole (e.g., headache, dizziness, syncope, GI intolerance.) There is also questionable efficacy at lower doses.

> Danger Lvl: This order check is exported with a High clinical danger level.

<span id="_Toc206054213" class="anchor"></span>Figure 88: CPRS Order Check: Glucophage Lab Results

> Glucophage-Lab Results Interactions

> Trigger: Selection of a Pharmacy orderable item.

> Mechanism: The CPRS Expert System checks the pharmacy orderable item’s local text (from the Dispense Drug file \[#50\]) to determine if it contains “glucophage” or “metformin”. The expert system next searches for a serum creatinine result within the past x number of days as determined by parameter ORK GLUCOPHAGE CREATININE. If the patient’s creatinine result was greater than 1.5 or does not exist, OE/RR is notified and the warning message is displayed.

> Message: Metformin– no serum creatinine within past \<x\> days. else:

> Metformin – Creatinine results: \<creatinine greater than 1.5 w/in past \<x\> days\> Danger Lvl: This order check is exported with a High clinical danger level

### Clinical Reminder Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Clinical Reminder Order Checks (CROCs) functionality. Order Checks now include the ability to view Clinical Reminders (prior to the display of Enhanced Drug-Drug interactions). Reminders are used to aid clinicians in performing tasks to fulfill Clinical Practice Guidelines and periodic procedures or education as needed for patients.

Clinical Reminder Order Checks will have a severity of low, medium, or high. CROCs with a severity of high require an intervention to be entered. An intervention is optional for a severity of low and medium.

For an IV order, if there are multiple drugs that are involved in a CROC, one will have to log an intervention for each drug.

Only the CPRS orderable item and drug level CROCs are displayed through the Pharmacy Backdoor.

Example: Clinical Reminder Order Check with severity of Medium

Now processing Clinical Reminder Order Checks. Please wait ...

\*\*\* Clinical Reminder Order Check \| Severity: MEDIUM \*\*\*

Potentially Teratogenic Medication (FDA Category D or C)

Concern has been raised about use of this medication during pregnancy.

1\) Pregnancy status should be determined. Discuss use of this medication on the

context of risks to the mother and child of untreated disease. Potential

benefits may warrant use of the drug in pregnant women despite risks.

2\) The patient must be provided contraceptive counseling on potential risk vs.

benefit of taking this medication if she were to become pregnant.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The 'Teratogenic Medications' Order Check will display for female patients

between the ages of 12 and 50, except those with a known exclusion criterion

(e.g., hysterectomy), or those with a documented IUD placement that is more

recent than a documented IUD removal.

----------------------------------------------------------------------------

Do you want to Intervene? N// NO

> **NOTE:** For a Clinical Reminder Order Check with a low or medium severity, the entry of an intervention is optional. For a Clinical Reminder Order Check with a high severity, the user <u>must</u> enter an intervention before continuing.

Example: Clinical Reminder Order Check with severity of High.

Now processing Clinical Reminder Order Checks. Please wait ...

============================================================================

\*\*\* Clinical Reminder Order Check \| Severity: HIGH \*\*\*

Patient is greater than 64yo and on Statins

This alert will display for patients greater than 64yo and who are taking a

STATIN drug.

----------------------------------------------------------------------------

Do you want to Continue? Y// ES

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

For LOVASTATIN 40MG TAB

PROVIDER: INPATIENT

1 INPATIENT-MEDS,NURSE NURSE

2 INPATIENT-MEDS,PHARMACIST PI

3 INPATIENT-MEDS,PROVIDER PROV

CHOOSE 1-3: 3 INPATIENT-MEDS,PROVIDER PROV

RECOMMENDATION: CHANGE DRUG

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N// O

### Enhanced Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Duplicate Therapy Order Checks

Inpatient orders are checked for therapeutic duplication with drugs within similar therapeutic classes. If orders share similar classes with the order being processed, they will be included in the list within the therapeutic duplication warning. If 2 orders are entered for the same drug, such as one scheduled and one PRN order, they are checked and displayed as a Duplicate Therapy warning.

The user will have the opportunity to discontinue duplicate therapy order(s) after the duplicate therapy warning is displayed as long as at least one of the orders listed is an inpatient order and that order is not being worked on (i.e., copy action taken).

Each First Databank therapeutic class is assigned a duplication allowance value. The duplication allowance value indicates how many duplications (drug pairs) are considered appropriate before a warning is generated. If the number of duplicate therapy drug pairs exceeds the duplication allowance value, a warning is displayed. In the example below, if the patient is already receiving orders containing a Dispense Drug in the same class as one of the Dispense Drugs in the new order, the orders containing the drug in that class are displayed. Inpatient duplicate orders of this kind are displayed in a numbered list. The user is first asked whether to continue the current order. If the user selects to continue the order then the user is prompted with which, if any, numbered Inpatient duplicate orders to discontinue. The user may enter a range of numbers from the numbered list of duplicate orders or bypass the prompt by selecting \<Enter\> and continue with the order. Entry of orders with duplicate drugs of the same class will be allowed.

Table: Duplication Allowance

![](inpatient-medications-nurse-s-user-manual-psj-5-447/068.png)

- ![](inpatient-medications-nurse-s-user-manual-psj-5-447/069.png)Note: Inpatient Medications order checks display orders with the same
- drug as Duplicate Therapy instead of Duplicate Drug.

Therapeutic Duplication - IV and Unit Dose clinic order therapeutic duplications display in the same format as drug interactions. See examples below:

Example: Unit Dose Duplicate Therapy Order Check:

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

POTASSIUM CHLORIDE 30 MEQ

Clinic Order: POTASSIUM CHLORIDE 10MEQ TAB (PENDING)

Schedule: BID

Dosage: 20MEQ

Requested Start Date: NOV 20, 2012@17:00

Stop Date: \*\*\*\*\*\*\*\*

Class(es) Involved in Therapeutic Duplication(s): Potassium

Example: IV Duplicate Therapy Order Check:

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

CEFAZOLIN 1 GM

Clinic Order: CEFAZOLIN 2 GM (PENDING)

Solution(s): 5% DEXTROSE 50 ML

Order Date: NOV 20, 2012@11:01

Start Date: \*\*\*\*\*\*\*\*

Stop Date: \*\*\*\*\*\*\*\*

Clinic Order: CEFAZOLIN SOD 1GM INJ (EXPIRED)

Solution(s): 5% DEXTROSE 50 ML

Start Date: OCT 24, 2012@16:44

Stop Date: OCT 25, 2012@24:00

Class(es) Involved in Therapeutic Duplication(s): Beta-Lactams,

Cephalosporins, Cephalosporins - 1st Generation

#### Drug/Drug Interaction Order Checks

Drug Interaction Order Checks are performed when new orders are processed and compare prospective drug to the existing profile drugs. For Drug Interaction Order Checks, local outpatient orders include all active, non-verified, pending and Non-VA medication orders. Remote outpatient orders include all active orders. For Duplicate Therapy Order Checks, local outpatient orders include all active, expired (Exp Date + 120), discontinued (Cancel Date + Days Supply +7), non-verified, pending and Non-VA Medication orders. Remote outpatient orders include all active, expired (Exp Date +30) and discontinued (Cancel Date +30).

Inpatient medication orders include all active, non-verified, pending orders for both IV and Unit Dose modules.

Clinic Orders participate in both Drug Interaction Order Checks and Duplicate Therapy Order Checks for Inpatient and Outpatient medication orders.

For Significant Drug Interaction Order Checks, a pharmacy intervention is optional. Critical Drug Interaction Order Checks require a pharmacy intervention during processing. See examples below:

Example: Critical Drug Interaction – Pharmacy Intervention required

================================================================================

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with WARFARIN 2MG TABS:

CIPROFLOXACIN TAB C 08/13 08/18 A

Give: 500MG PO BID

Concurrent use of quinolones may be associated with an increase in

hypoprothrombinemic effects of anticoagulants, which may result in an

increased risk of bleeding.

================================================================================

Display Professional Interaction Monograph(s)? NO//

Do you want to Continue with WARFARIN 2MG TABS? NO// YES

Now creating Pharmacy Intervention

PROVIDER: PSJPROVIDER, ONE

RECOMMENDATION: ORDER LAB TEST

Example: Significant Drug Interaction

Now Processing Enhanced Order Checks! Please wait...

================================================================================

This patient is receiving the following order(s) that have a SIGNFICANT Drug Interaction

with ASPIRIN 325MG TAB:

WARFARIN TAB C 08/15 08/30 A

Give: 2.5MG PO QPM

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

For Drug Interaction Order Checks, a profession interaction monograph is available to display during order processing through backdoor pharmacy. See example below:

Example: Significant Drug Interaction for Unit Dose Order – Display Monograph

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

================================================================================

This patient is receiving the following order(s) that have a SIGNFICANT Drug Interaction

with ASPIRIN 325MG TAB:

WARFARIN TAB C 08/15 08/30 A

Give: 2.5MG PO QPM

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

================================================================================

Display Professional Interaction Monograph? No// Y es

Device: Home// \<Home would print to screen, or a specific device could be specified\>

Professional Monograph

Drug Interaction with WARFARIN AND ASPIRIN

This information is generalized and not intended as specific medical advice. Consult your healthcare professional before taking or discontinuing any drug or commencing any course of treatment.

MONOGRAPH TITLE: Anticoagulants/Salicylates

SEVERITY LEVEL: 2-Severe Interaction: Action is required to reduce the risk of severe adverse interaction.

MECHANISM OF ACTION: Multiple processes are involved: 1) Salicylate doses greater than 3 gm daily decrease plasma prothrombin levels. 2) Salicylates may also displace anticoagulants from plasma protein binding sites. 3) Salicylates impair platelet function, resulting in prolonged bleeding time. 4) Salicylates may cause gastrointestinal bleeding due to irritation.

CLINICAL EFFECTS: The concurrent use of anticoagulants and salicylates may result in increased INR values and increase the risk of bleeding.

PREDISPOSING FACTORS: None determined.

PATIENT MANAGEMENT: Avoid concomitant administration of these drugs. If salicylate use is necessary, monitor prothrombin time, bleeding time or INR values closely. When possible, the administration of a non-aspirin salicylate would be preferable.

DISCUSSION: This interaction has been reported between aspirin and warfarin and between aspirin and dicumarol. Diflunisal, sodium salicylate, and topical methyl salicylate have been shown to interact with anticoagulants as well. Based on the proposed mechanisms, other salicylates would be expected to interact with anticoagulants as well. The time of highest risk for a coumarin-type drug interaction is when the precipitant drug is initiated, altered, or discontinued.

REFERENCES:

1.Quick AJ, Clesceri L. Influence of acetylsalicylic acid and salicylamide on the coagulation of blood. J Pharmacol Exp Ther 1960;128:95-8.

2.Watson RM, Pierson RN, Jr. Effect of anticoagulant therapy upon aspirin-induced gastrointestinal bleeding. Circulation 1961 Sep;24:613-6.

3.Barrow MV, Quick DT, Cunningham RW. Salicylate hypoprothrombinemia in rheumatoid arthritis with liver disease. Report of two cases. Arch Intern Med 1967 Nov;120(5):620-4.

4.Weiss HJ, Aledort LM, Kochwa S. The effect of salicylates on the hemostatic properties of platelets in man. J Clin Invest 1968 Sep; 47(9):2169-80.

5.Udall JA. Drug interference with warfarin therapy. Clin Med 1970 Aug; 77:20-5.

6.Fausa O. Salicylate-induced hypoprothrombinemia. A report of four cases. Acta Med Scand 1970 Nov;188(5):403-8.

7.Zucker MB, Peterson J. Effect of acetylsalicylic acid, other nonsteroidal anti-inflammatory agents, and dipyridamole on human blood platelets. J Lab Clin Med 1970 Jul;76(1):66-75.

8.O'Reilly RA, Sahud MA, Aggeler PM. Impact of aspirin and chlorthalidone on the pharmacodynamics of oral anticoagulant drugs in man. Ann N Y Acad Sci 1971 Jul 6;179:173-86.

9.Dale J, Myhre E, Loew D. Bleeding during acetylsalicylic acid and anticoagulant therapy in patients with reduced platelet reactivity after aortic valve replacement. Am Heart J 1980 Jun;99(6):746-52.

10.Donaldson DR, Sreeharan N, Crow MJ, Rajah SM. Assessment of the interaction of warfarin with aspirin and dipyridamole. Thromb Haemost 1982 Feb 26;47(1):77.

11.Chesebro JH, Fuster V, Elveback LR, McGoon DC, Pluth JR, Puga FJ, Wallace RB, Danielson GK, Orszulak TA, Piehler JM, Schaff HV. Trial of combined warfarin plus dipyridamole or aspirin therapy in prosthetic heart valve replacement: danger of aspirin compared with dipyridamole. Am J Cardiol 1983 May 15;51(9):1537-41.

12.Chow WH, Cheung KL, Ling HM, See T. Potentiation of warfarin anticoagulation by topical methylsalicylate ointment. J R Soc Med 1989 Aug;82(8):501-2.

13.Meade TW, Roderick PJ, Brennan PJ, Wilkes HC, Kelleher CC. Extra-cranial bleeding and other symptoms due to low dose aspirin and low intensity oral anticoagulation. Thromb Haemost 1992 Jul 6;68(1):1-6.

Copyright \<2010\> First DataBank, Inc.

#### Dosing Order Checks

MOCHA v2.0 implemented the first increment of dosage checks and introduced the Maximum Single Dose Check for simple and complex orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.1b implemented the second increment of dosage checks and introduced the Max Daily Dose Check for simple orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.0 and MOCHA v2.1b use the same interface to First Databank (FDB) as MOCHA v1.0. See example below:

Example: Dosing order checks – Frequency, Max Single & Max Daily Dose warnings

Max Daily Dose Check could not be performed for Drug: SIMVASTATIN 10MG

TAB

Reason(s): Invalid or Undefined Frequency

SIMVASTATIN 10MG TAB: Single dose of 160 milligrams exceeds the maximum

single dose of 80 milligrams.

General dosing range for SIMVASTATIN 10MG TAB (ORAL): 5 milligram/day to

40 milligram/day. Maximum daily dose is 80 milligram/day.

![](inpatient-medications-nurse-s-user-manual-psj-5-447/070.png) Please refer to the Dosing Order Checks User Manual for a detailed description of dosing order checks.

#### Pharmacogenomic Order Checks

Mocha 3.0 implemented pharmacogenomic (PGx) order checks, providing additional guidance for selecting suitable drug therapies based on genomic factors and indicators. This assists clinicians in delivering safe and effective treatment options tailored to individual patients

In order to perform the Pharmacogenomic Order Checks, the system first retrieves the patient’s pharmacogenomic lab results which are stored in the Health Data Repository (HDR), regardless of where they were drawn. Results are retrieved at the time the order is accepted in CPRS or being processed in VistA. If the HDR server or the MOCHA server are not able to connect, a corresponding message will be displayed to the user.

Pharmacogenomic order checks have two levels of severity.

- High order checks require an override by the provider and an intervention by the pharmacist
- Medium order checks have provider overrides or interventions that are optional.

At the time of entering or processing the order, the user can display ‘Additional Information’ to see the order check content as well as the sources and references returned from the vendor.

Only VA Products that are marked as PGx Eligible in the National Drug File are eligible for PGx Order checks.

PGx order checks are not rechecked when the order is edited, unless the dispense drug field or dosage related fields are edited.

A screened message will appear when the PGx order check cannot be completed due to uninterpretable gene or phenotype results, even though the vendor database contains genomic findings and PGx guidance exists for the prospective drug.

An email notification to the PBM PGx CDS group is sent when an HDR-retrieved gene or phenotype cannot be mapped to the FDB gene database. The Pharmacogenomic Email Log (File \#51.29) will store the pertinent information. If an order is entered or processed for that specific patient with the same unresolved gene or unresolved or null phenotype greater than 7 days from the last email, another email and log will be sent.

Suppression of Pharmacogenomic Order Checks may occur at the following 2 levels:

- Profile suppression occurs if the ingredient for the prospective order is set to PGx Eligible and PGx Suppress, the severity of the PGx order check is Medium (Informational), and the patient has an active outpatient or inpatient order (Unit Dose, Clinic Meds, IV or Clinic Infusion) for prospective Inpatient orders, or an active outpatient order for prospective outpatient orders, for a drug with the same ingredient as the prospective drug. NOTE: Non-VA medications are NOT included for suppression logic.
- Severity and PGx Action Category Suppression occurs if the severity of the order check is Medium (Informational) and the PGx Action Category is one of the following:
  - 9 – No therapy adjustment needed
  - 14 – No therapy recommendation
  - 2 – Await genotype test result
  - 4 – Consider genotype test or prescribe alternative
  - 13 – Consider genotype test
  - 5 – Order genotype test or prescribe alternative
- ![](inpatient-medications-nurse-s-user-manual-psj-5-447/071.png) Please refer to the MOCHA FAQs for more detailed information.

Pharmacogenomic HIGH Order Check:

GENOMIC FINDING: CYP2D6 poor metabolizer

IMPACTED MEDICATION: AMITRIPTYLINE 100MG

ACTION: For conditions requiring higher starting doses (e.g., 25 mg/day or

higher) such as depression, consider alternate drug with less dependence on

CYP2D6 metabolism (e.g., citalopram, sertraline). If amitriptyline use is

warranted, consider a 50% reduction of the standard starting dose and use

therapeutic drug monitoring to guide subsequent dose adjustment.

MONITORING: If using amitriptyline, monitor for symptom improvement as well as

adverse reactions (e.g., anticholinergic, central nervous system, and cardiac

effects).

For more details on VA National Pharmacogenomics Program go to:

[<https://bit.ly/VA-PGx>](https://bit.ly/VA-PGx)

Display Additional Information on Pharmacogenomic Order Check(s)? NO// YES

DEVICE: HOME// Linux Telnet /SSh

Pharmacogenomics Detailed Information

GENOMIC FINDING: CYP2D6 poor metabolizer

IMPACTED MEDICATION: AMITRIPTYLINE 100MG

SEVERITY LEVEL: HIGH

EVIDENCE RATINGS:

SOURCE: Clinical Pharmacogenetics Implementation Consortium (CPIC)

(1,2)

RATING: Strong

SOURCE: Dutch Pharmacogenetics Working Group (DPWG) (3)

RATING: 3, A

ACTION:

For conditions requiring higher starting doses (e.g., 25 mg/day or higher)

such as depression, consider alternate drug with less dependence on CYP2D6

metabolism (e.g., citalopram, sertraline). If amitriptyline use is

warranted, consider a 50% reduction of the standard starting dose and use

therapeutic drug monitoring to guide subsequent dose adjustment.

Type \<Enter\> to continue or '^' to exit:

RATIONALE:

Greatly reduced amitriptyline metabolism results in higher concentrations of

active drug and increased risk of adverse reactions.

MONITORING:

If using amitriptyline, monitor for symptom improvement as well as adverse

reactions (e.g., anticholinergic, central nervous system, and cardiac

effects).

CITATIONS:

\(1\) Hicks JK, Sangkuhl K, Swen JJ, et al. Clinical Pharmacogenetics

Implementation Consortium Guideline (CPIC) for CYP2D6 and CYP2C19 Genotypes

and Dosing of Tricyclic Antidepressants: 2016 update. Clinical Pharmacology

and Therapeutics. 2017 Jul 01; 102 (1): 37-44. Available from

[<https://cpicpgx.org/content/guideline/publication/TCA/2016/TCA_2016.pdf>](https://cpicpgx.org/content/guideline/publication/TCA/2016/TCA_2016.pdf)

\(2\) Clinical Pharmacogenetics Implementation Consortium (CPIC). CPIC Guideline

for Tricyclic Antidepressants and CYP2D6 and CYP2C19. Available from

[<https://cpicpgx.org/guidelines/guideline-for-tricyclic-antidepressants-and-cyp2d>](https://cpicpgx.org/guidelines/guideline-for-tricyclic-antidepressants-and-cyp2d)

6-and-cyp2c19/

\(3\) Dutch Pharmacogenetics Working Group. Pharmacogenomics guidelines.

Type \<Enter\> to continue or '^' to exit:

Available from

[<https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf>](https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf)

First Databank database updated on 07/02/2025.

Do you want to Continue with AMITRIPTYLINE 100MG? NO// Y

Example: PGx MEDIUM Order Check, no intervention required

Pharmacogenomic MEDIUM Order Check:

GENOMIC FINDING: CYP2D6 intermediate metabolizer

IMPACTED MEDICATION: TRAMADOL HCL 100MG TAB

ACTION: Initiate therapy with usual recommended starting dose. If there is

poor therapeutic response, consider alternative analgesic such as morphine or

a nonopioid. Codeine and hydrocodone are also affected by CYP2D6 polymorphisms

and may not be suitable alternatives.

MONITORING: Monitor for analgesic response.

For more details on VA National Pharmacogenomics Program go to:

https://bit.ly/VA-PGx

Display Additional Information on Pharmacogenomic Order Check(s)? NO//

Do you want to Intervene with TRAMADOL HCL 100MG TAB ? NO//

Press Return to continue...

## Check Pharmacogenomic Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS CHECK PGX INTERACTION\]

The Check Pharmacogenomic Interaction option allows a user to check for pharmacogenomic interactions for one or more drugs and may include genes, genotypes, and phenotypes. The user can also select a specific patient and use the patient’s pharmacogenomic information stored in HDR to perform the order check. Additionally, the user may choose to use the patient’s current medication profiles or select different medications. This option is located on the Unit Dose Medications \[PSJU MGR\] Menu and the IV \[PSJI MGR\] Menu.

<span id="Figure_108" class="anchor"></span>Figure 92: Example: Check PGx Interaction (same for IV \[PSJI MGR\] Menu)

(PGx) Order Check is performed when verifying a non-verified IV medication order for an identified drug that participates in genetic testing. The following set of figures is an example of a Non-Verified IV Medication with a PGx Order Check.

> Select OPTION NAME: CHECK PHARMACOGENOMIC INTERACTION PSS CHECK PGX INTERACTION

> Check Pharmacogenomic Interaction

> PHARMACOGENOMIC (PGx) TEST OPTION

> Do you want to use a specific patient? Y// NO

> Drug selection \*\*\*Only PGx-eligible drugs are available for selection\*\*\*

> Do you want to see the PGx eligible drugs? N// YES

> ABACAVIR SULFATE 300MG TAB

> ACETAMINOPHEN AND CODEINE 30MG

> ALLOPURINOL 100MG S.T.

> ALLOPURINOL 300MG S.T.

> ALLOPURINOL 300MG, 30'S

> ALLOPURINOL NA 500MG/VIL INJ

> AMIKACIN SULFATE 1GM INJ.

> AMIKACIN SULFATE 500MG INJ

> AMITRIPTYLINE 100MG

> AMITRIPTYLINE 10MG TAB

> AMITRIPTYLINE 25MG

> Press Return to continue, '^' to exit list: ^

> Select DRUG: ABACAVIR SULFATE 300MG TAB AM800

> VA PRODUCT: ABACAVIR SO4 300MG TAB

> GCNSEQNO: 40964

> Select Another DRUG:

> Drugs Selected:

> ABACAVIR SULFATE 300MG TAB

> Press Return to continue:

> Select Gene: HLA-B 57:01

> Select Another Gene:

> Genes Selected:

> HLA-B 57:01

> Press Return to continue:

> Genotype selection for HLA-B 57:01 (optional):

> Enter HLA-B 57:01 Activity Score:

> Phenotype selection for HLA-B 57:01

> 1\) HIGH RISK

> 2\) INDETERMINANT ACTIVITY

> 3\) LOW RISK

> Select HLA-B 57:01 Phenotype: (1-3): 1 HIGH RISK

> Gene: HLA-B 57:01

> Genotype:

> Activity Score:

> Phenotype: HIGH RISK

> Inputs:

> Drug: ABACAVIR SULFATE 300MG TAB

> VA Product: ABACAVIR SO4 300MG TAB

> GCNSEQNO: 40964

> Gene: HLA-B 57:01

> Genotype:

> Activity Score:

> Phenotype: HIGH RISK

> Pharmacogenomic HIGH Order Check:

> GENOMIC FINDING: HLA-B \*57:01 positive

> IMPACTED MEDICATION: ABACAVIR SULFATE 300MG TAB

> ACTION: Avoid abacavir use and choose alternative antiretroviral. Alternative

> nucelos(t)ide reverse transcriptase inhibitors (NRTIs) include tenofovir

> disoproxil fumarate, tenofovir alafenamide, lamivudine and emtricitabine.

> RATIONALE: HLA-B\*57:01 carriers are at high risk for severe hypersensitivity

> reaction.

> MONITORING: Abacavir is contraindicated in patients who have the HLA-B\*57:01

> allele.

> For more details on VA National Pharmacogenomics Program go to:

> https://bit.ly/VA-PGx

> Display Additional Information on Pharmacogenomic Order Check(s)? NO// YES

> DEVICE: HOME// Linux Telnet /SSh

> Pharmacogenomics Detailed Information

> GENOMIC FINDING: HLA-B \*57:01 positive

> IMPACTED MEDICATION: ABACAVIR SULFATE 300MG TAB

> SEVERITY LEVEL: HIGH

> EVIDENCE RATINGS:

> SOURCE: Clinical Pharmacogenetics Implementation Consortium (CPIC)

> (1,2)

> RATING: Strong

> SOURCE: Dutch Pharmacogenetics Working Group (DPWG) (3)

> RATING: 4, E

> SOURCE: FDA Table of Pharmacogenetic Associations (4)

> RATING: Therapeutic management recommendation

> SOURCE: Manufacturer prescribing information (5)

> RATING: not applicable

> ACTION:

> Avoid abacavir use and choose alternative antiretroviral. Alternative

> nucelos(t)ide reverse transcriptase inhibitors (NRTIs) include tenofovir

> disoproxil fumarate, tenofovir alafenamide, lamivudine and emtricitabine.

> RATIONALE:

> HLA-B\*57:01 carriers are at high risk for severe hypersensitivity reaction.

> MONITORING:

> Abacavir is contraindicated in patients who have the HLA-B\*57:01 allele.

> CITATIONS:

> \(1\) Martin MA, Klein TE, Dong BJ, et al. Clinical Pharmacogenetics

> Implementation Consortium Guidelines for HLA-B Genotype and Abacavir Dosing.

> Clinical Pharmacology and Therapeutics. 2012 Apr; 91 (4): 734-738. Available

> from

> https://cpicpgx.org/content/guideline/publication/abacavir/2012/22378157.pdf

> \(2\) Clinical Pharmacogenetics Implementation Consortium (CPIC). CPIC Guideline

> for Abacavir and HLA-B. Available from

> https://cpicpgx.org/guidelines/guideline-for-abacavir-and-hla-b/

> \(3\) Dutch Pharmacogenetics Working Group. Pharmacogenomics guidelines.

> Available from

> https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf

> \(4\) FDA Table of Pharmacogenetic Associations. Available from

> https://www.fda.gov/medical-devices/precision-medicine/table-pharmacogenetic-ass

> ociations

> \(5\) Ziagen \[package insert\]. Research Triangle Park, NC. ViiV HealthCare. 2020

> Nov. Available from

> https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/020977s035,020978s038l

> bl.pdf

> First Databank database updated on 07/02/2025.

### From: Inpatient Medications Nurse's User Manual (updated PSJ*5*399)

## Discontinue All of a Patient’s Orders\[PSJU CA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Discontinue All of a Patient’s Orders* option allows a nurse to discontinue all of a patient’s orders. Also, it allows a ward clerk to mark all of a patient’s orders for discontinuation. If the ALLOW USER TO D/C ORDERS parameter is turned on to take action on active orders, then the ward clerk will also be able to discontinue orders. This ALLOW USER TO D/C ORDERS parameter is set using the *Inpatient User Parameter’s Edit* option under the *PARameter’s Edit Menu* option, which is under the *Supervisor’s Menu* option.

This option is then used to discontinue the selected orders. If a non-verified or pending order is discontinued, it is deleted completely from the system.

## Edit Inpatient User Parameters\[PSJ UEUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Edit Inpatient User Parameters* option allows users to edit various Inpatient User parameters. The prompts that will be encountered are as follows:

- “PRINT PROFILE IN ORDER ENTRY:”

> Enter YES for the opportunity to print a profile after entering Unit Dose orders for a patient.

- “INPATIENT PROFILE ORDER SORT:”

This is the sort order in which the Inpatient Profile will show inpatient orders. The options will be sorted either by medication or by start date of order. Entering the words “Medication Name” (or the number 0) will show the orders within schedule type (continuous, one-time, and then PRN) and then alphabetically by drug name. Entering the words “Start Date of Order” (or the number 1) will show the order chronologically by start date, with the most recent dates showing first and then by schedule type (continuous, one-time, and then PRN).

![](inpatient-medications-nurse-s-user-manual-updated-psj-5-399/083.png)Note: The Profile first shows orders by status (active, non-verified, and then non-active).

- “LABEL PRINTER:”

Enter the device on which labels are to be printed.

- “USE WARD LABEL SETTINGS:”

> Enter YES to have the labels print on the printer designated for the <u>ward</u> instead of the printer designated for the <u>pharmacy</u>.
