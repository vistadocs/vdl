---
title: AMIE Version 2.7 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: DVBA
app_name: Automated Medical Information Exchange (AMIE)
section: FIN
app_status: active
pkg_ns: DVBA
patch_ver: 2.7
patch_id: DVBA*2.7
group_key: "DVBA:DVBA:2.7"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Medical Center Release Notes](#medical-center-release-notes) - [User Release Notes](#user-release-notes) - [### Start/Stop 35 Day Clock for AMIS 290](#startstop-35-day-clock-for-amis-290) - [## ### Insufficient 2507 Exam Tracking](#insufficient-2507-exam-tracking) - [Divisional Transfer of 7131](
audience: 
keywords: 
  - table
  - contents
  - exam
  - report
  - amie
  - request
  - requests
  - appointment
  - exams
  - guide
page_count: 0
word_count: 3349
section_count: 18
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 1/23/09
revision_oldest: 1/23/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Medical_Info_Exchg_(AMIE)/rnotes.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Medical_Info_Exchg_(AMIE)/rnotes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=31"
---

![](amie-version-2-7-release-notes/001.png)

Automated Medical Information Exchange (AMIE) V. 2.7Release NotesApril 1995

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 1/23/09

| Date | Description (Patch \# if applic.) | Project Manager | Technical Writer |
|----------|---------------------------------------|---------------------|----------------------|
| 1/23/09  | Reformatted Manual                    |                     | REDACTED             |

Table of Contents

# Medical Center Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Medical Center Release Notes](#medical-center-release-notes)
  - [User Release Notes](#user-release-notes)
  - [### Start/Stop 35 Day Clock for AMIS 290](#startstop-35-day-clock-for-amis-290)
  - [## ### Insufficient 2507 Exam Tracking](#insufficient-2507-exam-tracking)
    - [Divisional Transfer of 7131](#divisional-transfer-of-7131)
    - [Inactivation of AMIE Exams](#inactivation-of-amie-exams)
  - [## ### Reprinting 21 Day Certificates by Name or SSN in addition to Date](#reprinting-21-day-certificates-by-name-or-ssn-in-addition-to-date)
    - [Pending 21 Day Certificates Report](#pending-21-day-certificates-report)
    - [Purging Parameter for 2507 Requests](#purging-parameter-for-2507-requests)
  - [## ### Mapped Printing/Super Quit Keys](#mapped-printingsuper-quit-keys)
  - [## ### More Keywords for Physician's Guide for Disability Evaluation Examinations](#more-keywords-for-physicians-guide-for-disability-evaluation-examinations)
    - [Addition of Keywords to the Exam Exceptions for the Physician's Guide for](#addition-of-keywords-to-the-exam-exceptions-for-the-physicians-guide-for)
    - [Disability Evaluation Examinations](#disability-evaluation-examinations)
  - [## ### Exam Introductions Selection added to the Physician's Guide for Disability Evaluation Examinations](#exam-introductions-selection-added-to-the-physicians-guide-for-disability-evaluation-examinations)
  - [## ### Addition of Descriptions on the Initial, Reevaluation, Overview, and Exam Introductions Selections for the Physician's Guide for Disability Evaluation Examinations](#addition-of-descriptions-on-the-initial-reevaluation-overview-and-exam-introductions-selections-for-the-physicians-guide-for-disability-evaluation-examinations)
  - [Technical Release Notes](#technical-release-notes)
    - [I. Data Dictionary](#i-data-dictionary)
    - [II. Templates](#ii-templates)
    - [III. Menu Options](#iii-menu-options)
    - [IV. VA List Manager](#iv-va-list-manager)
    - [V. Miscellaneous](#v-miscellaneous)
    - [VI. Protocols](#vi-protocols)
    - [VII. Printer Configuration](#vii-printer-configuration)
- [# Regional Office Release Notes](#regional-office-release-notes)
  - [User Release Notes](#user-release-notes-1)
    - [Combining Options for Entering 7131 for Admitted Veterans and 7131 for Non-Admitted Veterans](#combining-options-for-entering-7131-for-admitted-veterans-and-7131-for-non-admitted-veterans)
  - [## ### Reverse Print Order of Admission Dates - 7131 Requests](#reverse-print-order-of-admission-dates-7131-requests)
  - [## ### Discharge Types for Discharge Report and Report for Pension and A&A](#discharge-types-for-discharge-report-and-report-for-pension-and-aa)
    - [Inactivation of AMIE Exams](#inactivation-of-amie-exams-1)
  - [## ### Reprinting 21 Day Certificates by Name or SSN in addition to Date](#reprinting-21-day-certificates-by-name-or-ssn-in-addition-to-date-1)
  - [## ### Claim Folder Location](#claim-folder-location)
  - [## ### Start/Stop 35 Day Clock for AMIS 290](#startstop-35-day-clock-for-amis-290-1)
    - [Insufficient 2507 Exam Tracking](#insufficient-2507-exam-tracking-1)
    - [Option added to the Regional](#option-added-to-the-regional)
  - [## ### Divisional Transfer of 7131](#divisional-transfer-of-7131-1)
    - [Device Selection Change](#device-selection-change)
- [Appendix](#appendix)
  - [Hints to Facilitate the Adjustment of the Processing Time of 2507 Requests due to Cancellations at the Veteran's Request](#hints-to-facilitate-the-adjustment-of-the-processing-time-of-2507-requests-due-to-cancellations-at-the-veterans-request)
The Medical Center Release Notes are divided into two sections. The User Release Notes describe changes to the functionality of the MAS portion of the AMIE package. The Technical Release Notes outline changes made to the AMIE files, namespace, options, templates, etc.

## User Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ### Start/Stop 35 Day Clock for AMIS 290

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 2507 average processing time reported on the AMIE AMIS 290 is changed to include adjustments made to the processing time of 2507 requests as the result of veterans cancelling C&P appointments. NOTE: Please see the Appendix of this manual for help in facilitating the adjustment of the processing time of 2507 requests due to cancellations at the veteran's request.

Option(s) Affected: AMIS 290 Report for C&P

Regional File Site Parameter Setup

Check C&P File Integrity (TaskMan)

AMIE/C&P Appointment Link Management (New Option)

Appointment Check-in/Check-out (Scheduling Option)

Cancel Appointment (Scheduling Option)

Make Appointment (Scheduling Option)

Multiple Appointment Booking (Scheduling Option)

Multiple Clinic Display/Book (Scheduling Option)

Appointment Management (Scheduling Option)

Any PIMS Scheduling option from which an appointment

may be made

## ## ### Insufficient 2507 Exam Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMIE allows the entry of 2507 requests with a priority of INSUFFICIENT EXAM whenever a completed 2507 request is returned to the regional office lacking the information necessary to adjudicate the veteran's claim. This enhancement allows the linking of insufficient 2507 requests to the originally entered request.

Option(s) Affected: Manual Printing of New C&P Requests

Reprint C&P Final Report

Print New C&P Requests (TaskManager)

Purge Old 2507 Requests (TaskMan)

Add an Exam to an Existing Request

Transfer a C&P Request to Another Site

Option added to the

C&P Reports Menu: Insufficient Exam Report

### Divisional Transfer of 7131

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement allows the staff at a multidivisional medical center to transfer any portion of a 7131 between their divisions.

Option(s) Affected: New Form 7131 Request Report

Pending Form 7131 Requests Report

Beneficiary Information Status Inquiry

7131 Divisional Transfer (New Option)

### Inactivation of AMIE Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each AMIE exam has a corresponding name and worksheet number. There are two worksheet numbers that have more than one exam name associated with them which reference and display the same information. There should only be one active exam associated with each worksheet. It has been decided by the AMIE Expert Panel (EP) that the Regular Aid and Attendance and the Scars AMIE exams be marked as inactive.

Option(s) Affected: Add an Exam to an Existing Request

Transcribe C&P Data

Print/Reprint C&P Work Sheets

Physician's Guide for Disability Evaluation Exams

Cancel C&P Requests/Exams

Reopen C&P Requests/Exams (Supervisors Only)

## ## ### Reprinting 21 Day Certificates by Name or SSN in addition to Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, a 21 Day Certificate can only be reprinted by the original processing date (the date the 21 Day Certificate was printed). This enhancement allows the user to reprint a 21 Day Certificate by the veteran's name or social security number, as well as the original processing date. Also included in this enhancement is the ability to print 7131s by veteran's name or social security number in addition to the date of the 7131 request.

Option(s) Affected: Reprint 21-day Certificates for MAS

New Form 7131 Request Report

### Pending 21 Day Certificates Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 21-day Cert/Notice of Discharge Report option currently prints a report of both the 21 Day Certificates and the Notices of Discharge. It is not possible to print just the pending 21 Day Certificate report or just the pending Notice of Discharge report. This enhancement allows the user to print both reports (current functionality), print only the pending 21 Day Certificate report, or only the pending Notice of Discharge report.

Option(s) Affected: 21-day Cert/Notice of Discharge Report

### Purging Parameter for 2507 Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, the AMIE package keeps 2507 requests for a preset amount of time before they are purged from the system. This enhancement allows the individual medical centers to select the length of time to keep completed 2507 exams.

Option(s) Affected: Purge Old 2507 Requests (TaskMan)

## ## ### Mapped Printing/Super Quit Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement allows the use of function keys to perform the printing and super quit actions during operation of the on-line Physician's Guide. (NOTE: Super Quit is a function that returns the user back to the menu containing the Physician's Guide option.)

Option(s) Affected: Physician's Guide for Disability Evaluation Exams

## ## ### More Keywords for Physician's Guide for Disability Evaluation Examinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, there is a National Keyword List associated with specific disability exams which allows the user to quickly and easily locate an exam in the Physician's Guide. This enhancement adds additional words and phrases to the distributed National Keyword List. These additional keywords are supplied by the Physician's Guide Work Group.

Option(s) Affected: Physician's Guide for Disability Evaluation Exams

### Addition of Keywords to the Exam Exceptions for the Physician's Guide for 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Disability Evaluation Examinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current keywords available to assist the users in getting to an exam are only available for exams that have an associated diagnostic code. There are several exams that do not have an associated diagnostic code. These exams are referenced as Exam Exceptions. Adding keywords to the exams in the Exam Exceptions makes these exams easily accessible to the users and promotes consistency across examinations. These keywords are supplied by the Physician's Guide Work Group.

Option(s) Affected: Physician's Guide for Disability Evaluation Exams

## ## ### Exam Introductions Selection added to the Physician's Guide for Disability Evaluation Examinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, the Overview selection contains the general overviews and exam introductions. This enhancement separates the overviews and the exam introductions into two separate selections. The result is an Overview selection and an Exam Introductions selection. The Overview selection contains general overviews for the Physician's Guide. The Exam Introductions selection contains introductions to any of the exams contained in the Physician's Guide. Both selections contain the corresponding overviews and introductions from version 2.6 and any added overviews or introductions.

Option(s) Affected: Physician's Guide for Disability Evaluation Exams

## ## ### Addition of Descriptions on the Initial, Reevaluation, Overview, and Exam Introductions Selections for the Physician's Guide for Disability Evaluation Examinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement adds a brief description after each of the prompt selections for Initial, Reevaluation, Overview, and Exam Introductions selections. This description gives the user a better idea of what each selection is about.

Option(s) Affected: Physician's Guide for Disability Evaluation Exams

## Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### I. Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A. FORM 7131 file ^DVB(396,

> 21 DAY CERT RELEASE STATUS field (#6.82) contained a 'C' cross-reference. VA FileMan attempted to use this cross-reference during lookups on this file. This lookup did not work correctly. Version 2.7 of AMIE changes this cross-reference to 'AC'. This prevents VA FileMan from using it during a lookup. All other functionality should remain the same.

> Nodes 6 & 7 are added with V. 2.7. Division and transfer date fields are added for each report field on a 7131. The 'AE' and 'AF' cross-references are added for these new fields.

> The 'AE' cross-reference has been added for the DATE OF REQUEST (#23) and DIVISION (#29) fields.

> B. AMIE SITE PARAMETER file ^DVB(396.1,

> 2507 INTEGRITY REPORT STATUS field (#14) was added. This field controls the 2507 requests to review when running the C&P Exam Integrity Report.

> APPT LINKING ENHANCED DIALOGUE field (#17) was added. This field is an on/off switch that controls the prompts which may be displayed when making C&P appointments.

> DAYS TO KEEP 2507 HISTORY field (#.11) was added. This field holds the number of days to keep 2507 requests.

> C. 2507 REQUEST file ^DVB(396.3,

> REQUEST STATUS field (#17) contained a 'D' cross-reference. VA FileMan attempted to use this cross-reference during lookups on this file. This lookup did not work correctly. Version 2.7 of AMIE changes this cross-reference to 'AF'. This prevents VA FileMan from using it during a lookup. All other functionality should remain the same.

> Two fields have been added to this file. The orIginal 2507 request field (#44) is a pointer to the 2507 request the priority insufficient request is entered for. If the original 2507 request has been purged, the original 2507 processing time is used for the priority insufficient 2507. The original 2507 processing time field (#45) holds the processing time of the original request.

> Two cross-references have been added to this file. The 'ADP' cross-reference has been added for use by the Summary Insufficient Exam report. The 'AORQ' cross-reference has been added for purging old 2507 requests.

> D. 2507 EXAM file ^DVB(396.4,

> Three new fields and one cross-reference have been added to this file. The insufficient remarks field (#80) was added to allow the regional office to provide specifics when a 2507 exam is returned as insufficient. Original providEr field (#.12) was added to hold the name of the provider who completed the original exam. Insufficient reason field (#.11) was added to hold the reason the original exam was insufficient. The 'AIT' cross-reference was added for use by the Detailed Insufficient Exam report.

> E. 2507 INSUFFICIENT REASONS file ^DVB(396.94,

> This is a new file used when priority insufficient 2507 requests are entered. It is installed with data and contains reasons an exam may be returned as insufficient.

> F. AMIE C&P EXAM TRACKING file ^DVB(396.95,

> This is a new file used to keep historical information for C&P exam appointments. It is used to adjust the total processing time for AMIE 2507 requests.

> G. Local Keyword file ^XT(8984.1,

> Local SHORTCUT file ^XT(8984.2,

> Local Synonym file ^XT(8984.3,

> No new fields are being added to these files, although a new variable pointer is being added to the Local Keyword (#8984.1) and Local SHORTCUT (#8984.2) files in the ENTRY field (#.02) of each. This new variable pointer is to allow for the lookup on the EXAM EXCEPTIONS file (#396.93). Entries for the LOCAL Keyword (#8984.1) file will be added during the post-init.

> H. Local Lookup file ^XT(8984.4,

> No new fields have been added to this KERNEL file. AMIE 2.7 adds an entry to this file in order to use MTLU on the EXAM EXCEPTIONS file (#396.93). Along with this new entry is an index and display protocol.

### II. Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Print Templates

> DVBA 21 DAY CERT Prints the 21 day certificate informa-

> (File \#396) tion that is part of the Pending 21 day Certificate Report.

> DVBA NOTICE OF DISCHARGE Prints the notice of discharge informa-

> (File \#396) tion that is part of the Pending 21 day Certificate Report.

> DVBA STATUS Prints the status of reports requested

> (File \#396) on a 7131.

> Sort Templates

> DVBA 21 DAY CERT Sorts the print templates named

> DVBA NOTICE OF DISCHARGE above.

> (Both File \#396)

> Input Template

> DVBA SITE EDIT Edits the information in the AMIE

> (File \#396.1) SITE PARAMETER file (#396.1).

### III. Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Request for 7131 Information (Non-Admitted Vets) option is put out of order. It is also removed from the Regional Office Main Menu. No renumbering of menu options takes place. This option may be removed from any secondary menu options. Once this is done, the option may be deleted altogether.

> The Request for 7131 Information (Admitted Vets) option is renamed to Request for 7131 Information. This option remains as Option Number 1. With the new functionality for entering 7131s, only this option is needed.

> DVBA C MEDICAL ADMIN C&P menu has the AMIE/C&P Appointment Link Management option added as Option Number 12.

> DVBA C REGIONAL OFF RPT menu has the Insufficient Exam Report option added as Option Number 6.

> DVBA C MEDICAL ADM REPORT menu has the Insufficient Exam Report option added as Option Number 10.

### IV. VA List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A. List Template

> DVBA DISCHARGE TYPES - This template is the VA List Manager screen used to collect, adjust, and display the discharge types for the Discharge Report and the Report for Pension and A&A.

> B. Protocols Used when Editing the Discharge Types.

> DVBA Accept Discharge Types - accepts the list of discharge types.

> DVBA Add Discharge Type - allows user to add discharge types to the list.

> DVBA Create Discharge Type List - allows user to create a new list of discharge types.

> DVBA Delete Discharge Types - allows user to delete from the list.

> DVBA Discharge Types (MENU)

### V. Miscellaneous

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In V. 2.7, AMIE no longer makes the call to the LetterMan Editor in the Transcribe C&P Data option. Sites need to evaluate this change and possibly use the Preferred Editor to allow selection of the LetterMan Editor. Information about the Preferred Editor is available in the Kernel documentation.

> The Physician's Guide now uses two function keys, F9 and F12, to execute the actions "Print List" and "Super Quit" respectively.

> AMIE now utilizes the PATIENT file (#2) claim folder location field (#.314) instead of \#.312.

### VI. Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DVBA C&P SCHD EVENT is added to the PROTOCOL file (#101). It asks a series of questions when a user makes a C&P appointment. This protocol is added as an item on the SDAM APPOINTMENT EVENTS protocol. What questions the user is prompted with may be adjusted with the APPT LINKING ENHANCED DIALOGUE field (#17) in the AMIE SITE PARAMETER file (#396.1). (See AMIE Site Parameter file in the technical release notes section of this document.)

### VII. Printer Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Numerous regional offices have reported blank pages printing throughout their C&P Final Reports. This can be corrected by making a change to the TERMINAL TYPE file (#3.2) in one of two ways.

> 1\. Set up a new terminal type, "P-OTHER.xxx", (xxx being whatever characters you choose). Make the characteristics of this terminal type the same as "P-OTHER" except set the page length field (#3) to 58. This option is the preferred choice if terminal type "P-OTHER" is used by other DHCP reports.

> 2\. Edit terminal type "P-OTHER" so that the page length field (#3) is set to 58. Before taking this action, ensure terminal type "P-OTHER" is not used by other DHCP reports.

> Once the terminal type is defined, all regional offices dialing into your medical center utilizing AMIE should be notified to use the correct terminal type when printing/reprinting C&P Final Reports.

> If feasible, naming of the terminal type used should be coordinated with the IRM staffs of other medical centers so that regional offices are using the same terminal type name at each of the medical centers they work with.

# # Regional Office Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The regional office release notes describe enhancement and functionality changes to the regional office portion of the AMIE package.

## User Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Combining Options for Entering 7131 for Admitted Veterans and 7131 for Non-Admitted Veterans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entering a 7131 for an admitted veteran and for a non-admitted veteran is currently two separate options. If a veteran is admitted, you cannot enter a request for 7131 through the non-admitted veterans option and the non-admitted veterans request cannot be entered through the admitted veterans option. In AMIE 2.7, these two options are combined.

Option(s) Affected: Request for 7131 Information (Admitted Veterans)

Request for 7131 Information (Non-admitted Veterans)

New Option: Request for 7131 Information

## ## ### Reverse Print Order of Admission Dates - 7131 Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the regional office enters a 7131 request, the prompt for admission date displays the dates in chronological order. AMIE 2.7 displays the dates in reverse chronological order so that the most recent dates are viewed first.

New Option: Request for 7131 Information

## ## ### Discharge Types for Discharge Report and Report for Pension and A&A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The regional office Discharge Report and Report for Pension and A&A options currently allow the user to select any of the patient movement types. This enhancement limits the type of selectable movements to discharge types. A default list of the ten types most often requested has been formulated by the AMIE EP. This default list is utilized to generate the discharge report.

Option(s) Affected: Discharge Report

Report for Pension and A&A

### Inactivation of AMIE Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each AMIE exam has a corresponding name and worksheet number. There are two worksheet numbers that have more than one exam name associated with them which reference and display the same information. There should only be one active exam associated with each worksheet. It has been decided by the AMIE Expert Panel (EP) that the Regular Aid and Attendance and the Scars AMIE exams be marked as inactive.

Option(s) Affected: Enter a C&P Exam Request

Add an Exam to an Existing Request

Cancel C&P Requests/Exams

## ## ### Reprinting 21 Day Certificates by Name or SSN in addition to Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, a 21 Day Certificate can only be reprinted by the original processing date (the date the 21 Day Certificate was printed). This enhancement allows the user to reprint a 21 Day Certificate by the veteran's name or social security number, as well as the original processing date. Also included in this enhancement is the ability to print 7131s by veteran's name or social security number in addition to the date of the 7131 request.

Option(s) Affected: Reprint a 21-day Certificate for the RO

## ## ### Claim Folder Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As the result of changes to the PATIENT file (#2), AMIE is making a change to the use of the PATIENT file CLAIM FOLDER LOCATION field (#.314). When the regional office is entering a new patient to the PATIENT file, this enhancement allows selection of a claim folder location by station number, name, or from a list of institutions.

Option(s) Affected: Enter a C&P Exam Request

## ## ### Start/Stop 35 Day Clock for AMIS 290

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 2507 average processing time reported on the AMIE AMIS 290 is changed to include adjustments made to the processing time of 2507 requests as the result of veterans cancelling C&P appointments.

Option(s) Affected: AMIS 290 for the Regional Office

### Insufficient 2507 Exam Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMIE allows the entry of 2507 requests with a priority of INSUFFICIENT EXAM whenever a completed 2507 request is returned to the regional office lacking the information necessary to adjudicate the veteran's claim. This enhancement allows the linking of insufficient 2507 requests to the originally entered request.

Option(s) Affected: Enter a C&P Exam Request

Print C&P Final Report (Manual)

Reprint C&P Final Report

Add an Exam to an Existing Request

### Option added to the Regional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Office Reports Menu: Insufficient Exam Report

## ## ### Divisional Transfer of 7131

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement allows the staff at a multidivisional medical center to transfer any portion of a 7131 between their divisions.

Option(s) Affected: Pending Form 7131 Requests Report

Beneficiary Information Status Inquiry

### Device Selection Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Numerous regional offices have reported blank pages printing throughout their C&P Final Reports. This can be corrected by the medical centers making a change to the terminal type you select at the "output device" prompt when utilizing the final report options. The medical center technical release notes in this manual provide instructions for making the change.

You may want to contact the medical center IRM Service to determine if the change has been made and what you should enter at the "output device" prompt (the default of "P-OTHER" may still be appropriate).

Option(s) Affected: Print C&P Final Report (Manual)

Reprint C&P Final Report

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Hints to Facilitate the Adjustment of the Processing Time of 2507 Requests due to Cancellations at the Veteran's Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A key to understanding the automatic adjustment of 2507 processing times due to veteran cancellations is to understand that the important points in the history of the appointments scheduled to complete an examination must be tracked. Appointment history tracking is accomplished through the proper linking of C&P appointments to the 2507 requests that have prompted their scheduling.

The AMIE C&P EXAM TRACKING file (#396.95) keeps appointment history via links between C&P appointments and 2507 requests. A single link should be included in this file for each unique set of appointments scheduled to complete a single examination. In other words, if a radiology exam was scheduled and then cancelled and rescheduled, there should be a single link in the tracking file to indicate the appointment history that occurred to complete the radiology exam.

The tracking of appointment history can be made significantly easier if the APPT LINKING ENHANCED DIALOGUE parameter is set to ON in the AMIE Site Parameter file (# 396.1). This parameter may be turned on or off through the Regional File Site Parameter Setup option.

Turning the APPT LINKING ENHANCED DIALOGUE parameter to ON will add history tracking prompts to the options that allow the scheduling of C&P appointments. If these prompts are correctly answered, the C&P appointment to 2507 request links will be properly maintained.

Turning the APPT LINKING ENHANCED DIALOGUE parameter to OFF will require the site to maintain the C&P appointment to 2507 request links through the AMIE/C&P Appointment Link Management option if they want AMIE to adjust the processing time of their 2507 requests.

The user may inspect the C&P appointment to 2507 request links when scheduling a C&P appointment. The links are displayed for selection when the following prompt is answered YES.

> This 2507 already has appointments.

> Enter '?' for help

> Is this appointment due to a cancellation? NO// YES

The user may also inspect the links through the AMIE/C&P Appointment Link Management option with selection number 1 from the screen titled "Select an appointment to link to the 2507 request".

Duplicate links can be created by answering NO to the prompt "Was {appt date} scheduled to rebook a previous appointment?" after selecting a previously linked appointment, if the previously created link for that appointment has been rescheduled and linked to a different "Current Appt" date. This allows the software to be flexible enough to handle the rescheduling of part of an examination because an exam was not completed due to a veteran's action, (i.e., he or she was late to the appointment).

When inspecting current C&P appointment to 2507 request links, the user may see "\*CL" before the status listed with the appointment. "\*CL" indicates that the listed appointment is the "Current Appt" date on one of the links to that 2507 request.

The AMIE software allows the user to link appointments to 2507 exams cancelled on the 2507. This is to allow the adjustment of processing time if an appointment is cancelled more than an allowable number of times by the veteran, causing the 2507 exam requested to be cancelled and the 2507 to be completed/released back to the regional office.

It is suggested that, when possible, the clerk scheduling and/or linking C&P appointments should have the 2507 available for reference.

The report generated with the Check C&P File Integrity option or the Check C&P File Integrity (TaskMan) option has been changed to include information to assist the medical center in linking C&P appointments to 2507 requests. This report can be customized with the 2507 INTEGRITY REPORT STATUS parameter in the AMIE Site Parameter file (#396.1). If this report is not OFF, it can potentially be large if the site does not set up C&P appointment to 2507 request links. As the site builds its' links, the report will become shorter. This will likely be the case when AMIE V. 2.7 is first installed because no link history will exist.

It is suggested that the medical center continue to track adjustments to 2507 request processing times on paper for two months while building appointment history in the AMIE C&P EXAM TRACKING file (#396.95).