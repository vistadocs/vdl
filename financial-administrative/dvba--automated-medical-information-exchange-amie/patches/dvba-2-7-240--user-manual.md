---
title: AMIE Version 2.7 Medical Admin Service User Manual (UM)
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Medical Admin Service  (UM)
app_code: DVBA
app_name: Automated Medical Information Exchange (AMIE)
section: FIN
app_status: active
pkg_ns: DVBA
patch_ver: 2.7
patch_id: DVBA*2.7*240
group_key: "DVBA:DVBA:2.7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - request
  - date
  - requests
  - report
  - table
  - contents
  - medical
  - appointment
  - number
  - exams
page_count: 0
word_count: 12521
section_count: 20
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: July 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Medical_Info_Exchg_(AMIE)/amie_2_7_240_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Medical_Info_Exchg_(AMIE)/amie_2_7_240_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=31"
---

---
title: |

  Automated Medical Information Exchange (AMIE)

  Software Version 2.7

  Medical Administration Service (MAS) User Manual
---

![](amie-version-2-7-medical-admin-service-user-manual-um/001.png)

July 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 49%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description (Patch # if Applicable)</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/2022</td>
<td>2.0</td>
<td><p>Manual reformatted to VA standards.</p>
<p>New sections under C&amp;P Reports Menu – <a href="#clindocs-metrics-report">4.13.10.11</a> ClinDocs Metrics Report and <a href="#clinical-doc-metrics-data-purge">4.13.10.12</a> Clinical Doc Metrics Data Purge</p>
<p>Updated <a href="#option-index">Section 6</a> Option Index – to include new C&amp;P Reports Menu options.</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>02/2016</td>
<td></td>
<td>Per patch DVBA*2.7*194, update made to replace reference to "eight" validation points with "seven," as the "PRIORITY OF EXAM" has been removed on the Medical Administration C&amp;P Menu. Page 57.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/2009</td>
<td></td>
<td>Reformatted Manual</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [7131/7132](#71317132)
  - [Compensation and Pension](#compensation-and-pension)
  - [Enhancements and Functionality Changes](#enhancements-and-functionality-changes)
  - [Veteran Cancellation Effects on the Start/Stop 35 Day Clock for AMIS 290](#veteran-cancellation-effects-on-the-startstop-35-day-clock-for-amis-290)
- [Orientation](#orientation)
  - [How to Use this Manual](#how-to-use-this-manual)
  - [On-line Help](#on-line-help)
- [AMIE Medical Administration Menu](#amie-medical-administration-menu)
  - [Edit Beneficiary Information Status](#edit-beneficiary-information-status)
  - [Edit 7131 Remarks](#edit-7131-remarks)
  - [New Form 7131 Request Report](#new-form-7131-request-report)
  - [Beneficiary Information Status Inquiry](#beneficiary-information-status-inquiry)
  - [Pending Form 7131 Requests Report](#pending-form-7131-requests-report)
  - [Regional File Site Parameter Setup](#regional-file-site-parameter-setup)
  - [Incomplete Request Report](#incomplete-request-report)
  - [Finalized Report](#finalized-report)
  - [Admission Review Report](#admission-review-report)
  - [Automatic 7131 Finalization (User Mode)](#automatic-7131-finalization-user-mode)
  - [Edit Competency Status](#edit-competency-status)
  - [Medical Administration 7132 Menu](#medical-administration-7132-menu)
    - [Manual Discharge Notification Processing](#manual-discharge-notification-processing)
    - [Manual 21-day Certificate Processing](#manual-21-day-certificate-processing)
    - [Reprint 21-day Certificates for MAS](#reprint-21-day-certificates-for-mas)
    - [MAS Edit/Release of 21-day Certificates](#mas-editrelease-of-21-day-certificates)
    - [21-day Cert/Notice of Discharge Report](#21-day-certnotice-of-discharge-report)
  - [Medical Administration C&P Menu](#medical-administration-cp-menu)
    - [Add an Exam to an Existing Request](#add-an-exam-to-an-existing-request)
    - [Transfer a C&P Request to Another Site](#transfer-a-cp-request-to-another-site)
    - [Manual Return of Transferred C&P Requests](#manual-return-of-transferred-cp-requests)
    - [Schedule C&P Exams](#schedule-cp-exams)
    - [Cancel C&P Requests/Exams](#cancel-cp-requestsexams)
    - [Reopen C&P Requests/Exams (Supervisors Only)](#reopen-cp-requestsexams-supervisors-only)
    - [Transcribe C&P Data](#transcribe-cp-data)
    - [Release C&P Requests](#release-cp-requests)
    - [Inquiry for C&P Requests](#inquiry-for-cp-requests)
    - [C&P Reports Menu](#cp-reports-menu)
    - [Print Blank C&P Worksheet](#print-blank-cp-worksheet)
    - [AMIE/C&P Appointment Link Management](#amiecp-appointment-link-management)
  - [Divisional Transfer](#divisional-transfer)
- [Glossary](#glossary)
- [Option Index](#option-index)
- [Appendix A – AMIE Work Sheet Listing by Body System, Exam Name, and Work Sheet Number](#appendix-a-amie-work-sheet-listing-by-body-system-exam-name-and-work-sheet-number)
The AMIE software automates the administrative procedures involved in sending medical information used in determining veteran benefit payments from the VA medical centers to the VA regional offices.
The AMIE software is composed of two separate modules: 7131/7132 and 2507 Compensation and Pension. Each of these sections provides requesting, tracking, and reporting functions for the various requests entered.

# 7131/7132

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAF 21-7131 is a request for information. The regional office can log into the appropriate VA medical center and request a number of reports for a veteran. These include, but are not limited to, competency reports, admission reports, and asset information. Items such as 21-Day Certificate and Notice of Discharge are automatically tracked and issued only when the event occurs. At this point, they become a 7132, Notice of Discharge and 21-Day Certificate.

Multi-divisional medical centers may transfer portions of the 7131 request between their divisions.

## Compensation and Pension

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A 2507 examination request is a request for specific examination(s) to be performed on a veteran to determine compensation or pension benefits. The regional office has the ability to add a patient to the medical center's database if s/he does not exist there. All aspects of the examination process from notifying MAS of the request to scheduling of the exams, transcribing the results, and forwarding the results to the RO are handled through AMIE.

Medical centers can transfer any exams they are unable to perform to other sites via MailMan messages. The AMIE software at the receiving medical center takes the mail message and enters a 2507 request into that hospital's database. Once these exams are completed, they are transferred back to the original medical center.

Both modules of AMIE generate a number of reports to provide medical center and regional office personnel with the status and timeliness of any request. The AMIS 290 report monitors the progress of 2507 exams.

The AMIE software greatly reduces the time it takes to exchange patient information between the medical centers and regional offices. It reduces the amount of paper forms, provides better monitoring of the exam process, and most importantly, allows the veteran to receive benefits due her/him in a more timely and efficient manner. The AMIE user documentation is divided into two separate manuals; one designed for Medical Administration Service personnel at the medical centers, and the other for regional office personnel. The documentation has been presented in this manner to accommodate these two distinct groups of AMIE users. Each manual provides detailed information on how to use the options contained in the respective menus, AMIE Medical Administration Menu and AMIE Regional Office Main Menu.

Related manuals include the AMIE Regional Office User Manual, AMIE Technical Manual, AMIE Package Security Guide, AMIE Installation Guide, and the AMIE Release Notes.

## Enhancements and Functionality Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Medical Center

- Ability to print the pending 21 Day Certificate report and the pending Notice of Discharge report, print only the pending 21 Day Certificate report, or only the pending Notice of Discharge report.
- Allow the individual medical centers to select the length of time to keep completed 2507 exams.

Regional Office

- Reverse print order of admission dates - 7131 Requests.
- Combining options for entering 7131 for admitted veterans and 7131 for non-admitted veterans.
- Limit the type of selectable movements to Discharge Types for Discharge Report and Report for Pension and A&A.

Both Medical Center and Regional Office

- Reprinting 21 Day Certificates by name or SSN in addition to date.
- Print 7131s by name or SSN in addition to date.
- Select the claim folder location by station number, name, or from a list of institutions when entering a new patient to the PATIENT file.
- Average processing time reported on the AMIE AMIS 290 changed to include adjustments made to the processing time of 2507 requests as the result of veterans cancelling C&P appointments.
- Allow the linking of insufficient 2507 requests to the originally entered request.
- Transfer any portion of a 7131 between the divisions of multidivisional medical centers.
- Inactivation of the Regular Aid and Attendance and the Scars AMIE exams.

## Veteran Cancellation Effects on the Start/Stop 35 Day Clock for AMIS 290

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The average processing time reported on the AMIE AMIS 290 is the average time it takes to process 2507 requests from the time they are reported to MAS to the time they are released to the regional office. This calculation does not adjust for processing time added as the result of the cancellation and rescheduling of a C&P examination by the veteran.

The following guidelines were developed from discussions between AMIE development at the REDACTED and the AMIE Expert Panel regarding adjustments to the 2507 C&P request processing clock as reported on the AMIE AMIS 290.

- Adjustments may be made to the processing clock only when a C&P appointment is canceled and rescheduled at the request of the veteran, or the veteran fails to report for the appointment (no-show).
- No more than a total of 30 days may be subtracted from the processing time of a C&P request because an appointment has been rescheduled at the request of the veteran.
- The processing time clock may not be stopped until the date of the last original appointment scheduled by the medical center.
- An appointment that is canceled and rescheduled for a date prior to another originally scheduled appointment will not affect the total processing time of that 2507 request.
- The occurrence of the regional office adding an examination to a 2507 request is rare enough so that it does not warrant adjustments to the processing clock.
- If an appointment is rescheduled by the medical center, a cancellation by the veteran does not warrant the returning of that 2507 request to the regional office as incomplete. This is due to only one of the cancellations being at the veteran's request.
- If an original appointment is rescheduled by the medical center, that rescheduled date will be considered the original appointment date. If an original appointment date is rescheduled by the medical center for a date later than the current last original appointment date, the rescheduled appointment date will redefine the point at which the processing clock can be stopped.
- If the veteran reschedules an appointment for a date beyond the last originally scheduled appointment \[therefore stopping the processing time clock at the last originally scheduled appointment date and starting it again on the reschedule date\] and the medical center then reschedules the new appointment, the starting of the processing time clock will not be affected unless the appointment is moved to a date earlier than the date rescheduled at the request of the veteran. (See Diagrams 6 and 7.)

The following are diagrams of scenarios that may result from C&P appointment cancellations. Included with each diagram is a description of how the AMIE software will implement the effect of that situation on the calculation of the AMIE AMIS 290 Average Processing Time.

![](amie-version-2-7-medical-admin-service-user-manual-um/002.png)

This is a simple scenario in which a single appointment is canceled and rescheduled by the veteran. The appointment is rescheduled within 30 days of its original schedule date so those days between the original and rescheduled appointment dates are not counted into the total processing time of the request (and therefore do not affect the average processing time for the medical center.) In this scenario, the total processing time for this request is 20 days.

![](amie-version-2-7-medical-admin-service-user-manual-um/003.png)

In the above scenario, appointment 2 is canceled and rescheduled by the veteran before the last originally scheduled appointment date (appointment 3). In this case, no time is deducted from the total processing of the 2507 request. Its processing time is 41 days (May 1st until June 10).

![](amie-version-2-7-medical-admin-service-user-manual-um/004.png)

In this scenario, appointment 2 is canceled and rescheduled for a date later than the last originally scheduled appointment date (appointment 3). Because the reschedule date for appointment 2 (6/4) is within 30 days of the original date for appointment 2 (the rescheduling window runs until 6/19), the elapsed time between appointment 3 (5/27) and the rescheduled date for appointment 2 (6/4) is not counted as part of the total processing time for the request. For this 2507 request, the total processing time would be 33 days.

![](amie-version-2-7-medical-admin-service-user-manual-um/005.png)

The rescheduled date of a C&P appointment is required to be within 30 days of the last original appointment date of those appointments on the 2507 that have been rescheduled. If a C&P appointment is rescheduled by the veteran for a date later than the end of that 30 day window, those days beyond the end of that window are counted against the processing time of that 2507 request. Diagram 4 depicts such a situation. Appointment 2 was originally scheduled May 20. That appointment is canceled and then rescheduled by the veteran for June 25. The days from May 27 (the latest originally scheduled appointment date) until June 19 (the end of the 30 day window for the originally scheduled date of appointment 2) are not counted against the processing of that 2507 request. However, the days beyond the end of the 30 day rescheduling window (June 19) until the rescheduled appointment date (June 25) are counted against the processing time of the 2507 request. This request would have a total processing time of 38 days.

![](amie-version-2-7-medical-admin-service-user-manual-um/006.png)

The above scenario depicts the rescheduling of two appointments for a 2507 at the request of the veteran. Appointment 2 is rescheduled to June 25 from its original date of May 20. Appointment 3 is rescheduled to June 22 from its original date of May 26. Under these circumstances, appointment 2 is scheduled outside its 30 day rescheduling window and appointment 3 is scheduled within its 30 day rescheduling window. The 30 day rescheduling window extends from the latest originally scheduled appointment date. Hence, both appointments 2 and 3 may be rescheduled by June 25, and the processing time clock starts again on June 25 (the latest rescheduled appointment date of the two exams rescheduled). The processing time for this 2507 request would be 32 days.

![Diagram 6 depicts the occurrence of a veteran rescheduling appointment 3 originally scheduled for May 27. The reschedule date is June 19. The medical center then reschedules the June 19 appointment for June 25. The processing clock would not run from May 27 until June 19 because this is the result of the veteran rescheduling the appointment. The clock would count those days processing from June 19 until June 25, however, because this reschedule was the result of action by the medical center. The processing time for this request is 38 days.](amie-version-2-7-medical-admin-service-user-manual-um/007.png)

*Diagram 6 depicts the occurrence of a veteran rescheduling appointment 3 originally scheduled for May 27. The reschedule date is June 19. The medical center then reschedules the June 19 appointment for June 25. The processing clock would not run from May 27 until June 19 because this is the result of the veteran rescheduling the appointment. The clock would count those days processing from June 19 until June 25, however, because this reschedule was the result of action by the medical center. The processing time for this request is 38 days.*

![](amie-version-2-7-medical-admin-service-user-manual-um/008.png)

The above scenario diagrams the occurrence of an appointment originally rescheduled by the veteran for June 19 being rescheduled again by the medical center for a date earlier than June 19. Prior to the second reschedule, the days between May 27 and June 19 would not have been counted against the processing clock of the 2507 request. Because the second reschedule moved the appointment date up, only the days between May 27 and June 10 are not counted. The processing time for this request is 47 days. (Please note the fact that the medical center moving the C&P appointment to an earlier date is irrelevant. The occurrence of the appointment being moved to an earlier date changes the amount of adjustment that may be made to the processing clock.)

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Use this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMIE MAS User Manual is provided in Adobe Acrobat PDF (portable document format) files. The Acrobat Reader is used to view the documents. If you do not have the Acrobat Reader loaded, it is available from the VISTA Home Page, “Viewers” Directory.

Once you open the file, click on the “Show/Hide Navigation Pane” icon on the Acrobat toolbar, then the “Bookmarks” tab. You may then click on the desired entry name to go to that entry in the document. You may print any or all pages of the file. Click on “Print” icon and select the desired pages. Then click “OK”.

Each menu section begins with an overview of the options contained in it, followed by the actual option documentation. The options are listed in the order in which they appear on the menu. The option documentation gives a detailed description of the option and what it is used for. It contains any special instructions related to the option.

## On-line Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Typing in a \<?\> at most prompts will display any on-line help available. Help messages provide lists of acceptable responses or format requirements which provide instruction on how to respond. Anytime choices appear with numbers, the system will usually accept the number or the name. As many as three question marks \<???\> may be entered to get varying degrees of help.

# AMIE Medical Administration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the main menu for medical center users. The following is a brief description of the options contained in this menu.

Edit Beneficiary Information Status

This option allows MAS personnel to update 7131 request statuses.

Edit 7131 Remarks

This option is used to add/edit the ADDITIONAL REMARKS field of the 7131 request.

New Form 7131 Request Report

The New Form 7131 Request Report option provides new 7131 requests for a date range. It should be used if the TaskMan version of this option has not been set to run or did not run correctly.

Beneficiary Information Status Inquiry

This option provides the current status of any request for information.

Pending Form 7131 Requests Report

This report will display all requests that are not finalized. It lists only the items pending for each patient request.

Regional File Site Parameter Setup

This option is used to add/edit AMIE site specific parameters and is normally utilized by IRM Service.

Incomplete Request Report

The Incomplete Request Report option will print a list of incomplete requests by date of request.

Finalized Report

This option provides information on those 7131 requests which have been finalized.

Admission Review Report

This option provides eligibility data for veterans admitted on a selected date.

Automatic 7131 Finalization (User Mode)

If the TaskMan option fails, MAS may use this option to manually finalize all applicable 7131 requests.

Edit Competency Status

This option allows editing of the RATED INCOMPETENT field (#.293) of the PATIENT file (#2).

Medical Administration 7132 Menu

This submenu contains the options relating to 21-Day Certificates and Notices of Discharge.

Medical Administration C&P Menu

This submenu contains the options relating to compensation and pension examinations.

7131 Divisional Transfer

This option is used to transfer the request for reports received from the regional office on 7131s from one medical center division to another.

## Edit Beneficiary Information Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users who hold the DVBA SUPERVISOR security key may see requests with both the PENDING and COMPLETED statuses. Users without the key will only see requests with the PENDING status. If the user does not hold the supervisor key, and the request has been closed, the message "This record has already been finalized on {date}" will be displayed and editing will not be allowed.

This option allows MAS personnel to update 7131 request statuses. It can be used to edit both types of 7131 requests; those requested by admission date, and those requested by activity date. As MAS personnel comply with the regional office requested items, they may use this option to change the item status from PENDING to COMPLETED.

“This record is finalized. Do you want to un-finalize it?” prompt may appear if the user is designated as a supervisor and the request is already finalized.

Items on the request will be listed individually. If you change a status from PENDING to COMPLETED, the system will prompt for the completion date.

## Edit 7131 Remarks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to add/edit the ADDITIONAL REMARKS field of the 7131 request. It may be used for either activity or admission date requests. If more than one applicable request exists for the selected patient, you will be prompted to choose the request you wish to see. Utilizing this option will not change the last edit date of the request.

You may enter \<??\> at the EDIT Option prompt for a list of editing capabilities.

## New Form 7131 Request Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The New Form 7131 Request Report option provides new 7131 requests for a date range or individual patient. The TaskMan version of this option is usually set to run daily as a background option and new requests for the day are sent to a designated MAS printer. This particular option has been designed to be printed to the screen and may be used if the TaskMan option has not been set to run or did not run correctly.

You may select the request(s) by individual patient name, social security number, or date range. You may choose a long or short version of the report. The long version provides a separate report for each request in the selected date range. Information provided on the long report may include division, patient name, claim number, social security number, admission or activity date, request date, remarks, items requested, and requester. The short version contains the requests in a list format and does not include remarks, items requested, or requester. The division listed at the top of each 7131 printed will be the division entered by the regional office as the routing location. Normally the short version will NOT be used except for re-reporting of a day or by supervisors.

To use this option, you must hold the DVBA SUPERVISOR security key.

The REMOTE SITE prompt will appear if date range was entered at the first prompt. Enter your site name if you are at a single-division facility. If you are at a multi-divisional facility, enter the name of the division for which you wish to see requests. All 7131s that have a report assigned to the division will be printed.

> **NOTE:** The appearance of an asterisk (\*) appended to the REQUESTED BY field denotes that the request was modified with the addition of either a Notice of Discharge, hospital summary, or both by the 21-Day Certificate generation program. The \* is added when the request is made new to MAS.

## Beneficiary Information Status Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will give the current status of any request for information. It provides the user with what information was requested, when it was requested, and who took the action. This option may be used to view either admission date or activity date requests.

Requests prior to installation of AMIE V. 2.7 may not show an entry in the "Current Division" column for each requested item. In those cases, the division is the same as the receiving division. Requests subsequent to installation of AMIE V. 2.7 will display an entry in the "Current Division" column for each requested item.

Users may see two "operator" names on the output for the Notice of Discharge and the 21-Day Certificate data items. For the Notice of Discharge, the operator will be "Notice of Discharge" only after the regional office actually prints the notice. For the 21-Day Certificate, the operator will be "21-Day Certificate" if the certificate was generated or "Not applicable" if the certificate was not generated.

You will be prompted for a patient name and a device. The recommended device is HOME as this report was designed to print on the screen. If more than one applicable admission or activity date exists for the selected patient, you will be prompted to choose the date you wish to see.

> **NOTE:** The appearance of an asterisk (\*) appended to the REQUESTED BY field denotes that the request was modified with the addition of either a Notice of Discharge, hospital summary, or both by the 21-Day Cert generation program. The \* is added when the request is made new to MAS.

## Pending Form 7131 Requests Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will display all requests that are not finalized. It lists only the items pending for each patient request. The elapsed days (total work days passed since the request was logged) is displayed which may be useful in keeping track of outstanding requests. You may choose to sort the report by regional office number and division. If you choose to report for a specific division, any 7131 that has that division responsible for any portion of the request will be included.

Requests may appear on this report with no items listed as pending. These are requests where the final item(s) have been completed but the request itself has not yet been finalized by the system. This should be a rare occurrence. If this does occur, wait 24 hours to see if the auto-finalization program will remedy the situation. If the auto-finalization program did not run, you may use the Request for 7131 Information options to edit the request. IRM Service should be notified if it appears the auto-finalization program is not set to run.

Since the pending report may serve many divisions or remote sites, the division which is responsible for the completion of the request is displayed at the top of each printed record.

## Regional File Site Parameter Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to add/edit AMIE site-specific parameters and is normally utilized by IRM Service. It is very important that all parameters are set up correctly or the package will not function properly. To use this option, you must hold the DVBA SUPERVISOR security key.

Be sure to give the regional office personnel the necessary FileMan access codes to be able to add new veterans to the PATIENT file (#2). This is required for the C&P part of the package.

All of the regional office users should have only one division assigned to them in the NEW PERSON file (#200). This should be the station number of their regional office. Failure to assign the correct division or if multiple divisions are inadvertently assigned will result in incorrect data being entered into the file.

The following is an explanation of some of the parameters.

DAYS TO KEEP 2507 HISTORY:

This is the number of days 2507 requests will be kept on file before being purged. Enter a number between 120 and 999.

The prompts from ALL ADMISSIONS REPORT DATE to PENSION/A&A REPORT DATE are courtesy report dates for the regional office. These dates will appear in other options and tell the regional office the last time the report was processed. Once entered, they are usually only modified by the system.

NUMBER OF DAYS TO KEEP HISTORY:

This is the number of days 7131 information will be kept on file before being purged. Enter a number between 30 and 999.

Select REGIONAL OFFICES ALLOWED:

Set up the regional offices which will be accessing your system for reporting. The offices must be set up or the Notices of Discharge and 21-Day Certificates will not be produced. This field is a pointer to the INSTITUTION file (#4) and as each Notice of Discharge is compiled, this field is checked to see if the veteran's claim folder location is one of the allowed regional offices.

Select REMOTE SITE (7131):

Enter a valid medical center division for your facility for the 7131/7132 part of the package. If this is not properly filled in, reports for new requests will not be generated. Even if you are at a single-division facility, this must be filled in.

PRINTER NUMBER:

Enter a valid printer name or number for the selected division. Type the name or number of the device where you want 7131/7132 requests to print. The device must exist in the DEVICE file (#3.5). Repeat these two steps for each applicable division.

Regional File Site Parameter Setup

Select REMOTE SITE (2507):

Enter a valid medical center division for your facility for the 2507 part of the package. Even if you are at a single-division facility, this must be filled in.

PRINTER NUMBER:

Enter a valid printer name or number for the selected division. Type the name or number of the device where you want 2507 requests to print. The device must exist in the DEVICE file (#3.5). Repeat these two steps for each applicable division.

2507 INTEGRITY REPORT STATUS:

Determines which 2507s to review when reporting C&P appointment links on the C&P Exam Integrity report. If the parameter has a value of OPEN, the following statuses are reviewed and reported: pending; reported; pending, scheduled. If the parameter has a value of COMPLETED, the following statuses are reviewed and reported: released to RO, not printed; completed, printed by RO. With a value of ALL, all 2507 requests are reviewed and reported. With a value of OFF, the site turns off the review and reporting of 2507 request appointments.

Select C&P ROUTING LOCATION:

Enter any hospital location (pointer to HOSPITAL LOCATION file (#44)) where automatic lab and/or X-ray results would be routed. This is a multiple field so as many as necessary may be entered. These locations will be used during the final printing of a C&P request to screen lab and radiology results which were ordered for a C&P exam. If the routing location is incorrect and/or does not reside in the AMIE SITE PARAMETER file (#396.1), lab and radiology results will NOT be printed with the final C&P results.

RUN NEW REQUESTS ON SATURDAY:

Answer YES to have Friday requests printed on Saturday or NO to have them printed on Monday or the first work day after Monday. If this field is left blank, the system will automatically assume a NO response.

APPT LINKING ENHANCED DIALOGUE:

Enter ON or OFF to display/not display warnings and certain prompts that may appear when scheduling C&P appointments. If turned OFF, the appointment is associated to the 2507 with a new link. If turned ON, the software checks for the existence of C&P appointment links, and depending on what is found, provides prompts and warnings to ensure that the links are properly maintained.

## Incomplete Request Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will print out statistics on incomplete requests. The report is sorted by date of request and provides the following data items: patient name, social security number, date of request, requesting location, and person who made the request. Subtotals for each date of request and a total amount are also provided.

The option should be run and the report reviewed on a regular basis to keep track of all outstanding requests.

> **NOTE:** The appearance of an asterisk (\*) appended to the REQUESTED BY field denotes that the request was modified with the addition of either a Notice of Discharge, hospital summary, or both by the 21-Day Cert generation program. The \* is added when the request is made new to MAS.

## Finalized Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a report on finalized requests. It provides the following data items for each request listed: patient name, social security number, requesting regional office, number of days it took to process the request, date requested, date finalized, and employee who finalized. It also gives the cumulative number of elapsed days for all requests. This report requires a 132 column margin width to print correctly.

## Admission Review Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is designed for the eligibility clerk in MAS. It provides eligibility data for veterans admitted on a selected date. The clerk may review the data and supply any missing information that may be needed for AMIE purposes. This missing information would be entered through the appropriate MAS options.

You will be prompted for an admission date and a device. The report requires a 132 column margin width for proper display.

## Automatic 7131 Finalization (User Mode)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From time to time TaskMan may miss running the automatic finalization program during off hours. If this occurs, MAS may use this option to manually finalize all 7131 requests that are ready for finalization. Information provided for each veteran on the report includes name, social security number, and admission date. The total requests finalized is also provided.

## Edit Competency Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows editing of the RATED INCOMPETENT? field (#.293) in the PATIENT file (#2), if necessary. You will be prompted to enter the patient name and whether or not the patient is rated incompetent. You may enter 0 or N for NO, 1 or Y for YES.

## Medical Administration 7132 Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medical Administration 7132 Menu contains those options that pertain to 21-Day Certificates and Notices of Discharge. The following is a brief description of the options contained in this menu.

Manual Discharge Notification Processing

This option allows MAS personnel to reprocess any discharge date and generate any missed Notice of Discharge. It should be run only if the automatic discharge notification processing fails.

Manual 21-day Certificate Processing

This option is used to process original 21-Day Certificates. It should be used only if the automatic processing fails.

Reprint 21-day Certificates for MAS

This option is used to reprint 21-Day Certificates.

MAS Edit/Release of 21-day Certificates

Through this option 21-Day Certificates are completed and released to the regional office for printing.

21-day Cert/Notice of Discharge Report

This report displays all 7131 requests which contain a request for a Notice of Discharge or a 21-Day Certificate.

### Manual Discharge Notification Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow MAS personnel to reprocess any discharge date and generate any missed Notices of Discharge. It should be run only if the automatic discharge notification processing fails, since the reprocessing of past dates may possibly regenerate notices that the regional office already has received and disposed of.

You will be prompted for a beginning date, ending date, and device. The program will process the entered date range and log notices for each patient record which meets the criteria. This program will NOT produce duplicate notices for the same patient; that is, if there is already one on file for a particular discharge date, another one will not be produced.

Information provided includes patient name, social security number, and admission date.

### Manual 21-day Certificate Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow MAS personnel to process original 21-Day Certificate copies. It should be run only if the automatic 21-Day Certificate processing fails. Utilizing this option will change the 21-Day Certificate status on the 7131 from "pending" to "completed". A "completed" status indicates the certificate has been printed and sent to the physician for diagnosis and signature.

Only one day at a time can be reprinted. ROC 119, which appears at the bottom of each certificate, stands for VA Form 119 - Report of Contact.

### Reprint 21-day Certificates for MAS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From time to time it may be necessary for MAS to reprint original 21-Day Certificates. This may be due to printer problems, certificate loss, etc. This option will allow MAS to reprint all certificates for any given day (provided the 7131 record has not already been purged) or an individual patient's certificate.

You may choose to reprint an individual certificate by patient name or social security number, or all certificates by original processing date. The certificate produced is exactly the same as the original certificate.

ROC 119, which appears at the bottom of each certificate, stands for VA Form 119 - Report of Contact.

This option will not work correctly if the original date is not known or is incorrect.

### MAS Edit/Release of 21-day Certificates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Through this option 21-Day Certificates are completed and released to the regional office for printing.

Before this option is utilized the original certificates must have been produced either automatically or manually on the system and delivered to the physicians for diagnosis and signature.

Since the system automatically finalizes requests, it is possible that a request would be finalized before the certificate was actually completed. Note that there is not any check for the request status for any phase of the 21-day completion process.

You must hold the DVBA 21-DAY CERT CLERK security key to enter data through this option and the DVBA RELEASE 21-DAY CERT security key to release the certificate to the regional office.

### 21-day Cert/Notice of Discharge Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display a list of 7131 requests which contain a request for a Notice of Discharge, a request for a 21-Day Certificate, or both. Patients appear on the report in alphabetical order.

Information provided on the report includes patient name, social security number, and the following fields for both Notice of Discharge and 21-Day Certificate: item requested (yes/no), completion date, status (pending or completed), and completed by.

If both items are selected, the report requires a 132 column margin width to print properly.

## Medical Administration C&P Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medical Administration C&P Menu contains all the options necessary to handle compensation and pension examinations at the medical center. The following is a brief description of the options contained in this submenu.

Add an Exam to an Existing Request

This option allows an examination to be added to an existing C&P request.

Transfer a C&P Request to Another Site

This option allows medical center personnel to transfer an exam or entire C&P request to another site.

Manual Return of Transferred C&P Requests

If the automatic return of a transferred-in request fails, it may be transferred out manually through the use of this option.

Schedule C&P Exams

The Schedule C&P Exams option allows medical center personnel to schedule C&P exams without leaving the AMIE software.

Cancel C&P Requests/Exams

This option is used to cancel an exam on a C&P request or cancel the entire request.

Reopen C&P Requests/Exams (Supervisors Only)

This option allows authorized personnel to reopen an entire C&P request or an individual exam on the request.

Transcribe C&P Data

The Transcribe C&P Data option may be used for original transcription or editing of existing transcribed data for C&P exams.

Release C&P Requests

This option allows medical center personnel to release a completed compensation and pension exam for transmission to the regional office. Medical Administration C&P MenuInquiry for C&P Requests

This option is designed to provide information on those veterans who have compensation and pension requests on file.

C&P Reports Menu

This submenu contains the options necessary to produce compensation and pension request reports as well as the options to print requests and final results.

AMIE/C&P Appointment Link Management

This option allows the user to add links between 2507 requests and C&P appointments as well as adjust existing links. Users holding the required security key may delete links.

### Add an Exam to an Existing Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From time to time it may be necessary to add an exam to an existing request. This may be due to an exam omission at the time the request was logged or a change in the exams required by the regional office or the examining physician.

An exam may be added to an existing request only if the request has not been transcribed, transferred out, cancelled, or completed. If it has already been put into one of these statuses, another request must be logged by the regional office. When adding exams, accompanying work sheets will usually be generated at the same time.

> **NOTE:** Any exams which are in an inactive status (as designated in the AMIE EXAM file \[#396.6\]) cannot be selected. This does not affect any 2507 requests that previously contained these exams. It prohibits selecting them as new exams.

Adding an exam to an existing request will cause a MailMan bulletin to be generated to members of the DVBA C EXAM ADDED mail group.

### Transfer a C&P Request to Another Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to staff and service limitations, it is not always possible for a medical center to furnish all C&P exams which may be requested by the regional office. This option allows transfer of a C&P request to another site. The transfer out process occurs in several steps.

- The request/exams to be transferred are selected, loaded into a network mail message, and sent to the site which can perform the exam(s).
- The message is processed at the receiving site by the server function of MailMan. During this processing of the message, many checks are made for items such as duplicate patient entries. If the veteran is not in the site's PATIENT file (#2), he is added, conforming to the new record addition requirements of the MAS package. In addition, a notice is sent to members of the DVBC NEW C&P VETERAN mail group that a veteran has been added to the database. The request and exam(s) are then added in a new C&P request. If the transfer fails, you will receive a mail bulletin entitled C&P REQUEST TRANSFER FAILURE providing the reason for failure.
- The request is processed in the normal fashion at the remote site. When it is completed, and the release option is utilized, it is automatically sent back to the original site.

Transfer of insufficient exams will include the reason the regional office returned the exam as insufficient, but it should be noted that the remarks the RO entered will not be available at the site the exam was transferred to. If further clarification is needed, the remote site should call the original site to obtain the RO remarks.

Only exams with a NEW or PENDING, REPORTED status may be transferred. Sites will not be allowed to transfer requests in the TRANSCRIBED, CANCELLED, or COMPLETED status nor those that have been transferred in from other sites.

If the mail message is sent out successfully, the user will see:

"Transmitted as message \# {number} from this site to {site name}.VA.GOV."

If the message fails (and therefore the transfer fails) the user will be so informed:

"Message transmission error! Request WILL NOT be sent !"

Transfer a C&P Request to Another Site

Additional Notes about Transfers

The following information may be helpful to sites who will transfer requests or exams to other sites.

- The servers have been adjusted to send a reply in all cases. This will let the sending site know that the server message reached its destination.
- You cannot transfer an exam which has already been transferred. You may, however, transfer other exams on the request which are still open at the owner site. Hence, it is possible to have several different exams at several different remote sites.
- Transfers show up on all reports and are flagged as such.
- Only complete cancellation of a transferred-in request will notify the home site. Cancellation of individual exams will not notify the home site since the record will eventually be sent back.
- You cannot totally cancel a request which has been partially or totally transferred. You cannot cancel individual exams which are transferred out.
- You cannot transcribe an exam which has been transferred out.
- You cannot add an exam to a request which was transferred in.
- You may reopen a request which was transferred in or out; however, the same advisories still prevail. Reopening of exams or entire requests should be done only for corrections and may involve coordination at the remote site.
- You may not schedule requests which have been totally transferred out; however, you may schedule those which still have exams to be done locally.
- When a 2507 request is received by a remote medical center as a transfer, that request will always be entered with a routing location equal to the primary division of the receiving facility.

### Manual Return of Transferred C&P Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the automatic return of a transferred-in request fails (via the release option), it will be necessary to transfer it out manually through the use of this option. The request and exams to be transferred out are selected, loaded into a network mail message, and returned to the home site.

Only those requests which have been transferred in and are completed will be allowed to be returned.

If the mail message is sent successfully the user will see:

"Transmitted as message \# {number} from this site to{site name}.VA.GOV"

If the message fails the user will see:

"Message transmission error! Request WILL NOT be sent!"

### Schedule C&P Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Schedule C&P Exams option uses the Make Appointment option software of the PIMS Scheduling module to accomplish its task. It should be noted that if the Make Appointment option software changes, portions of this option will also change.

When this option is utilized, information is captured for the AMIS 290 report.

If the APPT LINKING ENHANCED DIALOGUE site parameter is turned OFF, the appointment is associated to the 2507 request with a new link. If the parameter is turned ON, the AMIE software checks for the existence of C&P appointment links. If found, additional prompts and warnings are provided to ensure that the links are properly maintained.

### Cancel C&P Requests/Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally, it may be necessary for either the regional office or MAS to cancel one or more exams on a request or cancel the entire request. This option will allow such cancellations while leaving an accurate audit trail and adjusting the figures for AMIS reporting. It will also allow cancellation of incomplete requests which may have been generated by premature disconnection from the DHCP system by regional office users.

You will not be allowed to cancel a request which has completed exams on it or exams which have been transferred out.

Any cancellation action taken will result in a bulletin being sent to members of the 2507 CANCELLATION mail group. Any exams which were cancelled will be itemized in the bulletin message along with the reason they were cancelled. If the cancellation of any exam results in the request becoming completed, that will also be noted in the cancellation bulletin.

Since there may be users from several different regional offices in the 2507 CANCELLATION mail group, the bulletin will be screened to limit who receives it. The bulletin will be sent to a mail group member if any of the following is true. In all cases, the person who cancels the request/exam will receive the bulletin.

- The member's division number is the same as the veteran's claim folder location. This would assure reporting of the cancellation to anyone from a specific regional office.
- The member is designated as a supervisor for the 2507 package.
- The member is the person who entered the request initially.
- In the event the request has been transferred in, the mail group at the owner site will also receive a bulletin that the request/exams were cancelled.

### Reopen C&P Requests/Exams (Supervisors Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow supervisors to reopen an entire C&P request or individual exams on a request. Both completed and cancelled exams may be reopened. The supervisor should be aware that if requests are reopened, paperwork will not automatically be produced the next morning. The hospital will have to manually generate any paperwork required by the staff (exam work sheets, etc.).

This option should be used infrequently and only for correction of errors. Other usage could adversely affect AMIS 290 totals since the original date of the request is not changed.

A bulletin will be sent to the 2507 REOPEN mail group notifying them of the action taken.

If the following error messages appear, please contact your IRM Service for assistance.

"Reopen error !"

Although the program has attempted to reopen the desired request and the selected exams, the request status is still cancelled.

"Exam name not found in file 396.6"

The request has an exam which points to a non-existent record in File \#396.6.

### Transcribe C&P Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transcribe C&P Data option may be used for entering original transcription or editing existing transcribed data. The transcription process uses one standard FileMan word processing field for all data entry.

If the utilization of this option causes the C&P exam to be ready for release, a MailMan bulletin will be generated and sent to members of the DVBA C 2507 EXAM READY mail group.

### Release C&P Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release of a completed and approved request is the final step in the 2507 process. When released, the request and its associated exams will be ready for transmission via FAX or for direct printing at the regional office. To use this option, you must hold the DVBA C RELEASE C&P REQUESTS security key.

The FAX method will be used if there are associated documents which must be returned with the final results (e.g., eye charts). If no documents will be sent with the final results, then the results will be set up to print automatically at the regional office.

If a request has been transferred in, the following message will appear when release is attempted: "This request was transferred in - please wait while I return it." The request and its associated data will be loaded into a network mail message and transmitted to the owner site without any user intervention. If the transmission is successful, you will be notified and the number of the mail message displayed. If the transmission fails, you will be so notified. The AMIE supervisor should then review the request and attempt to send it back manually. This would be done through the Manual Return of Transferred C&P Requests option.

### Inquiry for C&P Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inquiry for C&P Requests option is designed to provide information for a veteran who has compensation and pension requests on file. It will display demographic data such as address, date of birth, phone numbers, and service dates; future compensation and pension appointments; requested exams currently on file; the requesting regional office, requester, and date request initiated; rated and other disabilities; general remarks concerning the request.

### C&P Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The C&P Reports Menu contains the options necessary to produce compensation and pension request reports as well as the options to print requests and final results. The following is a brief description of the options contained in this menu.

Manual Printing of New C&P Requests

This option is designed to allow users to manually print C&P requests if the automatic print failed or the original requests needed to be reprinted.

Print/Reprint C&P Work Sheets

This option is used to print the examination work sheets for the exams on a C&P request.

Pending C&P Exams Report

This option will print out all pending C&P requests.

Report for Exams Not Scheduled in Three Days

This option will provide a list of all C&P requests that were not scheduled within the recommended three-day period.

AMIS 290 Report for C&P

The AMIS 290 report manually produced by the medical center may now be produced electronically through this option.

Print a Fee Exam Cover Sheet

This option is used to print a courtesy cover sheet for those exams which are sent to fee physicians for completion.

Reprint C&P Final Report

This option will allow the reprinting of any final 2507 exam.

C&P Request List by Date Range

This option will print a list of 2507 requests for a selected request date date range or by physician.

Check C&P File Integrity

This option checks the 2507 REQUEST file for missing data.

Insufficient Exam Report

This option prints a report of 2507 requests entered with a priority of Insufficient Exam for a specified date range.

ClinDocs Metrics Report

This option prints a report for transmission metrics such as success and failure data for a specified date range.

Clinical Doc Metrics Data Purge

This option is used to remove stored clinical document transmission data.

#### Manual Printing of New C&P Requests

This option is designed to allow users to manually print C&P requests if the automatic printing failed or the original requests need to be reprinted. You may choose to print all requests for a date range or a single request for a selected veteran.

The output is designed to be sent to a printer and not printed to the screen. You will not be able to print accompanying work sheets through this option.

If you choose to print for a date range, a recap sheet will be generated which will give a breakdown of the three categories of requests which will be printed: new requests, modified requests, and additional exams. Each category will display the veteran's name, social security number, and claim number. The purpose of this recap sheet is to allow the C&P clerk to more efficiently work with the output by knowing how many requests there should be and their breakdown.

In order to determine the reason an original 2507 request contained insufficient results, the medical center may have to locate and review that request. To assist the medical center in finding the original 2507, information has been added to the insufficient C&P exam request printed at the medical center. If the original 2507 request has not been purged from the AMIE database, its date reported to MAS is printed on the priority insufficient 2507 request. If the original 2507 request has been purged from the AMIE database, this information is not included on the priority insufficient request. Additionally, the insufficient reason and insufficient remarks are printed with each exam on a new priority insufficient request.

Transfer of insufficient exams will include the reason the regional office returned the exam as insufficient, but it should be noted that the remarks the RO entered will not be available at the site the exam was transferred to. If further clarification is needed, the remote site should call the original site to obtain the RO remarks.

#### Print/Reprint C&P Work Sheets

The Print/Reprint C&P Work Sheets option is used to print the examination work sheets for the exams on a C&P request. The exams must have an OPEN status. You cannot print work sheets for transferred, transcribed, cancelled, or completed exams. This option was designed to be sent to a printer.

The heading of the output will include the AMIE work sheet number, type of format, and exam name.

With V. 2.7 of AMIE the Regular Aid and Attendance and SCARS AMIE exams are inactive and may not be selected. This does not affect any 2507 requests that previously contained these exams. It prohibits selection for new exams.

#### Pending C&P Exams Report

This option will print out all pending C&P requests. You may sort the reports by request status, routing location, veteran name, or age of the request. Each report will display the following information, if applicable: veteran name, social security number, claim number, request date, elapsed days, exams requested, and requester name and location. The total number of exams pending will also be provided.

#### Report for Exams Not Scheduled in Three Days

This is primarily a management report and will report all C&P requests for a selected date range which were requested by the regional office and not scheduled within the recommended three-day period. The report requires a right margin width of 132 columns and will include the following data elements. The total number of requests will also be displayed.

Veteran name

Social security number

Date C&P request reported to MAS

Date C&P exam scheduled

Requesting regional office

Number of calendar days

If the request has been scheduled, the number of calendar days shown will be those between the date the C&P request was reported to MAS and the date the exam was scheduled. If the request is not scheduled, the calendar days shown will be those between today's date and the date the C&P request was reported to MAS.

#### AMIS 290 Report for C&P

This AMIS C&P report manually produced by the medical center may now be produced electronically through this option. AMIS stands for Automated Management Information System. It is a general system of computer programs used to process management reports. The AMIS 290 report covers compensation and pension examination request activity.

The MAS AMIS 290 calculates the data based on requests from all of their regional offices while the regional office AMIS 290 calculates based only on that specific regional office's requests.

With V. 2.7 of AMIE, the average processing time reported on the AMIS 290 report now accounts for lost 2507 request processing time due to appointment reschedules at the request of the veteran.

Processing time for an insufficient request will include the processing time of the original request.

In addition to a hard copy report being produced, the option allows you to send a MailMan message either locally or via network mail. The mail bulletin will contain the same information that appears on the report.

You may run the report at any time of the month for any time period. Past time periods may be run provided the pending information from the month previous to the one being rerun is provided and the information has not been purged.

AMIS 290 Report for C&P

Supplement

The supplement provides explanations of the data contained in the output.

Total pending from previous month: This is the total number of 2507 requests reported to MAS before the last day of the previous month that were not completed prior to the end of that month, or were completed prior to the end of that month and reopened.

Requests received for date range: This is the total number of requests that were not entered with a priority of exam equal to Insufficient and had a date reported to MAS that fell within the date range entered by the user.

Exams returned as insufficient: This is the total number of requests that were entered with a priority of exam equal to Insufficient and had a date reported to MAS that fell within the date range entered by the user.

Requests returned complete: This is the total number of requests that have a date released that fell within the date range entered and have a request status of COMPLETED, PRINTED BY RO or RELEASED TO RO, NOT PRINTED.

Requests returned incomplete: This is the total number of requests that have a cancellation date that falls within the date range entered and a request status that equals CANCELLED BY RO or CANCELLED BY MAS.

Total processing time: This is the sum of the days it took to complete all requests that were released during the date range entered.

Pending end of month: This is calculated according to the following formula: (total pending from previous month) plus (requests received for date range) plus (exams returned as insufficient) minus (requests returned complete) minus (requests returned incomplete).

Average processing time: This is calculated by dividing the total processing time by the requests returned complete.

Greater than 3 days to schedule: This is total number of requests with date reported to MAS within the entered range that had more than 3 days elapsed from the date reported to MAS to the date scheduling completed.

AMIS 290 Report for C&P

Greater than 30 days to examine: This is the total number of requests with greater than 30 days elapsed from the date reported to MAS to the date of the scheduled C&P examination.

Pending, 0-90 days: This is the number of requests that had been pending 0 to 90 days from their date reported to MAS and were not completed or cancelled prior to the entered ending date.

Pending, 91-120 days: This is the number of requests that had been pending 91 to 120 days from their date reported to MAS and were not completed or cancelled prior to the entered ending date.

Pending, 121-150 days: This is the number of requests that had been pending 121 to 150 days from their date reported to MAS and were not completed or cancelled prior to the entered ending date.

Pending, 151-180 days: This is the number of requests that had been pending 151 to 190 days from their date reported to MAS and were not completed or cancelled prior to the entered ending date.

Pending, 181-365 days: This is the number of requests that had been pending 191 to 365 days from their date reported to MAS and were not completed or cancelled prior to the entered ending date.

Pending, 366 or more days: This is the number of requests that had been pending 366 or more days from their date reported to MAS and were not completed or cancelled prior to the entered ending date.

AMIS 290 Report for C&P

\*Transfers in from other sites: This is the number of requests received as transfers from other sites during the entered date range.

\*Transfers returned to other sites: This is the number of requests received as transfers that were completed and returned to their originating sites during the entered date range.

\*Transfers pending return to other sites: This is the number of requests received as transfers that have not been returned to the originating site as of the AMIS 290 run date.

\*Transfers out to other sites: This is the number of requests pending return from remote sites that had examinations transferred to remote sites during the entered date range.

\*Transfers returned from other sites: This is the number of requests that had all transferred exams returned during the entered date range.

\*Transfers pending return from other sites: This is the number of requests that have examinations pending return from their remote sites as of the AMIS 290 run date.

\*Transfer figures are for information only and should not be used to balance this report.

#### Print a Fee Exam Cover Sheet

Due to a number of different circumstances, it is not always possible for a veteran to have the C&P exam performed at a VA medical center. In those cases, the exams may be performed by a physician in the veteran's home area on a fee for service basis.

This option will print a courtesy cover sheet, which contains a brief explanation of the intent of a C&P exam. It should be attached to the paperwork that will be sent to the fee basis physician.

#### Reprint C&P Final Report

This option will allow the reprinting of any final 2507 exam. The reports will be sorted by the last two digits of the claim number. You may choose to print by date or patient name.

Reprinting a request is not allowed unless the person requesting the reprint has a division which matches the station number of the requesting regional office. However, anyone who is designated as a supervisor for the C&P package may reprint requests, regardless of whether his division matches the regional office station number.

If you choose to print by date, the output will include a summary portion. This includes patient name, social security number, claim number, and request date. The total number of requests to be printed will also be provided.

The DVBA SUPERVISOR key is required to utilize this option.

#### C&P Request List by Date Range

This option may be used to produce two distinct and separate reports.

You may choose to report by physician for fee basis reconciliation purposes. The output will include those requests that have an entry in the examining physician field. This report requires a margin width of 132 columns and displays the following fields: veteran name, social security number, regional office name, exam, exam date, and examining physician. You may print this report for a range of exam dates, regional offices, and physicians.

You may print a list of 2507 requests for a selected request-date date range. This report requires a margin width of 80 columns and displays the following data fields: veteran name, social security number, request date, requester. The request date is the date the medical center received the C&P request from the regional office.

#### Check C&P File Integrity

The Check C&P File Integrity option checks the 2507 REQUEST file (#396.3) for missing data. The seven different data fields that are checked are displayed when the option is invoked. The report lists the veteran's name, social security number, and the missing items.

The seventh item, Requests older than 3 days without C&P Appt links, checks the Date Reported to MAS and the C&P appointment links to the request. If it has been more than three days since the 2507 was reported to MAS and it does not have associated compensation and pension appointments linked to it, the 2507 will be included on the output.

The AMIE Appointment Integrity Report reviews the C&P appointments scheduled for those veterans reported as having 2507 requests without associated C&P exams. Using the AMIE/C&P Appointment Link Management option to establish links will help remove the linking problem entries from this report. If the 2507 INTEGRITY REPORT STATUS parameter is set to OFF, appointment links are not reviewed and reported, and the AMIE Appointment Integrity Report would not be generated.

#### Insufficient Exam Report

The Insufficient Exam Report option prints a report of 2507 requests entered with a priority of Insufficient Exam for a specified date range. You may choose a detailed or summary version of the report. For the detailed report, it should be noted that only exam reasons and types that have information to report will be included on the output.

The summary version of the report is divided into two parts. The first portion contains the total number of 2507 requests/exams received for the date range, the total number of priority insufficient requests/exams for the date range, and the percentage of insufficient requests/exams received. Due to rounding of the component percentages, the total of the percentages may not equal 100% . The second portion of this version is a breakdown of each reason an exam was returned.

The detailed version allows you to display one/many/all insufficient reasons and AMIE exams. Other information provided includes exam type, patient name, SSN, and claim number. Provider and exam date on this report are the provider and date from the originally completed 2507. The exam date will not be included if the original 2507 has been purged. The length of the veteran's name and the provider will be limited to 15 characters. If either field has been truncated, it will appear with two asterisks (\*\*). Again, no matter what reasons and exams are selected, only exam reasons and types that have information to report will be included on the output.

#### ClinDocs Metrics Report

The ClinDocs Metrics Report option prints a report for eFolder transmission requests entered for a specified date range. The report contains transmission metrics that includes transmission date, sender, patient, path, status, and report details.

#### Clinical Doc Metrics Data Purge

The Clinical Doc Metrics Data Purge option is used to remove stored eFolder transmission data.

The DVBA CAPRI METRICS PURGE key is required to utilize this option.

### Print Blank C&P Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to print blank C&P worksheets which are currently active. The only prompts are for worksheet and device. Below is an abbreviated example of a worksheet.

Compensation and Pension Examination

For ACROMEGALY

\# 0420 Worksheet

Name: SSN:

C-number:

Date of exam: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Place of exam: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

A. Review of Medical Records:
B. Medical History (Subjective Complaints):

Comment on:

1\. Date diagnosis established.

2\. Joint pains.

3\. Changes in vision.

C. Physical Examination (Objective Findings):

Address each of the following and fully describe current findings:

1\. Arthropathy.

2\. Vascular fragility.

3\. Evidence of increased intracranial pressure.

D. Diagnostic and Clinical Tests:

Provide:

1\. CT of brain or X-ray of sella turcica.

2\. Glucose tolerance test.

3\. Include results of all diagnostic and clinical tests conducted

in the examination report.

E. Diagnosis:

Comment on:

1\. Is the disease active or in remission?

Signature: Date:

### AMIE/C&P Appointment Link Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally, a 2507 request may not get linked to a C&P appointment. It is also possible that links established between 2507 requests and C&P appointments may be incorrect. This option allows the user to add links as well as adjust existing links. Users holding the DVBA C SUPERVISOR security key may also delete links.

Please note that links should be maintained through Scheduling software options. This option would usually only be used to make adjustments on those appointments that for some reason were not maintained through Scheduling. C&P appointments that are not linked to 2507 requests are displayed on the AMIE Appointment Integrity Report generated through the Check C&P File Integrity option.

Requests may be linked to one or more appointments, and a request may be linked to an appointment that has any number of other 2507 requests linked to it.

All 2507 requests for this veteran that have been reported but not purged will be displayed for selection. All exams associated with the selected request will then be displayed.

All C&P appointments after "2507 request date reported to MAS" (date 2507 request was printed at the medical facility) will be displayed. "\*CL" on the display indicates the current appointment for one of the links. AUTO on the display indicates the appointment was auto rebooked. The first choice of every display at this prompt will be "Display Current C&P Appointment Links". When selected, all current appointment links are displayed.

## Divisional Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to transfer the request for reports received from the regional office on 7131s from one medical center division to another. Only reports with a status of "pending" may be transferred.

All of the reports requested on a 7131 are initially requested from the division the regional office entered as the routing location for that 7131. Through this option, the division for a particular report can be changed to the division which has the required information. The day following the transfer, 7131s that had requested reports transferred to another division are printed at the new division. It then becomes the responsibility of that division to complete that portion of the 7131.

Requests prior to installation of AMIE V. 2.7 may not show an entry in the "Division" column for each requested item. In those cases, the division is the same as the routing location for that 7131. Requests subsequent to installation of AMIE V. 2.7 will display an entry in the "Division" column for each requested item.

You will be prompted for patient name. If more than one 7131 request exists for the veteran, they will be displayed by admission/activity date for selection. The request is then displayed showing the requested reports. You will be prompted for the report(s) you wish to transfer and to what division. You may only transfer to divisions that have been set up through the Regional File Site Parameter Setup option.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

21-Day Certificate The 7132 issued to the regional office after a veteran has been hospitalized for a period of 21 days or more.
AMIE Automated Medical Information Exchange
AMIE Work Sheet A form used to aid the physician in the completion of a C&P exam. It provides instruction as to what medical information is required for a particular C&P examination.
Body System The systemic area of the human body to which a particular examination belongs. This is in accordance with the definition in the C&P Rating Specialist Guide at each regional office.
Bulletin An electronic mail message generated whenever certain conditions are met while executing application programs.
C&P Compensation and Pension
C&P Routing Location An entry in the AMIE Site Parameter file (#396.1) which points to the Hospital Location file (#44). Any locations entered are used to screen lab and radiology results for veterans when final C&P information is printed.
Discharge Summary A report issued upon a veteran's release from hospitalization.
Division A field which is in each user's record and which denotes to what station the user belongs. It is translated for program usage into the three digit station number of the hospital or the regional office.
FAX Facsimile transmission. A document may be sent via the telephone lines to another site over a facsimile machine. Requires one transmitter and one receiver.
Request An electronic log of information needed by the regional office.
Routing Location The medical center division (reference File \#40.8) to which a request belongs and at which initial paperwork should be printed.
Transfer The movement of an entire C&P request or one or more exams of a request to another site for processing and subsequent return.
VBA Veterans Benefits Administration
VHA Veterans Health Administration

# Option Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

21-day Cert/Notice of Discharge Report

7131 Divisional Transfer

Add an Exam to an Existing Request

Admission Review Report

AMIE/C&P Appointment Link Management

AMIS 290 Report for C&P

Automatic 7131 Finalization (User Mode)

Beneficiary Information Status Inquiry

C&P Request List by Date Range

Cancel C&P Requests/Exams

Check C&P File Integrity

ClinDocs Metrics Report

Clinical Doc Metrics Data Purge

Edit 7131 Remarks

Edit Beneficiary Information Status

Edit Competency Status

Finalized Report

Incomplete Request Report

Inquiry for C&P Requests

Insufficient Exam Report

Manual 21-day Certificate Processing

Manual Discharge Notification Processing

Manual Printing of New C&P Requests

Manual Return of Transferred C&P Requests

MAS Edit/Release of 21-day Certificates

New Form 7131 Request Report

Pending C&P Exams Report

Pending Form 7131 Requests Report

Print a Fee Exam Cover Sheet

Print Blank C&P Worksheet

Print/Reprint C&P Work Sheets

Regional File Site Parameter Setup

Release C&P Requests

Reopen C&P Requests/Exams (Supervisors Only)

Report for Exams Not Scheduled in Three Days

Reprint 21-day Certificates for MAS

Reprint C&P Final Report

Schedule C&P Exams

Transcribe C&P Data

Transfer a C&P Request to Another Site

# Appendix A – AMIE Work Sheet Listing by Body System, Exam Name, and Work Sheet Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exam Name Worksheet \# Related Body System

ACROMEGALY 0420 ENDOCRINE

AID AND ATTENDANCE OR HOUSEBOUND 1720 SPECIAL EXAMINATIONS

AMPUTATION, RESIDUALS OF 1405 MUSCULOSKELETAL

ARRHYTHMIAS 0115 CARDIOVASCULAR

ARTERIES AND VEINS 0105 CARDIOVASCULAR

AUDIO 1305 ORGANS OF SENSE

BONES (FRACTURES AND BONE DISEASE) 1410 MUSCULOSKELETAL

BRAIN AND SPINAL CORD 1210 NEUROLOGIC

CHRONIC FATIGUE SYNDROME 1810 INFECTIOUS/IMMUNE/NUTRITIONAL

COLD INJURY PROTOCOL EXAMINATION 1730 SPECIAL EXAMINATIONS

CRANIAL NERVES 1205 NEUROLOGIC

CUSHING'S SYNDROME 0415 ENDOCRINE

DENTAL AND ORAL 0205 DENTAL AND ORAL

DIABETES MELLITUS 0410 ENDOCRINE

DIGESTIVE CONDITIONS, MISCELLANEOUS 0330 DIGESTIVE

EAR DISEASE 1310 ORGANS OF SENSE

EATING DISORDERS (MENTAL DISORDERS) 0915 MENTAL

ENDOCRINE DISEASES, MISCELLANEOUS 0425 ENDOCRINE

EPILEPSY AND NARCOLEPSY 1220 NEUROLOGIC

ESOPHAGUS AND HIATAL HERNIA 0310 DIGESTIVE

EYE EXAMINATION 1330 ORGANS OF SENSE

FEET 1415 MUSCULOSKELETAL

FIBROMYALGIA 1445 MUSCULOSKELETAL

GENERAL MEDICAL EXAMINATION 0505 GENERAL MEDICAL

GULF WAR GUIDELINES 1740 SPECIAL EXAMINATIONS

GENITOURINARY EXAMINATION 0605 GENITOURINARY

GYNECOLOGICAL CONDITIONS AND 0705 GYNECOLOGICAL AND BREAST

DISORDERS OF THE BREAST

HAND, THUMB, AND FINGERS 1420 MUSCULOSKELETAL

HEART AND HYPERTENSION 0110 CARDIOVASCULAR

HEMIC DISORDERS 0805 HEMIC AND LYMPHATIC

HIV-RELATED ILLNESS 1815 INFECTIOUS/IMMUNE/NUTRITIONAL

INFECTIOUS, IMMUNE, AND NUTRITIONAL 1805 INFECTIOUS/IMMUNE/NUTRITIONAL

DISABILITIES

INTESTINES (LARGE AND SMALL) 0315 DIGESTIVE

JOINTS (SHOULDER/ELBOW/WRIST/HIP 1430 MUSCULOSKELETAL KNEE/ANKLE)

LIVER, GALL BLADDER, AND PANCREAS 0305 DIGESTIVE

LYMPHATIC DISORDERS 0810 HEMIC AND LYMPHATIC

MENTAL DISORDERS (NOT INITIAL PTSD 0905 MENTAL DISORDERS

AND EATING DISORDERS)

MOUTH, LIPS, AND TONGUE 0335 DIGESTIVE

MUSCLES 1435 MUSCULOSKELETAL

NEUROLOGICAL DISORDERS 1225 NEUROLOGIC MISCELLANEOUS

NOSE, SINUS, LARYNX, AND PHARYNX 1510 RESPIRATORY

PERIPHERAL NERVES 1215 NEUROLOGIC

POST-TRAUMATIC STRESS DISORDER 0910 MENTAL (PTSD)

PRISONER OF WAR PROTOCOL EXAMINATION 1705 SPECIAL EXAMINATIONS

PULMONARY TUBERCULOSIS AND 1515 RESPIRATORY, RESTRICTIVE AND

MYCOBACTERIAL DISEASES INTERSTITIAL

RESPIRATORY DISEASES, MISCELLANEOUS 1520 RESPIRATORY

| Exam Name | Worksheet \# | Related Body System |     |
|---------------|------------------|-------------------------|-----|

SCARS 1605 SKIN

SENSE OF SMELL AND TASTE 1320 ORGANS OF SENSE

SKIN DISEASES (OTHER THAN SCARS) 1610 SKIN

SPINE (CERVICAL, THORACIC, & LUMBAR) 1440 MUSCULOSKELETAL

STOMACH, DUODENUM AND PERITONEAL 0325 DIGESTIVE ADHESIONS

THYROID AND PARATHYROID DISEASES 0405 ENDOCRINE