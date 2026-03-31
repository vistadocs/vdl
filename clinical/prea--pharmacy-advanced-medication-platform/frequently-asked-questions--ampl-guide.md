---
title: AMPL Frequently Asked Questions Guide
doc_type: FAQ
doc_label: Frequently Asked Questions
doc_layer: anchor
doc_subject: AMPL  Guide
app_code: PREA
app_name: "Pharmacy: Advanced Medication Platform"
section: CLI
app_status: active
pkg_ns: PREA
patch_ver: 1.14
patch_id: PREA*1.14
group_key: "PREA:PREA:1.14"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - ampl
  - questions
  - frequently
  - asked
  - guide
  - figure
  - class
  - anchor
  - filter
page_count: 0
word_count: 9550
section_count: 45
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA/PREA_1_14_AMPL_GUI_FAQ.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA/PREA_1_14_AMPL_GUI_FAQ.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=237"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Advanced Medication Platform (AMPL)

  Graphic User Interface (GUI)

  Frequently Asked Questions (FAQ)
---

![](ampl-frequently-asked-questions-guide/001.png)

January 2026

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date    | Revision | Description              | Author    |
|---------|----------|--------------------------|-----------|
| 01/2026 | 2.0      | Updates for Version 1.13 | AMPL Team |
| 07/2023 | 1.0      | Baseline Document        | AMPL Team |

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.

Artifact Rationale

The FAQ provides answers to frequently asked questions that may be needed by the AMPL GUI users and support teams to answer questions as they arise during the development and continuation of AMPL GUI. The FAQ is an optional resource that serves as an addition to required documentation support for AMPL GUI users and testers.

