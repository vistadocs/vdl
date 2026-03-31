---
title: Clinical Configuration Manager (CCM) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Clinical Configuration Manager (CCM)
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
  - clinic
  - button
  - table
  - contents
  - shown
  - class
  - anchor
  - seen
page_count: 0
word_count: 12837
section_count: 32
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 2
revision_newest: 3/3/2026
revision_oldest: 12/4/2025
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/ccm_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/ccm_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=100"
---

![](clinical-configuration-manager-ccm-user-guide/001.png)

OFFICE OF  
INFORMATION  
AND TECHNOLOGY

Clinic Configurations Manager  
User Interface (CCM-UI)  
User Guide

*Version 1.10.0* \| March 2026
## Table of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Table 1: Filter Descriptions for Clinic Audit Report [131](#_Ref185861019)](#_Ref185861019)

[Table 2: Tool Tip Descriptions [154](#_Toc223532592)](#_Toc223532592)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date      | Version | Description                                                              | Author              |
|-----------|---------|--------------------------------------------------------------------------|---------------------|
| 3/3/2026  | 1.10.0  | Updated UI changes to Multi-select timeslots and Timeslot Recovery       | Booz Allen Hamilton |
| 12/4/2025 | 1.7.0   | Updated UI changes to v3, added Letters and Annual Clinic Review Section | Booz Allen Hamilton |

<span id="_Ref185861019" class="anchor"></span>Table 1: Filter Descriptions for Clinic Audit Report

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
  - [Prerequisite Credentials](#prerequisite-credentials)
  - [PIV Login](#piv-login)
- [Familiarizing Yourself with CCM-UI](#familiarizing-yourself-with-ccm-ui)
  - [Changing Site Locations](#changing-site-locations)
  - [My Account](#my-account)
    - [User Preferences](#user-preferences)
    - [Logging Out of CCM-UI](#logging-out-of-ccm-ui)
  - [Resources](#resources)
  - [Filters](#filters)
    - [Sort by Ascending and Descending](#sort-by-ascending-and-descending)
    - [Toggle Density](#toggle-density)
    - [Filtering Rows](#filtering-rows)
    - [Filtering Columns](#filtering-columns)
    - [Show, Hide, and Search Filters](#show-hide-and-search-filters)
    - [Search Function](#search-function)
- [Search and View Clinic Configurations](#search-and-view-clinic-configurations)
  - [Search for a Clinic Configuration](#search-for-a-clinic-configuration)
  - [View Current Clinic Configurations](#view-current-clinic-configurations)
    - [Viewing Clinic Settings](#viewing-clinic-settings)
    - [Viewing Preselected Settings](#viewing-preselected-settings)
    - [Viewing Optional Settings](#viewing-optional-settings)
    - [Viewing Clinic Availability](#viewing-clinic-availability)
- [Editing Clinic Configurations](#editing-clinic-configurations)
  - [Editing Mandatory Fields](#editing-mandatory-fields)
  - [Editing Preselected Default Fields](#editing-preselected-default-fields)
  - [Editing Optional Fields](#editing-optional-fields)
  - [Editing Clinic Availability](#editing-clinic-availability)
    - [Add or Modify Timeslots for Single Day Modification](#add-or-modify-timeslots-for-single-day-modification)
    - [Add or Modify Timeslots for Indefinite Modification](#add-or-modify-timeslots-for-indefinite-modification)
    - [Add or Modify Timeslots for Multi-select Modification](#add-or-modify-timeslots-for-multi-select-modification)
    - [Add or Modify Timeslots for Recurring Modification](#add-or-modify-timeslots-for-recurring-modification)
  - [Cancelling and Restoring Timeslots](#cancelling-and-restoring-timeslots)
    - [Cancelling a Timeslot](#cancelling-a-timeslot)
    - [Restoring a Timeslot](#restoring-a-timeslot)
  - [Creating a New Clinic](#creating-a-new-clinic)
    - [Mandatory Fields](#mandatory-fields)
    - [Preselected Settings](#preselected-settings)
    - [Optional Settings](#optional-settings)
  - [Inactivating and Reactivating a Clinic](#inactivating-and-reactivating-a-clinic)
    - [Inactivating a Clinic](#inactivating-a-clinic)
    - [Reactivating a Clinic](#reactivating-a-clinic)
  - [Replicating a Clinic](#replicating-a-clinic)
- [Clinic Audit Report](#clinic-audit-report)
  - [Familiarizing Yourself with the Clinic Audit Report](#familiarizing-yourself-with-the-clinic-audit-report)
  - [Filtering Reports and Exporting Data](#filtering-reports-and-exporting-data)
    - [Filtering Results](#filtering-results)
    - [Filtering with Dropdowns](#filtering-with-dropdowns)
    - [Filtering by Date Range](#filtering-by-date-range)
  - [Exporting Data](#exporting-data)
- [Letters](#letters)
  - [Create a Letter](#create-a-letter)
  - [Edit a Letter](#edit-a-letter)
  - [Delete a Letter](#delete-a-letter)
- [VA Tool Set](#va-tool-set)
  - [Veteran Self Scheduling](#veteran-self-scheduling)
    - [View Veteran Self Scheduling](#view-veteran-self-scheduling)
    - [Edit Veteran Self Scheduling](#edit-veteran-self-scheduling)
  - [Veteran Appointment Requests](#veteran-appointment-requests)
    - [View Veteran Appointment Requests](#view-veteran-appointment-requests)
    - [Edit Veteran Appointment Requests](#edit-veteran-appointment-requests)
- [Annual Clinic Profile Review](#annual-clinic-profile-review)
- [References](#references)
  - [Additional Features and Options for CCM-UI](#additional-features-and-options-for-ccm-ui)
  - [Tool Tip Descriptions](#tool-tip-descriptions)
  - [Additional Help with Errors](#additional-help-with-errors)
    - [Connection Issues Error](#connection-issues-error)
    - [Server Issue Error](#server-issue-error)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinic Configuration Manager User Interface (CCM-UI) is a user friendly, easy to navigate application that will help users View, Edit and Create data attribution changes to and from either the VA Tool Set or VistA systems.

## Prerequisite Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user’s PIV card must be linked to the VistA site. (See [<u>link</u>](https://urldefense.com/v3/__https:/yourit.va.gov/kb_view.do?sysparm_article=KB0013359__;!!May37g!IDPcRnXuA41Qsx8l5PC9V-RCPZs-oQgJY5ff0TiThG5w5YC5glJL3EhBNB3EloD_HTbfRTs9JzMgV8wVvNcmw-Ke$) for guidance)
2.  After confirming that the user’s PIV card is linked to the user’s VistA account, the user will be able to sign into the CCM-UI.
3.  To access the Clinic Configuration Manager Change Assessment Report, users will need to be added to the [<u>VHACLINICPROFILEMANAGERS@VA.GOV</u>](mailto:VHACLINICPROFILEMANAGERS@VA.GOV) email distribution group.
- Note: Users who have not been added to the [<u>VHACLINICPROFILEMANAGERS@VA.GOV</u>](mailto:VHACLINICPROFILEMANAGERS@VA.GOV) email distribution group will need to contact their supervisor to be added.
- Note: If a user has not been added to the appropriate email distribution group, the user will receive the following message seen in [⁠Figure 1⁠](#_Ref185007111) below notifying them that the correct access permissions have not been allocated to the account.

  ![](clinical-configuration-manager-ccm-user-guide/002.png)

> <span id="_Ref185007111" class="anchor"></span>Figure 1: Access Permissions Notification

## PIV Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Begin by opening a browser and going to the following web address: [<u>link</u>](https://staff.apps.va.gov/vas-config/). The VA Single Sign-On page will then appear. Select the “Sign in with PIV” option, as seen in [⁠Figure 2⁠](#_Ref183435089), to proceed with the log in process.

> ![](clinical-configuration-manager-ccm-user-guide/003.png)

> <span id="_Ref183435089" class="anchor"></span>Figure 2: PIV Card Sign-On Image

2.  After selecting, an ActivClient Login dialog box will appear to prompt you to enter your PIN. Type the numbers of your PIN as prompted in [⁠Figure 3⁠](#_Ref183435104). If authentication is successful, CCM-UI will load. If it is not successful, you will be prompted to enter your correct PIN instead.

> ![](clinical-configuration-manager-ccm-user-guide/004.png)

> <span id="_Ref183435104" class="anchor"></span>Figure 3: ActivClient Login Pop-Up Window

# Familiarizing Yourself with CCM-UI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Changing Site Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To change site locations, the user must first select the green box in the upper right-hand corner of the page as shown in [⁠Figure 4⁠](#_Ref184736303).

> ![](clinical-configuration-manager-ccm-user-guide/005.png)

> <span id="_Ref184736303" class="anchor"></span>Figure 4: Change Site Locations Buttons

2.  The user will then need to select the requested site location by clicking the arrow shown in [⁠Figure 5⁠](#_Ref184736361) if it is not already the default selection.

> ![](clinical-configuration-manager-ccm-user-guide/006.png)

> <span id="_Ref184736361" class="anchor"></span>Figure 5: Change Site Location Accordion

- Note: The user will only see sites that are provisioned to their account after selecting the arrow shown in [⁠Figure 5⁠](#_Ref184736361). If sites assigned to the user are not shown, please contact the local Clinical Applications Coordinator or Supervisor for assistance.
3.  The user can then select the button boxed below in [⁠Figure 6⁠](#_Ref184737185) to view the selected settings.

> ![](clinical-configuration-manager-ccm-user-guide/007.png)

> <span id="_Ref184737185" class="anchor"></span>Figure 6: View Settings Button

## My Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To change user preferences, the user can select the “My Account” button in the upper right-hand corner, seen in [⁠Figure 7⁠](#_Ref207198258), to open the dropdown.

> ![](clinical-configuration-manager-ccm-user-guide/008.png)

<span id="_Ref207198258" class="anchor"></span>Figure 7: My Account Button for User Preferences

2.  The user can then select the “Preferences” button shown in [⁠Figure 8⁠](#_Ref207198308) to be taken to the User Preferences page.

> ![](clinical-configuration-manager-ccm-user-guide/009.png)

<span id="_Ref207198308" class="anchor"></span>Figure 8: Preferences Button

#### Default Site Location Preferences

1.  To adjust the default site location, the user will need to select the arrow, seen in [⁠Figure 9⁠](#_Ref207198350) below, to choose a location from the dropdown.

> ![](clinical-configuration-manager-ccm-user-guide/010.png)

<span id="_Ref207198350" class="anchor"></span>Figure 9: Default Site Location Dropdown Button

2.  After selecting a location, the user can then select the “Save” button in [⁠Figure 10⁠](#_Ref207198402) to save the change.

> ![](clinical-configuration-manager-ccm-user-guide/011.png)

<span id="_Ref207198402" class="anchor"></span>Figure 10: Save Changes Button for Default Site Locations

3.  To reset the default location, select the “Clear Selection” button seen in [⁠Figure 11⁠](#_Ref207198426).

> ![](clinical-configuration-manager-ccm-user-guide/012.png)

<span id="_Ref207198426" class="anchor"></span>Figure 11: Clear Selection Button for Default Site Location

- Note: User preferences will be reset whenever the user clears their browser cache.

#### Locations in Site Selector Preferences

1.  To change the locations in the site selector, the user will need to select the buttons boxed in [⁠Figure 12⁠](#_Ref207198601). The user will know that the site is hidden when a “\\ displays through the icon as shown in [⁠Figure 13⁠](#_Ref207198634).

> ![](clinical-configuration-manager-ccm-user-guide/013.png)

<span id="_Ref207198601" class="anchor"></span>Figure 12: Toggle Button for Locations in Site Selector

2.  The user can then select the “Save” button seen in [⁠Figure 13⁠](#_Ref207198634) to save their changes.

> ![](clinical-configuration-manager-ccm-user-guide/014.png)

<span id="_Ref207198634" class="anchor"></span>Figure 13: Save Changes Button for Locations in Site Selector

3.  To reset preferences, select the “Show All” button within the individual sections as seen in [⁠Figure 14⁠](#_Ref207198686).

> ![](clinical-configuration-manager-ccm-user-guide/015.png)

<span id="_Ref207198686" class="anchor"></span>Figure 14: Show All Button for Locations in Site Selector

- Note: User preferences will be reset whenever the user clears their browser cache.

### Logging Out of CCM-UI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To log out of CCM-UI, the user will need to select the “My Account” button in the upper-right hand corner, as seen in [⁠Figure 15⁠](#_Ref184740944).

> ![](clinical-configuration-manager-ccm-user-guide/016.png)

> <span id="_Ref184740944" class="anchor"></span>Figure 15: My Account Button for CCM-UI

2.  The user will then need to select the “Log Out” button from the dropdown menu shown in [⁠Figure 16⁠](#_Ref205391213).

> ![](clinical-configuration-manager-ccm-user-guide/017.png)

<span id="_Ref205391213" class="anchor"></span>Figure 16: Log Out Button for CCM-UI

3.  Upon logging out of the CCM-UI application, the user will be taken to the page seen in [⁠Figure 17⁠](#_Ref184740966) that will prompt them to log out of the VA SSOi and close the browser.

> ![](clinical-configuration-manager-ccm-user-guide/018.png)

> <span id="_Ref184740966" class="anchor"></span>Figure 17: Logged Out of Mobile Applications Page

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For additional information or help with the CCM-UI application, the user can select the “Resources” tab to the left of the CCM-UI page. See [⁠Figure 18⁠](#_Ref184740919) below for reference.

![](clinical-configuration-manager-ccm-user-guide/019.png)

<span id="_Ref184740919" class="anchor"></span>Figure 18: Example of Additional Links for CCM-UI

## Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Sort by Ascending and Descending

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When looking for clinics within the grid, the user can sort rows by hovering the cursor next to a column’s name and selecting the arrow button that appears in [⁠Figure 19⁠](#_Ref185610605).

> ![](clinical-configuration-manager-ccm-user-guide/020.png)

<span id="_Ref185610605" class="anchor"></span>Figure 19: Ascending/Descending Filter Arrow

2.  Selecting the arrow once will cause results to sort by ascending order (↑), a second time to sort by descending order (notated by ↓), and a third time to cause results to appear in the default order again (notated with no arrow).

### Toggle Density

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user has the option to adjust toggle density of the grid. To begin adjusting the toggle density, select the button shown in [⁠Figure 20⁠](#_Ref185610630).

> ![](clinical-configuration-manager-ccm-user-guide/021.png)

<span id="_Ref185610630" class="anchor"></span>Figure 20: Toggle Density Button

2.  There are three different options for the user to choose from depending on the user’s preference. Simply keep selecting the “Toggle Density” button to rotate through the options until the user finds their preferred density.

### Filtering Rows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users can increase or decrease the number of rows shown on the page by selecting the arrow shown in [⁠Figure 21⁠](#_Ref185610649)

> ![](clinical-configuration-manager-ccm-user-guide/022.png)

<span id="_Ref185610649" class="anchor"></span>Figure 21: Rows per Page Option

2.  Users can also navigate the grid to more available clinics by selecting the arrows “\<” to navigate one page backwards and “\>” to navigate one-page forwards, as seen in [⁠Figure 22⁠](#_Ref185610670).

> ![](clinical-configuration-manager-ccm-user-guide/023.png)

<span id="_Ref185610670" class="anchor"></span>Figure 22: Grid Navigation

- Note: Arrows will be greyed out and un-selectable if the user cannot navigate in a certain direction.

### Filtering Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users can filter columns by selecting the three vertical bars pictured in [⁠Figure 23⁠](#_Ref185610721) titled “Show/Hide Columns.” This action will cause a dropdown (see [⁠Figure 24⁠](#_Ref185610739)) to appear.

> ![](clinical-configuration-manager-ccm-user-guide/024.png)

<span id="_Ref185610721" class="anchor"></span>Figure 23: Show/Hide Columns Button

2.  To hide a column, users will need to select the slider, shown below in [⁠Figure 24⁠](#_Ref185610739), next to an active column (indicated by slider’s blue appearance). The slider will become grey, and the column will be hidden from view within the grid.

> ![](clinical-configuration-manager-ccm-user-guide/025.png)

<span id="_Ref185610739" class="anchor"></span>Figure 24: Active Column Slider Example

3.  To show a column, users will need to select the slider, shown below in [⁠Figure 25⁠](#_Ref185610779), next to a hidden column (indicated by slider’s grey appearance). The slider will then become blue, and the column will be shown within the grid once more.

> ![](clinical-configuration-manager-ccm-user-guide/026.png)

<span id="_Ref185610779" class="anchor"></span>Figure 25: Hidden Column Slider Example

4.  Optionally, users can choose to hide all columns within the grid at once by selecting the “Hide All” button seen in [⁠Figure 26⁠](#_Ref185610802).

> ![](clinical-configuration-manager-ccm-user-guide/027.png)

<span id="_Ref185610802" class="anchor"></span>Figure 26: Hide All Button

5.  Users can also select the “Show All” button seen below in [⁠Figure 27⁠](#_Ref185610821) to show all hidden columns within the grid at one time.

> ![](clinical-configuration-manager-ccm-user-guide/028.png)

<span id="_Ref185610821" class="anchor"></span>Figure 27: Show All Button

- Note: The “Show All” button will not be selectable until at least one column has been hidden.

### Show, Hide, and Search Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When looking for availability within the grid, the option to show and hide filters is available. To begin the user will need to select the “Show/Hide Filters” button shown in [⁠Figure 28⁠](#_Ref165300734). Selecting either will cause the search functions to appear under each column name.

> ![](clinical-configuration-manager-ccm-user-guide/029.png)

> <span id="_Ref165300734" class="anchor"></span>Figure 28: Show/Hide Filter Options Buttons

2.  Once the search options appear as seen in [⁠Figure 29⁠](#_Ref165300749), the user can select the search bar or dropdown menu under the desired column to be filtered and enter or select the required information needed.

> ![](clinical-configuration-manager-ccm-user-guide/030.png)

> <span id="_Ref165300749" class="anchor"></span>Figure 29: Example of Filter Search Menu on Grid View

3.  Once the filter field has been populated, results will automatically refresh and show items based on the filtered criteria as seen below in [⁠Figure 30⁠](#_Ref165300767).

> ![](clinical-configuration-manager-ccm-user-guide/031.png)

> <span id="_Ref165300767" class="anchor"></span>Figure 30: Example of Filtered Results in Grid View

4.  To clear the search, the user will need to select the “X” next to the search bar seen in [⁠Figure 31⁠](#_Ref165300795). Selecting this will cause all results to appear within the table.

> ![](clinical-configuration-manager-ccm-user-guide/032.png)

> <span id="_Ref165300795" class="anchor"></span>Figure 31: Clearing Filter Button

5.  Once finished searching, the user can then select the “Show/Hide Search” button seen in [⁠Figure 32⁠](#_Ref165300814) to hide the search bar.

> ![](clinical-configuration-manager-ccm-user-guide/033.png)

> <span id="_Ref165300814" class="anchor"></span>Figure 32: Selecting Show/Hide Filters Button to Hide Filter Menu

### Search Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user can search through all items within the grid by selecting the “Show/Hide Search” button seen in [⁠Figure 33⁠](#_Ref185610845).

> ![](clinical-configuration-manager-ccm-user-guide/034.png)

<span id="_Ref185610845" class="anchor"></span>Figure 33: Show/Hide Search Button

2.  The user can then type the requested information into the search function. This will cause matching results to appear automatically highlighted within the grid as shown in [⁠Figure 34⁠](#_Ref185610862).

> ![](clinical-configuration-manager-ccm-user-guide/035.png)

<span id="_Ref185610862" class="anchor"></span>Figure 34: Highlighted Search Example

3.  To clear the search, the user will need to select the “X” next to the search bar seen in [⁠Figure 35⁠](#_Ref185610899). Selecting this will cause all results to appear within the grid.

> ![](clinical-configuration-manager-ccm-user-guide/036.png)

<span id="_Ref185610899" class="anchor"></span>Figure 35: Clear Button for Search Bar

4.  Once finished searching, the user can then select the “Show/Hide Search” button seen in [⁠Figure 33⁠](#_Ref185610845) above to hide the search bar from view.

# Search and View Clinic Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the Clinic Configuration page, users can search and view clinic configurations for a specific clinic.

- Note: Users with the correct user access will default to edit mode when entering Clinic Configurations.

## Search for a Clinic Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the “Clinic Configurations” tab shown in [⁠Figure 36⁠](#_Ref184907140).

> ![](clinical-configuration-manager-ccm-user-guide/037.png)

> <span id="_Ref184907140" class="anchor"></span>Figure 36: Clinic Configurations Tab

2.  To search for a desired clinic, select the search bar shown in [⁠Figure 37⁠](#_Ref184907162)*.*

> ![](clinical-configuration-manager-ccm-user-guide/038.png)

> <span id="_Ref184907162" class="anchor"></span>Figure 37: Search Bar for Clinic Configurations

3.  A user must enter the first 3+ characters of the clinic name to begin a search.
- Note: Search input must be at least three characters and can only include uppercase or lowercase letters, numbers, spaces, hyphens, and forward slashes. If the user does not adhere to the aforementioned rules, the error message shown in [⁠Figure 38⁠](#_Ref184907061) will appear.

> ![](clinical-configuration-manager-ccm-user-guide/039.png)

> <span id="_Ref184907061" class="anchor"></span>Figure 38: Error Message When Searching for a Clinic

4.  Once entering a valid search, the user must select enter or select “Search” shown in [⁠Figure 37⁠](#_Ref184907162).
5.  The user will then see the grid shown below in [⁠Figure 39⁠](#_Ref184907401) which displays the following: Clinic Name, Abbreviations, Provider(s), Patient Friendly Name, Stop Code, Credit Stop Code, and Status (Active or Inactive).

> ![](clinical-configuration-manager-ccm-user-guide/040.png)

> <span id="_Ref184907401" class="anchor"></span>Figure 39: Clinic Configurations Grid Table

## View Current Clinic Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  After searching and selecting the desired clinic outlined in [*⁠*3.1 Search for a Clinic Configuration⁠](#search-for-a-clinic-configuration) (see [⁠Figure 37⁠](#_Ref184907162) for guidance), [⁠Figure 40⁠](#_Ref184908374) will appear.

> ![](clinical-configuration-manager-ccm-user-guide/041.png)

> <span id="_Ref184908374" class="anchor"></span>Figure 40: Clinic Configurations Accordions

- Note: Users with Edit access will need to select the “View Clinic Data” button seen below in [⁠Figure 41⁠](#_Ref185878695) to only view clinic data.

> ![](clinical-configuration-manager-ccm-user-guide/042.png)

> <span id="_Ref185878695" class="anchor"></span>Figure 41: View Clinic Data Button

2.  The user will see the four clinic configuration settings: Clinic Settings, Preselected Settings, Optional Settings, and Clinic Availability, which can be viewed by selecting the “+” button highlighted in [⁠Figure 40⁠](#_Ref184908374). Optionally, the user can select the “Expand All” button to open all accordions at once.
- Note: This function is available to Read Only and Write Access users. <u>Only Write Access users will be able to edit</u>.
- Note: The first menu option labeled “Clinic Settings” is only available when attempting to view details. This accordion will change to “Mandatory Fields” when attempting to edit.

### Viewing Clinic Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In [⁠Figure 42⁠](#_Ref184908577) below, users can view the fields that appear within Clinic Settings.

![](clinical-configuration-manager-ccm-user-guide/043.png)

<span id="_Ref184908577" class="anchor"></span>Figure 42: Clinic Settings View

### Viewing Preselected Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In [⁠Figure 43⁠](#_Ref184909409) below, users can view the fields that appear within Preselected Settings.

![](clinical-configuration-manager-ccm-user-guide/044.png)

<span id="_Ref184909409" class="anchor"></span>Figure 43: Preselected Settings View

### Viewing Optional Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In [⁠Figure 44⁠](#_Ref184909570) below, users can view the fields that appear within Optional Settings.

![](clinical-configuration-manager-ccm-user-guide/045.png)

<span id="_Ref184909570" class="anchor"></span>Figure 44: Optional Settings View

### Viewing Clinic Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  View-only users can search for clinic availability by choosing a date (mm/dd/yyyy format) from the calendar shown below in [⁠Figure 45⁠](#_Ref184910917).

> ![](clinical-configuration-manager-ccm-user-guide/046.png)

> <span id="_Ref184910917" class="anchor"></span>Figure 45: Viewing Clinic Availability Calendar Button

- Note: The “Search” button will remain greyed out until a date is chosen; once chosen, the button will become available for selection as seen in [⁠Figure 46⁠](#_Ref184910951).

> ![](clinical-configuration-manager-ccm-user-guide/047.png)

> <span id="_Ref184910951" class="anchor"></span>Figure 46: Viewing Clinic Availability Search Button

2.  After selecting search, the user will see the “Clinic Timeslots” table as seen below in [⁠Figure 47⁠](#_Ref184910982) that will show the timeslots available for the most recent Sunday to the upcoming Saturday of that week.
- Note: Selecting the “Hide Table” button shown below in [⁠Figure 47⁠](#_Ref184910982) will reset the “Clinic Timeslots” table <u>completely</u>.

> ![](clinical-configuration-manager-ccm-user-guide/048.png)

> <span id="_Ref184910982" class="anchor"></span>Figure 47: Viewing Clinic Availability Timeslots Example

- Note: Users can edit the number of timeslots shown on the page by selecting the arrows shown in [⁠Figure 48⁠](#_Ref184911034).

> ![](clinical-configuration-manager-ccm-user-guide/049.png)

> <span id="_Ref184911034" class="anchor"></span>Figure 48: Viewing Clinic Availability Timeslot Page View Options

3.  The user can either look through the dates manually, or select the button shown below in [⁠Figure 49⁠](#_Ref184911079) to filter the search results to a specific date. Once selected, the window shown in [⁠Figure 50⁠](#_Ref184911099) will appear.

> ![](clinical-configuration-manager-ccm-user-guide/050.png)

> <span id="_Ref184911079" class="anchor"></span>Figure 49: Viewing Clinic Availability Filter Dates Button

4.  After entering the required dates, the user can then select the filter dates button. The user will be shown an updated “Clinic Timeslots” table with the requested results.

> ![](clinical-configuration-manager-ccm-user-guide/051.png)

> <span id="_Ref184911099" class="anchor"></span>Figure 50: Viewing Clinic Availability Filter Date Range Example

# Editing Clinic Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: This section of the guide is only applicable to users with the correct write access permissions. If the user does not have write access permissions set to the account, the user will receive the error message shown in [⁠Figure 51⁠](#_Ref185428463). If a user needs access to make changes on this application, please contact the local Clinical Applications Coordinator or Supervisor for assistance.*

![](clinical-configuration-manager-ccm-user-guide/052.png)

<span id="_Ref185428463" class="anchor"></span>Figure 51: Authorization Error Message for Clinic Configurations

1.  After searching and selecting the desired clinic outlined in [⁠3.1 Search for a Clinic Configuration⁠](#search-for-a-clinic-configuration), (see [⁠Figure 37⁠](#_Ref184907162) for guidance), [⁠Figure 52⁠](#_Ref184911577) will appear.

> ![](clinical-configuration-manager-ccm-user-guide/053.png)

> <span id="_Ref184911577" class="anchor"></span>Figure 52: Edit Clinic Page

2.  The user will see the four clinic configuration settings: Mandatory Fields, Preselected Default Fields, Optional Fields, and Clinic Availability, which can be expanded by selecting the “+” next to each in [⁠Figure 53⁠](#_Ref184911693). Optionally, the user can select the “Expand All” button to open all accordions at once.

> ![](clinical-configuration-manager-ccm-user-guide/054.png)

> <span id="_Ref184911693" class="anchor"></span>Figure 53: Editing Clinic Availability Accordions

- Note: Users will not be able to update certain fields. If these fields need editing, users must create a new clinic.
- Note: User are allowed to add additional time slots. Basic functions of adding days of the week, Start Times, End Times, and number of slots are available.

## Editing Mandatory Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users with Write Access can edit the fields that appear within Mandatory Fields as shown in [⁠Figure 54⁠](#_Ref184912518) below. The field(s) labeled “Required” must be edited before saving.

> ![](clinical-configuration-manager-ccm-user-guide/055.png)

> <span id="_Ref184912518" class="anchor"></span>Figure 54: Editing Mandatory Fields

- Note: Please go to Section [⁠9.2 Tool Tip Descriptions⁠](#tool-tip-descriptions) for more information on populating clinic settings.
2.  Once the desired edits have been made, the user must be sure to select the “Save Changes” button shown in [⁠Figure 55⁠](#_Ref184912546) in the lower right-hand corner of the page.

> ![](clinical-configuration-manager-ccm-user-guide/056.png)

> <span id="_Ref184912546" class="anchor"></span>Figure 55: Update Clinic Button for Mandatory Fields

- Note: The “Save Changes” button only becomes available when <u>a minimum of one</u> change has been made; if no change is made, the “Save Changes” button will remain greyed out.
- Note: The user must confirm their changes by selecting the “Save Changes” button, otherwise the user will receive the error message shown in [⁠Figure 56⁠](#_Ref184912585).

> ![](clinical-configuration-manager-ccm-user-guide/057.png)

> <span id="_Ref184912585" class="anchor"></span>Figure 56: Changes Unsaved Message for Mandatory Fields

## Editing Preselected Default Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users with Write Access can edit the fields that appear within Preselected Default Fields as shown in [⁠Figure 57⁠](#_Ref184912756) below.

> ![](clinical-configuration-manager-ccm-user-guide/058.png)

> <span id="_Ref184912756" class="anchor"></span>Figure 57: Editing Preselected Default Fields

- Note: Please go to Section [⁠9.2 Tool Tip Descriptions⁠](#tool-tip-descriptions) for more information on populating clinic settings.
2.  Once the desired edits have been made, the user must select the “Update Clinic” button shown in [⁠Figure 58⁠](#_Ref184912788) in the lower right-hand corner of the page.

> ![](clinical-configuration-manager-ccm-user-guide/059.png)

> <span id="_Ref184912788" class="anchor"></span>Figure 58: Update Clinic Button for Preselected Default Fields

- Note: The “Save Changes” button only becomes available when <u>a minimum of one</u> change has been made; if no change is made, the “Save Changes” button will remain greyed out.
- Note: The user must confirm their changes by selecting the “Save Changes” button, otherwise the user will receive the error message shown in [⁠Figure 59⁠](#_Ref184912826).

> ![](clinical-configuration-manager-ccm-user-guide/060.png)

> <span id="_Ref184912826" class="anchor"></span>Figure 59: Changes Unsaved Message for Preselected Default Fields

## Editing Optional Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users with Write Access can edit the fields that appear within Preselected Default Fields as shown in [⁠Figure 60⁠](#_Ref184913290) below.

> ![](clinical-configuration-manager-ccm-user-guide/061.png)

> <span id="_Ref184913290" class="anchor"></span>Figure 60: Editing Optional Fields

- Note: Please go to Section [⁠9.2 Tool Tip Descriptions⁠](#tool-tip-descriptions) for more information on populating clinic settings.
- Note: The “See Full Special Instructions” button only becomes available when <u>a minimum of one</u> special instructions change has been made; if no change is made, the “See Full Special Instructions” button will not appear.
- Note: The “Add/Remove Privileged User(s)” dropdown only becomes available when the “Prohibit Access to Clinic?” radio button is toggled to yes; if toggled to no, the ‘Add/Remove Privileged User(s)” dropdown will not appear.
2.  Once the desired edits have been made, the user must select the “Save Changes” button shown in [⁠Figure 61⁠](#_Ref184913320) in the lower right-hand corner of the page.

![](clinical-configuration-manager-ccm-user-guide/062.png)

<span id="_Ref184913320" class="anchor"></span>Figure 61: Update Clinic Button for Optional Fields

- Note: The “Save Changes” button only becomes available when <u>a minimum of one</u> change has been made; if no change is made, the “Save Changes” button will remain greyed out.
- Note: The user must confirm their changes by selecting the “Save Changes” button, otherwise the user will receive the error message shown in [⁠Figure 62⁠](#_Ref184913341).

> ![](clinical-configuration-manager-ccm-user-guide/063.png)

> <span id="_Ref184913341" class="anchor"></span>Figure 62: Changes Unsaved Message for Optional Fields

## Editing Clinic Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: The section below is a brief overview on searching timeslots. The user may select the “Timeslot Manager” button seen in [⁠Figure 63⁠](#_Ref184913704) and skip to section [⁠4.4.1 Add or Modify Timeslots for Single Day Modification⁠](#add-or-modify-timeslots-for-single-day-modification) if needed.*

![](clinical-configuration-manager-ccm-user-guide/064.png)

<span id="_Ref184913704" class="anchor"></span>Figure 63: Add/Modify Slot Button on Clinic Availability Drop Menu

1.  Users with correct Write Access will be asked to select a date (mm/dd/yyyy format) from the calendar seen in [⁠Figure 64⁠](#_Ref184913745).

> ![](clinical-configuration-manager-ccm-user-guide/065.png)

> <span id="_Ref184913745" class="anchor"></span>Figure 64: Calendar Button for Editing Clinic Availability

2.  After selecting the “Search” button, the Clinic Timeslots table (see [⁠Figure 65⁠](#_Ref184913858) for example) will appear that will show the timeslots available for the most recent Sunday to the upcoming Saturday of that week.
- Note: The “Search” button will remain greyed out until a date is chosen; once chosen, the button will become available for selection.
3.  The user can either look through the dates manually or filter the search results to a specific date (see [⁠2.4 Filters⁠](#filters) for more information on filtering within grids).
- Note: Selecting the “Clear Search” button shown below in [⁠Figure 65⁠](#_Ref184913858) will reset the “Clinic Timeslots” table completely.

> ![](clinical-configuration-manager-ccm-user-guide/066.png)

> <span id="_Ref184913858" class="anchor"></span>Figure 65: Available Timeslots Example for Editing Clinic Availability

### Add or Modify Timeslots for Single Day Modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the “Timeslot Manager” button shown in [⁠Figure 66⁠](#_Ref184993390) to add a timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/067.png)

> <span id="_Ref184993390" class="anchor"></span>Figure 66: Add Slot Button for Editing Clinic Availability for Single Modification

2.  After selecting the “Timeslot Manager” button, the user will be taken to the Timeslot Manager page shown in [⁠Figure 67⁠](#_Ref184993523). This will allow the user to add or remove timeslot(s) for a selected day.

> ![](clinical-configuration-manager-ccm-user-guide/068.png)

> <span id="_Ref184993523" class="anchor"></span>Figure 67: Timeslot Manager Page for Single Day

#### Adding Timeslots for Single Day Modification

1.  To add a timeslot, select the radio button next to “Edit Grid Availability” shown in [⁠Figure 68⁠](#_Ref184996810).

> ![](clinical-configuration-manager-ccm-user-guide/069.png)

> <span id="_Ref184996810" class="anchor"></span>Figure 68: Edit Grid Availability Radio Button for Single Day Modification

2.  The user will then need to select a date from the calendar shown below in [⁠Figure 69⁠](#_Ref184996845).

> ![](clinical-configuration-manager-ccm-user-guide/070.png)

> <span id="_Ref184996845" class="anchor"></span>Figure 69: Calendar for Editing Grid Availability in Single Day Modification

3.  After selecting a date, the user will be prompted to check for cancelled timeslots as seen in [⁠Figure 70⁠](#_Ref184996945).

> ![](clinical-configuration-manager-ccm-user-guide/071.png)

> <span id="_Ref184996945" class="anchor"></span>Figure 70: Check for Cancelled Timeslots Button for Single Day Modification

- Note: If a user attempts to add timeslots to a day with previous cancellations, the following information will display after selecting “Check for Cancelled Timeslots” (see [⁠Figure 71⁠](#_Ref185864826) for example).

> ![](clinical-configuration-manager-ccm-user-guide/072.png)

> <span id="_Ref185864826" class="anchor"></span>Figure 71: Cancelled Timeslot Information for Single Day

4.  The page will then expand to full view, and the user will be required to populate the fields shown below in [⁠Figure 72⁠](#_Ref184997008).

> ![](clinical-configuration-manager-ccm-user-guide/073.png)

> <span id="_Ref184997008" class="anchor"></span>Figure 72: Add Timeslot for Single Day Modification

- Note: The user is only allotted 1 to 26 slots. Going under the minimum or over the maximum amount will result in the error shown [⁠Figure 73⁠](#_Ref184997097).

> ![](clinical-configuration-manager-ccm-user-guide/074.png)

> <span id="_Ref184997097" class="anchor"></span>Figure 73: Number of Slots Error for Single Day Modification

- Note: If a timeslot has been previously cancelled for the chosen date, the user will receive a notification prompting them to either keep the previously cancelled timeslots or overwrite the cancellation, as seen in [⁠Figure 74⁠](#_Ref184997189). After selecting an action, the user will need to select “Continue” to move forward with the modification.

  ![](clinical-configuration-manager-ccm-user-guide/075.png)

> <span id="_Ref184997189" class="anchor"></span>Figure 74: Cancelled Timeslots Information for Single Day Modification

5.  The user can also add multiple timeslots for the chosen day by selecting the “+” button seen in [⁠Figure 75⁠](#_Ref184997287) and populating the same required fields.

> ![](clinical-configuration-manager-ccm-user-guide/076.png)

> <span id="_Ref184997287" class="anchor"></span>Figure 75: Adding Multiple Timeslots in Single Day Modification

- Note: The user is only allowed to create multiple timeslots for different times. If duplicate or overlapping times are attempted, the user will receive the error seen below in [⁠Figure 76⁠](#_Ref184998277).

> ![](clinical-configuration-manager-ccm-user-guide/077.png)

> <span id="_Ref184998277" class="anchor"></span>Figure 76: Duplicate Timeslot Error for Single Day Modification

- Note: To remove additional timeslots, select the “x” button seen in [⁠Figure 77⁠](#_Ref184998365).

> ![](clinical-configuration-manager-ccm-user-guide/078.png)

> <span id="_Ref184998365" class="anchor"></span>Figure 77: Removing Timeslots for Single Day Modification

6.  When all required information has been entered, the user can select the “Add Timeslot(s)” button seen in [⁠Figure 78⁠](#_Ref184998461) and save the intended changes.

> ![](clinical-configuration-manager-ccm-user-guide/079.png)

> <span id="_Ref184998461" class="anchor"></span>Figure 78: Adding Timeslots Button for Single Day Modification

- Note: The user is required to select options from the hour <u>and</u> minutes field in “Start Hour” for the “Add Timeslot(s)” button to become highlighted.
7.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 79⁠](#_Ref184998492) appears.

> ![](clinical-configuration-manager-ccm-user-guide/080.png)

> <span id="_Ref184998492" class="anchor"></span>Figure 79: Save Successful Message for Single Day Modification

8.  After successfully saving the edit, the user can select the “Continue” button shown in [⁠Figure 79⁠](#_Ref184998492) to be returned to the clinic configurations page for the specified clinic.

#### Removing Timeslots for Single Day Modification

1.  Select the radio button next to “Remove Grid Availability” as seen in [⁠Figure 80⁠](#_Ref184998809) to remove a timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/081.png)

> <span id="_Ref184998809" class="anchor"></span>Figure 80: Remove Grid Availability Radio Button for Single Day Modification

2.  The user will then need to select a date from the calendar shown below in [⁠Figure 81⁠](#_Ref184998848).

> ![](clinical-configuration-manager-ccm-user-guide/082.png)

> <span id="_Ref184998848" class="anchor"></span>Figure 81: Calendar for Removing Grid Availability in Single Day Modification

3.  After choosing the specific date, the user will need to select the “Remove Timeslot(s)” button shown in [⁠Figure 82⁠](#_Ref184998883) to save the intended change.

> ![](clinical-configuration-manager-ccm-user-guide/083.png)

> <span id="_Ref184998883" class="anchor"></span>Figure 82: Remove Timeslot(s) Button for Single Day Modification

4.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 83⁠](#_Ref184998924) appears.

> ![](clinical-configuration-manager-ccm-user-guide/084.png)

> <span id="_Ref184998924" class="anchor"></span>Figure 83: Save Successful for Remove Timeslot(s) in Single Day Modification

### Add or Modify Timeslots for Indefinite Modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the “Timeslot Manager” button shown in [⁠Figure 84⁠](#_Ref185000107) to add a timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/085.png)

<span id="_Ref185000107" class="anchor"></span>Figure 84: Timeslot Manager Button for Editing Clinic Availability for Indefinite Modification

2.  After selecting the “Timeslot Manager” button, the user will be taken to the Timeslot Manager page shown in [⁠Figure 85⁠](#_Ref185000137).
- Note: This will allow the user to edit or remove grid availability for an indefinite period on any consecutive day of the week. For example, if the user chooses to change timeslots on a Wednesday, indefinite modification will allocate the changes to every Wednesday thereafter.

> ![](clinical-configuration-manager-ccm-user-guide/086.png)

<span id="_Ref185000137" class="anchor"></span>Figure 85: Timeslot Manager Page for Indefinite Modification

#### Adding Timeslots for Indefinite Modification

1.  To add a timeslot, select the radio button next to “Edit Grid Availability” shown in [⁠Figure 86⁠](#_Ref185003022).

> ![](clinical-configuration-manager-ccm-user-guide/087.png)

> <span id="_Ref185003022" class="anchor"></span>Figure 86: Edit Grid Availability Radio Button for Indefinite Modification

2.  The user will then need to select a date from the calendar shown below in [⁠Figure 87⁠](#_Ref185003089).

> ![](clinical-configuration-manager-ccm-user-guide/088.png)

> <span id="_Ref185003089" class="anchor"></span>Figure 87: Calendar for Edit Grid Availability in Indefinite Modification

3.  After selecting a date, the user will be prompted to check for cancelled timeslots as seen in [⁠Figure 88⁠](#_Ref185003121).

> ![](clinical-configuration-manager-ccm-user-guide/089.png)

> <span id="_Ref185003121" class="anchor"></span>Figure 88: Check for Cancelled Timeslots for Indefinite Modification

- Note: If a user attempts to add timeslots to a day with previous cancellations, the following information will display after selecting “Check for Cancelled Timeslots” (see [⁠Figure 89⁠](#_Ref185864849) for example).

> ![](clinical-configuration-manager-ccm-user-guide/090.png)

> <span id="_Ref185864849" class="anchor"></span>Figure 89: Cancelled Timeslot Information for Indefinite

4.  The page will then expand to full view, and the user will be required to populate the fields shown below in [⁠Figure 90⁠](#_Ref185003153).

> ![](clinical-configuration-manager-ccm-user-guide/091.png)

> <span id="_Ref185003153" class="anchor"></span>Figure 90: Add/Modify Timeslot Window Expansion for Indefinite Modification

- Note: The user is only allotted 1 to 26 slots. Going under the minimum or over the maximum amount will result in the error shown in [⁠Figure 91⁠](#_Ref185003179).

> ![](clinical-configuration-manager-ccm-user-guide/092.png)

> <span id="_Ref185003179" class="anchor"></span>Figure 91: Number of Slots Error for Indefinite Modification

- Note: If a timeslot has been previously cancelled for the chosen date, the user will receive a notification prompting them to either keep the previously cancelled timeslots or overwrite the cancellation, as seen in [⁠Figure 92⁠](#_Ref185003206). After selecting an action, the user will need to select “Continue” to move forward with the modification.

> ![](clinical-configuration-manager-ccm-user-guide/093.png)

> <span id="_Ref185003206" class="anchor"></span>Figure 92: Cancelled Timeslots Information for Indefinite Modification

5.  The user can also add multiple timeslots for the chosen day by selecting the “+” button seen in [⁠Figure 93⁠](#_Ref185003234) and populating the same required fields.

> ![](clinical-configuration-manager-ccm-user-guide/094.png)

> <span id="_Ref185003234" class="anchor"></span>Figure 93: Adding Multiple Timeslots for Indefinite Modification

- Note: The user is only allowed to create multiple timeslots for different times. If duplicate or overlapping times are attempted, the user will receive the error seen below in [⁠Figure 94⁠](#_Ref185003268).

> ![](clinical-configuration-manager-ccm-user-guide/095.png)

> <span id="_Ref185003268" class="anchor"></span>Figure 94: Duplicate Timeslot Error for Indefinite Modification

- Note: To remove additional timeslots, select the “x” button seen in [⁠Figure 95⁠](#_Ref185003292).

> ![](clinical-configuration-manager-ccm-user-guide/096.png)

> <span id="_Ref185003292" class="anchor"></span>Figure 95: Removing Timeslots for Indefinite Modification

6.  When all required information has been entered, the user can select the “Add Timeslot(s)” button seen in [⁠Figure 96⁠](#_Ref185003334) and save the intended changes.

> ![](clinical-configuration-manager-ccm-user-guide/097.png)

> <span id="_Ref185003334" class="anchor"></span>Figure 96: Adding Timeslots Button for Indefinite Modification

- Note: The user is required to select options from the hour <u>and</u> minutes field in “Start Hour” for the “Add Timeslot(s)” button to become highlighted.
7.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 97⁠](#_Ref185003356) appears.

> ![](clinical-configuration-manager-ccm-user-guide/098.png)

> <span id="_Ref185003356" class="anchor"></span>Figure 97: Save Successful Message for Indefinite Modification

- Note: When using the indefinite option, the indefinite pattern set for the timeslot will go as far as it can until it meets a pre-existing known pattern that has already been established.
8.  After successfully saving the edit, the user can select the “Continue” button shown in [⁠Figure 97⁠](#_Ref185003356) to be returned to the clinic configurations page of the specified clinic.

#### Removing Timeslots for Indefinite Modification

1.  Select the radio button next to “Remove Grid Availability” as seen in [⁠Figure 98⁠](#_Ref185003893) to remove a timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/099.png)

> <span id="_Ref185003893" class="anchor"></span>Figure 98: Remove Grid Availability Radio Button for Indefinite Modification

2.  The user will then need to select a date from the calendar shown below in [⁠Figure 99⁠](#_Ref185003953).

> ![](clinical-configuration-manager-ccm-user-guide/100.png)

> <span id="_Ref185003953" class="anchor"></span>Figure 99: Calendar for Removing Grid Availability in Indefinite Modification

3.  After selecting a date, the page will expand, and the user will be prompted to choose “Yes” or “No” as shown in [⁠Figure 100⁠](#_Ref185003995). Select “Yes” to remove timeslots indefinitely from the chosen day of the week.

> ![](clinical-configuration-manager-ccm-user-guide/101.png)

> <span id="_Ref185003995" class="anchor"></span>Figure 100: Removing Timeslot(s) Options for Indefinite Modification

> If selecting “No”, the user will be prompted to specify the days to be removed from the calendar as seen in [⁠Figure 101⁠](#_Ref185004047).

> ![](clinical-configuration-manager-ccm-user-guide/102.png)

> <span id="_Ref185004047" class="anchor"></span>Figure 101: Choosing Multiple Days to Remove in Indefinite Modification

4.  To save intended changes, the user will need to select the “Remove Timeslot(s)” button shown in [⁠Figure 102⁠](#_Ref185004087).

> ![](clinical-configuration-manager-ccm-user-guide/103.png)

> <span id="_Ref185004087" class="anchor"></span>Figure 102: Remove Timeslot(s) Button for Indefinite Modification

5.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 103⁠](#_Ref185004167) appears.

> ![](clinical-configuration-manager-ccm-user-guide/104.png)

> <span id="_Ref185004167" class="anchor"></span>Figure 103: Save Successful for Remove Timeslot(s) in Indefinite Modification

6.  After successfully saving the edit, the user can select the “Continue” button shown in [⁠Figure 103⁠](#_Ref185004167) to be returned to the clinic configurations page for the specified clinic.

### Add or Modify Timeslots for Multi-select Modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the “Timeslot Manager” button shown in [⁠Figure 104⁠](#_Ref185428565) to add a timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/105.png)

<span id="_Ref185428565" class="anchor"></span>Figure 104: Timeslot Manager Button for Editing Clinic Availability for Multi-select

2.  After selecting the “Timeslot Manager” button, the user will be taken to the Timeslot Manager page shown in [⁠Figure 105⁠](#_Ref185428739).
- Note: This will allow the user to add or remove timeslots for multiple dates on the same consecutive day of the week. For example, if the first date chosen is a Tuesday, only dates from subsequent Tuesdays will be available.

> ![](clinical-configuration-manager-ccm-user-guide/106.png)

<span id="_Ref185428739" class="anchor"></span>Figure 105: Timeslot Manager Page for Multi-select Modification

#### Adding Timeslots for Multi-select Modification

1.  To add a timeslot, select the radio button next to “Edit Grid Availability” shown in [⁠Figure 106⁠](#_Ref185428774).

> ![](clinical-configuration-manager-ccm-user-guide/107.png)

<span id="_Ref185428774" class="anchor"></span>Figure 106: Edit Grid Availability Radio Button for Multi-select Modification

2.  The user will then need to either select the dates using the calendar shown below in [⁠Figure 107⁠](#_Ref185429945), or by manually entering the dates via the “Date Input” field located to the right of the calendar.

> ![](clinical-configuration-manager-ccm-user-guide/108.png)

<span id="_Ref185429945" class="anchor"></span>Figure 107: Calendar for Multi-select Modification

- Note: The formats MM-DD-YYYY or MM/DD/YYYY need to be used when manually entering dates into the “Date Input” field. Any other format will result in the error seen below in [⁠Figure 108⁠](#_Ref223524688).

  ![](clinical-configuration-manager-ccm-user-guide/109.png)

> <span id="_Ref223524688" class="anchor"></span>Figure 108: Invalid Date Format Error

3.  After selecting a date(s), the user will be prompted to check for cancelled timeslots as seen in [⁠Figure 109⁠](#_Ref185430002).

> ![](clinical-configuration-manager-ccm-user-guide/110.png)

<span id="_Ref185430002" class="anchor"></span>Figure 109: Check for Cancelled Timeslots Button for Multi-select Modification

- Note: When using the Multi-select timeslot type, users can choose to bulk paste dates from another source. If the user enters a date that falls on a federal holiday, in the past, or on a date more than 2 years in the future, an error message will appear (seen in [⁠Figure 110⁠](#_Ref212814213) for example).

  ![](clinical-configuration-manager-ccm-user-guide/111.png)

> <span id="_Ref212814213" class="anchor"></span>Figure 110: Bulk Paste Example for Multi-select Timeslots

- Note: If a user attempts to add timeslots to a day with previous cancellations, the following information will display after selecting “Check for Cancelled Timeslots” (see [⁠Figure 111⁠](#_Ref185864876) for example).

> ![](clinical-configuration-manager-ccm-user-guide/112.png)

> <span id="_Ref185864876" class="anchor"></span>Figure 111: Cancelled Timeslot Information for Multi-select

4.  The page will expand to full view, and the user will be required to populate the fields shown below in [⁠Figure 112⁠](#_Ref185430193).

> ![](clinical-configuration-manager-ccm-user-guide/113.png)

<span id="_Ref185430193" class="anchor"></span>Figure 112: Add/Modifying Expanded Page for Multi-select Modification

- Note: The user is only allotted 1 to 26 slots. Going under the minimum or over the maximum amount will result in the error shown in [⁠Figure 113⁠](#_Ref185430300).

> ![](clinical-configuration-manager-ccm-user-guide/114.png)

> <span id="_Ref185430300" class="anchor"></span>Figure 113: Number of Slots Error for Multi-select Modification

- Note: If a timeslot has been previously cancelled for the chosen date, the user will receive a notification prompting them to either keep the previously cancelled timeslots or overwrite the cancellation, as seen in [⁠Figure 114⁠](#_Ref185430332). After selecting an action, the user will need to select “Continue” to move forward with the modification.

> ![](clinical-configuration-manager-ccm-user-guide/115.png)

> <span id="_Ref185430332" class="anchor"></span>Figure 114: Cancelled Timeslots Information for Multi-select Modification

9.  The user can also add multiple timeslots for the chosen days by selecting the “+” button seen in [⁠Figure 115⁠](#_Ref185430368) and populating the same required fields.

> ![](clinical-configuration-manager-ccm-user-guide/116.png)

<span id="_Ref185430368" class="anchor"></span>Figure 115: Adding Multiple Timeslots in Multi-select Modification

- Note: The user is only allowed to create multiple timeslots for different times. If duplicate or overlapping times are attempted, the user will receive the errors seen below in [⁠Figure 116⁠](#_Ref185430392).

> ![](clinical-configuration-manager-ccm-user-guide/117.png)

> <span id="_Ref185430392" class="anchor"></span>Figure 116: Duplicate Timeslot Error for Multi-select Modification

- Note: To remove additional timeslots, select the “x” button seen in [⁠Figure 117⁠](#_Ref185430426).

> ![](clinical-configuration-manager-ccm-user-guide/118.png)

> <span id="_Ref185430426" class="anchor"></span>Figure 117: Removing Timeslots for Multi-select Modification

10. When all required information has been entered, the user can select the “Add Timeslot(s)” button seen in [⁠Figure 118⁠](#_Ref185430574) and save the intended changes.

> ![](clinical-configuration-manager-ccm-user-guide/119.png)

<span id="_Ref185430574" class="anchor"></span>Figure 118: Adding Timeslots Button for Multi-select Modification

- Note: The user is required to select options from the hour <u>and</u> minutes field in “Start Hour” for the “Add Timeslot(s)” button to become highlighted.
11. The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 119⁠](#_Ref185430621) appears.

> ![](clinical-configuration-manager-ccm-user-guide/120.png)

<span id="_Ref185430621" class="anchor"></span>Figure 119: Save Successful Message for Multi-select Modification

12. After successfully saving the edit, the user can select the “Continue” button shown in [⁠Figure 119⁠](#_Ref185430621) to be returned to the clinic configurations page of the specified clinic

#### Removing Timeslots for Multi-select Modification

1.  Select the radio button next to “Remove Grid Availability” as seen in [⁠Figure 120⁠](#_Ref185430668) to remove a timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/121.png)

<span id="_Ref185430668" class="anchor"></span>Figure 120: Remove Grid Availability Radio Button for Multi-select Modification

2.  The user will then need to either select the specified dates from the calendar shown below in [⁠Figure 121⁠](#_Ref185430696), or by manually entering the dates via the “Date Input” field located to the right of the calendar.

> ![](clinical-configuration-manager-ccm-user-guide/122.png)

<span id="_Ref185430696" class="anchor"></span>Figure 121: Calendar for Removing Grid Availability in Multi-select Modification

3.  After choosing the dates, the user will need to select the “Remove Timeslot(s)” button shown in [⁠Figure 122⁠](#_Ref185430737) save the intended changes.

> ![](clinical-configuration-manager-ccm-user-guide/123.png)

<span id="_Ref185430737" class="anchor"></span>Figure 122: Remove Timeslot(s) Button for Multi-select Modification

- Note: When using the Multi-select timeslot type, users can choose to bulk paste dates from another source. If the user enters a date that falls on a federal holiday, in the past, or on a date more than 2 years in the future, an error message will appear (seen in [⁠Figure 123⁠](#_Ref212820098) for example).

  ![](clinical-configuration-manager-ccm-user-guide/124.png)

> <span id="_Ref212820098" class="anchor"></span>Figure 123: Bulk Paste Example for Removing Multi-select Timeslots

4.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 124⁠](#_Ref185430775) appears.

> ![](clinical-configuration-manager-ccm-user-guide/125.png)

<span id="_Ref185430775" class="anchor"></span>Figure 124: Save Successful for Remove Timeslot(s) in Multi-select Modification

5.  After successfully saving the edit, the user can select the “Continue” button shown in [⁠Figure 124⁠](#_Ref185430775) to be returned to the clinic configurations page for the specified clinic.

### Add or Modify Timeslots for Recurring Modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the “Timeslot Manager” button shown in [⁠Figure 125⁠](#_Ref212822430) to add a timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/126.png)

<span id="_Ref212822430" class="anchor"></span>Figure 125: Timeslot Manager Button for Editing Clinic Availability for Recurring

2.  After selecting the “Timeslot Manager” button, the user will be taken to the Timeslot Manager page shown in [⁠Figure 126⁠](#_Ref213064554).
- Note: This will allow the user to add or remove timeslots on repeat for a specified pattern. For example, if the user chooses to create timeslots for the second Sunday of every month, then that pattern will recur every month until the specified end date.

> ![](clinical-configuration-manager-ccm-user-guide/127.png)

<span id="_Ref213064554" class="anchor"></span>Figure 126: Timeslot Manager Page for Recurring Modification

#### Adding Timeslots for Recurring Modification

1.  To add a timeslot, select the radio button next to “Edit Grid Availability” shown in [⁠Figure 127⁠](#_Ref213065294).

> ![](clinical-configuration-manager-ccm-user-guide/128.png)

<span id="_Ref213065294" class="anchor"></span>Figure 127: Edit Grid Availability Radio Button for Recurring Modification

2.  The user will then need to select a Start and End date from the dropdowns shown below in [⁠Figure 128⁠](#_Ref213065258).

> ![](clinical-configuration-manager-ccm-user-guide/129.png)

<span id="_Ref213065258" class="anchor"></span>Figure 128: Calendar Dropdown for Recurring Modification

- Note: The user can select the “Maximum End Date” checkbox seen in [⁠Figure 128⁠](#_Ref213065258) above to auto-populate the field with the latest possible end date.
3.  After selecting a date(s), the user will be prompted to check for cancelled timeslots as seen in [⁠Figure 109⁠](#_Ref185430002).

> ![](clinical-configuration-manager-ccm-user-guide/130.png)

<span id="_Toc223532465" class="anchor"></span>Figure 129: Check for Cancelled Timeslots Button for Recurring Modification

- Note: If a user attempts to add timeslots to a day with previous cancellations, the following information will display after selecting “Check for Cancelled Timeslots” (see [⁠Figure 130⁠](#_Ref213066273) for example).

> ![](clinical-configuration-manager-ccm-user-guide/131.png)

> <span id="_Ref213066273" class="anchor"></span>Figure 130: Cancelled Timeslot Information for Recurring

4.  The user will then need to select from the “Recurrence Pattern” dropdown menu seen in [⁠Figure 131⁠](#_Ref213067835).

> ![](clinical-configuration-manager-ccm-user-guide/132.png)

> <span id="_Ref213067835" class="anchor"></span>Figure 131: Recurrence Pattern Dropdown

5.  After selecting a recurrence pattern, the user will be required to specify the information and populate the fields for either a Monthly (see [⁠Figure 132⁠](#_Ref213068515) for example) or Weekly pattern (see [⁠Figure 133⁠](#_Ref213066293) for example).

> ![](clinical-configuration-manager-ccm-user-guide/133.png)

<span id="_Ref213068515" class="anchor"></span>Figure 132: Example of Monthly Recurrence Pattern

> ![](clinical-configuration-manager-ccm-user-guide/134.png)

<span id="_Ref213066293" class="anchor"></span>Figure 133: Example of Weekly Recurrence Pattern

6.  Once all recurrence pattern information has been entered, the user will need to populate the timeslot information seen below in [⁠Figure 134⁠](#_Ref213068852).

> ![](clinical-configuration-manager-ccm-user-guide/135.png)

<span id="_Ref213068852" class="anchor"></span>Figure 134: Add/Modify Timeslot for Recurring

- Note: The user is only allotted 1 to 26 slots. Going under the minimum or over the maximum amount will result in the error shown in [⁠Figure 135⁠](#_Ref213157171).

> ![](clinical-configuration-manager-ccm-user-guide/136.png)

> <span id="_Ref213157171" class="anchor"></span>Figure 135: Number of Slots Error for Recurring Modification

- Note: If a timeslot has been previously cancelled for the chosen date, the user will receive a notification prompting them to either keep the previously cancelled timeslots or overwrite the cancellation, as seen in [⁠Figure 136⁠](#_Ref213157200). After selecting an action, the user will need to select “Continue” to move forward with the modification.

> ![](clinical-configuration-manager-ccm-user-guide/137.png)

> <span id="_Ref213157200" class="anchor"></span>Figure 136: Cancelled Timeslots Information for Recurring Modification

7.  When all required information has been entered, the user can select the “Add Recurring Timeslot(s)” button seen in [⁠Figure 137⁠](#_Ref213157584) and save the intended changes.

> ![](clinical-configuration-manager-ccm-user-guide/138.png)

<span id="_Ref213157584" class="anchor"></span>Figure 137: Adding Timeslots Button for Recurring Modification

- Note: The user is required to select options from the hour <u>and</u> minutes field in “Start Hour” for the “Add Recurring Timeslot(s)” button to become highlighted.
8.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 138⁠](#_Ref213157908) appears.

> ![](clinical-configuration-manager-ccm-user-guide/139.png)

<span id="_Ref213157908" class="anchor"></span>Figure 138: Save Successful Message for Recurring Modification

9.  After successfully saving the edit, the user can select the “Continue” button shown in [⁠Figure 138⁠](#_Ref213157908) to be returned to the clinic configurations page of the specified clinic

#### Removing Timeslots for Recurring Modification

1.  Select the radio button next to “Remove Grid Availability” as seen in [⁠Figure 139⁠](#_Ref213157909) to remove a timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/140.png)

<span id="_Ref213157909" class="anchor"></span>Figure 139: Remove Grid Availability Radio Button for Recurring Modification

2.  The user will then need to select a Start and End date from the dropdowns shown below in [⁠Figure 140⁠](#_Ref213158043).

> ![](clinical-configuration-manager-ccm-user-guide/141.png)

<span id="_Ref213158043" class="anchor"></span>Figure 140: Calendar Dropdown for Removing Grid Availability in Recurring Modification

3.  The user will also need to select from the “Recurrence Pattern” dropdown menu seen in [⁠Figure 141⁠](#_Ref213158929).

> ![](clinical-configuration-manager-ccm-user-guide/142.png)

> <span id="_Ref213158929" class="anchor"></span>Figure 141: Recurrence Pattern Dropdown for Removing Grid Availability

4.  After selecting a recurrence pattern, the user will be required to specify the information and populate the fields for either a Monthly (see [⁠Figure 142⁠](#_Ref213159256) for example) or Weekly pattern (see [⁠Figure 143⁠](#_Ref213159257) for example).

> ![](clinical-configuration-manager-ccm-user-guide/143.png)

<span id="_Ref213159256" class="anchor"></span>Figure 142: Example of Monthly Recurrence Pattern for Removing Grid Availability

> ![](clinical-configuration-manager-ccm-user-guide/144.png)

<span id="_Ref213159257" class="anchor"></span>Figure 143: Example of Weekly Recurrence Pattern for Removing Grid Availability

5.  Once all recurrence pattern information has been entered, the user will need to select the “Remove Recurring Timeslot(s)” button shown in [⁠Figure 144⁠](#_Ref213159583) save the intended changes.

> ![](clinical-configuration-manager-ccm-user-guide/145.png)

<span id="_Ref213159583" class="anchor"></span>Figure 144: Remove Recurring Timeslot(s) Button

6.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 145⁠](#_Ref213159584) appears.

> ![](clinical-configuration-manager-ccm-user-guide/146.png)

<span id="_Ref213159584" class="anchor"></span>Figure 145: Save Successful for Remove Timeslot(s) in Recurring Modification

7.  After successfully saving the edit, the user can select the “Continue” button shown in [⁠Figure 145⁠](#_Ref213159584) to be returned to the clinic configurations page for the specified clinic.

## Cancelling and Restoring Timeslots

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: This section of the guide is only applicable to users with access permissions SDCANCEL for timeslot cancellations and SDRESTORE for timeslot restorations. If the user does not have elevated access permissions set to their VistA account, the user will not see the “Cancel Timeslot(s)” or “Restore” buttons seen in [⁠Figure 146⁠](#_Ref185430989). If a user needs access to make changes on this application, please contact the local Clinical Applications Coordinator or Supervisor for assistance.*

![](clinical-configuration-manager-ccm-user-guide/147.png)

<span id="_Ref185430989" class="anchor"></span>Figure 146: Cancel and Restore Buttons for Timeslots

To cancel and restore clinic timeslots, the user will first need to search and select a clinic within the Clinic Configurations tab. Once a clinic is selected, the user will need to search for a date and then select it within the Clinic Availability accordion (see [⁠Figure 147⁠](#_Ref185431041)).

![](clinical-configuration-manager-ccm-user-guide/148.png)

<span id="_Ref185431041" class="anchor"></span>Figure 147: Date Search for Cancel and Restore

### Cancelling a Timeslot

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  After searching for a specific date, the user will be shown a full week of scheduling clinic availability. The user will then click the ellipsis next to the necessary timeslot and select the “Cancel Timeslot(s)” button seen in [⁠Figure 148⁠](#_Ref185431066).

> ![](clinical-configuration-manager-ccm-user-guide/149.png)

<span id="_Ref185431066" class="anchor"></span>Figure 148: Cancel Timeslot Button

2.  After selecting the “Cancel Timeslot(s)” button, the pop-up window shown in [⁠Figure 149⁠](#_Ref185431093) will appear.

> ![](clinical-configuration-manager-ccm-user-guide/150.png)

<span id="_Ref185431093" class="anchor"></span>Figure 149: Cancel Timeslot Window

#### Cancelling for a Single Timeslot

1.  To cancel for a single timeslot, the user will need to select “No” on the Cancel Timeslot window seen in [⁠Figure 150⁠](#_Ref185431118).

> ![](clinical-configuration-manager-ccm-user-guide/151.png)

<span id="_Ref185431118" class="anchor"></span>Figure 150: Single Timeslot Cancellation Option

2.  Next, the user can choose to cancel the single timeslot seen at the top of the window. Optionally, the user may also enter a start and end time or cancel multiple consecutive timeslots, as seen below in [⁠Figure 151⁠](#_Ref216266190).

> ![](clinical-configuration-manager-ccm-user-guide/152.png)

<span id="_Ref216266190" class="anchor"></span>Figure 151: Manual Time Entered for Timeslot Cancellation Example

3.  The user will then need to enter a reason for cancellation into the box seen in [⁠Figure 152⁠](#_Ref185431148) and select the “Continue” button to proceed with cancelling the timeslot.

> ![](clinical-configuration-manager-ccm-user-guide/153.png)

<span id="_Ref185431148" class="anchor"></span>Figure 152: Reason for Cancellation Example for Single Timeslot Cancellation

- Note: The user is only allotted 3 to 30 characters. Going under the minimum or over the maximum amount will result in the error shown in [⁠Figure 153⁠](#_Ref185431176).

> ![](clinical-configuration-manager-ccm-user-guide/154.png)

> <span id="_Ref185431176" class="anchor"></span>Figure 153: Reason for Cancellation Error for Single Timeslot Cancellation

- Note: If the user attempts to cancel a timeslot with patient association, the user will receive the window shown below in [⁠Figure 154⁠](#_Ref185431200). The user can then choose to either continue with cancellation or return to the grid.

> ![](clinical-configuration-manager-ccm-user-guide/155.png)

> <span id="_Ref185431200" class="anchor"></span>Figure 154: Patient Association Window for Single Timeslot Cancellation

4.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 155⁠](#_Ref185431230) appears. The user can select “Continue” to return to the grid.

> ![](clinical-configuration-manager-ccm-user-guide/156.png)

<span id="_Ref185431230" class="anchor"></span>Figure 155: Save Successful for Cancelling Single Timeslot

- Note: The grid will say “Yes/Blocked” within the Cancelled column for single timeslot cancellations (see [⁠Figure 156⁠](#_Ref185431253)).

> ![](clinical-configuration-manager-ccm-user-guide/157.png)

> <span id="_Ref185431253" class="anchor"></span>Figure 156: Single Timeslot Cancellation Example in Grid

#### Entire Day Cancellation

1.  To cancel timeslots for the entire day, the user will need to select “Yes” on the Cancel Timeslot window seen in [⁠Figure 157⁠](#_Ref185431277).

> ![](clinical-configuration-manager-ccm-user-guide/158.png)

<span id="_Ref185431277" class="anchor"></span>Figure 157: Entire Day Timeslot Cancellation Option

- Note: The user will not be able to cancel timeslots for the entire day if there is already an existing timeslot block for the same day. To cancel the entire day, the user will either need to cancel timeslots one at a time or restore the timeslot block so that the option becomes available (See section [⁠4.5.2 Restoring a Timeslot⁠](#restoring-a-timeslot) for information on restoring timeslots).
2.  The user will then need to enter a reason for cancellation into the box seen in [⁠Figure 158⁠](#_Ref185431305) and select the “Continue” button to proceed with cancelling all timeslots.

> ![](clinical-configuration-manager-ccm-user-guide/159.png)

<span id="_Ref185431305" class="anchor"></span>Figure 158: Reason for Cancellation Example for Entire Day Cancellation

- Note: The user is only allotted 3 to 30 characters. Going under the minimum or over the maximum amount will result in the error shown in [⁠Figure 159⁠](#_Ref185431344).

> ![](clinical-configuration-manager-ccm-user-guide/160.png)

> <span id="_Ref185431344" class="anchor"></span>Figure 159: Reason for Cancellation Error for Entire Day Cancellation

- Note: If the user attempts to cancel timeslots with patient association, the user will receive the window seen below in [⁠Figure 160⁠](#_Ref185431369). The user can then choose to either continue with cancellation of the entire day or return to the grid.

> ![](clinical-configuration-manager-ccm-user-guide/161.png)

> <span id="_Ref185431369" class="anchor"></span>Figure 160: Patient Association Window for Entire Day Timeslots Cancellation

3.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 161⁠](#_Ref185431395) appears. The user can select “Continue” to return to the grid.

> ![](clinical-configuration-manager-ccm-user-guide/162.png)

<span id="_Ref185431395" class="anchor"></span>Figure 161: Save Successful for Cancelling All Timeslots

- Note: The grid will say “Yes/Cancelled” within the Cancelled column for entire day timeslot cancellations (see [⁠Figure 162⁠](#_Ref185431416)).

> ![](clinical-configuration-manager-ccm-user-guide/163.png)

> <span id="_Ref185431416" class="anchor"></span>Figure 162: Entire Day Timeslot Cancellation Example in Grid

### Restoring a Timeslot

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Restoring for a Single Day Timeslot

1.  After searching for a specific date, the user will be shown a full week of scheduling clinic availability. The user will then click the ellipsis next to the necessary timeslot, or grouping of multiple consecutive timeslots, and select the “Restore” button seen in [⁠Figure 163⁠](#_Ref185431483).

> ![](clinical-configuration-manager-ccm-user-guide/164.png)

<span id="_Ref185431483" class="anchor"></span>Figure 163: Restore Timeslot Button for Single Timeslot Restoration

2.  The Restore Timeslot window will appear. From here, the user can then choose to restore the entire blocked timeslot or select a start and end time to restore from the blocked period via the dropdown seen below in [⁠Figure 164⁠](#_Ref185431508).

> ![](clinical-configuration-manager-ccm-user-guide/165.png)

<span id="_Ref185431508" class="anchor"></span>Figure 164: Restore Timeslot Window for Single Timeslot

3.  After choosing the required times, the user will need to select the “Restore Timeslot(s)” button shown in [⁠Figure 165⁠](#_Ref223532593) save the intended changes.

> ![](clinical-configuration-manager-ccm-user-guide/166.png)

<span id="_Ref223532593" class="anchor"></span>Figure 165<span id="_Toc223532501" class="anchor"></span>: Restore Timeslot(s) Button for Single Day Timeslot

4.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 166⁠](#_Ref185431532) appears. The user can select “Continue” to return to the grid.

> ![](clinical-configuration-manager-ccm-user-guide/167.png)

<span id="_Ref185431532" class="anchor"></span>Figure 166: Save Successful Window for Single Timeslot Restoration

#### Entire Day Restoration

1.  After searching for a specific date, the user will be shown a full week of scheduling clinic availability. The user will then click the ellipsis next to the necessary timeslot and select the “Restore” button seen in [⁠Figure 167⁠](#_Ref185431555).

> ![](clinical-configuration-manager-ccm-user-guide/168.png)

<span id="_Ref185431555" class="anchor"></span>Figure 167: Restore Timeslot Button for Entire Day Restoration

2.  The Restore Timeslot window will appear. The user will need to select the “Submit” button, seen below in [⁠Figure 168⁠](#_Ref185431574), to continue with restoring timeslots for the entire day.

> ![](clinical-configuration-manager-ccm-user-guide/169.png)

<span id="_Ref185431574" class="anchor"></span>Figure 168: Restore Timeslot Window for Entire Day Timeslots Restoration

3.  The user can confirm the changes have been made successfully when the pop-up seen in [⁠Figure 169⁠](#_Ref185431608) appears. The user can select “Continue” to return to the grid.

> ![](clinical-configuration-manager-ccm-user-guide/170.png)

<span id="_Ref185431608" class="anchor"></span>Figure 169: Save Successful Window for Entire Day Timeslots Restoration

## Creating a New Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: This section of the guide is only applicable to users with the correct write access permissions. If the user does not have write access permissions set to the account, the user will receive the error message shown in [⁠Figure 170⁠](#_Ref185431644). If a user needs access to make changes on this application, please contact the local Clinical Applications Coordinator or Supervisor for assistance.*

![](clinical-configuration-manager-ccm-user-guide/171.png)

<span id="_Ref185431644" class="anchor"></span>Figure 170: Authorization Error Message for Creating a Clinic

1.  To create a new clinic, the users must select the “Create New Clinic” button boxed in [⁠Figure 171⁠](#_Ref185431682) under the Clinic Configurations tab. Selecting the button will cause the Create New Clinic page shown in [⁠Figure 172⁠](#_Ref185431712) to appear.

> ![](clinical-configuration-manager-ccm-user-guide/172.png)

<span id="_Ref185431682" class="anchor"></span>Figure 171: Create a Clinic Button

2.  The user will then see three configuration accordions: Mandatory Fields, Preselected Settings, and Optional Settings, which can be viewed and edited by selecting the “+” shown in [⁠Figure 172⁠](#_Ref185431712). Optionally, the user can select the “Expand All” button to open all accordions at once.

> ![](clinical-configuration-manager-ccm-user-guide/173.png)

<span id="_Ref185431712" class="anchor"></span>Figure 172: Create a Clinic Accordions

- Note: Please see sections [⁠4.6.1 Mandatory Fields⁠](#mandatory-fields), [⁠4.6.2 Preselected Settings⁠](#_Ref217902411), and [⁠4.6.3 Optional Settings⁠](#optional-settings) for examples of the accordions.
3.  Once the required fields have been correctly filled, the “Create Clinic” button seen in [⁠Figure 173⁠](#_Ref185431857) will appear. If not entered correctly, the button will remain greyed out.

> ![](clinical-configuration-manager-ccm-user-guide/174.png)

<span id="_Ref185431857" class="anchor"></span>Figure 173: Create a Clinic Button after Entering Required Information

- Note: The user must create a clinic before timeslots can be added; this function cannot be done in the process of creation. After creating a new clinic, the UI will immediately take the user to the Edit Clinic Availability section to add timeslots associated to the clinic. Please refer to the section [⁠Editing Clinic Configurations⁠](#editing-clinic-configurations) for guidance.

### Mandatory Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with Write Access can edit the fields that will appear within Mandatory Fields shown below in [⁠Figure 174⁠](#_Ref185431742). The field(s) labeled “Required” must be edited before saving. Once all the mandatory fields have been populated with data, a new clinic can be created.

![](clinical-configuration-manager-ccm-user-guide/175.png)

<span id="_Ref185431742" class="anchor"></span>Figure 174: Editing Mandatory Fields for Create a Clinic

- Note: Please go to Section [⁠9.2 Tool Tip Descriptions⁠](#tool-tip-descriptions) for more information on populating clinic settings.
- Note: Users will receive the error message shown in [⁠Figure 175⁠](#_Ref185431773) if users fail to populate any of the required fields.

> ![](clinical-configuration-manager-ccm-user-guide/176.png)

> <span id="_Ref185431773" class="anchor"></span>Figure 175: Error Message from Lack of Required Fields

### Preselected Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with Write Access can edit the fields that will appear within Preselected Fields shown below in [⁠Figure 176⁠](#_Ref185431806).

![](clinical-configuration-manager-ccm-user-guide/177.png)

<span id="_Ref185431806" class="anchor"></span>Figure 176: Editing Preselected Default Fields for Create a Clinic

- Note: Please go to Section [⁠9.2 Tool Tip Descriptions⁠](#tool-tip-descriptions) for more information on populating clinic settings.

### Optional Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with Write Access can edit the fields that will appear within Optional Settings shown below in [⁠Figure 177⁠](#_Ref185431828).

![](clinical-configuration-manager-ccm-user-guide/178.png)

<span id="_Ref185431828" class="anchor"></span>Figure 177: Editing Optional Fields for Create a Clinic

- Note: Please go to Section [⁠9.2 Tool Tip Descriptions⁠](#tool-tip-descriptions) for more information on populating clinic settings.

## Inactivating and Reactivating a Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: This section of the guide is only applicable to users with access permissions SD INACTIVATE for inactivation and SD REACT for reactivation. If the user does not have elevated access permissions set to their VistA account, the user will not see the “Inactivate Clinic” button seen in [⁠Figure 178⁠](#_Ref185431950). If a user needs access to make changes on this application, please contact the local Clinical Applications Coordinator or Supervisor for assistance.*

![](clinical-configuration-manager-ccm-user-guide/179.png)

<span id="_Ref185431950" class="anchor"></span>Figure 178: Inactivate Clinic Button

### Inactivating a Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To inactivate a clinic, the user will first need to search and select a clinic within the Clinic Configurations tab (see [⁠Figure 179⁠](#_Ref185431995)).

> ![](clinical-configuration-manager-ccm-user-guide/180.png)

<span id="_Ref185431995" class="anchor"></span>Figure 179: Clinic Search Example for Inactivating a Clinic

- Note: When trying to inactivate a clinic, the user will receive the error seen in [⁠Figure 180⁠](#_Ref185432021) if patients are actively scheduled. Ensure that <u>all</u> <u>future</u> appointments have been canceled to move forward with inactivation.

> ![](clinical-configuration-manager-ccm-user-guide/181.png)

> <span id="_Ref185432021" class="anchor"></span>Figure 180: Error Message for Inactivating a Clinic

2.  Once a clinic is selected, the user will select the “Inactivate” button seen in [⁠Figure 181⁠](#_Ref185432168).

> ![](clinical-configuration-manager-ccm-user-guide/182.png)

<span id="_Ref185432168" class="anchor"></span>Figure 181: Inactivate Clinic Button for Inactivating a Clinic

3.  Selecting the “Inactivate” button will cause a pop-up to appear (see [⁠Figure 182⁠](#_Ref185432206)) and the user will be asked to select a date of inactivation within a six-month period.

> ![](clinical-configuration-manager-ccm-user-guide/183.png)

<span id="_Ref185432206" class="anchor"></span>Figure 182: Inactivate Date Pop-up

- Note: Inactivating a clinic will remove all existing timeslots. The user will need to rebuild the timeslots upon reactivation of the clinic.
4.  Selecting the “Continue” button (see [⁠Figure 182⁠](#_Ref185432206)) will place the clinic into an inactive status on the date of selection highlighted in red, as seen in [⁠Figure 183⁠](#_Ref185432271).

> ![](clinical-configuration-manager-ccm-user-guide/184.png)

<span id="_Ref185432271" class="anchor"></span>Figure 183: Inactivate Status Date

- Note: A banner of inactivation will display in the Clinic Availability Archive section after the clinic has been inactivated as seen in [⁠Figure 184⁠](#_Ref185432303).

> ![](clinical-configuration-manager-ccm-user-guide/185.png)

> <span id="_Ref185432303" class="anchor"></span>Figure 184: Clinic is Inactive Message

### Reactivating a Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To reactivate a clinic, the user will first need to search and select a clinic within the Clinic Configurations tab (see [⁠Figure 185⁠](#_Ref185432330)).

> ![](clinical-configuration-manager-ccm-user-guide/186.png)

<span id="_Ref185432330" class="anchor"></span>Figure 185: Clinic Search Example for Reactivating a Clinic

2.  Once a clinic is selected, the user will need to select the “Reactivate Clinic” button located in the “Clinic Actions” dropdown seen in [⁠Figure 186⁠](#_Ref185432356).

> ![](clinical-configuration-manager-ccm-user-guide/187.png)

<span id="_Ref185432356" class="anchor"></span>Figure 186: Reactivate Clinic Button

3.  After selecting the “Reactivate Clinic” button, the pop-up window shown in [⁠Figure 187⁠](#_Ref185432385) will appear. This will allow the user to select a date and provider for the clinic to become reactivated.

> ![](clinical-configuration-manager-ccm-user-guide/188.png)

<span id="_Ref185432385" class="anchor"></span>Figure 187: Reactivate Clinic Pop-up

4.  The user will then need to select a date by clicking the calendar button shown below in [⁠Figure 188⁠](#_Ref185432415).

> ![](clinical-configuration-manager-ccm-user-guide/189.png)

<span id="_Ref185432415" class="anchor"></span>Figure 188: Calendar Button for Reactivating a Clinic

5.  The user will also need to enter a provider into the field seen in [⁠Figure 189⁠](#_Ref213167644).

> ![](clinical-configuration-manager-ccm-user-guide/190.png)

<span id="_Ref213167644" class="anchor"></span>Figure 189: Provider Field for Reactivating a Clinic

6.  After entering the required information, the user will need to select the checkbox seen in [⁠Figure 190⁠](#_Ref213230705) to confirm.

> ![](clinical-configuration-manager-ccm-user-guide/191.png)

<span id="_Ref213230705" class="anchor"></span>Figure 190: Confirmation Checkbox for Reactivating a Clinic

- Note: The “Reactivate Clinic” button will remain greyed out until a date and provider are chosen; once chosen, the button will become available for selection as seen in [⁠Figure 191⁠](#_Ref185432455).
7.  Once the information is confirmed, the user can select the “Reactivate Clinic” button seen in [⁠Figure 191⁠](#_Ref185432455).

> ![](clinical-configuration-manager-ccm-user-guide/192.png)

<span id="_Ref185432455" class="anchor"></span>Figure 191: Reactivate Clinic Button

- Note: The user is unable to reactivate a clinic on the same day of inactivation; only future dates are available for selection.

## Replicating a Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: This section of the guide is only applicable to users with the correct write access permissions. If the user does not have write access permissions set to the account, the user will receive the error message shown in [⁠Figure 192⁠](#_Ref213672154). If a user needs access to make changes on this application, please contact the local Clinical Applications Coordinator or Supervisor for assistance.*

![](clinical-configuration-manager-ccm-user-guide/193.png)

<span id="_Ref213672154" class="anchor"></span>Figure 192: Authorization Error Message for Replicating a Clinic

1.  The user will need to follow the steps outlined in section [⁠3.1 Search for a Clinic Configuration⁠](#search-for-a-clinic-configuration) (see [⁠Figure 37⁠](#_Ref184907162) for guidance) to open the clinic configurations for a clinic. On the Clinic Configurations page, the user will need to select the “Clinic Actions” button seen in [⁠Figure 193⁠](#_Ref213672788).

> ![](clinical-configuration-manager-ccm-user-guide/194.png)

<span id="_Ref213672788" class="anchor"></span>Figure 193: Clinic Actions Button for Replicating a Clinic

2.  This will cause the action menu to appear, and the user can then select the “Replicate Clinic” option shown in [⁠Figure 194⁠](#_Ref213673016).

> ![](clinical-configuration-manager-ccm-user-guide/195.png)

<span id="_Ref213673016" class="anchor"></span>Figure 194: Replicate Clinic Option from the Clinic Action Menu

3.  The user will be taken to the Replicate Clinic page where the three configuration accordions: Mandatory Fields, Preselected Settings, and Optional Settings, will be auto-populated with information from the selected clinic (see [⁠Figure 195⁠](#_Ref213673987) for example).

> ![](clinical-configuration-manager-ccm-user-guide/196.png)

<span id="_Ref213673987" class="anchor"></span>Figure 195: Example of Auto-populated Fields for Replicating a Clinic

4.  The clinic configurations for the replicated clinic can be edited, if needed, by selecting the “+” shown in [⁠Figure 196⁠](#_Ref213673355). The user will only be required to enter information for the “Clinic Name” and “Patient Friendly Name” fields, located under the Mandatory Fields accordion, if edits are not necessary.

> ![](clinical-configuration-manager-ccm-user-guide/197.png)

<span id="_Ref213673355" class="anchor"></span>Figure 196: Replicate Clinic Accordions

- Note: Please see sections [⁠4.6.1 Mandatory Fields⁠](#mandatory-fields), [⁠4.6.2 Preselected Settings⁠](#_Ref217902508), and [⁠4.6.3 Optional Settings⁠](#optional-settings) for examples of the accordions.
- Note: Editing the “Length of Appointment,” “Display Increments Per Hour,” or the “Hour Clinic Display Begins” fields located in the Mandatory and Preselected Default Fields accordion will remove the timeslots for the new replicated clinic. Users will see the notification seen in [⁠Figure 197⁠](#_Ref216360809) at the bottom of the Replicate Clinic page upon change.

  ![](clinical-configuration-manager-ccm-user-guide/198.png)

> <span id="_Ref216360809" class="anchor"></span>Figure 197: Clinic Availability Not Replicated Notification

4.  Once the required fields have been correctly filled, the “Replicate Clinic” button seen in [⁠Figure 198⁠](#_Ref213675499) will appear. If not entered correctly, the button will remain greyed out.

> ![](clinical-configuration-manager-ccm-user-guide/199.png)

<span id="_Ref213675499" class="anchor"></span>Figure 198: Replicate Clinic Button after Entering Required Information

- Note: Users will see the window shown below in [⁠Figure 199⁠](#_Ref216361170), when selecting the “Replicate Clinic” button, if changes to the “Length of Appointment,” “Display Increments Per Hour,” or “Hour Clinic Display Begins” fields have been made. The user can either continue with replicating the clinic without timeslots included or close the window to edit the mentioned fields.

  ![](clinical-configuration-manager-ccm-user-guide/200.png)

> <span id="_Ref216361170" class="anchor"></span>Figure 199: Unable to Replicate Clinic Availability Window

5.  After selecting “Replicate Clinic,” the user will see the pop-up seen in [⁠Figure 200⁠](#_Ref216355935), where they can choose to either keep the original clinic or select a date of inactivation. The user will then need to select the “Continue” button to save changes.

    ![](clinical-configuration-manager-ccm-user-guide/201.png)

<span id="_Ref216355935" class="anchor"></span>Figure 200: Clinic Successfully Replicated Window

- Note: The user must create a clinic before timeslots can be added or modified; this function cannot be done in the process of creation. After creating a replicate clinic, the UI will immediately take the user to the Edit Clinic Availability section to add or modify timeslots associated to the clinic. Please refer to the section [⁠Editing Clinic Configurations⁠](#editing-clinic-configurations) for guidance.

# Clinic Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the Clinic Audit Report, the user will need to select the “Clinic Audit Report” tab seen in [⁠Figure 201⁠](#_Ref207199930).

![](clinical-configuration-manager-ccm-user-guide/202.png)

<span id="_Ref207199930" class="anchor"></span>Figure 201: Clinic Audit Report Tab

- Note: Users will see the error in [⁠Figure 1⁠](#_Ref185007111) if they do not have access to the page. Please see [⁠1.2 Prerequisite Credentials⁠](#prerequisite-credentials) for more information.

## Familiarizing Yourself with the Clinic Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once log in is complete, users will see the CCM Clinic Audit Report page as seen in [⁠Figure 202⁠](#_Ref185432640). The user will be able to access reports for both “Clinic Profile Edit” and “Clinic Profile Add” on this webpage. By default, all clinic profile information is shown within these grids until further filtered. Please be aware that selecting any info in the header will navigate the user away from the report.

![](clinical-configuration-manager-ccm-user-guide/203.png)

<span id="_Ref185432640" class="anchor"></span>Figure 202: CCM Change Assessment Report Homepage

- *Note: When viewing entries in the Clinic Profile Edit section, data will only be shown to the user if the value has been changed. The report will have a blank value if there have been no changes to a clinic attribution or will show an “@” symbol if there was once data that has since been removed.*
- *Note: Users can expand the dropdown labeled “Clinic Modification Trends (Last 30 Days),” seen in [⁠Figure 203⁠](#_Ref185860638) to see an overview ofClinic Modification Trends over the past 30 days.*

> ![](clinical-configuration-manager-ccm-user-guide/204.png)

> <span id="_Ref185860638" class="anchor"></span>Figure 203: Clinic Modification Trends

## Filtering Reports and Exporting Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Filtering Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users have the ability to filter data for both the Clinic Profile Add and Clinic Profile Edit reports simultaneously by adjusting the filter options shown in [⁠Figure 204⁠](#_Ref185432673).

![](clinical-configuration-manager-ccm-user-guide/205.png)

<span id="_Ref185432673" class="anchor"></span>Figure 204: Filter Options

Only one option can be chosen within each of the filter selections at a time. Search results will continue to narrow down further as more of the filters are added. Once any filter is selected, the “Reset Filters” button will appear to give users the options to reset all filters that have been applied, as seen in [⁠Figure 205⁠](#_Ref185861005). See the [⁠Table 1⁠](#_Ref185861019) below for a brief description on what each filter does.

![](clinical-configuration-manager-ccm-user-guide/206.png)

<span id="_Ref185861005" class="anchor"></span>Figure 205: Reset Filters Button

| Filter Name  | Filter Descriptions                                                                |
|--------------|------------------------------------------------------------------------------------|
| Station      | Parent and child site numbers                                                      |
| Username     | Name of the individual that made the edit or add                                   |
| Clinic IEN   | Clinic Internal Entry Number (referred to as the unique identifier for the clinic) |
| Clinic Name  | Name of the clinic                                                                 |
| Filter Dates | Ability to change the report start and end time                                    |

<span id="_Toc223532592" class="anchor"></span>Table 2: Tool Tip Descriptions

### Filtering with Dropdowns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To filter by dropdown, select the dropdown function located underneath a filter’s name as seen in [⁠Figure 206⁠](#_Ref185432701).

> ![](clinical-configuration-manager-ccm-user-guide/207.png)

> <span id="_Ref185432701" class="anchor"></span>Figure 206: Example of Choosing Filter Selection

2.  The user will then select the preferred option from the available selection, shown in [⁠Figure 207⁠](#_Ref185432730).

> ![](clinical-configuration-manager-ccm-user-guide/208.png)

> <span id="_Ref185432730" class="anchor"></span>Figure 207: Example of Filter Selection Dropdown

3.  Once selected, search results within both Clinic Profile Edit and Clinic Profile Add will automatically update. Users can choose to further narrow the report by selecting more filters.

### Filtering by Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To filter by date range, select the “Filter Dates” button shown in [⁠Figure 208⁠](#_Ref185432764).

> ![](clinical-configuration-manager-ccm-user-guide/209.png)

> <span id="_Ref185432764" class="anchor"></span>Figure 208: Filter Dates Button

2.  Users will be brought to the Filter Date Ranges window. To begin, the user will need to select the calendar button, shown below in [⁠Figure 209⁠](#_Ref185432784), to choose a start date, or manually type the date into the Enter Start Date field.

> ![](clinical-configuration-manager-ccm-user-guide/210.png)

> <span id="_Ref185432784" class="anchor"></span>Figure 209: Calendar Button for Enter Start Date

3.  Users will then need to select the calendar button, shown below in [⁠Figure 210⁠](#_Ref185432807), to choose an end date, or manually type the date into the Enter End Date field.

> ![](clinical-configuration-manager-ccm-user-guide/211.png)

> <span id="_Ref185432807" class="anchor"></span>Figure 210: Calendar Button for Enter End Date

4.  Once both dates are selected, users will then select the “Filter Dates” button shown in [⁠Figure 211⁠](#_Ref185432831).

> ![](clinical-configuration-manager-ccm-user-guide/212.png)

> <span id="_Ref185432831" class="anchor"></span>Figure 211: Filter Dates Button on the Filter Date Ranges Window

- *Note: The user can also select the “Cancel” button seen in [⁠Figure 211⁠](#_Ref185432831) to exit filter date ranges and go back to the Change Assessment Report page.*
5.  Once selected, search results within both Clinic Profile Edit and Clinic Profile Add will automatically update. Users can choose to further narrow the report by selecting more filters.

## Exporting Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users also have the ability to export data from either the Clinic Profile Edit or Clinic Profile Add tables into an excel document. To do so, select the “Export All Data” button, shown in [⁠Figure 212⁠](#_Ref185432969), found above the table the user wishes to export. Once selected, the user will then need to follow the on-screen browser instructions to save and download the file to the computer.

![](clinical-configuration-manager-ccm-user-guide/213.png)

<span id="_Ref185432969" class="anchor"></span>Figure 212: Export All Data Button

# Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the Letters page, users can create a new letter or edit an existing letter.

## Create a Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a new letter, the user will need to select the “Letters” tab shown below in [⁠Figure 213⁠](#_Ref208411852) to be brought to the Letters page.

> ![](clinical-configuration-manager-ccm-user-guide/214.png)

<span id="_Ref208411852" class="anchor"></span>Figure 213: Letters Tab

2.  The user will then need to select the “Create Letter” button seen in [⁠Figure 214⁠](#_Ref208411908).

> ![](clinical-configuration-manager-ccm-user-guide/215.png)

<span id="_Ref208411908" class="anchor"></span>Figure 214: Create Letter Button on the Letters Page

3.  The Create New Letter page will then appear. Fill in all the required fields and select optional toggle boxes, as needed (See [⁠Figure 215⁠](#_Ref208411973) for example).

> ![](clinical-configuration-manager-ccm-user-guide/216.png)

<span id="_Ref208411973" class="anchor"></span>Figure 215: Example of Letter

4.  Once all the required fields have been filled out, the user will need to select the “Create Letter” button, shown in [⁠Figure 216⁠](#_Ref208412012), to create the letter.

> ![](clinical-configuration-manager-ccm-user-guide/217.png)

<span id="_Ref208412012" class="anchor"></span>Figure 216: Create Letter Button on the Create New Letter Page

## Edit a Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To edit a letter, the user will need to search for an existing letter by selecting the letter type of the original letter that needs modification. Optionally, the user can use the “Search by Letter Name” function (case sensitive) to further narrow the results. After inputting the necessary information, the user will need to select the “Search” button, shown below in [⁠Figure 217⁠](#_Ref208412375).

> ![](clinical-configuration-manager-ccm-user-guide/218.png)

<span id="_Ref208412375" class="anchor"></span>Figure 217: Search Button for Editing Letters

2.  All existing letters that match the search criteria will appear. The user will need to select the ellipsis next to the letter that needs to be edited and then select the “Edit Letter” option seen in [⁠Figure 218⁠](#_Ref208415226).

> ![](clinical-configuration-manager-ccm-user-guide/219.png)

<span id="_Ref208415226" class="anchor"></span>Figure 218: Edit Letter Button from the Action Menu

3.  The Edit Letter page will appear (see [⁠Figure 219⁠](#_Ref208415363) for example) where users will need to make minimum of one edit to continue.

> ![](clinical-configuration-manager-ccm-user-guide/220.png)

<span id="_Ref208415363" class="anchor"></span>Figure 219: Edit Letter Page

4.  Once all edits have been made, the user will select the “Save Changes” button shown in [⁠Figure 220⁠](#_Ref208415446) to save all changes.

> ![](clinical-configuration-manager-ccm-user-guide/221.png)

<span id="_Ref208415446" class="anchor"></span>Figure 220: Save Changes Button for Edit Letter Page

## Delete a Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To delete a letter, the user will need to search for an existing letter by selecting the letter type of the original letter that needs to be deleted. Optionally, the user can use the “Search by Letter Name” function (case sensitive) to further narrow the results. After inputting the necessary information, the user will need to select the “Search” button, shown below in [⁠Figure 221⁠](#_Ref208415536).

> ![](clinical-configuration-manager-ccm-user-guide/222.png)

<span id="_Ref208415536" class="anchor"></span>Figure 221: Search Button for Deleting Letters

2.  All existing letters that match the search criteria will appear. The user will need to select the ellipsis next to the letter that needs to be deleted and then select the “Delete Letter” option, shown in [⁠Figure 222⁠](#_Ref208415610).

> ![](clinical-configuration-manager-ccm-user-guide/223.png)

<span id="_Ref208415610" class="anchor"></span>Figure 222: Delete Letter Button from the Action Menu

3.  The Delete Letter window will appear. The user will need to select the “Delete Letter” button, shown below in [⁠Figure 223⁠](#_Ref208415688), to delete the letter.

> ![](clinical-configuration-manager-ccm-user-guide/224.png)

<span id="_Ref208415688" class="anchor"></span>Figure 223: Delete Letter Button

# VA Tool Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the pages within VA Tool Set, select the “+” shown below in [⁠Figure 224⁠](#_Ref185513301). Afterwards, the accordion view shown in [⁠Figure 225⁠](#_Ref185516786) will appear.

![](clinical-configuration-manager-ccm-user-guide/225.png)

<span id="_Ref185513301" class="anchor"></span>*Figure 224: VA Tool Set Tab*

![](clinical-configuration-manager-ccm-user-guide/226.png)

<span id="_Ref185516786" class="anchor"></span>*Figure 225: VA Tool Set Accordion View*

## Veteran Self Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the Veteran Self Scheduling tab, users can search and view Veteran Self Scheduling for a specific clinic. In addition to these capabilities, users with the correct edit permissions are able to edit in Veteran Self Scheduling. Please note that services vary depending on location.

### View Veteran Self Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the tab labeled “Veteran Self Scheduling” shown below in [⁠Figure 226⁠](#_Ref185432993) to be directed to the Veteran Self Scheduling page.

> ![](clinical-configuration-manager-ccm-user-guide/227.png)

> <span id="_Ref185432993" class="anchor"></span>*Figure 226: Viewing Veteran Self Scheduling*

2.  Select the “+” shown in [⁠Figure 227⁠](#_Ref185433024) to expand the pinned services accordion. Afterwards, the accordion view shown in [⁠Figure 228⁠](#_Ref185433044) will appear.

> ![](clinical-configuration-manager-ccm-user-guide/228.png)

> <span id="_Ref185433024" class="anchor"></span>*Figure 227: Pinned Services Button for Viewing VA Self Scheduling*

> ![](clinical-configuration-manager-ccm-user-guide/229.png)

> <span id="_Ref185433044" class="anchor"></span>*Figure 228: Expanded Accordions of Viewing VA Self Scheduling Settings*

### Edit Veteran Self Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: This section of the guide is only applicable to users with the correct write access permissions. If the user does not have write access permissions set to the account, the user will receive the error message shown in [⁠Figure 229⁠](#_Ref185433067). If a user needs access to make changes on this application, please contact the local Clinical Applications Coordinator or Supervisor for assistance.*

![](clinical-configuration-manager-ccm-user-guide/230.png)

<span id="_Ref185433067" class="anchor"></span>*Figure 229: Authorization Error Message for VA Self Scheduling Settings*

1.  Select the tab labeled “Veteran Self Scheduling” shown below in [⁠Figure 230⁠](#_Ref185433092) to be directed to the Veteran Self Scheduling page.

> ![](clinical-configuration-manager-ccm-user-guide/231.png)

> <span id="_Ref185433092" class="anchor"></span>*Figure 230: Editing Veteran Self Scheduling*

2.  Select the “+” shown in [⁠Figure 231⁠](#_Ref185433110) to expand the pinned services accordion. Afterwards, the accordion shown in [⁠Figure 232⁠](#_Ref185433126) will appear where the user will be able to edit selections.

> ![](clinical-configuration-manager-ccm-user-guide/232.png)

> <span id="_Ref185433110" class="anchor"></span>*Figure 231: Pinned Services Button for Editing VA Self Scheduling*

> ![](clinical-configuration-manager-ccm-user-guide/233.png)

> <span id="_Ref185433126" class="anchor"></span>*Figure 232: Accordion View of Editing VA Self Scheduling Settings*

3.  After making necessary changes, select the save button shown in [⁠Figure 233⁠](#_Ref185433147).

> ![](clinical-configuration-manager-ccm-user-guide/234.png)

> <span id="_Ref185433147" class="anchor"></span>*Figure 233: Save Button for VA Self Scheduling Settings*

- *Note: The “Save” button only becomes available in the bottom right-hand corner on the VA Self Scheduling page when <u>a minimum of one</u> change has been made; if no change is made, the “Save” button as seen in [⁠Figure 233⁠](#_Ref185433147) will not appear.*
- *Note: Some but not all fields have a mandatory (\*Required) field which needs to be populated before saving. If a user tries to save without selecting a mandatory (\*Required) field, they will receive the error message shown in [⁠Figure 234⁠](#_Ref185433205).*

  ![](clinical-configuration-manager-ccm-user-guide/235.png)

> <span id="_Ref185433205" class="anchor"></span>*Figure 234: Error Field for Saving in VA Self Scheduling*

4.  Once the save is complete, the user should select “Continue” from the pop-up window shown below in [⁠Figure 235⁠](#_Ref185433223).

> ![](clinical-configuration-manager-ccm-user-guide/236.png)

> <span id="_Ref185433223" class="anchor"></span>*Figure 235: Saving in VA Self Scheduling*

5.  A timestamp will then be presented to the user, which details the date of the last modification(s) and the name of the person who had last modified shown in [⁠Figure 236⁠](#_Ref185433245).

> ![](clinical-configuration-manager-ccm-user-guide/237.png)

> <span id="_Ref185433245" class="anchor"></span>*Figure 236: Time Stamp after Saving in VA Self Scheduling*

## Veteran Appointment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the Veteran Appointment Requests tab, users can search and view Veteran Appointment Requests for a specific clinic. In addition to these capabilities, users with the correct edit permissions are able to edit Veteran Appointment Requests. Please note that services vary depending on location.

### View Veteran Appointment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the tab labeled “Veteran Appointment Requests” shown below in [⁠Figure 237⁠](#_Ref213676481) to be directed to the Veteran appointment requests page.

> ![](clinical-configuration-manager-ccm-user-guide/238.png)

> <span id="_Ref213676481" class="anchor"></span>*Figure 237: Viewing Veteran Appointment Requests*

2.  Select the “+” shown in [⁠Figure 238⁠](#_Ref213676482) to expand the pinned services accordion. Afterwards, the accordion view shown in [⁠Figure 239⁠](#_Ref213676483) will appear.

> ![](clinical-configuration-manager-ccm-user-guide/239.png)

> <span id="_Ref213676482" class="anchor"></span>*Figure 238: Pinned Services Button for Viewing VA Appointment Requests*

> ![](clinical-configuration-manager-ccm-user-guide/240.png)

> <span id="_Ref213676483" class="anchor"></span>*Figure 239: Expanded Accordions of Viewing VA Appointment Requests*

### Edit Veteran Appointment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Disclaimer: This section of the guide is only applicable to users with the correct write access permissions. If the user does not have write access permissions set to the account, the user will receive the error message shown in [⁠Figure 240⁠](#_Ref213676484). If a user needs access to make changes on this application, please contact the local Clinical Applications Coordinator or Supervisor for assistance.*

![](clinical-configuration-manager-ccm-user-guide/241.png)

<span id="_Ref213676484" class="anchor"></span>*Figure 240: Authorization Error Message for VA Appointment Requests Settings*

1.  Select the tab labeled “Veteran Appointment Requests” shown below in [⁠Figure 241⁠](#_Ref213676485) to be directed to the Veteran appointment requests page.

> ![](clinical-configuration-manager-ccm-user-guide/242.png)

> <span id="_Ref213676485" class="anchor"></span>*Figure 241: Veteran Appointment Requests Tab*

2.  Select the “+” shown in [⁠Figure 242⁠](#_Ref213676486) to expand the pinned services accordion. Afterwards, the accordion shown in [⁠Figure 243⁠](#_Ref213676487) will appear where the user will be able to edit selections.

> ![](clinical-configuration-manager-ccm-user-guide/243.png)

> <span id="_Ref213676486" class="anchor"></span>*Figure 242: Pinned Services Button for VA Appointment Requests*

> ![](clinical-configuration-manager-ccm-user-guide/244.png)

> <span id="_Ref213676487" class="anchor"></span>*Figure 243: Accordion View of VA Appointment Requests*

3.  After making necessary changes, select the save button shown in [⁠Figure 244⁠](#_Ref213676488).

> ![](clinical-configuration-manager-ccm-user-guide/245.png)

> <span id="_Ref213676488" class="anchor"></span>*Figure 244: Save Button for VA Appointment Requests Settings*

- *Note: The “Save” button only becomes available in the bottom right-hand corner on the Veteran Appointment Requests page when <u>a minimum of one</u> change has been made. If no change is made, the “Save” button as seen in [⁠Figure 244⁠](#_Ref213676488) will not appear.*
- *Note: Some but not all fields are mandatory (\*Required) and need to be populated before saving. If a user tries to save without populating a mandatory (\*Required) field, the user will receive the error message shown in [⁠Figure 245⁠](#_Ref213677462).*

  ![](clinical-configuration-manager-ccm-user-guide/246.png)

> <span id="_Ref213677462" class="anchor"></span>*Figure 245: Error Field for Saving in VA Appointment Requests*

4.  Once the save is complete, the user should select “Continue” from the pop-up window shown below in [⁠Figure 246⁠](#_Ref213677488).

> ![](clinical-configuration-manager-ccm-user-guide/247.png)

> <span id="_Ref213677488" class="anchor"></span>*Figure 246: Saving in VA Appointment Requests*

5.  A timestamp will then be presented to the user, which details the date of the last modification(s) and the name of the person who had last modified shown below in [⁠Figure 247⁠](#_Ref213677520).

> ![](clinical-configuration-manager-ccm-user-guide/248.png)

> <span id="_Ref213677520" class="anchor"></span>*Figure 247: Time Stamp after Saving in VA Appointment Requests*

# Annual Clinic Profile Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Annual Clinic Profile Review page can be navigated to by selecting the Annual Clinic Profile Review tab shown in [⁠Figure 248⁠](#_Ref207376601).

> ![](clinical-configuration-manager-ccm-user-guide/249.png)

<span id="_Ref207376601" class="anchor"></span>Figure 248: Annual Clinic Profile Review Tab

2.  Users will need to complete at least one of the search criteria to select the “Run Report” button seen in [⁠Figure 249⁠](#_Ref207376602).

> ![](clinical-configuration-manager-ccm-user-guide/250.png)

<span id="_Ref207376602" class="anchor"></span>Figure 249: Run Report Button for Annual Clinic Profile Review

- Note: CCM will only return active clinics. Clinics that have been inactivated will not be included in the report.
3.  Once the report has been run and valid results appear, the Clinic Profile Review Successful message will appear. Users will then select the “Click to download Clinic Profile Review” button, shown in [⁠Figure 250⁠](#_Ref207376603).

> ![](clinical-configuration-manager-ccm-user-guide/251.png)

<span id="_Ref207376603" class="anchor"></span>Figure 250: Download Link for Annual Clinic Profile Review

- Note: If the user tries to search for a clinic with no available results, the error message shown in [⁠Figure 251⁠](#_Ref207376604) will appear.

  ![](clinical-configuration-manager-ccm-user-guide/252.png)

> <span id="_Ref207376604" class="anchor"></span>Figure 251: No Results Found Notification for Annual Clinic Profile Review

4.  Once selected, the user will need to follow the on-screen browser instructions to save and download the file to the computer.
- Note: If the user needs more information regarding annual clinic profile reviews, please select the Annual Clinic Profile Review button shown below in [⁠Figure 252⁠](#_Ref207376605).

  ![](clinical-configuration-manager-ccm-user-guide/253.png)

> <span id="_Ref207376605" class="anchor"></span>Figure 252: Resource Information Link for Annual Clinic Profile Review

# References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Additional Features and Options for CCM-UI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Users can stay in their existing browser session to view and/or change their Site or Divisions that they are provisioned to. There is no need to log out and log back in every time.
- Job Guide/pdf link for new user orientation.
- [<u>Link</u>](https://dvagov.sharepoint.com/sites/ClinicProfileManagementGuide30/SiteAssets/Forms/AllItems.aspx?id=%2Fsites%2FClinicProfileManagementGuide30%2FSiteAssets%2FSitePages%2FHome%2FClinic%2DProfile%2DManagement%2DBusiness%2DRules%2Epdf&parent=%2Fsites%2FClinicProfileManagementGuide30%2FSiteAssets%2FSitePages%2FHome) to Clinic Profile Management Business Rules.
- Help desk contact info if users need assistance with the new CCM-UI application:
- [<u>YourIT Service Portal</u>](https://yourit.va.gov/va)
- VA Help Desk: 855-673-4357
- TTY: 844-224-6186
- Veterans Crisis Hotline: 800-273-8255

## Tool Tip Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name                                 | Tool Tip Info                                                                                                                                                                                                                                                                                                                                                          | Section                                                  |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| Clinic Name (\*Required)                   | Examples: SGV-PACT BLUE TEAM 1 PA or MIA/CVT DERMATOLOGY PRO                                                                                                                                                                                                                                                                                                           | Mandatory                                                |
| Patient Friendly Name (\*Required)         | Example: MOREHEAD VA VIDEO CONNECT PACT 3 DOCTOR SMITH                                                                                                                                                                                                                                                                                                                 | Mandatory                                                |
| Stop Code (Primary)(\*Required)            | Three digit stop code number assigned to specific location. Each stop code number represents a type of care or Service/treating specialty (clinics only). Example: 001 - 999 Please confirm with your MCA Representative on using the correct stop code.                                                                                                               | Mandatory                                                |
| Medical Center Division (\*Required)       | Division name assigned to each entry in this file to identify where the specific location is. Only one division per location.                                                                                                                                                                                                                                          | Mandatory                                                |
| Select Provider(s) (\*Required)            | Provider must be active and have an active entry in the NEW PERSON file for PERSON CLASS                                                                                                                                                                                                                                                                               | Mandatory                                                |
| Length of Appointments (\*Required)        | Length of appointment designated for clinic. Type a whole number between 10 and 240 - must be a multiple of 10 or 15.                                                                                                                                                                                                                                                  | Mandatory                                                |
| Telephone (\*Required)                     | Example: 303-555-1212 or 303 555 1212                                                                                                                                                                                                                                                                                                                                  | Mandatory                                                |
| Telephone Extension (\*Required)           | Example: 542. If no extension is available, use N/A or n/a                                                                                                                                                                                                                                                                                                             | Mandatory                                                |
| Physical Location (\*Required)             | Where the Veteran will check-in for an appointment. Limit 25 characters. If the location does not require the patient to travel to a VA facility for the appointments, the service must ensure that the location reflects PHONE for telephone appointments and VIDEO CONNECT for VA connect appoints within all reminders (Pre-Appointment Letters, VEText, AudioCare) | Mandatory                                                |
| Clinic meets at this facility?             | Enter YES unless non-VA care                                                                                                                                                                                                                                                                                                                                           | Preselected Default                                      |
| Allow Direct Patient Scheduling?           | This field will determine if patients can self-schedule into this clinic. A "Yes" in this field will enable patients to directly schedule appointments into this clinic. Default selection is set to Yes.                                                                                                                                                              | Preselected Default                                      |
| Non-count Clinic?                          | Is this clinic to be a non-count clinic for workload purposes? OR are visits to this clinic to be included in workload statistics? Default selection is set to Yes                                                                                                                                                                                                     | Preselected Default                                      |
| Variable Appointment Length?               | Does the clinic have variable appointment lengths? If length of appointment is 10 minutes, can user make longer appointments in increments of 10 minutes when scheduling appointment?                                                                                                                                                                                  | Preselected Default                                      |
| Display Appointments to Patients?          | The Office of Community Care recommends that all appointments are viewable to our Veterans. Allows patients to view appointments in My HealtheVet and VA Online Scheduling. Default selection is set to Yes'                                                                                                                                                           | Preselected Default                                      |
| Schedule on Holidays?                      | Should the user be able to schedule appointments on holidays for this location?                                                                                                                                                                                                                                                                                        | Preselected Default                                      |
| Hour Clinic Display Begins                 | The hour clinic will begin displaying availability (e.g. 8 AM)                                                                                                                                                                                                                                                                                                         | Preselected Default                                      |
| Default Appointment Type                   | The default or usual appointment type to be associated with this clinic                                                                                                                                                                                                                                                                                                | Preselected Default                                      |
| Max Days for Future Booking                | Maximum number of days that can be available when clerk searching for open clinic slots in the future. Allows for 11 to 999 days in advance for future bookings.                                                                                                                                                                                                       | Preselected Default                                      |
| Display Increments Per Hour                | Select the increment that best fits the length of appointment. Choose from: 60-Min; 30-Min; 15-Min; 20-Min; 10-Min.                                                                                                                                                                                                                                                    | Preselected Default                                      |
| Overbooks Per Day Maximum                  | Number of allowable overbooks per day. If overbooks are not allowed, the number should be set to zero. Only Numeric values of 0 to 9999 are only allowed.                                                                                                                                                                                                              | Preselected Default                                      |
| Pre-Checkin Allowed?                       | This field will determine if PRE-Checkin is allowed for this clinic                                                                                                                                                                                                                                                                                                    | Preselected Default                                      |
| E-Checkin Allowed?                         | This field will determine if E-Checkin is allowed for the clinic.                                                                                                                                                                                                                                                                                                      | Preselected Default                                      |
| Administer Inpatient Meds?                 | This field should contain a YES only if the clinic location is authorized to dispense inpatient medications to outpatients.                                                                                                                                                                                                                                            | Preselected Default                                      |
| Workload Validation at Check Out?          | Yes or 1 will result in a validation being performed on each checked out encounter for this clinic. No or zero will stop the validation of the encounters as they are checked out for this clinic. This validation is to help ensure that the workload data is acceptable to the Austin National Patient Care Database.                                                | Preselected Default                                      |
| Service Code                               | Enter the Service Line. Example would be Medicine, Surgery, etc.                                                                                                                                                                                                                                                                                                       | Preselected Default                                      |
| Abbreviations                              | Consistency will help schedulers have easy access to the clinic. Example: Community Care clinics must enter abbreviation COMCARE. This will be utilized for reporting.                                                                                                                                                                                                 | Optional                                                 |
| Credit Stop Code (Secondary)               | Enter the Stop Code which should be credited for an appointment to this clinic (only if Code different than the one assigned to this clinic). Appointments to this clinic will receive this stop code credit in addition to the 'normal' stop code credit if a stop code different from the 'normal' stop code for this clinic is entered here. Example: 001 - 999     | Optional                                                 |
| Select Default Provider                    | Please select one default for Provider                                                                                                                                                                                                                                                                                                                                 | Optional                                                 |
| Clinic Cancellation Letter                 | Enter the clinic cancellation letter to be associated with this clinic, so if clinic is cancelled, this letter will print as opposed to generic clinic cancellation letter.                                                                                                                                                                                            | Optional                                                 |
| No Show Letter                             | Enter the no-show letter to be associated with this clinic, so if patient does not show for appointment, this specific no-show letter will print as opposed to the generic no-show letter.                                                                                                                                                                             | Optional                                                 |
| Pre-Appointment Letter                     | Enter the pre-appointment letter to be associated with this clinic, so if letters are generated, this specific pre-appointment letter will print as opposed to the generic pre-appointment letter                                                                                                                                                                      | Optional                                                 |
| Appointment Cancellation Letter            | Enter appointment cancellation letter to be associated with this clinic, so if veteran cancels appointment, this letter will print as opposed to generic appointment cancellation letter.                                                                                                                                                                              | Optional                                                 |
| Special Instructions                       | Special instructions (free text) entered by clerk at time of making the appointment. If you have new instructions, please remove the old ones. It is preferable to keep this as short and simple as possible. Example instructions: SCHEDULE CONSULTS IN PM, FOLLOW-UPS IN AM.                                                                                         | Optional                                                 |
| Prohibit Access to Clinic?                 | Should only privileged users have access to book to this clinic?                                                                                                                                                                                                                                                                                                       | Optional                                                 |
| Add/Remove Privileged User(s) (\*Required) | Current list shows existing Privileged Users associated to this facility/clinic. Please select a name to remove any users from current list.                                                                                                                                                                                                                           | Optional                                                 |
| Select Day of Week (\*Required)            | Select week for date range from Sunday through Saturday to view Timeslots of the week.                                                                                                                                                                                                                                                                                 | Clinic Configuration Clinic Availability accordion panel |
| Single Day                                 | Single Day allows new timeslot entries that will not repeat. Can add multiple entries for that day.                                                                                                                                                                                                                                                                    | Add/Modify Timeslot Modal                                |
| Indefinite                                 | Indefinite allows new timeslot entries that will repeat indefinitely until new timeslots overwrite any pre-existing entries. Can add multiple entries for that day.                                                                                                                                                                                                    | Add/Modify Timeslot Modal                                |
| Multi-select                               | Multi-Select allows timeslot entries associated to that day to repeat in multiple weeks as needed. Can add multiple entries for that day.                                                                                                                                                                                                                              | Add/Modify Timeslot Modal                                |

## Additional Help with Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Connection Issues Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If users receive the 500 Error Message seen below in [⁠Figure 253⁠](#_Ref185433564), please contact IT Support. Go to [<u>YourIT Service Portal</u>](https://yourit.va.gov/va) to open a new ticket or view existing service tickets.
![](clinical-configuration-manager-ccm-user-guide/254.png)
<span id="_Ref185433564" class="anchor"></span>Figure 253: 500 Error Message for Connection
<u>Possible Root Cause</u>: An API connection to the database is down or impaired. 
Additional Resources:
- VA Help Desk: 855-673-4357
- TTY: 844-224-6186

### Server Issue Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If users receive the 500 Error Message seen below in [⁠Figure 254⁠](#_Ref185433581), please contact IT support. Go to [<u>YourIT Service Portal</u>](https://yourit.va.gov/va) to open a new ticket or view existing service tickets.
![](clinical-configuration-manager-ccm-user-guide/255.png)
<span id="_Ref185433581" class="anchor"></span>Figure 254: 500 Error Message for Server Issues
<u>Possible Root Cause</u>: Possible recent server reboot. Please select your browser refresh and try again. If the issue persists, please contact your IT support.
Additional Resources:
- VA Help Desk: 855-673-4357
- TTY: 844-224-6186
