---
title: Outpatient Pharmacy Version 7 User Manual - Supplemental (updated PSO*7*643)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Supplemental (updated PSO*7*643)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 1
description: <span id="_top" class="anchor"></span>OUTPATIENT PHARMACY (PSO)SUPPLEMENTAL USER MANUAL
audience: 
keywords: 
  - table
  - strong
  - pharmacy
  - order
  - label
  - contents
  - outpatient
  - days
  - prescription
  - class
page_count: 0
word_count: 11653
section_count: 18
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_sup_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_sup_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

<span id="_top" class="anchor"></span>OUTPATIENT PHARMACY (PSO)SUPPLEMENTAL USER MANUAL

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/001.png)

Version 7.0December 1997(Revised April 2023)

Office of Information and Technology (OIT)

Enterprise Program Management Office

######### Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/23</td>
<td><p><a href="#_top">Title Page</a></p>
<p><a href="#p43">43</a>-<a href="#p45">45</a></p>
<p><a href="#p48">48</a></p></td>
<td>PSO*7*643</td>
<td><p>Updated title page to reflect release month</p>
<p>Updated <u>OneVA Pharmacy Laser Labels (PSO*7*454)</u></p>
<p>Updated <u>OneVA Pharmacy Reprint</u></p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>06/22</td>
<td><a href="#OLE_LINK033">33</a></td>
<td>PSO*7*676</td>
<td>Updated <u>Patient Medication Information (PMI) Sheet Section</u> to include new hazardous medication warning.</td>
</tr>
<tr class="odd">
<td>06/20</td>
<td><p><a href="\l">Title Page</a></p>
<p><a href="#p477_13_remove_EXCEPT_ref"><u>13</u></a></p>
<p><a href="#p477_18_removed_EXCEPT_section"><u>18</u></a></p></td>
<td>PSO*7*477</td>
<td><p>Updated title page to reflect release month</p>
<p>Removed a reference to the EXCEPT conjunction</p>
<p>Removed a section about “No Default Quantity Calculation – Complex Order including “EXCEPT”’</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>02/18</td>
<td><p><a href="\l">Title Page</a></p>
<p><a href="#Page_19">19</a></p></td>
<td>PSO*7*402</td>
<td><p>Updated title page to reflect release month</p>
<p>Updated Available Dosage List display and Schedule display</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>05/17</td>
<td>42</td>
<td>PSO*7*479</td>
<td><p>Modifies the prompt to the user when printing a OneVA Pharmacy label.</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>12/16</td>
<td>i-vi, 42-45, 46</td>
<td>PSO*7*454</td>
<td><p>Updated Title Page to current OI&amp;T standards; Updated Revision History; Updated footer date; Updated Table of Contents; Added section for OneVA Pharmacy Laser labels.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>03/10</td>
<td>29, 33</td>
<td>PSO*7*338</td>
<td><p>Laser labels updated: Additional Warnings section added to the top of PMI section. Lengthy labels are truncated so text referring them to the Additional Warnings section could be added and the lengthy label is printed there.</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>05/09</td>
<td>37a-b</td>
<td>PSO*7*305</td>
<td><p>Notice of Privacy Practice reminder printed on PMI with prescription’s laser labels.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>10/07</td>
<td>All</td>
<td>PSO*7*264</td>
<td><p>Separated Appendices from <em>Outpatient Pharmacy V. 7.0 User Manua</em>l, and created this new document.</p>
<p>REDACTED</p></td>
</tr>
</tbody>
</table>

# # Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Preface](#preface)
- [# # Chapter 1: Creating a Sig Using Information from CPRS Order Entry](#chapter-1-creating-a-sig-using-information-from-cprs-order-entry)
- [Creating a New Outpatient Order in CPRS](#creating-a-new-outpatient-order-in-cprs)
- [Creating a New Order When Finishing a CPRS Order in Outpatient Pharmacy](#creating-a-new-order-when-finishing-a-cprs-order-in-outpatient-pharmacy)
- [Creating the Sig Formula](#creating-the-sig-formula)
  - [## Simple Possible Dosages](#simple-possible-dosages)
- [Chapter 2: Calculating Default Quantity (QTY) values](#chapter-2-calculating-default-quantity-qty-values)
- [Calculating Quantities](#calculating-quantities)
  - [Default Quantity Calculation, Simple Dosage Order](#default-quantity-calculation-simple-dosage-order)
    - [Simple Order, No Duration Given](#simple-order-no-duration-given)
    - [Simple Order, Duration Less Than Days Supply](#simple-order-duration-less-than-days-supply)
    - [Simple Order, Days Supply Less Than Duration](#simple-order-days-supply-less-than-duration)
    - [Simple Order, Days Supply Equals Duration](#simple-order-days-supply-equals-duration)
  - [Default Quantity Calculation – Complex Order, all Conjunctions of “AND”](#default-quantity-calculation-complex-order-all-conjunctions-of-and)
    - [Complex Order, No Duration For Any Dosing Sequence](#complex-order-no-duration-for-any-dosing-sequence)
    - [Complex Order, Durations For Some But Not All Dosing Sequences](#complex-order-durations-for-some-but-not-all-dosing-sequences)
    - [Complex Order, Different Durations For All Dosing Sequences](#complex-order-different-durations-for-all-dosing-sequences)
  - [Examples of Default Quantity Calculation – Complex Order, all Conjunctions of “THEN”](#examples-of-default-quantity-calculation-complex-order-all-conjunctions-of-then)
    - [Complex Order, Durations For All Dosing Sequences](#complex-order-durations-for-all-dosing-sequences)
    - [Complex Order, One Duration Missing](#complex-order-one-duration-missing)
  - [Default Quantity Calculation – Complex Order, both “AND” and “THEN”](#default-quantity-calculation-complex-order-both-and-and-then)
    - [Complex Order, One Missing Duration](#complex-order-one-missing-duration)
    - [Complex Order, Missing Durations in More Than One Sub-Sequence](#complex-order-missing-durations-in-more-than-one-sub-sequence)
- [Chapter 3: Tips for Working with Laser Printed Prescription Labels](#chapter-3-tips-for-working-with-laser-printed-prescription-labels)
- [Laser Label Phase I – PSO\7\120 and PSO\7\117](#laser-label-phase-i-pso7120-and-pso7117)
  - [Narrative Text](#narrative-text)
  - [Accessing the Laser Label Format](#accessing-the-laser-label-format)
  - [Modifications to Existing Features](#modifications-to-existing-features)
    - [Affected Options](#affected-options)
- [Laser Labels Phase II (PSO\7\161) and FY07 Q2 Release (PSO\7\200)](#laser-labels-phase-ii-pso7161-and-fy07-q2-release-pso7200)
  - [Prescription Label Section](#prescription-label-section)
  - [<u> </u>Warning Label Section](#u-uwarning-label-section)
  - [<u> </u>Mail Address Section](#u-umail-address-section)
  - [Pharmacy Fill Section](#pharmacy-fill-section)
  - [<u> </u>Patient Fill Section](#u-upatient-fill-section)
  - [<u> </u>Patient Medication Information (PMI) Sheet Section](#u-upatient-medication-information-pmi-sheet-section)
  - [Multi-Rx Refill Document Section](#multi-rx-refill-document-section)
- [OneVA Pharmacy Laser Labels (PSO\7\454)](#oneva-pharmacy-laser-labels-pso7454)
  - [Narrative Text](#narrative-text-1)
  - [OneVA Pharmacy Reprint](#oneva-pharmacy-reprint)
- [Index](#index)
This *User Manual -- Supplemental* includes information that pertains to the Outpatient Pharmacy V. 7.0 application and is intended for pharmacists and technicians who are familiar with the functioning of Outpatient Pharmacy in a Veterans Affairs (VA) Medical Center (MC).

# # # Chapter 1: Creating a Sig Using Information from CPRS Order Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter provides explanations and examples for creating a Sig.

# Creating a New Outpatient Order in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user enters an Outpatient order through CPRS, the information is sent to the Outpatient Pharmacy package, and this information is displayed to the user who finishes this order in the Outpatient Pharmacy package. Previously, the Sig was entered as a single free text field that could be edited. Now the user is prompted for the different fields that make up a possible Sig. The Outpatient Pharmacy package builds a possible Sig based on the information entered in these fields, and this possible Sig is displayed on the Pharmacy Finish screen. Whoever finishes the order can either accept the Sig or edit the fields used to build the Sig. If the possible Sig is accepted, that will become the Sig for the prescription and will print on the labels, profiles, etc. Entries in the SCHEDULE field will be checked against the MEDICATION INSTRUCTION file for possible expansion. A new order will be created if values are changed in some of the fields. This process will be explained after we describe how the possible Sig is created by using the information entered through CPRS.

Example 1: The first part of this example shows the prompts and what is entered through CPRS for a DIGOXIN 0.25MG TAB ORDER. The actual CPRS screen looks different, but the prompts are the same.

> Orderable Item: DIGOXIN TAB

> Dispense Drug: DIGOXIN 0.25 MG TAB

> Complex dose? NO//\<Enter\>

> Take (in TABLET(S)): 2

> Route: ORAL

> Schedule: Q12H

> Limit duration to (in DAYS): 30

> Quantity: 60

> Refills (0-11)://<u>5</u>

> Pick up: WINDOW//\<Enter\>

> Provider Instructions:

> 1\>

The Take prompt in the above example will vary, depending on the Dose Form associated with the selected medication. For example:

<u>DOSAGE FORM</u> <u>PROMPT</u>

TAB Take

CREAM,TOP Apply

INJ Inject

SOLN,OPH Instill

From this information entered through CPRS, the possible Sig that Outpatient Pharmacy would display when this order is finished in pharmacy is

TAKE 2 TABLET(S) BY MOUTH EVERY 12 HOURS FOR 30 DAY(S)

This possible Sig is created using this method:

\* The word TAKE is derived from the VERB entry in the DOSAGE FORM file that is associated with the Dosage Form TAB, which is derived from the Dose Form associated with the Orderable Item DIGOXIN TAB.

\* The number 2 is taken from what was entered at the "Take" prompt.

\* The word TABLET(S) is derived from the NOUN entry in the DOSAGE FORM file that is associated with the Dosage Form TAB, which is derived from the Dose Form associated with the Orderable Item DIGOXIN TAB.

\* The word BY is derived from the PREPOSITION entry in the DOSAGE FORM file that is associated with the Dosage Form TAB, which is derived from the Dose Form associated with the Orderable Item DIGOXIN TAB. The PREPOSITION will only be printed if there is an Outpatient expansion associated with the Med Route.

\* The word MOUTH is derived from the OUTPATIENT EXPANSION in the MEDICATION ROUTES file, which is associated with the Med Route ORAL. If there is no outpatient expansion, the abbreviation will be used. If there is no abbreviation the name will be used.

\* The words EVERY 12 HOURS are derived from the OUTPATIENT EXPANSION in the ADMINISTRATION SCHEDULE file that is associated with the Schedule Q12H. If no Outpatient expansion is found in the ADMINISTRATION SCHEDULE file, the software will then derive an expansion from the MEDICATION INSTRUCTION file.

\* The words FOR 30 DAY(S) are derived from the 30 entered for Duration. The word FOR is always used when there is a Duration. The number 30 is used because that is what was entered. DAYS is used as a default time period. If 30D was entered for Duration, (D for days), the possible Sig would still be the same. The CPRS user could have changed the time period by preceding the number 30 with these letters:

<u>USER ENTERS</u> <u>EXPANSION</u>

30D FOR 30 DAYS

30H FOR 30 HOURS

30M FOR 30 MINUTES

30 FOR 30 DAYS (Default to DAYS)

  
Example 2: This example is similar to Example 1, only a second set of Instructions is entered for this order.

> Medication: DIGOXIN TAB

> Dispense Drug: DIGOXIN 0.25 MG TAB

> Complex dose? NO://YES

> Take (in TABLET(S)): 2

> Route: ORAL

> Schedule: Q12H

> Limit duration to (in DAYS): 30

> Then Take (in TABLET(S)): 1

> Route: ORAL

> Schedule: Q8H

> Limit duration to (in DAYS): 10

> Then Take (in TABLET(S)): \<Enter\>

> Quantity: 90

> Refills (0-11)://5

> Pick up: WINDOW//\<Enter\>

> Provider Instructions:

> 1\>

Since there is a second set of Instructions entered for this order, the word "THEN" is used to put together these Instructions, so the possible Sig would be as follows:

TAKE 2 TABLET(S) BY MOUTH EVERY 12 HOURS FOR 30 DAY(S) THEN

TAKE 1 TABLET(S) BY MOUTH EVERY 8 HOURS FOR 10 DAY(S)

# Creating a New Order When Finishing a CPRS Order in Outpatient Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a CPRS order is finished in the Outpatient Pharmacy package, it is possible that the order can be edited in such a way that the original order is discontinued, and a new order is created. This will only happen if any of these three items change: Orderable Item, Med Route, or Schedule.

The Orderable Item can be edited directly when finishing an order. If a new Orderable Item is selected, a new Dispense Drug would also then have to be selected, causing a new order to be created.

Checking for a new Med Route and a new Schedule is a little different. These fields are not edited directly when an order is Finished, rather new Med Routes and Schedules are only derived if the possible Sig that has been made by the CPRS entries is not accepted, and a new Sig has to be entered when an order is finished. Using Example 2 from the possible Sig examples, we have the following Order Entry dialogue:

> Medication: DIGOXIN TAB

> Dispense Drug: DIGOXIN 0.25 MG TAB

> Instructions:

> 1\. Take: 2

> Route: ORAL

> Schedule: Q12H

> Duration: 30

> 2\. Take: 1

> Route: ORAL

> Schedule: Q8H

> Duration: 10

> Quantity: 90

> Refills: 5

> Pick up: Window

From this dialogue, our possible Sig is

TAKE 2 TABLET(S) BY MOUTH EVERY 12 HOURS FOR 30 DAY(S) THEN

TAKE 1 TABLET(S) BY MOUTH EVERY 8 HOURS FOR 10 DAY(S)

And our Med Route and Schedules are

Med Route: ORAL

Schedule: Q12H

Schedule: Q8H

If the possible Sig is not accepted, a new Sig must be entered. When this new Sig is entered, we will expand the Sig as has always been done by running each word entered through the MEDICATION INSTRUCTION file, looking for anything that needs expanded. But now a Med Route and Schedule can be associated with each entry in this file. So, when we check for any expansions on the new Sig being entered, we also gather the Med Routes and Schedules associated with the new Sig. We check those new Med Route(s) and new Schedule(s) against the original Med route(s) and Schedule(s), and if there are any discrepancies, a new order will be created.

For example, our Med Route from CPRS is ORAL. When we get all the Med Routes from the new Sig, the only way a new order would not be created is if the only Med Route we find is Oral. If we find any other Med Route, or if we don't find any Med Route at all, a new Order will be created.

We received two Schedules from CPRS, Q12H and Q8H. When we gather all the Schedules from the new Sig, if we find any other Schedules besides Q12H and Q8H, a new order will be created. If we don't find Q12H or don't find Q8H at least once, a new order will be created. The order of the Schedules does not matter, it only matters that the same schedules are found.

These same checks are done anytime a Sig is edited. For example, if a CPRS order is finished in Outpatient Pharmacy, and the possible Sig is accepted from CPRS, the Med Route and Schedule(s) are kept with the prescription. If at some later time that Sig is changed, the same new order checks will be done at that point. The same med route and schedule checks are done on orders entered through the Outpatient Pharmacy package.

The Med Routes and Schedules can be added to the MEDICATION INSTRUCTION file by using the *Medication Instruction File Add/Edit* option in the Pharmacy Data Management package. Some examples for associating Med Routes and Schedules with entries in the MEDICATION INSTRUCTION file are as follows:

> ENTRY IN FILE MED ROUTE SCHEDULE

> ---------------------------------------------------------------

> SLC SUBLINGUAL (no schedule)

> BID (no med route) BID

> PO BID ORAL BID

# Creating the Sig Formula 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Earlier versions of the Pharmacy Data Management software allowed the Sig to be directly edited from within the Outpatient Pharmacy package. Following the release of the Pharmacy Ordering Enhancements patch, however, the Sig will no longer be edited as a unit. Instead, individual fields are populated and then concatenated to create the Sig. Although the Sig, as a unit, cannot be edited, each individual field that creates the Sig can be edited until the Sig displays as desired.

Four basic types of Sigs exist: Simple Possible Dosages, Simple Local Possible Dosages, Complex Possible Dosages and Complex Local Possible Dosages. The Sig for each of these dosages is created by combining fields from various Pharmacy files. To simplify the process, each dosage can be thought of as having its own Sig “formula”. These formulas are displayed below, followed by the relevant field and file information displayed in the chart following the formulas.

Simple Possible Dosages

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/002.png)

Simple Local Possible Dosages

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/003.png)

Complex Possible Dosages

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/004.png)

Complex Local Possible Dosages

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/005.png)

Table A: Formula Symbols

| Symbol                                                                                           | File                      |     | Symbol                                                                                           | File                                                                  |
|------------------------------------------------------------------------------------------------------|-------------------------------|-----|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/006.png)  | DOSAGE FORM file \#50.606     |     | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/007.png)  | ADMINISTRATION SCHEDULE file \#51.1                                       |
| ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/008.png)  | DRUG file \#50                |     | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/009.png)  | ORDERABLE ITEM file \#50.7 or Provider Comments stored within CPRS orders |
| ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/010.png) | DOSAGE FORM file \#50.606     |     | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/011.png) |                                                                           |
| ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/012.png) | DOSAGE FORM file \#50.606     |     | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/013.png) |                                                                           |
| ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/014.png) | MEDICATION ROUTES file \#51.2 |     |                                                                                                      |                                                                           |

## ## Simple Possible Dosages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The formula for creating a Sig for a simple possible dosage is displayed below. The charts following the formula define how various sample Sigs were created using this formula.

Simple Possible Dosage Formula

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/015.png)

Utilizing the formula above creates a Sig for a simple possible dosage. For example, to create the Sig, “TAKE 2 TABLETS BY MOUTH EVERY 12 HOURS AFTER MEALS”, the Sig must be broken down into each of the elements in the simple possible dosage formula. The table below outlines each element of the desired Sig. By identifying the symbol to the right of the element, it is easy to identify which file provided that element’s information. For example, to the right of the word “TAKE” in the table, the Verb symbol is displayed. By referencing “Table A: Formula Symbols”, it is apparent that Verb entries are taken from the DOSAGE FORM file.

The table below defines each element of the Sig and identifies which files provided that element’s information. The complete Sig is displayed at the top of the table.

> TAKE 2 TABLETS BY MOUTH

> EVERY 12 HOURS AFTER MEALS

| TAKE           | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/016.png)  |
|--------------------|------------------------------------------------------------------------------------------------------|
| 2              | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/017.png)  |
| TABLETS        | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/018.png) |
| BY             | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/019.png) |
| MOUTH          | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/020.png) |
| EVERY 12 HOURS | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/021.png)  |
| AFTER MEALS    | ![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/022.png) |

# Chapter 2: Calculating Default Quantity (QTY) values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter provides explanations and examples for calculating quantity values for a prescription.

# Calculating Quantities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To calculate a default Quantity value for a prescription, the prescription must have certain attributes:

- Every dosage of the order must be a Possible Dosage with a valid (numeric) Dispense Units Per Dose.
- Every dosing sequence of the order must have a Schedule from which to derive a frequency. A frequency can be associated with the Schedule from either the ADMINISTRATION SCHEDULE file or the MEDICATION INSTRUCTION file.
- A Days Supply value must exist for the order.

If any of the above attributes are missing, a default Quantity cannot be calculated and a value will have to be entered.

To derive a frequency, the software looks first at the Schedule as a whole, including any spaces entered. If the Schedule entry is found in the ADMINISTRATION SCHEDULE file, then the associated frequency, if found, is the frequency used. If this does not happen, then the software searches for a match to the entry in the MEDICATION INSTRUCTION file with an associated frequency. If the Schedule entry does not match as a whole in either file, then the software breaks the Schedule entry into individual words. Each word found in the Schedule goes through the same process just described to determine a frequency. If at the end of this process, only one frequency is found, it is used for the order. If more than one frequency is found, even if they are all the same, then no frequency is applied, and a default Quantity cannot be calculated. For example, Schedules of QAM AND NOON and QAM OR NOON could have frequencies of 1440 for QAM and 1440 for NOON. But because of the AND/OR differences in the Schedule the frequency should be different. Since the Schedule is a text entry, the software cannot determine with complete accuracy the intent when multiple frequencies are found.

Orders are classified into four different types when calculating default Quantity values.

1\. Simple Dosage Order

2\. Complex Dosage Order with all Conjunctions of “AND”

3\. Complex Dosage Order with all Conjunctions of “THEN”

4\. Complex Dosage Order with Conjunctions of “AND” and “THEN”

The <span id="p477_13_remove_EXCEPT_ref" class="anchor"></span>software converts all time values (Days Supply, Frequency, Duration) into minutes and divides the Days Supply or Duration by the Frequency. This value is multiplied by the Dispense Units Per Dose to get the default Quantity value.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/023.png)Some of the Sigs used in the following examples do not make sense for a prescription but are used to illustrate how QTY defaults are calculated. All examples are in days or hours, but the calculations will also work for minutes. When a default QTY ends in a decimal, it is rounded up to the next whole number.

## Default Quantity Calculation, Simple Dosage Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there is a Duration entered and it is not equal to the Days Supply, then the software will use whichever value is lower in calculating the default Quantity.

### Simple Order, No Duration Given

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this example, the Dispense Units Per Dose is 2 and the Schedule of Q12H (Every 12 hours) has an associated frequency of 720 minutes (12 hours x 60 minutes/hour). Because there is no Duration given, the Days Supply of 30 will be used in the calculation. The software converts the Days Supply into minutes (by multiplying 30 x 1440, the number of minutes in a day) and then divides the Days Supply minutes by the minutes of frequency (43,200/720) to arrive at 60. The software then multiplies that result by the Dispense Units Per Dose (60 x 2) to get a default Quantity value of 120.

> (TAKE TWO TABLETS BY MOUTH EVERY 12 HOURS)  
> DAYS SUPPLY: (1-90): 30// \<Enter\>  
> QTY (TAB): 120//

### Simple Order, Duration Less Than Days Supply

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this example, the Duration of 36 hours is used to calculate the QTY of 9 since it is less than the 2 Days Supply (48 hours).

> (TAKE ONE TABLET BY MOUTH EVERY 4 HOURS FOR 36 HOURS)

> DAYS SUPPLY: (1-90): 30// 2

> QTY (TAB): 9//

### Simple Order, Days Supply Less Than Duration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this example, the QTY of 40 is calculated using the 10 Days Supply because it is less than the 20 days Duration.

> (TAKE TWO TABLETS BY MOUTH EVERY 12 HOURS FOR 20 DAYS)  
> DAYS SUPPLY: (1-90): 30// 10

> QTY (TAB): 40//

### Simple Order, Days Supply Equals Duration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this example, the Duration is the same as the Days Supply, so the QTY of 40 is calculated based on 20 days.

> (TAKE TWO TABLETS BY MOUTH EVERY NIGHT FOR 20 DAYS)  
> DAYS SUPPLY: (1-90): 30// 20

> QTY (TAB): 40//

## Default Quantity Calculation – Complex Order, all Conjunctions of “AND”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the following examples have dosing sequences with Possible Dosages having a numeric Dispense Units Per Dose and a Schedule with a frequency. If any dosing sequence lacks either of these, then a default QTY cannot be calculated. All examples are in days, but the calculations will also work for hours or minutes. When a default QTY ends in a decimal, the value is rounded up to the next whole number.

### Complex Order, No Duration For Any Dosing Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this example, the 31 Days Supply is applied to all dosing sequences to come up with a default QTY of 124 (31+62+31).

> (TAKE ONE TABLET BY MOUTH EVERY MORNING AND TAKE TWO TABLETS AT NOON AND TAKE ONE TABLET AT BEDTIME)

> DAYS SUPPLY: (1-90): 31// \<Enter\>

> QTY ( ): 124://

### Complex Order, Durations For Some But Not All Dosing Sequences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the dosing sequences that have durations all have the same Duration, and that Duration is less than the value of Days Supply, then QTY is calculated by applying the value of that Duration to all dosing sequences. In this example, we have “like” Durations of 10 days, which is less than the 20 Days Supply. By applying the 10 day Duration to the last two dosing sequences, a QTY of 110 is calculated ((3\*10)+(2\*10)+(2\*10)+(4\*10)). If the Duration had been greater than Days Supply or if not all Durations had been the same, then QTY would not have been calculated.

> (TAKE THREE TABLETS BY MOUTH EVERY MORNING FOR 10 DAYS, AND TAKE TWO TABLETS EVERY NIGHT FOR 10 DAYS, AND TAKE ONE TABLET EVERY 12 HOURS AND TAKE ONE TABLET EVERY SIX HOURS)  
> DAYS SUPPLY: (1-90): 30// 20  
> QTY (TAB): 110//

### Complex Order, Different Durations For All Dosing Sequences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If all dosing sequences in an order have a Duration but they are not all the same, then the values of all the Durations are totaled. If the total of all the Durations is less than or equal to the Days Supply value, then a QTY is calculated. The total of all the Durations in this example adds up to 18 days (10+5+3), and since that is less than the 30 Days Supply, the QTY of 46 is calculated based on each Duration (30+10+6).

> (TAKE THREE TABLETS BY MOUTH EVERY MORNING FOR 10 DAYS, AND TAKE TWO TABLETS EVERY NIGHT FOR 5 DAYS, AND TAKE ONE TABLET EVERY 12 HOURS

> FOR 3 DAYS)  
> DAYS SUPPLY: (1-90): 30// \<Enter\>  
> QTY (TAB): 46//

## Examples of Default Quantity Calculation – Complex Order, all Conjunctions of “THEN”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When all conjunctions in a complex order are THEN, a QTY can be calculated only if:

- every dosing sequence has a Duration, and the total of all the Durations is less than or equal to the Days Supply,  
  or
- no more than one Duration is missing in the dosing sequence and the total of all the other Durations is less than the Days Supply.

All examples are in days, but the calculations will also work for hours or minutes. When a default QTY ends in a decimal, the value is rounded up to the next whole number.

### Complex Order, Durations For All Dosing Sequences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this example, every dosing sequence has a Duration, and the total of those values (5+4+3=12) is less than the 20 Days Supply. A default QTY of 21 is calculated based on the sum of each dosing sequence (10+8+3).

> (TAKE ONE TABLET BY MOUTH EVERY 12 HOURS FOR 5 DAYS, THEN TAKE TWO TABLETS EVERY MORNING FOR 4 DAYS, THEN TAKE ONE TABLET EVERY NIGHT FOR 3 DAYS.)  
> DAYS SUPPLY: (1-90): 30//20  
> QTY (TAB): 21//

### Complex Order, One Duration Missing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the following example, there are two Durations (6 days and 8 days) and one missing Duration. Since the sum of the Durations (6+8=14) is less than the 30 Days Supply, the difference between that sum and the Days Supply (30-14=16) is applied to the dosing sequence missing a Duration, leading to a default QTY of 76 (12+16+48).

> (TAKE ONE TABLET BY MOUTH EVERY 12 HOURS FOR 6 DAYS, THEN TAKE TWO TABLETS EVERY MORNING FOR 8 DAYS, THEN TAKE THREE TABLETS EVERY NIGHT)  
> DAYS SUPPLY: (1-90): 30// \<Enter\>  
> QTY (TAB): 76//

## Default Quantity Calculation – Complex Order, both “AND” and “THEN”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When there is a mix of the Conjunctions AND and THEN, the dosing sequences are broken down into “sub-sequences” with each THEN as the separator. In the following examples, every other sub-sequence has been bolded. Both a QTY subtotal for the sub-sequences and a decrementing Days Supply are kept. Each sub-sequence gets a final Days Supply total, which is then decremented through the sequences. QTY cannot be calculated if more than one dosing sequence is missing a Duration or if the total Duration is greater than the total Days Supply entered.

### Complex Order, One Missing Duration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the first sub-sequence below, the QTY is 18 (2+4+12) and, because the Duration values are not all the same, the sum of the Durations (2+2+3=7) is used for Days Supply.

The second sub-sequence yields a QTY of 24 (16+8) and a Days Supply of 4 (because both Durations are the same, they are not added together.)

The last sub-sequence has no Duration. The sum of the Days Supply from the first two sub-sequences (7+4=11) is subtracted from the 90 entered for Days Supply and that difference (79) is applied to the QTY for the last sub-sequence. Adding up the QTYs from all three sub-sequences (18+24+79) gives a default QTY of 121.

> (TAKE ONE TABLET BY MOUTH EVERY MORNING FOR TWO DAYS, AND TAKE TWO TABLETS EVERY MORNING FOR 2 DAYS, AND TAKE TWO TABLETS EVERY 12 HOURS FOR 3 DAYS, THEN TAKE TWO TABLETS EVERY 12 HOURS FOR 4 DAYS, AND TAKE ONE TABLET EVERY 12 HOURS FOR 4 DAYS, THEN TAKE ONE TABLET EVERY MORNING)  
> DAYS SUPPLY: (1-90): 30// 90  
> QTY (TAB): 121//

### Complex Order, Missing Durations in More Than One Sub-Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> (TAKE THREE TABLETS BY MOUTH EVERY 12 HOURS FOR 8 DAYS, THEN TAKE TWO TABLETS EVERY 12 HOURS FOR 3 DAYS, AND TAKE TWO TABLETS EVERY NIGHT, THEN TAKE THREE TABLETS EVERY NIGHT FOR TWO DAYS, THEN TAKE TWO TABLETS EVERY MORNING FOR 2 DAYS, AND TAKE THREE TABLETS EVERY MORNING FOR 2 DAYS, THEN TAKE ONE TABLET EVERY 12 HOURS)  
> DAYS SUPPLY: (1-90): 30// 50  
> QTY (TAB): 146//

In this example, there are five sub-sequences:

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 27%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sub-sequence</strong></th>
<th><strong>Sub-sequence text</strong></th>
<th><strong>QTY</strong></th>
<th><strong>QTY calc.</strong></th>
<th><p><strong>Days</strong></p>
<p><strong>Supply</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>#1</td>
<td>TAKE THREE TABLETS BY MOUTH EVERY 12 HOURS FOR 8 DAYS</td>
<td>48</td>
<td>(3*2)*8</td>
<td>8</td>
<td>The Duration and Days Supply are the same.</td>
</tr>
<tr class="even">
<td>#2</td>
<td>THEN TAKE TWO TABLETS EVERY 12 HOURS FOR 3 DAYS, AND TAKE TWO TABLETS EVERY NIGHT</td>
<td>18</td>
<td><p>((2+2)*3)+</p>
<p>(2*3)</p></td>
<td>3</td>
<td>Value for first sequence applied to missing Duration within the sub-sequence</td>
</tr>
<tr class="odd">
<td>#3</td>
<td>THEN TAKE THREE TABLETS EVERY NIGHT FOR TWO DAYS</td>
<td>6</td>
<td>(3*2)</td>
<td>2</td>
<td>Only one value given.</td>
</tr>
<tr class="even">
<td>#4</td>
<td>THEN TAKE TWO TABLETS EVERY MORNING FOR 2 DAYS, AND TAKE THREE TABLETS EVERY MORNING FOR 2 DAYS</td>
<td>10</td>
<td>(2+3)*2</td>
<td>2</td>
<td>Same Duration given for both sequences within the sub-sequence; do not add together</td>
</tr>
<tr class="odd">
<td>SUBTOT</td>
<td></td>
<td>82</td>
<td></td>
<td>15</td>
<td></td>
</tr>
</tbody>
</table>

At this point, the QTY subtotal is 82 and Days Supply is 15. The current Days Supply subtotal (15) is subtracted from the 50 entered in the order for Days Supply. Applying that difference (35) to the last sub-sequence results in a default QTY of 70. Adding the QTYs for all five sub-sequences yields a total QTY of 152.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 27%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sub-sequence</strong></th>
<th><strong>Sub-sequence text</strong></th>
<th><strong>QTY</strong></th>
<th><strong>QTY calc.</strong></th>
<th><p><strong>Days</strong></p>
<p><strong>Supply</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SUBTOT</td>
<td></td>
<td>82</td>
<td></td>
<td>15</td>
<td></td>
</tr>
<tr class="even">
<td>#5</td>
<td>THEN TAKE ONE TABLET EVERY 12 HOURS</td>
<td>70</td>
<td>(2*35)</td>
<td>35</td>
<td>Difference between Days Supply Entered (50) and subtotal Days Supply (15) = Days Supply for last sub-sequence (35).</td>
</tr>
<tr class="odd">
<td><span id="p477_18_removed_EXCEPT_section" class="anchor"></span><strong>TOTALS</strong></td>
<td></td>
<td><strong>152</strong></td>
<td></td>
<td><strong>50</strong></td>
<td></td>
</tr>
</tbody>
</table>

# Chapter 3: Tips for Working with Laser Printed Prescription Labels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter provides information and tips for working with laser labels.

# Laser Label Phase I – PSO\*7\*120 and PSO\*7\*117

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy patch PSO\*7\*120 introduced the ability to print laser printed prescription labels. There are some differences in function when you print these new labels. These differences are detailed below. For more information about laser printed labels, refer to the Release Notes for patch PSO\*7\*120, *Laser Printed Prescription Labels with PMI Sheets Phase I Release Notes.*

Outpatient Pharmacy patch PSO\*7\*117 introduced the support of non-English languages for the SIG. For laser labels, PSO\*7\*138 will allow the bottle label SIG to be in a non-English language while still printing the SIG in English on the Pharmacy Fill Document. It is important to note that the Patient Medication Information (PMI) sheet will not use the patient’s language specification. The PMI will print in either Spanish or English, based on the PMIS LANGUAGE field of the PHARMACY SYSTEM file.

## Narrative Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The laser form has a limited amount of space allocated to print the following fields from the OUTPATIENT SITE file: NARRATIVE FOR COPAY DOCUMENT, NARRATIVE REFILLABLE RX and NARRATIVE NON-REFILLABLE RX. You may need to adjust or modify the text to print correctly. Once you have installed PSO\*7\*120 and set up the printer, examine the printout of this text on the labels and make necessary adjustments. Any text that doesn’t fit in the space allocated will be truncated.

When editing text for these fields, there are two things to keep in mind. First, if the line of text is too long at print time, the program will wrap to the next line. Second, each ‘new’ line (as it is viewed on the screen) when editing will also cause the print to wrap to the next line.

## Accessing the Laser Label Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the new laser label format, the user must make the appropriate entries in the CONTROL CODES multiple of the TERMINAL TYPE file.

> **NOTE:** Installation of PSO\*7\*120 has no major effect on the existing label functionality and will not change the printed format of the label until you perform further steps, as described in the *Outpatient Pharmacy V. 7.0 Technical Manual*. An example of a CONTROL CODE follows:

> NUMBER: 11 CTRL CODE ABBREVIATION: MLI

> FULL NAME: MAILING LABEL INITIALIZATION

> CONTROL CODE: S PSOFONT="F10",PSOX=1700,PSOY=175,PSOYI=50

In this control code, the setup is done that defines the font, starting page position, and line size for the Mailing Label Section of the label.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/024.png) The detailed description of these control codes is found in the *Outpatient Pharmacy V. 7.0 Technical Manual.*

## Modifications to Existing Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase I affects some fields in the OUTPATIENT SITE file and other Outpatient Pharmacy prescription label print features.

When a user selects a device defined for Laser Label output, the “OK to assume label alignment is correct? YES//” prompt is not asked.

### Affected Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are affected by the “OK to assume label alignment is correct” YES//” prompt:

- *Rx (Prescriptions)* \[PSO RX\] option
- *Outpatient Pharmacy Manager* \[PSO MANAGER\] option
- *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option
- *Complete Orders from OERR* \[PSO LMOE FINISH\] option
- *Pharmacist Menu* \[PSO USER1\] option
- *Pharmacy Technician's Menu* \[PSO USER2\] option
- *Suspense Functions* \[PSO PND\] option
- *Print from Suspense File* \[PSO PNDLBL\] option
- *Reprint Batches from Suspense* \[PSO PNDRPT\] option
- *Pull Early from Suspense* \[PSO PNDRX\] option
- *Reprint an Outpatient Rx Label* \[PSO RXRPT\] option
- *Label/Profile Monitor Reprint* \[PSO B\] option
- *Barcode Batch Prescription Entry* \[PSO BATCH BARCODE\] option
- *Change Label Printer* \[PSO CHANGE PRINTER\] option

The system reference to the COPIES field in the PRESCRIPTION file is changed. For a new prescription, when COPIES is set to 1, the full prescription content prints. If COPIES is greater than 1, the full prescription content prints one time. On the additional copies, only the adhesive prescription label portion prints. The adhesive portion includes the bottle label, warning label, and patient address label.

The prompt “Print ‘LEFT’ side of label only? N//” is changed to “Print adhesive portion of label only? N//.”

When “Print adhesive portion of label only? N//” prompt is answered NO, the full prescription content prints. When answered YES, only the adhesive portion of the label prints.

The BARCODES ON REQUEST FORMS field of the OUTPATIENT SITE file is not used in this enhancement. Regardless of the value of this field, barcodes will print on the request form.

The NEW LABEL STOCK field of the OUTPATIENT SITE file is not used in this enhancement. The device setup controls the branch to the new functionality.

# Laser Labels Phase II (PSO\*7\*161) and FY07 Q2 Release (PSO\*7\*200)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of Laser Labels Phase I (PSO\*7\*120), dot matrix labels routines will no longer be updated.

This Appendix describes the layout of the laser labels sections along with the changes made to each section of the labels. These sections are Prescription label (sometimes referred to as the bottle label), Warning labels, Mail Address, Pharmacy Fill Card, Patient Fill, Prescription Document PMI, Trailing Document, and Multi-Rx Refill Document. The following layouts display where these sections are located on the laser label pages.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/025.png)All examples in this appendix are compressed to fit on these pages. The pre-printed forms are legal size (8 ½ x 14) and are displayed as letter size (8 ½ x 11) or smaller.

Example: Laser Label Layout

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/026.png)

  
Example: Trailing Document Layout

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/027.png)

Example: Multi-Rx Refill Document Layout

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/028.png)

## Prescription Label Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/029.png) VAMC ALBANY NY 12208</p>
<p>500 (11881/) Ph: 518-555-4307</p>
<p><strong>Rx# REDACTED</strong> FEB 2, 2005 Fill 1 of 4</p>
<p><strong>OPPATIENT, ONE</strong> REDACTED</p>
<p>TAKE ONE TABLET BY MOUTH TWICE A DAY</p>
<p>Discard after FEB 2, 2006____________ Mfr_______</p>
<p>May refill 3X by FEB 2, 2006</p>
<p>Qty: 60 OPPROVIDER25, THREE</p></th>
<th>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/030.png)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CAPTOPRIL 100MG TABS</strong></td>
<td></td>
</tr>
</tbody>
</table>

These are the changes made to this section:

- When the length of the SIG requires the use of two or more labels, the first four lines of the label will not print on the second and subsequent labels. These lines include the Department of Veterans Affairs Medical Center (VAMC) name and address lines, the prescription number along with the refill information and the last line is the patient’s name and last portion of the Social Security Number (SSN).
- The number of lines of the SIG that print on each label is increased to reduce the number of labels needed for the prescription. This also allows the overlapping of the multiple labels to eliminate the need for cutting the labels to make them fit.
- The SIG is bottom-justified within lines 5 to 8, above the “Discard after” date line on the last continued label.
- The text “May refill nX by MMM DD, YYYY” or “NO REFILLS LEFT” or “NO REFILL” is added between the “Discard after” date line and the “Qty:” line.
- “Mfr\_\_\_\_” is added to the “Discard after” date line beside the discard date. This line along with the quantity, physician, and drug name appear only on the last continued label.
- “Discard after” text prints for all drugs except those marked as supply items.
- On the first bottle label, the phrase “(continued on next label)” is eliminated, however the Rx number and “(label continued)” do remain on the subsequent continuation labels.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/031.png)

With the release of patch PSO\*7\*200, the SSN display changes from six digits to the last four digits.

## <u> </u>Warning Label Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/032.png) These warnings illustrate both old and new warning sources and may not be the current warnings for this drug.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Take medication on an empty stomach one hour before or two to the three hours after a meal unless otherwise directed by your doctor.</p>
<p>This drug may impair the ability to drive or operate machinery. Use care until you become familiar with its effects.</p>
<p>It is very important that you take or use this exactly as directed. Do not skip doses or discontinue unless directed by your doctor.</p>
<p>The dose of the medication will likely need adjustment if you become pregnant. Soon after your pregnancy is confirmed, contact your primary care … See printed Additional Warnings.</p>
<p>CAUTION: Federal law prohibits the transfer of this drug to any person other than the patient for whom it was prescribed.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

These are the changes made to this section:

- Warnings print in English or Spanish depending on the patient’s PMI preference.
- When there are fewer than five warning labels, the warning labels are bottom-justified.
- When the DEA SPECIAL HDLG field in the DRUG file begins with 1, 2, 3, 4, or 5, the NO TRANSFER warning label from the RX CONSULT file (entry number 20) prints in the appropriate language.
- The new data source contains several lengthy warnings (especially Spanish translations). A fourth line of text is allowed, if needed, for the smallest font.
- If the text of a warning exceeds four lines, the fourth line is truncated so the text “… See printed Additional Warnings.” can be added. Then, that warning is printed in its entirety under Additional Warnings in the PMI section.
- When there are more than five warning labels for the prescription, the additional warnings print at the top of the PMI section under Additional Warnings.
- The top warning label sometimes printed on or over the perforated line. For some fonts, the white space between the lines of this warning is reduced so the warning will fit on the label.

## <u> </u>Mail Address Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Attn: (119)</p>
<p>114 HOLLAND AVE</p>
<p>ALBANY, NY 12206</p>
<p>REGULAR MAIL- Forwarding Service Requested</p>
<p>OPPATIENT, ONE</p>
<p>123 OAK STREET</p>
<p>ALBANY, NY 12211</p>
<p>WINDOW – PLEASE HOLD FOR PICKUP</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

These are the changes made to this section:

- The current date is printing in the upper right corner. It is right justified and is retrieved from the LABEL DATE/TIME field. This date prints to the right on the same line as “Attn: (119)”
- The patient name prints first name first instead of last name, first name.
- When the routing is “Window”, the word “Window” is bolded. “Mail” is also bolded in this section.
- With patch PSO\*7\*233, if the permanent address is flagged with a bad address indicator and there is no active temporary address, \*\* BAD ADDRESS INDICATED will print where the address normally would, and the rest of the address will not print.

## Pharmacy Fill Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>500 (11881/) FEB 2, 2005@12:05</p>
<p>Rx#REDACTED FEB 2, 2005 FILL 1 of 4</p>
<p><strong>OPPATIENT, ONE 9955</strong></p>
<p>TAKE ONE TABLET BY MOUTH TWICE A DAY</p>
<p>Qty: 60 OPPROVIDER25, THREE</p>
<p>CAPTOPRIL 100MG TABS</p>
<p>NDC/MFR__________ Lot# ________________</p>
<p>Tech _____________________ RPh _________________</p>
<p>Routing: WINDOW Days supply: 30 Cap: <strong>NON-SAFETY</strong></p>
<p>Isd: FEB 2, 2005 Exp: FEB 2, 2006 Last Fill: APR 6, 2004</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/033.png)</p>
<p>DRUG WARNING 3N, 16N, 13N, 9N</p>
<p>20</p>
<p>Pat. Stat ONSC Clinic: 5TH F</p></td>
</tr>
</tbody>
</table>

These are the changes made to this section:

- The seconds are removed from the label date/time.
- The drug warnings are listed and separated by commas. If an entry in the list does not have an “N” (for “New”), then that warning number is from the RX CONSULT file. Otherwise the warning is from the new commercial data source residing in the WARNING LABEL-ENGLISH file or the WARNING LABEL-SPANISH file.
- The patient status and location (clinic) are added beneath the drug warnings.
- The patient’s name and last portion of the social security number is bolded.
- When the bottle cap is “non-safety”, the words “NON-SAFETY” are bolded.
- The number of lines of the SIG that print on each pharmacy fill card label is increased to reduce the number of labels needed for the prescription.
- With the release of patch PSO\*7\*200, the SSN display changes from six digits to the last four digits.
- With the release of patch PSO\*7\*200, “Mfr\_\_\_\_\_\_” is replaced with:

> NDC/MFR\_\_\_\_\_\_\_\_\_\_\_ (for non-ePharmacy sites)  
> or

> NDC nnnnn-nnnn-nn (for ePharmacy sites)

## <u> </u>Patient Fill Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PHONE IN OR MAIL THIS REFILL REQUEST</p>
<p>Follow the refill instructions provided with your prescription.</p>
<p>For Refill Call (518) 555-4307</p>
<p>OPPATIENT, ONE REDACTED</p>
<p>Rx#REDACTED FEB 2, 2005 FILL 1 of 4</p>
<p>Qty: 60 Days supply:30</p>
<p>third party Rx</p>
<p>CAPTOPRIL 100MG TABS</p>
<p>00003-0###-##</p>
<p>May refill 3X by FEB 2, 2006</p>
<p>COPAY ALBANY-500</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/034.png)</td>
</tr>
</tbody>
</table>

These are the changes made to this section:

- The barcode prints every time even when there are no refills.
- The site telephone number prints when the “PHONE IN OR MAIL THIS REFILL REQUEST” prints.
- The text “n refills left until MMM DD, YYYY” is changed to “May refill nX by MMM DD, YYYY”.
- The text “third party Rx” and the NDC number are added when this information is available. This enhancement is in request to the ePharmacy requirements.

## <u> </u>Patient Medication Information (PMI) Sheet Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CAUTION: HAZARDOUS MEDICATION, PLEASE HANDLE PROPERLY.</p>
<p><strong>Additional Warnings:</strong></p>
<p>0192: The dose of the medication will likely need adjustment if you become pregnant. Soon after your pregnancy is confirmed, contact your primary care doctor or nurse practitioner for the new dosage of medication.</p>
<p>OPPATIENT, ONE Rx#: REDACTED CAPTOPRIL 100MG TABS</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>CAPTOPRIL – ORAL:</strong> (KAP-toe-pril)</p>
<p><strong>WARNING:</strong> This drug can cause serious fetal harm if used during the last six months of pregnancy. If pregnancy occurs, stop using this drug and immediately contact your physician.</p>
<p>.</p>
<p>. (Compressed due to space)</p>
<p>.</p>
<p><strong>MISSED DOSE:</strong> If you miss a dose, take it as soon as remembered; do not take it if it is almost time for the next dose, instead, skip the missed dose and resume your usual dosing schedule. Do not “double-up” the dose to catch up.</p></td>
</tr>
</tbody>
</table>

These are the changes made to this section:

- The PMI section prints in the patient’s language preference.
- The white spaces between the sections of this document are reduced to allow more lines to print on the page.
- When there are more than five warning labels for the prescription, the additional warnings print at the top of the PMI section under Additional Warnings.
- If the warnings in the Warning Label section are more than 4 lines in length, they are printed at the top of the PMI section under Additional Warnings.

<span id="OLE_LINK033" class="anchor"></span>With the release of PSO\*7\*676, Hazardous to Handle and Hazardous to Dispose medications as identified in the National Drug Files (NDF) system display a warning at the top of the PMI section.

- Medications defined by the NDF system as hazardous to handle display the warning “CAUTION: HAZARDOUS MEDICATION, PLEASE HANDLE PROPERLY.”.
- Medications defined by the NDF system as hazardous to dispose of display the warning “CAUTION: HAZARDOUS MEDICATION, PLEASE DISPOSE OF PROPERLY.”
- Medications defined by the NDF system as both hazardous to handle and hazardous to dispose of display the warning message “CAUTION: HAZARDOUS MEDICATION, PLEASE HANDLE AND DISPOSE OF PROPERLY.”.

Trailing Document Section

The Trailing Document section includes the Signature Log, Mail-Back Address Label, Address Change Form, Allergies/ADR Document, Suspended Prescription Information, Refill Narratives, and Copay Narratives.

- For all sections, with the release of patch PSO\*7\*200, the SSN display changes from six digits to the last four digits.

############################### Signature Log Section

<table>
<colgroup>
<col style="width: 87%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/035.png) VAMC ALBANY NY 12208</p>
<p>500 Ph: 518-555-4307 FEB 2, 2005</p>
<p><strong>By signing below</strong></p>
<p><strong>You acknowledge receipt of the following Rx’s</strong></p>
<p>100002278 (1) 02/2/05 CAPTOPRIL 100MG</p>
<p>Pt. Sig.______________________________________</p>
<p>EXPRESS SCRIPTS</p>
<p>Relation_________Counseling Refused__ Accepted__</p></th>
<th>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/036.png)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>OPPATIENT,ONE ####</strong></td>
<td></td>
</tr>
</tbody>
</table>

- A signature log prints in the bottle label section of the trailing documents. The patient will sign for the medications received on this log. This option is in request to the ePharmacy requirements.
- With the release of patch PSO\*7\*200, the following changes are made:
  - Print current date at top.
  - Do not print user name (if more than 1 prescription was included to be signed, the user name could be different for each one).
  - Correct the spacing and continuation paging issues if one or more of the prescriptions has been discontinued before printing the signature log.
  - Add a barcode to enable scanning to remove the patient's name from the Bingo Board.
  - Add as much of the drug name as will fit on the label.
  - While printing original labels (not reprint of the signature log), if all of the fills have a routing of mail, the signature log will not be printed.
  - The line "Relationship\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Counseled? \_\_\_\_\_" is changed to:  
      
    Relation\_\_\_\_\_ Counseling Refused\_\_ Accepted\_\_

###############################  Mail-Back Address Label Section

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Attn: (119)</p>
<p>EXT</p>
<p>114 HOLLAND AVE</p>
<p>ALBANY, NY 12206</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- There were no changes to this section.

############################### Address Change Form Section

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>HAS YOUR ADDRESS CHANGED?</strong></p>
<p>Write address changes in the blanks, sign the form, and return to your pharmacy.</p>
<p>OPPATIENT, ONE ####</p>
<p>123 OAK STREET_______________________________________</p>
<p>ALBANY, NY 12211_____________________________________</p>
<p>518-555-4567____________________________________________</p>
<p>[ ] Permanent [ ] Temporary until ___/___/___</p>
<p>Signature _______________________________________________</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- The patient’s phone number, followed by an underline, prints on the Address Change form.

############################### <u> </u>Allergies/ADR Document Section

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>OPPATIENT, ONE ####</strong></p>
<p><u>Verified Allergies</u></p>
<p>STRAWBERRIES</p>
<p><u>Verified Adverse Reactions</u></p>
<p>CODEINE</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- The name and last portion of the social security number are bolded and the font is enlarged in the Allergies/ADR section.
- In the Allergies/ADR section, when the TYPE field of the HOSPITAL LOCATION file equals “W” (Ward) for any prescription for this patient, then the word “INPATIENT” prints on the line following the patient name.
- When no information is available or exists in the Allergies/ADR section, then “No Assessment Made” prints under the Verified Allergies heading. When the assessment is No Known Allergies (NKA), the Verified Allergies heading prints with the “NKA” indicator. All other subheadings/lines are removed for both of these examples due to no data being available.

############################### Suspended Prescription Information Section

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>OPPATIENT, ONE #### FEB 2, 2005</p>
<p>The following prescription(s) have been requested and will be mailed to you on or after the date indicated.</p>
<p>Rx# Date</p>
<p>REDACTED FEB 17, 2005</p>
<p>CIMETIDINE 200MG TAB</p>
<p>REDACTED FEB 17, 2005</p>
<p>ACETIC ACID 2% OTIC SOLN</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- When the Suspended Prescription section contains no suspended prescriptions, then the heading does not print.
- The second and third lines of text from the Suspended Prescription section is modified to contain “The following prescription(s) have been requested and will be mailed to you on or after the date indicated”.

###############################  Refill Narrative Section

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>OPPATIENT, ONE #### FEB 2, 2005</p>
<p>Please use the toll free automated refill system to request a refill of your prescriptions. Simply dial 1-800-555-6331 and follow the instructions. Have your FULL social security number and prescription number(s) ready.</p>
<p>This system is available 24 hours a day, 7 days a week. Calling during off peak hours (after 5PM) may allow you to use the system more quickly.</p>
<p>Please contact your VA provider for any non-refillable prescriptions if needed.</p>
<p>You may choose to use the option of mailing the enclosed refill request of each refillable prescription to the pharmacy using the label provided.</p>
<p>*NOTE<strong>*</strong> Medications to be picked up at the pharmacy window MUST be requested in person.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- In the Refill Narrative section, the first seven lines print when there are more than seven lines from the original text. However, it could appear that more than seven lines are printing when the text wraps for a particular line.
- When the Refill Narrative section contains no narrative, then the heading does not print.

############################### Copay Narrative Section

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>OPPATIENT, ONE 9955 FEB 2, 2005</p>
<p>This is a copay prescription.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- In the Copay Narrative section, the first seven lines print when there are more than seven lines from the original text. However, it could appear that more than seven lines are printing when the text wraps for a particular line.
- When the Copay Narrative section contains no narrative, then the heading does not print.

############################### Privacy Notification Narrative Section

When the labels are printed for a patient's prescriptions, the following narrative will be printed on the trailer page in either English or Spanish, depending on the patient's language preference.

The English version reads as follows.

The VA Notice of Privacy Practices, IB 10-163, which outlines your privacy rights, is available online at http://www1.va.gov/Health/ or you may obtain a copy by writing the VHA Privacy Office (19F2), 810 Vermont Avenue NW, Washington DC 20420.

The Spanish language translation for the Privacy Notification reads as follows.

La Notificacion relacionada con las Politicas de Privacidad del Departamento de Asuntos del Veterano, IB-10-163, contiene los detalles acerca de sus derechos de privacidad y esta disponible electronicamente en la siguiente direccion: http://www1.va.gov/Health/. Usted tambien puede conseguir una copia escribiendo a la Oficina de Privacidad del Departamento de Asuntos de

Salud del Veterano, (19F2), 810 Vermont Avenue NW, Washington, DC 20420.

## Multi-Rx Refill Document Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Multi-Rx Refill Document section includes the Patient Instruction section and the Multi-Rx Refill Request Form.

############################### Patient Instruction Section 

| Use the adhesive label above to mail prescription documents to your pharmacy. |
|-------------------------------------------------------------------------------|

- There were no changes to this section.

############################### Multi-Rx Refill Request Form Section 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>OPPATIENT, ONE ####</p>
<p>Please check prescriptions to be refilled, sign the form, then mail or return to your pharmacy.</p>
<p>_____ ALLEGRA 60MG TABS</p>
<p>REFILLS 10 Exp 12/13/2005 Rx# 10000####</p>
<p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/037.png)</p>
<p>_____WELLBUTRIN XL 300MG TABS</p>
<p>REFILLS 2 Exp 06/16/2005 Rx# 10000####</p>
<p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/038.png)</p>
<p>_____ CAPTOPRIL 100MG TABS</p>
<p>REFILLS 3 Exp 02/02/2006 Rx# 10000####</p>
<p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/039.png)</p>
<p><strong>_______________________________________________</strong></p>
<p>Patient’s Signature &amp; Date 514 FEB 2, 2005</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- When the Multi-Rx Refill section is blank, indicating the patient does not have any refillable prescriptions, the SITE NUMBER field of the OUTPATIENT SITE file prints on the bottom of the section and is right-justified.

Example: Laser Label

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 18%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/040.png) VAMC ALBANY NY 12208</p>
<p>500 (11881/) Ph: 518-555-4307</p>
<p><strong>Rx# 100002278</strong> FEB 2, 2005 Fill 1 of 4</p>
<p><strong>OPPATIENT, ONE</strong> ####</p>
<p>TAKE ONE TABLET BY MOUTH TWICE A DAY</p>
<p>Discard after FEB 2, 2006____________ Mfr_______</p>
<p>May refill 3X by FEB 2, 2006</p>
<p>Qty: 60 OPPROVIDER25, THREE</p></th>
<th>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/041.png)</th>
<th colspan="2"><p>Take medication on an empty stomach one hour before or two to the three hours after a meal unless otherwise directed by your doctor.</p>
<p>This drug may impair the ability to drive or operate machinery. Use care until you become familiar with its effects.</p>
<p>It is very important that you take or use this exactly as directed. Do not skip doses or discontinue unless directed by your doctor.</p>
<p>Some ono-prescription drugs may aggravate your condition. Read all labels carefully. If a warning appears, check with your doctor.</p>
<p>CAUTION: Federal law prohibits the transfer of this drug to any person other than the patient for whom it was prescribed.</p></th>
<th><p>Attn: (119)</p>
<p>114 HOLLAND AVE</p>
<p>ALBANY, NY 12206</p>
<p>REGULAR MAIL- Forwarding Service Requested</p>
<p>OPPATIENT, ONE</p>
<p>123 OAK STREET</p>
<p>ALBANY, NY 12211</p>
<p><strong>WINDOW</strong> – PLEASE HOLD FOR PICKUP</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><p>500 (11881/) FEB 2, 2005@12:05</p>
<p>Rx#10000#### FEB 2, 2005 FILL 1 of 4</p>
<p><strong>OPPATIENT, ONE 9955</strong></p>
<p>TAKE ONE TABLET BY MOUTH TWICE A DAY</p>
<p>Qty: 60 OPPROVIDER25, THREE</p>
<p>CAPTOPRIL 100MG TABS</p>
<p>NDC/MFR__________ Lot# ________________</p>
<p>Tech _____________________ RPh _________________</p>
<p>Routing: WINDOW Days supply: 30 Cap: <strong>NON-SAFETY</strong></p>
<p>Isd: FEB 2, 2005 Exp: FEB 2, 2006 Last Fill: APR 6, 2004</p></td>
<td colspan="2"><p><strong>PHONE IN OR MAIL THIS REFILL REQUEST</strong></p>
<p>Follow the refill instructions provided with your prescription.</p>
<p>For Refill Call (518) 555-4307</p>
<p><strong>OPPATIENT, ONE</strong> <strong>9955</strong></p>
<p><strong>Rx#10000XXXX</strong> FEB 2, 2005 FILL 1 of 4</p>
<p>Qty: 60 Days supply:30</p>
<p>third party Rx</p>
<p>CAPTOPRIL 100MG TABS</p>
<p>00003-0485-50</p>
<p><strong>May refill 3X by FEB 2, 2006</strong></p>
<p>COPAY ALBANY-500</p></td>
</tr>
<tr class="even">
<td colspan="3"><p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/042.png)</p>
<p>DRUG WARNING 3N, 16N, 13N, 9N</p>
<p>20</p>
<p>Pat. Stat ONSC Clinic: 5TH F</p></td>
<td colspan="2">![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/043.png)</td>
</tr>
<tr class="odd">
<td colspan="3">OPPATIENT, ONE Rx#: 10000XXXX CAPTOPRIL 100MG TABS</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="5"><p><strong>CAPTOPRIL – ORAL:</strong> (KAP-toe-pril)</p>
<p><strong>WARNING:</strong> This drug can cause serious fetal harm if used during the last six months of pregnancy. If pregnancy occurs, stop using this drug and immediately contact your physician.</p>
<p><strong>USES:</strong> Captopril belongs to a group of drugs called “ACE inhibitors.” ACE inhibitors prevent certain enzymes in the body from constricting blood vessels. This helps to lower blood pressure and makes the heart beat stronger. This medication is used to treat hypertension (high blood pressure), heart failure and kidney disease in certain diabetic patients.</p>
<p><strong>HOW TO USE:</strong> Captopril should be taken on an empty stomach, one hour before or two hours after a meal. Take this medication exactly as prescribed. Try to take it at the same time each day. Do not stop taking this medication without consulting your doctor. Some conditions may become worse when the drug is abruptly stopped. Your dose may need to be gradually decreased. Consult your doctor before using salt substitutes or low salt milk. It is important to continue taking this medication even if you feel well. Most people with high blood pressure do not feel sick.</p>
<p><strong>SIDE EFFECTS:</strong> Dizziness, headache, diarrhea, constipation, loss of appetite, nausea, loss of taste, flushing or fatigue may occur. If these effects persist or worsen, notify your doctor. This medication can increase sensitivity to sunlight. To avoid dizziness and lightheadedness when rising from a seated or lying position, get up slowly. Inform your doctor if you develop: chest pain, tingling of the hands or feet, yellowing of the eyes or skin, dry cough, persistent sore throat. In the unlikely event you have an allergic reaction to this drug, seek immediate medical attention. Symptoms of an allergic reaction include: rash, itching, swelling, dizziness, trouble breathing. If you notice other effects not listed above, contact your doctor or pharmacist.</p>
<p><strong>PRECAUTIONS:</strong> Tell your doctor your medical history, especially of: high blood levels of potassium, kidney problems, liver problems, salt-restricted diet, swelling (angioedema), heart problems, allergies (especially drug allergies). This medicine may make you more prone to sunburn. Wear protective clothing and a sunscreen. Limit your intake of alcohol and avoid overheating because this can aggravate dizziness and lightheadedness. This medication should be used only when clearly needed during the first three months of pregnancy. It is not recommended for use during the last six months of the pregnancy. Discuss the risks and benefits with your doctor. Captopril passes into breast milk. Because the possibility exists that a nursing infant may be harmed, consult your doctor before breast-feeding.</p>
<p><strong>DRUG INTERACTIONS:</strong> Inform your doctor about all the medicine you use (both prescription and nonprescription), especially of: lithium, potassium supplements, potassium-sparing water pills, anti-inflammatory medicine (NSAID like ibuprofen). Avoid “stimulant” drugs that may increase your heart rate such as decongestants or caffeine. Decongestants can be found in cough-and-cold medicines. Do not start or stop any medicine without doctor or pharmacist approval.</p>
<p><strong>OVERDOSE:</strong> If overdose is suspected, contact your local poison control center or emergency room immediately. Symptoms of overdose may include dizziness and weakness.</p>
<p><strong>NOTES:</strong> It is important to have your blood pressure checked regularly while taking this medication. Learn how to monitor your blood pressure. Discuss this with your doctor.</p>
<p><strong>MISSED DOSE:</strong> If you miss a dose, take it as soon as remembered; do not take it if it is almost time for the next dose, instead, skip the missed dose and resume your usual dosing schedule. Do not “double-up” the dose to catch up.</p></td>
</tr>
</tbody>
</table>

Example: Laser Label (continued)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/044.png) VAMC ALBANY NY 12208</p>
<p>500 (11881/) Ph: 518-555-XXXX</p>
<p><strong>By signing below</strong></p>
<p><strong>You acknowledge receipt of the following Rx’s</strong></p>
<p>10000#### (1) 02/2/05 CAPTOPRIL 100MG</p>
<p>Pt. Sig.______________________________________</p>
<p>EXPRESS SCRIPTS</p>
<p>Relation_________Counseling Refused__ Accepted__</p></th>
<th colspan="2"></th>
<th><p>Attn: (119)</p>
<p>EXT</p>
<p>114 HOLLAND AVE</p>
<p>ALBANY, NY 12206</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>HAS YOUR ADDRESS CHANGED?</strong></p>
<p>Write address changes in the blanks, sign the form, and return to your pharmacy.</p>
<p>OPPATIENT, ONE ####</p>
<p>123 OAK STREET_______________________________________</p>
<p>ALBANY, NY 12211_____________________________________</p>
<p>518-555-4567____________________________________________</p>
<p>[ ] Permanent [ ] Temporary until ___/___/___</p>
<p>Signature _______________________________________________</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><p>OPPATIENT, ONE #### FEB 2, 2005</p>
<p>The following prescription(s) have been requested and will be mailed to you on or after the date indicated.</p>
<p>Rx# Date</p>
<p>300#### FEB 17, 2005</p>
<p>CIMETIDINE 200MG TAB</p>
<p>300#### FEB 17, 2005</p>
<p>ACETIC ACID 2% OTIC SOLN</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><p>OPPATIENT, ONE #### FEB 2, 2005</p>
<p>This is a copay prescription.</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

---------------------------------example continues---------------------------------------Example: Laser Label (continued)

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 18%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/045.png)</th>
<th></th>
<th><p>Attn: (119)</p>
<p>EXT</p>
<p>114 HOLLAND AVE</p>
<p>ALBANY, NY 12206</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2">Use the adhesive label above to mail prescription documents to your pharmacy.</td>
</tr>
<tr class="even">
<td><p>OPPATIENT, ONE ####</p>
<p>Please check prescriptions to be refilled, sign the form, then mail or return to your pharmacy.</p>
<p>_____ ALLEGRA 60MG TABS</p>
<p>REFILLS 10 Exp 12/13/2005 Rx# 10000####</p>
<p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/046.png)</p>
<p>_____WELLBUTRIN XL 300MG TABS</p>
<p>REFILLS 2 Exp 06/16/2005 Rx# 10000####</p>
<p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/047.png)</p>
<p>_____ CAPTOPRIL 100MG TABS</p>
<p>REFILLS 3 Exp 02/02/2006 Rx# 10000####</p>
<p>![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/048.png)</p>
<p><strong>_______________________________________________</strong></p>
<p>Patient’s Signature &amp; Date 514 FEB 2, 2005</p></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

# OneVA Pharmacy Laser Labels (PSO\*7\*454)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Narrative Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy Patch PSO\*7\*454 introduced the OneVA Pharmacy label-generation functionality with new/updated label routines. In order to print the OneVA Pharmacy label, each site must use a standard VistA laser label printer and label stock. The printer must be able to print a legal length form and must print barcodes. In addition, the printer must support Hewlett Packard’s Printer Control Language (PCL) version 5 or greater. For additional information related to the label stock refer to the sections in this document titled “Laser Labels Phase II (PSO\*7\*161) and FY07 Q2 Release (PSO\*7\*200).”

In developing the routine(s) to print an OneVA Pharmacy label at a dispensing site-printing device the OneVA Pharmacy patch contains routines cloned from the current PSO label routine. However, the barcode printed on the OneVA Pharmacy label will contain the host site information where the prescription order originated.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/049.png) IMPORTANT: The host pharmacy, the pharmacy where the prescription originated, will be the name and address printed on the label which is consistent with how Consolidated Mail Outpatient Pharmacy (CMOP) processes prescriptions.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/050.png) IMPORTANT: The OneVA Pharmacy requires stock prescription labels and a laser printer that is accessible at the Select LABEL DEVICE: prompt. If either one of the requirements are lacking, then the label will not print as programmed.

When the user executes the OneVA Pharmacy ‘refill’ or ‘partial’ the system displays the label processing refill request message as shown in the following example.

> <u>OneVA Pharmacy Refill – label processing message:</u>

> Processing refill request. Please be patient as it may take a moment

> for the host site to respond and generate your label data...

The system completes the remote refill process and generates the label data for printing.

OneVA Pharmacy patch PSO\*7\*479 modifies routine PSORRX2 to add the following text if no error message is returned when retrieving the label information from the host system. The following text is displayed just prior to the Label Device: ‘ prompt:

Example: Reprinting a OneVA Pharmacy Label

For a refill:

> TRANSACTION SUCCESSFUL... The refill for RX \#REDACTED has been recorded on

> the prescription at the host system.

> Select a printer to generate the label or '^' to bypass printing.

> QUEUE TO PRINT ON

> DEVICE:

For a partial fill:

> TRANSACTION SUCCESSFUL... The partial for RX \#REDACTED has been recorded on

> the prescription at the host system.

> Select a printer to generate the label or '^' to bypass printing.

> QUEUE TO PRINT ON

> DEVICE: ONEVA

> 1 ONEVA NULL NUL

> 2 ONEVAPRT\$PRT BAY PINES TEST LAB

> Choose 1-2\> 1 ONEVA NULL NUL

> Label queued!

> Refill complete for RX \#2718862.

> Press RETURN to continue:

> Updating prescription order list...

OneVA Pharmacy remote refill and remote partial fill actions at times receives the following exception message:

> MESSAGE SENT TO TARGET VISTA; TIME OUT AWAITING REPLY

> Press RETURN to continue:

The user pressed RETURN and must execute the transaction steps for a second time. If the user repeats the transaction, the process successfully executes.

Prescription label is provided for illustration below. The label is identical to what would have printed out at the host site.

VAMC ANYTOWN, OH 45428-0415 VAMC ANYTOWN, OH 45428-0415

984 937-267-0000 (35783/ ) 984 937-267-0000 (35783/ ) 984 (35783/ ) JUL 27,2016@10:7

Rx# 2718862 JUL 27,2016 Fill 2 of 12 Rx# 2718862 JUL 27,2016 Fill 2 of 12 Rx# 2718862 JUL 27,2016 Fil2

PSOPATIENT,SIX PSOPATIENT,SIX PSOPATIENT,SIX

TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED

--TAKE WITH FOOD IF GI UPSET OCCURS/DO NOT --TAKE WITH FOOD IF GI UPSET OCCURS/DO NOT --TAKE WITH FOOD IF GI UPSET OCCURS/DO NOT

CRUSH OR CHEW-- CRUSH OR CHEW-- CRUSH OR CHEW--

PSOPROVIDER,ONE PSOPROVIDER,ONE PSOPROVIDER,ONE

Qty: 60 TAB Qty: 60 TAB Qty: 60 TAB

IBUPROFEN 800MG TAB IBUPROFEN 800MG TAB IBUPROFEN 800MG TAB

10 Refills remain prior to JUN 1,2017 Mfg \_\_\_\_\_\_\_\_ Lot# \_\_\_\_\_\_\_\_

PO BOX 415 COPAY Days Supply: 30 Tech\_\_\_\_\_\_\_\_\_\_RPh\_\_\_\_\_\_\_\_\_

ANYTOWN, OH 45428-0415

ADDRESS SERVICE REQUESTED Read FDA Med Guide

\*\*\*DO NOT MAIL\*\*\* Routing: WINDOW

Days supply: 30 Cap: SAFETY

Isd: MAY 31,2016 Exp: JUN 1,27

PSOPATIENT,SIX \*Indicate address change on back of this form Last Fill: 05/31/2016

\[ \] Permanent Pat. Stat ONSC Clinic: CINCI

\[ \] Temporary until \_\_/\_\_/\_\_ DRUG WARNING 8,10,19

Signature\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PSOPATIENT,SIX PSOPATIENT,SIX

Rx# 2718862

IBUPROFEN 800MG TAB Verified Allergies

DRUG WARNING: ------------------

DO NOT DRINK ALCOHOLIC BEVERAGES

when taking this medication. Non-Verified Allergies

TAKE WITH FOOD OR MILK. ----------------------

This is the same medication you

have been getting. Color, size Verified Adverse Reactions

or shape may appear different. --------------------------

Non-Verified Adverse Reactions

------------------------------

PSOPATIENT,SIX JUL 27,2016

Pharmacy Service (119)

VAMC ANYTOWN, OH

P.O. BOX 415

ANYTOWN, OH 45428-0415

Use the label above to mail the computer

copies back to us. Apply enough postage

to your envelope to ensure delivery.

The VA Notice of Privacy Practices, IB 10-163, which outlines your privacy

rights, is available online at http://www.va.gov/Health/ or you may obtain

a copy by writing the VHA Privacy Office (19F2), REDACTED,

Washington, DC 20420.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/051.png)IMPORTANT: The OneVA Pharmacy requires stock prescription labels and a laser printer that is accessible at the Select LABEL DEVICE: prompt. If either one of the requirements are lacking, then the label will not print as programmed.

