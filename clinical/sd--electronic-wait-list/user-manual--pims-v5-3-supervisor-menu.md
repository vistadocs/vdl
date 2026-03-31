---
title: PIMS Version 5.3 Supervisor Menu User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Supervisor Menu
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3
group_key: "SD:SD:5.3"
file_numbers: 
  - 407
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - clinic
  - appointment
  - table
  - contents
  - date
  - resource
  - report
  - edit
  - scheduling
  - time
page_count: 0
word_count: 10120
section_count: 10
table_count: 0
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: December 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/PIMS_User_Manual-Supervisor_Menu.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/PIMS_User_Manual-Supervisor_Menu.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

Department of Veterans AffairsOffice of Information and Technology (OIT)

![](pims-version-5-3-supervisor-menu-user-manual/001.png)

Patient Information Management System (PIMS)Scheduling Module Supervisor MenuUSER MANUALVersion 5.3

December 2020

Scheduling Module User Manual Supervisor Menu

Add/Edit a Holiday

Appointment Inquiry

Appointment Status Update Menu

> Appointment Status Update

> Print Appointment Status Update (Date Range)

> Purge Appointment Status Update Log File

> View Appointment Status Update Date (Single Date)

Appointment Waiting Time Report

Appointments with missing resources

Appointments with no resource report

Automatically Fix Appointments with No Resource

Cancel Clinic Availability

Change Patterns to 30-60

Clinics without matching resource list

Clinic Edit Log Report

Convert Patient File Fields to PCMM

Create a resource

Create/Edit Local Cancellation Comments

Current MAS Release Notes

Edit Clinic Stop Code Name- Local Entries Only

Edit Resource

Edit resource for an appointment

Encounter Inquiry

Enter/Edit Letters

Inactivate a Clinic

List Appointments and Encounters by status

Look Up on Clerk Who Made Appointment

Manually Fix Appointments with No Resource

Non-Conforming Clinics Stop Code Report

<span id="p586_title" class="anchor"></span>Pending RTC Cleanup – by Date

Pending RTC Cleanup - FULL

Print Clinic Installation Checklist

Purge Scheduling Data

Reactivate a Clinic

Release Appointment Request Locks

Remap Clinic

Resource Inquiry

Restore Clinic Availability

Scheduling Parameters

Set up a Clinic

Sharing Agreement Category Update

VS GUI Help Pane Edit

Wait List (Sch/PCMM) Utilities

> Inter-Facility Transfer Request

> Inter-Facility Transfer Accept

> Wait List Batch Clinic Change

> Wait List Enter/Edit as a Scheduling Reminder

> Open Closed EWL Entry

Revision History

