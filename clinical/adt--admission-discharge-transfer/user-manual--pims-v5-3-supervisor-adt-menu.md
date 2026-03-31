---
title: PIMS Version 5.3 User Manual - Supervisor ADT Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Supervisor ADT Menu
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: archive
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: The options on this menu are used to enter the information necessary to run the ADT module, initialize the Daily Gains and Losses Report, check the integrity of DG routines and validity of patient transfers, purge scheduled admissions, recalculate G&L cumulative totals, view G&L corrections, and pro
audience: 
keywords: 
  - edit
  - patient
  - table
  - contents
  - date
  - number
  - ward
  - service
  - parameter
  - entry
page_count: 0
word_count: 13224
section_count: 19
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/sadt_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/sadt_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=327"
---

## Table of Contents

  - [Overview](#overview)
  - [ADT System Definition Menu](#adt-system-definition-menu)
    - [Add/Edit Beds](#addedit-beds)
    - [Bed Out-of-Service Date Enter/Edit](#bed-out-of-service-date-enteredit)
    - [Bulletin Selection](#bulletin-selection)
    - [Device Selection](#device-selection)
    - [Edit Bed Control Movement Types](#edit-bed-control-movement-types)
    - [Edit Ward Out-of-Service Dates](#edit-ward-out-of-service-dates)
    - [Embosser Edit Menu](#embosser-edit-menu)
    - [Edit Data Card File (39.1)](#edit-data-card-file-391)
    - [Edit Embosser Device File (39.3)](#edit-embosser-device-file-393)
    - [Enter/Edit Transmission Routers File](#enteredit-transmission-routers-file)
    - [G&L Parameter Edit](#gl-parameter-edit)
    - [Gains and Losses Initialization](#gains-and-losses-initialization)
    - [MAS Parameter Entry/Edit](#mas-parameter-entryedit)
    - [MAS Parameter Entry/Edit](#mas-parameter-entryedit-1)
    - [Means Test Threshold Entry/Edit](#means-test-threshold-entryedit)
    - [Reasons for Lodging Entry/Edit](#reasons-for-lodging-entryedit)
    - [Template Selection](#template-selection)
    - [Treating Specialty Set-up](#treating-specialty-set-up)
    - [Ward Definition Entry/Edit](#ward-definition-entryedit)
  - [Check Routine Integrity](#check-routine-integrity)
  - [Current MAS Release Notes](#current-mas-release-notes)
  - [Inconsistency Supervisor Menu](#inconsistency-supervisor-menu)
    - [Overview](#overview-1)
    - [Determine Inconsistencies to Check/Don't Check](#determine-inconsistencies-to-checkdont-check)
    - [Purge Inconsistent Data Elements](#purge-inconsistent-data-elements)
    - [Rebuild Inconsistency File](#rebuild-inconsistency-file)
    - [Update Inconsistency File](#update-inconsistency-file)
  - [Institution File Enter/Edit](#institution-file-enteredit)
  - [Insurance Company Entry/Edit](#insurance-company-entryedit)
    - [Insurance Company Editor Screen](#insurance-company-editor-screen)
    - [Insurance Company Editor Screen Actions](#insurance-company-editor-screen-actions)
    - [Insurance Plan List Screen](#insurance-plan-list-screen)
    - [Insurance Plan List Screen Actions](#insurance-plan-list-screen-actions)
    - [Annual Benefits Editor Screen](#annual-benefits-editor-screen)
    - [Annual Benefits Editor Screen Actions](#annual-benefits-editor-screen-actions)
    - [View/Edit Plan Screen](#viewedit-plan-screen)
    - [View/Edit Plan Screen Actions](#viewedit-plan-screen-actions)
  - [Military Service Data Inconsistencies Report](#military-service-data-inconsistencies-report)
  - [Patient Type Update](#patient-type-update)
  - [Purge Scheduled Admissions](#purge-scheduled-admissions)
  - [Recalculate G&L Cumulative Totals](#recalculate-gl-cumulative-totals)
  - [RUG Semi-Annual Background Job](#rug-semi-annual-background-job)
  - [Sharing Agreement Category Update](#sharing-agreement-category-update)
  - [Show MAS System Status Screen](#show-mas-system-status-screen)
  - [Transmit/Generate Release Comments](#transmitgenerate-release-comments)
  - [Unsupported CV End Date Report](#unsupported-cv-end-date-report)
  - [View G&L Corrections](#view-gl-corrections)
  - [WWU Enter/Edit for RUG-II](#wwu-enteredit-for-rug-ii)
PIMS V. 5.3 ADT Module User Manual
Supervisor ADT Menu
ADT System Definition Menu
> Add/Edit Beds
> Bed Out-of-Service Date Enter/Edit
> Bulletin Selection
> Device Selection
> Edit Bed Control Movement Types
> Edit Ward Out-of-Service Dates
> Embosser Edit Menu
> Edit Data Card File (39.1)
> Edit Embosser Device File (39.3)
> Enter/Edit Transmission Routers File
> G&L Parameter Edit
> Gains and Losses Initialization
> MAS Parameter Entry/Edit
> Means Test Threshold Entry/Edit
> Reasons for Lodging Entry/Edit
> Template Selection
> Treating Specialty Set-up
> Ward Definition Entry/Edit
Check Routine Integrity
Current MAS Release Notes
Inconsistency Supervisor Menu
> Overview
> Determine Inconsistencies to Check/Don't Check
> Purge Inconsistent Data Elements
> Rebuild Inconsistency File
> Update Inconsistency File
Institution File Enter/Edit
Insurance Company Entry/Edit
Military Service Data Inconsistencies Report
Patient Type Update
Purge Scheduled Admissions
Recalculate G&L Cumulative Totals
Reimbursable Insurance Primary EC Report
RUG Semi-Annual Background Job
Sharing Agreement Category Update
Show MAS System Status Screen
Transmit/Generate Release Comments
Unsupported CV End Date Report
View G&L Corrections
WWU Enter/Edit for RUG-II
Revision History
Initiated on 11/5/04
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 38%" />
<col style="width: 23%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description (Patch # if applic.)</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>11/5/04</td>
<td>DG*5.3*564 - HEC VistA Enhancements</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="odd">
<td>11/18/04</td>
<td>Manual updated to comply with SOP 192-352 - Displaying Sensitive Data</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="even">
<td>1/7/05</td>
<td>DG*5.3*632 - HVE Follow-up Enhancements. Added Consistency Check for Filipino Vet BOS.</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="odd">
<td>8/12/05</td>
<td>DG*5.3*624 - 10-10EZ 3.0 Enhancements</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="even">
<td>2/21/06</td>
<td>DG*5.3*672 – Enrollment VistA Changes Early Release – added Reimbursable Insurance Primary EC Report</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="odd">
<td>1/19/07</td>
<td>DG*5.3*657 - Update Data Entry Consistency Checks – Updated Determine Inconsistencies to Check/Don’t Check option</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="even">
<td>7/11/07</td>
<td>DG*5.3*653 – Enrollment VistA Changes Release 1 (EVC R1) – Updated Determine Inconsistencies to Check/Don't Check option</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="odd">
<td>9/6/07</td>
<td>DG*5.3*729 - PTF Fields No Longer Needed – enhancements</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="even">
<td>2/6/08</td>
<td>Updated Determine Inconsistencies to Check/Don’t Check option as a result of patch DG*5.3*765 released on 7/31/07; patch DG*5.3*764 released on 10/9/07; and patch DG*5.3*771 released on 2/5/08.</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="odd">
<td>8/14/08</td>
<td>Minor Formatting Changes</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="even">
<td>1/29/09</td>
<td>Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)</td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="odd">
<td>11/16/09</td>
<td><p>DG*5.3*754 – PMAS PARAMENTER MENU ESR 3.1 Changes:</p>
<ul>
<li><p>New Special Treatment Authority Expiration date fields added for Agent Orange and SWAC to the Means Test User Menu section.</p></li>
</ul></td>
<td>redacted</td>
<td>redacted</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 38%" />
<col style="width: 23%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description (Patch # if applic.)</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>5/18/10</td>
<td><p>DG*5.3*754 – PMAS PARAMENTER MENU ESR 3.1 Changes:</p>
<ul>
<li><p>Added sentence about subsequent patch to populate date fields for the New Special Treatment Authority Expiration date fields added for Agent Orange and SWAC to the Means Test User Menu section.</p></li>
<li><p>In <em>Determine Inconsistencies to Check/Don't Check</em> section, changed #31 (VA PENSION CLAIMED, NONVET) from YES to NO,</p></li>
<li><p>Added #87 (SC ELIG BUT NO RD CODES) – NO.</p></li>
</ul></td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="odd">
<td>12/3/10</td>
<td><p>DG*5.3*754 – PMAS</p>
<p>Updated Determine Inconsistencies to Check/Don't Check section.</p></td>
<td>redacted</td>
<td>redacted</td>
</tr>
<tr class="even">
<td>9/12/22</td>
<td>DG*5.3*1081 – Updated Determine Inconsistencies to Check/Don't Check section: 15 INEL REASON UNSPECIFIED = NO (p. 42)</td>
<td>redacted</td>
<td>redacted</td>
</tr>
</tbody>
</table>

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options on this menu are used to enter the information necessary to run the ADT module, initialize the Daily Gains and Losses Report, check the integrity of DG routines and validity of patient transfers, purge scheduled admissions, recalculate G&L cumulative totals, view G&L corrections, and provide support of the Consistency Checker feature. This entire menu is locked and you must hold the DG SUPERVISOR security key in order to access it. The following is a list of each option found in the Supervisor ADT menu along with a brief description.

ADT SYSTEM DEFINITION MENU

> ADD/EDIT BEDS

> This option is used to add a new bed or edit an existing bed. This option does not allow deletion of a bed.

> BED OUT-OF-SERVICE DATE ENTER/EDIT

> This option is used to place a bed out of service or return a bed to service.

> BULLETIN SELECTION

> This option is used to define the mail groups which should receive the various bulletins generated by this package.

> DEVICE SELECTION

> This option is used to define the default output devices.

> EDIT BED CONTROL MOVEMENT TYPES

> This option is used to define the bed movement types used at your site.

> EDIT WARD OUT-OF-SERVICE DATES

> This option is used to place a ward out of service or return a ward to service.

> EMBOSSER EDIT MENU

> EDIT DATA CARD FILE (39.1)

> This option is used to edit the Data Card file.

> EDIT EMBOSSER DEVICE FILE (39.3)

> This option is used to edit the EMBOSSER DEVICE file.

Overview

> ENTER/EDIT TRANSMISSION ROUTERS FILE

> This option allows the user to enter/edit data in the TRANSMISSION ROUTERS file (#407.7).

> G&L PARAMETER EDIT

> This option allows the supervisor to edit the parameters used by the G&L and recalculation routines and options.

> GAINS AND LOSSES INITIALIZATION

> This option is used to initialize the Gains and Losses Sheet and Bed Status Report.

> MAS PARAMETER ENTRY/EDIT

> This option is used to customize the PIMS package to your site's specific needs.

> MEANS TEST THRESHOLD ENTRY/EDIT

> This option is used to enter/edit the thresholds necessary for Means Test category determination and VA billing amounts used to calculate Category C bills.

> REASONS FOR LODGING ENTRY/EDIT

> This option is used to add new reasons for lodging or edit existing reasons.

> TEMPLATE SELECTION

> This option is used to substitute local templates in the place of distributed templates for certain options.

> TREATING SPECIALTY SET-UP

> This option is used to define the treating specialties at your site and the associated PTF bed section, AMIS service, providers and abbreviation.

> WARD DEFINITION ENTRY/EDIT

> This option is used to define the characteristics and G&L order of the wards at your site.

CHECK ROUTINE INTEGRITY

This option is used to check the integrity of a routine following application of a patch.

CURRENT MAS RELEASE NOTES

This option is used to generate a copy of the current release notes for the PIMS product.

Overview

INCONSISTENCY SUPERVISOR MENU

> OVERVIEW

> DETERMINE INCONSISTENCIES TO CHECK/DON'T CHECK

> This option is used to specify those data items you wish the Consistency Checker to check at your site.

> PURGE INCONSISTENT DATA ELEMENTS

> This option is used to purge data from the INCONSISTENT DATA file.

> REBUILD INCONSISTENCY FILE

> This option is used to add those patient names whose records contain inconsistent/unspecified data.

> UPDATE INCONSISTENCY FILE

> This option scans entries in the file and removes those for which inconsistent/unspecified data has been corrected.

INSTITUTION FILE ENTER/EDIT

This option is used to enter/edit information contained in the INSTITUTION file (#4). The DG INSTITUTION security key is needed for access to this option.

INSURANCE COMPANY ENTRY/EDIT

This option allows you to enter new insurance companies into the system and edit information for existing ones.

MILITARY SERVICE DATA INCONSISTENCIES REPORT

This option provides information on veteran records that have missing or incorrect military service data by producing a Print Inconsistencies Detail Report.

PATIENT TYPE UPDATE

This option is used to enter/edit patient types and define the information which will be collected through the registration process accordingly.

PURGE SCHEDULED ADMISSIONS

This option is used to purge scheduled admissions prior to a specified date.

RECALCULATE G&L CUMULATIVE TOTALS

This option is used to perform a recalculation of gains and losses totals from a specified date.

Overview

Reimbursable Insurance Primary EC Report

This option produces a report that lists patients with the invalid code “Reimbursable Insurance” as their Primary Eligibility Code.

RUG SEMI-ANNUAL BACKGROUND JOB

This option is used to create a Patient Assessment Instrument for all bed occupants on Intermediate Care and Nursing Home Units on semi-annual census dates.

SHARING AGREEMENT CATEGORY UPDATE

This option allows you to define subcategories for admitting regulations and assign them an active status.

SHOW MAS SYSTEM STATUS SCREEN

This option is used to display the MAS System Status Screen.

TRANSMIT/GENERATE RELEASE COMMENTS

This option is used to send comments concerning the installation of ADT/Scheduling to the developers.

UNSUPPORTED CV END DATE REPORT

Because HEC shares the CV End Date with VistA sites but NOT the Military Service Data (MSD) to support this determination, there may be some inconsistencies created at the VistA site. This option runs a report helping the sites identify CV End Dates without the supporting MSD.

VIEW G&L CORRECTIONS

This option displays corrections to the G&L.

WWU ENTER/EDIT FOR RUG-II

This option allows the user to enter/edit the national fiscal year RUG-II weighted work unit values.

## ADT System Definition Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add/Edit Beds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add/Edit Beds option is used to enter a new or edit an existing room-bed. This option will also be used to designate which wards may assign patients to the selected bed.

You must enter a value at the DESCRIPTION prompt. Double question marks (??) may be entered for a listing of available descriptions or you may enter a new description.

You will NOT be able to delete a room-bed; however, you may delete all wards which may assign to the room-bed.

If you wish to inactivate a room-bed for a period of time, you must utilize the Bed Out-of-Service Date Enter/Edit option.

ADT System Definition Menu

### Bed Out-of-Service Date Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bed Out-of-Service Date Enter/Edit option is used to inactivate a bed for bed availability purposes only. If you also wish this bed to show as statistically out-of-service on the Gains and Losses Sheet, you must utilize the Edit Ward Out-of-Service option and enter the current number of beds that are out-of-service for the specified ward.

This option is also used to edit the out-of-service and return-to-service dates. Enter a \<RET\> at the RETURN TO SERVICE DATE prompt (no default) if the bed is to be out of service indefinitely.

The system will warn you if you choose a bed that is currently occupied.

ADT System Definition Menu

### Bulletin Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to select from a list of available mail groups, those to which notification is to be sent when specific actions occur. Once a mail group is selected for a specific action, bulletins will be sent in the form of MailMan messages to all members of the selected group whenever that action occurs. If no bulletin is to be sent for an action, no mail group should be specified.

To delete a default mail group for a specific action, enter an at-sign \<@\> at that prompt.

The mail group specified Will receive notificationat this prompt

death group each time a patient death is entered into the

system

new patient group each time a new patient name is added to

the Patient file

name change group each time the spelling of an existing

patient’s name is changed

ssn change group each time the ssn of an existing patient is

changed

unverified admit group each time a patient is admitted for whom

eligibility has not been verified. It will also receive notifications for patients admitted

with verified eligibility that have either

future scheduled admissions or waiting list

entries.

inconsistency edit group whenever inconsistencies are found in a

patient's data base which cannot be

corrected by the user due to security key

restrictions (i.e., users not holding the DG

ELIGIBILITY security key).

ADT System Definition MenuBulletin SelectionThe mail group specified Will receive notificationat this prompt

non-veteran admit group whenever a non-veteran is admitted to the

facility

overdue absences group whenever the G&L is run and the user elects

to search for patients overdue on return from

authorized/unauthorized absence and pass

patient deleted group each time a patient name is deleted from the

PATIENT file

sensitive rec accessed group each time a patient record is accessed which

has a security level of SENSITIVE

sensitivity removed group each time the security level of SENSITIVE is

removed from a record

auto recalc group each time the G&L auto recalc starts and

finishes

Means Test required group that a Means Test is required each time an

appointment is made

ADT System Definition Menu

### Device Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Device Selection function is used to enter, edit, and view default output devices for printing 10-10s, drug profiles, and routing slips. The device selected must be in your DEVICE file. At multidivisional facilities, the output devices may differ for each division. The division names entered must have been previously entered through the MAS Parameter Entry/Edit option.

These devices are prompted for during parameter set up through the MAS Parameter Entry/Edit option. However, the Device Selection option provides a quick way to edit only those device parameters specific to a division.

If the PIMS parameter USE CLOSEST PRINTER is set to YES, the registration routines may not use the default output devices entered here. If the PIMS parameter USE CLOSEST PRINTER is set to YES and the CLOSEST PRINTER for user's current device is defined in the DEVICE file, the output goes to the CLOSEST PRINTER device. Otherwise, the output goes to the default device defined in the MAS PARAMETERS file.

The default devices should be defined even if your division is set up to use the device defined as the CLOSEST PRINTER.

ADT System Definition Menu

### Edit Bed Control Movement Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Bed Control Movement Types option is used to enter a new or edit an existing locally defined facility movement type. These movement types include admission, discharge, transfer, check-in lodger, check-out lodger, and specialty change. This option is also used to install the standard (default) values for selected transaction types. Standard values may be put in place for ADMISSION, TRANSFER, DISCHARGE, CHECK-IN LODGER, CHECK-OUT LODGER, and SPECIALTY TRANSFER transactions.

Through this option, you may determine which movement types can follow the one you are entering/editing. No movement types can follow DISCHARGE or CHECK-OUT. Likewise, CHECK-IN and ADMISSION cannot follow another movement type.

To facilitate the process, it is recommended that the standard default values be installed and then, if necessary, edit the data to fit your facility's needs. In all likelihood, the standard defaults will coincide with the desired values.

If you reinstall the standard default values after you have modified them locally, the standard values will override and replace any local modifications.

ADT System Definition Menu

### Edit Ward Out-of-Service Dates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Ward Out-of-Service Dates option is used to place a ward out of service or to return a ward to service. You may deactivate an entire ward or part of a ward.

The system will warn you if there are active patients on the selected ward. If you do not enter a date at the "RETURN TO SERVICE DATE" prompt, the ward will remain inactive indefinitely. You will also be prompted to determine if the out-of-service status of the ward should appear on the Gains and Losses Sheet.

In order for your statistics to reflect accurate numbers, you should recalculate your G&L statistics back to the date of change or at least back to the beginning of the current fiscal year. The statistical calculations are based on BED DAYS (the number of days in the fiscal year the bed was available) versus FYTD days. This signifies that when a ward is closed, its statistics on the date of closure would be maintained.

<u>  
</u>ADT System Definition Menu

### Embosser Edit Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit Data Card File (39.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit Embosser Device File (39.3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Embosser Edit Menu consists of two options, the Edit Data Card File (39.1) option and the Edit Embosser Device File (39.3) option. The embosser devices should be entered before entering the embosser parameters.

EDIT DATA CARD FILE (39.1) This option is used to set up or edit card type parameters for each data card type - service connected, non-service connected, non-veteran, and free text. The parameters are as follows.

Default Device - used to assign the default embosser device to each card type

Mandatory Hold - used to determine whether cards should be printed immediately, put into hold status, or the user should be prompted for the desired action

Default Number of Cards - used to assign the number of duplicate cards to be embossed (between 1-8)

Mail to Requestor - used to determine if users who request data cards who are not in the DGEMBOSSER mail group should receive embosser error messages

EDIT EMBOSSER DEVICE FILE (39.3) This option is used to enter/edit the embosser output devices used at your facility. These include data card, addressograph, and plain printer. Entries in this file must exist in the DEVICE file (#3.5).

ADT System Definition Menu

### Enter/Edit Transmission Routers File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Transmission Routers File option allows the user to enter/edit data in the TRANSMISSION ROUTERS file (#407.7). It is used to enter/edit receiving users and their mail router domain for transmission of OPC, PTF, and RUG-II data. Domains are locations set up in the DOMAIN file (#4.2) to receive the transmissions. Redacted

To enable transmission of data to the selected receiving user, the TRANSMIT field must be set to YES. Once the users have been entered for a particular domain, the transmit flags are easily turned on/off. This provides a quick and efficient means of enabling or disabling transmission of the data to that user in that domain.

ADT System Definition Menu

### G&L Parameter Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The G&L Parameter Edit option allows the PIMS supervisor to edit the parameters used by the Gains and Losses Sheet and recalculation routines and options.

Double question marks (??) entered at any prompt will display an explanation of what is required in making an entry at that parameter.

Only holders of the DG SUPERVISOR security key will have access to this option.

You may edit the following parameters.

G&L INITIALIZATION DATE

Date on which you wish to begin calculating statistics for the G&L Sheet and the Bed Status Report. The first day of the fiscal year chosen should be used. For example, if a site wishes to initialize their G&L on 10/30/92 and make it effective for the prior fiscal year, the date 10/1/91 should be used for this parameter. Normally, once this parameter is entered, it is not necessary to change the date unless there is a specific need.

TSR INITIALIZATION DATE

10/1 for the fiscal year in which you wish to initialize your Treating Specialty Report. The date selected must be on or after 10/1/92 and census statistics will be calculated from this date.

SSN FORMAT

This parameter determines whether the patient's SSN will print on the G&L Sheet in full format (all 9 digits) or just the last four digits.

MEANS TEST DISPLAY

This parameter determines whether the current Means Test Status (if applicable) will be displayed on the first portion of the G&L Sheet.

PATIENT'S TREATING SPECIALTY

This parameter determines whether or not the exact treating specialty to which a patient is assigned will be displayed whenever a movement is shown on the G&L Sheet.

ADT System Definition MenuG&L Parameter Edit

SHOW NON-MOVEMENTS ON G&L

This parameter determines if changes in a patient's treating specialty that do not involve a physical move will show on the G&L Sheet. For example, JOHN DOE is currently on ward 3SURG and his treating specialty is changed from surgery to medicine, but he is too ill to be moved to a medical ward. This parameter, once set, will display on the INTERWARD TRANSFERS subcategory of the first portion of the G&L that JOHN DOE was transferred from 3SURG \[SURG\] to 3SURG \[MED\]. If there is an abbreviation associated with the treating specialty, the G&L will print the abbreviation. If the abbreviation is blank, it will print the first five (5) characters of the treating specialty name.

RECALCULATE FROM

The earliest date for which a recalculation can be run. This date must be on or after the G&L initialization date. It is recommended a recalculation be run, at a minimum, for the current fiscal year. It is also recommended that the date not exceed more than two prior fiscal years (preferably one). The farther back the year is set, the more likely old errors will recur and be brought forward on the current G&L.

COUNT VIETNAM VETS REMAINING

This parameter determines whether the system will calculate the number of Vietnam era veterans remaining at the end of each census date. If you answer YES, the G&L process time will increase significantly. Please note that this data is no longer reported on any AMIS segment; however, it is stored in the CENSUS file (#41.9).

COUNT OVER 65'S REMAINING

This parameter determines whether the system will calculate the number of veterans over 65 years of age remaining at the end of each census date. If you answer YES, the G&L process time will increase significantly. Please note that this data is no longer reported on any AMIS segment; however, it is stored in the CENSUS file (#41.9).

ADT System Definition MenuG&L Parameter Edit

DAYS TO MAINTAIN G&L CORR

This parameter contains the number of days (between 14 and 365) you want to maintain G&L corrections in the system. Leave this field blank if you wish to maintain the complete G&L CORRECTION file (#43.5). It is recommended this parameter not be set higher than 90 days as this file can become very large. Corrections older than the number of days contained in this parameter are purged by the system when

the DG G&L Recalculation Auto background job option is run;

the Recalculate G&L Cumulative Totals manual option is run;

the "Recalculate BSR/TSR Totals? NO//" prompt is answered YES when printing the G&L Sheet through the Gains and Losses (G&L) Sheet option.

This same parameter is contained in the MAS Parameter Entry/Edit option. Editing the parameter here will change it in that option and vice versa.

<u>  
</u>ADT System Definition Menu

### Gains and Losses Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to initialize the Gains and Losses Sheet and Bed Status Report as of the date specified in the EARLIEST DATE FOR G&L PIMS parameter. Before using this option, wards and PIMS parameters must be defined. (See Ward Definition Entry/Edit and MAS Parameter Entry/Edit options.)

This option prompts the user for statistical data for each ward location. The data entered should be current as of midnight of the day previous to the date that is entered in the EARLIEST DATE FOR G&L parameter.

When this option refers to patients on pass, it means patients on authorized absence of less than 96 hours. When this option refers to Census Day, it means the day previous to the date that is entered in the EARLIEST DATE FOR G&L parameter. FYTD means that the statistical data asked for should be cumulative for the fiscal year to date.

Following is a description of the fields to be entered for each ward location.

PATIENTS REMAINING

Number of patients remaining on this ward at end of census day.

CUM PATIENT DAYS OF CARE

Total number of patient days of care (not including pass days) on this ward FYTD.

CUM BED

Total number of operating beds on this ward FYTD.

CUM DISCHARGES

Total number of discharges from this ward FYTD.

CUM INTER XFERS

Total number of interward transfers out from this ward FTYD.

CUM PAT REMAIN

Sum of number of patients remaining on this ward (including PASS patients) at end of every day since beginning of fiscal year.

CUM INTSERV XFERS

Total number of bed section transfers for this ward FYTD.

<u>  
</u>ADT System Definition MenuGains and Losses Initialization

CUM PASS DAYS

Total number of pass days for this ward FYTD.

CUM ABO DAYS

Total number of authorized absence days for this ward FYTD.

CUM UA DAYS

Total number of unauthorized absence days for this ward FYTD.

CUM 1 DAY DIALYSIS PATIENTS

Total number of patients who received 1 day dialysis treatment on this ward FYTD.

CUM ADMIS FROM XFER IN

Total number of transfer-in admissions from other VA facilities to this ward FYTD.

CUM DISCH TO XFER OUT

Total number of transfer-out discharges from this ward FYTD.

CUM DISCHARGES TO DEATH

Total number of DEATH status discharges from this ward FYTD.

CUM DISCH TO 'OPT/NSC'

Total number of discharges from this ward to OPT/NSC status (excluding dialysis patients) FYTD.

CUM ADMISSIONS

Total number of admissions to this ward FYTD (including dialysis patients).

ADM AFTER REHOSP \>30DAYS

If this ward is a DOM or NHCU, total number of readmissions to this ward after hospital episode \> 30 days FYTD.

FROM ASIH

If this ward is a DOM or NHCU, total number of readmissions to this ward from ASIH FYTD.

TO ASIH

If this ward is a DOM or NHCU, total number of transfers TO ASIH FYTD.

<u>  
</u>ADT System Definition MenuGains and Losses Initialization

DISCHARGE WHILE ASIH

If this ward is a DOM or NHCU, total number of discharges from hospital ward while on ASIH.

DIED WHILE ASIH

If this ward is a DOM or NHCU, total number of patients on ASIH from this ward who died in hospital FYTD.

CUM INTSERV XFERS IN

Total number of transfers from another bed section into this ward's bed section FYTD.

CUM LOSSES

Total number of transfers and discharges from this ward FYTD.

CUM MONTHLY PAT DAYS

Total number of patient days of care from beginning of this month.

CUM AUTHORIZED ABSENCE

Total number of transfers from this ward to authorized absence FYTD.

CUM UNAUTHORIZED ABSENCES

Total number of transfers from this ward to unauthorized absence FYTD.

FEMALE PATIENTS REMAINING

Number of female patients remaining on this ward at end of census day.

ADT System Definition Menu

### MAS Parameter Entry/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MAS Parameter Entry/Edit option is used to enter, edit, and view site specific parameters necessary to run the MAS system. The parameters in this option affect the ADT software while the Scheduling software is affected by the parameters found in the Scheduling Parameters option.

Your facility's wards must be defined in the system before defining the MAS parameters. If you have not already done so, enter wards through the Ward Definition Entry/Edit option.

The parameters are presented via a formatted screen with three separate data groups. It is important to note that if your facility is multidivisional, the parameters defined in Data Groups 1 and 2 will apply to each division. You may define different parameters in Data Group 3 for each division, if you wish. When a division does not have its own parameters defined in Group 3, the system will automatically use those of the primary facility.

Data Group 3 will appear differently for multidivisional sites; the divisions will be listed rather than the parameters. In order to view the parameters defined for each division, enter "D". In order to edit them, enter "3". You will be prompted for the name of the division and then for the data items.

A new Special Treatment Authority Expiration date fields will be added to the MAS PARAMETERS file (#43) for Agent Orange and SW Asia Conditions. The initial value of these fields will be null or empty. A subsequent patch will be released to populate the date fields once the expiration of the Special Treatment Authority is scheduled to expire. The assigning of newly enrolled veterans to Priority Group 6 determination rules whose AO Indicator is "Y" and Location is Vietnam and/or their SWAC exposure indicator is "Y" will be ignored if the Special Treatment Authority Expiration Date fields are nulled or empty.

Parameters requiring only a YES/NO answer will be designated by an asterisk (\*). You may enter 0 for NO, or 1 for YES. The following are in alphabetical order.

\*ABBREVIATED PATIENT INQUIRY

Do you wish an abbreviated patient inquiry to be displayed through the Patient Inquiry option? An abbreviated inquiry will include the following: name, SSN, date of birth, address, temporary address, Means Test status, eligibility status, admission and appointment enrollment information. Items such as religion, claim number, and period of service will be excluded.

AFFILIATED

Is your facility affiliated with a teaching facility? 0 NO

> 1 YES

> 2 INTERMEDIATE

  
ADT System Definition Menu

### MAS Parameter Entry/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*ASK DEVICE IN REGISTRATION

YES, will force the DEVICE prompt at the beginning of registration the first time through and set the 10/10, routing sheet, and profile printer to that device. This takes precedence over all devices defined as default printers or closest printer.

If data for the patient does not exist in the VistA patient database, a message displays informing the user that the 10-10 forms will not be printed.

\*AUTOMATIC PTF MESSAGES

Indicates whether the site wants to automatically generate PTF messages as part of normal ADT processing. If YES, entries into the PTF MESSAGE file will occur. If NO, no PTF messages will be generated during ADT activities.

BACKGROUND JOB FUNCTION

Determines which of the following actions the background job performs.

> D DELETE ALL ENTRIES - Removes all entries from the Preregistration Call List.

> P DELETE CALLED PATIENTS - Removes only the called patients from the Preregistration Call List.

> DA DELETE ENTRIES AND ADD NEW - Removes all entries from the Preregistration Call List and adds new entries.

> PA DELETE CALLED PATIENTS AND ADD NEW - Removes only the called patients from the Preregistration Call List and adds new entries.

> AO ADD NEW ENTRIES ONLY - Adds entries to the Preregistration Call List without removing any.

> N NOTHING - Tells the background job to leave the Preregistration Call List alone.

\*CHOICE OF DRUG PROFILE TYPE

If YES is entered for the PRINT DRUG PROFILES WITH 10-10 field, answering YES to this field will offer the user a choice between the action and informational drug profiles.

\*CONSISTENCY CHECKER ON

Do you wish to turn on the automatic Consistency Checker? If YES, data will be checked in accordance with parameters set through the Determine Inconsistencies to Check/Don't Check option of the Inconsistency Supervisor menu.

DAYS BETWEEN CALLS

Used to determine how many days from the latest DATE CHANGED field (#1) in PRE-REGISTRATION AUDIT file (#41.41) before the patient will be added to the call list again. If the patient has another appointment within x number of days of the date in the DATE CHANGED field (#1), s/he will not be added.

ADT System Definition MenuMAS Parameter Entry/Edit

DAYS TO MAINTAIN G&L CORR

This parameter contains the number of days (between 14 and 365) you want to maintain G&L corrections in the system. Leave this field blank if you wish to maintain the complete G&L CORRECTION file (#43.5). It is recommended this parameter not be set higher than 90 days as this file can become very large. Corrections older than the number of days contained in this parameter are purged by the system when:

- the DG G&L Recalculation Auto background job option is run
- the Recalculate G&L Cumulative Totals manual option is run
- the "Recalculate BSR/TSR Totals? NO//" prompt is answered YES when printing the G&L Sheet through the Gains and Losses Sheet option.

This same parameter is contained in the G&L Parameter Edit option. Editing the parameter here will change it in that option and vice versa.

DAYS TO MAINTAIN LOG

The number of days to maintain entries in the PRE-REGISTRATION CALL LOG file (#41.43). All entries before this limit will be purged.

DAYS TO MAINTAIN SENSITIVITY

This parameter is associated with the patient security options (Security Officer menu). Enter the number of days sensitivity data must remain on file before being purged. If no entry is made, the system assumes purging is not allowed. At least 30 days of data must be maintained. Enter a whole number between 30 and 365.

DAYS TO PULL APPOINTMENT

Sets the number of days in advance to look for patient appointments to add to the Preregistration Call List.

DAYS TO UPDATE MEDICAID

Enter the number of days after which an inconsistency will be created if the DATE MEDICAID LAST ASKED field is not updated.

DEFAULT 1010 PRINTER

Enter name or number from your DEVICE file of default printing device for 10-10EZ/R forms.

ADT System Definition MenuMAS Parameter Entry/Edit

DEFAULT CODE SHEET PRINTER

Enter name or number from your DEVICE file of default printing device for AMIS code sheets.

DEFAULT DRUG PROFILE PRINTER

Enter name or number from your DEVICE file of default printing device for drug profile sheets.

DEFAULT EF PRINTER

Will only appear if PRINT ENCOUNTER FORM AT REG. is answered YES. Enter name or number from your DEVICE file of default printing device for encounter forms.

DEFAULT HEALTH SUMMARY

Will only appear if PRINT HEALTH SUMMARY parameter is answered YES. Enter health summary type name, title, or owner.

DEFAULT PTF MESSAGE PRINTER

Enter name or number from your DEVICE file of default printing device for PTF messages.

DEFAULT ROUTING SLIP PRINTER

Enter name or number from your DEVICE file of default printing device for routing slips.

DEFAULT TYPE OF DRUG PROFILE

Enter the type of drug profile to print. Choose from: A Action

I Informational

\*DISPLAY MEANS TEST REQ IF GUI

Should a Means Test Required message be displayed on patient GUI lookups for this division?

\*DISPLAY MEANS TEST REQUIRED

Should a Means Test Required message be displayed on patient lookups for this division?

ADT System Definition MenuMAS Parameter Entry/Edit

DIVISION PTF PRINTER

Enter name or number from your DEVICE file of default printing device for this division's PTF messages.

\*DOMICILIARY WARDS

Does your medical center have domiciliary wards?

\*EMBOSSERS ON-LINE

Do you wish to have embossing of data card prompted during registration options?

INSTITUTION FILE POINTER

Enter the name or number of the institution in File \#4 to which this facility/division corresponds.

MEANS TEST TEXT

If the Display Means Test Required prompt was answered YES, enter the message to be displayed upon patient lookup.

MEDICAL CENTER DIVISION FACILITY NUMBER

Enter internal facility number of division (between 0 and 999999).

MEDICAL CENTER DIVISION NUM

Enter division number (between 1 and 999). The system will provide the next number as the default when initially entered.

MEDICAL CENTER NAME

Enter name of primary facility for which you are defining parameters.

\*MULTIDIVISION MED CENTER

Is your facility multidivisional?

NHCU/DOM/HOSP G&L

This prompt will not appear if the OUTPATIENT ONLY parameter is answered 1 (OUTPATIENT ONLY). Do you wish to have NHCU and/or domiciliary information combined or separate from medical center G&L Sheet?

Choose from: 0 COMBINED

1 SEPARATE

\*NURSING HOME WARDS

Does your site have nursing home ward(s)?

ADT System Definition MenuMAS Parameter Entry/Edit

OUTPATIENT ONLY

Applies to division parameters (Data Group 3). Enter 1 if this division does not have any wards.

PRE-REGISTRATION SORT

Determines the sort order of the Preregistration Call List display. Do you want to sort by P PATIENT NAME or S MEDICAL SERVICE (service associated with the clinic in which the patient has an appointment)?

\*PRINT 'AA' ON G&L

Applies to division parameters. This prompt will only appear if division has wards. This prompt will not appear if the OUTPATIENT ONLY parameter is answered 1 (OUTPATIENT ONLY). Do you wish to have authorized absences printed on G&L?

\*PRINT 'AA'\<96' ON G&L

Applies to division parameters. This prompt will only appear if division has wards. This prompt will not appear if the OUTPATIENT ONLY parameter is answered 1 (OUTPATIENT ONLY). Do you wish to have authorized absences of less than 96 hours printed on G&L?

\*PRINT DRUG PROFILES WITH 10-10

Do you wish to have printing of drug profiles prompted with 10-10 printing?

\*PRINT ENCOUNTER FORM AT REG.

Do you want the “Print Encounter Form” prompt asked at registration? If answered YES, the clinic(s) to print the encounter forms will also be asked.

\*PRINT HEALTH SUMMARY

If you have selected a free-form 10-10, answer YES here if you would like to be asked to print the health summary as well.

\*PRINT PTF MESSAGES

Do you want PTF messages to print?

\*PRINT WRISTBANDS

Do you want patient wristbands printed at this division?

ADT System Definition MenuMAS Parameter Entry/Edit

PURPLE HEART SORT

Enter the sort order used by the tasked Purple Heart status report. Choose from

A-Ascending or D-Descending (default value).

REGISTRATION TEMPLATE (LOCAL)

A site may need to capture certain registration data in a format other than that of the distributed registration screens. It may do so by creating a local registration screen (through a VA FileMan template) specifying that data in the PATIENT file they wish to capture. The template name should be specified at this prompt. This screen will then be prompted during the registration or load/edit process at the end of the other registration screens.

\*RESTRICT PATIENT RECORD ACCESS

If set to YES and the user does not hold the DG RECORD ACCESS security key, they will not be allowed to access their own record.

\*RUN FOR WEEKEND

Do you want the Preregistration nightly background job to run on weekends?

Select CLINIC EXCLUSION:

Clinics selected for exclusion will be not be checked for patient appointments when adding new patient entries to the Preregistration Call List. This parameter will only appear on the PIMS VERSION 5.3 PARAMETER ENTRY/EDIT screen if it contains data.

Select ELIGIBILITY EXCLUSION:

Patients with excluded eligibilities will not be added to the Preregistration Call List when new patient entries are being added. This parameter will only appear on the PIMS VERSION 5.3 PARAMETER ENTRY/EDIT screen if it contains data. For patients with multiple eligibilities, if the eligibility of visit is not set at check-in/check-out, the patient’s primary eligibility will be excluded.

Select EXCLUDE WHICH TERMINAL TYPES

If the USE HIGH INTENSITY ON SCREENS field has been set to YES, you may wish to exclude it from being used on certain terminal types. If so, at this prompt you should specify the terminal type(s) which should not use high intensity. This field allows you to specify multiple terminal types. You will be returned to it repeatedly until no more entries are made.

ADT System Definition MenuMAS Parameter Entry/Edit

\*SHOW STATUS SCREEN

Do you want the MAS Status Screen to be displayed to users upon entering the ADT Menu?

SYSTEM TIMEOUT

Enter number of seconds to wait for user to respond to prompts (at least 10 seconds). Enter 99999 if you wish no system timeout.

TIME FOR LATE DISPOSITION

Enter the number of hours you want an active registration to remain open before the disposition is considered late (between 0 and 240).

\*USE CLOSEST PRINTER

Do you wish closest printer to be default for 10/l0s, routing slips, and pharmacy profiles?

\*USE HIGH INTENSITY ON SCREENS

Should high intensity be used for those options in MAS which allow it? This feature works in conjunction with the Registration screens to signify that data which may or may not be edited. Under certain circumstances some screens or individual data groups may only be edited by selected users. When this feature is turned on, those screens and/or data group numbers which a specific user may edit will be "high-lighted" on their terminal. They will not be "highlighted" to those users who may not edit the screens/data groups.

\*USE HINQ INQUIRY

Do you wish ability to make HINQ request during registration?

\*USE TEMPORARY ADDRESS

Do you want the patient's temporary address to be used on scheduling letters if one is provided in the patient file?

ADT System Definition Menu

### Means Test Threshold Entry/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Means Test Threshold Entry/Edit option is used to view/enter/edit the monetary values used in making Means Test Category determinations. These include veteran income threshold, dependent increments, property threshold, and child income exclusion.

This option should be used to enter new data when changes are mandated. The figures are released annually and are effective on January 1st. They are applied to the previous year income.

Following is a description of the data fields.

CAT A VET INCOME

Dollar amount threshold under which a veteran with no dependents will be placed in Category A.

CAT A FIRST DEPENDENT INCOME

Dollar amount increment allowable for first dependent for veteran to be placed in Category A.

CAT A INCOME PER DEPENDENT

Dollar amount increment allowable per additional dependent for veteran to be placed in Category A.

THRESHOLD PROPERTY

Dollar value of attributable income above which veteran would be placed in Category C or Means Test would be referred to adjudication.

CHILD INCOME EXCLUSION

Dollar amount exclusion allowable for each child for the veteran to be placed in Category A.

<u>  
</u>ADT System Definition Menu

### Reasons for Lodging Entry/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reasons for Lodging Entry/Edit option is used to enter/edit justifications for granting lodger status to patients. A lodger is a patient kept in the hospital overnight for a non-medical reason.

Examples of possible lodger reasons are as follows.

- Early Appointment
- Inclement Weather
- Traveling Distance Too Far
- Lack of Transportation

A reason for lodging must be entered through this option before it can be used in the Check-in Lodger option. Once entered, the reasons cannot be deleted; therefore, care should be exercised when entering lodger reasons.

ADT System Definition Menu

### Template Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to define a local template which would be used in place of the nationally distributed template for the option specified. Data must not be added to or deleted from this file locally. This option should be used only to establish a list of allowable templates.

The message "\[DISTRIBUTED 'PRINT' TEMPLATE NAME IS '{template name}'\]" will always appear so that you may retrieve the original template as necessary.

ADT System Definition Menu

### Treating Specialty Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit the treating specialties to be used at your facility. Each treating specialty is assigned one associated PTF specialty. More than one treating specialty may be assigned to the same specialty. All specialties used by the facility should be associated with at least one treating specialty. Any number of providers may be assigned to a treating specialty.

Note that the TSR Initialization Date must be set prior to running the Treating Specialty Set-up option. The data entered must be as of midnight 9/30/yr, the date preceding the TSR Initialization Date. Also, the Recalculate G&L Cumulative Totals option must be run as of 10/1/yr following the set-up of a new treating specialty or modifications to any of the PATIENTS REMAINING fields using the Treating Specialty Set-up option.

The G&L sheet has an output that displays statistical data in terms of treating specialty. This Treating Specialty Report (TSR) reflects inpatient activity by the actual treating specialty assigned to each patient movement. Proper crediting of workload regarding "boarders" takes place as the credit is to treating specialty as opposed to a ward location. The order in which treating specialties will print on the TSR is determined through this option.

Following is an explanation of some of the data fields.

PATIENTS REMAINING - number of patients remaining at end of census day for this treating specialty.

PASS PATIENTS REMAINING - number of patients on pass (AA\<96) at end of census day (not cumulative) for this treating specialty.

AA PATIENTS REMAINING - number of patients remaining on authorized absence at end of census day (not cumulative) for this treating specialty.

UA PATIENTS REMAINING - number of patients remaining on unauthorized absence at end of census day (not cumulative) for this treating specialty.

ASIH PATIENTS REMAINING - number of absent-sick-in-hospital patients remaining at end of census day (not -cumulative) for this treating specialty.

TSR ORDER - order in which this treating specialty will print on the treating specialty report.

ADT System Definition Menu

### Ward Definition Entry/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Ward Definition Entry/Edit option is used to enter a facility's wards into the system. Wards are defined and edited through this option. The order in which the ward is to appear on the Bed Status Report, the AMIS Service the ward belongs to, and the PTF specialty code associated with the ward are some of the items defined. This specialty code and its MPCR (Monthly Program Cost Report) number are sent in the physical specialty and physical MPCR elements of the N501 and N535 PTF transactions.

Each level of TOTALS on the Bed Status Report includes figures of all previous TOTALS of lower levels according to G&L order.

Through the "PRIMARY LOCATION" prompt in this option, you may group different ward designations together for a "mini" Bed Status Report. For example, if you wanted to show all fourth floor ward totals in a single line on the Bed Status Report, each of the wards on the fourth floor would be set up with a primary location of FOUR. If this field is left blank, the primary location for that ward will be "unknown".

To prevent past data from being lost, wards may not be deleted from the system. If you wish to inactivate a ward, you must do so through the Edit Ward Out-of-Service Dates option.

This option is a vital step in setting up the PIMS package on your system. It is necessary to define your facility's wards before attempting to run the PIMS package. Other VA packages which use the WARD LOCATION file such as Inpatient Pharmacy and Lab are also dependent on the wards being defined.

You may enter double question marks (??) at most prompts for an explanation of what is required in answering that prompt.

## Check Routine Integrity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to check routine integrity. It is recommended for use in conjunction with the installation of patches, as well as whenever it is necessary to check a routine's integrity.

Included with the release of each patch will be the NOW and ORIGINAL values. These values should be compared against those computed by the system to assure routine integrity. When used in conjunction with patch installation, this option should be run both prior to and after installation. A site must assume responsibility for routines which have undergone local modifications, as they are deemed Class III software.

The option works by entering the routine name for which you wish to check the integrity. Multiple routines may be entered. The system will then make the necessary calculations and display the values on the screen.

The PIMS package uses the Kernel Integrity Checker. Please see the Kernel documentation for further information, if necessary.

## Current MAS Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Current MAS Release Notes option is used to generate a copy of the current release notes for the PIMS software product. When selected, the option will display which version number of the PIMS release notes it is generating. You will then be prompted for a device. Due to the length of the PIMS release notes, you may wish to queue the output.

## Inconsistency Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The four options on this menu are provided in support of the Consistency Checker feature. The Consistency Checker provides a method of better assuring accuracy of the data contained in patients' records. It may be turned OFF or ON via the CONSISTENCY CHECKER field of your PIMS site parameters. This is done through the MAS Parameter Entry/Edit option of the ADT System Definition Menu.

When turned on, this Checker will run automatically in any option utilizing the registration screens.

When the Consistency Checker runs, it looks at the data contained in the patient's record to assure consistency with other data in that record; i.e., the VETERAN Y/N prompt is not answered NO while the SERVICE CONNECTED prompt is answered YES. If any inconsistent/unspecified data items are found, the patient's name is placed in the INCONSISTENT DATA file (#38.5). The user is then afforded the opportunity to correct the deficiencies. Certain inconsistent data elements will appear followed by an asterisk (\*). This signifies the user does not hold the required security key to edit that item. Those which are shown with two asterisks (\*\*) can only be updated through the appropriate PIMS menu options.

If all deficiencies are not corrected, a MailMan message is generated advising that inconsistent/unspecified data exists in the patient's record. This message is sent to the Inconsistency Edit mail group specified through the Bulletin Selection option of the ADT System Definition Menu. There are actually three mail messages which may be generated depending upon the situation. An initial MailMan message is generated when inconsistencies are first detected in a patient's record. A reminder message is sent when inconsistencies remain unresolved, and it has been more than seven days since the last message. An update message is sent when additional inconsistencies have been detected since the initial message.

These messages may be generated whenever the Consistency Checker is run on the patient's record. When all deficiencies are corrected, the patient's name is automatically removed from the INCONSISTENT DATA file. The Inconsistent Data Elements Report will provide a listing of those patients in the file and the inconsistent/ unspecified data elements in their records.

Inconsistency Supervisor MenuOverview

As previously mentioned, the INCONSISTENT DATA file is automatically updated by using any option utilizing the registration screens. It is not updated, however, when data is entered/edited in patient records through other ADT options or software packages including VA FileMan. The following three options found on the Inconsistency Supervisor Menu are dedicated to keeping the INCONSISTENT DATA file up to date for such records: Rebuild Inconsistency File, Update Inconsistency File, and Purge Inconsistent Data Elements. These options should be run routinely to assure the file is kept up to date and the Inconsistent Data Elements Report reflects the proper entries.

Inconsistency Supervisor Menu

### Determine Inconsistencies to Check/Don't Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to choose what data items should be checked for inconsistencies at your site when running the Consistency Checker. Once a data item is selected, a message will be displayed telling you under what conditions that data item will be considered inconsistent.

Below is a numerical listing of each of the data items which you may select to have checked by the Consistency Checker. A single asterisk (\*) indicates the data element is set to ON by the PIMS software and cannot be edited. A double asterisk (\*\*) indicates the data element is set to OFF by the PIMS software and cannot be edited.

For item \#72 - MSE Data Missing/Incomplete - the HEC shares the CV End Date, but NOT the supporting Military Service Data, with the VAMCs. The VAMCs will always accept the CV End Date sent by the HEC; they will NOT be able to modify a CV End Date if one already exists.

A review of consistency checks has been added to the HL7 Z07 Full Data Transmission process. Before a Z07 transmission is sent to the HEC (either during the batch process or in response to a query), the patient data must pass a list of required consistency checks (as indicated in the table below). If the data fails any of the checks, the Z07 transmission will *not* be sent to the HEC. At the completion of the Z07 batch process, a bulletin is sent to the DGEN ELIGIBILITY ALERT mail group with the number of Z07 messages that were not sent due to inconsistent data.

| Code  | Description                   | Use for Z07 Checks? |
|-------|-------------------------------|---------------------|
| 1     | NAME FORMAT UNACCEPTABLE      | NO                  |
| \*\*2 | ALIAS FORMAT INCONSISTENT     | NO                  |
| 3     | SEX UNSPECIFIED               | NO                  |
| 4     | DOB UNSPECIFIED               | YES                 |
| 5     | MARITAL STATUS UNSPECIFIED    | NO                  |
| 6     | RELIGION UNSPECIFIED          | NO                  |
| 7     | SSN UNSPECIFIED               | YES                 |
| 8     | ADDRESS DATA INCOMPLETE       | NO                  |
| \*9   | VETERAN STATUS UNSPECIFIED    | YES                 |
| \*10  | SC PROMPT UNANSWERED          | NO                  |
| 11    | SC PROMPT INCONSISTENT        | YES                 |
| 12    | SC% UNSPECIFIED FOR SC VET    | NO                  |
| \*13  | POS UNSPECIFIED               | YES                 |
| \*14  | ELIG CODE UNSPECIFIED         | NO                  |
| 15    | INEL REASON UNSPECIFIED       | NO                  |
| 16    | DATE OF DEATH IN FUTURE       | YES                 |
| 17    | EXPIRED, PENDING APPOINTMENTS | NO                  |

Inconsistency Supervisor MenuDetermine Inconsistencies to Check/Don't Check

| 18     | ELIG/VET STATUS INCONSISTENT                     | NO  |
|--------|--------------------------------------------------|-----|
| 19     | ELIG/NONVET STAT INCONSISTENT                    | YES |
| 20     | ELIG/SC% INCONSISTENT                            | NO  |
| *21*   | *At this time, this data item has been removed.* | NO  |
| \*22   | ELIG CODE INCONSISTENT                           | NO  |
| 23     | VERIFIED, NO ELIG DATE                           | NO  |
| 24     | POS/ELIG CODE INCONSISTENT                       | YES |
| 25     | AO CLAIMED, W/OUT VIETNAM POS                    | NO  |
| 29     | A&A CLAIMED, NONVET                              | YES |
| 30     | HOUSEBOUND CLAIMED, NONVET                       | YES |
| 31     | VA PENSION CLAIMED, NONVET                       | YES |
| 32     | MILIT. RET. CLAIMED, NONVET                      | NO  |
| 34     | POW CLAIMED, NONVET                              | YES |
| 36     | PATIENT TYPE UNDEFINED                           | NO  |
| 37     | POW DATA MISSING OR INCOMPLETE                   | NO  |
| 38     | POW DATES INCONSISTENT                           | NO  |
| 39     | COMBAT DATA MISSING/INCOMPLETE                   | NO  |
| 40     | COMBAT DATES INCONSISTENT                        | NO  |
| 41     | VIETNAM DATA MISSING (superseded)                | NO  |
| 42     | VIETNAM DATES INCONSISTENT (superseded)          | NO  |
| 48     | GI INSURANCE MISSING DOLLARS                     | NO  |
| 49     | INSURANCE 'YES' BUT NONE ACTIVE                  | NO  |
| 50     | INSURANCE NOT 'YES' BUT SOME ACTIVE              | NO  |
| \*\*51 | BOS/POS INCONSISTENT                             | NO  |
| \*52   | INSURANCE PROMPT UNANSWERED                      | NO  |
| \*53   | EMPLOYMENT STATUS UNANSWERED                     | NO  |
| 54     | DEPENDENT'S SSN MISSING                          | NO  |
| 55     | INCOME DATA MISSING                              | NO  |
| 56     | VA DISABILITY MISSING DOLLARS                    | NO  |
| 57     | MEDICAID NEEDS UPDATING                          | NO  |
| 58     | EC CLAIM-NO PERS GULF/SOM SVC                    | NO  |
| 59     | CATASTROPHIC DISAB. INCOMPLETE                   | NO  |
| 60     | AGENT ORANGE EXP LOC MISSING                     | YES |
| 61     | MISSING PHONE NUMBER DATA                        | NO  |
| 62     | EMERGENCY CONTACT NAME MISSING                   | NO  |
| 63     | CONF. ADDRESS DATA INCOMPLETE                    | NO  |
| 64     | POB CITY/STATE MISSING                           | NO  |
| 65     | MOTHER'S MAIDEN NAME MISSING                     | NO  |
| 66     | PSEUDO SSN IN USE                                | NO  |
| 67     | NO CV, CHECK SERVICE SEP DATE                    | NO  |
| 68     | NO CV, CHECK COMBAT TO DATE                      | NO  |
| 69     | NO CV, CHECK YUGOSLAV TO DATE                    | NO  |
| 70     | NO CV, CHECK SOMALIA TO DATE                     | NO  |
| 71     | NO CV, CHECK PERS GULF TO DATE                   | NO  |
| 72     | MSE DATA MISSING/INCOMPLETE                      | NO  |
| 73     | MSE DATES INCONSISTENT                           | NO  |

Inconsistency Supervisor MenuDetermine Inconsistencies to Check/Don't Check

| 74  | CONFLICT DT MISSING/INCOMPLETE | NO  |
|-----|--------------------------------|-----|
| 75  | CONFLICT TO DT BEFORE FROM DT  | NO  |
| 76  | INACCURATE CONFLICT DATE       | NO  |
| 77  | INACCURATE POW DT/LOCATION     | NO  |
| 78  | INACCURATE COMBAT DT/LOC       | NO  |
| 79  | MSE DATES OVERLAP              | NO  |
| 80  | POW DT NOT WITHIN MSE          | NO  |
| 81  | COMBAT DT NOT WITHIN MSE       | NO  |
| 82  | CONFLICT DT NOT WITHIN MSE     | NO  |
| 83  | BOS REQUIRES DATE W/IN WWII    | YES |
| 84  | FILIPINO VET, PROOF MISSING    | NO  |
| 85  | FILIPINO VET SHOULD BE VET='Y' | YES |
| 86  | INEL FIL VET SHOULD BE VET='N' | YES |
| 87  | SC ELIG BUT NO RD CODES        | NO  |
| 99  | CAN'T PROCESS FURTHER          | NO  |
| 301 | PERSON LASTNAME REQUIRED       | YES |
|     |                                |     |
| 303 | GENDER REQUIRED                | YES |
| 304 | GENDER INVALID                 | YES |
| 306 | VALID SSN/PSEUDO SSN REQUIRED  | NO  |
| 307 | PSEUDO SSN REASON REQUIRED     | NO  |
| 308 | DATE OF DEATH BEFORE DOB       | YES |
| 309 | PATIENT RELATIONSHIP INVALID   | YES |
| 310 | DEPENDENT EFF. DATE REQUIRED   | YES |
|     |                                |     |
| 312 | PERSON MUST HAVE NATIONAL ICN  | YES |
| 401 | RATED INCOMPETENT INVALID      | YES |
| 402 | ELIGIBLE FOR MEDICAID INVALID  | YES |
| 403 | DT MEDICAID LAST ASKED INVALID | YES |
| 406 | CLAIM FOLDER NUMBER INVALID    | YES |
| 407 | ELIGIBILITY STATUS INVALID     | YES |
| 409 | AGREE TO PAY DEDUCT INVALID    | NO  |
| 411 | ENROLLMENT APP DATE INVALID    | YES |
| 501 | POW STATUS INVALID             | YES |
| 502 | MIL DIS RETIREMENT INVALID     | YES |
| 503 | DISCHARGE DUE TO DISAB INVALID | YES |
| 504 | AGENT ORANGE EXPOSURE INVALID  | YES |
| 505 | RADIATION EXPOSURE INVALID     | YES |
| 506 | ENV CONTAMINANTS EXP INVALID   | YES |
| 507 | RAD EXPOSURE METHOD INVALID    | YES |
| 508 | MST STATUS INVALID             | YES |
| 509 | MST STATUS CHANGE DATE MISSING | YES |
| 510 | MST STATUS SITE REQUIRED       | YES |
| 511 | MST STATUS SITE INVALID        | YES |
| 516 | DOB INVALID-MEXICAN BORDER WAR | YES |
| 517 | DOB INVALID-WORLD WAR I        | YES |

Inconsistency Supervisor MenuDetermine Inconsistencies to Check/Don't Check

| 701 | CD 'DECIDED BY' CANNOT BE HINQ   | YES |
|-----|----------------------------------|-----|
| 702 | CD 'DECIDED BY' NOT VALID        | YES |
| 703 | CD 'DECIDED BY' IS REQUIRED      | YES |
| 704 | CD 'REVIEW DATE' IS REQUIRED     | YES |
| 705 | CD 'REVIEW DATE' IS INVALID      | YES |
| 706 | CD CONDITION SCORE IS NOT VALID  | YES |
| 707 | CD REVIEW DT AFTER DECISION DT   | YES |
| 708 | CD AFFECTED EXTREMITY IS INVALID | YES |
| 709 | CD DIAGNOSIS IS NOT VALID        | YES |
| 710 | CD PROCEDURE IS NOT VALID        | YES |
| 711 | CD REASON IS NOT PRESENT         | YES |
| 712 | CD DATE OF DECISION IS NOT VALID | YES |
| 713 | CD DATE OF DECISION IS REQUIRED  | YES |
| 714 | CD FACILITY IS NOT VALID         | YES |
| 715 | CD METHOD IS REQUIRED            | YES |
| 716 | CD METHOD IS NOT VALID           | YES |
| 717 | CD NOT ENOUGH TO QUALIFY         | YES |
| 718 | CD PERMANENT INDICATOR INVALID   | NO  |
| 719 | CD STATUS UNSPECIFIED            | YES |
| 720 | CD ENOUGH TO QUALIFY             | YES |
| 723 | CD REVIEW DATE MUST BE PRECISE   | YES |
| 724 | CD DECISION DT MUST BE PRECISE   | YES |
| 725 | CD EXTREMITY REQUIRED            | YES |
| 726 | CD SCORE REQUIRED                | YES |

Inconsistency Supervisor Menu

### Purge Inconsistent Data Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to purge data from the INCONSISTENT DATA file. The user is prompted to select a date. The system then finds all patients who have not been admitted or registered, or who do not have appointments, since that date. The inconsistent data elements for those patients will be removed from the file.

If a job request is currently pending, the following message will be displayed and you will be unable to run the option.

"UNABLE TO RUN THIS OPTION AT CURRENT TIME!!

'INCONSISTENCY PURGE' OPTION RUNNING FROM {DATE/TIME OF PENDING QUEUED REQUEST}."

Inconsistency Supervisor Menu

### Rebuild Inconsistency File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to rebuild or to add data to the INCONSISTENT DATA file. You may either delete the existing data and rebuild the file or you may simply add to the existing file. The system will find all patients admitted or registered on or after a selected date whose files have inconsistencies. These inconsistencies will then be stored in the INCONSISTENT DATA file.

If a job request is currently pending, the following message will be displayed and you will be unable to run the option.

"UNABLE TO RUN THIS OPTION AT CURRENT TIME!!

'INCONSISTENCY REBUILD' OPTION RUNNING FROM {DATE/TIME OF PENDING QUEUED REQUEST}."

Inconsistency Supervisor Menu

### Update Inconsistency File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to update the INCONSISTENT DATA file. The system scans through all entries in the file checking to see if the inconsistencies still exist. If an inconsistency no longer exists, that entry is deleted from the file. You will be prompted to enter the date/time at which to begin running the update. When you enter this option, a brief paragraph explaining its function is displayed.

It is a good idea to run this option periodically as it will remove from the file any data which may no longer have inconsistencies due to the execution of another option which does not call up the consistency checker.

If a job request is currently pending, the following message will be displayed and you will be unable to run the option.

"UNABLE TO RUN THIS OPTION AT CURRENT TIME!!

'INCONSISTENCY UPDATE' OPTION RUNNING FROM {DATE/TIME OF PENDING QUEUED REQUEST}."

## Institution File Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to enter/edit the information contained in the INSTITUTION file (#4). You must hold the DG INSTITUTION security key in order to access this option.

You will be prompted for the following data fields for the selected institution.

- NAME
- REGION (#)
- DISTRICT (#)
- VA TYPE CODE
- STATION NUMBER
- ADDRESS
- MULTIDIVISION FACILITY

You may enter a new institution or edit the information pertaining to an existing one through this option.

You may enter double question marks (??) throughout the process for further explanation of the data fields.

## Insurance Company Entry/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Insurance Company Entry/Edit option is used to enter new insurance companies into the INSURANCE COMPANY file and edit data on existing companies. An insurance company must be in the INSURANCE COMPANY file before it can be entered into a patient's record.

When entering new insurance companies, you will be prompted for the company street address, city, and whether or not the company will reimburse for treatment.

The option then employs the List Manager utility. In the top left corner of each screen is the screen title. The following line is a description of the information displayed. A plus sign (+) at the bottom of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right of the screen. Available actions are displayed below the screen. Double question marks (??) entered at any "Select Action" prompt displays all available actions for that screen.

You may QUIT from any screen which will bring you back one level or screen. EXIT is also available on most screens. When EXIT is entered, you are asked if you wish to "Exit option entirely?". A yes response returns you to the menu. A NO response has the same result as the QUIT action.

Following is a listing of the actions found on the screen in this option and a brief description of each. Once an action has been selected, double question marks (??) may be entered at most of the prompts that appear for lists of acceptable responses or instruction on how to respond.

### Insurance Company Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the insurance company is selected, this screen is displayed listing the following groups of information for that company: billing parameters, main mailing address, inpatient claims office data, outpatient claims office data, prescription claims office data, appeals office data, inquiry office data, remarks, and synonyms.

Insurance Company Entry/Edit

### Insurance Company Editor Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BP Billing Parameters - Allows you to add/edit the billing parameters for the selected insurance company.

MM Main Mailing Address - Allows you to add/edit the company's main mailing address. The address entered here will automatically be entered for the other office addresses.

IC Inpt Claims Office - Allows you to add/edit the company's inpatient claims office name, address, phone, and fax numbers.

OC Opt Claims Office - Allows you to add/edit the company's outpatient claims office name, address, phone, and fax numbers.

PC Prescr Claims Of - Allows you to add/edit the company's prescription claims office name, address, phone, and fax numbers.

AO Appeals Office - Allows you to add/edit the company's appeals office name, address, phone, and fax numbers.

IO Inquiry Office - Allows you to add/edit the company's inquiry office name, address, phone, and fax numbers.

RE Remarks - Allows the user to enter comments concerning the selected insurance company.

SY Synonyms - Allows you to add/edit any synonyms for the selected company.

EA Edit All - Lists editable fields line by line for quick data entry.

AI (In)Activate Company - Allows you to activate/inactivate the selected insurance company. This may be used to inactivate duplicate companies in the system. When an insurance company is no longer valid, it is important to inactivate the company rather than delete it from the system. The IB INSURANCE SUPERVISOR security key is required. Once a company has been inactivated, it may not be selected when entering billing information.

Insurance Company Entry/Edit

You may also obtain a report of patients insured by a given company through this action.

CC Change Insurance Co. - Allows you to change to another company without returning to the beginning of the option.

DC Delete Company - Allows you to delete an entry from the INSURANCE COMPANY file (#36). If claims have been submitted to the company, another company must be selected to point all claims and receivables information to.

PL Plans (accesses Insurance Plan List screen) - Allows you to display and change plan attributes associated with the insurance company.

### Insurance Plan List Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen lists all plans (active and inactive, group and individual) for the selected insurance company.

### Insurance Plan List Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VP View/Edit Plan (accessesView/Edit Plan screen) - Allows you to display/change detailed information for the plan.

IP Inactive Plan - Allows you to inactivate an insurance plan, or move subscribers from multiple insurance plans into one master plan.

AB Annual Benefits - (accesses Annual Benefits Editor screen) Used to enter annual benefits data for the selected policy.

### Annual Benefits Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the benefit year is selected, this screen is displayed listing all the benefits for the selected insurance policy and benefit year. Benefit categories may include inpatient benefits, outpatient benefits, mental health, home health care, hospice, rehabilitation, and IV management.

Insurance Company Entry/Edit

### Annual Benefits Editor Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PI Policy Information - Allows entry/edit of maximum out of pocket and ambulance coverage.

IP Inpatient - Allows entry/edit of inpatient benefits data.

OP Outpatient - Allows entry/edit of outpatient benefits data.

MH Mental Health - Allows entry/edit of mental health inpatient and outpatient benefits data.

HH Home Health - Allows entry/edit of home health care benefits data.

HS Hospice - Allows entry/edit of hospice benefits data.

RH Rehab - Allows entry/edit of rehabilitation benefits data.

IV IV Mgmt. - Allows entry/edit of intravenous management benefits data.

EA Edit All - Lists editable fields line by line for quick data entry.

CY Change Year - Allows you to change to another benefit year.

### View/Edit Plan Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays plan information for viewing/editing including utilization review info, plan coverage limitations, annual benefit dates, user information, and plan comments.

### View/Edit Plan Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PI Policy Information - Allows entry/edit of maximum out of pocket and ambulance coverage.

UI UR Info - Allows entry/edit of utilization review information.

Insurance Company Entry/Edit

CV Add/Edit Coverage - Allows you to add or edit coverage limitations for a specific plan.

PC Plan Comments - Allows editing of comments for the plan.

IP Inpatient - Allows entry/edit of inpatient benefits data.

AB Annual Benefits - (accesses Annual Benefits Editor screen) Used to enter annual benefits data for the selected policy.

CP Change Plan - Allows you to select another plan for this insurance company without having to exit back to the previous screen.

This option now belongs to the Integrated Billing package. Any requested changes or enhancements should be directed to the MCCR developers.

## Military Service Data Inconsistencies Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Military Service Data Inconsistencies Report option provides information on veteran records that have missing or incorrect data. This report requires a two-step process.

1.  Use the Extract and Count Inconsistencies option to queue a process to read through the PATIENT file (#2) and find those records that contain inconsistent military service data before running the detail report. If you attempt to run the detailed report before extracting the inconsistencies, you will receive an error. Also, if the extract has been queued and not yet run, you will receive an error if you attempt to run the detailed report.

> The system displays the last time the extract was run.

> Respond “Yes” to run the extraction or “No” to cancel it. If you respond “Yes”, you can run the extract immediately, or you may want to queue it to run at a later time, since it may take some time to perform this operation on large numbers of records.

> The system sends a confirmation email to REDACTED as well as via VA MailMan to the DGEN ELIGIBILITY ALERT mail group, after the extract is completed, that includes: a list of statistics, time of the extract, number of records, and count of inconsistencies. The Total on this report represents the total number of individual veterans found with inconsistencies; any veteran can have more than one inconsistency. This information provides an idea of the amount and difficulty of work needed to clean up records with inconsistent military service data.

> After you run the extract, you can print the detailed report that describes the inconsistencies for the specified veteran in detail.

2.  Use the Print Inconsistencies Report option to produce a full detail report of inconsistencies for individual veterans.

> Specify how many records to include in the detailed report, the device it should print to, etc.

> Specify to sort the detailed report by SSN (terminal digits) or by Name (default). Since records may be stored in some facilities according to the SSN (terminal digits), running the report in this format may be advantageous for the correction process.

Military Service Data Inconsistencies Report

Each detailed report lists the veteran’s name and SSN, the category of military service data, and the specific inconsistency associated with that category. Any given veteran may have more than one category of military service data and more than one type of inconsistency within a category. Category and Inconsistency Abbreviations are listed in the tables below.

The final page of the report contains the range of records selected to be on the detailed report. You may print the detailed report again for another range of records. For example, if you first chose to run the report on records 1-50, you can subsequently specify to run the report on records 51-140.

*Military Service Data Category Abbreviations*

| ABBREVIATION | CATEGORY               |
|------------------|----------------------------|
|                  |                            |
| COM              | Combat                     |
| GREN             | Grenada                    |
| GULF             | Persian Gulf               |
| LEB              | Lebanon                    |
| MSE1             | Military Service Episode 1 |
| MSE2             | Military Service Episode 2 |
| MSE3             | Military Service Episode 3 |
| PAN              | Panama                     |
| POW              | Prisoner of War            |
| SOM              | Somalia                    |
| VIET             | Vietnam                    |
| YUG              | Yugoslavia                 |

*Military Service Data Inconsistency Abbreviations*

| ABBREVIATION       | INCONSISTENCY                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------|
|                        |                                                                                                           |
| BEC                    | Service Branch is B.E.C.                                                                                  |
| DT IMPR                | Date is imprecise (year only)                                                                             |
| DT INVALID FOR LOC     | Date is invalid for the location                                                                          |
| DT NOT W/IN MSE        | Date is not within the Military Service Episodes                                                          |
| DT OVRLP W/ MSE1       | Date overlaps with Military Service Episode 1                                                             |
| DT OVRLP W/ MSE2       | Date overlaps with Military Service Episode 2                                                             |
| END DT BEFORE START DT | End Date is before Start Date                                                                             |
| MERC SEA NO WWII SVC   | Service Branch is Merchant Seaman but Military Service Episode dates are invalid for World War II service |
| MISS DAT               | Missing Data                                                                                              |

## Patient Type Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to specify what patient data will be collected and/or displayed through the registration and load/edit processes. These processes work according to the patient's patient type and the specifications made through this option. Each new patient entered into the system must be assigned a patient type.

Using this option, you may turn various registration screens OFF and ON according to patient type. If you enter NO to a screen prompt, the entire screen will not be presented when registering or loading/editing a patient of that patient type. For certain screens, you may elect to have the screen presented but not allow editing of certain data groups on that screen.

You may select to have all records of a particular patient type (i.e., EMPLOYEE) assigned a level of "sensitive" thus causing access of those records to be tracked and logged by the system. (See Security Officer Menu documentation for further information, if desired.)

Patient types and associated defaults are distributed with this package. They should not be altered or it could adversely affect daily operations of the PIMS software.

There are fifteen Registration Screens distributed with PIMS. Screens 1, 2, 4, 5, 7, 12, 13, 14, and 15 will always be presented during the registration or load/edit processes. Depending upon whether a user holds the DG ELIGIBILITY security key and whether certain information has been verified, some data may not be editable by certain users. This is more fully explained in the Registration Supplement.

The specifications made through this option only apply to data contained on Screens 3, and 6 through 11. These screens are as follows.

\#3 EMERGENCY CONTACT DATA

\#6 MILITARY SERVICE DATA

\#7 ELIGIBILITY STATUS DATA

\#8 FAMILY DEMOGRAPHIC DATA

\#9 INCOME SCREENING DATA

\#10 INELIGIBLE/MISSING DATA

\#11 ELIGIBILITY VERIFICATION DATA

Patient Type Update

For each patient type, you will be prompted with "Ignore Veteran Checks". If NO is answered here, a user will be able to enter veteran information for patient types considered non-veteran. For example, although military retiree patients are not considered to have veteran status, you may wish to have their service record information.

The New Patient INPUT DR prompt allows the specification of a DR STRING to be asked when new patients of the selected patient type are entered into the system. Only users with programmer access to the system will see this prompt.

Following is a list of all fields which may be prompted when using the Patient Type Update option. They are listed in the order in which they will appear along with a brief explanation. You may enter 0 for NO, 1 for YES, or a \<RET\> to accept the default value. When no default exists, an entry of \<RET\> will signify a NULL response which the system will interpret as a NO.

Select TYPE OF PATIENT NAME

Enter the patient type for which you wish to enter/edit parameters. These patient types should not be added to or altered.

NAME

Your entry at the first prompt will appear as the default.

VETERAN

Are patients of this patient type veterans? If this is a non-veteran patient type, but patients with this type COULD be veterans, respond YES to the next prompt - IGNORE VETERAN CHECKS.

IGNORE VETERAN CHECKS

Answer YES to allow "veteran" information to be entered for patients with non-veteran patient types. An example would be military retirees who are seen as non-veterans but may have veteran periods of service, POW dates, etc.

MAKE RECORD SENSITIVE

Do you wish all records for patients of this type to be flagged as SENSITIVE and have access tracked and logged for review by the Security Officer?

<u>  
</u>Patient Type Update

SHOW CONTACT SCREEN

Should the contact screen be presented when registering or loading/editing patients of this patient type? This screen contains names and addresses of next of kin, emergency contacts, and designee.

SHOW SERVICE SCREEN

Should the service screen be presented when registering or load/editing patients of this patient type? The service record screen contains service history, POW status, agent orange and ionizing radiation exposure information, etc.

ON SCREEN 7 (ELIGIBILITY STATUS DATA), EDIT SC CONDITIONS PER PT

Should users be allowed to enter/edit SC conditions as stated by the patient for patients of this type?

SHOW FAMILY INFO SCREEN

Should the family demographic screen be presented when registering or loading/editing patients of this patient type? This screen contains name, ssn, date of birth, and sex for all dependents of the patient. You must answer YES for NSC VETERAN patient type as income screening is required for all non-service connected veterans.

SHOW INCOME SCREENING SCREEN

Should the income screening screen be presented when registering or loading/editing patients of this patient type? This screen contains information on the patient's income for the previous calendar year as well as data on the spouse and dependents. You must answer YES for NSC VETERAN patient type as income screening is required for all non-service connected veterans.

SHOW INELIGIBLE SCREEN

Should the ineligible data screen be presented when registering or loading/editing patients of this patient type? The screen contains information on the patient's eligibility for care and data on missing patients. If YES is entered, the following two fields will be prompted.

> EDIT INELIGIBLE DATA - Should users be allowed to enter/edit data concerning a patient's eligibility for care for this patient type? If NO is entered, the data will display on the screen but will not be editable by the user.

> EDIT MISSING DATA - Should users be allowed to enter/edit data concerning missing veterans for this patient type? If NO is entered, the data will display on the screen but will not be editable by the user.

Patient Type Update

SHOW VERIFICATION SCREEN

Should the service verification screen be presented when registering or loading/editing patients of this patient type? This screen contains information concerning the verification of eligibility and service record data, and data on VA-rated disabilities.

NEW PATIENT INPUT DR

This field (also known as a DR String) only appears for those users having programmer ("@") access through FileMan. You may need to see the Chief, IRM Service for assistance. This field allows you to automatically prompt for specified data when adding a new patient to the system.

## Purge Scheduled Admissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Scheduled Admissions option is used to queue a background job to purge your SCHEDULED ADMISSION file (#41.1) of old data. This option is necessary because scheduled admissions cannot be deleted from the system.

At least 90 days worth of data must be retained in the file. You will be prompted for the date through which to purge the file. If the date is less than 90 days in the past or if no scheduled admissions exist on or prior to that date, a message will be displayed advising you of such. Otherwise, the job will be queued to run.

## Recalculate G&L Cumulative Totals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Recalculate G&L Cumulative Totals option is used to update the cumulative totals after past patient movements have been recorded. This eliminates the need for reprinting numerous G&L sheets.

The patient days are not automatically recalculated. The appropriate statistical data is calculated based on the prior days remaining totals and the current (recalculation) days actual gains and losses.

The user specifies the date to correct from but the date selected cannot be before the date defined in the parameter, EARLIEST DATE FOR G&L.

This option only allows one request for recalculation of G&L totals at a time. If a recalculation is currently running at the time this option is called, the following message will be displayed and the option will not be performed.

"Recalculation is running and currently processing on {date}."

If a recalculation is already queued when this option is called, the following message will be displayed and the option will not be performed.

"Recalc Already Scheduled for {date/time}"

Reimbursable Insurance Primary EC Report

The Reimbursable Insurance Primary EC Report option produces a report that lists patients with the invalid code “Reimbursable Insurance” as their primary eligibility code. Users can review the report, and manually assign a new primary eligibility code via the Load/Edit Patient Data option on the Registration Menu. The search for data includes user enrollees and non-user enrollees. Deceased patients are excluded. VAMCs can generate the report multiple times.

The output includes the following data:

- Patient’s Name
- Patient’s SSN
- Patient’s Primary Eligibility Code

## RUG Semi-Annual Background Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RUG Semi-Annual Background Job option is used to create a Patient Assessment Instrument (PAI) for all bed occupants on Intermediate Care and Nursing Home Units on semi-annual census dates. An assessment date of April 1 (and the appropriate year) will be automatically assigned if the option is run between March 1 and April 30 of that year. An assessment date of September 30 (and the appropriate year) will be assigned if the option is run between September 1 and October 30 of that year. The system will not allow you to run this job more than 31 days prior to or after a census date. If attempted, the following message will be displayed.

"Semi-annual assessments can only be run for April 1 and September 30. Cannot complete now."

The output generated is sorted by ward, listing each patient for whom a PAI has been created. The patient's social security number and admission/transfer in date will also appear on the printout.

The PAIs on this listing should be reviewed to ensure that the patient has been on the ward in excess of 7 days and has not been discharged prior to the semi-annual census date.

Depending on the setup at your site, the RUG-II semi-annual background job may be queued to run automatically and will not appear as an option.

## Sharing Agreement Category Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to define subcategories for admitting regulations and assign them an active status. Each regulation may have multiple subcategories. You may associate subcategories with any admitting regulation but the intent of this option is to do so for the “sharing agreement” admitting regulation.

This information is utilized at the site level only and is not transmitted to a national database.

## Show MAS System Status Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Show MAS System Status Screen option is used to display the MAS System Status Screen. This is the same display which may appear (depending on how the site specific parameter is set) upon entering the ADT Main Menu.

The display provides the last run date for such items as AMIS 334, 345, and 401-420 reports, Auto Recalculation, the G&L Sheet, RUG-II Background Job, and Appointment Status Update. It shows if the HINQ and Embosser Options from Registration are turned on or off and provides the scheduled run date for Auto Recalculation and Appointment Status Update. The user will also be informed of the account he/she is presently working in.

The screen is automatically displayed upon entering the option and you are returned to the menu regardless of what entry is made at the prompt.

## Transmit/Generate Release Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transmit/Generate Release Comments option is used to send comments concerning the installation of the PIMS software package to the developers at the Albany CIO Field Office. A series of questions are asked and an opportunity is provided to enter your general comments and suggestions.

The comments may be generated either as a MailMan message (which will be automatically forwarded) or as a letter which you may print and mail to the CIO Field Office. Network mail must be up in order to transmit the comments via MailMan.

The system will inform you of the date/time the initial response letter was sent if the option had been previously utilized forwarding the comments by letter.

Only holders of the DG SUPERVISOR security key may access this option.

If the installation times are not stored in the MAS RELEASE NOTES file, you may not be able to transmit the message or generate the letter.

## Unsupported CV End Date Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Eligibility Center (HEC) shares the CV End Date, but NOT the Military Service Data (MSD), with the VAMCs to support the CV determination. This option runs a report that helps the VAMCs to identify CV End Dates without the supporting MSD.

The report has the following fields:

- Veteran’s DFN
- Veteran’s Name and SSN
- CV End Date

The report may be sorted by:

- Veteran’s DFN
- Veteran’s Name

A bulletin is sent to the members of the DGEN ELIGIBILITY ALERT mail group at the veteran’s VAMCs of record to update the veteran’s CV Eligibility information when there’s a change to the CV Eligibility End Date at the HEC.

The following is an example of the Unsupported CV End Date Bulletin. Note that the Veteran’s DFN is displayed in the Subject line to help you correlate the data in the bulletin to the data in the Unsupported CV End Date Report.

Subj: DFN: 7171686 - CV END DATE IS UNSUPPORTED \[#33613\]

25 Jun 2004 12:56:20 -0500 (EST) 23 lines

From: \<ADTEMPLOYEE,ONE@ redacted \> In 'IN' basket. Page 1 \*New\*

------------------------------------------------------------------------------

A New Combat Vet Eligibility End Date has been determined at HEC for

the following patient:

Name: ADTpatient,One

SSN: 000168000

CV End Dt: Jun 20, 2006

This new Combat Vet Eligibility End was determined using the following

Military Service and Conflict Information from Site \# 500:

Branch of Service\[Last\]: ARMY

Service Number\[Last\]: 000168000

Service Entry Date\[Last\]: Feb 01, 2002

Service Separation Date\[Last\]: Jun 21, 2004

Service Discharge Type\[Last\]: HONORABLE

Conflict Location: PERSIAN GULF WAR

Conflict Indicator: YES

Conflict From Date: Aug 02, 2002

Conflict To Date: Feb 21, 2004

Please update your records to reflect the above information or contact the

site listed above if this information is inaccurate.

## View G&L Corrections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View G&L Corrections option is used to view changes in inpatient activity which were made to patients' admission records.

The user may choose either the date that the correction was entered into the system or the name of the patient whose record was changed.

If more than one G&L correction was entered on the selected date, the system displays all G&L corrections which were entered on that date. The date entered, the type of change, the patient name, and the admission date for each correction are displayed. The user selects the G&L correction he/she wants to view.

## WWU Enter/Edit for RUG-II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WWU Enter/Edit for RUG-II option allows you to enter/edit the national fiscal year RUG-II weighted work unit values.

You will be prompted for the WWU value for each RUG number from RUG l to RUG 16/17 (the value for RUG 17 will be asked if the selected fiscal year is greater than 1987.) If a value has been previously entered, it will appear as a default.

The entry for all of the 17 RUG values must be completed or those that you have just entered will be deleted.

National weighted work unit values are assigned and distributed by VA Central Office, Washington, D.C.