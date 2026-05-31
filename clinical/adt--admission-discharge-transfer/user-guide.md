---
title: Integrated Scheduling Solution (ISS) Release 1.22.3 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: null
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: archive
pkg_ns: ADT
patch_ver: 1.22.3
patch_id: ADT*1.22.3
group_key: ADT:ADT:1.22.3
file_numbers: []
security_keys:
- SD SUPERVISOR
- SDMOB
- SDOB
menu_options: 4
description: '''Table 1: ISS User Profiles 12 [Table 2: List of Cancellation Reasons'''
audience: End users and package coordinators (ADPAC)
keywords: []
page_count: 0
word_count: 15109
section_count: 32
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: June 2025
revision_count: 15
revision_newest: 6/10/2025
revision_oldest: 7/31/2024
docx_url: https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/iss_release_1_22_3_user_guide.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/iss_release_1_22_3_user_guide.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=327
audit_applied: '2026-05-31'
master_source: Integrated Scheduling Solution (ISS) Release 1.22.3 User Guide
master_pub_date: June 2025
consolidated_from: 14 versions
prior_versions:
- Integrated Scheduling Solution (ISS) Release 1.11.11 User Guide
- Integrated Scheduling Solution (ISS) Release 1.12.0 User Guide
- Integrated Scheduling Solution (ISS) Release 1.13.3 User Guide
- Integrated Scheduling Solution (ISS) Release 1.14.1 User Guide
- Integrated Scheduling Solution (ISS) Release 1.15.4 User Guide
- Integrated Scheduling Solution (ISS) Release 1.16.1 User Guide
- Integrated Scheduling Solution (ISS) Release 1.17.2 User Guide
- Integrated Scheduling Solution (ISS) Release 1.18.10 User Guide
- Integrated Scheduling Solution (ISS) Release 1.19.1 User Guide
- Integrated Scheduling Solution (ISS) Release 1.21.2 User Guide
- Integrated Scheduling Solution (ISS) Release 1.5.4.0 User Guide
- Integrated Scheduling Solution (ISS) Release 1.7.1.0 User Guide
- Integrated Scheduling Solution (ISS) Release 1.8.6.0 User Guide
consolidated_title: integrated scheduling solution (iss) user guide
---

OFFICE OF  
INFORMATION  
AND TECHNOLOGY

Integrated Scheduling SolutionUser Guide

