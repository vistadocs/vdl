---
title: Patient Check In Clinical Staff Viewer (PCICSV) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Patient Check In Clinical Staff Viewer (PCICSV)
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
description: 
audience: 
keywords: 
  - figure
  - span
  - class
  - table
  - button
  - contents
  - anchor
  - patient
  - queue
  - appointment
page_count: 0
word_count: 8366
section_count: 26
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/pcicsv_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/pcicsv_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=100"
---

OFFICE OF  
INFORMATION  
AND TECHNOLOGY

Patient Check In  
Clinical Staff Viewer (PCICSV)  
User Guide

*Version 2.2.0* \| February 2026
## Table of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc221538983" class="anchor"></span>Table 1: Icons</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 53%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/09/2026</td>
<td>2.2.0</td>
<td>Addition of sections 4.3.1.4 Time Column and 4.3.2 Expanded Details.</td>
<td>Tech Writers Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>08/20/2025</td>
<td>2.0.0</td>
<td>Update to UI and format. Update outdated information throughout document.</td>
<td>Tech Writers Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>05/28/2024</td>
<td>1.29</td>
<td>Updated to add the new Arrived Column on the Daily Appointment List. Also added Arrived as a new Workflow Status selection on the Daily Workflow List.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>02/15/2024</td>
<td>1.28</td>
<td><p>Updated to add a filter function to the Insurance and Demographics columns of the Daily Appointment List.</p>
<p>Enables users to: undo marking a queue appointment complete; view a list of multiple appointments patients have for the day across all clinics; and select and deselect column filters with more than three filter options.</p></td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>12/13/2023</td>
<td>1.27</td>
<td>Updated to add a filter function to Check-In Step column of Daily Appointment List. Reinstated sorting feature to Check-In Time column of Daily Appointment/Daily Workflow Lists.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>11/13/2023</td>
<td>1.26</td>
<td>Updated to add filter to columns for Check-In Times on the Daily Appointment/Daily Workflow Lists, and Pre-Check-In and eCheck-In on the Daily Appointment List.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>08/28/2023</td>
<td>1.25</td>
<td>Updated to display the Clinic List drop-down in alphabetical order.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>07/07/2023</td>
<td>1.24</td>
<td>Updated to implement the ability to provide system notifications to users.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>06/13/2023</td>
<td>1.23</td>
<td>Updated the Queue List to include the Memo Column</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>04/04/2023</td>
<td>1.22</td>
<td>Updated to show eCheck-Ins and Pre-Check-Ins completed count on the Daily Appointment and Daily Workflow Lists. Updated verbiage presented when attempting to delete a queue that still has patients in an incomplete status.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>03/20/2023</td>
<td>1.21</td>
<td>Updated document to remove the trash can icon from queuing so users cannot delete patient from a queue</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>03/07/2023</td>
<td>1.20</td>
<td>Updated the document to update the phone number field under section 5.6</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>02/14/2023</td>
<td>1.19</td>
<td>Updated the document with section 5.6 on added messaging</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>02/07/2023</td>
<td>1.18</td>
<td>Updated the document to revise sections 5.4.1.1 and 5.4.1.3 on queues</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>02/03/2023</td>
<td>1.17</td>
<td>Updated the document to revise section 5.4 on queues</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>01/25/2023</td>
<td>1.16 (not published)</td>
<td>Updated the document with section 5.4 on queues</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>12/14/2022</td>
<td>1.15</td>
<td>Updated the document with section 5.2.2 Updates Check In and Check Out Status Logic</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>10/19/2022</td>
<td>1.14</td>
<td>Updated the document with section 5.7 Displays Checkout Time and Indicator.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>09/28/2022</td>
<td>1.13</td>
<td><p>Added section 6.3 Pop-up Message to Ensures Users are Running the Current Version.</p>
<p>Updated 6.1 Enhanced Error message section to include the new error message logic.</p></td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>09/21/2022</td>
<td>1.12</td>
<td>Updated document to include removal of insurance column for MANILA – RO 358.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>09/15/2022</td>
<td>1.11</td>
<td>Updated document to include sections 5.6 Display Number of Checked-In Appointments and 6.2 Reset Button</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>09/07/2022</td>
<td>1.10</td>
<td>Updated document to include section 5.1.3 Validating User Access to VistA Instances.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>08/30/2022</td>
<td>1.9</td>
<td>Updated document to include the following functionalities: Flag Legend and Toggle to Disable Notifications for Updated Appointments.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>08/22/2022</td>
<td>1.8</td>
<td>Updated document to include the following new functionalities: Display Fugitive Felon, Local/National &amp; Restricted Record Flags, and Enhanced Error Messages.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>08/10/2022</td>
<td>1.7</td>
<td>Updated Section 5.3 Daily Workflow List to include the Memo functionality.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>06/14/2022</td>
<td>1.6</td>
<td>Updated Section 5.4 Medication List and Pre-Visit Summary with Sensitive record pop-up page.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>05/12/2022</td>
<td>1.5</td>
<td>Updated the document with Test Patient Screenshots</td>
<td>VSE PMO</td>
</tr>
<tr class="even">
<td>03/03/2022</td>
<td>1.4</td>
<td>Accepted all recommended changes and finalized the document</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
<tr class="odd">
<td>03/01/2022</td>
<td>1.3</td>
<td>Updated the document with Medications List, Pre-Visit Summary, and Alert Notifications.</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
<tr class="even">
<td>02/08/2022</td>
<td>1.2</td>
<td>Final review/proofread and accepted all recommended changes</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
<tr class="odd">
<td>01/28/2022</td>
<td>1.1</td>
<td>Developers Review</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
<tr class="even">
<td>12/30/2021</td>
<td>1.0</td>
<td>Baseline for VSECS</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
</tbody>
</table>

<span id="_Toc221538983" class="anchor"></span>Table 1: Icons

