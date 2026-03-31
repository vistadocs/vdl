---
title: AMPL Frequently Asked Questions
doc_type: FAQ
doc_label: Frequently Asked Questions
doc_layer: anchor
doc_subject: AMPL
app_code: PREA
app_name: "Pharmacy: Advanced Medication Platform"
section: CLI
app_status: archive
pkg_ns: PREA
patch_ver: 1.4
patch_id: PREA*1.4
group_key: "PREA:PREA:1.4"
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
  - class
  - anchor
  - figure
  - filter
  - table
page_count: 0
word_count: 7604
section_count: 39
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA_Archive/prea_1_4_ampl_gui_faq.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA_Archive/prea_1_4_ampl_gui_faq.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=398"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Advanced Medication Platform (AMPL)  
  Graphic User Interface (GUI)

  Frequently Asked Questions (FAQ)
---

![](ampl-frequently-asked-questions/001.png)

August 2023

Revision History

| Date    | Version | Description       | Author    |
|---------|---------|-------------------|-----------|
| 07/2023 | 1.0     | Baseline Document | AMPL Team |

Revision History showing date artifact was created or revised, version number, description, and author.

Artifact Rationale

The FAQ provides answers to frequently asked questions which may be needed by the AMPL GUI and AMPL GUI support teams to answer questions as they arise during the development and continuation of AMPL GUI. The FAQ is an optional resource which serves as addition to required documentation support for AMPL GUI users and testers.

