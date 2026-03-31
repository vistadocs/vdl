---
consolidated_title: "user manual change pages"
app_code: PSS
doc_type: UM
master_source: "PSS*1*159 User Manual Change Pages"
master_pub_date: September 1997
consolidated_from: 13 versions
prior_versions:
  - "PSS*1*137 User Manual Change Pages"
  - "PSS*1*140 User Manual Change Pages"
  - "PSS*1*141 User Manual Change Pages"
  - "PSS*1*142 User Manual Change Pages"
  - "PSS*1*143 User Manual Change Pages"
  - "PSS*1*146 User Manual Change Pages"
  - "PSS*1*147 User Manual Change Pages"
  - "PSS*1*153 User Manual Change Pages"
  - "PSS*1*155 User Manual Change Pages"
  - "PSS*1*163 User Manual Change Pages"
  - "PSS*1*172 User Manual Change Pages"
  - "PSS*1*174 User Manual Change Pages"
---

#### ![](pss-1-159-user-manual-change-pages/001.png) 

PHARMACY DATA MANAGEMENT

> USER MANUAL

> Version 1.0

> September 1997

# (Revised December 2011)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(Revised December 2011)](#revised-december-2011)
- [Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.](#each-time-this-manual-is-updated-the-title-page-lists-the-new-revised-date-and-this-page-describes-the-changes-if-the-revised-pages-column-lists-all-replace-the-existing-manual-with-the-reissued-manual-if-the-revised-pages-column-lists-individual-entries-eg-25-32-either-update-the-existing-manual-with-the-change-pages-document-or-print-the-entire-new-manual)
  - [(This side left blank for two-sided copying)](#this-side-left-blank-for-two-sided-copying)
    - [Example 3: Drug Enter/Edit Editing Local Possible Dosages and Orderable Item (continued)](#example-3-drug-enteredit-editing-local-possible-dosages-and-orderable-item-continued)
    - [Example 3: Drug Enter/Edit Editing Local Possible Dosages and Orderable Item (continued)](#example-3-drug-enteredit-editing-local-possible-dosages-and-orderable-item-continued-1)
  - [(This side left blank for two-sided copying)](#this-side-left-blank-for-two-sided-copying-1)
    - [Example 4: Drug Enter/Edit Editing Non-VA Medications](#example-4-drug-enteredit-editing-non-va-medications)
    - [Example 4: Drug Enter/Edit Editing Non-VA Medications (continued)](#example-4-drug-enteredit-editing-non-va-medications-continued)
  - [(This side left blank for two-sided copying)](#this-side-left-blank-for-two-sided-copying-2)
    - [Example 4: Reactivated Standard Medication Route](#example-4-reactivated-standard-medication-route)
- [Patch PSS\1\153 added the ability to include printing the POSSIBLE MED ROUTES multiple. If the DEFAULT MED ROUTE field is populated then that value will be returned as the default value. If the DEFAULT MED ROUTE field is not populated and the POSSIBLE MED ROUTES multiple is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field is set to “NO,” the single entry will be returned as the default value. If the DEFAULT MED ROUTE field is not populated and the POSSIBLE MED ROUTES multiple is populated with more than one entry and the USE DOSAGE FORM MED ROUTE LIST field is set to “NO,” no value will be returned as the default value. The med routes selection list in CPRS will be populated with all the medication routes associated with the orderable item’s dosage form if the USE DOSAGE FORM MED ROUTE LIST field is set to "YES," otherwise it will be populated from the POSSIBLE MED ROUTES multiple. These conditions are shown in the following table and examples are provided.](#patch-pss1153-added-the-ability-to-include-printing-the-possible-med-routes-multiple-if-the-default-med-route-field-is-populated-then-that-value-will-be-returned-as-the-default-value-if-the-default-med-route-field-is-not-populated-and-the-possible-med-routes-multiple-is-populated-with-a-single-entry-and-the-use-dosage-form-med-route-list-field-is-set-to-no-the-single-entry-will-be-returned-as-the-default-value-if-the-default-med-route-field-is-not-populated-and-the-possible-med-routes-multiple-is-populated-with-more-than-one-entry-and-the-use-dosage-form-med-route-list-field-is-set-to-no-no-value-will-be-returned-as-the-default-value-the-med-routes-selection-list-in-cprs-will-be-populated-with-all-the-medication-routes-associated-with-the-orderable-items-dosage-form-if-the-use-dosage-form-med-route-list-field-is-set-to-yes-otherwise-it-will-be-populated-from-the-possible-med-routes-multiple-these-conditions-are-shown-in-the-following-table-and-examples-are-provided)
    - [Example 1: Default Med Route for Orderable Item Report](#example-1-default-med-route-for-orderable-item-report)
- [The Edit Orderable Items \[PSS EDIT ORDERABLE ITEMS\] option allows the user to enter and edit data in the PHARMACY ORDERABLE ITEM file (#50.7). If a Pharmacy Orderable Item Drug Text Entry is identified at the “OI-DRUG-TEXT” prompt, it will be viewable during medication order entry processes through CPRS, Outpatient Pharmacy, and Inpatient Medications. Pharmacy Orderable Item defaults can be entered for selected fields. These defaults will be displayed to the user during the medication order entry processes for all applications through which medication orders can be entered.](#the-edit-orderable-items-pss-edit-orderable-items-option-allows-the-user-to-enter-and-edit-data-in-the-pharmacy-orderable-item-file-507-if-a-pharmacy-orderable-item-drug-text-entry-is-identified-at-the-oi-drug-text-prompt-it-will-be-viewable-during-medication-order-entry-processes-through-cprs-outpatient-pharmacy-and-inpatient-medications-pharmacy-orderable-item-defaults-can-be-entered-for-selected-fields-these-defaults-will-be-displayed-to-the-user-during-the-medication-order-entry-processes-for-all-applications-through-which-medication-orders-can-be-entered)
- [The default medication route for CPRS will be derived from the DEFAULT MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated or from the POSSIBLE MED ROUTES multiple (#50.711) of the PHARMACY ORDERABLE ITEM file](#the-default-medication-route-for-cprs-will-be-derived-from-the-default-med-route-field-06-of-the-pharmacy-orderable-item-file-507-if-it-is-populated-or-from-the-possible-med-routes-multiple-50711-of-the-pharmacy-orderable-item-file)
- [Additional med routes for selection in the drop-down list in CPRS will be derived from the POSSIBLE MED ROUTES multiple (#50.711) if the USE DOSAGE FORM MED ROUTE](#additional-med-routes-for-selection-in-the-drop-down-list-in-cprs-will-be-derived-from-the-possible-med-routes-multiple-50711-if-the-use-dosage-form-med-route)
- [The method of deriving the appropriate medication routes listed above will be for Inpatient Medications unit dose orders, IV Fluids orders, and Outpatient Pharmacy orders entered via CPRS orders dialog.](#the-method-of-deriving-the-appropriate-medication-routes-listed-above-will-be-for-inpatient-medications-unit-dose-orders-iv-fluids-orders-and-outpatient-pharmacy-orders-entered-via-cprs-orders-dialog)
    - [Example 1: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “NO”](#example-1-edit-orderable-items-with-use-dosage-form-med-route-list-set-to-no)
    - [Example 2: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “NO” and there are no Default Med Route nor Possible Med Routes](#example-2-edit-orderable-items-with-use-dosage-form-med-route-list-set-to-no-and-there-are-no-default-med-route-nor-possible-med-routes)
    - [Example 3: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “YES”](#example-3-edit-orderable-items-with-use-dosage-form-med-route-list-set-to-yes)
- [If the orderable item being edited is matched to any dispense drugs that are in VA drug classes IM100 through IM900, an additional prompt will appear to permit mapping for the orderable item to an associated immunization file entry. This feature is introduced with the Immunizations Documentation by BCMA application in patches PSS\1\141 and PSB\3\47.](#if-the-orderable-item-being-edited-is-matched-to-any-dispense-drugs-that-are-in-va-drug-classes-im100-through-im900-an-additional-prompt-will-appear-to-permit-mapping-for-the-orderable-item-to-an-associated-immunization-file-entry-this-feature-is-introduced-with-the-immunizations-documentation-by-bcma-application-in-patches-pss1141-and-psb347)
    - [Example: Editing Immunization-Related Pharmacy Orderable Items](#example-editing-immunization-related-pharmacy-orderable-items)
> Department of Veterans Affairs Product Development

# Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/11</td>
<td><blockquote>
<p>i, ii, iii, 38-40b, 62d-64d</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*159</p>
</blockquote></td>
<td><p>Updated screens</p>
<p>Updated the Edit Orderable Items option for the default medication route</p>
<p>Due to data being moved, pages 62e and 62f have been removed <mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/11</td>
<td><blockquote>
<p>i-iii, 101- 101b,</p>
<p>102</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*163</p>
</blockquote></td>
<td><p>Updated the Schedule/Reschedule Check PEPS Interface section</p>
<ul>
<li><p>Updated overview of Schedule/Reschedule Check PEPS Interface</p></li>
<li><p>Updated the Schedule/Reschedule Check PEPS Interface example</p></li>
<li><p>Added a warning regarding the DEVICE FOR QUEUED JOB OUTPUT field</p></li>
<li><p>Added a blank page for two-sided copying</p></li>
</ul>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/11</td>
<td><blockquote>
<p>i-iii, 3-4b, 7-16b, 44d-j, 114, 118,</p>
<p>121, 129, 137,</p>
<p>204-206</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*155</p>
</blockquote></td>
<td><p>Utilized three new fields that were added to the VA PRODUCT file (#50.68) with PSN*4*261. The fields are used during the Match/Rematch process of the <em>Drug Enter/Edit</em> [PSS DRUG ENTER/EDIT] and the <em>Enter/Edit Dosages</em> [PSS EDIT DOSAGES] options to determine whether possible dosages should be auto-created for supra-therapeutic drugs.</p>
<p>Retired the <em>Auto Create Dosages</em> [PSS DOSAGE CONVER- SION] option and removed the option from the <em>Dosages</em> [PSS DOSAGES MANAGEMENT] menu. Updated Index.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/11</td>
<td><blockquote>
<p>i, ii, iii, added iv, v; changed 3, 4,</p>
<p>45, 46; added 46a- 46d, re-numbered all sections starting on page 87 and ending with page 106; changed page. 89; added 90e and 90f; changed 99-</p>
<p>106; added 106a-b;</p>
<p>deleted 107-112;</p>
<p>changed 151,</p>
<p>153, 154; added 154a-b; updated index;</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*136 &amp; PSS*1*117</p>
</blockquote></td>
<td><p>Besides the developer’s changes, this document incorporates the comments from <mark>REDACTED</mark> and colleagues for the PRE functionality included with patch PSS*1*117 (a combined patch with PSS*1*136).</p>
<p>Sections changed are:</p>
<ul>
<li><p>Changed overview of menu item descriptions to match application</p></li>
<li><blockquote>
<p>Changed menu item description named <em><strong>Drug Interaction Management</strong></em> to <em><strong>Order Check Management</strong></em> and changed text</p>
</blockquote></li>
<li><blockquote>
<p>Changed submenu item <em><strong>Enter/Edit Local Drug Interaction</strong></em> [PSS-INTERACTION-LOCAL-ADD] to <em><strong>Request Changes to Enhanced Order Check Databas</strong></em>e. [PSS ORDER CHECK CHANGES] and changed text.</p>
</blockquote></li>
<li><blockquote>
<p>Changed example in <em><strong>Report of Locally Entered</strong></em></p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><p><em><strong>Interactions</strong></em> option Section deleted:</p>
<ul>
<li><p>Deleted <em><strong>Enhanced Order Checks Setup Menu</strong></em> and all its sub-menu items (<em>Find Unmapped Local Medication Routes; Map Local Medication Route to Standard; Medication Route Mapping Report; Medication Route File Enter/Edit; Medication Route Mapping History Report; Request Change to Standard Medication Route; Find Unmapped Local Possible Dosages; Map Local Possible Dosages; Local</em></p></li>
<li><p><em>Possible Dosages Report; Strength Mismatch Report; Enter/Edit Dosages; Request Change to Dose Unit; Mark PreMix Solutions; IV Solution Report; Administration Schedule File Report; Medication Instruction File Report</em>)</p></li>
</ul>
<p>The deleted Enhanced Order Checks Setup Menu and its submenus is replaced by the following addition:</p>
<ul>
<li><p>Added <em><strong>PEPS Services</strong></em> menu and its submenus: <em>Check Vendor Database Link; Check PEPS Services Setup; and Schedule/Reschedule PEPS Interface</em></p></li>
</ul>
<p>Added a heading for <em><strong>Stand-Alone Menu Options</strong></em> with the description for the <em>Enable/Disable Vendor Database Link</em> option and a short description for the <em>Other Language Translation Setup</em> option.</p>
<p>Added definitions in the glossary for PECS and PEPS, and updated the index.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/11</td>
<td><blockquote>
<p>i-ii, 38, 40, 62d-f,</p>
<p>64, 64a</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*153</p>
</blockquote></td>
<td><p>Renamed the MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) to be DEFAULT MED</p>
<p>ROUTE. Provided the ability to print the POSSIBLE MED ROUTES multiple on <em>the Default Med Route For OI Report</em> [PSS DEF MED ROUTE OI RPT] option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/11</td>
<td><blockquote>
<p>i, 63</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*142</p>
</blockquote></td>
<td><p>Added functionality to denote the default med route for IV orders in the selection list in CPRS if all of the orderable items on the order have the same default med route defined. Updated TOC. Released with CPRS version 28.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/10</td>
<td><blockquote>
<p>i, iii, 84, 84a-84b, 203, 205-206</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*143</p>
</blockquote></td>
<td>Added new Schedule Validation Requirements. Updated Index. <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>02/10</td>
<td><blockquote>
<p>iii-iv, 3-4, 44a-d,</p>
<p>47-48, 61-62d, 89-</p>
<p>90b, 112, 203-206</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*147</p>
</blockquote></td>
<td><p>Described new process for requesting changes to Standard Medication Routes and the New Term Rapid Turnaround (NTRT) process;</p>
<p>Added <em>IV Additive/Solution Reports</em> menu, with suboptions <em>IV Solution Report</em> option and <em>V Additive Report</em> [PSS IV ADDITIVE REPORT] option</p>
<p>Added <em>Default Med Route for OI Report</em> option to the <em>Medication Routes Management...</em> menu<em>.</em>(this change was made but not documented with PSS*1*140)</p>
<p>Updated <em>Drug Enter/Edit</em> option to display NUMERIC DOSE and DOSE UNIT fields defined for Local Possible Dosage</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><p>Updated the Drug Enter/Edit option display to include the new ADDITIVE FREQUENCY field</p>
<p>Updated Table of Contents and Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/09</td>
<td><blockquote>
<p>i, 64a-b, 65, 65a-b, 66</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*141</p>
</blockquote></td>
<td><p>Added ASSOCIATED IMMUNIZATION field to <em>Edit Orderable Items</em> option and <em>Dispense Drug/Orderable Item Maintenance</em> option. Reorganized content within sections to accommodate new information.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/09</td>
<td><blockquote>
<p>iii-iv, 53,</p>
<p>62a-b, 63, 81, 203</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*140</p>
</blockquote></td>
<td><p>Added DEFAULT MED ROUTE FOR CPRS field and <em>Default Med Route For OI Report</em> [PSS DEF MED ROUTE OI RPT] option for the enhancement of default medication</p>
<blockquote>
<p>route being defined for an orderable item.</p>
</blockquote>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/09</td>
<td><blockquote>
<p>27-34</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*131</p>
</blockquote></td>
<td><p>Added explanations of DEA special handling code U for sensitive drug.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/09</td>
<td><blockquote>
<p>81</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*137</p>
</blockquote></td>
<td><p>Added Automate CPRS Refill field to the <em>Pharmacy System Parameters Edit</em> [PSS MGR] option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/09</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*129</p>
</blockquote></td>
<td><p>Pages renumbered to accommodate added pages. Pharmacy Reengineering (PRE) V.0.5 Pre-Release. Restructured <em>Pharmacy Data Management</em> menu:</p>
<ul>
<li><p>Grouped related options under the following new sub-menus: <em>Drug Text Management, Medication Instruction Management, Medication Routes Management,</em> and <em>Standard Schedule Management</em></p></li>
<li><p>Added temporary <em>Enhanced Order Checks Setup Menu</em></p></li>
<li><p>Added the following options: <em>Find Unmapped Local Medication Routes, Find Unmapped Local Possible Dosages, Map Local Medication Route to Standard, Map Local Possible Dosages, Mark PreMix Solutions, Request Change to Dose Unit</em>, and <em>Request Change to Standard Medication Route</em></p></li>
<li><p>Added the following reports: <em>Administration Schedule File Report, IV Solution Report, Local Possible Dosages Report, Medication Instruction File Report, Medication Route Mapping Report, Medication Route Mapping History Report,</em> and <em>Strength Mismatch Report</em></p></li>
<li><p>Updated Table of Contents, Index, and Glossary <mark>REDACTED</mark></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>09/97</td>
<td></td>
<td></td>
<td>Original Release of User Manual</td>
</tr>
</tbody>
</table>

## (This side left blank for two-sided copying)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Example 3: Drug Enter/Edit Editing Local Possible Dosages and Orderable Item (continued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Do you wish to match/rematch to NATIONAL DRUG file? No// \<Enter\> (No)

> Just a reminder...you are editing TIMOLOL MALEATE 0.5% OPH SOLN. LOCAL POSSIBLE DOSAGES:

1.  DROP PACKAGE: IO
2.  DROPS PACKAGE: IO

> Do you want to edit Local Possible Dosages? N// YES

> This drug has the following Local Possible Dosages:

1.  DROP PACKAGE: IO
2.  DROPS PACKAGE: IO

> Do you want to merge new Local Possible Dosages? Y// NO

> Strength: 0.5 Unit: %

> Select LOCAL POSSIBLE DOSAGE: 1 DROP IO

> LOCAL POSSIBLE DOSAGE: 1 DROP//\<Enter\> OTHER LANGUAGE DOSAGE NAME: \<Enter\>

> PACKAGE: Both// \<Enter\> BCMA UNITS PER DOSE: \<Enter\> DOSE UNIT: DROP(S)// \<Enter\> NUMERIC DOSE: 1// \<Enter\>

> Strength: 0.5 Unit: % Select LOCAL POSSIBLE DOSAGE: \<Enter\>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* This entry is marked for the following PHARMACY packages:

> Outpatient Unit Dose Non-VA Med

> MARK THIS DRUG AND EDIT IT FOR:

> O - Outpatient U - Unit Dose I - IV

> W - Ward Stock

> D - Drug Accountability C - Controlled Substances X - Non-VA Med

> A - ALL

> Enter your choice(s) separated by commas : O

> O - Outpatient

> \*\* You are NOW editing OUTPATIENT fields. \*\*

> AN Outpatient Pharmacy ITEM? Yes// \<Enter\> (Yes) CORRESPONDING INPATIENT DRUG: \<Enter\>

> MAXIMUM DOSE PER DAY: \<Enter\> LOCAL NON-FORMULARY: \<Enter\> NORMAL AMOUNT TO ORDER: \<Enter\> SOURCE OF SUPPLY: 6P// \<Enter\> CURRENT INVENTORY: \<Enter\>

> ACTION PROFILE MESSAGE (OP): \<Enter\> MESSAGE: \<Enter\>

> QUANTITY DISPENSE MESSAGE: \<Enter\> OP EXTERNAL DISPENSE: \<Enter\>

> Do you wish to mark to transmit to CMOP? Enter Yes or No: YES

> This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP.

> Example 3: Drug Enter/Edit Editing Local Possible Dosages and Orderable Item (continued) If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable.

> Local Drug Generic Name: TIMOLOL MALEATE 0.5% OPH SOLN

> ORDER UNIT: BT DISPENSE UNITS/ORDER UNITS: 5

> DISPENSE UNIT: ML PRICE PER DISPENSE UNIT: 0.1780

> VA Print Name: TIMOLOL MALEATE 0.5% OPH SOLN VA Dispense Unit: ML VA Drug Class: OP101 CMOP ID: T0056

> Do you wish to mark this drug to transmit to CMOP? Enter Yes or No: YES

> QUANTITY DISPENSE MESSAGE: DISP IN MLS

> Do you wish to overwrite your local name? Enter Yes or No: NO

> Do you wish to mark/unmark as a LAB MONITOR or CLOZAPINE DRUG? Enter Yes or No: NO

> \*\* You are NOW in the ORDERABLE ITEM matching for the dispense drug. \*\*

> TIMOLOL MALEATE 0.5% OPH SOLN is already matched to TIMOLOL SOLN,OPH

> Do you want to match to a different Orderable Item? NO// YES Dosage Form -\> SOLN,OPH

> Match to another Orderable Item with same Dosage Form? NO//

> Dosage Form -\> SOLN,OPH

> Dispense Drug -\> TIMOLOL 0.5% OPTH SOL 10ML

> Orderable Item Name: TIMOLOL//

> Matching TIMOLOL 0.5% OPTH SOL 10ML

> to

> TIMOLOL SOLN,OPH

> Is this OK? YES// Match Complete!

> Now editing Orderable Item: TIMOLOL SOLN,OPH

> FORMULARY STATUS:

> Select OI-DRUG TEXT ENTRY:

> INACTIVE DATE:

> DAY (nD) or DOSE (nL) LIMIT:

> DEFAULT MED ROUTE:

> List of med routes associated with the dosage form of the orderable item: RIGHT EYE

> LEFT EYE BOTH EYES

> If you answer YES to the next prompt, the DEFAULT MED ROUTE (if populated)

> 38 Pharmacy Data Management V. 1.0 December 2011

### Example 3: Drug Enter/Edit Editing Local Possible Dosages and Orderable Item (continued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> December 2011 Pharmacy Data Management V. 1.0 38a

## (This side left blank for two-sided copying)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Example 4: Drug Enter/Edit Editing Non-VA Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select DRUG GENERIC NAME: GINGER ROOT TAB/CAP

> Are you adding 'GINGER ROOT' as a new DRUG (the 1756TH)? No// Y (Yes) DRUG NUMBER: 112// \<Enter\>

> DRUG VA CLASSIFICATION: \<Enter\>

> DRUG FSN: \<Enter\>

> DRUG NATIONAL DRUG CLASS: \<Enter\>

> DRUG LOCAL NON-FORMULARY: N \<Enter\> N/F DRUG INACTIVE DATE: \<Enter\>

> DRUG MESSAGE: \<Enter\>

> DRUG RESTRICTION: \<Enter\>

> GENERIC NAME: GINGER ROOT TAB/CAP// ^DI

1.  DISPENSE UNIT
2.  DISPENSE UNITS PER ORDER UNIT CHOOSE 1-2: 2 DISPENSE UNITS PER ORDER UNIT DISPENSE UNITS PER ORDER UNIT: \<Enter\>

> PRICE PER DISPENSE UNIT: 0.0000

> DAW CODE: 0// \<Enter\> - NO PRODUCT SELECTION INDICATED

> Do you wish to match/rematch to NATIONAL DRUG file? Yes// (Yes) Deleting Possible Dosages...

> Match local drug GINGER ROOT

> No NDC to match...

> ORDER UNIT: DISPENSE UNITS/ORDER UNITS: 2

> DISPENSE UNIT:

> I will attempt to match the NDCs from your SYNONYMS. No match by Synonym NDC... now first word

> Match made with GINGER ROOT TAB/CAP Now select VA Product Name

> 1 GINGER CAP/TAB CAP/TAB HA000 G0226 Enter your choice: 1

> Is this a match \< Reply Y, N or press return to continue \> : Y

> CHOOSE FROM:

1.  60 BOTTLE
2.  OTHER OTHER

> Enter Package Size & Type Combination: 1

> Local drug ginger root matches GINGER CAP/TAB PACKAGE SIZE: OTHER PACKAGE TYPE: OTHER

> \< Enter "Y" for yes \>

> \< Enter "N" for no \> OK? : Y

> LOCAL DRUG NAME: GINGER ROOT TAB/CAP

> ORDER UNIT:

DISPENSE UNITS/ORDER UNITS:

DISPENSE UNIT:

> VA PRODUCT NAME: GINGER CAP/TAB

> VA PRINT NAME: GINGER CAP/TAB CMOP ID: G0226

> VA DISPENSE UNIT: CAP/TAB MARKABLE FOR CMOP: NO PACKAGE SIZE: BOTTLE

> PACKAGE TYPE: OTHER

> VA CLASS: HA000 HERBS/ALTERNATIVE THERAPIES INGREDIENTS:

### Example 4: Drug Enter/Edit Editing Non-VA Medications (continued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NATIONAL FORMULARY INDICATOR: NO NATIONAL FORMULARY RESTRICTION:

> \< Enter "Y" for yes, "N" for no \>

> Is this a match ? Y

> You have just VERIFIED this match and MERGED the entry.

> Resetting Possible Dosages.. Press Return to continue:

> Just a reminder...you are editing GINGER ROOT TAB/CAP..

> LOCAL POSSIBLE DOSAGES:

> Do you want to edit Local Possible Dosages? N// \<Enter\> O

> MARK THIS DRUG AND EDIT IT FOR:

> O - Outpatient U - Unit Dose I - IV

> W - Ward Stock

> D - Drug Accountability C - Controlled Substances X - Non-VA Med

> A - ALL

> Enter your choice(s) separated by commas : X

> X - Non-VA Med

> \*\* You are NOW Marking/Unmarking for NON-VA MEDS. \*\* A Non-VA Med ITEM? No// Y (Yes)

> \*\* You are NOW in the ORDERABLE ITEM matching for the dispense drug. \*\*

> There are other Dispense Drugs with the same VA Generic Name and same Dose Form already matched to orderable items. Choose a number to match, or enter '^' to enter a new one.

> Disp. drug -\> GINGER ROOT TAB/CAP

> 1 GINGER CAP/TAB

> Choose number of Orderable Item to match, or '^' to enter a new one: 1 Matching GINGER ROOT TAB/CAP

> to

> GINGER CAP/TAB

> Is this OK? YES// \<Enter\>

> Match Complete!

> Now editing Orderable Item: GINGER CAP/TAB

> FORMULARY STATUS: \<Enter\>

> Select OI-DRUG TEXT ENTRY: \<Enter\>

> INACTIVE DATE: \<Enter\>

> DAY (nD) or DOSE (nL) LIMIT: \<Enter\>

> DEFAULT MED ROUTE: \<Enter\>

> List of med routes associated with the dosage form of the orderable item: NO MED ROUTE DEFINED

> If you answer YES to the next prompt, the DEFAULT MED ROUTE (if populated)

> Example 4: Drug Enter/Edit Editing Non-VA Medications (continued)

## (This side left blank for two-sided copying)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Example 4: Reactivated Standard Medication Route

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Subj: Standard Medication Route File Update \[#136380\] 08/21/09@09:58 64 lines From: STANDARD MEDICATION ROUTE FILE PROCESSOR In 'IN' basket. Page 1 \*New\*

> The following entries have been added to the Standard Medication Routes (#51.23) File:

> (None)

> The following entries have been inactivated in the Standard Medication Routes (#51.23) File:

> (None)

> The following entries have been reactivated in the Standard Medication Routes (#51.23) File:

> INTRADUCTAL

> FDB Route: INTRADUCTAL

> The following entries in the Medication Routes (#51.2) File have been mapped/remapped to a Standard Medication Route (#51.23) File entry.

> (None)

> PLEASE REVIEW, MAY REQUIRE YOUR ATTENTION!

> The following entries in the Medication Routes (#51.2) File have been unmapped from a Standard Medication Route (#51.23) File entry.

> (None)

> The following entries in the Standard Medication Routes (#51.23) File have had changes to the associated First DataBank Med Route and/or Replacement Term.

> INTRADUCTAL

> Replacement Term: \<deleted\>

> The following entries in the Medication Routes (#51.2) File were to be mapped/remapped to a Standard Medication Route (#51.23) File entry, but could not occur because the Medication Route (#51.2) File entry was locked.

> (None)

> The following entries in the Medication Routes (#51.2) File were to be unmapped from a Standard Medication Route (#51.23) File entry, but

> could not occur because the Medication Route (#51.2) File entry was locked. (None)

> Enter message action (in IN basket): Ignore //

> 1.8.5 Default Med Route for OI Report

> \[PSS DEF MED ROUTE OI RPT\]

> The *Default Med Route for OI Report* option is listed on the *Medication Routes Management* \[PSS MEDICATION ROUTES MGMT\] menu. This report can be used to help identify the current default medication routes for the orderable items. The following is an example of the report.

# Patch PSS\*1\*153 added the ability to include printing the POSSIBLE MED ROUTES multiple. If the DEFAULT MED ROUTE field is populated then that value will be returned as the default value. If the DEFAULT MED ROUTE field is not populated and the POSSIBLE MED ROUTES multiple is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field is set to “NO,” the single entry will be returned as the default value. If the DEFAULT MED ROUTE field is not populated and the POSSIBLE MED ROUTES multiple is populated with more than one entry and the USE DOSAGE FORM MED ROUTE LIST field is set to “NO,” no value will be returned as the default value. The med routes selection list in CPRS will be populated with all the medication routes associated with the orderable item’s dosage form if the USE DOSAGE FORM MED ROUTE LIST field is set to "YES," otherwise it will be populated from the POSSIBLE MED ROUTES multiple. These conditions are shown in the following table and examples are provided.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 22%" />
<col style="width: 20%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>DEFAULT MED ROUTE FIELD POPULATED?</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>POSSIBLE MED ROUTES FIELD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>USE DOSAGE FORM MED ROUTE LIST</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VALUE RETURNED – MED ROUTES SELECTION IN CPRS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td>N</td>
<td>N</td>
<td>DEFAULT MED ROUTE field value</td>
</tr>
<tr class="even">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td>Single Entry</td>
<td>N</td>
<td>Single Entry</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td>More Than One Entry</td>
<td>N</td>
<td>All med routes listed in the Possible Med Routes multiple</td>
</tr>
<tr class="even">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td>N</td>
<td>Y</td>
<td>All medication routes associated with orderable item’s dosage form</td>
</tr>
</tbody>
</table>

### Example 1: Default Med Route for Orderable Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 21%" />
<col style="width: 29%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><p>DEFAULT MED</p>
<p>OI NAME</p></th>
<th colspan="2"><p>ROUTE FOR ORDERABLE ITEM REPORT</p>
<p>DOSAGE FORM ASSOCIATED ROUTES</p></th>
<th><p>JUN 17,2009 PAGE 1</p>
<p>DEFAULT ROUTE POSSIBLE MED</p></th>
<th>ROUTES</th>
<th>DRUG</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IBERET</td>
<td>LIQUID</td>
<td><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>IBERET-500 ORAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IBUPROFEN</td>
<td>TAB</td>
<td><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>IBUPROFEN 600MG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IDOXURIDINE</td>
<td>OINT,OPH</td>
<td><blockquote>
<p>RIGHT EYE</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><blockquote>
<p>LEFT EYE</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><blockquote>
<p>BOTH EYES</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>IDOXURIDINE 0.5%</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IMIPRAMINE</td>
<td>TAB</td>
<td><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>IMIPRAMINE 25MG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>IMIPRAMINE 50MG</p>
</blockquote></td>
</tr>
<tr class="even">
<td>INDOCYANINE</td>
<td>INJ,SOLN</td>
<td><blockquote>
<p>INTRAMUSCULAR</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td>INTRAVENOUS</td>
<td colspan="2"><blockquote>
<p>INDOCYANINE 25MG</p>
</blockquote></td>
</tr>
<tr class="even">
<td>INSULIN</td>
<td>INJ</td>
<td><blockquote>
<p>INTRAMUSCULAR</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><blockquote>
<p>ORAL</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><blockquote>
<p>SUBCUTANEOUS</p>
</blockquote></td>
<td>INTRAVENOUS</td>
<td colspan="2"><blockquote>
<p>INSULIN LENTE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>INSULIN NPH</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 62d Pharmacy Data Management V. 1.0 December 2011

9.  Orderable Item Management

> \[PSS ORDERABLE ITEM MANAGEMENT\]

> The *Orderable Item Management* sub-menu provides an option through which the Pharmacy Orderable Items are maintained.

1.  Edit Orderable Items

> \[PSS EDIT ORDERABLE ITEMS\]

# The *Edit Orderabl*e *Items* \[PSS EDIT ORDERABLE ITEMS\] option allows the user to enter and edit data in the PHARMACY ORDERABLE ITEM file (#50.7). If a Pharmacy Orderable Item Drug Text Entry is identified at the “OI-DRUG-TEXT” prompt, it will be viewable during medication order entry processes through CPRS, Outpatient Pharmacy, and Inpatient Medications. Pharmacy Orderable Item defaults can be entered for selected fields. These defaults will be displayed to the user during the medication order entry processes for all applications through which medication orders can be entered.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Edit Orderable Items* \[PSS EDIT ORDERABLE ITEMS\] option allows the user to enter a default medication route and med route selection list.

# The default medication route for CPRS will be derived from the DEFAULT MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated or from the POSSIBLE MED ROUTES multiple (#50.711) of the PHARMACY ORDERABLE ITEM file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> (#50.7) if it is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO."

# Additional med routes for selection in the drop-down list in CPRS will be derived from the POSSIBLE MED ROUTES multiple (#50.711) if the USE DOSAGE FORM MED ROUTE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> LIST field (#10) is set to "NO." Otherwise, the med routes associated with the orderable item's dosage form, MED ROUTE FOR DOSAGE FORM multiple (#50.6061) of the DOSAGE FORM file (#50.606) will be returned.

# The method of deriving the appropriate medication routes listed above will be for Inpatient Medications unit dose orders, IV Fluids orders, and Outpatient Pharmacy orders entered via CPRS orders dialog.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Additionally, a report is available to view all current default medication routes as well as all possible med routes for the listed orderable items. See the section entitled *Default Med Route For OI Report* \[PSSDEF MED ROUTE OI RPT\].

### Example 1: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “NO”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example 1: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “NO” (continued)

> Dispense Drugs:

> INSULIN REGULAR U-100 INJ

> Are you sure you want to edit this Orderable Item? NO//Y YES

> Now editing Orderable Item: INSULIN INJ

> Orderable Item Name: INSULIN// This Orderable Item is Formulary.

> This Orderable Item is marked as a Non-VA Med.

> Select OI-DRUG TEXT ENTRY: INACTIVE DATE:

> DAY (nD) or DOSE (nL) LIMIT: DEFAULT MED ROUTE: SUBCUTANEOUS//

> List of med routes associated with the DOSAGE FORM of the orderable item:

> INTRAVENOUS INTRAMUSCULAR

> If you answer YES to the next prompt, the DEFAULT MED ROUTE (if populated) and this list (if populated) will be displayed as selectable med routes during medication ordering dialog. If you answer NO, the DEFAULT MED ROUTE (if populated) and POSSIBLE MED ROUTES list will be displayed instead.

> USE DOSAGE FORM MED ROUTE LIST: N NO

> List of Possible Med Routes associated with the orderable item:

> INTRAVENOUS

> Select POSSIBLE MED ROUTES: ORAL

1.  ORAL PO
2.  ORAL (BY MOUTH) PO
3.  ORAL INHALATION ORALINHL
4.  ORAL INTRADERMAL PERIOSTEAL ORALID PER
5.  ORAL INTRAMUSCULAR ORALIM

> Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 1 ORAL PO

> The selected entry does not match any of the dosage form med routes. Are you adding 'ORAL' as a new POSSIBLE MED ROUTE? NO// YES

> Select POSSIBLE MED ROUTES: SCHEDULE TYPE:

> SCHEDULE:

> PATIENT INSTRUCTIONS:

> Select SYNONYM:

### Example 2: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “NO” and there are no Default Med Route nor Possible Med Routes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select PHARMACY ORDERABLE ITEM NAME: INSULIN INJ

> Orderable Item -\> INSULIN Dosage Form -\> INJ

> List all Drugs/Additives/Solutions tied to this Orderable Item? YES// NO

> Are you sure you want to edit this Orderable Item? NO// YES

> Now editing Orderable Item: INSULIN INJ

> Orderable Item Name: INSULIN//

> This Orderable Item is Formulary.

> This Orderable Item is marked as a Non-VA Med.

> Select OI-DRUG TEXT ENTRY: INACTIVE DATE:

> DAY (nD) or DOSE (nL) LIMIT: DEFAULT MED ROUTE:

> List of med routes associated with the DOSAGE FORM of the orderable item:

> INTRAVENOUS INTRAMUSCULAR

> ORAL INTRAMUSCULAR

> If you answer YES to the next prompt, the DEFAULT MED ROUTE (if populated) and this list (if populated) will be displayed as selectable med routes during medication ordering dialog. If you answer NO, the DEFAULT MED ROUTE (if populated) and POSSIBLE MED ROUTES list will be displayed instead.

> USE DOSAGE FORM MED ROUTE LIST: NO//

> POSSIBLE MED ROUTES:

> You have not selected ANY med routes to display during order entry. In order to have med routes displayed during order entry, you must either define a DEFAULT MED ROUTE and/or at least one POSSIBLE MED ROUTE, or answer YES to the USE DOSAGE FORM MED ROUTE LIST prompt.

> \*\*WITH THE CURRENT SETTINGS, NO MED ROUTES WILL DISPLAY FOR SELECTION DURING ORDER ENTRY FOR THIS ORDERABLE ITEM\*\*

> The current setting is usually only appropriate for supply items.

> Continue with no med routes displaying for selection during order entry? NO// YE S

> SCHEDULE TYPE: SCHEDULE:

> PATIENT INSTRUCTIONS:

> OTHER LANGUAGE INSTRUCTIONS:

> Select SYNONYM:

### Example 3: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “YES”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select PHARMACY ORDERABLE ITEM NAME: INSULIN INJ

> Orderable Item -\> INSULIN Dosage Form -\> INJ

> List all Drugs/Additives/Solutions tied to this Orderable Item? YES// Y YES

> Orderable Item -\> INSULIN Dosage Form -\> INJ

> Dispense Drugs:

> INSULIN REGULAR U-100 INJ

> Are you sure you want to edit this Orderable Item? NO//Y YES

> Now editing Orderable Item: INSULIN INJ

> Orderable Item Name: INSULIN//

> This Orderable Item is Formulary.

> This Orderable Item is marked as a Non-VA Med.

> Select OI-DRUG TEXT ENTRY: INACTIVE DATE:

> DAY (nD) or DOSE (nL) LIMIT: DEFAULT MED ROUTE: SUBCUTANEOUS//

> List of med routes associated with the DOSAGE FORM of the orderable item:

> INTRAVENOUS INTRAMUSCULAR

> If you answer YES to the next prompt, the DEFAULT MED ROUTE (if populated) and this list (if populated) will be displayed as selectable med routes during medication ordering dialog. If you answer NO, the DEFAULT MED ROUTE (if populated) and POSSIBLE MED ROUTES list will be displayed instead.

> USE DOSAGE FORM MED ROUTE LIST: Y YES SCHEDULE TYPE:

> SCHEDULE:

> PATIENT INSTRUCTIONS:

> Select SYNONYM:

# If the orderable item being edited is matched to any dispense drugs that are in VA drug classes IM100 through IM900, an additional prompt will appear to permit mapping for the orderable item to an associated immunization file entry. This feature is introduced with the Immunizations Documentation by BCMA application in patches PSS\*1\*141 and PSB\*3\*47.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Example: Editing Immunization-Related Pharmacy Orderable Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select PHARMACY ORDERABLE ITEM NAME: INFLUENZA INFLUENZA INJ

> Orderable Item -\> INFLUENZA Dosage Form -\> INJ

> List all Drugs/Additives/Solutions tied to this Orderable Item? YES// \<Enter\>

> Orderable Item -\> INFLUENZA Dosage Form -\> INJ

> Dispense Drugs:

> INFLUENZA VACCINE

> Are you sure you want to edit this Orderable Item? NO// YES

> Now editing Orderable Item:

> INFLUENZA INJ

> Orderable Item Name: INFLUENZA// \<Enter\>

> This Orderable Item is Formulary.

> This Orderable Item is marked as a Non-VA Med. Select OI-DRUG TEXT ENTRY: \<Enter\>

> INACTIVE DATE: \<Enter\>

> DAY (nD) or DOSE (nL) LIMIT: \<Enter\>

> DEFAULT MED ROUTE: \<Enter\>

> List of med routes associated with the dosage form of the orderable item:

> INTRAVENOUS INTRAMUSCULAR

> If you answer YES to the next prompt, the DEFAULT MED ROUTE (if populated) and this list (if populated) will be displayed as selectable med routes during medication ordering dialog. If you answer NO, the DEFAULT MED ROUTE (if populated) and POSSIBLE MED ROUTES list will be displayed instead.

> USE DOSAGE FORM MED ROUTE LIST: NO// Y YES SCHEDULE TYPE: \<Enter\>

> SCHEDULE: \<Enter\>

> PATIENT INSTRUCTIONS: \<Enter\>

> ASSOCIATED IMMUNIZATION: INFLUENZA FLU,3 YRS INFLUENZA

> Select SYNONYM: \<Enter\>

> *(This page left blank for two-sided copying)*

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSS*1*153 User Manual Change Pages

### Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>04/11</p>
</blockquote></td>
<td><blockquote>
<p>i-ii, 38, 40,</p>
<p>62d-f, 64, 64a</p>
</blockquote></td>
<td>PSS*1*153</td>
<td><blockquote>
<p>Renamed the MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) to be DEFAULT MED</p>
<p>ROUTE. Provided the ability to print the POSSIBLE MED ROUTES multiple on <em>the Default Med Route For OI Report</em> [PSS DEF MED ROUTE OI RPT] option.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>02/11</p>
</blockquote></td>
<td><blockquote>
<p>i, 63</p>
</blockquote></td>
<td>PSS*1*142</td>
<td><blockquote>
<p>Added functionality to denote the default med route for IV orders in the selection list in CPRS if all of the orderable items on the order have the same default med route defined. Updated TOC. Released with CPRS version 28.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>02/10</p>
</blockquote></td>
<td><blockquote>
<p>iii-iv, 3-4, 44a-</p>
<p>d, 47-48, 61- 62d, 89-90b,</p>
<p>112, 203-206</p>
</blockquote></td>
<td>PSS*1*147</td>
<td><blockquote>
<p>Described new process for requesting changes to Standard Medication Routes and the New Term Rapid Turnaround (NTRT) process;</p>
<p>Added <em>IV Additive/Solution Reports</em> menu, with suboptions <em>IV Solution Report</em> option and <em>V Additive Report</em> [PSS IV ADDITIVE REPORT] option</p>
<p>Added <em>Default Med Route for OI Report</em> option to the <em>Medication Routes Management...</em> menu<em>.</em>(this change was made but not documented with PSS*1*140)</p>
<p>Updated <em>Drug Enter/Edit</em> option to display NUMERIC DOSE and DOSE UNIT fields defined for Local Possible Dosage Updated the Drug Enter/Edit option display to include the new ADDITIVE FREQUENCY field</p>
<p>Updated Table of Contents and Index <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/09</p>
</blockquote></td>
<td><blockquote>
<p>i, 64a-b, 65,</p>
<p>65a-b, 66</p>
</blockquote></td>
<td>PSS*1*141</td>
<td><blockquote>
<p>Added ASSOCIATED IMMUNIZATION field to <em>Edit</em></p>
<p><em>Orderable Items</em> option and <em>Dispense Drug/Orderable Item Maintenance</em> option. Reorganized content within sections to accommodate new information.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/09</p>
</blockquote></td>
<td><blockquote>
<p>iii-iv, 53,</p>
<p>62a-b, 63, 81,</p>
<p>203</p>
</blockquote></td>
<td>PSS*1*140</td>
<td><blockquote>
<p>Added DEFAULT MED ROUTE FOR CPRS field and <em>Default Med Route For OI Report</em> [PSS DEF MED ROUTE OI RPT] option for the enhancement of default medication route being defined for an orderable item.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/09</p>
</blockquote></td>
<td><blockquote>
<p>27-34</p>
</blockquote></td>
<td>PSS*1*131</td>
<td><blockquote>
<p>Added explanations of DEA special handling code U for sensitive drug.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>05/09</p>
</blockquote></td>
<td><blockquote>
<p>81</p>
</blockquote></td>
<td>PSS*1*137</td>
<td><blockquote>
<p>Added Automate CPRS Refill field to the <em>Pharmacy System Parameters Edit</em> [PSS MGR] option.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>02/09</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td>PSS*1*129</td>
<td><blockquote>
<p>Pages renumbered to accommodate added pages. Pharmacy Reengineering (PRE) V.0.5 Pre-Release. Restructured <em>Pharmacy Data Management</em> menu:</p>
</blockquote>
<ul>
<li><p>Grouped related options under the following new sub-menus: <em>Drug Text Management, Medication Instruction Management, Medication Routes Management,</em> and <em>Standard Schedule Management</em></p></li>
<li><blockquote>
<p>Added temporary <em>Enhanced Order Checks Setup Menu</em></p>
</blockquote></li>
<li><p>Added the following options: <em>Find Unmapped Local Medication Routes, Find Unmapped Local Possible Dosages, Map Local Medication Route to Standard, Map Local Possible Dosages, Mark PreMix Solutions, Request Change to Dose Unit</em>, and <em>Request Change to Standard Medication Route</em></p></li>
<li><p>Added the following reports: <em>Administration Schedule File Report, IV Solution Report, Local Possible Dosages Report, Medication Instruction File Report, Medication Route Mapping Report, Medication Route Mapping History Report,</em> and <em>Strength Mismatch Report</em></p></li>
<li><blockquote>
<p>Updated Table of Contents, Index, and Glossary <mark>REDACTED</mark></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>09/97</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Original Release of User Manual</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Example 3: Drug Enter/Edit Editing Local Possible Dosages and Orderable Item (continued)

> Do you wish to match/rematch to NATIONAL DRUG file? No// \<Enter\> (No)
> Just a reminder...you are editing TIMOLOL MALEATE 0.5% OPH SOLN.
> LOCAL POSSIBLE DOSAGES:
1.  DROP PACKAGE: IO
2.  DROPS PACKAGE: IO
> Do you want to edit Local Possible Dosages? N// YES
> This drug has the following Local Possible Dosages:
1.  DROP PACKAGE: IO
2.  DROPS PACKAGE: IO
> Do you want to merge new Local Possible Dosages? Y// NO
> Strength: 0.5 Unit: %
> Select LOCAL POSSIBLE DOSAGE: 1 DROP IO
> LOCAL POSSIBLE DOSAGE: 1 DROP//\<Enter\> OTHER LANGUAGE DOSAGE NAME: \<Enter\>
> PACKAGE: Both// \<Enter\>
> BCMA UNITS PER DOSE: \<Enter\> DOSE UNIT: DROP(S)// \<Enter\> NUMERIC DOSE: 1// \<Enter\>
> Strength: 0.5 Unit: %
> Select LOCAL POSSIBLE DOSAGE: \<Enter\>
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* This entry is marked for the following PHARMACY packages:
> Outpatient Unit Dose Non-VA Med
> MARK THIS DRUG AND EDIT IT FOR:
> O - Outpatient U - Unit Dose I - IV
> W - Ward Stock
> D - Drug Accountability
> C - Controlled Substances X - Non-VA Med
> A - ALL
> Enter your choice(s) separated by commas : O
> O - Outpatient
> \*\* You are NOW editing OUTPATIENT fields. \*\*
> AN Outpatient Pharmacy ITEM? Yes// \<Enter\> (Yes) CORRESPONDING INPATIENT DRUG: \<Enter\>
> MAXIMUM DOSE PER DAY: \<Enter\> LOCAL NON-FORMULARY: \<Enter\> NORMAL AMOUNT TO ORDER: \<Enter\> SOURCE OF SUPPLY: 6P// \<Enter\> CURRENT INVENTORY: \<Enter\>
> ACTION PROFILE MESSAGE (OP): \<Enter\> MESSAGE: \<Enter\>
> QUANTITY DISPENSE MESSAGE: \<Enter\> OP EXTERNAL DISPENSE: \<Enter\>
> Do you wish to mark to transmit to CMOP? Enter Yes or No: YES
> This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP.

#### Example 3: Drug Enter/Edit Editing Local Possible Dosages and Orderable Item (continued)

> If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable.
> Local Drug Generic Name: TIMOLOL MALEATE 0.5% OPH SOLN
> ORDER UNIT: BT DISPENSE UNITS/ORDER UNITS: 5
> DISPENSE UNIT: ML PRICE PER DISPENSE UNIT: 0.1780
> VA Print Name: TIMOLOL MALEATE 0.5% OPH SOLN VA Dispense Unit: ML VA Drug Class: OP101 CMOP ID: T0056
> Do you wish to mark this drug to transmit to CMOP? Enter Yes or No: YES
> QUANTITY DISPENSE MESSAGE: DISP IN MLS
> Do you wish to overwrite your local name? Enter Yes or No: NO
> Do you wish to mark/unmark as a LAB MONITOR or CLOZAPINE DRUG? Enter Yes or No: NO
> \*\* You are NOW in the ORDERABLE ITEM matching for the dispense drug. \*\*
> TIMOLOL MALEATE 0.5% OPH SOLN is already matched to
> TIMOLOL SOLN,OPH
> Do you want to match to a different Orderable Item? NO// YES
> Dosage Form -\> SOLN,OPH
> Match to another Orderable Item with same Dosage Form? NO// \<Enter\>
> Dosage Form -\> SOLN,OPH
> Dispense Drug -\> TIMOLOL MALEATE 0.5% OPH SOLN
> Orderable Item Name: TIMOLOL// \<Enter\>
> Matching TIMOLOL MALEATE 0.5% OPH SOLN
> to
> TIMOLOL SOLN,OPH
> Is this OK? YES// \<Enter\> Match Complete!
> Now editing Orderable Item: TIMOLOL SOLN,OPH
> FORMULARY STATUS: \<Enter\>
> Select OI-DRUG TEXT ENTRY: \<Enter\> INACTIVE DATE: \<Enter\>
> DAY (nD) or DOSE (nL) LIMIT: \<Enter\> DEFAULT MED ROUTE: \<Enter\>
> SCHEDULE TYPE: \<Enter\> SCHEDULE: \<Enter\>
> PATIENT INSTRUCTIONS: \<Enter\>
> OTHER LANGUAGE INSTRUCTIONS: \<Enter\>
> Select SYNONYM: \<Enter\>

#### Example 4: Drug Enter/Edit Editing Non-VA Medications

> Select DRUG GENERIC NAME: GINGER ROOT TAB/CAP
> Are you adding 'GINGER ROOT' as a new DRUG (the 1756TH)? No// Y (Yes) DRUG NUMBER: 112// \<Enter\>
> DRUG VA CLASSIFICATION: \<Enter\>
> DRUG FSN: \<Enter\>
> DRUG NATIONAL DRUG CLASS: \<Enter\>
> DRUG LOCAL NON-FORMULARY: N \<Enter\> N/F DRUG INACTIVE DATE: \<Enter\>
> DRUG MESSAGE: \<Enter\>
> DRUG RESTRICTION: \<Enter\>
> GENERIC NAME: GINGER ROOT TAB/CAP// ^DI
1.  DISPENSE UNIT
2.  DISPENSE UNITS PER ORDER UNIT CHOOSE 1-2: 2 DISPENSE UNITS PER ORDER UNIT DISPENSE UNITS PER ORDER UNIT: \<Enter\>
> PRICE PER DISPENSE UNIT: 0.0000
> DAW CODE: 0// \<Enter\> - NO PRODUCT SELECTION INDICATED
> Do you wish to match/rematch to NATIONAL DRUG file? Yes// (Yes)
> Deleting Possible Dosages...
> Match local drug GINGER ROOT
> ORDER UNIT:
> No NDC to match...
> DISPENSE UNITS/ORDER UNITS: 2
> DISPENSE UNIT:
> I will attempt to match the NDCs from your SYNONYMS.
> No match by Synonym NDC... now first word
> Match made with GINGER ROOT TAB/CAP Now select VA Product Name
> 1 GINGER CAP/TAB CAP/TAB HA000 G0226 Enter your choice: 1
> Is this a match \< Reply Y, N or press return to continue \> : Y
> CHOOSE FROM:
1.  60 BOTTLE
2.  OTHER
> Enter Package Size & Type Combination: 1
> Local drug ginger root matches GINGER CAP/TAB PACKAGE SIZE: OTHER PACKAGE TYPE: OTHER
> \< Enter "Y" for yes \>
> \< Enter "N" for no \> OK? : Y
> LOCAL DRUG NAME: GINGER ROOT TAB/CAP
> ORDER UNIT:
DISPENSE UNITS/ORDER UNITS:
DISPENSE UNIT:
> VA PRODUCT NAME: GINGER CAP/TAB
> VA PRINT NAME: GINGER CAP/TAB CMOP ID: G0226
> VA DISPENSE UNIT: CAP/TAB MARKABLE FOR CMOP: NO PACKAGE SIZE: BOTTLE
> PACKAGE TYPE: OTHER
> VA CLASS: HA000 HERBS/ALTERNATIVE THERAPIES INGREDIENTS:

#### Example 4: Drug Enter/Edit Editing Non-VA Medications (continued)

> NATIONAL FORMULARY INDICATOR: NO NATIONAL FORMULARY RESTRICTION:
> \< Enter "Y" for yes, "N" for no \>
> Is this a match ? Y
> You have just VERIFIED this match and MERGED the entry.
> Resetting Possible Dosages..
> Press Return to continue:
> Just a reminder...you are editing GINGER ROOT TAB/CAP..
> LOCAL POSSIBLE DOSAGES:
> Do you want to edit Local Possible Dosages? N// \<Enter\> O
> MARK THIS DRUG AND EDIT IT FOR:
> O - Outpatient U - Unit Dose I - IV
> W - Ward Stock
> D - Drug Accountability
> C - Controlled Substances X - Non-VA Med
> A - ALL
> Enter your choice(s) separated by commas : X
> X - Non-VA Med
> \*\* You are NOW Marking/Unmarking for NON-VA MEDS. \*\* A Non-VA Med ITEM? No// Y (Yes)
> \*\* You are NOW in the ORDERABLE ITEM matching for the dispense drug. \*\*
> There are other Dispense Drugs with the same VA Generic Name and same Dose Form already matched to orderable items. Choose a number to match, or enter '^' to enter a new one.
> Disp. drug -\> GINGER ROOT TAB/CAP
> 1 GINGER CAP/TAB
> Choose number of Orderable Item to match, or '^' to enter a new one: 1
> Matching GINGER ROOT TAB/CAP to
> GINGER CAP/TAB
> Is this OK? YES// \<Enter\>
> Match Complete!
> Now editing Orderable Item: GINGER CAP/TAB
> FORMULARY STATUS: \<Enter\>
> Select OI-DRUG TEXT ENTRY: \<Enter\>
> INACTIVE DATE: \<Enter\>
> DAY (nD) or DOSE (nL) LIMIT: \<Enter\>
> DEFAULT MED ROUTE: \<Enter\> SCHEDULE TYPE: \<Enter\> SCHEDULE: \<Enter\>
> PATIENT INSTRUCTIONS: \<Enter\>
> OTHER LANGUAGE INSTRUCTIONS: \<Enter\>
> Select SYNONYM: \<Enter\>

#### Example 4: Reactivated Standard Medication Route

> Subj: Standard Medication Route File Update \[#136380\] 08/21/09@09:58 64 lines From: STANDARD MEDICATION ROUTE FILE PROCESSOR In 'IN' basket. Page 1 \*New\*
> The following entries have been added to the Standard Medication Routes (#51.23) File:
> (None)
> The following entries have been inactivated in the Standard Medication Routes (#51.23) File:
> (None)
> The following entries have been reactivated in the Standard Medication Routes (#51.23) File:
> INTRADUCTAL
> FDB Route: INTRADUCTAL
> The following entries in the Medication Routes (#51.2) File have been mapped/remapped to a Standard Medication Route (#51.23) File entry.
> (None)
> PLEASE REVIEW, MAY REQUIRE YOUR ATTENTION!
> The following entries in the Medication Routes (#51.2) File have been unmapped from a Standard Medication Route (#51.23) File entry.
> (None)
> The following entries in the Standard Medication Routes (#51.23) File have had changes to the associated First DataBank Med Route and/or Replacement Term.
> INTRADUCTAL
> Replacement Term: \<deleted\>
> The following entries in the Medication Routes (#51.2) File were to be mapped/remapped to a Standard Medication Route (#51.23) File entry, but could not occur because the Medication Route (#51.2) File entry was locked.
> (None)
> The following entries in the Medication Routes (#51.2) File were to be unmapped from a Standard Medication Route (#51.23) File entry, but
> could not occur because the Medication Route (#51.2) File entry was locked.
> (None)
> Enter message action (in IN basket): Ignore //
> 1.8.1 Default Med Route for OI Report
> \[PSS DEF MED ROUTE OI RPT\]
> The *Default Med Route for OI Report* option is listed on the *Medication Routes Management* \[PSS MEDICATION ROUTES MGMT\] menu. This report can be used to help identify the current default medication routes for the orderable items. Example 3 below illustrates the report.

### Patch PSS\*1\*153 added the ability to include printing the POSSIBLE MED ROUTES multiple. If the DEFAULT MED ROUTE field is populated then that value will be returned as the default value. If the DEFAULT MED ROUTE field is not populated and the POSSIBLE MED ROUTES multiple is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field is set to “NO”, the single entry will be returned as the default value. If the DEFAULT MED ROUTE field is not populated and the POSSIBLE MED ROUTES multiple is populated with more than one entry and the USE DOSAGE FORM MED ROUTE LIST field is set to “NO”, no value will be returned as the default value. The med routes selection list in CPRS will be populated with entries in all the medication routes associated with the orderable item’s dosage form if the USE DOSAGE FORM MED ROUTE LIST field is set to "YES"; otherwise it will be populated from the POSSIBLE MED ROUTES multiple. These conditions are shown in the following table and examples are provided.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 23%" />
<col style="width: 19%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>DEFAULT MED ROUTE FIELD POPULATED?</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>POSSIBLE MED ROUTES FIELD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>USE DOSAGE FORM MED ROUTE LIST</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VALUE RETURNED – MED ROUTES SELECTION IN CPRS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td><blockquote>
<p>--</p>
</blockquote></td>
<td><blockquote>
<p>--</p>
</blockquote></td>
<td><blockquote>
<p>DEFAULT MED ROUTE field value</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>Single Entry</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>Single Entry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>More Than One Entry</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>None</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td><blockquote>
<p>All medication routes associated with orderable item’s dosage form</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Example 1: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “NO”

> Example 1: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “NO” continued

#### Example 2: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “YES”

> Example 2: Edit Orderable Items with USE DOSAGE FORM MED ROUTE LIST set to “YES” continued

#### Are you sure you want to edit this Orderable Item? NO//Y YES

> Now editing Orderable Item:

#### INSULIN INJ

> Orderable Item Name: INSULIN// This Orderable Item is Formulary.

#### This Orderable Item is marked as a Non-VA Med.

> Select OI-DRUG TEXT ENTRY:

#### INACTIVE DATE:

> DAY (nD) or DOSE (nL) LIMIT:

#### DEFAULT MED ROUTE: SUBCUTANEOUS//

> List of med routes associated with the dosage form of the orderable item: INTRAVENOUS

#### INTRAMUSCULAR

> If you answer YES to the next prompt, the DEFAULT MED ROUTE (if defined) and this list will be displayed as selectable med routes in CPRS in the

#### medication ordering dialog. If you answer NO, the DEFAULT MED ROUTE (if defined) and POSSIBLE MED ROUTES list will be displayed instead.

> USE DOSAGE FORM MED ROUTE LIST: Y YES SCHEDULE TYPE:

#### SCHEDULE:

> PATIENT INSTRUCTIONS:
> Select SYNONYM:
> Example 3: Default Med Route for Orderable Item Report
<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 3%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEFAULT MED</p>
<p>OI NAME</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>ROUTE FOR ORDERABLE ITEM</p>
<p>DOSAGE FORM ASSOCIATED</p>
</blockquote></th>
<th><blockquote>
<p>REPORT</p>
</blockquote>
<p>ROUTES</p></th>
<th><blockquote>
<p>JUN 17,2009</p>
<p>DEFAULT ROUTE</p>
</blockquote></th>
<th><p>PAGE</p>
<p>POSSIBLE</p></th>
<th><blockquote>
<p>1</p>
</blockquote>
<p>MED</p></th>
<th><blockquote>
<p>ROUTES</p>
</blockquote></th>
<th><blockquote>
<p>DRUG</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IBERET</p>
</blockquote></td>
<td><blockquote>
<p>LIQUID</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>IBERET-500 ORAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IBUPROFEN</p>
</blockquote></td>
<td><blockquote>
<p>TAB</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>IBUPROFEN 600MG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IDOXURIDINE</p>
</blockquote></td>
<td><blockquote>
<p>OINT,OPH</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>RIGHT EYE</p>
</blockquote></td>
<td></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>LEFT EYE</p>
</blockquote></td>
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>BOTH EYES</p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>IDOXURIDINE 0.5%</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IMIPRAMINE</p>
</blockquote></td>
<td><blockquote>
<p>TAB</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>IMIPRAMINE 25MG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td></td>
<td colspan="4"><blockquote>
<p>IMIPRAMINE 50MG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INDOCYANINE</p>
</blockquote></td>
<td><blockquote>
<p>INJ,SOLN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>INTRAMUSCULAR</p>
</blockquote></td>
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>INDOCYANINE 25MG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INSULIN</p>
</blockquote></td>
<td><blockquote>
<p>INJ</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>INTRAMUSCULAR</p>
</blockquote></td>
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>ORAL</p>
</blockquote></td>
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>SUBCUTANEOUS</p>
</blockquote></td>
<td><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>INSULIN LENTE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td></td>
<td colspan="4"><blockquote>
<p>INSULIN NPH</p>
</blockquote></td>
</tr>
</tbody>
</table>

## \[PSS ORDERABLE ITEM MANAGEMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Orderable Item Management* sub-menu provides an option through which the Pharmacy Orderable Items are maintained.

> 1.9.1 Edit Orderable Items

## \[PSS EDIT ORDERABLE ITEMS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The *Edit Orderabl*e *Items* option allows the user to enter and edit data in the PHARMACY ORDERABLE ITEM file (#50.7). If a Pharmacy Orderable Item Drug Text Entry is identified at the “OI-DRUG-TEXT” prompt, it will be viewable during medication order entry processes through CPRS, Outpatient Pharmacy, and Inpatient Medications. Pharmacy Orderable Item defaults can be entered for selected fields. These defaults will be displayed to the user during the medication order entry processes for all applications through which medication orders can be entered.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Edit Orderable Items* option allows the user to enter a default medication route. If a default medication route has been defined for an orderable item and the Default Med Route for CPRS field is set to YES (see the *Pharmacy System Parameters Edit* \[PSS SYS EDIT\] section for details), that default medication route will be the only route displayed for selection from the drop-down list on the CPRS Inpatient Medications dialog and the Outpatient Pharmacy dialog. However, the provider can still type in a valid medication route or valid medication route abbreviation to change the medication route for the order. If the Default Med Route for CPRS is set to NO and a default medication route has been defined for an orderable item, the medication route in the order dialog will be the default medication route; however the additional medication routes associated with the dosage form will display for selection from the drop-down list. If a default medication route has not been defined for the orderable item, all possible medication routes for the dosage form will be available for the provider to select in CPRS.

### ![](pss-1-153-user-manual-change-pages/002.png)Additionally, a report is available to view all current default medication routes for the listed orderable items. See the section entitled *Default Med Route For OI Report* \[PSS DEF MED ROUTE OI RPT\].

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Edit Orderable Items* option allows the user to enter patient instructions in a language other than English. PDM does not translate English terms into another language; instead, it allows the user to enter a translation of a term. If a value has not been entered in the OTHER LANGUAGE INSTRUCTIONS field, PDM will default to the value entered in the PATIENT INSTRUCTIONS field. If the PATIENT INSTRUCTIONS field does not contain data for the selected orderable item, the system will not present default patient instructions to the user during CPRS or Outpatient Pharmacy prescription order processing. However, when building the SIG, Outpatient Pharmacy will default to the value the user input through backdoor Outpatient Pharmacy order entry.

#### Example: Editing Pharmacy Orderable Items

> Example: Editing Pharmacy Orderable Items (continued)

### If the orderable item being edited is matched to any dispense drugs that are in VA drug classes IM100 through IM900, an additional prompt will appear to permit mapping for the orderable item to an associated immunization file entry. This feature is introduced with the Immunizations Documentation by BCMA application in patches PSS\*1\*141 and PSB\*3\*47.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example: Editing Immunization-Related Pharmacy Orderable Items

#### Select PHARMACY ORDERABLE ITEM NAME: INFLUENZA INFLUENZA INJ

> Orderable Item -\> INFLUENZA Dosage Form -\> INJ

#### List all Drugs/Additives/Solutions tied to this Orderable Item? YES// \<Enter\>

> Orderable Item -\> INFLUENZA Dosage Form -\> INJ

#### Dispense Drugs:

> INFLUENZA VACCINE

#### Are you sure you want to edit this Orderable Item? NO// YES

> Now editing Orderable Item:

#### INFLUENZA INJ

> Orderable Item Name: INFLUENZA// \<Enter\>

#### This Orderable Item is Formulary.

> This Orderable Item is marked as a Non-VA Med. Select OI-DRUG TEXT ENTRY: \<Enter\>

#### DAY (nD) or DOSE (nL) LIMIT: \<Enter\>

> DEFAULT MED ROUTE: \<Enter\> SCHEDULE TYPE: \<Enter\> SCHEDULE: \<Enter\>

> PATIENT INSTRUCTIONS: \<Enter\>

#### ASSOCIATED IMMUNIZATION: INFLUENZA FLU,3 YRS INFLUENZA

> Select SYNONYM: \<Enter\>

> *(This page included for two-sided copying)*

### From: PSS*1*172 User Manual Change Pages

### = High risk/high alert – recommended to witness in BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  3 = High risk/high alert – required to witness in BCMA
> To set the HIGH RISK/HIGH ALERT DRUG field (#1) values in the local PHARMACY ORDERABLE ITEM file (#50.7), complete the steps shown in the example below.
> Example (Modify Pharmacy Orderable Item File):
> Select OPTION NAME: PSS EDIT ORDERABLE ITEMS Edit Orderable Items Edit Orderable Items
> This option enables you to edit Orderable Item names, Formulary status, drug text, Inactive Dates, and Synonyms.
> Select PHARMACY ORDERABLE ITEM NAME: HEPARIN
1.  HEPARIN INJ,SOLN
2.  HEPARIN SOLN
> CHOOSE 1-2: 1 HEPARIN INJ,SOLN
> Orderable Item -\> HEPARIN Dosage Form -\> INJ,SOLN
> List all Drugs/Additives/Solutions tied to this Orderable Item? YES// Orderable Item -\> HEPARIN
> Dosage Form -\> INJ,SOLN
> Dispense Drugs:
> HEPARIN BEEF 1,000 UNITS/ML 30ML HEPARIN 1,000 UNIT/ML 10ML INJ HEPARIN 10,000 UNITS 4ML
> HEPARIN 1,000 UNITS/ML 30ML HEPARIN, BEEF 10,000 UNIT/ML 4ML HEPARIN, BEEF 1,000 UNIT/ML 10ML
> Are you sure you want to edit this Orderable Item? NO// YES
> Now editing Orderable Item:
> HEPARIN INJ,SOLN
> Orderable Item Name: HEPARIN// This Orderable Item is Formulary.
> This Orderable Item is marked as a Non-VA Med.
> Select OI-DRUG TEXT ENTRY:
> INACTIVE DATE:
> DAY (nD) or DOSE (nL) LIMIT:
> DEFAULT MED ROUTE: INTRAVENOUS//
> List of med routes associated with the DOSAGE FORM of the orderable item:
> ![](pss-1-172-user-manual-change-pages/003.png)Note: When responding to the prompt above, VistA accepts a 0, 1, 2, or 3 or will allow the user to type the first letter of the description, i.e., N, H, R or W.

### \[PSS INFINS MGR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Infusion Instruction Management* \[PSS INFINS MGR\] menu contains the following options:

- Infusion Instructions Add/Edit
- Infusion Instructions Report
  1.  Infusion Instructions Add/Edit

### \[PSS INFINS ADED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Infusion Instructions Add/Edit* \[PSS INFINS ADED\] option allows the entry and editing of abbreviations and expansions in the INFUSION INSTRUCTIONS (#53.47) file. When entered into the Infusion Rate field during the entry of inpatient medication orders, Infusion Instruction abbreviations are replaced with the expanded text associated with the abbreviation.

> Example: *Infusion Instructions Add/Edit* \[PSS INFINS ADED\] Option

## Infusion Instructions Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS INFINS RPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Provides a report of entries from the INFUSION INSTRUCTIONS (#53.47) file.

> Example: *Infusion Instructions Report* \[PSS INFINS RPT\] Option

## Enable/Disable Vendor Database Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS ENABLE/DISABLE DB LINK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enable/Disable Vendor Database Link is a stand-alone option that exists ONLY as a way for technical personnel to turn on/off the database connection if required for debugging. When disabled, NO drug-drug interactions, duplicate therapy, or dosing order checks will be performed in Outpatient Pharmacy, Inpatient Medication applications, or in the Computerized Patient Record System (CPRS).

> Normally the link is enabled and the Vendor Database updates are performed centrally at the Austin Information Technology Center (AITC) and Philadelphia Information Technology Center (PITC).

> The option is rarely used. It is NOT exported as part of the main Pharmacy Data Management \[PSS MGR\] menu option. *The examples provided are for technical personnel only.*

> Example 1: Disabling the Vendor Database Link

> Example 2: Enabling the Vendor Database Link

## Other Language Translation Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS OTHER LANGUAGE SETUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a stand-alone menu option that is not exported with the main menu. The *Other Language Translation Setup* option provides the ability to enter/edit data in the PHARMACY SYSTEM file (#59.7). This option allows sites to enter appropriate terms in another language that make up parts of the SIG when printing prescription bottle labels. If the user does not enter a translation, the English word will print. The *Other Language Translation Setup* option is a stand-alone option that must be assigned to the person(s) responsible for maintaining it. See Appendices C-G for lists of Spanish equivalents for some of the more common terms used for administration schedules, dosage forms, local possible dosages, medication instructions, and medication routes.

> Example: Other Language Translation Setup

## Find Unmapped Local Possible Dosages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS LOCAL DOSAGES EDIT ALL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new option called *Find Unmapped Local Possible Dosages* \[PSS LOCAL DOSAGES EDIT ALL\] is provided to identify all Local Possible Dosages that are eligible for dosage checks and do not have either the Numeric Dose or Dose Unit populated.

> Drugs with the following criteria will be screened out from this option.

- Inactive
- Not Matched to NDF

## All Stand-Alone Menu Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of all stand-alone options that are NOT exported as part of the main PDM menu \[PSS MGR\]:

> \*Other Language Translation Setup \[PSS OTHER LANGUAGE SETUP\]

> Drug Inquiry (IV)

> \[PSSJI DRUG INQUIRY\]

> Electrolyte File (IV)

> \[PSSJI ELECTROLYTE FILE\]

> Enable/Disable Vendor Database Link \[PSS ENABLE/DISABLE DB LINK\]

> *Find Unmapped Local Possible Dosages*

> \[PSS LOCAL DOSAGES EDIT ALL\]

> *Add Default Med Route*

> \[PSS ADD DEFAULT MED ROUTE\]

> ![](pss-1-172-user-manual-change-pages/004.png)The *Enable/Disable Vendor Database Link* option exists ONLY as a way for technical personnel to turn on/off the database connection if required for debugging. Normally, it is enabled and the Vendor Database updates are performed centrally on the MOCHA servers, not at the individual sites. This option is rarely used. It is NOT exported as part of the main PDM menu \[PSS MGR\]

> In the rare case where this option is used and the database link is disabled, NO drug-drug interaction, duplicate therapy, or dosing order checks will be performed in Pharmacy or in the Computerized Patient Record System (CPRS).

> \*Other Language Translation Setup is a stand-alone option that must be assigned to the person(s) responsible for maintaining it.

> *(This page left blank for two-sided copying)*

### From: PSS*1*174 User Manual Change Pages

## Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/13</td>
<td><blockquote>
<p>i-iv, v-vi, 26a-26b,</p>
<p>102a-102f</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*174</p>
</blockquote></td>
<td><ul>
<li><p>Update TOC</p></li>
<li><p>Identical additives and solutions</p></li>
<li><p>Additive and Generic Drug Distinction</p></li>
<li><p>Additive and Generic Drug Distinction, Solution Strength, and Quick Codes</p></li>
<li><p>Additive Strength</p></li>
</ul></td>
</tr>
<tr class="even">
<td>01/13</td>
<td><blockquote>
<p>i - vi, 4 - 4a, 26 – 26b, 100 - 100b,</p>
<p>101a – 101b, 102a</p>
<p>– 102f, 103, 104-</p>
<p>104d, 105, 205 -</p>
<p>208</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*164 &amp; PSS*1*169</p>
</blockquote></td>
<td><ul>
<li><p>Added REQuest Change to Dose Unit example to the Request Change Dose Unit section.</p></li>
<li><p>Added note to Check PEPS Services Setup section.</p></li>
<li><p>Added check options to the Vendor Database Reachable; Enhanced Order Checks Executed example.</p></li>
<li><p>Added Print Interface Data File option</p></li>
<li><p>Added Section 1.21 Inpatient Drug Management as this information was missing from patch PSS*1*146 release.</p></li>
<li><p>Added Section 1.22 Check Drug Interaction option</p></li>
<li><p>Added Find Unmapped Local Possible Dosages option</p></li>
<li><p>Updated the heading number for the Stand-Alone Menu Options section this was previously 1.21 and is now 1.23.</p></li>
<li><p>Updated Index</p></li>
</ul>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>06/12</td>
<td><blockquote>
<p>i, ii, iii, 3-4, 4a – 4b, 44c, 44ib, 44j, 105</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*146</p>
</blockquote></td>
<td>New sub-menu named Inpatient Drug Management [PSS INP MGR]. Enter/Edit dosages Additive Solution enhancement. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/12</td>
<td><blockquote>
<p>i, ii, iii, 27, 44ia – 44ib, 89</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*156</p>
</blockquote></td>
<td><p>New multiple named Outpatient Pharmacy Automation Interface (OPAI) in the DRUG file (#50) sub-file (#50.0906).</p>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/11</td>
<td><blockquote>
<p>i, ii, iii, 38-40b, 62d-64d</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*159</p>
</blockquote></td>
<td>Updated screens. Updated the Edit Orderable Items option for the default medication route. Due to data being moved, pages 62e and 62f have been removed <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/11</td>
<td><blockquote>
<p>i-iii, 101- 101b,</p>
<p>102</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*163</p>
</blockquote></td>
<td><p>Updated the Schedule/Reschedule Check PEPS Interface section</p>
<ul>
<li><p>Updated overview of Schedule/Reschedule Check PEPS Interface</p></li>
<li><p>Updated the Schedule/Reschedule Check PEPS Interface example</p></li>
<li><p>Added a warning regarding the DEVICE FOR</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>QUEUED JOB OUTPUT field</p>
</blockquote>
<ul>
<li><p>Added a blank page for two-sided copying</p></li>
</ul>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/11</td>
<td><blockquote>
<p>i-iii, 3-4b, 7-16b, 44d-j, 114, 118,</p>
<p>121, 129, 137,</p>
<p>204-206</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*155</p>
</blockquote></td>
<td><p>Utilized three new fields that were added to the VA PRODUCT file (#50.68) with PSN*4*261. The fields are used during the Match/Rematch process of the <em>Drug Enter/Edit</em> [PSS DRUG ENTER/EDIT] and the <em>Enter/Edit Dosages</em> [PSS EDIT DOSAGES] options to determine whether possible dosages should be auto-created for supra-therapeutic drugs.</p>
<p>Retired the <em>Auto Create Dosages</em> [PSS DOSAGE CONVER- SION] option and removed the option from the <em>Dosages</em> [PSS DOSAGES MANAGEMENT] menu. Updated Index.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/11</td>
<td><blockquote>
<p>i, ii, iii, added iv, v; changed 3, 4,</p>
<p>45, 46; added 46a- 46d, re-numbered all sections starting on page 87 and ending with page 106; changed page. 89; added 90e and 90f; changed 99-</p>
<p>106; added 106a-b;</p>
<p>deleted 107-112;</p>
<p>changed 151,</p>
<p>153, 154; added 154a-b; updated index;</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*136 &amp; PSS*1*117</p>
</blockquote></td>
<td><p>Besides the developer’s changes, this document incorporates the comments from <mark>REDACTED</mark> and colleagues for the PRE functionality included with patch PSS*1*117 (a combined patch with PSS*1*136).</p>
<p>Sections changed are:</p>
<ul>
<li><p>Changed overview of menu item descriptions to match application</p></li>
<li><p>Changed menu item description named <em><strong>Drug Interaction Management</strong></em> to <em><strong>Order Check Management</strong></em> and changed text</p></li>
<li><p>Changed submenu item <em><strong>Enter/Edit Local Drug Interaction</strong></em> [PSS-INTERACTION-LOCAL-ADD] to <em><strong>Request Changes to Enhanced Order Check Databas</strong></em>e. [PSS ORDER CHECK CHANGES] and changed text.</p></li>
<li><blockquote>
<p>Changed example in <em><strong>Report of Locally Entered Interactions</strong></em> option</p>
</blockquote></li>
</ul>
<p>Section deleted:</p>
<ul>
<li><blockquote>
<p>Deleted <em><strong>Enhanced Order Checks Setup Menu</strong></em> and all its sub-menu items (<em>Find Unmapped Local Medication Routes; Map Local Medication Route to Standard; Medication Route Mapping Report; Medication Route File Enter/Edit; Medication Route Mapping History Report; Request Change to Standard Medication Route; Find Unmapped Local Possible Dosages; Map Local Possible Dosages; Local Possible Dosages Report; Strength Mismatch Report; Enter/Edit Dosages; Request Change to Dose Unit; Mark PreMix Solutions; IV Solution Report; Administration Schedule File Report; Medication Instruction File Report</em>)</p>
</blockquote></li>
</ul>
<p>The deleted Enhanced Order Checks Setup Menu and its submenus is replaced by the following addition:</p>
<ul>
<li><blockquote>
<p>Added <em><strong>PEPS Services</strong></em> menu and its submenus: <em>Check Vendor Database Link; Check PEPS Services Setup; and Schedule/Reschedule PEPS Interface</em></p>
</blockquote></li>
</ul>
<p>Added a heading for <em><strong>Stand-Alone Menu Options</strong></em> with the description for the <em>Enable/Disable Vendor Database Link</em> option and a short description for the <em>Other Language Translation</em></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><p><em>Setup</em> option.</p>
<p>Added definitions in the glossary for PECS and PEPS, and updated the index.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/11</td>
<td><blockquote>
<p>i-ii, 38, 40, 62d-f,</p>
<p>64, 64a</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*153</p>
</blockquote></td>
<td><p>Renamed the MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) to be DEFAULT MED</p>
<p>ROUTE. Provided the ability to print the POSSIBLE MED ROUTES multiple on <em>the Default Med Route For OI Report</em> [PSS DEF MED ROUTE OI RPT] option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/11</td>
<td><blockquote>
<p>i, 63</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*142</p>
</blockquote></td>
<td><p>Added functionality to denote the default med route for IV orders in the selection list in CPRS if all of the orderable items on the order have the same default med route defined. Updated TOC. Released with CPRS version 28.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/10</td>
<td><blockquote>
<p>i, iii, 84, 84a-84b, 203, 205-206</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*143</p>
</blockquote></td>
<td><p>Added new Schedule Validation Requirements. Updated Index.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/10</td>
<td><blockquote>
<p>iii-iv, 3-4, 44a-d,</p>
<p>47-48, 61-62d, 89-</p>
<p>90b, 112, 203-206</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*147</p>
</blockquote></td>
<td><p>Described new process for requesting changes to Standard Medication Routes and the New Term Rapid Turnaround (NTRT) process;</p>
<p>Added <em>IV Additive/Solution Reports</em> menu, with suboptions <em>IV Solution Report</em> option and <em>V Additive Report</em> [PSS IV ADDITIVE REPORT] option</p>
<p>Added <em>Default Med Route for OI Report</em> option to the <em>Medication Routes Management...</em> menu<em>.</em>(this change was made but not documented with PSS*1*140)</p>
<p>Updated <em>Drug Enter/Edit</em> option to display NUMERIC DOSE and DOSE UNIT fields defined for Local Possible Dosage Updated the Drug Enter/Edit option display to include the new ADDITIVE FREQUENCY field</p>
<p>Updated Table of Contents and Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/09</td>
<td><blockquote>
<p>i, 64a-b, 65, 65a-b, 66</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*141</p>
</blockquote></td>
<td><p>Added ASSOCIATED IMMUNIZATION field to <em>Edit Orderable Items</em> option and <em>Dispense Drug/Orderable Item Maintenance</em> option. Reorganized content within sections to accommodate new information.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/09</td>
<td><blockquote>
<p>iii-iv, 53,</p>
<p>62a-b, 63, 81, 203</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*140</p>
</blockquote></td>
<td><p>Added DEFAULT MED ROUTE FOR CPRS field and <em>Default Med Route For OI Report</em> [PSS DEF MED ROUTE OI RPT] option for the enhancement of default medication</p>
<blockquote>
<p>route being defined for an orderable item.</p>
</blockquote>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/09</td>
<td><blockquote>
<p>27-34</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*131</p>
</blockquote></td>
<td><p>Added explanations of DEA special handling code U for sensitive drug.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/09</td>
<td><blockquote>
<p>81</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*137</p>
</blockquote></td>
<td><p>Added Automate CPRS Refill field to the <em>Pharmacy System Parameters Edit</em> [PSS MGR] option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/09</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*129</p>
</blockquote></td>
<td><p>Pages renumbered to accommodate added pages. Pharmacy Reengineering (PRE) V.0.5 Pre-Release. Restructured <em>Pharmacy Data Management</em> menu:</p>
<ul>
<li><p>Grouped related options under the following new sub-menus: <em>Drug Text Management, Medication Instruction Management, Medication Routes Management,</em> and <em>Standard Schedule Management</em></p></li>
<li><p>Added temporary <em>Enhanced Order Checks Setup Menu</em></p></li>
<li><p>Added the following options: <em>Find Unmapped Local Medication Routes, Find Unmapped Local Possible Dosages, Map Local Medication Route to Standard, Map Local Possible Dosages, Mark PreMix Solutions, Request Change to Dose Unit</em>, and <em>Request Change to Standard Medication Route</em></p></li>
<li><p>Added the following reports: <em>Administration Schedule File Report, IV Solution Report, Local Possible Dosages Report, Medication Instruction File Report, Medication Route Mapping Report, Medication Route Mapping History Report,</em> and <em>Strength Mismatch Report</em></p></li>
<li><p>Updated Table of Contents, Index, and Glossary <mark>REDACTED</mark></p></li>
</ul></td>
</tr>
<tr class="even">
<td>09/97</td>
<td></td>
<td></td>
<td>Original Release of User Manual</td>
</tr>
</tbody>
</table>

### Dispense Drug Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[PSSJU DRG\]

> This option allows the user to enter data into fields that are used as default values, and in calculating default values, when the drug is chosen in Unit Dose ORDER ENTRY. This option allows the selection of any drug, including INACTIVE or NON-FORMULARY items.

### Dispense Drug/ATC Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[PSSJU DRUG/ATC SET UP\]

> This allows the user to edit the drug fields necessary to send drugs to ATC Unit Dose dispensing machine. In order for a drug to be sent to the ATC, the drug must have a CANISTER NUMBER for each ward group that will be sending a pick list to the ATC, and the drug must also have a MNEMONIC.

### Edit Cost Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[PSSJU DCC\]

> Allows the user to edit the dispensing cost data used for the cost reports. If any data is changed, a MailMan message is sent to all users holding the PSJU MGR security key (supervisors).

### EDit Drug Cost (IV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[PSSJI EDIT DRUG COST\]

> This menu option allows the cost per unit to be entered for drugs (both additives and solutions).

### MARk/Unmark Dispense Drugs For Unit Dose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[PSSJU MARK UD ITEMS\]

> This allows users to easily mark or unmark items from the Drug file (#50) for use by the Unit Dose Medications package. Only those items marked for Unit Dose are selectable for Unit Dose orders. When the Inpatient Medications package is first installed, it marks all items in the Drug file for use by Unit Dose so that users may immediately continue to use the package. This can be used to unmark those dispense items that Unit Dose users should not be able to select.

### PRimary Solution File (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[PSSJI SOLN\]

> This option is for the applications coordinator to add, change, or inactivate primary solutions used in the IV section. The solution must already exist in the Drug File to be selected here. If use of a primary solution is to be discontinued, the solution should be inactivated by entering an inactivation date, rather than by deleting the solution from the file.
> PSS\*1\*174 enhanced the capabilities of the IV SOLUTIONS File (#52.7) so that a user can enter a new solution that has the same name as an existing entry. Previously, a FileMan workaround had to be used to enter an identically named entry. Now, if the user types in a name that already exists in the file, they will first be presented with a list of available selections. If the user scrolls through the list without selecting an entry, they will be presented with the prompt to add a new entry.
> Example: IV SOLUTIONS File (#52.7)

### From: PSS*1*147 User Manual Change Pages

### \[PSSJI ELECTROLYTE FILE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Electrolyte File (IV)* option allows the contents of the DRUG ELECTROLYTES file (#50.4) to be altered. This file contains the names of anions/cations and their concentration units. The file provides the ability for sites to enter intravenous (IV) orders for electrolytes as individual ingredients so that the IV label will print the total of individual electrolytes rather than the additive names. The ELECTROLYTES sub-file in the IV ADDITIVES file (#52.6) and IV SOLUTIONS file (#52.7) point to this Electrolyte file.

> Example 1: Electrolyte File (Adding)

> Example 2: Electrolyte File (Deleting)

### \[PSS LOOK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Lookup into Dispense Drug File* option provides a lookup into the DRUG file (#50) and displays fields that are commonly edited. It is not possible to edit entries in the DRUG file (#50) from this option. Edits can be made through the use of the *Drug Enter/Edit* option. Patch PSS\*1\*61 ensures that the newly populated CS FEDERAL SCHEDULE field of the VA PRODUCT file (#50.68) is also included as part of the drug details in the *Lookup into Dispense Drug File* option. Patch PSS\*1\*147 adds the Numeric Dose and Dose Unit fields defined for Local Possible Dosages to the display.

> Example 1: Lookup Drug

> Example 1: Lookup Drug continued

<table>
<colgroup>
<col style="width: 82%" />
<col style="width: 1%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>TIMOLOL MALEATE 0.5% OPH SOLN</p>
</blockquote></th>
<th rowspan="21"></th>
<th rowspan="39"></th>
</tr>
<tr class="odd">
<th>=============================================================================</th>
</tr>
<tr class="header">
<th>VA PRINT NAME: TIMOLOL MALEATE 0.5% OPH SOLN CMOP ID#: T0056</th>
</tr>
<tr class="odd">
<th>VA PRODUCT NAME: TIMOLOL MALEATE 0.5% SOLN,OPH CMOP DISPENSE: NO</th>
</tr>
<tr class="header">
<th>ORDERABLE ITEM: TIMOLOL SOLN,OPH NDF DF: SOLN,OPH</th>
</tr>
<tr class="odd">
<th>ORDERABLE ITEM TEXT:</th>
</tr>
<tr class="header">
<th>SYNONYM(S): TIMOPTIC 0.5% Trade Name</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>T/5 Quick Code</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>T.5 Quick Code</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>024208032405 Drug Accountability</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>1677 Quick Code</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>MESSAGE: NATL REVIEW; 5 ML/BT (IEN)</th>
</tr>
<tr class="header">
<th>DEA, SPECIAL HDLG: 6P NDC: 61314-227-05</th>
</tr>
<tr class="odd">
<th>DAW CODE: 5 – SUBSTITUTION ALLOWED-BRAND DRUG DISPENSED AS A GENERIC</th>
</tr>
<tr class="header">
<th>CS FEDERAL SCHEDULE:</th>
</tr>
<tr class="odd">
<th>INACTIVE DATE:</th>
</tr>
<tr class="header">
<th>QUANTITY DISPENSE MESSAGE: ML (5/BT)</th>
</tr>
<tr class="odd">
<th>WARNING LABEL SOURCE is set to 'NEW'</th>
</tr>
<tr class="header">
<th>NEW WARNING LABEL:</th>
</tr>
<tr class="odd">
<th>22N For the eye.</th>
</tr>
<tr class="header">
<th>Pharmacy fill card display: DRUG WARNING 22N</th>
</tr>
<tr class="odd">
<th>ORDER UNIT: BT PRICE/ORDER UNIT: 1.45</th>
<th rowspan="18"></th>
</tr>
<tr class="header">
<th>DISPENSE UNIT: ML VA DISPENSE UNIT: ML</th>
</tr>
<tr class="odd">
<th>DISPENSE UNITS/ORDER UNIT: 5 PRICE/DISPENSE UNIT: 0.2900</th>
</tr>
<tr class="header">
<th>APPL PKG USE: Outpatient Unit Dose</th>
</tr>
<tr class="odd">
<th>STRENGTH: UNIT:</th>
</tr>
<tr class="header">
<th>POSSIBLE DOSAGES:</th>
</tr>
<tr class="odd">
<th>LOCAL POSSIBLE DOSAGES:</th>
</tr>
<tr class="header">
<th><blockquote>
<p>LOCAL POSSIBLE DOSAGE: 1 DROP PACKAGE: IO</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>BCMA UNITS PER DOSE: 1</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NUMERIC DOSE: 1 DOSE UNIT: DROP(S)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>LOCAL POSSIBLE DOSAGE: 2 DROPS PACKAGE: IO</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>BCMA UNITS PER DOSE: 1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NUMERIC DOSE: 2 DOSE UNIT: DROP(S)</p>
</blockquote></th>
</tr>
<tr class="header">
<th>VA CLASS: OP101 BETA-BLOCKERS,TOPICAL OPHTHALMIC</th>
</tr>
<tr class="odd">
<th>LOCAL NON-FORMULARY: VISN NON-FORMULARY:</th>
</tr>
<tr class="header">
<th>National Formulary Indicator: YES</th>
</tr>
<tr class="odd">
<th>National Restriction:</th>
</tr>
<tr class="header">
<th>Local Drug Text:</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example 2: Lookup into Dispense Drug File

<table>
<colgroup>
<col style="width: 82%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Pharmacy Data Management Option: <strong>LOOKUP INTO</strong> Dispense Drug File Select DRUG GENERIC NAME: <strong>LOVASTATIN 20MG TAB</strong> CV350 N/F</p>
<p>RESTRICTED TO CARDIOLOGY SERVICE LOVASTATIN 20MG TAB</p>
<p>============================================================================ VA PRINT NAME: LOVASTATIN 20MG TAB CMOP ID#: L0060</p>
<p>VA PRODUCT NAME: LOVASTATIN 20MG TAB CMOP DISPENSE: YES ORDERABLE ITEM: LOVASTATIN TAB (N/F) NDF DF: TAB ORDERABLE ITEM TEXT:</p>
<p>Refer to PBM/MAP Hyperlipidemia treatment guidelines for use. SYNONYM (S): MEVACOR Trade Name</p>
<p>MESSAGE: THIS IS RESTRICTED TO CARDIOLOGY SERVICE</p></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><p>DEA, SPECIAL HDLG: 6 NDC: 000006-0731-82 CS FEDERAL SCHEDULE:</p>
<p>INACTIVE DATE:</p>
<p>QUANTITY DISPENSE MESSAGE: DISPENSE IN 30'S WARNING LABEL: WITH FOOD</p></th>
</tr>
<tr class="header">
<th>ORDER UNIT: BT PRICE/ORDER UNIT: 50 DISPENSE UNIT: TAB VA DISPENSE UNIT: TAB</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Request Change to Standard Medication Route

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS MEDICATION ROUTE REQUEST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Request Change to Standard Medication Route* option was provided for users to request additions or changes to the STANDARD MEDICATION ROUTES file (#51.23). PSS\*1\*147 changes this option to now refer the requestor to a web site to make the request.

> A list of all Standard Medication Routes and corresponding FDB Route mapping initially released with the PRE V.0.5 Pre-Release patch can be found in Appendix A of the *Pharmacy Reengineering (PRE) Version 0.5 Pre-Release Implementation Guide*. Since then, there have been additions pushed out by the New Term Rapid Turnaround (NTRT) process. For a complete listing use FileMan to print the NAME field (#.01) and FIRST DATABANK MED ROUTE field (#1) from the STANDARD MEDICATION ROUTES file (#51.23)

> Example 1: Request Change to Standard Medication Route

### Standard Medication Routes File Update Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Updates to the Standard Medication Route File are made by the New Term Rapid Turnaround (NTRT) process. Patch PSS\*1\*147 provides MailMan notifications to the mail group PSS ORDER CHECKS when changes occur. The following changes will generate a notification:

- Inactivation of a standard medication route
- Reactivation of a standard medication route
- Addition of a new standard medication route
- Change (add/delete/modify) to a FDB medication route mapping
- Change (add/delete/modify) to a replacement route for a standard medication route Changes to a standard medication route that can result in an unmapping of a local medication route are:
- Inactivation of a standard medication route
- Change (add/delete/modify) to an FDB Medication Route Mapping

> If a local medication route that is marked for ‘All Packages’ is unmapped, the software will attempt to do an automatic remapping to an active standard medication route. If the unmapping occurred due to an inactivation of the standard medication route and a replacement route is provided, the local medication route will be remapped to the new standard replacement route. If no replacement route was provided in the update, a defined set of business rules will be used to attempt an automatic remapping to another standard medication route.

> The MailMan message will include the reason for notification, what was updated and will also include any automatic mapping activities that occurred from the local Medication Routes file to the Standard Medication Routes file.

> Example 1: Addition of New Standard Medication Route

> Subj: Standard Medication Route File Update \[#136380\] 08/21/09@09:58 64 lines From: STANDARD MEDICATION ROUTE FILE PROCESSOR In 'IN' basket. Page 1 \*New\*

> The following entries have been added to the Standard Medication Routes (#51.23) File:

> ENTERAL

> FDB Route: ORAL

> The following entries have been inactivated in the Standard Medication Routes (#51.23) File:

> (None)

> The following entries have been reactivated in the Standard Medication Routes (#51.23) File:

> (None)

> The following entries in the Medication Routes (#51.2) File have been mapped/remapped to a Standard Medication Route (#51.23) File entry.

> G-TUBE

> Previous Standard Route: ORAL New Standard Route: ENTERAL

> PLEASE REVIEW, MAY REQUIRE YOUR ATTENTION!

> The following entries in the Medication Routes (#51.2) File have been unmapped from a Standard Medication Route (#51.23) File entry.

> (None)

> The following entries in the Standard Medication Routes (#51.23) File have had changes to the associated First DataBank Med Route and/or Replacement Term.

> (None)

> The following entries in the Medication Routes (#51.2) File were to be mapped/remapped to a Standard Medication Route (#51.23) File entry, but could not occur because the Medication Route (#51.2) File entry was locked.

> J-TUBE

> Current Standard Route: ORAL

> Recommend mapping to Standard Route: ENTERAL

> The following entries in the Medication Routes (#51.2) File were to be unmapped from a Standard Medication Route (#51.23) File entry, but

> could not occur because the Medication Route (#51.2) File entry was locked. (None)

> Enter message action (in IN basket): Ignore //

> Example 2: Inactivation of Standard Medication Routes; one with a Replacement Route and the other without

> Subj: Standard Medication Route File Update \[#136380\] 08/21/09@09:58 64 lines From: STANDARD MEDICATION ROUTE FILE PROCESSOR In 'IN' basket. Page 1 \*New\*

> The following entries have been added to the Standard Medication Routes (#51.23) File:

> INTRA-URETHRAL

> FDB Route: INTRA-URETHRAL

> The following entries have been inactivated in the Standard Medication Routes (#51.23) File:

> URETHRAL

> FDB Route: INTRA-URETHRAL

> Replacement Term: INTRA-URETHRAL Replacement Term FDB Route: INTRA-URETHRAL

> INTRAVITREAL

> FDB Route: INTRAVITREAL

> Replacement Term: (None) Replacement Term FDB Route: (None)

> The following entries have been reactivated in the Standard Medication Routes (#51.23) File:

> (None)

> The following entries in the Medication Routes (#51.2) File have been mapped/remapped to a Standard Medication Route (#51.23) File entry.

> URETHRAL

> Previous Standard Route: URETHRAL New Standard Route: INTRA-URETHRAL

> PLEASE REVIEW, MAY REQUIRE YOUR ATTENTION!

> The following entries in the Medication Routes (#51.2) File have been unmapped from a Standard Medication Route (#51.23) File entry.

> INTRAVITREAL

> Previous Standard Route: INTRAVITREAL New Standard Route: (None)

> The following entries in the Standard Medication Routes (#51.23) File have had changes to the associated First DataBank Med Route and/or Replacement Term.

> (None)

> The following entries in the Medication Routes (#51.2) File were to be mapped/remapped to a Standard Medication Route (#51.23) File entry, but could not occur because the Medication Route (#51.2) File entry was locked.

> (None)

> The following entries in the Medication Routes (#51.2) File were to be unmapped from a Standard Medication Route (#51.23) File entry, but

> could not occur because the Medication Route (#51.2) File entry was locked. (None)

> Example 3: Remapping and Unmapping could not occur due to locked file

> Example 4: Reactivated Standard Medication Route

> Subj: Standard Medication Route File Update \[#136380\] 08/21/09@09:58 64 lines From: STANDARD MEDICATION ROUTE FILE PROCESSOR In 'IN' basket. Page 1 \*New\*

> The following entries have been added to the Standard Medication Routes (#51.23) File:

> (None)

> The following entries have been inactivated in the Standard Medication Routes (#51.23) File:

> (None)

> The following entries have been reactivated in the Standard Medication Routes (#51.23) File:

> INTRADUCTAL

> FDB Route: INTRADUCTAL

> The following entries in the Medication Routes (#51.2) File have been mapped/remapped to a Standard Medication Route (#51.23) File entry.

> (None)

> PLEASE REVIEW, MAY REQUIRE YOUR ATTENTION!

> The following entries in the Medication Routes (#51.2) File have been unmapped from a Standard Medication Route (#51.23) File entry.

> (None)

> The following entries in the Standard Medication Routes (#51.23) File have had changes to the associated First DataBank Med Route and/or Replacement Term.

> INTRADUCTAL

> Replacement Term: \<deleted\>

> The following entries in the Medication Routes (#51.2) File were to be mapped/remapped to a Standard Medication Route (#51.23) File entry, but could not occur because the Medication Route (#51.2) File entry was locked.

> (None)

> The following entries in the Medication Routes (#51.2) File were to be unmapped from a Standard Medication Route (#51.23) File entry, but

> could not occur because the Medication Route (#51.2) File entry was locked. (None)

> Enter message action (in IN basket): Ignore //

## Default Med Route for OI Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS DEF MED ROUTE OI RPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Default Med Route for OI Report* option is listed on the *Medication Routes Management* \[PSS MEDICATION ROUTES MGMT\] menu. This report can be used to help identify the current default medication routes for the orderable items. The following is an example of the report.

### \[PSS MASTER FILE ALL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option sends updated information for every entry in the DRUG file (#50) to the external interface for Outpatient Pharmacy dispensing systems, using HL7 standard V. 2.4 messages. All entries are sent, regardless of how they are marked for Application Package Use.

> To use this option, the following items must be set up properly in the OUTPATIENT SITE file (#59):

- In the AUTOMATED DISPENSE field (#105), the value should be set to V. 2.4. This enables sending data through the Interface Engine using HL7 V. 2.4 standard.
- In the ENABLE MASTER FILE UPDATE field (#105.2), the value should be set to

> YES.

- In the DISPENSE DNS NAME field (#2006), there should be some value defined. This value sends the DNS name of the dispensing system (for example, dispensemachine1.vha.med.va.gov) to the Interface Engine, so that the Interface Engine knows where to route the HL7 messages.

> Example: Send Entire Drug File to External Interface

> The *Enhanced Order Checks Setup Menu* options are located here on the main menu. Because this menu will be removed when PRE V.0.5 is released, the descriptions have been moved to the end of this chapter (1.23).

### \[PSS ADDITIVE/SOLUTION REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *IV Additive/Solution Reports* option was created by Patch PSS\*1\*147 to provide an umbrella for all the options related to reviewing IV Additive and IV Solution data.

## IV Additive Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS IV ADDITIVE REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PSS\*1\*147 creates a new *IV Additive Report* option to display IV Additive information. A user can select to display only entries marked with '1 BAG/DAY' in the Additive Frequency field, or only those entries with nothing entered in the Additive Frequency field, or all entries can be displayed. The report will print the following data elements:

- Print Name
- Generic Drug
- Drug Unit
- Synonyms
- Pharmacy Orderable Item
- Inactivation Date
- Used in IV Fluid Order Entry
- Additive Frequency

> If the user chooses to print only the IV Additives marked with ‘1 BAG/DAY’ in the Additive Frequency field or those entries with nothing entered in the Additive Frequency field and none are found, the report will display ‘No IV Additives marked as '1 BAG/DAY' or ‘No IV Additives marked as null’ respectively.

> Example 1: User selects only IV Additives marked with no value in the Additive Frequency Field

> Example 2: User Selects Only IV Additives marked with ‘1BAG/DAY’ in the Additive Frequency Field

> Example 3: User selects all IV Additives

> Select one of the following:

> 1 Print entries marked as '1 BAG/DAY' for ADDITIVE FREQUENCY N Print entries marked as Null for ADDITIVE FREQUENCY

> A Print all IV Additives

> Print which IV Additives: A// \<ENTER\> Print all IV Additives

> This report is designed for 80 column format!

> DEVICE: HOME// \<ENTER\>

> All IV Additives Page: 1

> Print Name: AMINOPHYLLINE Drug Unit: MG

> Synonyms:

> Generic Drug: AMINOPHYLLINE 25MG/ML 20ML INJ

> Pharmacy Orderable Item: AMINOPHYLLINE INJ,SOLN Inactivation Date:

> Used in IV Fluid Order Entry: YES

> Additive Frequency: ALL BAGS

> Print Name: CALCIUM GLUCONATE

> Drug Unit: MEQ Synonyms: CAGLUC

> Generic Drug: CALCIUM GLUCONATE 1GM

> Pharmacy Orderable Item: CALCIUM GLUCONATE INJ,SOLN Inactivation Date:

> Used in IV Fluid Order Entry: YES

> Additive Frequency:

> Print Name: HEPARIN Drug Unit: UNITS

> Synonyms:

> Generic Drug: HEPARIN 10,000 UNITS 4ML

> Pharmacy Orderable Item: HEPARIN INJ,SOLN Inactivation Date:

> Used in IV Fluid Order Entry: YES

> Additive Frequency: ALL BAGS

> Print Name: TRACE ELEMENTS Drug Unit: ML

> Synonyms:

> Generic Drug: TRACE ELEMENTS 5ML INJ

> Pharmacy Orderable Item: TRACE ELEMENTS INJ,CONC-SOLN Inactivation Date:

> Used in IV Fluid Order Entry: YES

> Additive Frequency: 1 BAG/DAY

> End of Report.

## IV Solution Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS IV SOLUTION REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *IV Solution Report* option displays only IV solutions marked as PreMixes or all IV solutions.

> The report will print the following data elements:

- Print Name
- Print Name {2}
- Volume
- Synonyms
- Generic Drug
- Pharmacy Orderable Item
- Inactivation Date
- Used in IV Fluid Order Entry
- PreMix

> If the user chooses to print only the IV solutions marked as PreMixes and none are found the report will display ‘No IV Solutions marked as PreMixes found.’

> Example 1: User selects only solutions marked as PreMix

> Example 2: User Selects all IV Solutions

> P Print only IV Solutions marked as PreMix A Print All IV Solutions

> Print report for PreMix (P), or All IV Solutions (A): (P/A): Premix: P// a Print All IV Solutions

> This report is designed for 80 column format!

> DEVICE: HOME// \<ENTER\>

> Solution PreMix report for all IV Solutions Page: 1

> Print Name: 0.9% SODIUM CHLORIDE Volume: 100 ML Print Name {2}:

> Synonyms: 2673

> Generic Drug: SODIUM CHLORIDE 0.9% 100ML

> Pharmacy Orderable Item: SODIUM CHLORIDE INJ Inactivation Date:

> Used in IV Fluid Order Entry: YES

> PreMix:

> Print Name: 0.9% SODIUM CHLORIDE Volume: 50 ML Print Name {2}:

> Synonyms: 2672

> Generic Drug: SODIUM CHLORIDE 0.9% 50ML

> Pharmacy Orderable Item: SODIUM CHLORIDE INJ Inactivation Date:

> Used in IV Fluid Order Entry: YES

> PreMix:

> Print Name: 20% DEXTROSE Volume: 500 ML Print Name {2}:

> Synonyms:

> Generic Drug: DEXTROSE 20% IN WATER 500ML

> Pharmacy Orderable Item: DEXTROSE INJ,SOLN Inactivation Date:

Used in IV Fluid Order Entry: YES

PreMix:

> Print Name: METRONIDAZOLE 500MG IN NACL Volume: 100 ML

Print Name {2}:

Synonyms:

> Generic Drug: METRONIDAZOLE 500MG/100ML NACL

> Pharmacy Orderable Item: METRONIDAZOLE/SODIUM CHLORIDE INJ,SOLN Inactivation Date:

Used in IV Fluid Order Entry: YES

PreMix: YES

> End of Report.

## Enter/Edit Dosages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS EDIT DOSAGES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Enter/Edit Dosages* option has previously been described in this manual under the *Dosages*

> menu*.*

## Request Change to Dose Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS DOSE UNIT REQUEST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Request Change to Dose Unit* option has been described in this manual under the *Dosages*

> menu.

## Mark PreMix Solutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS MARK PREMIX SOLUTIONS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Mark PreMix Solutions* option allows a user to quickly mark an IV Solution as a PreMix. The following data fields can be edited:

- Print Name
- Print Name {2}
- Generic Drug
- Volume
- Inactivation Date
- Used in IV Fluid Order Entry
- PreMix

> After successful edit of an entry, the user will be prompted to enter another IV Solution to edit. Press \<ENTER\>, to exit out of the option.

> February 2009 Pharmacy Data Management V. 1.0 111

> User Manual

## IV Solution Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS IV SOLUTION REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *IV Solution Report* option has been described in this manual under the IV Additive/Solution Reports menu option.

## Administration Schedule File Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS SCHEDULE REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Administration Schedule File Report* option has been described in this manual under the

> *Standard Schedule Management* sub-menu.

## Medication Instruction File Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS MED INSTRUCTION REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Medication Instruction File Report* option has been described in this manual under the

> *Medication Instruction Management* sub-menu.

> <span id="_bookmark9" class="anchor"></span>112 Pharmacy Data Management V. 1.0 February 2010

### From: PSS*1*146 User Manual Change Pages

## CMOP Mark/Unmark (Single drug)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[PSSXX MARK\]

> The *CMOP Mark/Unmark (Single drug)* option allows the user to mark/unmark a single drug for transmission to the Consolidated Mail Outpatient Pharmacy (CMOP). Pertinent DRUG file (#50) and VA PRODUCT file (#50.68) fields shall be displayed to the user for review whenever a drug is marked or unmarked for CMOP transmission.

> If the user marks the entry to transmit to CMOP, it will replace the Dispense Unit with the VA Dispense Unit. In addition, if the user overwrites the local drug name with the VA Print Name, the entry may not be edited. The VA Print Name will be displayed on all profiles and prescription labels if the local drug name is overwritten with the VA Print Name. The local drug name will no longer be selectable during order entry.

> If the user chooses not to overwrite the local drug name with the VA Print Name, the local drug name will continue to be displayed on all profiles and can be used for drug selection during order entry. The VA Print Name will be displayed on all prescription labels regardless of the local drug name.

> A drug cannot be marked for CMOP if:

1.  It is inactive in DRUG file (#50) or VA PRODUCT file (#50.68).
2.  It is not marked for Outpatient Medications use.
3.  It is not matched to National Drug File.
4.  It is a Schedule I or II narcotic.
5.  It is not marked for CMOP in National Drug File.

> The ability to mark/unmark a single drug for CMOP transmission is also available utilizing the

> *Drug Enter/Edit* option.

> ![](pss-1-146-user-manual-change-pages/004.png) Locked: PSXCMOPMGR

> Without the PSXCMOPMGR key, the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

> ![](pss-1-146-user-manual-change-pages/005.png)LOCAL DRUG NAME: TIMOLOL 0.5% OPTH SOL 10ML

> ORDER UNIT: BT DISPENSE UNITS/ORDER UNITS: 1

> DISPENSE UNIT:

> VA PRODUCT NAME: TIMOLOL MALEATE 0.5% SOLN,OPH

> VA PRINT NAME: TIMOLOL MALEATE 0.5% OPH SOLN CMOP ID: T0056

> VA DISPENSE UNIT: ML MARKABLE FOR CMOP: YES PACKAGE SIZE: 10 ML

> PACKAGE TYPE: BOTTLE

> VA CLASS: OP101 BETA-BLOCKERS,TOPICAL OPHTHALMIC CS FEDERAL SCHEDULE:

> INGREDIENTS:

> TIMOLOL MALEATE 0.5 % NATIONAL FORMULARY INDICATOR: YES NATIONAL FORMULARY RESTRICTION:

> \< Enter "Y" for yes, "N" for no \>

> Is this a match ? Y

> You have just VERIFIED this match and MERGED the entry.

> Resetting Possible Dosages..

> Press Return to continue: \<ENTER\>

> Do you want to merge new Local Possible Dosages? Y// NO

> Just a reminder...you are editing TIMOLOL 0.5% OPTH SOL 10ML.

> Do you want to edit Local Possible Dosages? N// YES

> Do you want to merge new Local Possible Dosages? Y// NO

> .

> .

> 44b Pharmacy Data Management V. 1.0 February 2009

> ![](pss-1-146-user-manual-change-pages/006.png)Example 2: Editing Additive Frequency for IV Additive

> Select Pharmacy Data Management Option: Drug Enter/Edit

> Select DRUG GENERIC NAME: CIMETIDINE 150MG/ML MDV INJ (8ML) GA301

> ...OK? Yes// \<ENTER\> (Yes)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* This entry is marked for the following PHARMACY packages:

> IV

> Ward Stock

> GENERIC NAME: CIMETIDINE 150MG/ML MDV INJ (8ML) Replace \<ENTER\> VA CLASSIFICATION: GA301// \<ENTER\>

> DEA, SPECIAL HDLG: \<ENTER\> DAW CODE: \<ENTER\>

> .

> .

> .

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* This entry is marked for the following PHARMACY packages:

> IV

> Ward Stock

> MARK THIS DRUG AND EDIT IT FOR:

> O - Outpatient U - Unit Dose I - IV

> W - Ward Stock

> D - Drug Accountability

> C - Controlled Substances X - Non-VA Med

> A - ALL

> Enter your choice(s) separated by commas : I

> I - IV

> \*\* You are NOW editing IV fields. \*\*

> AN IV ITEM? Yes// \<ENTER\> (Yes)

> Edit Additives or Solutions:

> Select one of the following:

> A ADDITIVES

> S SOLUTIONS

> Enter response: ADDITIVES

> <span id="_bookmark2" class="anchor"></span>Select IV SOLUTIONS PRINT NAME: CIMETIDINE// \<ENTER\>

> PRINT NAME: CIMETIDINE// \<ENTER\>

> Select DRUG GENERIC NAME: CIMETIDINE 150MG/ML MDV INJ (8ML)// \<ENTER\>

> ARE YOU SURE YOU WANT TO SELECT CIMETIDINE 150MG/ML MDV INJ (8ML) ? No// Y (Yes) USED IN IV FLUID ORDER ENTRY: YES// \<ENTER\>

> DRUG UNIT: MG// \<ENTER\>

> NUMBER OF DAYS FOR IV ORDER: \<ENTER\> USUAL IV SCHEDULE: \<ENTER\> ADMINISTRATION TIMES: \<ENTER\>

> Select QUICK CODE: \<ENTER\>

> AVERAGE DRUG COST PER UNIT: \<ENTER\> Select ELECTROLYTE: \<ENTER\>

> Select SYNONYM: \<ENTER\> DRUG INFORMATION: \<ENTER\>

> 1\>

> INACTIVATION DATE: \<ENTER\> CONCENTRATION: \<ENTER\> MESSAGE: \<ENTER\>

> ADDITIVE FREQUENCY: ALL BAGS// \<ENTER\>

> Edit Additives or Solutions: \<ENTER\>

> Select one of the following:

> June 2012 Pharmacy Data Management V. 1.0 44c User Manual

#### Multiple Automated Dispensing Devices (ADD)

> Patch PSS\*1\*156, in conjunction will PSO\*7\*354, allows sites to send prescriptions to multiple ADDs. Defining a dispensing device at the drug level for a division will override the dispensing device settings in the OUTPATIENT SITE File (#59). If populated, the drug will be sent to the dispensing device for that division. There are two types of ADDs, window and mail, and these are based on the route of the prescription. The prompt “OP EXTERNAL DISPENSE:” must be YES for an ADD to be added to a drug. The following example illustrates the set-up for the drug CIMETIDINE 200MG TAB to be sent to the dispensing device SCRIPTPRO1 for window prescriptions and SCRIPTPRO2 for mail prescriptions.

> Example 1: Assigning Dispensing Device for a Drug

> 44ia Pharmacy Data Management V. 1.0 February 2009

> The following actions will apply when OP EXTERNAL DISPENSE field (#28) is YES:

- To change where a drug is being routed, simply change the ADD associated with the drug.

> ADDs can be removed from an ADD defined in the DRUG file (#50) for specific drugs for a site.

- If the response to OP EXTERNAL DISPENSE field (#28) is NO, then there will be no prompt to add an ADD.

> <span id="_bookmark3" class="anchor"></span>Patch PSS\*1\*146 addresses a functionality change to prevent erroneous matching with Dispense Drugs. It is very easy to select the wrong item and incorrectly change the PRINT NAME field (#.01) of the IV ADDITIVES file (#52.6) and/or IV SOLUTIONS file (#52.7). Also, once an additive or solution is selected, it is unclear as to whether or not the user is still selecting or editing.

> Patch PSS\*1\*146 enhances this process by displaying the previously entered Print Name as the default if only one is entered.

> Example:

> If more than one Print Name were previously entered, the software will display the list of all linked Additives and/or Solutions to select from so an edit may be made.

> June 2012 Pharmacy Data Management V. 1.0 44ib User Manual

> <span id="_bookmark4" class="anchor"></span>Example:

> The Patch PSS\*1\*146 enhancement also allows the user to enter a new Additive or Solution and link it to the dispense drug. The software will give the user the choice to enter and link the dispense drug to a new Additive or Solution as well as require a confirmation of the selected dispense drug that will be linked to the selected Additive/Solution.

> Example (Create new IV Additive and link to drug):

> 44j Pharmacy Data Management V. 1.0 June 2012 User Manual

### From: PSS*1*155 User Manual Change Pages

### Stand-Alone Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *\*Enable/Disable Vendor Database Link is a stand-alone option that is to be used ONLY by* technical personnel to turn on/off the database connection if required for debugging. Normally it is enabled and the Vendor Database updates are performed centrally in Austin and Martinsburg, not at the individual sites. This option is rarely used. *It is NOT exported as part of the main PDM menu \[PSS MGR\]*
> \*Other Language Translation Setup is a stand-alone option that must be assigned to the person(s) responsible for maintaining it.

### Dosage Form File Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[PSS DOSAGE FORM EDIT\]

> The *Dosage Form File Enter/Edit* option provides the ability to edit data in the DOSAGE FORM file (#50.606). Changes made using this option may affect the way CPRS and Outpatient Pharmacy SIGs display and how Local Possible Dosages are created. The Noun entries are used to populate the Local Possible Dosages for DRUG file (#50) entries, when these entries are matched to National Drug File. These Nouns may be package specific (i.e. Outpatient Pharmacy, Inpatient Medications, or both). Entries in this file will be used as default values in the construction of the Outpatient Pharmacy prescription SIG.

> The conjunction will be used to provide a connector between the Local Possible Dosage and the strength and units or Dispense Drug name when displaying the dosage list through CPRS. For example, the dosage 1 TEASPOONFUL GUAIFENESIN WITH DEXTROMETHORPHAN SYRUP would display as 1 TEASPOONFUL OF GUAIFENESIN WITH

> DEXTROMETHORPHAN SYRUP in CPRS after the conjunction “OF” was provided using the

> *Dosage Form File Enter/Edit* option.

> The *Dosage Form File Enter/Edit* option allows the user to associate one or more local medication routes with a dosage form. The user will only be able to select a local medication route that has already been defined in the MEDICATION ROUTES file (#51.2).

> The *Dosage Form File Enter/Edit* option allows the user to enter a noun, verb, or preposition in a language other than English. PDM does not translate English terms into another language; instead, it allows the user to enter a translation of a term. If a value has not been entered in the OTHER LANGUAGE VERB, OTHER LANGUAGE PREPOSITION, or OTHER

> LANGUAGE NOUN fields, PDM defaults to the values entered in the VERB, PREPOSITION, or NOUN fields. If the VERB, PREPOSITION, or NOUN fields do not contain data for the selected item, the system will not display default values for those fields during CPRS or Outpatient Pharmacy prescription order entry processing. However, when building the SIG, Outpatient Pharmacy will default to the values the user input during order entry. See Appendix D for a list of Spanish equivalents for some of the more common dosage forms.

> Example: Dosage Form File Enter/Edit

## Diagram B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pss-1-155-user-manual-change-pages/010.png)

> Diagram B

> Diagram B shows the drug entry with the new data. Two new fields, STRENGTH and UNIT, have been added to the DRUG file (#50). These two fields are populated with data based on the data contained in the STRENGTH and UNITS fields of the VA PRODUCT file (#50.68) match. The DOSE field of the POSSIBLE DOSAGE sub-file of the DRUG file (#50) is populated by multiplying the entry in the DISPENSE UNITS PER DOSE field of the POSSIBLE DOSAGE sub-file of DRUG file (#50) by the numeric value of the STRENGTH field in the DRUG file (#50). (DOSE=DISPENSE UNITS PER DOSE x STRENGTH)

> Diagram C shows dosage selections for a PROPRANOLOL TAB Orderable Item when one or more drugs are matched to that Orderable Item. (See Diagram C.)

> Additionally, another screen that is used for duplicate doses is the non-formulary screen.

![](pss-1-155-user-manual-change-pages/011.png)

> The non-formulary drug filter is executed prior to the lowest Dispense Units Per Dose filter. So in this example, if the PROPRANOLOL HCL 40MG TAB is marked as non-formulary, and the PROPRANOLOL HCL 20MG TAB is formulary, the 40MG dosage selection would be associated with the PROPRANOLOL HCL 20MG TAB, even though it has a higher Dispense Units Per Dose (2) than the 40MG entry for PROPRANOLOL HCL 40MG TAB (1 Dispense Units Per Dose).

> Once the Possible Dosages have been created, doses can be deleted or added by editing the DISPENSE UNITS PER DOSE field using the *Enter/Edit Dosages* option. The DOSE field is automatically calculated by multiplying the DISPENSE UNITS PER DOSE field times the STRENGTH field. For example, if the PROPRANOLOL TABLET is commonly given in a 10MG dose, and there is not a Dispense Drug entry in DRUG file (#50) of PROPRANOLOL HCL 10MG TAB, a Dispense Units Per Dose of .5 can be added for the PROPRANOLOL HCL 20MG TAB, and a dose of 10MG will be created. If a dose of 60MG is sometimes given for PROPRANOLOL TAB, entering a Dispense Units Per Dose of 3 for the PROPRANOLOL HCL 20MG TAB drug will provide a 60MG dose. Similarly, if the 80MG dose is rarely given, the Dispense Units Per Dose of 2 can be deleted for the PROPRANOLOL HCL 40MG TAB drug, and the 80MG dose will be deleted.

> The PACKAGE field can also be edited, but this is a “controlled” type of edit. If the Dosage Form/Unit Combination is not marked as convertible in the DOSAGE FORM file (#50.606) for the package, then that package cannot be added as a package for that Possible Dosage. Strength can also be edited in the DRUG file (#50). If the strength is edited, then all of the doses are automatically re-calculated based on the DISPENSE UNITS PER DOSE and new STRENGTH entry. It is recommended that the strength only be edited in the rare case that the Dispense Drug must be matched to a VA Product with an inappropriate strength. (This scenario is discussed in further detail later in this document.) In summary, by adding new DISPENSE UNITS PER DOSE of .5 and 3 to the PROPRANOLOL HCL 20MG TAB entry, and by deleting the DISPENSE UNITS PER DOSE of 2 for the PROPRANOLOL HCL 40MG TAB entry, the

> following Possible Dosages now exist for PROPRANOLOL TAB Orderable Item. (See Diagram D.)

## Diagram D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pss-1-155-user-manual-change-pages/012.png)

> Diagram G (continued)

> These two drugs meet the first three of the Possible Dosages criteria, but do not meet criteria number four. The Dosage Form/Unit Combination of SOLN,OPH / % is not marked as convertible in the DOSAGE FORM file (#50.606) for Inpatient Medications or for Outpatient Pharmacy. Since Possible Dosages cannot be created for these drugs, Local Possible Dosages must be created. To create Local Possible Dosages the Noun field in the DOSAGE FORM file (#50.606) is utilized. By default, all Local Possible Dosages will be marked for Inpatient Medications and/or Outpatient Pharmacy use based on the package identification of the Noun.

> The NOUN field already exists in the DOSAGE FORM file (#50.606). It is a multiple field, meaning that more than one Noun can be associated with each Dosage Form. Some Dosage Forms may have multiple Nouns, while other Dosage Forms may have only one Noun. For example, the Dosage Form CREAM could have the following entries in the NOUN field.

> Alternately, the Dosage Form of TAB would most likely only have one NOUN, TABLET(S).

> TABLET(S)

> In the TIMOLOL example, a review of the Dosage Form entry for SOLN,OPH, shows that the Dispense Units Per Dose of 1 and 2 are designated, and a Noun of DROP(S) is specified. If the *Auto Create Dosages* option is rerun with the current setup, no Possible Dosages for the two TIMOLOL drugs will be created because the drugs do not meet all four Possible Dosages criteria. Local Possible Dosages will be created of 1 DROP and 2 DROPS.

> If a NOUN ends in “(S)” or “(s)”, such as TABLET(S) or capsule(s), the “(S)” or “(s)” will be completely dropped from the Noun when building the SIGs, as long as the Dispense Units Per Dose is 1 or less. If the Dispense Units Per Dose is greater than 1, the parenthesis around the “(S)” will be eliminated, creating a plural Noun, such as TABLETS. For this to happen, the Noun must precisely end in the three characters “(S)”.

> Keep in mind that if an Orderable Item is selected in CPRS, and there are Possible Dosages for any of the Dispense Drugs tied to that Orderable Item, only the Possible Dosages will be returned and any Local Possible Dosages will be ignored. Local Possible Dosages will only be used when no Possible Dosages can be found for drugs tied to the selected Orderable Item and identified for use by the selected application (Inpatient Medications or Outpatient Pharmacy).

> In the TIMOLOL example, the Noun of DROP(S) and the Dosage Form of SOLN, OPH produces the following results. (See Diagram H.)

### From: PSS*1*142 User Manual Change Pages

## Edit Orderable Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS EDIT ORDERABLE ITEMS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Edit Orderabl*e *Items* option allows the user to enter and edit data in the PHARMACY ORDERABLE ITEM file (#50.7). If a Pharmacy Orderable Item Drug Text Entry is identified at the “OI-DRUG-TEXT” prompt, it will be viewable during medication order entry processes through CPRS, Outpatient Pharmacy, and Inpatient Medications. Pharmacy Orderable Item defaults can be entered for selected fields. These defaults will be displayed to the user during the medication order entry processes for all applications through which medication orders can be entered.

> The *Edit Orderable Items* option allows the user to enter a default medication route. If a default medication route has been defined for an orderable item and the Default Med Route for CPRS field is set to YES (see the *Pharmacy System Parameters Edit* \[PSS SYS EDIT\] section for details), that default medication route will be the only route displayed for selection from the

> drop-down list on the CPRS Inpatient Medications dialog and the Outpatient Pharmacy dialog. If all of the orderable items on the order have the same default med route defined, the default med route will be denoted in the selection list in CPRS. However, the provider can still type in a valid medication route or valid medication route abbreviation to change the medication route for the order. If the Default Med Route for CPRS is set to NO and a default medication route has been defined for an orderable item, the medication route in the order dialog will be the default medication route; however the additional medication routes associated with the dosage form will display for selection from the drop-down list. If a default medication route has not been defined for the orderable item, all possible medication routes for the dosage form will be available for the provider to select in CPRS.

> ![](pss-1-142-user-manual-change-pages/002.png)![](pss-1-142-user-manual-change-pages/003.png)![](pss-1-142-user-manual-change-pages/004.png)Additionally, a report is available to view all current default medication routes for the listed orderable items. See the section entitled *Default Med Route For OI Report* \[PSS DEF MED ROUTE OI RPT\].

> The *Edit Orderable Items* option allows the user to enter patient instructions in a language other than English. PDM does not translate English terms into another language; instead, it allows the user to enter a translation of a term. If a value has not been entered in the OTHER LANGUAGE INSTRUCTIONS field, PDM will default to the value entered in the PATIENT INSTRUCTIONS field. If the PATIENT INSTRUCTIONS field does not contain data for the selected orderable item, the system will not present default patient instructions to the user during CPRS or Outpatient Pharmacy prescription order processing. However, when building the SIG, Outpatient Pharmacy will default to the value the user input through backdoor Outpatient Pharmacy order entry.

> February 2011 Pharmacy Data Management V. 1.0 63

> User Manual PSS\*1\*142

> Example: Editing Pharmacy Orderable Items

> Example: Editing Pharmacy Orderable Items (continued)

> 64 Pharmacy Data Management V. 1.0 February 2011 User Manual

> PSS\*1\*142

### \[PSS SCHEDULE MANAGEMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Standard Schedule Management* option was created to provide an umbrella for all the options related to working with standard schedules.

## Standard Schedule Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSS SCHEDULE EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Standard Schedule Edit* option allows the user to enter or edit entries in the ADMINISTRATION SCHEDULE file (#51.1). The set of times associated with the standard dosage administration schedules can be assigned, as can ward-specific administration times. This feature may be used to define the outpatient expansion to be used when the schedule is entered for an Outpatient Pharmacy medication order. Entry of a frequency in minutes allows the software to calculate the interval between dosages for Inpatient Medication orders and BCMA and is used by Outpatient Pharmacy to calculate default quantities. When the frequency is entered, a message displays telling the user, in hours, how often the administration will occur. If the schedule type is on call, the system does not require a frequency.

> Schedules with a frequency that is not evenly divisible into or by 24 hours are considered ‘odd’. Odd schedules are not allowed to have administration times. If the schedule type is continuous and it is an odd schedule, the system does not allow the entry of administration times.

> Continuous, non-odd schedules still require administration times.

> The *Standard Schedule Edit* option allows the user to enter the outpatient expansion value in a language other than English. PDM does not translate English terms into another language; instead, it allows the user to enter a translation of a term. If a value has not been entered in the OTHER LANGUAGE EXPANSION field, PDM defaults to the value entered in the OUTPATIENT EXPANSION field. If no values exist in the OUTPATIENT EXPANSION and OTHER LANGUAGE EXPANSION fields, the system will not present default values for those fields to the user during CPRS or Outpatient Pharmacy prescription order processing. However, when building the SIG, Outpatient Pharmacy will default to the value the user input through Outpatient Pharmacy backdoor order entry. See Appendix C for a list of Spanish equivalents for some of the more common administration schedules.

> In order to perform a daily dose range check on a prescribed medication, the software needs to determine how many times per day the single dosage is taken. The schedule from an order will be used to obtain that information. If the schedule is found, the value in the FREQUENCY (IN MINUTES) field (#2) in the ADMINISTRATION SCHEDULE file (#51.1) will be used to calculate the frequency.

> If a frequency cannot be determined, a daily dose range check will not be performed. The user will be informed of this and a reason given as to why. A maximum single dose check will still be performed and general dosing information for the drug will be provided.

> February 2009 Pharmacy Data Management V. 1.0 83

> User Manual

> If the type of schedule for an administration schedule used for an order is designated as ONE- TIME or ON CALL or if the Schedule Type for a Unit Dose order is ONE-TIME or ON CALL only a maximum single dosage check will be performed on the order and a frequency is not needed. General dosing information for the drug will also be provided.

> If the TYPE OF SCHEDULE for an Administration Schedule within an order is designated as DAY OF THE WEEK, the number of administration times will be used to determine the frequency in order to perform a daily dose range check. If none are defined, a frequency of ‘1’ will be assumed.

> ![](pss-1-142-user-manual-change-pages/005.png)![](pss-1-142-user-manual-change-pages/006.png)![](pss-1-142-user-manual-change-pages/007.png)Note: A schedule name of OTHER is not allowed. This name is used to allow building a Day-of-Week and/or admin-time schedule in CPRS.

> Example: Standard Schedule Edit

### PSS Schedule Edit Option Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Validation checks were added to the Standard Schedule Edit \[PSS SCHEDULE EDIT\] option to prevent the Standard Administration Times, Ward Administration Times, Frequency and Schedule Type fields of a schedule from conflicting with one another.

### Schedule Edit Validation One

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system shall validate, for schedules with a Schedule Type of Continuous and a frequency of 1 day (1440 minutes) or less that the number of administration times is less than or equal to 1440 divided by the frequency. For example, a schedule frequency of 720 minutes must have at least one administration time and cannot exceed two administration times. Similarly, a schedule frequency of 360 minutes must have at least one administration time but cannot exceed four administration times.

> The system shall present warning/error messages to the user if the number of administration times is less than or greater than the maximum admin times calculated for the schedule or if no administration times are entered. If the number of administration times entered is less than the maximum admin times calculated for the schedule, the warning message: “The number of admin times entered is fewer than indicated by the schedule.” shall appear. In this case, the user will be allowed to continue after the warning. If the number of administration times entered is greater

> 84 Pharmacy Data Management V. 1.0 June 2010 User Manual

> than the maximum admin times calculated for the schedule, the error message: “The number of admin times entered is greater than indicated by the schedule.” shall appear. The user will not be allowed to accept the order until the number of admin times is adjusted. If no admin times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

### Schedule Edit Validation Two

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system shall validate for frequencies greater than one day (1440 minutes), that only one administration time is permitted. The system shall present an error message to the user if more than one administration time is entered.

> The error message: “This schedule has a frequency greater than one day (1440 minutes). More than one Administration Time is not permitted.” shall appear if more than one administration time is entered.

### Schedule Edit Validation Three

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the Standard Administration Times and the Ward Administration Times fields in the PSS SCHEDULE EDIT option, for a schedule that has a Schedule Type of Continuous, the system shall prevent a user from entering administration times to Odd Schedules {a schedule whose frequency is not evenly divisible by or into 1440 minutes (1 day)}.

> The system shall present an error message to the user if an administration time is entered. The error message: “This is an odd schedule that does not require administration times. BCMA will determine the administration times based off the start date/time of the medication order.” shall appear.

### Schedule Edit Validation Four

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A validation to TYPE OF SCHEDULE field in the PSS SCHEDULE EDIT was added to remove frequency from the schedule file entry, if the TYPE OF SCHEDULE is changed from CONTINUOUS to ONE TIME, PRN, ON CALL, or DAY OF WEEK.

> The warning message: “The Type of Schedule has changed. The frequency will be removed.” shall appear.

### Schedule Edit Validation Five

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the PSS SCHEDULE EDIT option, the system shall prevent a user from creating Day of Week (DOW) schedules that are not in the correct day of week order. The correct order is: SU- MO-TU-WE-TH-FR-SA. The system shall display an error message if the user does not enter the correct order.

> The error message: “The day of the week schedule must be in the correct day of week order. The correct order is: SU-MO-TU-WE-TH-FR-SA.” shall appear.

> June 2010 Pharmacy Data Management V. 1.0 84a User Manual

### \[PSS SCHEDULE REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Administration Schedule File Report* option prints out entries from the ADMINISTRATION SCHEDULE file (#51.1) in order to check to see if a frequency is defined. A report can be run for all administration schedules or only the administration schedules without a defined frequency.

> Only administration schedules with a PACKAGE PREFIX field (#4) in the ADMINISTRATION SCHEDULE file (#51.1) set to ‘PSJ’ will be included in the report.

> The report can be set to print in either an 80 or 132 column format.

> 84b Pharmacy Data Management V. 1.0 June 2010 User Manual

### From: PSS*1*140 User Manual Change Pages

### \[PSS MEDICATION ROUTES MGMT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Medication Routes Management* option allows users to review and edit Local Medication Routes, request changes to Standard Medication Routes, and view a report of default med routes for orderable items.

### Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Medication Route File Enter/Edit* option .provides the ability to enter and edit data in the MEDICATION ROUTES file (#51.2). Medication routes may be designated for use in all packages or for use only in the National Drug File package. If an Outpatient Pharmacy expansion has been entered at the “OUTPATIENT EXPANSION” prompt, the Outpatient Pharmacy expansion portion of the medication route will appear as part of the SIG on the prescription label exactly as the Outpatient Pharmacy expansion was entered in MEDICATION ROUTES file (#51.2). The IV FLAG field (#6) in the MEDICATION ROUTES file (#51.2) is used to determine that the order can be processed through the IV portion of the Inpatient Medications package. The PROMPT FOR INJ. SITE IN BCMA field (#8) in the MEDICATION ROUTES
> file (#51.2) is used to send information to be displayed on the BCMA Virtual Due List and Coversheet and to verify whether the user should be prompted for an injection site. The DSPLY ON IVP/IVPB TAB IN BCMA? field (#9) in the MEDICATION ROUTES file (#51.2) is used to send information to be displayed on the BCMA IVP/IVPB Tab and Coversheet.
> The *Medication Route File Enter/Edit* option allows the user to enter an interpretation of the OUTPATIENT EXPANSION field in a language other than English. PDM does not translate English terms into another language; instead, it allows the user to enter a translation of a term. If a value has not been entered in the OTHER LANGUAGE EXPANSION field, PDM will default to the value entered in the OUTPATIENT EXPANSION field. If no values exist in the OUTPATIENT EXPANSION and OTHER LANGUAGE EXPANSION fields, the system will not display default values for those fields during CPRS or Outpatient Pharmacy prescription order entry processing. However, when building the SIG, Outpatient Pharmacy will default to the value the user input during order entry. See Appendix G for a list of Spanish equivalents for some of the more common medication routes.
> The *Medication Route File Enter/Edit* option allows the user to map/remap their Local Medication Routes that are marked for 'All Packages’ to an active Standard Medication Route. This is the only option that allows a Standard Medication Route mapping to be deleted. When dosage checks are performed, the software will use this mapping to pass the equivalent FDB Route for the Local Medication Route that was specified in the medication order for the drug to the interface. If the Local Medication Route is not mapped, dosage checks will not be performed. A user will not be prompted to map to a Standard Medication Route if the Local Medication Route is not marked for ‘All Packages.’
> 1.8.5 Default Med Route For OI Report

### \[PSS DEF MED ROUTE OI RPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Default Med Route For OI Report* option is listed on the *Medication Routes Management* \[PSS MEDICATION ROUTES MGMT\] menu. This report can be used to help identify the current default medication routes for the orderable items. The following is an example of the report.
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 21%" />
<col style="width: 16%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>DEFAULT MED ROUTE FOR ORDERABLE ITEM REPORT JUN 17,2009 PAGE 1</p>
<p>OI NAME DOSAGE FORM ASSOCIATED ROUTES DEFAULT ROUTE DRUG</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IBERET</p>
</blockquote></td>
<td><blockquote>
<p>LIQUID</p>
</blockquote></td>
<td><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>IBERET-500 ORAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IBUPROFEN</p>
</blockquote></td>
<td><blockquote>
<p>TAB</p>
</blockquote></td>
<td><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>IBUPROFEN 600MG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IDOXURIDINE</p>
</blockquote></td>
<td><blockquote>
<p>OINT,OPH</p>
</blockquote></td>
<td><blockquote>
<p>RIGHT EYE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>LEFT EYE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>BOTH EYES</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>IDOXURIDINE 0.5%</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IMIPRAMINE</p>
</blockquote></td>
<td><blockquote>
<p>TAB</p>
</blockquote></td>
<td><blockquote>
<p>ORAL (BY MOUTH)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>IMIPRAMINE 25MG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>IMIPRAMINE 50MG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INDOCYANINE</p>
</blockquote></td>
<td><blockquote>
<p>INJ,SOLN</p>
</blockquote></td>
<td><blockquote>
<p>INTRAMUSCULAR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td><blockquote>
<p>INDOCYANINE 25MG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INSULIN</p>
</blockquote></td>
<td><blockquote>
<p>INJ</p>
</blockquote></td>
<td><blockquote>
<p>INTRAMUSCULAR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ORAL</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>SUBCUTANEOUS</p>
</blockquote></td>
<td><blockquote>
<p>INTRAVENOUS</p>
</blockquote></td>
<td><blockquote>
<p>INSULIN LENTE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>INSULIN NPH</p>
</blockquote></td>
</tr>
</tbody>
</table>
> \<This page left blank for two-sided printing.\>

### \[PSS SYS EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Pharmacy System Parameters Edit* option allows the user to edit the Pharmacy System Parameters used in PDM.

> Example: Pharmacy System Parameters Edit

> \<This page left blank for two-sided printing.\>

### Mail Message following completion of Auto Create Dosages, 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Map Local Medication Routes to Standard, 114
> *Map Local Possible Dosage*, 119
> Mark PreMix Solutions, 123
> Marking a CMOP Drug (Single drug), 6 Medication Instruction File Add/Edit, 49 Medication Instruction File Report, 51, 124 Medication Instruction Management, 49 Medication Instructions, Spanish Translations, 197 Medication Route File Enter/Edit, 54, 116 Medication Route Mapping History Report, 59, 116

### From: PSS*1*143 User Manual Change Pages

### \[PSS SCHEDULE EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Standard Schedule Edit* option allows the user to enter or edit entries in the ADMINISTRATION SCHEDULE file (#51.1). The set of times associated with the standard dosage administration schedules can be assigned, as can ward-specific administration times. This feature may be used to define the outpatient expansion to be used when the schedule is entered for an Outpatient Pharmacy medication order. Entry of a frequency in minutes allows the software to calculate the interval between dosages for Inpatient Medication orders and BCMA and is used by Outpatient Pharmacy to calculate default quantities. When the frequency is entered, a message displays telling the user, in hours, how often the administration will occur. If the schedule type is on call, the system does not require a frequency.

> Schedules with a frequency that is not evenly divisible into or by 24 hours are considered ‘odd’. Odd schedules are not allowed to have administration times. If the schedule type is continuous and it is an odd schedule, the system does not allow the entry of administration times.

> Continuous, non-odd schedules still require administration times.

> The *Standard Schedule Edit* option allows the user to enter the outpatient expansion value in a language other than English. PDM does not translate English terms into another language; instead, it allows the user to enter a translation of a term. If a value has not been entered in the OTHER LANGUAGE EXPANSION field, PDM defaults to the value entered in the OUTPATIENT EXPANSION field. If no values exist in the OUTPATIENT EXPANSION and OTHER LANGUAGE EXPANSION fields, the system will not present default values for those fields to the user during CPRS or Outpatient Pharmacy prescription order processing. However, when building the SIG, Outpatient Pharmacy will default to the value the user input through Outpatient Pharmacy backdoor order entry. See Appendix C for a list of Spanish equivalents for some of the more common administration schedules.

> In order to perform a daily dose range check on a prescribed medication, the software needs to determine how many times per day the single dosage is taken. The schedule from an order will be used to obtain that information. If the schedule is found, the value in the FREQUENCY (IN MINUTES) field (#2) in the ADMINISTRATION SCHEDULE file (#51.1) will be used to calculate the frequency.

> If a frequency cannot be determined, a daily dose range check will not be performed. The user will be informed of this and a reason given as to why. A maximum single dose check will still be performed and general dosing information for the drug will be provided.

> If the type of schedule for an administration schedule used for an order is designated as ONE- TIME or ON CALL or if the Schedule Type for a Unit Dose order is ONE-TIME or ON CALL only a maximum single dosage check will be performed on the order and a frequency is not needed. General dosing information for the drug will also be provided.

> If the TYPE OF SCHEDULE for an Administration Schedule within an order is designated as DAY OF THE WEEK, the number of administration times will be used to determine the frequency in order to perform a daily dose range check. If none are defined, a frequency of ‘1’ will be assumed.

> ![](pss-1-143-user-manual-change-pages/002.png)Note: A schedule name of OTHER is not allowed. This name is used to allow building a Day-of-Week and/or admin-time schedule in CPRS.

> Example: Standard Schedule Edit

### PSS Schedule Edit Option Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Validation checks were added to the Standard Schedule Edit \[PSS SCHEDULE EDIT\] option to prevent the Standard Administration Times, Ward Administration Times, Frequency and Schedule Type fields of a schedule from conflicting with one another.

### Schedule Edit Validation One

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system shall validate, for schedules with a Schedule Type of Continuous and a frequency of 1 day (1440 minutes) or less that the number of administration times is less than or equal to 1440 divided by the frequency. For example, a schedule frequency of 720 minutes must have at least one administration time and cannot exceed two administration times. Similarly, a schedule frequency of 360 minutes must have at least one administration time but cannot exceed four administration times.

> The system shall present warning/error messages to the user if the number of administration times is less than or greater than the maximum admin times calculated for the schedule or if no administration times are entered. If the number of administration times entered is less than the maximum admin times calculated for the schedule, the warning message: “The number of admin times entered is fewer than indicated by the schedule.” shall appear. In this case, the user will be allowed to continue after the warning. If the number of administration times entered is greater

> than the maximum admin times calculated for the schedule, the error message: “The number of admin times entered is greater than indicated by the schedule.” shall appear. The user will not be allowed to accept the order until the number of admin times is adjusted. If no admin times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

### Schedule Edit Validation Two

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system shall validate for frequencies greater than one day (1440 minutes), that only one administration time is permitted. The system shall present an error message to the user if more than one administration time is entered.

> The error message: “This schedule has a frequency greater than one day (1440 minutes). More than one Administration Time is not permitted.” shall appear if more than one administration time is entered.

### Schedule Edit Validation Three

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the Standard Administration Times and the Ward Administration Times fields in the PSS SCHEDULE EDIT option, for a schedule that has a Schedule Type of Continuous, the system shall prevent a user from entering administration times to Odd Schedules {a schedule whose frequency is not evenly divisible by or into 1440 minutes (1 day)}.

> The system shall present an error message to the user if an administration time is entered. The error message: “This is an odd schedule that does not require administration times. BCMA will determine the administration times based off the start date/time of the medication order.” shall appear.

### Schedule Edit Validation Four

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A validation to TYPE OF SCHEDULE field in the PSS SCHEDULE EDIT was added to remove frequency from the schedule file entry, if the TYPE OF SCHEDULE is changed from CONTINUOUS to ONE TIME, PRN, ON CALL, or DAY OF WEEK.

> The warning message: “The Type of Schedule has changed. The frequency will be removed.” shall appear.

### Schedule Edit Validation Five

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the PSS SCHEDULE EDIT option, the system shall prevent a user from creating Day of Week (DOW) schedules that are not in the correct day of week order. The correct order is: SU- MO-TU-WE-TH-FR-SA. The system shall display an error message if the user does not enter the correct order.

> The error message: “The day of the week schedule must be in the correct day of week order. The correct order is: SU-MO-TU-WE-TH-FR-SA.” shall appear.

### Non-VA Meds, Drug Enter/Edit, 39, 40

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Noun/Dosage Form Report, 19
> Orderable Item Management, 75
> Orderable Item Report, 83
> Original Drug Text File Entries Combinations, 175
> Other Language Translation Setup option, 99
> Pharmacy Data Management options, 3 Pharmacy System Parameters Edit, 93 Possible Dosages, 125, 155
> PROMPT FOR INJ. SITE IN BCMA, 54
> PSS Schedule Edit Option Validation, 84 PSXCMOPMGR key, 5
> PSXCOMPMGR key, 1
> Request Change to Standard Medication Route, 61, 116
> Request Changes to Dose Unit, 25, 123 Rerun Auto Create Dosages, 7 Review Dosages Report, 21
> Revision History, i
> Screen prompts, 1
> Sig formula, 155
> Sig Formulas (Formulas), 153
> Simple Local Possible Dosages, 151 Simple Possible Dosage Formula, 155 Simple Possible Dosages, 151 Standard Schedule Management, 95 Strength Mismatch Report, 122 Synonym Enter/Edit, 97
> Table of Contents, iii
> Unmarking a CMOP Drug (Single drug), 6
> Warning Builder, 103
> Warning Mapping, 109
> 206 Pharmacy Data Management V. 1.0 June 2010

### From: PSS*1*141 User Manual Change Pages

## \[PSS MAINTAIN ORDERABLE ITEMS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Dispense Drug/Orderable Item Maintenance* option is used for maintaining the relationship between Dispense Drugs and Pharmacy Orderable Items. Entries made at the Pharmacy Orderable Item prompts will be used by the Outpatient Pharmacy, Inpatient Medications, and CPRS packages as defaults during the medication order entry processes. If no entries are made at the “MED ROUTE” and “SCHEDULE TYPE” prompts, the software will assume the defaults of PO (oral) and CONTINUOUS, respectively.

> The *Dispense Drug/Orderable Item Maintenance* option allows the user to enter patient instructions in a language other than English. PDM does not translate English terms into another language; instead, it allows the user to enter a translation of a term. If a value has not been entered in the OTHER LANGUAGE INSTRUCTIONS field, PDM will default to the value entered in the PATIENT INSTRUCTIONS field. If the PATIENT INSTRUCTIONS field does not contain data for the selected orderable item, the system will not present default patient instructions to the user during CPRS or Outpatient Pharmacy prescription order processing.

> However, when building the SIG, Outpatient Pharmacy will default to the value the user input through backdoor Outpatient Pharmacy order entry.

> Example: Dispense Drug/Orderable Item Maintenance

> Following the on-screen instructions of “Now editing Orderable Item,” if the orderable item being edited is matched to any dispense drugs that are in VA drug classes IM100 through IM900, an additional prompt will appear to permit mapping of the orderable item to an associated immunization file entry. This feature is introduced with the Immunizations Documentation by BCMA application in patches PSS\*1\*141 and PSB\*3\*47.

> Example: Editing Immunization-Related Pharmacy Orderable Items

> Note: The ASSOCIATED IMMUNIZATION field is only presented when at least one of the dispense drugs tied to the selected orderable item is in a VA Drug Class in the IM100 to IM900 range. Immunizations are typically found in VA Drug Classes IM100, IM105, IM109, IM700 or IM900.

## \[PSS ORDERABLE ITEM DOSAGES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Orderable Item/Dosages Report* option prints a report that displays Inpatient Medication and Outpatient Pharmacy dosages for each Pharmacy Orderable Item. These are the dosages that will display for selection through CPRS when an Orderable Item is selected through CPRS at the time an Orderable Item is selected for a medication order. Due to the length of this report, it must be queued to a printer.

> This option prints a report, sorted by Pharmacy Orderable Item that displays Inpatient Medication and Outpatient Pharmacy dosages for Pharmacy Orderable Items. These dosages will display for selection through CPRS when an Orderable Item is selected for a medication order.

> Along with each dosage that is displayed on the report, the name of the drug entry from the DRUG file (#50) that provided the dosage is displayed.

> Not every dosage from the DRUG file (#50) will display on this report. For example, if there are duplicate Possible Dosages for a Pharmacy Orderable Item, and there are different Dispense Units Per Dose, only the Possible Dosage with the lowest Dispense Units Per Dose will display on the report. If there are package specific Possible Dosages and Local Possible Dosages for drugs tied to the Pharmacy Orderable Item, only the Possible Dosages will display on the report because Possible Dosages always override Local Possible Dosages.

> In summary, this report will screen out Possible Dosages and Local Possible Dosages when appropriate, so only the dosages selectable through CPRS will display on this report.

> Additionally, the report will display in parenthesis the dosage, as it will appear on the Outpatient Pharmacy prescription label, if the dosage is a Possible Dosage.

> *Screen Print Follows*