<span class="mark">  
</span>

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Table of Figures](#table-of-figures)
  - [Table of Tables](#table-of-tables)
  - [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Overview](#overview)
  - [User Access Levels](#user-access-levels)
  - [PIV Login](#piv-login)
- [Familiarizing Yourself with PCICSV](#familiarizing-yourself-with-pcicsv)
  - [My Account](#my-account)
    - [User Preferences](#user-preferences)
    - [Signing Out of PCICSV](#signing-out-of-pcicsv)
  - [Help](#help)
  - [Filters](#filters)
    - [Sort by Ascending and Descending](#sort-by-ascending-and-descending)
    - [Toggle Density](#toggle-density)
    - [Show, Hide, and Search Filters](#show-hide-and-search-filters)
    - [Search Function](#search-function)
    - [Reset Filters](#reset-filters)
- [Clinic List Management](#clinic-list-management)
  - [Create New Clinic List](#create-new-clinic-list)
  - [Edit a Personal Clinic List](#edit-a-personal-clinic-list)
  - [Delete a Personal Clinic List](#delete-a-personal-clinic-list)
- [Daily Appointment and Workflow List](#daily-appointment-and-workflow-list)
  - [Daily Appointment List](#daily-appointment-list)
    - [Patient Arrived](#patient-arrived)
    - [Printing](#printing)
  - [Daily Workflow List](#daily-workflow-list)
    - [Change A Workflow Status](#change-a-workflow-status)
    - [Memos](#memos)
  - [Commonalities for Both List Pages](#commonalities-for-both-list-pages)
    - [General Grid Information](#general-grid-information)
    - [Expanded Details](#expanded-details)
    - [Messaging](#messaging)
    - [Pre-Visit Summary](#pre-visit-summary)
    - [Medications](#medications)
    - [Appointment Comments](#appointment-comments)
    - [Current Day Appointments](#current-day-appointments)
- [Queue Management](#queue-management)
  - [Creating Queues](#creating-queues)
  - [Editing Queues](#editing-queues)
  - [Deleting Queues](#deleting-queues)
- [Queue](#queue)
  - [Utilizing Queues](#utilizing-queues)
  - [Queue List Memos](#queue-list-memos)
  - [Marking Visit as Complete/Undo Mark as Complete in Queue](#marking-visit-as-completeundo-mark-as-complete-in-queue)
- [Appendix](#appendix)
  - [Alert Notifications](#alert-notifications)
  - [Icon Descriptions](#icon-descriptions)
  - [Flag Descriptions](#flag-descriptions)
  - [Acronyms and Abbreviations](#acronyms-and-abbreviations)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA) Patient Check In Clinical Staff Viewer (PCICSV) module is a VA-internal web application that allows clinical staff to track patient appointments from check-in, through the clinic workflow, and to a completed appointment. The purpose of PCICSV is to improve the overall Veteran check-in experience and reduce operating costs for VHA. With this document, users can familiarize themselves with the features and navigation of PCICSV, including clinic list management, daily appointment and workflow lists, queues, and queue management.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCICSV is accessible to any VA network user who has a Personal Identity Verification (PIV) card and Identity and Access Management (IAM) account provisioned to a VistA station.

- Schedulers are required to have the SDECRPC Menu Option. All scheduling personnel should already have the menu option.
- Non-Schedulers, Nurses, and Providers are required to have SDECRPC Menu Option and SDECVIEW Key.
- Users needing access to the Queue Management tab must have SD SUPERVISOR Key assigned to them.
- Users must have SECONDARY MENU OPTIONS: VIAB WEB SERVICES OPTION to utilize patient search for queuing.

PCICSV will validate a user’s clinic list access upon app load. Clinics that the user no longer has access to will be removed from the drop-down on the Daily Appointment List and Daily Workflow List. Additionally, the clinics the user no longer has access to will only be able to be deleted within the Clinic List Management page to indicate the user no longer has access to that clinic.

## PIV Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Begin by opening a browser and going to the PCICSV web application. The VA Single Sign-On page will then appear. Select the “Sign in with PIV” option, as seen in Figure 1, to proceed with the log in process.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/001.png)

<span id="_Ref206425642" class="anchor"></span>Figure 1: Single Sign-On Internal (SSOi) Login

2.  After selecting, an ActivClient Login dialog box will appear to prompt you to enter your PIN. Type the numbers of your PIN as prompted in Figure 2. If authentication is successful, PCICSV will load. If it is not successful, you will be prompted to enter your correct PIN instead.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/002.png)

<span id="_Ref206425677" class="anchor"></span>Figure 2: ActivClient Login Pop-Up Window

# Familiarizing Yourself with PCICSV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once log in is complete, the user will see the Daily Appointment List page seen in Figure 3. The user can then select the tabs on the left-hand side of the page to maneuver through the different features of PCICSV.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/003.png)

<span id="_Ref209185774" class="anchor"></span>Figure 3: Logging in to PCICSV

- Note: The user can select the “Side Menu” button seen in Figure 4 to collapse or expand the menu.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/004.png)

> <span id="_Ref209186566" class="anchor"></span>Figure 4: Side Menu Button for PCICSV

## My Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To change user preferences, the user can select the “My Account” button in the upper right-hand corner, seen in Figure 5, to open the dropdown.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/005.png)

<span id="_Ref206595447" class="anchor"></span>Figure 5: My Account Button for PCICSV

2.  The user can then select the “Preferences” button, seen in Figure 6, to be taken to the User Preferences page.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/006.png)

<span id="_Ref206596029" class="anchor"></span>Figure 6: Preferences Button

#### Notifications

On the User Preferences page, the user has the option to disable windows alerts or notifications by selecting the checkbox seen below in Figure 7.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/007.png)

<span id="_Ref206586013" class="anchor"></span>Figure 7: Disable Windows Notifications Setting

#### Daily Appointment and Workflow List

*Disclaimer: The information contained in this section applies to both the Daily Appointment List and the Daily Workflow List sections on the User Preferences page. For information on Workflow Status preferences, please see section 2.1.1.3 Workflow Status.*

1.  To adjust the default columns, the user will need to select the checkboxes in Figure 8 to show or hide columns. The user will know that the column is hidden when the checkbox displays empty (see Figure 9 for example).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/008.png)

<span id="_Ref209189520" class="anchor"></span>Figure 8: Daily Appointment and Workflow List Column Checkbox

2.  The user can also select the button seen below in Figure 9 to drag and drop the column and change the default order.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/009.png)

<span id="_Ref209189521" class="anchor"></span>Figure 9: Button to Adjust Column Order

3.  The user can then select the “Save Changes” button seen in Figure 10 to save their changes.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/010.png)

<span id="_Ref209189522" class="anchor"></span>Figure 10: Save Changes Button for Daily Appointment and Workflow List Settings

4.  To reset preferences, select the “Reset to Default” button shown in Figure 11.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/011.png)

<span id="_Ref209189563" class="anchor"></span>Figure 11: Reset to Default Button for Daily Appointment and Workflow List Settings

- Note: User preferences will be reset whenever the user clears their browser cache.

#### Workflow Status

1.  To adjust the default options, the user will need to select the checkboxes in Figure 12 to show or hide status options. The user will know that the options are hidden when the checkbox displays empty (see Figure 13 for example).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/012.png)

<span id="_Ref209190696" class="anchor"></span>Figure 12: Workflow Status Checkbox Settings

2.  The user can then select the “Save Changes” button seen in Figure 13 to save their changes.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/013.png)

<span id="_Ref209190697" class="anchor"></span>Figure 13: Save Changes Button for Workflow Status Settings

3.  To reset preferences, select the “Reset to Default” button shown in Figure 14.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/014.png)

<span id="_Ref209190698" class="anchor"></span>Figure 14: Reset to Default Button for Workflow Status Settings

- Note: User preferences will be reset whenever the user clears their browser cache.

### Signing Out of PCICSV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To sign out of PCICSV, the user will need to select the “My Account” button in the upper-right hand corner, as seen in Figure 15.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/015.png)

> <span id="_Ref184740944" class="anchor"></span>Figure 15: My Account Button for PCICSV

2.  The user will then need to select the “Sign Out” button from the dropdown menu shown in Figure 16.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/016.png)

<span id="_Ref205391213" class="anchor"></span>Figure 16: Sign Out Button for PCICSV

3.  Upon signing out of the PCICSV application, the user will be taken to the page seen in Figure 17 that will prompt them to log out of the VA SSOi and close the browser.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/017.png)

> <span id="_Ref184740966" class="anchor"></span>Figure 17: Logged Out of Mobile Applications Page

## Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can select the Help tab to be brought to the Help page. From here, users will be shown the number of the VA Help Desk, the create YourIT service portal ticket link, the PCICSV user guide link, and the Reset Session button (see Figure 18 for example).

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/018.png)

<span id="_Ref206585742" class="anchor"></span>Figure 18: Help Page for PCICSV

## Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Sort by Ascending and Descending

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When looking in the grids on PCICSV, the user can sort rows within the table. To begin, the user will need to select the vertical ellipsis next to the desired column, as seen below in Figure 19.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/019.png)

<span id="_Ref206425742" class="anchor"></span>Figure 19: Selecting Column Actions Button to Sort Order

- Note: The table will be defaulted to ascending appointment time.
2.  The user can then select either “Sort by (Column Name) Ascending” or “Sort by (Column Name) descending” to sort rows in an ascending or descending order within the table, outlined within Figure 20.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/020.png)

> <span id="_Ref206425915" class="anchor"></span>Figure 20: Sort Options for Table Information

3.  To return the sorting to default, the user will need to select the vertical ellipsis seen in Figure 19, then select the “Clear Sort” button shown in Figure 21.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/021.png)

<span id="_Ref206425968" class="anchor"></span>Figure 21: Clear Sort Button

4.  Optionally, the user can sort rows by hovering the cursor next to a column’s name and selecting the arrow button that appears in Figure 22.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/022.png)

<span id="_Ref185610605" class="anchor"></span>Figure 22: Ascending/Descending Filter Arrow

5.  Selecting the arrow once will cause results to sort by ascending order (↑), a second time to sort by descending order (notated by ↓), and a third time to cause results to appear in the default order again (notated with no arrow).

### Toggle Density

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user has the option to adjust toggle density of the grid. To begin adjusting the toggle density, select the button shown in Figure 23.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/023.png)

<span id="_Ref185610630" class="anchor"></span>Figure 23: Toggle Density Button

2.  There are three different options for the user to choose from depending on the user’s preference. Simply keep selecting the “Toggle Density” button to rotate through the options until the user finds their preferred density.

### Show, Hide, and Search Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user has the option to show and hide filters. To begin, the user will need to select the “Show/Hide Filters” button, or the “Filter by (Column Name)” button, both shown in Figure 24. Selecting either will cause the search functions to appear under each column name.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/024.png)

> <span id="_Ref165300734" class="anchor"></span>Figure 24: Show/Hide Filter Options Buttons

2.  Once the search options appear as seen in Figure 25, the user can select the search bar or dropdown menu under the desired column to be filtered and enter or select the required information needed.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/025.png)

> <span id="_Ref165300749" class="anchor"></span>Figure 25: Example of Filter Search Menu on Grid View

- Note: Leaving the individual filters unpopulated will result in the grid showing all unfiltered data.
3.  Once the filter field has been populated, results will automatically refresh and show items based on the filtered criteria as seen below in Figure 26.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/026.png)

> <span id="_Ref165300767" class="anchor"></span>Figure 26: Example of Filtered Results in Grid View

4.  To clear the search, the user can then select either the “X” next to the search bar or the “Clear Filter” button seen in Figure 27. Selecting this will cause all results to appear within the table.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/027.png)

> <span id="_Ref165300795" class="anchor"></span>Figure 27: Clearing Filter Button

5.  Once finished searching, the user can then select the “Show/Hide Filters” button seen in Figure 28 to hide the search bar.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/028.png)

> <span id="_Ref165300814" class="anchor"></span>Figure 28: Selecting Show/Hide Filters Button to Hide Filter Menu

### Search Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user can search through all items within the grid by selecting the “Show/Hide Search” button seen in Figure 29.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/029.png)

<span id="_Ref185610845" class="anchor"></span>Figure 29: Show/Hide Search Button

2.  The user can then type the requested information into the search function. This will cause matching results to filter within the grid as shown in Figure 30 below.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/030.png)

<span id="_Ref185610862" class="anchor"></span>Figure 30: Filtered Search Example

3.  To clear the search, the user will need to select the “X” next to the search bar seen in Figure 31. Selecting this will cause all results to appear within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/031.png)

<span id="_Ref185610899" class="anchor"></span>Figure 31: Clear Button for Search Bar

4.  Once finished searching, the user can then select the “Show/Hide Search” button seen in Figure 29 above to hide the search bar from view.

### Reset Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To reset any filters within the grid, the user can select the “Reset Filters” button, as seen in Figure 32.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/032.png)

<span id="_Ref165300877" class="anchor"></span>Figure 32: Reset Filters Button on Grid View

# Clinic List Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinic List Management page can be navigated to by selecting the “Clinic List Management” tab shown in Figure 33. The user can use this page to create new clinic lists, as well as edit and delete personal clinic lists.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/033.png)

<span id="_Ref206427120" class="anchor"></span>Figure 33: Clinic List Management Tab

- Note: If a user’s VistA access is removed, the lists previously made under Clinic List Management for those instances will receive the error seen in Figure 34.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/034.png)

> <span id="_Ref213328051" class="anchor"></span>Figure 34: VistA Access Removed Error for Clinic List Management

## Create New Clinic List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Creating a clinic list allows the clinicians to group clinics into one manageable list. The Clinic List grid will display in alphabetical order, with the default clinic list at the top. After successfully logging into PCICSV, follow the steps below to create a new clinic list.

1.  To create a new clinic list, the user will need to select the “Create New Clinic List” button shown in Figure 35 to open the Create Clinic List window.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/035.png)

<span id="_Ref206427145" class="anchor"></span>Figure 35: Create New Clinic List Button

2.  The user will then need to fill in all the required information (see Figure 36 for example) and any optional information as needed.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/036.png)

<span id="_Ref206427161" class="anchor"></span>Figure 36: Create Clinic List Window

3.  Once all applicable information has been filled, the user will select the “Create Clinic List” button, seen in Figure 37, to create the new clinic list.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/037.png)

<span id="_Ref206427214" class="anchor"></span>Figure 37: Create Clinic List Button

- Note: The user can select the “Cancel” button seen in Figure 38 to exit creating a clinic list and go back to the Clinic List Management page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/038.png)

> <span id="_Ref206427236" class="anchor"></span>Figure 38: Cancel Button for Create Clinic List Window

- Note: The first clinic list created by the user will automatically be set as the default clinic list. To change the default clinic list once more are created, the user will need to select the “Set as Default” button seen below in Figure 39.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/039.png)

> <span id="_Ref206427256" class="anchor"></span>Figure 39: Set as Default Clinic List Button

## Edit a Personal Clinic List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To edit a clinic list, the user will need to select the ellipsis, seen in Figure 40, next to any clinic list within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/040.png)

<span id="_Ref206427276" class="anchor"></span>Figure 40: Action Menu Button for Editing Clinic List

2.  This will cause the action menu to appear. The user will then need to select the “Edit List” button, seen in Figure 41, to open the Edit Clinic List window.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/041.png)

<span id="_Ref206427298" class="anchor"></span>Figure 41: Edit Clinic List Button

3.  On this window, the user can edit the name of the clinic list, as well as add or delete any clinic(s) included (see Figure 42).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/042.png)

<span id="_Ref206427317" class="anchor"></span>Figure 42: Edit Clinic List Window

4.  Once all edits have been made, the user will need to select the “Save Changes” button, seen in Figure 43, to save the edits to the clinic list.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/043.png)

<span id="_Ref206427344" class="anchor"></span>Figure 43: Save Changes Button for Edit Clinic List

- Note: The user can select the “Cancel” button seen in Figure 44 to exit editing a clinic list and go back to the Clinic List Management page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/044.png)

> <span id="_Ref206427368" class="anchor"></span>Figure 44: Cancel Button for Edit Clinic List Window

## Delete a Personal Clinic List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To delete a clinic list, the user will need to select the ellipsis, seen in Figure 45, next to any clinic list within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/045.png)

> <span id="_Ref206427387" class="anchor"></span>Figure 45: Action Menu Button for Deleting Clinic List

2.  This will cause the action menu to appear. The user will then need to select the “Delete List” button, seen in Figure 46.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/046.png)

<span id="_Ref206427406" class="anchor"></span>Figure 46: Delete Clinic List Button in the Clinic List Management Action Menu

- Note: The default clinic list is unable to be deleted and the “Delete List” button will always be disabled for that list (see Figure 47 for example).

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/047.png)

> <span id="_Ref206671183" class="anchor"></span>Figure 47: Example of Delete Clinic List Button Disabled for Default List

3.  The Delete Clinic List window will appear. The user can then select the “Delete List” button, shown in Figure 48, to confirm clinic list deletion.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/048.png)

<span id="_Ref206427555" class="anchor"></span>Figure 48: Delete List Button

- Note: The user can select the “Cancel” button seen in Figure 49 to exit deleting a clinic list and go back to the Clinic List Management page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/049.png)

> <span id="_Ref206427581" class="anchor"></span>Figure 49: Cancel Button for Delete Clinic List Window

# Daily Appointment and Workflow List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Daily Appointment List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: The Daily Appointment List and Daily Workflow List pages both share similar functionality. Please see the <u>4.3 Commonalities</u> section for steps on how to complete actions for either page.*

The Daily Appointment List page can be navigated to by selecting the “Appointment List” tab shown in Figure 50.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/050.png)

<span id="_Ref206427664" class="anchor"></span>Figure 50: Daily Appointment List Page

Once a clinic list is created and appointments are made within one of the clinics included, the grid will populate with information on the Daily Appointment List page for clinical staff to view and track. The Daily Appointment List displays all current day appointments for the clinics under the selected clinic list. It also tracks patient attributes like Current Check-In Step, Pre-Check-In status, E-Check-In status, Demographics, and Insurance indicators.

- Note: Users can use the dropdown button, shown in Figure 51, to select a different clinic list.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/051.png)

> <span id="_Ref206427718" class="anchor"></span>Figure 51: Select Clinic List Dropdown for Daily Appointment List

- Note: Users can select a patient’s name from the Daily Appointment List to copy it to their clipboard.

### Patient Arrived

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To mark a patient has arrived, the user will need to select the ellipsis, seen in Figure 52, next to an eligible patient within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/052.png)

<span id="_Ref206427751" class="anchor"></span>Figure 52: Action Menu button for Patient Arrival

2.  This will cause the action menu to appear. The user will then need to select the “Patient Arrived” option, seen in Figure 53.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/053.png)

<span id="_Ref206427775" class="anchor"></span>Figure 53: Patient Arrived Button

3.  This will cause the Confirm Workflow Status Change window to appear. From here, the user will need to select the “Confirm Change” button, seen below in Figure 54, to mark the patient as arrived.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/054.png)

<span id="_Ref206427799" class="anchor"></span>Figure 54: Confirm Workflow Status Change Window for Patient Arrival

- Note: The user can select the “Close” button seen in Figure 55 to cancel the workflow status change. This will take the user back to the Daily Appointment List page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/055.png)

> <span id="_Ref206427821" class="anchor"></span>Figure 55: Close Button for Patient Arrival

4.  Confirming status change will cause the Daily Appointment List grid to update and display a green “Yes” in the Arrived column (see Figure 56 for example).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/056.png)

<span id="_Ref206427860" class="anchor"></span>Figure 56: Example of Confirming Patient Arrival

- Note: When a patient is checked in via ISS or VS GUI, the patient will automatically be marked as arrived within the grid. The Arrived column will also display a green “Yes” if the patient’s status is anything past “Checked In.”

### Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can print from the Daily Appointment List page. Selecting the “Print” button, seen in Figure 57, will prompt the user to open or save a PDF file, where the ability to print the list is accessible.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/057.png)

<span id="_Ref206427090" class="anchor"></span>Figure 57: Print List Button

## Daily Workflow List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: The Daily Appointment List and Daily Workflow List pages both share similar functionality. Please see the <u>4.3 Commonalities</u> section for steps on how to complete actions for either page.*

The Daily Workflow List page can be navigated to by selecting the “Workflow List” tab shown in Figure 58.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/058.png)

<span id="_Ref206427896" class="anchor"></span>Figure 58: Daily Workflow List Page

Once a clinic list is created and appointments are made within one of the clinics included, the clinic list will show up in the Daily Workflow List for the clinical staff to view. The Daily Workflow List page shows a patient’s current workflow status and allows users to track and change the status of the workflow.

- Note: Users can use the dropdown button shown in Figure 59 to view different clinic lists.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/059.png)

