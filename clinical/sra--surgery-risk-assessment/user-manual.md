---
title: Surgery Risk Assessment Version 3 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: SRA
app_name: Surgery Risk Assessment
section: CLI
app_status: active
pkg_ns: SRA
patch_ver: 3
patch_id: SRA*3
group_key: "SRA:SRA:3"
file_numbers: []
security_keys: 
  - SR DOWNLOAD
  - XM GROUP PRIORITY
  - XUMGR
  - XUPROG
menu_options: 2
description: - [Revision History](#revision-history) - [Risk Assessment Database - New User Set-Up](#risk-assessment-database-new-user-set-up) - [Setting up OIT Staff Supporting the Risk Assessment Database](#setting-up-oit-staff-supporting-the-risk-assessment-database) - [File Manager Access Code](#file-manager
audience: 
keywords: 
  - assessment
  - risk
  - visn
  - workload
  - surgery
  - table
  - contents
  - download
  - transmission
  - messages
page_count: 0
word_count: 9176
section_count: 15
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Risk_Assessment_(SRA)/SRA_3_P9_UM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Risk_Assessment_(SRA)/SRA_3_P9_UM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=437"
---

Surgery Risk Assessment

User Manual

![](surgery-risk-assessment-version-3-user-manual/001.png)

June 2024

Office of Information and Technology (OIT)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Risk Assessment Database - New User Set-Up](#risk-assessment-database-new-user-set-up)
  - [Setting up OIT Staff Supporting the Risk Assessment Database](#setting-up-oit-staff-supporting-the-risk-assessment-database)
    - [File Manager Access Code](#file-manager-access-code)
    - [Primary Menu](#primary-menu)
    - [Secondary Menus](#secondary-menus)
    - [Security Keys](#security-keys)
    - [Mail Groups](#mail-groups)
  - [Setting up National Surgery Office Staff Supporting the Risk Assessment Database](#setting-up-national-surgery-office-staff-supporting-the-risk-assessment-database)
    - [File Manager Access Code](#file-manager-access-code-1)
    - [Primary Menu](#primary-menu-1)
    - [Secondary Menus](#secondary-menus-1)
    - [Security Keys](#security-keys-1)
    - [Mail Groups](#mail-groups-1)
    - [Outlook Distribution Groups](#outlook-distribution-groups)
  - [Risk Assessment Database Menus and Options](#risk-assessment-database-menus-and-options)
    - [Menu Diagram](#menu-diagram)
    - [Menu Option Descriptions](#menu-option-descriptions)
    - [Tasked Option Descriptions](#tasked-option-descriptions)
- [NSO Staff Activities and Processes](#nso-staff-activities-and-processes)
  - [Risk Assessment Database Maintenance Menu Options](#risk-assessment-database-maintenance-menu-options)
    - [Risk Assessment Download Schedule (Enter/Edit) \[SRA DOWNLOAD EDIT\]](#risk-assessment-download-schedule-enteredit-sra-download-edit)
    - [Print Risk Assessment Download Schedule \[SRA DOWNLOAD\]](#print-risk-assessment-download-schedule-sra-download)
    - [VISN Identified for Medical Center (Enter/Edit) \[SRA VISN UPDATE\]](#visn-identified-for-medical-center-enteredit-sra-visn-update)
    - [Display VISN/Medical Center Alignment \[SRA VISN DISPLAY\]](#display-visnmedical-center-alignment-sra-visn-display)
    - [VISN Workload Report Recipients (Enter/Edit) \[SRA VISN NURSE\]](#visn-workload-report-recipients-enteredit-sra-visn-nurse)
    - [List of VISNS and Surgical Nurse Contacts \[SRA VISN RN LIST\]](#list-of-visns-and-surgical-nurse-contacts-sra-visn-rn-list)
    - [Risk Assessment Site (Enter/Edit) \[SRA SITE EDIT\]](#risk-assessment-site-enteredit-sra-site-edit)
  - [Downloading Assessment Text Files](#downloading-assessment-text-files)
    - [Download and Deliver Text Files (Automatically Done per the Download Schedule)](#download-and-deliver-text-files-automatically-done-per-the-download-schedule)
  - [Creating Text Files Manually](#creating-text-files-manually)
  - [Creating Monthly Workload Reports](#creating-monthly-workload-reports)
    - [Monthly Workload Reports for the VISN Leaders](#monthly-workload-reports-for-the-visn-leaders)
- [OIT Staff – Monitoring Activities](#oit-staff-monitoring-activities)
  - [Daily Monitoring Activities](#daily-monitoring-activities)
  - [Download and Report Monitoring Activities](#download-and-report-monitoring-activities)
  - [Linux Script for Delivering .txt Files](#linux-script-for-delivering-txt-files)
  - [Transmission Layouts](#transmission-layouts)
  - [Error Messages](#error-messages)
  - [Troubleshooting Other Problems](#troubleshooting-other-problems)
    - [Problems Accessing the System](#problems-accessing-the-system)
    - [Low Volume of Incoming Transmissions](#low-volume-of-incoming-transmissions)
    - [Acknowledgements are Not Received at a Medical Center](#acknowledgements-are-not-received-at-a-medical-center)
  - [OI&T Staff Utilities for Risk Assessment Menu Options](#oit-staff-utilities-for-risk-assessment-menu-options)
    - [Print SRA Transmission Message Format \[SRAMLR\]](#print-sra-transmission-message-format-sramlr)
    - [Edit Transmission Layouts File (#139.4) \[SRA TRANSMISSION LAYOUTS\]](#edit-transmission-layouts-file-1394-sra-transmission-layouts)
    - [Decipher SRA Transmission Message \[SRAPARSE\]](#decipher-sra-transmission-message-sraparse)
- [Purging Assessments Older than Three Years](#purging-assessments-older-than-three-years)
Each time this manual is updated, the Title Page lists the new revised date, and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>6/2024</td>
<td>All</td>
<td><p>SRA*3*9,</p>
<p>SRA*3*10</p></td>
<td><p>Renamed document &amp; updated Title page.</p>
<p>Added section 1.2.1 File Manager Access Code</p>
<p>Documented the access required to add new Risk Assessment Download Schedule entries in sections <strong>1.3.2</strong> <u>Menu Option Descriptions</u> &amp; <strong>2.1.1</strong> <u>Risk Assessment Download Schedule (Enter/Edit</u>) [SRA DOWNLOAD EDIT]</p>
<p>Documented the modifications to the Check for Risk Assessment Transmission Errors [SRAFERR] option introduced in SRA*3.0*10 in sections <strong>1.3.3</strong> <u>Tasked Option Descriptions.</u></p>
<p>Added info about Cardiac Risk Assessment transmissions in section <strong>3.4</strong> <u>Transmission Layouts</u>.</p></td>
</tr>
<tr class="even">
<td>7/30/2021</td>
<td></td>
<td>SRA*3*5, SRA*3*8</td>
<td>Updated to include new OIT Staff Menu and options used to manage transmission error messages and layouts. Updated Daily Monitoring message.</td>
</tr>
<tr class="odd">
<td>8/31/2020</td>
<td></td>
<td>SRA*3*4</td>
<td>Changes and additions to options and associated new routines.</td>
</tr>
<tr class="even">
<td>6/30/2020</td>
<td></td>
<td>SRA*3*3</td>
<td>Changes and additions to options and associated new routines.</td>
</tr>
<tr class="odd">
<td>5/29/2020</td>
<td>6,8</td>
<td>SRA*3*2</td>
<td>Corrected reference to PURGE^SRAPURGE and message text of the download file notification.</td>
</tr>
<tr class="even">
<td>05/05/2020</td>
<td>All</td>
<td>N/A</td>
<td>Final review (PMO Office Review)</td>
</tr>
<tr class="odd">
<td>3/27/2020</td>
<td>All</td>
<td>N/A</td>
<td>Updates to overview and content (PMO Office Review)</td>
</tr>
<tr class="even">
<td>03/2020</td>
<td>All</td>
<td>N/A</td>
<td><p>Updated the manual to simplify and reflect updated processes.</p>
<p>(S. Winterton, R. Felder, M. Montali)</p></td>
</tr>
<tr class="odd">
<td>06/2017</td>
<td>35,37-38,40</td>
<td>N/A</td>
<td><p>Verbiage &amp; screen shots changed due to Reflections version update</p>
<p>(M. J. Thomas)</p></td>
</tr>
<tr class="even">
<td>04/2017</td>
<td>All</td>
<td>N/A</td>
<td><p>Original Document</p>
<p>(A. Monosky, M. J. Thomas, M. Montali)</p></td>
</tr>
</tbody>
</table>
Table of Contents
Overview
The intended audience for this Surgery Risk Assessment User manual is a broad base of stakeholders who include, but are not limited to, Department of Veterans Affairs (VA) participants, the VA National Surgery Office (NSO), the VA Office of Information and Technology (OIT), Health Product Support (HPS), the VA Project Management Team, Functional Analyst(s), and System Administrators that may work on this project.
The Surgery Risk Assessment Database and the associated processes are designed to document, collect, organize, and transmit surgery case data. It collects non-cardiac assessment data from all the VA medical centers in order to process and store them in a database file at the Surgery Risk Assessment Database. Due to lower volume (about 5,000 cases annually versus 400,000 for non-cardiac), the Cardiac risk assessments are sent via a separate data stream directly to the VA NSO in Denver, CO via Veterans Health Information Systems and Technology Architecture’s (VistA) MailMan messages. (MailMan is software for managing electronic mail and can run processes to route electronic mail.)
Data documented in the Surgery Risk Assessment Database is validated, formatted, analyzed, and developed into reports by the NSO using the VA Surgical Quality Improvement Program (VASQIP) system in a secure online environment. VASQIP characterizes mortality and morbidity rates, both unadjusted and risk adjusted. The VASQIP reports help show comparable and actionable surgical program data to Veterans Health Administration (VHA) facilities, Veterans Integrated Service Networks (VISNs), and VHA Leadership for surgical program assessment and quality improvement.
The published NSO Quarterly Report includes facility-level surgery-specific data for surgical outcomes, quality, staff workload, efficiency, utilization, patient satisfaction, and policy compliance. The NSO Annual Surgery Report and NSO Quarterly Report are reviewed by approximately 2,160 users each year.
This document contains instructions for setup, monitoring, and managing the Surgery Risk Assessment Database, transmissions, and workload reports. It is broken down into four main sections.
1.  Surgery Risk Assessment Database New User Set-Up
2.  NSO Staff Activities and Processes
3.  OIT Staff - Monitoring Activities
4.  Purge Old Assessments

# Risk Assessment Database - New User Set-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section will identify the set-up for Office of Information and Technology (OIT) staff managing and maintaining the Surgery Risk Assessment Module and Database.

## Setting up OIT Staff Supporting the Risk Assessment Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OIT staff supporting the Surgery Risk Assessment Database must have full access to all aspects of the system. This includes programmer level access to troubleshoot and sustain the product. This level of access is given only to a small number of staff specifically assigned and privileged to fulfill this role.

Create and activate new user with the following characteristics:

### File Manager Access Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Manager Access Code should be set to “@”.

FILE MANAGER ACCESS CODE: @//

### Primary Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign the MailMan Menu \[XMUSER\] as the user’s Primary Menu.

### Secondary Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign the following secondary menus:

- Surgery Risk Assessment Manager Menu \[SRATMENU\]
- VA FileMan \[DIUSER\]
- Programmer mode \[XUPROGMODE\]

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign the following security keys:

- SR DOWNLOAD
- SRA CLEANUP \*
- XM GROUP PRIORITY
- XUMGR
- XUPROG
- XUPROGMODE

\*The SRA CLEANUP security key is used to identify whether the user would like daily transmission messages automatically deleted each night from the MailMan IN box. When assigned, all messages that do not indicate a transmission error or workload report will be deleted from the IN box.

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment Database uses several mail groups.

Assign the new user to the following mail groups:

- SRCOSERV – This mail group receives monthly workload report transmission messages.
- RISK ASSESSMENT – This mail group receives non-cardiac and 1-liner transmission messages.
- SRCARDIAC – This mail group receives cardiac transmission messages.
- SRA DOWNLOAD – This mail group receives VASQIP Download message when the download process runs, and the text files are created.
- SRA-MGR – This mail group is made up of those who maintain the Surgery Risk Assessment Database and who receive the monthly workload report.
- SRA OIT SUPPORT – This mail group receives transmission error messages and the message generated at the end of the download process that contains the number of assessment download messages created for each facility.
- SRA RESOURCE MONITOR – This mail group receives notifications of possible stuck resource device. The resource device is used to process surgery risk assessment transmissions.

## Setting up National Surgery Office Staff Supporting the Risk Assessment Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section will identify the set up for National Security Office (NSO) users who will be running options to create reports and downloads on the Surgery Risk Assessment Database.

### File Manager Access Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Manager Access Code should be set to “@”.

FILE MANAGER ACCESS CODE: @//

### Primary Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign the Surgery Risk Assessment Manager Menu \[SRATMENU\] as the user’s Primary Menu.

### Secondary Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign the following secondary menus:

- MailMan Menu \[XMUSER\]

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following security keys are assigned to NSO staff.:

- SR DOWNLOAD

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment Database uses several mail groups. Assign the new NSO user to the following mail group:

- SRA DOWNLOAD – This mail group receives mail messages created by the data download process.

### Outlook Distribution Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign the NSO user to the Outlook Distribution group Surgery Risk Assessment Monthly Download.

## Risk Assessment Database Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes a screen capture and descriptions of the menus and options within the Surgery Risk Assessment Database.

### Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgery Risk Assessment Manager Menu

> 1 Risk Assessment Database Maintenance Menu ...

> 2 \*Create Surgery Risk Assessment Download Files

> 3 \*Download Monthly Workload Reports

> 4 Surgical Case Workload Report (VISNs)

> 5 OI&T Staff Utilities for Risk Assessment Menu...

> Risk Assessment Database Maintenance Menu

> 1 Risk Assessment Download Schedule (Enter/Edit)

> 2 Print Risk Assessment Download Schedule

> 3 VISN Identified for Medical Center (Enter/Edit)

> 4 Display VISN/Medical Center Alignment

> 5 VISN Workload Report Recipients (Enter/Edit)

> 6 List of VISNS and Surgical Nurse Contacts

> 7 Risk Assessment Site (Enter/Edit)

> OI&T Staff Utilities for Risk Assessment Menu

> 1 Print SRA Transmission Message Format

> 2 Edit Transmission Layouts File (#139.4)

> 3 Decipher SRA Transmission Message

### Menu Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the descriptions for each option listed in the menu diagram in the previous section (1.3.1. Menu Diagram). They are listed in alphabetical order.

\*Create Surgery Risk Assessment Download Files \[SRATDL\]

*Note: This option has been replaced with the Task Risk Assessment Download Auto Process \[SRATDLTASK\] option which automates the risk assessment download process. See the Tasked Option Descriptions section for additional information.*

This option tasks the surgery risk assessment download process to run at the date and time selected.

Decipher SRA Transmission Message \[SRAPARSE\]

User can enter a message IEN or find a NC or 1-Liner from their inbox. Tool will ask to choose one case or all (if the message has multiple cases). All lines of the message will be parsed.

Display VISN/Medical Center Alignment \[SRA VISN DISPLAY\]

This option displays the medical center and VISN alignment stored in the RISK ASSESSMENT SITE file (#139.1).

\*Download Monthly Workload Reports \[SRAWTXT\]

*Note: This option has been replaced with the Task Monthly Surgical Case Workload Report \[SRAWTASK\] option. See the Tasked Option Descriptions section for additional information.*

This option allows the downloading of monthly surgical case workload reports to a text file.

Edit Transmission Layouts File (#139.4) \[SRA TRANSMISSION LAYOUTS\]

This option allows modification of the TRANSMISSION LAYOUTS file (#139.4).

List of VISNS and Surgical Nurse Contacts \[SRA VISN RN LIST\]

This option lists the surgical nurse point of contact listed in the Remote Member field in the Risk Assessment mail group for each VISN.

OI&T Staff Utilities for Risk Assessment Menu \[SRA OIT UTILITIES\]

This menu contains options used by OIT Staff to management the Surgical Risk Assessment Database.

Print Risk Assessment Download Schedule \[SRA DOWNLOAD\]

This option prints the download dates stored in the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9).

Print SRA Transmission Message Format \[SRAMLR\]

For either Non-Cardiac or 1-Liner messages, user may select a message line to see a map of the data that is sent in that line.

Risk Assessment Database Maintenance Menu \[SRA MAINTENANCE\]

This menu contains options used to maintain configurable files and mail groups used within the Surgery Risk Assessment Database. These options are used to update these items when changes in staff, VISN associations, or download schedules are made.

Risk Assessment Download Schedule (Enter/Edit) \[SRA DOWNLOAD EDIT\]

This option allows for the entry and editing of the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9). Note that if a date needs to be changed, it will need to be deleted and the new date entered.

The data in this file is used by the daily tasked job, Task Risk Assessment Download Auto Process \[SRATDLTASK\], to determine the dates for which a download text file should be created.

\*\*\*In order to add a new entry using this option, the user must have the FILE MANAGER ACCESS CODE field (#3) in the NEW PERSON file (#200) set to “@”.

Risk Assessment Site (Enter/Edit) \[SRA SITE EDIT\]

This option is used to add, edit, or inactivate sites in the RISK ASSESSMENT SITE file (#139.1). When edits are made, a message is sent to the Surgery Risk Assessment Monthly Download distribution group in Outlook.

Surgery Risk Assessment Manager Menu \[SRATMENU\]

This is the main menu for Surgery Risk Assessment. It contains the options used for the maintenance and functions of the application.

Surgical Case Workload Report (VISNs) \[SRAWRPT\]

*Note: As of November 2019, this report is created and sent to VISN Nurses automatically. This option will only be used for ad hoc requests requiring manual creation.*

This option produces the VASQIP Surgical Case Workload Report which includes surgery workload information and incomplete assessment totals for the selected month. The report may be produced for a single VISN or for all VISNs. The report produced may be e-mailed to VISN Nurse Leaders or to selected individuals. The report may also be displayed on the screen or sent to a printer.

VISN Identified for Medical Center (Enter/Edit) \[SRA VISN UPDATE\]

This option can update the medical center and VISN alignment stored in the RISK ASSESSMENT SITE file (#139.1).

VISN Workload Report Recipients (Enter/Edit) \[SRA VISN NURSE\]

This option allows editing of the VISN RN who receives the Surgical Case Workload Report.

### Tasked Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the list of tasked options that can be utilized. Tasked options do not appear on any Surgery Risk Assessment Database menu used by staff. They are listed in alphabetical order.

Check for Risk Assessment Transmission Errors \[SRAFERR\]

This option is tasked nightly. It checks the IN box of the members of the SRA-MGR mail group who have been assigned the "SRA CLEANUP" security key. It identifies messages which contain "ERROR" or "PROBLEM" in the subject. It sends an email to the member and their remote email with the number of messages in the IN box, total error messages, total messages deleted and information on any error messages. After processing, it will purge non-error Risk Assessment Transmission messages.

For research purposes, the counts, Internal Entry Number (IEN) and Message Subject of deleted messages will be stored in the ^XTMP("SRAFERR") global if needed for 120 days.

Annually, on December 31st, this background task will also call PURGE^SRAPURGE and delete data greater than three full fiscal years old. A temporary backup of the purged records is kept in the ^XTMP global for sixty days. Therefore, copies of the purged records are now stored in the global ^XTMP("SRAPURGE_AUDIT "\_date. The date is in VistA format. (Example:

^XTMP("SRAPURGE_AUDIT 3231116") The global will be purged automatically after sixty days. If the purged records need to be restored with 60 days of the purge, the command RESTORE^SRAPURGE may be invoked from programmer's mode.

SRA Resource Device Monitor \[SRA RESOURCE MONITOR\]

This option monitors the SRA resource device and sends an email notification if a slot in use appears hung.

Task Monthly Surgical Case Workload Report \[SRAWTASK\]

This option is used to queue a recurring task which will be executed on the 27th day of each month to create the VASQIP Surgical Case Workload Report. This report includes surgery workload information and incomplete assessment totals for each VISN. The report is emailed to VISN Nurse Leaders identified in the associated VISN mail group. By tasking this report, the option Surgical Case Workload Report (VISNs) \[SRAWRPT\] will not need to be used manually each month.

Task Risk Assessment Download Auto Process \[SRATDLTASK\]

This option is to be used to queue a recurring task which will be executed daily. It will check the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9) to determine if the process is to be executed. If a download is scheduled for this date, the Surgery Risk Assessment, the Surgery Case Workload Totals, and the Surgery Case Work Incomplete Assessments Totals data will be downloaded to text files.

The text file name format will be as follows:

SRDL_mmddyy.TXT - Surgery Risk Assessment

SRTOTALS_mmddyy.TXT - Workload Totals

SRINCOMP_mmddyy.TXT - Workload Incomplete Assessments Totals

mm = 2-digit month, dd = 2-digit day, and yy = 2-digit year

It will send a MailMan message to users in the G.SRA DOWNLOAD mail group with the file names and directory name. For the Surgery Risk Assessment, it will include details on the number of records included from each site.

Routine also removes SR\* text files greater than 60 days old.

# NSO Staff Activities and Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Risk Assessment Database Maintenance Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the options used to manage data in files used to produce downloads and reports. These options are found on the Risk Assessment Database Maintenance Menu \[SRA MAINTENANCE\].

### Risk Assessment Download Schedule (Enter/Edit) \[SRA DOWNLOAD EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows for the entry and editing of the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9). Note that if a date needs to be changed, it will need to be deleted and the new date entered.

The data in this file is used by the daily tasked job, Task Risk Assessment Download Auto Process \[SRATDLTASK\], to determine the dates for which a download text file should be created.

\*\*\*In order to add a new entry using this option, the user must have the FILE MANAGER ACCESS CODE field (#3) in the NEW PERSON file (#200) set to “@”.

### Print Risk Assessment Download Schedule \[SRA DOWNLOAD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints the download dates stored in the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9).

### VISN Identified for Medical Center (Enter/Edit) \[SRA VISN UPDATE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a medical center has aligned with a different VISN, this needs to be updated in the Risk Assessment Database so that information is passed to appropriate staff. This option allows the realignment of medical centers to different VISNs.

### Display VISN/Medical Center Alignment \[SRA VISN DISPLAY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays each medical center and the associated VISN. Option can display all medical centers, one medical center, or provide a list of the medical centers associated with a specific VISN.

### VISN Workload Report Recipients (Enter/Edit) \[SRA VISN NURSE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows updating of the VISN Surgical Nurse identified to receive Surgical Case Workload Reports. These nurses are set as remote members in VISN mail groups (SRA-VISNxx). The option automatically notifies added recipients to inform them they have been designated to receive these emails and asking to verify the email is correct. These changes are also communicated to the team making up the Outlook mail group: <SurgeryRiskAssessmentMonthlyDownload@VA.GOV>.

### List of VISNS and Surgical Nurse Contacts \[SRA VISN RN LIST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the Surgical Nurse for each VISN who is set to receive Surgical Case Workload Reports.

### Risk Assessment Site (Enter/Edit) \[SRA SITE EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows for adding or editing properties of a Surgery Risk Assessment site. Sites cannot be deleted. They can be designated as ‘inactive’ with this option. Actions taken through this option are communicated to the team making up the Outlook mail group: <SurgeryRiskAssessmentMonthlyDownload@VA.GOV>.

## Downloading Assessment Text Files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The activities within this section are done after the monthly automated process to create assessment download files and workload reports has completed. This introduction will explain the automated process and then the sections specific to downloads and report generation will follow. *Note: The manual process to create text files and workload reports are explained in section 2.3. Manual creation is not needed under normal circumstances.*

### Download and Deliver Text Files (Automatically Done per the Download Schedule)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The automated process to create text files runs based on the Risk Assessment Download Schedule. Three text files are created once the automated process has run.

- Risk Assessment Download file
- Surgical Case Workload Totals
- Workload Incomplete Assessments

After the three text files have been created, a message is sent to members of the SRA DOWNLOAD mail group. The files are securely sent to the NSO staff using tools outside the Surgery Risk Assessment software.

Example: Scheduled Download Message: \<report truncated for this example\>

Subject: VASQIP Download from NDB on 2/21/20

The text file(s) from today's download process are:

Risk Assessment Download file: SRDL_022120.TXT

Surgical Case Workload Totals: SRTOTALS_022120.TXT

Workload Incomplete Assessments: SRINCOMP_022120.TXT

These files will be sent in separate Outlook messages to recipients of the  
Surgery Risk Assessment Monthly Download distribution group. Each file will  
be attached to the message as an encrypted, password protected zip file.

Total Non-Card Assessment Records: 1465

Total VASQIP 1-Liner Records: 1378

Detailed Number Of Records Per Site

SITE NON-CARD 1-LINER

---- -------- -------

405 52 2

436 97

437 9 3

The three files are then automatically sent to members of the *Surgery Risk Assessment Monthly Download* distribution group in Outlook using a Linux Script. This script runs hourly to determine whether new files have been created. The files are sent encrypted, zipped, and are password protected.

Example: Outlook Message with File Attached

![](surgery-risk-assessment-version-3-user-manual/002.png)

## Creating Text Files Manually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a site is late in reporting and the report needs to be re-run by hand, then the text files will need to be recreated manually.  
This can be done two ways:

1.  A new date can be added to the Risk Assessment Download Schedule and the three text files (SRDL_022120.TXT, SRTOTALS_022120.TXT, and SRINCOMP_022120.TXT) will be automatically created on the date added.
2.  The option \*Create Surgery Risk Assessment Download Files \[SRATDL\] can be used to generate the report if needed immediately.

In either case, the files created are automatically delivered the next time that the hourly Linux Script runs.

## Creating Monthly Workload Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Monthly Workload Reports for the VISN Leaders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the process for creating the VISN Workload Reports.  
(Note: With the inception of the automated creation of this report in November 2019, this manual option is less likely to be needed.)

Creating the VISN Workload Report consists of two primary steps:

1.  On the 26th of the month, each site transmits a workload report to the Surgery Risk Assessment Database system for the previous calendar month.
2.  On the 27th (or the next business day), a VISN report is sent automatically from the Surgery Risk Assessment Database system to the VISN nurse leaders.

The Surgical Case Workload Report (VISNs) \[SRAWRPT\] option on the Surgery Risk Assessment Manager Menu \[SRATMENU\] can also be used to manually create the reports if needed.

#### Monthly Workload Report Transmissions from Medical Centers to the Surgery Risk Assessment Database

The Monthly Workload Reports are generated locally at the facilities and are transmitted by VistA MailMan to the Surgery Risk Assessment Database.

Medical centers generate reports by three different mechanisms:

1.  Automatically by the assessment transmission process. This only sends updated workload reports previously submitted.
2.  Manually using the menu option on the Surgery Risk Assessment menu
3.  Automatically on the 26th day of the month when the Surgery Nightly Cleanup and Updates \[SRTASK-NIGHT\] option runs.

Example: Monthly Workload Report Transmission Message

Subj: SURGERY WORKLOAD FOR FEB 2017 \[#10406451\]

27 Mar 2017 17:22:31 -0700 (PDT) 3 lines

From: \<POSTMASTER@LOMA-LINDA.MED.VA.GOV\> In 'WASTE' basket. Page 1

-------------------------------------------------------------------------------

605^3170200^3170327^414^21^16^0^0^16^.8^0^414^0^14^0^5^0^1^1^0^^^0

605^3160200^0^0^3160300^0^0^3160400^0^0^3160500^0^0^3160600^0^0^3160700^0^0^316

0800^0^0^3160900^0^0^3161000^0^0^3161100^0^0^3161200^0^0^3170100^0^0^3170200^0^1^0

605^1^166^129

#### Send the Surgical Case Workload Report (VISNs) to VISN Nurse Leads 

The option Task Monthly Surgical Case Workload Report \[SRAWTASK\] is tasked to run on the 27th of each month to create and send Surgical Case Workload Report (VISNs) to each VISN Nurse. When this option is tasked to run, the manual option described in section 2.3 should only be needed if requested or if for some reason the tasked job isn’t completed as requested.

This option is scheduled or unscheduled using the following Taskman Management option:

Select Taskman Management \<TEST ACCOUNT\> Option: SCHEDULE/Unschedule Options

Select OPTION to schedule or reschedule: SRAWTASK Task Monthly Surgical

Case Workload Report

...OK? Yes// (Yes)

\(R\)

Edit Option Schedule

Option Name: SRAWTASK

Menu Text: Task Monthly Surgical Case Workl TASK ID: 1124594

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: NOV 27,2019@08:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1M

TASK PARAMETERS:

SPECIAL QUEUEING:

After the process is executed, a MailMan message will be sent to the SRA-MGR MailMan group as follows. This message is also sent to mail group members on Outlook.

Subj: SRA Monthly Case Workload Report was tasked to run on Oct 27, 201

\[#11399581\] 10/27/19@08:00 2 lines

From: OITSURUSER.ONE In 'MONTHLY PROCESSING' basket. Page 1

-------------------------------------------------------------------------------

SRA For OCT 2019 Monthly Case Workload Report by VISN was tasked to run.

Please validate the required Mailman Messages were created and sent to the VISN POCs.

#### Review VISN Workload Messages

After the process is completed, confirm that you received the messages sent to the assigned VISN Nurses.

The alignment between medical centers and VISNs, along with the VISN Nurse leader assigned to each VISN are maintained by NSO.

> **NOTE:** There are gaps in VISN numbers. That is expected as some VISNs no longer exist (.i.e., VISN \#3, VISN \#11).

Select MailMan Menu Option: <u>RE</u>ad/Manage Messages

Read mail in basket: IN// \<Enter\> (19 messages)

Last message number: 19 Messages in basket: 19

Enter ??? for help.

IN Basket Message: 1// <u>?</u>

IN Basket, 19 messages (1-19)

\*=New/!=Priority.......Subject.........................From....................

1\. VISN \#1 Workload and Incompletes SURUSER.ONE

2\. VISN \#2 Workload and Incompletes SURUSER.ONE

3\. VISN \#4 Workload and Incompletes SURUSER.ONE

4\. VISN \#5 Workload and Incompletes SURUSER.ONE

5\. VISN \#6 Workload and Incompletes SURUSER.ONE

6\. VISN \#7 Workload and Incompletes SURUSER.ONE

7\. VISN \#8 Workload and Incompletes SURUSER.ONE

8\. VISN \#9 Workload and Incompletes SURUSER.ONE

9\. VISN \#10 Workload and Incompletes SURUSER.ONE

10\. VISN \#12 Workload and Incompletes SURUSER.ONE

11\. VISN \#15 Workload and Incompletes SURUSER.ONE

12\. VISN \#16 Workload and Incompletes SURUSER.ONE

13\. VISN \#17 Workload and Incompletes SURUSER.ONE

14\. VISN \#18 Workload and Incompletes SURUSER.ONE

15\. VISN \#19 Workload and Incompletes SURUSER.ONE

16\. VISN \#20 Workload and Incompletes SURUSER.ONE

17\. VISN \#21 Workload and Incompletes SURUSER.ONE

18\. VISN \#22 Workload and Incompletes SURUSER.ONE

19\. VISN \#23 Workload and Incompletes SURUSER.ONE

IN Basket Message: 1// <u>S</u>ave messages to another basket

Save which messages: (1-19): <u>1-19</u>

Save messages to which basket? <u>WORK</u>LOAD

19 messages saved.

No messages in 'IN' basket.

Below is an example of one of these messages. The message is designed to display 132 columns; therefore, it wraps when displayed on an 80-column screen or printer.

MailMan message for OITUSER.ONE SYSTEMS ANALYST

Printed at FO-HINES.MED.VA.GOV 03/13/17@15:07

Subj: VISN \#22 Workload and Incompletes \[#10374381\] 02/28/17@09:06 39 lines

From: SURUSER.ONE In 'WORKLOAD' basket. Page 1

-------------------------------------------------------------------------------

VA Surgical Quality Improvement Program

Surgical Case Workload Report for VISN \#22

For JAN 2017

Report Generated: FEB 28,2017

\- Cases Performed - Not Non-

Assessed Report

Facility Total Eligible Excluded Assessed Logged Cardiac Cardiac

Cases/Day Received

-------- ----- -------- -------- -------- ------ ------- -----

-- --------- --------

Loma Linda, CA 454 174 18 47 111 0 4

7 2.35 02/27/17

Long Beach, CA 284 92 0 59 41 0 5

9 2.95 02/26/17

San Diego, CA 377 185 44 114 28 7 10

7 5.70 02/28/17

West-LA, CA 283 150 27 120 3 10 11

0 6.00 02/27/17

Number of Facilities Reporting: 4

Number of Incomplete Assessments Report for

VISN \#22

For JAN 2017

Report Generated: FEB 28,2017

01/16 02/16 03/16 04/16 05/16 06/16 07/16 08/16

09/16 10/16 11/16 12/16

Facility C N C N C N C N C N C N C N C N

C N C N C N C N

-------- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

--- --- --- --- --- --- --- ---

Loma Linda, CA 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0

Long Beach, CA 0 0 0 1 0 0 0 1 0 2 0 3 0 0 0 3

0 4 0 3 0 4 0 0

San Diego, CA 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0

West-LA, CA 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0

10% Rule Excluded Cases for VISN \#22

For JAN 2017

Report Generated: FEB 28,2017

Facility 01/16 02/16 03/16 04/16 05/16 06/16 07/16 08/16 09/16

10/16 11/16 12/16 01/17

-------- ----- ----- ----- ----- ----- ----- ----- ----- -----

----- ----- ----- -----

Loma Linda, CA 0 21 0 24 7 31 0 71 32

0 38 0 0

Long Beach, CA 1 62 0 4 17 35 8 37 0

36 0 0 0

San Diego, CA 19 0 41 0 0 18 38 43 21

53 0 56 1

West-LA, CA 7 2 7 10 30 20 19 37 52

0 2 8 0

Enter message action (in WORKLOAD basket): Ignore//

#### Recipients of VISN Monthly Workload Reports

The members of VISN specific mail groups are sent the VISN Monthly Workload Report VistA MailMan messages. Each VISN mail group includes the VISN nurse leader(s) and OIT individuals who maintain the Surgery Risk Assessment Database.

The current list of VISN Nurse Reviewers can be found at the following link:

[<u>VISN Lead Surgical Nurse (sharepoint.com)</u>](https://dvagov.sharepoint.com/sites/VHANSO/SitePages/VISN-Lead-Surgical-Nurse.aspx)

The remote member for a given VISN should correspond to what is documented there. It may be advisable to check the listing once or twice a year to see if there have been any updates. That can be compared with what is set in the Surgery Risk Assessment Database via the option List of VISNS and Surgical Nurse Contacts \[SRA VISN RN LIST\] and, if needed, updated with option VISN Workload Report Recipients (Enter/Edit) \[SRA VISN NURSE\] on the Risk Assessment Database Maintenance Menu \[SRA MAINTENANCE\].

Below is the list of mail groups which these options use to get or set the members. Mail groups can also be edited directly.

NAME: SRA-MGR

NAME: SRA-VISN1

NAME: SRA-VISN2

NAME: SRA-VISN4

NAME: SRA-VISN5

NAME: SRA-VISN6

NAME: SRA-VISN7

NAME: SRA-VISN8

NAME: SRA-VISN9

NAME: SRA-VISN10

NAME: SRA-VISN12

NAME: SRA-VISN15

NAME: SRA-VISN16

NAME: SRA-VISN17

NAME: SRA-VISN18

NAME: SRA-VISN19

NAME: SRA-VISN20

NAME: SRA-VISN21

NAME: SRA-VISN22

NAME: SRA-VISN23

#### Manually Run Surgical Case Workload Report Option

Beginning in November 2019, a scheduled option is used to generate this report, eliminating the need to use this option. It still works and can be used on demand if ever needed.

If there is a need to manually create this report, it can be done using the Surgical Case Workload Report (VISNs) \[SRAWRPT\] option found within the Surgery Risk Assessment Manager Menu \[SRATMENU\]. This option generates individual messages to the VISN nurse leaders.

Surgery Risk Assessment Manager Menu

1 Risk Assessment Database Maintenance Menu ...

2 \*Create Surgery Risk Assessment Download Files

3 \*Download Monthly Workload Reports

4 Surgical Case Workload Report (VISNs)

5 OI&T Staff Utilities for Risk Assessment Menu ...

Select Surgery Risk Assessment Manager Menu \<TEST ACCOUNT\> Option: 4 Surgical Case Workload Report (VISNs)

Surgical Case Workload Report

This report is created automatically on the 27th of each month.

There is no need to create the report using this option unless

there was an issue with the monthly task job.

Do you want to manually create this report? No// y YES

Surgical Case Workload Report

Send VISN reports to VISN leaders ? NO// YES

Compile workload totals for which month and year? MAY 2020//

Compile totals for MAY 2020? YES//

# OIT Staff – Monitoring Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines activities done by OIT staff. It includes daily monitoring of transmissions and potential errors and other monitoring throughout each month.

## Daily Monitoring Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OIT staff assigned to support the Surgery Risk Assessment Database does the daily monitoring activities. The system is monitored to evaluate the number of the transmission messages received from VA medical centers and to identify whether any transmission errors or software errors occurred. It also includes a count and summary of VISTA errors in the Error Trap.

The monitoring done by assigned OIT technical staff consists of two activities: reviewing the nightly message and checking the error trap to validate that no errors are occurring.

Check for Risk Assessment Transmission Errors \[SRAFERR\]

This option is scheduled nightly. It checks the IN box of the members of the SRA-MGR mail group who have been assigned the “SRA CLEANUP” Security Key. It identifies whether there were any transmission errors in the last 24 hours. Any messages which contain “ERROR” or “PROBLEM” in the subject identify a Transmission Error. The task sends an email to the member and their remote email with the number of messages in the IN box, total error messages, total messages deleted and information on any error messages. After processing it will purge non-error Risk Assessment Transmission messages.

For research purposes, the counts, Internal Entry Number (IEN) and Message Subject of deleted messages will be stored in the ^XTMP(“SRAFERR”) global if needed for 120 days.

Example: Nightly Message to OIT Staff (No Errors Identified)

Subj: SRA Daily processing on 1/1/20 \[#11471551\] 01/01/20@23:50 14 lines

From: OITUSER.ONE In 'IN' basket. Page 1

----------------------------------------------------------------------------

Each night, the Surgery Risk Assessment Database automatically captures

the count of VISTA errors logged in the error trap, a count of MailMan

messages in your IN box, and a count of all Risk Assessment transmission

error messages. It sends this information to staff assigned to the SRA-MGR

mail group. If you are also assigned the 'SRA CLEANUP' Security Key,

transmission messages will be deleted.

======================================================================

VISTA ERROR LOG for Jul 19, 2021: 3 errors

COUNT ERROR

1 \<NOTOPEN\>Q1+8^NURARWL1

1 \<UNDEFINED\>REMOTE+2^XMKPR ^DIC(4.2,754,0)

1 \<UNDEFINED\>ZTSK+8^XQ1 \*M

Review and validate that these errors are unrelated to the Surgery Risk

Assessment application.

======================================================================

Here are the results for the cleanup of your MailMan IN box run on 1/1/20:

Total Messages in IN Box: 76

Total Error Messages: 0

Total Deleted Messages: 76

Date Received 1/1/2020: 73

Date Received 12/31/2019: 3

Example: Nightly Message to OIT Staff (Error Identified)

Subj: SRA Daily processing on 1/12/20 - \*\*\*Error Message(s)\*\*\* \[#11471551\] 01/01/20@23:50 14 lines

From: OITUSER.ONE In 'IN' basket. Page 1

----------------------------------------------------------------------------

Each night, the Surgery Risk Assessment Database automatically captures

the count of VISTA errors logged in the error trap, a count of MailMan

messages in your IN box, and a count of all Risk Assessment transmission

error messages. It sends this information to staff assigned to the SRA-MGR

mail group. If you are also assigned the 'SRA CLEANUP' Security Key,

transmission messages will be deleted.

======================================================================

VISTA ERROR LOG for Jul 19, 2021: 1 error

COUNT ERROR

1 \<UNDEFINED\>ZTSK+8^XQ1 \*M

Review and validate that these errors are unrelated to the Surgery Risk

Assessment application.

======================================================================

Here are the results for the cleanup of your MailMan IN box run on 1/1/20:

Total Messages in IN Box: 77

Total Error Messages: 1

Total Deleted Messages: 76

Date Received 1/1/2020: 73

Date Received 12/31/2019: 3

Identified Error Message(s) To Review:

Message \# 11335439

## Download and Report Monitoring Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download monitoring activities are done by OIT staff assigned to support the Surgery Risk Assessment Database. These activities are done at different times each month and consist of checking that the tasked jobs have processed, and notification emails have been received.

Notification of when the download text files and VISN Workload Reports which are created monthly are sent to members of the SRA DOWNLOAD mail group. OIT staff monitors to make sure the process was completed as scheduled.

Example: Scheduled Download Message (display has been truncated)

Subject: VASQIP Download from NDB on 2/21/20

The text file(s) from today's download process are:

Risk Assessment Download file: SRDL_022120.TXT

Surgical Case Workload Totals: SRTOTALS_022120.TXT

Workload Incomplete Assessments: SRINCOMP_022120.TXT

These files will be sent in separate Outlook messages to recipients of the  
Surgery Risk Assessment Monthly Download distribution group. Each file will  
be attached to the message as an encrypted, password protected zip file.

Total Non-Card Assessment Records: 1465

Total VASQIP 1-Liner Records: 1378

Detailed Number Of Records Per Site

SITE NON-CARD 1-LINER

---- -------- -------

405 52 2

436 97

437 9

442 6

460 6

501 15 1

506 15 18

508 41 5

512 1

> **NOTE:** SR\* host files older than 60 days will be deleted when this

process is executed.

## Linux Script for Delivering .txt Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents the setup and use of the Linux Script that delivers the three .txt files after they are created. This script runs every day, hourly. If the files are created since the last time run, the script delivers each file to the *Surgery Risk Assessment Monthly Download* distribution group in Outlook. The files attached to the message are encrypted, zipped, and password protected.

This section of the process guide is primarily used by IT staff assigned to provide System Administration.

Installation:

- Copy script (autoMailer) into /usr/local/sbin
  - chown root:root autoMailer
  - chmod 700 autoMailer
- Copy config file (autoMailer.cfg) into /user/local/sbin
  - chmod root:root autoMailer.cfg
  - chmod 600 autoMailer.cfg
  - Edit config file to ensure correct information is entered
- Put entry into cron to run every hour of every day
  - crontab -e
- \* \*/1 \* \* \* /usr/local/sbin/autoMailer \</dev/null \>/dev/null 2\>&1 &

Files involved:

- /usr/local/sbin/autoMailer
  - bash script file
- /usr/local/sbin/autoMailer.cfg
  - editable configuration file
- /var/log/autoMailer.log
  - automatically created by the script
  - log file of all emails sent
- /tmp/\<zipFileName\>
  - automatically created by the script
  - system temp directory for zip file creation
  - created, sent, and immediately deleted

Script commands:

- To run the script manually
  - /usr/local/sbin/autoMailer
- To view the last 10 emails sent by the script
  - /usr/local/sbin/autoMailer showlog
- To view the prefix to email list in the config file
  - /usr/local/sbin/autoMailer showlist
- To empty the log file
  - If the log file is emptied it will resend any matching files it finds when executed again
    - /usr/local/sbin/autoMailer clearlog

You will get prompted with a confirmation.

Example: autoMailer.cfg File Contents

\# This file is used as a configuration file for the script

\# This file must be in the same directory as the script file

\# Any changes to this file will NOT need a restart of the script

\##### EMAIL CONFIGURATION

\# User to send email from (server will add "@\<serverFQDN" onto the end)

sMailUser="Surgery_Risk_Assessment_Database"

\# Email subject

sMailSubj="Surgery Risk Assessment Download Files"

\# Email body

sMailBody="The download files were created today. They will be provided in three separate messages. Each message has an encrypted zip file attached."

\##### SYSTEM FILE SETUP

\# Log file location and name

sLogFile="/var/log/autoMailer.log"

\# directory to monitor for new files (no trailing /)

\#! this will need to be changed

sFilesDir="/srv/vista/fou/user/hfs"

\##### PREFIX TO EMAIL MATCH

\# If password is set then encryption will be enabled for that user (cannot use "~" in password)

\# Do not use quotes in this section or add spaces in email section

\# UNIQUE PREFIX PASSWORD EMAIL (COMMA SEPERATED W/O SPACES)

SRDL\_ ?????????

REDACTED

SRTOTALS\_ ?????????

REDACTED

SRINCOMP\_ ?????????

REDACTED

Example: Outlook Message with File Attached

![](surgery-risk-assessment-version-3-user-manual/003.png)

## Transmission Layouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The most current transmission mapping documents for each of the four types of transmission messages can be found in the Surgery Risk Assessment Technical Manual. These layouts are used by OIT staff when Transmission Errors are identified.

\*\*\*Note: Cardiac Risk Assessment transmission messages are sent as read-only to the Surgery Risk Assessment Database and are not processed and stored in the SURGERY RISK ASSESSMENT file (#139).

- Cardiac Transmission Layout
- Non-Cardiac Transmission Layout
- 1-Liner Transmission Layout
- Workload Report Transmission Layout

## Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a system generated error message is received, the message must be analyzed to determine the cause of the error. These errors are usually rare and, when they do occur, they are usually caused by a piece of data that failed to pass the input transform on a field in the database. Corrective action depends upon the specific error. Starting in FY21, error messages will parse the line of data that generated the error to help in identifying the issue and provide a more readable format for identifying the source of the error. If corrective action must be taken at the medical center, a mail message should be sent to the appropriate mail group at the medical center, e.g., the RISK ASSESSMENT mail group for a VASQIP data problem.

The OI&T Staff Utilities for Risk Assessment Menu \[SRA OIT UTILITIES\] and options are used to manage transmission layouts for error processing. These options are described in section 3.7.

Example: System Generated Error Message

IN Basket, 264 messages (1-264), 264 new

\*=New/!=Priority.......Subject.........................From....................

\* 81. SURGERY WORKLOAD FOR SEP 2016 \<KSUSER.ONE@KANSAS-

\* 82. SURGERY WORKLOAD FOR SEP 2016 \<KSUSER.ONE@KANSAS-

\* 83. SURGERY WORKLOAD FOR SEP 2016 \<KSUSER.ONE@@KANSAS-

\* 84. SURGERY WORKLOAD FOR SEP 2016 \<KSUSER.ONE@KANSAS-

\* 85. SURGERY WORKLOAD FOR SEP 2016 \<KSUSER.ONE@KANSAS-

\* 86. WEST PALM BEACH VAMC: SURG-NC (1 OF 2) 10/25/1 \<FLUSER.ONE@WEST-P

\* 87. WEST PALM BEACH VAMC: SURG-NC (2 OF 2) 10/25/1 \<FLUSER.ONE@WEST-P

\* 88. SURGERY WORKLOAD FOR SEP 2016 \<FLUSER.ONE@WEST-P

\* 89. \*\* ERROR: 101-223266 VASQIP TRANSMISSION ERROR VASQIP NATIONAL DATABASE

\* 90. WASHINGTON: SURG-NC (1 OF 2) 10/25/16 \<OITUSER.ONE@WASHINGTON.

\* 91. WASHINGTON: SURG-NC (2 OF 2) 10/25/16 \<OITUSER.ONE@WASHINGTON.

\* 92. SURGERY WORKLOAD FOR AUG 2016 \<OITUSER.ONE@WASHINGTON.

\* 93. WEST LA VAMC: SURG-NC (1 OF 1) 10/25/16 \<CAUSER.ONE@WEST-LA.M

\* 94. WEST LA VAMC: CICSP (1 OF 1) 10/25/16 \<CAUSER.ONE@WEST-LA.M

\* 95. WEST LA VAMC: SURG-NC (1 OF 1) 10/25/16 \<CAUSER.ONE@WEST-LA.M

\* 96. SURGERY WORKLOAD FOR JUN 2016 \<CAUSER.ONE@WEST-LA.M

\* 97. SURGERY WORKLOAD FOR SEP 2016 \<CAUSER.ONE@WEST-LA.M

\* 98. BAY PINES VA HCS: SURG-NC (1 OF 1) 10/25/16 \<FLUSER.TWO@BAY-PINES.

\* 99. HOUSTON VAMC: SURG-NC (1 OF 1) 10/25/16 \<TXUSER.ONE@HOUSTON.

\*100. SURGERY WORKLOAD FOR MAY 2016 \<TXUSER.ONE@HOUSTON.

Enter RETURN to continue or '^' to exit: ^

The system generated error message captures the assessment containing the error and identifies the line (node) containing the error. The software attempts to identify the specific error on the line, as well as breakout the data sent on that line for review. Error messages will also contain the original message IEN, and, if available, the patient, the data-entry nurse, and the VISN surgery nurse.

In the example below, the height value (305) is out of range.

Subj: \*\* ERROR: 101-223266 VASQIP TRANSMISSION \[#215864\] 09/15/20@12:54 105 lines

From: VASQIP NATIONAL DATABASE In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

NODE 2 of a NON CARDIAC transmission from Test Location triggered an error.

Possible cause of error:

HEIGHT: 305 - FAILS INPUT TRANSFORM

The point of contact and the nurse at the identified

Medical Center will need to be contacted to correct the issue.

The VISN Nurse identified with this Medical Center: VISNNURSE, ONE

RN reviewer that completed the case: NURSE, ONE

======================================================================

Type of Transmission: NON CARDIAC

Line of message causing the error: NODE 2

Station number: 101

Surgery Case Number: 223415

Patient Name (last 4): SURPATIENT, TWO (1234)

Original Message IEN: 215861

The following fields are contained on the line of data causing issues.

They are listed in the order they appear on the line.

Position Field Name VALUE

======================================================================

15-15 DIABETES: N

16-16 CURRENT SMOKER:

17-17 ETOH \> 2 DRINKS/DAY: N

18-18 PREOP FUNCTIONAL STATUS: 2

19-19 DYSPNEA: 1

20-20 DNR STATUS: N

21-21 EXPECTED TO BE BLANK:

22-22 VENTILATOR DEPENDENT: N

23-23 HISTORY OF COPD: N

24-24 CURRENT PNEUMONIA: N

25-25 INTRAOPERATIVE ASCITES: N

26-26 ASCITES: N

27-28 EXPECTED TO BE BLANK: S

29-29 PRIOR MI: 0

30-30 PCI: 1

31-31 PREVIOUS CARDIAC SURGERY:

32-32 ANGINA SEVERITY:

33-33 CHF WITHIN ONE MONTH:

34-34 HYPERTENSION: 3

35-35 RENAL FAILURE: N

36-36 CURRENTLY ON DIALYSIS: N

37-37 PERIPHERAL ARTERIAL DISEASE: 1

38-38 REST PAIN/GANGRENE (Y/N): N

39-39 EXPECTED TO BE BLANK:

40-40 IMPAIRED SENSORIUM: N

41-41 EXPECTED TO BE BLANK:

42-42 COMA: N

43-44 EXPECTED TO BE BLANK:

45-45 HEMIPLEGIA (Y/N): N

46-46 HISTORY OF TIA'S:

47-47 CVA/RESIDUAL NEURO DEFICIT:

48-48 CVA/NO NEURO DEFICIT:

49-49 EXPECTED TO BE BLANK:

50-50 TUMOR INVOLVING CNS (Y/N): N

51-51 DISSEMINATED CANCER (Y/N): N

52-52 OPEN WOUND OR INFECTION: Y

53-53 CHRONIC STEROID USE (Y/N): Y

54-54 WEIGHT LOSS \> 10%: Y

55-55 BLEEDING DISORDERS: N

56-56 TRANSFUSION \> 4 RBC UNITS: N

57-58 PREGNANCY: NA

59-61 SURGICAL SPECIALTY: 62

62-63 PGY OF PRIMARY SURGEON: 4

64-64 EMERGENCY CASE (Y/N): N

65-66 WOUND CLASSIFICATION: D

67-67 REDO PROCEDURE:

68-68 ASA CLASS: 3

69-69 PRINCIPAL ANESTHESIA TECHNIQUE: G

70-70 ASA CLASS:

71-71 INTUBATED? (Y/N):

72-72 PREOPERATIVE SLEEP APNEA: 2

73-76 HEIGHT: 305 \<\<\<\<\<

77-80 WEIGHT: 296

81-86 PRIOR HEART SURGERY: 0

87-87 ANGINA TIMEFRAME: 1

88-88 BLEEDING RISK DUE TO MED: N

89-91 SPONGE FINAL COUNT CORRECT: Y

92-94 SHARPS FINAL COUNT CORRECT: Y

95-97 INSTRUMENT FINAL COUNT CORRECT: Y

98-98 POSSIBLE ITEM RETENTION: Y

99-99 WOUND SWEEP: Y

100-100 INTRA-OPERATIVE X-RAY: N

101-103 NUM OF PROSTHESIS INSTALLED: 1

104-106 NUM OF READ BACK PERFORMED: 1

107-109 ANGINA SEVERITY: N

110-112 CONGESTIVE HEART FAILURE:

113-115 OP DISPOSITION: W

116-117 IMPAIRED COGNITIVE FUNCTION: 0

118-119 SLEEP APNEA-COMPLIANCE:

120-121 CHEMO FOR MALIG LAST 90 DAYS: 1

122-123 RESIDENCE 30 DAYS PREOP: 3

124-125 AMBULATION DEVICE: 3

126-127 HISTORY OF CANCER DIAGNOSIS: N

128-129 HX RAD RX TO PLANNED SURG: N

130-131 PRIOR SURG SAME OP FIELD: 1

132-133 CONGESTIVE HEART FAILURE PREOP: 0

134-134 PALLIATION: N

135-136 DC/REL DESTINATION: 4

Enter message action (in IN basket): Ignore//

## Troubleshooting Other Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Problems Accessing the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there is an incident that requires the services of the System Administration Support person, and a Developer or OIT Staff support member is not available, assistance through the National Help Desk may be requested to troubleshoot and solve problems.  
*In Service Now the ticket can be assigned to:  
Category: Affected ServiceAffected Service: Surgery Risk Assessment Database*

These incidents may include problems such things as:

- Unable to connect to the account
- Can connect to the account, but cannot log on
- TaskMan is down
- Network mail is down
- VistA mail is not working for an unknown reason

### Low Volume of Incoming Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When reviewing messages, notice the number of messages received. An unusually low number (~300 a day, for several days) may indicate a problem, especially if no new messages have been received in several hours.

Steps to ensure if a problem exists or if it is just a low message volume day may include logging into the system and confirming access to the tools and menu options. The team should send email messages from the environment to FORUM to validate that mail connectivity is complete. They may send a message from an external domain to the Surgery Risk Assessment Database system.

If messages are sent and received without difficulty, there is probably no problem.  
Playing a script to and from an external domain, e.g., FO-BIRM.MED.VA.GOV, also may be useful to further troubleshoot.

### Acknowledgements are Not Received at a Medical Center

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally, a medical center may report that it is transmitting assessments, but not receiving acknowledgement messages. When this occurs, do the following steps:

Note - These steps do not need to be completed in the order listed:

- Determine if the user received the local message listing the assessments transmitted that was created at the time the transmission process ran. This would confirm the transmission process ran.
- Determine if transmission messages have been received from other medical centers and determine if those messages appear to have been processed successfully.
- Determine if transmission messages were received from the medical center on the Surgery Risk Assessment Database. If so, were any error messages generated? If not, open one of the messages, get the station number and an assessment number, then see if the assessment was added to the database by using the VA FileMan inquire option to do a lookup in the SURGERY RISK ASSESSMENT file (#139). The field ID-NUMBER (#.01) is a combination of station number and assessment number separated by a hyphen.

Below is an example of a couple of lines from an assessment message.

\$<u>523</u><u>387159</u> 33170201.08323170201.1029 9 N 0 M16.11 3 N 3J 0

2510311

\$<u>523</u><u>387159</u> 4 0 0

The station number is 523 and the assessment number is 387159.

If reviewing this case, you would do a lookup on “523-387159” in the SURGERY RISK ASSESSMENT file (#139).

To determine if the acknowledgment message was sent, list the next ten messages starting from the message number. This is done by doing a global listing of ^XMB(3.9.

For example, if the message number was 10406257, you would list the entries in ^XMB(3.9 from 10406257-10406267 to see if an acknowledgement message was sent.

Global <u>^XMB(3.9,10406257:10406267,0)</u> -- NOTE: translation in effect

^XMB(3.9,10406257,0)="VA HEARTLAND - WEST, VISN 15: SURG-NC (1 OF 1) 03/27/17^\<KSSURUSER.ONE@KANSAS-CITY.MED.VA.GOV\>^27 Mar 2017 15:00:30 -0500 (CDT)

"

^XMB(3.9,10406258,0)="SURGERY WORKLOAD FOR FEB 2017^\<POSTMASTER@KANSAS-CITY.MED.

VA.GOV\>^27 Mar 2017 15:00:31 -0500 (CDT)"

^XMB(3.9,10406259,0)="SURGERY WORKLOAD FOR FEB 2017^\<POSTMASTER@KANSAS-CITY.MED.

VA.GOV\>^27 Mar 2017 15:00:31 -0500 (CDT)"

^XMB(3.9,10406260,0)="SURGERY WORKLOAD FOR FEB 2017^\<POSTMASTER@KANSAS-CITY.MED.

VA.GOV\>^27 Mar 2017 15:00:31 -0500 (CDT)"

^XMB(3.9,10406261,0)="KANSAS-CITY \*\* ACKNOWLEDGEMENT MESSAGE, VASQIP \*\*^VASQIPNATIONAL DATABASE@FO-HINES.MED.VA.GOV^3170327.150055"

^XMB(3.9,10406262,0)="SURGERY WORKLOAD FOR FEB 2017^\<POSTMASTER@KANSAS-CITY.MED.

VA.GOV\>^27 Mar 2017 15:00:31 -0500 (CDT)"

^XMB(3.9,10406263,0)="SURGERY WORKLOAD FOR FEB 2017^\<POSTMASTER@KANSAS-CITY.MED.

VA.GOV\>^27 Mar 2017 15:00:31 -0500 (CDT)"

^XMB(3.9,10406264,0)="SURGERY WORKLOAD FOR FEB 2017^\<POSTMASTER@KANSAS-CITY.MED.

VA.GOV\>^27 Mar 2017 15:00:31 -0500 (CDT)"

^XMB(3.9,10406265,0)="VDEF ALERT - HINES ISC (578)^\<""VDEF ALERT - HINES ISC (57

8)""@TST.DEV.FO-HINES.MED.VA.GOV\>^27 Mar 2017 15:03:25 -0500 (CDT)"

^XMB(3.9,10406266,0)="CINCINNATI: SURG-NC (1 OF 20) 03/27/17^\<OHSURUSER.ONE@CINCI

NNATI.MED.VA.GOV\>^27 Mar 2017 16:04:34 -0400 (EDT)"

^XMB(3.9,10406267,0)="CINCINNATI: SURG-NC (2 OF 20) 03/27/17^\<OHSURUSER.ONE@CINCI

NNATI.MED.VA.GOV\>^27 Mar 2017 16:04:34 -0400 (EDT)"

If no acknowledgement message is found, check the error trap for an error related to processing the transmission message.

FOURISC4A1:FOU\>D ^XTER

In response to the DATE prompt you can enter:

'S' to specify text to be matched in error or routine name

No error logged on 3/27/2017

Which date? \>

If no related error is in the error trap, try forwarding the message to S.SRATSRV again.

- Find out if the medical center transmitted via the nightly task or via the menu option. If transmission was by the nightly task, is the Surgery Nightly Cleanup and Updates \[SRTASK-NIGHT\] option queued to run and, if so, was it queued by a still active user? If transmission was by the nightly task, have the user transmit via the menu option to see if transmissions are successful.

From time to time, changes are made to IP addresses that result in loss of connectivity with a site. If this happens, the problem may be solved by updating the DOMAIN file. IP addresses may be found using the Domain file inquire option on FORUM.

## OI&T Staff Utilities for Risk Assessment Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OI&T Staff Utilities for Risk Assessment Menu \[SRA OIT UTILITIES\] contains tools used by OIT Staff assigned to support the Surgery Risk Assessment Database. This menu and its options are not used by National Surgery Office staff and do not affect the processing and downloads of assessments from the VA medical centers.

### Print SRA Transmission Message Format \[SRAMLR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display the transmission message formats for Non-Cardiac and 1-Liner transmissions. Using this option, you can view the transmission layout in human readable form for one line or the entire transmission type.

This option depends on data in the SRA TRANSMISSION LAYOUTS file (#139.4). If transmissions are modified by future enhancements to add, modify, or remove fields, information in this file will need to be updated.

### Edit Transmission Layouts File (#139.4) \[SRA TRANSMISSION LAYOUTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to maintain the information in the TRANSMISSION LAYOUTS file (#139.4). This file provides a map of the transmission layouts and is used in generating messages when transmission errors occur. It will only be updated if there are enhancements to Non-Cardiac or 1-Liner Risk Assessment transmissions to add, modify, or delete data being transmitted from the VA medical centers.

Using this option, you first pick the type of transmission and line number. For example, you will select NON CARDIAC-10 to update the information contained on line 10 of the Non-Cardiac Transmissions.

After identifying the transmission type and line number, you can modify the list of fields contained on that line. This is done by selecting the field number and file where the field is stored in the Surgery Risk Assessment Database. The file is most often the SURGERY RISK ASSESSMENT file (#139).

After selecting the field and file numbers, the field name is auto populated.

You will then enter the starting and ending location for the data on that line. In the example below, data for the ROBOTIC ASSISTANCE (Y/N) field is transmitted on characters 59-60 on line 10 of the Non-Cardiac Assessment transmissions.

Select TRANSMISSION LAYOUTS TRANSMISSION TYPE-ROW: NON CARDIAC-10

TRANSMISSION TYPE-ROW: NON CARDIAC-10//

Select FIELD NUMBER: 2006//

FIELD NUMBER: 2006//

FILE NUMBER: 139//

FIELD NAME: ROBOTIC ASSISTANCE (Y/N) Replace

STARTING LOCATION: 59//

ENDING LOCATION: 60//

### Decipher SRA Transmission Message \[SRAPARSE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to select a transmission message received at the Surgery Risk Assessment Database and display the data transmitted for one or more cases included in that message. You can either enter the specific transmission message IEN, or have the option search your inbox for Non-Cardiac or 1-Liner transmission messages.

Once you select a message, you will get a choice of the case numbers transmitted in the message (most messages transmit multiple cases, 1-liner messages can have over 20 different cases/message). You can select a specific assessment, or all of them. The tool will parse each line of the message(s) chosen. Note that each Non-Cardiac message has 24 lines associated with a transmission.

# Purging Assessments Older than Three Years

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As part of the nightly tasked option Check for Risk Assessment Transmission Errors \[SRAFERR\], the software checks to determine whether it is time to purge old assessments. If the date is December 31<sup>st</sup>, the software will delete all entries in the SURGERY RISK ASSESSMENT file (#139) prior to the previous three fiscal years. For example, when run on December 31, 2023, all entries with a date prior to October 1, 2020 will be deleted.