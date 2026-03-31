---
title: Inpatient Medications Version 5 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Table of Contents](#table-of-contents) - [# # # Introduction](#introduction) - [# List Manager](#list-manager) - [Using List Manager](#using-list-manager) - [Order Processing](#order-processing) - [Non-Verified/Pending Orders](#non-verifiedpending-orders) - [Inpatient Order Entry/Order Entry (UD)
audience: 
keywords: 
  - order
  - orders
  - entry
  - patient
  - schedule
  - dose
  - inpatient
  - unit
  - table
  - contents
page_count: 0
word_count: 4918
section_count: 11
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/iprn5_0.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/iprn5_0.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

![](inpatient-medications-version-5-release-notes/001.png)

INPATIENT MEDICATIONS<span class="smallcaps">RELEASE NOTES</span>Version 5.0

December 1997

<span class="smallcaps">REVISED 2-15-98</span>

Office of Chief Information Officer

# Table of Contents


## Table of Contents

- [Table of Contents](#table-of-contents)
- [# # # Introduction](#introduction)
- [# List Manager](#list-manager)
- [Using List Manager](#using-list-manager)
- [Order Processing](#order-processing)
  - [Non-Verified/Pending Orders](#non-verifiedpending-orders)
  - [Inpatient Order Entry/Order Entry (UD)](#inpatient-order-entryorder-entry-ud)
  - [## Patient Profile List](#patient-profile-list)
  - [Unit Dose Order View List](#unit-dose-order-view-list)
  - [Unit Dose Order View List](#unit-dose-order-view-list-1)
  - [Inpatient Medication IV Order View](#inpatient-medication-iv-order-view)
  - [## ## IV Fluid Order View](#iv-fluid-order-view)
  - [New Order Entry (Unit Dose)](#new-order-entry-unit-dose)
  - [New Order Entry (IV)](#new-order-entry-iv)
  - [Other Order Actions - Edit, Hold, Discontinue, Renew, On Call](#other-order-actions-edit-hold-discontinue-renew-on-call)
Introduction [1](#introduction)
List Manager [3](#list-manager)
Using List Manager [4](#using-list-manager)
Order Processing [9](#order-processing)
Non-Verified/Pending Orders [9](#non-verifiedpending-orders)
Inpatient Order Entry/Order Entry (UD) [9](#inpatient-order-entryorder-entry-ud)
Patient Profile List [12](#patient-profile-list)
Unit Dose Order View List [13](#unit-dose-order-view-list)
Unit Dose Order View List [13](#unit-dose-order-view-list-1)
Inpatient Medication IV Order View [14](#inpatient-medication-iv-order-view)
IV Fluid Order View [14](#iv-fluid-order-view)
New Order Entry (Unit Dose) [16](#new-order-entry-unit-dose)
New Order Entry (IV) [20](#new-order-entry-iv)
Other Order Actions - Edit, Hold, Discontinue, Renew, On Call [23](#other-order-actions---edit-hold-discontinue-renew-on-call)

# # # # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications Unit Dose module is a method of computerizing inpatient drug distribution within the hospital. Unit dose orders are entered/edited by a ward clerk, healthcare provider (physician), nurse, or pharmacist, and verified by a nurse and pharmacist. Orders may also be canceled or renewed as appropriate. Once active, the orders are dispensed to the wards by means of the pick list. The system allows for dispensing tracking from the pick list.

The Unit Dose module can also produce a 24-hour, 7-day, or 14-day Medication Administration Record (MAR). This report is a computerized Continuing Medication Record (CMR). The MAR contains patient demographics, and all active orders with their administration schedules. With access to the MARs, you have the following four options:

> 1\. Use the computerized MAR—update it with labels,

> 2\. Use the computerized MAR without labels—update by hand,

> 3\. Use the manual CMR—update it with labels, or

> 4\. Continue to use the manual CMR with no labels—update by hand.

# # List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You have probably noticed that when you process an order, the screen has dramatically changed from the previous version. The new screen was designed using List Manager.

This new screen will give you

- more pertinent information and
- easier access to vital other reports and areas of a patient’s chart you may wish to see.

![](inpatient-medications-version-5-release-notes/002.png)Please take the time to read over the explanation of the screen and the actions that you can now execute at the touch of a key. This type of preparation before attempting to use List Manager has been proven effective in saving time and effort.

  
Screen Title: The screen title changes according to what type of information List Manager is displaying (e.g., Patient Information, Non-Verified Order, Inpatient Order Entry, etc).

Allergy Indicator: This indicator will display only when allergy information has been entered for the patient.

Header area: The header area is a “fixed” (non-scrollable) area that displays information for a patient.

List area: (scrolling region): This is the section that will scroll (like the previous version) and display the information that an action can be taken on.

Message window: This section displays a plus (+) sign, minus (-) sign, if the list is longer than one screen, and informational text (i.e., Enter ?? for more actions). If you enter the plus sign at the action prompt, List Manager will “jump” forward to the next screen. If there is a minus sign displayed and you enter one at the action prompt, List Manager will “jump” back to the previous screen. The plus and minus signs are only valid actions if they are displayed in the message window.

Action area: The list of valid actions display in this area of the screen. If you enter a double question mark (??) at the “Select Action” prompt, you will receive a “hidden” list of additional actions that are available to you.

# Using List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> List Manager is a tool designed so that a list of items can be presented to the user for an action.

> For Inpatient Pharmacy, the List Manager does the following:

- gives capability to browse through a list of actions.
- gives capability to take action(s) against those items.
- gives capability to print MARs, labels, and profiles from within the Inpatient Order Entry option.
- gives the user the capability to select a different option than the option you are in.

> Actions are entered by typing the name(s), or synonym(s) at the “Select Action” prompt. In addition to the various actions that may be available specific to the option you are working in, List Manager provides generic actions applicable to any List Manager screen. You may enter a double question mark (??) at the “Select Action” prompt for a list of all actions available. The following is a list of generic List Manager actions with a brief description. The synonym for each action is shown in brackets following the action name. Entering the synonym is the quickest way to select an action.

> Action Description

> Next Screen \[+\] move to the next screen

> Previous Screen \[-\] move to the previous screen

> Up a Line \[UP\] move up one line

> Down a line \[DN\] move down one line

> First Screen \[FS\] move to the first screen

> Last Screen \[LS\] move to the last screen

> Go to Page \[GO\] move to any selected page in the list

> Re Display Screen \[RD\] redisplay the current screen

> Print Screen \[PS\] prints the header and the portion of

the list currently displayed

> Print List \[PL\] prints the list of entries currently

> displayed

> Search List \[SL\] finds selected text in list of entries

> Quit \[Q\] exits the screen

> Auto Display (On/Off) \[ADPL\] toggles the menu of actions to be

> displayed/not displayed automatically

> Shift View to Right \[\>\] Shifts the view on the screen to the

> right

> Shift View to Left \[\<\] Shifts the view on the screen to the

> left

The following is a list of Inpatient Medications specific hidden actions with a brief description. The synonym for each action is shown in brackets following the action name. Entering the synonym is the quickest way to select an action.

> MAR Menu \[MAR\] takes you to the MAR Menu

> 24 Hour MAR \[24\] will show the 24 Hour MAR

> 7 Day MAR \[7\] will show the 7 Day MAR

> 14 Day MAR \[14\] will show the 14 Day MAR

> Medications Due will show the Worksheet

> Worksheet \[MD\]

> Label Print/Reprint \[LBL\] Takes you to the Label Print/Reprint

> Menu

> Align Labels (Unit Dose) \[ALUD\] Allows you to align the MAR label

> stock on a printer

> Label Print/Reprint \[LPUD\] Allows you to print or reprint an MAR

> label

> Align Labels (IV) \[ALIV\] Allows you to align the IV bag label

> stock on a printer

> Individual Labels (IV) \[ILIV\] Allows you to print or reprint an IV

> bag label

> Scheduled Labels (IV) \[SLIV\] Allows you to print the scheduled IV

> bag label

> Reprint Scheduled Labels (IV) Allows you to reprint scheduled IV bag

> \[RSIV\] labels

> Other Pharmacy Options \[OTH\] Takes you to more pharmacy options

> Pick List Menu \[PIC\] Takes you to the Pick List Menu

> Enter Units Dispensed \[EN\] Allows you to enter the units actually

> Dispensed for a Unit Dose order

> Extra Units Dispensed \[EX\] Allows you to enter extra units

> dispensed for a Unit Dose order

> Pick List \[PL\]

> Report Returns \[RRS\] Allows you to enter units returned for

> a Unit Dose order

> Reprint Pick List \[RPL\] Allows you to reprint a pick list

> Send Pick list to ATC \[SND\] Allows you to send a pick list to the

> ATC

> Update Pick List \[UP\] Allows you to update a pick list

> Returns/Destroyed Menu \[RET\] Takes you to the Returns/Destroyed

> options

> Report Returns (UD) \[RR\] Allows you to enter units returned for

> a Unit Dose order

> Returns/Destroyed Entry (IV) Allows you to enter units returned or

> \[RD\] destroyed for an order

> Patient Profiles \[PRO\] Takes you to the Patient Profile menu

> Inpatient Medications Profile Allows you to generate an Inpatient

> \[IP\] Profile for a patient

> IV Medications Profile \[IV\] Allows you to generate an IV Profile

> for a patient

> Unit Dose Medications Profile Allows you to generate a Unit Dose

> \[UD\] profile for a patient

> Outpatient Prescriptions \[OP\] Allows you to generate an Outpatient

> profile for a patient

> Action Profile \#1 \[AP1\] Allows you to generate an Action

> Profile \#1

> Action Profile \#2 \[AP2\] Allows you to generate an Action

> Profile \#2

> Patient Profile (Extended) \[EX\] Allows you to generate an Extended

> Patient Profile

The following actions are available when selecting an order for processing.

> Speed Discontinue \[DC\] will be able to speed discontinue

> Speed Renew \[RN\] will be able to speed renew

> Speed Finish \[SF\] will be able to speed finish

> Speed Verify \[SV\] will be able to speed verify

The following action is available when selecting an order that is a Non-Verified Pending order.

> Jump to a Patient \[JP\] will take you to another patient

# Order Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Order Entry* options allow you to create new orders for a patient as well as take various actions on existing Unit dose or IV orders.

Within the Inpatient Medications package there are three different paths that you can take to enter a new order or take action on an existing order. They are Non-Verified/Pending Orders, Inpatient Order Entry, and Order Entry (UD). Each of these paths differ by the prompts that you will be asked. Once you have reached the point of entering a new order or selecting an existing order, the process becomes the same for each path. Below is a summary of the different paths.

## Non-Verified/Pending Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows easy identification and processing of non-verified and/or pending orders. This option will also show pending and pending renewal orders, which are orders from OE/RR that have not been finished by Pharmacy Service. Please refer either the Inpatient Medications Nurses’ or Pharmacists Manuals for more information.

You can choose to look at non-verified and/or pending orders for a ward group (G), ward (W), or single patient (P). If Ward or Ward Groups is selected, patients will be listed by wards and then by teams.

If no profile is chosen, the orders for the patient selected will be displayed for verification or completion by login date with the earliest date showing first. If a profile is chosen, the orders will be selected from this list for processing (any order may be selected).

## Inpatient Order Entry/Order Entry (UD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Order Entry allows the pharmacist to create, edit, renew, hold, and discontinue Unit Dose and IV orders, as well as put existing IV orders on call for any patient, while remaining in the Unit Dose module.

When you access the Inpatient Order Entry option from the Unit Dose module for the first time within a session, you are first asked to select the IV room in which you wish to enter orders. You are then given the label and report devices defined for the IV room you choose. If no devices have been defined, you will be given the opportunity to choose them. If you exit this option and re-enter within the same session, you are shown your current label and report devices.

Order Entry (UD) functions almost identically to Inpatient Order Entry but does not include IV orders on the profile and only Unit Dose orders may be entered or processed.

  
Name of the Patient

The Brief Patient Information List is then displayed for the selected patient. This list contains the patient’s demographic data, Allergy/Adverse Reaction data, and Pharmacy Narratives.

- Patient Demographics

The patient’s demographic information is displayed in the heading of the List Manager display, and includes information about the patient’s current admission.

![](inpatient-medications-version-5-release-notes/003.png)

- Allergy/ADR Information

This includes non-verified and verified Allergy/ADR information as defined in the Adverse Reaction Tracking (ART) package. The allergy data is sorted by type (DRUG, DRUG/FOOD, DRUG/FOOD/OTHER, DRUG/OTHER, FOOD, FOOD/OTHER, OTHER). If no data is found for a category, the heading for that category is not displayed.

- Pharmacy Narratives

A new INPATIENT NARRATIVE field has been added in version 5.0. This field is similar to the OUTPATIENT NARRATIVE, and may be used by inpatient pharmacy staff to display information specific to the current admission for the patient. Data in this field is automatically deleted when the patient is admitted.

Allergies - Verified: NEOSPORIN, PENICILLIN

Non-Verified: DEMEROL HYDROCHLORIDE

Adverse Reactions:

Inpatient Narrative: This is a test of the Inpatient Narrative

Outpatient Narrative:

- Other Actions that can be taken on this profile.

Enter ?? for more actions

PU Patient Record Update NO New Order Entry IN Intervention Menu

DA Detailed ADR List VP View Profile

Below are the primary actions available from the Brief Patient Information list:

- PU Patient Record Update

Allows editing of the Inpatient Narrative and the Patient’s Default Stop Date for Unit Dose Order entry.

- DA Detailed Allergy Display

Displays a detailed listing of the selected item from the patient’s allergy/ADR list. Entry to the Edit Allergy/ADR Data option is provided with this list also.

- EA Edit Allergy/ADR Data

> Provides access to the Adverse Reaction Tracking (ART) package to allow entry and/or edit of allergy adverse reaction data for the patient. See the ART package documentation for more information on allergy/ADR processing.

- SA Select Allergy

> Allows selection of a specific allergy for which detailed is to be displayed.

- NO New Order Entry

Allows new Unit Dose and IV orders to be entered for the patient.

- VP View Profile

Allows selection of a Long, Short, or NO profile for the patient. The profile displayed in the *Inpatient Order Entry* and *Non-Verified/Pending Orders* options will include IV and Unit Dose orders.

- IN Intervention Menu

Allows entry of new interventions or edit, delete, view, or printing of an existing intervention.

- New: This option is used to enter an entry into the APSP INTERVENTION file.
- Edit: This option is used to edit an already existing entry in the Intervention file.
- Delete: This option is used to delete an intervention from the APSP INTERVENTION file. You may only delete an intervention that was entered on the same day.
- View: This option is used to display Pharmacy Interventions in a captioned format.
- Print: This option is used to obtain a captioned printout of Pharmacy Interventions for a certain date range. It will print out on normal width paper and can be queued to print at a later time.

## ## Patient Profile List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Profile List contains all orders for a selected profile type.

- A long profile lists Unit Dose and IV orders for the current admission including discontinued and expired orders, (IV orders are not included in the Order Entry (Unit Dose) option).
- A short profile lists the active, non-verified, or pending orders.

The orders on the profile are sorted first by the status of ACTIVE, NON-VERIFIED, PENDING, PENDING RENEWALS, and then alphabetically by SCHEDULE TYPE. Pending orders with a priority of STAT are listed first and are displayed in a bold and blinking text for easy identification. After SCHEDULE TYPE, orders are sorted alphabetically by DRUG (the drug name listed on the profile), and then in descending order by START DATE

> Note: The START DATE and DRUG sort may be reversed using the

> INPATIENT ORDER SORT field in the INPATIENT USER PARAMETERS file.

If a Unit Dose order not yet verified by pharmacy has been verified by nursing, it will be listed under the ACTIVE heading with a -\> next to its number identifying it as non-verified. Orders may be selected by choosing the Select Order action, or directly from the profile using the order number displayed to the left of the drug. Multiple orders may be chosen by entering the numbers of each order to be included separated by commas (e.g., 1,2,3), or a range of numbers using the dash (e.g., 1-3).

\+ Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Next Screen//

*Below are the primary actions available in the Patient Profile list:*

- PI Patient Information

Displays the Brief Patient Information list described in section.

- PU Patient Record Update

Allows edit of the Inpatient Narrative and the Patient’s Default Stop Date for Unit Dose Order entry.

-   
  SO Select Order (See Unit Dose Order View List Below)

Allows selection of the orders to be processed. Multiple orders may be chosen by entering the numbers of each order to be included separated by commas (e.g., 1,2,3), or a range of numbers using the dash (e.g., 1-3).

- NO New Order Entry

Allows new Unit Dose and IV orders to be entered for the patient.

## Unit Dose Order View List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the patient is selected and length of profile is chosen, order entry follows three basic steps:

> 1\. Take action on a previously entered order by selecting it from the profile *or* create a new order by entering the drug, schedule, administration times, etc., pertaining to the type of order.

> 2\. If Auto-Verify is disabled, the order must be verified before it is included on the Pick List, MAR, etc. For more information on the Auto- Verify function see the Edit User Parameters section of the Pharmacy Supervisor Manual.

> 3\. If orders have been verified, you must provide information for the *Pre- Exchange Units: Report*. After verifying an order, you are prompted to identify the number of units required before the next cart exchange (pre-exchange units). Information will be requested for each order that has been verified. When you finish entering new orders, a *Pre- Exchange Report* will be printed. The report lists patient name, ward location, room and bed, orderable item, dispense drug, and pre- exchange needs for each order. You can immediately print this report to the screen or queue it to print on a printer. We advise that you print a copy on the printer. Once you exit this option, you cannot reprint this report.

Patient Demographics/Allergy/ADR Data

Detailed ADR List Mar 21, 1997 14:24:55 Page: 1 of 1

IOWA,LUKE Ward: NHCU-33 \<A\>

PID: 123-45-6789 Room-Bed: NORTH Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 06/06/25 (71) Wt(kg): 77.59 (07/16/96)

Sex: MALE Admitted: 02/17/97

Dx: COPD Last transferred: \*\*\*\*\*\*\*\*

This includes a condensed listing of the patient’s demographic and location information. If the patient has Allergy/ADR data defined, an “\<A\>“ is displayed to the right of the ward location to alert the user of the existence of this information (Note: This data may be displayed using the *Brief Patient Information* option from this list’s hidden menu). The status and type of order are displayed in the top left corner of the heading, and will include the priority (if defined) for pending orders.

## Unit Dose Order View List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*(1)Orderable Item: ACETAMINOPHEN TAB

Instructions: 325mg

(2)Dosage Ordered: 325mg (3) Start: 02/26/97 09:30

\*(4) Med Route: ORAL (5) Stop: 03/02/97 06:00

\(6\) Schedule Type: CONTINUOUS (7) Self Med: NO

\*(8) Schedule: BID

\(9\) Admin Times: 0600-2000

\*(10) Provider: AGUSTA,DON

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

------------------------------------------------------------------------------

ACETAMINOPHEN 325MG TAB UD 1

Entry By: AGUSTA,DON Entry Date: 02/26/97 09:30

The Unit Dose Order View List displays detailed order information and allows actions to be taken on the selected Unit Dose Order. Fields that may be edited will be identified by a number displayed to the left of the field name. This number is used when selecting fields to be edited. Fields marked with an “\*” next to its number will cause this order to be discontinued and a new one created if it is changed. If a pending order is selected, the system will determine any default values for fields not entered through OE/RR and display them along with the data entered by the clinician.

Actions

\+ Enter ?? for more actions

DC Discontinue ED Edit VF (Verify)

HD Hold RN Renew AL Activity Logs

Select Item(s): Next Screen//

This list contains each field included in the Unit Dose order.

## Inpatient Medication IV Order View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACTIVE IV Jun 04, 1996 09:31:42 Page: 1 of 2

ARKANSAS,MARY Ward: 1 EAST

PID: 123-45-6789 Room-Bed: 244-B Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 09/03/58 (36) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1) Additives: Order number: 11 Type: PIGGYBACK

AMPICILLIN 1 GM

\(2\) Solutions:

0.9% NaCl 50 ML

IV Room: BIRMINGHAM ISC

\(3\) Infusion Rate: INFUSE OVER 15 MIN. \*(4) Start: 06/04/96 12:00

\*(5) Med Route: IV \*(6) Stop: 06/11/96 13:00

\*(7) Schedule: Q6H Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 06-12-18-24 Quantity: 0

\*(9) Provider: INPATIENT-MEDS,PROVIDER Cum. Doses:

\*(10)Orderable Item: AMPICILLIN INJ

Instructions:

\(11\) Other Print:

Provider Comments:

\(12\) Remarks :

Entry By: TAMPA,ANNETTE Entry Date: 06/04/96 09:24

## ## ## IV Fluid Order View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACTIVE IV Jun 04, 1996 09:30:47 Page: 1 of 1

ARKANSAS,MARY Ward: 1 EAST

PID: 123-45-6789 Room-Bed: 244-B Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 09/03/58 (36) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1) Additives: Order number: 12 Type: ADMIXTURE

MULTIVITAMINS 5 ML 1

POTASSIUM CHLORIDE 20 MEQ

\*(2) Solutions:

D5-0.45% NaCl 1000 ML

IV Room: BIRMINGHAM ISC

\*(3) Infusion Rate: 125 ml/hr \*(4) Start: 06/04/96 10:00

\*(5) Med Route: IV \*(6) Stop: 06/18/96 13:00

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: INPATIENT-MEDS,PROVIDER Cum. Doses:

\(10\) Other Print:

Provider Comments:

\(11\) Remarks :

Entry By: INPATIENT-MEDS,PHA Entry Date: 06/04/96 13:54

\+ Enter ?? for more actions

DC Discontinue ED Edit OC On Call

HO Hold RN Renew AL Activity Logs

Select Item(s): Next Screen// <u>QUIT</u> QUIT

> **NOTE:** Actions enclosed in parenthesis are not available. Fields that may be edited will be identified by a number displayed to the left of the field name. This number is used when selecting fields to be edited. Fields marked with an “\*” next to its number will cause this order to be discontinued and a new one created if it is changed.

## New Order Entry (Unit Dose)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Unit Dose order entry you must respond at the “Select DRUG:” prompt. Once you choose the drug, you can follow the same procedure as Unit Dose order entry, as defined in your user parameters.

- DRUG

Pharmacists select Unit Dose medications directly from the DRUG file (#50). The Orderable Item for the selected drug will automatically be added to the order, and all dispense drugs entered for the order must be linked to that Orderable Item. If the Orderable Item is edited, data in the DOSAGE ORDERED and DISPENSE DRUG fields will be deleted. If multiple dispense drugs are needed in an order, they may be entered by selecting the DISPENSE DRUG field (#12) from the edit list before accepting the new order (see either the Inpatient Medications Nurses’ or Pharmacists Manual for more information on this process). After each dispense drug is selected, it will be checked against the patient’s current medications for duplicate drug or class orders, and drug-drug/drug-allergy interactions (see either the Inpatient Medications Nurses’ or Pharmacists Manual for more information on this process).

> **NOTE:** For IV order entry, you must bypass the “Select DRUG:” prompt in the Inpatient Order Entry option (by pressing the Return key) and then choose the IV type at the “Select IV TYPE:” prompt.

- DOSAGE ORDERED

To allow pharmacy greater control over the order display shown for Unit Dose orders on profiles, labels, MARs, etc., the DOSAGE ORDERED field is no longer required. If no DOSAGE ORDERED is defined for an order, the order will be displayed as:

> DISPENSE DRUG NAME

> Give: UNITS/DOSE MEDICATION ROUTE SCHEDULE

If DOSAGE ORDERED is defined for the order, it will be displayed as:

> ORDERABLE ITEM NAME DOSE FORM

> Give: DOSAGE ORDERED MEDICATION ROUTE SCHEDULE

> **NOTE:** If an order contains multiple DISPENSE DRUG, DOSAGE ORDERED will be required, and should contain the total dosage of the medication to be administered.

- UNITS PER DOSE

This is the number of units (tablets, capsules, etc.) of the dispense drug selected to be given when the order is administered. If no data is entered, the UNITS PER DOSE is assumed to be 1.

- MED ROUTE

This is the route of administration to be used for the order. If a default Medication Route is identified for the selected Orderable Item, it will be used as the default for the order.

- SCHEDULE TYPE

This defines the type of schedule to be used when administering the order. If the schedule type entered is one time, the order’s start and stop dates must be the same. When a new order is entered or an order entered through CPRS is finished by pharmacy the default Schedule Type is determined as described below:

If a schedule type is defined for the Orderable Item selected, that schedule type is used for the order.

If no schedule type has been found and if no schedule is defined, schedule type is CONTINUOUS.

If no schedule type has been found and the schedule contains PRN, the schedule type is PRN.

If no schedule type has been found and the schedule entered is found in the ADMINISTRATION SCHEDULE file (#51.1), and a schedule type is defined for it, that schedule type is used for the order.

If no schedule type has been found and the schedule is “NOW”, “STAT”, “ONCE”, or “ONE-TIME” the schedule type is ONCE.

If the schedule type determined above is DAY OF WEEK the schedule type is set to CONTINUOUS.

If no schedule type was determined above, the schedule type is CONTINUOUS

- SCHEDULE

This defines the frequency the order is to be administered. Schedules may be selected from the ADMINISTRATION SCHEDULE file (#51.1) or non-standard schedules may be used. A non-standard schedule is one that does not have a consistent interval between administrations. Unit Dose recognizes schedules in the following formats:

QxH - Hourly schedules where x is the number of hours between administrations

QxD - Daily schedules where x is the number of days between administrations

QxM - Monthly schedules where x is the number of months between administrations

If a schedule is defined for the Orderable Item selected when entering a new order, that schedule is displayed as the default for the order.

- ADMINISTRATION TIMES

This defines the time(s) of day the order is to be given. If the schedule for the order contains “PRN” any administration times for the order will be ignored. In new order entry the default administration times are determined as described below:

If administration times are defined for the Orderable Item selected, they will be shown as the default for the order.

If administration times are defined in the ADMINISTRATION SCHEDULE file (#51.1) for the patient’s ward and the order’s schedule, they will be shown as the default for the order.

If administration times are defined for the Schedule, they will be shown as the default for the order.

- PROVIDER

This identifies the provider who authorized the order. Only users identified as providers who are authorized to write medication orders may be selected.

- SELF MED

Identifies the order as to be given for administration by the patient. This prompt is only shown if the ‘SELF MED’ IN ORDER ENTRY field of the INPATIENT WARD PARAMETERS file (#59.6) is set to on.

- NATURE OF ORDER

This specifies how the order originated. An order can be specified as written on the chart, telephoned, or verbal. This data is stored and displayed through OE/RR.

## New Order Entry (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- TYPE

This describes the type of IV order to be placed. Orders identified as admixtures, chemotherapy admixtures, chemotherapy syringes (continuous) and hyperals are treated as continuous orders. Other types are assumed to be administered intermittently based on the order’s schedule.

- ADDITIVE

There can be any number of additives for an order, including zero. You can enter an additive or additive synonym. If your IRM Chief/Site Manager or Application Coordinator has defined it in the IV Additives file, you may enter a quick code for an additive. The quick code allows you to pre-define certain fields, thus speeding up the order entry process.

- STRENGTH

The strength of the additive specified to be included in the order. Strength must be entered for each additive.

- SOLUTION

There can be any number of solutions in an order, depending on the type. It is even possible to require zero solutions when an additive is pre-mixed with a solution. If no solutions are chosen, the computer will give you a warning message, in case it is an oversight, and give you an opportunity to add one. You may enter an IV solution or IV solution synonym.

- VOLUME

This is the amount of the solution to be included in the order. The total volume of

the order is used along with Infusion Rate to determine projected administration times for the order.

- INFUSION RATE

The infusion rate is the rate at which the IV is to be administered. This value, in conjunction with the total volume of the hyperal or the admixture type, is used to determine the time covered by one bag; hence the system can predict the bags needed during a specified time of coverage. This field is free text for piggybacks. For admixtures you must enter a number that will represent the infusion rate. You can also specify the \# of bags per day that will be needed. Example: 125 = 125 ml/hr (IV system will calculate bags needed per day), 125@2 = 125 ml/hr with 2 labels per day, Titrate@1 = Titrate with 1 label per day. The format of this field is either a number only or \<free text \> @ \<Number of labels per day \> (e.g., Titrate @ 1).

- MED ROUTE

This is the route of administration for this medication (e.g., IV, SQ). If a corresponding abbreviation is found for this route in the MEDICATION ROUTES file, this module will print that abbreviation on its reports.

-   
  SCHEDULE

This defines the frequency the order is to be administered. Schedules may be selected from the ADMINISTRATION SCHEDULE file (#51.1) or non-standard schedules may be used. A non-standard schedule is one that does not have a consistent interval between administrations. Inpatient Medications recognizes schedules in the following formats:

QxH - Hourly schedules where x is the number of hours between administrations

QxD - Daily schedules where x is the number of days between administrations

QxM - Monthly schedules where x is the number of months between administrations

If a schedule is defined for the Orderable Item selected when entering a new order, that schedule is displayed as the default for the order.

- ADMINISTRATION TIMES

This defines the time(s) of day the order is to be given. If the schedule for the order contains “PRN” any administration times for the order will be ignored. In new order entry the default administration times are determined as described below:

If administration times are defined for the Orderable Item selected, they will be shown as the default for the order.

If administration times are defined in the ADMINISTRATION SCHEDULE file (#51.1) for the patient’s ward and the order’s schedule, they will be shown as the default for the order.

If administration times are defined for the Schedule, they will be shown as the default for the order.

- REMARKS

This contains additional information about the order that is not to be included on the IV or MAR labels.

- OTHER PRINT

This data is included on the IV and MAR labels.

- START DATE

The default start date/time for the order is calculated based on the DEFAULT START DATE CALCULATION field (#.05) of the INPATIENT WARD PARAMETERS file (#59.6). This allows the site to use the next or closest administration or delivery time, or the order’s login date/time as the default start date/time. For continuous IV orders the default start date/time is based on the delivery times for the IV room specified. For intermittent IV orders this default is based on the order’s administration times.

-   
  STOP DATE

The default stop date/time for the order is determined by the \<IV TYPE\> GOOD FOR HOW MANY DAYS fields in the IV ROOM file (#59.5), where \<IV TYPE\> is piggyback, admixture, syringe, chemotherapy, etc. If the NUMBER OF DAYS FOR IV ORDER field (#3) of the IV ADDITIVES file (#52.6) is less then it will be used instead.

- PROVIDER

This identifies the provider who authorized the order. Only users identified as providers who are authorized to write medication orders may be selected.

- NATURE OF ORDER

This specifies how the order originated. An order can be specified as written on the chart, telephoned, or verbal. This data is stored and displayed through OE/RR.

- ON CALL

Only active orders may be placed on call. Orders placed on call will continue to show under the active heading of the profile until it is taken off call. An entry is placed in the order’s activity log recording the person who took the action and when it was taken.

## Other Order Actions - Edit, Hold, Discontinue, Renew, On Call

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit

This allows modification of any field shown on the order view that is preceded by a number in parenthesis (\*).

> Asterisk: If a field marked with an asterisk is changed, the original order will be discontinued and a new order containing the edited data will be created.

> The Stop Date/Time of the original order will be changed to the date/time the new edit order is accepted. The old and new orders are linked and may be viewed using the History Log function. When the screen is refreshed, the field(s) that were changed will now be shown in blinking reverse video and “This change will cause a new order to be created” will be displayed in the message window.

> \*(10) Provider: TOPEKA,MARK

> \(11\) Special Instructions:

> \(12\) Dispense Drug U/D Inactive Date

> ---------------------------------------------------------------------------

> DIGOXIN 0.125MG U/D 1

> Entry By: INPATIENT,NURSE Entry Date: 02/05/98 11:21

> \+ This change will cause a new order to be created.

> ED Edit AC ACCEPT

> Orderable Item or Dosage Ordered fields: If these fields are edited, the dispense drug data will not be transferred to the new order. If the Orderable Item is changed, data in the Dosage Ordered and Dispense Drug field will not be transferred. New Start Date/Time, Stop Date/Time, Login Date/Time, and Entry Code will be determined for the new order. Changes to other fields (those without the asterisk) will be recorded in the order’s activity log.

Renew

Only active orders or those which have been expired less than 24 hours may be renewed. The default Start Date/Time for a renewal order is determined as follows:

> Default Start Date Calculation = NOW

> The default start date/time for the renewal order will be the order’s Login Date/time.

> Default Start Date Calculation = USE NEXT ADMIN TIME

> The original order’s Start Date/Time, the new order’s Login Date/Time, Schedule, and Administration Times are used to find the next date/time the order is to be administered after the new order’s Login Date/Time. If the schedule contains “PRN” any administration times for the order are ignored.

> Default Start Date Calculation = USE CLOSEST ADMIN TIME

> The original order’s Start Date/Time, the new order’s Login Date/Time, Schedule, and Administration Times are used to find the closest date/time the order is to be administered after the new order’s Login Date/Time. If the schedule contains “PRN” any administration times for the order are ignored.

After the new (renewal) order is accepted, the Start Date/Time for the new order becomes the Stop Date/Time for the original (renewed) order. The original order’s status is changed to RENEWED. The renewal and renewed orders are linked and may be viewed using the History Log function. Once an order has been renewed it may not be renewed or edited.

Discontinue

When an order is discontinued the order’s Stop Date/Time is changed to the date/time the action is taken. Pending and Non-verified orders are deleted when discontinued and will no longer appear on the patient’s profile. An entry is placed in the order’s Activity Log recording who discontinued the order and when the action was taken.

Hold

Only active orders may be placed on hold. Orders placed on hold will continue to show under the ACTIVE heading on the profiles until it is removed from hold. An entry is placed in the order’s Activity Log recording the person who placed/removed the order from hold and when the action was taken.

Activity Log

This submenu allows viewing of a long or short activity log, dispense log, or a History Log of the order. A short activity log only shows actions taken on orders and does not include field changes. If a history log is selected, it will find the first order linked to the order where the history log was invoked from, then shows an order view of each order associated with it in the order which they were created.

  
Verify

Orders must be verified before they can become active and are included on the pick list, MAR, etc. If \*AUTO-VERIFY is enabled for the pharmacist, new orders immediately become active after entered or finished (pending orders entered through OE/RR). Orders verified by nursing prior to pharmacist verification are displayed on the profile under the active header marked with an -\> next to the order number. When verify is selected, the user must enter any missing data and correct any invalid data before the verification is accepted.

\*AUTO-VERIFY is controlled by the ALLOW AUTO-VERIFY FOR USER field in the INPATIENT USER PARAMETERS file (#53.45).

On Call

Only active orders may be placed on call. Orders placed on call will continue to show under the active heading of the profile until it is taken off call. An entry is placed in the order’s activity log recording the person who took the action and when it was taken.