> <span id="_Ref206427927" class="anchor"></span>Figure 59: Select Clinic List Button for Daily Workflow List

- Note: Users can select a patient’s name from the Daily Workflow List to copy it to their clipboard.

### Change A Workflow Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To change a patient’s workflow status, the user will need to navigate to the Workflow Status column seen in Figure 60.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/060.png)

<span id="_Ref206427952" class="anchor"></span>Figure 60: Workflow Status Column

2.  The user will then need to expand the dropdown menu and select the appropriate status from the options listed (see Figure 61 for example).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/061.png)

<span id="_Ref206427972" class="anchor"></span>Figure 61: Example of Workflow Status Options

3.  After selecting a status, the Confirm Workflow Status Change window will display asking the user to confirm. The user will need to select the “Confirm Change” button, seen below in Figure 62, to save a patient’s status.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/062.png)

<span id="_Ref206427994" class="anchor"></span>Figure 62: Confirm Workflow Status Change Window

- Note: The user can select the “Close” button seen in Figure 63 to cancel the workflow status change. This will take the user back to the Daily Workflow List page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/063.png)

> <span id="_Ref206428016" class="anchor"></span>Figure 63: Close Button for Workflow Status Change

### Memos

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To add a memo to patient appointments, the user can select the “New” button shown in Figure 64.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/064.png)