June 2025
## List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Table 1: ISS User Profiles [12](#_Ref491934432)](#_Ref491934432)
[Table 2: List of Cancellation Reasons [162](#_Toc165637562)](#_Toc165637562)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date       | Version | Description                                                                                                                                                                                          | Author              |
|------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| 6/10/2025  | 1.22.3  | Added Section on Temporary Address Feature, Updated UI Changes in Demographics section                                                                                                               | Booz Allen Hamilton |
| 6/4/2025   | 1.21.2  | Updated section 6 and added subsection on Recurring Slot Availability                                                                                                                                | Booz Allen Hamilton |
| 4/15/2025  | 1.19.1  | Added information on Refresh button to section 2.3.8 and Disposition confirmation to section 4.2.4                                                                                                   | Booz Allen Hamilton |
| 3/28/2025  | 1.18.10 | Updated UI for section 4.2, added information on new Action menu on Viewing Requests page                                                                                                            | Liberty ITS         |
| 3/17/2025  | 1.17.2  | Added information on Active Prescriptions to the Demographics section, updated ISS link                                                                                                              | Liberty ITS         |
| 2/19/2025  | 1.16.1  | Added sections on Duplicate Appointment Requests for Clinic/Service, added information on duplicate appointment requests to APPT and PtCSch sections, updated UI changes in APPT and PtCSch sections | Liberty ITS         |
| 1/30/2025  | 1.15.4  | Updated information on Comment Tracking, Cancellation Reasons, and Video Visits, removed information on Column filters, added information on orphaned requests to MRTC section                       | Liberty ITS         |
| 1/06/2025  | 1.14.0  | Added information on Comment Tracking and a section on the Scheduling Activity Report                                                                                                                | Liberty ITS         |
| 11/22/2024 | 1.13.3  | Removed Show/Hide Columns section, added section on Refresh Table, added information on VVC Ready and Undo Check out                                                                                 | Liberty ITS         |
| 11/05/2024 | 1.12.0  | Updated UI changes in the Check In section                                                                                                                                                           | Liberty ITS         |
| 10/29/2024 | 1.11.11 | Updated UI changes in the Patient Overview section, and in the System section                                                                                                                        | Liberty ITS         |
| 10/02/2024 | 1.11.2  | Updated UI changes in the Introduction and Contact Attempts section, removed information on VVC Ready Status                                                                                         | Liberty ITS         |
| 8/29/2024  | 1.8.6   | Updated Video Visits section to reflect UI changes                                                                                                                                                   | Liberty ITS         |
| 8/14/2024  | 1.7.1   | Added section about the demographics banner                                                                                                                                                          | Liberty ITS         |
| 7/31/2024  | 1.5.4   | First Release for ISS User Guide                                                                                                                                                                     | Liberty ITS         |

<span id="_Toc165637562" class="anchor"></span>Table 2: List of Cancellation Reasons

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [List of Figures](#list-of-figures)
  - [List of Tables](#list-of-tables)
  - [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Prerequisite Credentials](#prerequisite-credentials)
  - [PIV Login](#piv-login)
- [Familiarizing Yourself with ISS](#familiarizing-yourself-with-iss)
  - [Home Page](#home-page)
    - [Changing Site Locations](#changing-site-locations)
    - [Veteran Requests Report](#veteran-requests-report)
    - [Additional Links](#additional-links)
  - [My Account](#my-account)
    - [User Preferences](#user-preferences)
    - [Logging Out of ISS](#logging-out-of-iss)
  - [Filters](#filters)
    - [Column Order](#column-order)
    - [Sort by Ascending and Descending](#sort-by-ascending-and-descending)
    - [Toggle Density](#toggle-density)
    - [Show, Hide, and Search Filters](#show-hide-and-search-filters)
    - [Filtering Rows](#filtering-rows)
    - [Reset Filters](#reset-filters)
    - [Refresh Table](#refresh-table)
    - [Filtering & Navigating on Calendar](#filtering-navigating-on-calendar)
    - [Pending Appointments & Appointment History](#pending-appointments-appointment-history)
- [Patient Overview](#patient-overview)
  - [Patient Search](#patient-search)
  - [Patient Profile Home](#patient-profile-home)
  - [Appointments & Requests](#appointments-requests)
  - [Demographics](#demographics)
    - [Demographics Banner](#demographics-banner)
    - [Temporary Address](#temporary-address)
  - [Patient Inquiry](#patient-inquiry)
  - [Medication](#medication)
- [Patient Appointments and Requests](#patient-appointments-and-requests)
  - [Creating Appointment Requests](#creating-appointment-requests)
    - [APPT](#appt)
    - [PtCSch (Recall)](#ptcsch-recall)
    - [MRTC](#mrtc)
    - [Consult/Procedure](#consultprocedure)
    - [RTC](#rtc)
    - [VETERAN](#veteran)
    - [Dispositioning Duplicate Clinic Requests](#dispositioning-duplicate-clinic-requests)
    - [Dispositioning Duplicate Service Requests](#dispositioning-duplicate-service-requests)
  - [Appointment Request Actions](#appointment-request-actions)
    - [Viewing Appointment Requests](#viewing-appointment-requests)
    - [Editing Appointment Requests](#editing-appointment-requests)
    - [Contact Attempts](#contact-attempts)
    - [Disposition an APPT, RTC, or VETERAN Request](#disposition-an-appt-rtc-or-veteran-request)
    - [Disposition a PtCSch Request](#disposition-a-ptcsch-request)
    - [Disposition an MRTC Parent Request](#disposition-an-mrtc-parent-request)
    - [Disposition an MRTC Child Request](#disposition-an-mrtc-child-request)
  - [Creating a Pending Appointment](#creating-a-pending-appointment)
    - [APPT](#appt-1)
    - [PtCSch (Recall)](#ptcsch-recall-1)
    - [MRTC](#mrtc-1)
    - [Consult/Procedure](#consultprocedure-1)
    - [RTC](#rtc-1)
    - [VETERAN](#veteran-1)
    - [Overbooking an Appointment](#overbooking-an-appointment)
    - [MISSION Act](#mission-act)
    - [Clinic Stop Code](#clinic-stop-code)
    - [Patient Conflicts](#patient-conflicts)
  - [Appointment Actions](#appointment-actions)
    - [View](#view)
    - [Edit](#edit)
    - [Cancel an APPT, PtCSch, Consult/Procedure, RTC, or VETERAN Appointment](#cancel-an-appt-ptcsch-consultprocedure-rtc-or-veteran-appointment)
    - [Cancel an MRTC Appointment](#cancel-an-mrtc-appointment)
    - [Expand Entry](#expand-entry)
    - [Block and Move](#block-and-move)
    - [Check In](#check-in)
    - [Undo Check In](#undo-check-in)
    - [Undo Check Out](#undo-check-out)
    - [Mark as No Show](#mark-as-no-show)
    - [Undo Mark as No Show](#undo-mark-as-no-show)
    - [Calendar View](#calendar-view)
    - [Letter Printing](#letter-printing)
  - [Video Visits](#video-visits)
    - [Creating Video Visits](#creating-video-visits)
    - [Viewing Video Visits](#viewing-video-visits)
    - [Editing Video Visits](#editing-video-visits)
    - [Resending Video Visits](#resending-video-visits)
    - [Cancelling Video Visits](#cancelling-video-visits)
    - [Launch Video Visit](#launch-video-visit)
  - [Printing and Exporting Reports for Appointments and Requests](#printing-and-exporting-reports-for-appointments-and-requests)
    - [Export an Appointment Requests Report](#export-an-appointment-requests-report)
    - [Print for Appointments](#print-for-appointments)
- [Calendar Search](#calendar-search)
  - [Clinic Search](#clinic-search)
  - [Provider Search](#provider-search)
  - [Clinic Group Search](#clinic-group-search)
  - [Create Walk-in](#create-walk-in)
- [Reports](#reports)
  - [Query Tool](#query-tool)
    - [Section 1](#section-1)
    - [Section 2](#section-2)
    - [Section 3](#section-3)
  - [Recurring Slot Availability](#recurring-slot-availability)
- [System](#system)
  - [Privileged Users](#privileged-users)
  - [Clinic Groups](#clinic-groups)
    - [Edit Clinic Group](#edit-clinic-group)
    - [Remove Clinic Group](#remove-clinic-group)
    - [Creating New Clinic Groups](#creating-new-clinic-groups)
  - [Activity Report](#activity-report)
- [References](#references)
  - [Cancellation Reasons](#cancellation-reasons)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Integrated Scheduling Solution (ISS) is a web version of the VistA Scheduling Enhancements (VSE) GUI, utilizing the JavaScript React framework and providing equivalent appointment management functions used in the original application. The purpose of ISS is to deliver users with a modernized look and feel while reducing operating costs and improving operational efficiencies. With this document, users can familiarize themselves with important features and navigational elements of ISS, including patient search, patient appointments and requests, calendar search, query tool, privileged user functionality, and clinic group creation.

This document is intended for ISS users supporting the Veterans Health Administration (VHA). See below for details on the authorized users and their responsibilities.

<span id="_Ref491934432" class="anchor"></span>Table 1: ISS User Profiles

| User                  | Description and Responsibilities                                                                                                                                                    |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scheduler             | Users responsible for creating and processing patient requests and scheduling appropriate care.                                                                                     |
| Scheduling Supervisor | Users can create requests and schedule appointments. These users also have additional capabilities such as creating clinic groups or adding privileged users to prohibited clinics. |
| View Only             | This user profile is intended for those who need the ability to view clinic schedules and patient appointment information, but do not need the ability to schedule appointments.    |

JLV User ProfilesDescription of each JLV user profile

## Prerequisite Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user's PIV card must be linked to the VistA site (See [link](https://urldefense.com/v3/__https:/yourit.va.gov/kb_view.do?sysparm_article=KB0013359__;!!May37g!IDPcRnXuA41Qsx8l5PC9V-RCPZs-oQgJY5ff0TiThG5w5YC5glJL3EhBNB3EloD_HTbfRTs9JzMgV8wVvNcmw-Ke$) for guidance).
2.  After confirming that the user's PIV card is linked to the user's VistA account, the user will be able to sign into the ISS.
3.  The user will also need to ensure that the specific VistA keys are assigned to their account before being able to complete certain tasks. Schedulers will need SDECZMENU. Scheduling Supervisors will need SDECZMGR. For overbook privileges, users will need either SDOB or SDMOB (See <u>4.3.7 Overbooking an Appointment</u> for more information).
- Note: For users who do not have the appropriate keys, please contact your Supervisor or [yourIT](https://yourit.va.gov/va) for assistance.

## PIV Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Begin by opening a browser and going to the following web address: [ISS - Home Page (va.gov)](https://staff.apps.va.gov/iss/). The VA Single Sign-On page will then appear. Select the "Sign in with PIV" option, as seen in Figure 1, to proceed with the log in process.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/001.png)

> <span id="_Ref173328413" class="anchor"></span>Figure 1: PIV Card Sign-On Image

2.  After selecting, an ActivClient Login dialog box will appear to prompt you to enter your PIN. Type the numbers of your PIN as prompted in Figure 2. If authentication is successful, ISS will load. If it is not successful, you will be prompted to enter your correct PIN instead.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/002.png)

> <span id="_Ref173328442" class="anchor"></span>Figure 2: ActivClient Login Pop-Up Window

# Familiarizing Yourself with ISS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once log in is complete, users will see the ISS homepage as seen in Figure 3.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/003.png)

> <span id="_Ref165299674" class="anchor"></span>Figure 3: ISS Home Page

### Changing Site Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To change site locations, the user must first select the site location dropdown in the upper right-hand corner of the page as shown in Figure 4.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/004.png)

> <span id="_Ref165299721" class="anchor"></span>Figure 4: Site Locations

2.  The user will then need to select the requested site location by clicking the arrow shown in Figure 5 if it is not already the default selection.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/005.png)

> <span id="_Ref165299739" class="anchor"></span>Figure 5: Dropdown Arrow for Changing Site Locations

- Note: The user will only see sites that are provisioned to their account after selecting the arrow shown in Figure 5. If sites assigned to the user are not shown, please contact the local Clinical Applications Coordinator or Supervisor for assistance.
3.  The user can then select the "Select" button seen below in Figure 6 to view the chosen site.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/006.png)

> <span id="_Ref165299794" class="anchor"></span>Figure 6: Select Button on Changing Site Locations Window

- Note: The "Close" button shown in Figure 7 can be selected at any time to close the pop-up window and continue with the default site location.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/007.png)

> <span id="_Ref165299812" class="anchor"></span>Figure 7: Close Button on Changing Site Locations Window

### Veteran Requests Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To export a Veteran Request report, the user can select the "Run Veteran Request Report" button seen in Figure 8.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/008.png)

> <span id="_Ref165299840" class="anchor"></span>Figure 8: Run Veteran Request Report Button

2.  After selecting the button, the Veteran Requests page, seen in Figure 9, will display.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/009.png)

> <span id="_Ref165299879" class="anchor"></span>Figure 9: Veteran Requests Report Page

- Note: The report will only include the first 200 requests.
3.  To export, select the "Export Veteran Report" button seen in Figure 10. This will allow the user to download the report into an Excel document.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/010.png)

> <span id="_Ref165299924" class="anchor"></span>Figure 10: Export Veteran Report Button

### Additional Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can locate links at the bottom of the ISS page within the "Getting Started with ISS" and "Help" sections for additional information. Links may vary depending on user and location. See Figure 11 below for reference.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/011.png)

> <span id="_Ref165299940" class="anchor"></span>Figure 11: Example of Additional Links for ISS

## My Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To change user preferences, the user can select the "My Account" button in the upper right-hand corner, seen in Figure 12, to open the dropdown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/012.png)

> <span id="_Ref165299955" class="anchor"></span>Figure 12: Selecting My Account Icon when Changing Preferences

2.  The user can then select the "Preferences" button, seen in Figure 13, to be taken to the User Preferences page.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/013.png)

> <span id="_Ref165299979" class="anchor"></span>Figure 13: Preferences Button

3.  To adjust the default order of Pending Appointments and Appointment Requests, drag and drop the different selections as seen in Figure 14 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/014.png)

> <span id="_Ref165299999" class="anchor"></span>Figure 14: Adjusting Pending Appointments and Appointment Request Column Order from Preferences

4.  The user can then select the "Save" button seen in Figure 15 to save their changes.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/015.png)

> <span id="_Ref165300016" class="anchor"></span>Figure 15: Save Button for Appointments and Requests Column Order

5.  To change the default calendar view for Clinic Schedule, select the arrow shown in Figure 16.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/016.png)

> <span id="_Ref165300035" class="anchor"></span>Figure 16: Dropdown Arrow for Changing Default Calendar View

6.  Once the dropdown displays, the user can select their preferred view option from the list seen below in Figure 17.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/017.png)

> <span id="_Ref165300055" class="anchor"></span>Figure 17: Dropdown View of Calendar View Selections

7.  The user can then select the "Save" button seen in Figure 18 to save their changes.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/018.png)

> <span id="_Ref165300072" class="anchor"></span>Figure 18: Save Button for Calendar View Preference

8.  To reset preferences, select the "Reset to Default" button within the individual sections as seen in Figure 19.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/019.png)

> <span id="_Ref165300086" class="anchor"></span>Figure 19: Reset to Default Button for Preferences

### Logging Out of ISS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To log out of ISS, the user will need to select the "My Account" button in the upper right-hand corner, as seen in Figure 20, to open the dropdown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/020.png)

> <span id="_Ref165300107" class="anchor"></span>Figure 20: Selecting My Account Icon when Logging Out

2.  The user will then select the "Log out" button shown below in Figure 21.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/021.png)

> <span id="_Ref165300124" class="anchor"></span>Figure 21: Log Out Button from My Account Dropdown

3.  Upon logging out of the ISS application, the user will be taken to the page seen in Figure 22 that will prompt them to log out of the VA SSOi and close the browser.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/022.png)

> <span id="_Ref165300148" class="anchor"></span>Figure 22: Logged Out of Mobile Applications Page

- Note: If you are logged in but not actively using ISS, the user will automatically be logged out after 15 minutes (see Figure 23 for reference).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/023.png)

> <span id="_Ref165300175" class="anchor"></span>Figure 23: User Session is Ending Notification

## Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Column Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When looking for availability within the grid, the user can rearrange the column order. To begin, the user will need to select the "Move" button pictured in Figure 24 to grab the column.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/024.png)

> <span id="_Ref165300234" class="anchor"></span>Figure 24: Move Button from Grid View

2.  The user can then move the column to a different spot by dragging the column and dropping it in the desired spot seen in Figure 25.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/025.png)

> <span id="_Ref165300260" class="anchor"></span>Figure 25: Example of Changing Column Order from Grid View

### Sort by Ascending and Descending

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When looking for availability within the grid, the user can sort rows within the table. To begin, the user will need to select the vertical ellipsis next to the desired column, as seen below in Figure 26.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/026.png)

> <span id="_Ref165300400" class="anchor"></span>Figure 26: Selecting Column Actions Button to Sort Order

2.  The user can then select either "Sort by (Column Name) Ascending" or "Sort by (Column Name) descending" to sort rows in an ascending or descending order within the table, outlined within Figure 27.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/027.png)

> <span id="_Ref165300427" class="anchor"></span>Figure 27: Sort Options for Table Information

3.  To return the sorting to default, the user will need to select the vertical ellipsis seen in figure x, then select the "Clear Sort" button shown in Figure 28.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/028.png)

> <span id="_Ref165300462" class="anchor"></span>Figure 28: Clear Sort Button

4.  Optionally, the user can sort rows by hovering the cursor next to a column's name and selecting the arrow button that appears in Figure 29.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/029.png)

> <span id="_Ref165300493" class="anchor"></span>Figure 29: Sort Order Button

5.  Selecting the arrow once will cause results to sort by ascending order (↑), a second time to sort by descending order (notated by ↓), and a third time to cause results to appear in the default order again (notated with no arrow).

### Toggle Density

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When looking for availability within the grid, the option to adjust the toggle density is available. To begin adjusting the toggle density, select the button shown in Figure 30.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/030.png)

> <span id="_Ref165300704" class="anchor"></span>Figure 30: Toggle Density Button

2.  There are three different options for the user to choose from depending on the user's preference. Simply keep selecting the "Toggle Density" button to rotate through the options until the user finds their preferred density.

### Show, Hide, and Search Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When looking for availability within the grid, the option to show and hide filters is available. To begin the user will need to select the "Show/Hide Filters" button, or the "Filter by (Column Name)"button, both shown in Figure 31. Selecting either will cause the search functions to appear under each column name.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/031.png)

> <span id="_Ref165300734" class="anchor"></span>Figure 31: Show/Hide Filter Options Buttons

2.  Once the search options appear as seen in Figure 32, the user can select the search bar or dropdown menu under the desired column to be filtered and enter or select the required information needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/032.png)

> <span id="_Ref165300749" class="anchor"></span>Figure 32: Example of Filter Search Menu on Grid View

3.  Once the filter field has been populated, results will automatically refresh and show items based on the filtered criteria as seen below in Figure 33.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/033.png)

> <span id="_Ref165300767" class="anchor"></span>Figure 33: Example of Filtered Results in Grid View

4.  To clear the search, the user will need to select the "X" next to the search bar seen in Figure 34. Selecting this will cause all results to appear within the table.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/034.png)

> <span id="_Ref165300795" class="anchor"></span>Figure 34: Clearing Filter Button

5.  Once finished searching, the user can then select the "Show/Hide Search" button seen in Figure 35 to hide the search bar.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/035.png)

> <span id="_Ref165300814" class="anchor"></span>Figure 35: Selecting Show/Hide Filters Button to Hide Filter Menu

### Filtering Rows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users can increase or decrease the number of rows shown on the page by selecting the arrow shown in Figure 36.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/036.png)

> <span id="_Ref165300837" class="anchor"></span>Figure 36: Arrow Button for Changing Row Number

2.  Users can also navigate the table to more available timeslots by selecting the arrows, shown in Figure 37 from left to right as follows; "\|\<" to jump to the first page, "\<" to navigate one page backwards, "\>" to navigate one page forwards, and "\>\|" to jump to the last page.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/037.png)

> <span id="_Ref165300858" class="anchor"></span>Figure 37: Buttons for Navigating Result Pages on Grid View

- Note: Arrows will be greyed out and un-selectable if the user cannot navigate in a certain direction.

### Reset Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To reset any filters that are set on either the "Appointments" or "Appointment Requests" grids, the user can select the "Reset Filters" button, as seen in Figure 38.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/038.png)

> <span id="_Ref165300877" class="anchor"></span>Figure 38: Reset Filters Button on Grid View

### Refresh Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To refresh the table for either the "Appointments" or "Appointment Requests" grids, the user can select the "Refresh Table" button, as seen in Figure 39.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/039.png)

> <span id="_Ref182923394" class="anchor"></span>Figure 39: Refresh Table Button

### Filtering & Navigating on Calendar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To navigate through the calendar, the user can use the arrows shown in Figure 40.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/040.png)

> <span id="_Ref165300891" class="anchor"></span>Figure 40: Arrow Buttons on Calendar to Change Dates

2.  Optionally, the user can choose a specified date, as highlighted in Figure 41, by selecting the arrow to the right of the date.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/041.png)

> <span id="_Ref165300908" class="anchor"></span>Figure 41: Mini Calendar on Calendar View to Choose Specific Date

3.  Users can also choose to view the calendar in Day, Week, or Month mode by selecting the associated button shown below in Figure 42.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/042.png)

> <span id="_Ref165300929" class="anchor"></span>Figure 42: Changing Default Calendar View from Calendar

4.  The user can also select the "Today" button, seen in Figure 43, at any point to bring the calendar back to the current date.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/043.png)

> <span id="_Ref165300950" class="anchor"></span>Figure 43: Bringing Calendar Back to Current Date on Calendar View

- Note: The user can refresh the calendar at any time by selecting the "Refresh" button seen in Figure 44.

  ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/044.png)

> <span id="_Ref195617362" class="anchor"></span>Figure 44: Refresh Button on Calendar

### Pending Appointments & Appointment History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the "Appointments" section found within <u>3.3 Appointments & Requests,</u> users can navigate between pending appointments and appointment history for a selected patient. To do so, the user can simply select the desired tab to update the appointment list with the corresponding tab. Please see Figure 45 for a description on which appointments will appear where depending on the corresponding status.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/045.png)

> <span id="_Ref165300982" class="anchor"></span>Figure 45: Information on the Pending and History Tabs for Appointments

# Patient Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To search for a patient, the user will select the search bar, seen in Figure 46, and enter valid search criteria. Once entering the information, a list of patients will appear in a dropdown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/046.png)

> <span id="_Ref165301006" class="anchor"></span>Figure 46: Patient Search Bar

- Note: See Figure 47 below for a list of valid search criteria for patient search.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/047.png)

> <span id="_Ref165301025" class="anchor"></span>Figure 47: Valid Search Criteria for Patient Search

2.  The user will then select the intended patient from the available options.
3.  Once a patient is selected, the user will need to read the "Patient Eligibility" window, shown in Figure 48, and select "Acknowledge Eligibility" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/048.png)

> <span id="_Ref165301082" class="anchor"></span>Figure 48: Patient Eligibility Notification

- Note: The user is able to select "Expand" to see more information about the patient in context (see <u>3.4.1 Demographics Banner</u> for more information).
4.  To view information or interact with the patient, the user will need to select the "Patient" tab seen in Figure 49.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/049.png)

> <span id="_Ref165301144" class="anchor"></span>Figure 49: Patient Tab from the Home Screen

5.  To bring a new patient into context, the user will need to select the "Clear" button seen below in Figure 50. The page will automatically reload and "No Patient in Context" will be shown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/050.png)

> <span id="_Ref165301162" class="anchor"></span>Figure 50: Clear Button for Patient Search

6.  The user is then able to search for a new patient. To load the last selected patient, the user can select the "Load Last Selected" button, seen in Figure 51, or type "spacebar + enter" into the search bar.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/051.png)

> <span id="_Ref165301183" class="anchor"></span>Figure 51: Load Last Selected Button for Patient Search

## Patient Profile Home

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Profile Page can be navigated to by selecting the "Patient Profile Home" tab shown in Figure 52. This page gives a brief overview of the patient's information.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/052.png)

> <span id="_Ref165301199" class="anchor"></span>Figure 52: Example of Patient Profile Home Tab

## Appointments & Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Appointments & Requests Page can be navigated to by selecting the "Appointments & Requests" tab shown in Figure 53. The user can use this page to view and schedule appointments and requests. For more information on how to do this please visit <u>Patient Appointments and Requests</u>.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/053.png)

> <span id="_Ref165301214" class="anchor"></span>Figure 53: Example of Appointments & Requests Tab

## Demographics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Demographics Page can be navigated to by selecting the "Demographics" tab shown in Figure 54.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/054.png)

> <span id="_Ref165301229" class="anchor"></span>Figure 54: Demographics Tab

2.  Users can edit the fields that appear within the Demographics page as shown in Figure 55 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/055.png)

> <span id="_Ref165301250" class="anchor"></span>Figure 55: Example of the Demographics Page

- Note: The user can edit the fields under "Contact Information" by either selecting the "+" button next to an individual row, or by selecting "Expand all +.
- Note: When editing a patient's mailing address who has an active prescription, the user will receive a notification asking to confirm the location change of where the prescriptions are being sent (see Figure 56 below).

  ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/056.png)

> <span id="_Ref193190884" class="anchor"></span>Figure 56: Mailing Address Change Notification with Active Prescription

- Note: When editing Special Needs and Preferences, the user can add remarks to any of the individual options seen below in Figure 57. To leave a remark, the user will first need to select an option in the special needs/preferences section. Once selected, the Remarks field will become available to edit.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/057.png)

> <span id="_Ref168577336" class="anchor"></span>Figure 57: Special Needs/Preferences Options

3.  Once the user has made their preferred edits to the patient's demographics, the user will need to select "Save Changes", as seen in Figure 58, to save any changes made.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/058.png)

> <span id="_Ref165301278" class="anchor"></span>Figure 58: Save Changes Button for the Demographics Page

- Note: The user can verify the patient's demographics by selecting "Verify Demographics" seen in Figure 59.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/059.png)

> <span id="_Ref165301367" class="anchor"></span>Figure 59: Verify Demographics Button

- *Note: If the User would like to undo any changes made within the demographics page, they can select "Undo Changes" at any time as seen in Figure 60.*

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/060.png)

> <span id="_Ref165301398" class="anchor"></span>Figure 60: Undo Changes Button for Demographics Page

### Demographics Banner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Demographics banner is located at the top of the page and is populated with the patient's information when a patient is brought into context. Users may select the expand button, as seen in Figure 61, to see more information regarding the selected patient and their demographics.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/061.png)

> <span id="_Ref174546745" class="anchor"></span>Figure 61: Demographics Banner Expand Button

By default, the user will be able to see the patient's name, DOB, any patient flags (if applicable), VVC status, birth sex, patient type, and SSN (Last 4). Users can select the Special Needs/Preferences dropdown to see what is currently associated with the patient. If any edits are needed, the user can select the Demographics link, underlined in Figure 62, to take them to the Demographics tab (see <u>3.4 Demographics</u> for more information on editing).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/062.png)

> <span id="_Ref174546746" class="anchor"></span>Figure 62: Demographics Link in the Special Needs/Preferences Dropdown

The user can also select the Patient Eligibility dropdown seen in Figure 63 to view more specific information about the patient's eligibility and health conditions.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/063.png)

> <span id="_Ref174546747" class="anchor"></span>Figure 63: Patient Eligibility Dropdown

- Note: If the patient has joined at least 3 video visit appointments within the past 120 days, the VVC status will state "VVC READY" and be green (see Figure 64). For more information on video visits please see <u>4.5 Video Visits</u>.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/064.png)

> <span id="_Ref182927193" class="anchor"></span>Figure 64: VVC Ready Pill

### Temporary Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users may find the need to edit a patients address to a temporary address. To do so the user will need to select the "+" symbol, shown below in Figure 65, to expand the temporary address accordion.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/065.png)

<span id="_Ref200453186" class="anchor"></span>Figure 65: Temporary Address Accordion Expand Button

2.  Once the accordion has been expanded, the user will need to activate the temporary address function by selecting the "Activate Temporary Address" toggle button seen in Figure 66.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/066.png)

<span id="_Ref200453206" class="anchor"></span>Figure 66: Activate Temporary Address Toggle Button

3.  The user will then need to fill out all the required information displayed in Figure 67, as well as any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/067.png)

<span id="_Ref200453235" class="anchor"></span>Figure 67: Temporary Address Information Example

- Note: Users may receive the validation notification, seen in Figure 68, that prompts users to review if the address entered is accurate. If the information is incorrect, the user will need to select cancel and fix the address entered. If the address is correct, the user can select the "Use this address" button and then select OK to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/068.png)

> <span id="_Ref200453264" class="anchor"></span>Figure 68: Address Validation Failed Notification

4.  Once all applicable information has been filled, the user will select the "Save Changes" button, seen in Figure 69, to save the temporary address.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/069.png)

<span id="_Ref200453286" class="anchor"></span>Figure 69: Save Changes Button for Temporary Address

- Note: Users will receive the notification shown in Figure 70 when accessing the demographics page of a patient whose temporary address will soon expire. The user will need to select Acknowledge to proceed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/070.png)

> <span id="_Ref200453306" class="anchor"></span>Figure 70: Temporary Address Expiring Soon Notification

- Note: The temporary address will be shown in the demographics banner of the patient with an active temporary address (see Figure 71).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/071.png)

> <span id="_Ref200453332" class="anchor"></span>Figure 71: Active Temporary Address in Demographics Banner Example

## Patient Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Inquiry Page can be navigated to by selecting the "Patient Inquiry" tab shown in Figure 72. On this page, users can view information about the patient such as contact information, demographics, status, future appointments, etc.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/072.png)

> <span id="_Ref165301458" class="anchor"></span>Figure 72: Example of Patient Inquiry Tab

## Medication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medication Page can be navigated to by selecting the "Medication" tab shown in Figure 73. This page will list any medications the patient uses or have been prescribed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/073.png)

> <span id="_Ref165301478" class="anchor"></span>Figure 73: Example of Medication Tab

# Patient Appointments and Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all the following sections within <u>Patient Appointments and Requests</u>, the user will first need to bring a patient into context. The user can find information on how to do so by following the steps outlined in <u>3.1 Patient Search</u>.

## Creating Appointment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### APPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a new APPT request, the user will first need to select "New Request," as shown in Figure 74.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/074.png)

> <span id="_Ref165301496" class="anchor"></span>Figure 74: New Requests Button for APPT Requests

2.  The user will then select "APPT" from the dropdown that appears in Figure 75 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/075.png)

> <span id="_Ref165301509" class="anchor"></span>Figure 75: APPT Option from the New Request Dropdown

3.  The user will be brought to the New Appointment Request page. On this page, the user will need to fill out all the required information displayed in Figure 76. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/076.png)

> <span id="_Ref165301530" class="anchor"></span>Figure 76: New Appointment Request Page for APPT

- Note: The ISS application will automatically cross check to ensure no duplicate appointment requests are being made for the selected clinic/service. If there are no potential duplicate requests, the notification seen in Figure 78 will appear in green and the user can continue creating the appointment request. If there are potential duplicate appointment request(s), the notification and table shown in Figure 77 will appear. Please see <u>4.1.7 Dispositioning Duplicate Clinic Requests</u> for more information on handling duplicate appointments when creating a request for a clinic and <u>4.1.8 Dispositioning Duplicate Service Requests</u> when creating a request for a service.

  ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/077.png)

> <span id="_Ref190866294" class="anchor"></span>Figure 77: Duplicate Appointment Conflicts Example for APPT

4.  Once all applicable information has been filled, the user will select the "Create Request" button, seen in Figure 78, to create the new APPT request.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/078.png)

> <span id="_Ref165301553" class="anchor"></span>Figure 78: Create Request Button for APPT Request

- Note: The user can also select the "Cancel" button seen in Figure 78 to exit creating a request and go back to the Appointments & Requests page.

### PtCSch (Recall)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a new PtCSch request, the user will first need to select "New Request," as shown in Figure 79.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/079.png)

> <span id="_Ref165378263" class="anchor"></span>Figure 79: New Request Button for PtCSch Requests

2.  The user will then select "PtCSch" from the dropdown that appears in Figure 80 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/080.png)

> <span id="_Ref165378285" class="anchor"></span>Figure 80: PtCSch Option from the New Request Dropdown

3.  The user will be brought to the New PtCSch Request page. On this page, the user will need to fill out all the required information displayed in Figure 81. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/081.png)

> <span id="_Ref165378303" class="anchor"></span>Figure 81: New PtCSch Request Page

- Note: The ISS application will automatically cross check to ensure no duplicate appointment requests are being made for the selected clinic/service. If there are no potential duplicate requests, the notification seen in Figure 83 will appear in green and the user can continue creating the appointment request. If there are potential duplicate appointment request(s), the notification and table shown in Figure 82 will appear. Please see <u>4.1.7 Dispositioning Duplicate Clinic Requests</u> for more information on handling duplicate appointments when creating a request for a clinic and <u>4.1.8 Dispositioning Duplicate Service Requests</u> when creating a request for a service.

  ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/082.png)

> <span id="_Ref190866295" class="anchor"></span>Figure 82: Duplicate Appointment Conflicts Example for PtCSch

4.  Once all applicable information has been filled, the user will select the "Create Request" button, seen in Figure 83, to create the new PtCSch request.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/083.png)

> <span id="_Ref165383999" class="anchor"></span>Figure 83: Create Request Button for PtCSch Requests

- Note: The user can also select the "Cancel" button seen in Figure 83 to exit creating a request and go back to the Appointments & Requests page.

### MRTC 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a new MRTC request, the user will first need to select "New Request," as shown in Figure 84.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/084.png)

> <span id="_Ref165384050" class="anchor"></span>Figure 84: New Request Button for MRTC Requests

2.  The user will then select "MRTC" from the dropdown that appears in Figure 85 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/085.png)

> <span id="_Ref165384110" class="anchor"></span>Figure 85: MRTC Option from New Request Dropdown

3.  The user will be brought to the New MRTC Request (Multiple Returns to Clinic) page. On this page, the user will need to fill out all the required information displayed in Figure 86. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/086.png)

> <span id="_Ref165384130" class="anchor"></span>Figure 86: New MRTC Request Page

4.  Once all applicable information has been filled, the user will select the "Create Request" button, seen in Figure 87, to create the new MRTC request.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/087.png)

> <span id="_Ref165384144" class="anchor"></span>Figure 87: Create Request Button for MRTC Requests

- Note: The user can also select the "Cancel" button seen in Figure 87 to exit creating a request and go back to the Appointments & Requests page.
- Note: Once an MRTC Request has been created, it will appear within the Appointment Requests grid under the request type "APPT." To interact with the MRTC, the user can either select the ellipsis next to the parent MRTC or select the arrow next to the request to interact with each individual child request.

### Consult/Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Consult and Procedure requests are not created within the ISS application. To interact with these requests, the user will need to locate any previously created Consult/Procedure requests by navigating the Appointment Requests grid (See Figure 88 for an example.)

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/088.png)

> <span id="_Ref165384188" class="anchor"></span>Figure 88: Example of Consult Requests in the Grid

### RTC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RTC requests are not created within the ISS application. To interact with these requests, the user will need to locate any previously created RTC requests by navigating the Appointment Requests grid (See Figure 89 for an example).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/089.png)

> <span id="_Ref165384206" class="anchor"></span>Figure 89: Example of RTC Requests in the Grid

### VETERAN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VETERAN requests are not created within the ISS application. To interact with these requests, the user will need to locate any previously created VETERAN requests by navigating the Appointment Requests grid (See Figure 90 for an example).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/090.png)

> <span id="_Ref165384222" class="anchor"></span>Figure 90: Example of VETERAN Requests in the Grid

### Dispositioning Duplicate Clinic Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When creating an appointment request for APPT or PtCSch, the ISS application will cross-check duplicate clinic requests within the system for the current patient. The steps below detail how to handle these requests. For more information on APPT or PtCSch, see sections <u>4.1.1 APPT</u> and <u>4.1.2 PtCSch (Recall)</u>.

1.  Navigate to the "Warning: Duplicate Appointment Request Conflict. Existing requests must be dispositioned in order to create a new request" notification, shown in Figure 91.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/091.png)

<span id="_Ref190876038" class="anchor"></span>Figure 91: Duplicate Appointments Warning for Clinic Requests

2.  The user will then need to review each appointment listed in the table and decide whether to cancel a previously made appointment request(s), or to cancel the current request being created. If the user decides to continue with the current request, the other appointment request(s) will need to be dispositioned.
3.  To remove existing appointments, the user will need to select a disposition reason listed within the dropdown in the Disposition Reason column shown in Figure 92. This step may need to be repeated if there are multiple duplicate requests that need to be dispositioned.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/092.png)

<span id="_Ref190876039" class="anchor"></span>Figure 92: Disposition Dropdown for Clinic Requests

- Note: The user may need to navigate between pages of the table to find all duplicate requests. For more information, please see section <u>2.3.5 Filtering Rows</u>.
4.  Once all previously created appointment requests have been given a disposition reason and all the required information has been inputted for the appointment request, the user can then select "Create Request."

### Dispositioning Duplicate Service Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When creating an appointment request for APPT, the ISS application will cross-check duplicate service requests within the system for the current patient. The steps below detail how to handle these requests. For more information on APPT, see section <u>4.1.1 APPT.</u>

1.  Navigate to the "Warning: Duplicate Appointment Request Conflict. Existing requests must be dispositioned in order to create a new request" notification, seen in Figure 93.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/093.png)

<span id="_Ref190876040" class="anchor"></span>Figure 93: Duplicate Appointments Warning for Service Requests

2.  The user will then need to review each appointment listed in the table and decide whether to cancel a previously made appointment request(s), to cancel the current request being created, or to do a combination of both. If the user decides to continue with the current request, the other appointment request(s) will either need to be dispositioned or be given a reason for why they should remain with the new request.
3.  For the appointment requests that need to be dispositioned, select a disposition reason listed within the dropdown in the Disposition Reason column, shown in Figure 94. This step may need to be repeated if there are multiple duplicate requests that need to be dispositioned.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/094.png)

<span id="_Ref190876041" class="anchor"></span>Figure 94: Disposition Dropdown for Service Requests

- Note: The user may need to navigate between pages of the table to find all duplicate requests. For more information, please see section <u>2.3.5 Filtering Rows</u>.
4.  For the appointment requests that will remain, the user will need to leave the disposition reason in the default state. The user will then need to enter a reason for creating a new request in the text box shown in Figure 95.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/095.png)

<span id="_Ref190876093" class="anchor"></span>Figure 95: Reason Text Box for not Dispositioning Service Requests

5.  Once all of the previous steps have been completed successfully and all the required information has been inputted for the appointment request, the user can then select "Create Request."

## Appointment Request Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Viewing Appointment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To view an appointment request, the user can select the ellipsis, seen in Figure 96, next to any appointment within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/096.png)

> <span id="_Ref165384240" class="anchor"></span>Figure 96: Selecting Action Menu Button to View Requests

2.  This will cause the action menu to appear. The user will then need to select the "View" option, seen in Figure 97.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/097.png)

> <span id="_Ref165384258" class="anchor"></span>Figure 97: View Option from the Request Actions Dropdown

3.  The user will be brought to the View (Appointment Request Type) Request page, shown below in Figure 98.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/098.png)

> <span id="_Ref165384284" class="anchor"></span>Figure 98: View APPT Request Page

- Note: Users can perform Appointment Requests actions via the view request page by selecting the "Actions" button seen in Figure 98. This will cause the action menu to appear (see Figure 99 for example). For more information on Appointment Request actions, see the following sections 4.2.2 Editing Appointment Requests - 4.2.7 Disposition an MRTC Child Request.

  ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/099.png)

> <span id="_Ref194050476" class="anchor"></span>Figure 99: Action Menu from the View Request Page

- Note: Users will be able to track comments via the View page. Comments will show the name of the commenter, as well as the date the comment was added to the appointment request (see Figure 98 for example).

### Editing Appointment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To edit an appointment request, the user will select the ellipsis, seen in Figure 100, next to any appointment within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/100.png)

> <span id="_Ref165384305" class="anchor"></span>Figure 100: Selecting Action Menu Button to Edit Requests

2.  This will cause the action menu to appear. The user will then need to select the "Edit" option, seen in Figure 101.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/101.png)

> <span id="_Ref165384320" class="anchor"></span>Figure 101: Edit Option from the Request Actions Dropdown

3.  The user will be brought to the Edit (Appointment Request Type) Request page. On this page, the user can edit any of the fields highlighted below in Figure 102.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/102.png)

> <span id="_Ref165384336" class="anchor"></span>Figure 102: Edit Appointment Request Page

- Note: Users can add additional comments to an appointment request, as well as track previous comments via the Edit page. Previous comments will show the name of the commenter and the date the comment was added (see Figure 103 for example).
4.  Once all edits have been made, the user will need to select the "Save Changes" button, seen in Figure 103, to save any edits to the request.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/103.png)

> <span id="_Ref165384375" class="anchor"></span>Figure 103: Save Changes Button for Editing Requests

- Note: The user can also select the "Cancel" button seen in Figure 103 to exit editing a request and go back to the Appointments & Requests page.

### Contact Attempts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a contact attempt request, the user will select the ellipsis, seen in Figure 104, next to any appointment within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/104.png)

> <span id="_Ref165384417" class="anchor"></span>Figure 104: Selecting Action Menu Button to Create Contact Attempts

2.  This will cause the action menu to appear. The user will then need to select the "Contact Attempts" option, seen in Figure 105.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/105.png)

> <span id="_Ref165384434" class="anchor"></span>Figure 105: Contact Attempts Option from the Request Actions Dropdown

3.  The user will be brought to the Contact Attempts page, shown below in Figure 106.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/106.png)

> <span id="_Ref165384451" class="anchor"></span>Figure 106: Contact Attempts Page

4.  To create a new contact attempt, the user will need to select the "New Contact Attempt" button seen in Figure 107.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/107.png)

> <span id="_Ref165384468" class="anchor"></span>Figure 107: New Contact Attempt Button

5.  The user will be brought to the Create Contact Attempt Page seen in Figure 108 below. From here, the user will need to fill out the required information displayed and fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/108.png)

> <span id="_Ref165384482" class="anchor"></span>Figure 108: Create Contact Attempt Page

- Note: The first contact attempt cannot be done via a letter. Once the user has made at least one contact attempt, the "Letter" option will be available within the Contact Type field.
6.  Once the user has filled out all applicable information, the user will need to select the "Create Attempt" button, seen in Figure 109, to create the contact attempt.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/109.png)

> <span id="_Ref165384501" class="anchor"></span>Figure 109: Create Attempt Button

- Note: The user can also select the "Cancel" button seen in Figure 109 to exit creating a contact attempt and go back to the Contact Attempts page.
7.  After saving their changes, the user will be brought back to the Contact Attempts page. The grid, shown below in Figure 110, will be updated with the newly created contact attempt information.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/110.png)

> <span id="_Ref165384538" class="anchor"></span>Figure 110: Example of Contact Attempts Grid after Creating Attempt

### Disposition an APPT, RTC, or VETERAN Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To disposition an APPT, RTC, or VETERAN request, the user will select the ellipsis, seen in Figure 111, next to any appointment within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/111.png)

> <span id="_Ref165384560" class="anchor"></span>Figure 111: Selecting Action Menu Button to Disposition Requests

2.  This will cause the action menu to appear. The user will then need to select one of the disposition options highlighted below in Figure 112.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/112.png)

> <span id="_Ref165384580" class="anchor"></span>Figure 112: Disposition Options from the Request Actions Dropdown

- Note: When dispositioning a request via failure to respond, the user will need to have made at least 2 contact attempts at least 2 weeks prior to the disposition date. Attempting to disposition otherwise will result in the notification seen in Figure 113 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/113.png)

> <span id="_Ref165384603" class="anchor"></span>Figure 113: Notification when Dispositioning Failure to Respond without Attempts

3.  After selecting a disposition type, the user will need to select the "Disposition" button seen below in Figure 114 to confirm the request.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/114.png)

<span id="_Ref195803314" class="anchor"></span>Figure 114: Confirm Disposition Request Notification

4.  Once the disposition is confirmed, the page will automatically refresh, and the request will be removed from the Appointment Requests grid.

### Disposition a PtCSch Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To disposition a PtCSch request, the user will select the ellipsis, seen in Figure 115, next to any appointment within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/115.png)

> <span id="_Ref165384641" class="anchor"></span>Figure 115: Selecting Action Menu Button to Disposition Requests for PtCSch

2.  This will cause the action menu to appear. The user will then need to select one of the disposition options highlighted below in Figure 116.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/116.png)

> <span id="_Ref165384663" class="anchor"></span>Figure 116: Disposition Options for PtCSch on the Requests Actions Dropdown

- Note: When dispositioning a request via failure to respond, the user will need to have made at least 2 contact attempts at least 2 weeks prior to the disposition date. Attempting to disposition otherwise will result in the notification seen in Figure 117 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/117.png)

> <span id="_Ref165384686" class="anchor"></span>Figure 117: Notification when Dispositioning Failure to Respond without Attempts on PtCSch

3.  After the disposition type is selected, the PtCSch Disposition window will appear. The user can choose to add a comment, if needed, and then select "Continue" to finish the disposition, as seen in Figure 118.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/118.png)

> <span id="_Ref165384730" class="anchor"></span>Figure 118: Continue Button for Disposition Comments Window for PtCSch Requests

- Note: The user can also select the "Cancel" button or the "x" button, seen in Figure 118, to cancel the disposition and go back to the Appointments & Requests page.
4.  The page will automatically refresh, and the request will be removed from the Appointment Requests grid.

### Disposition an MRTC Parent Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When dispositioning an MRTC request, the user can choose to either disposition an individual child request (See <u>4.2.7 Disposition an MRTC Child Request</u>), or the parent request. To disposition a parent request, the user will select the ellipsis, seen in Figure 119, next to the parent request within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/119.png)

> <span id="_Ref165384779" class="anchor"></span>Figure 119: Selecting Action Menu Button to Disposition for MRTC Parent Requests

2.  This will cause the action menu to appear. The user will then need to select one of the disposition options highlighted below in Figure 120.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/120.png)

> <span id="_Ref165384792" class="anchor"></span>Figure 120: Disposition Options for MRTC Parent Request on the Actions Dropdown

- Note: When dispositioning a request via failure to respond, the user will need to have made at least 2 contact attempts at least 2 weeks prior to the disposition date. Attempting to disposition otherwise will result in the notification seen in Figure 121 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/121.png)

> <span id="_Ref165384811" class="anchor"></span>Figure 121: Notification when Dispositioning Failure to Respond without Attempts on MRTC Parent Requests

3.  After the disposition type is selected, the user will be brought to the Close MRTC Request page. For a parent request, all pending appointments and requests will be dispositioned. The user will select the "Disposition MRTC" button, seen in Figure 122, to finish the disposition.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/122.png)

> <span id="_Ref165384827" class="anchor"></span>Figure 122: Disposition MRTC Button for Parent Requests

- Note: If a pending appointment exists when dispositioning a parent request, the user will also need to fill out the fields under the Cancel MRTC Appointment(s) section, seen in Figure 123, before continuing. The user will have the option to preview a cancellation letter, if needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/123.png)

> <span id="_Ref165384847" class="anchor"></span>Figure 123: Cancel MRTC Section Example when Dispositioning Parent Request

- Note: The user can also select the "Back" button seen in Figure 122 to cancel the disposition and go back to the Appointments & Requests page.

### Disposition an MRTC Child Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To disposition a child request, the user will need to expand the MRTC request by selecting the arrow next to the MRTC parent. The user will then need to select one of the corresponding ellipsis next to a child appointment, as shown in Figure 124 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/124.png)

> <span id="_Ref165384956" class="anchor"></span>Figure 124: Selecting Action Menu Button to Disposition for MRTC Child Requests

2.  This will cause the action menu to appear. The user will then need to select one of the disposition options highlighted below in Figure 125.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/125.png)

> <span id="_Ref165384974" class="anchor"></span>Figure 125: Disposition Options for MRTC Child Requests on the Actions Dropdown

- Note: When dispositioning a request via failure to respond, the user will need to have made at least 2 contact attempts at least 2 weeks prior to the disposition date. Attempting to disposition otherwise will result in the notification seen in Figure 126 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/126.png)

> <span id="_Ref165384993" class="anchor"></span>Figure 126: Notification when Dispositioning Failure to Respond without Attempts on MRTC Child Requests

3.  After the disposition type is selected, the user will be brought to the Close MRTC Request page. For a child request, the user will be given the option to close either the selected appointment request only, or all the appointment requests in the series. Once making their preferred selection, the user will select the "Disposition MRTC" button, seen in Figure 127, to finish the disposition.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/127.png)

> <span id="_Ref165385018" class="anchor"></span>Figure 127: Disposition MRTC Button for MRTC Child Requests

- Note: If the user decides to cancel all appointments and requests and a pending appointment exists when dispositioning a child request, the user will also need to fill out the fields under the Cancel MRTC Appointment(s) section, seen in Figure 128, before continuing. The user will have the option to preview a cancellation letter, if needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/128.png)

> <span id="_Ref165385040" class="anchor"></span>Figure 128: Cancel MRTC Section Example when Dispositioning Child Requests

- Note: The user can also select the "Back" button seen in Figure 127 to cancel the disposition and go back to the Appointments & Requests page.

## Creating a Pending Appointment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### APPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create an APPT appointment, the user will first need to create a request by following the steps in <u>4.1.1 APPT</u>.
2.  After creating the appointment request, the user will select the ellipsis, seen in Figure 129, next to the request within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/129.png)

> <span id="_Ref165447831" class="anchor"></span>Figure 129: Selecting Action Menu Button to Create APPT Appointment

3.  This will cause the action menu to appear. The user will then need to select the "New" option, seen in Figure 130.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/130.png)

> <span id="_Ref165447846" class="anchor"></span>Figure 130: New Option from the Request Actions Dropdown for APPT

4.  The user will be brought to the Schedule Search page shown below. On this page, the user can right click within the preferred timeslot on the calendar and select the "Create Appointment" option seen in Figure 131.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/131.png)

> <span id="_Ref165447868" class="anchor"></span>Figure 131: Create Appointment Button for APPT

5.  The user will be brought to the New Appointment page. On this page, the user will need to fill out all the required information displayed in Figure 132. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/132.png)

> <span id="_Ref165447883" class="anchor"></span>Figure 132: New Appointment Page for APPT

- Note: Users will be able to track comments via the New Appointment page. Comments will show the name of the commenter, as well as the date the comment was added to the appointment request. Comments added under the 'Notes" section of the page will be added to comment tracking and available for viewing once the appointment has been created.
6.  Once all applicable information has been filled, the user will select the "Create Appointment" button, seen in Figure 133, to create the new APPT appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/133.png)

> <span id="_Ref165447898" class="anchor"></span>Figure 133: Create Appointment Button for New APPT

- Note: The user can also select the "Cancel" button seen in Figure 133 to exit creating an appointment and go back to the Appointments & Requests page.
7.  The Appointment Successfully Created window, shown below in Figure 134, will appear. The user can choose to preview the patient letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/134.png)

> <span id="_Ref165447933" class="anchor"></span>Figure 134: Preview Patient Letter Window for Creating APPT Appointment

### PtCSch (Recall)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a PtCSch appointment, the user will first need to create a request by following the steps in <u>4.1.2 PtCSch (Recall)</u>.
2.  After creating the appointment request, the user will select the ellipsis, seen in Figure 135, next to the request within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/135.png)

> <span id="_Ref165447951" class="anchor"></span>Figure 135: Selecting Action Menu Button to Create PtCSch Appointment

3.  This will cause the action menu to appear. The user will then need to select the "New" option, seen in Figure 136.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/136.png)

> <span id="_Ref165447965" class="anchor"></span>Figure 136: New Option from the Request Actions Dropdown for PtCSch

4.  The user will be brought to the Schedule Search page shown below. On this page, the user can right click within the preferred timeslot on the calendar and select the "Create Appointment" option seen in Figure 137.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/137.png)

> <span id="_Ref165447976" class="anchor"></span>Figure 137: Create Appointment Button for PtCSch

5.  The user will be brought to the New Appointment page. On this page, the user will need to fill out all the required information displayed in Figure 138. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/138.png)

> <span id="_Ref165447991" class="anchor"></span>Figure 138: New Appointment Page for PtCSch

- Note: Users will be able to track comments via the New Appointment page. Comments will show the name of the commenter, as well as the date the comment was added to the appointment request. Comments added under the 'Notes" section of the page will be added to comment tracking and available for viewing once the appointment has been created.
6.  Once all applicable information has been filled, the user will select the "Create Appointment" button, seen in Figure 139, to create the new PtCSch appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/139.png)

> <span id="_Ref165448005" class="anchor"></span>Figure 139: Create Appointment Button for New PtCSch

- Note: The user can also select the "Cancel" button seen in Figure 139 to exit creating an appointment and go back to the Appointments & Requests page.
7.  The Appointment Successfully Created window, shown below in Figure 140, will appear. The user can choose to preview the patient letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/140.png)

> <span id="_Ref165448035" class="anchor"></span>Figure 140: Preview Patient Letter Window for Creating PtCSch Appointment

### MRTC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create an MRTC appointment, the user will first need to locate an MRTC request created through CPRS, as seen in Figure 141, or follow the steps in <u>4.1.3 MRTC</u> to create a request through ISS.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/141.png)

> <span id="_Ref168581450" class="anchor"></span>Figure 141: Example of CPRS MRTC in Grid

- Note: MRTC requests created through CPRS will display as "RTC" in the Request column.
- Note: MRTC requests without an existing parent request will display in red as seen below in Figure 142.

  ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/142.png)

> <span id="_Ref189148400" class="anchor"></span>Figure 142: Orphaned MRTC Child Request Example

2.  After creating the appointment request, the user will select the ellipsis, seen in Figure 143, next to the request within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/143.png)

> <span id="_Ref165448211" class="anchor"></span>Figure 143: Selecting Action Menu Button to Create MRTC Appointment

- Note: If the user would like to schedule a child request individually, simply expand the parent MRTC request and select the ellipsis next to the child request needed. The user can then follow the steps from <u>4.3.1 APPT</u> to create the appointment.
3.  This will cause the action menu to appear. The user will then need to select the "New" option, seen in Figure 144.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/144.png)

> <span id="_Ref165448262" class="anchor"></span>Figure 144: New Option from the Request Actions Dropdown for MRTC

4.  The user will be brought to the New MRTC Appointment (1 of x) page. On this page, the user can right click within the preferred timeslot on the calendar and select the "Create MRTC Appointment (1 of x)" option seen in Figure 145.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/145.png)

> <span id="_Ref165448277" class="anchor"></span>Figure 145: Create Appointment Button for MRTC

5.  The user will be brought to the New Appointment page. On this page, the user will need to fill out all the required information displayed in Figure 146. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/146.png)

> <span id="_Ref165448293" class="anchor"></span>Figure 146: New Appointment Page for MRTC

- Note: When creating an MRTC Appointment, the user may see prerequisites attached to the request, as seen below in Figure 147.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/147.png)