Initiated on 04/11/05

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 51%" />
<col style="width: 16%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description (Patch # if applic.)</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>10/14/2020</td>
<td><p>VistA Scheduling Graphical User Interface (VS GUI) patch:</p>
<p>Release 1.7.1 R1/SD*5.3*745 and 751 released 10/1/20</p>
<p>Release 1.7.2.1 R2/SD*5.3*756 and 757 released 12/9/2020 2020</p></td>
<td>REDACTED</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>07/2020</td>
<td><p>VistA Scheduling Graphical User Interface (VS GUI) patches:</p>
<p>SD*5.3*723 released 11/6/19</p>
<p>SD*5.3*731 released 11/19/19</p>
<p>SD*5.3*734 released 12/9/19</p>
<p>Release 1.6.0 released 12/17/19</p>
<p>SD*5.3*732 IOC only release 11/20/19</p>
<p>SD*5.3*740 released 1/30/20</p>
<p>SD*5.3*737 released 3/9/20</p>
<p>SD*5.3*744 released 3/25/20</p>
<p>SD*5.3*755 IOC only release 6/8/20</p>
<p>Release 1.7.0.2/SD*5.3*694/695/762 released 8/19/20</p></td>
<td>REDACTED</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>10/2018</td>
<td>SD*5.3*705 – modified Scheduling Site Parameters and Division Parameters (p. <a href="#p75">75</a>, <a href="#p76">76</a>).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>09/2018</td>
<td>SD*5.3*682 and OR*3.0*483 Remove/hides Auto-rebook to prevent new entries and RTC comments/error messages improved</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/2018</td>
<td><p>SD*5.3*680 – modified the salutation of Scheduling letters to display the patients name rather than Mr/Ms (p. <a href="#p64">64</a></p>
<p><a href="https://www.va.gov/vdl/documents/Clinical/Scheduling/User%20Manual%20-%20Supervisor%20Menu%20PIMS%20(3).doc">https://www.va.gov/vdl/documents/Clinical/Scheduling/User Manual - Supervisor Menu PIMS (3).doc</a>)</p></td>
<td>REDACTED</td>
<td>REDACTED (SQA Manager)</td>
</tr>
<tr class="odd">
<td>09/2017</td>
<td>SD*5.3*646 - changed prompt text for ALLOW DIRECT PATIENT SCHEDULING?: (p. <a href="#p37">37</a>) and DISPLAY CLIN APPT TO PATIENTS? (p. <a href="#p37_2">37</a>)</td>
<td>REDACTED</td>
<td>REDACTED (SQA Manager) &amp; REDACTED (Developer)</td>
</tr>
<tr class="even">
<td>07/2015</td>
<td><p>SD*5.3*635 – Added to the description of basic clinic information established through the Set up a Clinic option. (p. <a href="#print-clinic-installation-checklist---example"><u>30</u></a>)</p>
<p>Added description of new fields that appear during entry of a new clinic. (p. <a href="#p586_81"><u>25</u></a>)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/2014</td>
<td><p>SD*5.3*622 – Added new fields for printing the default provider and clinic location on Scheduling letters (p. <a href="#enteredit-letters"><u>14</u></a>), file #407.5</p>
<p>Added mail group for notification of clinic inactivation (p. <a href="#p64"><u>14</u></a>), option Inactivate a Clinic</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>07/2014</td>
<td><p>SD*5.3*586 – Added new option to the Supervisor Menu: Print Clinic Installation Checklist report, (<a href="#p586_title">Title page</a>)</p>
<p>Added ICD-10 update regarding the new Print Clinic Installation report, (p. <a href="#ICD10p86">86</a>)</p>
<p>Added Print Clinic Installation Checklist Example, (p. <a href="#print-clinic-installation-checklist---example">87</a>)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/25/10</td>
<td>SD*5.3*568 – Added two new options to the SDSUP menu: “Edit Clinic Stop Code Name- Local Entries Only” option and the “Clinic Edit Log Report” option.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/27/10</td>
<td>SD*5.3*547 – Update to: Non-Conforming Clinics Stop Code Report</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/14/08</td>
<td>Minor Formatting Changes</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/31/06</td>
<td><p>SD*5.3*478 - Consult/Scheduling Appointment Link</p>
<p>Updated Cancel Clinic Availability option</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/13/05</td>
<td><p>SD*5.3*398 – updated option</p>
<p>Cancel Clinic Availability</p></td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/11/05</td>
<td><p>SD*5.3*380 – updated options:</p>
<p>Inactivate a Clinic</p>
<p>Reactivate a Clinic</p>
<p>Set up a Clinic</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

Table of Contents

List of Figures

[Figure 1: Print Clinic Installation Checklist - Example [31](#_Toc54010299)](#_Toc54010299)

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Add/Edit a Holiday](#addedit-a-holiday)
- [Appointment Inquiry](#appointment-inquiry)
- [Appointment Status Update Menu](#appointment-status-update-menu)
    - [Appointment Status Update](#appointment-status-update)
- [### Print Appointment Status Update (Date Range)](#print-appointment-status-update-date-range)
    - [Purge Appointment Status Update Log File](#purge-appointment-status-update-log-file)
- [# Appointment Waiting Time Report](#appointment-waiting-time-report)
- [Appointments With Missing Resources](#appointments-with-missing-resources)
- [Appointments With No Resource Report](#appointments-with-no-resource-report)
- [Automatically Fix Appointments with No Resource](#automatically-fix-appointments-with-no-resource)
- [Cancel Clinic Availability](#cancel-clinic-availability)
- [The option provides the capability to print cancellation letters at this time. A cancellation letter must have been previously entered through the Enter/Edit Letters option and assigned to the clinic being cancelled through the Set up a Clinic option. This letter will notify patients of the appointment cancellation and the new date/time scheduled. A list of patients with a Bad Address indicator will print after the cancellation letters have printed. Letters for these patients will not print.](#the-option-provides-the-capability-to-print-cancellation-letters-at-this-time-a-cancellation-letter-must-have-been-previously-entered-through-the-enteredit-letters-option-and-assigned-to-the-clinic-being-cancelled-through-the-set-up-a-clinic-option-this-letter-will-notify-patients-of-the-appointment-cancellation-and-the-new-datetime-scheduled-a-list-of-patients-with-a-bad-address-indicator-will-print-after-the-cancellation-letters-have-printed-letters-for-these-patients-will-not-print)
- [# Change Patterns to 30-60](#change-patterns-to-30-60)
- [Clinic Edit Log Report](#clinic-edit-log-report)
- [# Clinics Without Matching Resource List](#clinics-without-matching-resource-list)
- [Convert Patient File Fields to PCMM](#convert-patient-file-fields-to-pcmm)
- [Create/Edit Local Cancellation Comments](#createedit-local-cancellation-comments)
- [Create a Resource](#create-a-resource)
- [Current MAS Release Notes](#current-mas-release-notes)
- [Edit Clinic Stop Code Name – Local Entries Only](#edit-clinic-stop-code-name-local-entries-only)
- [# Edit Resource](#edit-resource)
- [Edit resource for an appointment](#edit-resource-for-an-appointment)
- [Encounter Inquiry](#encounter-inquiry)
- [Enter/Edit Letters](#enteredit-letters)
- [Inactivate a Clinic](#inactivate-a-clinic)
- [List Appointment and Encounters By Status](#list-appointment-and-encounters-by-status)
- [Look Up on Clerk Who Made Appointment](#look-up-on-clerk-who-made-appointment)
- [# Manually Fix Appointments with No Resource](#manually-fix-appointments-with-no-resource)
- [Non-Conforming Clinics Stop Code Report](#non-conforming-clinics-stop-code-report)
- [Pending RTC Cleanup – by Date](#pending-rtc-cleanup-by-date)
- [Pending RTC Cleanup – Full](#pending-rtc-cleanup-full)
- [Print Clinic Installation Checklist](#print-clinic-installation-checklist)
- [Purge Scheduling Data](#purge-scheduling-data)
- [Reactivate a Clinic](#reactivate-a-clinic)
- [Release Appointment Request Locks](#release-appointment-request-locks)
- [Remap Clinic](#remap-clinic)
- [The following message may appear on the output.](#the-following-message-may-appear-on-the-output)
- [# Resource Inquiry](#resource-inquiry)
- [Restore Clinic Availability](#restore-clinic-availability)
- [# Scheduling Parameters](#scheduling-parameters)
  - [Site Parameters](#site-parameters)
- [> API NOTIFICATIONS TO PROCESS](#api-notifications-to-process)
  - [Division Parameters](#division-parameters)
  - [Clinic Print Manager](#clinic-print-manager)
  - [## Division Print Manager](#division-print-manager)
- [# Set up a Clinic](#set-up-a-clinic)
- [Print Clinic Installation Checklist - Example](#print-clinic-installation-checklist-example)
- [Sharing Agreement Category Update](#sharing-agreement-category-update)
- [VS GUI Help Pane Edit](#vs-gui-help-pane-edit)
- [# Wait List (Sch/PCMM) Utilities](#wait-list-schpcmm-utilities)
  - [Inter-facility Transfer Request](#inter-facility-transfer-request)
  - [Inter-Facility Transfer Accept](#inter-facility-transfer-accept)
  - [Wait List Batch Clinic Change](#wait-list-batch-clinic-change)
  - [Wait List Enter/Edit As A Scheduling Reminder](#wait-list-enteredit-as-a-scheduling-reminder)
  - [Open Closed Ewl Entry](#open-closed-ewl-entry)
The Supervisor Menu provides the capability for supervisors and their designees to set up and maintain the Scheduling module. The following is a brief description of the options included in the Supervisor Menu.
ADD/EDIT A HOLIDAY
This option is used to add, edit, and delete holidays to or from the HOLIDAY file.
APPOINTMENT INQUIRY
This option was created as part of a suite of VistA Scheduling (VS) Graphical User Interface (GUI) utility options and reports to allow sites to correct missing or mismatched hospital location clinics and VS GUI resources. This option performs FileMan inquiry in the SDEC APPOINTMENT (#409.84) file that supports VS GUI for users who do not have FileMan inquiry access.
APPOINTMENT STATUS UPDATE MENU
This menu contains options for supervisors to assist in correcting or managing appointment status.
APPOINTMENT STATUS UPDATE
This option is used by the supervisor to update the status of appointments within a specified date range.
PRINT APPOINTMENT STATUS UPDATE (DATE RANGE)
This option is used to produce a report showing the status update history in the APPOINTMENT STATUS UPDATE LOG file for each individual date in a specified date range.
PURGE APPOINTMENT STATUS UPDATE LOG FILE
This option is used to purge data within a specified date range from the APPOINTMENT STATUS UPDATE LOG file.
VIEW APPOINTMENT STATUS UPDATE DATE (SINGLE DATE)
This option is used to view the status update history for a specified date in the APPOINTMENT STATUS UPDATE LOG file.
APPOINTMENT WAITING TIME REPORT
This option is used to show the waiting times for patients with scheduled appointments.
APPOINTMENTS WITH MISSING RESOURCES
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This report option will provide a list of appointments that have a resource issue which needs to be resolved.
APPOINTMENTS WITH NO RESOURCE REPORT
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This report option identifies appointments with no resource that may require correction. This report uses the same criteria as the Automatically Fix Appointments with No Resource option without automatically fixing the appointments.
AUTOMATICALLY FIX APPOINTMENTS WITH NO RESOURCE
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. It will check for existing appointments with resource issues and will automatically fix any appointment that is an exact match. It will also display appointments that may potentially require the site to fix manually.
CANCEL CLINIC AVAILABILITY
This option is used to cancel a clinic's availability for either a whole day or portions of a day.
CHANGE PATTERNS TO 30-60
This option is used to change patterns which had been created with 15-minute increments to the 30-60 minute increment pattern.
CLINIC EDIT LOG REPORT
Option was added by patch SD\*5.3\*568. This option may not appear on the SDSUP menu.
This option will allow you to identify changes made to entries in the HOSPITAL LOCATION file (#44). This report is sorted by USER NAME or by DATE CHANGED and will identify the field changed. Each change is reported individually and includes the old and new values along with identifying who made the change. NOTE: This option will not be assigned to any given menu in the SD namespace at this time; however, it can be assigned to any menu or individual user as needed.
CLINICS WITHOUT MATCHING RESOURCE LIST
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option is used to identify clinic locations that have a missing or mismatched resource in the VS GUI files.
CONVERT PATIENT FILE FIELDS TO PCMM
This option is used to convert the primary care data manually entered prior to the release of the PCMM software.
CREATE/EDIT LOCAL CANCELLATION COMMENTS
Use this option to create or edit a local cancellation comments that appear in VS GUI’s Cancel Appointment Dialog box.
CREATE A RESOURCE
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option allows the site to create a VS GUI resource for any active clinic missing a resource.
CURRENT MAS RELEASE NOTES
This option is used to generate a copy of the current release notes for the MAS product.
EDIT CLINIC STOP CODE NAME-LOCAL ENTRIES ONLY
This option will allow the user to edit only the NAME field for CLINIC STOP (#40.7) file. Only those entries identified as “local” may be edited.
EDIT RESOURCE
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option allows the site to correct any active clinic with a mismatch between the LOCATION NAME and RESOURCE NAME identified in the Clinic without Matching Resource List output.
EDIT RESOURCE FOR AN APPOINTMENT
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option allows a site to directly fix the resource of a single appointment using the appointment’s internal entry number (IEN).
ENCOUNTER INQUIRY
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option provides FileMan encounter inquiry for users without access to FileMan.
ENTER/EDIT LETTERS
This option is used to enter individual letters under the following four letter types: Pre-appointment, Appointment Cancelled, No-Show, and Clinic Cancelled.
INACTIVATE A CLINIC
This option is used to render a clinic inactive (no activity allowed) as of a selected date. Once the clinic is inactivated, it will remain so until it is reactivated through the Reactivate a Clinic option.
LIST APPOINTMENT AND ENCOUNTERS BY STATUS
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option lists all patient appointment-encounter-appointment
file triples that match user selected status values for each file.
LOOK UP ON CLERK WHO MADE APPOINTMENT
This option is used to view information on a selected appointment.
MANUALLY FIX APPOINTMENTS WITH NO RESOURCE
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option lists appointments with null resources, determines if there is a likely match by looking into the PATIENT File (#2) and then prompts the user to fix the appointment or bypass it.
NON-CONFORMING CLINICS STOP CODE REPORT
This option is used to list clinics in the HOSPITAL LOCATION file that do not conform to the stop code restriction types. Additionally, the report will include clinics that contain stop codes (i.e. primary, secondary, or both) that have been inactivated and the effective date of the inactivation.
PENDING RTC CLEANUP – BY DATE
This option closes pending Return to Clinic (RTC) orders in the Computerized Patient Record System (CPRS) where the VS GUI Appointment Request has been closed or dispositioned for a user selected date range.
PENDING RTC CLEANUP – FULL
This option closes pending RTC orders in CPRS where the VS GUI Appointment Request has been closed or dispositioned.
PRINT CLINIC INSTALLATION CHECKLIST
For the ICD-10 implementation of VistA Scheduling, the *Supervisor menu* option provides a new report, Print Clinic Installation Checklist, which contains the following information:
Clinic
Diagnosis (both ICD9 and ICD10 codes)
Short Description
Default (Y/N)
PURGE SCHEDULING DATA
This option is used to delete various non-essential nodes created by the Scheduling module in the HOSPITAL LOCATION and PATIENT files.
REACTIVATE A CLINIC
This option is used to reactivate clinic availability for any clinic which has been inactivated through the Inactivate a Clinic option.
RELEASE APPOINTMENT REQUEST LOCKS
Option Release Appointment Request Locks is used to unlock a request that is locked in VS GUI, but not currently being modified by any user. This option will only remove scheduling locks, not locks in the Orders files (consults, procedures, some RTCs, etc.)
REMAP CLINIC
This option is used to reset the clinic availability patterns of established clinics. It updates the pattern to insure knowledge of a holiday or deletion of a holiday.
RESOURCE INQUIRY
This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option users to view VS GUI resource file inquiry without FileMan access.
RESTORE CLINIC AVAILABILITY
This option is used to restore the availability for a previously cancelled clinic.
SCHEDULING PARAMETERS
This option is used to display and edit the Scheduling site parameters.
SET UP A CLINIC
This option is used to define/edit clinic parameters and establish appointment availability patterns for the clinics.
SHARING AGREEMENT CATEGORY UPDATE
This option is used to define subcategories for appointment types and assign them as active status.
VS GUI HELP PANE EDIT
This option is used to add, edit, or remove local links in the VistA Scheduling Graphical User Interface (VS GUI) Help Pane in the Ribbon Bar.
WAIT LIST (Sch/PCMM) UTILITIES
This option is addressed in the Electronic Wait List User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>
INTER-FACILITY TRANSFER REQUEST
This option is addressed in the Electronic Wait List User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>
INTER-FACILITY TRANSFER ACCEPT
This option is addressed in the Electronic Wait List User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>
WAIT LIST BATCH CLINIC CHANGE
This option is addressed in the Electronic Wait List User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>
WAIT LIST ENTER/EDIT AS A SCHEDULING REMINDER
This option is addressed in the Electronic Wait List User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>
OPEN CLOSED EWL ENTRY
This option is addressed in the Electronic Wait List User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>

# Add/Edit a Holiday

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add/Edit a Holiday option is used to add/edit/delete holidays. It is important to note that clinics affected by changes to holiday dates must be remapped. Remapping updates the clinic pattern to insure inclusion or exclusion of the holiday.

# Appointment Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched hospital location clinics and VS GUI resources. This option performs FileMan inquiry in the SDEC APPOINTMENT (#409.84) file that supports VS GUI for users who do not have FileMan inquiry access.

# Appointment Status Update Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Appointment Status Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Appointment Status Update option is used by the Scheduling supervisor to update the status of outpatient encounters (appointments, add/edits, and dispositions) within a specified date range.

> A status of NO ACTION TAKEN or ACTION REQUIRED is assigned to any encounter within the specified date range that has not been checked in, checked out, no-showed or cancelled. These appointments will not be transmitted to the National Patient Care Database (NPCDB) to Austin.

> Normally, the system should be set up to automatically execute this function by running the SDAM BACKGROUND JOB. This background job should be queued to run daily. If, however, this daily background job fails to run or does not complete the update, you may use this option to execute the update functionality.

> You are prompted for a date range. The date range entered must be in the past, beginning on 6/1/92 or later and ending no later than the current date. You are also prompted for a date/time to queue the update. Once the update function has been queued, it will be assigned an internal task number. This is the number you would use to identify the task to Office of Information Technology (OIT) should problems occur.

> Both the background job and this option generate a MailMan message to the mail group specified by the APPT. UPDATE MAIL GROUP site parameter. The message includes the following information: the start and finish date/time for the job, date range covered by the update, clinic or stop code name, number of outpatient encounters that require action, total number of appointments, stops, and dispositions, and the percentage of each with a status of NO ACTION TAKEN or ACTION REQUIRED.

# ### Print Appointment Status Update (Date Range)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Print Appointment Status Update (Date Range) option is used to produce a report showing the status update history in the APPOINTMENT STATUS UPDATE LOG file for each individual date in a specified date range.

> You will be prompted to select a date range and a device. If the appointment status update process has not been accomplished for any date within the selected date range, that date will not appear in the output.

> An Appointment Status Log will be displayed showing the following information for the specified date:

- Appointment Date - date specified by user
- Date Update Started - date/time the appointment status update process was begun
- Completed - date/time the appointment status update process was completed
- Method - will be either DAILY BACKGROUND JOB (if update process was accomplished automatically) or MANUALLY QUEUED (if update process was generated through the Appointment Status Update option)
- By - user who generated the status update process

### Purge Appointment Status Update Log File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Purge Appointment Status Update Log File option is used to purge data within a specified date range from the APPOINTMENT STATUS UPDATE LOG file.

> You will be prompted for a date range. The selected time frame cannot be later than the current fiscal year plus one fiscal year. For example, if today's date is March 18, 1997, you may only select a date range before September 30, 1995 (current FY97 plus FY96). Remember, September 30 is the last day of the fiscal year.

> Once the output has been queued, it will be assigned an internal task number. This is the number you would use to identify the task to IRM service should problems occur.

> A MailMan bulletin will be generated to the user who purged the data. It will appear as NEW mail and will show the date/time the appointment status update log purge was completed, and the total number of records purged within the selected date range.

#### ### View Appointment Status Update Date (Single Date)

> The View Appointment Status Update Date (Single Date) option is used to view the status update history for a specified date in the APPOINTMENT STATUS UPDATE LOG file.

> You will be prompted to select a single appointment date. You will only be allowed to select a date for which the appointment status update process has been accomplished. The default date at this prompt will be LAST, allowing you to select the last date the appointment status update process was generated.

> An Appointment Status Log will be displayed showing the following information for the specified date.

#### Appointment Date - date specified by user

#### Date Update Started - date/time the appointment status update process was begun

#### Completed - date/time the appointment status update process was completed

#### Method - will be either DAILY BACKGROUND JOB if update process was accomplished automatically) or MANUALLY QUEUED (if update process was generated through the Appointment Status Update option)

#### By - user who generated the status update process

# # Appointment Waiting Time Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Appointment Waiting Time Report option is used to show the waiting times for patients with scheduled appointments. The patient must have been checked-in and checked-out to appear on the output.

You may choose a full report (containing individual patient names, appointment dates/times, check-in/check-out dates/times) or a totals report only.

The top level sort of any report will be by division. Second level sort choices include the following.

Clinic, patient

Clinic, appointment date/time

Stop code, clinic

Stop code, patient

Patient, appointment date/time

If choosing to sort by clinic or stop code, all or up to 20 individual clinics/stop codes may be selected. When choosing the last sort selection, all patients will be included.

Definitions of the data elements used on the report are provided as part of the output. You must print the output at 132 col. margin width.

# Appointments With Missing Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched HOSPITAL LOCATION File (#44) clinics and VS GUI resources in SDEC RECOURCE File (#409.831).  This report option will provide a list of appointments that have a resource issue which needs to be resolved.

The report output displays the Internal Entry Number (IEN) of the appointment, the appointment start time, patient name, clinic location, and number of data points in agreement between the PATIENT File (#2) and the SDEC APPOINTMENT File (#409.84).

Step by step instructions for this option are in the VS GUI User Guide. At time of publishing, the information is in Appendix G.5.1 of the 1.6 VS GUI User Guide, page 209.

The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

# Appointments With No Resource Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched HOSPITAL LOCATION File (#44) clinics and VS GUI resources in SDEC RECOURCE File (#409.831).  This report option identifies appointments with no resource that may require correction. This report uses the same criteria as the Automatically Fix Appointments with No Resource \[SDEC NO RES APPT AUTO FIX\] option without automatically fixing the appointments.

This option allows the site to review the discrepancies between the PATIENT File (#2), HOSPITAL LOCATION File (#44), and the SDEC APPOINTMENT File (#409.84). The report will display the appointment date and time, the IEN in parenthesis, the patient name, clinic location, and the results of comparing the data points in columns labeled SOURCE, STATUS, DATE MADE, and MADE BY.

Step by step instructions for this report option are in the VS GUI User Guide. If any are found, the site can fix it using Correct Clinic Resource Issues instructions provided in the VS GUI User Guide. At time of publishing, the information is in Appendix G.5.2 of the 1.6 VS GUI User Guide, page 211.

The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

# Automatically Fix Appointments with No Resource

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. It will check for existing appointments with resource issues and will automatically fix any appointment that is an exact match. It will also display appointments that may potentially require the site to fix manually.

Step by step instructions for this report option are in the VS GUI User Guide. At time of publishing, the information is in Appendix E of the 1.6 VS GUI User Guide, page 204.

The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

# Cancel Clinic Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cancel Clinic Availability option allows the user to cancel a clinic's availability for either a whole day or portions of a day. Only one portion of a day may be cancelled at a time. If several portions of a day are to be cancelled, the option must be re-entered to cancel each portion. If part of the same day has been cancelled previously, the cancellation(s) will be listed. You may cancel other portion(s) as long as the new cancellation does not overlap any previous cancellation(s).

After you have entered the desired clinic name and date, the system will list any scheduled appointments that exist during that time in a report entitled Pre-cancellation List. This report lists the patient name, SSN, appointment time, appointment length, and the patient's telephone number. Any patients with a Bad Address indicator will be denoted with an asterisk (\*) and a message will be printed at the end of the report. Historically, if the cancelled appointments are not auto-rebooked, they will need to be manually rescheduled through the Make Appointment option in the Appointment Menu. Now, users can still use Make Appointment in legacy VistA, but the recommended method is to reschedule through VistA Scheduling GUI (VS GUI). The information requested to accomplish this could be taken from the Pre-Cancellation List report. The report could also be an aid in notifying patients of cancellations by telephone in the event there was not enough time to reach them by mail.

Historically, if you chose to automatically re-book the cancelled appointments, the Cancelled Clinic Auto-Rebook Report will have been generated. Only new auto rebooks are prevented, and this report remains intact. This report provides the clinic name, date cancelled, patient name and social security number, old appointment time, and new date and time.

If auto-rebooking of appointments occurred while utilizing this option, the Cancelled Clinic Auto-Rebook Report will have been generated. This report shows the new date/time of the rebooked appointments including the ancillary test time. There are three parameters that affect the auto-rebooking of appointments with associated ancillary tests. They are: OP LAB TEST START TIME, OP EKG START TIME, and OP X-RAY START TIME. If a time is entered at these parameters, the ancillary test time will not have rebooked before the start time specified in the parameter.

The option requires a reason for clinic cancellation (3-160 characters). This reason will be made part of all cancelled appointments and can be seen using the Expand Entry (EP) command in Appointment Management.

# The option provides the capability to print cancellation letters at this time. A cancellation letter must have been previously entered through the Enter/Edit Letters option and assigned to the clinic being cancelled through the Set up a Clinic option. This letter will notify patients of the appointment cancellation and the new date/time scheduled. A list of patients with a Bad Address indicator will print after the cancellation letters have printed. Letters for these patients will not print.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A status of CANCELLED BY CLINIC will appear on the Patient Profile of each patient whose appointments are cancelled through this option. The user who entered the cancellation will also be noted.

# # Change Patterns to 30-60

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change Patterns to 30-60 option allows you to change patterns that were created with 15 minute increments to the 30-60 minute increment pattern. If you need assistance in establishing clinic availability patterns, please refer to the Set Up a Clinic option documentation.

The “Display Increments per Hour: {#} MIN//” field SHOULD NOT BE EDITED when patterns have been established using another increment per hour. Editing this field will cause existing patterns to be erroneous and scheduling conflicts may also occur if the increments are changed.

You may be asked if you wish to delete clinic availability for a particular day of the week. The system will not permit deletion of existing appointments through this option.

Utilizing the Change Patterns to 30-60 option may adversely affect existing appointments.

The software will check to see if any availability dates for the selected clinic have previously been cancelled. If so, the following message will appear, and you will be given the opportunity to print a listing of the affected days.

"Availability has been cancelled previously. The day(s) has been overwritten with the new availability. Would you like to see the day(s) that has been affected? YES//".

> **NOTE:** If you initially set up a clinic with 20 minute increments, using this option to change the pattern could cause the clinic availability pattern to display incorrectly. This option is NOT recommended for use with 20 minute increment appointment slots.

# Clinic Edit Log Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinic Edit Log Report option allows the user the ability to identify changes made to entries in the HOSPITAL LOCATION file (#44). This option has the capability of sorting a report by using one of the following categories: USER NAME or DATE CHANGED, either method will identify the field changed and include the old and new values.

Option was added by patch SD\*5.3\*568. This option may not appear on the SDSUP menu. This option is added to the ECX SETUP CLINIC menu.

# # Clinics Without Matching Resource List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option is used to identify clinic locations that have a missing or mismatched resource in the VS GUI files.

Step by step instructions for this report option are in the VS GUI User Guide. If any are found, the site can fix it using Correct Clinic Resource Issues instructions provided in the VS GUI User Guide. At time of publishing, the information is in Appendix B and C of the 1.6 VS GUI User Guide, page 195.

The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

# Convert Patient File Fields to PCMM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to convert the data stored in the following fields of the PATIENT file (#2) to primary care data for those facilities which have been manually entering primary care data prior to the release of the PCMM software.

CURRENT PC PRACTITIONER (#404.01) and CURRENT PC TEAM (#404.42)

The team must be fully defined, and a practitioner can be assigned to only one position on the team before the software will assign patients to that team and team positions.

You may choose to assign patients to teams and team positions right away. It is recommended that you initially choose not to assign patients, so that the option will generate a report showing how what assignments would be made. You could then use the output as a guide when setting up new teams and assigning practitioners and patients to teams.

You may also choose to print a detail line on the report for each patient that is assignable. At those sites where the patient number would be quite large, you may wish to just print the team and practitioner information.

Since this output may be quite lengthy, it is recommended the report be queued.

> **NOTE:** This option is not intended for use as an alternative to patient assignments via PCMM.

# Create/Edit Local Cancellation Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to create or edit a local cancellation comments that appear in VS GUI’s Cancel Appointment Dialog box.

Step by step instructions for this option are in the 1.7.2 VS GUI User Guide Addendem. The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

> **NOTE:** Users must request LAYGO access to FileMan SDEC CANCELLATION COMMENT File (#409.88) to to add, edit or remove local cancellation reasons.

# Create a Resource

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option allows the site to create a VS GUI resource for any active clinic location missing a resource. These locations can be identified in the Clinic without Matching Resource List output, as they will have a blank for the corresponding resource.

Step by step instructions for this option are in the VS GUI User Guide. At time of publishing, the information is in Appendix D.2 of the 1.6 VS GUI User Guide, page 200.

The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

# Current MAS Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Current MAS Release Notes option is used to generate a copy of the current release notes for the MAS (PIMS) software product. When selected, the option will display which version number of the MAS release notes it will generate. You will then be prompted for a device. Due to the length of the MAS release notes, you may wish to queue the output.

# Edit Clinic Stop Code Name – Local Entries Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option was added by patch SD\*5.3\*568. This option may not appear on the SDSUP menu.

# # Edit Resource

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched HOSPITAL LOCATION File (#44) clinics and VS GUI resources in SDEC RECOURCE File (#409.831).  This option allows the site to correct any active clinic with a mismatch between the clinic’s LOCATION NAME and its corresponding RESOURCE NAME in the VS GUI files as identified in the Clinic without Matching Resource List output.

Step by step instructions for this report option are in the VS GUI User Guide. If any are found, the site can fix it using Correct Clinic Resource Issues instructions provided in the VS GUI User Guide. At time of publishing, the information is in Appendix D.1 of the 1.6 VS GUI User Guide, page 198.

The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

# Edit resource for an appointment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched HOSPITAL LOCATION File (#44) clinics and VS GUI resources in SDEC RECOURCE File (#409.831). This option allows a site to directly fix the resource of a single appointment using the appointment’s internal entry number (IEN).

Step by step instructions for this option are in the VS GUI User Guide. At time of publishing, the information is in Appendix G.6.2 of the 1.6 VS GUI User Guide, page 214.

The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

# Encounter Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option provides FileMan encounter inquiry for users without access to FileMan.

# Enter/Edit Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Letters option is used to enter individual letters under the following four letter types: Pre-appointment, Appointment Cancelled, No-Show, and Clinic Cancelled. At the time a clinic is set up, the user may choose which specific letter for each letter type he/she wants associated with that clinic. These letters will then be generated through selected Scheduling options.

The field PRINT DEFAULT PROVIDER? allows for the printing of the default provider in the scheduling letter if set to YES. If the field is left empty, no provider is printed on the scheduling letter.

The field PRINT CLINIC LOCATION? allows for the printing of the clinic physical location if set to YES. If the field is left empty, no clinic location is printed on the scheduling letter.

The purposes of the four letter types are:

Pre-Appointment - to remind the patient of pending appointment(s).

Clinic Cancelled - to notify patient(s) that a clinic appointment has been cancelled by the clinic; due to either cancellation of the entire clinic or cancellation of an individual appointment, and to inform them if a new appointment was made through auto-rebook. Auto-rebook function is no longer available.

No-Show - to alert the patient to the fact that a scheduled appointment was missed.

Appointment Cancelled - to inform the patient that an appointment was Cancelled by Patient. Historically, this letter also notified patients of an auto-rebooked appointment.

Whether the patient's address appears at the top or bottom of the page when these letters are generated depends on how the site parameter, ADDRESS LOCATION ON LETTER, is set at your facility. If parameter, USE TEMPORARY ADDRESS, is set to NO, the patient's permanent address will be used when printing the letters even if the temporary address date range is in effect.

<span id="p64" class="anchor"></span>The Salutation listed on all scheduling letters was modified with patch SD\*5.3\*680. The patch altered the salutation to be non-gender specific. The new salutation shows as “Dear \[Name\]”.

Sites with bulk-mail or Postcard auto-printing may need to adjust the programming of the downstream processing program to accommodate the change, especially if the downstream system is looking for "Dear Mr./Ms." to find the beginning of the veteran's name.

This is an example of a pre-appointment letter:

\[NAME\]

\[ADDR1\]

\[ADDR2\]

\[ZIP\]

Dear \[Name\]

Your appointment is on THURSDAY DEC 21,2017@13:30

Thank you

THE VA

# Inactivate a Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inactivate a Clinic option is used to render a clinic inactive (no activity allowed) as of a selected date. Once the clinic is inactivated, it will remain so until it is reactivated through the Reactivate a Clinic option. You may not inactivate a clinic which has appointments scheduled on and/or after the selected inactivation date.

The mail group SD CLINIC INACTIVATE REMINDER is used to inform Scheduling users when a clinic is inactivated. A mail message is sent to the group on the date the clinic becomes inactive, whether it is the current date or a future date. It is critical that the mail group be populated with the appropriate Scheduling users to keep them informed of any clinic inactivation.

If the clinic was previously scheduled to be inactivated, you will be able to choose one of the following courses of action: to delete the inactivate date and either restore or reconstruct the previous clinic availability patterns; to allow the present inactivation date to remain in effect; to change the present inactivation date to another date.

If you decide to restore or reconstruct clinic availability patterns, you will be prompted to either examine existing patterns and verify them and/or enter each new availability date, time, and number of slots. See the Set Up a Clinic option for help in establishing clinic availability patterns.

If a clinic has nonconforming stop codes in the CREDIT STOP CODE (ACST) \[2053,(0;18)\] and STOP CODE NUMBER \[8,(0;7)\] you will be given a warning message. You may inactivate the clinic without fixing the problem. To correct the problem, use the Set up a Clinic option.

# List Appointment and Encounters By Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option lists all patient appointment-encounter-appointment

file triples that match user selected status values for each file.

# Look Up on Clerk Who Made Appointment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Look up on Clerk Who Made Appointment option is used to view information on a selected appointment. The user chooses the patient, clinic, and date/time of appointment.

Information which may be displayed includes patient name and SSN, clinic name, appointment date/time, person who made appointment, date appointment was made, purpose of visit, and appointment type.

The first two groups of data headings will be shown for every appointment. The elements which appear in the third group will depend on the appointment status. If the appointment was cancelled, the first two entries in the second data group will be blank.

The appointment status may be NO-SHOW, CANCELLED, or INPATIENT. If the appointment was a no-show or cancellation, the name of the clerk who entered the status may be provided along with the date/time of the entry, cancellation reason, cancellation remarks, auto-rebook date, and whether or not the appointment was rescheduled. If the appointment was routinely kept or is in the future, the appointment status will read ACTIVE.

If the Purge Scheduling Data option has been utilized, some fields may not appear.

# # Manually Fix Appointments with No Resource

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched HOSPITAL LOCATION File (#44) clinics and VS GUI resources in SDEC RECOURCE File (#409.831).  This option lists appointments with null resources, determines if there is a likely match by looking into the PATIENT File (#2) and then prompts the user to fix the appointment or bypass it.

Step by step instructions for this report option are in the VS GUI User Guide. If any are found, the site can fix it using Correct Clinic Resource Issues instructions provided in the VS GUI User Guide. At time of publishing, the information is in Appendix G.6.1 of the 1.6 VS GUI User Guide, page 195.

The list of current VS GUI manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

# Non-Conforming Clinics Stop Code Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Effective 10/1/2003, stop codes shall be assigned a restriction type of primary, secondary, or either. Primary types can only be used in the primary stop code position; secondary types can only be used in the secondary stop code position; and those with a type of either can be used in the primary or secondary stop code position. Stop codes that have a restriction type of primary or secondary will also have a restriction date to track when the stop code is designated as a restricted stop code.

The Non-Conforming Clinics Stop Code Report option is used to print a listing of the clinics that do not conform to the stop code restriction types. Additionally, the report will include clinics that contain stop codes (i.e. primary, secondary, or both) that have been inactivated and the effective date of the inactivation.

You may choose to print the report for active clinics, inactive clinics, or both. The report will list the IEN number, clinic name, primary stop code, secondary stop code, and the reason for non-conformance.

If all the selected clinics conform to the stop code restriction types, "No problem clinics found" is displayed on the report. If necessary, you may use the Set up a Clinic option to make corrections to the problem clinics.

# Pending RTC Cleanup – by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option closes pending RTC orders in CPRS where the SDEC Appointment Request has been closed or dispositioned for a user selected date range. This will search through existing “Closed” Return to Clinic (RTC) SDEC Appointment Requests with a corresponding CPRS RTC Order that is in a “Pending” status and update as needed.

Once the option runs, it will report to the user how many RTC Orders were updated for this date range.

# Pending RTC Cleanup – Full

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option closes pending RTC orders in CPRS where the SDEC Appointment Request has been closed or dispositioned. This will search through all existing “Closed” Return to Clinic (RTC) SDEC Appointment Requests with a corresponding CPRS RTC Order that is in a “Pending” status and update as needed. VistA will pause at “Starting search and clean-up…” and add additional dots to that statement as it works.

Be patient and do not continue to hit Enter while it is working. This can take some time. Once the option runs, it will report to the user how many RTC Orders were updated for this site.

# Print Clinic Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the ICD-10 implementation of VistA Scheduling, the *Supervisor menu* option provides a new report, Print Clinic Installation Checklist, which contains the following information:

Clinic

Diagnosis (both ICD9 and ICD10 codes)

Short Description

Default (Y/N)

# Purge Scheduling Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Scheduling Data option is used to delete various non-essential nodes created by the Scheduling module in the HOSPITAL LOCATION and PATIENT files. You are required to keep one full fiscal year of data online. You may select which files to purge and may choose to print the nodes (in GLOBAL format - %G) as they are deleted.

This option is utilized to retrieve disk space and should be run during off-hours.

# Reactivate a Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables the user to reactivate clinic availability for any clinic which has been inactivated through the Inactivate a Clinic option. A valid reactivate date is any date that is later than the inactivate date.

When the clinic is initially reactivated, you will be prompted to establish clinic availability patterns for the reactivate date. It is imperative that a pattern be established for this date. Without re-establishing the pattern, users will be unable to book appointments into the reactivated clinic. Patterns for other dates may be established at this time, if desired. For assistance in establishing clinic availability patterns, please refer to the Set Up a Clinic option.

If the selected clinic was previously assigned a reactivate date, you may either change the old date to a new date or delete the old date entirely. It is important to note that if you choose to delete, the clinic will remain inactivated until a new reactivate date is entered.

If a clinic does not have conforming stop codes, you will not be able to reactive it before correcting the problem by returning to Set up a Clinic. Stop codes are used in accordance with their assigned restriction types. Stop codes with restriction type “P” can only be used in the primary stop code position. Stop codes with restriction type “S” can only be used in the secondary stop code position. Stop codes with restriction type “E” can be used in either the primary or secondary stop code position.

# Release Appointment Request Locks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option Release Appointment Request Locks is used to unlock a VS GUI request, but not currently being modified by any user. This option will only remove scheduling request locks for this user, not orders locks that occur when scheduling an order (consults, procedures, etc.)

A request may become locked when a user accesses a request in the Request Management grid and steps away from the system, or the system locks or crashes while the user is still accessing the request. When trying to access the same request that is locked by another user, the user will be presented with a dialog on the screen with the following message “The selected Appointment Request cannot be accessed. LAST,FIRST NAME is editing the request”, as shown below.

> **NOTE:** Before using Release Appointment Request Locks, ensure the user whose lock you are releasing is logged out of VS GUI and VistA. This will avoid releasing a legitimate lock. This locking system does not apply to CPRS.

The Release Appointment Request Locks option is available on the Scheduling Supervisor Menu \[SDSUP\] or assigned to a user as a stand-alone menu option. Due to the nature of the option and the potential to release legitimate locks, it is recommended that this option is not distributed widely

1.  Select the SDEC RELEASE LOCKS menu option from the Supervisor Menu \[SDSUP\] or as a secondary menu option.
2.  WHOSE LOCK TO RELEASE?
    1.  Type NAME OF USER that locked the request in VS GUI
    2.  Press Enter to release the lock.
3.  The lock will be released, and the prompt “Whose locks to release?” will be displayed again. Press Enter to return to the previous menu

# Remap Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remap Clinic option is used to reset the clinic availability patterns of established clinics. It updates the pattern to insure knowledge of the holiday or deletion of the holiday. The HOLIDAY file is usually updated annually. This option must be run for each clinic which meets on the date of the holiday. The Remap Clinic option would also be utilized if the clinic set-up was edited from no scheduling on holidays to scheduling on holidays or vice/versa. Before the clinic is remapped for any date on which existing appointments may be deleted, the appointments must be cancelled.

You may choose to remap for one/many/all clinics and, at multidivisional facilities, for one/many/all divisions. The system will insert the holiday name into clinic availability patterns even if the clinic does not meet on the day of the holiday.

The following messages may appear under the "Remark" section of the output generated by this option or on your screen while utilizing the option.

MESSAGE OCCURS WHEN

Bogus clinic day- Appts! the date and day of the week

do not correspond

\[HOLIDAY NAME\]- Appts! appointments exist on a holiday and

the clinic does not schedule on

holidays. This allows you to cancel

and reschedule appointments if

necessary.

no master pattern found no day of the week template exists

for this day for this day of the week

# The following message may appear on the output.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MESSAGE OCCURS WHEN

Cancelled availability was cancelled. If

appointments were originally

scheduled on a holiday and later

cancelled, you must restore

availability for the selected date and

remap that date to insert the holiday;

otherwise, it will remain cancelled.

The following message may appear on the screen.

Cancelled - Appts! appointments were originally

scheduled on a holiday and

later cancelled. You must first

restore clinic availability for the

selected date in order to remap and to

show the holiday in the pattern.

# # Resource Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was created as part of a suite of VS GUI utility options and reports to allow sites to correct missing or mismatched Hospital Location clinics and VS GUI resources. This option users to view VS GUI resource file inquiry without FileMan access.

# Restore Clinic Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Restore Clinic Availability option is used to restore the availability for a previously cancelled clinic. Availability may be restored for the entire day. If only portions of the day were cancelled, one/many/all of those portions may be restored.

Appointments which were rescheduled using the auto-rebook feature at the time of cancellation will not be moved back to their original time slots. This function is no longer available to create new auto-rebooks.

# # Scheduling Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling Parameters option is used to display and edit the Scheduling-related parameters using the List Manager functionality.

If a plus sign + appears at the bottom of the display region, it means more information is available and you may use other commands (e.g., Next Screen, Previous Screen, First Screen, Last Screen, Up a Line, Down a Line) to scroll the display and view the additional screens. \<??\> may be entered to display all of the List Manager actions available.

## Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> APPT. SEARCH THRESHOLD

> The number of days in the past the Appointment Management option should initially search for appointments. When the user selects a patient, this parameter will automatically be used to search that many days in the past for appointments. When a clinic is selected, the user is prompted for a date range. This number will be used to calculate the default beginning date. If this field is left blank, the system will use 2 days.

> APPT. UPDATE MAIL GROUP

> The name of the mail group which should be notified whenever the Appointment Status Update Job has been completed.

> NPCDB GENERATE MAIL GROUP

> The name of the mail group which should be notified whenever generation of the NPCDB update has been completed.

> VIEW CHECK OUT INFO DEFAULT

> During the editing of the disposition, should the user default answer to the “Do you wish to see the checkout screen” prompt by YES or NO.

> LATE ACTIVITY MAIL GROUP

> The name of the mail group which should be notified when there is late entry/edit of NPCDB-related information. "Late entry" is defined as information entered after workload closeout has occurred for the visit date.

> API ERRORS MAIL GROUP

> The name of the mail group that will receive notification messages from the Scheduling API.

# > API NOTIFICATIONS TO PROCESS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the type of notification messages the Scheduling API should process. The choices are Errors Only, Warnings & Errors, or None.

> ALLOW UP-ARROW OUT OF CLASSIFICATION

> If set to YES, this parameter allows the user to up-arrow out of the classification questions. These questions are required for workload credit. Allowing the user to exit without answering these questions could also result in additional work at a later time.

> <span id="p75" class="anchor"></span>ENABLE BLANK LINE?

> If this parameter is enabled (set to YES) then a blank line will be inserted between each appointment in the output of the letters when using the Print Scheduling Letters \[SDPRLETTERS\] option. This is an optional field which only needs to be set to "YES" when a site desires to use this functionality.

> EXCLUDE ADMIN CLINICS?

> If this parameter is set to YES, then administrative clinics will not be being added to the Appointment List when using the Display Appointments \[SDDISPPEND\] option. This will help prevent patients from unnecessarily attending an administrative appointment. This is an optional field which only needs to be set to "YES" when a site desires to use this functionality.

## Division Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ADDRESS LOCATION ON LETTERS

> The location (top or bottom) where the address should appear for letters generated for appointments or other activities at this division.

> OP LAB TEST START TIME

> OP EKG START TIME

> OP X-RAY START TIME

> The time at which lab, EKG, x-ray tests begin. When an appointment is rebooked, the test time will not rebook before the time specified in the parameters. The times must be entered in military time format (e.g., 0800).

> <span id="p76" class="anchor"></span>ADDITIONAL HEADER TEXT

> INSTITUTION

> Enter the Institution for which you would like to include additional header text for Display Appointments.

> HEADER TEXT

> This field includes text which will be included for the header of the Display Appointments report generated by the Display Appointments \[SDDISPPEND\] option.

> PRINT STARTING AT FIRST LINE?

> This field will allow the site to designate if the enter text will start printing at the first line of the display/printout or after the existing first line which is the Appointment for patient line.

> Two functions of the Automated Information Collection System (AICS) software are available through this option - Clinic Print Manager and Division Print Manager.

## Clinic Print Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter or edit reports/encounter forms printed for a specified clinic.

> BASIC DEFAULT ENCOUNTER FORM

> This is the encounter form that will be printed for every appointment.

> SUPPLMNTL FORM - ALL PATIENTS

> A supplemental form to be used by all patients of the clinic. A form in this category should not also be in one of the other categories for supplemental forms or it would print twice. You may have up to three supplemental forms for all patients.

> SUPPLMNTL FORM - ESTBLSHED PT.

> A supplemental form that will print only for patients who have previously been seen in the clinic.

> SUPPLMNTL FORM - FIRST VISIT

> A supplemental form that will print only for patients who have not previously been seen at the clinic.

> FORM W/O PATIENT DATA

> The encounter form that should be printed for unscheduled visits. It can have a space in the top left-hand corner for imprinting the embossed patient card or writing in patient data.

> RESERVED FOR FUTURE USE

> This category was created to store new forms that have not yet been completed. Forms entered here are not printed.

> DON'T USE PCMM PROVIDERS

> The software defaults to printing providers specified in PCMM, if defined; otherwise, providers from the clinic setup are used. If YES is entered, the software prints the providers from clinic setup regardless of PCMM.

> Select REPORT

> Reports that should be printed for the clinic in addition to the encounter forms that have been selected. Only reports contained in the Package Interface file can be selected at this prompt.

> SIMPLEX/DUPLEX

> Allows reports to be printed one-sided or two-sided.

> Select EXCLUDED REPORT

> Reports that you do not want to print for this clinic. Entering a report as an excluded report will prevent it from printing even if it is defined to print for every appointment for the division. Reports defined through the Division Print Manager action as printing *only earliest appointment* or *only if multiple appointments* will not be excluded from printing for the first clinic.

## ## Division Print Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Print selected reports for a specified division under certain conditions.

> SELECT REPORT

> Only reports contained in the Package Interface file can be printed. Other reports can be added to the file; however, only health summary reports can be added by most users. Reports other than health summary can only be added by IRM personnel.

> REPORT PRINT CONDITION

> The condition under which the report should print. Choose from:

> For Every Appointment - Form will print for every appointment.

> Only for Earliest Appointment - Form will print once per patient, even if the patient has multiple appointments. It will print even if it is defined to be excluded through the Clinic Print Manager action. One form will print for each division.

> Only if Multiple Appointments - Form will print for the earliest appointment for patients with multiple appointments. It will print even if it is defined to be excluded through the Clinic Print Manager action. One form will print for each division.

> SIMPLEX/DUPLEX

> Allows reports to be printed one-sided or two-sided.

# # Set up a Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Set up a Clinic option is used to define/edit clinic parameters and establish appointment availability patterns for the clinics at your facility. Appointments may not be made through the Scheduling package to clinics not defined through this option.

Following is some of the basic clinic information established through this option.

- service associated with the clinic
- is/is not a non-count clinic
- ask for check in/out time
- number of allowable consecutive no-shows
- appropriate stop code number
- is/is not a variable length clinic
- can/cannot schedule to this clinic on holidays
- include/don't include on file room lists
- whether or not each visit to the clinic requires x-ray films and/or action profiles
- patient friendly name that is meaningful to patients
- flags a clinic to be exposed for direct patient scheduling
- flags a clinic to be exposed to patients by other applications such as My HealtheVet

> Prior to using this option, the four letter types which the Scheduling package uses (NO-SHOW, PRE-APPOINTMENT, CLINIC CANCELLED, and APPOINTMENT CANCELLED) must have letters defined through the Enter/Edit Letters option of this menu. Each letter type may have several differently worded letters associated with it. This option will allow you to associate these letters with the clinic you are entering. Letters are automatically generated when the appropriate action is taken through one of the Scheduling menu options.

> When editing the parameters of an existing clinic, previous entries will appear as defaults. When setting up a new clinic, certain prompts will appear with defaults. When editing an existing clinic, entry of an up-arrow \<^\> will generally advance you to the "AVAILABILITY DATE" prompt. When entering a new clinic, up-arrows \<^\> are generally not permitted until all information up to the "AVAILABILITY DATE" prompt has been entered.

> Once you have established the pattern for the clinic you will be asked if that pattern is correct for that day of the week indefinitely. If you answer YES, the Availability Date prompt will appear again. You may enter a date for a new day of the week and then establish the pattern or enter \<RET\> to exit. If you answer NO, you must then verify the pattern for each consecutive matching day of the week as far into the future as is necessary.

> When editing an existing clinic set up through this option, the software will check to see if any availability dates for that clinic have previously been cancelled. If so, the following message will appear, and you will be given the opportunity to print a listing of the affected days.

> "Availability has been cancelled previously. The day(s) has been overwritten with the new availability. Would you like to see the day(s) that has been affected? YES//".

> You cannot establish a pattern for a clinic that is too wide to fit the 80-character screen. The INCREMENTS PER HOUR, LENGTH OF APPOINTMENT, and HOUR CLINIC DISPLAY BEGINS fields SHOULD NOT BE EDITED (either through this option or through FileMan) once the clinic has been established. If the desired changes cannot be made through the Change Patterns to 30-60 option, the clinic will have to be inactivated and then rebuilt.

> This supplement describes the fields as they will appear during entry of a new clinic.

> <span id="p586_81" class="anchor"></span>

> ABBREVIATION

> An abbreviation for the clinic name 1-7 characters in length.

> PATIENT FRIENDLY NAME

> A clinic description (3-80 chars) that's meaningful to patients. The name should not have any sensitive patient information such as HIV CLINIC.

> CLINIC MEETS AT THIS FACILITY? YES

> \<RET\> to accept the default of YES. NO if the clinic meets elsewhere.

> ALLOW DIRECT PATIENT SCHEDULING?

> YES, if patients can self-schedule into this clinic. NO if patients cannot self-schedule into this clinic.

> <span id="p37" class="anchor"></span>*Note: Once this is set to yes it will automatically set DISPLAY CLIN APPT TO PATIENTS to yes and will lock out the prompt from update until set back to NO. Functionality added with patch, SD\*5.3\*646.*

> DISPLAY CLIN APPT TO PATIENTS?

> YES, if clinic appointment will be displayed to patients. NO if clinic appointment will not be displayed to patients.

> <span id="p37_2" class="anchor"></span><u>Must be set to yes if ALLOW DIRECT PATIENT SCHEDULING is set to yes.</u> (Functionality added with SD\*5.3\*646).

> SERVICE

> The hospital service associated with this clinic. Enter \<RET\> for a list of services.

> NON-COUNT CLINIC? (Y OR N)

> YES, if visits should not affect AMIS statistics. NO if visits should affect AMIS statistics

> INCLUDE ON FILE ROOM LISTS

> This field will only appear for non-count clinics. YES, to include this clinic on file room lists; NO to not include.

> STOP CODE NUMBER

> Three digits stop code number assigned to this clinic. \<??\> for a list of stop codes. Inactive stop codes are invalid. Stop code 900 cannot be used for a clinic. Stop code must have a restriction type of “Primary” or “Either” and not have a future restriction date.

> DEFAULT APPOINTMENT TYPE: REGULAR

> Default appointment type for this clinic. \<RET\> to accept default. \<?\> for list of

> appointment types.

> REQUIRE X-RAY FILMS

> YES, to have x-ray films pulled for visits to this clinic. \<RET\> for no films.

> *If you are editing the parameters of an existing clinic and wish to change a previous YES entry to NO, enter an at-sign \<@\> to delete the YES entry. This will change the entry to a null response which will be interpreted as NO by the system.*

> REQUIRE ACTION PROFILES? YES

> Will pharmacy action profiles be required for patients scheduled in this clinic?

> \<RET\> or 0 for YES, 1 for NO.

> The next four fields prompt for the letters which are printed for this clinic through other menu options. An entry is not required; however, no letter will be printed for this clinic when action is taken through the listed menu option if the field is blank.

> NO-SHOW LETTER

> This letter will be generated in conjunction with no-shows entered for this clinic through the No-Show option of the Appointment menu. Enter the name of the no-show letter. \<?\> for a list of no-show letters. \<RET\> to leave blank.

> PRE-APPOINTMENT LETTER

> This letter will be generated through the Print Scheduling Letters option of the Output menu advising patients of upcoming appointments to this clinic. Enter the name of the pre-appointment letter. \<?\> for a list of pre-appointment letters. \<RET\> to leave blank.

> CLINIC CANCELLATION LETTER

> This letter will be generated for this clinic whenever either the clinic availability is cancelled through the Cancel Clinic Availability option of this menu, or when an appointment is cancelled through the Cancel Appointment option of the Appointment menu and the cancellation is at the request of the clinic. Enter the name of the clinic cancellation letter. \<?\> for a list of clinic cancellation letters. \<RET\> to leave blank.

> APPT. CANCELLATION LETTER

> This letter will be generated for this clinic whenever an appointment is cancelled at the patient's request through the Cancel Appointment option of the Appointment menu. Enter the name of the appt. cancellation letter. \<?\> for a list of appt. cancellation letters. \<RET\> to leave blank.

> ASK FOR CHECK IN/OUT TIME

> YES, to ask the date/time each time a patient is checked in or out of this clinic. \<RET\> or NO to have the system automatically enter the current date/time.

> It is recommended you set this parameter to NO for most clinics; however, if you wish to track the actual check in or out time for a particular clinic, set this parameter to YES.

> Your entry here will override how this field is set in the Scheduling Parameters. A \<RET\> entered here will act the same as a NO response and will also override the Scheduling Parameters.

> When retroactively scheduling an appointment, the system will use the date/time of the appointment as the check in time. This date/time will either be automatically entered or used as the default, depending on how this parameter is set.

> SELECT PROVIDER

> Enter the providers associated with this clinic. These providers will then be displayed when updating the provider through Appointment Management or Check Out.

> DEFAULT PROVIDER

> Enter 1 or YES if you wish to make the selected provider appear as the default provider for this clinic; otherwise, enter 0 or NO.

> DEFAULT TO PC PRACTITIONER

> Should the primary care practitioner be the default provider for this clinic if no default provider has been indicated? 1=YES, 0=NO. If the DEFAULT PROVIDER field is answered YES, this field will have no effect.

> SELECT DIAGNOSIS

> Enter the diagnoses associated with this clinic. These diagnoses will then be displayed when updating the provider through Appointment Management or Check Out.

> DEFAULT DIAGNOSIS

> Enter 1 or YES if you wish to make the selected diagnosis appear as the default diagnosis for this clinic; otherwise, enter 0 or NO.

> WORKLOAD VALIDATION AT CHK OUT

> For this clinic, run a validation as each encounter is checked out? 1=YES, 0=NO.

> The validation logic will perform the same validation checks as the Austin database to identify encounter errors before they are transmitted. All errors are stored for later reporting and correction.

> ASK STOP CODES AT CHECK OUT

> When checking out a patient for an appointment, should the user be prompted for stop codes? 1=YES, 0=NO.

> ALLOWABLE CONSECUTIVE NO-SHOWS

> This is the number of times in a row that a patient can be a no-show in this clinic before being flagged for possible discharge from the clinic.

> MAX \# DAYS FOR FUTURE BOOKING

> Maximum number of days available when searching for open clinic slots for this clinic in the future. A number between 11 and 999.

> HOUR CLINIC DISPLAY BEGINS

> Appears for new clinics only. \<RET\> if 8AM. Otherwise, the time should be entered as follows.

> 9AM = 9 1PM = 13

> 10AM = 10 2PM = 14

> 11AM = 11 3PM = 15

> NOON = 12 4PM = 16

> START TIME FOR AUTO REBOOK

> Start time (hour of day) that should be searched for when auto rebooking an appointment to this clinic. Enter the time or \<RET\> to begin at the clinic start time.

> MAX \# DAYS FOR AUTO REBOOK

> Maximum number of days the system can be set to search up to when auto rebooking appointments. A number between 1 and 365.

> SCHEDULE ON HOLIDAYS

> Should the user be able to schedule appointments to this clinic on holidays?

> YES or \<RET\> for NO.

> *If you are editing the parameters of an existing clinic and wish to change a previous YES entry to NO, enter an at-sign \<@\> to delete the YES entry. This will change the entry to a null response which will be interpreted as NO by the system.*

> CREDIT STOP CODE

> \<RET\> if credit should be made to the same stop code as entered in the STOP CODE NUMBER field. Otherwise, enter stop code to credit.

> PROHIBIT ACCESS TO CLINIC

> Should only privileged users have access to book to this clinic?

> YES or \<RET\> for NO.

> *If you are editing the parameters of an existing clinic and wish to change a previous YES entry to NO, enter an at-sign \<@\> to delete the YES entry. This will change the entry to a null response which will be interpreted as NO by the system.*

> SELECT PRIVILEGED USER

> Will only appear if previous field answered YES. Enter the user’s name or DUZ.

> This prompt will repeat until \<RET\> is entered. You may delete a previous entry by entering an at-sign \<@\> at this prompt.

> PHYSICAL LOCATION

> Enter the location of the clinic (0-25 characters). \<RET\> to not enter a location.

> PRINCIPAL CLINIC

> If enrollment in this clinic is equivalent to enrollment in a larger one, enter the larger clinic here. If your entry is not in the HOSPITAL LOCATION file, you will be prompted for Hospital Location Type and Hospital Location Type Extension.

> OVERBOOKS/DAY MAXIMUM

> Enter the number of allowable overbooks per day to this clinic. If overbooks are not allowed, enter zero

> SELECT SPECIAL INSTRUCTIONS

> Any special instructions concerning this clinic, 0-25 characters.

> LENGTH OF APP’T

> Enter the time, in minutes, of an average appointment for this clinic (must be a multiple of 10 or 15). The length of time entered here directly affects the INCREMENTS PER HOUR display set up later. Be sure to calculate the desired time/increment relationship before entering them as you are not able to edit INCREMENTS PER HOUR after an availability date has been entered.

> VARIABLE APPOINTMENT LENGTH

> Does this clinic have variable appointment lengths? Enter V to allow for a

> varied appointment length or \<RET\> to not allow variable appointment length.

> DISPLAY INCREMENTS PER HOUR: 4

> The number of increments that will be displayed per hour for this clinic. Accept the default or enter a \<?\> for a list of choices.

> AVAILABILITY DATE

> Enter the first date appointments can be made to this clinic.

> TIME

> Scheduling patterns for the date chosen at the previous prompt may now be set up. Enter the time range the clinic will be available. Decide upon times/slots prior to entering them into the system as each day the clinic will meet in the future will need to be changed individually if the data is entered erroneously. Times should be entered in this format: 0800-1200. You cannot establish a pattern for the clinic that is too wide to fit the 80 character screen.

> NUMBER OF SLOTS: 1

> This is the number of patients which will be seen in each increment per hour. \<RET\> to accept the default or enter another number up to 9. If you enter 10 to 26, the display will be in letters of the alphabet starting with j and ending with z. Block scheduling should only be used for group clinics such as group therapy.

> *The Time and No. of Slots prompts will repeat until a \<RET\> is entered instead of a time.*

<span id="ICD10p86" class="anchor"></span>ICD-10 Update

For the ICD-10 implementation of VistA Scheduling, the *Supervisor menu* option provides a new report, Print Clinic Installation Checklist, which contains the following information:

Clinic

- Diagnosis (both ICD9 and ICD10 codes)
- Short Description
- Default (Y/N)

This list is available at the time of the ICD-10 Patch Install to help ensure the ICD-10 equivalent Default Diagnoses are set up for each Clinic that previously had ICD-9 Default Diagnoses.

Note 1: ICD-10 diagnosis codes are available for Default Diagnosis setup *prior to* the ICD-10 activation date.

Note 2: The ICD-9 diagnosis fields are not available for setting up Default Diagnosis *after* the ICD-10 activation date.

# Print Clinic Installation Checklist - Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION NAME:    SDSUP     Supervisor Menu

Add/Edit a Holiday

Appointment Inquiry

Appointment Status Update Menu ...

Appointment Waiting Time Report

Appointments with missing resources

Appointments with no resource report

Automatically Fix Appointments with No Resource

Cancel Clinic Availability

Change Patterns to 30-60

Clinics without matching resource list

Clinic Edit Log Report

Convert Patient File Fields to PCMM

Create a resource

Current MAS Release Notes

Edit Clinic Stop Code Name- Local Entries Only

Edit Resource

Edit resource for an appointment

Enter/Edit Letters

Inactivate a clinic

List Appointments and Encounters by status

Look up on Clerk Who Made Appointment

Manually Fix Appointments with No Resource

Non-Conforming Clinics Stop Code Report

Print Clinic Installation Checklist

Purge Scheduling Data

Reactivate a Clinic

Release Appointment Request Locks

Remap Clinic

Resource Inquiry

Restore Clinic Availability

Scheduling Parameters …

Set up a Clinic

Sharing Agreement Category Update

VS GUI Help Pane Edit

Wait List (Sch/PCMM) Utilities ...     

Select Supervisor Menu \<TEST ACCOUNT\> Option: Print Clinic Installation Checklist

DEVICE: HOME//   UCX/TELNET    Right Margin: 80//

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

Clinic Installation Checklist                                    Jul 15, 2014

Clinic                ICD Code(s)   Short Description          Default (ICD)

--------------------  ------------  -------------------------  --------------

EXAMPLE'S CLINIC      F14.150       Cocaine abuse w cocaine-i  N

EXAMPLE'S CLINIC      J30.89        Other allergic rhinitis    N

EXAMPLE'S CLINIC      S06.0X2D      Concussion w loss of cons  Y

EXAMPLE'S CLINIC      780.60        FEVER NOS                  N

EXAMPLE'S CLINIC      100.9         LEPTOSPIROSIS NOS          Y

ZTEST                 330.0         LEUKODYSTROPHY             N

SAMPLENAME Hospice        487.8         FLU W MANIFESTATION NEC    Y

SAMPLENAME Hospice        487.1         FLU W RESP MANIFEST NEC    N

SAMPLENAME Hospice        V04.8         VACCIN FOR INFLUENZA       N

SAMPLENAME Hospice        V03.81        PROPHY VACCINE HIB         N

SAMPLENAME Hospice        V06.6         PROPHY VACC STREP PNEU&FL  N

SAMPLENAME Hospice        482.2         H.INFLUENZAE PNEUMONIA     N

SAMPLENAME Hospice        038.41        H. INFLUENAE SEPTICEMIA    N

SAMPLENAME Hospice        041.5         H. INFLUENZAE INFECT NOS   N

ZZAT TEST2            100.81        LEPTOSPIRAL MENINGITIS     N

<span id="_Toc54010299" class="anchor"></span>Figure 1: Print Clinic Installation Checklist - Example

# Sharing Agreement Category Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to define subcategories for appointment types and assign them an active status. Each appointment type may have multiple subcategories. You may associate subcategories with any appointment type but the intent of this option is to do so for the “sharing agreement” appointment type.

This information is utilized at the site level only and is not transmitted to a national database.

# VS GUI Help Pane Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to add, edit, or remove local links in the VistA Scheduling Graphical User Interface (VS GUI) help section introduced in VS GUI v1.7.0.1 Release. Links can be http, https, or mailto. This allows a site to add their local SharePoint, web applications that have site-specific links, local email distribution list for VS GUI super users/trainers, etc.

The Help section has been pre-populated with national hyperlinks to items such as the Veteran Crisis Line (and their new chat), VSE Resources, and contact information to report a problem or suggestion. The VA National Links can only be updated through the release of new patches.

Local links can be added or updated by the site through option VS GUI Help Pane Edit \[SDEC HELP PANE EDIT (LOCAL)\]. The option has been added to the Supervisor Menu \[SDSUP\] and cannot be a stand-alone option. Users must hold the SDEC HELP security key in order to access this new option.

Please review the most recent VS GUI User Guide in the VistA Document Library (VDL) for step by step instructions. Current scheduling manual list is below. At time of publishing, the information can be found in the 1.7.0.1 User Guide Addendum, page 11, Section 3.3.

<https://www.va.gov/vdl/application.asp?appid=100>

# # Wait List (Sch/PCMM) Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Inter-facility Transfer Request 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is addressed in the Electronic Wait List (EWL) User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>

At time of publishing, this menu is on page 62 of the revised EWL User Guide from March 2016. At time of publishing, the EWL process will be decommissioned at the end of calendar year 2020.

## Inter-Facility Transfer Accept

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

his option is addressed in the Electronic Wait List (EWL) User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>

At time of publishing, this menu is on page 67 of the revised EWL User Guide from March 2016. At time of publishing, the EWL process will be decommissioned at the end of calendar year 2020.

## Wait List Batch Clinic Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is addressed in the Electronic Wait List (EWL) User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>

At time of publishing, this menu is on page 69 of the revised EWL User Guide from March 2016. At time of publishing, the EWL process will be decommissioned at the end of calendar year 2020.

## Wait List Enter/Edit As A Scheduling Reminder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is addressed in the Electronic Wait List (EWL) User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>

At time of publishing, this menu is on page 70 of the revised EWL User Guide from March 2016. At time of publishing, the EWL process will be decommissioned at the end of calendar year 2020.

## Open Closed Ewl Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is addressed in the Electronic Wait List (EWL) User Guide on the VistA Document Library (VDL). <https://www.va.gov/vdl/application.asp?appid=131>

At time of publishing, this menu is on page 71 of the revised EWL User Guide from March 2016. At time of publishing, the EWL process will be decommissioned at the end of calendar year 2020.