<span id="_Ref206428033" class="anchor"></span>Figure 64: New Memo Button

2.  The user will be brought to the Add New Memo to Appointment window, shown in Figure 65. From here, users may add a memo that is up to 100 characters.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/065.png)

<span id="_Ref206428051" class="anchor"></span>Figure 65: Add New Memo to Appointment Window

- Note: Users may also choose to view all previous memos from this page. Simply select the “View All Memos” button, shown in Figure 66, to expand the window with all previously entered memos.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/066.png)

> <span id="_Ref206428075" class="anchor"></span>Figure 66: View All Memos Button

3.  Once the memo has been entered, select the “Add Memo” button, shown in Figure 67, to add the memo to the appointment.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/067.png)

<span id="_Ref206428096" class="anchor"></span>Figure 67: Add Memo Button

- Note: The user can select the “Close” button seen in Figure 68 to cancel adding a memo to an appointment. This will take the user back to the Daily Workflow List page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/068.png)

> <span id="_Ref206428115" class="anchor"></span>Figure 68: Close Button for Add New Memos Window

4.  The user will then return to the Daily Workflow List page, where the memo will be displayed in the Memo column of the related appointment with a timestamp and the initials of the user (see Figure 69 for example).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/069.png)

<span id="_Ref206675631" class="anchor"></span>Figure 69: Example of Memo Entered on Appointment