> <span id="_Ref168650922" class="anchor"></span>Figure 147: Prerequisites Example for MRTC

- Note: Users will be able to track comments via the New Appointment page. Comments will show the name of the commenter, as well as the date the comment was added to the appointment request. Comments added under the 'Notes" section of the page will be added to comment tracking and available for viewing once the appointment has been created.
6.  Once all applicable information has been filled, the user will select the "Create Appointment" button, seen in Figure 148, to create the new MRTC appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/148.png)

> <span id="_Ref165448309" class="anchor"></span>Figure 148: Create Appointment Button for New MRTC

- Note: The user can also select the "Cancel" button seen in Figure 148 to exit creating an appointment and go back to the Appointments & Requests page.
7.  The Appointment Successfully Created window, shown below in Figure 149, will appear. The user can choose to preview the patient letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/149.png)

> <span id="_Ref165448341" class="anchor"></span>Figure 149: Preview Patient Letter Window for Creating MRTC Appointments

8.  Once the appointment is created, the user will be brought back to the New MRTC Appointment page. From here, the user can follow steps 4-7 to create the other appointments on the MRTC request or select close to exit and return to the Appointments & Requests page.

### Consult/Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a Consult/Procedure appointment, the user will need to locate any previously created Consult/Procedure requests by navigating the Appointment Requests grid (See Figure 150 for an example.)

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/150.png)