## OneVA Pharmacy Reprint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy patch PSO\*7\*454 retrieves the prescription information for the label from the host site and transmits the data back to the dispensing site for printing. As of this writing, there is no ‘REMOTE REPRINT’ option available for OneVA Pharmacy orders. The ‘REPRINT’ action is not operational for the OneVA Pharmacy refills or partials; however, plans are being made to release a new action option as part of the OneVA Pharmacy Phase II initiative.

PSO\*7\*643 removed the ‘REPRINT’ notation from all OneVA refill/partial fill generated labels. It will be reinstated when a future patch introduces a reprint action for OneVA refills/partial fills.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/052.png)IMPORTANT: In order to reprint a label due to a paper jam, a malfunction of the printer, or the need to label multiple packages like inhalers, it is suggested to use the OneVA Pharmacy ‘[Partial Fill Prescription Order](#_Partial_Fill_Prescription)’ process and perform the transaction again.

![](outpatient-pharmacy-version-7-user-manual-supplemental-updated-pso-7-643/053.png)Note: For additional information regarding OneVA Pharmacy partial processing go to the [Outpatient Folder](https://www.va.gov/vdl/application.asp?appid=90) on the VA Software Document Library ([VDL](https://www.va.gov/vdl/application.asp?appid=90)). Locate the *OneVA Pharmacy User Manual* and review the section titled: ‘Label Reprinting’.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

C
Calculating Default Quantity (QTY) values, 10
Creating A New Order, 1, 4
Creating A Sig, 1
Creating the Sig Formula, 6
L
Laser Labels
Address Change Form Section, 28
Allergies/ADR Document Section, 29
Copay Narrative Section, 30
Laser Label Layout, 18
Mail Address Section, 23
Mail-Back Address Label Section, 28
Multi-Rx Refill Document Layout, 20
Multi-Rx Refill Document Section, 38
Multi-Rx Refill Request Form Section, 38
Patient Fill Section, 25
Patient Instruction Section, 38
Patient Medication Information (PMI) Sheet Section, 26
Pharmacy Fill Section, 24
Prescription Label Section, 21
Refill Narrative Section, 30
Signature Log Section, 27
Suspended Prescription Information Section, 29
Trailing Document Layout, 19
Trailing Document Section, 27
Warning Label Section, 22
Laser Labels Phase II (PSO\*7\*161), 18
Laser Printed Prescription Labels, 16
O
OneVA Pharmacy Laser Labels (PSO\*7\*454), 43
OneVA Pharmacy Reprint, 45