- Note: When users add more than one memo to an appointment, the “All” button will appear in the Memo column of the grid as seen in Figure 70. When selected, the user will be brought to the View All Memos for Appointment window where they can see all previous memos for the appointment, as well as who made the memo and what time it was created.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/070.png)

> <span id="_Ref206428134" class="anchor"></span>Figure 70: View All Memos Button on the Daily Workflow List Page

## Commonalities for Both List Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Daily Appointment List and Daily Workflow List pages both share similar functionality. Please see the sections below for steps on how to complete actions for either page.

### General Grid Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Refresh

Users can refresh the grid from the Daily Appointment and Daily Workflow List pages. Selecting the “Refresh” button, seen in Figure 71, engages the page to refresh and allows any new information to display. Please be aware that the table will refresh automatically every two minutes with updated information.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/071.png)

<span id="_Ref206427069" class="anchor"></span>Figure 71: Refresh List Button

#### Checked in Appointments

The number of Checked-in appointments, eCheck-ins, and Pre Check-ins will show on the Daily Appointment and Daily Workflow List page. Please see Figure 72 for reference.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/072.png)

<span id="_Ref206427043" class="anchor"></span>Figure 72: Check-In Data Example

- Note: If a patient is more than 15 minutes late to an appointment, the appointment time will display in red with an “!” icon, as seen in Figure 73.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/073.png)

