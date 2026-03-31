---
title: PATS User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: PATS
app_code: QAC
app_name: Patient Advocate Tracking System (PATS)
section: GUI
app_status: active
pkg_ns: QAC
patch_ver: 1.5
patch_id: QAC*1.5
group_key: "QAC:QAC:1.5"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 35%\\" /> <col style=\\"width: 64%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Report Category</th> <th><p><strong>Patient Advocates Reports:</strong> There are five report categories on the menu bar: Employee, Facility Service or Section, Issue code, Patient, R"
audience: 
keywords: 
  - report
  - issue
  - table
  - pats
  - contents
  - edit
  - contact
  - patient
  - date
  - query
page_count: 0
word_count: 27521
section_count: 70
table_count: 23
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: May 2007
revision_count: 1
revision_newest: 05/09/07
revision_oldest: 05/09/07
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Patient_Advocate_Track/pats_1_5_userguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Patient_Advocate_Track/pats_1_5_userguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=172"
---

![](pats-user-guide/001.png)

PATIENT ADVOCATE TRACKING SYSTEM (PATS)USER GUIDE

May 2007

Revised June 2009;

Revised October 2009;

Revised July 2010;

Office of Enterprise Development (OED)

Revision History

The following table displays the revision history for this document.

|              |             |                                                                                                                                                                              |                                    |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Date     | Version | Description                                                                                                                                                              | Author                         |
| 05/09/07 | 1.0         | Initial Assembly                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 6-2-09   | 1.1         | Updated screenshots (Based on KAAJEE upgrade)                                                                                                                                | <span class="mark">REDACTED</span> |
| 10-20-09 | 1.2         | Added Session Timeout warning information                                                                                                                                    | <span class="mark">REDACTED</span> |
| 07-10-10 | 1.3         | Updated former references to EMC to a new name - EIE                                                                                                                         | <span class="mark">REDACTED</span> |
| 07-13-12 | 1.4         | Updated ‘About This Document’ and ‘Chapter 1 – PATS Overview’ sections and added section 2.5 ‘Automatic ROC Creation’ to include Patient Advocacy Database (PAD) information | <span class="mark">REDACTED</span> |
| 03-10-13 | 1.5         | Updated screenshot for add ROC to show the new treatment status. Added additional PAD servlet information to identify IRIS-sent ROCs.                                        | <span class="mark">REDACTED</span> |

Contents