Table of Contents

Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Logging On](#logging-on)
  - [How do I log onto AMPL GUI?](#how-do-i-log-onto-ampl-gui)
  - [How do I know my three-digit station number?](#how-do-i-know-my-three-digit-station-number)
- [Pending Orders Manager (POM)](#pending-orders-manager-pom)
  - [What is the Pending Orders Manager?](#what-is-the-pending-orders-manager)
  - [Why are patients not showing under the POM?](#why-are-patients-not-showing-under-the-pom)
  - [What does the Select Ordering Institution button do?](#what-does-the-select-ordering-institution-button-do)
  - [What are those numbers I see in the blue bubbles on the tabs?](#what-are-those-numbers-i-see-in-the-blue-bubbles-on-the-tabs)
  - [What are those green arrows in the column headers?](#what-are-those-green-arrows-in-the-column-headers)
  - [What is the black funnel symbol in the column headers?](#what-is-the-black-funnel-symbol-in-the-column-headers)
  - [How can I get more information about the column headers?](#how-can-i-get-more-information-about-the-column-headers)
  - [Can I sort the patient by the age of the orders?](#can-i-sort-the-patient-by-the-age-of-the-orders)
  - [How can I take advantage of Clinic Sort Groups or Ward Groups that are set up in VistA?](#how-can-i-take-advantage-of-clinic-sort-groups-or-ward-groups-that-are-set-up-in-vista)
  - [For Inpatient Pending Orders, do ASAP orders show up under the STAT heading?](#for-inpatient-pending-orders-do-asap-orders-show-up-under-the-stat-heading)
  - [How can I get more details while still viewing the inpatient or clinic pending orders list?](#how-can-i-get-more-details-while-still-viewing-the-inpatient-or-clinic-pending-orders-list)
  - [Can I find flagged outpatient orders in AMPL?](#can-i-find-flagged-outpatient-orders-in-ampl)
  - [Why do some outpatient orders show at the top of the POM and don’t appear to have an institution?](#why-do-some-outpatient-orders-show-at-the-top-of-the-pom-and-dont-appear-to-have-an-institution)
  - [I have my patient list. Now what?](#i-have-my-patient-list-now-what)
  - [How do I change patients?](#how-do-i-change-patients)
  - [What is the “i” symbol next to Pending Orders Manager?](#what-is-the-i-symbol-next-to-pending-orders-manager)
  - [What is the “i” symbol next to the VistA Patient Lookup?](#what-is-the-i-symbol-next-to-the-vista-patient-lookup)
  - [What if I just want to go to an individual patient not on the Pending Orders Manager?](#what-if-i-just-want-to-go-to-an-individual-patient-not-on-the-pending-orders-manager)
  - [Can I save my preferences for next time?](#can-i-save-my-preferences-for-next-time)
- [Patient Cover Sheet](#patient-cover-sheet)
  - [How do I view more detailed patient demographics?](#how-do-i-view-more-detailed-patient-demographics)
  - [How do I get more detailed Allergy/ADR information?](#how-do-i-get-more-detailed-allergyadr-information)
  - [How can I address the No Allergy Assessment indicator for a patient?](#how-can-i-address-the-no-allergy-assessment-indicator-for-a-patient)
  - [What is CWAD and how do I find that information?](#what-is-cwad-and-how-do-i-find-that-information)
  - [How do I see recent additions or changes to the patient’s data from VistA or CPRS?](#how-do-i-see-recent-additions-or-changes-to-the-patients-data-from-vista-or-cprs)
  - [What is the number that I sometimes see next to the Tab name?](#what-is-the-number-that-i-sometimes-see-next-to-the-tab-name)
  - [Is there a way to see allergies or ADRs that were “Entered in Error?”](#is-there-a-way-to-see-allergies-or-adrs-that-were-entered-in-error)
  - [How do I know what facility entered the allergy/ADR?](#how-do-i-know-what-facility-entered-the-allergyadr)
  - [Okay, but how do I know what facility corresponds to that facility number?](#okay-but-how-do-i-know-what-facility-corresponds-to-that-facility-number)
  - [How do I find more information about column headers?](#how-do-i-find-more-information-about-column-headers)
  - [It would be nice to be able to graph vitals to see trends. Can I do that with AMPL?](#it-would-be-nice-to-be-able-to-graph-vitals-to-see-trends-can-i-do-that-with-ampl)
  - [How many progress note titles are displayed per page?](#how-many-progress-note-titles-are-displayed-per-page)
  - [How can I see a particular date range or an earlier date range than what is shown?](#how-can-i-see-a-particular-date-range-or-an-earlier-date-range-than-what-is-shown)
  - [There are a lot of progress notes. How do I sort and filter them?](#there-are-a-lot-of-progress-notes-how-do-i-sort-and-filter-them)
  - [How do I see the actual progress note?](#how-do-i-see-the-actual-progress-note)
  - [How do I see Remote meds?](#how-do-i-see-remote-meds)
  - [How do I see a more detailed view of the meds?](#how-do-i-see-a-more-detailed-view-of-the-meds)
  - [Okay, but how do I see an even MORE detailed view of the medication orders?](#okay-but-how-do-i-see-an-even-more-detailed-view-of-the-medication-orders)
  - [I see buttons at the bottom of that view. What are those for?](#i-see-buttons-at-the-bottom-of-that-view-what-are-those-for)
  - [For Inpatient and Clinical Med Orders, can I see PADE inventory amounts for the associated device?](#for-inpatient-and-clinical-med-orders-can-i-see-pade-inventory-amounts-for-the-associated-device)
  - [How can I identify flagged orders and obtain more details?](#how-can-i-identify-flagged-orders-and-obtain-more-details)
- [Filter and Sort (Queries)](#filter-and-sort-queries)
  - [What is the difference between National and User queries?](#what-is-the-difference-between-national-and-user-queries)
  - [Can I get more information on sort and filter functionality for Allergies and ADRs Labs, Consults, Progress Notes, Immunizations, Problem List, and Appointments tabs?](#can-i-get-more-information-on-sort-and-filter-functionality-for-allergies-and-adrs-labs-consults-progress-notes-immunizations-problem-list-and-appointments-tabs)
    - [Meds](#meds)
    - [Allergies](#allergies)
    - [Vitals](#vitals)
    - [Labs Tab](#labs-tab)
    - [Progress Notes](#progress-notes)
    - [Consults](#consults)
    - [Problem List](#problem-list)
    - [Immunizations](#immunizations)
    - [Appointments](#appointments)
    - [Pharmacogenomics](#pharmacogenomics)
- [Index](#index)
The Advanced Medication Platform (AMPL) Graphic User Interface (GUI) is a front-end application supporting the Department of Veterans Affairs (VA) pharmacists by fulfilling the need for medical knowledge during patient care. AMPL GUI provides a single point of access for pharmacists to do their work, such as reviewing patient records and processing pending orders.
Currently, AMPL GUI is a read-only application with an initial feature for writing data to VistA. AMPL has the ability to mark No Known Allergies (NKA) for a patient with no allergy assessment who is determined to have No Known Allergies. Writing and processing of orders as well as note writing, etc., is planned for a later phase.

# Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How do I log onto AMPL GUI?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter the AMPL URL into the address bar of your internet browser: <https://ampl.vaec.va.gov/login>
2.  After selecting Login, users are redirected to the VA SSOi page.
    1.  Click on the Sign In button with a VA Personal Identity Verification (PIV) Card graphic.
    2.  Select the appropriate certificate.
    3.  Type your Personal Identification Number (PIN) and click on the OK button

<span id="_Toc217371169" class="anchor"></span>Figure 1: VA Advanced Medication Platform Login Page

![](ampl-frequently-asked-questions-guide/002.png)

<span id="_Toc217371170" class="anchor"></span>Figure 2: VA Single Sign-On

![](ampl-frequently-asked-questions-guide/003.png)

## How do I know my three-digit station number?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc217371171" class="anchor"></span>Figure 3: Set VistA Context Three-Digit Station Number

![](ampl-frequently-asked-questions-guide/004.png)

The links below can be used to get a report of facilities and their station number:

Internet: <https://www.va.gov/find-locations>

Intranet: <https://vaww.va.gov/directory/guide/rpt_fac_list.cfm?isflash=1>

Your station number is also found in VistA. It is displayed when you enter your division. See the example below:

<span id="_Toc217371172" class="anchor"></span>Figure 4: Station Number in VistA

![](ampl-frequently-asked-questions-guide/005.png)

# Pending Orders Manager (POM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is the Pending Orders Manager?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pending Orders Manager (POM) is a dashboard intended to help pharmacists manage and process pending orders for their facilities.

## Why are patients not showing under the POM?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To display a list of patients under the Pending Orders Manager, select an outpatient site from the dropdown list next to Select Outpatient Site.

## What does the Select Ordering Institution button do?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Ordering Institution allows users to drill down to see orders for a specific CBOC or VAMC included under a station.

## What are those numbers I see in the blue bubbles on the tabs?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the category tabs on the POM, the number of orders within that tab are displayed in the blue bubble on the tab.

<span id="_Toc217371173" class="anchor"></span>Figure 5: POM Number of Orders

![](ampl-frequently-asked-questions-guide/006.png)

## What are those green arrows in the column headers?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To reveal if a column is sortable, click the column header. If it is sortable, the ![](ampl-frequently-asked-questions-guide/007.png)icon will display. Repeatedly clicking the sortable column will toggle between ascending, descending then back to default. If more than one column is sorted, a small number by the arrow ![](ampl-frequently-asked-questions-guide/008.png) indicates the order.

<span id="_Toc217371174" class="anchor"></span>Figure 6: Green Arrows Sorting Columns

![](ampl-frequently-asked-questions-guide/009.png)

## What is the black funnel symbol in the column headers?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The black funnel symbol indicates that column is included in the current query.

<span id="_Toc217371175" class="anchor"></span>Figure 7: Black Funnel Symbol

![](ampl-frequently-asked-questions-guide/010.png)

## How can I get more information about the column headers?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hovering your mouse over the column headers will reveal help text providing additional information. The hover functionality is available throughout AMPL, if you are not sure, hover!

<span id="_Toc217371176" class="anchor"></span>Figure 8: Hover Text

![](ampl-frequently-asked-questions-guide/011.png)

## Can I sort the patient by the age of the orders?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, pending orders are displayed oldest first.

Clicking on the desired date range in the Order Aging Summary, located near the upper right-hand section of your screen will display only the orders that fall within that date range.

<span id="_Toc217371177" class="anchor"></span>Figure 9: VA Ordering Aging Summary

![](ampl-frequently-asked-questions-guide/012.png)

Orders that display in any of the Pending Orders tabs may also be filtered using the Query Editor. Clicking on the blue arrow will expand the Query Editor.

<span id="_Toc217371178" class="anchor"></span>Figure 10: Current Query: All Records

![](ampl-frequently-asked-questions-guide/013.png)

## How can I take advantage of Clinic Sort Groups or Ward Groups that are set up in VistA?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Choose the Outpatient Orders by Location, Inpatient Orders, or Clinic Orders tab near the top of your screen. You will find Outpatient Clinic Sort Groups, Inpatient Ward Groups and Clinic Groups for Clinic Orders if you have them set up at your facility.

When you check a box for a clinic group or ward group, patients in the clinic or ward group with pending orders will be viewable below in the Select Patients to Process section (you may have to scroll down if there are a lot of groups).

There is also a Query Editor available in the Select Patients to Process section to further filter the list of patients. To filter the list, click on the down arrow to access the Query Editor (shown below).

> **NOTE:** Currently, AMPL is read-only. The ability to process orders will be added in a later version.

<span id="_Toc217371179" class="anchor"></span>Figure 11: Select Patient(s) to Process

![](ampl-frequently-asked-questions-guide/014.png)

## For Inpatient Pending Orders, do ASAP orders show up under the STAT heading?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes. The red symbol displays for ASAP and STAT orders, so they are easy to locate.

<span id="_Toc217371180" class="anchor"></span>Figure 12: Ward List Priority Indicator

![](ampl-frequently-asked-questions-guide/015.png)

<span id="_Toc217371181" class="anchor"></span>Figure 13: Patient List Priority Indicator

![](ampl-frequently-asked-questions-guide/016.png)

## How can I get more details while still viewing the inpatient or clinic pending orders list?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A toggle button was added to switch between a summary view and a detailed view of a patient’s pending inpatient or clinic orders. When the toggle is turned off, the list displays a summary for all pending inpatient or clinic orders by patient. When the toggle is turned on, it shows individual inpatient or clinic orders by date, pharmacy orderable item, login date/time, and wait time for each order.

<span id="_Toc217371182" class="anchor"></span>Figure 14: Inpatient or Clinic Orders - Select Patient(s) to Process List - Details

![](ampl-frequently-asked-questions-guide/017.png)

## Can I find flagged outpatient orders in AMPL?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes. The red flag symbol displays next to Flagged orders, so they are easy to locate.

The Flag Date and Unflagged columns are available in the Pending Orders Manager, Outpatient Orders tables. The Flag Date column will display the flagged date/time. If an order was flagged, the Unflagged column will display N for Not Unflagged, or it will contain the date/time that the order was unflagged. Hovering over a date/time value in these columns will display more information. The Query Editor provides options to filter by Flagged By, Flag Reason, Flag Date, Unflagged By, Unflagged Reason, and Unflagged Date.

<span id="_Toc217371183" class="anchor"></span>Figure 15: Flagged Outpatient Pending Orders

![](ampl-frequently-asked-questions-guide/018.png)

To retrieve a list of flagged orders from the POM, set the filters for Flagged Date greater than \<DATE\>, and Unflagged is “false.” See figure below:

<span id="_Toc217371184" class="anchor"></span>Figure 16: Filter to Find Flagged Orders

![](ampl-frequently-asked-questions-guide/019.png)

## Why do some outpatient orders show at the top of the POM and don’t appear to have an institution?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the order has not been associated with a valid outpatient site, the order will be highlighted in peach and a message “\*\*Process under correct Outpatient Site” will display above the list. These orders will always display first and will not be included in any of the sort options. NOTE: Once these orders are processed under the correct Outpatient division in VistA, they will be cleared. To find the correct division, check Appointments or Progress Notes for the division where the order was entered.

<span id="_Toc217371185" class="anchor"></span>Figure 17: Orders with Invalid Outpatient Sites

![](ampl-frequently-asked-questions-guide/020.png)

## I have my patient list. Now what?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One or more patients may be selected from the list for processing using the Process Selected or Process All buttons. If multiple patients are selected, the first one will open to the Patient Cover Sheet and the rest will be added to the patient queue and their names will display at the bottom of the screen and using the patient queue button at the top of the screen.

<span id="_Toc217371186" class="anchor"></span>Figure 18: Patient Queue or Multiple Patients

![](ampl-frequently-asked-questions-guide/021.png)

## How do I change patients?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once patient(s) are selected, you will be taken to the Patient Cover Sheet. If you want to go back into the Pending Orders Manager, you can select Pending Orders from the upper right corner of your screen. If you selected multiple patients and want to change patients, click on the Patient Queue button.

<span id="_Toc217371187" class="anchor"></span>Figure 19: POM Button Toggle to Cover Sheet and Retained in Patient Queue

![](ampl-frequently-asked-questions-guide/022.png)

<span id="_Toc217371188" class="anchor"></span>Figure 20: Patient Cover Sheet with Patient Queue List

![](ampl-frequently-asked-questions-guide/023.png)

## What is the “i” symbol next to Pending Orders Manager?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ![](ampl-frequently-asked-questions-guide/024.png) icon next to Pending Orders Manager text gives informational text regarding POM Navigational help. Click on it to view the help.

<span id="_Toc217371189" class="anchor"></span>Figure 21: Pending Orders "i" Icon

![](ampl-frequently-asked-questions-guide/025.png)

## What is the “i” symbol next to the VistA Patient Lookup?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you click on the ![](ampl-frequently-asked-questions-guide/026.png) icon next to VistA Patient Lookup, it will display help text on different ways to search for the patient you need.

<span id="_Toc217371190" class="anchor"></span>Figure 22: VistA Patient Lookup Help Text

![](ampl-frequently-asked-questions-guide/027.png)

## What if I just want to go to an individual patient not on the Pending Orders Manager?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can locate and select individual patients from the VISTA Patient Lookup located in the upper left corner of your screen.

<span id="_Toc217371191" class="anchor"></span>Figure 23: Pending Order Manager VistA Patient Lookup

![](ampl-frequently-asked-questions-guide/028.png)

## Can I save my preferences for next time?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes. Preferences that you set will remain until you change them.

Click on the Star icons to save your preferences.

<span id="_Toc217371192" class="anchor"></span>Figure 24: POM with No Selected Preferences

![](ampl-frequently-asked-questions-guide/029.png)

If you want the Outpatient Orders by Location tab to automatically display on the POM when you open AMPL, click on the Star icon on that tab. The star will be filled in, indicating the personal preference is saved.

<span id="_Toc217371193" class="anchor"></span>Figure 25: POM with Selected Tab Preference

![](ampl-frequently-asked-questions-guide/030.png)

Choose the outpatient sites and ordering institutions, then click on the Star icon. The star will be filled in, indicating a personal preference is saved.

<span id="_Toc217371194" class="anchor"></span>Figure 26: POM with Selected Tab, Sites, and Institutions Preferences

![](ampl-frequently-asked-questions-guide/031.png)

The next time you open AMPL, the tab, sites, and institutions will automatically be selected for you.

To change preferences, click on the Star icons for your new preferences. The previously selected stars will be cleared and your new selections will be set.

You may also set or change your user preferences by clicking on the User Name button in the header.

<span id="_Toc217371195" class="anchor"></span>Figure 27: Set User Preferences Button

![](ampl-frequently-asked-questions-guide/032.png)

# Patient Cover Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How do I view more detailed patient demographics?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the down arrow to the left of More (below the patient’s picture) to get more patient demographics.

<span id="_Toc217371196" class="anchor"></span>Figure 28: More Patient Demographics

![](ampl-frequently-asked-questions-guide/033.png)

## How do I get more detailed Allergy/ADR information?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the allergen in the Allergy Summary ribbon. It appears on the Allergy Summary ribbon, the Allergies and ADRs tab, and the CWAD section.

<span id="_Toc217371197" class="anchor"></span>Figure 29: More Information for Allergies and ADRs

![](ampl-frequently-asked-questions-guide/034.png)

## How can I address the No Allergy Assessment indicator for a patient?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a patient with no allergy assessment, AMPL has the capability to mark No Known Allergies at the selected site, if appropriate. If the patient has no allergy assessment, a pop-up dialog will display. If it is confirmed the patient has no known allergies and the user holds the proper VistA keys, clicking the Mark No Known Allergies button will record NKA in the patient’s VistA record. If the patient does have known allergies, AMPL does not currently have the capability to enter them.

<span id="_Toc217371198" class="anchor"></span>Figure 30: Mark No Known Allergies

![](ampl-frequently-asked-questions-guide/035.png)

## What is CWAD and how do I find that information?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CWAD is Crisis, Warnings, Allergies, and Directives found in the Postings button in the upper right corner. Click on this button to see the CWAD entries for that patient. Hovering over the Postings button shows additional information.

<span id="_Toc217371199" class="anchor"></span>Figure 31: Postings CWAD Buttons

![](ampl-frequently-asked-questions-guide/036.png)

## How do I see recent additions or changes to the patient’s data from VistA or CPRS?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Like VistA and CPRS, new changes made to patient data after the patient’s record is accessed in AMPL (entering a new order, discontinuing an active order) are not seen until the patient is refreshed. See figure below.

- In AMPL, the Refresh button is used.
- In CPRS, the File/Refresh Patient Information is used.
- In VistA, close the patient in a backdoor pharmacy option and open the patient again.

<span id="_Toc217371200" class="anchor"></span>Figure 32: Refresh Patient Data

![](ampl-frequently-asked-questions-guide/037.png)

## What is the number that I sometimes see next to the Tab name?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A numeric value indicates the total number of Allergy and Adverse Reaction records for the selected patient and the “+" sign indicates that patient has "allergies/ADRs that were entered in error."

<span id="_Toc217371201" class="anchor"></span>Figure 33: Total Number of Allergy and Adverse Reactions

![](ampl-frequently-asked-questions-guide/038.png)

## Is there a way to see allergies or ADRs that were “Entered in Error?”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes, click on the check box to the left of Show Entered in Error records.

<span id="_Toc217371202" class="anchor"></span>Figure 34: Allergies Entered in Error

![](ampl-frequently-asked-questions-guide/039.png)

## How do I know what facility entered the allergy/ADR?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility number where the allergy/ADR originated is in the last column to the right in the Allergies and ADRs tab.

<span id="_Toc217371203" class="anchor"></span>Figure 35: Originating Facility for Allergies and ADRs

![](ampl-frequently-asked-questions-guide/040.png)

## Okay, but how do I know what facility corresponds to that facility number?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hover over the facility number and the facility name will appear.

<span id="_Toc217371204" class="anchor"></span>Figure 36: Hover for Facility Name

![](ampl-frequently-asked-questions-guide/041.png)

## How do I find more information about column headers?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hover over the header and information about that header will appear.

<span id="_Toc217371205" class="anchor"></span>Figure 37: Hover Text for Column Headers

![](ampl-frequently-asked-questions-guide/042.png)

## It would be nice to be able to graph vitals to see trends. Can I do that with AMPL?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes, you can select date ranges, toggle between metric and US Standard units, and graph the vitals. The Graph button is on the far right and next to it is the Table button to return to table view.

<span id="_Toc217371206" class="anchor"></span>Figure 38: Graph Vitals

![](ampl-frequently-asked-questions-guide/043.png)

## How many progress note titles are displayed per page?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A maximum of 100 progress notes can be displayed per page. Additional notes may be viewed, 100 at a time, by clicking the Next button at the bottom of the page.

## How can I see a particular date range or an earlier date range than what is shown?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Query Editor can be used to filter and/or sort data for a date range. The Query Editor is opened by selecting the down arrow next to the Current Query button. Choose the Add Filter button to show filter options. Date/Time Entered is one of the options.

<span id="_Toc217371207" class="anchor"></span>Figure 39: Query Editor for Date Range

![](ampl-frequently-asked-questions-guide/044.png)

## There are a lot of progress notes. How do I sort and filter them?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Progress Notes Tab, there is a Current Query with a down arrow to the left of it. Select the down arrow to bring up the Sort and Filter options. Choose the Add Filter button to show filter options.

If Add Sort Field is selected, the same options appear but will sort by those fields instead of filter.

Don’t forget to click on the Add button after you make your selection (multiple filters and sort fields may be added at once). Execute the new filter and sort criteria by clicking on the Refresh button to the right of the page.

See <u>0</u> for more info on sorting and filtering Progress Notes

<span id="_Toc217371208" class="anchor"></span>Figure 40: Progress Notes Sort and Filter

![](ampl-frequently-asked-questions-guide/045.png)

## How do I see the actual progress note?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the note title to get a detailed view.

## How do I see Remote meds?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are remote meds, under the Med List Tab, there will be a circle with an “R” inside to the right of the column header. Click on that R.

> **NOTE:** There will be no “inpatient” remote medications.

<span id="_Toc217371209" class="anchor"></span>Figure 41: Remote Meds

![](ampl-frequently-asked-questions-guide/046.png)

## How do I see a more detailed view of the meds?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the More button to the right of the header. This will give more information about all the meds in that section.

<span id="_Toc217371210" class="anchor"></span>Figure 42: Detailed View of Meds

![](ampl-frequently-asked-questions-guide/047.png)

## Okay, but how do I see an even MORE detailed view of the medication orders?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the medication name in the section and it will give you a detailed view of the medication order.

<span id="_Toc217371211" class="anchor"></span>Figure 43: Even More Detailed View of Medication Order

![](ampl-frequently-asked-questions-guide/048.png)

## I see buttons at the bottom of that view. What are those for?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A screenshot of those buttons is below. They include Order Checks, Drug Restrictions/ Guidelines, Drug Info, Provider Info, PADE Inventory Activity, Admin Hx, and Close. These buttons put often needed information that you can find in VistA and CPRS, but in a much easier to find and read format for each order. If the button is greyed out, there is no information for that item.

<span id="_Toc217371212" class="anchor"></span>Figure 44: Order Checks, Drug Restrictions/Guidelines, Drug Info, Provider Info, PADE Inventory Activity, Admin Hx, and Close

![](ampl-frequently-asked-questions-guide/049.png)

## For Inpatient and Clinical Med Orders, can I see PADE inventory amounts for the associated device?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes, click on the PADE Inventory Activity button at the bottom of the screen when in a medications detailed view.

<span id="_Toc217371213" class="anchor"></span>Figure 45: PADE Inventory Activity

![](ampl-frequently-asked-questions-guide/050.png)

## How can I identify flagged orders and obtain more details?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Medication List views, a flagged icon is displayed on flagged orders, hovering over the flagged icon will display the date/time the order was flagged, flagged by, and the flag reason. In Medication Order Detail views, Flag/Unflag information is displayed.

# Filter and Sort (Queries)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is the difference between National and User queries?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

National queries are created by Pharmacy Benefits Management (PBM) and available to users across all sites. Personal user queries are only available to the user who created and saved them.

As a user, you will not be able to add or edit a national query and make it available to all sites. However, you can edit a national query and save it as a personal user query, which will be available to only you.

<span id="_Toc217371214" class="anchor"></span>Figure 46: National Query

![](ampl-frequently-asked-questions-guide/051.png)

<span id="_Toc217371215" class="anchor"></span>Figure 47: Personal User Query

![](ampl-frequently-asked-questions-guide/052.png)

## Can I get more information on sort and filter functionality for Allergies and ADRs Labs, Consults, Progress Notes, Immunizations, Problem List, and Appointments tabs?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each tab has its own unique filter and sort criteria to quickly and efficiently filter and sort to find the information you need.

There are several things to remember. After selecting the filter or sort, don’t forget to click the Add button to add your new criteria to the filter or sort section above the options. You can add multiple filter or sort criteria if needed. Once you have your filter and sort criteria finished, click the Refresh button to the right side of the screen. Below the Refresh button is a Reset button to return to the default search and sort settings.

Listed below are figures and information for each tab to show what types of data may be used to filter or sort data.

### Meds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Starting out with an exception, the Med List tab doesn’t currently include a Query Editor. Instead, it displays all Active/Recently Expired, Pending and Non-Verified orders. Remote Outpatient, Clinic and Non-VA orders may be added by checking the R button in the section header.

<span id="_Toc217371216" class="anchor"></span>Figure 48: Remote Order Button

![](ampl-frequently-asked-questions-guide/053.png)

An expanded view for orders in a category may be accessed by clicking the More button for that category. Additional details for a specific order are displayed by clicking on the order from the Expanded View.

<span id="_Toc217371217" class="anchor"></span>Figure 49: More Button

![](ampl-frequently-asked-questions-guide/054.png)

> **NOTE:** The Outpatient medications included in the discontinued and expired categories are determined by RECENTLY DC’D/EXPIRED DAYS Field (#3.2) in the OUTPATIENT SITE (#59) File. Inpatient Medication Orders include orders that were discontinued or expired in the last 24 hours in the RECENTLY DC’D/EXPIRED section.

A long profile view for orders in a category may be accessed by clicking on the Long button for that category. This will display additional discontinued and expired orders for the patient, providing a more comprehensive view of their order history. Additional details for a specific order can be displayed by clicking on the order from the Long Profile View.

<span id="_Toc217371218" class="anchor"></span>Figure 50: Long Button

![](ampl-frequently-asked-questions-guide/055.png)

For more FAQs about the Meds tab, see [Section 4.17](#how-do-i-see-a-more-detailed-view-of-the-meds) of this document.

### Allergies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Allergies/ADRs and Assessments are displayed for all sites where a patient has been seen. Records may be further filtered or sorted using the Query Editor. It is accessed by clicking on the down arrow next to the Current Query.

<span id="_Toc217371219" class="anchor"></span>Figure 51: Current Query

![](ampl-frequently-asked-questions-guide/056.png)

After adding new filter or sort criteria, don’t forget to click on the Add button to add your new criteria to the Filters or Sort sections above the options. You may add multiple filter or sort criteria. Once you have completed filter and sort criteria changes, click on the Refresh button to the right side of the screen. Below the Refresh button is a Reset button, which will return to the default search and sort settings.

<span id="_Toc217371220" class="anchor"></span>Figure 52: Allergies Filtering and Sorting

![](ampl-frequently-asked-questions-guide/057.png)

#### Adding Filter Criteria

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators changes based on the type of data selected in the filter field.

<span id="_Toc217371221" class="anchor"></span>Figure 53: Allergies Adding Filter Criteria

![](ampl-frequently-asked-questions-guide/058.png)

<span id="_Toc217371222" class="anchor"></span>Figure 54: Allergies Adding Filter

![](ampl-frequently-asked-questions-guide/059.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or selecting from common date ranges by clicking on the down arrows to the left of the date/time as shown below:

<span id="_Toc217371223" class="anchor"></span>Figure 55: Allergies Date Range Filter

![](ampl-frequently-asked-questions-guide/060.png)

If a text field is selected, the Filter Text box turns into a Select a Value drop down that includes only values included in the patient’s data. In the example below for causative agent, the possible options are displayed and as many or few as you like can be checked.

<span id="_Toc217371224" class="anchor"></span>Figure 56: Allergies Selecting a Value

![](ampl-frequently-asked-questions-guide/061.png)

#### Adding Sort Criteria

Setting Sort criteria is like setting filter criteria. A drop-down box shows the fields that can be used for sorting.

<span id="_Toc217371225" class="anchor"></span>Figure 57: Allergies Adding Sort Field

![](ampl-frequently-asked-questions-guide/062.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for both filter and Sort sections, located on the right side of the section.

<span id="_Toc217371226" class="anchor"></span>Figure 58: Allergies New Filter Add Button

![](ampl-frequently-asked-questions-guide/063.png)

The Refresh and Reset buttons are in the Execute section on the right of the Query Editor. Refresh will apply any new filters. Reset will return the display to the default criteria.

<span id="_Toc217371227" class="anchor"></span>Figure 59: Allergies Refresh Button

![](ampl-frequently-asked-questions-guide/064.png)

To remove a single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc217371228" class="anchor"></span>Figure 60: Allergies Red X Button

![](ampl-frequently-asked-questions-guide/065.png)

To clear all filters and sorts added by the user and return to the default settings for the tab, click the Reset button.

<span id="_Toc217371229" class="anchor"></span>Figure 61: Allergies Reset Button

![](ampl-frequently-asked-questions-guide/066.png)

### Vitals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals is the second tab that does not include a query editor. Instead, the Vitals tab initially displays a table of the latest common vitals. You can view past readings by clicking on the vital name, results will display to the right with a default date range of one year for Outpatient and one week for Inpatient. Additional Vitals may be added to the table by clicking on the Vital name. They can be removed by clicking again.

<span id="_Toc217371230" class="anchor"></span>Figure 62: Vitals Display with Details

![](ampl-frequently-asked-questions-guide/067.png)

To change the date range, modify the Readings from or through dates.

<span id="_Toc217371231" class="anchor"></span>Figure 63: Vitals Date Range

![](ampl-frequently-asked-questions-guide/068.png)

There are several ways to enter dates - typing the date, clicking on the calendars or selecting from common date ranges by clicking on the down arrows to the left of the date/time as shown below.

<span id="_Toc217371232" class="anchor"></span>Figure 64: Vitals Commonly Used Date Ranges

![](ampl-frequently-asked-questions-guide/069.png)

Vital types in the date range table may also be shown in a graph by selecting the Graphing icon located in the top right corner of the Vitals screen.

<span id="_Toc217371233" class="anchor"></span>Figure 65: Vitals Graphing

![](ampl-frequently-asked-questions-guide/070.png)

### Labs Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Current Query default for Labs is Collection Date/Time within the past year, sorted by Collection Date/Time with newest results first, and 100 records per page. The Filter and sort criteria can be changed using the Query Editor. The Query Editor is accessed by clicking the blue down arrow.

<span id="_Toc217371234" class="anchor"></span>Figure 66: Labs Current Query

![](ampl-frequently-asked-questions-guide/071.png)

#### Adding Filter Criteria

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators changes based on the type of data selected in the filter field.

<span id="_Toc217371235" class="anchor"></span>Figure 67: Labs Select Filter Field

![](ampl-frequently-asked-questions-guide/072.png)

<span id="_Toc217371236" class="anchor"></span>Figure 68: Labs Filter Contains Field

![](ampl-frequently-asked-questions-guide/073.png)

For efficiency, the Filter Text box turns into a Select a Value drop down with options specific to the patient’s data.

<span id="_Toc217371237" class="anchor"></span>Figure 69: Labs Filter Contains Field

![](ampl-frequently-asked-questions-guide/074.png)

<span id="_Toc217371238" class="anchor"></span>Figure 70: Labs Selecting a Value

![](ampl-frequently-asked-questions-guide/075.png)

If the filter is a date range, there are several ways to enter dates: typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box, which displays common date ranges as shown below:

<span id="_Toc217371239" class="anchor"></span>Figure 71: Labs Selecting a Date Range

![](ampl-frequently-asked-questions-guide/076.png)

#### Adding Sort Criteria

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc217371240" class="anchor"></span>Figure 72: Labs Adding Sort Criteria

![](ampl-frequently-asked-questions-guide/077.png)

By selecting Results per Page, you can decrease the number of results per page as below, the default is 100.

<span id="_Toc217371241" class="anchor"></span>Figure 73: Labs Results Per Page

![](ampl-frequently-asked-questions-guide/078.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located in the right side of the section.

<span id="_Toc217371242" class="anchor"></span>Figure 74: Labs Add Button for Sort Criteria

![](ampl-frequently-asked-questions-guide/079.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc217371243" class="anchor"></span>Figure 75: Labs Refresh Button

![](ampl-frequently-asked-questions-guide/080.png)

To remove a single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc217371244" class="anchor"></span>Figure 76: Labs Red X Button

![](ampl-frequently-asked-questions-guide/081.png)

To clear all filters and sorts added by the user and return to the default settings for the tab, click the Reset button.

<span id="_Toc217371245" class="anchor"></span>Figure 77: Labs Reset button

![](ampl-frequently-asked-questions-guide/082.png)

### Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default filter/sort criteria for Progress Notes is: Records within the last year, sorted by Date/Time Entered with most recent notes first, 100 results per page. These criteria may be changed using the Query Editor by clicking on the blue drop-down arrow to the left of the Current Query.

<span id="_Toc217371246" class="anchor"></span>Figure 78: Progress Notes Current Query

![](ampl-frequently-asked-questions-guide/083.png)

#### Adding Filter Criteria

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators changes based on the type of data selected in the filter field. 

<span id="_Toc217371247" class="anchor"></span>Figure 79: Progress Notes Select Filter Field

![](ampl-frequently-asked-questions-guide/084.png)

<span id="_Toc217371248" class="anchor"></span>Figure 80: Progress Notes Add Filter Contains

![](ampl-frequently-asked-questions-guide/085.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc217371249" class="anchor"></span>Figure 81: Progress Notes Add Filter

![](ampl-frequently-asked-questions-guide/086.png)

#### Adding Sort Criteria

Setting Sort criteria is like setting filter criteria. A drop-down box shows the fields that can be used for sorting.

<span id="_Toc217371250" class="anchor"></span>Figure 82: Progress Notes Add Sort Field

![](ampl-frequently-asked-questions-guide/087.png)

Selecting Results per Page. You can decrease the number of results per page as below, the default is 100.

<span id="_Toc217371251" class="anchor"></span>Figure 83: Progress Notes Results Per Page

![](ampl-frequently-asked-questions-guide/088.png)

As each filter or sort is defined, click the Add button to add it to the query. There is an Add button for each section, located in the right side of the section.

<span id="_Toc217371252" class="anchor"></span>Figure 84: Progress Notes Add Buttons

![](ampl-frequently-asked-questions-guide/089.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc217371253" class="anchor"></span>Figure 85: Refresh Button

![](ampl-frequently-asked-questions-guide/090.png)

To remove a single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc217371254" class="anchor"></span>Figure 86: Remove Single Criteria Notes Tab

![](ampl-frequently-asked-questions-guide/091.png)

To clear all filters and sorts added by the user and return to the default settings for the tab, click the Reset button.

<span id="_Toc217371255" class="anchor"></span>Figure 87: Reset Button for Notes

![](ampl-frequently-asked-questions-guide/092.png)

### Consults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default display for the Consults tab is All Records, sorted by Date/Time descending, 100 results/page. The filter and sort criteria maybe changed using the Query Editor.

<span id="_Toc217371256" class="anchor"></span>Figure 88: Consults Current Query

![](ampl-frequently-asked-questions-guide/093.png)

#### Adding Filter Criteria

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators changes based on the type of data selected in the filter field.

<span id="_Toc217371257" class="anchor"></span>Figure 89: Consults Select Filter Field

![](ampl-frequently-asked-questions-guide/094.png)

<span id="_Toc217371258" class="anchor"></span>Figure 90: Consults Filter Contains

![](ampl-frequently-asked-questions-guide/095.png)

To make it easy to add filters, the Filter Text box turns into a Select a Value drop down with options specific to the patient’s data.

<span id="_Toc217371259" class="anchor"></span>Figure 91: Consults Selecting a Value

![](ampl-frequently-asked-questions-guide/096.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

#### Adding Sort Criteria

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc217371260" class="anchor"></span>Figure 92: Consults Add Sort Field

![](ampl-frequently-asked-questions-guide/097.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located in the right side of the section.

<span id="_Toc217371261" class="anchor"></span>Figure 93: Consults New Filter Add Button

![](ampl-frequently-asked-questions-guide/098.png)

Selecting Results per Page. You can decrease the number of results per page as shown below, the default is 100.

<span id="_Toc217371262" class="anchor"></span>Figure 94: Consults Results Per Page

![](ampl-frequently-asked-questions-guide/099.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc217371263" class="anchor"></span>Figure 95: Refresh/Reset Buttons

![](ampl-frequently-asked-questions-guide/100.png)

To remove a single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc217371264" class="anchor"></span>Figure 96: Consult Remove Single Criteria

![](ampl-frequently-asked-questions-guide/101.png)

To clear all filters and sorts added by the user and return to the default settings for the tab, click the Reset button.

<span id="_Toc217371265" class="anchor"></span>Figure 97: Consult Reset Button

![](ampl-frequently-asked-questions-guide/102.png)

### Problem List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default view for the Problem List tab is all active problems sorted by Immediacy (Acute, Chronic or Unknown) in alphabetical order, then by Description in Alphabetical order.

<span id="_Toc217371266" class="anchor"></span>Figure 98: Problem List Current Query

![](ampl-frequently-asked-questions-guide/103.png)

#### Adding Filter Criteria

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators changes based on the type of data selected in the filter field. 

<span id="_Toc217371267" class="anchor"></span>Figure 99: Problem List Select Filter Field

![](ampl-frequently-asked-questions-guide/104.png)

<span id="_Toc141258478" class="anchor"></span>Figure 100: Problem List Add Filter Operators

![](ampl-frequently-asked-questions-guide/105.png)

To make it easy to add filters, the Filter Text box turns into a Select a Value drop down with values specific to the patient’s data.

<span id="_Toc217371269" class="anchor"></span>Figure 101: Problem List Selecting a Value

![](ampl-frequently-asked-questions-guide/106.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc217371270" class="anchor"></span>Figure 102: Problem List Add Date Range Filter

![](ampl-frequently-asked-questions-guide/107.png)

#### Adding Sort Criteria

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc217371271" class="anchor"></span>Figure 103: Problem List Adding Sort Field

![](ampl-frequently-asked-questions-guide/108.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located in the right side of the section. 

<span id="_Toc141258482" class="anchor"></span>Figure 104: Problem List Add Buttons

![](ampl-frequently-asked-questions-guide/109.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc141258483" class="anchor"></span>Figure 105: Problem List Refresh Button

![](ampl-frequently-asked-questions-guide/110.png)

To remove a single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc141258484" class="anchor"></span>Figure 106: Problem List Remove Single Filter or Sort

![](ampl-frequently-asked-questions-guide/111.png)

To clear all filters and sorts added by the user and return to the default settings for the tab, clickthe Reset button.

<span id="_Toc141258485" class="anchor"></span>Figure 107: Problem List Reset button

![](ampl-frequently-asked-questions-guide/112.png)

### Immunizations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default view for the Immunizations tab is All Records, sorted by Name (of immunization), most recent record first. The filter and sort criteria may be changed using the Query Editor. It is access by clicking on the blue down-arrow next to the Current Query.

<span id="_Toc217371276" class="anchor"></span>Figure 108: Immunizations Current Query

![](ampl-frequently-asked-questions-guide/113.png)

#### Adding Filter Criteria

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators changes based on the type of data selected in the filter field. 

<span id="_Toc217371277" class="anchor"></span>Figure 109: Immunizations Select Filter Field

![](ampl-frequently-asked-questions-guide/114.png)

<span id="_Toc217371278" class="anchor"></span>Figure 110: Immunizations Add Filter Operators

![](ampl-frequently-asked-questions-guide/115.png)

To make it easy to add filters, the Filter Text box turns into a Select a Value drop-down with options specific to the patient’s data.

<span id="_Toc217371279" class="anchor"></span>Figure 111: Immunizations Selecting a Value

![](ampl-frequently-asked-questions-guide/116.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box, which displays common date ranges as shown below:

<span id="_Toc217371280" class="anchor"></span>Figure 112: Immunization Date Filter

![](ampl-frequently-asked-questions-guide/117.png)

#### Adding Sort Criteria

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc217371281" class="anchor"></span>Figure 113: Immunizations Adding Sort Criteria

![](ampl-frequently-asked-questions-guide/118.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located on the right side of the section.

<span id="_Toc217371282" class="anchor"></span>Figure 114: Immunizations Add Buttons

![](ampl-frequently-asked-questions-guide/119.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc217371283" class="anchor"></span>Figure 115: Immunizations Refresh Button

![](ampl-frequently-asked-questions-guide/120.png)

To remove a single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc217371284" class="anchor"></span>Figure 116: Immunization Remove Single Criteria

![](ampl-frequently-asked-questions-guide/121.png)

To clear all filters and sorts added by the user and return to the default settings for the tab, clickthe Reset button.

<span id="_Toc217371285" class="anchor"></span>Figure 117: Immunization Reset Button

![](ampl-frequently-asked-questions-guide/122.png)

### Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default display for the Appointments tab is Records within the last year, sorted by Date/Time descending, 100 results/page. The filter and sort criteria may be changed using the Query Editor. It is accessed by clicking on the blue down-arrow next to the Current Query.

<span id="_Toc217371286" class="anchor"></span>Figure 118: Appointments Current Query

![](ampl-frequently-asked-questions-guide/123.png)

#### Adding Filter Criteria

The drop-down list of Filter Fields displays fields that can be used to restrict the list. The list of operators changes based on the type of data selected in the filter field.

<span id="_Toc217371287" class="anchor"></span>Figure 119: Appointments Select Filter Field

![](ampl-frequently-asked-questions-guide/124.png)

<span id="_Toc217371288" class="anchor"></span>Figure 120: Appointments Add Filter Operators

![](ampl-frequently-asked-questions-guide/125.png)

To make it easy to add filters, the Filter Text box turns into a Select a Value drop-down with options specific to the patient’s data.

<span id="_Toc217371289" class="anchor"></span>Figure 121: Appointments Filter

![](ampl-frequently-asked-questions-guide/126.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc217371290" class="anchor"></span>Figure 122: Appointments Date Filter

![](ampl-frequently-asked-questions-guide/127.png)

#### Adding Sort Criteria

Setting sort criteria is like setting filter criteria. A drop-down box shows the fields that can be used for sorting.

<span id="_Toc217371291" class="anchor"></span>Figure 123: Appointments Add Sort Criteria

![](ampl-frequently-asked-questions-guide/128.png)

Select the number of results per page. You can decrease the number of results per page as below. The default is 100.

<span id="_Toc217371292" class="anchor"></span>Figure 124: Appointments Results Per Page

![](ampl-frequently-asked-questions-guide/129.png)

As each filter or sort is defined, click the Add button to add it to the query. There is an Add button for each section, located in the right side of the section.

> <span id="_Toc217371293" class="anchor"></span>Figure 125: Appointments Add Buttons

![](ampl-frequently-asked-questions-guide/130.png)

To process the list with your new criteria, click on the Refresh button.

<span id="_Toc217371294" class="anchor"></span>Figure 126: Appointments Refresh Button

![](ampl-frequently-asked-questions-guide/131.png)

To remove a single filter or sort criteria, including one of the defaults, click on the Red X next to it.

<span id="_Toc217371295" class="anchor"></span>Figure 127: Appointments Remove Single Criteria

![](ampl-frequently-asked-questions-guide/132.png)

To clear all filters and sorts added by the user and return to the tab’s default, click on the Reset button.

### Pharmacogenomics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default display for Pharmacogenomics tab is all records, sorted by Lab Date descending, then gene ascending. The filter and sort criteria may be changed using the Query Editor. It is accessed by clicking on the blue down-arrow next to the Current Query. The Select a Value drop down list displays options specific to the patient’s data.

<span id="_Toc217371296" class="anchor"></span>Figure 128: Pharmacogenomics Default Query

![](ampl-frequently-asked-questions-guide/133.png)

<span id="_Toc217371297" class="anchor"></span>Figure 129: Pharmacogenomics Filter

![](ampl-frequently-asked-questions-guide/134.png)

<span id="_Toc217371298" class="anchor"></span>Figure 130: Pharmacogenomics Sort Options

![](ampl-frequently-asked-questions-guide/135.png)

To reorganize the genes in alphabetical order, change the Sort order to Gene by deleting the Lab Date from the sort criteria and clicking Refresh. Note the green arrow by the Lab Date column no longer displays and the list is sorted by gene.

<span id="_Toc217371299" class="anchor"></span>Figure 131: Pharmacogenomics Sort Genes Alphabetically

![](ampl-frequently-asked-questions-guide/136.png)

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

: POM Button Toggle to Cover Sheet, 8
“i” symbol, 8
Add button
Labs Sort Criteria, 29
Add Buttons
Appointments, 47
Immunizations, 43
Problem List, 40
Progress Notes, 33
Add Filter
Progress Notes, 31
Add Filter Operators
Appointments, 45
Immunizations, 41
Adding Filter Criteria
Allergies, 21
Adding Sort Criteria
Allergies, 23
Admin Hx, 17
Allergies Tab, 20
Allergy/ADR, 11
AMPL URL, 1
Appointments Tab, 44
ASAP orders, 6
Black Funnel Symbol, 4
Change Patients, 8
Clinic Orders, 5
Clinic Pending Orders List, 6
Clinic Sort Groups, 5
Consults Tab, 34
Current Query
Allergies, 20
Appointments, 44
Immunizations, 41
Labs, 26
CWAD, 12
Date Filter
Appointments, 46
Immunizations, 42
Date Range, 15
Labs, 28
Vitals, 25
Date Range Filter
Problem List, 39
Drug Info, 17
Drug Restrictions/ Guidelines, 17
Entered in Error, 13
Facility Number, 14
File/Refresh Patient Information, 13
Filter and Sort, 18
Filter Contains Field
Labs, 27
Filter Criteria
Appointments, 44
Consults, 34
Immunizations, 41
Problem List, 37
Progress Notes, 30
Filtering and Sorting
Allergies, 21
Find Flagged Orders, 7
Flagged Orders, 18
Flagged Outpatient Orders, 6
Funnel Symbol, 4
Graph Vitals, 15
Graphing, 25
Green Arrows, 3
Hover Text, 4
Hover Text for Column Headers, 14
Immunizations Tab, 40
Inpatient Orders, 5
Inpatient Pending Orders, 6
Inventory Activity, 17
Labs Tab, 26
Logging On, 1
Long Button, 20
Mark No Known Allergies, 12
Medication Orders More Details, 17
Meds Detailed View, 17
Meds Tab, 19
More Button, 20
More Patient Demographics, 11
Multiple Patients, 8
National Queries, 18
Order Aging Summary, 4
Order Checks, 17
Ordering Aging Summary, 5
Orders with Invalid Outpatient Sites, 7
Outpatient Orders by Location, 5
PADE Inventory Activity, 17
PADE inventory amounts, 18
Patient Cover Sheet, 8, 11
Patient List Priority Indicator, 6
Patient Queue, 8
Pending Orders, 5
Personal Identification Number, 1
Pharmacogenomics Tab, 48
PIN, 1
PIV, 1
POM, 3
Preferences, 10
Problem List Tab, 37
Process under correct Outpatient Site, 7
Progress Notes, 15
Progress Notes Sort and Filter, 16
Progress Notes Tab, 30
Provider Info, 17
Queries, 18
Query
Pharmacogenomics, 48
Problem List, 37
Progress Notes Current Query, 30
Query Editor, 5
Recently DC’d/Expired, 20
Red X
Consults, 36
Red X Button
Allergies, 24
Labs, 30
Refresh button
Labs, 29
Refresh Button
Allergies, 24
Appointments, 47
Consults, 36
Immunizations, 43
Problem List, 40
Progress Notes, 33
Remote meds, 16
Remote Order Button, 20
Remove Single Criteria
Appointments, 47
Consults, 37
Immunizations, 44
Remove Single Filter or Sort
Problem List, 40
Report of facilities, 2
Reset button
Allergies, 24
Labs, 30
Problem List, 40
Reset Button
Consults, 36, 37
Immunizations, 44
Progress Notes, 33
Results Per Page
Consults, 36
Labs, 29
Progress Notes, 32
Select a Value
Appointments, 45
Immunizations, 42
Problem List, 38
Select Filter Field
Appointments, 45
Consults, 34
Immunizations, 41
Labs, 26
Select Ordering Institution, 3
Select Patients to Process, 5
Selecting a Value
Consults, 35
Set User Preferences Button, 11
Sort and Filter, 16
Sort Criteria
Appointments, 46
Consults, 35
Immunizations, 42
Labs, 28
Problem List, 39
Progress Notes, 32
Sort Genes Alphabetically, 49
Sort Options
Pharmacogenomics, 48
Station Number, 2
User queries, 18
VA Ordering Aging Summary, 5
VA Personal Identity Verification, 1
VA Single Sign-On, 2
VA SSOi page, 1
VistA Patient Lookup, 9
VistA Patient Lookup Help Text, 9
Vitals Tab, 25
Ward Groups, 5
Ward List Priority Indicator, 6