> <span id="_Ref165448368" class="anchor"></span>Figure 150: Example for Finding Consult/Procedure Requests

2.  Once the consult/procedure request is located, the user will select the ellipsis, seen in Figure 151, next to the request within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/151.png)

> <span id="_Ref165448387" class="anchor"></span>Figure 151: Selecting Action Menu Button to Create Consult/Procedure Appointment

3.  This will cause the action menu to appear. The user will then need to select the "New" option, seen in Figure 152.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/152.png)

> <span id="_Ref165448400" class="anchor"></span>Figure 152: New Option from the Request Actions Dropdown for Consult/Procedure

4.  The user will be brought to the Schedule Search page shown below. To search for a clinic, the user will select the search bar, seen in Figure 153, and enter a valid clinic name. Once the information has been entered, a list of clinics will appear in the dropdown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/153.png)

> <span id="_Ref165448413" class="anchor"></span>Figure 153: Searching for a Clinic when Creating a Consult/Procedure Appointment

- Note: It is suggested that the user searches for a clinic within the service/specialty of the original appointment request. Attempting to use a clinic outside of the service/specialty in the request will result in the Clinic Stop Code notification seen in Figure 154 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/154.png)

> <span id="_Ref165448434" class="anchor"></span>Figure 154: Clinic Stop Code Window for Consult/Procedure

