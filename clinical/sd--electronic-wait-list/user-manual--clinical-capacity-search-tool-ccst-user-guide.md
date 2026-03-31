---
title: Clinical Capacity Search Tool (CCST) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Clinical Capacity Search Tool (CCST)
app_code: SD
app_name: Scheduling
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: The Clinical Capacity Search Tool (CCST) is an internal web application that was developed to assist the Department of Veteran Affairs (VA) staff in finding available appointment slots across multiple VA facilities. The purpose of CCST is to deliver users with the functionality to find virtual avail
audience: 
keywords: 
  - figure
  - span
  - search
  - table
  - available
  - class
  - anchor
  - contents
  - site
  - button
page_count: 0
word_count: 4869
section_count: 17
table_count: 2
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2026
revision_count: 13
revision_newest: 7/18/2025
revision_oldest: 1/11/2024
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/ccst_release_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/ccst_release_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=100"
---

OFFICE OF  
INFORMATION  
AND TECHNOLOGY

Clinical Capacity Search Tool  
User Guide

*Version 2.6.0* \| January 2026
## List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[*Table 1: Search Criteria for Filtering* [32](#_Ref179290059)](#_Ref179290059)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date       | Version | Description                                                                                                                                                                                                                      | Author              |
|------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| 1/7/2025   | 2.6.0   | Updated screenshots for UI changes, updated format of document                                                                                                                                                                   | Booz Allen Hamilton |
| 7/18/2025  | 1.2     | New baseline for Section 5.                                                                                                                                                                                                      | Booz Allen Hamilton |
| 6/16/2025  | 1.1     | New baseline for Sections 2, 3 and 4. Added Sections 5 and 6 to provide information about the Utilization Report and Preferences web pages, respectively.                                                                        | Booz Allen Hamilton |
| 3/6/2025   | 1.0     | Updated images in Sections 3 and 4, which reflect UI changes made to CCST since November 2024. Added information about the collapse/expand function for the Start New Search panel in Section 3.2. New baseline for Section 4.2. | Liberty ITS         |
| 11/18/2024 | 0.9     | New baseline for Sections 1.1 and 1.2. Replaced Change Site modal screenshots in Section 2. Added information about the partial results alert to Section 3.                                                                      | Liberty ITS         |
| 10/22/2024 | 0.8     | New baseline for entire document.                                                                                                                                                                                                | Liberty ITS         |
| 3/26/2024  | 0.7     | New baseline for page 15.                                                                                                                                                                                                        | Liberty ITS         |
| 3/25/2024  | 0.6     | Replaced all screenshots with the Show/Hide Column icon and Move icon. New baseline for Section 3 and 4.                                                                                                                         | Liberty ITS         |
| 3/19/2024  | 0.5     | Removed instructions for the Move and Show/Hide Column functionality.                                                                                                                                                            | Liberty ITS         |
| 3/13/2024  | 0.4     | Watermark “DRAFT” removed.                                                                                                                                                                                                       | Liberty ITS         |
| 2/26/2024  | 0.3     | New baseline for Section 3, Searching for Available Appointments.                                                                                                                                                                | Liberty ITS         |
| 2/14/2024  | 0.2     | Modifications made throughout document based on business owner feedback.                                                                                                                                                         | Liberty ITS         |
| 1/11/2024  | 0.1     | Draft.                                                                                                                                                                                                                           | Liberty ITS         |

## # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Capacity Search Tool (CCST) is an internal web application that was developed to assist the Department of Veteran Affairs (VA) staff in finding available appointment slots across multiple VA facilities. The purpose of CCST is to deliver users with the functionality to find virtual available appointment slots based on existing clinical agreements and the ability to find in-person available appointment slots. With this document, users can familiarize themselves with important features and navigational elements of CCST, such as searching for available appointments and how to use the utilization report. This document is intended for CCST users supporting the Veterans Health Administration (VHA).

