---
title: PSJ*5*160/175 Nurse's User Manual Change Pages
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Nurse's  Change Pages
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*160
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: > Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the exi
audience: 
keywords: 
  - blockquote
  - class
  - table
  - order
  - width
  - style
  - drug
  - patient
  - contents
  - colgroup
page_count: 0
word_count: 5696
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p175_p160_nurse_um_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p175_p160_nurse_um_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/001.png)

INPATIENT MEDICATIONS

> NURSE’S USER MANUAL

> Version 5.0

> January 2005

> (Revised October 2007)

> Department of Veterans Affairs

> VistA Health Systems Design and Development

> Revision History

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 63%" />
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
<p>10/2007</p>
</blockquote></td>
<td><blockquote>
<p>iv, 74a- 74d</p>
<p>5, 12,</p>
<p>16-17, 26,</p>
<p>34-38,</p>
<p>41-42,</p>
<p>72-73</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*175</p>
<p>PSJ*5*160</p>
</blockquote></td>
<td><blockquote>
<p>Modified outpatient header text for display of duplicate orders.</p>
<p>Added new functionality to Duplicate Drug and Duplicate Class definitions.</p>
<p>Modifications for remote allergies, to ensure all allergies are included when doing order checks using VA Drug Class; Analgesic order checks match against specific class only; check for remote data interoperability performed when entering patient’s chart; and list of remote allergies added to Patient Information screen.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/2007</p>
</blockquote></td>
<td><blockquote>
<p>79a-79b,</p>
<p>86a-86b,</p>
<p>92a-92b</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*145</p>
</blockquote></td>
<td><blockquote>
<p>On 24-Hour, 7-Day, and 14-Day MAR Reports, added prompt to include Clinic Orders when printing by Ward or Ward Group.</p>
<p>Also added prompt to include Ward Orders when printing by Clinic or Clinic Group.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/2005</p>
</blockquote></td>
<td><blockquote>
<p>1,</p>
<p>73-74b</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*146</p>
</blockquote></td>
<td><blockquote>
<p>Remote Data Interoperability (RDI) Project:</p>
<p>Removed document revision dates in Section 1. Introduction.</p>
<p>Updated Section 4.9. Order Checks, to include new functionality for remote order checking.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/2005</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*111</p>
</blockquote></td>
<td><blockquote>
<p>Reissued entire document to include updates for Inpatient Medications Orders for Outpatients and Non-Standard Schedules.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page intended for two-sided copying)*
# List Manager


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [List Manager](#list-manager)
    - [List Area (scrolling region)](#list-area-scrolling-region)
    - [Screen Title CWAD\ Indicator](#screen-title-cwad-indicator)
    - [Header Area](#header-area)
- [Order Options](#order-options)
  - [Order Entry](#order-entry)
    - [\[PSJU NE\]](#psju-ne)
  - [Inpatient Order Entry](#inpatient-order-entry)
    - [\[PSJ OE\]](#psj-oe)
  - [Patient Actions](#patient-actions)
    - [Patient Record Update](#patient-record-update)
    - [New Order Entry](#new-order-entry)
    - [Detailed Allergy/ADR List](#detailed-allergyadr-list)
    - [Enter/Edit Allergy/ADR Data](#enteredit-allergyadr-data)
    - [Select Allergy](#select-allergy)
    - [Intervention Menu](#intervention-menu)
    - [Patient Information](#patient-information)
    - [Select Order](#select-order)
  - [Order Checks](#order-checks)
    - [Outpatient Duplicate Orders](#outpatient-duplicate-orders)
    - [Inpatient Duplicate Orders](#inpatient-duplicate-orders)
    - [Example: Duplicate Order Entry Screen](#example-duplicate-order-entry-screen)
> The new screen, which was designed using List Manager, has dramatically changed from the previous version.
> This new screen will give the user:
- More pertinent information
- Easier accessibility to vital reports and areas of a patient’s chart the user may wish to see.
> Please take the time to read over the explanation of the screen and the actions that can now be executed at the touch of a button. This type of preparation before using List Manager is effective in saving time and effort.

### List Area (scrolling region)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/002.png)Message Window
> \* Crises,
Inpatient List Manager

### Screen Title CWAD\* Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/003.png)
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 58%" />
<col style="width: 9%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 15, 2000 11:32:08 Page:</p>
</blockquote></th>
<th><blockquote>
<p>1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT2,TWO PID: 000-00-0002</p>
<p>DOB: 02/22/42 (58) Sex: MALE</p>
<p>Dx: TEST PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 West &lt;A&gt;</p>
</blockquote>
<p>Room-Bed: A-6 Ht(cm): 167.64 (04/21/99)</p>
<p>Wt(kg): 85.00 (04/21/99)</p>
<blockquote>
<p>Admitted: 09/16/99 Last transferred: </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Allergies - Verified: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE,</p>
<p>CHOCOLATE, NUTS, STRAWBERRIES, DUST Non-Verified: AMOXICILLIN, AMPICILLIN, TAPE, FISH,</p>
<p>FLUPHENAZINE DECANOATE</p>
<p>Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: Inpatient narrative for PSJPATIENT2</p>
<p>Outpatient Narrative: This patient doesn't like waiting at the pickup window. He gets very angry.</p>
</blockquote></td>
</tr>
</tbody>
</table>
> ----------Enter ?? for more actions---------------------------------------

### Header Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Action Area
> 5 Inpatient Medications V. 5.0 October 2007 Nurse’s User Manual
> PSJ\*5\*160
> Screen Title: The screen title changes according to what type of information List Manager is displaying (e.g., Patient Information, Non-Verified Order, Inpatient Order Entry, etc.).
> CWAD Indicator: This indicator will display when the crises, warnings, allergies, and directives information has been entered for the patient. (This information is entered via the Text Integration Utilities (TIU) package.) When the patient has Allergy/ADR data defined, an “\<A\>” is displayed to the right of the ward location to alert the user of the existence of this information.
> ![](psj-5-160-175-nurse-s-user-manual-change-pages/004.png)Note: This data may be displayed using the Detailed Allergy/ADR List action). Crises, warnings, and directives are displayed respectively, “\<C\>”,“\<W\>”,“\<D\>”. This data may be displayed using the CWAD hidden action. Any combination of the four indicators can display.
> Header Area: The header area is a “fixed” (non-scrollable) area that displays the patient’s demographic information. This also includes information about the patient’s current admission. The status and type of order are displayed in the top left corner of the heading, and will include the priority (if defined) for pending orders.
> List Area: (scrolling region): This is the section that will scroll (like the previous version) and display the information that an action can be taken on. The Allergies/Reactions line includes non-verified and verified Allergy/ADR information as defined in the Allergy package. The allergy data is sorted by type (DRUG, OTHER, FOOD). If no data is found for a category, the heading is displayed as “Allergies/Reactions: No Allergy Assessment”. The Inpatient and Outpatient Narrative lines may be used by the inpatient pharmacy staff to display information specific to the current admission for the patient.
> Message Window: This section displays a plus sign (+), if the list is longer than one screen, and informational text (i.e., Enter ?? for more actions). If the plus sign is entered at the action prompt, List Manager will “jump” forward to the next screen. The plus sign is only a valid action if it is displayed in the message window.
> Action Area: The list of valid actions available to the user display in this area of the screen. If a double question mark (??) is entered at the “Select Action:” prompt, a “hidden” list of additional actions that are available will be displayed.

# Order Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Unit Dose Medications* option is used to access the order entry, patient profiles, and various reports, and is the main starting point for the Unit Dose system.

> Example: Unit Dose Menu

> Within the Inpatient Medications package there are three different paths the nurse can take to enter a new order or take action on an existing order. They are (1) *Order Entry*, (2) *Non- Verified/Pending Orders* and (3) *Inpatient Order Entry*. Each of these paths differs by the prompts that are presented. Once the nurse has reached the point of entering a new order or selecting an existing order, the process becomes the same for each path.

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/005.png)Note: When the selected order type (non-verified or pending) does not exist (for that patient) while the user is in the *Non-Verified/Pending Orders* option, the user cannot enter a new order or take action on an existing order for that patient.

> Patient locks and order locks are incorporated within the Inpatient Medications package. When a user (User 1) selects a patient through any of the three paths, *Order Entry*, *Non-Verified/Pending Orders,* or *Inpatient Order Entry*, and this patient has already been selected by another user (User 2), the user (User 1) will see a message that another user (User 2) is processing orders for this patient. This will be a lock at the patient level within the Pharmacy packages. When the other user (User 2) is entering a new order for the patient, the user (User 1) will not be able to access the patient due to a patient lock within the VistA packages. A lock at the order level is issued when an order is selected through Inpatient Medications for any action other than new order entry. Any users attempting to access this patient’s order will receive a message that another user is working on this order. This order-level lock is within the VistA packages.

> The three different paths for entering a new order or taking an action on an existing order are summarized in the following sections.

## Order Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSJU NE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Order Entry* option allows the nurse to create, edit, renew, hold, and discontinue Unit Dose orders while remaining in the Unit Dose Medications module.

> The *Order Entry* option functions almost identically to the *Inpatient Order Entry* option, but does not include IV orders on the profile and only Unit Dose orders may be entered or processed.

> After selecting the *Order Entry* option from the *Unit Dose Medications* option, the nurse will be prompted to select the patient. At the “Select PATIENT:” prompt, the user can enter the patient’s name or enter the first letter of the patient’s last name and the last four digits of the patient’s social security number (e.g., P0001). The Patient Information Screen is displayed:

> Example: Patient Information Screen

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 11, 2000 16:09:05 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT1,ONE PID: 000-00-0001</p>
<p>DOB: 08/18/20 (80) Sex: MALE</p>
<p>Dx: TESTING</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 EAST</p>
<p>Room-Bed: B-12 Ht(cm): ( )</p>
<p>Wt(kg): ( ) Admitted: 05/03/00</p>
<p>Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies/Reactions: No Allergy Assessment Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: INP NARR... Outpatient Narrative:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

> The nurse can now enter a Patient Action at the “Select Action: View Profile//” prompt in the Action Area of the screen.

> October 2007 Inpatient Medications V. 5.0 12

> Nurse’s User Manual PSJ\*5\*160

> Example: Short Profile

> Enter ?? for more actions

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/006.png)The nurse can enter a Patient Action at the “Select Action: Quit//” prompt in the Action Area of the screen or choose a specific order or orders.

> When the nurse holds the PSJ RNURSE key, it will be possible to take any available actions on selected Unit Dose or IV orders and verify non-verified orders.

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/007.png)![](psj-5-160-175-nurse-s-user-manual-change-pages/008.png)The following keys may be assigned if the user already holds the PSJ RNURSE key: PSJ RNFINISH key will allow the nurse to finish Unit Dose orders.

> PSJI RNFINISH key will allow the nurse to finish IV orders.

> 15 Inpatient Medications V. 5.0 January 2005 Nurse’s User Manual

## Inpatient Order Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSJ OE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Inpatient Order Entry* option, if assigned, allows the nurse to create, edit, renew, hold, and discontinue Unit Dose and IV orders, as well as put existing IV orders on call for any patient, while remaining in the Unit Dose Medications module.

> When the user accesses the *Inpatient Order Entry* option from the Unit Dose Medications module for the first time within a session, a prompt is displayed to select the IV room in which to enter orders. When only one active IV room exists, the system will automatically select that IV room. The user is then given the label and report devices defined for the IV room chosen. If no devices have been defined, the user will be given the opportunity to choose them. If this option is exited and then re-entered within the same session, the current label and report devices are shown. The following example shows the option re-entered during the same session.

> Example: Inpatient Order Entry

> At the “Select PATIENT:” prompt, the user can enter the patient’s name or enter the first letter of the patient’s last name and the last four digits of the patient’s social security number (e.g., P0001). The Patient Information Screen is displayed:

> Example: Patient Information Screen

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 12, 2000 10:36:38 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT1,ONE PID: 000-00-0001</p>
<p>DOB: 08/18/20 (80) Sex: MALE</p>
<p>Dx: TESTING</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 EAST</p>
<p>Room-Bed: B-12 Ht(cm): ( )</p>
<p>Wt(kg): ( ) Admitted: 05/03/00</p>
<p>Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies/Reactions: No Allergy Assessment Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: INP NARR... Outpatient Narrative:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

> The nurse can now enter a Patient Action at the “Select Action: View Profile//” prompt in the Action Area of the screen.

## Patient Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Actions are the actions available in the Action Area of the List Manager Screen. These actions pertain to the patient information and include editing, viewing, and new order entry.

### Patient Record Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Record Update action allows editing of the Inpatient Narrative and the Patient’s Default Stop Date and Time for Unit Dose Order entry.

> Example: Patient Record Update

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 12, 2000 14:39:07 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT1,ONE PID: 000-00-0001</p>
<p>DOB: 08/18/20 (80) Sex: MALE</p>
<p>Dx: TESTING</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 EAST</p>
<p>Room-Bed: B-12 Ht(cm): ( )</p>
<p>Wt(kg): ( ) Admitted: 05/03/00</p>
<p>Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies/Reactions: No Allergy Assessment Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: INP NARR … Outpatient Narrative:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

> The “INPATIENT NARRATIVE: INP NARR...//” prompt allows the nurse to enter information in a free text format, up to 250 characters.

> The “UD DEFAULT STOP DATE/TIME:” prompt is the date and time entry to be used as the default value for the STOP DATE/TIME of the Unit Dose orders during order entry and renewal processes. This value is used only if the corresponding ward parameter is enabled. The order entry and renewal processes will sometimes change this date and time.

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/009.png)Note: If the Unit Dose order, being finished by the nurse, is received from CPRS and has a duration assigned, the UD DEFAULT STOP DATE/TIME is displayed as the Calc Stop Date/Time.

> When the SAME STOP DATE ON ALL ORDERS parameter is set to Yes, the module will assign the same default stop date for each patient. This date is initially set when the first order is entered for the patient, and can change when an order for the patient is renewed. This date is shown as the default value for the stop date of each of the orders entered for the patient.

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/010.png)Note: If this parameter is not enabled, the user can still edit a patient’s default stop date. Unless the parameter is enabled, the default stop date will not be seen or used by the module.

> Examples of Valid Dates and Times:

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

> Unit Dose

> The New Order Entry action allows the nurse to enter new Unit Dose and IV orders for the patient depending upon the order option selected (*Order Entry*, *Non-Verified Pending Orders*, or *Inpatient Order Entry*). Only one user is able to enter new orders on a selected patient due to the patient lock within the VistA applications. This minimizes the chance of duplicate orders.

> For Unit Dose order entry, a response must be entered at the “Select DRUG:” prompt. The nurse can select a particular drug or enter a pre-defined order set.

> Depending on the entry in the “Order Entry Process:” prompt in the *Inpatient User Parameters Edit* option, the nurse will enter a regular or abbreviated order entry process. The abbreviated order entry process requires entry into fewer fields than regular order entry. Beside each of the prompts listed below, in parentheses, will be the word regular, for regular order entry and/or abbreviated, for abbreviated order entry.

- “Select DRUG:” (Regular and Abbreviated)

> Nurses select Unit Dose medications directly from the DRUG file. The Orderable Item for the selected drug will automatically be added to the order, and all Dispense Drugs entered for the order must be linked to that Orderable Item. If the Orderable Item is edited, data in the DOSAGE ORDERED field and the DISPENSE DRUG field will be deleted. If multiple Dispense Drugs are needed in an order, they may be entered by selecting the DISPENSE DRUG field from the edit list before accepting the new order. After each Dispense Drug is selected, it will be checked against the patient’s current medications for duplicate drug or class, and drug-drug/drug-allergy interactions. (See Section 4.9 Order Checks for more information.)

- “NATURE OF ORDER:” (Regular and Abbreviated)

> This is the method the provider used to communicate the order to the user who entered or took action on the order. Nature of Order is defined in CPRS. Written will be the default for new orders entered. When a new order is created due to an edit, the default will be Service Correction. The following table shows some Nature of Order examples.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 40%" />
<col style="width: 24%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Nature of Order</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Prompted for Signature in CPRS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Chart Copy Printed?</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Written</p>
</blockquote></td>
<td><blockquote>
<p>The source of the order is a written doctor’s order</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Verbal</p>
</blockquote></td>
<td><blockquote>
<p>A doctor verbally requested the order</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Telephoned</p>
</blockquote></td>
<td><blockquote>
<p>A doctor telephoned the service to request the order</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Service Correction</p>
</blockquote></td>
<td><blockquote>
<p>The service is discontinuing or adding new orders to carry out the intent of an order already received</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Duplicate</p>
</blockquote></td>
<td><blockquote>
<p>This applies to orders that are discontinued because they are a duplicate of another order</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Policy</p>
</blockquote></td>
<td><blockquote>
<p>These are orders that are created as a matter of hospital policy</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The Nature of Order abbreviation will display on the order next to the Provider’s Name. The abbreviations will be in lowercase and enclosed in brackets. Written will display as \[w\], telephoned as \[p\], verbal as \[v\], policy as \[i\], electronically entered as \[e\], and service correction as \[s\]. If the order is electronically signed through the CPRS package <u>AND</u> the CPRS patch OR\*3\*141 is installed on the user’s system, then \[es\] will appear next to the Provider’s Name instead of the Nature of Order abbreviation.

> Example: New Order Entry

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Feb 14, 2001 10:21:33 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT1,ONE PID: 000-00-0001</p>
<p>DOB: 08/18/20 (80) Sex: MALE</p>
<p>Dx: TEST</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 EAST</p>
<p>Room-Bed: Ht(cm): ( )</p>
<p>Wt(kg): ( ) Admitted: 11/07/00</p>
<p>Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies/Reactions: No Allergy Assessment Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: Narrative for Patient PSJPATIENT1 Outpatient Narrative:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

> -----------------------------------------report continues--------------------------------

> October 2007 Inpatient Medications V. 5.0 26

> Nurse’s User Manual PSJ\*5\*160

> Example: New Order Entry (continued)

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 37%" />
<col style="width: 5%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>NON-VERIFIED IV Feb 28, 2002@13:</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>56:44 Page: 1 of 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PSJPATIENT1,ONE Ward: 1 EAST PID: 000-00-0001 Room-Bed: B-12 DOB: 08/18/20 (81)</p>
<p>Sex: MALE</p>
<p>Dx: TESTING Last</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Ht(cm): ( )</p>
<p>Wt(kg): ( )</p>
<p>Admitted: 05/03/00 transferred: </p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>*(1) Additives:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Type: PIGGYBACK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MULTIVITAMINS 2 ML</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>(2) Solutions:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>0.9% SODIUM CHLORIDE 100 ML</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Duration:</p>
</blockquote></td>
<td><blockquote>
<p>(4)</p>
</blockquote></td>
<td><blockquote>
<p>Start: 02/28/02 13:56</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>(3) Infusion Rate: INFUSE OVER 125 MIN.</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>*(5)</td>
<td><blockquote>
<p>Med Route: IV</p>
</blockquote></td>
<td><blockquote>
<p>(6)</p>
</blockquote></td>
<td><blockquote>
<p>Stop: 03/30/02 24:00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>*(7)</td>
<td><blockquote>
<p>Schedule: QID</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Last Fill: </p>
</blockquote></td>
</tr>
<tr class="even">
<td>(8)</td>
<td><blockquote>
<p>Admin Times: 09-13-17-21</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Quantity: 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>*(9)</td>
<td><blockquote>
<p>Provider: PSJPROVIDER,ONE [w]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Cum. Doses:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>*(10)Orderable Item: MULTIVITAMINS INJ</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Instructions:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>(11) Other Print:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \+ Enter ?? for more actions

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 7%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DC</p>
</blockquote></th>
<th><blockquote>
<p>Discontinue</p>
</blockquote></th>
<th><blockquote>
<p>RN (Renew)</p>
</blockquote></th>
<th><blockquote>
<p>VF</p>
</blockquote></th>
<th><blockquote>
<p>Verify</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>(Hold)</p>
</blockquote></td>
<td><blockquote>
<p>OC (On Call)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ED</p>
</blockquote></td>
<td><blockquote>
<p>Edit</p>
</blockquote></td>
<td><blockquote>
<p>AL Activity Logs</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>Select Item(s): Next Screen// <strong>VF</strong> Verify</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Detailed Allergy/ADR List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Detailed Allergy/ADR List action displays a detailed listing of the selected item from the patient’s Allergy/ADR List. Entry to the *Edit Allergy/ADR Data* option is provided with this list also.

### Enter/Edit Allergy/ADR Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Provides access to the Adverse Reaction Tracking (ART) package to allow entry and/or edit of allergy adverse reaction data for the patient. See the Allergy package documentation for more information on Allergy/ADR processing.

### Select Allergy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Allows the user to view a specific allergy.

> January 2005 Inpatient Medications V. 5.0 33

> Nurse’s User Manual

### Intervention Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/011.png)This option is only available to those users who hold the PSJ RPHARM key.

> The Intervention Menu action allows entry of new interventions and existing interventions to be edited, deleted, viewed, or printed. Each kind of intervention will be discussed and an example will follow.

- New: This option is used to add an entry into the APSP INTERVENTION file.

> Example: New Intervention

<table style="width:100%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep</p>
</blockquote></th>
<th><blockquote>
<p>22, 2000</p>
</blockquote></th>
<th><blockquote>
<p>08:03:07</p>
</blockquote></th>
<th><blockquote>
<p>Page:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT2,TWO PID: 000-00-0002</p>
<p>DOB: 02/22/42 (58) Sex: MALE</p>
<p>Dx: TEST PATIENT</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>Ward: 1 West &lt;A&gt;</p>
</blockquote>
<p>Room-Bed: A-6 Ht(cm): 167.64 (04/21/99)</p>
<p>Wt(kg): 85.00 (04/21/99)</p>
<p>Admitted: 09/16/99</p>
<p>Last transferred: </p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p>Allergies - Verified: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE,</p>
<p>CHOCOLATE, NUTS, STRAWBERRIES, DUST Non-Verified: AMOXICILLIN, AMPICILLIN, TAPE, FISH,</p>
<p>FLUPHENAZINE DECANOATE</p>
<p>Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: Inpatient narrative</p>
<p>Outpatient Narrative: This is the Outpatient Narrative. This patient doesn't like waiting at the pickup window. He gets very angry.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

- Edit: This option is used to edit an existing entry in the APSP INTERVENTION file.

> Example: Edit an Intervention

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 22, 2000 08:03:07 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT2,TWO PID: 000-00-0002</p>
<p>DOB: 02/22/42 (58) Sex: MALE</p>
<p>Dx: TEST PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 West &lt;A&gt;</p>
</blockquote>
<p>Room-Bed: A-6 Ht(cm): 167.64 (04/21/99)</p>
<p>Wt(kg): 85.00 (04/21/99)</p>
<blockquote>
<p>Admitted: 09/16/99 Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies - Verified: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE,</p>
<p>CHOCOLATE, NUTS, STRAWBERRIES, DUST Non-Verified: AMOXICILLIN, AMPICILLIN, TAPE, FISH,</p>
<p>FLUPHENAZINE DECANOATE</p>
<p>Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: Inpatient narrative</p>
<p>Outpatient Narrative: This is the Outpatient Narrative. This patient doesn't like waiting at the pickup window. He gets very angry.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

- Delete: This option is used to delete an entry from the APSP INTERVENTION file. The nurse may only delete an entry that was entered on the same day.

> Example: Delete an Intervention

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 22, 2000 08:03:07 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT2,TWO PID: 000-00-0002</p>
<p>DOB: 02/22/42 (58) Sex: MALE</p>
<p>Dx: TEST PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 West &lt;A&gt;</p>
</blockquote>
<p>Room-Bed: A-6 Ht(cm): 167.64 (04/21/99)</p>
<p>Wt(kg): 85.00 (04/21/99)</p>
<blockquote>
<p>Admitted: 09/16/99 Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies - Verified: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE,</p>
<p>CHOCOLATE, NUTS, STRAWBERRIES, DUST Non-Verified: AMOXICILLIN, AMPICILLIN, TAPE, FISH,</p>
<p>FLUPHENAZINE DECANOATE</p>
<p>Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: Inpatient narrative</p>
<p>Outpatient Narrative: This is the Outpatient Narrative. This patient doesn't like waiting at the pickup window. He gets very angry.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

- View: This option is used to display Pharmacy Interventions in a captioned format.

> Example: View an Intervention

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 22, 2000 08:03:07 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT2,TWO PID: 000-00-0002</p>
<p>DOB: 02/22/42 (58) Sex: MALE</p>
<p>Dx: TEST PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 West &lt;A&gt;</p>
</blockquote>
<p>Room-Bed: A-6 Ht(cm): 167.64 (04/21/99)</p>
<p>Wt(kg): 85.00 (04/21/99)</p>
<blockquote>
<p>Admitted: 09/16/99 Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies - Verified: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE,</p>
<p>CHOCOLATE, NUTS, STRAWBERRIES, DUST Non-Verified: AMOXICILLIN, AMPICILLIN, TAPE, FISH,</p>
<p>FLUPHENAZINE DECANOATE</p>
<p>Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: Inpatient narrative</p>
<p>Outpatient Narrative: This is the Outpatient Narrative. This patient doesn't like waiting at the pickup window. He gets very angry.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

- Print: This option is used to obtain a captioned printout of Pharmacy Interventions for a certain date range. It will print out on normal width paper and can be queued to print at a later time.

> Example: Print an Intervention

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 22, 2000 08:03:07 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT2,TWO PID: 000-00-0002</p>
<p>DOB: 02/22/42 (58) Sex: MALE</p>
<p>Dx: TEST PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 West &lt;A&gt;</p>
</blockquote>
<p>Room-Bed: A-6 Ht(cm): 167.64 (04/21/99)</p>
<p>Wt(kg): 85.00 (04/21/99)</p>
<blockquote>
<p>Admitted: 09/16/99 Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies - Verified: CARAMEL, CN900, LOMEFLOXACIN, PENTAMIDINE, PENTAZOCINE,</p>
<p>CHOCOLATE, NUTS, STRAWBERRIES, DUST Non-Verified: AMOXICILLIN, AMPICILLIN, TAPE, FISH,</p>
<p>FLUPHENAZINE DECANOATE</p>
<p>Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: Inpatient narrative</p>
<p>Outpatient Narrative: This is the Outpatient Narrative. This patient doesn't like waiting at the pickup window. He gets very angry.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example: Active Complex Order in Profile View

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Inpatient Order Entry Mar 07, 2004@15:00:05 Page: 1 of 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT1,ONE Ward: 1 EAST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PID: 000-00-0001 Room-Bed: B-12 Ht(cm): ( )</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DOB: 08/18/20 (81) Wt(kg): ( )</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sex: MALE Admitted: 03/03/04</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Dx: TESTING Last transferred: </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>- - - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - - - -</p>
</blockquote>
<ol type="1">
<li><p>CAPTOPRIL TAB C 03/26 03/27 A Give: 25MG PO QDAILY</p></li>
<li><p>CAPTOPRIL TAB C 03/28 03/29 A Give: 50MG PO BID</p></li>
<li><p>CAPTOPRIL TAB C 03/30 03/31 A Give: 100MG PO TID</p></li>
</ol></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

### Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Information screen is displayed for the selected patient. The header contains the patient’s demographic data, while the list area contains Allergy/Adverse Reaction data, including remote data and Pharmacy Narratives. If an outpatient is selected, all future appointments in clinics that allow Inpatient Medications orders will display in the list area, too.

> Example: Patient Information

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>Sep 13, 2000 15:04:31 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT1,ONE PID: 000-00-0001</p>
<p>DOB: 08/18/20 (80) Sex: MALE</p>
<p>Dx: TESTING</p>
</blockquote></td>
<td><blockquote>
<p>Ward: 1 EAST</p>
<p>Room-Bed: B-12 Ht(cm): ( )</p>
<p>Wt(kg): ( ) Admitted: 05/03/00</p>
<p>Last transferred: </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies/Reactions: No Allergy Assessment Remote:</p>
<p>Adverse Reactions:</p>
<p>Inpatient Narrative: Narrative for Patient PSJPATIENT1 Outpatient Narrative:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

> Example: Patient Information Screen for Outpatient Receiving Inpatient Medications

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 55%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Information</p>
</blockquote></th>
<th><blockquote>
<p>May 12, 2003 14:27:13 Page: 1 of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT3,THREE</p>
</blockquote></td>
<td><blockquote>
<p>Last Ward: 1 West</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PID: 000-00-0003</p>
</blockquote></td>
<td>Last Room-Bed: Ht(cm): ( )</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DOB: 02/01/55 (48)</p>
</blockquote></td>
<td>Wt(kg): ( )</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sex: FEMALE</p>
</blockquote></td>
<td><blockquote>
<p>Last Admitted: 01/13/98</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Dx: TESTING</p>
</blockquote></td>
<td><blockquote>
<p>Discharged: 01/13/98</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Allergies/Reactions: No Allergy Assessment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Remote:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Adverse Reactions:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Inpatient Narrative:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Outpatient Narrative:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Clinic: Date/Time of Appointment:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Clinic A May 23, 2003/9:00 am</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Flu Time Clinic June 6, 2003/10:00 am</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

### Select Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Select Order action is used to take action on a previously entered order by selecting it from the profile, after the patient is selected and length of profile is chosen (i.e., short or long).

> Example: Selecting an Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Inpatient Order Entry Mar 07, 2002@13:01:56 Page: 1 of 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJPATIENT1,ONE Ward: 1 EAST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PID: 000-00-0001 Room-Bed: B-12 Ht(cm): ( )</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DOB: 08/18/20 (81) Wt(kg): ( )</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sex: MALE Admitted: 05/03/00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Dx: TESTING Last transferred: </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 in 0.9% SODIUM CHLORIDE 1000 ML 125 ml/hrC 03/07 03/07 E</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 in 5% DEXTROSE 50 ML 125 ml/hr C 03/06 03/06 E</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 CEPHAPIRIN 1 GM C 03/04 03/09 A</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>in DEXTROSE 5% IN N. SALINE 100 ML QID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4 ASPIRIN CAP,ORAL O 03/07 03/07 E</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Give: 650MG PO NOW</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>- - - - - - - - - - - - - - - - P E N D I N G - - - - - - - - - - - - - - - -</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5 in DEXTROSE 10% 1000 ML 125 ml/hr ?  P</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter ?? for more actions

> -----------------------------------------report continues--------------------------------

> Example: Inpatient Profile

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>I N P A T I E N T M E D I C A T I O N S 09/21/00 12:33</p>
<p>SAMPLE HEALTHCARE SYSTEM</p>
<blockquote>
<p>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PSJPATIENT1,ONE Ward: 1 EAST</p>
<p>PID: 000-00-0001 Room-Bed: B-12 Ht(cm): ( )</p>
<p>DOB: 08/18/20 (80) Wt(kg): ( )</p>
<p>Sex: MALE Admitted: 05/03/00</p>
<p>Dx: TESTING</p>
<p>Allergies:</p>
<p>ADR:</p>
<p>- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -</p>
</blockquote>
<ol type="1">
<li><p>-&gt; AMPICILLIN CAP C 09/07 09/21 A Give: 500MG PO QID</p></li>
</ol>
<blockquote>
<p>- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -</p>
</blockquote>
<ol start="2" type="1">
<li><p>DOXEPIN CAP,ORAL ?  N Give: 100MG PO Q24H</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Patient: PSJPATIENT1,ONE Status: ACTIVE Orderable Item: AMPICILLIN CAP</p>
<p>Instructions:</p>
<p>Dosage Ordered: 500MG</p>
<p>Duration: Start: 09/07/00 15:00</p>
<p>Med Route: ORAL (PO) Stop: 09/21/00 24:00 Schedule Type: CONTINUOUS</p>
<p>Schedule: QID</p>
<p>Admin Times: 01-09-15-20</p>
<p>Provider: PSJPROVIDER,ONE [es]</p>
<p>Units Units Inactive</p>
<p>Dispense Drugs U/D Disp'd Ret'd Date</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AMPICILLIN 500MG CAP 1 0 0</p>
<p>ORDER NOT VERIFIED</p>
<p>Entry By: PSJPROVIDER,ONE Entry Date: 09/07/00 13:37</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>Date: 09/07/00 14:07 User: PSJPHARMACIST,ONE Activity: ORDER VERIFIED BY PHARMACIST</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table>

> -----------------------------------------report continues--------------------------------

> Example: Inpatient Profile (continued)

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient: PSJPATIENT1,ONE</p>
<p>Orderable Item: DOXEPIN CAP,ORAL Instructions:</p>
<p>Dosage Ordered: 100MG Duration:</p>
<p>Med Route: ORAL (PO) Schedule Type: NOT FOUND</p>
<p>Schedule: Q24H (No Admin Times)</p>
<p>Provider: PSJPROVIDER,ONE [es] Special Instructions: special for DOXEPIN</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>Status: NON-VERIFIED</p>
<p>Start: 09/20/00 09:00</p>
<p>Stop: 10/04/00 24:00</p>
<p>Units Units Inactive U/D Disp'd Ret'd Date</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Dispense Drugs</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DOXEPIN 100MG U/D</p>
</blockquote></td>
<td><blockquote>
<p>1 0 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DOXEPIN 25MG U/D</p>
</blockquote></td>
<td><blockquote>
<p>1 0 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORDER NOT VERIFIED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Self Med: NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Entry By: PSJPROVIDER,ONE</p>
</blockquote></td>
<td><blockquote>
<p>Entry Date: 09/19/00 09:55</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Order checks (allergy/adverse drug reactions, drug-drug interactions, duplicate drug, and duplicate class) are performed when a new medication order is placed through either the Inpatient Medications or CPRS applications. They are also performed when medication orders are renewed or during the finishing processes. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error due to the omission of an order check when a non-active medication order is renewed.

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/012.png)Note: The check for remote data availability is performed when entering a patient’s chart, rather than on each order.

> The following actions will initiate an order check:

- Action taken through Inpatient Medications to enter a medication order will initiate order checks (allergy, drug-drug interaction, duplicate drug, and duplicate class) against existing medication orders.
- Action taken through Inpatient Medications to finish a medication order placed through CPRS will initiate order checks (allergy, drug-drug interaction, duplicate drug, and duplicate class) against existing medication orders.
- Action taken through IV Menu to finish a medication order placed through CPRS will initiate order checks (allergy, drug-drug interaction, duplicate drug, and duplicate class) against existing medication orders.
- Action taken through Inpatient Medications to renew a medication order will initiate order checks (allergy, drug-drug interaction, duplicate drug, and duplicate class) against existing medication orders.
- Action taken through IV Menu to renew a medication order will initiate order checks (allergy, drug-drug interaction, duplicate drug, and duplicate class) against existing medication orders.

> 72 Inpatient Medications V. 5.0 October 2007

> The following are the different items used for the order checks:

- Checks each Dispense Drug within the Unit Dose order for allergy/adverse drug reactions.
- Checks each Dispense Drug within the Unit Dose order against existing orders for drug- drug interaction, duplicate drug, and duplicate class.
- Checks each additive within an IV order for drug-drug interaction, duplicate drug, and duplicate class against solutions or other additives within the order.
- Checks each IV order solution for allergy/adverse reactions.
- Checks each IV order solution for drug-drug interaction against other solutions or additives within the order.
- Checks each IV order additive for allergy/adverse reaction.
- Checks each IV order additive for drug-drug interaction, duplicate drug, and duplicate class against existing orders for the patient.
- Checks each IV order solution for drug-drug interaction against existing orders for the patient.

> Override capabilities are provided based on the severity of the order check, if appropriate.

> Order Checks warnings will be displayed/processed in the following order:

- Duplicate drug or class
- Critical or significant drug-drug interactions
- Critical or significant drug-allergy interactions

> These checks will be performed at the Dispense Drug level. Order checks for IV orders will use the Dispense Drugs linked to each additive/solution in the order. All pending, non-verified, active and renewed Inpatient orders, active Outpatient orders and active Non-Veterans Affairs (VA) Meds documented in CPRS will be included in the check. In addition, with the release of OR\*3\*238, order checks will be available using data from the Health Data Repository Historical (HDR-Hx) and the Health Data Repository Interim Messaging Solution (HDR-IMS). This will contain both Outpatient orders from other VAMCs as well as from Department of Defense (DoD) facilities, if available. Any remote Outpatient order that has been expired for 30 days or less will be included in the list of medications to be checked.

> There is a slight difference in the display of local Outpatient orders compared with remote Outpatient orders. Below are examples of the two displays:

> Example: Local Outpatient Order Display

<table>
<colgroup>
<col style="width: 78%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>The patient has the following Outpatient order(s):</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Rx #: 40074 PHENYTOIN 100MG (Extended) CAP</p>
<p>Status: Active Issued: 07/11/05 SIG: TAKE ONE CAPSULE BY MOUTH TWICE A DAY</p>
<p>QTY: 60 # of refills: 11</p>
<p>Provider: PSOPROVIDER,ONE Refills remaining: 11</p>
<p>Last filled on: 07/11/05 Days Supply: 30</p>
</blockquote></th>
</tr>
<tr class="header">
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Remote Outpatient Order Display

> In the Remote Outpatient Order Display example above, notice the name of the remote location has been added. In addition, the number of refills is not available.

> If the order is entered by the Orderable Item only, these checks will be performed at the time the Dispense Drug(s) is specified. The checks performed include:

- Duplicate Drug - If the patient is already receiving orders containing the Dispense Drug selected for the new order, these duplicate orders are displayed. Inpatient duplicate orders of this kind are displayed in a numbered list. The user is first asked whether or not to continue the current order. If the user selects to continue the order then the user is prompted with which, if any, numbered Inpatient duplicate orders to discontinue. The user may enter a range of numbers from the numbered list of duplicate orders or bypass the prompt by selecting \<Enter\> and continue with the order. Entry of duplicate drug orders will be allowed. Only Additives are included in the duplicate drug check for IV orders. The solutions are excluded from this check.
- Duplicate Class - If the patient is already receiving orders containing a Dispense Drug in the same class as one of the Dispense Drugs in the new order, the orders containing the drug in that class are displayed. Inpatient duplicate orders of this kind are displayed in a numbered list. The user is first asked whether or not to continue the current order. If the user selects to continue the order then the user is prompted with which, if any, numbered Inpatient duplicate orders to discontinue. The user may enter a range of numbers from the numbered list of duplicate orders or bypass the prompt by selecting \<Enter\> and continue with the order. Entry of orders with duplicate drugs of the same class will be allowed.
- Drug-Drug Interactions - Drug-drug interactions will be either critical or significant. If the Dispense Drug selected is identified as having an interaction with one of the drugs the patient is already receiving, the order the new drug interacts with will be displayed.
- Drug-Allergy Interactions - Drug-allergy interactions will be either critical or significant. If the Dispense Drug selected is identified as having an interaction with one of the patient’s allergies, the allergy the drug interacts with will be displayed.

> ![](psj-5-160-175-nurse-s-user-manual-change-pages/013.png)Note: For a Significant Interaction, the user who holds the PSJ RPHARM key is allowed to enter an intervention, but one is not required. For a Critical Interaction, the user who holds the PSJ RPHARM key <u>must</u> enter an intervention before continuing.

### Outpatient Duplicate Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Outpatient duplicate order check results display together on the first screen before all other order check information. These results are displayed for informational purposes only. The header for Outpatient duplicate orders reads as follows:

> The patient has the following Outpatient order(s):

### Inpatient Duplicate Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Duplicate drug and duplicate drug class Inpatient orders display together in a numbered sequence. The user selects from the numbered sequence the order(s) to be discontinued, if any. The header for Inpatient duplicate orders reads as follows:

> After the user has discontinued an order, if any duplicate Inpatient orders remain, they are displayed again in a numbered list. The following header is displayed:

> This cycle repeats until there are no more duplicate Inpatient orders or until the user indicates there are no more duplicate Inpatient orders they wish to discontinue.

### Example: Duplicate Order Entry Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 95%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Unit Dose Order Entry Jun 27, 2006@16:08:46 Page: 1 of 1</p>
<p>PSJPATIENT,ONE Ward: 7B A</p>
<p>PID: 666-666-1234 Room-Bed: Ht(cm): ( ) DOB: --/--/70 (35) Wt(kg): ( )</p>
</blockquote>
<p>Sex: MALE Admitted: 03/08/06</p>
<p>Dx: SICK Last transferred: </p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Select DRUG: warf</p>
<p>Lookup: DRUG GENERIC NAME</p>
</blockquote>
<ol type="1">
<li><p>WARFARIN 2MG TABS BL110</p></li>
<li><p>WARFARIN SOD. 50MG COMB.PACK. BL110</p></li>
<li><p>WARFARIN SODIUM 5MG S.T. BL110</p></li>
</ol>
<blockquote>
<p>CHOOSE 1-3: 2 WARFARIN SOD. 50MG COMB.PACK. BL110</p>
<p>The patient has the following Outpatient order(s):</p>
</blockquote></td>
<td rowspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rx #: 300410 ASPIRIN BUFFERED 325MG TAB</p>
<p>Status: Active Issued: 06/08/06 SIG: TAKE TWO TABLETS BY MOUTH AFTER MEALS TAKE THESE</p>
<p>AFTER YOU GET HOME</p>
<p>QTY: 100 # of refills: 0 Provider: PSOPROVIDER,ONE Refills remaining: 0</p>
<p>Last filled on: 06/08/06 Days Supply: 90</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>This patient is receiving the following medication that has an interaction with WARFARIN SOD. 50MG COMB.PACK.:</p>
<p>ASPIRIN TAB,EC C 06/19 07/03 A Give: 324MG PO Q4H</p>
<p>This patient is already receiving the following INPATIENT order(s) for the same drug or in the same drug class as WARFARIN SOD. 50MG COMB.PACK.:</p>
</blockquote>
<ol type="1">
<li><p>WARFARIN TAB C 06/27 07/03 A Give: 2MG PO Q6H PSJProvider, One</p></li>
<li><p>WARFARIN TAB C 06/27 07/03 A Give: 2MG PO Q2H PSJProvider, Two</p></li>
</ol>
<blockquote>
<p>Do you wish to continue with the current order? YES// yes YES Do you wish to DISCONTINUE any of the listed orders? NO// Y Choose for DISCONTINUE 1-2: 1</p>
<p>NATURE OF ORDER: (TBD)// &lt;cr&gt;</p>
<p>REQUESTING PROVIDER: PSJProvider, One P1O</p>
<p><em>------------------screen continues on next page------------------</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Discontinuing Duplicate Inpatient Orders

> When duplicate Inpatient orders are found, the following prompt is presented after each display or redisplay of a numbered list:

> Do you wish to DISCONTINUE any of the listed orders? NO//

> Note: If the user selects the default of NO, the order process continues.

> If the user enters YES to the DISCONTINUE prompt, the following prompt is presented to allow selecting orders:

> Choose for DISCONTINUE 1-N:

> Note: N represents the highest numbered duplicate order in the numbered list.

> Exiting the Order Process

> When duplicate Inpatient orders have been found, the following prompt is displayed after the first numbered list of duplicate Inpatient orders:

> Do you wish to continue with the current order? YES//

> Note: The wording of this existing prompt has been slightly modified. Also, the current default of NO has been changed to YES.

> Each time a user chooses to discontinue an Inpatient duplicate order(s), a prompt is presented to enter a value for NATURE OF ORDER. This value applies to all of those orders just selected to be discontinued.

> Also, each time a user chooses to discontinue an Inpatient duplicate order(s), a prompt is presented to enter a value for Requesting PROVIDER. This value applies to all of those orders just selected to be discontinued.