5.  After selecting a preferred clinic from the available options, the user will be brought to the Time Slot Calendar for the selected clinic. The user can then right click within the preferred timeslot on the calendar and select the "Create Appointment" option seen in Figure 155.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/155.png)

> <span id="_Ref165448452" class="anchor"></span>Figure 155: Create Appointment Button for Consult/Procedure

6.  The user will be brought to the New Appointment page. On this page, the user will need to fill out all the required information displayed in Figure 156. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/156.png)

> <span id="_Ref165448467" class="anchor"></span>Figure 156: New Appointment Page for Consult/Procedure

- Note: Users will be able to track comments via the New Appointment page. Comments will show the name of the commenter, as well as the date the comment was added to the appointment request. Comments added under the 'Notes" section of the page will be added to comment tracking and available for viewing once the appointment has been created.
7.  Once all applicable information has been filled, the user will select the "Create Appointment" button, seen in Figure 157, to create the new Consult/Procedure appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/157.png)

> <span id="_Ref165448485" class="anchor"></span>Figure 157: Create Appointment Button for New Consult/Procedure

- Note: The user can also select the "Cancel" button seen in Figure 157 to exit creating an appointment and go back to the Appointments & Requests page.
8.  The Appointment Successfully Created window, shown below in Figure 158, will appear. The user can choose to preview the patient letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/158.png)

> <span id="_Ref165448515" class="anchor"></span>Figure 158: Preview Patient Letter Window for Creating Consult/Procedure Appointment

### RTC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a RTC appointment, the user will need to locate any previously created RTC requests by navigating the Appointment Requests grid (See Figure 159 for an example.)

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/159.png)

> <span id="_Ref165448535" class="anchor"></span>Figure 159: Example for Finding RTC Requests

2.  Once the RTC request is located, the user will select the ellipsis, seen in Figure 160, next to the request within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/160.png)

> <span id="_Ref165448551" class="anchor"></span>Figure 160: Selecting Action Menu Button to RTC Appointments

3.  This will cause the action menu to appear. The user will then need to select the "New" option, seen in Figure 161.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/161.png)

> <span id="_Ref165448565" class="anchor"></span>Figure 161: New Option from the Request Actions Dropdown for RTC

4.  The user will be brought to the Schedule Search page shown below. On this page, the user can right click within the preferred timeslot on the calendar and select the "Create Appointment" option seen in Figure 162.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/162.png)

> <span id="_Ref165448579" class="anchor"></span>Figure 162: Create Appointment Button for RTC

5.  The user will be brought to the New Appointment page. On this page, the user will need to fill out all the required information displayed in Figure 163. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/163.png)

> <span id="_Ref165448593" class="anchor"></span>Figure 163: New Appointment for RTC

- Note: When creating an RTC Appointment, the user may see prerequisites attached to the request, as seen below in Figure 164.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/164.png)

> <span id="_Ref168650923" class="anchor"></span>Figure 164: Prerequisites Example for RTC

- Note: Users will be able to track comments via the New Appointment page. Comments will show the name of the commenter, as well as the date the comment was added to the appointment request. Comments added under the 'Notes" section of the page will be added to comment tracking and available for viewing once the appointment has been created.
6.  Once all applicable information has been filled, the user will select the "Create Appointment" button, seen in Figure 165, to create the new RTC appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/165.png)

> <span id="_Ref165448607" class="anchor"></span>Figure 165: Create Appointment Button for Creating RTC Appointments

- Note: The user can also select the "Cancel" button seen in Figure 165 to exit creating an appointment and go back to the Appointments & Requests page.
7.  The Appointment Successfully Created window, shown below in Figure 166, will appear. The user can choose to preview the patient letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/166.png)

> <span id="_Ref165448641" class="anchor"></span>Figure 166: Preview Patient Letter Window for Creating RTC Appointments

### VETERAN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a VETERAN appointment, the user will need to locate any previously created VETERAN requests by navigating the Appointment Requests grid (See Figure 167 an example.)

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/167.png)

> <span id="_Ref165448665" class="anchor"></span>Figure 167: Example for Finding VETERAN Requests

2.  Once the VETERAN request is located, the user will select the ellipsis, seen in Figure 168, next to the request within the grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/168.png)

> <span id="_Ref165448691" class="anchor"></span>Figure 168: Selecting Action Menu Button to VETERAN Appointments

3.  This will cause the action menu to appear. The user will then need to select the "New" option, seen in Figure 169.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/169.png)

> <span id="_Ref165448709" class="anchor"></span>Figure 169: New Option from the Request Actions Dropdown for VETERAN

4.  The user will be brought to the Schedule Search page shown below. To search for a clinic, the user will select the search bar, seen in Figure 170, and enter a valid clinic name. Once the information has been entered, a list of clinics will appear in the dropdown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/170.png)

> <span id="_Ref165448725" class="anchor"></span>Figure 170: Searching for a Clinic when Creating a VETERAN Appointment

- Note: It is suggested that the user searches for a clinic within the service/specialty of the original appointment request. Attempting to use a clinic outside of the service/specialty in the request will result in the Clinic Stop Code notification seen in Figure 171 below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/171.png)

> <span id="_Ref165448740" class="anchor"></span>Figure 171: Clinic Stop Code Window for VETERAN Appointments

5.  After selecting a preferred clinic from the available options, the user will be brought to the Time Slot Calendar for the selected clinic. The user can then right click within the preferred timeslot on the calendar and select the "Create Appointment" option seen in Figure 172.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/172.png)

> <span id="_Ref165448755" class="anchor"></span>Figure 172: Create Appointment Button for VETERAN

6.  The user will be brought to the New Appointment page. On this page, the user will need to fill out all the required information displayed in Figure 173. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/173.png)

> <span id="_Ref165448772" class="anchor"></span>Figure 173: New Appointment Page for VETERAN

- Note: Users will be able to track comments via the New Appointment page. Comments will show the name of the commenter, as well as the date the comment was added to the appointment request. Comments added under the 'Notes" section of the page will be added to comment tracking and available for viewing once the appointment has been created.
7.  Once all applicable information has been filled, the user will select the "Create Appointment" button, seen in Figure 174, to create the new VETERAN appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/174.png)

> <span id="_Ref165448789" class="anchor"></span>Figure 174: Create Appointment Button for Creating VETERAN Appointments

- Note: The user can also select the "Cancel" button seen in Figure 174 to exit creating an appointment and go back to the Appointments & Requests page.
8.  The Appointment Successfully Created window, shown below in Figure 175, will appear. The user can choose to preview the patient letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/175.png)

> <span id="_Ref165448818" class="anchor"></span>Figure 175: Preview Patient Letter Window for Creating VETERAN Appointments

### Overbooking an Appointment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When creating appointments, users have the ability to overbook an appointment slot. To do so, the user will need to follow the steps outlined in <u>4.3 Creating a Pending Appointment</u> until asked to select a timeslot on the clinic calendar.

1.  To overbook an appointment slot, the user will right-click on the preferred timeslot on the calendar and select "Create Appointment (Overbooked)," as seen below in Figure 176.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/176.png)

> <span id="_Ref165448844" class="anchor"></span>Figure 176: Create Appointment (Overbooked) Button

2.  The Overbook Slot window will appear, as shown in Figure 177, and the user will be asked to confirm before proceeding with appointment creation as normal.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/177.png)

> <span id="_Ref165448859" class="anchor"></span>Figure 177: Overbook Slot Window

- Note: Users with an SDOB key will only be able to overbook within clinic hours and up to the maximum number of overbooks allowed per day for a clinic. Users with an SDMOB key will be able to overbook outside of clinic hours and can exceed the maximum allotted overbooks slots per day for a clinic.

### MISSION Act

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may receive an alert when creating an appointment if an appointment is MISSION Act eligible. For more information regarding MISSION Act, please visit this [link](https://vaww.insider.va.gov/MISSION-Act/).

### Clinic Stop Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user will receive a clinic stop code notification if an appointment is being created in a clinic that is not within the service/specialty of the appointment request.

### Patient Conflicts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When creating an appointment, the user will see a Patient Conflict notification at the bottom of the New Appointment page. If no conflict exists, the notification will display "No Potential Appointment Conflicts" in green, as shown in Figure 178, and the user can move forward with creating the appointment as usual.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/178.png)

> <span id="_Ref165644290" class="anchor"></span>Figure 178: No Potential Appointment Conflicts Notification

If the user attempts to make more than one appointment for a patient on the same day at any clinic, the notification will display "Potential Patient Conflict for \[DAY\]" in yellow and show the potential conflicting appointment(s) in a grid, as seen below in Figure 179. The user can then choose to continue making the appointment for the patient or go back and choose a different day and time.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/179.png)

> <span id="_Ref165644291" class="anchor"></span>Figure 179: Potential Appointment Conflicts Notification

From the clinic calendar, the calendar will display the "Create Appointment" button as greyed out and unavailable when attempting to create an appointment with a known conflict (See Figure 180 below).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/180.png)

> <span id="_Ref165644500" class="anchor"></span>Figure 180: Patient Conflict on Calendar

If the user changes the time to one with a patient conflict on the New Appointment page, the notification will display "This Time Has the Conflict Highlighted Below:" in red and show the conflicting appointment in a grid, as seen below in Figure 181.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/181.png)

> <span id="_Ref165644694" class="anchor"></span>Figure 181: Patient Conflict on New Appointment Page

- Note: The user will be unable to create an appointment with a Patient Conflict displayed in red.

## Appointment Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To view an appointment, the user will select the ellipsis, seen in Figure 182, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/182.png)

> <span id="_Ref165625740" class="anchor"></span>Figure 182: Action Menu Button to View Appointments

2.  This will cause the action menu to appear. The user will then need to select the "View" option, seen in Figure 183.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/183.png)

> <span id="_Ref165626708" class="anchor"></span>Figure 183: View Option from Pending Appointments Action Menu

3.  The user will be brought to the View Appointment page, shown below in Figure 184.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/184.png)

> <span id="_Ref165626723" class="anchor"></span>Figure 184: View Appointment Page

- Note: Users will be able to track comments via the View page. Comments will show the name of the commenter, as well as the date the comment was added to the appointment (see Figure 184 for example).
- Note: The user has the ability to print a patient letter by selecting the "Print" button seen in Figure 185.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/185.png)

> <span id="_Ref165626759" class="anchor"></span>Figure 185: Print Patient Letter Button from View Appointment Page

### Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To edit an appointment, the user will select the ellipsis, seen in Figure 186, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/186.png)

> <span id="_Ref165626778" class="anchor"></span>Figure 186: Action Menu Button to Edit Appointments

2.  This will cause the action menu to appear. The user will then need to select the "Edit" option, seen in Figure 187.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/187.png)

> <span id="_Ref165626796" class="anchor"></span>Figure 187: Edit Option from the Pending Appointments Action Menu

3.  The user will be brought to the Edit Appointment page. On this page, the user can edit any of the fields highlighted below in Figure 188.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/188.png)

> <span id="_Ref165626810" class="anchor"></span>Figure 188: Edit Appointment Page

- Note: Users can add additional comments to an appointment, as well as track previous comments via the Edit page. Previous comments will show the name of the commenter and the date the comment was added (see Figure 188 for example).
4.  Once all edits have been made, the user will need to select the "Save Changes" button, seen in Figure 189, to save any edits to the appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/189.png)

> <span id="_Ref165626828" class="anchor"></span>Figure 189: Save Changes Button for Edit Appointment Page

- Note: The user can also select the "Cancel" button seen in Figure 189 to exit editing an appointment and go back to the Appointments & Requests page.

### Cancel an APPT, PtCSch, Consult/Procedure, RTC, or VETERAN Appointment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To cancel an APPT, PtCSch, Consult/Procedure, RTC, or VETERAN appointment, the user will select the ellipsis, seen in Figure 190, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/190.png)

> <span id="_Ref165626862" class="anchor"></span>Figure 190: Action Menu Button to Cancel an Appointment

2.  This will cause the action menu to appear. The user will then need to select the "Cancel" option, seen in Figure 191.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/191.png)

> <span id="_Ref165626902" class="anchor"></span>Figure 191: Cancel Option from the Pending Appointments Action Menu