> <span id="_Ref213329366" class="anchor"></span>Figure 73: Late Patient Example

#### Check-In Time Column

The Daily Appointment and Daily Workflow List both contain a Check-In column within the grid. This column will show the following, depending on status: appointment not checked in, the time the appointment has been checked in, or if the appointment is checked out and the time of check out.

#### Time Column

The Daily Appointment and Daily Workflow List both contain a Time column within the grid. This column will display the total care time for the visit, i.e., from check-in to check-out. The column will remain blank for patients who have not checked in.

#### Icon Indicators

Users can hover over icons within PCICSV to see a brief description about what the icon is indicating (see Figure 74 for an example of Walk-In Appointment and Patient eCheck In). For a full list of icons and flags in the application, please see sections 7.2 Icon Descriptions and 7.3 Flag Descriptions.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/074.png)

<span id="_Ref209191398" class="anchor"></span>Figure 74: Icon Example

- Note: When hovering over flags, the user will see more detailed information on the patient’s applied flags (see Figure 75 below).

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/075.png)

> <span id="_Ref209191657" class="anchor"></span>Figure 75: Flag Information Example

### Expanded Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To access expanded details, the user will need to select the ellipsis, seen in Figure 76, next to a patient or an appointment within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/076.png)

<span id="_Ref221539117" class="anchor"></span>Figure 76: Action Menu Button for Expanded Details

2.  This will cause the action menu to appear. The user will then need to select the “Expanded Details” option, seen in Figure 77, where the user will be brought to the Expanded Details window.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/077.png)

<span id="_Ref221539181" class="anchor"></span>Figure 77: Expanded Details Button

3.  From here, the user can select the “Expand All+” button to open all of the accordions at once or individually expand each accordion by selecting the “+” button seen in Figure 78 below.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/078.png)

<span id="_Ref221539207" class="anchor"></span>Figure 78: Expanded Details Accordion Buttons

- Note: The user can select the “X” button seen in Figure 79 to close the Expanded Details window. This will take the user back to either the Daily Appointment or Daily Workflow List pages.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/079.png)

> <span id="_Ref221539290" class="anchor"></span>Figure 79: Close Button for Expanded Details

### Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  On the Daily Workflow and Daily Appointment Lists pages, patients who have started or completed the eCheck-in process meet the criteria for messaging. Users will see the icon highlighted in Figure 80 next to a patient who has completed the eCheck-In process.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/080.png)

<span id="_Ref206428157" class="anchor"></span>Figure 80: eCheck-In Icon for a Completed eCheck-In

2.  To send a message, the user will need to select the ellipsis, seen in Figure 81, next to an eligible patient within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/081.png)

<span id="_Ref206428171" class="anchor"></span>Figure 81: Action Menu Button for Messaging

3.  This will cause the action menu to appear. The user will then need to select the “Messages” option, seen in Figure 82, where the user will be brought to the Messages page.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/082.png)

<span id="_Ref206428191" class="anchor"></span>Figure 82: Messages Button

4.  From here, the user will need to select the “New Message” button to open the dropdown and select a template from the options shown in Figure 83.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/083.png)

<span id="_Ref206428208" class="anchor"></span>Figure 83: New Message Dropdown Menu

5.  Once a template has been chosen, the New Message – (Template Name Here) window will appear (see Figure 84 below for an example of the general new message template and Figure 85 for an example of the Post Lab/X-Ray template).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/084.png)

<span id="_Ref206428223" class="anchor"></span>Figure 84: New Message for General Template Window

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/085.png)

<span id="_Ref213326626" class="anchor"></span>Figure 85: New Message for Post Lab/X-Ray Window

6.  Users will need to fill in the Clinic Phone Number field with a valid phone number to update the information in the message template section. Once finished, select the “Send Message” button shown in Figure 86.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/086.png)

<span id="_Ref206428241" class="anchor"></span>Figure 86: Send Message Button

- Note: The user can select the “Close” button seen in Figure 87 to cancel creating a message. This will take the user back to the Messages page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/087.png)

> <span id="_Ref206678022" class="anchor"></span>Figure 87: Close Button for Creating New Message

- Note: If the message was not sent, the Message Was Not Sent window will appear (see Figure 88). The user will need to close the window and retry sending the message.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/088.png)

> <span id="_Ref206428281" class="anchor"></span>Figure 88: Message Was Not Sent Notification

### Pre-Visit Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This PCICSV functionality allows users the ability to print or save a PDF format of the Pre-Visit Summary for a patient to ensure patients are informed before their appointment. This functionality is available on both the Daily Appointment and Daily Workflow List.

1.  To access a patient’s pre-visit summary, the user will need to select the ellipsis, seen in Figure 89, next to an eligible patient within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/089.png)

<span id="_Ref206502090" class="anchor"></span>Figure 89: Action Menu Button for Pre-Visit Summary

2.  This will cause the action menu to appear. The user will then need to select the “Pre-Visit Summary” option, seen in Figure 90.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/090.png)

<span id="_Ref206502224" class="anchor"></span>Figure 90: Pre-Visit Summary Button