Table of Contents

Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [What is AMPL GUI?](#what-is-ampl-gui)
- [Logging On](#logging-on)
  - [How do I log on to AMPL GUI?](#how-do-i-log-on-to-ampl-gui)
    - [How do I know what my 3-digit station number is?](#how-do-i-know-what-my-3-digit-station-number-is)
- [Pending Orders Manager (POM)](#pending-orders-manager-pom)
  - [What is the “Pending Orders Manager”?](#what-is-the-pending-orders-manager)
  - [Why are patients not showing under the Pending Orders Manager?](#why-are-patients-not-showing-under-the-pending-orders-manager)
  - [What does the “Select Ordering Institution” button do?](#what-does-the-select-ordering-institution-button-do)
  - [What are those numbers I see in the blue bubbles on the tabs?](#what-are-those-numbers-i-see-in-the-blue-bubbles-on-the-tabs)
  - [What are those green arrows in the column headers?](#what-are-those-green-arrows-in-the-column-headers)
  - [What is the black funnel symbol I see in the column headers?](#what-is-the-black-funnel-symbol-i-see-in-the-column-headers)
  - [How can I get more information about the column headers?](#how-can-i-get-more-information-about-the-column-headers)
  - [Can I sort the patients by the age of the orders?](#can-i-sort-the-patients-by-the-age-of-the-orders)
  - [How can I take advantage of Clinic Sort Groups or Ward Groups that are set-up in VistA?](#how-can-i-take-advantage-of-clinic-sort-groups-or-ward-groups-that-are-set-up-in-vista)
  - [For Inpatient pending orders, do ASAP orders show up under the STAT heading?](#for-inpatient-pending-orders-do-asap-orders-show-up-under-the-stat-heading)
  - [Can I find flagged Outpatient orders in AMPL?](#can-i-find-flagged-outpatient-orders-in-ampl)
  - [I have my patient list, now what?](#i-have-my-patient-list-now-what)
  - [How do I change patients?](#how-do-i-change-patients)
  - [What is the “i” symbol next to Pending Orders Manager?](#what-is-the-i-symbol-next-to-pending-orders-manager)
  - [What if I just want to go to an individual patient not on the Pending Orders Manager?](#what-if-i-just-want-to-go-to-an-individual-patient-not-on-the-pending-orders-manager)
  - [What is the “i” symbol next to VISTA Patient Lookup?](#what-is-the-i-symbol-next-to-vista-patient-lookup)
- [Patient Coversheet](#patient-coversheet)
  - [How do I view more detailed patient demographics?](#how-do-i-view-more-detailed-patient-demographics)
  - [How do I get more detailed Allergy/ADR information?](#how-do-i-get-more-detailed-allergyadr-information)
  - [What is CWAD and how do I find that information?](#what-is-cwad-and-how-do-i-find-that-information)
  - [How do I see recent additions or changes to the patient's data from VistA or CPRS?](#how-do-i-see-recent-additions-or-changes-to-the-patients-data-from-vista-or-cprs)
  - [What is the number that I sometimes see next to the Tab Name?](#what-is-the-number-that-i-sometimes-see-next-to-the-tab-name)
  - [Is there a way to see allergies or ADRS that were “Entered in Error”?](#is-there-a-way-to-see-allergies-or-adrs-that-were-entered-in-error)
  - [How do I know what facility entered the allergy/ADR?](#how-do-i-know-what-facility-entered-the-allergyadr)
  - [Okay, but how do I know what facility corresponds to that facility number?](#okay-but-how-do-i-know-what-facility-corresponds-to-that-facility-number)
  - [How do I find more information about column headers?](#how-do-i-find-more-information-about-column-headers)
  - [It would be nice to be able to graph vitals to see trends, can I do that with AMPL?](#it-would-be-nice-to-be-able-to-graph-vitals-to-see-trends-can-i-do-that-with-ampl)
  - [How many progress note titles are displayed per page?](#how-many-progress-note-titles-are-displayed-per-page)
  - [How can I see a particular date range or an earlier date range than what is shown?](#how-can-i-see-a-particular-date-range-or-an-earlier-date-range-than-what-is-shown)
  - [There are a lot of progress notes, how do I sort and filter them?](#there-are-a-lot-of-progress-notes-how-do-i-sort-and-filter-them)
  - [How do I see the actual progress note?](#how-do-i-see-the-actual-progress-note)
  - [How do I see Remote meds?](#how-do-i-see-remote-meds)
  - [How do I see a more detailed view of the meds?](#how-do-i-see-a-more-detailed-view-of-the-meds)
  - [Okay, but how do I see an even MORE detailed view of the medication orders?](#okay-but-how-do-i-see-an-even-more-detailed-view-of-the-medication-orders)
  - [I see buttons at the bottom of that view, what are those for?](#i-see-buttons-at-the-bottom-of-that-view-what-are-those-for)
  - [For Inpatient and Clinical Med Orders, can I see PADE inventory amounts for the associated device?](#for-inpatient-and-clinical-med-orders-can-i-see-pade-inventory-amounts-for-the-associated-device)
- [Filter and Sort](#filter-and-sort)
  - [Can I get more information on sort and filter functionality for Allergies and ADRs, Labs, Consults, Progress Notes, Immunizations, Problem List, and Appointments tabs?](#can-i-get-more-information-on-sort-and-filter-functionality-for-allergies-and-adrs-labs-consults-progress-notes-immunizations-problem-list-and-appointments-tabs)
    - [Meds](#meds)
    - [Allergies](#allergies)
    - [Vitals](#vitals)
    - [Labs](#labs)
    - [Progress Notes](#progress-notes)
    - [Consults](#consults)
    - [Problem List](#problem-list)
    - [Immunizations](#immunizations)
    - [Appointments](#appointments)

## What is AMPL GUI?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Advanced Medication Platform (AMPL) Graphic User Interface (GUI) is a front-end application supporting the Department of Veterans Affairs (VA) pharmacists by fulfilling the need for medical knowledge during patient care. AMPL GUI provides a single point of access for pharmacists to do their work, such as reviewing patient records and processing pending orders.

Currently, AMPL GUI is a READ ONLY application. Writing and processing of orders as well as note writing, etc. is planned for a later phase.

# Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How do I log on to AMPL GUI?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter the AMPL URL (<https://ampl.vaec.va.gov/login>) into the address bar of your internet browser.
2.  After selecting Login, users are redirected to the VA SSOi page.
- Click on Sign In with VA Personal Identity Verification (PIV) Card graphic.
- Select the appropriate certificate.
- Enter your Personal Identification Number (PIN) and select OK.

<span id="_Toc95211569" class="anchor"></span>Figure 1: VA Advanced Medication Platform Login Page

![](ampl-frequently-asked-questions/002.png)

<span id="_Toc141258391" class="anchor"></span>Figure 2: VA Single Sign-On

![](ampl-frequently-asked-questions/003.png)

### How do I know what my 3-digit station number is?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc141258392" class="anchor"></span>Figure 3: Set VistA Context 3-Digit Station Number

![](ampl-frequently-asked-questions/004.png)

The links below can be used to get a report of facilities and their station number:

> Internet - [To Facility Listing - Locations (va.gov)](https://www.va.gov/directory/guide/rpt_fac_list.cfm)

> Intranet - [Report - Facility Listing - Facilities Locator & Leadership Directory (va.gov)](https://vaww.va.gov/directory/guide/rpt_fac_list.cfm?isflash=1)

> Your station number is also found in VistA, it is displayed when you enter your division. See example below:

<span id="_Toc141258393" class="anchor"></span>Figure 4: Station Number in VistA

> ![](ampl-frequently-asked-questions/005.png)

# Pending Orders Manager (POM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is the “Pending Orders Manager”?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pending orders manager of POM is a dashboard intended to help pharmacists manage and process pending orders for their facility.

## Why are patients not showing under the Pending Orders Manager?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To display a list of patients under the Pending Orders Manager, select an outpatient site from the dropdown list next to Select Outpatient Site.

## What does the “Select Ordering Institution” button do? 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Ordering Institution allows users to drill down to see orders for a specific CBOC or VAMC included under a Station.

## What are those numbers I see in the blue bubbles on the tabs?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the category tabs on the POM, the number of orders within that tab are displayed in the blue bubble on the tab.

<span id="_Toc141258394" class="anchor"></span>Figure 5: POM Number of Orders

![](ampl-frequently-asked-questions/006.png)

## What are those green arrows in the column headers?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To reveal if a column is sortable, click the column header. If it is sortable, the ![](ampl-frequently-asked-questions/007.png)icon will display. Repeatedly clicking the sortable column will toggle between ascending, descending then back to default. If more than 1 column is sorted, a small number by the arrow ![](ampl-frequently-asked-questions/008.png) indicates the order.

<span id="_Toc141258395" class="anchor"></span>Figure 6: Green Arrows Sorting Columns

![](ampl-frequently-asked-questions/009.png)

## What is the black funnel symbol I see in the column headers?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The black funnel symbol indicates that column is included in the current query.

<span id="_Toc141258396" class="anchor"></span>Figure 7: Black Funnel Symbol

![](ampl-frequently-asked-questions/010.png)

## How can I get more information about the column headers?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hovering your mouse over the column headers will reveal help text providing additional information. The hover functionality is available throughout AMPL, if you are not sure, hover!

<span id="_Toc141258397" class="anchor"></span>Figure 8: Hover Text

![](ampl-frequently-asked-questions/011.png)

## Can I sort the patients by the age of the orders?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, pending orders are displayed oldest first.

Clicking on the desired date range in the Order Aging Summary, located near the upper right-hand section of your screen will display only the orders that fall within that date range.

<span id="_Toc141258398" class="anchor"></span>Figure 9: VA Order Aging Summary

![](ampl-frequently-asked-questions/012.png)

Orders that display in any of the Pending Orders tabs may also be filtered using the Query Editor. Clicking on the blue arrow will expand the Query Editor.

<span id="_Toc141258399" class="anchor"></span>Figure 10: Current Query: All Records

![](ampl-frequently-asked-questions/013.png)

## How can I take advantage of Clinic Sort Groups or Ward Groups that are set-up in VistA?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Choose the Outpatient Orders by Location, Inpatient Orders, or Clinic Orders tab near the top of your screen. You will find Outpatient Clinic Sort Groups, Inpatient Ward Groups and Clinic Groups for Clinic Orders if you have them set up at your facility.

When you check a box for a clinic group or ward group, patients in the clinic or ward group with pending orders will be viewable below in the Select Patients to Process section (you may have to scroll down if there are a lot of groups).

There is also a Query Editor available in the Select Patients to Process section to further filter the list of patients. To filter the list, click on the down arrow to access the Query Editor (shown below).

> **NOTE:** Currently, AMPL is read only. The ability to process orders will be added in a later version.

<span id="_Toc141258400" class="anchor"></span>Figure 11: Select Patient(s) to Process

![](ampl-frequently-asked-questions/014.png)

## For Inpatient pending orders, do ASAP orders show up under the STAT heading?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes. The red symbol displays next to STAT orders, so they are easy to locate.

<span id="_Toc141258401" class="anchor"></span>Figure 12: Priority Indication Screen

![](ampl-frequently-asked-questions/015.png)

## Can I find flagged Outpatient orders in AMPL?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes. The red flag symbol displays next to Flagged orders, so they are easy to locate.

<span id="_Toc141258402" class="anchor"></span>Figure 13: Flagged Outpatient Pending Orders

![](ampl-frequently-asked-questions/016.png)

## I have my patient list, now what?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One or more patients may be selected from the list for processing using the Process Selected or Process All buttons. If multiple patients are selected, the first one will open to the Patient Coversheet and the rest will be added to the patient queue and their names will display at the bottom of the screen and using the patient queue button at the top of the screen.

<span id="_Toc141258403" class="anchor"></span>Figure 14: Patient Queue for Multiple Patients

![](ampl-frequently-asked-questions/017.png)

## How do I change patients?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once patient(s) are selected, you will be taken to the Patient Coversheet. If you want to go back into the Pending Orders Manager, you can select Pending Orders from the upper right corner of your screen. If you selected multiple patients and want to change patients, click on the Patient Queue button.

<span id="_Toc141258404" class="anchor"></span>Figure 15: POM Button Toggle to Coversheet and Retained in Patient Queue

![](ampl-frequently-asked-questions/018.png)

<span id="_Toc141258405" class="anchor"></span>Figure 16: Patient Cover Sheet with Patient Queue List

![](ampl-frequently-asked-questions/019.png)

## What is the “i” symbol next to Pending Orders Manager?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “i” next to Pending Orders Manager text gives informational text regarding POM Navigational help once it is clicked.

<span id="_Toc141258406" class="anchor"></span>Figure 17: Pending Orders Manager "i" Button

![](ampl-frequently-asked-questions/020.png)

## What if I just want to go to an individual patient not on the Pending Orders Manager?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can locate and select individual patients from the VISTA Patient Lookup located in the upper left corner of your screen.

<span id="_Toc141258407" class="anchor"></span>Figure 18: Pending Order Manager VistA Patient Lookup

![](ampl-frequently-asked-questions/021.png)

## What is the “i” symbol next to VISTA Patient Lookup?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you click on the “i” next to VISTA Patient Lookup, it will display help text on different ways to search for the patient you need.

<span id="_Toc141258408" class="anchor"></span>Figure 19: VistA Patient Lookup Help Text

![](ampl-frequently-asked-questions/022.png)

# Patient Coversheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How do I view more detailed patient demographics?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click the down arrow to the left of More (below where the patient’s picture would be) to get more patient demographics.

<span id="_Toc141258409" class="anchor"></span>Figure 20: More Patient Demographics

![](ampl-frequently-asked-questions/023.png)

## How do I get more detailed Allergy/ADR information?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the allergen in the allergy summary ribbon, on the Allergies and ADRs tab or in the CWAD section.

<span id="_Toc141258410" class="anchor"></span>Figure 21: More Information for Allergies and ADRs

![](ampl-frequently-asked-questions/024.png)

## What is CWAD and how do I find that information?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CWAD is Crisis, Warnings, Allergies, and Directives found in the Postings button in the upper right corner. Click on this button, to see the CWAD entries for that patient. Hovering over the Postings button shows additional information.

<span id="_Toc141258411" class="anchor"></span>Figure 22: Postings CWAD Button

![](ampl-frequently-asked-questions/025.png)

## How do I see recent additions or changes to the patient's data from VistA or CPRS?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Like VistA and CPRS, new changes made to patient data after the patient’s record is accessed in AMPL (entering a new order, discontinuing an active order) are not seen until the patient is refreshed. See figure below:

- In AMPL, the Refresh button is used
- In CPRS, the File/Refresh Patient Information is used
- In VistA, close the patient in a backdoor pharmacy option and open the patient again.

<span id="_Toc141258412" class="anchor"></span>Figure 23: Refresh Patient Data

![](ampl-frequently-asked-questions/026.png)

## What is the number that I sometimes see next to the Tab Name?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A numeric value indicates the total number of Allergy and Adverse Reaction records for the selected patient and the “+" sign indicates that patient has "allergies/ADRs that were entered in error".

<span id="_Toc141258413" class="anchor"></span>Figure 24: Total Number of Allergy and Adverse Reactions

![](ampl-frequently-asked-questions/027.png)

## Is there a way to see allergies or ADRS that were “Entered in Error”?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes, click on the check box to the left of Show Entered in Error Records.

<span id="_Toc141258414" class="anchor"></span>Figure 25: Allergies Entered in Error

![](ampl-frequently-asked-questions/028.png)

## How do I know what facility entered the allergy/ADR?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility number where the allergy/ADR originated is in the last column to the right in the Allergies and ADRs tab.

<span id="_Toc141258415" class="anchor"></span>Figure 26: Originating Facility for Allergies and ADRs

![](ampl-frequently-asked-questions/029.png)

## Okay, but how do I know what facility corresponds to that facility number?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hover over the facility number and the facility name will appear.

<span id="_Toc141258416" class="anchor"></span>Figure 27: Hover for Facility Name

![](ampl-frequently-asked-questions/030.png)

## How do I find more information about column headers?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hover over the header and information about that header will appear.

<span id="_Toc141258417" class="anchor"></span>Figure 28: Hover Text for Column Headers

![](ampl-frequently-asked-questions/031.png)

## It would be nice to be able to graph vitals to see trends, can I do that with AMPL?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes, you can select date ranges, toggle between metric and US Standard units, and graph the vitals. The graph button is on the far right and next to it is the table button to return to table view.

<span id="_Toc141258418" class="anchor"></span>Figure 29: Graph Vitals

![](ampl-frequently-asked-questions/032.png)

## How many progress note titles are displayed per page? 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A maximum of 100 progress notes can be displayed per page. Additional notes may be viewed, 100 at a time, by clicking the Next button at the bottom of the page.

## How can I see a particular date range or an earlier date range than what is shown?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Query Editor can be used to filter and/or sort data for a date range. The Query Editor is opened by selecting the down arrow next to the Current Query button. Choose the Add Filter button to show filter options. Date/Time Entered is one of the options. See <u>Section 5: Filter and Sort</u> for more info on the Query Editor.

<span id="_Toc141258419" class="anchor"></span>Figure 30: Query Editor for Date Range

![](ampl-frequently-asked-questions/033.png)

## There are a lot of progress notes, how do I sort and filter them?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Progress Notes Tab, is a Current Query with a down arrow to the left of it. Select the down arrow to bring up the Sort and Filter options. Choose the Add Filter button to show filter options.

If Add Sort Field is selected, the same options appear, but will sort by those fields instead of filter.

Don’t forget to click Add after you make your selection (multiple filters and sort fields may be added at once). Execute the new filter and sort criteria by clicking on the Refresh button to the right of the page.

See <u>5.1.5: Progress Notes</u> for more info on sorting and filtering Progress Notes

<span id="_Toc141258420" class="anchor"></span>Figure 31: Progress Notes Sort and Filter

![](ampl-frequently-asked-questions/034.png)

## How do I see the actual progress note?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the note title to get a detailed view.

## How do I see Remote meds?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are remote meds, under the Med List Tab, there will be a circle with an “R” inside to the right of the column header. Click on that “R”.

> **NOTE:** There will be no “inpatient” remote medications.

<span id="_Toc141258421" class="anchor"></span>Figure 32: Remote Meds

![](ampl-frequently-asked-questions/035.png)

## How do I see a more detailed view of the meds?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on More to the right of the header. This will give more information about all the meds in that section.

<span id="_Toc141258422" class="anchor"></span>Figure 33: Detailed View of Meds

![](ampl-frequently-asked-questions/036.png)

## Okay, but how do I see an even MORE detailed view of the medication orders?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the medication name in the section and it will give you a detailed view of the medication order.

<span id="_Toc141258423" class="anchor"></span>Figure 34: Even More Detailed View of Medication Order

![](ampl-frequently-asked-questions/037.png)

## I see buttons at the bottom of that view, what are those for?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A screenshot of those buttons is below. They include Order Checks, Drug Restrictions/Guidelines, Drug Info, Provider Info, PADE Inventory Activity, Admin Hx, and Close. These buttons put often needed information that you can find in VistA and CPRS, but in a much easier to find and read format for each order. If the button is greyed out, there is no information for that item.

<span id="_Toc141258424" class="anchor"></span>Figure 35: Order Checks, Drug Restrictions/Guidelines, Drug Info, Provider Info, PADE Inventory Activity, Admin Hx, and Close

![](ampl-frequently-asked-questions/038.png)

## For Inpatient and Clinical Med Orders, can I see PADE inventory amounts for the associated device?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes, click on the PADE Inventory Activity button at the bottom of the screen when in a medications detailed view.

<span id="_Toc141258425" class="anchor"></span>Figure 36: PADE Inventory Activity

![](ampl-frequently-asked-questions/039.png)

# Filter and Sort

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Can I get more information on sort and filter functionality for Allergies and ADRs, Labs, Consults, Progress Notes, Immunizations, Problem List, and Appointments tabs?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each tab has its own unique filter and sort criteria to easily filter and sort to find the information you need quickly and efficiently.

There are several things to remember. After selecting the filter or sort, don’t forget to click the Add button to add your new criteria to the filter or sort section above the options. You can add multiple filter or sort criteria if needed. Once you have your filter and sort criteria finished, click the Refresh button to the right side of the screen. Below the Refresh button is a Reset button to return to the default search and sort settings.

Listed below are figures and information for each tab to show what types of data may be used to filter or sort data.

### Meds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Starting out with an exception, the Med List tab doesn’t currently include a Query Editor. Instead, it displays all Active/Recently Expired, Pending and Non-Verified orders. Remote Outpatient, Clinic and Non-VA orders may be added by checking the R button in the section header.

<span id="_Toc141258426" class="anchor"></span>Figure 37: Remote Order Button

![](ampl-frequently-asked-questions/040.png)

An expanded view for orders in a category may be accessed by clicking the More button for that category. Additional details for a specific order are displayed by clicking on the order from the Expanded View.

<span id="_Toc141258427" class="anchor"></span>Figure 38: More Button

![](ampl-frequently-asked-questions/041.png)

> **NOTE:** The Outpatient medications included in the discontinued and expired categories are determined by RECENTLY DC’D/EXPIRED DAYS Field (#3.2) in the OUTPATIENT SITE (#59) File. Inpatient Medication Order include orders that were discontinued or expired in the last 24 hours in the RECENTLY DC’D/EXPIRED section.

For more FAQs about the Meds tab, see <u>Section 4.14</u> of this document.

### Allergies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Allergies/ADRs and Assessments are displayed for all sites where a patient has been seen. Records may be further filtered or sorted using the Query Editor. It is accessed by clicking on the down arrow next to the Current Query.

<span id="_Toc141258428" class="anchor"></span>Figure 39: Current Query

![](ampl-frequently-asked-questions/042.png)

After adding new filter or sort criteria, don’t forget to click the Add button to add your new criteria to the Filters or Sort sections above the options. You may add multiple filter or sort criteria. Once you have completed filter and sort criteria changes, click the Refresh button to the right side of the screen. Below the Refresh button is a Reset button to return to the default search and sort settings.

<span id="_Toc141258429" class="anchor"></span>Figure 40: Allergies Filtering and Sorting

![](ampl-frequently-asked-questions/043.png)

Adding Filter Criteria:

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators’ changes based on the type of data selected in the filter field.

<span id="_Toc141258430" class="anchor"></span>Figure 41: Allergies Adding Filter Criteria

![](ampl-frequently-asked-questions/044.png)

<span id="_Toc141258431" class="anchor"></span>Figure 42: Allergies Adding Filter

![](ampl-frequently-asked-questions/045.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars or select from common date ranges by clicking on the down arrows to the left of the date/time as shown below:

<span id="_Toc141258432" class="anchor"></span>Figure 43: Allergies Date Range Filter

![](ampl-frequently-asked-questions/046.png)

If a text field is selected, the Filter Text box turns into a Select a Value drop down that includes only values included in the patient’s data. In the example below for causative agent, the possible options are displayed and as many or few as you like can be checked.

<span id="_Toc141258433" class="anchor"></span>Figure 44: Allergies Selecting a Value

![](ampl-frequently-asked-questions/047.png)

Adding Sort Criteria:

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc141258434" class="anchor"></span>Figure 45: Allergies Adding Sort Field

![](ampl-frequently-asked-questions/048.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for both filter and Sort sections, located on the right side of the section.

<span id="_Toc141258435" class="anchor"></span>Figure 46: Allergies New Filter Add Button

![](ampl-frequently-asked-questions/049.png)

The Refresh and Reset buttons are in the Execute section on the right of the Query Editor. Refresh will apply any new filters. Reset will return the display to the default criteria.

<span id="_Toc141258436" class="anchor"></span>Figure 47: Allergies Refresh Button

![](ampl-frequently-asked-questions/050.png)

To remove single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc141258437" class="anchor"></span>Figure 48: Allergies Red "X" Button

![](ampl-frequently-asked-questions/051.png)

To clear all filters and sorts added by the user and return to the tab’s default, click the Reset button.

<span id="_Toc141258438" class="anchor"></span>Figure 49: Allergies Reset Button

![](ampl-frequently-asked-questions/052.png)

### Vitals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals is the second tab that does not include a query editor. Instead, the vitals tab initially displays a table of the latest common vitals. You can view past readings by clicking on the vital name, results will display to the right with a default date range of one year for Outpatient and one week for Inpatient. Additional Vitals may be added to the table by clicking on the Vital name. They can be removed by clicking again.

<span id="_Toc141258439" class="anchor"></span>Figure 50: Vitals Display

![](ampl-frequently-asked-questions/053.png)

To change the date range, modify the Readings from or through dates.

<span id="_Toc141258440" class="anchor"></span>Figure 51: Vitals Date Range

![](ampl-frequently-asked-questions/054.png)

There are several ways to enter dates - typing the date, clicking on the calendars or select from common date ranges by clicking on the down arrows to the left of the date/time as shown below.

<span id="_Toc141258441" class="anchor"></span>Figure 52: Vitals Commonly Used Date Ranges

![](ampl-frequently-asked-questions/055.png)

Vital types in the date range table may also be shown in a graph by selecting the graphing icon located in the top right corner of the Vitals screen.

<span id="_Toc141258442" class="anchor"></span>Figure 53: Vitals Graphing

![](ampl-frequently-asked-questions/056.png)

### Labs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Current Query default for Labs is Collection Date/Time within the past year, sorted by Collection Date/Time with newest results first, and 100 records per page. The Filter and sort criteria can be changed using the Query Editor. The Query Editor is accessed by clicking the blue down arrow.

<span id="_Toc141258443" class="anchor"></span>Figure 54: Labs Current Query

![](ampl-frequently-asked-questions/057.png)

Adding Filter Criteria:

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators’ changes based on the type of data selected in the filter field.

<span id="_Toc141258444" class="anchor"></span>Figure 55: Labs Select Filter Field

![](ampl-frequently-asked-questions/058.png)

<span id="_Toc141258445" class="anchor"></span>Figure 56: Labs Filter Contains Field

![](ampl-frequently-asked-questions/059.png)

For efficiency, the Filter Text box turns into a Select a Value drop down with options specific to the patient’s data.

<span id="_Toc141258446" class="anchor"></span>Figure 57: Labs Filter Contains Field

![](ampl-frequently-asked-questions/060.png)

<span id="_Toc141258447" class="anchor"></span>Figure 58: Labs Selecting a Value

![](ampl-frequently-asked-questions/061.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc141258448" class="anchor"></span>Figure 59: Labs Selecting a Date Range

![](ampl-frequently-asked-questions/062.png)

Adding Sort Criteria:

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc141258449" class="anchor"></span>Figure 60: Labs Adding Sort Criteria

![](ampl-frequently-asked-questions/063.png)

By selecting Results per Page, you can decrease the number of results per page as below, the default is 100.

<span id="_Toc141258450" class="anchor"></span>Figure 61: Labs Results Per Page

![](ampl-frequently-asked-questions/064.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located in the right side of the section.

<span id="_Toc141258451" class="anchor"></span>Figure 62: Labs Add Button for Sort criteria

![](ampl-frequently-asked-questions/065.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc141258452" class="anchor"></span>Figure 63: Labs Refresh Button

![](ampl-frequently-asked-questions/066.png)

To remove single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc141258453" class="anchor"></span>Figure 64: Labs Red "X" Buttons

![](ampl-frequently-asked-questions/067.png)

To clear all filters and sorts added by the user and return to the tab’s default, click the Reset button.

<span id="_Toc141258454" class="anchor"></span>Figure 65: Labs Reset Button

![](ampl-frequently-asked-questions/068.png)

### Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default filter/sort criteria for Progress Notes is: Records within the last year, sorted by Date/Time Entered with most recent notes first, 100 results per page. These criteria may be changed using the Query Editor by clicking on the blue drop-down arrow to the left of the Current Query.

<span id="_Toc141258455" class="anchor"></span>Figure 66: Progress Notes Current Query

![](ampl-frequently-asked-questions/069.png)

Adding Filter Criteria:

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators’ changes based on the type of data selected in the filter field. 

<span id="_Toc141258456" class="anchor"></span>Figure 67: Progress Notes Select Filter Field

![](ampl-frequently-asked-questions/070.png)

<span id="_Toc141258457" class="anchor"></span>Figure 68: Progress Notes Add Filter Contains

![](ampl-frequently-asked-questions/071.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc141258458" class="anchor"></span>Figure 69: Progress Notes Add Filter

![](ampl-frequently-asked-questions/072.png)

Adding Sort Criteria:

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc141258459" class="anchor"></span>Figure 70:Progress Notes Add Sort Field

![](ampl-frequently-asked-questions/073.png)

Selecting Results per Page. You can decrease the number of results per page as below, the default is 100.

<span id="_Toc141258460" class="anchor"></span>Figure 71: Progress Notes Results Per Page

![](ampl-frequently-asked-questions/074.png)

As each filter or sort is defined, click the Add button to add it to the query. There is an Add button for each section, located in the right side of the section.

<span id="_Toc141258461" class="anchor"></span>Figure 72: Progress Notes Add Buttons

![](ampl-frequently-asked-questions/075.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc141258462" class="anchor"></span>Figure 73: Refresh Button

![](ampl-frequently-asked-questions/076.png)

To remove single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc141258463" class="anchor"></span>Figure 74: Remove single criteria Notes tab

![](ampl-frequently-asked-questions/077.png)

To clear all filters and sorts added by the user and return to the tab’s default, clickthe Reset button.

<span id="_Toc141258464" class="anchor"></span>Figure 75: Reset button for Notes

![](ampl-frequently-asked-questions/078.png)

### Consults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default display for the Consults tab is All Records, sorted by Date/Time descending, 100 results/page. The filter and sort criteria maybe changed using the Query Editor.

<span id="_Toc141258465" class="anchor"></span>Figure 76: Consults current query

![](ampl-frequently-asked-questions/079.png)

Adding Filter Criteria:

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators’ changes based on the type of data selected in the filter field. 

<span id="_Toc141258466" class="anchor"></span>Figure 77:Consults Select Filter Field

![](ampl-frequently-asked-questions/080.png)

<span id="_Toc141258467" class="anchor"></span>Figure 78:Consults Filter Contains

![](ampl-frequently-asked-questions/081.png)

To make it easy to add filters, the Filter Text box turns into a Select a Value drop down with options specific to the patient’s data.

<span id="_Toc141258468" class="anchor"></span>Figure 79:Consults Selecting a Value

![](ampl-frequently-asked-questions/082.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc141258469" class="anchor"></span>Figure 80: Consult Date/time filter

![](ampl-frequently-asked-questions/083.png)

Adding Sort Criteria:

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc141258470" class="anchor"></span>Figure 81: Consults Add Sort Field

![](ampl-frequently-asked-questions/084.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located in the right side of the section.

<span id="_Toc141258471" class="anchor"></span>Figure 82: Consults New Filter Add button

![](ampl-frequently-asked-questions/085.png)

Selecting Results per Page. You can decrease the number of results per page as shown below, the default is 100.

<span id="_Toc141258472" class="anchor"></span>Figure 83: Consults Results Per Page

![](ampl-frequently-asked-questions/086.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc141258473" class="anchor"></span>Figure 84: Refresh/Reset Buttons

![](ampl-frequently-asked-questions/087.png)

To remove single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc141258474" class="anchor"></span>Figure 85: Consult Remove Single Criteria

![](ampl-frequently-asked-questions/088.png)

To clear all filters and sorts added by the user and return to the tab’s default, clickthe Reset button.

<span id="_Toc141258475" class="anchor"></span>Figure 86: Consult Reset Button

![](ampl-frequently-asked-questions/089.png)

### Problem List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default view for the Problem List tab is all active problems sorted by Immediacy (Acute, Chronic or Unknown) in alphabetical order, then by Description in Alphabetical order.

<span id="_Toc141258476" class="anchor"></span>Figure 87: Problem List Current Query

![](ampl-frequently-asked-questions/090.png)

Adding Filter Criteria:

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators’ changes based on the type of data selected in the filter field. 

<span id="_Toc141258477" class="anchor"></span>Figure 88: Problem List Select Filter Field

![](ampl-frequently-asked-questions/091.png)

<span id="_Toc141258478" class="anchor"></span>Figure 89: Problem List Add Filter Operators

![](ampl-frequently-asked-questions/092.png)

To make it easy to add filters, the Filter Text box turns into a Select a Value drop down with values specific to the patient’s data.

<span id="_Toc141258479" class="anchor"></span>Figure 90: Problem List Selecting a Value

![](ampl-frequently-asked-questions/093.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc141258480" class="anchor"></span>Figure 91: Problem List Add Date Range Filter

![](ampl-frequently-asked-questions/094.png)

Adding Sort Criteria:

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc141258481" class="anchor"></span>Figure 92: Problem List Adding Sort Field

![](ampl-frequently-asked-questions/095.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located in the right side of the section. 

<span id="_Toc141258482" class="anchor"></span>Figure 93: Problem List Add Buttons

![](ampl-frequently-asked-questions/096.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc141258483" class="anchor"></span>Figure 94: Problem List Refresh Button

![](ampl-frequently-asked-questions/097.png)

To remove single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc141258484" class="anchor"></span>Figure 95: Problem List Remove single Filter or Sort

![](ampl-frequently-asked-questions/098.png)

To clear all filters and sorts added by the user and return to the tab’s default, clickthe Reset button.

<span id="_Toc141258485" class="anchor"></span>Figure 96: Problem List Reset button

![](ampl-frequently-asked-questions/099.png)

### Immunizations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default view for the Immunizations tab is All Records, sorted by Name (of immunization), most recent record first. The filter and sort criteria may be changed using the Query Editor. It is access by be clicking on the blue down-arrow next to the Current Query.

<span id="_Toc141258486" class="anchor"></span>Figure 97: Immunizations Current Query

![](ampl-frequently-asked-questions/100.png)

Adding Filter Criteria:

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators’ changes based on the type of data selected in the filter field. 

<span id="_Toc141258487" class="anchor"></span>Figure 98: Immunizations Select Filter Field

![](ampl-frequently-asked-questions/101.png)

<span id="_Toc141258488" class="anchor"></span>Figure 99: Immunizations Add Filter Operators

![](ampl-frequently-asked-questions/102.png)

To make it easy to add filters, the Filter Text box turns into a Select a Value drop down with options specific to the patient’s data.

<span id="_Toc141258489" class="anchor"></span>Figure 100: Immunizations Selecting a Value

![](ampl-frequently-asked-questions/103.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc141258490" class="anchor"></span>Figure 101: Immunization Date Filter

![](ampl-frequently-asked-questions/104.png)

Adding Sort Criteria:

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc141258491" class="anchor"></span>Figure 102: Immunizations Adding Sort Criteria

![](ampl-frequently-asked-questions/105.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located on the right side of the section.

<span id="_Toc141258492" class="anchor"></span>Figure 103: Immunizations Add Buttons

![](ampl-frequently-asked-questions/106.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc141258493" class="anchor"></span>Figure 104: Immunizations Refresh Button

![](ampl-frequently-asked-questions/107.png)

To remove single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc141258494" class="anchor"></span>Figure 105: Immunization Remove Single Criteria

![](ampl-frequently-asked-questions/108.png)

To clear all filters and sorts added by the user and return to the tab’s default, clickthe Reset button.

<span id="_Toc141258495" class="anchor"></span>Figure 106: Immunization Reset button

![](ampl-frequently-asked-questions/109.png)

### Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default display for the Appointments tab is Records within the last year, sorted by Date/Time descending, 100 results/page. The filter and sort criteria may be changed using the Query Editor. It is access by be clicking on the blue down-arrow next to the Current Query.

<span id="_Toc141258496" class="anchor"></span>Figure 107: Appointments Current Query

![](ampl-frequently-asked-questions/110.png)

Adding Filter Criteria:

The drop-down list of Filter Fields displays a list of fields that can be used to restrict the list. The list of operators’ changes based on the type of data selected in the filter field.

<span id="_Toc141258497" class="anchor"></span>Figure 108: Appointments Select Filter Field

![](ampl-frequently-asked-questions/111.png)

<span id="_Toc141258498" class="anchor"></span>Figure 109: Appointments Add Filter Operators

![](ampl-frequently-asked-questions/112.png)

To make it easy to add filters, the Filter Text box turns into a Select a Value drop down with options specific to the patient’s data.

<span id="_Toc141258499" class="anchor"></span>Figure 110: Appointments Filter

![](ampl-frequently-asked-questions/113.png)

If the filter is a date range, there are several ways to enter dates - typing the date, clicking on the calendars, or clicking on the down arrows to the left of the date/time box which displays common date ranges as shown below:

<span id="_Toc141258500" class="anchor"></span>Figure 111: Appointments Date Filter

![](ampl-frequently-asked-questions/114.png)

Adding Sort Criteria:

Setting Sort criteria is like setting filter criteria. A dropdown box shows the fields that can be used for sorting.

<span id="_Toc141258501" class="anchor"></span>Figure 112: Appointments Add Sort Criteria

![](ampl-frequently-asked-questions/115.png)

Selecting Results per Page. You can decrease the number of results per page as below, the default is 100.

<span id="_Toc141258502" class="anchor"></span>Figure 113: Appointments Results Per Page

![](ampl-frequently-asked-questions/116.png)

As each filter or sort is defined, click the Add button to add it to the query.

There is an Add button for each section, located in the right side of the section. 

<span id="_Toc141258503" class="anchor"></span>Figure 114: Appointments Add Buttons

![](ampl-frequently-asked-questions/117.png)

To process the list with your new criteria, click the Refresh button.

<span id="_Toc141258504" class="anchor"></span>Figure 115: Appointments Refresh Button

![](ampl-frequently-asked-questions/118.png)

To remove single filter or sort criteria, including one of the defaults, click the Red X next to it.

<span id="_Toc141258505" class="anchor"></span>Figure 116: Appointments Remove Single Criteria

![](ampl-frequently-asked-questions/119.png)

To clear all filters and sorts added by the user and return to the tab’s default, clickthe Reset button.

<span id="_Toc141258506" class="anchor"></span>Figure 117: Appointments Reset Button

![](ampl-frequently-asked-questions/120.png)