3.  The user will be brought to the Cancel Appointment page. On this page, the user will need to fill out all the required information displayed in Figure 192. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/192.png)

> <span id="_Ref165626914" class="anchor"></span>Figure 192: Cancel Appointment Page

- Note: The PID section, highlighted below in Figure 193, will be editable when an appointment is cancelled by a patient.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/193.png)

> <span id="_Ref165626931" class="anchor"></span>Figure 193: Editable PID Example when Cancelled by Patient

4.  Once all applicable information has been filled, the user will then select the "Cancel Appointment" button, seen in Figure 194, to cancel the appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/194.png)

> <span id="_Ref165626948" class="anchor"></span>Figure 194: Cancel Appointment Button on the Cancel Appointment Page

5.  The Appointment Successfully Cancelled window, shown below in Figure 195, will appear. The user can choose to preview the cancellation letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/195.png)

> <span id="_Ref165626963" class="anchor"></span>Figure 195: Preview Cancellation Letter Window

- Note: After cancelling, most appointments will return to the Appointment Request grid and the user will have the ability to create a new appointment, if needed. For specific cancellation reasons that do not reopen and return to the grid, see <u>8.1 Cancellation Reasons</u> for more information.

### Cancel an MRTC Appointment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To cancel an MRTC appointment, the user will select the ellipsis, seen in Figure 196, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/196.png)

> <span id="_Ref165626990" class="anchor"></span>Figure 196: Action Menu Button to Cancel MRTC Appointments

2.  This will cause the action menu to appear. The user will then need to select the "Cancel" option, seen in Figure 197.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/197.png)

> <span id="_Ref165627004" class="anchor"></span>Figure 197: Cancel Option from the Pending Appointments Action Menu for MRTC

3.  Once selected, the user will be brought to the Cancel MRTC Appointment page, as seen below in Figure 198. The user will be given the option to cancel either the selected appointment only, or all the appointments in the series. If canceling all appointment, the user also has the option to close the MRTC parent request, which would close all associated appointment request(s) in the series.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/198.png)

> <span id="_Ref165627024" class="anchor"></span>Figure 198: Cancel MRTC Appointment Options for Parent and Child Appointments

4.  Below the options for cancelling other associated MRTC appointments and requests, the user will also need to fill out all the required information displayed in Figure 199. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/199.png)

> <span id="_Ref165627043" class="anchor"></span>Figure 199: Cancel MRTC Appointment(s) Page

5.  Once all applicable information has been filled out, the user will then select the "Cancel MRTC Appointment" button, seen below in Figure 200, to cancel the appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/200.png)

> <span id="_Ref165627061" class="anchor"></span>Figure 200: Cancel MRTC Appointment Button

6.  The Appointment Successfully Cancelled window, shown below in Figure 201, will appear. The user can choose to preview the cancellation letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/201.png)

> <span id="_Ref165627076" class="anchor"></span>Figure 201: Preview Cancellation Letter Window for MRTC

### Expand Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To expand entry on an appointment, the user will select the ellipsis, seen in Figure 202, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/202.png)

> <span id="_Ref165627093" class="anchor"></span>Figure 202: Action Menu Button to Expand Entry

2.  This will cause the action menu to appear. The user will then need to select the "Expand Entry" option, seen in Figure 203.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/203.png)

> <span id="_Ref165627121" class="anchor"></span>Figure 203: Expand Entry Option from Pending Appointments Action Menu

3.  The user will be brought to the Expanded Entry page, shown below in Figure 204. The user can view the fields within expanded entry by either selecting the "+" button next to an individual row, or by selecting "Expand all +."

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/204.png)

> <span id="_Ref165627144" class="anchor"></span>Figure 204: Expanded Entry Page

### Block and Move

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To block and move an appointment, the user will select the ellipsis, seen in Figure 205, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/205.png)

> <span id="_Ref165627165" class="anchor"></span>Figure 205: Action Menu Button to Block and Move an Appointment

2.  This will cause the action menu to appear. The user will then need to select the "Block and Move" option, seen in Figure 206.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/206.png)

> <span id="_Ref165627187" class="anchor"></span>Figure 206: Block and Move Option from the Pending Appointments Action Menu

3.  The user will be brought to the Block and Move Appointment page, seen below in Figure 207. The user will need to navigate to the preferred available timeslot on the calendar and left click on the date.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/207.png)

> <span id="_Ref165627204" class="anchor"></span>Figure 207: Block and Move Appointment Page

- Note: The user can use the Appointment Information section, seen in Figure 208, to change any of the editable fields on the appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/208.png)

> <span id="_Ref165627225" class="anchor"></span>Figure 208: Appointment Information Section for Block and Move

4.  Once an available date is selected, the user can then select the "Block and Move" button, seen in Figure 209, to block and move the appointment to the intended date.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/209.png)

> <span id="_Ref165627245" class="anchor"></span>Figure 209: Block and Move Button

5.  The Appointment Successfully Created window, shown below in Figure 210, will appear. The user can choose to preview the patient letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/210.png)

> <span id="_Ref165627262" class="anchor"></span>Figure 210: Preview Patient Letter for Block and Move

### Check In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To check in an appointment, the user will select the ellipsis, seen in Figure 211, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/211.png)

> <span id="_Ref165627348" class="anchor"></span>Figure 211: Action Menu Button to Check In Appointments

- Note: Users cannot check in a future appointment.
2.  This will cause the action menu to appear. The user will then need to select the "Check In" option, seen in Figure 212.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/212.png)

> <span id="_Ref165627363" class="anchor"></span>Figure 212: Check In Patient Option from the Pending Appointments Action Menu

3.  The user will be brought to the Appointment Check In page. On this page, the user will need to select the "Check In" button, seen in Figure 213, to check the appointment in.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/213.png)

> <span id="_Ref165627380" class="anchor"></span>Figure 213: Check In Button

- Note: Users can change the check in time by editing the Check In Time field. The edited time and date must be in the past.
- Note: The user can also select the "Cancel" button seen in Figure 213 to exit the check in process and go back to the Appointments & Requests page.
- Note: Users can also select the "View Demographics" option to navigate to the patient demographic tab. See section <u>3.4 Demographics</u> for more information.

### Undo Check In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To undo check in on a previously checked in appointment, the user will select the ellipsis, seen in Figure 214, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/214.png)

> <span id="_Ref165627425" class="anchor"></span>Figure 214: Action Menu Button to Undo Check In

2.  This will cause the action menu to appear. The user will then need to select the "Undo Check In Patient" option, seen in Figure 215. This will cause the page to automatically refresh and the appointment to no longer be checked in.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/215.png)

> <span id="_Ref165627439" class="anchor"></span>Figure 215: Undo Check In Patient Option from the Pending Appointments Action Menu

### Undo Check Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: This section of the guide is only applicable to users holding the SD SUPERVISOR key. If the user does not have elevated access permissions set to their VistA account, the "Undo Check Out" button in Figure 217 will be greyed out and unavailable for selection. If a user needs access to make changes on this application, please contact your Supervisor for assistance.*

1.  To undo check out on a previously checked out appointment, the user will select the ellipsis, seen in Figure 216, next to the appointment within the History grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/216.png)

> <span id="_Ref165627454" class="anchor"></span>Figure 216: Action Menu Button to Undo Check Out

2.  This will cause the action menu to appear. The user will then need to select the "Undo Check Out Patient" option, seen in Figure 217. This will cause the page to automatically refresh, and the appointment moved to the Pending grid where it is no longer checked out.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/217.png)

> <span id="_Ref165627466" class="anchor"></span>Figure 217: Undo Check Out Patient Option from the Pending Appointments Action Menu

- Note: Users can only undo a checkout on the day of the appointment being checked out.

<span id="_Toc172206327" class="anchor"></span>

### Mark as No Show

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To mark an appointment as no show, the user will select the ellipsis, seen in Figure 218, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/218.png)

> <span id="_Ref165627480" class="anchor"></span>Figure 218: Action Menu Button to Mark as No Show

2.  This will cause the action menu to appear. The user will then need to select the "Mark as No Show" option, seen in Figure 219.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/219.png)

> <span id="_Ref165627496" class="anchor"></span>Figure 219: Mark as No Show Option from the Pending Appointment Action Menu

- Note: Users can only mark an appointment as no show on the day of the appointment after the start time of the appointment has passed.
3.  Once selected, the Confirm No Show window will appear. The user will need to select the "Confirm" button, seen in Figure 220, to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/220.png)

> <span id="_Ref165627515" class="anchor"></span>Figure 220: Confirm Button to Mark as No Show

- Note: The user can also select the "Cancel" button seen in Figure 220 to cancel marking the appointment as no show and go back to the Appointments & Requests page.
5.  The Successfully Marked as No Show window, shown below in Figure 221, will appear. The user can choose to preview the no show letter, if needed, or select "Cancel" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/221.png)

> <span id="_Ref165627546" class="anchor"></span>Figure 221: Preview No Show Letter Window

### Undo Mark as No Show

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To undo no show on a previously marked as no show appointment, the user will select the ellipsis, seen in Figure 222, next to the appointment within the History grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/222.png)

> <span id="_Ref165627572" class="anchor"></span>Figure 222: Action Menu Button to Undo No Show

2.  This will cause the action menu to appear. The user will then need to select the "Undo No Show" option, seen in Figure 223. This will cause the page to automatically refresh, and the appointment moved to the Pending grid where it is no longer marked as no show.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/223.png)

> <span id="_Ref165627596" class="anchor"></span>Figure 223: Undo No Show Option from the Pending Appointments Action Menu

### Calendar View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users have the ability to view the calendar for a specific appointment.

1.  To view, users can select the ellipsis, seen in Figure 224, next to the appointment within the Pending grid.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/224.png)

> <span id="_Ref165627611" class="anchor"></span>Figure 224: Action Menu Button to View on Calendar

2.  This will cause the action menu to appear. The user will then need to select the "View on Calendar" option, seen in Figure 225.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/225.png)

> <span id="_Ref165627624" class="anchor"></span>Figure 225: View on Calendar Option from the Pending Appointments Action Menu

3.  Once on the clinic calendar, the user has the option to utilize all other appointment actions, seen in sections <u>4.4.1 View</u> - <u>4.4.11 Undo Mark as No Show</u> above, by navigating to a specific appointment on the calendar.
4.  The user will then need to right-click on the appointment to bring up the action menu to see the available options, as seen below in Figure 226.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/226.png)

> <span id="_Ref165627668" class="anchor"></span>Figure 226: Action Menu from Calendar View

- Note: The user can also create a walk-in appointment on this page by following the steps outlined in <u>5.4 Create Walk-in</u>.

### Letter Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users have the ability to print different letter types within the ISS application. This can be accomplished by either selecting the "Preview Patient Letter" button when prompted, or by following the steps outlined in <u>4.4.1 View</u>, selecting a letter option in the Select Report dropdown, and clicking "Print" (shown in Figure 227.)

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/227.png)

> <span id="_Ref165627876" class="anchor"></span>Figure 227: Print Button for Letter Printing

1.  After choosing to preview or print a letter, the user will be brought to the Patient Appointment Letter window. From here, the user will need to select a printer from the dropdown seen below in Figure 228.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/228.png)

> <span id="_Ref171429742" class="anchor"></span>Figure 228: Printer Options Dropdown

- Note: If the user chooses "VistA Print Device" from the printer options, the user will need to search and select a VistA printer, as seen below in Figure 229, before the print button becomes available to select.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/229.png)

> <span id="_Ref171432595" class="anchor"></span>Figure 229: VistA Print Option

2.  After choosing a printer from the dropdown seen in Figure 228, the print button will become available to select, as seen in Figure 230. Selecting this will bring the user to the print preview screen.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/230.png)

> <span id="_Ref171432597" class="anchor"></span>Figure 230: Print Button from Patient Appointment Letter Window

- Note: The user can also change the font of the letter from this screen. To do so, the user can enter a specific font size within the box, seen in Figure 231, or select the arrows to increase/decrease the size.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/231.png)

> <span id="_Ref171432596" class="anchor"></span>Figure 231: Changing Font Size for Letter Printing

## Video Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Creating Video Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a video visit, users will need to follow the steps outlined in <u>4.1 Creating Appointment Requests</u> and ensure a clinic with video visit eligibility is selected.
2.  Users will then need to follow the steps outlined in <u>4.3 Creating a Pending Appointment</u>. Once the Appointment Successfully Created window appears, the user will need to select the "Create Video Visit" button, seen in Figure 232, to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/232.png)

> <span id="_Ref165627942" class="anchor"></span>Figure 232: Create Video Visit Button from Creation Window

1.  The Confirm Patient Contact window will appear. The user will need to select the "OK" button, seen in Figure 233, to continue to the New Video Visit page.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/233.png)

> <span id="_Ref165627957" class="anchor"></span>Figure 233: Ok Button to Confirm Patient Contact

2.  On the New Video Visit page, the user will need to fill out all the required information displayed in Figure 234. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/234.png)

> <span id="_Ref165627970" class="anchor"></span>Figure 234: New Video Visit Page

- Note: Users with VA-issued devices will have an additional check box as seen in Figure 235 below. If checked, the appointment will automatically be sent to the user's VA-issued device. If unchecked, the user will continue video visit creation as normal and enter their preferred email.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/235.png)

> <span id="_Ref168580843" class="anchor"></span>Figure 235: VA-issued Device Selection for Video Visit

3.  Once all applicable information has been filled, the user will then select the "Create Video Visit" button, seen in Figure 236, to create the video visit. The user will have the option to preview a patient letter, if needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/236.png)

> <span id="_Ref165628000" class="anchor"></span>Figure 236: Create Video Visit Button when Creating Video Visit

### Viewing Video Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To view a video visit, the user can select the ellipsis, seen in Figure 237, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/237.png)

> <span id="_Ref165628014" class="anchor"></span>Figure 237: Action Menu Button to View Video Visits

2.  This will cause the action menu to appear. The user will then need to select the "View" option, seen in Figure 238.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/238.png)

> <span id="_Ref165628032" class="anchor"></span>Figure 238: View Option for Video Visits from the Pending Appointments Action Menu

3.  The user will be brought to the View Appointment page. On this page, the user will need to select the "View Video Visit" button, seen in Figure 239, to continue to the View Video Visit page.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/239.png)

> <span id="_Ref165628050" class="anchor"></span>Figure 239: View Video Visit Button

### Editing Video Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To edit a video visit, the user can select the ellipsis, seen in Figure 240, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/240.png)

> <span id="_Ref165628063" class="anchor"></span>Figure 240: Action Menu Button to Edit Video Visits

2.  This will cause the action menu to appear. The user will then need to select the "Edit" option, seen in Figure 241.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/241.png)