# About this Document


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [About this Document](#about-this-document)
    - [Chapter Descriptions](#chapter-descriptions)
    - [What Users Should Read](#what-users-should-read)
    - [Naming Conventions](#naming-conventions)
- [Chapter 1 - PATS Overview](#chapter-1-pats-overview)
  - [Logging onto PATS](#logging-onto-pats)
  - [Setting up an Icon on the Desktop](#setting-up-an-icon-on-the-desktop)
  - [User Settings](#user-settings)
  - [Timing Out](#timing-out)
  - [Using the Calendar Icons](#using-the-calendar-icons)
  - [Entering Required Fields](#entering-required-fields)
  - [Using Online Help](#using-online-help)
  - [Navigation](#navigation)
- [Chapter 2 - Creating a Report of Contact](#chapter-2-creating-a-report-of-contact)
  - [Creating a New ROC](#creating-a-new-roc)
  - [Adding Contact Information](#adding-contact-information)
  - [Adding Patient Information](#adding-patient-information)
  - [Adding Issue Text](#adding-issue-text)
  - [Automatic ROC Creation through the PAD interface](#automatic-roc-creation-through-the-pad-interface)
- [Chapter 3 - Editing a Saved ROC](#chapter-3-editing-a-saved-roc)
  - [Finding an ROC](#finding-an-roc)
  - [Listing an ROC](#listing-an-roc)
  - [Updating Contact Information](#updating-contact-information)
  - [Changing Patient Information](#changing-patient-information)
  - [Changing Issue Text](#changing-issue-text)
  - [Sending Informational Notifications](#sending-informational-notifications)
  - [Sending Action Request Notifications](#sending-action-request-notifications)
  - [Adding, Changing, Removing Issue Codes](#adding-changing-removing-issue-codes)
  - [Adding and Removing an Employee from an Existing Issue](#adding-and-removing-an-employee-from-an-existing-issue)
  - [Closing an ROC](#closing-an-roc)
  - [Reopening a Closed ROC](#reopening-a-closed-roc)
  - [Deleting an ROC](#deleting-an-roc)
- [# Chapter 4 – Standard Reports](#chapter-4-standard-reports)
  - [Understanding Terminology/Conventions](#understanding-terminologyconventions)
    - [Summary](#summary)
  - [Scheduling Reports](#scheduling-reports)
  - [Entering Selection Criteria](#entering-selection-criteria)
    - [Selecting the Date Range](#selecting-the-date-range)
    - [Selecting the Division](#selecting-the-division)
    - [Selecting the Employee Involved](#selecting-the-employee-involved)
    - [Selecting the Facility Service or Section](#selecting-the-facility-service-or-section)
    - [Selecting the Patient](#selecting-the-patient)
    - [Selecting the ROC number](#selecting-the-roc-number)
    - [Scheduling the Report to Run Now or Later](#scheduling-the-report-to-run-now-or-later)
  - [Using the Report Toolbar](#using-the-report-toolbar)
  - [Exporting Reports to Other Media](#exporting-reports-to-other-media)
  - [Printing Reports](#printing-reports)
- [# Chapter 5 – Ad Hoc Reports](#chapter-5-ad-hoc-reports)
  - [Display Resolution](#display-resolution)
  - [Definitions](#definitions)
  - [Building a Report Query](#building-a-report-query)
    - [Creating the Query—Defining Fields](#creating-the-querydefining-fields)
    - [Creating Filters](#creating-filters)
    - [Creating Filters Based on Is Not Null](#creating-filters-based-on-is-not-null)
    - [Creating Filters based on Between](#creating-filters-based-on-between)
    - [Creating Filters Based on a List](#creating-filters-based-on-a-list)
  - [The Report Design Toolbar](#the-report-design-toolbar)
  - [Designing the Report](#designing-the-report)
    - [Rearranging objects in the report](#rearranging-objects-in-the-report)
    - [Adding a new column to the report](#adding-a-new-column-to-the-report)
    - [Other ways to add a column](#other-ways-to-add-a-column)
    - [Deleting a column from the report](#deleting-a-column-from-the-report)
    - [Changing a column heading](#changing-a-column-heading)
    - [Grouping and sorting objects in the report](#grouping-and-sorting-objects-in-the-report)
    - [Keeping section entries together on a page](#keeping-section-entries-together-on-a-page)
    - [Grouping objects within the table](#grouping-objects-within-the-table)
    - [Deleting a section from a report](#deleting-a-section-from-a-report)
    - [Displaying long text fields](#displaying-long-text-fields)
    - [Adding a Header and Footer](#adding-a-header-and-footer)
    - [Adding a Report Title](#adding-a-report-title)
    - [Adding Page Numbers](#adding-page-numbers)
    - [Adding a prompt for date range](#adding-a-prompt-for-date-range)
  - [Adding Subtotals and Totals](#adding-subtotals-and-totals)
    - [Subtotals - Count the number of Issue Codes within a Date of Contact](#subtotals-count-the-number-of-issue-codes-within-a-date-of-contact)
  - [Saving a Report to your PC](#saving-a-report-to-your-pc)
  - [508 Compliance](#508-compliance)
  - [Sharing Reports with other Advocates](#sharing-reports-with-other-advocates)
    - [Moving Reports to the Public Folder](#moving-reports-to-the-public-folder)
    - [Using a Reports from the Public Folder](#using-a-reports-from-the-public-folder)
- [# Chapter 6 - Maintenance (Patient Advocates & VPACs)](#chapter-6-maintenance-patient-advocates-vpacs)
  - [Managing Congressional Contacts](#managing-congressional-contacts)
  - [Managing Hospital Locations](#managing-hospital-locations)
  - [Managing Comps](#managing-comps)
  - [Managing Boilerplate Resolution Text](#managing-boilerplate-resolution-text)
  - [Managing Facility Service or Section](#managing-facility-service-or-section)
- [Chapter 7 – Maintenance (NPO)](#chapter-7-maintenance-npo)
  - [Managing Issue Categories](#managing-issue-categories)
  - [Managing Issue Codes](#managing-issue-codes)
  - [Managing Methods of Contact](#managing-methods-of-contact)
  - [Managing Treatment Status](#managing-treatment-status)
  - [Managing Contacting Entities](#managing-contacting-entities)
  - [Changing the Number of Days for All ROCs to Become Overdue](#changing-the-number-of-days-for-all-rocs-to-become-overdue)
- [# Appendix A: Informational and Action Request Notifications](#appendix-a-informational-and-action-request-notifications)
    - [Sample Email to send to Notification Recipients:](#sample-email-to-send-to-notification-recipients)
- [# Appendix B: Ad Hoc Tutorial](#appendix-b-ad-hoc-tutorial)
  - [Display Resolution](#display-resolution-1)
  - [Scenario \#1: Building a Report Query](#scenario-1-building-a-report-query)
  - [Scenario \#2: Creating Filters and Prompts](#scenario-2-creating-filters-and-prompts)
  - [Scenario \#3: Deleting a column from the report](#scenario-3-deleting-a-column-from-the-report)
  - [Scenario \#4: Creating sections – Group the data by Institution](#scenario-4-creating-sections-group-the-data-by-institution)
  - [Scenario \#5: Breaking by Location – Another way to group data](#scenario-5-breaking-by-location-another-way-to-group-data)
  - [Scenario \#6: Creating sections – another way to group the data by Location](#scenario-6-creating-sections-another-way-to-group-the-data-by-location)
  - [Scenario \#7: Adding a field to an existing report](#scenario-7-adding-a-field-to-an-existing-report)
  - [Scenario \#8: Subtotals - Count the number of Issue codes within a Location](#scenario-8-subtotals-count-the-number-of-issue-codes-within-a-location)
  - [Scenario \#9: Grand Totals - Count the total number of issue codes](#scenario-9-grand-totals-count-the-total-number-of-issue-codes)
  - [Scenario \#10: Add a title and page numbers](#scenario-10-add-a-title-and-page-numbers)
- [## Scenario \#11: Displaying long text fields](#scenario-11-displaying-long-text-fields)
  - [Scenario \#12: The report design toolbar](#scenario-12-the-report-design-toolbar)
  - [Scenario \#13: Save a report to your PC](#scenario-13-save-a-report-to-your-pc)
  - [Scenario \#14: Saving a public report](#scenario-14-saving-a-public-report)
  - [Scenario \#15: Change a column heading](#scenario-15-change-a-column-heading)
  - [Scenario \#16: Removing a section from a report](#scenario-16-removing-a-section-from-a-report)
  - [Scenario \#17: Filter based on a list (Contacting entity)](#scenario-17-filter-based-on-a-list-contacting-entity)
  - [Scenario \#18: Move captions to the left hand side of the data (508c)](#scenario-18-move-captions-to-the-left-hand-side-of-the-data-508c)
- [# Appendix C: Ad Hoc Report Totals](#appendix-c-ad-hoc-report-totals)
- [Index](#index)
*Introduction*
The Patient Advocate Tracking System (PATS) is a web-based system used to document, track, and report patient-related issues. PATS replaces the legacy Patient Representative (Patient Rep) system. The Patient Advocacy Database (PAD) servlet extends PATS functionality by allowing a Report of Contact (ROC) to be created and sent to PATS from the Inquiry Routing and Information System (IRIS).
*The Patient Advocate Tracking System User Guide* is intended for all users of the PATS application (see the section entitled *What Users Should Read*). The guide provides step-by-step instructions for using PATS.

### Chapter Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table outlines how the user guide is organized.
<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 32%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Chapter</th>
<th>Title</th>
<th>Provides…</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>PATS Overview</td>
<td>An introduction to the PATS.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Creating a Report of Contact (ROC)</td>
<td>Instructions for creating a new Report of Contact (ROC) and description of the automatic ROC creation through the IRIS-PAD interface.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Editing a Saved ROC</td>
<td>Instructions for finding an ROC, adding or changing information in an existing ROC, and closing an open ROC.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Standard Reports</td>
<td>Instructions for creating, viewing, printing, and saving standard reports.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Ad Hoc Reports</td>
<td>Instructions for creating a report query, limiting data by creating filters, and designing the report.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Maintenance – Patient Advocates and VPACs<br />
(VISN Patient Advocate Coordinators)</td>
<td>Instructions for managing user access to the system and adding or changing Congressional contacts, hospital locations, comps, and facility services or sections.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Maintenance – National Program Office (NPO)</td>
<td>Instructions for NPO users to change information used throughout the system: issue categories, issue codes, methods of contact, treatment statuses, contacting entities, and ROC expiration days.</td>
</tr>
<tr class="even">
<td>Appendix A</td>
<td>Informational and Action Request Notifications</td>
<td>Sample email for Advocates to send to recipients of notifications explaining how to view and respond to the notification.</td>
</tr>
<tr class="odd">
<td>Appendix B</td>
<td>Ad Hoc Tutorial</td>
<td>Tutorial from Ad Hoc UAT for creating a report query, creating filters, and designing the report.</td>
</tr>
<tr class="even">
<td>Appendix C</td>
<td>Ad Hoc Totals</td>
<td>Information on how to count Issues when creating Ad Hoc reports.</td>
</tr>
</tbody>
</table>

### What Users Should Read

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below summarizes the sections that each user group should read.
| User Group                     | Read Chapters/Sections             |
|--------------------------------|------------------------------------|
| Patient Advocates              | Chapters 1 – 5, Sections 6.1 – 6.4 |
| Site Information Takers        | Chapters 1 & 2, Sections 3.1 – 3.5 |
| National Program Office Users  | Chapters 1 & 7                     |
| VISN Level Advocates           | Chapters 1 – 6                     |
| Employees (involved in issues) | Chapter 1, Section 3.7.2           |
| Central Office                 | Chapter 4                          |

### Naming Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the naming conventions used in this guide for pages and items in the Patient Advocate Tracking System (PATS).
- The first page you see when accessing PATS is the *PATS Login page*.
> ![](pats-user-guide/002.png)
- After you log onto PATS, the *PATS Main page* displays.
> ![](pats-user-guide/003.png)
- Each user role that accesses PATS has its own set of options on the *PATSMain page.* For example, the *PATSMain page* for Patient Advocates (above) has different options than the *PATS Main pag*e for the National Program Office (below).
> ![](pats-user-guide/004.png)
- On the left-hand side of the PATS Main page is the *Menu bar*. The *Menu bar* provides links to navigate through PATS.
> ![](pats-user-guide/005.png)
- In some parts of the application you will see a box followed by a down arrow ![](pats-user-guide/006.png).  
  When you click on the down-arrow, a *Drop-down list* of selectable items displays.
> ![](pats-user-guide/007.png)
> ![](pats-user-guide/008.png)
*Other Resources*
Additional PATS documentation resources are listed in the table.
<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>For information about…</strong></td>
<td><strong>See the…</strong></td>
</tr>
<tr class="even">
<td>Completing tasks using PATS</td>
<td>PATS Online Help</td>
</tr>
<tr class="odd">
<td>Installing PATS</td>
<td><em>PATS Installation Guide for EIE Staff<br />
PATS Installation Guide for IRM Staff</em></td>
</tr>
<tr class="even">
<td>Migrating data from Patient Representative to PATS</td>
<td><em>PATS Data Migration Guide</em></td>
</tr>
<tr class="odd">
<td>Technical details about PATS</td>
<td><em>PATS Systems Management Guide</em></td>
</tr>
<tr class="even">
<td>IRIS UI Inquiry Details</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

# Chapter 1 - PATS Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Advocate Tracking System (PATS) is a web-based application with a centralized database and notification function (email) for tracking patient-related issues. PATS is designed to work on various operating systems (e.g., Windows 2000, Windows XP, Linux).

PATS enables users to perform the following tasks:

- Add a Report of Contact (ROC) which details a Veteran’s issue (compliment or complaint).
- Edit, close, reopen, and delete an ROC.
- Send Informational Notifications to communicate an issue to an employee involved in a Report of Contact and/or the employee’s supervisor.
- Send Action Request Notifications, which require a response from the individual regarding action to be taken or next steps.
- Generate site-specific and National reports.
- Create ad hoc reports.
- Display reports online and save them in a variety of formats (i.e., Word, Excel, PDF files).

PATS automatically rolls up data to the VISN Support Service Center (VSSC) to provide additional National reports.

National Program Office and Patient Advocates can add and change (update, activate, and inactivate) PATS table-reference data (e.g., Hospital Location).

PATS includes online help pages that you can access from the menu or directly from each page within the application.

The PAD application extends the functionality of PATS by allowing the creation of a ROC in PATS from information transferred from IRIS. PAD does not change the PATS User Interface; however, Patient Advocates will see new ROCs that have been automatically generated as a result of this additional functionality.

## Logging onto PATS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To log onto PATS:

1.  Access the PATS application at the link provided by the Program Implementation Office.

Result: The PATS Login page displays.

> **NOTE:** The first time you log into PATS, you need to indicate the Institution you want to access. You can display the Institution drop-down list by Station Number or Station Name by selecting the appropriate radio button. The next time you log onto PATS, the Login page will display the Institution you selected.

![](pats-user-guide/009.png)

2\. If you want to sort the Institution list by Institution number, select the Sort by Station Number radio button.

If you want to sort the Institution list by Institution name, select the Sort by Station Name radio button.

3\. Enter your VistA access code.

4\. Enter your VistA verify code.

5\. Select the Institution you want to access from the drop-down list.

> Note: NPO users will sign on to their local Institution; however, they will have access to data report for ALL institutions.

6\. Click Login.

Result: The PATS Main page displays.

## Setting up an Icon on the Desktop

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set up an icon on your desktop as a shortcut to access PATS:

1\. Click on the website URL provided by the Program Implementation Office to go to the PATS Login page.

2\. Right click anywhere on the Login page.

Result: A dialogue box with a list of actions displays.

3\. Select Create Shortcut.

Result: A dialogue box displays with the message that a shortcut will be placed on your desktop.

4\. Click OK to confirm.

Result: A shortcut displays on the desktop.

![](pats-user-guide/010.png)

## User Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must enter your email address in order to receive responses to PATS Action Request Notifications (ARNs). The User Settings page allows you to enter:

- Your email address
- Set your preference to display summary information for expired ARNs on the PATS Main page.
- Enter your phone number for NPO reports
- Generate 508 accessible reports.

You can change these settings at any time by clicking User Settings on the Menu bar.

To set/change your settings:

1\. On the PATS Main page, click User Settings.

Result: The User Settings page displays.

2\. Email Address: Click the Enter Default button for the system to automatically enter your VA address or enter it manually.

![](pats-user-guide/011.png)

3\. Display Expired Action Request Notifications on Main Page (*optional)*: Select/deselect the checkbox to display/not display summary information for expired ARNs on the PATS Main page.

4\. Contact Phone Number *(optional)*: Enter your area code and phone number. The contact number will display on National reports. You can enter multiple phone numbers. This field is a text box, so you can enter extension information or other relevant text.

5\. Generate 508c Accessible Reports *(optional)*: If you check this box, all standard reports will be generated specifically for screen readers (508 compliant).

6\. Click Save.

## Timing Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PATS Application

For security reasons, PATS application times out after a certain amount of time if the user is inactive. Previously this value was set to 20 minutes (and that is still the value an application ships with), starting with the version 1.0.1.x of a PATS application this value can be adjusted by the centralized server administrator to accommodate for specific site needs.

The newly introduced Session Timeout warning feature is designed to do the following:

- Provide a warning to the user of a pending timeout.
- Provide an option to reset the timeout without navigating away from the page of interest or losing any unsaved data.
- Provide a countdown timer for the response, allowing the user to finish a train of thought and respond in time. Should the timeout occur, present an option to save data

Timeout warning prompt appears at the three-quarters of a preconfigured session timeout. In other words if a session timeout is configured at 20 minutes, the box will appear at a 15 minute mark, allowing 5 minutes for the user to respond.

![](pats-user-guide/012.png)

There are two possible outcomes of the prompt. You can extend your session timer by clicking OK or let it expire. Upon clicking OK you will get a “Your session was updated successfully!” message. The prompt then disappears.

![](pats-user-guide/013.png)

If you or failed to respond to the prompt in time, the message on the box changes once the countdown timer reaches zero.

![](pats-user-guide/014.png)

If you navigate to any page after the Session Timeout warning prompt was expired, you will get a Suspended due to inactivity error message. In that case, save any uncommitted text to a temporary text file or a clipboard, close the browser and then log onto PATS again.

![](pats-user-guide/015.png)

Ad Hoc Reporting

The Session Timeout warning functionality applies to Ad Hoc reporting as well, even though Ad Hoc reporting tool is being a separate application. If a report takes a while to compete, respond to the warning prompt in time and your session will be extended, allowing an application to finish its processing.

<span id="_1.5_Using_the" class="anchor"></span>

## Using the Calendar Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Calendar icons provide a shortcut for entering a date or date ranges. When searching for an ROC by date range, a “From” date is required.

To use the Calendar icons to enter a date:

1\. Click the Calendar icon.

2\. Click ≤ or ≥ as needed to select a month and year.

3\. Click the day of the month.

4\. If you have a range of dates: Repeat steps 1 – 3 for the “To date.”

> Note: If the calendar does not display when you click the icon, minimize any open windows to see if the calendar is open. Close the calendar and return to PATS.

## Entering Required Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Required fields are indicated by a red asterisk (\*). You must enter information in that field before you can continue to the next page, tab, or exit the PATS application. If you forget to enter required information, an error message displays indicating the data you need to enter.

![](pats-user-guide/016.png)

## Using Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PATS provides online help to assist users to complete tasks. The Online Help page is accessible by selecting Help from the menu bar. This page includes a table of contents which displays information by subject. To view subtopics, click the top-level entries. When you are finished, click the ![](pats-user-guide/017.png) at the top right corner to close the page and return to the PATS Main page.

![](pats-user-guide/018.png)

When you’re in the application and have a question about how to complete a task or what to enter in a specific field, click the Help icon at the top right of the page ![](pats-user-guide/019.png).

![](pats-user-guide/020.png)

Help information specific to the page you’re on displays.

## Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ONLY use the blue buttons and links on the pages in PATS to move within the application. If you use the Back or Forward buttons on the browser toolbar, you may get unexpected results.

When you are in the edit mode and change or modify information, the Menu bar is inactivated (dark blue without an underline). This prevents your moving to another function without saving the work. Once you save or cancel your changes, you can navigate within PATS by using the Menu bar.

When the menu is active (bright blue), use the menu options to navigate PATS. When the menu is inactive (dark blue), use the Cancel button to reactivate the menu bar.

# Chapter 2 - Creating a Report of Contact 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Report of Contact (ROC) includes describing all the details of a complaint or compliment reported by a patient or visitor, along with information about the resolution of the issue.

In this Chapter

The table lists the topics covered in this chapter.

|                                                         |                                   |
|---------------------------------------------------------|-----------------------------------|
| <span id="_Ref43803812" class="anchor"></span>Topic | Page                          |
| 2.1 Creating a New ROC                                  | [13](#_Ref43803812)               |
| 2.2 Adding Contact Information                          | [14](#_Toc41373059)               |
| 2.3 Adding Patient Information                          | [15](#adding-patient-information) |
| 2.4 Adding Issue Text                                   | [17](#adding-issue-text)          |
| 2.5 Automatic ROC Creation                              | 15                                |

## Creating a New ROC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Creating an ROC involves the following tasks:

1\. Click NewROC on the PATS menu bar.

2\. Add contact information (Cover Sheet page).

3\. Add patient information, if applicable (Patient page).

4\. Enter a description of the issue (Issue Text page).

5\. View summary information for the ROC (Summary page).

6\. Save the ROC.

> **NOTE:** You must complete steps 1-5 before you can save a new ROC.

<span id="_Toc41373059" class="anchor"></span>

## Adding Contact Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add contact information:

1\. On the PATS menu bar, click New ROC.

Result: The Add Report of Contact – Cover Sheet displays.

![](pats-user-guide/021.png)

2\. Dateof Contact (required): Populated with a default date, which is the current date. Verify that the date of contact is correct; if not, enter the correct date.

> Note: You can enter a date in mm/dd/yyyy format or click the calendar icon and select a date. Future dates are not allowed.

3\. Info Taken By *(required)*: Populated with a default value, the name of the person who logged into the session. Verify the name is correct; if not, select the appropriate name from the drop-down list.

4\. Contacting Entities *(required)*: Click the check boxes to select as many contacts as appropriate.

5\. Method of Contact *(optional)*: Click the check boxes to select as many methods of contact as appropriate.

6\. Congressional Contact: If you selected Congressional as a Contacting Entity, select a Congressional Contact from the drop-down list.

> Note: You can enter the Congressional Contact now, or when you edit the ROC.

7\. Phone/Fax (for contacting entities):

a\. Enter a Name or Description and Number (up to 50 characters each) in the appropriate boxes and click Add.

b\. Verify the information. To change information, click Edit. To delete all the information, click Delete.

c\. You can enter multiple Names or Descriptions (e.g., home phone, cell, fax) and Numbers (repeat Steps 7a and 7b).

![](pats-user-guide/022.png)

8\. Click the Patient tab to continue adding the ROC.

## Adding Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROC you are creating may or may not involve a patient. If the ROC doesn’t involve a patient, mark the appropriate Treatment Status (defaults to “no patient associated”). If a patient is involved, you add the patient name using the Person Service Lookup tool, and then indicate the treatment status.

![](pats-user-guide/023.png)

If the ROC does not involve a patient:

1.  Treatment Status: Defaults to “No Patient Associated.”

2\. Click the Issue Text tab to continue.

If the ROC involves a patient:

1\. Patient Name: Click Search.

Result: The Patient Lookup screen displays. Patient Lookup is part of the Person Service Lookup tool.

![](pats-user-guide/024.png)

2\. Limit Patient Selection by: You can search for the patient by name or by using filters: inpatient provider, ward, clinic.

> Note: For more information about using the Person Service Lookup tool, review the *PSL IR4 User Manual (Web-based)* in the Project Artifacts section at the following site: <span class="mark">REDACTED</span>

> Select Patient: Enter the Patient name in ‘Last, First middle’ format in upper or lower case.

Result: The Patient Lookup Status Notification box displays (several boxes may display).

![](pats-user-guide/025.png)

3\. Click Continue.

Result: The Patient Details page displays with Patient demographics.

> **NOTE:** If you click Cancel, you must choose another patient.

To handle Status Notification dialogue boxes, refer to the *PSL IR4 User Manual (Web-based),* section on Acknowledging Status Notifications.

4\. Treatment Status: Select the appropriate treatment status. Once a patient is selected you cannot select a Treatment Status of “No Patient Associated” or “Undetermined – IRIS”

5\. Click the Issue Text tab to continue.

## Adding Issue Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can enter up to 4,000 characters (including spaces) to explain a problem, issue, comment, or compliment. Input is limited to letters, numbers, and punctuation characters.

To add issue text:

1\. Click the Issue Text tab.

Result: The Issue Text page displays.

2\. Briefly Describe the Issue: Briefly describe the problem, issue, comment, or compliment (4,000 characters including spaces).

> **NOTE:** The system does not accept HTML commands. If you enter “\<” followed by “\>” (i.e., \< *any text* \>), the text appears to contain HTML. Delete brackets \< and \>.

![](pats-user-guide/026.png)

3\. Click the Summary tab and review the information.

![](pats-user-guide/027.png)

> Note: The Summary page is the first page that the Save button displays. You must enter information on the Cover, Patient, and Issue Text pages before you can save an ROC.

4\. Click Save.

Result: A dialogue box displays asking if you want to add the Report of Contact.

5\. To add the ROC, click OK.

Result: A confirmation page displays with the ROC number and the Date of Contact.

> Note: The ROC number is the division number followed by a period, the fiscal year, and 5 digits. For example: 442.200600011.

![](pats-user-guide/028.png)

6\. Click Edit this ROC to send notifications, add other information (issue code, employee involved), or make changes to the ROC you just created. (See *Chapter 3, Editing a Saved ROC*.)

OR

Click an available option on the menu bar.

## Automatic ROC Creation through the PAD interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Advocacy Database (PAD) project is implemented as an extension to current PATS functionality and allows the Inquiry Routing and Information System (IRIS) to send new ROCs to the PATS application through an automated interface that requires no user input. Patient Advocates using the IRIS system will transmit new or existing veteran inquiries to PATS in order to generate a new Report of Contact.

The following indicators describe how to identify a ROC that was automatically created through the IRIS-PAD interface

- Method of Contact = “IRIS”
  - This value indicates that the contact inquiry was originally sent to the IRIS system, which then forwarded the inquiry to PATS to create a ROC.
- Treatment Status = “Undetermined – IRIS”
  - This value indicates that the primary contact listed in the inquiry could not be automatically identified in PATS during ROC creation.
  - The PATS user/Patient Advocate needs to research the issue text description and attempt to manually search for an identified patient using the Edit ROC Search functionality.
  - If the patient was automatically identified during ROC creation, the Treatment Status will be set to “Outpatient”
- Issue Description is prepopulated with standard fields in the headline
  - The ROC issue description text field will always have the following standard format when a ROC was automatically generated
    - IRIS \#:130326-000004 (Phone: 111-222-3456) Contact is Veteran VetAddress:123 Fake Street, Denver, Colorado, United States, 80916 VetEmail:ioc@test.REDACTED
    - The actual description of the issue will follow the standard information fields above
- Information Taken By = “IRIS, SYSTEM”
  - This field identifies the user that created the ROC
  - This may be useful when creating reports or searching for all ROCs generated by the automated interface

    IRIS can send a maximum of 8000 characters in the ROC Issue Text. PAD will prepend Veteran contact information to the IRIS Issue Text received and store the first 4000 characters in the PATS Issue Description and any remaining text in the PATS Resolution Text. If there is any text automatically entered into PATS Resolution Text then the PATS Issue Description will be appended with the following overflow message ‘\[CONTINUED IN RESOLUTION TEXT\]’.

> **NOTE:** The following screen shot shows how the prepended Veteran Information is displayed.

![](pats-user-guide/029.png)

> **NOTE:** The following screen shot shows where the Issue Text overflow message is displayed.

![](pats-user-guide/030.png)

What do I do with these ROCs?

Once the ROC is transmitted to PATS and stored, there is no functional or implicit difference in the way PATS users will view, edit, or otherwise interact with the data. The ROCs that are automatically created should be treated the same as all manually entered ROCs through normal PATS business rules. See Chapter 3 for instructions on how to edit a previously created ROC.

# Chapter 3 - Editing a Saved ROC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Report of Contact (ROC) includes describing all the details of a complaint or compliment reported by a patient or visitor, along with information about the resolution of the issue. After you create and save an ROC, you can:

1\. Change Information

- Contact information
- Patient information
- Issue text

2\. Update Issue Details

- Add, Change, and Remove Issue Codes
- Add, Change, and Remove Facility Service or Section, Employee Involved, and Hospital Location associated with an Issue Code

3\. Send/View Notifications

- Send an Informational Notification (IN) or Action Request Notification (ARN)
- View an Informational or Action Request Notification
- Respond to an ARN
- Modify an ARN

4\. Resolve Issues

- Add resolution information: copy ARN thread to the Resolution Text box, enter Resolution text, select a comp, if applicable
- Close an ROC

In this Chapter

The table lists the topics covered in this chapter.

|                                                            |                                                               |
|------------------------------------------------------------|---------------------------------------------------------------|
| Topic                                                  | Page                                                      |
| 3.1 Finding an ROC                                         | [22](#finding-an-roc)                                         |
| 3.2 Listing an ROC                                         | [25](#listing-an-roc)                                         |
| 3.3 Updating Contact Information                           | [26](#updating-contact-information)                           |
| 3.4 Changing Patient Information                           | [27](#changing-patient-information)                           |
| 3.5 Changing Issue Text                                    | [29](#_Toc41373066)                                           |
| 3.6 Sending Informational Notifications                    | [29](#_Add,_edit_or)                                          |
| 3.7 Sending Action Request Notifications                   | [32](#sending-action-request-notifications)                   |
| 3.8 Adding, Changing, Removing Issue Codes                 | [39](#adding-changing-removing-issue-codes)                   |
| 3.9 Adding and Removing an Employee from an Existing Issue | [41](#adding-and-removing-an-employee-from-an-existing-issue) |
| 3.10 Closing an ROC                                        | 40                                                            |
| 3.11 Reopening a Closed ROC                                | [46](#reopening-a-closed-roc)                                 |
| 3.12 Deleting an ROC                                       | [47](#deleting-an-roc)                                        |

## Finding an ROC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add or change information in an ROC, the first step is to locate the ROC in the PATS database. One way to select a ROC for editing is by using the Edit ROC option from the main menu. From Edit ROC, you can search by:

- Patient name
- Date range
- Employee involved
- Information taker
- ROC number

*Note:See Section 3.2 to find an ROC by listing your open ROCs or all open ROCs.*

![](pats-user-guide/031.png)

3.1.1 Search by Patient Name

1\. Click Edit ROC on the menu bar.

2\. Click Patient Search.

3\. Limit Patient Search by: You can search for the patient by name or by using filters: input provider, ward, and clinic.

Select Patient: Enter the patient’s name in ‘Last, First Middle’ format. After selecting the patient, a list of open ROCs displays for that patient.

> Note: For detailed information about using the Person Service Lookup tool, review the *PSL User Manual (Web-based)* in the Project Artifacts section at the following site: <span class="mark">REDACTED</span>.

4\. From the results list, locate the appropriate ROC and click Edit. To display the details of the ROC, click View.

5\. Add or change information using the procedures in this chapter (sections 3.3 – 3.12)*.*

3.1.2 Search by Date Range

1\. Click Edit ROC on the menu bar.

2\. From Date, To Date: Enter search parameters (“from date” and “to date”) in the appropriate boxes in mm/dd/yyyy format or use the calendar icons.

> Note: You can use the calendar icons to select dates. The “From” date must be populated. If you leave the “To” date blank, the search will extend through the current date.

3\. Click Search.

4\. From the results list, locate the appropriate ROC and click Edit. To display the details of the ROC, click View.

5\. Make your changes using the procedures in this chapter (sections 3.3 – 3.12)*.*

3.1.3 Search by Employee Involved

1\. Click Edit ROC on the menu bar.

2\. Employee Involved:Last Name: Enter at least two characters of the employee's last name.

First Name: Enter at least one character of the employee’s first name.

> Note: To limit the search results, enter as much of the employee’s name as possible.

3\. Click Search.

4\. Click Select to select an employee from the results list.

5\. From the results list, locate the appropriate ROC and click Edit. To review the details of the ROC, click View.

6\. Make your changes using the procedures in this chapter (sections 3.3 – 3.12)*.*

3.1.4 Search by Information Taker

> 1\. Click Edit ROC on the menu bar.

2\. Information Taker:

- To search for ROCs related to the default Information Taker (person who logged into PATS), click Search.
- To search for ROCs for a different Information Taker, click the drop-down arrow and select the appropriate individual. Click Search.

3\. From the results list, locate the appropriate ROC and click Edit. To display the details for an ROC, click View.

4\. Make your changes using the procedures in this chapter (sections 3.3 – 3.12)*.*

3.1.5 Search by ROC Number

1\. Click Edit ROC on the menu bar.

2\. ROC Number: Enter the first few digits of the ROC number

> Note: The convention for ROC numbers is *Division Number.yyyynnnnn*. The Division number is pre-populated. To limit your search results, enter as many digits as possible.

3\. Click Search.

4\. From the results list, locate the ROC and click Edit. If the list is long, click View All. To display the details for an ROC, click View.

5\. Make your changes using the procedures in this chapter (sections 3.3 – 3.12)*.*

## Listing an ROC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add or change information in an ROC, the first step is to locate the ROC in the PATS database. You can also search by:

- Your open ROCs (you are the information taker)
- All open ROCs (ROCs for all patient advocates in the Institution)

3.2.1 Search by Your Open ROCs

1\. Click List ROCs on the menu bar.

Result: The List of Open Reports of Contact page displays.

> ![](pats-user-guide/032.png)

2\. From the results list, locate the appropriate ROC and click Edit. To display the details for an ROC, click View.

3\. Make your changes using the procedures in this chapter (sections 3.3 – 3.12)*.*

3.2.2 Search by All Open ROCs

1\. Click List ROCs on the menu bar.

Result: The List of Open Reports of Contact page displays.

2\. Click the All Open ROCs tab.

3\. From the results list, locate the appropriate ROC and click Edit. To display the details for an ROC, click View.

4\. Make your changes using the procedures in this chapter (sections 3.3 – 3.12)*.  
*

## Updating Contact Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change any contact information on the Cover Sheet of a saved ROC.

![](pats-user-guide/033.png)

To change contact information:

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. On the Cover Sheet tab, you can change the following information:

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>If you want to change...</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Then...</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Date of Contact</p>
</blockquote></td>
<td><p>Highlight the date and enter the new date in the box in mm/dd/yyyy format. Or, click the calendar icon and select a date. Future dates are not allowed.</p>
<p><strong>If the ROC number contains 2007 or any prior year:</strong></p>
<blockquote>
<p>You can change the Date of Contact within either calendar year or fiscal year (for ROC 110.200600011, you can change the date of contact within the calendar year 1/1/2006 – 12/31/2006 or the fiscal year 10/1/2005 – 9/30/2006).</p>
</blockquote>
<p><strong>If the ROC number contains 2008 or any year after:</strong></p>
<blockquote>
<p>You can change the Date of Contact only within the fiscal year (for ROC 110.200800023 dates allowed are between 10/1/2007 – 9/30/2008).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Information Taker's name</p>
</blockquote></td>
<td>Select a name from the drop-down list.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Contacting Entities</p>
</blockquote></td>
<td>Check the appropriate boxes to select or clear as many <strong>Contacting Entities</strong> as apply.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Methods of Contact</p>
</blockquote></td>
<td>Check the appropriate boxes to select or clear as many <strong>Methods<br />
of Contact</strong> as apply.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Congressional Contact</p>
</blockquote></td>
<td><p>Available only if you checked Congressional contacting entity.</p>
<p>Select the appropriate name from the drop-down list, if applicable.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Phone/Fax</p>
</blockquote></td>
<td><blockquote>
<p><strong>Note:</strong> To delete the Name/Description and Number, click <strong>Delete</strong>.</p>
</blockquote>
<ol type="a">
<li><p>Click <strong>Edit</strong>.</p></li>
<li><p>Change the description and phone number as needed.</p></li>
</ol>
<blockquote>
<p><strong>Note:</strong> You can enter up to 50 characters, including spaces, for the description and the phone number.</p>
</blockquote>
<ol start="3" type="a">
<li><p>Click <strong>Update</strong>.</p></li>
</ol>
<blockquote>
<p><strong>Note:</strong> To add another name/phone number, enter the information and click <strong>Add</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

3\. To continue editing the ROC, click Save and then click another tab.

4\. When you’re finished editing this ROC, click Save and Exit.

## Changing Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three options for changing patient information:

- Changing the patient that is attached to the ROC
- Deleting a patient from the ROC
- Automatically updating PATS information on this patient to match the patient’s information in VistA (such as eligibility status)

3.4.1 Changing the patient attached to this ROC

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Patient tab.

3\. Click Change.

4\. You can search for the patient by name or by using filters: input provider, ward, clinic.

> Note: For detailed information about using the Person Service Lookup tool, review the *PSL User Manual (Web-based)* in the Project Artifacts section at the following site: <span class="mark">REDACTED</span>

5\. Locate the patient in the results list and click on the name.

6\. If a Patient Lookup Status Notification displays, press Continue.

> **NOTE:** If you press Cancel, the results list displays; you can select a new patient.

7\. To continue editing the ROC, click Save and then click another tab.

If you’re finished editing this ROC, click Save and Exit.

3.4.2 Deleting the patient from this ROC

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Patient tab.

3\. Click Remove.

4\. Change Treatment Status to No Patient Associated.

5\. To continue editing the ROC, click Save and then click another tab.

If you’re finished editing this ROC, click Save and Exit.

3.4.3 Updating the patient information from VistA

This action refreshes all of the patient data in PATS with the current information from the VistA PATIENT file.

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Patient tab.

3\. Click Update.

4\. To continue editing the ROC, click Save and then click another tab.

If you’re finished editing this ROC, click Save and Exit.

<span id="_Toc41373066" class="anchor"></span>

## Changing Issue Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change issue text:

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. On the Issue Text tab, edit the text as necessary.

> Note: You can enter a maximum of 4,000 characters including spaces. The system does not accept HTML commands. If you enter “\<” followed by “\>” (i.e., \< *any text* \>), the text appears to contain HTML. Delete brackets \< and \>.

<span id="_Add,_edit_or" class="anchor"></span>3. To continue editing the ROC, click Save and then click another tab.

If you’re finished editing this ROC, click Save and Exit.

## Sending Informational Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have saved an ROC, you can send a notification to the employee involved and/or the employee’s supervisor. The Patient Rep system used VistA mail to send alert notifications to employees regarding patient complaints. The PATS application uses Outlook to send notifications.

There are two types of notifications:

- Informational Notification (IN): information only; no action or response from recipients
- Action Request Notification (ARN): a response is required from the recipient

You can send an informational notification to multiple recipients. Adding a person to receive a notification is a two step process: first the PATS application verifies the person exists in the local VistA system, and then PATS verifies that the person has an email address in Exchange (MS Outlook).

When you send a notification, the recipient receives an email with a link to PATS and the notification. The recipient must log into PATS to read the notification. When a recipient has read the notification, PATS automatically logs the date in the ROC.

3.6.1 Adding an Informational Notification

To add an informational notification (no action or response is required):

1\. If necessary, find the ROC. ( See page [22](#finding-an-roc).)

2\. Click the Notifications tab.

![](pats-user-guide/034.png)

3\. Informational Notifications: Click the New button.

4\. Click Search to be prompted for the names of the recipients you want to send the notification to.

5\. Last Name: Enter at least two characters of the last name.

6\. First Name: Enter at least one character of the recipient’s first name.

7\. Click Search to find all entries on the VistA NEW PERSON file that match your lookup criteria.

> Note: PATS searches the VistA New Person File.

8\. On the *Search Results* list, locate the recipient and click Select.

> Note: PATS searches the Microsoft Outlook file for the individual.

9\. On the *List of possible email matches found*, click Select next to the appropriate name.

> Note: If the error message ‘No suitable matches found in Exchange’ displays, the recipient is not in the Global Address List. This means that an IN can’t be sent to this person.

> Result: The List of Recipients displays with the recipient’s email address.

> ![](pats-user-guide/035.png)

10\. To send the Informational Notification to more than one recipient, repeat steps 5 – 9.

Result: PATS displays a List of Recipients containing the names of each recipient you have requested to receive the IN.

11\. Click the Continue button after building the list of all recipients of the IN.

Result: New Informational Notification page displays.

12\. Click the Send button to send the IN to the recipients.

> **NOTE:** You can remove recipients from the list prior to sending the IN by clicking Remove next to the recipient’s name. You may also add more names to the list by clicking Search.

13\. To continue editing the ROC, click Save and then click another tab.

> If you’re finished editing this ROC, click Save and Exit.

3.6.2 Viewing an Informational Notification

An Informational Notification (IN) is sent to the recipient’s VA email address with a link. The person must have valid VistA access and verify codes for the site to view informational notifications.

> **NOTE:** Since the PATS application uses Outlook rather than VistA to send notifications, you might want to explain to recipients what to do when they receive a notification. (See Appendix A for a sample email that you can send to recipients of an Informational Notification.)

To view an informational notification:

1\. Click the link in the email message or copy and paste it in the Address bar of your browser.

> ![](pats-user-guide/036.png)

> Result: The PATS Logon page displays.

2\. Log onto PATS by selecting the division indicated in the email message and entering your Institution access and verify codes.

> Result: The View Informational Notification page displays.

> ![](pats-user-guide/037.png)

3\. After you view the notification, click <u>Log off</u>.

## Sending Action Request Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have saved a ROC, you can send a notification to the employee involved and/or the supervisor. The Patient Rep system used VistA mail to send alert notifications to employees regarding patient complaints. The PATS application uses Outlook to send notifications.

An Action Request Notification (ARN) requires a response from the recipient within 7 days. Unlike informational notifications, an action request notification can only be sent to one person.

Adding a person to receive a notification is a two step process: first PATS verifies the person exists in the local VistA system, and then PATS verifies that the person has an email address in Exchange (MS Outlook).

When you send a notification, the recipient receives an email with a link. The recipient must log into PATS to read the notification. When the recipient responds, the Patient Advocate receives an email that includes a link to PATS.

3.7.1 Sending an Action Request Notification

To add an Action Request Notification (a response is required):

1\. If necessary, find the ROC. ( See page [22](#finding-an-roc).)

2\. Click the Notifications tab.

![](pats-user-guide/038.png)

3\. Action Request Notifications: Click the New button.

4\. Click Search to find the recipient you want to send the notification to.

> Note: For an ARN, you can only select onerecipient per email.

5\. Last Name: Enter at least two characters of the last name.

First Name: Enter at least one character of the recipient’s first name, and click Search.

> Note: PATS searches the VistA New Person File.

6\. On the *Search Results* list, locate the recipient and click Select.

> Note: PATS searches the Microsoft Outlook file for the individual.

7\. On the *List of possible email matches found*, click Select next to the appropriate name.

> Note: If the error message ‘No suitable matches found in Exchange’ displays, the recipient is not in the Global Address List. This means that an ARN can’t be sent to this person.

> Result: The New Action Request Notification page displays.

> ![](pats-user-guide/039.png)

8\. Number of Default Days to Respond: You can accept the default of 7 days for the recipient to respond to the ARN or change the response time (1-6 days) using the drop-down list.

9\. Add Comment: Enter text you want the recipient of the ARN to receive and respond to.

10\. Click Send.

Result: The page that shows the list of current INs and ARNs for this ROC displays with a confirmation that the notification in green.

> **NOTE:** When you click the Send button, ARN comments are saved and the notification is sent. If you press the Cancel button later when working with this ROC, that doesn’t change the fact that the notification was sent. Any other changes on this ROC are discarded.

11\. To continue editing the ROC, click Save and then click another tab.

> If you’re finished editing this ROC, click Save and Exit.

  
3.7.2 Employee Response to an Action Request Notification

When an Action Request Notification (ARN) is sent, the employee receives an email with a link to PATS and the notification. A response is expected between 1 - 7 days (set by the sender) from the date the notification was sent.

> **NOTE:** Since the PATS application uses Outlook rather than VistA to send notifications, you might want to explain to recipients what to do when they receive a notification. (See Appendix A for a sample email that you can send to recipients of an Action Request Notification).

To respond to an Action Request Notification, the employee:

1\. Clicks the link in the email message.

> ![](pats-user-guide/040.png)

> Result: The PATS Logon page displays.

2\. Logs onto PATS by selecting the division indicated in the email message and entering their Institution access and verify codes.

> Result: The View Action Request Notification page displays.

![](pats-user-guide/041.png)

3\. Add Comment: Enters a response to the notification.

![](pats-user-guide/042.png)

4\. Clicks Add.

> *Result: Your comment is added to the Additional Comments section and a message displays at the top of the page: “The advocate has been notified that a comment has been added. Your comment is displayed below. You may close the browser.”*

5\. After the comments display in the Additional Comments section, the employee clicks <u>Log off</u>.

3.7.3 Receiving the Response to an Action Request Notification (Patient Advocate)

When an individual responds to an ARN, the originator receives an email with a link to PATS and the View Notification page. Depending on the nature of the response, you may want to respond back.

To receive/respond to an Action Request Notification:

1\. Click the link in your email message.

> ![](pats-user-guide/043.png)

> Result: The PATS Logon page displays.

2\. Log onto PATS using your Institution access and verify codes.

> Result: The View Action Request Notification page displays.

3\. Review the response to the ARN.

4\. Add Comment: Enter your response to the notification.

> If you want the employee to read the new response, leave the Notify Employee option selected. Otherwise, de-select the Notify Employee box.

> Note: When you de-select the Notify Employee box, the employee is not sent an email notification. However, the employee can still view your latest comment if the employee clicks on the email notification link they previously received. Do not enter sensitive or delicate comments that you do not want the employee to read.

5\. Click Done.

> Result: The advocate is brought into the ROC in edit mode on the Notifications tab.

3.7.4 Modifying an Action Request Notification

When a Patient Advocate clicks on the link in an ARN response from the recipient or when they select notifications while editing a ROC, they can modify an existing Action Request Notification (ARN) for an ROC.

Turn to the next page…

![](pats-user-guide/044.png)

To modify an ARN:

1\. On the View Action Request Notification page, do any of the following:

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>If you want to...</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Then...</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Change the expiration date of the Action Request Notification</p>
</blockquote></td>
<td><ol type="a">
<li><blockquote>
<p>Select a different number from the drop-down list.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Apply</strong>.</p>
</blockquote></li>
</ol>
<p>Result: The Expiration Date changes.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Add a comment to an Action Request Notification</p>
</blockquote></td>
<td><ol type="a">
<li><blockquote>
<p>Enter the comment in the box.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Add</strong>.</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Close the Action Request and flag it as completed.</p>
</blockquote></td>
<td><blockquote>
<p>Click <strong>Mark as Complete</strong>.</p>
</blockquote>
<p>Result: ARN Status is Complete.</p>
<blockquote>
<p><strong>Note:</strong> This affects only the displayed Action Request. See the instructions for closing an open ROC.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Notify an employee that a comment has been added to a notification.</p>
</blockquote></td>
<td><p><strong>Note:</strong> Depending on your user role, this option may not be available to you.</p>
<blockquote>
<p>Click <strong>Notify Employee</strong> to send an email to the employee with additional comments.</p>
</blockquote></td>
</tr>
</tbody>
</table>

2\. Click Done.

Result: If a new comment was added and the Notify Employee box is checked, a new mail message is sent to the recipient.

> Note: When you de-select the Notify Employee box, the employee is not sent an email notification. However, the employee can still view your latest comment if the employee clicks on the email notification link they previously received Do not enter sensitive or delicate comments that you do not want the employee to read.

## Adding, Changing, Removing Issue Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can add, change, and remove issue codes for a ROC, along with the associated Facility Service or Section, Employee Involved, and Hospital Location.

<span id="_Adding_Issue_Codes" class="anchor"></span>3.8.1 Adding Issue Codes and Associated Information

To add an issue code:

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Resolution tab.

3\. Click the New Issue button.

> Result: The Edit Report of Contact – ROC Issue Details screen displays.

4\. Issue Code: If you know the issue code, enter the 4-character code.

> Result: When you move to the next field, the issue description displays.

> ![](pats-user-guide/045.png)

5\. Issue Category: If you don’t know the issue code,

1.  Select the appropriate category from the Issue Category drop-down list.

> Result: A list of available issue codes displays.

2.  Select an issue code from the list (for a definition of the code, click View).

> Result: The issue code and description displays in the Issue code box.

> ![](pats-user-guide/046.png)

6\. Hospital Location (*optional)*: Select a Hospital Location from the drop-down list.

7\. Facility Service or Section *(required)*: Select a Facility Service or Section from the drop-down list.

8\. Add Employee Involved *(optional)*: Click Add Employee Involved to add an employee to the ROC. ([How?](#adding-and-removing-an-employee-from-an-existing-issue) See page [41](#adding-and-removing-an-employee-from-an-existing-issue).).

9\. Click Add.

> Result: The Edit Report of Contact – Resolution page displays. Issue Code information displays in the ROC Issue Details field.

> ![](pats-user-guide/047.png)

10. If you’re finished editing this ROC, click Save and Exit.
11. To continue editing the ROC, click Save.
- To add another issue detail, follow Steps 3 – 9.
- To edit other information, click the appropriate tab.

3.8.2 Changing Issue Codes

To change an issue code:

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Resolution tab.

3\. Find the applicable issue code in the ROC Issue Detail section and click Edit.

> Result: The Edit Report of Contact – ROC Issue Details displays.

4\. Issue Code: If you know the new issue code, highlight the current code in the box and enter the new code over it.

> Result: When you move to another field, the issue description displays.

5\. Issue Category: If you don’t know the new issue code,

1.  Select the appropriate category from the Issue Category drop-down list.

> Result: A list of available issue codes displays.

2.  Select an issue code from the list (for more details, click View).

> Result: The issue code and description displays in the Issue code box.

6\. Click OK.

> Result: The Edit Report of Contact screen displays with the revised ROC Issue details.

7\. To continue editing the ROC, click Save and then click another tab.

If you’re finished editing this ROC, click Save and Exit.

3.8.3 Removing Issue Codes

To remove an issue code:

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Resolution tab.

3\. Find the Issue Code you want to delete and click Remove.

> Result: The ROC Issue Details are deleted.

4\. To continue editing the ROC, click Save and then click another tab.

If you’re finished editing this ROC, click Save and Exit.

## Adding and Removing an Employee from an Existing Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a specific employee is involved in an issue, you can add (or remove) the employee’s name in PATS.

3.9.1 Adding an Employee Involved

To add an employee involved:

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Resolution tab.

![](pats-user-guide/048.png)

3\. Select an issue (there may be more than one issue listed) and click Edit.

4\. Click Add Employee Involved.

5\. Enter at least 2 characters of the employee's last name and first name.

> Note: To narrow your search, enter the entire last name and at least two letters of the first name.

6\. Click Search.

> Result: A list of Search Results displays.

7\. Locate the employee's name in the list and click Select.

> Result: The Employee Involved list displays.

> Note: To add another employee, repeat Steps 5-7. (When you enter information in the Search box, the previous employee’s name remains in the list.)

8\. Click Continue.

9\. Click OK.

> Result: The employee’s name is added to the ROC Issue Details section.

> ![](pats-user-guide/049.png)

10\. To continue editing the ROC, click Save and then click another tab.

> If you’re finished editing this ROC, click Save and Exit.

3.9.2 Removing an Employee Involved

To remove an employee involved:

One employee involved in an issue:

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Resolution tab.

3\. Find the issue that involves the employee you want to remove and click Edit.

> **NOTE:** If you click Remove instead of Edit, you remove the entire Issue Code rather than just the employee involved.

4\. In the Employee Involved List, click Remove next to the appropriate employee’s name.

5\. Click OK.

6\. To continue editing the ROC, click Save and then click another tab.

> If you’re finished editing this ROC, click Save and Exit.

More than one employee involved in an issue:

1\. If necessary, find the saved ROC. ( See page [22](#finding-an-roc).)

2\. Click the Resolution tab.

3\. Find the issue that involves the employee you want to remove and click Remove.

4\. Click OK.

5\. To continue editing the ROC, click Save and then click another tab.

> If you’re finished editing this ROC, click Save and Exit.

## Closing an ROC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to closing an ROC, you need to assign at least one issue code to the report and select a facility service or section. When closing an ROC you are required to enter a closing date. You can also automatically copy comments from Action Requests Notifications (ARNs) and save them with the ROC.

To enter the resolution information and close the ROC:

1\. Find the ROC to close ( See page [22](#finding-an-roc).)

2\. Click the Resolution tab.

3\. If you’ve entered an Issue code for the ROC, go to Step 4.

If you haven’t added an Issue code:

1.  Click New Issue to add an issue code. ( See page [39](#_Adding_Issue_Codes).)
2.  Facility Service or Section *(required)*: Select a facility service or section from the drop-down list.
3.  Hospital Location *(optional)*: Select a Hospital Location from the drop-down list.
4.  Employee Involved *(optional)*: Enter an Employee Involved. ( See page [41](#adding-and-removing-an-employee-from-an-existing-issue).)
5.  Click Add.
4.    
    Describe the Resolution: Enter how the issue was resolved. You can enter up to 8,000 characters (including spaces).
- If you want to copy ARN comments into the Resolution text, click the Copy button next to the ARN.
- If you have boilerplate resolution text associated with an Issue Code, you will see a Copy button next to the Issue. Press the button to copy the boilerplate resolution text into the Resolution text for this ROC.

> **NOTE:** The system does not accept HTML commands. If you enter “\<” followed by “\>” (i.e., \< *any text* \>), the text appears to contain HTML. Delete brackets \< and \>.

| ![](pats-user-guide/050.png) | *Any ARN comments associated with the ROC that you don’t copy to the description box will be permanently deleted from PATS when you close the ROC.* |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|

![](pats-user-guide/051.png)

5\. If applicable, select any of the following:

1.  Select a Comp from the drop-down list.
2.  To set an internal appeal flag for the ROC, click the Clinical Appeal button.

6\. Date of Closing: Enter the date in mm/dd/yyyy format or use the calendar icon ([How?](#_1.5_Using_the) See page [10](#_1.5_Using_the)).

> Note: To automatically enter today's date and close the ROC, click Close ROC.

7\. Click Close ROC.

Result: The Confirmation: ROC Closed screen displays.

![](pats-user-guide/052.png)

## Reopening a Closed ROC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system allows you to reopen a ROC that was previously closed. Any ARNs associated with a closed ROC are no longer available. Only ARNs copied to the Resolution text are available when you reopen an ROC.

To reopen a closed ROC:

1\. Click Reopen ROC on the menu bar.

2\. Find the ROC to reopen. ( See page [22](#finding-an-roc).)

3\. Locate the closed ROC on the results list and click Reopen.

4\. Click OK.

Result: ROC is reopened and the Edit Report of Contact – Cover Sheet displays.

> Note: If you need more information to identify the correct ROC to reopen, click the View button to display more details about the ROC.

![](pats-user-guide/053.png)

5\. You can do the following

a\. Edit the ROC information. ([How?](#updating-contact-information) See the procedures beginning on page [26](#updating-contact-information).)

b\. To close the ROC, click the Resolution tab and the Close ROC button.

c\. To return to the PATS Main page, click Save & Exit.

## Deleting an ROC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can delete an ROC. However once you delete an ROC, you can no longer access it.

To delete an ROC:

1\. Click Delete ROC on the menu bar.

Result: The Find a Report of Contact page displays.

2\. Find the ROC to delete. ( See page [22](#finding-an-roc).)

3\. Locate the ROC on the results list and click Delete.

> Note: If you want to view more information about the ROC to confirm it is the correct one to delete, click the View button to display the ROC.

4\. A pop-up window appears asking if you want to delete the ROC.

> Warning: Once you delete an ROC, you can’t reopen it.

5.  Click OK to confirm. Click Cancel to leave the ROC open.

# # Chapter 4 – Standard Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three types of reports capture PATS application data: standard reports (referred to as “application site” reports in Patient Rep), spreadsheet reports, and ad hoc reports. Reports are only available to Patient Advocates; Site Information Takers do not have access to this feature. The menu bar on the PATS Main page has folders that contain the reports. The folders are organized according to report categories and are in alphabetical order. Spreadsheet reports are included in the applicable folder and are identified in the report title and description (for example: Spreadsheet – Issue Count by Division).

Because of differing information needs, Patient Advocates and the National Program Office (NPO) have access to different reports.

Patient Advocate reports are divided into the following categories:

- Employee
- Facility Service or Section
- Issue Code
- Patient
- Report of Contact

  NPO and Central Office users have access to National Reports.

> **NOTE:** NPO users will sign on to their local Institution; however, they will have access to reports of data for ALL institutions.

In this Chapter

The table lists the topics covered in this chapter.

|                                           |                                             |
|-------------------------------------------|---------------------------------------------|
| Topic                                 | Page                                    |
| 4.1 Understanding Terminology/Conventions | [50](#understanding-terminologyconventions) |
| 4.2 Scheduling Reports                    | [53](#scheduling-reports)                   |
| 4.3 Entering Selection Criteria           | [54](#entering-selection-criteria)          |
| 4.4 Using the Report Toolbar              | [57](#_Ref121896373)                        |
| 4.5 Exporting Reports to Other Media      | [58](#exporting-reports-to-other-media)     |
| 4.6 Printing Reports                      | [60](#printing-reports)                     |

## Understanding Terminology/Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains terminology and conventions used in PATS Reports. A Summary table at the end of this section has definitions of these important terms.

- The *menu bar* on the PATS Main page lists folders for the *five report categories*: Employee, Facility Service or Section, Issue code, Patient, Report of Contact.

> ![](pats-user-guide/054.png)

- When you click on a report category (for example, Employee), the *Reports Folder page* displays.

> ![](pats-user-guide/055.png)

> The *Reports Folder page* lists all the reports in that particular category with a description of the report Purpose, User Input, Sorted By, and Detail Report Items.

- When you click Schedule, the *Schedule Report page* displays.

> ![](pats-user-guide/056.png)

> ![](pats-user-guide/057.png)

- Once the scheduled report has run, the *Reports Folder page* will display a *View Latest Instance button*.

  ![](pats-user-guide/058.png)
- Click View Latest Instance to display the last report you scheduled for this particular report title.
- When you click the Report title or the History button, the *Report Details page* displays.

> ![](pats-user-guide/059.png)

> The *Report Details page* displays the report description and *Report Instances*—a list of the last three reports that you have run (scheduled). You can View the report or Delete it from the list, Schedule a report, or go Back to the Report Folder page.

### Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below summarizes Report terminology/conventions:

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Report Category</th>
<th><p><strong>Patient Advocates Reports:</strong> There are five report categories on the menu bar: Employee, Facility Service or Section, Issue code, Patient, Report of Contact.</p>
<p><strong>NPO Reports:</strong> National</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Report Folder page</td>
<td>Lists all the reports in the category with a description of the report <strong>Purpose, User Input, Sorted By, and Detail Report Items</strong>.</td>
</tr>
<tr class="even">
<td>Report Instances</td>
<td>A list of the last 6 reports that you have run (scheduled).</td>
</tr>
<tr class="odd">
<td>History button</td>
<td>Displays the Report Details page which gives the report description and Report Instances.</td>
</tr>
<tr class="even">
<td>Schedule button</td>
<td>Displays the page where you can select report parameters.</td>
</tr>
<tr class="odd">
<td>View Latest Instance button</td>
<td>Displays the last report you scheduled for a particular report title.</td>
</tr>
</tbody>
</table>

## Scheduling Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PATS application allows you to schedule just the reports you need when you need them. You can schedule a report to run immediately or later. If you schedule a report in the future, make a note to “pick up” the report when it’s ready.

> **NOTE:** *When you add an ROC, the data will not be included on reports until the next day.* A batch job is run every night to refresh the data in the report tables.

To schedule a report to run, you perform the following tasks:

1\. Select a *report category* from the menu bar on the PATS Main page.

- Patient Advocates: Employee, Facility Service or Section, Issue code, Patient, Report of Contact
- NPO: National

2\. Select the report from the list on the Report Folder page.

3\. Enter selection criteria: Date Range, Division (one or All), Employee Involved, Facility Service or Section, Schedule to run now or later (select date and time).

4\. If you scheduled the report to run Now: On the Report Details page, click Refresh until the status reads “Success.”

> Note: For reports you schedule to run at a later time, complete this step at the appropriate date and time.

5\. View the report. (Optionally, view the latest instance of the report.)

6\. *Optional features:* Export the report to Acrobat format (PDF), MS Word, MS Excel 97-2000, MS Excel 97-2000 (data only), Rich text format. You can also print the report.

## Entering Selection Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on the report you want to run, you can enter selection criteria that controls the data that is returned. For most reports you select a date range, division(s) covered, and whether to run the report now or later. This section explains each of the sort options.

The selection criteria you are prompted to enter depends on the report category you choose:

- Date Range
- Division (one or All)
- Employee Involved
- Facility Service or Section
- Patient
- ROC number
- Information Taker
- Schedule to run now or later (select date and time)

### Selecting the Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To schedule a report, you select the dates the report will cover from the drop-down lists or the Calendar icons. *Data is available for reports for the current fiscal year and two previous fiscal years.*

> Note: Be sure to select the radio button next to the date range you want to use.

> ![](pats-user-guide/060.png)

- Monthly: Select the month and calendar year.
- Quarterly: Select the quarter and the fiscal year (October 1 – September 30).
- Semi-Annual: Select the two quarters and the fiscal year.
- Fiscal year: October 1 – September 30.
- Selectable: Use the Calendar icons to select the date range. Though you can select a calendar that goes back several years (for example, 2002), data is only available for the current fiscal year and the previous fiscal year.

### Selecting the Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To schedule a report, you select the division(s) whose data you want to show in the report. If you have access to multiple divisions within your computing facility, you will see a drop-down list of divisions.

> 1\. Use the default to select all divisions to which you have access (INCLUDE ALL).

> 2\. Scroll down then left-click to select a single division.

> 3\. To select multiple divisions, select the first division, hold the Ctrl key and left click to select other divisions; or hold the Shift key and left click to select a range of divisions.

### Selecting the Employee Involved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Enter at least two characters of the Employee’s last name and optionally at least the first letter of the first name and click Search.

> Note: The more characters you enter, the easier it is to locate the employee involved.

> ![](pats-user-guide/061.png)

> Results: The Employee Search Results page displays.

> 2\. Find the employee in the list and click Select.

### Selecting the Facility Service or Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a Facility Service or Section from the drop-down list or leave blank to include ALL.

### Selecting the Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. To select a patient, enter one of the following search criteria:

- Patient’s last name, first name
- Patient’s social security number (SSN)
- First character of the patient’s last name following by the last 4 digits of the SSN

> ![](pats-user-guide/062.png)

2\. Click Patient Search.

> Result: Patient Search Results page displays a list of patients that meet the search criteria with the patient name, ICN, SSN, station, date of birth, gender.

3\. Find the appropriate patient and click Select.

> Result: The patient’s name displays on the Select Report page.

> ![](pats-user-guide/063.png)

### Selecting the ROC number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the 12-digit ROC Number (to find an ROC number, see page [22](#finding-an-roc)).

### Scheduling the Report to Run Now or Later

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can schedule a report to run immediately or later. If you schedule a report to run later, you must indicate the:

- time you want the report to run (hour and minutes, AM or PM)
- date using the calendar icon or in mm/dd/yyyy format

| ![](pats-user-guide/064.png) | When you schedule a report to run later, you must convert the time you want the report to run into Eastern time (because the location of the report server is in Falling Waters, VA, which is in the Eastern time zone). For example, if you want the report to run at 8:00 am Pacific Time, you need to schedule it for 11:00 am. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref121896373" class="anchor"></span>

## Using the Report Toolbar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you’ve scheduled and refreshed the report, you can view it on the Report Instance Display page. This section explains report features and toolbar icons.

![](pats-user-guide/065.png)

1 2 3 4 5 6 7 8 9

| Icon                | Comments                                                                                                                                               |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 Show/hide group tree  | Show/hide report groups such as the Divisions in the report. Select a level in the hierarchy to move to the corresponding level in the body of the report. |
| 2 Export this report    | Export the report to Acrobat format (PDF), MS Word, MS Excel 97-2000, MS Excel 97-2000 (data only), or Rich text format.                                   |
| 3 Print this report     | You have the option to open the PDF file or save it to your computer.                                                                                      |
| 4 Move to the beginning | Move to the first page of the report.                                                                                                                      |
| 5 Move backward         | Move back in the report one page at a time.                                                                                                                |
| 6 Move forward          | Move forward in the report one page at a time.                                                                                                             |
| 7 Move to the end       | Move to the last page of the report.                                                                                                                       |
| 8 Go to page            | Enter a page number and click the arrow.                                                                                                                   |
| 9 Zoom feature          | Pull the drop-down list to change the size of the view (25% to 400%).                                                                                      |

| ![](pats-user-guide/066.png) | If you use Internet Explorer as your browser, you may be unable to use the Export or Print option to display, print or save a standard report in a format such as PDF or Microsoft Word. If these options don’t work on your PC, the problem can be addressed by *letting your local Internet Explorer session know that the PATS application server is a trusted site*. If you do not have access or do not feel comfortable performing these steps, you can ask your local IRM staff to help. |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Complete the following steps to add the EIE server running PATS to your list of trusted servers:

1.  Log onto PATS.
2.  From the top toolbar, select Tools\>Internet Options.
3.  Select the Security tab.
4.  Highlight Local intranet.
5.  Press the Sites button.
6.  Press the Advanced button.
7.  In the blank box labeled “Add this Web site to the zone,” enter:  [http://vaww.pats.med.REDACTED](http://vaww.pats.med.va.gov)
8.  Press Add.

> *Result: The server should appear in the box labeled “Web sites:”*

9.  Press OK until you are out of the Tools option.
10. Use the Log Off option to log out of PATS.
11. Press the link that says “Close this window” to close the browser.
12. Log into PATS to activate the new Internet Explorer settings.

## Exporting Reports to Other Media

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can export reports to other media for the purpose of saving the report, printing the report, or preparing spreadsheets. PATS allows you to export reports to:

- Acrobat Format (PDF)
- MS Word
- MS Excel 97-2000
- MS Excel 97-2000 (data only): use this option to export spreadsheet/graphs
- Rich text format

To export reports:

1\. Click the envelope with the arrow icon.

> ![](pats-user-guide/067.png)

Result: The Export Options pop-up window displays.

![](pats-user-guide/068.png)

2\. Click the Formats drop-down list and highlight the desired export format.

![](pats-user-guide/069.png)

3\. Indicate the report pages you want to export: All or specific pages.

4\. Click OK.

Result: A dialogue box displays asking if you want to Open or Save the file.

5\. Click Open (open the report file) or Save (save the file to your computer).

*Optionally* you can print the file, email it to another Patient Advocate, or prepare a spreadsheet in Excel.

## Printing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Click the printer icon.

> ![](pats-user-guide/070.png)

Result: A pop-up window displays asking if you want to open or save the document.

2\. Click Open.

Result: The report in PDF format displays.

3\. Select File\>Print.

4\. Complete the Print screen (select Printer, Properties).

5\. Click OK.

# # Chapter 5 – Ad Hoc Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### *Overview*

The Ad Hoc report feature lets you create a report to your own specifications. You decide what data is included in the report and how the report looks. The ad hoc reporting tool is Business Objects software called WebIntelligence (WEBI for short) and has been incorporated in the PATS application. For additional information on creating Ad Hoc reports, see *Appendix B, Ad Hoc Tutorial*.

There are two parts to building an ad hoc report—the report query and the report design.

> 1\. The Query: The query allows you to select the data that you want available for the report. When you add a new report, the first thing you do is define the query. Some of the things you might do in the query are:

- Define which fields will be included in the report from the available list of fields.
- Define rules for filtering or limiting the data that is returned. For example, the filter rule could be “to return only Reports of Contact (ROCs) with a contacting entity of Congressional.”
- Define input parameters for filtering the data by adding a prompt such as a date range for Date of Contact. Each time the report is run, the user is prompted to enter a date range, so the same report can be used from month to month.

> 2\. The Design: After you have created a query, you will design your report. This means that you define the look and feel of the report. Some of the things you might do are:

- Decide which fields to display on the report
- Group or sort data by various fields
- Create and display formulas based on the available fields
- Add counts and other calculations
- Change fonts and color
- Add page headings and page numbers

In this Chapter

The table lists the topics covered in this chapter.

|                                          |                                             |
|------------------------------------------|---------------------------------------------|
| Topic                                | Page                                    |
| 5.1 Display Resolution                   | [62](#display-resolution)                   |
| 5.2 Definitions                          | [62](#definitions)                          |
| 5.3 Building a Report Query              | [64](#building-a-report-query)              |
| 5.4 The Report Design Toolbar            | [73](#the-report-design-toolbar)            |
| 5.5 Designing the Report                 | [74](#designing-the-report)                 |
| 5.6 Adding Subtotals and Totals          | [87](#adding-subtotals-and-totals)          |
| 5.7 Saving a Report to your PC           | [89](#saving-a-report-to-your-pc)           |
| 5.8 508 Compliance                       | [90](#compliance)                           |
| 5.9 Sharing Reports with other Advocates | [90](#sharing-reports-with-other-advocates) |

## Display Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you use the Ad Hoc reporting tool, if the right side of your display is cut off, you may need to increase the resolution on your screen monitor.

To change the screen resolution, complete the following:

1.  At the bottom left of your screen, click Start\>Control Panel\>Display.
2.  Select the Settings tab.
3.  In the Screen resolution box, move the arrow to the right to increase the resolution.

> ![](pats-user-guide/071.png)

4.  Click Apply (if you also want to change the font size) or click OK.

To display a larger font size:

1.  Select the Appearance tab.
2.  Under Font size, select the Large fonts or Extra large fonts.
3.  Click OK.

> **NOTE:** When you’re working in the Ad Hoc tool, if your screen doesn’t look the same as the *User Guide*, check your screen resolution.

## Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Universe

On the left side of the screen, you will see a familiar list of data items or fields, with the word Universe above them. Business Objects uses the word Universe to mean the group of data items (referred to as “objects” in WEBI) that is available to build your report. The Universe is a list of all the fields in PATS. It is equivalent to the list of fields you see in the Print Fields and Sort Fields lists in the current Patient Rep ad hoc report option.

Some of the object names are preceded by a plus sign (+). The plus sign indicates that there are additional objects available within the object name. Click the plus sign to display the additional objects.

![](pats-user-guide/072.png)

Objects

Business Objects uses the word object to represent the data items that are available from the Universe to build your report. This is equivalent to field names in the Patient Rep system.

Panes

A pane represents something like a window pane or frame; it is also referred to as a panel.

When you open the ad hoc tool to create a new report, you will see the Query page. The Query page contains three panes:

- Universe: On the left side of the Ad Hoc Reporting page, you’ll see the Universe object pane that was discussed above. It contains a list of all the fields in PATS.
- Result Objects: On the top right, you’ll see the Result Objects pane. The objects that you select for your report are displayed in this pane (like the sort fields and print fields you select when building an ad hoc report in Patient Rep).
-   
  > Query Filters: On the bottom right, you’ll see the Query Filters pane. This is where you define rules that limit the records returned to your report. (This is similar to putting starting and ending values for a sort field when building an ad hoc report in Patient Rep.)

Cell

A cell is a rectangular block within the report, containing a single piece of data. When you’re designing a report, each piece of data is displayed in a cell.

Table

The main body of most reports contains rows and columns of data cells. This main block of data is referred to as the table.Toolbar

The toolbar at the top of the Query page allows you to take certain actions while building the query. You will probably use two of the buttons on the Query toolbar.

- Run Query – Once you have selected the fields for your report and created any filters to limit the data, you will click the Run Query button. The system reads data from the database that meets the criteria you defined while building the query, and it puts you into the report design mode, where you can refine the look and feel of your report.
- Cancel – If you start running a query and it’s taking a long time or you change your mind, you can use the Cancel button to stop the query.

![](pats-user-guide/073.png)

For information about the other toolbar buttons, refer to the Business Objects manual for queries in TSPR (Background/Supporting Documents section), *[Ad Hoc Reports: Queries (BOEXI)](http://tspr.vista.med.va.gov/warboard/anotebk.asp?proj=604&Type=Active).*

## Building a Report Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new report, the first thing you do is build the report query—that is, you define the fields you want to include in the report. You can then create filters to limit the data returned within the selected fields. The filter options are explained in this section.

### Creating the Query—Defining Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  On the PATS main menu under Ad Hoc, click the Private link.

> *Result: A list of your current private reports displays.*

2.  Click the Add button.

> *Result: The Ad Hoc Reporting page displays.*

![](pats-user-guide/074.png)

3.  To define the objects that you want in your report query, you move objects from the Universe pane to the Result Objects pane by:
- Double-clicking the object name, or
- Highlighting the object and click the \>\> arrow next to the Result Objects pane.

> Note: Once objects are in the Result Objects pane, you can use the arrows () () to change the order of the fields when WEBI builds that initial report. You can remove objects from the Result Objects pane by highlighting the object and pressing the \<\< arrow.

> The Quick Filter button ( ![](pats-user-guide/075.png) ) allows you to build a simple query filter; however, it has not been found to be very useful).

4.  Click Run Query.

> *Result: When you run a query for the first time, WEBI automatically sets up a report design to get you started. It contains all of the data you specified in your query.*

5.  Click Save (disc icon next to Insert).

> *Result: A new window opens for the save document information.*

> ![](pats-user-guide/076.png)

> Note: When you’re creating or editing a report, *it’s a good idea to save your work often*. If you’re in the middle of editing a report and you get called away and time out, or if you accidentally click on a link that takes you out of the report, you will lose all of the work you’ve done if you haven’t saved the report.

| ![](pats-user-guide/077.png) | *The ad hoc reporting tool is set to time out after 20 minutes of inactivity; save your work as you make changes.* |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|

6.  Title: Enter the name of the report.
7.  Description (*optional*): Enter a description, so that you can readily identify the report in the list. This is especially important as you create more ad hoc reports.
8.  Location: Although there are several different folders where you can save reports, you should only save to the default Favorites sub-folder of My Folders.
9.  Click OK.

### Creating Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A filter limits the report data that is returned. For example, you might limit:

- Date range for Date of Contact
- Specific values for Contacting entity, Hospital location, or other objects

To create a filter:

1.  If you ran the query, you will be in the report design mode. Click the Editquery button to return to the page that allows you to edit the query.

> If you’re already on the edit query page, go to Step 2.

2.  In the Universe pane on the left, highlight the object you want to limit or filter.
3.  Press the \>\> arrow to the left of the Query Filters pane.

> *Result: The object displays in the Query Filters pane.*

> ![](pats-user-guide/078.png)

4.  Select the Filter radio button.
5.  Click the In List drop-down arrow and highlight the appropriate filter command (see the table below for an explanation of the filter commands).

> ![](pats-user-guide/079.png)

The table explains the filter commands and gives an example of how to use each command.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><br />
Filter Command</strong></th>
<th><strong><br />
Used to return data that is:</strong></th>
<th><strong><br />
Example</strong></th>
<th><strong>Object in Query Filter pane</strong></th>
<th><strong>Filter Value Entry for Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Equal to</td>
<td>equal to a value you specify</td>
<td>Show ROCs with Issue Code equal to EV03</td>
<td>Issue Code</td>
<td>Enter <strong>EV03</strong> in the <strong>Value 1</strong> box</td>
</tr>
<tr class="even">
<td>Not Equal to</td>
<td>different from a value you specify</td>
<td>Show ROCs with any Issue Code except AC09</td>
<td>Issue Code</td>
<td>Enter <strong>AC09</strong> in the <strong>Value 1</strong> box</td>
</tr>
<tr class="odd">
<td>Greater than</td>
<td>greater than the value you specify</td>
<td>Show all ROCs with date of contact after 04/14/2006</td>
<td>Date of Contact</td>
<td>Enter 04/14/2006 in the <strong>Value 1</strong> box</td>
</tr>
<tr class="even">
<td>Greater than or Equal to</td>
<td>greater than or equal to a value you specify</td>
<td>Show ROCs with date of contact on or after 01/01/2006</td>
<td>Date of Contact</td>
<td>Enter 01/01/2006 in the <strong>Value 1</strong> box</td>
</tr>
<tr class="odd">
<td>Less than</td>
<td>lower than a value you specify</td>
<td>Show ROCs with date of contact before 10/01/2005</td>
<td>Date of Contact</td>
<td>Enter 10/01/2005 in the <strong>Value 1</strong> box</td>
</tr>
<tr class="even">
<td>Less than or Equal to</td>
<td>lower than or equal to a value you specify</td>
<td>Show ROCs with date of contact on or before 04/01/2006</td>
<td>Date of Contact</td>
<td>Enter 04/01/2006 in the <strong>Value 1</strong> box</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><br />
Filter Command</strong></th>
<th><strong><br />
Used to return data that is:</strong></th>
<th><strong><br />
Example</strong></th>
<th><strong>Object in Query Filter pane</strong></th>
<th><strong>Filter Value Entry for Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Between</td>
<td>between two values you specify (includes the starting and ending values)</td>
<td>Show Contact Dates on or between 10/01/2005 and 03/31/06</td>
<td>Date of Contact</td>
<td>Enter 10/01/2005 in the <strong>Value 1</strong> box and 03/31/2006 in the <strong>Value 2</strong> box</td>
</tr>
<tr class="even">
<td>Not Between</td>
<td>outside the range of the two values you specify (does not include the starting and ending values)</td>
<td>Show Contact Dates before 01/01/2004 or after 01/01/2005</td>
<td>Date of Contact</td>
<td>Enter 01/01/2004 in the <strong>Value 1</strong> box and 01/01/2005 in the <strong>Value 2</strong> box</td>
</tr>
<tr class="odd">
<td>In List</td>
<td>equal to the values you select from the list</td>
<td>Show Contacting Entities: Patient, friend, relative</td>
<td>Contacting Entity</td>
<td><p><em>Can have multiple values.</em></p>
<p>Use <strong>Values</strong> button to select patient, relative and friend</p></td>
</tr>
<tr class="even">
<td>Not in List</td>
<td>different from the values you select</td>
<td>Show all Methods of Contact except email and Internet</td>
<td>Contacting Entity</td>
<td><p><em>Can have multiple values.</em></p>
<p>Use <strong>Values</strong> button to select email and internet</p></td>
</tr>
<tr class="odd">
<td>Is Null</td>
<td>that doesn’t have a value—is empty</td>
<td>Show all ROCs with no patient</td>
<td>Patient Name</td>
<td>No value required</td>
</tr>
<tr class="even">
<td>Is not Null</td>
<td>only data has a value—isn’t empty</td>
<td>Show only ROCs with at least one Issue Code</td>
<td>Issue Code</td>
<td>No value required</td>
</tr>
<tr class="odd">
<td>Matches pattern</td>
<td>that includes a specific string (use % as a wildcard, i.e., to represent ‘any characters’)</td>
<td>Show only patients whose last name begins with <strong>SMI.</strong></td>
<td>Patient Name</td>
<td>Enter <strong>SMI%</strong> in the <strong>Value 1</strong> box</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><br />
Filter Command</strong></th>
<th><strong><br />
Used to return data that is:</strong></th>
<th><strong><br />
Example</strong></th>
<th><strong>Object in Query Filter pane</strong></th>
<th><strong>Filter Value Entry for Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Different from pattern</td>
<td>that doesn’t include a specific string</td>
<td>Show patients whose last name does not begin with <strong>A.</strong></td>
<td>Patient Name</td>
<td>Enter <strong>A%</strong> in the <strong>Value 1</strong> box</td>
</tr>
<tr class="even">
<td>Both</td>
<td>that corresponds to two values you specify</td>
<td><em>Not applicable to PATS data</em></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Except</td>
<td>that corresponds to one value you specify and does not correspond to another value you specify</td>
<td><em>Not applicable to PATS data</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

6.  Depending on the item you select from the list, you may be prompted to enter data values. This is similar to entering the starting and ending values for a sort field when running a Patient Rep ad hoc report.

> Note: If the object is a date, you can enter the value by using the calendar icon (as described below), or you can enter the value in mm/dd/yyyy format. Only data within the current fiscal year or previous 2 fiscal years is available for ad hoc reports.

> If you are selecting from a list of values, use the Values button to see all the entries available for selection and to select the ones you want.

7.  Click the Update Filter button.

> *Result: The description of your filter in the Query Filters pane changes depending on the type of filter you applied.*

8.  Click the Run Query button.

> *Result: The new report with filters displays.*

9.  Click Save.

### Creating Filters Based on Is Not Null

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to create a filter so only objects with data display. For example, in a report containing Issue Codes, some ROCs may not have Issue Codes. You can create a filter so that only ROCs with Issue Codes display (i.e., filter = Issue Code is not blank/not null).

To create a filter so that no blank object (e.g., Issue codes) displays:

1.  On the Menu bar under Ad Hoc, click the Private link.
2.  Click the Add button.
3.  Create a new report with the following objects:
- ROC Number
- Date of Contact
- Issue Code
4.  In the Universe pane on the left, highlight the object (e.g., Issue Code) and press the \>\> arrow to the left of the Query Filters pane.

> *Result: Issue Code in List displays in the Query Filters pane. This is where the description of your current query filters is displayed.*

5.  At the bottom of the Query Filters pane, click the In List drop-down arrow and highlight Is not Null. Notice that the Filter and Prompt buttons are grayed out.
6.  Click Update Filter.

> *Result: The description of your filter in the Query Filters pane changes to Issue code Is not Null.*

> ![](pats-user-guide/080.png)

5.  Click Run Query.
6.  Click Save.

> Note: Remember to save your report often.

7.  Enter the Title and Description.
8.  Click OK.

### Creating Filters based on Between

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To demonstrate a filter between two values, use the report that was created in section 5.3.3 and put a filter on the Date of Contact. This example shows how you can limit the date range of ROCs that display in the report—that is, you’ll define a start date and an end date for the Date of Contract.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click the EditQuery button.
3.  In the Universe pane on the left, highlight the Date of Contact and press the \>\> arrow to the left of the Query Filters pane.

> *Result: The Issue code Is not Null AND Date of Contact in List displays in the Query Filters pane.*

4.  At the bottom of the Query Filters pane, click the Filter radio button. ![](pats-user-guide/081.png)
5.  Click the In List drop-down arrow and highlight Between.
6.  You can enter the start and end dates in m/d/yyyy format or use the calendar option.
- *Enter dates*
1.  Value 1: Enter the start date in m/d/yyyy format.
2.  Value 2: Enter the end date in m/d/yyyy format.
3.  Go to Step 7.
- *Use the calendar option*

> a\. Click the Values button.

> *Result: The List of Values box displays.*

> b\. In the empty box at the top under List of Values, click the drop-down arrow.

> *Result: A calendar displays.*

> c\. The arrows at the top of the calendar make the following changes:

- Left arrows: month
- Right arrows: year

> Select the appropriate month and year and click the date you want to start (e.g., 01/25/2005) or end (e.g., 01/26/2006).

> ![](pats-user-guide/082.png)

> *  
> Result: The date appears in the box next to the drop-down arrow.*

> ![](pats-user-guide/083.png)

> d\. Press the \>\> arrow next to the blank box under Date of Contact Between.

> *Result: The date displays in the Date of contact Between box.*

> e\. Repeat steps a - c to enter the end date of the date range filter.

> f\. Press the \>\> arrow next to the blank box under And.

> *Result: The date displays in the And box.*

7.  Click OK.

> *Result: Date of Contact between 01/25/2005 and 01/26/06 displays in the Query Filters pane.*

8.  Click Run Query.

> *Result: The report design page displays and you’ll notice that data has been refreshed (re-selected) from the database, based on the date range specified by the new query filter.*

9.  Click Save.

### Creating Filters Based on a List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can limit the data that displays on an Ad hoc report by creating filters based on a list. This means that you can select one or more values from a list (Contacting Entity, Hospital Location, Issue Category, etc.), so that *only* those values display on the report. For example, you could create a filter on Contact Entity to display only congressional ROCs on the report.

To create a filter based on a list:

1.  On the Menu bar under Ad Hoc, click the Private link.
2.  Click the Add button.
3.  Create a new report with the following objects:
- ROC Number
- Patient Name
- Issue Text
- Contacting Entity
4.  Click Run Query.
5.  Click Edit Query.
6.  In the left pane, highlight the object (e.g., Contacting entity) and press the \>\> arrow to move it into Query Filters window in the lower right hand pane.
7.  At the bottom of the Query Filters pane, select the Filter radio button.
8.  Make sure that In List is selected in the drop-down list of possible filter types.
9.  Click the Values button.

> *Result: A window will pop up containing the list of available values (e.g., Contacting Entities).*

10. You can move one or more values into the filter list. Double-click the value (e.g., Congressional) you want to filter on or highlight it and press the \>\> arrow to move it into the right hand pane (e.g., Contacting Entity in List).
11. Click OK.

> *Result: The filter is updated. You should see the description of the filter at the top of the Query Filters pane change to describe the values you selected.*

12. Click Run Query to display the report.

## The Report Design Toolbar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report design toolbar contains the following buttons and drop-down lists:

![](pats-user-guide/084.png)

- Document: Displays actions you can take on the entire document (report).
- Save: Works the same as the Save button.
- Save As: Saves a copy of the report with a different name. (Useful when you want to experiment without changing your original report, or when you want to use an existing report as the basis for a new report.)

| ![](pats-user-guide/085.png) | If you save the report to the Public folder, you must set the Property to Refresh on Open (using Document\>Properties from the toolbar), so that your data is not displayed to other sites. (You may notice that in the screen that prompts for the report title and description, there is a Refresh on Open checkbox, but there is a bug and this will not cause your data to refresh. You must edit the report and use Document\>Properties to set this feature.) |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

- Save to my computer (Excel (open or save an Excel file), PDF (Adobe), CSV (Excel Comma Separated Values file)): Allows you to save the report results in a different format.
- Properties: Displays the document name and description and allows you to set properties.
- View: Controls your local view of the report while editing or viewing the data. Page mode (default), Draft mode (shows the entire report), PDF mode, Left Panel (show or hide), Toolbars (show or hide the formatting, report, or formula toolbar).
- Insert (New row, New column, Break, Filter, Sort, Calculation): Another way of performing actions during report editing rather than using right-click to perform the action.
- Save: The first time you save a report, you’re prompted for a report name and description. After that, the Save button saves the latest changes you’ve made.
- Find: Used to search the report data for a certain value (for example, for a particular Date of Contact).
- Undo: Undo the last change.
- Redo: Reinstates the last change that you undid (undo the undo).
- Pages: Moves you to the first page, back a page, forward a page, last page.
- Edit Query: Changes from report design mode to edit query mode in order to either add or delete a field available to the current report, or to change the filter on the data returned to the report.
- Refresh: Refreshes the data. This re-runs the query using the current query filter values. If there are parameters on the report, you will be prompted for new parameter values.

## Designing the Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you create the query, then you design your report. This means that you define the look and feel of the report. You can do the following:

- Decide which fields to display on the report
- Group or sort data by various fields
- Create and display formulas based on the available fields
- Add counts and other calculations
- Change fonts and color
- Add page headings, page numbers

### Rearranging objects in the report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first time you run the report query, WEBI automatically arranges all of the fields you selected in a report format. You can rearrange the objects in the report at any time to suit your needs. For our example, we’ll use the report that was created in section 5.3.3.

To rearrange objects in the report:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click in any data cell in the report and select Format\>Table.
3.  Select the Pivot tab.

> *Result: The available objects display in the left pane. Buttons with the object/field name display in the Column(s) pane.*

> ![](pats-user-guide/086.png)

4.  In the Columns pane, select the object you want to move.

> *Result: The button becomes gray.*

5.  Use the arrows on the right of the Columns pane to move the object to the left or right in the report.
6.  Click OK.

> *Result: The report displays with the rearranged objects.*

> ![](pats-user-guide/087.png)

7.  Click Save.

### Adding a new column to the report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can add an object (field) to a report after you have run the query. To add a new column, you edit the query so that the field gets pulled from the database when you run the report.

To add a new column:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click Edit Query.
3.  From the Universe pane on the left side, double-click the object you want to add to the report (e.g., Facility Service or Section) or highlight the object and click the \>\> arrow to move it into the Result Objects pane.
4.  Click Run Query.

> *Result: The report design mode displays. Unlike the first time you ran a query on the report, WEBI doesn’t automatically display the field in the report. You won’t see any change in the report.*

> ![](pats-user-guide/088.png)

> Note: The field you added is now available to be added to the report. You will see a list of available objects in the left panel. Then you need to decide where you want the new data to display.

5.  Right click in any data cell in the column to the left (or right) of where you want to place the new column.
6.  Select Insert\>Column\>Right (Insert\>Column\>Left).

> *Result: A blank column displays to the right (or left) of the column you indicated.*

7.  From the left panel, drag the blue box next to the object you’re adding into any blank data cell (not the heading cell).

> *Result: The data displays in the column.*

> ![](pats-user-guide/089.png)

6.  Click Save.

### Other ways to add a column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have an object in the Available Objects pane (Section 5.5.2, steps 1-3), there are two other ways to add a column to the report design.

1.  Highlight the column to the left of where you want to place the new column.
2.  From the toolbar, select Insert\>New column\>Right.
3.  From the left panel (list of Available Objects), drag the blue box next to the object you’re adding into any blank data cell (not the heading cell)
4.  Click Save.

Here’s a third way to add a field to your report design:

1.  Right click anywhere in the data area of the report and select Format\>Table.
2.  Select the Pivot tab.
3.  Move the object (double click the object or highlight the object and click the \>\> arrow) from the list of available objects on the left hand pane into the Columns pane on the right.
4.  Click OK.

> *Result: The new object displays on the report with data.*

5.  Click Save.

### Deleting a column from the report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are many reasons why you might not want to display a column in a report. You might want to use a field in a calculation but not display the field on the report. You might have repetitious information that you don’t want to display. In the report created in section 5.3.5, we added a filter to select only ROCs with a contacting entity of Congressional. Since the report displays the same contacting entity on every line, we could delete the contacting entity column and change the report title to indicate that the report only shows Congressional ROCs.

To delete a column from the report:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click Edit Query.
3.  Right click on a data cell in the column you want to delete.
4.  Select Remove\>Column.

> *Result: The column is deleted from the report, but the data is still available from the query (i.e., the object still displays in the list of Available objects).*

### Changing a column heading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can customize your report by changing the name of any of the column headings.

To change the name of a column heading:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)

    Verify that the Formula toolbar displays. (To display the Formula toolbar, select View\>Toolbars\>Formula.)

> ![](pats-user-guide/090.png)

Highlight the heading of the column you want to edit (e.g., ROC number).

> *Result: The current formula displays in the text box (ex. Highlight the column heading ROC number and you will see in the formula bar, the value =NameOf(\[ROC number\])).*

> ![](pats-user-guide/091.png)

Part of the formula =NameOf( ) indicates the special function used by WEBI to return the name of an object in the universe. The value in the parenthesis is the name of the object whose name is to be returned by the formula. Object names in formulas are surrounded by square brackets.

> Replace the entire heading formula (e.g., *=NameOf(\[ROC number\])* ) with the new heading name (e.g., My ROC).

> ![](pats-user-guide/092.png)

Click the green check mark to apply the change.

> *Result: The column heading displays the new text (e.g., My ROC).*

> ![](pats-user-guide/093.png)

Click Save.

### Grouping and sorting objects in the report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have defined the data you want to display in your report, WEBI displays the data in columns.

> ![](pats-user-guide/094.png)

To make your report more readable and informative, you can group data by creating sections.

To create a section:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click any data cell in the column that you want to use as the section to group data under (e.g., Date of Contact) and select Set as section.

> *Result: Date of Contact (or the object you chose) becomes a section header and groups the other items in a block beneath the header.*

> ![](pats-user-guide/095.png)

3.  You have the option to sort sections to determine the order in which data appears in the report. For example, to sort the report with the most recent date of contact first, right click on the section cell (the date, in the above example) and select Sort\>Descending.

> *Result: The most recent Dates of Contact appear at the top of the report.*

> ![](pats-user-guide/096.png)

> Note: You can click on any data cell and select Sort\>Descending or Sort\>Ascending. Sort\>Ascending sorts from lowest value to highest. It’s the normal sort default for alpha fields, since it sorts from A through Z.

4.  Click Save.

### Keeping section entries together on a page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sometimes the entries in a section will be split between two pages. You can keep all items in a section together on one page, unless the section itself is longer than one page.

To keep items within a section together on the same page:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click to the right of the section data, so that the entire section is highlighted (not just the data cell). In our example, we’d right click to the right side of the Date of Contact.
3.  Select Format\>Section.
4.  Select the Layout Properties tab and check the avoid page breaks in a block box.
5.  Click OK.

> *Result: The report will insert a page break to keep all ROCs within a section on one page. Of course, if there are too many ROCs within the section to fit on a single page, they will be split between two pages.*

6.  Click Save.

### Grouping objects within the table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Suppose you want to group items, but keep them within the table rather than pulling them out as a separate section. To keep the objects in the same table, we will do something that WEBI refers to as breaking on the section (e.g., ROC number).

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click any data cell in the column you want to group the other objects in the table by (e.g., right click on one of the ROC numbers).
3.  Select Break\>Insert to group the other items within the table.

> *Result: Whenever you insert a break on a data cell, WEBI automatically puts a break footer at the end of each unique data value. This is a placeholder for adding subtotals.*

> ![](pats-user-guide/097.png)

4.  Right click a data cell in the column again (e.g., ROC number).
5.  Select Sort\>ascending to sort all of the items within the other objects (e.g., the ROCs within the same Date of Contact by ROC Number).
6.  Click Save.

### Deleting a section from a report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you create a section on a report and later change your mind, you can delete the section. The data no longer displays in the report, but the object is still in the Available Objects list. That means that you have the option to display the object in the report or leave it as.

To delete a section from the report:

> 1\. Right click to the right of the section data, so that the entire section is highlighted—not just the data cell.

> 2\. Click Remove Section.

> *Result: The section headings are deleted. You’ve deleted the section from the report, but object is still part of the query and appears in the Available Object list.*

> 3\. Click Save.

### Displaying long text fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some fields may be very long—for example, Issue text or Resolution test. To display these fields so they are easily read, you can set the width, make the height of the cell variable, and make the text wrap.

1.  Right click in any data cell containing the long text, and select Format\>Cell.

> *Result: The dialogue box to format a cell pops up and opens to the General tab.*

2.  Specify width: Change the value of inches in the box to the desired width for the text cell.
3.  Check the box that says Wrap text.
4.  Uncheck the box that says Specify height.

> *Result: The height of the cell will grow or shrink, depending on the length of the text.*

5.  Click OK.
6.  Click Save.

### Adding a Header and Footer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you can add a title or page numbers to your report, you must create a space for the information. You do this by adding a header and footer.

To add a header and footer:

1.  Right click in a blank area outside the data cells.
2.  Select Format Report.
3.  On the General tab, check the Show header and Show footer boxes.
4.  Enter an amount for the height of the header and footer (i.e., 0.5—you may want to adjust this height; see what works when you print the report).
5.  Click OK.

> Note: There is empty space above and below the data for the header and footer.

6.  Click Save.

### Adding a Report Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you add a title to your report, make sure that you created a header and footer (see Section 5.5.11).

To add a title to the report:

1.  Verify that the left panel displays.

> Note: To display the left pane, click the Show left pane icon (![](pats-user-guide/098.png)) at the top left of the report, or select View\>Left Panel from the toolbar.

2.  Click the drop-down list at the top of the left pane, and select Chart and Table Types.

> *Result: The categories of chart, table, and cell types appear.*

> ![](pats-user-guide/099.png)

> Note: If the Cells category is not visible, click the + next to Report Elements.

3.  Click the + next to Cells.
4.  Click the + next to Formula and Text Cells.
5.  Select the Blank Cell format; drag the white box next to Blank Cell to the header.
6.  Right click in the blank cell.
7.  Select Format\>Cell.
8.  On the General tab in the Name box, enter the title of the report.
9.  If you want the title to appear on every page of the report, click the Layout Properties tab and check the box next to Repeat on every page.
10. You also have the option of changing the font, alignment (*within the cell*: left, center, right), layout (*within the header*), and the border under the title.
11. Click OK.
12. Click Save.

### Adding Page Numbers 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you add page numbers to your report, make sure that you created a header and footer (see Section 5.5.11).

To add page numbers to the report:

1.  In the left panel, click the arrow to the right of the drop-down list box and select Chart and Table Types.
2.  Click the + next to Page number cells and select the type of page number you want to display.

> ![](pats-user-guide/100.png)

3.  Drag the box next to the page-number type to the footer.
4.  Right-click in the page number cell.
5.  Select Format\>Cell.
6.  If you want the word Page to display with the number (e.g., Page 1, Page 2), on the General tab in the Name box, type Page and a space (i.e., Page \[page\]).
7.  You also have the option of changing the font, alignment (*within the cell*: left, center, right), layout (*within the header*), and the border under the page number.
8.  Click OK.
9.  Click Save.

### Adding a prompt for date range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you want to re-use your report and show different subsets of the data each time, you can add a prompt. For example, you can show data within different date ranges.

To add a prompt for date range:

1.  To create a report prompt, you need to be in the query design mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click the Edit Query button.
3.  We’ll add a prompt for Date of contact values. Select the Date of contact object and use the arrows to move it into the Query Filters pane.
4.  From the In List drop-down list, select Between.
5.  Select the prompt radio button.
6.  You can accept the default value for the prompt text, or you can change the prompts (e.g., Starting Date and Ending Date).

> Note: If you want to change the prompt values, enter text in the Prompt 1 box (e.g., Starting Date) and the Prompt 2 box (e.g., Ending Date).).

7.  Click Update Filter.

> *Result: The Date of contact Between prompt (‘Starting Date’) And prompt (‘Ending Date’) displays in the Query Filters pane.*

> ![](pats-user-guide/101.png)

8.  Click Run Query to rerun the query.

> *Result: The Prompts box displays. You must enter a date range before you can run the query. You will notice a list of dates in the lower left hand side of the box. The list of possible values to choose from is not very useful for dates since it is long, but can be useful for lists that have fewer values.*

> ![](pats-user-guide/102.png)

9.  Highlight Starting date at the top of the Prompt box.
10. In the blank box under Starting date (lower right) enter the date in m/d/yyyy format and go to step 12.

> OR

> Click the Starting date drop-down list arrow.

> *Result: A calendar displays.*

11. The arrows at the top of the calendar change the month (left arrows) and year (right arrows). Click the date you want to start.

> *Result: The starting date displays in the box and at the top of the page.*

> ![](pats-user-guide/103.png)

12. Highlight the Ending date at the top of the Prompt box. The heading at the bottom right changes to Ending Date.
13. Enter the date in m/d/yyyy format and go to step 15.

> OR

> Click the Ending date drop-down list on the lower right.

> *Result: A calendar displays.*

14. Select the date you want to end.

> *Result: The ending date displays in the box and at the top of the page.*

> ![](pats-user-guide/104.png)

15. Click Run Query.

> *Result: The report displays only ROCs with a Date of Contact within your selected date range. Now, every time you open this report, you will be prompted for a date range.*

16. Click Save.

## Adding Subtotals and Totals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Designing how to subtotal or total on a given field requires some thought about what to you constitutes an item to be counted. For example, let’s say you have a report with Date of contact, ROC Number, Issue Code and Facility Service or Section (FSoS), and you wish to count the total number of Issues within a Date of contact. One ROC in your result set has the same Issue Code for three different Facility Service or Sections (and displays 3 detail lines in the report). For example:

Date of Contact: 01/22/2005

> ROC Number Issue Code FSoS

> 442.200600044 SC02 8S3

> SC02 9W

> SC02 5N2

> 442.200600043 SC02 9W

Should the total number of issues for 01/22/2005 be counted as one Issue, four, or two? Appendix C contains an explanation of the Count formula and gives the formula for different ways of counting an Issue.

### Subtotals - Count the number of Issue Codes within a Date of Contact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this scenario, we are assuming that we want to count an issue as a distinct issue code within a ROC, regardless of whether the same issue code has multiple FSoS or not. (In the above example for ROC number 442.200600044, that would mean that the Issue Code SC02 would be counted as 1).

In this example, we start with a report that contains Date of Contact, ROC numbers, Issue codes and FSoS. The ROCs are grouped by Date of Contact, and there is a break on ROC numbers so that we have a break footer for each ROC number.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click on the Issue code data within any ROC number, select Calculation\>Count. This creates a count of issues by ROC Number, and it also creates a count of issues by Date of Contact at the end of each date of contact section.
3.  If you don’t want a count of issues by ROC Number, you can delete the entire ROC footer. Right click anyplace within the break footer for any ROC number, and select Remove\>Row.

> ![](pats-user-guide/105.png)

> *Result: This deletes the ROC footer row from every ROC. Now you should see just a single count of Issues within a Date of Contact.*

> Note: Based on our definition, you may notice that the count doesn’t look right. By default, WEBI counts the number of distinct Issue Codes within the section (i.e., the Date of Contact in this case). If the same issue code appears in more than one ROC on the same Date of Contact, that Issue Code value just counts as one. What we really want to count is the number of distinct issue codes within each ROC and then total them by Date of Contact. We need to tell WEBI how to count the ROCs.

4.  Make sure that the formula toolbar shows beneath the main toolbar at the top. (If not, select View\>Toolbars\>Formula.)
5.  Make sure that the list of Available Objects shows up in the left hand pane. If not, you can select it from the list just above the left hand pane. We will want this visible so we can make sure to get the object names correct in our formula.
6.  To correct the count, highlight any of the actual count values within a Date of contact. The window should show the current formula =Count(\[Issue code and name\]).

> Note: In order to get the right count based on our assumption that an “issue” is a distinct Issue Code within a ROC, you must specify that you want to count the distinct Issue Codes within each ROC. To do that, edit the formula in the window to put together the ROC number with the Issue Code (use + between field names to indicate that you want to put them together, and remember that object names are case sensitive and must be surrounded by square brackets).

7.  Enter the new formula: =Count(\[ROC number\]+\[Issue code and name\])

> ![](pats-user-guide/106.png)

> Note: In the example the heading name was changed to My ROC, but the object name (ROC number) must be entered in the formula—not the heading name.

8.  Click the green check mark to validate and apply the new formula for the count.
9.  Note that the count for Date of Contact 12/23/05 has now changed to the correct value of four (4).

> ![](pats-user-guide/107.png)

10. Click Save.

> Note: For a further explanation of why the count must include the ROC Number as well as the Issue Code, and to see examples of formulas that let you count issues in other ways, see *Appendices B and C*.

## Saving a Report to your PC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can save a report to your PC: you can save to Excel, to PDF format, or to Excel as a comma separated value file.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Select Document\>Save to my computer as.
3.  Select PDF.

> *Result: A dialogue box displays. You can Open, Save, or Cancel the PDF version of the report.*

4.  Click Save.

> *Result: You are prompted to indicate where you want to save the file on your computer. You can also change the name of the file or leave it as is.*

5.  Navigate to the directory you want to save the report to. You can leave the title as is or give it a new title.
6.  Click Save.

> *Result: A dialogue box displays saying the download is complete. You can open the report or close it.*

7.  Let’s look at the PDF version of the report you saved to your PC. Click Open.

> *Result: The PDF report displays.*

8.  Let’s close the report. Click the red X in the box in the right corner to close the document.

> *Result: You are returned to the edit mode page.*

## 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, WEBI builds reports in table format, where each data type is in a column with a caption at the top. This structure isn’t compatible with how a screen reader operates; it reads left to right, top to bottom. A better way to design the report for 508 compliance is to display a field caption to the left of every field value.

To move captions to the left hand side of the data:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click anywhere within the report data and select Turn table to…
3.  From the Available Formats on the right side of the dialogue box, select Form.
4.  Click OK.

> *Result: The columnar format has been changed to display each field value with a leading caption. Since the format has been completely changed, you may need to re-adjust the size of your data cells.*

5.  Click Save.

## Sharing Reports with other Advocates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PATS application allows you to share report templates with other Patient Advocates. Your individual reports are in your Private folder. You are the only one who can see these private reports. All Advocates have access to reports that are in the Public Ad Hoc folder.

There are two ways to share a report with other advocates in the Public folder. The first way, using the Share Report button is the recommended way because it does most of the work for you. However, you can also use the Save As option (see important steps detailed below).

### Moving Reports to the Public Folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>![](pats-user-guide/108.png)</th>
<th><p>When you share a report with other Advocates, you don’t want your Institution data to display. When a new user opens the report, you want them to see data for their own site. When you use:</p>
<ul>
<li><blockquote>
<p><strong>Share Report</strong> button: the system automatically sets a flag that will cause the report to be refreshed with new data each time it is opened, based on the user who is opening the report.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Save As</strong> option: you must set the flag by using the Document properties (see <em>Use Save As to copy an existing report to the Public folder</em>).</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Use the Share Report button to copy a report to the Public folder (Recommended):

> 1\. On the Ad Hoc Folder – Private Reports page, find the report you want to copy to the Public folder.

> 2\. Click the Share Report button.

> *Result: The message “The report was copied to the Public Ad Hoc folder” displays in green at the top of the page. The report is now available to all users.*Use Save As to copy an existing report to the Public folder:

> 1\. On the Ad Hoc Folder – Private Reports page, click on the report title you want to copy to the Public folder.

> 2\. Select Document\>Edit.

> 3\. Select Document\>Properties.

> 4\. Check the Refresh on Open box, so that the report will be refreshed with new data each time it is opened.

> ![](pats-user-guide/109.png)

| ![](pats-user-guide/110.png) | If you don’t set the Document properties to Refresh on Open, the report will contain your site’s data. Since all Advocates have access to the Public folder, Advocates from other Institutions will see your data. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

> 5\. Click OK.

> 6\. Select Document\>Save As.

> *Result: A new window opens to prompt you for the save document information.*

> ![](pats-user-guide/111.png)

7. Title: Enter the name of the report.

8\. Description (*optional*): Complete this field, so that other Advocates can tell what the report covers.

9\. Location: You must indicate the folder you want to save your report in. Select Public Folder\>PATS\>Ad Hoc (highlight Ad Hoc, so the background turns grey).

10\. Click OK.

11\. Click on the Public folder link to display the Public folder listing and verify that the report has successfully been copied.

### Using a Reports from the Public Folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reports in the Public folder are available for all Advocates to view and use. Advocates can delete any report in the Public folder. So, if there is report in the Public folder that you would like to use or edit, move it to your private folder. (You can’t edit reports in the Public folder). Once you’ve moved a report to your private folder, you can run the query and edit the report or leave it as is.

To copy a report from the Public folder to your own Private folder:

> 1\. Click the Public folder link (on the menu bar).

> 2\. Find the report you want to copy to your Private folder and click on the title to open the report.

> 3\. Select Document\>Save As.

> 4\. Complete the title and description.

> Note: You can use the same title or a different title.

> 5\. Location: Since the private Favorites folder is the default folder, you don’t have to make any changes.

> 6\. Click OK.

> *Result: The report is copied to your Private folder.*

> 7\. Click the Private folder link (on the menu bar) and locate the report.

> Note: You now have your own copy of the report in your Private folder. You can edit the report or leave it as is.

# # Chapter 6 - Maintenance (Patient Advocates & VPACs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Advocates will maintain lists of site data that can be used in ROCs. These values can be maintained by any Patient Advocate with access to the site. These duties include:

- Add, update, activate, inactivate Congressional contact, Hospital Locations, and Comp information
- Add, update, or remove boilerplate Resolution Text

Each VISN-Level Advocate (VPAC) will be responsible for maintaining the list of Facility Service or Sections (formerly known as Service Disciplines in Patient Representative) for their VISN. VPACs will add, update, activate, and inactivate Facility Service or Section options.

> **NOTE:** Once information is added to the PATS maintenance tables, it cannot be deleted. However, you can inactivate information, so that it is not visible to users entering or editing ROCs.

In this Chapter

The following topics covered in this chapter.

|                                          |                                              |
|------------------------------------------|----------------------------------------------|
| Topic                                | Page                                     |
| 6.1 Managing Congressional Contacts      | [96](#managing-congressional-contacts)       |
| 6.2 Managing Hospital Locations          | [97](#managing-hospital-locations)           |
| 6.3 Managing Comps                       | [99](#managing-comps)                        |
| 6.4 Managing Boilerplate Resolution Text | [101](#managing-boilerplate-resolution-text) |
| 6.5 Managing Facility Service or Section | [103](#managing-facility-service-or-section) |

## Managing Congressional Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Advocates are responsible for maintaining a list of Congressional contacts in PATS. Update the list regularly, so that Congressional contacts are current. Congressional contacts are shared by all divisions within the default institution (i.e., Congressional contacts entered by a user logged on to station 110GA are also available to a user logged on to station 110 or 110GB and so on).

> **CAUTION:** Once Congressional contacts have been added to PATS tables, they cannot be deleted. However, you can inactivate congressional contacts, so they are not visible to users entering or editing ROCs.

6.1.1 Adding a Congressional Contact

To add Congressional contacts:

1\. On the PATS menu bar, click Maintenance.

> Result: The Table Maintenance page displays.

![](pats-user-guide/112.png)

2\. Congressional Contact: Enter the name of the Congressional contact in the box. You can enter up to 60 characters including spaces.

3\. Click Add.

> Result: A dialogue box displays, “Are you sure you want to add this Congressional contact?”

4\. Click OK to confirm.

6.1.2 Editing a Congressional Contact

To edit Congressional contacts:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the Congressional contact in the list and click Edit.

3\. Change the name as needed and click Update.

> Result: The Table Maintenance page displays a confirmation message. The updated information is displayed in the list.

6.1.3 Activating a Congressional Contact

To activate Congressional contacts that are inactive:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the Congressional contact in the list and click Activate.

> Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

6.1.4 Inactivating a Congressional Contact

To inactivate Congressional contacts:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the Congressional contact in the list and click Inactivate.

> Result: The Inactivation date and an Activate button displays after the contact name.

## Managing Hospital Locations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Advocates are responsible for maintaining a list of hospital locations in PATS. Hospital Locations must be entered for each division within the default institution (i.e., you must be logged onto station 110 to enter or select Hospital Locations for station 110; you must be logged onto station 110GB to enter or select Hospital Locations for station 110GB and so on).

> **NOTE:** Hospital locations cannot be deleted from the PATS database after they have been added. You can only activate or inactivate a hospital location.

6.2.1 Adding a Hospital Location

To add a hospital location:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Hospital Locations tab.

![](pats-user-guide/113.png)

3\. Hospital Location: Enter the name of the hospital location in the box. You can enter up to 30 characters, including spaces.

4\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Hospital Location?”

5\. Click OK to confirm.

> Result: The hospital location is added to the list.

6.2.2 Editing a Hospital Location

To edit a hospital location:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Hospital Locations tab.

3\. Find the hospital location you want to change in the list and click Edit.

4\. Change the location as needed and click Update.

Result: The Table Maintenance page displays a confirmation message. The updated information is displayed in the list.

*6.2.3 Activating a Hospital Location*

To activate an inactive hospital location:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Hospital Locations tab.

3\. Find the hospital location you want to activate in the list and click the Activate button.

Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

6.2.4 Inactivating a Hospital Location

To inactivate a hospital location:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Hospital Locations tab.

3\. Find the hospital location you want to inactivate in the list and click the Inactivate button.

Result: The Inactivation date and an Activate button display.

## Managing Comps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Advocates are responsible for maintaining a list of comps in PAT. Comps are items to compensate the person making the complaint for any inconvenience. Comps must be entered for each division within the default institution (i.e., you must be logged onto station 110 to enter or select Comps for station 110; you must be logged onto station 110GB to enter or select Comps for station 110GB and so on).

> **NOTE:** Comps cannot be deleted from the PATS database after they have been added. You can activate or inactivate a comp.

6.3.1 Adding a Comp

To add a comp:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Comps tab.

![](pats-user-guide/114.png)

3\. Comp: Enter the name/description of the comp in the box.

> Note: You can enter up to 30 characters, including spaces.

4\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Comp?”

5\. Click OK to confirm.

Result: The comp appears at the end of the Comp Name list.

6.3.2 Editing a Comp

To edit a comp:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Comps tab.

3\. Find the comp you want to change in the list and click Edit.

4\. Change the comp as needed and click Update.

Result: The Table Maintenance page displays a confirmation message. The updated information is displayed in the list.

6.3.3 Activating a Comp

To activate a comp:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Comps tab.

3\. Find the comp you want to activate in the list and click the Activate button.

Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

6.3.4 Inactivating a Comp

To inactivate a comp:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Comps tab.

3\. Find the comp you want to inactivate in the list and click the Inactivate button.

Result: The Inactivation date and an Activate button display.

## Managing Boilerplate Resolution Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Advocates are responsible for maintaining “boilerplate” resolution text in PATS. This is text that is often used in resolving issues. Boilerplate resolution text must be entered for each division within the default institution (i.e., you must be logged onto station 110 to enter or select Boilerplate resolution text for station 110; you must be logged onto station 110GB to enter or select Boilerplate resolution text for station 110GB and so on).

6.4.1 Adding Resolution Text

To add resolution text:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Resolution Text tab.

![](pats-user-guide/115.png)

3\. Issue Category *(Optional)*: If you know the issue code or want to see a list of all issue codes, leave this field blank.

> If you want to limit the issue codes in the drop-down list (step 4), select a specific issue category from the drop-down list.

4\. Issue code (Required): Select an issue code from the drop-down list.

5\. Resolution text (Required): Enter the resolution text in the text box (8,000 characters including spaces).

> Note: The system does not accept HTML commands. If you enter “\<” followed by “\>” (i.e., \< *any text* \>), the text appears to contain HTML. Do not enter brackets.

6\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Resolution Text?”

7\. Click OK to confirm.

Result: The Resolution Text is added to the corresponding Issue Code.

6.4.2 Editing Resolution Text

To edit resolution text:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Resolution Text tab.

3\. Find the resolution text you want to change and click Edit.

4\. Change the resolution text and click Update.

Result: The Table Maintenance page displays a confirmation message. The updated information is displayed in the list.

6.4.3 Deleting Resolution Text

To delete resolution text:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Resolution Text tab.

3\. Find the Resolution text you want to delete and click Delete.

Result: A dialogue box displays and asks if you want to delete the resolution text.

4\. Click OK to confirm. Click Cancel if you decide not to delete the text.

Result: The resolution text is deleted.

## Managing Facility Service or Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VISN-Level Advocate (VPAC) is responsible for maintaining a list of Facility Services or Sections in PATS. Facility Services or Sections are shared by all divisions within the VISN (i.e., Facility Services or Sections entered by a VPAC in VISN 1 logged onto Bedford 518 are also available to a user logged on to Manchester 608, Northampton 631, Togus 402 and so on).

> **NOTE:** Facility Service or Sections cannot be deleted from the PATS database after they have been added. You can only activate or inactivate a facility service or section.

Contact the VSSC prior to making any changes to ensure that changes do not adversely impact the Rollup process.

6.5.1 Adding a Facility Service or Section

To add a Facility Service or Section:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Facility Service or Section tab.

![](pats-user-guide/116.png)

3\. Facility Service or Section: Enter the name of the facility service or section in the box. You can enter up to 50 characters, including spaces.

4\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Facility Service or Section?”

5\. Click OK to confirm.

Result: The new Facility Service or Sections is added to the listing.

> Reminder: Be sure to inform Patient Advocates of changes made to Facility Services or Sections.

6.5.2 Editing a Facility Service or Section

To edit a Facility Service or Section:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Facility Service or Section tab.

3\. Find the Facility Service or Section you want to edit in the list and click Edit.

4\. Change the label as needed and click Update.

Result: The Table Maintenance page displays a confirmation message. The updated information is displayed in the list.

> Reminder: Be sure to inform Patient Advocates of changes made to Facility Services or Sections.

6.5.3 Activating a Facility Service or Section

To activate an inactive Facility Service or Section:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Facility Service or Section tab.

3\. Locate the facility service or section in the list and click Activate.

Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

> Reminder: Be sure to inform Patient Advocates of changes made to Facility Services or Sections.

6.5.4 Inactivating a Facility Service or Section

To inactivate a Facility Service or Section

1\. On the PATS menu bar, click Maintenance.

2\. Click the Facility Service or Section tab.

3\. Locate the facility service or section in the list and click the Inactivate button.

Result: The Inactivation date and an Activate button display.

> Reminder: Be sure to inform Patient Advocates of changes made to Facility Services or Sections.

# Chapter 7 – Maintenance (NPO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a National Program Office (NPO) administrator, you can add or change any of the following information available to PATS users nationally:

- Issue categories
- Issue codes
- Methods of contact
- Treatment statuses
- Contacting entities
- The number of days before an ROC is overdue

> **NOTE:** Once information is added to PATS tables, it cannot be deleted. However, you can inactivate information, so that it is not visible to users entering or editing ROCs.

 In this Chapter

The following topics are covered in this chapter.

|                                              |                                                                    |
|----------------------------------------------|--------------------------------------------------------------------|
| Topic                                    | Page                                                           |
| 7.1 Managing Issue Categories                | [107](#managing-issue-categories)                                  |
| 7.2 Managing Issue Codes                     | [110](#managing-issue-codes)                                       |
| 7.3 Managing Methods of Contact              | [113](#managing-methods-of-contact)                                |
| 7.4 Managing Treatment Status                | [115](#managing-treatment-status)                                  |
| 7.5 Managing Contacting Entities             | [117](#managing-contacting-entities)                               |
| 7.6 Changing the Number of Days for All ROCs | [120](#changing-the-number-of-days-for-all-rocs-to-become-overdue) |

## Managing Issue Categories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A National Program Office administrator is responsible for maintaining a list of issue categories in PATS. 

For issue categories, you can perform any of the following tasks:

- add an issue category
- change an issue category description
- change the sort order issue categories appear in the PATS drop-down list
- apply a customer service standard to an issue category
- inactivate an issue category, so that it is not visible or accessible to users
- reactivate an inactivated issue category

> **NOTE:** Issue categories cannot be deleted from the PATS database after they have been added. You can only activate or inactivate an issue category.

7.1.1 Adding an Issue Category

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To add an issue category:

1\. On the PATS menu bar, click Maintenance.

> Result: The Table Maintenance – Issue Categories page displays.

> ![](pats-user-guide/117.png)

2\. Issue Category (Required): Enter the name of the issue category. You can enter up to 50 characters, including spaces.

3\. Code (Required): Enter the 2 character~~s~~ (alpha) issue code.

4\. Sort Order (*Optional*): Enter a number (up to 999) for the order the issue categories appear in the drop-down list on the Edit Report of Contact – ROC Issue Details page.

> Note: If you don’t enter a sort order number, the issue category will appear at the end of the list.

5\. Customer Service Standard (*Optional*): Check the box if this issue is associated with a customer service standard.

6\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Issue Category?”

7\. Click OK to confirm.

Result: the Issue Category is added to the listing in the sort order indicated or at the end.

8\. Inform Patient Advocates of changes made.

Once you add an issue category, you must add an issue code ([How?](#managing-issue-codes) See page [110](#managing-issue-codes).)

7.1.2 Changing the Sort Order of Issue Categories

To change the sort order of issue categories:

1\. On the PATS menu bar, click Maintenance.

3\. Click Change Sort Order.

Result: The Table Maintenance – Sort Order page displays.

4\. Highlight the issue category and use the Up and Down buttons to reposition it.

5\. Click OK.

Result: The Table Maintenance page displays a confirmation message. The updated information is displayed in the list.

7.1.3 Editing an Issue Category

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To edit an issue category:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the issue category and click Edit.

Result: Issue-Category – Edit page displays.

3\. Change the name as needed and click Update.

Result: The Table Maintenance page displays saying the issue category was updated.

4\. Inform Patient Advocates of changes made.

> **NOTE:** Issue categories cannot be deleted from the PATS database after they have been added. You can only activate or inactivate an issue category.

7.1.4 Activating an Issue Category

To activate an inactive issue category:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the issue category on the list and click Activate.

Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

7.1.5 Inactivating an Issue Category

To inactivate an issue category:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the issue category on the list and click Inactivate.

Result: The Inactivation date and an Activate button display.

## Managing Issue Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A National Program Office administrator is responsible for maintaining a list issue codes in PATS.

You can do the following:

- add an issue code
- change an issue code name or description
- inactivate an issue code so that it is not visible or accessible to users
- reactivate an inactivated issue code

An issue code consists of two letters to identify its category, followed by two or three numbers (which PATS automatically adds).

> **NOTE:** Issue codes cannot be deleted from the PATS database after they have been added. You can only activate or inactivate an issue code.

  
7.2.1 Add an Issue Code

> **NOTE:** Contact the VSSC prior to making any changes to issue codes to ensure that they do not adversely impact the Rollup process.

To add an issue code:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Issue Code tab.

Result: The Table Maintenance – Issue Codes page displays.

> ![](pats-user-guide/118.png)

3\. Issue Code Name (Required): Enter the issue code name in the box. You can enter up to 60 characters, including spaces.

4\. Issue Category (Required): Highlight the appropriate category on the Issue Category drop-down list.

5\. Description (*Optional*): enter a description.

6\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Issue Code?”

7\. Click OK to confirm.

Result: The system-assigned Code and Issue Code Name display alphabetically in the list.

8\. Inform Patient Advocates of changes made.

7.2.2 Edit an Issue Code

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To edit an issue code:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the issue code and click Edit.

Result: The Issue Code – Edit page displays.

3\. Change the description as needed and click Update.

Result: The Table Maintenance page displays a confirmation message. The updated information is displayed in the list.

4\. Inform Patient Advocates of changes made.

7.2.3 Activate an Issue Code

To activate an issue code:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the issue code on the list and click Activate.

Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

7.2.4 Inactivate an Issue Code

To inactivate an issue code:

1\. On the PATS menu bar, click Maintenance.

2\. Locate the issue code on the list and click Inactivate.

Result: The Inactivation date and Activate button display.

## Managing Methods of Contact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A National Program Office administrator is responsible for maintaining the list of methods of contact. You can:

- add a Method of Contact
- change a Method of Contact description
- change the sort order of Methods of Contact
- inactivate a Method of Contact so that it is not visible or accessible to users
- reactivate an inactivated method of contact

> **NOTE:** Methods of contact cannot be deleted from the PATS database after they have been added. You can only activate or inactivate a method of contact.

7.3.1 Adding a Method of Contact

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To add a method of contact:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Method of Contact tab.

![](pats-user-guide/119.png)

3\. Method of Contact: Enter the method of contact (up to 20 characters).

4\. VSSC Code: Enter the 1-character (alpha) VSSC code.

> **NOTE:** The VSSC Code identifies the Method of Contact when the data is rolled up to Austin for the VSSC reports.

5\. Sort Order (*optional*): Enter up to 5 digits in the Sort Order box to indicate the position on the displayed list. Leaving this field blank will default to the bottom of the list.

6\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Method of Contact?”

7\. Click OK to confirm.

8\. Inform Patient Advocates of changes made.

7.3.2 Changing the Sort Order of Methods of Contact

To change the sort order of methods of contact:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Method of Contact tab.

3\. Click Change Sort Order.

4\. Highlight the method of contact you want to change and use the Up and Down buttons to reposition it.

> Note: You can move more than one item at the same time.

5\. Click OK.

Result: The Table Maintenance page displays a confirmation message. The updated information is displayed in the list.

7.3.3 Editing the Method of Contact

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To edit the method of contact:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Method of Contact tab.

3\. Locate the method of contact on the list and click Edit.

4\. Edit the method of contact name as needed and click Update. 

Result: The reminder box displays.

> Note: If you changed a Rollup code, contact the VSSC in Austin so that they can update their system to accept the code.

5\. Click OK.

6\. Inform Patient Advocates of changes made.

7.3.4 Activating the Method of Contact

To activate the method of contact:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Method of Contact tab.

3\. Locate the Method of Contact on the list and click Activate.

Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

7.3.5 Inactivating the Method of Contact

To inactivate the method of contact:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Method of Contact tab.

3\. Locate the Method of Contact on the list and click Inactivate.

Result: The Inactivation date and Activate button display.

## Managing Treatment Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A National Program Office administrator is responsible for maintaining the list of Treatment Statuses. You can:

- add a Treatment Status
- change a Treatment Status description
- change the sort order of Treatment Statuses
- inactivate a Treatment Status so that it is not visible or accessible to users
- reactivate an inactivated Treatment Status

> **NOTE:** Treatment Statuses cannot be deleted from the PATS database after they have been added. You can only activate or inactivate a Treatment Status.

7.4.1 Adding a Treatment Status

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To add a treatment status:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Treatment Status tab.

![](pats-user-guide/120.png)

3\. Treatment Status: Enter a new treatment status (up to 30 characters).

4\. VSSC Code: Enter the 1-character (alpha) rollup code.

> **NOTE:** The VSSC Code identifies the Treatment Status when the data is rolled up to Austin for the VSSC reports.

5\. Sort Order *(optional)*: Enter up to 5 digits in the Sort Order box to indicate the treatment status position on the displayed list. Leaving this field blank will default to the bottom of the list.

6\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Treatment Status?”

7\. Click OK to confirm.

Result: The Table Maintenance page displays with the new Treatment Status.

8\. Inform Patient Advocates of changes made.

7.4.2 Changing the Sort Order

To change the sort order of treatment statuses:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Treatment Status tab.

3\. Click Change Sort Order.

4\. Highlight the treatment status and use the Up and Down buttons to reposition the selected Treatment Status.

> Note: You can move more than one item at the same time.

5\. Click OK.

7.4.3 Editing a Treatment Status

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To edit a treatment status:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Treatment Status tab.

3\. Locate the treatment status on the list and click Edit.

4\. Edit the treatment status as needed and click Update.

5\. Click OK.

Result: The Table Maintenance page displays with the updated Treatment Status.

6\. Inform Patient Advocates of changes made.

7.4.4 Activating a Treatment Status

To activate a treatment status:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Treatment Status tab.

3\. Locate the treatment status on the list and click Activate.

Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

7.4.5 Inactivating a Treatment Status

To inactivate a treatment status:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Treatment Status tab.

3\. Locate the Treatment Status on the list and click Inactivate.

Result: The Inactivation date and an Activate button display.

## Managing Contacting Entities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A National Program Office administrator is responsible for maintaining the list of Contacting Entities. You can:

- add a Contacting Entity
- change a contacting entity description
- change the sort order of Contacting Entities
- inactivate a Contacting Entity so that it is not visible or accessible to users
- reactivate an inactivated Contacting Entity

> **NOTE:** Contacting entities cannot be deleted from the PATS database after they have been added. You can only activate or inactivate a contacting entity.

7.5.1 Adding a Contact Entity

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To add a Contacting Entity:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Contacting Entity tab.

Result: The Table Maintenance – Contacting Entities page displays.

![](pats-user-guide/121.png)

3\. Contacting Entity: Enter a new contacting entity in the box (up to 50 characters).

4\. VSSC Code: Enter the 2-character (alpha) VSSC code.

> **NOTE:** The VSSC Code identifies the Contacting Entity when the data is rolled up to Austin for the VSSC reports.

5\. Sort Order *(optional)*: Enter up to 5 digits in the Sort Order box to indicate the contacting entity position on the displayed list. Leaving this field blank will default to the bottom of the list.

6\. Click Add.

Result: A dialogue box displays, “Are you sure you want to add this Contacting Entity?”

7\. Click OK to confirm.

Result: The Table Maintenance page displays with the new Contacting Entity.

8\. Inform Patient Advocates of changes made.

7.5.2 Changing the Sort Order

To change the sort order of a contacting entity:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Contacting Entity tab.

3\. Click Change Sort Order.

4\. Highlight the Contacting Entity and use the Up and Down buttons to reposition it.

5\. Click OK.

7.5.3 Editing a Contact Entity

> **NOTE:** Contact the VSSC prior to making any changes to ensure that they do not adversely impact the Rollup process.

To edit a contacting entity:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Contacting Entity tab.

3\. Locate the contacting entity on the list and click Edit.

4\. Edit the contacting entity or VSSC code and click Update. 

Result: The Table Maintenance page displays with the updated Contacting Entity.

5\. Inform Patient Advocates of changes made.

7.5.4 Activating a Contact Entity

To activate a contacting entity:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Contacting Entity tab.

3\. Locate the contacting entity on the list and click Activate.

Result: The Inactivation date no longer displays; the Edit and Inactivate buttons display.

7.5.5 Inactivating a Contact Entity

To inactivate a contacting entity:

1\. On the PATS menu bar, click Maintenance.

2\. Click the Contacting Entity tab.

3\. Locate the inactive contacting entity on the list and click Inactivate.

Result: The Inactivation date and an Activate button display.

## Changing the Number of Days for All ROCs to Become Overdue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A National Program Office administrator is responsible for maintaining the number of days before an ROC becomes overdue. This becomes the setting for all ROCs.

To change the number of days before ROCs are overdue:

1\. On the PATS menu bar, click Maintenance.

2\. Click the ROC Expiration Days tab.

Result: The Table Maintenance – ROC Expiration Days page displays.

![](pats-user-guide/122.png)

3\. Number of Days for ROC is Overdue: The default for an ROC to be considered overdue is 7 days. Enter the number of days that an ROC is overdue (up to 999).

4\. Click Update.

# # Appendix A: Informational and Action Request Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Rep application used VistA mail to send alert notifications to employees regarding patient complaints. The PATS application uses Outlook to send notifications. You might want to explain to recipients what to do when they receive a notification. This appendix contains a sample email that you can send to recipients of Informational or Action Request Notifications.

### Sample Email to send to Notification Recipients:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“The Patient Representative system has recently been replaced by the Patient Advocate Tracking System (PATS). The Patient Rep system used VistA mail to send alert notifications to employees regarding patient complaints. The PATS application uses Outlook mail to send notifications.

> If you receive a notification from the PATS system, do the following:

> 1\. In the email message, note the division that sent the notification.

> 2\. Click on the link in the email message.

> *Result: The PATS logon page displays.*

> 3\. From the division drop-down list, select the division that was specified in the e-mail.

> 4\. Enter your VistA access and verify codes (i.e., the same as you use to access CPRS or other VistA applications).

> 5\. Press the Login button (if you press Enter, you will have to re-enter your access and verify codes).

> *Result: The Notification displays.*

> ![](pats-user-guide/123.png)

> 6\. If you receive an Informational Notification, view the Notification and then select Log off.

> 7\. If you receive an Action Request Notification, view the Notification, enter a response to the Patient Advocate, and then log off.”

# # Appendix B: Ad Hoc Tutorial

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ad Hoc Exercises

## Display Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the right side of your display is cut off when using the Ad Hoc reporting tool, you may need to increase the resolution on your screen monitor.

1.  At the bottom left of your screen, click Start\>Control Panel\>Display.
2.  Select the Settings tab.
3.  In the Screen resolution box, move the arrow to the right to increase the resolution.

> ![](pats-user-guide/124.png)

4.  Click OK.

## Scenario \#1: Building a Report Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new report, the first thing you do is build the report query—that is, you define the fields you want to include in the report.

1.  To obtain the URL for PATS on the EIE Training account, send an email to [VHA HSITES EMC HEV Support](mailto:VHA%20HSITES%20EMC%20HEV%20Support).

    Note: This tutorial was created as part of PATS National training. You can use your production account to perform these exercises; however, the data will look different from the examples shown. If you use your production account, log on to your own division using your VistA access and verify codes. When you are finished, you can delete any reports you created.
2.  Log into Test Parent Stn 110 (110) using your Student Access and Verify codes.
3.  On the PATS menu bar under Ad Hoc, select the Private link.
4.  Click the Add button.
5.  To define the objects that you want in your report query, you move objects from the Universe pane to the Result Objects pane by:
- Double-clicking the object name, or
- Highlighting the object and clicking the \>\> arrow next to the Result Objects pane.

  ![](pats-user-guide/125.png)
6.  Move these fields to the Result Objects pane:
- Institution number and name (click the + next to the words Institution number)
- Hospital location
- Date of contact
- Patient name
- Issue code and name (click the + next to the words Issue code)
- ROC number

> *Result: When you move Institution number and name to the Result Objects pane, it also brings over Institution number. The reason for this is Institution number and name is part of the Institution number group. The same thing occurs when you move Issue Code and name to the Result Objects pane.*

7\. Highlight Institution number (blue box) and use the \<\< arrow to delete the Institution Number box from the Result Objects pane.

8.  Highlight Issue code (blue box) and use the \<\< arrow to remove Issue Code box from the Result Objects pane.
10. Click the Run Query button. This is like running the report in Patient Rep.

    *Result: The first time you run the query, WEBI will automatically put all of the fields you selected into the report.*
11. Click the Save button (to the right of the Insert button; icon is a disc).

> *Result: A new window opens to prompt you for the save information.*

> ![](pats-user-guide/126.png)

> ![](pats-user-guide/127.png) When you’re working on a document/report, it’s always a good idea to save your work often. That way, if you’re in the middle of editing a report and you get called away and time out, or if you accidentally click on a link that takes you out of the report, you won’t lose all of the work you’ve done. The ad hoc reporting tool is set to time out after 20 minutes of inactivity, so be sure to save your work after you make any changes.

12. In the Title box, enter Issues by Location n (where n is your Student number and your initials).
13. Though the Description is optional, it is recommended that you enter a description to help readily identify the report in the listing. This will be important as you create more ad hoc reports.

    Let’s add the description: Report displays the Institution, Issues, patient name and date of contact grouped by Location within a date range.
14. Although you see several different folders, you can only save your private reports in the Favorites sub-folder under My Folders. (That’s the default folder that will be highlighted).
15. Click OK.

## Scenario \#2: Creating Filters and Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will notice that the Issue code and name field is blank on some of the records in our report. These are ROCs where issue codes have not been assigned yet. On this report, you will be doing totals by issue code, so before you start designing our report, let’s go back to the query again and limit the data--create a filter--that will only select ROCs that have at least one issue code.

Filter: Issue Codes

1.  Verify you are in the Edit mode by making sure that the Edit Query button appears in the upper right side of the screen. (To return to Edit mode, select Document\>Edit.)
2.  Click the Editquery button.
3.  In the Universe pane on the left, highlight Issue code and click the \>\> arrow key to the left of the Query Filters pane.

> *Result: Issue Code in List displays in the Query Filters pane.*

> ![](pats-user-guide/128.png)

4.  At the bottom of the Query Filters pane, click the filter criteria drop-down list (In List drop-down) and highlight Is not Null. This command tells the system to show only ROCs that have at least one issue code. Notice that the Filter and Prompt buttons are grayed out.
5.  Click the Update Filter button.

> *Result: The “Issue code Is not Null” button displays in the Query Filters pane.*

> ![](pats-user-guide/129.png)

6.  Click the Run Query button.

Result: All listed ROCs display an Issue Code.

7.  Click the Save button.

Add a Prompt for Date of Contact

In order to use a report from month to month, you can set up a prompt. For example, you could set up a prompt for starting and ending Date of Contact. Reports cover data for the current fiscal year and the two previous fiscal years. If you want more current information, you could limit the date range for Date of Contact to the current fiscal year, current quarter, or whatever meets your needs.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click the Editquery button.
3.  In the Universe pane on the left, highlight the Date of Contact and press the  
    \>\> arrow to the left of the Query Filters pane.

> *Result: The Issue code Is not Null AND Date of Contact in List displays in the Query Filters pane.*

4.  Click the filter criteria drop-down list (In List drop-down) and highlight Between.
5.  Make sure that the Prompt button is selected.
6.  You could accept the default value for the prompt text (what you see when you run the report and are prompted for values), but let’s change the values to Starting Date and Ending Date.
    - In Prompt text 1 box enter Starting Date.
    - In the Prompt text 2 box enter Ending Date.

> ![](pats-user-guide/130.png)

7.  Click the Update Filter button at the right (this button may be partially cut off).

> *Result: The Date of contact Between prompt (‘Starting Date’) And prompt (‘Ending Date’) displays in the Query Filters pane.*

> ![](pats-user-guide/131.png)

8.  Click the Run Query button to rerun the query.

> *Result: The Prompts box displays.*

9.  You should see the heading Starting Date above the prompt box on the lower right hand side. If you don’t see the Starting Date, click on the word Starting Date on the top left, where it says Prompts.

> ![](pats-user-guide/132.png)

10. In the box below Starting Date, enter 8/1/2006 in m/d/yyyy format. You don’t have to enter a time.
11. Click on Ending Date at the top left.

> *Result: The starting date you entered displays in the top box.*

> ![](pats-user-guide/133.png)

12. In the box below Ending Date, enter 12/29/2006 in m/d/yyyy format.

> ![](pats-user-guide/134.png)

13. Click on Ending Date in the top left to accept the date you’ve entered.

> ![](pats-user-guide/135.png)

14. Click the Run Query button.

> *Result: The report only displays ROCs between 8/1/2006 and 12/29/2006.*

15. Click the Save button.

> ![](pats-user-guide/136.png) To have the prompt for new starting and ending dates display and to refresh the data each time you open the report, set Refresh on Open in the Document Properties.

16. Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)

> 17\. Select Document\>Properties.

Result: the Document Properties box displays.

> 18\. Check the Refresh on Open box.

> ![](pats-user-guide/137.png)

> 19\. Click the OK button.

> 20\. Click the Save button.

## Scenario \#3: Deleting a column from the report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now you’re ready to start designing our report. WEBI created an initial design by putting all of the fields you selected during the query onto the report. The ROC number was added to the report because you’ll need it later for a calculation, but let’s not display it on the report. You can delete the field from the display but still access the information.

To delete a column from the report:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click on any data cell in the ROC number column.
3.  Select Remove\>Column.

> *Result: The column is deleted from the report, but the ROC number is still in the Available Objects list.*

> Note: When you delete a column or section from the display, the information is still available. Since the object (data field) is in the Available Objects list, you can add it back into the display if you want.

4.  Click Save.

## Scenario \#4: Creating sections – Group the data by Institution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Dividing reports into sections enables you to group related information together in reports.

To create a section:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click any data cell in the Institution number and name column and select Set as section.

> *Result: Institution number and name becomes a section header and groups the other items in a block beneath the header.*

> ![](pats-user-guide/138.png)

> ![](pats-user-guide/139.png) Before you save, make sure that everything is the way you want it. Once you click Save, the Undo button doesn’t work on the last change. Of course, you can always edit the report to undo a change.

3.  Click Save.

## Scenario \#5: Breaking by Location – Another way to group data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this section, you will group the data by Location. You will create a new section as you did with the Institution, but let’s see another way to group data that WEBI refers to as breaking.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click in any data cell in the Hospital location column. Click on Break\>Insert to group the other items within the block by location.

> *Result: You may notice a new line at the bottom of each location that contains the name of the location, but no other data. This extra line at the bottom is called the break footer.*

> ![](pats-user-guide/140.png)

3.  Because the data you’ll be putting in this report will take up quite a bit of space, let’s pull the location out of the table and put it above the rest of the data as a header.

> UNDO the break by clicking the Undo button.

## Scenario \#6: Creating sections – another way to group the data by Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a section:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Now let’s make Hospital location a section within the Institution section. Right click any data cell in the Hospital location column and select Set as section.

> *Result: Hospital Location becomes a section header and groups the other items in a block beneath the header.*

> ![](pats-user-guide/141.png)

3.  Click Save.

To keep the Location section entries together on a page:

Sometimes data within a location will be split between two pages. It would be preferable to keep all the data for a location on one page.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click to the right of the Hospital location cell, so that the entire section is highlighted, including the location, and the block of data below it.
3.  Select Format\>Section.
4.  Select the Layout Properties tab and check the Avoid page breaks in a block box.

> *Result: The report will then insert a page break to keep all data within one location together on one page. Of course, if there is too much data to fit on a single page, they will be split between two pages.*

5.  Click OK.
6.  Click Save.

## Scenario \#7: Adding a field to an existing report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a field to a report after you’ve run the query, you need to change or edit the query, so that the field gets pulled from the database when the report is run. Let’s add Issue Text to the report.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click the Edit Query button.
3.  From the Universe pane on the left side, double-click Issue Text or highlight it and use the \>\> arrows to move it into the Result Objects pane.
4.  Click the Run Query button.

> *Result: The Prompt box displays. You can change the dates or run the query with these dates. Let’s leave the dates as is.*

5.  Click the Run Query button.

> *Result: Issue Text doesn’t appear in your report. WEBI only displays all the data fields the first time you run a query. After that, WEBI doesn’t make any changes to the report design because it doesn’t want to second-guess you. Remember that the query returns the data, and the report design determines how or even if the data appears on the report.*

> ![](pats-user-guide/142.png)

> ![](pats-user-guide/143.png) The field is *available to be added to the report*. You will see a list of available objects in the left panel.

> (To display the left panel with Available Objects, click the Show left panel icon (![](pats-user-guide/144.png)) at the top left of the report, or select View\>Left Panel from the toolbar at the top. From the drop-down list, select Available Objects.)

6.  First you’ll add the column in the report and pull in the data. Let’s insert the new column to the right of the Patient Name, so right click in any data cell in the Patient Name column.
7.  Select Insert\>New column\>right.

> *Result: A blank column displays.*

8.  Drag the blue box next to Issue Text to a *blankdatacell* (don’t drag it to the header) in the new column.
9.  Click Save.

> ![](pats-user-guide/145.png)

## Scenario \#8: Subtotals - Count the number of Issue codes within a Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now let’s add subtotals to our report that count the number of Issue Codes within a Location.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click in any data cell in the Issue code and name column. Select Calculation\>count.

> *Result: A new row displays at the bottom of each Location with the count of Issue codes.*

> ![](pats-user-guide/146.png)

![](pats-user-guide/147.png) You may notice that the count doesn’t look right (Dental on page 2). WEBI by default, counts just the number of distinct Issue Codes, so if the same issue code appears more than once within a location, that Issue Code value just counts as one. If the same issue code appears in two different ROCs, you want to count it as 2, so you really want to count the number of distinct issue codes in a ROC.

3.  Make sure that the formula toolbar shows beneath the main toolbar at the top. (If not, select View\>Toolbars\>Formula.)

> ![](pats-user-guide/148.png)

4.  Make sure that the list of Available Objects shows up in the left hand pane. (If not, select View\>Left panel from the top toolbar, then select Available Objects from the drop-down list.) You want to display the Available Objects list, so you can enter the correct object names in the formula.
5.  To correct the count, highlight a cell with a count value. The window should show the current formula =Count(\[Issue code and name\]).

![](pats-user-guide/149.png) In order to get the right count, you want to count the distinct Issue Codes within each ROC. You deleted the ROC number from the display but the data can still be accessed. Let’s edit the formula in the window to put together the ROC number with the Issue Code. Enter + between field names to indicate that you want to put them together, and remember that field names are case sensitive and must be surrounded by square brackets) (i.e., you’re counting the distinct combination of ROC number and Issue Code).

6.  Enter the new formula: =Count(\[ROC number\]+\[Issue code and name\])

> ![](pats-user-guide/150.png)

> ![](pats-user-guide/151.png) Data item names are case sensitive.

7.  Click the green check mark to validate and apply the new formula for the count.
8.  Note that the count has now changed to the correct value (from 3 to 5).

> ![](pats-user-guide/152.png)

9.  Click Save.

## Scenario \#9: Grand Totals - Count the total number of issue codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Let’s add a grand total that counts the Issue Codes.

> To add a footer for the grand total:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  You need a place to put our grand total. First you’ll put some space at the bottom of our report (called a footer).
3.  Right click in a blank area outside the data.
4.  Select Format Report.
5.  Later on you’ll be putting a heading on our report, so as long as you’re here you’ll set up both a header and a footer.

> On the General tab, check the Show header box and check the Show footer box.

6.  Enter .5 for the header and footer height (you may want to adjust the height; see what works), then click OK.

> *Result: There is empty space above and below the data for the header and footer. Now you need to move a blank cell into the footer so you have a place to put the grand total.*

7.  Verify that the left panel is displayed. (If not, click the Show left pane icon (![](pats-user-guide/153.png)) at the top left of the report, or select View\>Left Panel from the toolbar at the top.)
8.  Click the drop-down list at the top of the left pane, and select Chart and Table Types.

> *Result: The categories of chart, table, and cell types appear.*

> ![](pats-user-guide/154.png)

![](pats-user-guide/155.png) If the Cells category is not visible, click the + next to Report Elements.

9.  Click the + next to Cells.
10. Click the + next to Formula and Text Cells.
11. Scroll to the bottom of the report. Drag the box next to Blank Cell to the report footer.

> *Result: The top of the report displays*

12. Scroll to the bottom of the report again and click in the blank cell to make sure it’s highlighted.
13. Make sure that the formula toolbar shows beneath the main toolbar at the top. (If not, select View\>Toolbars\>Formula.)
14. As before, in order to get the correct total, you want to count the distinct Issue Codes by ROC Number.
15. Enter the formula in the formula bar:

> =Count(\[ROC number\]+\[Issue code and name\])

> OR

1.  Highlight a Count cell and copy the formula (Ctrl C).
2.  Highlight the footer cell.
3.  Click in the formula cell at the top and paste the formula (Ctrl V).
16. Let’s put a caption on the total. Edit the existing formula to add the caption to the formula, so that it now says:

> =”Total Issues: “+Count(\[ROC number\]+\[Issue code\])

17. Click the green check mark to validate and apply the new formula for the count.

> ![](pats-user-guide/156.png)

18. Scroll to the bottom of the report again. Right click on the cell and select Format\>Cell. You then have the option of changing the font, changing the size of the cell, changing the layout of the cell (i.e., the position within the footer), and controlling whether you have a border around the cell.
19. Click Save.

## Scenario \#10: Add a title and page numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Creating a title on the report

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Verify that the left panel is displayed. (If not, click the Show left pane icon (![](pats-user-guide/157.png)) at the top left of the report, or select View\>Left Panel from the toolbar at the top).
3.  Click the drop-down list at the top of the left pane, and select Chart and Table Types.

> *Result: The categories of chart, table, and cell types appear.*

> ![](pats-user-guide/158.png)

> ![](pats-user-guide/159.png) If the Cells category is not visible, click the + next to Report Elements.

4.  Click the + next to Cells.
5.  Click the + next to Formula and Text Cells.
6.  Select the Blank Cell format and drag the box next to Blank Cell onto the header.
7.  Right click in the blank cell.
8.  Select Format\>Cell.
9.  On the General tab in the Name box, enter the title of the report—Issues by Location.
10. If you want the title to appear on every page of the report, select the Layout Properties tab and check the box next to Repeat on every page.
11. You also have the option of changing the font, alignment (*within the cell*: left, center, right), and the border under the title.
12. Click OK.
13. Click Save.

  
Creating page numbers for the report

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click the arrow to the right of the drop-down list box and select Chart and Table Types.
3.  Click the + next to Page number cells and select the type of page number you want.

> ![](pats-user-guide/160.png)

4.  Scroll down to the bottom of the page, and drag the box next to the page-number type to the footer.
5.  Scroll down to the bottom of the page again, and right-click in the page number cell.
6.  Select Format\>Cell.
7.  If you want the word Page along with the number (e.g., Page 1, Page 2), on the General tab in the Name box, type Page and a space (i.e., Page \[page\]).
8.  You also have the option of changing the font, color, alignment of the page number, and if you have a border around the page number or not.
9.  Change the font to Italic.
10. Select the Border tab and click the Thin drop-down list arrow and select None.
11. Click OK. Scroll down to the bottom of the page again to see the results.

> ![](pats-user-guide/161.png)

12. Click Save.

# ## Scenario \#11: Displaying long text fields 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pats-user-guide/162.png) You may notice that some of the data fields in the report are cut off. For fields that have a maximum length such as Patient name and Issue code and name, you can hover over the column until you see the left and right arrows, then left click and drag the right hand side of the column larger. There’s another way to make a field larger, which you’ll learn in this exercise.

Maximum Length Fields

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click any data cell in the Patient name column and select Format\>Cell.

> *Result: The dialogue box to format a cell pops up and opens to the General tab.*

3.  Let’s change the value of inches in the box following the caption Specify width to 1.5.

> ![](pats-user-guide/163.png) This may still cut off some patient names; you can adjust this later if you want to.

4.  Click OK.

> *Result: The cell holding the patient names is wider.*

5.  Click Save.

> ![](pats-user-guide/164.png) Patient names can be a maximum of 60 characters, so you can set the cell to a size that will be long enough to hold any patient name. But what about the Issue text or Resolution text? They can vary greatly in length.

> Variable Length Fields

1.  Right click any data cell in the column Issue text and select Format\>Cell.

> *Result: The dialogue box to format a cell will pop up, open to the General tab.*

2.  To make the cell a bit wider, change the value of inches in the box following the caption Specify width to 2.
3.  Check the box that says Wrap text.
4.  Uncheck the box that says Specify height.

> *Result: The height of the cell will increase, depending on the length of the text.*

5.  Click OK.
6.  Click the Save button.
7.  Repeat steps 1-6 for Issue Code and Name.

## Scenario \#12: The report design toolbar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Let’s go back and look at some additional features of the report tool. First, let’s return to the screen that shows us a list of all our private reports. You will see our new report on that list.

1.  Click on the Return to Private Ad Hoc Reports page link.
2.  Find and click on the report named Issues by Location n in the report listing.

![](pats-user-guide/165.png) At this point, the application has just opened the report. The default is to open the report showing the data from the last time you ran the query. You can refresh the data by clicking the Refresh bar. If your report has prompts, like the one you created, you will be prompted for new values. You can leave the dates as is or change the starting and ending date values. Then the query is re-run to refresh the data. However, you can cause the query to re-run and refresh the data each time you open the report by setting the Refresh on Open parameter.

> 3\. The application just assumes you want to see the report, but what if you want to edit it? Notice that the Edit Query button isn’t displayed in the toolbar. Click the Document drop-down list and select Edit.

> *Result: The report design toolbar displays.*

> ![](pats-user-guide/166.png)

> Document: Displays actions you can take on the entire document (report).

Save: Works the same as the Save button.

Save As: Save a second copy of the report with a different name. (Useful when you want to experiment without changing your original report, or when you want to use an existing report as the basis for a new report.)

| ![](pats-user-guide/167.png) | If you save the report to the Public folder, you must set the Property to Refresh on Open (using Document\>Properties from the toolbar), so that your data is not displayed to other sites. (You may notice that in the screen that prompts for the report title and description, there is a Refresh on Open checkbox, but there is a bug and this will not cause your data to refresh. You must edit the report and use Document\>Properties to set this feature.) |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Save to my computer \[Excel (open or save an Excel file), PDF, CSV (Excel Comma Separated Values file)\]: Allows you to save the report results in a different format on your PC.

Properties: Allows you to see the document name and description, and to set some properties. If you want the report to re-run the query and refresh the data on your report each time you open it, you can check the Refresh on Open checkbox here.

View: Let’s you control your local view of the report while editing or viewing the data. Page mode (default), Draft mode (shows the entire report), PDF mode, Left Panel (show or hide), Toolbars (show or hide the formatting, report, or formula toolbar).

Preferences: Allows you to control some elements of the behavior of the ad hoc tool. In most cases you’ll want to use the default behavior.

Insert (New row, New column, Break, Filter, Sort, Calculation): Another way of performing actions during report editing, rather than using right-click to perform the action.

Save: The first time a report is saved, you’re prompted for a report name, description, etc. After that, the Save button just saves the latest changes you’ve made.

Find: Used to search the report data for a certain value (for example, for a particular Date of Contact).

Undo: Undo the last change.

Redo: Reinstate the last change that you undid or deleted (undo the undo).

Pages: Moves you to the first page, back a page, forward a page, last page.

Edit Query: To change from Report Design mode to Edit Query mode in order to either add or delete a field available to the current report, or to change the filter on the data returned to the report.

Refresh: Refreshes the data. This re-runs the query, using the current query filter values. If there are parameters on the report, you will be re-prompted for new parameter values.

## Scenario \#13: Save a report to your PC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can save a report instance on your PC, either for a historical record, to email to a colleague, or perhaps you want to download the results to Excel in order to create graphs. You have several options: you can save to Excel, to PDF format, or to Excel as a comma separated value file. This exercise covers how to save your reports in PDF format.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  From the Document drop-down list, select Save to my computer as.
3.  Then select PDF.

> *Result: A dialogue box displays. You can Open, Save, or Cancel the PDF version of the report.*

4.  Let’s save the report. Click Save.

> *Result: You are prompted to indicate where you want to save the file on your computer. You can also change the name of the file or leave it as is.*

5.  Indicate the directory you want to save the report to. You’ll leave the name as is.
6.  Click Save.

> *Result:*

- *A dialogue box displays saying the download is complete. You can open the report or close it.*
- *If a dialogue box doesn’t display, open the report from the directory where you saved it. Then go to Step 8.*
7.  Let’s look at the PDF report. Click Open.

> *Result: The PDF report displays.*

8.  Close the report by clicking the red X in the box in the top right corner.

## Scenario \#14: Saving a public report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to share a report with other Patient Advocates. You will copy a report from your Private folder to the Public folder. All Advocates have access to the Public folder.

> 1\. At the top of the page, click on the Return to Private Ad Hoc Reports page link.

> 2\. Find Issues by Location n in the report listing.

> 3\. Click on the Share Report button.

> *Result: The message “The report was copied to the Public Ad Hoc folder” displays in green at the top of the page. The report is now available to all users.*

> Note: Using the Share Report button will cause the Refresh on Open property to be set for this report. This property must be set on all public reports to make sure that when a user opens the report; the data refreshes and they are shown only data for divisions to which they have access.

![](pats-user-guide/168.png) For this example, you’ll copy the report back into your own private folder, but keep in mind that any user could now go in to the public folder and copy this report into their private folder.

> 4\. On the Menu bar, select the Public folder.

> 5\. Locate and open the *Issues by Location* report.

> 6\. The Prompts box displays. Click the Run Query button.

> 7\. To have the report for your private use, you will move the report to your Private folder. From the Document drop-down list, select Save As.

> 8\. Enter the title with a new name, complete the description and click OK.

> *Result: The report is copied to your Private folder.*

> 9\. On the menu bar, select the Private folder and open the report.

> *Result: You have your own copy of the report. You can edit this copy if you want to; no one else will be able to view or edit it.*

## Scenario \#15: Change a column heading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can individualize your report by changing the column headings.

To change a column heading

Let’s change the Date of Contact column heading to Contact Date.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
    2.  Verify that the formula toolbar displays. (To display the formula toolbar, select View\>Toolbars\>Formula.)

> ![](pats-user-guide/169.png)

3.  Highlight the heading of the column you want to edit (Date of contact).

> *Result: The current formula displays in the text box (ex. Highlight the column heading ROC number and you will see in the formula bar, the value =NameOf(\[Date of contact\])).*

> ![](pats-user-guide/170.png)

4.  The part of the formula =NameOf( ) indicates the special function used by WEBI to return the name of an object in the universe. The value within the parenthesis is the name of the object itself. Note that object names must be surrounded by square brackets.

> Replace the current formula with the text you want to display. Replace *=NameOf(\[Date of contact\])* with *Contact Date*.

> ![](pats-user-guide/171.png)

5.  Click the green check mark to apply the change.

> ![](pats-user-guide/172.png)

6.  Click the Undo button.
7.  Click the Redo button ( ![](pats-user-guide/173.png) to the right of the Undo button).
8.  Click Save.

## Scenario \#16: Removing a section from a report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you create a section and later change your mind, you can remove the section. When you delete a section, the object is still in the Available Object list. That means that you can display the data again. You can change the design or leave it as is.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click outside the Hospital Location section cell.

> *Result: The section, delimited by a dotted line, becomes gray.*

3.  Click Remove Section.

> *Result: Hospital location sections have been deleted from the report, but Hospital location still part of the query and appears in the Available Object list.*

> ![](pats-user-guide/174.png)

4.  Click Save.
5.  From the Document drop-down list, click Edit.

![](pats-user-guide/175.png) Let’s display Hospital Locations in the main body of the report. Here is another way to add a column.

> 6\. Right click anywhere in the data and select Format\>Table.

> 7\. Select the Pivot tab.

> 8\. In the Available Objects list, double click Hospital Location.

> 9\. Click OK.

> ![](pats-user-guide/176.png)

> 10\. Click Save.

## Scenario \#17: Filter based on a list (Contacting entity)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To demonstrate a filter based on a list, you’ll add Contacting Entities to our report. Then you’ll limit the data to display only ROCs that have Congressional as a Contacting Entity.

Add data to the report

To add Contacting Entities to our report:

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click on the Edit Query button.
3.  From the PATS Universe in the left hand pane, double-click Contacting entity to move it into Result Objects pane.
4.  Click Run Query to get a new copy of the report.
5.  Click Run Query at the prompt to accept the current date range.

Result: Contacting Entity has been added to the Available Objects list.

![](pats-user-guide/177.png) Let’s display Contacting Entity in our report by adding a column.

Add a field (column) to the report

You could add a column to the report and then drag the Contacting Entity object into it as you did before, but here’s a third way to add a field to your report design.

1.  Highlight the Hospital Location column.
2.  Select Insert\>New column\>Left.
3.  From the Available Objects list, drag the blue box next to Contacting Entity to any data cell in the blank column.
4.  Click OK.

> *Result: Contacting entity displays on the report.*

> ![](pats-user-guide/178.png)

5.  Click Save.

Create the filter

To demonstrate a filter based on a list, you want to display only ROCs with Congressional contacts.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Click the Edit Query button.
3.  Highlight Contacting entity, and use the \>\>arrow to move it into Query Filters pane.
4.  At the bottom of the Query Filters pane, make sure that In List is selected in the drop-down list of possible query types.
5.  Click the Filter radio button.
6.  Click the Values button, and a new window will pop up, containing the list of available Contacting Entities.

> ![](pats-user-guide/179.png)

7.  Double-click the Congressional Contacting Entity or highlight it and use the \>\> arrow to move it into the right hand pane titled Contacting Entity in List.

> ![](pats-user-guide/180.png) You can move multiple entries (hold down the Ctrl key) into the list to filter more than one data object.

8.  Click OK.

> *Result: The filter is updated. You should see the description of the query at the top of the query pane change to Contacting Entity in List Congressional.*

9.  Click Run Query to get a new copy of the report.
10. Click Run Query at the prompt to accept the current date range.

> *Result: The report displays only ROCs with Congressional Contacting Entity.*

> ![](pats-user-guide/181.png)

11. Since only Congressional contacts display, you may want to remove the column and change the title--Congressional Issues by Institution. Right-click in any data cell in the Contacting entity column and select Remove\>Column.

> ![](pats-user-guide/182.png)

12. Click Save.

## Scenario \#18: Move captions to the left hand side of the data (508c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Let’s make one more change to the current report. By moving the captions from the top of the columns to the left hand side, the report will be more readable to a screen reader, thus making them more 508 compliant.

1.  Verify you are in the Edit mode. (To display the Edit Query button, select Document\>Edit.)
2.  Right click in any data cell and select Turn table to…
3.  From the Available Formats on the right side of the dialogue box, select Form.
4.  Click OK.

> *Result: The captions have been moved from the top of each column into the left hand side of each column. You may need to adjust the cells in order to make them wider—depending on the length of the text.*

> ![](pats-user-guide/183.png)

5.  Click Save.

# # Appendix C: Ad Hoc Report Totals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you add counts to a report, such as a count of issue codes, it’s important to be sure you’re counting the right way. For example, when counting issue codes, you usually really want to count the distinct issue codes within ROC numbers. This appendix discusses different ways of counting, and shows you how to control the formula that determines the way values will be counted in your report.

*Deciding how to count Issues*

Here’s an example of an ROC with a complicated Issue cluster of data.

<u>ROC Number Issue FSoS Employee Involved Hospital Location</u>

442.200600072 SC01 8S3 PATSemployee, One Dental

SC01 8S3 PATSemployee, One Admitting

SC02 8S3 PATSemployee, One Dental

SC02 8S3 PATSemployee, Two Admitting

SC02 8S3 PATSemployee, Three Dental

SC02 9W PATSemployee, Three Dental

SC03 9W PATSemployee, Three Emergency Room

How do we count the Issues?

- It could be 3 for 3 distinct issue codes
- It could be 4 because there are 4 distinct combinations of Issue Code and FSoS
- It could be 6 because there are 6 distinct combinations of Issue Code, FSoS, and Employee Involved
- It could be 7 because there are 7 distinct combinations of Issue Code, FSoS, Employee Involved and Hospital Location

![](pats-user-guide/184.png)Before you do any calculations, you must define what constitutes a distinct issue.*How to get totals by Issue Code, Facility Service or Section, Employee Involved, or Hospital Location*Assumption: The example below assumes that you want to count a distinct Issue Code within a ROC just one time, even if the same Issue Code appears more than once on that ROC because there are multiple FSoS, Employees Involved, or Hospital Locations associated with the same Issue Code.

![](pats-user-guide/185.png) If you want to count Issues in a different way, see section, *Other examples of counting Issues within an ROC* below.

Suppose the following three ROCs were entered on 10/31/2005. Below is a representation of how the ad hoc report data is stored:

ROC Number Issue Code FSOS

442.200600022 SC01 Acute Rehab

442.200600022 SC01 Emergency Room

442.200600022 SC02 Emergency Room

442.200600023 SC01 Emergency Room

442.200600023 SC02 Dental

442.200600023 SC02 Acute Rehab

442.200600024 AC01 Emergency Room

Suppose you want to count the number of Issue Codes for the Date of Contact 10/31/2005. By default, the ad hoc reporting tool always *counts distinct values*, which means that each unique Issue Code it encounters will be counted one time. That means that it would count the number of Issue Codes above as 3, because there are 3 distinct Issue Codes, SC01, SC02 and AC01. But that’s not the count you want.

You could change the ad hoc tool’s COUNT function to count all Issue Codes. But then it would count SC01 twice for ROC 442.200600022, and it would count SC02 twice for ROC 442.200600023. The count would be 7.

Solution: The solution is to give the ad hoc tool a way to count the distinct Issue Codes by each ROC Number. So in the COUNT formula, you put together both the ROC Number and the Issue Code, like this: =COUNT(\[ROC number\]+\[Issue code\]).

In that way, the ad hoc reporting tool counts each occurrence of Issue Code SC01 one time for each new ROC number, so you get the correct count of 5, because you’re counting the following distinct values.

- 442.200600022 SC01
- 442.200600022 SC02
- 442.200600023 SC01
- 442.200600023 SC02
- 442.200600024 AC01

![](pats-user-guide/186.png) Similarly, to get counts of Facility Service or Section, Employee Involved, or Hospital Location, you must put together the field you are trying to count with the ROC number field in the COUNT formula, in order to count distinct values of that field by ROC.  
*Other examples of counting Issues within an ROC*

Here’s the example shown at the beginning of the Appendix.

<u>ROC Number Issue FSoS Employee Involved Hospital Location</u>

442.200600072 SC01 8S3 PATSemployee, One Dental

SC01 8S3 PATSemployee, One Admitting

SC02 8S3 PATSemployee, One Dental

SC02 8S3 PATSemployee, Two Admitting

SC02 8S3 PATSemployee, Three Dental

SC02 9W PATSemployee, Three Dental

SC03 9W PATSemployee, Three Emergency Room

The formula you will use to count the Issues depends on what you want to consider as an Issue. We previously showed you the formula for counting just distinct issue codes within an ROC.

1.  Suppose you want to consider a distinct issue to be a combination of the Issue Code and the associated Facility Service or Section. In other words, if the same issue code appears on an ROC twice, because there are two different FSoS associated with it, then you want to count is as 2 issues rather than 1. In the above example, that would result in a count equal to 4.

> Use the formula:=COUNT(\[ROC number\]+\[Issue code\]+\[Facility service or section\]).

2.  If you want to consider a distinct issue to a combination of the Issue Code, the associated Facility Service or Section, the Employee Involved, and the Hospital Location.

> Use the formula:=COUNT(\[ROC number\]+\[Issue code\]+\[Facility service or section\]+\[Employee Involved\]+\[Hospital location\]).

So you must be very clear on what you’re trying to count, and you must tell the ad hoc reporting tool exactly what you want to count in your formula.

*How WebIntelligence Counts*

The COUNT function is provided by WebIntelligence (WEBI) to help you displays counts of fields in your report. The function looks like this: COUNT(…).

- Within the parenthesis, you must tell WEBI what to count.
- The object name is indicated by including square brackets around the name.
- By default, WEBI will count *distinct instances* of whatever you have included within the parenthesis.
- In many cases, you will be counting issues within an ROC.

  
You must decide exactly what constitutes a *distinct issue* to you.

- Is it just the issue code?
- If the same issue code appears twice on a ROC with two different FSoS, does that count as two issue codes or one?
- How about when there are multiple employees for the same issue code, or multiple hospital locations?

However you decide to count an issue, you must let WEBI know exactly what you want to count, by including the name of all fields that count as an issue to you.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

508c, 86
Action Request Notification
add comment, 33
change days to respond, 30
employee response, 31
modify, 33
receive employee response, 32
send, 28
send comment to employee, 33
when closing ROC, 41
activate
comps, 97
Congressional contacts, 93
Contacting entity, 115
Facility Service or Section, 101
Hospital locations, 95
Issue category, 106
Issue codes, 108
Methods of contact, 110
Treatment status, 113
ad hoc reports, 57
508c, 86
add column, 71, 72
Between filter, 66
break footer, 76
build query, 60
cell, 60
change column heading name, 73
copy from Public folder, 88
create filters, 62
create query, 60
create section, 74
define fields, 60
delete column, 73
delete section, 77
design, 57, 70
filter definitions, 63
font size, 58
header and footer, 78
Is not null filter, 65
long text fields, 77
move objects, 61
objects, 59
page numbers, 79
panes, 59
prompt, 80
query, 57
rearrange objects, 70
refresh on open, 87
save to PC, 85
share reports, 86
sort items, 75
sort objects, 74
subtotals and totals, 83
table, 60
time out, 62
title, 78
toolbar, 60, 69
universe, 58
add
column, 71, 72
comps, 96
Congressional contacts, 92
contact information, 10
Contacting entity, 114
cover sheet, 10
Employee involved, 38
Facility Service or Section, 99
header and footer, 78
Hospital locations, 94
Issue category, 104
Issue codes, 35, 107
Issue text, 13
Methods of contact, 109
page numbers, 79
patient information, 11
prompt, 80
report title, 78
Resolution text, 97
section, 74
Treatment status, 111
administrator tasks
activate comps, 97
activate Congressional contacts, 93
activate Facility Service or Section, 101
activate Hospital locations, 95
activate Issue category, 106
activate Issue codes, 108
add comps, 96
add Congressional contacts, 92
add Facility Service or Section, 99
add Hospital locations, 94
add Issue category, 104
add Issue codes, 107
add Resolution text, 97
delete Resolution text, 99
edit comps, 96
edit Congressional contacts, 92
edit Facility Service or Section, 100
edit Hospital locations, 94
edit Issue category, 105
edit Issue codes, 108
edit Resolution text, 98
inactivate comps, 97
inactivate Congressional contacts, 93
inactivate Facility Service or Section, 101
inactivate Hospital locations, 95
inactivate Issue category, 106
inactivate Issue codes, 108
Between filter, 66
break footer, 76
button
History, 48
Schedule, 48
View Latest Instance, 48
buttons
Cancel, 60
Filter, 66
Run Query, 60
Update Filter, 65
calendar icons, 7
Cancel button, 8, 60
canned reports. *See* standard reports
cell, 60
change
Contacting entity, 23
Contacting entity sort order, 115
cover sheet, 22
Date of contact, 22
Issue category sort order, 105
Methods of contact, 23
Methods of contact sort order, 110
name of column heading, 73
Treatment status sort order, 112
Chart and Table Types, 78
close ROC, 40
ARN comments, 41
reopen, 42
columns
add, 71, 72
change heading name, 73
delete, 73
rearrange, 70
comps
activate, 97
add, 96
edit, 96
inactivate, 97
Congressional contacts, 11
activate, 93
add, 92
edit, 23, 92
inactivate, 93
Contact information, 10
change, 22
Contacting entity, 10
activate, 115
add, 114
change, 23
change sort order, 115
edit, 115
inactivate, 116
Cover sheet, 10
change, 22
Congressional contacts, change, 23
Contacting entity, change, 23
Date of contact, change, 22
Info taken by change, 22
Methods of contact, change, 23
Phone/fax number, change, 23
create filters, 62
create ROC, 9
create section, 74
Date of contact, 10
change, 22
date range
calendar icon, 7, 67
filter, 66
prompt, 80
define ad hoc fields, 60
delete
column, 73
Employee involved, 39
Issue codes, 37
patient, 24
Resolution text, 99
ROC, 43
section, 77
design ad hoc report, 70
desktop shortcut, 3
drop-down list, viii
edit
comps, 96
Congressional contacts, 23, 92
Contacting entity, 23, 115
Date of contact, 22
Employee involved, 37
Facility Service or Section, 100
Hospital locations, 94
Info taken by, 22
Issue category, 105
Issue codes, 108
Issue Text, 25
Methods of contact, 23, 110
patient information, 23
Phone/fax number, 23
Resolution text, 98
ROC, 17
Treatment status, 113
Employee involved
add, 38
delete, 39
export
standard reports, 54
Facility Service or Section
activate, 101
add, 99
edit, 100
inactivate, 101
filters
Between, 66
commands, 63
create, 62
Is not null, 65
using calendar icon, 67
Find ROC, 18, 21
all open ROCs, 21
by date range, 19
by employee involved, 19
by information taker, 19
by patient name, 18
by ROC number, 20
your open ROCs, 21
font size, 58
footer, 78
formula toolbar, 74
header, 78
Hospital locations
activate, 95
add, 94
edit, 94
inactivate, 95
inactivate
comps, 97
Congressional contacts, 93
Contacting entity, 116
Facility Service or Section, 101
Hospital locations, 95
Issue category, 106
Issue codes, 108
Methods of contact, 111
Treatment status, 113
inactivity, 4
Info taken by, 10
change, 22
Informational notification, 25
add, 25
send, 25
view, 27
Is not null filter, 65
Issue category
activate, 106
add, 104
change sort order, 105
edit, 105
inactivate, 106
Issue codes
activate, 108
add, 35, 107
counting, 83
delete, 37
delete Employee involved, 39
edit, 37, 108
inactivate, 108
more than one employee involved, 39
select by Issue category, 35
Issue text
add, 13
change, 25
valid characters, 13, 25
keep section together, 76
log in, 2
logging onto PATS, 2
Login page, vi, 2
long text fields, 77
Main page, vii
NPO, vii
maintenance
comps, 95
Congressional contacts, 92
Facility Service or Section, 99
Hospital locations, 93
Resolution text, 97
maintenance (NPO)
Contacting entity, 113
Issue category, 103
Issue codes, 106
Methods of contact, 109
overdue ROC, 116
Treatment status, 111
menu bar, viii
Methods of contact, 10
activate, 110
add, 109
cannot delete, 109
change, 23
change sort order, 110
edit, 110
inactivate, 111
move objects, 61
naming conventions, vi
drop-down list, viii
menu bar, viii
PATS Login page, vi
PATS Main page, vii
navigation, 8
new ROC, 9
notifications
change default days to respond, 30
employee response, 31
modify action request, 33
receive employee response, 32
send action request notification, 28
send informational notification, 25
view informational notification, 27
NPO user
activate Contacting entity, 115
activate Issue codes, 108
activate Methods of contact, 110
activate Treatment status, 113
active Issue category, 106
add Contacting entity, 114
add Issue category, 104
add Issue codes, 107
add Methods of contact, 109
add Treatment status, 111
edit Contacting entity, 115
edit Issue category, 105
edit Issue codes, 108
edit Methods of contact, 110
edit Treatment status, 113
inactivate Contacting entity, 116
inactivate Issue category, 106
inactivate Issue codes, 108
inactivate Methods of contact, 111
inactivate Treatment status, 113
objects, 59
Available objects, 72, 77
group within section, 76
move, 61
rearrange, 70
online help, 8
page numbers, 79
panes, 59
Query Filters, 60
Result Objects, 59
patient information, 11
change, 23
delete patient, 24
update, 24
Patient Lookup, 12
Patient Lookup Status Notification, 12
PATS
overview, 1
PATS Main page, vii
NPO, vii
Person Service Lookup, 11
documentation, 12
Person Service Lookup tool, 18, 24
Phone/fax number, 11
change, 23
Pivot, 70
print
standard reports, 56
prompt, 80
Ending date, 80, 82
Starting date, 80
Public folder
copy reports, 88
rearrange objects, 70
Redo, 70
Refresh, 70
refresh on open, 87
reopen ROC, 42
report design
add column, 71, 72, 73
rearrange objects, 70
Report Details page, 48
Report of contact. *See* ROC
report query, 60
report title, 78
report toolbar, 69
ad hoc reports, 60
standard report, 53
reports. *See* ad hoc reports, *See* standard reports
reports
schedule, 49
reports
refresh on open, 87
required fields, 7
Resolution text, 41
add, 97
delete, 99
edit, 98
valid characters, 98
resources, viii
ROC
add, 9
close, 40
delete, 43
reopen, 42
summary information, 14
ROC number, format, 14, 20
Run Query button, 60
Save as, 69
schedule reports, 49
date range, 50
employee involved, 51
Facility Service or Section, 51
patient, 51
ROC number, 52
run later, 52
run now, 52
Search for ROC
all open ROCs, 21
date range, 19
employee involved, 19
information taker, 19
patient name, 18
ROC number, 20
your open ROCs, 21
section
create, 74
delete, 77
group objects within, 76
keep together, 76
sections to read, vi
Set as section, 75
share reports, 86
shortcut, 3
sort order
change Methods of contact, 110
Contacting entity, 115
Issue category, 105
Treatment status, 112
standard reports, 45
buttons, 48
categories, 45
conventions, 46, 49
data displays on report, 49
date range parameter, 50
employee involved parameter, 51
export, 54
Facility Service or Section parameter, 51
History button, 48
menu bar, 46
patient parameter, 51
print, 56
Report Details page, 48
Reports Folder page, 46
ROC number parameter, 52
schedule, 52
schedule reports, 47, 49
selection criteria, 50
terminology, 46, 49
toolbar, 53
View Latest Instance button, 48
Summary page, 14
table, 60
time out, 4, 62
title of report, 78
title on every page, 79
toolbar
ad hoc reports, 60, 69
formula, 74
standard reports, 53
Treatment status, 11, 12, 13, 24, 111, 112
activate, 113
add, 111
change sort order, 112
edit, 113
inactivate, 113
Undo, 70
universe, 58
update patient information, 24
User Settings, 3, 4
VSSC, 109, 110, 111, 113, 114, 115
VSSC code, 109, 112, 114
wrap text, 77
