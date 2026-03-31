---
title: AMIE Version 2.7 Regional Office User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Regional Office
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
description: Automated Medical Information Exchange (AMIE) V. 2.7Regional Office User ManualApril 1995
audience: 
keywords: 
  - request
  - report
  - office
  - date
  - regional
  - exam
  - table
  - contents
  - patient
  - discharge
page_count: 0
word_count: 9647
section_count: 26
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 1/23/09
revision_oldest: 1/23/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Medical_Info_Exchg_(AMIE)/rous.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Medical_Info_Exchg_(AMIE)/rous.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=31"
---

![](amie-version-2-7-regional-office-user-manual/001.png)

Automated Medical Information Exchange (AMIE) V. 2.7Regional Office User ManualApril 1995

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 1/23/09

| Date | Description (Patch \# if applic.) | Project Manager | Technical Writer |
|----------|---------------------------------------|---------------------|----------------------|
| 1/23/09  | Reformatted Manual                    |                     | REDACTED             |

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [7131/7132](#71317132)
  - [Compensation and Pension](#compensation-and-pension)
  - [Related Manuals](#related-manuals)
  - [Enhancements and Functionality Changes](#enhancements-and-functionality-changes)
- [# Orientation](#orientation)
  - [How to Use this Manual](#how-to-use-this-manual)
  - [## List Manager](#list-manager)
  - [On-line Help](#on-line-help)
- [Package Management/Operation](#package-managementoperation)
  - [Package Management](#package-management)
  - [Package Operation](#package-operation)
- [# AMIE Regional Office Main Menu](#amie-regional-office-main-menu)
  - [Request for 7131 Information](#request-for-7131-information)
  - [Beneficiary Information Status Inquiry](#beneficiary-information-status-inquiry)
  - [Edit 7131 Remarks](#edit-7131-remarks)
  - [Admission Inquiry By Date (All Admissions)](#admission-inquiry-by-date-all-admissions)
  - [Admission Report for Service Connected Veterans](#admission-report-for-service-connected-veterans)
  - [Discharge Report](#discharge-report)
  - [Incompetent Veterans Report](#incompetent-veterans-report)
  - [Regional Office Patient Inquiry](#regional-office-patient-inquiry)
  - [Detailed Inpatient Inquiry](#detailed-inpatient-inquiry)
  - [Report for Pension and A&A](#report-for-pension-and-aa)
  - [Re-admission Report](#re-admission-report)
  - [Patient Profile MAS](#patient-profile-mas)
  - [Pending Form 7131 Requests Report](#pending-form-7131-requests-report)
  - [MailMan Menu](#mailman-menu)
  - [## Regional Office 7132 Menu](#regional-office-7132-menu)
    - [Print New Notices of Discharge](#print-new-notices-of-discharge)
    - [Reprint a Notice of Discharge](#reprint-a-notice-of-discharge)
    - [Regional Office 21-day Certificate Printing](#regional-office-21-day-certificate-printing)
    - [Reprint a 21-day Certificate for the RO](#reprint-a-21-day-certificate-for-the-ro)
  - [Regional Office C&P Menu](#regional-office-cp-menu)
    - [Enter a C&P Exam Request](#enter-a-cp-exam-request)
    - [Add an Exam to an Existing Request](#add-an-exam-to-an-existing-request)
    - [Edit C&P Request Information](#edit-cp-request-information)
    - [Cancel C&P Requests/Exams](#cancel-cp-requestsexams)
    - [Inquiry for C&P Requests](#inquiry-for-cp-requests)
    - [Edit Patient Address Information](#edit-patient-address-information)
    - [Regional Office Reports Menu](#regional-office-reports-menu)
- [Glossary](#glossary)
- [Option Index](#option-index)
- [Appendix A – AMIE Work Sheet Listing by Body System, Exam Name, and Work Sheet Number](#appendix-a-amie-work-sheet-listing-by-body-system-exam-name-and-work-sheet-number)
The AMIE software automates the administrative procedures involved in sending medical information used in determining veteran benefit payments from the VA medical centers to the VA regional offices.
The AMIE software is composed of two separate modules: 7131/7132 and 2507 Compensation and Pension. Each of these sections provides requesting, tracking, and reporting functions for the various requests entered.

## 7131/7132

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAF 21-7131 is a request for information. The regional office can log into the appropriate VA medical center and request a number of reports for a veteran. These include, but are not limited to, competency reports, admission reports, and asset information. Items such as 21-Day Certificate and Notice of Discharge are automatically tracked and issued only when the event occurs. At this point, they become a 7132, Notice of Discharge and 21-Day Certificate.

Multi-divisional medical centers may transfer portions of the 7131 request between their divisions.

## Compensation and Pension

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A 2507 examination request is a request for specific examination(s) to be performed on a veteran to determine compensation or pension benefits. The regional office has the ability to add a patient to the medical center's database if s/he does not exist there. All aspects of the examination process from notifying MAS of the request to scheduling of the exams, transcribing the results, and forwarding the results to the RO are handled through AMIE.

Medical centers have the ability to transfer any exams they are unable to perform to other sites via MailMan messages. The AMIE software at the receiving medical center takes the mail message and enters a 2507 request into that hospital's database. Once these exams are completed, they are transferred back to the original medical center.

Both modules of AMIE generate a number of reports to provide medical center and regional office personnel with the status and timeliness of any request. The AMIS 290 report monitors the progress of 2507 exams.

The AMIE software greatly reduces the time it takes to exchange patient information between the medical centers and regional offices. It reduces the amount of paper forms, provides better monitoring of the exam process, and most importantly, allows the veteran to receive benefits due her/him in a more timely and efficient manner.

The AMIE user documentation is divided into two separate manuals; one designed for Medical Administration Service personnel at the medical centers, and the other for regional office personnel. The documentation has been presented in this manner to accommodate these two distinct groups of AMIE users. Each manual provides detailed information on how to use the options contained in the respective menus; AMIE Medical Administration Menu and AMIE Regional Office Main Menu.

Related manuals include the AMIE Regional Office User Manual, AMIE Technical Manual, AMIE Package Security Guide, AMIE Installation Guide, and the AMIE Release Notes.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMIE MAS User Manual

AMIE Technical Manual

AMIE Package Security Guide

AMIE Installation Guide

AMIE Release Notes

## Enhancements and Functionality Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Medical Center*

- Ability to print the pending 21 Day Certificate report and the pending Notice of Discharge report, print only the pending 21 Day Certificate report, or only the pending Notice of Discharge report.
- Allow the individual medical centers to select the length of time to keep completed 2507 exams.

*Regional Office*

- Reverse print order of admission dates - 7131 Requests.
- Combining options for entering 7131 for admitted veterans and 7131 for non-admitted veterans.
- Limit the type of selectable movements to Discharge Types for Discharge Report and Report for Pension and A&A.

*Both Medical Center and Regional Office*

- Reprinting 21 Day Certificates by name or SSN in addition to date.
- Print 7131s by name or SSN in addition to date.
- Select the claim folder location by station number, name, or from a list of institutions when entering a new patient to the PATIENT file.
- Average processing time reported on the AMIE AMIS 290 changed to include adjustments made to the processing time of 2507 requests as the result of veterans cancelling C&P appointments.
- Allow the linking of insufficient 2507 requests to the originally entered request.
- Transfer any portion of a 7131 between the divisions of multidivisional medical centers.

# # Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Use this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMIE MAS User Manual is provided in Adobe Acrobat PDF (portable document format) files. The Acrobat Reader is used to view the documents. If you do not have the Acrobat Reader loaded, it is available from the VISTA Home Page, “Viewers” Directory.

Once you open the file, click on the “Show/Hide Navigation Pane” icon on the Acrobat toolbar, then the “Bookmarks” tab. You may then click on the desired entry name to go to that entry in the document. You may print any or all pages of the file. Click on “Print” icon and select the desired pages. Then click “OK”.

Each menu section begins with an overview of the options contained in it, followed by the actual option documentation. The options are listed in the order in which they appear on the menu. The option documentation gives a detailed description of the option and what it is used for. It contains any special instructions related to the option.

## ## List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMIE V. 2.7 uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

## On-line Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Typing in a \<?\> at most prompts will display any on-line help available. Help messages provide lists of acceptable responses or format requirements which provide instruction on how to respond. Anytime choices appear with numbers, the system will usually accept the number or the name. As many as three question marks \<???\> may be entered to get varying degrees of help.

# Package Management/Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package does not impose any additional legal requirements on the user. All users are reminded that many of the reports generated by this package contain confidential patient information and should be treated with care. This package conforms to requirements set forth in the Code of Federal Regulations Part 38CRF3.326 for ordering C&P exams and Part 38CFR3.327 for authorizing re-examination for purposes of assessing the degree of disability.

There are no electronic signatures or other similar items for this package.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Elective Fee Basis and Health Summary Options</u>Option Name: FBCNH AMIEOption Text: Report of Admissions/Discharges for CNH

Description: Provides a listing of admissions and discharges from a community nursing

home within a user-specified date range.

Option Name: FBCNH ADMISSIONS \> 90 DAYS

Option Text: CNH Stays in Excess of 90 Days

Description: Provides a listing, for a specified date, of active community nursing home stays that exceed 90 days.

Option Name: FBCNH DISPLAY EPISODE OF CARE

Option Text: Display Episode of Care

Description: Shows all patient movements for a nursing home stay until date of discharge.

Option Name: GMTS HS ADHOC

Option Text: Ad Hoc Health Summary

Description: Generates an "Ad Hoc" Health Summary for specified patients. The user defines his own Ad Hoc Health Summary structure for temporary use instead of selecting a pre-defined Health Summary type.

Option Name: GMTS HS BY PATIENT

Option Text: Patient Health Summary

Description: Generates a Health Summary of a specified pre-defined Health Summary Type for a specified patient.

Option Name: GMRD MAIN MENU REMOTE USER

Option Text: Discharge Summary Remote User

Description: Allows a remote user (e.g., VBA RO claims auditors) with the GMRD REMOTE USER security key to access completed (signed by the attending physician) discharge summaries on a read only, need-to-know basis. It will display incomplete (unsigned) summaries if the user does not hold the security key.

# # AMIE Regional Office Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a brief description of the options contained in the AMIE Regional Office Main Menu.Request for 7131 Information

This option is used to enter a 7131 request for information.

Beneficiary Information Status Inquiry

This option provides the current status of any request for information.

Edit 7131 Remarks

This option is used to add/edit the ADDITIONAL REMARKS field of the 7131 request.

Admission Inquiry by Date (All Admissions)

This option will report all admissions to the station you are dialing into for a selected date range.

Admission Report for Service Connected Veterans

This option will report service-connected admissions to the station you are dialing into for a selected date range.

Discharge Report

The Discharge Report option will report service-connected, A&A, pension, or all discharges for the station you are dialing into for a selected date range.

Incompetent Veterans Report

This option will report all veterans who are on file as having been rated incompetent by Civil or VA authorities.

Regional Office Patient Inquiry

The Regional Office Patient Inquiry option is used to view demographic information for a selected patient.

Detailed Inpatient Inquiry

This option provides information for a selected patient admission.

Report for Pension and A&A

This option provides information on veterans receiving either VA pension or aid and attendance.

Re-admission Report

The Re-admission Report option provides information for any veteran receiving pension or aid and attendance who has been readmitted to a facility within 185 days of his last discharge date.

Patient Profile MAS

The Patient Profile MAS option provides a means by which you may view a great variety of information for a selected patient.

Pending Form 7131 Requests Report

This report will display all requests that are not finalized. It lists only the items pending for each patient request.

MailMan Menu

MailMan functions are provided. Please refer to the latest version of the MailMan documentation if you need assistance in using MailMan functions.

Regional Office 7132 Menu

This submenu contains those options that pertain to 21-Day Certificates and Notices of Discharge.

Regional Office C&P Menu

This submenu contains the options relating to compensation and pension examinations.

## Request for 7131 Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to request 7131 information on veterans. It allows the regional office user to electronically request any type of 7131 information that may be requested manually. When a request is entered for a patient, the system records who the user is and where he is located. This will appear on any report that is generated from this request.

It is possible to have multiple 7131s open for a patient, each with a different admission or activity date/time. If a request for the selected date/time is not on file, the user may add it. If it is already on file, he may change it; or if it is finalized, he may reopen it. Editing will change the original request date, and any additionally requested items will be added to the existing record. It will again be regarded as a new request and MAS will be notified.

Once a request has been completed and finalized by the medical center, it generally will be deleted from the records in about 30-60 days. However, if additional information is needed for that admission date, the user may reopen the request on file.

The following is an explanation of some of the messages you may see while utilizing this option.

> "There is a 7131 already on file for {date}.

> Do you want to delete the existing 7131 for this date?"

The system has found a finalized 7131 for the date you have selected. Only one request per admission/activity date may be entered. You may delete this request and enter another one for the same date.

> "You have no division code. Please contact the site manager."

You have not correctly selected any of the divisions assigned to you. Please contact IRM Service at the medical center you are dialing into to correct this.

If the patient has not been admitted, a list of stop codes, disposition dates, and outpatient clinic appointments are displayed in reverse chronological order for selection. If the patient only has admission data on file, a list of admission dates are displayed in reverse chronological order for selection. If the patient has both, the following prompt will appear.

If the user up-arrows out of the selection process, the system will search the 7131 file for any existing requests. This search will display all existing requests and the user may select one for editing if the request is not finalized.

You may request any of the ten items listed on the Information Request form by selecting the corresponding number. The Request Form will then be redisplayed with a YES in the "selected" column and PENDING in the "status" column for the requested items. If you change your mind, simply select the particular report again and the "selected" column will return to NO. You may not select items 1, 2, 3, or 9 for veterans with no admissions on file.

Request for 7131 Information

Items which may be requested are as follows.

1\. Notice of Discharge (The system will not allow a Notice of Discharge to

be requested for a veteran that has been discharged

for the selected admission date.)

2\. Hospital Summary

3\. Certificate (21-day)

4\. Other/Exam (Review Remarks)

5\. Special Report

6\. Competency Report

7\. VA Form 21-2680

8\. Asset Information

9\. Admission Report

10\. Beginning Date Care

If a 21-Day Certificate is requested and the length of stay turns out to be less than the required 21 full days, the system will automatically complete the request as being "Not applicable". It should also be noted that upon generation of a certificate, the system will automatically modify the existing 7131 to show requests for a Notice of Discharge and Hospital Summary. This will be done ONLY if they are not already requested, or requested and previously completed.

If \#4 Other/Exam (Review Remarks) was selected from the Information Request Report, you must enter remarks in the ADDITIONAL REMARKS field.

If you attempt to up-arrow out before reaching the end of the option, the request will be deleted.

## Beneficiary Information Status Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will give the current status of any request for information. It provides the user with what information was requested, when it was requested, and who took the action. This option may be used to view either admission date or activity date requests.

Requests prior to installation of AMIE V. 2.7 may not show an entry in the "Current Division" column for each requested item. In those cases, the division is the same as the receiving division. Requests subsequent to installation of AMIE V. 2.7 will display an entry in the "Current Division" column for each requested item.

Users may see two "operator" names on the output for the Notice of Discharge and the 21-Day Certificate data items. For the Notice of Discharge, the operator will be "Notice of Discharge" only after the regional office actually prints the notice. For the 21-Day Certificate, the operator will be "21-Day Certificate" if the certificate was generated or "Not applicable" if the certificate was not generated.

You will be prompted for a patient name and a device. The recommended device is HOME as this report was designed to print on the screen. If more than one applicable admission or activity date exists for the selected patient, you will be prompted to choose the date you wish to see.

> **NOTE:** The appearance of a \* appended to the REQUESTED BY field denotes that the request was modified with the addition of either a Notice of Discharge, hospital summary, or both by the 21-Day Cert generation program. The \* is added when the request is made new to MAS.

## Edit 7131 Remarks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to add/edit the ADDITIONAL REMARKS field of the 7131 request. It may be used for either activity or admission date requests. If more than one applicable request exists for the selected patient, you will be prompted to choose the request you wish to see. Utilizing this option will not change the last edit date of the request.

This is a standard word processing field and as many lines of text as necessary can be entered. You may enter \<??\> at the EDIT Option prompt for a list of editing capabilities.

## Admission Inquiry By Date (All Admissions)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will report all admissions to the station you are dialing into for any given date range. The report is primarily designed to be an auditing tool for the regional office.

Each time the report is processed <u>and</u> contains data, the date is captured and stored. It will then be displayed as the "last run date" for the next processing session.

Information which may be provided for each patient found includes claim number, claim folder location, social security number, admission date, admitting diagnosis, discharge date, bed service, whether the patient is receiving A&A or pension, and eligibility data. Depending on the date range selected, this report could be quite lengthy.

## Admission Report for Service Connected Veterans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will report all service-connected admissions to the station you are dialing into for any given date range.

Each time the report is processed <u>and</u> contains data, the date is captured and stored. It will then be displayed as the "last run date" for the next processing session.

Information which may be provided for each patient found includes claim number, claim folder location, social security number, admission date, admitting diagnosis, discharge date, bed service, whether the patient is receiving A&A or pension, and eligibility data. Depending on the date range selected, this report could be quite lengthy.

## Discharge Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will report all service connected, A&A, pension, or all discharges for the station you are dialing into for any given date range. The selectable patient movement types are limited to any active discharge types at the medical facility.

Each time the report is processed <u>and</u> contains data, the date is captured and stored. It will then be displayed as the "last run date" for the next processing session.

Information which may be provided for each patient found includes claim number, claim folder location, social security number, discharge date, type of discharge, length of stay, bed service, in receipt of A&A or pension, and eligibility data. Depending on the date range and number of discharge types selected, the report could be quite lengthy.

## Incompetent Veterans Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will report all veterans who have been ruled incompetent by Civil or VA authorities. For this report to run correctly, either the Date Ruled Incompetent (VA) or Date Ruled Incompetent (CIVIL) fields must have been edited by MAS personnel (OR) the Rated Incompetent field (#.293) in the patient file (#2) must contain a YES value.

Each time the report is processed <u>and</u> contains data, the date is captured and stored. It will then be displayed as the "last run date" for the next processing session.

Information which may be provided for each patient found includes claim number, claim folder location, social security number, discharge date, type of discharge, length of stay, bed service, eligibility data, and date ruled incompetent. Depending on the date range selected, the report could be quite lengthy.

## Regional Office Patient Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Inquiry option is used to view demographic information for a selected patient. Through ADT parameters, your site may have elected to display either an abbreviated or full patient inquiry. Depending upon this selection and the individual patient, the information displayed will vary. Below is a list of the possible data items which may appear. Those items preceded by an asterisk (\*) will be omitted when a site has elected to display an abbreviated inquiry.

This option is for viewing only. Editing is not allowed.

Patient Name

Social Security Number

Date of Birth

Address

County of Residence

Home and Office Phone

\*Period of Service

\*Religion

Primary Eligibility (and Verification Status)

Other Eligibilities

Means Test Status

Date of Last Means Test

Temporary Address

> From/To Dates of Temporary Address

> Temporary Phone

\*Claim Number

\*Sex

Inpatient Status

> Admission/Discharge Dates

> Ward

> Type of Discharge

> Length of Stay

> Number of Pass Days

> Number of Absence Days

> Future Appointments

> Remarks

## Detailed Inpatient Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will provide information concerning a specific admission for a selected patient. Some of the data items which may be displayed through this inquiry are admission date, treating specialty, ward location, admitting diagnosis, PTF entry, admitting regulation, discharge date, and type of discharge; if a patient movement occurred during this stay: transfer date, type of movement, location to, return date, or corresponding admission; if a treating specialty change occurred: date of specialty change, specialty, losing bedsection, admitting/transfer diagnosis,, provider, and movement number.

## Report for Pension and A&A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Report for Pension and A&A option provides information on veterans receiving either pension or aid and attendance. The selectable patient movement types are limited to any active discharge types at the medical facility.

Each time the report is processed <u>and</u> contains data, the date is captured and stored. It will then be displayed as the "last run date" for the next processing session.

Some of the data elements displayed may include claim number, claim folder location, social security number, admission date, admitting diagnosis, discharge date, type of discharge, bed service, in receipt of A&A or pension, and eligibility data. Depending on the date range and discharge types selected, this report could be quite lengthy.

## Re-admission Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will look at any veteran receiving a pension or aid and attendance who has been readmitted to a facility within 185 days of his last discharge date. The following criteria must be met for the patient to appear on this report.

If the patient is in receipt of pension and Hospital is selected: readmitted within 185 days of last discharge and has a length of stay \> 89 days.

If the patient is in receipt of pension and Hospital-Dom is selected: readmitted within 185 days of last discharge and has a length of stay \> 59 days.

If the patient is in receipt of aid and attendance and either Hospital or Hospital-Dom is selected: readmitted within 185 days of last discharge, has a current length of stay greater than 29 days, and last discharge was irregular.

Information provided may include veteran's claim number, claim folder location, eligibility, social security number, and whether or not in receipt of pension and aid and attendance. Admission data includes admission date, admission diagnosis, discharge date, discharge type, and bed service.

## Patient Profile MAS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Patient Profile option provides a means by which you may view a great variety of information for a selected patient. This is a MAS software option and will change as the MAS software is modified. Types of information displayed may include demographic, add/edits, appointments, enrollments, dispositions, and Means Test. You may choose to view all data in the patient's record for a particular category or only that data within a specified range. This option is for viewing only and editing is not allowed.

This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

## Pending Form 7131 Requests Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will display all requests that are not finalized. It lists only the items pending for each patient request. The elapsed days (total work days passed since the request was logged) is displayed which may be useful in keeping track of outstanding requests. You may choose to sort the report by regional office number and division. If you choose to report for a specific division, any 7131 that has that division responsible for any portion of the request will be included.

Requests may appear on this report with no items listed as pending. These are requests where the final item(s) have been completed but the request itself has not yet been finalized by the system. This should be a rare occurrence. If this does occur, wait 24 hours to see if the auto-finalization program will remedy the situation. If the auto-finalization program did not run, you may use the Request for 7131 Information options to edit the request. IRM Service of the medical center you are dialing into should be notified if it appears that the auto-finalization program is not set to run.

Since the pending report may serve many divisions or remote sites, the division which is responsible for the completion of the request is displayed at the top of each printed record.

## MailMan Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the latest version of the MailMan documentation if you need assistance in using MailMan functions.

## ## Regional Office 7132 Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Regional Office 7132 Menu contains those options pertaining to Notices of Discharge and 21-Day Certificates. The following is a brief description of the options contained in this menu.

Print New Notices of Discharge

This option is used to print the Notices of Discharge at the regional office.

Reprint a Notice of Discharge

This option allows reprinting of a Notice of Discharge for a single veteran or for all veterans for a selected processing date.

Regional Office 21-day Certificate Printing

This option is used to print the 21-Day Certificates at the regional office.

Reprint a 21-day Certificate for the RO

This option is used to reprint a 21-Day Certificate. The original processing date must be known to utilize this option.

Regional Office 7132 Menu

### Print New Notices of Discharge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print the Notices of Discharge. Information provided includes patient name, claim number, claim folder location, social security number, discharge date, type of discharge, length of stay, bed service, and eligibility data.

The AMIE system is designed to automatically provide notification of discharge in three cases.

The veteran has a pending Notice of Discharge request logged on a 7131.

The discharge is by death.

The veteran is discharged to a community nursing home.

The discharges for the site are checked nightly for "today's" date minus seven days. Processing this date range will give the hospital time to correct any errors that occur in the discharge process (e.g., wrong discharge type).

If the system determines that a Notice of Discharge is needed, one is generated with the information required by the regional office. In addition, if a 7131 has been logged with a request for Notice of Discharge, the 7131 request is updated at the notice printing time to reflect that the notice has been sent.

The system also provides automatic notification that there are new Notices of Discharge to print. At each log-on, until the documents are printed, a message is provided to anyone from the regional office who logs onto the system and whose office has new Notices of Discharge to print. Regional offices may not print any Notices of Discharge that do not belong to them.

Should the admission associated with the 7131 be deleted and notification has already been sent, a message will be displayed. The message will include the patient's name, SSN, date/time of admission, notice that the admission has been deleted, and a recommendation to contact the medical center.

Regional Office 7132 Menu

### Reprint a Notice of Discharge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From time to time it may be necessary to reprint a Notice of Discharge for a patient. This option allows you to reprint notices for one veteran or reprint notices for all veterans for a selected processing date.

Should the admission associated with the 7131 be deleted and notification has already been sent, a message will be displayed. The message will include the patient's name, SSN, date/time of admission, notice that the admission has been deleted, and a recommendation to contact the medical center.

Regional Office 7132 Menu

### Regional Office 21-day Certificate Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The regional office often needs to know when a patient has been hospitalized for 21 consecutive days since certain types of benefits warrant reductions or increases when this occurs. The system is designed to automatically examine all requests for 21-Day Certificates and electronically notify the regional office if a certificate is generated. The notification is automatic and immediate.

This option is used to print 21-Day Certificates. They must have been completed and released by MAS before they can be printed. ROC 119, which appears at the bottom of each certificate, stands for VA Form 119 - Report of Contact.

The regional office must request the 21 Day Certificate be generated by the computer. If the length of stay for the selected episode of care is 21 days or greater, a certificate will be generated regardless of the request date.

It should also be noted that upon generation of a certificate the system will automatically modify the existing 7131 on the veteran to show requests for a Notice of Discharge and Hospital Summary. This will be done ONLY if they are not already requested, or requested and previously completed.

If there are no new 21-Day Certificates to print, you will be so notified when this option is selected.

The only prompt is for device selection.

Regional Office 7132 Menu

### Reprint a 21-day Certificate for the RO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to reprint 21-Day Certificates. You must know the date the certificate was originally printed to reprint by date.

You may choose to reprint an individual certificate by patient name or social security number, or all certificates by the original processing date. The certificate produced is exactly the same as the original certificate.

ROC 119, which appears at the bottom of each certificate, stands for VA Form 119 - Report of Contact.

## Regional Office C&P Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Regional Office C&P Menu contains the options relating to C&P requests and reporting. The following is a brief description of the options contained in this menu.Enter a C&P Exam Request

This option is used by regional office personnel to enter requests for C&P examinations.

Add an Exam to an Existing Request

This option allows an examination to be added to an existing C&P request.

Edit C&P Request Information

This option is used to edit information on an existing C&P request.

Cancel C&P Requests/Exams

This option is used to cancel an exam on a C&P request or cancel the entire request.

Inquiry for C&P Requests

This option is designed to provide information on those veterans who have compensation and pension requests on file.

Edit Patient Address Information

This option is used to edit the patient's address information, if necessary.

Regional Office Reports Menu

This submenu contains the options necessary to produce C&P reports as well as the options to print the final reports and checklists.

Regional Office C&P Menu

### Enter a C&P Exam Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The entry of a 2507 request is the first step in the C&P examination process. This electronic entry will replace the paper 2507 examination request.

Once the veteran's name is entered, the veteran's current address, period of service, and eligibility information is displayed (for patients currently in the PATIENT file). This information should be verified before continuing to insure the request is being entered for the correct veteran. Editing of this demographic data, except for address information, is not permitted.

You may also enter a request for a patient not in the PATIENT file. The MAS package software is used here for entering the patient. The required information must be entered or the attempted addition will be disallowed and deleted. After the required information has been entered, the user will be asked to enter basic demographic information. The user may edit this information (since it is new); however, once the program proceeds past the editing, no further editing may be done by the regional office (except for address information). While these items are not required to be able to enter the veteran, all efforts should be made by the regional office to supply them. Failure to enter this information will result in a less-than-accurate database at the hospital where the veteran was added. MAS may also receive bulletins about patient record inconsistencies when the veteran registers for his appointment and this will require extra time and effort on the part of the medical center to research and correct.

If a new veteran is successfully added, a mail bulletin will be sent to the DVBC NEW C&P VETERAN mail group notifying the medical center of a new addition to the PATIENT file for C&P purposes.

The user will then see a list of any exams currently on file for the veteran as well as any rated disabilities. The regional office user should examine all outstanding requests for the veteran, if any. If the requester sees that the exam he wishes to enter is already logged, he may abort the entry. The user is also given the opportunity to enter any other disabilities.

The user selects the exams he wishes to have performed on the veteran. With

V. 2.7 of AMIE the Regular Aid and Attendance and SCARS AMIE exams are inactive and may not be selected. This does not affect any 2507 requests that previously contained these exams. It prohibits selection for new exams.

Numerous exams may be selected and if any are inadvertently not entered at this time, they may be added later through the Add an Exam to an Existing Request option.

The option allows the linking of insufficient 2507 requests to the originally entered request.

Regional Office C&P Menu*Enter a C&P Exam Request*

<u>For all exam priority statuses except Insufficient Exam</u>

The first five fields listed below are identifiers for the 2507 REQUEST file. Using the up-arrow to escape or allowing the system to time out while adding these identifiers will delete the request.

2507 REQUEST PRIORITY OF EXAM

Enter the priority assigned to this exam request (uppercase required). This is a required field.

2507 REQUEST OTHER DISABILITIES \[Line 1, Line 2, Line 3\]

There are three possible lines, up to 60 characters each.

2507 REQUEST LAST RATING EXAM DATE

Enter the date of the last rating exam, if known.

2507 REQUEST CLAIM FOLDER REQUIRED

If a review of the claim folder will be required during the exam process enter YES; otherwise enter NO. This is a required field.

2507 REQUEST ROUTING LOCATION

Enter the medical center division name or number of the routing location (medical center) where this request is being sent. This is a required field. The entry of the routing location is one of the most important parts of the request process as it establishes which medical facility is responsible for the request.

Select Exam

The name of the exam, the body system with which the exam is associated, or the associated AMIE work sheet number for the exam you wish to have performed on the veteran. (Refer to Appendix A for a list of AMIE work sheets by body system, exam name, and work sheet number.) NOTE: Any exams which are in an inactive status (as designated in the AMIE EXAM file) cannot be selected.

<u>For exam priority status Insufficient Exam</u>

The first five fields listed below are identifiers for the 2507 REQUEST file. Using the up-arrow to escape or allowing the system to time out while adding these identifiers will delete the request.

2507 REQUEST PRIORITY OF EXAM

Enter E for insufficient exam. This is a required field.

2507 REQUEST OTHER DISABILITIES \[Line 1, Line 2, Line 3\]

There are three possible lines, up to 60 characters each.

2507 REQUEST LAST RATING EXAM DATE

Enter the date of the last rating exam, if known.

2507 REQUEST CLAIM FOLDER REQUIRED

If a review of the claim folder will be required during the exam process enter YES; otherwise enter NO. This is a required field.

Regional Office C&P Menu*Enter a C&P Exam Request*2507 REQUEST ROUTING LOCATION

Enter the medical center division name or number of the routing location (medical center) where this request is being sent. This is a required field. The entry of the routing location is one of the most important parts of the request process as it establishes which medical facility is responsible for the request.

Select a 2507 request

Choose 1-{#}

This prompt will appear if there are any finalized 2507 requests on file that have not been purged. All finalized 2507 requests are displayed in reverse chronological order for selection. Select the appropriate request for association with the insufficient request (this creates the link). If the desired request is not displayed for selection, enter \<RET\> to proceed to the processing time prompt.

ORIGINAL 2507 PROCESSING TIME

If the original 2507 request has been purged from the system (and, therefore, cannot be selected for association to the insufficient request), you are required to enter the number of processing days of the original 2507. If the original request's final report does not contain the total processing days, enter zero (0).

Select Exam

On linked requests, you may only enter exams that were on the original 2507 request. You will receive an informational message for unlinked requests advising you to use care in selecting the proper exam(s). Enter the name of the exam, the body system with which the exam is associated, or the associated AMIE work sheet number for the exam you wish to have performed on the veteran. (Refer to Appendix A for a list of AMIE work sheets by body system, exam name, and work sheet number.) NOTE: Any exams which are in an inactive status (as designated in the AMIE EXAM file) cannot be selected.

ORIGINAL PROVIDER

This prompt will only appear if the insufficient request is not linked to a completed request. Enter the original provider who performed the exam (if the exam was performed on the original 2507 request). Include the facility name if the exam was performed at another site (e.g., JONES,EMPLOYEE @ VASITE).

Regional Office C&P Menu

### Add an Exam to an Existing Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From time to time it may be necessary to add an exam to an existing request. This may be due to an exam omission at the time the request was entered or a change in the exams required by the regional office.

An exam may be added to an existing request only if the request has not been transcribed, transferred out, cancelled, or completed. If it has already been put into one of these statuses, another request must be logged by the regional office.

When an exam is added to an existing request, a mail bulletin is sent to members of the DVBA C EXAM ADDED mail group informing them of the addition.

You are unable to add a C&P exam to a 2507 request with a priority of INSUFFICIENT EXAM.

Regional Office C&P Menu

### Edit C&P Request Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to edit certain information on the compensation and pension request. Only those requests with a status of NEW or PENDING, REPORTED may be edited. The Edit C&P Request Information option allows the linking of insufficient 2507 requests to the originally entered request.

The following fields may be edited. For requests with a priority of INSUFFICIENT EXAM, the second list of fields may also be entered/edited.

PRIORITY OF EXAMOTHER DISABILITIESROUTING LOCATIONCLAIM FOLDER REQUIRED?

> This is a required response.

LAST RATING EXAM DATEREMARKS

> Whenever this field on a C&P request is changed, the hard copy request will be regenerated at the medical center the next morning.

INSUFFICIENT REASONINSUFFICIENT REMARKSORIGINAL PROVIDER

> This prompt will only appear if the insufficient request is not linked to a completed request. Enter the original provider who performed the exam (if the exam was performed on the original 2507 request). Include the facility name if the exam was performed at another site (e.g., JONES,EMPLOYEE @ VASITE).

ORIGINAL 2507 PROCESSING TIME

> If the original 2507 request has been purged from the system (and, therefore, cannot be selected for association to the insufficient request), you are required to enter the number of processing days of the original 2507. If the original request's final report does not contain the total processing days, enter zero (0).

Select a 2507 requestChoose 1-{#}:

> This prompt will appear if there are any finalized 2507 requests on file that have not been purged. All finalized 2507 requests are displayed in reverse chronological order for selection. Select the appropriate request for association with the insufficient request (this creates the link). If the desired request is not displayed for selection, enter \<RET\> to proceed to the processing time prompt.

Regional Office C&P Menu

### Cancel C&P Requests/Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally it may be necessary for either the regional office or MAS to cancel one or more exams on a request or cancel the entire request. This option will allow such cancellations while leaving an accurate audit trail and adjusting the figures for AMIS reporting. It will also allow cancellation of incomplete requests which may have been generated by premature disconnection from the DHCP system by regional office users.

You will not be allowed to cancel a request which has completed exams on it or exams which have been transferred out.

If you choose to cancel the entire exam, the system will respond with the following prompts.

Reason for CancellationCancelled by MAS or ROCancellation Comments

> The comments in the CANCELLATION COMMENTS field will not be stored as part of the C&P request record. They are part of the bulletin which is sent as the final step of the cancellation process. Once the bulletin is sent, the comments will only be found on the bulletin itself.

If you choose to cancel an individual exam, the system will respond with the following prompts. If the request is incomplete, no exams will be displayed and you will have to use the option to cancel the entire request.

Exam to Cancel

> The name of the exam, the body system with which the exam is associated, or the associated AMIE work sheet number for the exam you wish to have performed on the veteran. (Refer to Appendix A for a list of AMIE work sheets by body system, exam name, and work sheet number.) Note: You can only select those exams which exist on a request in an OPEN status.

Cancellation codeCancellation ReasonCancellation comments

> These comments will not be stored as part of the C&P request record. They are part of the bulletin which is sent as the final step of the cancellation process. Once the bulletin is sent, the comments will only be found on the bulletin itself.

If cancelling any exam will result in the complete cancellation of the request, you will see "Since all exams have been cancelled the entire request will be CANCELLED". You must then answer the “Cancellation code for this request” prompt to complete information on the request. (NOTE: The up-arrow functionality has been changed. An up-arrow \<^\> will not be an acceptable response to any of the prompts following this message.)

Any cancellation action taken will result in a bulletin being sent to members of the 2507 CANCELLATION mail group. Any exams which were cancelled will be itemized in the bulletin message along with the reason they were cancelled. If the cancellation of any exam results in the request becoming completed, that will also be noted in the cancellation bulletin.

Regional Office C&P Menu*Cancel C&P Requests/Exams*

Since there may be users from several different regional offices in the 2507 CANCELLATION mail group, the bulletin will be screened to limit who receives it. The bulletin will be sent to a mail group member if any of the following is true. In all cases, the person who cancels the request/exam will receive the bulletin.

- The member's division number is the same as the veteran's claim folder location. This would assure reporting of the cancellation to anyone from a specific RO.
- The member is designated as a supervisor for the 2507 package.
- The member is the person who entered the request initially.
- In the event the request has been transferred in, the mail group at the owner site will also receive a bulletin that the request/exams were cancelled.

Regional Office C&P Menu

### Inquiry for C&P Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inquiry for C&P Requests option is designed to provide information for a veteran who has compensation and pension requests on file. It will display demographic data such as address, date of birth, phone numbers, and service dates; future compensation and pension appointments; requested exams currently on file; the requesting regional office, requester, and date request initiated; rated and other disabilities; and general remarks concerning the request.

You will be prompted for the veteran's name and a device. If more than one request exists, they will be displayed for selection.

Regional Office C&P Menu

### Edit Patient Address Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Patient Address Information option may be used to change the patient's address information. The fields which may be edited include, street address, city, state, zip code, county, and home and office phone numbers. Once editing is complete, the display will reappear containing the newly entered information.

If a temporary address exists for the veteran and is "active", it will be displayed. This is for informational purposes only. You cannot edit the temporary address.

Editing the address information will cause a mail bulletin to be sent to members of the DVBA C NEW C&P VETERAN mail group informing them of the change.

### Regional Office Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Regional Office Report Menu contains the options necessary to produce compensation and pension request reports as well as the options to print examination final reports and checklists. The following is a brief description of the options contained in this menu.

Print C&P Final Report (Manual)

This option allows printing of 2507 examination results sorted by the last two digits of the claim number.

Reprint C&P Final Report

This option is used to reprint final 2507 exams.

Pending C&P Exams Report

This option will print out all pending C&P requests.

AMIS 290 for the Regional Office

The AMIS report manually produced by the regional office may now be produced electronically through this option.

Print Exam Check List for RO

This option is used to print a checklist which regional office personnel may use in the selection of compensation and pension examinations for veterans.

Insufficient Exam Report

This option prints a report of 2507 requests entered with a priority of Insufficient Exam for a specified date range.

Regional Office C&P Menu*Regional Office Reports Menu*

#### Print C&P Final Report (Manual)

The Print C&P Final Report (Manual) option allows printing of 2507 examination results sorted by the last two digits of the claim number. It will print only those requests that have been released to the regional office and not printed. This option will only be used by the regional office and should be executed only if there is no supporting paperwork to go with the final results (e.g., eye charts).

The package is designed to automatically print any lab/radiology results designated for C&P. When printing, the system will examine all lab/radiology results for 120 days previous to the release date.

When a report is ready to be printed, it indicates that all exams for a particular request have been performed on the veteran (or cancelled) and the results completed, transcribed, approved, and released.

The output from this option will include the C&P final exam reports as well as a summary section. The summary section will list the patient name, social security number, claim number, and request date on each exam report that will be printed. The total number of requests to be printed is also provided.

Final C&P results may be received at the regional office in the following three ways.

> *Direct printing*

> Done at the regional office through the use of this option.

> *FAX delivery*

> If there is supporting paperwork for the final results, the request will be flagged as such when it is released. Once flagged, you will not be able to print it using this option. Only one original copy will be printed at the hospital, and it will be faxed along with supporting paperwork. This copy will be stored in the veteran's folder (after being signed). Fax delivery of all paperwork insures the entire exam will be kept together.

> *U. S. Mail*

> In cases where there is supporting documentation that would not FAX well, it will be necessary to mail the entire package to the regional office. An example would be an eye exam which included several different charts.

Regional Office C&P Menu*Regional Office Reports Menu*

#### Reprint C&P Final Report

This option will allow the reprinting of final 2507 exams with the status of "Completed, printed by RO". The reports will be sorted by the last two digits of the claim number. You may choose to print by date or patient name.

Reprinting a request is not allowed unless the person requesting the reprint has a division which matches the station number of the requesting regional office. The exam must have the status "Completed, printed by RO" or "Released to RO, not printed".

The package is designed to automatically print any lab/radiology results designated for C&P. When printing, the system will examine all lab/radiology results for 120 days previous to the release date.

If you choose to print by date, the output will include a summary portion. This includes patient name, social security number, claim number, and request date. The total number of requests to be printed will also be provided.

Regional Office C&P Menu*Regional Office Reports Menu*

#### Pending C&P Exams Report

This option will print out all pending C&P requests. You may sort the reports by request status, routing location, veteran name, or age of the request. Each report will display the following information, if applicable: veteran name, social security number, claim number, request date, elapsed days, exams requested, and requester name and location. The total number of exams pending will also be provided.

Regional Office C&P Menu*Regional Office Reports Menu*

#### AMIS 290 for the Regional Office

The AMIS C&P report manually produced by the regional office may now be produced electronically through this option. AMIS stands for Automated Management Information System. It is a general system of computer programs used to process management reports. The AMIS 290 report covers compensation and pension examination request activity.

The regional office AMIS 290 calculates the data based only on that specific regional office's requests while the MAS AMIS 290 calculates based on requests from all of their regional offices.

With V. 2.7 of AMIE, the average processing time reported on the AMIS 290 report now accounts for lost 2507 request processing time due to appointment reschedules at the request of the veteran. Processing time for an insufficient request will include the processing time of the original request.

In addition to a hard copy being produced, the option allows you to send a MailMan message either locally or via network mail. The mail bulletin will contain the same information that appears on the report.

Regional Office C&P Menu*Regional Office Reports Menu*

#### Print Exam Check List for RO

The Print Exam Check List for RO option is used to print a checklist used by regional office personnel to select compensation and pension examinations for veterans. The request worksheet lists the body systems and the exam worksheet names. It also contains a remarks section. The top portion of the work sheet allows the requestor to enter veteran-specific information, including

- Veteran's name, SSN, and C-Number
- VAMC where the exam is to be performed
- Veteran's day and night telephone numbers
- Power of Attorney
- Date the exam was ordered and by whom
- Insufficient exam date

Regional Office C&P Menu*Regional Office Reports Menu*

#### Insufficient Exam Report

The Insufficient Exam Report option prints a report of 2507 requests entered with a priority of Insufficient Exam for a specified date range. You may choose a detailed or summary version of the report. Only exam reasons and types that have information to report will be included on the detailed version of the report.

The summary version of the report is divided into two parts. The first portion contains the total number of 2507 requests/exams received for the date range, the total number of priority insufficient requests/exams for the date range, and the percentage of insufficient requests/exams received. Due to the rounding of the component percentages, the total of the percentages may not equal 100%. The second portion of this version is a breakdown of each reason an exam was returned.

The detailed version allows you to display one/many/all insufficient reasons and AMIE exams. Other information provided includes exam type, patient name, SSN, and claim number. Provider and exam date on this report are the provider and date from the originally completed 2507. The exam date will not be included if the original 2507 has been purged. The length of the veteran's name and the provider will be limited to 15 characters. If either field has been truncated, it will appear with two asterisks (\*\*). No matter what reasons and exams are selected, only exam reasons and types that have information to report will be included on the output.

If an insufficient 2507 is transferred from one site to another, that exam will be reported on the insufficient exam report for both sites (original and remote).

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

21-Day Certificate The 7132 issued to the regional office after a veteran has been hospitalized for a period of 21 days or more.
AMIE Automated Medical Information Exchange
AMIE Work Sheet A form used to aid the physician in the completion of a C&P exam. It provides instruction as to what medical information is required for a particular C&P examination.
Body System The systemic area of the human body to which a particular examination belongs. This is in accordance with the definition in the C&P Rating Specialist Guide at each regional office.
Bulletin An electronic mail message generated whenever certain conditions are met while executing application programs.
C&P Compensation and Pension
C&P Routing Location An entry in the AMIE Site Parameter file (#396.1) which points to the Hospital Location file (#44). Any locations entered are used to screen lab and radiology results for veterans when final C&P information is printed.
Diagnostic Code A number assigned to a specific diagnosis used in the Rating
Schedule.
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

Add an Exam to an Existing Request

Admission Inquiry By Date (All Admissions)

Admission Report for Service Connected Veterans

AMIS 290 for the Regional Office

Beneficiary Information Status Inquiry

Cancel C&P Requests/Exams

Detailed Inpatient Inquiry

Discharge Report

Edit 7131 Remarks

Edit C&P Request Information

Edit Patient Address Information

Enter a C&P Exam Request

Incompetent Veterans Report

Inquiry for C&P Requests

Insufficient Exam Report

MailMan Menu

Patient Profile MAS

Pending C&P Exams Report

Pending Form 7131 Requests Report

Print C&P Final Report (Manual)

Print Exam Check List for RO

Print New Notices of Discharge

Re-admission Report

Regional Office 21-day Certificate Printing

Regional Office Patient Inquiry

Report for Pension and A&A

Reprint a 21-day Certificate for the RO

Reprint a Notice of Discharge

Reprint C&P Final Report

Request for 7131 Information

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

GENITOURINARY EXAMINATION 0605 GENITOURINARY

GULF WAR GUIDELINES 1740 SPECIAL EXAMINATIONS

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