> <span id="_Ref165628078" class="anchor"></span>Figure 241: Edit Option for Video Visits from the Pending Appointments Action Menu

3.  The user will be brought to the Edit Appointment page. On this page, the user will need to select the "Edit Video Visit" button, seen in Figure 242, to continue to the Edit Video Visit page.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/242.png)

> <span id="_Ref165628092" class="anchor"></span>Figure 242: Edit Video Visits Button

4.  On the Edit Video Visit page, the user can edit any of the editable fields. Once all edits have been made, the user will then select the "Save Changes" button, seen in Figure 243, to save the edits.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/243.png)

> <span id="_Ref165628108" class="anchor"></span>Figure 243: Save Changes Button on the Video Visits Page

### Resending Video Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To resend video visit notifications, the user will select the ellipsis, seen in Figure 244, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/244.png)

> <span id="_Ref165628123" class="anchor"></span>Figure 244: Action Menu Button to Resend Video Visits

2.  This will cause the action menu to appear. The user will then need to select the "View" option, seen in Figure 245.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/245.png)

> <span id="_Ref165628139" class="anchor"></span>Figure 245: View Option for Resending Video Visits from the Pending Appointments Action Menu

3.  The user will be brought to the View Appointment page. On this page, the user will need to select the "View Video Visit" button, seen in Figure 246, to continue to the View Video Visit page.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/246.png)

> <span id="_Ref165628154" class="anchor"></span>Figure 246: View Video Visits Button to Resend Visit

4.  On the View Video Visit page, the user can select the "Resend Video Visit Notifications" button, seen in Figure 247, to resend the video visit notification to all attending parties.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/247.png)

> <span id="_Ref165628168" class="anchor"></span>Figure 247: Resend Video Visit Notification Button

### Cancelling Video Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To cancel a video visit, please follow the steps outlined in either <u>4.4.3 Cancel an APPT, PtCSch,</u> Consult/Procedure, RTC, or VETERAN Appointment or <u>4.4.4 Cancel an MRTC Appointment.</u>

### Launch Video Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To launch a video visit, the user will select the ellipsis, seen in Figure 248, next to the appointment within the Pending grid under Appointments.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/248.png)

> <span id="_Ref165628188" class="anchor"></span>Figure 248: Action Menu Button to Launch Video Visits

2.  This will cause the action menu to appear. The user will then need to select the "View" option, seen in Figure 249.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/249.png)

> <span id="_Ref165628201" class="anchor"></span>Figure 249: View Option for Launching Video Visits from the Pending Appointments Action Menu

3.  The user will be brought to the View Appointment page. On this page, the user will need to select the "View Video Visit" button, seen in Figure 250, to continue to the View Video Visit page.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/250.png)

> <span id="_Ref165628212" class="anchor"></span>Figure 250: View Video Visits Button for Launching Visit

4.  On the View Video Visit page, the user will need to select the "Launch Video Visit" button, seen in Figure 251, to launch the video visit. This will redirect the user to an external website where the video visit will be conducted.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/251.png)

> <span id="_Ref165628232" class="anchor"></span>Figure 251: Launch Video Visit Button

## Printing and Exporting Reports for Appointments and Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Export an Appointment Requests Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To export a report, the user will need to select the "Export" button shown in Figure 252.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/252.png)

> <span id="_Ref165628245" class="anchor"></span>Figure 252: Export Button for Appointment Requests

2.  The user will then be prompted to open or save an Excel worksheet, where the ability to print the list is accessible.

### Print for Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Appointments & Requests page, users have the ability to print a Pending Appointment(s) list and a Scheduled Appointment(s) list. The Pending Appointment(s) list will show all future appointments, including those that have been cancelled, whereas the Scheduled Appointment(s) list will only show all future to-be-attended appointments for the patient.

1.  To print a Pending Appointment(s) list or a Scheduled Appointment(s) list, the user will need to select the "Print" button shown in Figure 253.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/253.png)

> <span id="_Ref165628262" class="anchor"></span>Figure 253: Print Button for Appointment List Options

2.  The user will then select either "Print Pending" for the Pending Appointment(s) list or "Patient Friendly Print" for the Scheduled Appointment(s) list, as seen in Figure 254.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/254.png)

> <span id="_Ref165628274" class="anchor"></span>Figure 254: Appointment Print Options

3.  This will prompt the user to open or save a PDF file, where the ability to print the list is accessible.

# Calendar Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Clinic Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To search for a clinic, the user will select the search bar, seen in Figure 255, and enter a valid clinic name. Once the information has been entered, a list of clinics will appear in the dropdown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/255.png)

> <span id="_Ref165628292" class="anchor"></span>Figure 255: Search Bar for Clinic Search

2.  The user can then select their preferred clinic from the available options to be taken to the Time Slot Calendar for the clinic, as shown below in Figure 256. On this page, the user is able to view available timeslots within the clinic.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/256.png)

> <span id="_Ref165628307" class="anchor"></span>Figure 256: Clinic Calendar Example

## Provider Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To search for a provider, the user will first need to select the "Provider" tab shown in Figure 257.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/257.png)

> <span id="_Ref165628324" class="anchor"></span>Figure 257: Provider Tab

2.  The user will then select the search bar, seen in Figure 258, and enter a valid provider name. Once the information has been entered, a list of providers will appear in the dropdown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/258.png)

> <span id="_Ref165628338" class="anchor"></span>Figure 258: Provider Search Bar

3.  After selecting the preferred provider from the available options, the user will be brought to the Time Slot Calendar for the selected provider. The user can view available timeslots on this page within the associated clinics of the provider, as seen in Figure 259.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/259.png)

> <span id="_Ref165628410" class="anchor"></span>Figure 259: Provider Calendar Example

- Note: The user is able to view information about a clinic by selecting a clinic within the dropdown shown in Figure 260.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/260.png)

> <span id="_Ref165628439" class="anchor"></span>Figure 260: Dropdown to Select a Clinic for Information on Provider Calendar

## Clinic Group Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To search for a clinic group, the user will first need to select the "Clinic Group" tab shown in Figure 261.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/261.png)

> <span id="_Ref165628470" class="anchor"></span>Figure 261: Clinic Group Tab

2.  The user will then select the search bar, seen in Figure 262, and enter a valid clinic group name. Once the information has been entered, a list of clinic groups will appear in the dropdown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/262.png)

> <span id="_Ref165628484" class="anchor"></span>Figure 262: Clinic Group Search Bar

3.  After selecting the preferred clinic group from the available options, the user will be brought to the Time Slot Calendar, as shown below in Figure 263, for the selected clinic group. On this page, the user is able to view available timeslots from entities associated with the clinic group.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/263.png)

> <span id="_Ref165628499" class="anchor"></span>Figure 263: Clinic Group Calendar Example

- Note: The user is able to view information about a clinic by selecting a clinic within the dropdown shown in Figure 264.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/264.png)

> <span id="_Ref165628515" class="anchor"></span>Figure 264: Dropdown to Select a Clinic for Information on Clinic Group Calendar

- Note: The user has the ability to reorder the clinic order. To do so, the user will need to select "Reorder Clinics," shown is Figure 265, then drag and drop the clinics into their preferred order. Once completed, the user will need to select "OK" to save the changes.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/265.png)

> <span id="_Ref165628533" class="anchor"></span>Figure 265: Reorder Clinics Window

## Create Walk-in

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a walk-in, the user will first need to follow the steps outlined in <u>3.1 Patient Search</u> to bring a patient into context. Then, the user will need to navigate to the intended calendar by following the steps in any of the following; <u>4.4.12 Calendar View</u>, <u>5.1 Clinic Search</u>, <u>5.2 Provider Search</u>, or <u>Clinic Group Search</u>.
2.  Once a patient has been brought into context, the user will be able to right click on the preferred timeslot within the calendar and select "Create Walk-in," seen in Figure 266.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/266.png)

> <span id="_Ref165628554" class="anchor"></span>Figure 266: Create Walk-in Button on Calendar

3.  The user will be brought to the New Walk-in Appointment page. On this page, the user will need to fill out all the required information displayed in Figure 267. The user can also fill out any optional information as needed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/267.png)

> <span id="_Ref165628567" class="anchor"></span>Figure 267: New Walk- in Appointment Page

4.  Once all applicable information has been filled, the user will select the "Create Appointment" button, seen in Figure 268, to create the walk-in appointment.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/268.png)

> <span id="_Ref165628580" class="anchor"></span>Figure 268: Create Appointment Button for New Walk-in

- Note: The user can also select the "Cancel" button seen in Figure 268 to exit creating an appointment and go back to the Appointments & Requests page.
8.  The Appointment Successfully Created window, shown below in Figure 269, will appear. The user can choose to preview the patient letter, if needed, or select "Close" to continue.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/269.png)

> <span id="_Ref165628613" class="anchor"></span>Figure 269: Preview Patient Letter Window for Walk-in Appointment

# Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Query Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user will need to navigate to the home screen to find the Query Tool. Please see Figure 270 below for an overview on how to perform a query and the rules associated for each section. Please note that only the first 200 search results will appear in each query.

![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/270.png)

<span id="_Ref165629440" class="anchor"></span>Figure 270: Overview for How to Perform a Query

Once the minimum amount of search criteria has been made and the user is ready to make a search, it may be helpful to utilize the Change Sort Order function for better results. Simply select the dropdown under Change Sort Order and select the desired option. Please note that the "Default" sort order is Priority Group, PID, and Origination Date.

### Section 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Within the query tool, the user will find section 1 where patients will need to be selected for the query. To begin, the user will select the search bar under Patients, seen in Figure 271, and enter valid search criteria. A dropdown will appear with a list of patients that match the criteria given.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/271.png)

> <span id="_Ref165629400" class="anchor"></span>Figure 271: Dropdown to Select a Patient for Section 1 of Query Tools

2.  The user can then select the needed patient from the available options.
3.  Repeat steps 1 and 2 for as many patients the user wishes to include in the query.
- Note: The maximum number of patients that can be included in a query search is 50.
- Note: If the user needs to remove any previously selected patients, select either the "x" button next to any individual patient in the Patients field, or select "x" shown in Figure 272 to remove all previously selected patients.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/272.png)

> <span id="_Ref165629418" class="anchor"></span>Figure 272: Remove Previously Selected Patient Icon

4.  After selecting the patients needed, the user can run the query by selecting "Run Query," shown in Figure 273. Optionally, the user can narrow down search results by following the steps outlined in either <u>6.1.2 Section 2</u> or <u>6.1.3 Section 3</u>.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/273.png)

> <span id="_Ref165629464" class="anchor"></span>Figure 273: Run Query Button using Section 1 of Query Tools

### Section 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Within the query tool, the user will find section 2. To begin, the user will select the dropdown under Requests, seen in Figure 274, and choose a given request option. The user can individually add different requests or choose "Select All" to add all the options shown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/274.png)

> <span id="_Ref165629497" class="anchor"></span>Figure 274: Dropdown to Select a Request for Section 2 of Query Tools

2.  The user must then select "+ Add to List," seen in Figure 275, to open the Clinics/Services window.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/275.png)

> <span id="_Ref165629516" class="anchor"></span>Figure 275: Button to Add Clinics and Services in Section 2 of Query Tools

3.  After selecting the search bar shown in Figure 276 below, the user will need to enter valid search criteria. This will cause any applicable results to appear in the box below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/276.png)

> <span id="_Ref165629544" class="anchor"></span>Figure 276: Search Bar for Clinics/Services for Section 2 of Query Tools

4.  The user will then need to either select the add button next to any individual Clinic/Service option or can select the "Add All" button shown in Figure 277 to add all the options listed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/277.png)

> <span id="_Ref165629574" class="anchor"></span>Figure 277: Button to Add All Clinics/Services

- Note: If the user needs to remove any previously selected Clinics/Services from the query, the user can select either the remove button next to an individual Clinic/Service in the Selected for Query section or select the "Remove All" button shown in Figure 278 to remove all the options listed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/278.png)

> <span id="_Ref165629593" class="anchor"></span>Figure 278: Button to Remove All Clinics/Services

5.  The user will then select the "Apply" button, as seen in Figure 279, to be brought back to the query tool with any selected results applied.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/279.png)

> <span id="_Ref165629635" class="anchor"></span>Figure 279: Apply Button for Clinics/Services for Section 2 of Query Tools

6.  After filling the required fields, the user can run the query by selecting "Run Query," shown in Figure 280. Optionally, the user can narrow down search results by following the steps outlined in either <u>6.1.1 Section 1</u> or <u>6.1.3 Section 3</u>.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/280.png)

> <span id="_Ref165629654" class="anchor"></span>Figure 280: Run Query Button using Section 2 of Query Tools

### Section 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please note that all search criteria within section 3 is optional. If using section 3, the user must have entered search criteria into either Section 1, Section 2, or both.

1.  To begin, the user can select the dropdown under Priority Groups, seen in Figure 281, and choose a given priority group option. The user can individually add different priority groups or choose "Select All" to add all the options shown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/281.png)

> <span id="_Ref165629668" class="anchor"></span>Figure 281: Dropdown to Select a Priority Group for Section 3 of Query Tools

2.  The user can select the dropdown under Wait Time, seen in Figure 282, and choose the preferred wait time length. The user can choose "All Days" to view all wait times options.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/282.png)

> <span id="_Ref165629702" class="anchor"></span>Figure 282: Dropdown to Select a Wait Time for Section 3 of Query Tools

3.  When narrowing down a specific date, the user can select either an origination date, or PID (not both), if needed.
4.  If consult was chosen as a requests option from Section 2, the user can select an urgency type by navigating the dropdown selections, as seen in Figure 283.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/283.png)

> <span id="_Ref165629717" class="anchor"></span>Figure 283: Dropdown to Select an Urgency Status for Section 3 of Query Tools

## Recurring Slot Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To begin, the user will need to navigate to the Recurring Slot Availability tab on the homepage shown in Figure 284.

![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/284.png)

<span id="_Ref198049107" class="anchor"></span>Figure 284: Recurring Slot Availability Tab

2.  Under the "Appointment For" field, the Clinic radio button will be auto-populated. The user can either continue on and enter a clinic name or select either the "Provider" or "Clinic Group" radio button and enter the appropriate search criteria (see Figure 285 for example).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/285.png)

<span id="_Ref198049108" class="anchor"></span>Figure 285: Appointment For Search Bar

3.  The user will then need to fill out the remaining required and optional fields, as seen below in Figure 286.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/286.png)

<span id="_Ref198049109" class="anchor"></span>Figure 286: Recurring Slot Availability Fields

4.  Once all required fields have been populated, the user can select the "Search" button shown below in Figure 287.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/287.png)