3.  Once selected, a new tab will open in the user’s browser with the pre-visit summary (see Figure 91 for example). From here, the user can choose to print or save the pre-visit summary.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/091.png)

<span id="_Ref206502425" class="anchor"></span>Figure 91: Example of Pre-Visit Summary

### Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To access a patient’s medication list, the user will need to select the ellipsis, seen in Figure 92, next to an eligible patient within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/092.png)

<span id="_Ref206502512" class="anchor"></span>Figure 92: Action Menu Button for Medications

2.  This will cause the action menu to appear. The user will then need to select the “Medication” option, seen in Figure 93.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/093.png)

<span id="_Ref206502675" class="anchor"></span>Figure 93: Medications Button

3.  The user will be brought to the Medications window shown below in Figure 94, where they can see a list of the patient’s medications.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/094.png)

<span id="_Ref206503844" class="anchor"></span>Figure 94: Medications Window

### Appointment Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Appointment comments will appear in the Daily Appointment and Workflow List sections when a comment is added while making an appointment in the Integrated Scheduling Solution (ISS) application.

1.  To access the appointment comments<span class="mark">,</span> the user will need to select the ellipsis, seen in Figure 95, next to an eligible patient within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/095.png)

<span id="_Ref206504778" class="anchor"></span>Figure 95: Action Menu Button for Appointment Comments

2.  This will cause the action menu to appear. The user will then need to select the “Appointment Comments” option, seen in Figure 96.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/096.png)

<span id="_Ref206504801" class="anchor"></span>Figure 96: Appointment Comments Button

3.  The user will be brought to the Appointment Comments window, shown below in Figure 97, where they can see a list of the appointment comments.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/097.png)

<span id="_Ref206505498" class="anchor"></span>Figure 97: Appointment Comments Window

### Current Day Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To access the current day’s appointments for a patient, the user will need to select the ellipsis, seen in Figure 98, next to an eligible patient within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/098.png)

<span id="_Ref206506012" class="anchor"></span>Figure 98: Action Menu Button for Current Day Appointments

2.  This will cause the action menu to appear. The user will then need to select the “Current Day Appointments” option, seen in Figure 99.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/099.png)

<span id="_Ref206506178" class="anchor"></span>Figure 99: Current Day Appointments Button

3.  The user will be brought to the Current Day Appointments window, shown below in Figure 100, where they can see a list of the patients’ appointments for the day.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/100.png)

<span id="_Ref206506226" class="anchor"></span>Figure 100: Current Day Appointments Window

# Queue Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: Only users that have SD SUPERVISOR Key assigned to them will have the Queue Management tab within PCICSV. Please see <u>Queue</u> for information on how to utilize a Queue.*

The Queue Management page can be navigated to by selecting the “Queue Management” tab shown in Figure 101.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/101.png)

<span id="_Ref206506436" class="anchor"></span>Figure 101: Queue Management Page

## Creating Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a queue, the user will need to select the “Create New Queue” button seen in Figure 102 to open the Create Queue window.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/102.png)

<span id="_Ref206507184" class="anchor"></span>Figure 102: Create New Queue Button

2.  On this window, the user will need to fill in all required information displayed in Figure 103.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/103.png)

<span id="_Ref206507323" class="anchor"></span>Figure 103: Create Queue Window

- Note: Queue names must be greater than 3 characters, but less than 50.
3.  Once all applicable information has been filled, the user will select the “Create Queue” button, seen in Figure 104, to create the new queue.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/104.png)

<span id="_Ref206507878" class="anchor"></span>Figure 104: Create Queue Button

## Editing Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To edit a queue, the user will need to select the ellipsis, seen in Figure 105, next to any queue within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/105.png)

<span id="_Ref206508866" class="anchor"></span>Figure 105: Action Menu Button for Editing Queues

2.  This will cause the action menu to appear. The user will then need to select the “Edit Queue” option, seen in Figure 106, to open the Edit Queue window.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/106.png)

<span id="_Ref206509141" class="anchor"></span>Figure 106: Edit Queue Button

3.  From here, the user can edit the queue name, as shown in Figure 107.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/107.png)

<span id="_Ref206509717" class="anchor"></span>Figure 107: Edit Queue Window

4.  Once the edits have been made, the user will need to select the “Save Changes” button, seen in Figure 108, to save any edits to the queue.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/108.png)

<span id="_Ref206510130" class="anchor"></span>Figure 108: Save Changes Button for Editing Queue

## Deleting Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To delete a queue, the user will need to select the ellipsis, seen in Figure 109, next to any queue within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/109.png)

<span id="_Ref206510350" class="anchor"></span>Figure 109: Action Menu Button for Deleting Queues

2.  This will cause the action menu to appear. The user will then need to select the “Delete Queue” option, seen in Figure 110, to open the Delete Queue window.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/110.png)

<span id="_Ref206510487" class="anchor"></span>Figure 110: Delete Queue Button

3.  The user will need to select the “Delete Queue” button, shown in Figure 111, to confirm deletion.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/111.png)

<span id="_Ref206511364" class="anchor"></span>Figure 111: Delete Queue Window

- Note: A queue can only be deleted if no patients are assigned to it, or if the patients that are assigned to the queue are all in a complete status. If a user attempts to delete a queue where these requirements are not met, they will receive the notice shown below in Figure 112.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/112.png)

> <span id="_Ref206679819" class="anchor"></span>Figure 112: Queue Deletion Error

# Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCICSV allows users to add Veterans to a queue regardless of appointment or whether they are in the VA system so they can request services based on their arrival time. The Queue Page can be navigated to by selecting the “Queue” tab shown in Figure 113.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/113.png)

<span id="_Ref206512733" class="anchor"></span>Figure 113: Queue Page

## Utilizing Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To utilize queues, the user will need to select the “Select Queue” dropdown shown in Figure 114. From here, the user can either scroll and locate a queue or type and search for a specific queue.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/114.png)

<span id="_Ref206513370" class="anchor"></span>Figure 114: Select Queue Dropdown