## Prerequisite Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- To view in-person available appointments, one of three types of scheduler keys (i.e., SDECVIEW, SDECZMENU and SDECZMGR) must be in place for the user. For users from a CRH, a scheduler key request is made through VA’s [<u>LEAF</u>](https://leaf.va.gov/launchpad/) system. Users associated with a particular VAMC must contact their automated data processing applications coordinator about acquiring a scheduler key.
- The user’s PIV card must be linked to a VistA site (see [<u>link</u>](https://yourit.va.gov/va?sys_kb_id=209819ab9774c6980a27f1ece053af81&id=kb_article_view&sysparm_rank=2&sysparm_tsqueryId=d20aa78c1b2cde9434050f6fe54bcbf5) for guidance); additionally, viewing data on virtual available appointments requires the Telehealth Management Program to have scheduling packages in place.

## PIV Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Begin by opening a browser and entering the following web address in the browser’s address bar: [<u>https://staff.apps.va.gov/ccst/</u>](https://staff.apps.va.gov/ccst/). The VA Single Sign-On page will then appear. Select the PIV card image, as seen in [⁠⁠Figure 1⁠⁠](\l) to proceed with the log in process.

> ![](clinical-capacity-search-tool-ccst-user-guide/001.png)

<span id="_Toc219299243" class="anchor"></span>Figure 1: PIV Card Sign-In Image

2.  After selecting the PIV card image, a dialog box will appear prompting the user to select a certificate for authentication (see [⁠⁠Figure 2⁠⁠](\l)).

> ![](clinical-capacity-search-tool-ccst-user-guide/002.png)

<span id="_Toc219299244" class="anchor"></span>Figure 2: Certificate for Authentication Dialog Box

- Note: Signing in to CCST may vary depending on when security time outs occur. This may mean selecting a certificate for authentication and/or entering a PIN may not be necessary.
3.  After finalizing your certificate selection, an ActivClient Login dialog box will appear prompting the user to enter their PIN number (see [⁠⁠Figure 3⁠⁠](\l) for an example). If authentication is successful, CCST will load. If authentication is not successful, you will be prompted to enter your correct PIN instead.

> ![](clinical-capacity-search-tool-ccst-user-guide/003.png)

<span id="_Toc219299245" class="anchor"></span>Figure 3: ActivClient Login Pop-Up Window with PIN Entry

# Familiarizing Yourself with CCST


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [List of Figures](#list-of-figures)
  - [List of Tables](#list-of-tables)
  - [Revision History](#revision-history)
  - [# Introduction](#introduction)
  - [Overview](#overview)
  - [Prerequisite Credentials](#prerequisite-credentials)
  - [PIV Login](#piv-login)
- [Familiarizing Yourself with CCST](#familiarizing-yourself-with-ccst)
  - [Home Page](#home-page)
    - [Changing Site Location](#changing-site-location)
    - [Additional Links](#additional-links)
  - [My Account](#my-account)
    - [User Preferences](#user-preferences)
    - [Signing Out of CCST](#signing-out-of-ccst)
- [Searching for Available Appointments](#searching-for-available-appointments)
  - [Start New Search](#start-new-search)
  - [Available Appointments](#available-appointments)
- [Filtering and Column Actions](#filtering-and-column-actions)
  - [Sort by Ascending and Descending Order](#sort-by-ascending-and-descending-order)
  - [Toggle Density](#toggle-density)
  - [Filters](#filters)
  - [Search Function](#search-function)
- [Utilization Report](#utilization-report)
  - [Obtaining Data on CCST Usage](#obtaining-data-on-ccst-usage)

## Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once log in is complete, users will see the CCST website with top and bottom headers as seen in [⁠⁠Figure 4⁠⁠](\l).

![](clinical-capacity-search-tool-ccst-user-guide/004.png)

<span id="_Toc219299246" class="anchor"></span>Figure 4: CCST Webpage

### Changing Site Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To change site locations, the user must first select the site location dropdown in the upper right-hand corner of the page as shown in [⁠⁠Figure 5⁠⁠](\l).

> ![](clinical-capacity-search-tool-ccst-user-guide/005.png)

<span id="_Toc219299247" class="anchor"></span>Figure 5: Site Locations Dropdown

2.  The user will then need to select the desired site location by clicking on the arrow shown in <span id="_Ref179288636" class="anchor"></span>[⁠⁠Figure 6⁠⁠](\l).

> ![](clinical-capacity-search-tool-ccst-user-guide/006.png)

<span id="_Toc219299248" class="anchor"></span>Figure 6: Change Site Location Modal

- Note: The user can also change the patient sites via the “Recent Sites” dropdown seen in [⁠⁠Figure 7⁠⁠](\l). Using this option will only show the 10 most recently selected sites by the user and not the full set of options available from the Change Site modal shown in [⁠⁠Figure 6⁠⁠](#_Ref179288636).

> ![](clinical-capacity-search-tool-ccst-user-guide/007.png)

> <span id="_Toc219299249" class="anchor"></span>Figure 7: Recent Sites Button

3.  From the Change Site modal, the user can view a list of one or more medical centers and their divisions (e.g., clinics) in the same catchment area after selecting the dropdown arrow as seen in [⁠⁠Figure 8⁠⁠](\l).
- Note: A division will render the same search results as their parent VA medical center.

> ![](clinical-capacity-search-tool-ccst-user-guide/008.png)

> <span id="_Toc219299250" class="anchor"></span>Figure 8: Show Site Locations

- Note: Users may choose to type the name of the site location needed, instead of manually scrolling through the Change Site modal dropdown (see [⁠⁠Figure 9⁠⁠](\l) for example).

> ![](clinical-capacity-search-tool-ccst-user-guide/009.png)

> <span id="_Toc219299251" class="anchor"></span>Figure 9: Text Entry in Select Site Location Input Field

4.  Simply click on the “Select” button, shown in <span id="_Ref179288847" class="anchor"></span>[⁠⁠Figure 10⁠⁠](\l), to finalize the selection of a site location.

> ![](clinical-capacity-search-tool-ccst-user-guide/010.png)

<span id="_Toc219299252" class="anchor"></span>Figure 10: Select Button for Change Site Location Modal

- Note: Instead of using the “Select” button to change the site location, the user can click on the “Close” button shown in Figure 11 at any time to collapse the Change Site modal and continue with the previously selected location.

> ![](clinical-capacity-search-tool-ccst-user-guide/011.png)

> <span id="_Ref219286758" class="anchor"></span>Figure 11: Close Button for the Change Site Modal

5.  Once a site location is chosen, the site selection will continue to persist in future uses of CCST as part of the criteria used to search for available appointment time slots. The name of the selected site location will appear next to the Change Site dropdown arrow, replacing the name of the previous selection (see [⁠⁠Figure 10⁠⁠](#_Ref179288847) and Figure 12 comparatively).

> ![](clinical-capacity-search-tool-ccst-user-guide/012.png)

<span id="_Ref219286928" class="anchor"></span>Figure 12: Example of New Site Location Name

- Note: Site selections will continue to persist except under the conditions of making a new site selection, changing computers, or clearing the browser history.
- Note: The new site location selection will also appear in the Start New Search panel on the Availability Search page and automatically populated in the “Select Site Location(s)” dropdown on the Utilization Report page (see Figure 13 and Figure 14 for example).

> ![](clinical-capacity-search-tool-ccst-user-guide/013.png)

> <span id="_Ref219286980" class="anchor"></span>Figure 13: New Selected Site Location Displayed in the Start New Search Panel

> ![](clinical-capacity-search-tool-ccst-user-guide/014.png)

> <span id="_Ref219286998" class="anchor"></span>Figure 14: Auto-population of Selected Site Location in Utilization Report

<span id="_Toc157176282" class="anchor"></span>

### Additional Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are links to additional information located at the bottom of the CCST page. See Figure 15 below for reference.

![](clinical-capacity-search-tool-ccst-user-guide/015.png)

<span id="_Ref219287036" class="anchor"></span>Figure 15: Additional Links

## My Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To change user preferences, the user can select the “My Account” button in the upper right-hand corner, seen in Figure 16, to open the dropdown.

> ![](clinical-capacity-search-tool-ccst-user-guide/016.png)

<span id="_Ref219287059" class="anchor"></span>Figure 16: My Account Button for Preferences

2.  The user can then select the “Preferences” button, seen in Figure 17, to be taken to the User Preferences page.

> ![](clinical-capacity-search-tool-ccst-user-guide/017.png)

<span id="_Ref219287082" class="anchor"></span>Figure 17: Preferences Button

3.  After navigating to the User Preferences page, the user will see sections for Virtual Available Appointments, In-Person Available Appointments, and the Utilization Report that contain a list of column names to be adjusted for the specified table. To adjust the default order of the column names within the sections, left-click and hold to drag and drop the different selections as seen in Figure 18 below.

> ![](clinical-capacity-search-tool-ccst-user-guide/018.png)

<span id="_Ref219287112" class="anchor"></span>Figure 18: Drag and Drop Example for Column Order

4.  The user can then select the “Save” button seen in Figure 19 to save their changes.

> ![](clinical-capacity-search-tool-ccst-user-guide/019.png)

<span id="_Ref219287137" class="anchor"></span>Figure 19: Save Button for Column Order

- Note: Users will see the adjustments to column order in the respective tables located throughout CCST (see Figure 20 for example).

> ![](clinical-capacity-search-tool-ccst-user-guide/020.png)

> <span id="_Ref219287166" class="anchor"></span>Figure 20: Modification of Tables within CCST

5.  Once the “Save” button is selected, a save notification will appear and only the “Reset to Default” button will remain active (see Figure 21 below). The user will need to close the “Preferences Saved!” notification by selecting the “x” button to close it manually. Users will not be able to leave the User Preferences page until the notification is closed.

> ![](clinical-capacity-search-tool-ccst-user-guide/021.png)

<span id="_Ref219287197" class="anchor"></span>Figure 21: Preferences Saved Notification

6.  To restore the columns to default order for any section, select the “Reset to Default” button seen in Figure 22. Once selected, the “Reset Successful!” notification will appear and the columns will have returned to the default order (see Figure 23[\_Ref200627206](\l)).

> ![](clinical-capacity-search-tool-ccst-user-guide/022.png)

<span id="_Ref219287241" class="anchor"></span>Figure 22: Reset to Default Button for Column Order

- Note: To close the “Reset Successful” notification, the user must manually close the notification by selecting the “x” button seen in Figure 23. Users will not be able to leave the User Preferences page until the notification is closed.

> ![](clinical-capacity-search-tool-ccst-user-guide/023.png)

> <span id="_Ref219287282" class="anchor"></span>Figure 23: Reset to Default Notification

### Signing Out of CCST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To log off when you are finished using CCST, click Log Out after selecting the My Account icon in the upper right-hand corner of CCST (see Figure 24).

> ![](clinical-capacity-search-tool-ccst-user-guide/024.png)

<span id="_Ref219287362" class="anchor"></span>Figure 24: Log Out Button

2.  The user will be taken to the page seen in Figure 25 upon signing out, which prompts them to log out of SSOi and close the browser.

> ![](clinical-capacity-search-tool-ccst-user-guide/025.png)

<span id="_Ref219287392" class="anchor"></span>Figure 25: Log Out Page for CCST

- Note: The user will automatically be logged out and taken to the page shown in Figure 25 after one hour if logged in but not actively using CCST.

# Searching for Available Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Start New Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  After confirming the correct site location has been chosen, select one of three types of appointments: Virtual, In-Person, or Both by clicking on the appropriate radio button to establish the kind of clinical encounter desired as a criterion for performing a search on available appointments (located in the left panel) as shown in ⁠[⁠](\l)⁠Figure 26.
- Note: By default, the Virtual radio button is selected.

> ![](clinical-capacity-search-tool-ccst-user-guide/026.png)

> <span id="_Ref219287580" class="anchor"></span>Figure 26: Clinical Service Search Field

- *Note: If either “In-Person” or “Both” radio buttons are selected, the Search Radius field shown in Figure 27 will appear. Users will be required to choose a distance of 10 to 250 miles by either dragging the slider to the correct distance. The starting point for the distance is based on the zip code of the patient site selected by the user in [⁠⁠2.1 Changing Site Location⁠⁠](#changing-site-location). When running queries using the “Both” Appointment Type, the distance selected for Search Radius will only impact in-person search results.*

> ![](clinical-capacity-search-tool-ccst-user-guide/027.png)

> <span id="_Ref219296782" class="anchor"></span>Figure 27: Search Radius for In-Person Appointment Types

2.  In the Clinical Service input field, the user will need to either open the dropdown and search from the list provided or manually type the specific health care needed by the patient into the search field. When typing into the search field, CCST will list any clinical services matching the letters entered by the user in the input field via the dropdown list as shown in Figure 28.

> ![](clinical-capacity-search-tool-ccst-user-guide/028.png)

> <span id="_Ref219290308" class="anchor"></span>Figure 28: Clinical Service Search with Characters

- Note: The user can also pull up the exact clinical service needed by typing in a stop code. For instance, typing “323” into the Clinical Service input field will prompt CCST to list only PRIMARY CARE/MEDICINE as a selectable option.
3.  The user will then need to select the preferred option from the dropdown list to populate the clinical service input field (see Figure 29).

> ![](clinical-capacity-search-tool-ccst-user-guide/029.png)

<span id="_Ref219290696" class="anchor"></span>Figure 29: Populated Clinical Service

4.  To specify a date range as part of the criteria used to search for available appointments, the user will first select the left-hand input field for the Date Criteria as shown in Figure 30.

> ![](clinical-capacity-search-tool-ccst-user-guide/030.png)

<span id="_Ref219290751" class="anchor"></span>Figure 30: Start Date for Date Range

5.  The user will then be able to select the start date for the date range by either navigating the calendar and selecting the desired date, as seen in Figure 31, or manually typing it in the MM/DD/YYYY format and pressing the Enter key on the keyboard.

> ![](clinical-capacity-search-tool-ccst-user-guide/031.png)

<span id="_Ref219290812" class="anchor"></span>Figure 31: Start Date Calendar View

6.  Next, the user will select the right-hand input field for the Date Criteria as shown in Figure 32.

> ![](clinical-capacity-search-tool-ccst-user-guide/032.png)

<span id="_Ref219290833" class="anchor"></span>Figure 32: End Date for Date Range

7.  The user will then be able to select the end date by either navigating the calendar and selecting the desired end date as shown in Figure 33, or manually typing it in the MM/DD/YYYY format and pressing the Enter key on the keyboard.

> ![](clinical-capacity-search-tool-ccst-user-guide/033.png)

<span id="_Ref219290870" class="anchor"></span>Figure 33: End Date Calendar View

- Note: The start date defaults to today’s date and the end date defaults to 1 week from the start date (see Figure 34 for an example).

> ![](clinical-capacity-search-tool-ccst-user-guide/034.png)

> <span id="_Ref219290984" class="anchor"></span>Figure 34: Date Default for Search

- Note: The user may only select an end date that falls within 30 days of the start date.
- Note: A warning message about slow performance will appear for date ranges greater than 14 days (see [⁠⁠⁠Figure 35⁠](#_Ref219291031) for an example).

> ![](clinical-capacity-search-tool-ccst-user-guide/035.png)

> <span id="_Ref219291031" class="anchor"></span>Figure 35: Date Range Warning

8.  Providing all the required criteria in the Start New Search panel as described in the steps above will cause the Get Availability button to become selectable (changing from a grey to blue color) as shown below in [⁠⁠Figure 36⁠⁠](#_Ref219291069). The user can then select the Get Availability button to prompt a search by CCST for available appointments based on the chosen search criteria.

> ![](clinical-capacity-search-tool-ccst-user-guide/036.png)

<span id="_Ref219291069" class="anchor"></span>Figure 36: Get Availability Button

- Note: The Reset button shown below in Figure 37 can be selected at any time to return all required fields to their default value (e.g., Clinical Service input field returns to an empty state) in the Start New Search panel. In the event a query has been performed, the Reset button will also clear search results.

> ![](clinical-capacity-search-tool-ccst-user-guide/037.png)

> <span id="_Ref219291101" class="anchor"></span>Figure 37: Reset Button

## Available Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Once the user has completed all steps from [⁠⁠3.1 Start New Search⁠⁠](#start-new-search), the search results will become visible in a table as pictured below in Figure 38. In the event a query is based on the Both Appointment Type, two separate search results tables will be provided together: one for virtual available appointments and another for in-person available appointments, as shown in Figure 39.

> ![](clinical-capacity-search-tool-ccst-user-guide/038.png)

<span id="_Ref219292157" class="anchor"></span>Figure 38: Single-View Available Appointments Table

> ![](clinical-capacity-search-tool-ccst-user-guide/039.png)

<span id="_Ref219292185" class="anchor"></span>Figure 39: Multiview Search Results for Available Appointments

- Note: Except for Appointment Type, a blue banner appearing above the Available Appointments table(s) will display the search criteria chosen by the user. In addition to Site Location, Clinical Service, and Date Range for virtual available appointment queries, searches based on the In-Person or Both Appointment Type will also display Radius (see Figure 40).

> ![](clinical-capacity-search-tool-ccst-user-guide/040.png)

> <span id="_Ref219292220" class="anchor"></span>Figure 40: Search Criteria Banner

- Note: A partial results alert may also appear above the table(s) of search results if an incomplete dataset has been returned for a query (see Figure 41). Multiview search results based on the Both Appointment Type may show two partial results alerts: one for the virtual available appointment search results and another for the in-person available appointment search results.

> ![](clinical-capacity-search-tool-ccst-user-guide/041.png)

> <span id="_Ref219292242" class="anchor"></span>Figure 41: Partial Results Alert

- Note: Above the search results on in-person available appointments, a yellow banner will appear with a reminder for users to check for a Traveling Veteran agreement and a resource sharing agreement before scheduling a clinical encounter (see Figure 42).

> ![](clinical-capacity-search-tool-ccst-user-guide/042.png)

> <span id="_Ref219292344" class="anchor"></span>Figure 42: Search Results with a Reminder to Check Agreements

2.  The user will be able to look through available appointments manually and will need to scroll through a table of search results until an appropriate time slot is found.
- Note: Users can edit the number of rows shown in a table of search results by selecting the arrow seen in Figure 43.

> ![](clinical-capacity-search-tool-ccst-user-guide/043.png)

> <span id="_Ref219292371" class="anchor"></span>Figure 43: Button to Change Number of Rows

- Note: Users can navigate a table to view more available time slots by selecting the arrows shown in Figure 44. From left to right, “\|\<” will allow the user to jump to the first page, “\<” to navigate one page backward, “\>” to navigate one page forward, and “\>\|” to jump to the last page. Arrows will be grayed out and unselectable if the user cannot navigate in a certain direction.

> ![](clinical-capacity-search-tool-ccst-user-guide/044.png)

> <span id="_Ref219292394" class="anchor"></span>Figure 44: Table Navigation

3.  The user can select one or more items from a search results table by clicking on specific rows as seen in the screenshot of virtual available appointments in Figure 45.

> ![](clinical-capacity-search-tool-ccst-user-guide/045.png)

<span id="_Ref219292442" class="anchor"></span>Figure 45: Row Selection

4.  After selecting each available appointment row, the user can then scroll down to the bottom of the page, as shown in Figure 46, to see the information for each selected appointment.

> ![](clinical-capacity-search-tool-ccst-user-guide/046.png)<span id="_Ref156997859" class="anchor"></span>

Figure 46: Appointment Selected Information

- Note: Deselecting an appointment from the Available Appointments table or selecting the “x” for a selected appointment appearing below the table with remove that available appointment from the listed view.
- Note: For the multi-view of search results showing both in-person and virtual available appointments, selections from each table will appear at the bottom of the page (see Figure 47).

> ![](clinical-capacity-search-tool-ccst-user-guide/047.png)

> <span id="_Ref219292650" class="anchor"></span>Figure 47: Available Appointment Selections Displayed in the Multiview

- *Note: The Reset button shown in Figure 37 can be selected at any time to return all required fields to their default value (e.g., Clinical Service input field returns to an empty state) in the Start New Search panel. In the event a query has been performed, the Reset button will also clear search results.*

# Filtering and Column Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Sort by Ascending and Descending Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To make looking for an available appointment easier, the user can sort the search results within a table. To begin, the user will need to select a vertical ellipsis that serves as the Column Actions icon for the desired column, as seen below in Figure 48.

> ![](clinical-capacity-search-tool-ccst-user-guide/048.png)

<span id="_Ref219292817" class="anchor"></span>Figure 48: Column Actions Icons

2.  The user can then select the option “Sort by \[Column Name\] ascending” or “Sort by \[Column Name\] descending” to arrange the elements of a column in increasing or decreasing order, respectively (see Figure 49).

> ![](clinical-capacity-search-tool-ccst-user-guide/049.png)

<span id="_Ref219292839" class="anchor"></span>Figure 49: Sorting Options

3.  To return the search results to the default arranged order, the user will need to select the Column Actions icon again as seen in Figure 48, then select the “Clear sort” option shown in Figure 50.

> ![](clinical-capacity-search-tool-ccst-user-guide/050.png)

<span id="_Ref219292893" class="anchor"></span>Figure 50: Clear Sort Option

4.  As an alternative option to using Column Actions, the user can also sort columns by selecting the arrow symbol located immediately to the right-hand side of the column’s name (see Figure 51).

> ![](clinical-capacity-search-tool-ccst-user-guide/051.png)

<span id="_Ref219292925" class="anchor"></span>Figure 51: Sort Icon

5.  Selecting the Sort icon (represented as “↑↓”) once will arrange the data for a particular column in ascending order (signified by “↑”), clicking a second time will sort in descending order (signified by “↓”), and a third time will cause results to be organized in the unsorted default order (signified by “↑↓”).
- Note: The default organization for the Date column is in ascending order (i.e., a Sort icon of “↑↓” and “↑” will result in the same data arrangement).

## Toggle Density

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When looking for an available appointment, the option to adjust how much of the search results can be seen all at once is accomplished with the Toggle Density function. To adjust the default density level, select the Toggle Density icon once or twice, respectively (see Figure 52).

> ![](clinical-capacity-search-tool-ccst-user-guide/052.png)

<span id="_Ref219292954" class="anchor"></span>Figure 52: Toggle Density Icon

2.  There are three different density levels for the user to choose from: spacious, comfortable, and compact view, depending on the user’s preference. Simply keep selecting the Toggle Density button to rotate through the options until the preferred spacing of search results is found.

## Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The option to show and hide filters is available when looking for available appointments. To begin, the user will need to select the Show Filters icon seen in Figure 53. Once the Show Filters icon is selected, an input field will appear under each column’s name (see Figure 54).

> ![](clinical-capacity-search-tool-ccst-user-guide/053.png)

<span id="_Ref219293133" class="anchor"></span>Figure 53: Show Filters Icon

> ![](clinical-capacity-search-tool-ccst-user-guide/054.png)

<span id="_Ref219293170" class="anchor"></span>Figure 54: Input Fields for Filtering

- Note: The user can also filter via the “Filter by \[Column Name\]” option that is available through CCST’s Column Actions functionality. To access this, the user will need to select the Column Actions icon and make the appropriate selection from the dropdown list (see the example in Figure 55).

> ![](clinical-capacity-search-tool-ccst-user-guide/055.png)

> <span id="_Ref219293430" class="anchor"></span>Figure 55: Filter by Column Name Option

2.  Once the input field appears for each column, the user is able to narrow their search results via the dropdown options (see Figure 56 for an example), which is possible for all but three columns: Date, Start Time and End Time (see [⁠⁠Table 1⁠⁠](#_Ref179290059) for more details).

> ![](clinical-capacity-search-tool-ccst-user-guide/056.png)

<span id="_Ref219293462" class="anchor"></span>Figure 56: Applying Filter to Narrow Search Results by Duration

<span id="_Ref179290059" class="anchor"></span>*Table 1: Search Criteria for Filtering*

| Column                    | Search Format                                                                              |
|---------------------------|--------------------------------------------------------------------------------------------|
| Date                      | Free-text entry ranging from a single digit to using the entirety of the format MM/DD/YYYY |
| Day                       | Dropdown selection                                                                         |
| Start & End Time          | Free-text entry ranging from a single digit to using the entirety of the format h:mm AM/PM |
| Duration                  | Dropdown selection                                                                         |
| Modality (Virtual Only)   | Dropdown selection                                                                         |
| Provider Name             | Dropdown selection                                                                         |
| Clinic Name               | Dropdown selection                                                                         |
| Facility (In Person Only) | Dropdown selection                                                                         |
| VISN                      | Dropdown selection                                                                         |
| CONS.                     | Dropdown selection                                                                         |

- Note: To filter by date or time, the user must type a value into the appropriate input field. To narrow the search results based on a start or end time, the user can enter a single digit, or type a time based on a 12-hour clock using an h:mm format, such as 2:15 (see Figure 57). Additional options for filtering by time are provided in [⁠⁠Table 1⁠⁠](#_Ref179290059).

> ![](clinical-capacity-search-tool-ccst-user-guide/057.png)

> <span id="_Ref219293548" class="anchor"></span>Figure 57: Applying Filter to Narrow Search Results

3.  Once the input field has been populated, the page will automatically refresh and show the results for available appointments based on the filter(s) applied by the user. To clear the filter, simply select the “X” next to the filter input field as shown in Figure 58.

> ![](clinical-capacity-search-tool-ccst-user-guide/058.png)

<span id="_Ref219293631" class="anchor"></span>Figure 58: Clearing the Input for Filtering Search Results

- Note: A column filter can also be cleared by using the “Clear Filter” option seen in Figure 59.

> ![](clinical-capacity-search-tool-ccst-user-guide/059.png)

> <span id="_Ref219293690" class="anchor"></span>Figure 59: Using the Clear Filter Option from Column Actions

4.  When at least one filter is utilized to narrow search results, the “Reset Filters” button above the Available Appointments table will become active and selectable (see Figure 60). Selecting the “Reset Filters” button removes all active filters, and the table will immediately refresh to display the original unfiltered search results; additionally, the “Reset Filters” button will return to its default grey color and no longer be selectable (see Figure 61 for an example).

> ![](clinical-capacity-search-tool-ccst-user-guide/060.png)

> <span id="_Ref219293804" class="anchor"></span>Figure 60: Active Clear Applied Filters Button

> ![](clinical-capacity-search-tool-ccst-user-guide/061.png)

<span id="_Ref219298946" class="anchor"></span>Figure 61: Inactive Clear Applied Filters Button with Original Search Results

## Search Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Optionally, the Search function can be used to find certain available appointments based on a specific criterion. To begin, the user will need to select the Show Search icon near the upper right-hand corner of the Available Appointments table as shown in Figure 62.

> ![](clinical-capacity-search-tool-ccst-user-guide/062.png)

<span id="_Ref219294071" class="anchor"></span>Figure 62: Show Search Icon

2.  Once the icon is selected, a search bar becomes available as a dedicated input field for a free-text entry (i.e., letters, numbers, and symbols). CCST will use the specified criterion entered as a requirement for finding and displaying available appointments with matching data from the search bar (see Figure 63 for an example).

> ![](clinical-capacity-search-tool-ccst-user-guide/063.png)

<span id="_Ref219294353" class="anchor"></span>Figure 63: Matching Search Result

- Note: Examples of a specific criterion that serve as a search entry can include digits such as the number 60, to find available appointments with a 60-minute duration; a term like the word telephone, to find available appointments that will accommodate a clinical encounter by phone; or a name, to find available appointments with a particular provider.
3.  The user can remove the text from the search bar by using the backspace or delete key on their keyboard; alternatively, the user can select the Clear Search icon, which displays as an “X” in the search bar (see Figure 64).

> ![](clinical-capacity-search-tool-ccst-user-guide/064.png)

<span id="_Ref219294411" class="anchor"></span>Figure 64: Clearing the Search Field

4.  Once the search bar is cleared of any input, the Available Appointments table will refresh to show expanded search results. Assuming the Filter function is not in use, clearing the search bar will result in the return of the original search results. The user can then select the “Hide Search” icon seen in Figure 65 to conceal the search bar.

> ![](clinical-capacity-search-tool-ccst-user-guide/065.png)

<span id="_Ref219294723" class="anchor"></span>Figure 65: Hide Search Icon for Concealing the Search Field

# Utilization Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Obtaining Data on CCST Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Data on the usage of CCST (e.g., frequency of queries on available appointments) can be retrieved by navigating to the Utilization Report web page. To navigate to the Utilization Report, the user will need to select the Utilization Report tab on the upper left-hand side of the page as seen Figure 66.

> ![](clinical-capacity-search-tool-ccst-user-guide/066.png)

<span id="_Ref219294773" class="anchor"></span>Figure 66: Accessing the Utilization Report

2.  The user will be taken to the Utilization Report page shown below in Figure 67. On this page, the user can select the preferred search criteria for their utilization report. The default Date Range will automatically be populated with the start and end date for the week prior to the current day. Select Site Location(s) will also default to the site the user is currently in.

> ![](clinical-capacity-search-tool-ccst-user-guide/067.png)

<span id="_Ref219295023" class="anchor"></span>Figure 67: Utilization Report Web Page

3.  If a different start and end date is preferred over the default date range, users can select the button shown in Figure 68.

> ![](clinical-capacity-search-tool-ccst-user-guide/068.png)

<span id="_Ref219295061" class="anchor"></span>Figure 68: Date Range Dropdown for Utilization Report

- Note: No part of the Date Range can precede the first date of data capture or exceed the current day of data capture. Until the current day has completely passed, any search results for a utilization report that includes CCST usage for performing queries on available appointments today should be presumed incomplete.
4.  Once selected, a dropdown will appear with different selections for preset date ranges and an option for a custom date range. Selecting a preset date range will automatically populate the field with the proper dates. Choosing the “Custom Range” selection will cause the calendar shown in Figure 69 to appear.

> ![](clinical-capacity-search-tool-ccst-user-guide/069.png)

<span id="_Ref219295161" class="anchor"></span>Figure 69: Custom Date Range Calendar for the Utilization Report

5.  Users can then select the required start and end dates for the search. Once both search dates have been selected, the user can then select the “APPLY” button seen in Figure 70.

> ![](clinical-capacity-search-tool-ccst-user-guide/070.png)

<span id="_Ref219295215" class="anchor"></span>Figure 70: Selecting a Custom Date Range

- Note: The “APPLY” button only becomes available when a proper start and end date have both been selected.
- Note: Users can select the “CANCEL” button to close the custom date range calendar or select from the list of options seen in Figure 71 to continue search with a preset date range.

  ![](clinical-capacity-search-tool-ccst-user-guide/071.png)

> <span id="_Ref219295289" class="anchor"></span>Figure 71: Preset Date Ranges

6.  Users can edit the default Select Site Location search criteria by adding or removing as many sites as needed by using the dropdown selection seen in Figure 72. At least one site needs to be selected to perform a search.

> ![](clinical-capacity-search-tool-ccst-user-guide/072.png)

<span id="_Ref219295493" class="anchor"></span>Figure 72: Select Site Location(s) Field

- Note: Selecting a new site location via the Change Site modal will prompt an automatic repopulation of the Select Site Location(s) input field to the new chosen location. This will also automatically delete any other locations previously selected for the field.
- Note: Users can either remove specific site locations by selecting the “x” displayed next to the site number shown in Figure 73 or remove all sites by selecting the “X” button located on the far right as seen in Figure 74.

  ![](clinical-capacity-search-tool-ccst-user-guide/073.png)

> <span id="_Ref219295531" class="anchor"></span>Figure 73: Removing Patient Sites Individually from Select Site Location(s)

![](clinical-capacity-search-tool-ccst-user-guide/074.png)

> <span id="_Ref219295570" class="anchor"></span>Figure 74: Removing all Patient Sites from Select Site Location(s)

7.  The User Name Contains field, shown below in Figure 75, can be used if the user prefers to run a utilization report based on a specific CCST user. If the user would like to search for a specific user, please utilize the LASTNAME, FIRSTNAME format and include at least three characters in the field to perform the search.

> ![](clinical-capacity-search-tool-ccst-user-guide/075.png)

<span id="_Ref219295721" class="anchor"></span>Figure 75: User Name Contains Field

8.  Once all required search criteria has been entered, the search button shown in Figure 76 can be selected.

> ![](clinical-capacity-search-tool-ccst-user-guide/076.png)

<span id="_Ref219296780" class="anchor"></span>Figure 76: Search Button for Utilization Report

- Note: If the user incorrectly populates the Select Site Location(s) field, the search button will remain inactive as seen in Figure 77 .

> ![](clinical-capacity-search-tool-ccst-user-guide/077.png)

> <span id="_Ref219296815" class="anchor"></span>Figure 77: Inactive Search Button

- Note: Users can select the “Reset” button at any time to reset the entered search criteria.
9.  Once the search has been completed, the page will update to look like Figure 78. This page will display different informational charts and graphics relating to the previously selected search criteria. At the bottom of the page is a grid with more detailed information such as who made the searches, the number of queries they have made, etc.

![](clinical-capacity-search-tool-ccst-user-guide/078.png)

<span id="_Ref219296840" class="anchor"></span>Figure 78: Utilization Report on CCST Usage

- Note: A “No Results Found” message will appear if the available appointment query performed does not match the search criteria used to run a utilization report (see Figure 79).

> ![](clinical-capacity-search-tool-ccst-user-guide/079.png)

> <span id="_Ref219296868" class="anchor"></span>Figure 79: No Results Found Message

- Note: Users can select the “Reset” button shown in Figure 80 to reset the page.

> ![](clinical-capacity-search-tool-ccst-user-guide/080.png)

> <span id="_Ref219296917" class="anchor"></span>Figure 80: Reset Search Button