<span id="_Ref198049110" class="anchor"></span>Figure 287: Search Button for Recurring Slot Availability

- Note: After populating all required fields, the user will see a Search Summary of their choices (see Figure 287 for example).
5.  Results from the search will populate on the right-hand side of the page, as seen in Figure 288. For more information on how to navigate these results, see section <u>2.3 Filters</u>.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/288.png)

<span id="_Ref198049111" class="anchor"></span>Figure 288: Example of Recurring Slot Availability Search Results

6.  To clear results, the user can select either the "Clear" button in Figure 288, or the "Reset All Fields" button seen in Figure 289.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/289.png)

<span id="_Ref198049112" class="anchor"></span>Figure 289: Reset All Fields Button for Recurring Slot Availability

- Note: The user can also choose to go back to their previously completed search by selecting the "Last Search" button seen in Figure 290.

  ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/290.png)

> <span id="_Ref198049113" class="anchor"></span>Figure 290: Last Search Button for Recurring Slot Availability

7.  To export search results, select the "Export" button seen in Figure 291. This will allow the user to download the report into an Excel document.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/291.png)

<span id="_Ref198049114" class="anchor"></span>Figure 291: Export Button for Recurring Slot Availability

# System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the guide is only applicable to users who have been provisioned the SDECZMGR key. To access, select the System tab, seen in Figure 292, at the top of the webpage.

![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/292.png)

<span id="_Ref165634463" class="anchor"></span>Figure 292: Systems Tab on the Homepage

## Privileged Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To add or remove Privileged Users, the user will need to select the "Privileged Users" tab shown in Figure 293.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/293.png)

> <span id="_Ref165634490" class="anchor"></span>Figure 293: Privileged Users Tab

2.  The user will then need to enter the name of a prohibited clinic into the search bar. This will cause any applicable results to appear in a dropdown, as seen in Figure 294 below, where the user can select the intended clinic.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/294.png)

> <span id="_Ref165634557" class="anchor"></span>Figure 294: Search Bar for Privileged Users

3.  The (Clinic Name) window will appear. From here, the user can either search for a user by manually scrolling through the Users section or filter the results by typing in a user's name into the Search Users search bar, seen in Figure 295. Once the necessary user is found, select the add button next to the name. Repeat this step for each user that needs to be added to the prohibited clinic.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/295.png)

> <span id="_Ref165634583" class="anchor"></span>Figure 295: Search Users Look Up for Clinics Under Privileged Users

- Note: If the user needs to remove any previously selected users, select either the remove button next to any individual user, or select the "Remove All" button shown in Figure 296 to remove all of the users listed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/296.png)

> <span id="_Ref165634632" class="anchor"></span>Figure 296: Button to Remove All Users from a Clinic

4.  Once all Privileged users have been added, select the "Save Changes" button, seen in Figure 297, to save all changes.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/297.png)

> <span id="_Ref165634671" class="anchor"></span>Figure 297: Save Changes Button for Privileged Users

## Clinic Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit Clinic Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To search for a Clinic Group, the user will need to select the "Clinic Groups" tab shown in Figure 298.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/298.png)

> <span id="_Ref165634716" class="anchor"></span>Figure 298: Selecting Clinic Groups Tab for Editing

2.  The user will then need to enter the name of a clinic group into the search bar. This will cause any applicable results to appear in a dropdown, as seen in Figure 299 below, where the user can select the intended clinic group.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/299.png)

> <span id="_Ref165634750" class="anchor"></span>Figure 299: Search Bar for Finding a Clinic Group to Edit

3.  The user will be brought to the (Clinic Group Name) page. From here, the user can select the "Edit Clinic Group" button, seen in Figure 300, to open the Edit Clinic Group window.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/300.png)

> <span id="_Ref165634774" class="anchor"></span>Figure 300: Edit Clinic Group Button

4.  To change the clinic group name, select the field shown in Figure 301 and make the necessary changes.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/301.png)

> <span id="_Ref165634805" class="anchor"></span>Figure 301: Field for Clinic Group Name when Editing a Clinic Group

5.  To add resources, the user will need to enter valid search criteria into the search bar seen in Figure 302. This will cause any applicable results to appear in the box below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/302.png)

> <span id="_Ref165634829" class="anchor"></span>Figure 302: Search Bar to Find Resources when Editing a Clinic Group

8.  The user will then need to either select the add button next to any individual resource option or select the "Add All" button shown in Figure 303 to add all the options listed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/303.png)

> <span id="_Ref165634853" class="anchor"></span>Figure 303: Button to Add All Resources when Editing a Clinic Group

- Note: If the user needs to remove any previously selected resources, the user can select either the remove button next to an individual resource in the Clinic Group Resources section or select the "Remove All" button shown in Figure 304 to remove all the options listed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/304.png)

> <span id="_Ref165634969" class="anchor"></span>Figure 304: Button to Remove All Resources when Editing a Clinic Group

9.  After making the necessary edits, the user will need to select the "Save Changes" button, seen in Figure 305, to save all changes.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/305.png)

> <span id="_Ref165634997" class="anchor"></span>Figure 305: Save Changes Button for Editing Clinic Groups

10. The user will be brought to the Successfully Updated Clinic Group window shown in Figure 306 below. Select close to finish.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/306.png)

> <span id="_Ref165635026" class="anchor"></span>Figure 306: Successfully Updated Clinic Group Window

### Remove Clinic Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To search for a Clinic Group, the user will need to select the "Clinic Groups" tab shown in Figure 307.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/307.png)

> <span id="_Ref165635046" class="anchor"></span>Figure 307: Selecting Clinic Groups Tab to Remove

2.  The user will then need to enter the name of a clinic group into the search bar. This will cause any applicable results to appear in a dropdown, as seen in Figure 308 below, where the user can select the intended clinic group.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/308.png)

> <span id="_Ref165635068" class="anchor"></span>Figure 308: Search Bar for Finding a Clinic Group to Remove

3.  The user will be brought to the (Clinic Group Name) page. From here, the user can select the "Remove Clinic Group" button, seen in Figure 309. This will cause the Remove Clinic Group? notification to appear.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/309.png)

> <span id="_Ref165635090" class="anchor"></span>Figure 309: Remove Clinic Group Button

4.  The user can select the "Remove Clinic Group" button, seen in Figure 310, to successfully remove the clinic group.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/310.png)

> <span id="_Ref165635120" class="anchor"></span>Figure 310: Remove Clinic Group Button from Confirmation Window

- Note: The user can also select the "Cancel" button or the "x" button seen in the upper right hand corner of the notification in Figure 310 to exit the process and go back to the (Clinic Group Name) page.
5.  The user will be brought to the Successfully Deleted Clinic Group window shown in Figure 311 below. Select close to finish.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/311.png)

> <span id="_Ref165635217" class="anchor"></span>Figure 311: Successfully Deleted Clinic Group Window

### Creating New Clinic Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To search for a Clinic Group, the user will need to select the "Clinic Groups" tab shown in Figure 312.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/312.png)

> <span id="_Ref165635244" class="anchor"></span>Figure 312: Selecting Clinic Groups Tab to Create New Clinic Group

2.  The user can then select the "Create New Clinic Group" button shown in Figure 313 to be brought to the Create New Clinic Group window.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/313.png)

> <span id="_Ref165635267" class="anchor"></span>Figure 313: Create New Clinic Group Button

3.  To add a name for the clinic group, the user will need to enter a preferred name into the Clinic Group Name section seen in Figure 314.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/314.png)

> <span id="_Ref165635297" class="anchor"></span>Figure 314: Field for Clinic Group Name when Creating New Clinic Group

4.  To add resources to the clinic group, the user will need to enter valid search criteria into the search bar seen in Figure 315. This will cause any applicable results to appear in the box below.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/315.png)

> <span id="_Ref165635314" class="anchor"></span>Figure 315: Search Bar to Find Resources when Creating a New Clinic Group

5.  The user will then need to either select the add button next to any individual resource option or select the "Add All" button shown in Figure 316 to add all the options listed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/316.png)

> <span id="_Ref165635338" class="anchor"></span>Figure 316: Button to Add All Resources when Creating a Clinic Group

- Note: If the user needs to remove any previously selected resources, the user can select either the remove button next to an individual resource in the Clinic Group Resources section or select the "Remove All" button shown in Figure 317 to remove all the options listed.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/317.png)

> <span id="_Ref165635351" class="anchor"></span>Figure 317: Button to Remove All Resources when Creating a Clinic Group

6.  Once all necessary clinic group resources have been added, the user will need to select the "Create Clinic Group" button, seen in Figure 318, to create the new clinic group.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/318.png)

> <span id="_Ref165635378" class="anchor"></span>Figure 318: Create Clinic Group Button

7.  The user will be brought to the Successfully Created Clinic Group window shown in Figure 319 below. Select close to finish.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/319.png)

> <span id="_Ref165635397" class="anchor"></span>Figure 319: Successfully Created Clinic Group Window

## Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To access the Activity Report, the user will need to select the "Activity Report" tab seen in Figure 320.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/320.png)

<span id="_Ref187426472" class="anchor"></span>Figure 320: Activity Report Tab

2.  Upon selecting the "Activity Report" tab, the user will be taken to the Overview page by default. The user can then select any of the sub-tabs seen in Figure 321 to access them.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/321.png)

<span id="_Ref187426473" class="anchor"></span>Figure 321: Sub-Tabs for the Activity Report

3.  Within the sub-tabs, the user can navigate the graphs and tables for information relating to each section's title (see Figure 322 for example).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/322.png)

<span id="_Ref193193725" class="anchor"></span>Figure 322: Example of Data within Activity Report Sub-Tabs

- Note: See sections 2.3.2 Sort by Ascending and Descending, 2.3.3 Toggle Density, 2.3.4 Show, Hide, and Search Filters, and 2.3.5 Filtering Rows for information on filtering tables.
4.  The user can also filter the results shown within each sub-tab by selecting the preferred date range from the dropdown calendar found in the upper righthand corner of each page (see Figure 323).

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/323.png)

<span id="_Ref187426474" class="anchor"></span>Figure 323: Date Range Calendar Dropdown for Activity Report

- Note: While all four sections allow filtering of the date range, only the Overview tab allows the user to filter by VISN.
5.  On certain graphs within the "Activity Reports" tab, the user can hover the cursor over data points, as seen in Figure 324, to receive more context about the information being shown.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/324.png)

<span id="_Ref187426475" class="anchor"></span>Figure 324: Data Point Information on Activity Report Graphs

6.  The user can also export data of any table within the tabs by selecting the "Export" button seen in Figure 325. The user will then be prompted to open or save an Excel worksheet, where the ability to print the information is accessible.

> ![](integrated-scheduling-solution-iss-release-1-22-3-user-guide/325.png)

<span id="_Ref187426476" class="anchor"></span>Figure 325: Export Button for Activity Report

# References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Cancellation Reasons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                           | Type               | Ability to Reopen |
|--------------------------------|--------------------|-------------------|
| Appointment No Longer Required | Clinic             | No                |
| Block and Move                 | Clinic             | Yes               |
| Clinic Cancelled               | Clinic             | Yes               |
| Clinic Staffing                | Clinic             | Yes               |
| Death in Family                | Patient            | Yes               |
| Inpatient Status               | Clinic             | Yes               |
| Other                          | Clinic and Patient | Yes               |
| Pandemic                       | Clinic and Patient | Yes               |
| Patient Death                  | Clinic             | No                |
| Patient Not Eligible           | Clinic             | No                |
| Scheduling Conflict/Error      | Clinic             | Yes               |
| Transfer Opt Care to Other VA  | Clinic and Patient | No                |
| Travel Difficulty              | Patient            | Yes               |
| Unable to Keep Appointment     | Patient            | Yes               |
| Walk-In Entered in Error       | Clinic             | No                |
| Walk-In No Longer Necessary    | Patient            | No                |
| Weather                        | Clinic and Patient | Yes               |


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Integrated Scheduling Solution (ISS) Release 1.7.1.0 User Guide

### Show/Hide Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user can also hide a column from appearing. To do so, the user will need to select the vertical ellipsis next to the column they wish to hide, seen in Figure 34 below.

> ![](integrated-scheduling-solution-iss-release-1-7-1-0-user-guide/034.png)

> <span id="_Ref165300554" class="anchor"></span>Figure 34: Selecting Column Actions to Show/Hide Columns

2.  The user can then select "Hide (Column Name) column," seen below in Figure 35, to hide the column.

> ![](integrated-scheduling-solution-iss-release-1-7-1-0-user-guide/035.png)

> <span id="_Ref165300568" class="anchor"></span>Figure 35: Hide Column Button from Column Actions Dropdown

- Note: The "Actions" column cannot be moved or removed from the table.
3.  To reveal any columns that have been hidden, select the "Show all columns" button seen in Figure 36.

> ![](integrated-scheduling-solution-iss-release-1-7-1-0-user-guide/036.png)

> <span id="_Ref165300585" class="anchor"></span>Figure 36: Show All Columns Button from Column Actions Dropdown

4.  Optionally, the three vertical bars pictured in Figure 37 titled "Show/Hide Columns" can be used to show/hide columns.

> ![](integrated-scheduling-solution-iss-release-1-7-1-0-user-guide/037.png)

> <span id="_Ref165300598" class="anchor"></span>Figure 37: Show/Hide Columns Button

5.  Once selected, the user will be presented with the options shown below in Figure 38. To begin, the user can select the "Hide All" button to hide all the columns within the table.

> ![](integrated-scheduling-solution-iss-release-1-7-1-0-user-guide/038.png)

> <span id="_Ref165300615" class="anchor"></span>Figure 38: Show/Hide Columns Options

6.  The user can also select "Show All" to make all previously hidden columns appear again.
- Note: The "Show All" button will not be able to be selected until at least one column has been hidden.
7.  Another option presented to the user is to manually select which columns they would like to show and hide. To hide a column, select the button next to the column's name that is currently being shown (indicated by the button's blue appearance seen in Figure 39). The button will become grey, and the column will be hidden in the table.

> ![](integrated-scheduling-solution-iss-release-1-7-1-0-user-guide/039.png)

> <span id="_Ref165300653" class="anchor"></span>Figure 39: Example Button Appearance Indicating Column is Shown

8.  The user can also choose to show any previously hidden column by selecting the button next to a hidden column (indicated by the button's grey appearance seen in Figure 40). The button will become blue, and the column will be shown in the table.

> ![](integrated-scheduling-solution-iss-release-1-7-1-0-user-guide/040.png)

> <span id="_Ref165300674" class="anchor"></span>Figure 40: Example Button Appearance Indicating Column is Hidden