2.  Once the queue is selected, the Queue List page will be displayed. The user will need to select the “Add Patient” button, shown in Figure 115, to add patients to the queue.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/115.png)

<span id="_Ref206514334" class="anchor"></span>Figure 115: Add Patient Button

3.  The Add Patient to Queue window will appear (see Figure 116 for example). On this window, the user can choose to search for a patient already in the system or manually add a patient.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/116.png)

<span id="_Ref206514632" class="anchor"></span>Figure 116: Add Patient to Queue Window

4.  Once either the Patient Search field or the Manually Add Patient field is populated, the user can select the “Add” button, shown in Figure 117, to add the patient to the queue.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/117.png)

<span id="_Ref206514648" class="anchor"></span>Figure 117: Add Patient to Queue Button

- Note: The user can select the “Close” button seen in Figure 118 to exit from adding a patient to the queue and return to the Queue List page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/118.png)

> <span id="_Ref206514819" class="anchor"></span>Figure 118: Close Button on the Add Patient to Queue Window

5.  The user will return to the Queue List page where the grid will refresh with the added patient. Repeat steps 2-4 to add more patients to the queue as needed.

## Queue List Memos

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users can add a memo to a specific patient in the queue by selecting the “New” button shown in Figure 119.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/119.png)

<span id="_Ref206515022" class="anchor"></span>Figure 119: New Memo Button for Queue Patients

2.  The user will be brought to the Add New Memo to Visit window, shown in Figure 120. From here, users may add a memo that is up to 100 characters.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/120.png)

<span id="_Ref206515106" class="anchor"></span>Figure 120: Add New Memo to Visit for Queue Patients

- Note: Users may also choose to view all previous memos from this page. Simply select the View All Memos button, shown in Figure 121, to expand the window with all previously entered memos.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/121.png)

> <span id="_Ref206515435" class="anchor"></span>Figure 121: View All Memos Button for Queue Patients

3.  Once the memo has been entered, select the “Add Memo” button, shown in Figure 122 to add the memo to the visit.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/122.png)

> <span id="_Ref206515453" class="anchor"></span>Figure 122: Add Memo Button for Queue Patients

- Note: The user can select the “Close” button seen in Figure 123 to cancel adding a memo to a visit. This will take the user back to the Queue List page.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/123.png)

> <span id="_Ref206683426" class="anchor"></span>Figure 123: Close Button for Adding Memo to Visit

4.  The user will then return to the Queue List page, where the memo will be displayed in the Memo column of the related patient with a timestamp and the initials of the user (see Figure 124 for example).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/124.png)

<span id="_Ref206683427" class="anchor"></span>Figure 124: Example of Memo Entered in Queue List

- When users add more than one memo to a visit, the “All” button will appear in the Memo column of the grid as seen in Figure 125. When selected, the user will be brought to the View All Memos for Queued Patient window where they can see all previous memos for the visit.

  ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/125.png)

> <span id="_Ref206515468" class="anchor"></span>Figure 125: All Memos Button for Queue Patients

## Marking Visit as Complete/Undo Mark as Complete in Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To mark a visit as complete, the user will need to select the ellipsis, seen in Figure 126, next to a visit within the grid.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/126.png)

<span id="_Ref206584843" class="anchor"></span>Figure 126: Action Menu Button for Marking a Patient Complete

2.  This will cause the action menu to appear. The user will then need to select the “Mark as Complete” option, seen in Figure 127.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/127.png)

<span id="_Ref206585001" class="anchor"></span>Figure 127: Mark as Complete Button

3.  Once selected, the grid will refresh and mark the visit as complete (see Figure 128 for example).

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/128.png)

<span id="_Ref206585364" class="anchor"></span>Figure 128: Patient Marked as Complete in Grid of Queue List

4.  If the visit is not completed and the completion needs to be undone, the user will need to select the ellipsis again and select the “Undo Mark as Complete” option, shown in Figure 129. This will cause the grid to refresh and update the visit as not completed.

> ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/129.png)

<span id="_Ref206585533" class="anchor"></span>Figure 129: Undo Mark as Complete Button

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Alert Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whenever a change to the Daily Workflow List occurs, an alert notification will be displayed on the Windows taskbar (see Figure 130). Even if the PCICSV application is in the background, there will still continue to be notifications sent via the taskbar to inform staff of any changes. Changes that trigger an alert include a new appointment on the list or workflow status change.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/130.png)

<span id="_Ref206585867" class="anchor"></span>Figure 130: PCICSV Alert Notification

If there is an update on the Daily Workflow List while the user has the application open, the row added or changed will be highlighted as seen Figure 131.

![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/131.png)

<span id="_Ref206586435" class="anchor"></span>Figure 131: Update to Daily Workflow Example

## Icon Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Icon                                                                                                                              | Description                                    |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/132.png) | Denotes a walk-in appointment                  |
| ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/133.png)         | Denotes a patient has successfully eChecked In |

<span id="_Toc221538984" class="anchor"></span>Table 2: Flags

## Flag Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Flag                                                                                                                              | Description                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/134.png)  | Fugitive Felon                                                                                                                                                  |
| ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/135.png) | Sensitive Record – User will see a pop-up notification before viewing a sensitive record. Viewing additional information about this patient will also be logged |
| ![](patient-check-in-clinical-staff-viewer-pcicsv-user-guide/136.png)  | National/Local                                                                                                                                                  |

<span id="_Toc221538985" class="anchor"></span>Table 3: Acronyms and Abbreviations

## Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term   | Description                                                     |
|--------|-----------------------------------------------------------------|
| IAM    | Identity and Access Management                                  |
| PIV    | Personal Identity Verification                                  |
| SSOi   | Single Sign-On Internal                                         |
| VA     | Department of Veterans Affairs                                  |
| VHA    | Veterans Health Administration                                  |
| VistA  | Veterans Health Information Systems and Technology Architecture |
| VS     | VistA Scheduling                                                |
| VSE    | VistA Scheduling Enhancements                                   |
| PCICSV | Patient Check In Clinical Staff Viewer                          |
| ISS    | Integrated Scheduling Solution                                  |